# Review package — theme:raisa-jp

<!-- BEGIN GENERATED VERDICT STAMP — do not hand-edit; regenerate with review/build_review.py -->
## Verdict stamp
- Theme: theme:raisa-jp — origin EN, population #128 [GOSIGN2-LEDGER (b) row 128]
- Overall: PASS — NOT PASS at the ledger determination (section (e) register); its one OPEN item re-judged DISPOSITIONED with grounds by the FIX5 wave; go-sign issued 2026-11-17 (COMPLETION-REPORT §10) [GOSIGN2-LEDGER (b); GOSIGN2-LEDGER-SUPPLEMENT (d)]
- T1 (source check): FINDINGS (classified) — baseline 2026-11-16: exit 1, 2 errors / 0 warns / 2 infos (hotlink×1, pseudo-ref×1); standing classes dispositioned in register c1 [T1-ROWS row 153; GOSIGN2-LEDGER (b) row 128]
- T2/T3 (render, combined verdict): FINDINGS — [combined T2/T3] report `FINDINGS` — page-overflow 328px@320 + 380px@375 + runtime-hotlink site-theme chain; sample T2 no machine verdict (exit 2); T3 RAISA ring logo overprints header wordmark/account links at 375/320 (both engines); broken black-highlighter-logo.svg (deferred). [RENDER-ROWS-2 (RENDER-S2-C (EN17))]
- Engine coverage: full matrix as run by the lane; coverage not separately caveated in the row (the row records inconclusive runs, carried verbatim above) [RENDER-ROWS-2 row]
- Credit modal: no credit-modal line recorded [RENDER-ROWS-2 (RENDER-S2-C (EN17))]
- T4 (localize patterns + follow-up): FINDINGS — display-affecting findings: 3 [LOCALIZE-ROWS row 128, source LOCALIZE-S2-C]
- T5 (translation text): FINDINGS — the source reports judge T4/T5 jointly; one verdict word covers both [LOCALIZE-ROWS row 128]
- FIX5 re-judgement: item 24 (class F) DISPOSITIONED — FIX5-FUNC §6 (no edit): @media (max-width: 768px) block byte-identical to original (diff IDENTICAL); logo markup and sizing unchanged; KB-35 family [GOSIGN2-LEDGER-SUPPLEMENT (a) item 24]
- Computed against: canonical commit 1869877ffdcd33cb214b8dc421fb39e3de8d7e8d; candidate file pages/theme:raisa-jp.txt sha256:d23f2de3def5c170caee9b6a65a491d8dd633b5e20a53b190ba5eb839db0a2fc; record: GOSIGN2-LEDGER.md + GOSIGN2-LEDGER-SUPPLEMENT.md as of the FIX5 head 435a6bb
<!-- END GENERATED VERDICT STAMP -->

## Status

| | |
|---|---|
| Verdict | **PASS** — go-sign re-run (this theme is one of the 286 of 286 pass-eligible themes) |
| Blocking items at ledger time | GOSIGN2-LEDGER.md §(e) item 24 [F] — header interference (the RAISA ring logo overprints the header wordmark and account links at 375/320), the theme's only OPEN item |
| Re-judgment | GOSIGN2-LEDGER-SUPPLEMENT.md item 24: **DISPOSITIONED** (FIX5-FUNC §6, no edit), on the byte-identity ground argued in the per-theme record below |
| Standing items | **DISPOSITIONED** — localize row: P5 logo hotlink (class (ii) / KB-58); render row: page-overflow figures and the runtime-hotlink site-theme chain (environment layer, KB-40), sample T2 no machine verdict (coverage caveat), broken black-highlighter-logo.svg (KB-58 deferred). One further item is recorded with a flag rather than a disposition: the P11 body link (section 7), which the source report marks not display-affecting and whose §(e) charge pointer does not resolve |
| Go-sign basis | COMPLETION-REPORT.md §10 (go-sign issued; 81 FIXED / 26 DISPOSITIONED / 0 OPEN across the sweep) |
| Named exception | None for this theme (the sweep's single named exception is theme:amethyst-v2, which has no candidate) |

## Provenance

| | Original | Candidate |
|---|---|---|
| Page | theme:raisa | theme:raisa-jp |
| Wiki | scp-wiki.wikidot.com | SCP-JP Sigma-10 candidate (canonical repo) |
| Reference revision | 56, as recorded in the candidate's credit block (初訳時参照リビジョン: 56, candidate L38) and in review/sources.tsv | — |
| Source of this copy | Campaign cache `gosign2-lanes/lane-oc-gs-localize-s2-C/orig-raisa.txt`, via the mirror store (`review-mirrors/orig-raisa-rev56.txt`, class COPY; fetched once by the LOCALIZE-S2-C lane) | Canonical file `pages/theme:raisa-jp.txt`, copied at worktree HEAD 939d257; the file's last content change is commit 1869877f (FIX-CREDIT-D, translator attribution normalization), the stamp's computed-against commit |
| Lines / bytes | 678 lines / 24,363 bytes (the last line carries no trailing newline) | 688 lines / 26,428 bytes (the last line carries no trailing newline) |
| SHA-256 | 2bf8a29358cc7a29359177bfd65a0c7e893bac84803b54f8366f39966bd935e9 | d23f2de3def5c170caee9b6a65a491d8dd633b5e20a53b190ba5eb839db0a2fc |

Package files: `original.txt` and `candidate.txt` as tabled above; `classification.json` and the skeleton behind this README are from classify_hunks.py 0.1.0, signature table 2026-11-17.1, patterns commit 9c5e9079afb01d30cb9fc4ef9d714e5591eb2ffa.

## Summary

RAISA is a Black Highlighter based theme, and the port keeps its topology exactly: a module-css header frame, the usage body, one large code exhibit carrying the theme's own CSS, and a self-delivery tail. Nothing is relocated (the classifier's topology pass matches every component by kind across the two sides). What changes is the frame and the language: BHL delivery moves to the JP distribution (scp-jp.github.io) with the three-layer interwiki-style stack, the bare Rate module is swapped for the preview credit block, the font imports move from fonts.bunny.net to Google Fonts and gain Noto Sans JP, and the usage body and the CSS comments are translated in full. The measured churn (diff.md: +190/−186 in 13 hunks by the generator's count; the classifier's own alignment counts 116 change blocks, −149/+159, of which 93 sit in the translation section) is a translation with a frame swap, not a redesign. The theme's only blocking item was never a code defect: a render finding that the ring logo overprints the header at phone widths, dispositioned because every surface that could cause it is byte-identical to the original, as the per-theme record below re-derives from this package's own two files.

## 0. Header / provenance

- Delivery: no relocation detected between the sides; each side's components match by kind.

- **Provenance route:** derived from the branch original at the reference revision (theme:raisa rev 56 on scp-wiki). This is not an R4 production adoption: no production JP counterpart exists in the record for this theme, and the candidate's body is the S2 localization of the EN original. The evidence is threefold and mutually consistent: review/sources.tsv keys the row `standard` with the mirror sourced from the LOCALIZE-S2-C lane's rev-56 cache (class COPY); the candidate's credit block records 初訳時参照リビジョン: 56 (candidate L38); and the T4 follow-up diff (diff --from 56) shows no change, with the original's current revision still 56 (LOCALIZE-S2-C, EN17-4), so the mirror in this package is also the current original, not a superseded revision.


## Class summary

| Label | Blocks |
|---|---|
| ASSET-REHOST | 1 |
| BARE-RATE-DEL | 1 |
| COMMENT-TEXT | 52 |
| COMPONENT-SWAP | 1 |
| CONTENT-STRING | 1 |
| CREDIT-PREVIEW | 1 |
| CREDIT-PROSE | 1 |
| CSS-BODY | 2 |
| DELIVERY-HOST | 4 |
| DRAFT-HOST | 2 |
| EXHIBIT-RESTRUCTURE | 4 |
| FONT-IMPORT | 1 |
| HEADERVAR | 1 |
| IFTAGS | 1 |
| INCLUDE-REPOINT | 5 |
| JPFONT-LOAD | 1 |
| LINK-REPOINT | 1 |
| SELF-DELIVERY | 2 |
| TASL-FIELDS | 1 |
| TRANS-UNANCHORED | 74 |
| TRANSLATION-ANCHORED | 22 |

Counts: 116 blocks, 35 specific, 74 heuristic, 7 residue, 0 skipped (comment text).

## 1. Credit and attribution

- CREDIT-PREVIEW (A): Credit block swap (P3/T1): the JP environment's preview credit module is the rate-bearing form; the branch-original credit module does not render here.
  Verify: Re-run the T1 checker (check_source.py); the credit includes must resolve on scp-jp.
  - B7: orig 31-33 -> cand 31-40 (body -> body)

- **What (this theme):** B7 (original L31–33 → candidate L31–40) is the whole credit change. The original's right-aligned bare `[[module Rate]]` is deleted, and the `:scp-jp:credit:start-preview` block takes its place at the same position, carrying the eight ruling-3 fields (candidate L32–39): title RAISAテーマ, translator AI, translation year 2026, original title RAISA Theme, copyright holder Rounderhouse, creation year 2019, reference revision 56, and the source link to the EN page. The preview module is rate-bearing, so the rating widget survives the swap and no duplicate bare Rate stands beside it (KB-09 state: clean; the localize lane verified by grep that no live `[[module Rate]]` remains).
- **T7 credit CSS:** no supplement block was added, and no in-place (R6) correction was made: the theme's own code exhibit already carries BHL's credit-button rules (`div.rate-box-with-credit-button …`, candidate L584–597 and following), inherited byte-identical from the original — no change block covers them. KB-11's missing-supplement shape does not arise: that pattern charges a candidate that lacks credit CSS its production counterpart carries; here the credit furniture is the base BHL set inside the theme's own CSS on both sides of the diff.
- **License box (T4):** none, on either side. Neither file includes a license-box component; the `#license-area` rules inside the code exhibit are BHL variables, not a license box. Recorded as absent with that ground.
- **Record note:** the localize-era report records the translator field as `SCP-JP`; the current file reads `AI`, ruling 3's campaign-translator form, and the file's last content change (commit 1869877f, FIX-CREDIT-D, translator attribution normalization over 163 candidates) is exactly that normalization. The candidate is 4 bytes smaller than the localize-era measurement (26,432 → 26,428 B), consistent with the single field's change. This README follows the bytes.
- **Disposition:** Standing (the swap itself). The format deviation the localize lane noted (the holder and translator names as plain text, not `[[*user]]` links) sits in its T5 list as minor and was never charged in §(e).


## 2. Includes and components

- IFTAGS (A): Tag localization (P2/T2, KB-08): iftags conditions use JP tag names in the JP environment.
  Verify: KB-08 recipe: every iftags condition names JP tags; a bare [[iftags]] line is an anomaly.
  - B1: orig 1-1 -> cand 1-1 (body -> body)

- COMPONENT-SWAP (B): Component swap to a JP port (T8, ruling 4): the campaign component candidate replaces the branch component it ports.
  Verify: The swapped target is in the campaign component inventory and exists on the check wiki.
  - B14: orig 81-82 -> cand 88-89 (body -> body)

