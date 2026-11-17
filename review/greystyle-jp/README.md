# Review package — theme:greystyle-jp (EN → JP port)

<!-- BEGIN GENERATED VERDICT STAMP — do not hand-edit; regenerate with review/build_review.py -->
## Verdict stamp
- Theme: theme:greystyle-jp — origin EN, population #95 [GOSIGN2-LEDGER (b) row 95]
- Overall: STALE — candidate file changed since the verdict was computed (verdict against 435a6bb-era content, file sha256 now 03332d7dc7ae877fa128c631a8ff7cf8dce23cfd19f08533983bbc7edaa730ec); verdict not carried over, re-judgement required
> verdicts below describe the pre-change file
- T1 (source check): FINDINGS (classified) — baseline 2026-11-16: exit 1, 21 errors / 3 warns / 3 infos (hotlink×21); standing classes dispositioned in register c1 [T1-ROWS row 105; GOSIGN2-LEDGER (b) row 95]
- T2/T3 (render, combined verdict): FINDINGS — [combined T2/T3] report `FINDINGS` — page-overflow at 1366/320/375 both engines; sample 1569px@1366 + 789px@768; WebKit CC "S"; license-box include error = test-wiki resolution, not defect. [RENDER-ROWS-1 (RENDER-S2-B)]
- Engine coverage: full matrix as run by the lane; coverage not separately caveated in the row [RENDER-ROWS-1 row]
- Credit modal: no credit-modal line in this theme's row; no sample credit-modal error recorded [RENDER-ROWS-1 (RENDER-S2-B)]
- T4 (localize patterns + follow-up): FINDINGS — display-affecting findings: 2 [LOCALIZE-ROWS row 95, source LOCALIZE-S2-B]
- T5 (translation text): FINDINGS — the source reports judge T4/T5 jointly; one verdict word covers both [LOCALIZE-ROWS row 95]
- FIX5 re-judgement: none — no OPEN items at the ledger determination [GOSIGN2-LEDGER (b) row 95]
- Computed against: canonical commit 3cf1cd0313fa0d5319895d57a53decc7599630e9; candidate file pages/theme:greystyle-jp.txt sha256:03332d7dc7ae877fa128c631a8ff7cf8dce23cfd19f08533983bbc7edaa730ec; record: GOSIGN2-LEDGER.md + GOSIGN2-LEDGER-SUPPLEMENT.md as of the FIX5 head 435a6bb
<!-- END GENERATED VERDICT STAMP -->

Status: complete — skeleton by classify_hunks.py 0.1.0; every SLOT in the skeleton is resolved in the sections below and the Appendix.
Candidate: review/greystyle-jp/candidate.txt (sha256 34ff4c5ca3758ed944400526242857a05c6ec7b6375995abd36c2e19a26512d0)
Original: theme:greystyle — scp-wiki, revision 14 (sha256 882a7ca0e2e309087d2db07acdea87a21de6bd88e3dc741849c308e00d76caa6)
Classifier: classify_hunks.py 0.1.0; signature table 2026-11-17.1; patterns commit 9c5e9079afb01d30cb9fc4ef9d714e5591eb2ffa

## Status

| | |
|---|---|
| Verdict | **PASS** — passed at the ledger determination with no OPEN items (GOSIGN2-LEDGER (b) row 95); one of the 286 of 286 pass-eligible themes |
| Blocking items at ledger time | None — no section (e) items exist for this theme and the supplement carries no greystyle entries |
| Fixed after the localize check | P7 (Japanese font supplement), landed inside commit f931619 (FIX2-COLON) together with the KB-01 colon encoding; the exhibit copy's duplicate font imports were removed in commit a497307 (FIX4-MECH) |
| Standing items | **DISPOSITIONED** — T1 hotlink×21, class (ii) (ledger (c1)); localize P5 EN-storage logos, class (ii) / KB-58 (ledger (c3)); render findings: page-overflow at 1366/320/375 in both engines and the sample measurements (KB-33/KB-34/KB-37 families), WebKit CC "S" (KB-36) (ledger (c2)) |
| Carried flag (this package) | The original's three variant-parameter delivery modules ({$dark} / {$wide} / {$hide}) were dropped at creation and never recorded; the variant layers survive only as inert code exhibits (Per-theme record, item 1) |
| Go-sign basis | COMPLETION-REPORT.md §10 (go-sign issued; 81 FIXED / 26 DISPOSITIONED / 0 OPEN across the sweep) |

