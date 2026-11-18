# Review package — theme:foxtrot-jp (EN → JP, production-counterpart adoption)

<!-- BEGIN GENERATED VERDICT STAMP — do not hand-edit; regenerate with review/build_review.py -->
## Verdict stamp
- Theme: theme:foxtrot-jp — origin EN, population #13 [GOSIGN2-LEDGER (b) row 13]
- Overall: STALE — candidate file changed since the verdict was computed (verdict against 435a6bb-era content, file sha256 now 91b5b57ec3b0742815917d3e267f440c8454c93c70e5f35acaab5e714a401272); verdict not carried over, re-judgement required
> verdicts below describe the pre-change file
- T1 (source check): FINDINGS (classified) — baseline 2026-11-16: exit 1, 33 errors / 6 warns / 3 infos (http×30, foreign-include×2, hotlink×1); standing classes dispositioned in register c1 [T1-ROWS row 13; GOSIGN2-LEDGER (b) row 13]
- T2/T3 (render, combined verdict): FINDINGS — [combined T2/T3] report `FINDINGS` — T2 exit 2 ×2 both pages (chromium-320 `.open-menu a` click intercepted by `login-status`, deterministic); T3 320px ≡/sign-in overlap + SP overflow 729/754px. [RENDER-ROWS-1 (RENDER-B row 13)]
- Engine coverage: full matrix as run by the lane; coverage not separately caveated in the row (the row records inconclusive runs, carried verbatim above) [RENDER-ROWS-1 row]
- Credit modal: no credit-modal line in this theme's row; no sample credit-modal error recorded [RENDER-ROWS-1 (RENDER-B row 13)]
- T4 (localize patterns + follow-up): FINDINGS — display-affecting findings: 0 [LOCALIZE-ROWS row 14, source LOCALIZE-A]
- T5 (translation text): FINDINGS — the source reports judge T4/T5 jointly; one verdict word covers both [LOCALIZE-ROWS row 14]
- FIX5 re-judgement: none — no OPEN items at the ledger determination [GOSIGN2-LEDGER (b) row 13]
- Computed against: canonical commit 358955eb4013dac2399c414ba8ec2a6e416a3c11; candidate file pages/theme:foxtrot-jp.txt sha256:91b5b57ec3b0742815917d3e267f440c8454c93c70e5f35acaab5e714a401272; record: GOSIGN2-LEDGER.md + GOSIGN2-LEDGER-SUPPLEMENT.md as of the FIX5 head 435a6bb
<!-- END GENERATED VERDICT STAMP -->

Status: complete — skeleton by classify_hunks.py 0.1.0; every SLOT in the skeleton is resolved in the sections below and the Appendix.
Candidate: review/foxtrot-jp/candidate.txt (sha256 206d7c2d2159e447306673338542bf17a7a6bb3135ced3f59c54aae9c26c98ad)
Original: theme:foxtrot — scp-wiki, revision 171 (sha256 04407aa0cfb8cf27b6066cd994b7b1ae7d2c867f187aacbd90639423f7c78b5d)
Classifier: classify_hunks.py 0.1.0; signature table 2026-11-17.1; patterns commit 9c5e9079afb01d30cb9fc4ef9d714e5591eb2ffa

## Status