- **What (this theme):** the include census is original 6 → candidate 8. The three interwiki-style frame includes are repointed `:scp-wiki:` → `:scp-jp:` (head priorities 1–2 at L21/26; tail priority 3 at L685), the theme-squares exhibit include likewise (original L45 → candidate L52), and the credit pair is added (L31/40). The two usage-example includes (B14, original L81–82 → candidate L88–89) drop the site prefix entirely and name the JP candidate pages in bare posting form (`theme:black-highlighter-theme-jp`, `theme:raisa-jp`): inside an `@@…@@` exhibit on the JP wiki, the bare form is the form that resolves. No include in the candidate points at a `:scp-wiki:` page (grep-verifiable).
- **Frame layout:** the priority-3 include sits outside the `[[/iftags]]` gate (gate closes candidate L680; frame at L682–688), exactly the original's layout (gate closes original L670; frame at L672–678). The gate itself opens at L1 on both sides (B1: `+theme` → `+テーマ`; KB-08 state clean, no bare or unconditional iftags anomaly).
- **Judgment:** the exhibit's BHL target choice (the `-jp` candidate page, where the unsuffixed `theme:black-highlighter-theme` already exists on scp-jp) was flagged by the localize lane as a staff-confirmation item for posting time. It is recorded in section 11 as an observation, not a defect: the include names the campaign's own BHL port, which is this theme's base, and the mechanics resolve.
- **Disposition:** Standing; no foreign include is kept, so no KB-15/KB-54 exception is needed.


## 3. Delivery and code loading

- DELIVERY-HOST (A): Base/host repoint (P4/T9): deliveries are served from the JP hosts in this environment.
  Verify: Resolve the new host path; a kept old-host line is a class (ii) posting matter, recorded in section 11.
  - B4: orig 23-23 -> cand 23-23 (body -> body)
  - B6: orig 28-28 -> cand 28-28 (body -> body)
  - B114: orig 673-673 -> cand 683-683 (module-css -> module-css)
  - B116: orig 677-677 -> cand 687-687 (body -> body)

- **What (this theme):** the delivery topology does not change (no relocation; the topology pass matches module-css / code-css / module-css components by kind on both sides). The BHL normalize and base move to the JP distribution in both of their channels: the module-css `@import` lines (B2, original L3–4 → candidate L3–4, cdn.scpwiki.com → scp-jp.github.io) and the priority-1/2 interwiki-style theme arguments (B4/B6, nu-scptheme.github.io → scp-jp.github.io). The classifier filed B2 under section 8 as CSS-BODY because the line sits in the module-css channel; by mechanism it is this section's change, and it is argued here.
- **Priority stack:** 1 normalize / 2 BHL base / 3 own code, with only the `priority` and `theme` arguments surviving (KB-07 state: clean — no duplicate priority, no dropped-parameter finding in the T1 baseline).
- **Own-code channel (B114/B116):** the closing `[[module css]]` @import (candidate L683) and the priority-3 theme argument (candidate L687) point at the candidate's own local--code on the draft host (`sigma10-jp-test.wdfiles.com/local--code/theme%3Araisa-jp/1`). That is the class (iii) draft form, sanctioned at draft stage and rewritten to the production host at posting. One carried quirk: the @import line has no trailing semicolon, byte-identical to the original's (original L673); the CSS parser tolerates it in both, and the port preserves it under the closing rule rather than silently repairing it.
- **Disposition:** DISPOSITIONED for the two draft-host lines (class (iii)); the host repoints stand as applied.


## 4. Fonts and assets

- ASSET-REHOST (A): Asset re-hosted to JP storage (P5, KB-17): assets are served from the allowlisted JP hosts in this environment.
  Verify: KB-17 host list; the re-hosted URL serves.
  - B8: orig 36-36 -> cand 43-43 (body -> body)

- JPFONT-LOAD (A): JP font load added (P7/T5, KB-16): Japanese text needs a JP typeface loaded, and the resolved base may not load one.
  Verify: KB-16 recipe with base subtraction: the resolved base does not already load the family.
  - B54: orig 194-195 -> cand 201-203 (code-css -> code-css)

- **What (this theme):** two font changes and one asset change. B54 (original L194–195 → candidate L201–203): the two `fonts.bunny.net` @imports are replaced by three `fonts.googleapis.com` @imports carrying the same Latin families (Lato, PT Mono, Poppins, Share Tech Mono, Oxanium) plus a new Noto Sans JP load (400;700). B61 (original L214–218 → candidate L222–226): `'Noto Sans JP'` is inserted into all four font stacks (`--body-font`, `--header-font`, `--title-font`, `--mono-font`), and the body/title generic fallback changes from `cursive` to `sans-serif` with it; the classifier filed B61 under section 8 as CSS-BODY by channel, and it is argued here by mechanism. B8 (original L36 → candidate L43): the BHL logo image in the header exhibit is re-hosted from scp-wiki.wdfiles.com to scp-jp.wdfiles.com (P5 / KB-17).
- **Why:** fonts.bunny.net is not on the P5 allowlist (storage, Google Fonts, BootstrapCDN, cdnjs), so the original's import host could not be followed; Google Fonts is the allowlisted route, and KB-16's base-subtraction check is what makes the JP load a real supplement rather than a duplicate (the resolved BHL base loads no JP face). The stack insertions are the load's other half: a loaded face no stack names would change nothing.
- **The one asset not re-hosted:** the RAISA logo exhibit image (candidate L71) still loads from scp-wiki.wdfiles.com. That is the P5 item, DISPOSITIONED class (ii) / KB-58 in section 11; it is also the T1 baseline's hotlink×1.
- **Disposition:** the font changes and the BHL-logo re-host stand as applied; the RAISA logo host is DISPOSITIONED (section 11).


## 5. Header, sidebar, site furniture

- HEADERVAR (A): Header/title variables (P9/T6, KB-57): the header text variables are the theme's visible title surface.
  Verify: KB-57: where the value stays in the original's language, the disposition is ruling 2 (section 11).
  - B60: orig 211-212 -> cand 219-220 (code-css -> code-css)

- **What (this theme):** B60 (original L211–212 → candidate L219–220) is the only header-variable change: `--header-title` "RAISA ARCHIVE" → "RAISAアーカイブ" and `--header-subtitle` "Records And Information Security Administration" → "記録・情報保安管理局" (the administration's JP name form). `--logo-image` is not changed at all: the line is byte-identical (original L210 = candidate L218; the per-theme record gives the measurement). Sidebar and topbar: neither file carries sidebar/top-bar markup (the localize lane's pattern 8 is N-A at source level; the layout is inherited from the BHL base), so there is nothing theme-side to adapt. The narrow-width header rules the theme does own are its two @media blocks, and both are byte-identical (the 765px block, original L12–18 = candidate L12–18; the 768px block is measured in the per-theme record).
- **Why:** the P9/T6 variables are the theme's visible title surface. Ruling 2 would have allowed keeping the EN strings as a disposition (the KB-57 route other themes took); this theme translated them instead, so no header-language disposition is needed.
- **Disposition:** Standing.


## 6. Text translation

- TRANSLATION-ANCHORED (B): Prose/usage translation (P10, KB-18): reader-visible text localizes; anchored pairs are one-to-one translations.
  Verify: Read the pairs; the anchors (leading token, CSS property, selector, heading level) confirm the pairing.
  - B9: orig 42-42 -> cand 49-49 (body -> body)
  - B12: orig 70-70 -> cand 77-77 (body -> body)
  - B18: orig 93-94 -> cand 100-101 (body -> body)
  - B19: orig 96-96 -> cand 103-103 (body -> body)
  - B20: orig 98-98 -> cand 105-105 (body -> body)
  - B21: orig 100-100 -> cand 107-107 (body -> body)
  - B22: orig 102-102 -> cand 109-109 (body -> body)
  - B23: orig 104-104 -> cand 111-111 (body -> body)
  - B24: orig 110-111 -> cand 117-118 (body -> body)
  - B25: orig 113-114 -> cand 120-121 (body -> body)
  - B27: orig 118-119 -> cand 125-126 (body -> body)
  - B39: orig 143-143 -> cand 150-150 (body -> body)
  - B40: orig 145-145 -> cand 152-152 (body -> body)
  - B41: orig 147-147 -> cand 154-154 (body -> body)
  - B42: orig 149-149 -> cand 156-156 (body -> body)
  - B43: orig 151-151 -> cand 158-158 (body -> body)
  - B44: orig 153-154 -> cand 160-161 (body -> body)
  - B49: orig 167-169 -> cand 174-176 (body -> body)
  - B50: orig 174-176 -> cand 181-183 (body -> body)
  - B51: orig 182-182 -> cand 189-189 (body -> body)

- TRANS-UNANCHORED (C): Translation-shaped change without anchors (P10, KB-18): restructured lines are the queue where restorations and exhibit changes hide.
  Verify: Writer confirmation against the mirror, line by line.
  - B11: orig 66-66 -> cand 73-73 (body -> body)
  - B13: orig 78-78 -> cand 85-85 (body -> body)
  - B16: orig 87-87 -> cand 94-94 (body -> body)
  - B17: orig 91-91 -> cand 98-98 (body -> body)
  - B26: orig 116-116 -> cand 123-123 (body -> body)
  - B28: orig 121-121 -> cand 128-128 (body -> body)
  - B29: orig 123-123 -> cand 130-130 (body -> body)
  - B30: orig 125-125 -> cand 132-132 (body -> body)
  - B31: orig 127-127 -> cand 134-134 (body -> body)
  - B32: orig 129-129 -> cand 136-136 (body -> body)
  - B33: orig 131-131 -> cand 138-138 (body -> body)
  - B34: orig 133-133 -> cand 140-140 (body -> body)
  - B35: orig 135-135 -> cand 142-142 (body -> body)
  - B36: orig 137-137 -> cand 144-144 (body -> body)
  - B37: orig 139-139 -> cand 146-146 (body -> body)
  - B38: orig 141-141 -> cand 148-148 (body -> body)
  - B45: orig 158-158 -> cand 165-165 (body -> body)
  - B46: orig 160-160 -> cand 167-167 (body -> body)
  - B47: orig 162-162 -> cand 169-169 (body -> body)
  - B48: orig 164-165 -> cand 171-172 (body -> body)
  - B52: orig 185-189 -> cand 192-196 (code-css -> code-css)
  - B53: orig 192-192 -> cand 199-199 (code-css -> code-css)
  - B55: orig 197-197 -> cand 205-205 (code-css -> code-css)
  - B56: orig 200-201 -> cand 208-209 (code-css -> code-css)
  - B57: orig 203-203 -> cand 211-211 (code-css -> code-css)
  - B59: orig 209-209 -> cand 217-217 (code-css -> code-css)
  - B64: orig 225-225 -> cand 233-233 (code-css -> code-css)
  - B65: orig 227-227 -> cand 235-235 (code-css -> code-css)
  - B67: orig 231-231 -> cand 239-239 (code-css -> code-css)
  - B69: orig 235-235 -> cand 243-243 (code-css -> code-css)
  - B70: orig 237-237 -> cand 245-245 (code-css -> code-css)
  - B71: orig 239-239 -> cand 247-247 (code-css -> code-css)
  - B72: orig 241-241 -> cand 249-249 (code-css -> code-css)
  - B73: orig 243-243 -> cand 251-251 (code-css -> code-css)
  - B74: orig 245-245 -> cand 253-253 (code-css -> code-css)
  - B75: orig 247-247 -> cand 255-255 (code-css -> code-css)
  - B76: orig 251-251 -> cand 259-259 (code-css -> code-css)
  - B77: orig 256-256 -> cand 264-264 (code-css -> code-css)
  - B78: orig 267-267 -> cand 275-275 (code-css -> code-css)
  - B79: orig 271-272 -> cand 279-280 (code-css -> code-css)
  - B80: orig 274-274 -> cand 282-282 (code-css -> code-css)
  - B81: orig 279-279 -> cand 287-287 (code-css -> code-css)
  - B82: orig 283-283 -> cand 291-291 (code-css -> code-css)
  - B83: orig 313-313 -> cand 321-321 (code-css -> code-css)
  - B85: orig 323-323 -> cand 331-331 (code-css -> code-css)
  - B86: orig 326-326 -> cand 334-334 (code-css -> code-css)
  - B87: orig 328-329 -> cand 336-337 (code-css -> code-css)
  - B88: orig 331-331 -> cand 339-339 (code-css -> code-css)
  - B89: orig 334-334 -> cand 342-342 (code-css -> code-css)
  - B90: orig 341-343 -> cand 349-351 (code-css -> code-css)
  - B91: orig 347-347 -> cand 355-355 (code-css -> code-css)
  - B92: orig 353-353 -> cand 361-361 (code-css -> code-css)
  - B93: orig 363-363 -> cand 371-371 (code-css -> code-css)
  - B94: orig 365-365 -> cand 373-373 (code-css -> code-css)
  - B95: orig 374-374 -> cand 382-382 (code-css -> code-css)
  - B96: orig 376-376 -> cand 384-384 (code-css -> code-css)
  - B97: orig 381-382 -> cand 389-390 (code-css -> code-css)
  - B98: orig 386-386 -> cand 394-394 (code-css -> code-css)
  - B99: orig 390-390 -> cand 398-398 (code-css -> code-css)
  - B100: orig 394-394 -> cand 402-402 (code-css -> code-css)
  - B101: orig 403-403 -> cand 411-411 (code-css -> code-css)
  - B102: orig 413-415 -> cand 421-423 (code-css -> code-css)
  - B103: orig 419-419 -> cand 427-427 (code-css -> code-css)
  - B104: orig 422-422 -> cand 430-430 (code-css -> code-css)
  - B105: orig 429-429 -> cand 437-437 (code-css -> code-css)
  - B106: orig 434-434 -> cand 442-442 (code-css -> code-css)
  - B108: orig 443-443 -> cand 451-451 (code-css -> code-css)
  - B109: orig 448-448 -> cand 456-456 (code-css -> code-css)
  - B110: orig 459-459 -> cand 467-467 (code-css -> code-css)
  - B111: orig 466-466 -> cand 474-474 (code-css -> code-css)
  - B112: orig 472-472 -> cand 480-480 (code-css -> code-css)
  - B113: orig at 670 -> cand 678-679 (body -> body)