## Provenance

| | Original | Candidate |
|---|---|---|
| Page | theme:greystyle | theme:greystyle-jp |
| Wiki | scp-wiki.wikidot.com | SCP-JP Sigma-10 candidate (canonical repo) |
| Reference revision | 14, as recorded in the candidate's credit block: **初訳時参照リビジョン:** 14 | — |
| Source of this copy | Campaign mirror store `orig-greystyle-rev14.txt` (class COPY, byte-identical; review/sources.tsv) | Canonical file `pages/theme:greystyle-jp.txt`, created in commit a869415 (Stage 2 EN11); later commits f931619 (FIX2-COLON) and a497307 (FIX4-MECH, last content change) |
| Lines / bytes | 2,413 lines / 59,356 bytes | 3,879 lines / 98,944 bytes |
| SHA-256 | 882a7ca0e2e309087d2db07acdea87a21de6bd88e3dc741849c308e00d76caa6 | 34ff4c5ca3758ed944400526242857a05c6ec7b6375995abd36c2e19a26512d0 |

Provenance route: derived from the original at the reference revision (sources.tsv kind: standard; the start-themes.tsv base column reads "standalone"). No production counterpart was adopted: the candidate's CSS body measures 0.99-similar to the original's own code exhibit (classifier topology pass). The localize follow-up records "No unincorporated upstream updates."

## Summary

The original is a Black Highlighter based theme that delivers its stylesheet twice over: the main stylesheet sits in a code exhibit (orig L800–2289) served as the page's own local--code /1 and loaded by a tail module @import, three further fragment exhibits (/2, /3, /4) are loaded by include-parameter modules keyed to {$dark}, {$wide} and {$hide}, and three interwiki frames stack the BHL layers. The candidate inlines the main exhibit into its head `[[module CSS]]` (cand L8–1501), keeps two frames, adds the preview credit block, translates the body, and retains all four code exhibits as documentation. Two later wave commits touch the file: FIX2-COLON (colon encoding, with the P7 font supplement riding inside it) and FIX4-MECH (duplicate @import removal in the exhibit copy). The measured churn against the current (post-repair) candidate is dominated by the inline (diff.md: +2319/−832 in 17 sections / 29 change blocks; GNU-diff 1913 changed lines); the pre-repair figures were +2314/−848 in 18 sections (27 classifier blocks, all specific). The delivery loss flagged in item 1 below has since been repaired: the three variant-parameter modules are back in the candidate (Per-theme record, item 1). The theme passed at the ledger determination with no open items; the T1 hotlink errors are exactly the 21 surviving EN-storage logo URLs across the two CSS copies, dispositioned class (ii).

## Classification

| Label | Blocks |
|---|---|
| WS-ONLY | 13 |
| DELIVERY-MOVE | 10 |
| TRANS-UNANCHORED | 3 |
| EXHIBIT-RESTRUCTURE | 2 |
| IFTAGS | 2 |
| HEADERVAR | 2 |
| SELF-DELIVERY | 2 |
| CONTENT-STRING | 1 |
| CREDIT-PREVIEW | 1 |
| DELIVERY-HOST | 1 |
| INCLUDE-REPOINT | 1 |
| INFO-DEL | 1 |
| JPFONT-LOAD | 1 |
| RESTORATION | 1 |
| T7-CREDIT-CSS | 1 |
| TASL-FIELDS | 1 |
| TRANSLATION-ANCHORED | 1 |

Counts: 27 blocks — 27 specific (100%), 0 heuristic, 0 residue, 0 skipped. Topology: the original's main code exhibit (orig L800–2289) moved to the candidate's module-css (cand L8–1501) at 0.99 similarity, and the fragment-3 exhibit (orig L2348–2369) matched into the same module at 0.60; the candidate-side own-delivery companion body was unavailable to the classifier (its recorded caveat). Labels are sets per block; the per-section lists in the classifier's skeleton show each block once, under its primary label, so this README's sections were written from classification.json's label spans, not from the skeleton's section lists. Two blocks are alignment artefacts of the two-copy file and are resolved in the Appendix (B3, B24).

## Standing sections

### 0. Header and provenance frame

