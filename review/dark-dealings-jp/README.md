# Review package — theme:dark-dealings-jp (EN → JP port)

<!-- BEGIN GENERATED VERDICT STAMP — do not hand-edit; regenerate with review/build_review.py -->
## Verdict stamp
- Theme: theme:dark-dealings-jp — origin EN, population #76 [GOSIGN2-LEDGER (b) row 76]
- Overall: PASS — passed at the ledger determination; no OPEN items [GOSIGN2-LEDGER (b) row 76]
- T1 (source check): FINDINGS (classified) — baseline 2026-11-16: exit 1, 20 errors / 2 warns / 1 info (pseudo-ref×18, foreign-include×2); standing classes dispositioned in register c1 [T1-ROWS row 76; GOSIGN2-LEDGER (b) row 76]
- T2/T3 (render, combined verdict): FINDINGS — [combined T2/T3] report `FINDINGS` — T2 sample exit 2 (target networkidle ×3 attempts, no machine verdict, chromium OK); T3 sample overflow 351/392px@320/375 with footer clipping and dim ACS-bar cell at 1366; page runtime-hotlink. [RENDER-ROWS-1 (RENDER-S2-B)]
- Engine coverage: full matrix as run by the lane; coverage not separately caveated in the row (the row records inconclusive runs, carried verbatim above) [RENDER-ROWS-1 row]
- Credit modal: no credit-modal line in this theme's row; no sample credit-modal error recorded [RENDER-ROWS-1 (RENDER-S2-B)]
- T4 (localize patterns + follow-up): FINDINGS — display-affecting findings: 4 [LOCALIZE-ROWS row 76, source LOCALIZE-S2-A]
- T5 (translation text): FINDINGS — the source reports judge T4/T5 jointly; one verdict word covers both [LOCALIZE-ROWS row 76]
- FIX5 re-judgement: none — no OPEN items at the ledger determination [GOSIGN2-LEDGER (b) row 76]
- Computed against: canonical commit 666f54356acb463c56016c967dc52464b25ba4a2; candidate file pages/theme:dark-dealings-jp.txt sha256:2897a542ef55fcaaf1a8a76ce6f2bd32a602bdc10dbaf6f55b2ce998135ff215; record: GOSIGN2-LEDGER.md + GOSIGN2-LEDGER-SUPPLEMENT.md as of the FIX5 head 435a6bb
<!-- END GENERATED VERDICT STAMP -->

## Status

| | |
|---|---|
| Verdict | **PASS** — passed at the ledger determination; this theme had no OPEN items and no §(e) register entry (GOSIGN2-LEDGER (b) row 76) |
| Standing items | **DISPOSITIONED** — T1 pseudo-ref ×18 (class (ii)) and foreign-include ×2 (the named kept exception of section 2); the render row's items (coverage caveat; KB-33/KB-34; KB-40, section 11); T4's P1, P9, P11 (section 11). The credit fields the localize lane found missing were **FIXED**. No usage-example defect: the install example already names theme:dark-dealings-jp |
| Go-sign basis | COMPLETION-REPORT.md §10 (go-sign issued; 81 FIXED / 26 DISPOSITIONED / 0 OPEN across the sweep) |
| Named exception | The kept `:scp-wiki:component:author-label-source` include pair (section 2) — no JP counterpart exists, so the pair stands byte-unchanged as a named exception, not the sweep's amethyst-v2 exception |

## Provenance