- CONTENT-STRING (B): Visible string in CSS (KB-18, R1 reader-visible half): content: strings and string-valued variables render for readers.
  Verify: The string renders in the sample page's DOM text.
  - B58: orig 205-207 -> cand 213-215 (code-css -> code-css)

- **What (this theme):** 93 of the classifier's 116 blocks sit in this section, in three strata. (a) Anchored prose translation (22 blocks, tier B): headings, collapsible and tab labels, the table and font specimens — one-to-one pairs a reviewer can check line by line in diff.md. (b) Unanchored prose translation (the body-channel heuristic blocks, each resolved in the appendix): the syntax-guide prose of the usage body (original L66–176 → candidate L73–183). (c) In-CSS text (residue class R1): the code exhibit's comments and string values, 52 COMMENT-TEXT-labeled blocks including the banner comment (B52); its reader-visible half is B58, `--theme-name` "RAISA Theme" → "RAISAテーマ" with its instruction comments — a string-valued variable, the sub-shape the KB-18 amendment (patterns commit 9c5e907) names. Every heuristic and residue block in this section is resolved individually in the appendix.
- **Kept deliberately:** the coined colour names (Madras, Chenin, Pacifika, Anzak) stand verbatim as proper nouns, and the specimen's Lorem Ipsum stands. One slang localization is the porter's choice and is recorded by the localize lane: EN "weed lmao" (original L154) → 草 (candidate L161). No glyph-form (R5) conversions occur: the original is an EN theme and retains no CN strings to convert.
- **Why:** P10 is the port's purpose; the failure it prevents is a JP page whose instructions, labels, and specimens still read as the EN original. The R1 stratum is separated from reader-visible text because the two carry different weights: comments are porter-visible only (a completeness matter, recorded in the taxonomy's feedback as a known non-finding), while string-valued variables render.
- **Disposition:** Standing (the port itself).


## 7. Links

The skeleton reports no primary signature for this section; the section is not empty. Two link changes and one standing item sit here.

- **What:** (a) B12 (original L70 → candidate L77): the usage note's BHL link. The original's same-site form `[[[theme:black-highlighter-theme|…]]]` became an absolute EN URL in the candidate, `[[[https://scp-wiki.wikidot.com/theme:black-highlighter-theme|詳細はこちら]]]`. (b) The usage-example includes (B14, section 2) are the port's other reader-facing link surface and were repointed to the JP candidate pages. (c) The credit block's source link (candidate L39) points back to the original page, as the TASL record requires.
- **Why:** P11 exists because a link that leaves the JP wiki, or dies on it, fails the reader at click time. Item (a) does neither in the blocking sense: the EN BHL page exists and serves, and the link is a "learn more" pointer inside a usage note, not a dependency of the theme. The localize lane charged it MISSED under pattern 11 and marked it **not display-affecting** in its verdict line (REPORT-GOSIGN2-LOCALIZE-S2-C, EN17-4).
- **Verify:** Read candidate L77 against original L70; the target is the EN theme page the note describes.
- **Disposition:** Standing, with a record flag. The ledger's localize row (GOSIGN2-LEDGER.md §(c3)) writes "P11 → (e) H", but the §(e) register contains no H item for this theme and the supplement re-judges none: the pointer does not resolve. The item is recorded here so it is not silently passed over, at the weight the source report itself gives it (not display-affecting, no §(e) charge, no fix wave). If a future editor repoints it to theme:black-highlighter-theme-jp, that is a one-line editorial change, not a migration correction this record demands.

## 8. Structure

- CSS-BODY (C): Unclassified CSS content change: CSS churn with no mechanism signature; kept visible and counted rather than silently passed.
  Verify: Writer review; a recurring shape is a new-signature candidate for the patterns loop.
  - B2: orig 3-4 -> cand 3-4 (module-css -> module-css)
  - B61: orig 214-218 -> cand 222-226 (code-css -> code-css)

- EXHIBIT-RESTRUCTURE (C): Usage/sample exhibits dropped or replaced (R3): a sanctioned replacement and a silent deletion have the same diff shape; the ground must be stated.
  Verify: The exhibit-decision slot for this block, argued from the mirror.
  - B3: orig 21-21 -> cand 21-21 (body -> body)
  - B5: orig 26-26 -> cand 26-26 (body -> body)
  - B10: orig 45-45 -> cand 52-52 (body -> body)
  - B115: orig 675-675 -> cand 685-685 (body -> body)

- **What (this theme):** structure is preserved, per localize.md's closing rule: the same component topology on both sides (module-css frame L1–19; body; code exhibit `[[code]]` original L183–668 → candidate L190–676 inside its collapsible; self-delivery tail), the same variable names and selectors, and substitutions made inline (hosts, stacks, strings) rather than appended. Two classifier placements are corrected here rather than silently inherited: B2 is a delivery change argued in section 3, and B61 is the font-stack supplement argued in section 4; both were filed in this section as CSS-BODY by channel, not by mechanism. One malformed line is carried verbatim on purpose: `[[div_ style=""filter: display:flex;"]]` (original L35 → candidate L42) — malformed in the original, inert in both versions, and preserved because the port does not silently repair the original's markup (the localize lane records the same observation).
- **Disposition:** Standing.


- **Exhibit decision:** of the four EXHIBIT-RESTRUCTURE-labeled blocks, none drops or replaces an exhibit. B3, B5, and B115 are the interwiki-style frame includes (head priorities 1–2, tail priority 3), repointed `:scp-wiki:` → `:scp-jp:` (sections 2–3); the label fired on the include shape, not on any exhibit handling. B10 is the theme-squares exhibit include (original L45 → candidate L52), repointed the same way, the exhibit itself intact. The exhibit census is unchanged across the port: theme-squares, the tabview specimens, and the blockquote/table/font specimens are all present and translated, so no R3 ground is needed — nothing was dropped, and nothing was silently replaced. The bare-Rate reasoning sits in section 1 (B7): the original's bare `[[module Rate]]` was removed because the preview credit module that replaced it is rate-bearing; keeping both would have rendered two rating widgets (the KB-09 shape).


## 9. Formatting only

- WS-ONLY blocks: 0
- Re-indentation: 0 blocks pair up after leading-whitespace normalization

None — there is no formatting-only change in this port: no whitespace-only block, no re-indentation, so the R7 disclosure duty is not triggered and a follow-up diff against either file applies cleanly. The candidate's +10 net lines are content, accounted for in sections 1, 4, and 10.

## 10. Porter annotations

The skeleton reports no signature for this section; there is exactly one porter-side addition to record.

- **What:** the font-credit line at candidate L678 — `**フォント:** 使用している欧文・和文書体はいずれもGoogle Fontsで配信されるオープンライセンスの書体です（SIL Open Font License など）。日本語文字はNoto Sans JPにフォールバックします。` — inserted between `[[/collapsible]]` (candidate L677) and `[[/iftags]]` (candidate L680), where the original passes directly from one to the other (original L669–670). It has no original counterpart; the classifier counted it as B113, an unanchored translation-shaped block, and the appendix resolves it here.
- **Why:** P7's credit half: a font the port adds must be credited, and the line also tells JP readers which face renders their text. It is R2-shaped (an addition, not a translation), but it is not a translator's note about the text; it belongs to the deliverable's attribution surface, like the credit block.
- **Verify:** Read candidate L676–680 against original L668–670. It is the only added prose line outside the credit block and the translated body; the net line growth of the whole port (+10) is accounted for by the credit block (+7), this line and its blank separator (+2), and the third font @import line (+1).
- **Disposition:** Standing.

## 11. Dispositions and exceptions

