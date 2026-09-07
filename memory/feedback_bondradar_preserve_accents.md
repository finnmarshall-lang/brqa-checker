---
name: bondradar-preserve-accents
description: "BR body STRIPS accents / diacritics. Source names like `Société` / `Crédit` / `Länsförsäkringar` must be ASCII-folded in the BR body. Flag when accents remain."
metadata: 
  node_type: memory
  type: feedback
  originSessionId: 173ac7d1-9e30-4326-a6c3-3fdb541b1e25
  modified: 2026-09-07T08:46:58.207Z
---

**BR body does NOT preserve accents / diacritics — flag when they remain in the message.** Source names come with `é`, `ü`, `ö`, `ß`, `ñ`, `å`, `ç`, `ï`, etc.; the BR body carries the ASCII-folded equivalent. If a source proper-name still shows its diacritics in the outgoing message, that's a defect.

**Correct in BR body:**
- `Societe Generale Corporate & Investment Banking` — accents stripped.
- `Credit Agricole CIB` — accent stripped.
- `Lansforsakringar Hypotek AB (publ)` — umlauts stripped.
- `Turkiye` — dotted-I stripped.
- `Compania` — tilde stripped.
- `Offentliche Pfandbriefe` — umlaut stripped.
- `Autobahnen- und Schnellstrassen-Finanzierungs-Aktiengesellschaft` — ß stripped.

**Wrong (flag):**
- BR body has `Société Générale ...` when source has `Société` — flag as accents present.
- BR body has `Crédit Agricole ...` — flag.
- BR body has `Länsförsäkringar ...` — flag.

**Why:** Finn: "took accents out of message - just look out for accents in body of message, please flag them i.e Société - save to memory". Then clarified: "no its flag if they are in the message, they should be stripped". The desk deliberately ASCII-folds source names to avoid downstream Bloomberg/character-encoding issues.

**How to apply:**

1. **Do NOT run this check at the Mandated stage.** Mandate bodies are cleaned through the mandate cleaner (which handles the ASCII-fold automatically), so accents at Mandated aren't a defect the tick should flag. Finn: "for this rule you don't need to flag at mandates as they are cleaned through the mandate cleaner". Skip the accent check on any finding whose stage word is `Mandated`.
2. On any other stage (IPTs / Guidance / Revised guidance / Book Update / Spread set / Final terms / Launched / Allocations / Priced / Book stats / Priced tap), scan the body for any non-ASCII character in proper-names, listing venues, JLM lists, UOP prose.
3. If any are present, flag with a Fix bullet:
   `• Body — "Société Générale" → "Societe Generale". BR body strips diacritics; ASCII-fold the source name.`
4. Applies to every body field EXCEPT at Mandated: issuer, guarantor, bookrunner list, listing venue, law jurisdiction, UOP prose, anywhere source diacritics appear.
4. Common characters to fold:
   - `é/è/ê/ë` → `e`, `É/È/Ê/Ë` → `E`
   - `à/á/â/ä/å` → `a`, `À/Á/Â/Ä/Å` → `A`
   - `í/ì/î/ï` → `i`
   - `ó/ò/ô/ö/ø` → `o`, `Ö` → `O`
   - `ú/ù/û/ü` → `u`, `Ü` → `U`
   - `ñ` → `n`, `Ñ` → `N`
   - `ç` → `c`, `Ç` → `C`
   - `ß` → `ss`
   - `ý/ÿ` → `y`
   - `ř/š/č/ž/ě` → `r/s/c/z/e`

Related: [[bondradar-issuer-name-shortening]] (issuer-name variants — SCF/AG/N.V. dropping is a separate shortening rule).