| | Original | Candidate |
|---|---|---|
| Page | theme:dark-dealings | theme:dark-dealings-jp |
| Wiki | scp-wiki.wikidot.com | SCP-JP Sigma-10 candidate (canonical repo) |
| Reference revision | 17 (first translation; the candidate's credit block records 初訳時参照リビジョン: 17) | — |
| Source of this copy | Mirror store, class COPY (hash-verified against review/sources.tsv) | Canonical file `pages/theme:dark-dealings-jp.txt`, copied at worktree HEAD 1605bbd |
| Lines / bytes | 1,091 lines / 27,739 bytes | 1,087 lines / 30,155 bytes |
| SHA-256 | 0fa6ae211d72e10080c45437cf001b6916937842241f0e81737eb162af77201b | 2897a542ef55fcaaf1a8a76ce6f2bd32a602bdc10dbaf6f55b2ce998135ff215 |

Wave history: the candidate was created by the Stage 2 EN7 integration (commit 331ab7e) and last touched by FIX2-CREDIT (commit 666f543, the credit-missing-fields completions over 36 themes). No FIX5 commit touches this file, because the theme had no OPEN items for FIX5 to re-judge.

## Summary

A parameterized Sigma-9 variant theme: five optional feature modules (logo, sunset, vesper, author box, and the base) are gated by include parameters, each delivered as its own numbered code module. The port moves all five deliveries to the draft host, repoints the furniture includes, installs the preview credit block with the eight ruling-3 fields plus a font-credit field, adds the JP font load and stacks, converts the info module section into the credit form, and translates the exhibit-heavy body (48 translation blocks). Two items need a reviewer's attention rather than a skim: the `:scp-wiki:component:author-label-source` include pair is kept byte-unchanged because no JP counterpart exists (section 2, the named exception), and T2's sample run carries a coverage caveat (the lane's sample run exited without a machine verdict on three networkidle waits; chromium was OK) that the ledger dispositions as a capture-layer item. The install example (candidate L128) already names theme:dark-dealings-jp, so the batch's usage-example defect does not apply. Measured churn (diff.md: +143/−144, 287 changed lines in 74 change blocks / 19 diff sections).

## Class summary

Auto-classification by review/classify_hunks.py (signature table 2026-11-17.1): 74 change blocks — 47 specific (63.5%), 25 heuristic (33.8%), 2 residue (2.7%), 0 skipped. Pattern citations below name the KB entry; the patterns/ tree state cited throughout is commit 9c5e9079afb01d30cb9fc4ef9d714e5591eb2ffa.

| Label | Blocks |
|---|---|
| TRANS-UNANCHORED | 30 |
| DRAFT-HOST | 20 |
| TRANSLATION-ANCHORED | 18 |
| SELF-DELIVERY | 6 |
| DELIVERY-HOST | 5 |
| EXHIBIT-RESTRUCTURE | 4 |
| INCLUDE-REPOINT | 4 |
| LINK-REPOINT | 4 |
| BARE-RATE-DEL | 3 |
| IFTAGS | 2 |
| CREDIT-PREVIEW | 1 |
| TASL-FIELDS | 1 |
| COMPONENT-SWAP | 1 |
| INFO-DEL | 1 |
| JPFONT-LOAD | 1 |
| CSS-BODY | 1 |
| JPFONT-STACK | 1 |
| LICENSE-BOX | 1 |

Adjudication for this README (every block was read against the bytes): the one CSS-BODY heuristic block (B59) is a P7 font-stack rewrite (the decorative stack gains its JP face, section 4), adjudicated as that class. The four EXHIBIT-RESTRUCTURE labels are the standing false-fire shape (repoints inside exhibit regions); the census of section 8 decides. The two residue blocks are adjudicated in the appendix: a stylized-string normalization and a one-line specimen translation. After adjudication no block is left unexplained.

## Standing sections

### 0. Header and provenance frame

- **What:** Theme theme:dark-dealings-jp; original theme:dark-dealings on scp-wiki at reference revision 17; candidate `pages/theme:dark-dealings-jp.txt`. Provenance route: derived from the original at the reference revision (sources.tsv kind: standard; no production JP counterpart, so the R4 adoption question does not arise). The candidate adds the interwiki-style frame (candidate L48–50) the original does not carry as a separate block, in the bare include form.
- **Why:** Section 0 declares the provenance route so every later count is read against the right baseline.
- **Verify:** The sources.tsv row for dark-dealings-jp; `sha256sum original.txt` against the Provenance table.
- **Disposition:** Standing (the route itself).

### 1. Credit and attribution

- **What:** The candidate installs the preview credit block at candidate L55–65 with bare includes, carrying the eight ruling-3 fields — title Dark Dealings Theme; 翻訳責任者 AI; 翻訳年 2026; 原題 Dark Dealings Theme; 著作権者 TheDarkArtist; 作成年 2022; 初訳時参照リビジョン 17; the source link (candidate L63) naming scp-wiki.wikidot.com, the original's recorded host — plus the font-credit field 追加フォント (Noto Sans JP, Noto Serif JP; SIL OFL 1.1, Google Fonts) for the JP faces of section 4. The original's live `[[module Rate]]` (original L278–281) is deleted (B52; the BARE-RATE-DEL labels across the rate-adjacent blocks), and the original's info module section (original L169–182) is converted into the credit form inside a collapsible (B33, INFO-DEL): the preview block is the theme's credit form, and kept duplicates are the KB-09 failure. Historical note: the localize lane (LOCALIZE-ROWS row 76) found credit fields missing; FIX2-CREDIT completed them, and the ledger records P3 as FIXED. No T7 credit-module CSS supplement exists in this theme.
- **Why:** P3/T1 and ruling 3; KB-09 for the duplicates the deletions prevent.
- **Verify:** `grep -n 'module Rate\|info:start' candidate.txt` returns nothing; read candidate L55–65 against the fields above.
- **Disposition:** FIXED (GOSIGN2-LEDGER §(c3): P3 FIXED).

### 2. Includes and components

- **What:** The furniture includes are repointed to `:scp-jp:` (centered-header-sigma-9, candidate L16; toggle-sidebar, candidate L17), the frame pair and credit pair are sections 3 and 1, and the license-box-end is repointed (section 8). One pair is kept foreign, deliberately: `:scp-wiki:component:author-label-source` start/end at candidate L67/L71 — T1's foreign-include ×2. No page for this component exists in the canonical repo's component set (checked: no `component:author-label-source*` among the campaign's pages), so under AGENTS.md §3 the rule for a foreign include with no verified JP counterpart applies: leave it byte-unchanged and record it as a named exception, the KB-54 shape. The localize lane recorded the keep as silent at its reading (LOCALIZE-ROWS row 76, its P1 item); the ledger dispositions P1 under the posting-procedure convention class, and this package names the exception explicitly so the keep is a decision on record, not an oversight. The install example (candidate L128) names theme:dark-dealings-jp in its correct posting form.
- **Why:** P1 (KB-15) for the repoints; §3's counterpart rule for the exception — a repoint to a nonexistent JP page would break the include outright, which is worse than a foreign include that resolves.
- **Verify:** `grep -n '\[\[include' candidate.txt` — the pair at L67/L71 is the only `:scp-wiki:` include left; `ls pages/ | grep author-label` returns nothing.
- **Disposition:** Applied (repoints); the author-label pair is a named kept exception, DISPOSITIONED (GOSIGN2-LEDGER §(c3): P1, posting-procedure convention class).

### 3. Delivery and code loading

- **What:** The theme's signature structure: five parameterized delivery modules, /1 through /5, gated by the original's own include-parameter comment gates (`[!-- {$inc-logo}]`, `{$inc-sunset}`, `{$inc-vesper}`, `{$inc-authorbox}` — the gates are the original's mechanism, carried byte-identical). All five @import lines move to the draft host (candidate L21, L26, L32, L38, L44; SELF-DELIVERY ×6 with the frame, DELIVERY-HOST ×5, and the bulk of the DRAFT-HOST ×20 together with section 4's assets). These eighteen lines are T1's pseudo-ref ×18. The interwiki-style frame (candidate L48–50, bare form) names the base delivery.
- **Why:** P4/T9 and P6/T3. The draft-host form is KB-41, class (iii): sanctioned at draft stage, rewritten to the production host at posting — multiplied here by the parameterized structure, which is why this theme's pseudo-ref count is the batch's highest.
- **Verify:** `grep -n 'local--code' candidate.txt` — the five module lines and the frame, all draft-host.
- **Disposition:** DISPOSITIONED (class (iii)).

### 4. Fonts and assets

- **What:** Fonts (P7): the candidate adds a JP font load (candidate L306: Noto Sans JP and Noto Serif JP from Google Fonts, JPFONT-LOAD) beside the original's four Google Fonts imports (candidate L302–305, kept), and two stacks gain their JP faces: the decorative stack gains 'Noto Sans JP' (B59 — the classifier's CSS-BODY heuristic, adjudicated here as the P7 stack rewrite it is) and the 'PT Serif Caption' stack gains 'Noto Serif JP' (candidate L654, JPFONT-STACK). Assets: the theme's images move from `http://` EN-host URLs to the draft host over https (B60–B69's region) — host, scheme, and re-host in one move, which also closes the T12 mixed-scheme item by construction; the two `[[image]]` exhibit blurbs are re-hosted the same way (sunset-blurb.jpg, candidate L147; vesper-blurb.png, candidate L155).
- **Why:** P7/T5 (a JP face in each stack that can render Japanese, loaded and credited — the credit is section 1's 追加フォント field); P5/KB-17 for the assets.
- **Verify:** `grep -n '@import' candidate.txt` — candidate L302–306; `grep -n 'http://' candidate.txt` returns no asset URL.
- **Disposition:** Applied (fonts); DISPOSITIONED (assets, class (ii)/(iii) family).

### 5. Header, sidebar, and site furniture

- **What:** The sidebar anchor in the exhibits is repointed to the JP page (candidate's sidebar specimen names theme:dark-dealings-jp, B21). The header's stylized strings stand as the P9/T5 item: the original's deliberate mixed-case "PUBlISheD:" is normalized to "PUBLISHED:" in the candidate (residue B1, appendix) while the header's English styling otherwise stands — the localize lane charged the EN stylized header as P9, and the ledger dispositions it under ruling 2 (header language and styling are translation taste). No P8 layout adaptation was needed.
- **Why:** P9's charge and ruling 2's settlement, with the one normalization recorded so it is not mistaken for a translation of the string.
- **Verify:** `grep -n 'PUBLISHED' candidate.txt` against original.txt's stylized form.
- **Disposition:** DISPOSITIONED (ruling 2; GOSIGN2-LEDGER §(c3)).

### 6. Text translation

- **What:** The prose and exhibits are translated throughout (TRANSLATION-ANCHORED ×18, TRANS-UNANCHORED ×30) — the variant descriptions, the dictionary-entry exhibits (one adjudicated in the appendix: the part-of-speech label translates, the English definition stands as the specimen it is), the ACS and component specimens. The T5 items the lane named (the "By:" and "PUBLISHED:" credit strings inside exhibits) are the stylized-string class of section 5: they stand in their normalized form as recorded.
- **Why:** P10 (body and usage translation); KB-18 for reader-visible strings; the specimen rule for definitions quoted as exhibits.
- **Verify:** A CJK scan of candidate.txt outside the credit block's 原題 field returns translated text and the recorded specimens.
- **Disposition:** Standing (the port itself).

### 7. Links

- **What:** The credit source link (candidate L63) names scp-wiki.wikidot.com, the original's recorded host — the host check passes. The two prose hub links are repointed to absolute EN URLs and labelled （英語版）: the sigma-9-themes hub (candidate L115, B17) and the penumbra-bhl page (candidate L119, B19) — the P11 serving-original form with its label, since neither hub has a JP counterpart page; the localize lane charged the EN hub link as P11 and the ledger dispositions it as sibling/batch-posting.
- **Why:** P11: prose links take the JP counterpart or the serving original, labelled when kept.
- **Verify:** `grep -n 'wikidot.com' candidate.txt` — the source link and the two labelled EN links.
- **Disposition:** Standing (links); P11 DISPOSITIONED (section 11).

### 8. Structure

- **What:** The closing rule holds inside the CSS: selectors, rule order, and variable names are preserved through the delivery moves; the parameterized module structure (section 3) is the original's own and is untouched. Exhibit census (R3): the original's exhibits (variant blurbs, dictionary entries, component specimens, the license tail) all survive in the candidate in the same order; the four EXHIBIT-RESTRUCTURE labels sit on repoint blocks inside exhibit regions and are discharged on that ground. The license furniture is partial by the original's own shape: only license-box-end stands in the tail, repointed to `:scp-jp:` (candidate L1085, B74, LICENSE-BOX ×1).
- **Why:** R3 forces the census because a restructure and a deletion share a diff shape.
- **Verify:** Compare the exhibit sequence in original.txt against candidate.txt.
- **Disposition:** Standing; no structural deletion beyond section 1's furniture conversion, no class I item.

### 9. Formatting only

- **What:** None — the classifier finds no whitespace-only block pair and no re-indentation (0 and 0).
- **Why:** Formatting churn is disclosed as its own class so it is never mistaken for a semantic change.
- **Verify:** The summary counts in classification.json (`reindent_blocks: 0`).
- **Disposition:** None required.

### 10. Porter annotations

- **What:** None added by the porter — the candidate carries no translator notes and no editor line (checked explicitly). The `[!-- {$...}]` comment lines at candidate L24/L28/L30/L34 are the original's include-parameter gates (section 3), byte-identical to the original's, not annotations.
- **Why:** R2: porter-added text is part of the change record; distinguishing the original's gate mechanism from annotations is exactly the check this section exists for.
- **Verify:** `grep -n '\[!--' candidate.txt` — only the parameter gates, each present in original.txt.
- **Disposition:** Standing (checked, absent).

### 11. Dispositions and exceptions

- **What:** Four items, each with its ground. (1) T1's pseudo-ref ×18: class (ii)/(iii), posting-procedure — the draft-host delivery lines of sections 3–4. (2) T1's foreign-include ×2: the named kept exception of section 2. (3) The render row's items: the T2 sample run's coverage caveat (exit 2 on three networkidle waits, no machine verdict, chromium OK — a capture-layer limitation, dispositioned as such, not a page property); the T3 sample overflow at 320/375px, footer clipping, and the dim ACS-bar cell at 1366px (KB-33/KB-34 cross-cutting families); the page's runtime-hotlink site-theme chain (KB-40). (4) T4's P1, P9, P11: DISPOSITIONED (posting-procedure convention; ruling 2; sibling/batch-posting), sections 2, 5, 7.
- **Why:** A disposition is a decision with grounds (AGENTS.md §3 classes (i)/(ii)/(iii); the named KB entries), not an omission; a coverage caveat is recorded as a limit of the evidence, not as a pass or a failure of the page.
- **Verify:** Each item names its deciding record above and in the verdict stamp.
- **Disposition:** DISPOSITIONED (items 1–4); P3 FIXED (section 1).

### 12. Verification

- **What:** (a) T1 source check (T1-ROWS row 76): exit 1, 20 errors / 2 warns / 1 info; the errors are pseudo-ref ×18 and foreign-include ×2 (section 2's exception); there is no other class (i) error. (b) T2/T3 render (RENDER-ROWS-2, lane RENDER-S2-B (EN7)): FINDINGS with the coverage caveat of section 11(3), all items dispositioned. (c) T4/T5 (LOCALIZE-ROWS row 76): FINDINGS jointly, display-affecting findings 4 — the credit-fields item FIXED afterwards (section 1), the rest dispositioned in section 11(4). (d) This package is self-verifying: `python3 review/build_review.py --check` regenerates diff.md and the verdict stamp from the two byte-faithful copies in this directory and compares. Counts in this README are the generator's (difflib, autojunk off): +143/−144 in 74 change blocks / 19 diff sections.
- **Why:** Verification claims name the cheapest deciding check and its result, not a general assurance.
- **Verify:** Re-run the checker on `pages/theme:dark-dealings-jp.txt` and `python3 review/build_review.py --check` in this repo.
- **Disposition:** PASS (GOSIGN2-LEDGER (b) row 76; go-sign, COMPLETION-REPORT §10).

## Appendix — residue blocks adjudicated

| Block | Original → candidate | Adjudication |
|---|---|---|
| B1 | L7–8 → L7–8 | The stylized header string normalized: "PUBlISheD:" → "PUBLISHED:" (section 5; the P9/T5 stylized-string item, dispositioned under ruling 2) |
| B11 | L73–74 → L87–88 | One-line specimen translation inside a dictionary exhibit: //noun// → //名詞//, the English definition kept as the specimen |

## Change set outside the two diffed files

The diff covers two files; the port's record is two files larger. `pages/theme-decoration-sample-dark-dealings-jp.txt` is the decoration sample the render checks ran against (its findings, including the coverage caveat, are the sample half of section 11(3)); it belongs to this theme's record but carries no port change of its own to explain here. There are no companion fragments, no shared base file, and no inbound-link repairs in other candidates for this theme.