- HTTP-KEPT: 1 occurrence(s), e.g. --logo-image: url("data:image/svg+xml,%3C%3Fxml version='1.0' encoding='utf-8'%3F%3E%3Csvg xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink' id='RAISA_Logo' x='0' y='0' baseProfile='tiny' overflow='visible' version='1.2' viewBox='0 0 2318.9 2200' xml:space='preserve'%3E%3Cpath id='Outer_Ring' fill='%23E3E2D6' d='M2141.9 1272.1c5-40.5 7.5-81.3 7.5-122.1 0-410-249.3-761.8-604.6-912.2L1486.4 60h-654L774 237.8C418.7 388.2 169.4 740 169.4 1150c0 40.8 2.5 81.6 7.5 122.1L52 1411.8l327 566.4 183.5-38.4c166 125.7 372.8 200.2 597 200.2s431-74.5 597-200.2l183.5 38.4 327-566.4-125.1-139.7zm-242.8 616.7-164.2-34.4c-156.7 128.5-357.1 205.6-575.5 205.6-218.4 0-418.8-77.1-575.5-205.6l-164.2 34.4-270-467.7L262 1295.8c-7.6-47.5-11.6-96.1-11.6-145.8 0-389 243.9-721.1 586.9-851.2L889.4 140h540l52.1 158.8C1824.6 429 2068.4 761 2068.4 1150c0 49.6-4 98.3-11.6 145.8l112.3 125.4-270 467.6z'/%3E%3Cpath id='Outer_Dark_Ring' d='M2068.4 1150c0-389.1-243.9-721.1-586.9-851.2L1429.4 140h-540l-52.1 158.8C494.3 428.9 250.4 761 250.4 1150c0 49.6 4 98.3 11.6 145.8l-112.3 125.4 270 467.7 164.2-34.4C740.7 1982.9 941 2060 1159.4 2060c218.4 0 418.8-77.1 575.5-205.6l164.2 34.4 270-467.7-112.3-125.4c7.6-47.4 11.6-96.1 11.6-145.7zm-284.6 406.6-82.4-47.6c-116.4 175.3-315.7 290.9-541.9 290.9S734 1684.3 617.6 1509l-82.4 47.6-40-69.3 82.4-47.5c-43.5-87.3-68-185.7-68-289.8 0-345.6 269.6-628.1 610-648.8V406h80v95.2c340.4 20.7 610 303.2 610 648.8 0 104.1-24.5 202.6-68 289.8l82.4 47.5-40.2 69.3z'/%3E%3Cpath id='Inner_Ring' fill='%23E3E2D6' d='M1741.4 1439.8c43.5-87.3 68-185.7 68-289.8 0-345.6-269.6-628.1-610-648.8V406h-80v95.2c-340.4 20.7-610 303.2-610 648.8 0 104.1 24.5 202.6 68 289.8l-82.4 47.5 40 69.3 82.4-47.6c116.4 175.3 315.7 290.9 541.9 290.9s425.5-115.6 541.9-290.9l82.4 47.6 40-69.3-82.2-47.5zm-104.2-60.1c-11.6 24.2-25.1 47.3-40.1 69.2-95.5 139.5-255.9 231.1-437.7 231.1s-342.3-91.6-437.7-231.1c-15-22-28.4-45.1-40.1-69.2-33.5-69.5-52.2-147.4-52.2-229.7 0-279.3 216-508.1 490-528.5 13.2-1 26.5-1.5 40-1.5s26.8.5 40 1.5c274 20.4 490 249.3 490 528.5 0 82.3-18.7 160.2-52.2 229.7z'/%3E%3Cpath id='Inner_Circle' d='M1199.4 621.5c-13.2-1-26.5-1.5-40-1.5s-26.8.5-40 1.5c-274 20.4-490 249.3-490 528.5 0 82.3 18.8 160.2 52.2 229.7 11.6 24.2 25.1 47.3 40.1 69.2 95.5 139.5 255.9 231.1 437.7 231.1s342.3-91.6 437.7-231.1c15-22 28.4-45.1 40.1-69.2 33.5-69.5 52.2-147.4 52.2-229.7 0-279.3-215.9-508.1-490-528.5zm268.2 752.1H834.9l58.6-417.1-60.6 417.1V908.7h291.6l43.6 47.8h358.1l-58.6 417.1z'/%3E%3Cg id='File'%3E%3Cpath fill='%23E3E2D6' d='m1168.8 957.3-275.3-.8-58.6 417.1h632.7l58.6-417.1h-358.1z'/%3E%3Cpath fill='%23848484' d='m1168.1 956.5-43.6-47.8H832.9v464.9l60.6-417.1 275.3.8z'/%3E%3C/g%3E%3Cg id='Bevel'%3E%3Cpath fill='%23636363' d='M1544.8 237.8c355.3 150.3 604.6 502.1 604.6 912.2 0 40.8-2.5 81.6-7.5 122.1l125 139.7 44.7-40-107.1-119.7c3.3-33.9 4.9-68.1 4.9-102.1 0-210.4-62-413.4-179.3-587.1-56.5-83.7-124.7-158.7-202.7-223.1-71.4-58.9-150-108-233.9-146.2l-50.1-152.4-57 18.7 58.4 177.9z'/%3E%3Cpath fill='%23848484' d='M1802.4 1680h654v60h-654z' transform='matrix(0.5 -0.866 0.866 0.5 -416.2155 2699.0933)'/%3E%3Cpath fill='%23474747' d='m1543.4 41.3-57-41.3v60z'/%3E%3Cpath fill='%236B6B6B' d='m2266.9 1411.8 52 30-7.3-70-44.7 40z'/%3E%3Cpath fill='%23939393' d='m1927.6 2036.9 64.3-28.7-52-30z'/%3E%3Cpath fill='%23636363' d='M379 1978.2 52 1411.8l-52 30 327 566.4 64.2 28.7z'/%3E%3Cpath fill='%23848484' d='M1756.4 1939.8c-166 125.7-372.8 200.2-597 200.2s-431-74.5-597-200.2l-14 64.2c83.3 59.7 174.4 106.7 271.2 139.8 109.1 37.3 223.4 56.2 339.7 56.2 116.3 0 230.6-18.9 339.7-56.2 96.8-33.1 187.9-80.1 271.2-139.8l157.2 32.9 12.3-58.7-183.3-38.4z'/%3E%3Cpath fill='%236D6D6D' d='m379 1978.2 12.2 58.7 157.3-32.9 13.9-64.2z'/%3E%3Cpath d='m832.4 0-57 41.3-50.1 152.4c-83.9 38.1-162.5 87.2-233.9 146.2-78 64.3-146.2 139.4-202.7 223.1-117.3 173.6-179.3 376.6-179.3 587 0 33.9 1.7 68.2 4.9 102.1L7.2 1371.8l44.7 40 125-139.7c-5-40.5-7.5-81.3-7.5-122.1 0-410 249.3-761.8 604.6-912.2L832.4 60h654V0h-654z'/%3E%3Cpath fill='%23474747' d='m7.2 1371.8-7.2 70 52-30z'/%3E%3Cpath fill='%23E3E2D6' d='M2266.9 1411.8z'/%3E%3C/g%3E%3C/svg%3E"); (lines 218-218). Class: (ii) posting rewrite.

- **First, the stub above is a false positive, and a reviewer can settle it in one command.** The classifier's HTTP-KEPT line flags the `--logo-image` line (candidate L218) as a kept http:// occurrence. The only `http://` strings in the candidate are the two W3C namespace identifiers (`http://www.w3.org/2000/svg`, `http://www.w3.org/1999/xlink`) inside that line's SVG data URI, and the line is byte-identical to the original's L210. No http asset is loaded by either file, so there is no T12 residue to disposition. Verify: `grep -o 'http://[^" ]*' candidate.txt` returns exactly those two namespace strings.
- **Item 24 (class F), the ring-logo overprint — DISPOSITIONED.** The full argument is the per-theme record below; its one-sentence form is that every surface that could cause the overprint (the ≤768px header block, the logo markup and sizing, the `--logo-image` artwork) is byte-identical to the original, so the overprint is the original's own narrow-width behaviour, not a port defect. [GOSIGN2-LEDGER-SUPPLEMENT.md item 24; FIX5-FUNC §6; KB-35 family, patterns/ at commit 9c5e9079afb01d30cb9fc4ef9d714e5591eb2ffa]
- **P5, the RAISA logo exhibit image on the EN host (candidate L71) — DISPOSITIONED, class (ii) / KB-58.** The line is byte-identical to the original's L64 — it is part of item 24's own evidence that the sizing never changed. Re-hosting waits on the JP storage upload, which the campaign's no-re-upload rule defers to posting time (KB-58: deferred asset hosting state). This line is the T1 baseline's hotlink×1. The posting instruction, from the localize lane's observation, is on record: swap L71 to the JP-storage copy once uploaded; the same artwork is already embedded as the `--logo-image` data URI.
- **Render-row environment items — DISPOSITIONED, not charged to the theme.** The page-overflow figures (328px@320 + 380px@375) and the runtime-hotlink site-theme chain arrive via the shared site theme, not the candidate (KB-40, environment layer; ledger §(c2)). The sample's T2 exit 2 is a coverage caveat (the run returned no machine verdict), not a theme defect. The broken black-highlighter-logo.svg note is the KB-58 deferred-hosting state of the re-hosted BHL logo (candidate L43). [GOSIGN2-LEDGER.md §(c2), raisa row]
- **Draft-host self-delivery lines (candidate L683, L687) — class (iii) draft form**, rewritten to the production host at posting (section 3). The T1 baseline's pseudo-ref×1 carries the settled class (ii) posting-procedure mapping (AGENTS.md §3, as inventoried in the taxonomy).
- **P11 body link — standing with a record flag** (section 7): not a disposition, because no record dispositions it; it is listed here so the disposition set is complete and auditable in one place.
- **BHL exhibit target (candidate L88)** — a posting-time staff confirmation noted by the localize lane (the exhibit names the `-jp` BHL candidate where the unsuffixed page already exists on scp-jp), recorded in section 2; not a candidate defect.


## 12. Verification

- **T1 (source check):** baseline 2026-11-16: exit 1, 2 errors / 0 warns / 2 infos (hotlink×1, pseudo-ref×1) [T1-ROWS row 153]. Both error codes carry settled classes (section 11); no class (i) error stands against this candidate. Re-run: the campaign checker on `pages/theme:raisa-jp.txt` reproduces the multiset.
- **T2/T3 (render):** combined verdict FINDINGS [RENDER-ROWS-2 (RENDER-S2-C (EN17))]. The one theme-specific item (the ring-logo overprint) is dispositioned as item 24; the remainder are environment-layer and coverage items (section 11). No re-render was run for this package: the render record is the lane's, cited, not re-measured here.
- **T4 (follow-up diff):** `diff --from 56` → no change; the original's current revision is still 56, with no display-affecting updates past the reference revision [LOCALIZE-S2-C, EN17-4]. The mirror in this package is therefore also the current original.
- **T5 (translation text):** judged jointly with T4 by the source report: FINDINGS, whose items are the P5 hotlink and the P11 link (each recorded above at its own weight) and the credit format note, which the current credit bytes overtake (section 1). The lane found no mistranslations or term drift.
- **This package:** `python3 review/build_review.py --check` — the verdict stamp is fresh against the candidate's computed-against commit (1869877f) and hash (d23f2de3…), and diff.md regenerates identically from the two files in this package. The byte-identity measurements in the per-theme record were re-derived from this package's two files while this README was written, not transcribed from the supplement.

## Per-theme record

### The byte-identity disposition (ledger §(e) item 24)

The charge, as the ledger states it: "Header interference: the RAISA ring logo overprints the header wordmark and account links at 375/320 in both engines (render T3) — the same candidate-header-interference shape as queerstyle's. No fix, no disposition in the sources." [GOSIGN2-LEDGER.md §(e) item 24]. Class F charges a candidate-side functional defect, so the question the disposition turns on is narrow and decidable from the two files in this package: did the port introduce, move, resize, or re-layer anything that could make the logo overprint the header at phone widths? If every causally relevant surface is byte-identical to the original, the overprint is a property of the original's design as rendered in the shared header construction, and "fixing" it would mean departing from the original, an editorial change rather than a migration correction.

The relevant surfaces, each re-measured from this package's files for this README (the supplement's claim was not transcribed):

