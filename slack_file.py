#!/usr/bin/env python3
"""
Fetch the plain-text body of a Slack file attachment.

Bloomberg-forwarded term-sheets in #bond-deal-alerts are often HTML files
(text/html or multipart/related). slack_read_channel only shows the file
metadata (name + type + size), not the body — so the QA checker can't see
the source term sheet unless we fetch the file directly.

CLI:
    python3 slack_file.py <file_id>

    Prints the extracted text of the file. HTML is stripped to plain text.
    Anything else is dumped as UTF-8 (or replaced) verbatim.

Library:
    from slack_file import file_text
    body = file_text("F0BSAKZ5M88")  # str
"""

from __future__ import annotations

import html
import json
import os
import re
import sys
import urllib.parse
from pathlib import Path
from urllib import request, error

ENV_FILE = Path.home() / ".bondradar-env"
SLACK_API = "https://slack.com/api"


def _token() -> str:
    tok = os.environ.get("SLACK_BOT_TOKEN")
    if tok:
        return tok
    if not ENV_FILE.exists():
        raise RuntimeError(f"{ENV_FILE} not found and SLACK_BOT_TOKEN not in env")
    for line in ENV_FILE.read_text().splitlines():
        line = line.strip()
        if line.startswith("SLACK_BOT_TOKEN="):
            return line.split("=", 1)[1].strip()
    raise RuntimeError(f"SLACK_BOT_TOKEN not found in {ENV_FILE}")


def _call(method: str, params: dict) -> dict:
    url = f"{SLACK_API}/{method}?{urllib.parse.urlencode(params)}"
    req = request.Request(url, headers={"Authorization": f"Bearer {_token()}"})
    try:
        with request.urlopen(req, timeout=15) as resp:
            body = json.loads(resp.read().decode())
    except error.HTTPError as e:
        raise RuntimeError(f"Slack API {method} HTTP {e.code}: {e.read().decode()[:200]}")
    if not body.get("ok"):
        raise RuntimeError(f"Slack API {method} error: {body.get('error', 'unknown')}")
    return body


def _download(url_private: str) -> bytes:
    req = request.Request(url_private, headers={"Authorization": f"Bearer {_token()}"})
    try:
        with request.urlopen(req, timeout=30) as resp:
            return resp.read()
    except error.HTTPError as e:
        raise RuntimeError(f"file download HTTP {e.code}: {e.read()[:200]!r}")


_TAG = re.compile(r"<[^>]+>")
_WS = re.compile(r"[ \t]+")
_BLANK = re.compile(r"\n{3,}")


def _html_to_text(raw: bytes) -> str:
    # Bloomberg emails are usually latin-1 or utf-8; try utf-8 first.
    for enc in ("utf-8", "latin-1"):
        try:
            src = raw.decode(enc)
            break
        except UnicodeDecodeError:
            continue
    else:
        src = raw.decode("utf-8", errors="replace")

    # Kill script/style blocks wholesale.
    src = re.sub(r"<script[\s\S]*?</script>", "", src, flags=re.IGNORECASE)
    src = re.sub(r"<style[\s\S]*?</style>", "", src, flags=re.IGNORECASE)
    # Preserve line breaks: <br>, </p>, </div>, </tr>.
    src = re.sub(r"<br\s*/?>", "\n", src, flags=re.IGNORECASE)
    src = re.sub(r"</(p|div|tr|li|h[1-6])>", "\n", src, flags=re.IGNORECASE)
    src = re.sub(r"</td>", "\t", src, flags=re.IGNORECASE)
    # Strip remaining tags.
    text = _TAG.sub("", src)
    # Unescape entities.
    text = html.unescape(text)
    # Squash horizontal whitespace and collapse blank runs.
    text = _WS.sub(" ", text)
    text = _BLANK.sub("\n\n", text)
    return text.strip()


def file_text(file_id: str) -> str:
    """Return the extracted plain-text body of the Slack file.

    HTML files are stripped to text. Other text-typed files are decoded verbatim.
    Binary files raise RuntimeError — this helper is for text/email attachments.
    """
    info = _call("files.info", {"file": file_id})
    f = info.get("file") or {}
    mimetype = f.get("mimetype", "")
    url_private = f.get("url_private")
    if not url_private:
        raise RuntimeError(f"file {file_id} has no url_private (mimetype={mimetype})")

    raw = _download(url_private)

    if "html" in mimetype or f.get("filetype") in ("html", "htm"):
        return _html_to_text(raw)
    if mimetype.startswith("text/") or f.get("filetype") in ("text", "txt", "md"):
        return raw.decode("utf-8", errors="replace").strip()
    raise RuntimeError(f"file {file_id} is binary ({mimetype}); not supported")


def _cli(argv: list[str]) -> int:
    if len(argv) < 2:
        print("usage: slack_file.py <file_id>", file=sys.stderr)
        return 2
    try:
        print(file_text(argv[1]))
    except RuntimeError as e:
        print(f"error: {e}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(_cli(sys.argv))