- **What:** The original's head (L1–11) carries a comment naming its fragment pages (fragment:greystyle-0 and fragment:greystyle-1 on scp-wiki), the `[[iftags +theme]]` gate (L7) and a module CSS importing the two BHL layers from nu-scptheme.github.io (L8–11). The candidate's head comment repoints the two fragment URLs to scp-jp.wikidot.com (B1, cand L2–4); the gate is localized and the module at cand L8 opens the inlined delivery (section 3). The fragment pages named in the comment do not exist on the JP wiki and no file in this repo carries them; the comment is documentation only (Per-theme record, item 2).
- **Why:** The header frame is where the original declares its delivery and its fragment structure; P1/P4 rework exactly this frame, and each piece is accounted for in sections 2–3.
- **Verify:** Read original L1–11 against candidate L1–10; block B1 in classification.json.
- **Disposition:** Recorded; the delivery reading is section 3.

### 1. Credit and attribution

- **What:** The original's attribution sits in its info module (orig L30–33: "Greystyle by [[*user Greyve]]" with the author-page link). The candidate replaces it with the preview credit block (cand L1513–1522, spans inside B24): `:scp-jp:credit:start-preview` / `end-preview` carrying all eight ruling-3 fields — title グレイスタイルテーマ, translator AI, translation year 2026, original title "Greystyle", copyright holder Greyve, creation year 2023, reference revision 14, and the source link to the EN page. The author field agrees with the original's own credit (Greyve, in the info block and the exhibit comment header). The info module is deleted in the same rework (INFO-DEL spans orig L29–30 and L32–33, inside B3); its author-page link (orig L32) has no JP counterpart page and does not survive, while a second instance of the same link inside the linkbox exhibit survives as documentation (section 7). The theme's own credit-module CSS (the `.rate-box-with-credit-button` set) is inherited from the original, one set per CSS copy (grep: 2 hits in the original, 4 in the candidate): supplement type T7 by inheritance, not by addition (T7-CREDIT-CSS spans cand L2739–2748 and L3027–3044, in the exhibit copy; the module copy carries the same rules). No license box exists on either side, and none was charged (KB-63 covers dropped boxes; this original never had one). No bare `[[module Rate]]` exists on either side.
- **Why:** P3/T1: the preview credit module is the JP environment's credit form (patterns commit 9c5e9079afb01d30cb9fc4ef9d714e5591eb2ffa). Ruling 3 (RULINGS-20261116, in review/AUTHORITIES/) fixes the eight fields and credits campaign translations to AI.
- **Verify:** Read candidate L1513–1522 against the eight-field list and original L30–33; `grep -c 'rate-box-with-credit-button' original.txt candidate.txt` (2 and 4).
- **Disposition:** Standing (the port's credit form); the localize lane verified the credit form for this theme and charged no credit item.

### 2. Includes and components

- **What:** The candidate's include list (grep): the two interwiki-style frames (cand L1503–1511, section 3), the credit pair (L1513/L1522), the repointed tail components (cand L3870–3873: centered-header-bhl, toggle-sidebar-bhl, betterfootnotes, acs-animation, all `:scp-jp:`, block B26), the escaped usage include (cand L1854), and component includes inside exhibits. Changes against the original: (a) every live component include is repointed `:scp-wiki:` → `:scp-jp:` (INCLUDE-REPOINT); (b) the usage exhibits are reduced to the single line @@[[include theme:greystyle-jp]]@@ (cand L1854) — the original showed two exhibits (orig L365–366), the BHL include and the theme include; the BHL line is dropped from the exhibit because the candidate itself delivers the BHL layer, which is the correct JP usage form; (c) the tail component includes survive in the same order (orig L2382–2385 → cand L3870–3873). No `:scp-wiki:` include remains live in the candidate.
- **Why:** P1: foreign-site includes are repointed to the JP site, and a same-site include takes the bare fullname form. Ruling 4 (port a needed component with the theme) does not engage: all four tail components exist on the JP site.
- **Verify:** `grep -n '\[\[include' original.txt candidate.txt` and compare the two lists.
- **Disposition:** Standing; no include in the candidate points at an EN-wiki page.

### 3. Delivery and code loading

- **What:** The original loads its CSS through five channels: the head module's two BHL @imports (orig L8–11); three interwiki frames (priority=1 the BHL normalize layer; priority=2 theme= the black-highlighter layer, its URL carrying the original's own typo `black-highlighter.mprin.css`; priority=3 theme= the page's own /1 on scp-wiki.wdfiles.com, span orig L24–25 inside B3); a tail module @importing its own /1 unconditionally (orig L2387–2390); and three tail modules gated by include parameters, `[!-- {$dark}-]` → /2, `[!-- {$wide}-]` → /3, `[!-- {$hide}-]` → /4 (orig L2392–2406). The candidate delivers through two channels: the head module CSS (cand L8–1501), which repoints the BHL @imports to scp-jp.github.io and then carries the main exhibit's body inline (topology: code-css → module-css at 0.99), and two frames (cand L1503–1511: priority=1 normalize, priority=2 black-highlighter.min.css on the JP host — the original's `mprin` typo corrected in the repoint, already in the creation commit). The priority=3 frame is deleted, consistently with the inline. The unconditional tail @import is likewise deleted, consistently. The three parameter modules are also deleted (B27: SELF-DELIVERY spans orig L2387–2388, L2392–2393, L2398–2399, L2404–2405, candidate side empty) — and that deletion is NOT consistent with the inline, because the parameters have no replacement channel: the /2, /3 and /4 layers survive only as inert code exhibits (cand L3780–3835, L3837–3857, L3859–3864), nothing loads them, and the candidate's documentation nowhere mentions {$dark}, {$wide} or {$hide} (grep: no hits in the candidate; the creation commit a869415 already contains none). This is the package's carried flag (Per-theme record, item 1). The final iftags ListPages fragment module is retained verbatim (orig L2407–2409 → cand L3875–3879).
- **Why:** P4/T9: deliveries are served from JP hosts in this environment, and inlining the main layer removes the candidate's runtime dependence on the EN wiki's code page. The variant parameters are a documented mechanism of the original (its exhibits are titled as the dark/wide/hide layers); a mechanism whose definitions are absent is a delivery loss under the campaign's delivery-topology rule, whatever the ledger recorded.
- **Verify:** Read original L2387–2409 against candidate L3870–3879; `grep -n '{\$dark}\|{\$wide}\|{\$hide}' candidate.txt` (absent) against the same grep on original.txt (three gated modules); block B27 in classification.json.
- **Disposition:** The main-layer inline and the frame restructure are standing. The parameter-module drop is flagged, not dispositioned: no register charges it, no register dispositions it, and the theme's ledger PASS was determined without it (Per-theme record, item 1).

### 4. Fonts and assets

- **What:** Font changes, by commit. At creation: the font @imports of the exhibit (Josefin Sans, Oxygen, Fira Code from Google Fonts) carried into the module copy. In f931619 (FIX2-COLON): a Noto Sans JP @import added in both CSS copies and 'Noto Sans JP' inserted into the --body-font stack in both copies (label JPFONT-LOAD) — the P7 supplement, riding inside the colon commit (Per-theme record, item 3). In a497307 (FIX4-MECH): the exhibit copy's four font @import lines (Josefin Sans, Oxygen, Fira Code, Noto Sans JP) removed as duplicates (KB-65); the live module copy keeps its imports (cand L42–45), so the retained "Show code" exhibit now differs from the delivered CSS at the font-import block. Assets: the theme's logo images are `local--files` URLs of the EN theme page (theme%3Agreystyle paths on scp-wiki.wikidot.com) in both copies — exactly 21 candidate lines, which are the T1 checker's 21 hotlink errors (0 wdfiles lines). The BHL logo images in the body are repointed to scp-jp.github.io/Black-Highlighter/img/black-highlighter-logo.svg. The mode-changer links in the body are repointed to /theme:greystyle-jp/offset/N and translated.
- **Why:** P7/T5: the theme's stacks had no Japanese-capable font, so Japanese text fell back to an OS-dependent generic (the localize lane's item (b), display-affecting). KB-01 (FIX2-COLON's named scope): unencoded colons in local--files/local--code URLs break under the JP host's URL handling, so `theme:greystyle` became `theme%3Agreystyle` in every asset URL. KB-65: a duplicated @import inside one file is removed from the non-delivering copy. P5/KB-58: re-hosting the EN-storage logos is a posting-procedure act, class (ii), so the candidate keeps the original-state hosts.
- **Verify:** `grep -n 'Noto Sans JP' candidate.txt` (import + stack lines in both copies); `git show f931619 -- pages/theme:greystyle-jp.txt` (26 insertions / 24 deletions, 14 hunks, both copies); `git show a497307 -- pages/theme:greystyle-jp.txt` (one hunk, @@ -2320,10 +2320,6 @@).
- **Disposition:** P7 FIXED (ledger (c3), recorded there as "font wave"; the bytes sit in FIX2-COLON, see Multi-wave provenance). Assets DISPOSITIONED (ledger (c3): P5, class (ii) / KB-58; ledger (c1): the hotlink class is (ii)).

### 5. Header, sidebar, site furniture

- **What:** The header variables are carried verbatim in both copies: --header-title "SCP FOUNDATION" and --header-subtitle "SECURE, CONTAIN, PROTECT" (orig L933–935 ↔ cand L145–146 in the module copy and cand L2423 in the exhibit copy). The classifier's HEADERVAR labels fire on the --logo-image lines (B6: orig L932–933 → cand L144–145; B24 span cand L2421–2424), whose value is an EN-storage logo URL (section 4), not on the title strings, which matched equal. The sidebar and furniture rules are byte-preserved inside the moved body. The three memo-header display strings the localize lane noted in English are an observation item (staff call), not a charged defect.
- **Why:** P9 was not charged for this theme; ruling 2 (2026-11-16) places header and title language outside migration correctness in any case (KB-57, patterns 9c5e907).
- **Verify:** `grep -n 'header-title\|header-subtitle' candidate.txt` (four hits, two per copy, values as above).
- **Disposition:** Standing; no header item was charged in any register.

### 6. Text translation

- **What:** The body prose, the usage text, the mode-changer labels and the exhibit headings are translated (TRANSLATION-ANCHORED 1 block, TRANS-UNANCHORED 3 blocks, the unanchored mass being prose and CSS comment translation). The interview-transcript exhibit is translated in place; its CSS `content:` strings are the theme's own transcript labels and are carried as the theme defines them (CONTENT-STRING spans, 13 firings across both copies inside B24, e.g. cand L1404–1405 and L2327–2328). In-CSS comment text stays in English (residue class R1, porter-visible only). One correction of the original's own text happened at creation, in the body copy of the stylesheet: orig L397 `color: rgb(var(--txt-color4);` (an unbalanced parenthesis, an invalid declaration) reads `color: rgb(var(--txt-color4));` at cand L1885 — present already in the creation commit a869415 (its L1884). That is a fix of an EN-author defect, recorded here and in the Per-theme record (item 4) as report material for the EN author.
- **Why:** P10: body and usage text are translated; CSS comments and the theme's own content strings are not reader prose. The rgb( correction is not a translation change: the original declaration is invalid CSS and browsers drop it; the candidate restores the declaration the author plainly intended.
- **Verify:** Read orig L397 against cand L1885; `git show a869415:pages/theme:greystyle-jp.txt | sed -n '1884p'`.
- **Disposition:** Standing (the port itself); the localize T5 pass raised no mistranslation finding on this theme.

### 7. Links

- **What:** The candidate's prose links: the credit block's source link (cand L1521 area, to the EN original — the required ruling-3 back-reference) and the repointed mode-changer links (/theme:greystyle-jp/offset/N). The info module's author-page link (orig L32, to scp-wiki.wikidot.com/greyve-author-page) was dropped with the info module; no JP author page for Greyve exists. A second instance of the author-page link survives inside the linkbox exhibit (orig L764 → cand L2256), still pointing at the EN page: it is exhibit documentation of the theme's link styling, not a live navigation link.
- **Why:** P11 repoints links to their JP counterparts where the link survives and a counterpart exists; neither condition holds for the author page, and the exhibit instance is documentation, where rewriting the target would falsify the sample.
- **Verify:** `grep -n 'greyve-author-page' original.txt candidate.txt` (orig L32 and L764; cand L2256 only).
- **Disposition:** Standing; no link item was charged for this theme in any register.

### 8. Structure

- **What:** Three structural facts. (a) The main stylesheet's relocation (section 3) preserves rule order: the topology pass measures the move at 0.99 similarity, and the four code exhibits are all retained as documentation in the candidate's collapsible (cand L2292–3778 main, L3780–3835 fragment 2, L3837–3857 fragment 3, L3859–3864 fragment 4). (b) The exhibit copy and the module copy are two full copies of the stylesheet in one file, as in the original; every wave edit had to be applied to both, and FIX2-COLON was (14 hunks across both copies), while FIX4-MECH by design touched only the exhibit copy (section 4). (c) The tail restructure (B26/B27): component includes repointed and retained; the five tail modules reduced to the one retained ListPages fragment module — the four delivery modules' removal is section 3's subject. The classifier's EXHIBIT-RESTRUCTURE label on B3 is the reorder artefact resolved in the Appendix.
- **Why:** Residue class R3: a sanctioned exhibit replacement and a silent deletion have the same diff shape, so the ground for each is stated. The exhibits are retained because the theme's documentation presents the code as part of the page; the delivery modules are not exhibits, they are the mechanism section 3 accounts for.
- **Verify:** The exhibit census above against `grep -n '\[\[code' candidate.txt` (four blocks); read cand L3870–3879 against orig L2382–2409.
- **Disposition:** Standing, except the delivery-module removal carried as the section 3 flag.

### 9. Formatting only

- **What:** 13 of the 27 blocks are WS-ONLY (B7–B19), each a single blank-line change inside the moved CSS body; the classifier counts 0 re-indentation blocks and no rule's text differs by indentation. Brace balance, checked by depth with comment- and string-awareness: every live channel ends at depth 0 on both sides. The fragment-2 exhibit ends at depth +1 on BOTH sides (orig L2291–2346, cand L3780–3835): the fragment is a partial layer written to sit over the main stylesheet, and its unclosed block is the original's own shape, carried verbatim; in the candidate the fragment is inert documentation regardless (section 3).
- **Why:** Formatting-only churn is disclosed as its own class so it is never mistaken for semantic change; the depth check exists because a displaced closing brace keeps the counts equal while swallowing every later rule, and only a depth scan sees it.
- **Verify:** classification.json (13 WS-ONLY blocks, reindent_blocks 0); the depth figures are reproducible by scanning each [[module CSS]] / [[code]] channel of the two files.
- **Disposition:** None required.

### 10. Porter annotations

- **What:** none as annotations — the candidate contains exactly one `[!-- ... --]` block, the header fragment comment (cand L1–5), which is the original's own comment carried over with its label translated (フラグメント:), not a porter note; its URL repoint is section 0 and Per-theme record item 2. The one added prose with no original counterpart is the frame, the credit block and the font supplement, each accounted for in its own section. (The original's own `[!-- {$dark}-]`-style parameter markers at orig L2392–2406 are include-parameter syntax of the delivery modules, not annotations; their removal is section 3.)
- **Why:** R2: porter additions are listed so they are never mistaken for original content or for translation; here the ground for "none" is the grep below plus the section-by-section accounting.
- **Verify:** `grep -n '\[!--' candidate.txt` (one hit, cand L1, the header comment above).
- **Disposition:** None required.

### 11. Dispositions and exceptions

- **What:** Every finding not fixed in the candidate, in one place. (1) The 21 EN-storage logo URLs across the two copies: T1 hotlink×21, DISPOSITIONED class (ii) — posting-time rewrites and original-state asset hosts (GOSIGN2-LEDGER (c1) hotlink entry; (c3) P5, KB-58). (2) The render findings: page-overflow at 1366/320/375 in both engines, the sample measurements 1569px@1366 and 789px@768, and WebKit CC "S", DISPOSITIONED as the cross-cutting overflow and narrow-width families (ledger (c2), KB-33/KB-34/KB-37, KB-36). (3) The license-box include error in the render row: recorded in the row itself as a test-wiki resolution artefact, not a defect (this theme has no license box; the error arises from the sample page's own includes). (4) The three memo-header English display strings: an observation item in the localize row, left to a staff call, not a charged defect. (5) The variant-parameter delivery loss (section 3) is NOT in this list: it is not a dispositioned finding, it is an unrecorded one, and it is carried as a flag in the Per-theme record instead.
- **Why:** A disposition is a decision with grounds, not an omission; this section exists so the full set can be audited in one place, and so that an item no register decided is visibly absent from it.
- **Verify:** Each item names its deciding register above; the KB IDs resolve in patterns/ at commit 9c5e9079afb01d30cb9fc4ef9d714e5591eb2ffa.
- **Disposition:** DISPOSITIONED (items 1–4); item 5 flagged.

### 12. Verification

- **What:** (a) T1 source check, baseline 2026-11-16: exit 1, 21 errors / 3 warns / 3 infos; all 21 errors are hotlink, and they are exactly the 21 candidate lines carrying scp-wiki.wikidot.com/local--files theme%3Agreystyle URLs across the two copies (T1-ROWS row 105). Register (c1) dispositions the hotlink class as (ii). (b) T2/T3 render: FINDINGS, all items dispositioned in (c2) (section 11, items 2–3); engine coverage is the lane's full matrix as run (RENDER-ROWS-1, RENDER-S2-B). (c) T4 localize plus follow-up: FINDINGS with 2 display-affecting items (LOCALIZE-ROWS row 95); outcomes P5 DISPOSITIONED / P7 FIXED (ledger (c3)); the follow-up found no unincorporated upstream updates. (d) T5: judged jointly with T4 by the lane; no mistranslation finding. (e) This package is self-verifying: `python3 review/build_review.py --check` regenerates diff.md from the two byte-faithful copies and compares, and re-derives the verdict stamp. The count claim above describes the pre-repair candidate; the regenerated diff.md for the current candidate reports +2319/−832 in 17 sections / 29 change blocks (GNU-diff 1913 changed lines), the authoritative count for the bytes now in this package. The classifier's 27-block figure is the pre-repair adjudication, preserved as the record of that analysis.
- **Why:** Verification claims name the cheapest deciding check and its result, not a general assurance.
- **Verify:** Re-run the checker on `pages/theme:greystyle-jp.txt`, and `python3 review/build_review.py --check` in this repo.
- **Disposition:** PASS (ledger determination, (b) row 95).

## Per-theme record

### Item 1 — the variant-parameter modules were dropped at creation, unrecorded (flag)

The original delivers three optional layers by include parameter: a page that includes the theme with `dark`, `wide` or `hide` set loads fragment /2, /3 or /4 through the gated modules at orig L2392–2406. The candidate keeps the three layers' text as code exhibits but loads none of them, documents none of the parameters, and no lane record (localize, ledger, supplement) mentions the drop: the creation commit a869415 already contains zero `{$dark}` occurrences, so the mechanism was lost in the S2 port itself, before every later check. The shape is the one the foundom ruling covers (a carried mechanism without its definitions), with the difference that here the definitions' text survives as documentation while the loading modules are gone. The package records the loss with both sides' line ranges (orig L2392–2406; candidate: absent) and refers it to the coordinator; the candidate is not edited by this package.

The loss has since been repaired — FIX-GREYSTYLE, canonical commit `3cf1cd0313fa0d5319895d57a53decc7599630e9` ("review+pages: greystyle variant modules; three sources notes repaired", 2026-11-17; report `R/review-scout/FIX-GREYSTYLE.md`), on the foundom ruling the flag itself invoked. The three variant-parameter delivery modules were restored in the original's gated form at the candidate's tail: `[!-- {$dark}-]` (L3878), `[!-- {$wide}-]` (L3884) and `[!-- {$hide}-]` (L3890), each wrapping a `[[module css]]` that imports its own draft-host fragment (`local--code/theme%3Agreystyle-jp/2`, `/3`, `/4` respectively at L3880/3886/3892), with the delivered fragments byte-identical to the original's blocks. Item 2's head comment was corrected in the same commit: the two fabricated `scp-jp.wikidot.com/fragment:greystyle-0/1` URLs (candidate L2–4 as built) now read the candidate's actual delivery addresses `local--code/theme%3Agreystyle-jp/1` … `/4` on the draft host (candidate L3–6). Total diff 23 insertions / 2 deletions in three hunks; the checker found no new class (i) error. This package was rebuilt from the post-repair canonical bytes: `candidate.txt` recopied from `pages/theme:greystyle-jp.txt`, `diff.md` and the stamp regenerated. The regenerated stamp reads STALE with the current file sha256 — no re-judgement is fabricated and the frozen GOSIGN2 ledger remains the verdict record.

### Item 2 — the head comment names fragment pages that do not exist on the JP wiki

The creation commit repointed the header comment's fragment URLs from scp-wiki.wikidot.com/fragment:greystyle-0 and fragment:greystyle-1 to the scp-jp.wikidot.com forms (B1, cand L2–4). No such pages exist in this repo or on the JP candidate wiki; the EN URLs were the working references. The effect is comment-only (no display impact), but a reviewer following the candidate's own documentation reaches two dead pages where the original reached live ones. Recorded as a minor flag.

### Item 3 — wave attribution: the "font wave" for this file is inside FIX2-COLON

Ledger (c3) records P7 as "FIXED (font wave)". No font-wave commit touches this file: the file's history is a869415 (creation), f931619 (FIX2-COLON), a497307 (FIX4-MECH), and the Noto Sans JP import and stack insertion are in f931619's diff, alongside its named colon-encoding scope. The bytes are right; the record's wave name is wrong for this theme. The same pattern (a FIX2-COLON commit carrying a fix its subject does not name) recurs in this batch (helix's frame, highroller's and i57's font supplements) and in the ambrose package's FIX-CREDIT-D.

### Item 4 — an original-side CSS defect fixed at creation (EN-author report material)

Orig L397 declares `color: rgb(var(--txt-color4);` — the parenthesis never closes, so the declaration is invalid and dropped by browsers. The candidate's corresponding line (cand L1885) closes it. The fix is already in the creation commit, so no wave record mentions it. Recorded here because the campaign's standing rule is to note EN technical mistakes found in ports, with exact details, for reporting to the EN author.

## Change set outside the two diffed files

None for this theme: no other canonical file carries part of this port. The two wave commits are shared vehicles — f931619 (FIX2-COLON) touched 18 theme files and a497307 (FIX4-MECH) touched 29; this file's hunks in each are narrated in sections 3–4 and in Multi-wave provenance. The theme's rendering is exercised through the campaign's decoration sample pages, which are campaign infrastructure, not part of the candidate.

## Multi-wave provenance

| Commit | Wave | What it changed in this file |
|---|---|---|
| a869415 | Stage 2 EN11 creation | The whole port: BHL imports repointed to scp-jp.github.io, the main exhibit inlined into the head module, frames reduced to priorities 1–2 (the `mprin` typo corrected), the credit block added, the info module removed, the body translated, all four exhibits retained, the tail component includes repointed, the five tail delivery modules reduced to the retained ListPages module (the parameter-module loss, item 1), the rgb( defect corrected (item 4), the head comment's fragment URLs repointed (item 2) |
| f931619 | FIX2-COLON | Colon encoding `theme:greystyle` → `theme%3Agreystyle` in every local--files logo URL in both CSS copies (KB-01); riding in the same commit, the P7 supplement: Noto Sans JP @import added in both copies and 'Noto Sans JP' inserted into --body-font in both copies. 26 insertions / 24 deletions, 14 hunks |
| a497307 | FIX4-MECH | One hunk (@@ -2320,10 +2320,6 @@): the exhibit copy's four font @import lines removed as duplicates (KB-65); the live module copy keeps its imports (cand L42–45) |

## Appendix — heuristic and residue blocks

There are no heuristic and no residue blocks (27 specific of 27). Two specific blocks are alignment artefacts and are resolved here so they are not mistaken for content:

- **B3** (orig L13–800 → cand at L12, EXHIBIT-RESTRUCTURE): the differ anchors the original's whole pre-exhibit body against the candidate's module opening because the inline moved the exhibit's start to the head of the file. Its labeled spans are the real changes inside that range: INFO-DEL (orig L29–30, L32–33, the info module) and SELF-DELIVERY (orig L24–25, the priority=3 frame, candidate side empty). Nothing else in the range changed semantically; the body text inside it is accounted for in sections 6–7.
- **B24** (orig L2079–2081 → cand L1291–3570, RESTORATION): the two-copy alignment artefact. With two full copies of the stylesheet in each file, the differ pairs a late original region against a long candidate span; the block's label spans locate the real insertions inside it: CREDIT-PREVIEW (cand L1512–1513, L1521–1522) and TASL-FIELDS (cand L1513–1521) for the credit block, T7-CREDIT-CSS (cand L2739–2748, L3027–3044) for the exhibit copy's inherited credit CSS, HEADERVAR (cand L2421–2424) for the exhibit copy's --logo-image line, and CONTENT-STRING (13 spans) for the transcript rules' `content:` lines in both copies. The RESTORATION label is a diff-only signal (added lines matching the original's own earlier region, i.e. the second copy); nothing for this theme was deleted and later restored by a wave. The TASL-FIELDS label also fires spuriously at cand L1907–1908, L2145–2146, L2148–2149, L2167–2168 and L2170–2171, on field-shaped lines inside the transcript exhibits; the theme's only credit block is cand L1513–1522.