1. **The narrow-width header rules.** The theme's own CSS holds exactly one block that speaks to the header at phone widths, `@media only screen and (max-width: 768px)`: `#header h2` at height 100% with overflow hidden and pointer-events none, the `h2 span` marquee at width 150%, `#header h1 span` at 75%, and the `#top-bar` font size. Original L643–666 = candidate L651–674: 24 lines, 476 bytes, SHA-256 `a23b921ef3ca62a38263b9a7f67d77d653d929964af8018e597b8fd14cde98f8` on both sides. The FIX5-FUNC lane measured a wider window (original L643–668 / candidate L651–676, running through the `[[/code]]` line); that window is also byte-identical (487 bytes, SHA-256 `4556a6d9ffd1432bdf567d6e5a14a120459c32e2f379ee2a44eee2a524a8ed6e`), so a reviewer using either set of line numbers lands on the same bytes. The theme's other media block (765px, the page-title rule) is likewise identical (original L12–18 = candidate L12–18).
2. **The logo markup and sizing.** The ring logo's floated image block: the wrapper div (original L63 / candidate L70, `scp-image-block block-right`, `max-width:300px`) and the image line (original L64 / candidate L71, the same scp-wiki.wdfiles.com URL, `style="max-width:300px"`) — together 178 bytes, SHA-256 `328f322c350b14327a2e991b65f2a1960cbd635a4fb14254415bae4f01f6368b`, byte-identical. Only the block's caption text was translated ("Raisa Logo" → "RAISAロゴ").
3. **The header logo artwork.** The `--logo-image` variable (the ring artwork the BHL header renders) is one 4,162-byte line, byte-identical (original L210 = candidate L218).
4. **Nothing was layered in.** No added line in diff.md carries a `position` or `z-index` property (grep over the diff's added lines returns nothing): the port introduced no positioning anywhere, let alone near the header. Its deltas on the header surface are exactly the credit block, the delivery hosts, and the `--header-title` / `--header-subtitle` translations (section 5) — and header/title language is out of scope for migration correctness under ruling 2 in any case.

The conclusion the identity licenses: the candidate renders the header at 375/320 with the original's own rules, markup, sizing, and artwork, so the overprint the T3 walk photographed is the original theme's narrow-width behaviour, not a defect the port introduced. The supplement files it under the KB-35 family (narrow-width site-header phenomena not charged to the candidate; patterns/ at commit 9c5e9079afb01d30cb9fc4ef9d714e5591eb2ffa). Disposition: **DISPOSITIONED, no edit** [GOSIGN2-LEDGER-SUPPLEMENT.md item 24; FIX5-FUNC §6]. The sibling class-F item for queerstyle (item 22) was dispositioned by the same lane on the same ground (logo rule placement, height, and identity unchanged). A reviewer who wants to re-derive the whole argument needs only this package: extract the two windows named in (1) from original.txt and candidate.txt, hash them, and compare the lines named in (2) and (3).

### Record discrepancies flagged by this package

Three places where the prose record and the bytes (or the record and itself) disagree; in each case this package follows the bytes and the primary rows, and flags the prose.

1. **The render-row citation in §(e) item 24 points at the wrong parts file.** Item 24 cites "R/ledger-parts/RENDER-ROWS-1.md (raisa row)", but RENDER-ROWS-1 (Stage-1 themes plus EN1–EN12) contains no raisa row. The raisa combined render row is in RENDER-ROWS-2 (RENDER-S2-C, EN17), which is also what the generated verdict stamp cites. The finding's substance is unaffected; the pointer is wrong.
2. **The ledger's "P11 → (e) H" pointer does not resolve.** GOSIGN2-LEDGER.md §(c3) sends this theme's P11 item to a class-H entry in §(e); the register holds no H item for raisa and the supplement re-judges none. The source report (LOCALIZE-S2-C, EN17-4) marks the item not display-affecting, which is consistent with its absence from the register of charged items. Section 7 carries the item at that weight.
3. **The vendored LOCALIZE-ROWS cell is truncated mid-sentence.** Row 128's findings cell ends "…should point to the JP BHL page — not …" in the extraction vendored at review/AUTHORITIES/ledger-parts/LOCALIZE-ROWS.md. The source report completes the sentence: "not display-affecting". This README follows the source report.

### Multi-wave provenance

The candidate's current state is the product of successive waves, not one pass: the S2 localization wave (LOCALIZE-S2-C) produced the port itself (frame repoint, credit swap, font supplement, translation); FIX-CREDIT-D (commit 1869877f, the file's last content change) normalized the translator attribution to ruling 3's form; and FIX5-FUNC §6 closed the theme's only blocking item as a no-edit disposition, so no FIX5 commit touches this file. Citations, in place of a changelog: GOSIGN2-LEDGER.md §(c2) (render row), §(c3) (localize row), §(e) item 24; GOSIGN2-LEDGER-SUPPLEMENT.md item 24; REPORT-GOSIGN2-LOCALIZE-S2-C.md (EN17-4); REPORT-GOSIGN2-FIX5-FUNC.md §6. The go-sign re-run over that record is what the Status block certifies.

## Appendix — residue blocks

### Residue R1 — B15 (residue; orig 85-85 -> cand 92-92, body -> body)
- Removed first line: + Examples
- Added first line: + 例

Resolution: section 6, class P10. The section heading '+ Examples' → '+ 例'; the heading level (a single '+') is the anchor the classifier's anchor-majority rule missed.


### Residue R2 — B62 (residue; orig 221-221 -> cand 229-229, code-css -> code-css)
- Removed first line:     /* Standard Colors */
- Added first line:     /* 標準色 */

Resolution: section 6, class R1 (in-CSS text, comment half). A CSS comment translated in place. Comments are porter-visible only and never render, so this is translation completeness, not a display change; the taxonomy's patterns feedback records CSS comments as a known non-finding, and no KB entry is proposed.


### Residue R3 — B63 (residue; orig 223-223 -> cand 231-231, code-css -> code-css)
- Removed first line:     /* white */
- Added first line:     /* 白 */

Resolution: section 6, class R1 (in-CSS text, comment half). A CSS comment translated in place. Comments are porter-visible only and never render, so this is translation completeness, not a display change; the taxonomy's patterns feedback records CSS comments as a known non-finding, and no KB entry is proposed.


### Residue R4 — B66 (residue; orig 229-229 -> cand 237-237, code-css -> code-css)
- Removed first line:     /* gray */
- Added first line:     /* 灰色 */

Resolution: section 6, class R1 (in-CSS text, comment half). A CSS comment translated in place. Comments are porter-visible only and never render, so this is translation completeness, not a display change; the taxonomy's patterns feedback records CSS comments as a known non-finding, and no KB entry is proposed.


### Residue R5 — B68 (residue; orig 233-233 -> cand 241-241, code-css -> code-css)
- Removed first line:     /* black */
- Added first line:     /* 黒 */

Resolution: section 6, class R1 (in-CSS text, comment half). A CSS comment translated in place. Comments are porter-visible only and never render, so this is translation completeness, not a display change; the taxonomy's patterns feedback records CSS comments as a known non-finding, and no KB entry is proposed.


### Residue R6 — B84 (residue; orig 321-321 -> cand 329-329, code-css -> code-css)
- Removed first line:     ======= SPECIFIC COLORS =======
- Added first line:     ======= 個別色 =======

Resolution: section 6, class R1 (in-CSS text, comment half). A CSS comment translated in place. Comments are porter-visible only and never render, so this is translation completeness, not a display change; the taxonomy's patterns feedback records CSS comments as a known non-finding, and no KB entry is proposed.


### Residue R7 — B107 (residue; orig 441-441 -> cand 449-449, code-css -> code-css)
- Removed first line: /* ===GLOBAL ELEMENTS=== */
- Added first line: /* ===全体要素=== */

Resolution: section 6, class R1 (in-CSS text, comment half). A CSS comment translated in place. Comments are porter-visible only and never render, so this is translation completeness, not a display change; the taxonomy's patterns feedback records CSS comments as a known non-finding, and no KB entry is proposed.


### Residue R8 — B2 (heuristic; orig 3-4 -> cand 3-4, module-css -> module-css)
- Removed first line: @import url("https://cdn.scpwiki.com/theme/en/black-highlighter/css/min/normalize.min.css");
- Added first line: @import url("https://scp-jp.github.io/Black-Highlighter/css/min/normalize.min.css");
- Note: no other signature matched

Resolution: section 3, classes P4/T9. The BHL normalize @import host swap (cdn.scpwiki.com → scp-jp.github.io), the same change as B4/B6; the classifier filed it as CSS-BODY in section 8 because the line sits inside the module-css channel, and it is argued with the delivery frame in section 3.


### Residue R9 — B11 (heuristic; orig 66-66 -> cand 73-73, body -> body)
- Removed first line: Raisa Logo
- Added first line: RAISAロゴ
- Note: script delta without the anchor majority

Resolution: section 6, class P10. Usage/specimen prose translated one-to-one; the pairing is confirmed against the mirror at the lines in the heading above. The classifier left the block unanchored because the line carries no leading token or property to anchor on, not because the pairing is in doubt.


### Residue R10 — B13 (heuristic; orig 78-78 -> cand 85-85, body -> body)
- Removed first line: On any wiki:
- Added first line: どのウィキでも、以下のようにします。
- Note: script delta without the anchor majority

Resolution: section 6, class P10. Usage/specimen prose translated one-to-one; the pairing is confirmed against the mirror at the lines in the heading above. The classifier left the block unanchored because the line carries no leading token or property to anchor on, not because the pairing is in doubt.


### Residue R11 — B16 (heuristic; orig 87-87 -> cand 94-94, body -> body)
- Removed first line: A horizontal rule can be created with 5 hyphens "@@-----@@" and extends across the whole page if it's not placed inside anything (eg a blockquote). The lines separating sections of this document are horizontal rules.
- Added first line: 罫線は、5つのハイフン「@@-----@@」で作成できます。何かの内側（例: 引用ブロック）に置かれていなければ、ページ全体に伸びます。このドキュメントのセクションを区切る線は罫線です。
- Note: script delta without the anchor majority

Resolution: section 6, class P10. Usage/specimen prose translated one-to-one; the pairing is confirmed against the mirror at the lines in the heading above. The classifier left the block unanchored because the line carries no leading token or property to anchor on, not because the pairing is in doubt.


### Residue R12 — B17 (heuristic; orig 91-91 -> cand 98-98, body -> body)
- Removed first line: Titles can be created by putting between one and six plus "+" at the start of the line
- Added first line: 見出しは、行頭に1～6個の「+」を置くことで作成できます。
- Note: script delta without the anchor majority

Resolution: section 6, class P10. Usage/specimen prose translated one-to-one; the pairing is confirmed against the mirror at the lines in the heading above. The classifier left the block unanchored because the line carries no leading token or property to anchor on, not because the pairing is in doubt.


### Residue R13 — B26 (heuristic; orig 116-116 -> cand 123-123, body -> body)
- Removed first line: How quaint.
- Added first line: 趣がありますね。
- Note: script delta without the anchor majority

Resolution: section 6, class P10. Usage/specimen prose translated one-to-one; the pairing is confirmed against the mirror at the lines in the heading above. The classifier left the block unanchored because the line carries no leading token or property to anchor on, not because the pairing is in doubt.


### Residue R14 — B28 (heuristic; orig 121-121 -> cand 128-128, body -> body)
- Removed first line: This is a long tab. It contains a lot of text.
- Added first line: これは長いタブです。テキストがたくさん入っています。
- Note: script delta without the anchor majority

Resolution: section 6, class P10. Usage/specimen prose translated one-to-one; the pairing is confirmed against the mirror at the lines in the heading above. The classifier left the block unanchored because the line carries no leading token or property to anchor on, not because the pairing is in doubt.


### Residue R15 — B29 (heuristic; orig 123-123 -> cand 130-130, body -> body)
- Removed first line: This is a long tab. It contains a lot of text.
- Added first line: これは長いタブです。テキストがたくさん入っています。
- Note: script delta without the anchor majority

Resolution: section 6, class P10. Usage/specimen prose translated one-to-one; the pairing is confirmed against the mirror at the lines in the heading above. The classifier left the block unanchored because the line carries no leading token or property to anchor on, not because the pairing is in doubt.


### Residue R16 — B30 (heuristic; orig 125-125 -> cand 132-132, body -> body)
- Removed first line: This is a long tab. It contains a lot of text.
- Added first line: これは長いタブです。テキストがたくさん入っています。
- Note: script delta without the anchor majority

Resolution: section 6, class P10. Usage/specimen prose translated one-to-one; the pairing is confirmed against the mirror at the lines in the heading above. The classifier left the block unanchored because the line carries no leading token or property to anchor on, not because the pairing is in doubt.


### Residue R17 — B31 (heuristic; orig 127-127 -> cand 134-134, body -> body)
- Removed first line: This is a long tab. It contains a lot of text.
- Added first line: これは長いタブです。テキストがたくさん入っています。
- Note: script delta without the anchor majority

Resolution: section 6, class P10. Usage/specimen prose translated one-to-one; the pairing is confirmed against the mirror at the lines in the heading above. The classifier left the block unanchored because the line carries no leading token or property to anchor on, not because the pairing is in doubt.


### Residue R18 — B32 (heuristic; orig 129-129 -> cand 136-136, body -> body)
- Removed first line: This is a long tab. It contains a lot of text.
- Added first line: これは長いタブです。テキストがたくさん入っています。
- Note: script delta without the anchor majority

Resolution: section 6, class P10. Usage/specimen prose translated one-to-one; the pairing is confirmed against the mirror at the lines in the heading above. The classifier left the block unanchored because the line carries no leading token or property to anchor on, not because the pairing is in doubt.


