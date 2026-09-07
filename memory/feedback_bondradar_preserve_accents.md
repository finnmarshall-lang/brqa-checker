---
name: bondradar-preserve-accents
description: "Preserve accents / diacritics in the BR body. Never strip them. Flag when a source name/word with accents (`Société`, `Crédit`, `Länsförsäkringar`, etc.) appears in BR as the ASCII form."
metadata: 
  node_type: memory
  type: feedback
  originSessionId: 173ac7d1-9e30-4326-a6c3-3fdb541b1e25
  modified: 2026-09-07T08:39:59.768Z
---

BR body preserves accented characters exactly as they appear in the source. Do NOT ASCII-fold `Société` → `Societe`, `Crédit` → `Credit`, `Länsförsäkringar` → `Lansforsakringar`, `Compañía` → `Compania`, `Türkiye` → `Turkiye`, `Öffentliche` → `Offentliche`, `Autobahnen- und Schnellstraßen` → `Autobahnen- und Schnellstrassen`, etc.

**Correct:**
- `Société Générale Corporate & Investment Banking` — accents preserved.
- `Crédit Agricole CIB` — accent preserved.
- `Länsförsäkringar Hypotek AB (publ)` — umlauts preserved.

**Wrong (flag):**
- `Societe Generale Corporate & Investment Banking` — accents stripped.
- `Credit Agricole CIB` — accent stripped.
- `Lansforsakringar Hypotek AB (publ)` — umlauts stripped.

Applies to every field in the body: issuer name, guarantor name, bookrunner list, JLM ticker fields when the ticker uses accented characters, listing venue, law jurisdiction, UOP text, and anywhere else a source word originally carried a diacritic.

**Why:** Finn: "took accents out of message - just look out for accents in body of message, please flag them i.e Société - save to memory".

**How to apply:**

1. When walking the body, note every proper-name in the source that carries an accent / diacritic / umlaut / cedilla / tilde / eszett (ß) / etc.
2. Check the BR body carries the same accented form.
3. If BR has the ASCII fallback (`Societe` where source said `Société`), flag with a Fix bullet:
   `• Body <field> — "Societe Generale" → "Société Générale". BR preserves source accents; ASCII-folding is a defect.`

Applies to all BR body content. Does NOT apply to tranche form ticker fields (`bookOrRating=SG`, `banks.active`) — those are ticker shorthands and use their own ASCII conventions.

Related: [[bondradar-issuer-name-shortening]] (issuer-name variants — SCF/AG/N.V. dropping is fine; that's shortening, not accent-stripping. Two different rules.)
