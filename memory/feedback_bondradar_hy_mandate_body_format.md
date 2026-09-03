---
name: bondradar-hy-mandate-body-format
description: "HY mandate bodies with Key Terms use a concise single-paragraph house-style summary, NOT the verbatim quote of the source announcement + roadshow logistics + investor-call links."
metadata: 
  node_type: memory
  type: feedback
  originSessionId: 173ac7d1-9e30-4326-a6c3-3fdb541b1e25
  modified: 2026-09-03T07:37:46.479Z
---

**HY mandate bodies with Key Terms follow a concise house-style template.** Do NOT copy the source's mandate announcement verbatim. Do NOT include roadshow logistics, investor-call meeting links, MiFID/PRIIPs boilerplate, or the company presenter list.

## Template

```
<Issuer> is planning a <CCY><size> <tenor> <note-type>. UOP <use of proceeds shorthand>. <call terms>, <CoC feature>. List <listing venue> [within N days/months if pending], denoms <denoms>. Law <governing law>. Sole Global Coordinator <name>. Joint Lead Managers <name>, <name>, <name>, <name>. Timing: <timing sentence>.
```

Fields in order:

1. **Issuer + planning verb + ccy+size + tenor + note-type** — `Hurtigruten Group AS is planning a EUR100m 5-year senior unsecured FRN.`
2. **UOP** — plain-English one-sentence: `UOP refinancing of the EUR100m Bridge Facility and general corporate purposes.`
3. **Call terms** — MWC period, callable-thereafter language: `MWC for 30 months, thereafter callable`
4. **CoC feature** — Change of Control put (e.g. `COC 101`)
5. **Listing** — venue + timeframe if pending: `List Oslo Stock Exchange within 9 months`
6. **Denoms** — `denoms 100k+100k`
7. **Law** — governing law: `Law Norwegian`
8. **Global Coordinator(s)** — `Sole Global Coordinator DNB Carnegie.` OR `Global Coordinators X, Y.`
9. **Joint Bookrunners / JLMs** — `Joint Lead Managers DNB Carnegie, Danske Bank, Nordea, SEB.`
10. **Timing** — `Timing: Roadshow commencing 4 September.` (or `Timing: Investor meetings commencing DD Month.`)

## Reference example (correct HY-mandate body)

```
Hurtigruten Group AS is planning a EUR100m 5-year senior unsecured FRN. UOP refinancing of the EUR100m Bridge Facility and general corporate purposes. MWC for 30 months, thereafter callable, COC 101. List Oslo Stock Exchange within 9 months, denoms 100k+100k. Law Norwegian. Sole Global Coordinator DNB Carnegie. Joint Lead Managers DNB Carnegie, Danske Bank, Nordea, SEB. Timing: Roadshow commencing 4 September.
```

## What NOT to include

- Verbatim quote of the source's opening paragraph.
- Roadshow logistics block: `- ROADSHOW AND TRANSACTION DOCUMENTS -` header, `Global Investor Call #1/#2` schedules, Teams/Zoom links, `Time: 11:00 CEST` details.
- Company presenter list (`Andreas Thorling, Group CEO...`).
- Investor Login Details / Deal Roadshow URLs / Entry Codes.
- MiFID / UK MiFIR product-governance language.
- PRIIPs KID boilerplate.
- Detailed Key-Terms sections copy-pasted from source (security description, guarantors list, incurrence tests, permitted debt/distributions details, general undertakings). Those live in the source term sheet and downstream 9fin coverage; the BR mandate message is a one-paragraph summary.

Flag it as a Fix when the BR body has any of the above content instead of the concise template.

**Why:** Finn on Accru Partners EUR550m 4-year Mandated (id 14650474): BR body dumped the full source verbatim including the mandate quote, roadshow logistics block with Teams links, MiFID/PRIIPs boilerplate. Finn pointed at the Hurtigruten mandate body (`Hurtigruten Group AS is planning a EUR100m 5-year senior unsecured FRN. UOP refinancing... Timing: Roadshow commencing 4 September.`) and said "this should be something like [that]".

**How to apply:** On any Mandated-stage HY finding, cross-check the BR body against the template. If it deviates (quotes, roadshow logistics, boilerplate), flag with a single Fix bullet:

- `• Rewrite the BR body to the HY-mandate house-style paragraph — one concise summary sentence covering issuer/size/tenor/type, UOP, call terms, CoC, listing, denoms, law, coordinators, JLMs, and timing. Drop the verbatim source quote, the roadshow logistics block with Investor Call links, and the MiFID/PRIIPs paragraph.`

Related: [[bondradar-mandate-quotes]] (bank-quoted direct-mandate wording IS intentional in `"..."` wrapping — but that's for the IG mandate-quote pattern, not HY. HY mandates use the concise-summary template above, not verbatim quotes).