### Residue R19 — B33 (heuristic; orig 131-131 -> cand 138-138, body -> body)
- Removed first line: This is a long tab. It contains a lot of text.
- Added first line: これは長いタブです。テキストがたくさん入っています。
- Note: script delta without the anchor majority

Resolution: section 6, class P10. Usage/specimen prose translated one-to-one; the pairing is confirmed against the mirror at the lines in the heading above. The classifier left the block unanchored because the line carries no leading token or property to anchor on, not because the pairing is in doubt.


### Residue R20 — B34 (heuristic; orig 133-133 -> cand 140-140, body -> body)
- Removed first line: This is a long tab. It contains a lot of text.
- Added first line: これは長いタブです。テキストがたくさん入っています。
- Note: script delta without the anchor majority

Resolution: section 6, class P10. Usage/specimen prose translated one-to-one; the pairing is confirmed against the mirror at the lines in the heading above. The classifier left the block unanchored because the line carries no leading token or property to anchor on, not because the pairing is in doubt.


### Residue R21 — B35 (heuristic; orig 135-135 -> cand 142-142, body -> body)
- Removed first line: This is a long tab. It contains a lot of text.
- Added first line: これは長いタブです。テキストがたくさん入っています。
- Note: script delta without the anchor majority

Resolution: section 6, class P10. Usage/specimen prose translated one-to-one; the pairing is confirmed against the mirror at the lines in the heading above. The classifier left the block unanchored because the line carries no leading token or property to anchor on, not because the pairing is in doubt.


### Residue R22 — B36 (heuristic; orig 137-137 -> cand 144-144, body -> body)
- Removed first line: This is a long tab. It contains a lot of text.
- Added first line: これは長いタブです。テキストがたくさん入っています。
- Note: script delta without the anchor majority

Resolution: section 6, class P10. Usage/specimen prose translated one-to-one; the pairing is confirmed against the mirror at the lines in the heading above. The classifier left the block unanchored because the line carries no leading token or property to anchor on, not because the pairing is in doubt.


### Residue R23 — B37 (heuristic; orig 139-139 -> cand 146-146, body -> body)
- Removed first line: This is a long tab. It contains a lot of text.
- Added first line: これは長いタブです。テキストがたくさん入っています。
- Note: script delta without the anchor majority

Resolution: section 6, class P10. Usage/specimen prose translated one-to-one; the pairing is confirmed against the mirror at the lines in the heading above. The classifier left the block unanchored because the line carries no leading token or property to anchor on, not because the pairing is in doubt.


### Residue R24 — B38 (heuristic; orig 141-141 -> cand 148-148, body -> body)
- Removed first line: This is a long tab. It contains a lot of text.
- Added first line: これは長いタブです。テキストがたくさん入っています。
- Note: script delta without the anchor majority

Resolution: section 6, class P10. Usage/specimen prose translated one-to-one; the pairing is confirmed against the mirror at the lines in the heading above. The classifier left the block unanchored because the line carries no leading token or property to anchor on, not because the pairing is in doubt.


### Residue R25 — B45 (heuristic; orig 158-158 -> cand 165-165, body -> body)
- Removed first line: > This is a blockquote, created by putting "> " at the start of each line.
- Added first line: > これは引用ブロックです。各行の先頭に半角の「> 」を置くことで作成されます。
- Note: script delta without the anchor majority

Resolution: section 6, class P10. Usage/specimen prose translated one-to-one; the pairing is confirmed against the mirror at the lines in the heading above. The classifier left the block unanchored because the line carries no leading token or property to anchor on, not because the pairing is in doubt.


### Residue R26 — B46 (heuristic; orig 160-160 -> cand 167-167, body -> body)
- Removed first line: > More text
- Added first line: > 追加のテキスト
- Note: script delta without the anchor majority

Resolution: section 6, class P10. Usage/specimen prose translated one-to-one; the pairing is confirmed against the mirror at the lines in the heading above. The classifier left the block unanchored because the line carries no leading token or property to anchor on, not because the pairing is in doubt.


### Residue R27 — B47 (heuristic; orig 162-162 -> cand 169-169, body -> body)
- Removed first line: > That's a horizontal rule
- Added first line: > これは罫線です
- Note: script delta without the anchor majority

Resolution: section 6, class P10. Usage/specimen prose translated one-to-one; the pairing is confirmed against the mirror at the lines in the heading above. The classifier left the block unanchored because the line carries no leading token or property to anchor on, not because the pairing is in doubt.


### Residue R28 — B48 (heuristic; orig 164-165 -> cand 171-172, body -> body)
- Removed first line: >> Nested blockquotes
- Added first line: >> 入れ子になった引用ブロック
- Note: script delta without the anchor majority

Resolution: section 6, class P10. Usage/specimen prose translated one-to-one; the pairing is confirmed against the mirror at the lines in the heading above. The classifier left the block unanchored because the line carries no leading token or property to anchor on, not because the pairing is in doubt.


### Residue R29 — B52 (heuristic; orig 185-189 -> cand 192-196, code-css -> code-css)
- Removed first line:     Raisa Theme
- Added first line:     RAISAテーマ
- Note: porter-visible only; labeled and skipped by design
- Note: script delta without the anchor majority

Resolution: section 6, class R1 (in-CSS text, comment half). A CSS comment translated in place. Comments are porter-visible only and never render, so this is translation completeness, not a display change; the taxonomy's patterns feedback records CSS comments as a known non-finding, and no KB entry is proposed.


### Residue R30 — B53 (heuristic; orig 192-192 -> cand 199-199, code-css -> code-css)
- Removed first line: /* Fonts */
- Added first line: /* フォント */
- Note: porter-visible only; labeled and skipped by design
- Note: script delta without the anchor majority

Resolution: section 6, class R1 (in-CSS text, comment half). A CSS comment translated in place. Comments are porter-visible only and never render, so this is translation completeness, not a display change; the taxonomy's patterns feedback records CSS comments as a known non-finding, and no KB entry is proposed.


### Residue R31 — B55 (heuristic; orig 197-197 -> cand 205-205, code-css -> code-css)
- Removed first line: /* All Vars Used */
- Added first line: /* 使用する全変数 */
- Note: porter-visible only; labeled and skipped by design
- Note: script delta without the anchor majority

Resolution: section 6, class R1 (in-CSS text, comment half). A CSS comment translated in place. Comments are porter-visible only and never render, so this is translation completeness, not a display change; the taxonomy's patterns feedback records CSS comments as a known non-finding, and no KB entry is proposed.


### Residue R32 — B56 (heuristic; orig 200-201 -> cand 208-209, code-css -> code-css)
- Removed first line:     /* S-CSS-P Integration */
- Added first line:     /* S-CSS-P連携 */
- Note: porter-visible only; labeled and skipped by design
- Note: script delta without the anchor majority

Resolution: section 6, class R1 (in-CSS text, comment half). A CSS comment translated in place. Comments are porter-visible only and never render, so this is translation completeness, not a display change; the taxonomy's patterns feedback records CSS comments as a known non-finding, and no KB entry is proposed.


### Residue R33 — B57 (heuristic; orig 203-203 -> cand 211-211, code-css -> code-css)
- Removed first line:     /* mua be either "nuscp" or "sigma9" */
- Added first line:     /* "nuscp"か"sigma9"のどちらかにしてください。 */
- Note: porter-visible only; labeled and skipped by design
- Note: script delta without the anchor majority

Resolution: section 6, class R1 (in-CSS text, comment half). A CSS comment translated in place. Comments are porter-visible only and never render, so this is translation completeness, not a display change; the taxonomy's patterns feedback records CSS comments as a known non-finding, and no KB entry is proposed.


### Residue R34 — B59 (heuristic; orig 209-209 -> cand 217-217, code-css -> code-css)
- Removed first line:     /* Header */
- Added first line:     /* ヘッダー */
- Note: porter-visible only; labeled and skipped by design
- Note: script delta without the anchor majority

Resolution: section 6, class R1 (in-CSS text, comment half). A CSS comment translated in place. Comments are porter-visible only and never render, so this is translation completeness, not a display change; the taxonomy's patterns feedback records CSS comments as a known non-finding, and no KB entry is proposed.


### Residue R35 — B61 (heuristic; orig 214-218 -> cand 222-226, code-css -> code-css)
- Removed first line:     /* Typefaces */
- Added first line:     /* 書体 */
- Note: no other signature matched

Resolution: section 4, class P7. The typeface variable stacks gain 'Noto Sans JP' (and the body/title generic fallback changes from cursive to sans-serif with it); the classifier filed the block as CSS-BODY in section 8, and it is argued with the font supplement in section 4.


### Residue R36 — B64 (heuristic; orig 225-225 -> cand 233-233, code-css -> code-css)
- Removed first line:     /* v light gray for blockquotes and stuff */
- Added first line:     /* 引用ブロックなどに使うごく薄い灰色 */
- Note: porter-visible only; labeled and skipped by design
- Note: script delta without the anchor majority

Resolution: section 6, class R1 (in-CSS text, comment half). A CSS comment translated in place. Comments are porter-visible only and never render, so this is translation completeness, not a display change; the taxonomy's patterns feedback records CSS comments as a known non-finding, and no KB entry is proposed.


### Residue R37 — B65 (heuristic; orig 227-227 -> cand 235-235, code-css -> code-css)
- Removed first line:     /* light accent gray for login status */
- Added first line:     /* ログイン状態に使う薄いアクセント灰色 */
- Note: porter-visible only; labeled and skipped by design
- Note: script delta without the anchor majority

Resolution: section 6, class R1 (in-CSS text, comment half). A CSS comment translated in place. Comments are porter-visible only and never render, so this is translation completeness, not a display change; the taxonomy's patterns feedback records CSS comments as a known non-finding, and no KB entry is proposed.


### Residue R38 — B67 (heuristic; orig 231-231 -> cand 239-239, code-css -> code-css)
- Removed first line:     /* dark accent gray for sidebar background */
- Added first line:     /* サイドバー背景に使う濃いアクセント灰色 */
- Note: porter-visible only; labeled and skipped by design
- Note: script delta without the anchor majority

Resolution: section 6, class R1 (in-CSS text, comment half). A CSS comment translated in place. Comments are porter-visible only and never render, so this is translation completeness, not a display change; the taxonomy's patterns feedback records CSS comments as a known non-finding, and no KB entry is proposed.


### Residue R39 — B69 (heuristic; orig 235-235 -> cand 243-243, code-css -> code-css)
- Removed first line:     /* bright yellow for header */
- Added first line:     /* ヘッダー用の明るい黄色 */
- Note: porter-visible only; labeled and skipped by design
- Note: script delta without the anchor majority

Resolution: section 6, class R1 (in-CSS text, comment half). A CSS comment translated in place. Comments are porter-visible only and never render, so this is translation completeness, not a display change; the taxonomy's patterns feedback records CSS comments as a known non-finding, and no KB entry is proposed.


### Residue R40 — B70 (heuristic; orig 237-237 -> cand 245-245, code-css -> code-css)
- Removed first line:     /* medium yellow for header */
- Added first line:     /* ヘッダー用の中間黄色 */
- Note: porter-visible only; labeled and skipped by design
- Note: script delta without the anchor majority

Resolution: section 6, class R1 (in-CSS text, comment half). A CSS comment translated in place. Comments are porter-visible only and never render, so this is translation completeness, not a display change; the taxonomy's patterns feedback records CSS comments as a known non-finding, and no KB entry is proposed.


### Residue R41 — B71 (heuristic; orig 239-239 -> cand 247-247, code-css -> code-css)
- Removed first line:     /* dark yellow-brown */
- Added first line:     /* 濃い黄褐色 */
- Note: porter-visible only; labeled and skipped by design
- Note: script delta without the anchor majority