| | |
|---|---|
| Verdict | **PASS** — passed at the ledger determination with no OPEN items (GOSIGN2-LEDGER (b) row 13); one of the 286 of 286 pass-eligible themes. The generated stamp above also reads PASS |
| Kind | **K6 production-counterpart row.** The candidate is not a fresh port: it is SCP-JP's production page `theme:foxtrot` (translated by iti119 in 2022, against EN revision 148) carried into the campaign, plus campaign edits. The actual migration deliverable against the production page is the 24-line `pages/phase17-diff-foxtrot-jp.txt`. Read this package's diff through that fact (section 0) |
| Wave edits | Three campaign waves edited the file: the gosign2 T1 fixes (b816e10), FIX-CREDIT-C (5c32672), and FIX3-A2 (a0038b8, four items). Each is verified in the Per-theme record |
| Standing items | **DISPOSITIONED** — T1 baseline http×30 (class (ii), scheme rewrite at posting), foreign-include×2 (KB-54 named exception: the author-label-source pair), hotlink×1 (FIXED by FIX3-A2); the render row's coverage caveat and KB-33/KB-34 overflow items; T4's P1 (posting-procedure class), P4/P5 (class (ii) / KB-58 as recorded, with the rsms.me substance since FIXED) |
| Go-sign basis | COMPLETION-REPORT.md §10 (go-sign issued; 81 FIXED / 26 DISPOSITIONED / 0 OPEN across the sweep) |
| Named exception | None for this theme (the sweep's single named exception is theme:amethyst-v2, which has no candidate) |

## Provenance

| | Original | Candidate |
|---|---|---|
| Page | theme:foxtrot | theme:foxtrot-jp |
| Wiki | scp-wiki.wikidot.com | SCP-JP Sigma-10 candidate (canonical repo); its substance is the production page theme:foxtrot on scp-jp |
| Reference revisions | First translation 148; re-translation 171 (credit-only, Phase 22), both recorded in the candidate's credit block (cand L27-28). This package's mirror is revision 171 | — |
| Source of this copy | Campaign mirror store, FETCH-REGEN class (fetched 2026-11-17; hash-verified against review/sources.tsv) | Canonical file `pages/theme:foxtrot-jp.txt`, imported with the canonical sources (d727e92) from the production page; campaign edits in 9e83ff5, 69c5894, 8dcac74, d2a9dc0, b816e10, 5c32672, a0038b8 |
| Third source | The production page itself, held in the repo as `pages-existing/existing:theme-foxtrot.txt` (4,247 lines). The candidate differs from it by 169 diff lines: the campaign edits below | — |
| Lines | 3,767 (generator count, diff.md) | 4,285 (generator count, diff.md) |
| SHA-256 | 04407aa0cfb8cf27b6066cd994b7b1ae7d2c867f187aacbd90639423f7c78b5d | 206d7c2d2159e447306673338542bf17a7a6bb3135ced3f59c54aae9c26c98ad |

Provenance route: **adopted from the production JP counterpart (R4)**, then updated by campaign waves. The production page was translated by iti119 in 2022 against EN revision 148. Phase 17 recorded that reference; Phase 22 then faced the upstream 148→171 delta, which was display-affecting (font defaults, body composition, include conditions), judged that it conflicted with the JP localization's structure, and decided NO-FOLLOW: no content changes, credit bumped to 改訳時参照リビジョン： 171 only. That decision is the deliverable `pages/phase17-diff-foxtrot-jp.txt`, and it is why this package's original-vs-candidate diff is large (Tier 2: +830/−312, 1,142 changed lines in 205 blocks): most of the diff is the production page's independent localization history plus the upstream drift Phase 22 deliberately did not follow, not campaign porting churn. sources.tsv records the production drift against the candidate as 不一致（色の差） (a colour difference).

Wave history: canonical import (d727e92); exhibit escaping and gallery cleanup (69c5894); whitespace normalization and the paragraph-colour item (9e83ff5); Phase 17 reference recording (8dcac74); Phase 22 NO-FOLLOW with the credit bump (d2a9dc0); the gosign2 T1 fixes (b816e10: colon encodings, two credit fields); FIX-CREDIT-C (5c32672: the translator pair); FIX3-A2 (a0038b8: the font-delivery repair, the dropped-font restore, the duplicate-English removal, the docs-vs-CSS corrections). The Per-theme record verifies the three gosign2 waves hunk by hunk.

## Summary

Foxtrot is Liryn's Basalt-based theme, and on SCP-JP it is not a campaign invention: a production translation has served as theme:foxtrot since 2022. The campaign's task for this row was migration, not translation — bring the production page into the Sigma-10 candidate set, fix what the check waves found, and decide the upstream drift. The drift decision (Phase 22, NO-FOLLOW) is the row's most consequential act and it is recorded in a 24-line deliverable, not in this file's bytes: the candidate keeps the rev148-era composition the JP branch has localized around, and says so in its credit block. What the gosign2 waves then fixed is concrete and verifiable: a non-exception font CDN (rsms.me) replaced, a font the CSS named but nothing loaded (IBM Plex Sans) restored from the archived rev148 import, two places where untranslated English prose survived beside its own translation, three documentation defaults that contradicted the shipped CSS, two unencoded colons, and a credit block completed to the §3 field set. A reviewer should look hardest at the Phase 22 decision's record (does the NO-FOLLOW ground hold?) and at the credit block's one residue (the production page's 著者 line standing beside the campaign's 著作権者 line, section 1).

## Classification

Auto-classification by review/classify_hunks.py (signature table 2026-11-17.1): 205 change blocks — 136 specific (66.3%), 48 heuristic, 21 residue, 0 skipped. The residue and much of the heuristic mass are the production adoption's shape (documentation-entry translations and the candidate-only JP localization layer), adjudicated in the Appendix. Pattern citations below name the KB entry; the patterns/ tree state cited throughout is commit 9c5e9079afb01d30cb9fc4ef9d714e5591eb2ffa. Labels are sets per block; the sections below were written from classification.json's label sets, not from the skeleton's per-section lists.

| Label | Blocks |
|---|---|
| TRANSLATION-ANCHORED | 54 |
| TRANS-UNANCHORED | 51 |
| WS-ONLY | 42 |
| ASSET-REHOST | 16 |
| INCLUDE-REPOINT | 15 |
| ESCAPED-INCLUDE | 14 |
| HEADERVAR | 12 |
| FONT-IMPORT | 11 |
| IFTAGS | 5 |
| EXHIBIT-RESTRUCTURE | 3 |
| T7-CREDIT-CSS | 3 |
| LINK-REPOINT | 3 |
| BARE-RATE-DEL | 1 |
| COMMENT-TEXT | 1 |
| CREDIT-PREVIEW | 1 |
| CREDIT-PROSE | 1 |
| CSS-BODY | 1 |
| JPFONT-LOAD | 1 |
| TASL-FIELDS | 1 |

Topology (classification.json): the original delivers through 17 module-css blocks in its tail (orig L2228-3765); the candidate carries 39 module-css components — a head module (cand L33-62, the credit-module furniture CSS), the main inline block (cand L603 onward, `show="true"`), and a tail series (cand L2409-4285) mirroring the original's tail structure, plus small conditional blocks. The candidate's extra components are the production page's own structure and its JP localization layer (section 8), not campaign additions.

## 0. Header / provenance

- What: the package diffs the mirror of `theme:foxtrot` at revision 171 against the canonical candidate `pages/theme:foxtrot-jp.txt`. Because the candidate descends from the production JP page (translated against revision 148) and Phase 22 declined the 148→171 upstream delta, the diff measures three things at once: the production localization, the declined upstream drift, and the campaign's edits. The campaign's edits alone are the 169-line difference between the candidate and `pages-existing/existing:theme-foxtrot.txt`.
- Why: the mirror is the re-translation reference revision the credit block names; provenance for every row lives in review/sources.tsv, and this package's original.txt hash equals that row's value. The K6 shape (a production counterpart as a third source) is the SPECIAL-ROWS scout's K6 treatment.
- Verify: `sha256sum review/foxtrot-jp/original.txt` against review/sources.tsv; `cmp review/foxtrot-jp/candidate.txt pages/theme:foxtrot-jp.txt`; `diff pages-existing/existing:theme-foxtrot.txt pages/theme:foxtrot-jp.txt | grep -c "^[<>]"` returns 169.
- Disposition: PASS at the ledger determination (GOSIGN2-LEDGER (b) row 13), stamp PASS.

## 1. Credit and attribution

- What: CREDIT-PREVIEW / TASL-FIELDS / CREDIT-PROSE (B-credit blocks): the candidate's credit block (cand L17-30) is the production page's own block, completed by the campaign. It now carries the full §3 set: タイトル Foxtrotテーマ (L19), 翻訳責任者 iti119 (L20), 翻訳年 2022 (L21), 原題 as a link (L23), 著作権者 Liryn (L24), 作成年 2022 (L25), 初訳時参照リビジョン： 148 (L27), 改訳時参照リビジョン： 171 (L28), 元記事リンク with the 「ソース」 text (L29). One residue stands: the production page's original field `**著者:** Liryn` (cand L22) remains beside the campaign-added `**著作権者:** Liryn` (L24). Both name the same person; the duplication is a cosmetic residue of completing the field set without renaming the production line, recorded here rather than silently tidied.
- Why: P3 / ruling 3. The translator value is the production translator's human name, kept deliberately: the FIX-CREDIT-D census records that the production counterpart's creator is iti119 (2022), so the population's AI normalization does not apply to an adopted human translation. The two added fields have distinct wave homes: 著作権者 and 元記事リンク arrived in b816e10 (the T1 fix wave, which found them missing), and the 翻訳責任者/翻訳年 pair in 5c32672 (FIX-CREDIT-C, "complete translator pair in rows 1-22 credit blocks").
- Verify: read cand L17-30; every §3 field is present exactly once, except the author fact, which appears under both its production name （著者） and the standard name （著作権者）.
- Disposition: P3 FIXED per the ledger (c3) ("credit fields FIXED (credit waves; checker-verified)"), verified hunk by hunk in the Per-theme record. The 著者 duplication is this package's noted residue, not a ledger item.

## 2. Includes and components

- What: INCLUDE-REPOINT ×15 and ESCAPED-INCLUDE ×14 (the documentation's escaped include exhibits, repointed with the body). The head carries four same-site component includes (cand L1-4: toggle-sidebar, acs-animation, fade-in, betterfootnotes), the production page's own furniture set. One foreign include stands: `[[include :scp-wiki:component:author-label-source …]]` at cand L64 (start) and L70 (end), the EN component that renders the author bio block, with EN links inside it.
- Why: the author-label-source pair is a KB-54 named exception: no JP equivalent component exists (NOTFOUND-probed in the FIX2-INCLUDE work), so the include cannot be repointed, only ported (a separate staff call) or dropped. EN itself dropped this include in revision 171; the candidate keeps it because Phase 22's NO-FOLLOW kept the production composition, bio block included. The two facts belong together: the exception is a consequence of the adoption decision, not an oversight.
- Verify: `grep -n "author-label-source" review/foxtrot-jp/candidate.txt` — exactly the start/end pair; `grep -n "scp-wiki:" review/foxtrot-jp/candidate.txt` — no other foreign include outside exhibits.
- Disposition: T1 foreign-include×2 DISPOSITIONED under the KB-54 named exception (register (c1) and the ledger's exception list, which names foxtrot's two lines explicitly). T4 P1 DISPOSITIONED (posting-procedure convention class).

## 3. Delivery and code loading

- What: the theme's CSS is self-contained in inline `[[module CSS]]` blocks; there is no local--code self-delivery and no `[[code]]` block in the candidate (the original rev171 likewise delivers by module-css, from its tail). The candidate's delivery map: the head module (cand L33-62, credit-module furniture under a "SET INFOSTYLE" comment), the main block at cand L603 (`show="true"`, carrying the variables and core rules), and the tail series of conditional and variant blocks (cand L2409-4285) that mirrors the original's 17-block tail. The candidate additionally carries a JP localization CSS layer with no original counterpart at its position (the "LOCALIZATION FOR JP BRANCH" section, cand L2286 onward, T7-CREDIT-CSS): the production page's own rules adapting the credit module and furniture to the JP branch.
- Why: Basalt-based themes in the production JP form deliver inline; the campaign does not re-form an adopted page's delivery. The JP localization layer is production content, and its presence is exactly what the Phase 22 NO-FOLLOW protected: re-basing the candidate on rev171's structure would have discarded it.
- Verify: `grep -c "\[\[code" review/foxtrot-jp/candidate.txt` is 0; `grep -n "LOCALIZATION FOR JP BRANCH" review/foxtrot-jp/candidate.txt` finds the layer's header at cand L2286.
- Disposition: no delivery item stands against this theme beyond the font-delivery items of section 4 and the scheme class of section 11.

## 4. Fonts and assets

- What: FONT-IMPORT ×11, HEADERVAR ×12, ASSET-REHOST ×16, JPFONT-LOAD ×1. The candidate's font imports are all Google Fonts (cand L620-641 region: Montserrat, Lexend, JetBrains Mono, Fira Code, Sofia Sans, IBM Plex Sans, Inter, Figtree, M PLUS 1p, Noto Sans JP), where the original rev171 loads from fonts.bunny.net plus an scp-wiki local--files inter.css. Two of the candidate's imports are FIX3-A2's work, verified in the Per-theme record: the rsms.me Inter stylesheet (a non-exception third-party font CDN) replaced by the Google Fonts Inter variable import (cand L632), and the IBM Plex Sans import restored at cand L630 — `--ui-font` named 'IBM Plex Sans' with no `@import` anywhere, so UI text fell back; the restored import's exact family and weights were taken from the archived EN rev148 import preserved in the Phase 22 diff record, not invented. The stacks: `--head-font: 'Sans Normalcy', 'M PLUS 1p'` (cand L654), `--ui-font: 'IBM Plex Sans', 'Noto Sans JP'` (cand L655), `--mono-font: 'JetBrains Mono', 'Fira Code', monospace` (cand L657), `--page-font: 'Inter', 'verdana', var(--yu-gothic)` (cand L658). One named-but-unloaded family stands on both sides: 'Sans Normalcy' is loaded by no `@import` or `@font-face` in the candidate, and the original rev171 does not load it either (orig L589 names it identically) — it is an original-state property of the theme (a Basalt-ecosystem display face), and the candidate's stack pairs it with the loaded M PLUS 1p for Japanese. Assets: the production page's images sit on SCP-JP storage (scp-jp-storage.wdfiles.com, 29 references, e.g. the fxtrt.png credit image at cand L10); they were already JP-hosted by the production page, so ASSET-REHOST fires against the original's EN hosts, not against a campaign move.
- Why: P4/P5 (KB-17: font delivery must use exception-list hosts; KB-16: a named family must be loaded or the stack is a false record). The rsms.me line was the T1 baseline's single hotlink error; the IBM Plex Sans gap was the localize lane's pattern-7 finding.
- Verify: `grep -n "@import" review/foxtrot-jp/candidate.txt` — every import is fonts.googleapis.com. `grep -n "rsms.me" review/foxtrot-jp/candidate.txt` — no hits. `grep -n "IBM Plex Sans" review/foxtrot-jp/candidate.txt` — the import and the stack both present.
- Disposition: the hotlink is FIXED (FIX3-A2's table: foxtrot hotlink 1 → 0; T1 errors 33 → 32). The ledger (c3) records P4/P5 as DISPOSITIONED (delivery class (ii) / KB-58), written against the delivery classes; the rsms.me substance inside P4 was fixed by the wave, and this package records both the disposition line and the fix so neither is lost.

## 5. Header, sidebar, site furniture

- What: HEADERVAR ×12 is the variable documentation and definitions mass (header fonts, page font size, gradient variables), most of it production translation. The FIX3-A2 docs corrections live here: three documentation defaults that contradicted the shipped CSS were corrected in the docs, not the CSS — `--head-font` documented as Lexend, corrected to Sans Normalcy (cand L409 against CSS cand L654); `--ui-font` documented as Sofia Sans, corrected to IBM Plex Sans (cand L415 against L655); `--page-font-size` documented as 0.84rem, corrected to 1rem (cand L424 against L659).
- Why: a documentation default that contradicts the shipped value is a false record of the theme's behaviour (the same shape the main chat's ashes ruling names). Correcting the docs to the CSS preserves the Phase 22 composition; changing the CSS to match stale docs would have smuggled the declined rev171 values in through the back door — note the corrected values are the production composition's, and rev171's own defaults differ again.
- Verify: `sed -n '409p;415p;424p' review/foxtrot-jp/candidate.txt` against `sed -n '654p;655p;659p'`.
- Disposition: FIXED by FIX3-A2 item 4 (report §"Row 13", item 4), under the ledger's T5-wording line for this theme.

## 6. Text translation

- What: TRANSLATION-ANCHORED ×54 and TRANS-UNANCHORED ×51: the documentation body is the production translation (です・ます）, carried. FIX3-A2 removed the two places where the production page carried untranslated English beside its own translation: the `--darkmode-gradient-bottom` documentation row, which had both the EN line and the JP line, merged to the JP line only (cand L386); and the Collapsibles paragraph, whose EN bullet was deleted leaving the JP bullet (cand L547). The T1 fix wave's colon encodings also live in this mass's neighbourhood (the image-block name at cand L10 and a CSS url() at the nav:side background: `file%3A…` and `nav%3Aside` forms).
- Why: P10/T5 (KB-18): duplicated untranslated prose is reader-visible English in a JP deliverable, and the duplicated variable row additionally read as two different variables. The colon encodings are the checker's unencoded-colon class: a bare colon in a local--files path breaks the URL form the checker requires.
- Verify: `grep -n "The color of the bottom\|heavily styled" review/foxtrot-jp/candidate.txt` — no hits; both EN duplicates are gone.
- Disposition: the duplicates and defaults are FIXED by FIX3-A2 items 3-4; the ledger's cross-cutting T5 line records pattern-10/T5 wording as FIXED for foxtrot by name. The colon encodings are FIXED; the ledger's (c1) colon line names foxtrot among the 15 themes FIX-MECH repaired — the bytes for this file rode in b816e10 (the T1 fix commit), and the Per-theme record notes the attribution.

## 7. Links

- What: LINK-REPOINT ×3 and the prose link mass: the production page's links are JP-side (storage and scp-jp references) except the author-label-source component's internal EN links (inside the excepted include, section 2) and reference links to the EN original in the credit block (required) and documentation.
- Why / Verify: `grep -n "scp-wiki.wikidot.com" review/foxtrot-jp/candidate.txt` — the hits are the credit source links, the excepted component's parameters, and documentation references.
- Disposition: no P11 item stands against this theme in the ledger (c3).

## 8. Structure

- What: EXHIBIT-RESTRUCTURE ×3 and the topology gap of the Classification section: the candidate's 39 module-css components against the original's 17. Adjudicated by provenance, not by shape: the candidate's structure is the production page's structure (head furniture module, main inline block, JP localization layer, tail variant series), which reorganized the theme long before the campaign. The one campaign-era structural content is the JP localization layer's credit-module rules (T7-CREDIT-CSS ×3: the head "SET INFOSTYLE" module at cand L33-62 and the LOCALIZATION FOR JP BRANCH rules at cand L2286 onward), which adapt the credit module's geometry to the JP branch and have no original counterpart because the original's credit story is a different module.
- Why: R3's ground-stating rule, with the K6 ground: for an adopted production page, structural difference from the EN original is the expected state, and the deciding evidence is the third source (the production page), against which the candidate's structure matches except for the 169 lines of campaign edits.
- Verify: `diff pages-existing/existing:theme-foxtrot.txt pages/theme:foxtrot-jp.txt` — the structural identity with the production page, modulo the campaign edits.
- Disposition: nothing to disposition; no exhibit or module was dropped by the campaign. (The pre-campaign gallery-image drop in 69c5894 removed unshipped gallery images from the exhibits, recorded in that commit.)

## 9. Formatting only

- What: WS-ONLY ×42 — the largest formatting mass in this batch, and it has a provenance: the production page's whitespace conventions differ from the EN original's throughout, and commit 9e83ff5 (whitespace normalization; foxtrot paragraph colour) normalized the candidate's own whitespace once more. Re-indentation pairs are inside this count.
- Why / Verify / Disposition: whitespace-only; the classifier's count is in classification.json. Nothing to disposition.

## 10. Porter annotations

- What: the candidate carries production-era and campaign-era comment text (COMMENT-TEXT ×1 as a primary; the "SET INFOSTYLE" and "LOCALIZATION FOR JP BRANCH" CSS comments are the load-bearing ones). They are the production page's own section markers, not campaign porter annotations; the campaign added no annotation block to this file.
- Verify: `grep -n "LOCALIZATION FOR JP BRANCH\|SET INFOSTYLE" review/foxtrot-jp/candidate.txt` — cand L34 and L2286.
- Disposition: retained as the page's own documentation; not a defect.

## 11. Dispositions and exceptions

- T1 http×30: DISPOSITIONED, class (ii) — scheme rewrite at posting (register (c1) http preamble). The items are the production page's `http://` URLs on SCP-JP's own hosts (scp-jp-storage.wdfiles.com, scp-jp.wikidot.com local--files); a raw grep counts 34 `http://` occurrences in the candidate including exhibits. The fetched-http CSS subset (KB-42) is recorded in the register.
- T1 foreign-include×2: DISPOSITIONED under the KB-54 named exception (section 2); the ledger's exception list names foxtrot's two author-label-source lines explicitly.
- T1 hotlink×1: FIXED by FIX3-A2 (section 4). T1 unencoded-colon items: FIXED (section 6).
- Render items (RENDER-B row 13): the T2 walk's exit 2 on both pages (the chromium-320 open-menu click intercepted by login-status, deterministic) is a coverage caveat, recorded as such with no machine verdict; the T3 items (the 320px ≡/sign-in overlap; SP overflow 729/754px) DISPOSITIONED under KB-33/KB-34.
- T4: P1 DISPOSITIONED (posting-procedure convention class); P3 FIXED (credit waves, section 1); P4 DISPOSITIONED (delivery class (ii)) with the rsms.me substance FIXED (section 4); P5 DISPOSITIONED (class (ii) / KB-58).

## 12. Verification

- T1 (source check): baseline 2026-11-16: exit 1, 33 errors / 6 warns / 3 infos (http×30, foreign-include×2, hotlink×1); after FIX3-A2: 32 errors (hotlink 1 → 0), the rest in the dispositioned classes above. Re-runnable with the staff checker's check_source.py against candidate.txt.
- T2/T3 (render): RENDER-B row 13 (RENDER-ROWS-1): FINDINGS with the coverage caveat recorded in section 11.
- T4 follow-up (reference-revision currency): `diff-foxtrot.txt` (LOCALIZE-A lane): rev171 → rev171, no changes; upstream latest is still revision 171. The 148→171 delta itself was reviewed and NO-FOLLOW decided in Phase 22 (the lane's follow-up section enumerates its display-affecting parts).
- Package checks: `python3 review/build_review.py --check` passes for this package; candidate.txt is byte-identical to the canonical file; original.txt's SHA-256 equals the sources.tsv row.

## Per-theme record

1. **b816e10 (gosign2 T1 fixes, rows 1-44), verified.** The commit's diff for this file: the image-block name's colon encoded (`file:5722815-57-3pfp` → `file%3A5722815-57-3pfp`, cand L10), a CSS background url's colon encoded (`nav:side` → `nav%3Aside`), and two credit fields added （著作権者： Liryn; 元記事リンク）. The ledger's colon line attributes the repair class to FIX-MECH's 15-theme set; for this file the bytes rode in the T1 fix commit. The wave's other named work (furniture rows) does not appear in this file's diff.
2. **5c32672 (FIX-CREDIT-C), verified.** Two lines added: 翻訳責任者： iti119 and 翻訳年： 2022 — the translator pair the localize lane found missing. The value is the production translator's name, kept human through the later FIX-CREDIT-D normalization on the census ground recorded in section 1.
3. **a0038b8 (FIX3-A2, row 13), verified item by item.** (1) rsms.me Inter → Google Fonts Inter variable import (cand L632). (2) IBM Plex Sans import restored (cand L630), family/weights from the archived rev148 import in the Phase 22 diff record. (3) The two duplicated-English removals (cand L386, L547). (4) The three docs-vs-CSS default corrections (cand L409, L415, L424), docs changed, CSS untouched. The report's four items are all in the bytes, and the bytes contain no fifth edit.
4. **The Phase 22 decision is the row's real deliverable.** The 24-line `pages/phase17-diff-foxtrot-jp.txt` records it: upstream's 148→171 revision was a large, display-affecting overhaul; it conflicted with the JP localization's structure; the decision was no content follow, credit bump only. Every later wave worked inside that decision (FIX3-A2 item 4 states it explicitly: "the Phase 22 NO-FOLLOW composition remains intact"). A reviewer who wants to challenge this row should challenge that decision's ground, which the deliverable and the LOCALIZE-A follow-up section together make derivable.
5. **The 著者/著作権者 duplication** (section 1) is the credit completion's residue: the wave added the standard field rather than renaming the production field. Both name Liryn; nothing is misattributed.

## Change set outside the two diffed files

The migration deliverable `pages/phase17-diff-foxtrot-jp.txt` (the Phase 22 decision record and the production-page delta) is this row's defining companion file. One companion candidate: `pages/theme-decoration-sample-foxtrot-jp.txt`. The production page itself is held at `pages-existing/existing:theme-foxtrot.txt` as the third source. The EN-named `pages/theme-decoration-sample-foxtrot.txt` is a composition member of the display-check wikis.

## Multi-wave provenance

- Production origin: theme:foxtrot on SCP-JP, translated by iti119 (2022) from EN revision 148.
- Campaign intake: canonical sources import (d727e92); exhibit escaping and gallery cleanup (69c5894); whitespace normalization (9e83ff5); Phase 17 reference recording (8dcac74); Phase 22 drift decision, NO-FOLLOW with credit bump to rev171 (d2a9dc0).
- Check waves: T1 baseline (T1-ROWS row 13); render walk RENDER-B (RENDER-ROWS-1, row 13); localize walk LOCALIZE-A (LOCALIZE-ROWS row 14 in the lane's numbering; ledger row 13), which raised P1, P3, P4, P5 and the T5 items; the rev171 follow-up diff (no changes).
- Fix waves: gosign2 T1 fixes (b816e10); FIX-CREDIT-C (5c32672); FIX3-A2 (a0038b8).
- Ledger determination: GOSIGN2-LEDGER (b) row 13, PASS, no section (e) items; go-sign COMPLETION-REPORT.md §10.

## Appendix — residue and heuristic blocks

The 21 residue blocks resolve by shape, in four groups. (1) Seventeen 2-line blocks in the documentation region (B28, B34, B53, B55, B56, B61, B62, B72, B73, B80, B81, B83, B125, B126, B131, B132 and their kin): the variable-documentation entries, where each `{{--var}}` row's description line pairs against its production translation without the anchor majority the classifier wants; all are section-6 translation, verified against the production page as third source. (2) B107 (orig L555 → cand L612-614): the font-import region, where the production page's Google Fonts set replaces the original's bunny.net set; section 4. (3) B117, B118 (orig L588-592 → cand L653-657): the `--head-font` / `--ui-font` / `--page-font-size` definitions themselves, the FIX3-A2 docs-correction counterparts; section 5. (4) B151 (orig L2216 → cand L2283-2391): the candidate-only JP localization CSS layer (section 3/8) — a whole production-added section has no original lines to anchor to, which is the residue shape an R4 adoption produces. B159 is a tail module boundary of the same adoption. The 48 heuristic blocks are the translation, whitespace and asset mass of sections 6, 9 and 4. No new signature is proposed from this theme; the R4-adoption residue shape (a candidate-only localization layer) is recorded here as a shape the classifier will meet again on every production-counterpart row.

## License and attribution

- **Title:** Foxtrot Theme
- **Author:** Liryn
- **Source:** https://scp-wiki.wikidot.com/theme:foxtrot — revision 171 (revision date 2026-03-26 17:29:48)
- **License:** Creative Commons Attribution-ShareAlike 3.0 (CC BY-SA 3.0) — license deed: https://creativecommons.org/licenses/by-sa/3.0/
- **Adaptation:** This package holds a Sigma-10 migration port of the work; changes were made. See "Summary" and "Standing sections" in this README for what changed and why. Translator: iti119 — a human translator credited by the live JP page and retained as the package records it (campaign-rule exception); where the campaign translated, the translator is AI.