Resolution: section 6, class R1 (in-CSS text, comment half). A CSS comment translated in place. Comments are porter-visible only and never render, so this is translation completeness, not a display change; the taxonomy's patterns feedback records CSS comments as a known non-finding, and no KB entry is proposed.


### Residue R42 — B72 (heuristic; orig 241-241 -> cand 249-249, code-css -> code-css)
- Removed first line:     /* bright blue */
- Added first line:     /* 明るい青 */
- Note: porter-visible only; labeled and skipped by design
- Note: script delta without the anchor majority

Resolution: section 6, class R1 (in-CSS text, comment half). A CSS comment translated in place. Comments are porter-visible only and never render, so this is translation completeness, not a display change; the taxonomy's patterns feedback records CSS comments as a known non-finding, and no KB entry is proposed.


### Residue R43 — B73 (heuristic; orig 243-243 -> cand 251-251, code-css -> code-css)
- Removed first line:     /* faded yellow for terminal borders*/
- Added first line:     /* 端末風の境界線に使うくすんだ黄色 */
- Note: porter-visible only; labeled and skipped by design
- Note: script delta without the anchor majority

Resolution: section 6, class R1 (in-CSS text, comment half). A CSS comment translated in place. Comments are porter-visible only and never render, so this is translation completeness, not a display change; the taxonomy's patterns feedback records CSS comments as a known non-finding, and no KB entry is proposed.


### Residue R44 — B74 (heuristic; orig 245-245 -> cand 253-253, code-css -> code-css)
- Removed first line:     /* dark yellow-brown */
- Added first line:     /* 濃い黄褐色 */
- Note: porter-visible only; labeled and skipped by design
- Note: script delta without the anchor majority

Resolution: section 6, class R1 (in-CSS text, comment half). A CSS comment translated in place. Comments are porter-visible only and never render, so this is translation completeness, not a display change; the taxonomy's patterns feedback records CSS comments as a known non-finding, and no KB entry is proposed.


### Residue R45 — B75 (heuristic; orig 247-247 -> cand 255-255, code-css -> code-css)
- Removed first line:     /* Primary Theme Colors */
- Added first line:     /* 主要テーマ色 */
- Note: porter-visible only; labeled and skipped by design
- Note: script delta without the anchor majority

Resolution: section 6, class R1 (in-CSS text, comment half). A CSS comment translated in place. Comments are porter-visible only and never render, so this is translation completeness, not a display change; the taxonomy's patterns feedback records CSS comments as a known non-finding, and no KB entry is proposed.


### Residue R46 — B76 (heuristic; orig 251-251 -> cand 259-259, code-css -> code-css)
- Removed first line:     /* Primary Text Colors */
- Added first line:     /* 主要テキスト色 */
- Note: porter-visible only; labeled and skipped by design
- Note: script delta without the anchor majority

Resolution: section 6, class R1 (in-CSS text, comment half). A CSS comment translated in place. Comments are porter-visible only and never render, so this is translation completeness, not a display change; the taxonomy's patterns feedback records CSS comments as a known non-finding, and no KB entry is proposed.


### Residue R47 — B77 (heuristic; orig 256-256 -> cand 264-264, code-css -> code-css)
- Removed first line:     /* Primary Menu Colors */
- Added first line:     /* 主要メニュー色 */
- Note: porter-visible only; labeled and skipped by design
- Note: script delta without the anchor majority

Resolution: section 6, class R1 (in-CSS text, comment half). A CSS comment translated in place. Comments are porter-visible only and never render, so this is translation completeness, not a display change; the taxonomy's patterns feedback records CSS comments as a known non-finding, and no KB entry is proposed.


### Residue R48 — B78 (heuristic; orig 267-267 -> cand 275-275, code-css -> code-css)
- Removed first line:     /* Primary Header Colors */
- Added first line:     /* 主要ヘッダー色 */
- Note: porter-visible only; labeled and skipped by design
- Note: script delta without the anchor majority

Resolution: section 6, class R1 (in-CSS text, comment half). A CSS comment translated in place. Comments are porter-visible only and never render, so this is translation completeness, not a display change; the taxonomy's patterns feedback records CSS comments as a known non-finding, and no KB entry is proposed.


### Residue R49 — B79 (heuristic; orig 271-272 -> cand 279-280, code-css -> code-css)
- Removed first line:     /* ===SECONDARY & TERTIARY COLORS=== */
- Added first line:     /* ===第2・第3色=== */
- Note: porter-visible only; labeled and skipped by design
- Note: script delta without the anchor majority

Resolution: section 6, class R1 (in-CSS text, comment half). A CSS comment translated in place. Comments are porter-visible only and never render, so this is translation completeness, not a display change; the taxonomy's patterns feedback records CSS comments as a known non-finding, and no KB entry is proposed.


### Residue R50 — B80 (heuristic; orig 274-274 -> cand 282-282, code-css -> code-css)
- Removed first line:     /* Colors for Secondary & Tertiary items like Blockquote and YUI Tabs */
- Added first line:     /* 引用ブロックやYUIタブなど、第2・第3要素用の色 */
- Note: porter-visible only; labeled and skipped by design
- Note: script delta without the anchor majority

Resolution: section 6, class R1 (in-CSS text, comment half). A CSS comment translated in place. Comments are porter-visible only and never render, so this is translation completeness, not a display change; the taxonomy's patterns feedback records CSS comments as a known non-finding, and no KB entry is proposed.


### Residue R51 — B81 (heuristic; orig 279-279 -> cand 287-287, code-css -> code-css)
- Removed first line:     /* Text Colors for Secondary & Tertiary items like Sidebar Headers and Top-Bar Menu Text */
- Added first line:     /* サイドバー見出しやトップバーメニューテキストなど、第2・第3要素用のテキスト色 */
- Note: porter-visible only; labeled and skipped by design
- Note: script delta without the anchor majority

Resolution: section 6, class R1 (in-CSS text, comment half). A CSS comment translated in place. Comments are porter-visible only and never render, so this is translation completeness, not a display change; the taxonomy's patterns feedback records CSS comments as a known non-finding, and no KB entry is proposed.


### Residue R52 — B82 (heuristic; orig 283-283 -> cand 291-291, code-css -> code-css)
- Removed first line:     /* Header Gradients */
- Added first line:     /* ヘッダーのグラデーション */
- Note: porter-visible only; labeled and skipped by design
- Note: script delta without the anchor majority

Resolution: section 6, class R1 (in-CSS text, comment half). A CSS comment translated in place. Comments are porter-visible only and never render, so this is translation completeness, not a display change; the taxonomy's patterns feedback records CSS comments as a known non-finding, and no KB entry is proposed.


### Residue R53 — B83 (heuristic; orig 313-313 -> cand 321-321, code-css -> code-css)
- Removed first line:     /* Sidebar */
- Added first line:     /* サイドバー */
- Note: porter-visible only; labeled and skipped by design
- Note: script delta without the anchor majority

Resolution: section 6, class R1 (in-CSS text, comment half). A CSS comment translated in place. Comments are porter-visible only and never render, so this is translation completeness, not a display change; the taxonomy's patterns feedback records CSS comments as a known non-finding, and no KB entry is proposed.


### Residue R54 — B85 (heuristic; orig 323-323 -> cand 331-331, code-css -> code-css)
- Removed first line: /* Colors for Buttons, Tabs, Tables, Footnotes Hover/Modal, Etc. */
- Added first line: /* ボタン、タブ、表、脚注ホバー、モーダルなどの色 */
- Note: porter-visible only; labeled and skipped by design
- Note: script delta without the anchor majority

Resolution: section 6, class R1 (in-CSS text, comment half). A CSS comment translated in place. Comments are porter-visible only and never render, so this is translation completeness, not a display change; the taxonomy's patterns feedback records CSS comments as a known non-finding, and no KB entry is proposed.


### Residue R55 — B86 (heuristic; orig 326-326 -> cand 334-334, code-css -> code-css)
- Removed first line:     /* ===BACKGROUND GRADIENT=== */
- Added first line:     /* ===背景グラデーション=== */
- Note: porter-visible only; labeled and skipped by design
- Note: script delta without the anchor majority

Resolution: section 6, class R1 (in-CSS text, comment half). A CSS comment translated in place. Comments are porter-visible only and never render, so this is translation completeness, not a display change; the taxonomy's patterns feedback records CSS comments as a known non-finding, and no KB entry is proposed.


### Residue R56 — B87 (heuristic; orig 328-329 -> cand 336-337, code-css -> code-css)
- Removed first line:     /* ===GENERAL BACKGROUND=== */
- Added first line:     /* ===全体背景=== */
- Note: porter-visible only; labeled and skipped by design
- Note: script delta without the anchor majority

Resolution: section 6, class R1 (in-CSS text, comment half). A CSS comment translated in place. Comments are porter-visible only and never render, so this is translation completeness, not a display change; the taxonomy's patterns feedback records CSS comments as a known non-finding, and no KB entry is proposed.


### Residue R57 — B88 (heuristic; orig 331-331 -> cand 339-339, code-css -> code-css)
- Removed first line:     /* Gradient Color used for the --gradient-background var */
- Added first line:     /* --gradient-background変数で使うグラデーション色 */
- Note: porter-visible only; labeled and skipped by design
- Note: script delta without the anchor majority

Resolution: section 6, class R1 (in-CSS text, comment half). A CSS comment translated in place. Comments are porter-visible only and never render, so this is translation completeness, not a display change; the taxonomy's patterns feedback records CSS comments as a known non-finding, and no KB entry is proposed.


### Residue R58 — B89 (heuristic; orig 334-334 -> cand 342-342, code-css -> code-css)
- Removed first line:     /* ===LINK COLORS=== */
- Added first line:     /* ===リンク色=== */
- Note: porter-visible only; labeled and skipped by design
- Note: script delta without the anchor majority

Resolution: section 6, class R1 (in-CSS text, comment half). A CSS comment translated in place. Comments are porter-visible only and never render, so this is translation completeness, not a display change; the taxonomy's patterns feedback records CSS comments as a known non-finding, and no KB entry is proposed.


### Residue R59 — B90 (heuristic; orig 341-343 -> cand 349-351, code-css -> code-css)
- Removed first line:     /* ===HEADER ELEMENTS=== */
- Added first line:     /* ===ヘッダー要素=== */
- Note: porter-visible only; labeled and skipped by design
- Note: script delta without the anchor majority

Resolution: section 6, class R1 (in-CSS text, comment half). A CSS comment translated in place. Comments are porter-visible only and never render, so this is translation completeness, not a display change; the taxonomy's patterns feedback records CSS comments as a known non-finding, and no KB entry is proposed.


### Residue R60 — B91 (heuristic; orig 347-347 -> cand 355-355, code-css -> code-css)
- Removed first line:     /* Focus is when the search box has been clicked on */
- Added first line:     /* フォーカスは検索ボックスがクリックされた状態を指す */
- Note: porter-visible only; labeled and skipped by design
- Note: script delta without the anchor majority

Resolution: section 6, class R1 (in-CSS text, comment half). A CSS comment translated in place. Comments are porter-visible only and never render, so this is translation completeness, not a display change; the taxonomy's patterns feedback records CSS comments as a known non-finding, and no KB entry is proposed.


### Residue R61 — B92 (heuristic; orig 353-353 -> cand 361-361, code-css -> code-css)
- Removed first line:     /* ===LOGIN BOX ELEMENT=== */
- Added first line:     /* ===ログインボックス要素=== */
- Note: porter-visible only; labeled and skipped by design
- Note: script delta without the anchor majority

Resolution: section 6, class R1 (in-CSS text, comment half). A CSS comment translated in place. Comments are porter-visible only and never render, so this is translation completeness, not a display change; the taxonomy's patterns feedback records CSS comments as a known non-finding, and no KB entry is proposed.


### Residue R62 — B93 (heuristic; orig 363-363 -> cand 371-371, code-css -> code-css)
- Removed first line:     /* ===TOPBAR ELEMENTS=== */
- Added first line:     /* ===トップバー要素=== */
- Note: porter-visible only; labeled and skipped by design
- Note: script delta without the anchor majority

Resolution: section 6, class R1 (in-CSS text, comment half). A CSS comment translated in place. Comments are porter-visible only and never render, so this is translation completeness, not a display change; the taxonomy's patterns feedback records CSS comments as a known non-finding, and no KB entry is proposed.


### Residue R63 — B94 (heuristic; orig 365-365 -> cand 373-373, code-css -> code-css)
- Removed first line:     /* ===TOPBAR CATEGORIES=== */
- Added first line:     /* ===トップバーのカテゴリ=== */
- Note: porter-visible only; labeled and skipped by design
- Note: script delta without the anchor majority

Resolution: section 6, class R1 (in-CSS text, comment half). A CSS comment translated in place. Comments are porter-visible only and never render, so this is translation completeness, not a display change; the taxonomy's patterns feedback records CSS comments as a known non-finding, and no KB entry is proposed.


### Residue R64 — B95 (heuristic; orig 374-374 -> cand 382-382, code-css -> code-css)
- Removed first line:     /* ===SIDE-BAR ELEMENTS=== */
- Added first line:     /* ===サイドバー要素=== */
- Note: porter-visible only; labeled and skipped by design
- Note: script delta without the anchor majority

Resolution: section 6, class R1 (in-CSS text, comment half). A CSS comment translated in place. Comments are porter-visible only and never render, so this is translation completeness, not a display change; the taxonomy's patterns feedback records CSS comments as a known non-finding, and no KB entry is proposed.


### Residue R65 — B96 (heuristic; orig 376-376 -> cand 384-384, code-css -> code-css)
- Removed first line:     /* ===MENU-ITEMS=== */
- Added first line:     /* ===メニュー項目=== */
- Note: porter-visible only; labeled and skipped by design
- Note: script delta without the anchor majority

Resolution: section 6, class R1 (in-CSS text, comment half). A CSS comment translated in place. Comments are porter-visible only and never render, so this is translation completeness, not a display change; the taxonomy's patterns feedback records CSS comments as a known non-finding, and no KB entry is proposed.


### Residue R66 — B97 (heuristic; orig 381-382 -> cand 389-390, code-css -> code-css)
- Removed first line:     /* ===SIDEBAR COLLAPSIBLES=== */
- Added first line:     /* ===サイドバー折り畳み=== */
- Note: porter-visible only; labeled and skipped by design
- Note: script delta without the anchor majority

Resolution: section 6, class R1 (in-CSS text, comment half). A CSS comment translated in place. Comments are porter-visible only and never render, so this is translation completeness, not a display change; the taxonomy's patterns feedback records CSS comments as a known non-finding, and no KB entry is proposed.


### Residue R67 — B98 (heuristic; orig 386-386 -> cand 394-394, code-css -> code-css)
- Removed first line:     /*Unfolded Colors */
- Added first line:     /* 展開時の色 */
- Note: porter-visible only; labeled and skipped by design
- Note: script delta without the anchor majority

Resolution: section 6, class R1 (in-CSS text, comment half). A CSS comment translated in place. Comments are porter-visible only and never render, so this is translation completeness, not a display change; the taxonomy's patterns feedback records CSS comments as a known non-finding, and no KB entry is proposed.


### Residue R68 — B99 (heuristic; orig 390-390 -> cand 398-398, code-css -> code-css)
- Removed first line:     /* Unfolded Body Colors */
- Added first line:     /* 展開本文の色 */
- Note: porter-visible only; labeled and skipped by design
- Note: script delta without the anchor majority

Resolution: section 6, class R1 (in-CSS text, comment half). A CSS comment translated in place. Comments are porter-visible only and never render, so this is translation completeness, not a display change; the taxonomy's patterns feedback records CSS comments as a known non-finding, and no KB entry is proposed.


### Residue R69 — B100 (heuristic; orig 394-394 -> cand 402-402, code-css -> code-css)
- Removed first line: /* ===FOOTER=== */
- Added first line: /* ===フッター=== */
- Note: porter-visible only; labeled and skipped by design
- Note: script delta without the anchor majority

Resolution: section 6, class R1 (in-CSS text, comment half). A CSS comment translated in place. Comments are porter-visible only and never render, so this is translation completeness, not a display change; the taxonomy's patterns feedback records CSS comments as a known non-finding, and no KB entry is proposed.


### Residue R70 — B101 (heuristic; orig 403-403 -> cand 411-411, code-css -> code-css)
- Removed first line: /* ===LICENSE AREA=== */
- Added first line: /* ===ライセンス領域=== */
- Note: porter-visible only; labeled and skipped by design
- Note: script delta without the anchor majority

Resolution: section 6, class R1 (in-CSS text, comment half). A CSS comment translated in place. Comments are porter-visible only and never render, so this is translation completeness, not a display change; the taxonomy's patterns feedback records CSS comments as a known non-finding, and no KB entry is proposed.


### Residue R71 — B102 (heuristic; orig 413-415 -> cand 421-423, code-css -> code-css)
- Removed first line:     /* ===MAIN CONTENT UI ELEMENTS */
- Added first line:     /* ===本文UI要素 */
- Note: porter-visible only; labeled and skipped by design
- Note: script delta without the anchor majority

Resolution: section 6, class R1 (in-CSS text, comment half). A CSS comment translated in place. Comments are porter-visible only and never render, so this is translation completeness, not a display change; the taxonomy's patterns feedback records CSS comments as a known non-finding, and no KB entry is proposed.


### Residue R72 — B103 (heuristic; orig 419-419 -> cand 427-427, code-css -> code-css)
- Removed first line:     /* ===TEXT EDITOR ICONS=== */
- Added first line:     /* ===テキストエディタアイコン=== */
- Note: porter-visible only; labeled and skipped by design
- Note: script delta without the anchor majority

Resolution: section 6, class R1 (in-CSS text, comment half). A CSS comment translated in place. Comments are porter-visible only and never render, so this is translation completeness, not a display change; the taxonomy's patterns feedback records CSS comments as a known non-finding, and no KB entry is proposed.


### Residue R73 — B104 (heuristic; orig 422-422 -> cand 430-430, code-css -> code-css)
- Removed first line:     /* ===TABS=== */
- Added first line:     /* ===タブ=== */
- Note: porter-visible only; labeled and skipped by design
- Note: script delta without the anchor majority

Resolution: section 6, class R1 (in-CSS text, comment half). A CSS comment translated in place. Comments are porter-visible only and never render, so this is translation completeness, not a display change; the taxonomy's patterns feedback records CSS comments as a known non-finding, and no KB entry is proposed.


### Residue R74 — B105 (heuristic; orig 429-429 -> cand 437-437, code-css -> code-css)
- Removed first line:     /* ===FOOTNOTES/BIBLIOGRAPHY FOOTER=== */
- Added first line:     /* ===脚注・参考文献フッター=== */
- Note: porter-visible only; labeled and skipped by design
- Note: script delta without the anchor majority

Resolution: section 6, class R1 (in-CSS text, comment half). A CSS comment translated in place. Comments are porter-visible only and never render, so this is translation completeness, not a display change; the taxonomy's patterns feedback records CSS comments as a known non-finding, and no KB entry is proposed.


### Residue R75 — B106 (heuristic; orig 434-434 -> cand 442-442, code-css -> code-css)
- Removed first line:     /* ===PAGE TAGS=== */
- Added first line:     /* ===ページタグ=== */
- Note: porter-visible only; labeled and skipped by design
- Note: script delta without the anchor majority

Resolution: section 6, class R1 (in-CSS text, comment half). A CSS comment translated in place. Comments are porter-visible only and never render, so this is translation completeness, not a display change; the taxonomy's patterns feedback records CSS comments as a known non-finding, and no KB entry is proposed.


### Residue R76 — B108 (heuristic; orig 443-443 -> cand 451-451, code-css -> code-css)
- Removed first line:     /* ===UI BUTTONS=== */
- Added first line:     /* ===UIボタン=== */
- Note: porter-visible only; labeled and skipped by design
- Note: script delta without the anchor majority

Resolution: section 6, class R1 (in-CSS text, comment half). A CSS comment translated in place. Comments are porter-visible only and never render, so this is translation completeness, not a display change; the taxonomy's patterns feedback records CSS comments as a known non-finding, and no KB entry is proposed.


### Residue R77 — B109 (heuristic; orig 448-448 -> cand 456-456, code-css -> code-css)
- Removed first line:     /* ===RATING MODULE=== */
- Added first line:     /* ===評価モジュール=== */
- Note: porter-visible only; labeled and skipped by design
- Note: script delta without the anchor majority

Resolution: section 6, class R1 (in-CSS text, comment half). A CSS comment translated in place. Comments are porter-visible only and never render, so this is translation completeness, not a display change; the taxonomy's patterns feedback records CSS comments as a known non-finding, and no KB entry is proposed.


### Residue R78 — B110 (heuristic; orig 459-459 -> cand 467-467, code-css -> code-css)
- Removed first line:     /* ===MODALS=== */
- Added first line:     /* ===モーダル=== */
- Note: porter-visible only; labeled and skipped by design
- Note: script delta without the anchor majority

Resolution: section 6, class R1 (in-CSS text, comment half). A CSS comment translated in place. Comments are porter-visible only and never render, so this is translation completeness, not a display change; the taxonomy's patterns feedback records CSS comments as a known non-finding, and no KB entry is proposed.


### Residue R79 — B111 (heuristic; orig 466-466 -> cand 474-474, code-css -> code-css)
- Removed first line:     /* ===FOOTNOTES HOVER BLOCK=== */
- Added first line:     /* ===脚注ホバーブロック=== */
- Note: porter-visible only; labeled and skipped by design
- Note: script delta without the anchor majority

Resolution: section 6, class R1 (in-CSS text, comment half). A CSS comment translated in place. Comments are porter-visible only and never render, so this is translation completeness, not a display change; the taxonomy's patterns feedback records CSS comments as a known non-finding, and no KB entry is proposed.


### Residue R80 — B112 (heuristic; orig 472-472 -> cand 480-480, code-css -> code-css)
- Removed first line:     /* ===LISTPAGES PAGER=== */
- Added first line:     /* ===ListPagesページャー=== */
- Note: porter-visible only; labeled and skipped by design
- Note: script delta without the anchor majority

Resolution: section 6, class R1 (in-CSS text, comment half). A CSS comment translated in place. Comments are porter-visible only and never render, so this is translation completeness, not a display change; the taxonomy's patterns feedback records CSS comments as a known non-finding, and no KB entry is proposed.


### Residue R81 — B113 (heuristic; orig at 670 -> cand 678-679, body -> body)
- Added first line: **フォント:** 使用している欧文・和文書体はいずれもGoogle Fontsで配信されるオープンライセンスの書体です（SIL Open Font License など）。日本語文字はNoto Sans JPにフォールバックします。
- Note: script delta without the anchor majority

Resolution: sections 4 and 10, class P7 (credit half) with an R2 shape. This block is an addition, not a translation: the font-credit line at candidate L678 has no original counterpart. It is the credit the font supplement requires for the added JP face, placed after the code exhibit's collapsible; argued in section 10.


## License and attribution

- **Title:** RAISA Theme
- **Author:** Rounderhouse
- **Source:** https://scp-wiki.wikidot.com/theme:raisa — revision 56
- **License:** Creative Commons Attribution-ShareAlike 3.0 (CC BY-SA 3.0) — license deed: https://creativecommons.org/licenses/by-sa/3.0/
- **Adaptation:** This package holds a Sigma-10 migration port of the work; changes were made. See "Summary" and "Standing sections" in this README for what changed and why. Translator: AI (Muse and its delegated agents), per the campaign's standing attribution rule.
