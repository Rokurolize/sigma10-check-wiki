# Review package — theme:doap-bhl-jp

<!-- BEGIN GENERATED VERDICT STAMP — do not hand-edit; regenerate with review/build_review.py -->
## Verdict stamp
- Theme: theme:doap-bhl-jp — origin KO, population #259 [GOSIGN2-LEDGER (b) row 259]
- Overall: STALE — candidate file changed since the verdict was computed (verdict against 435a6bb-era content, file sha256 now 2fd386a32936e596007240f54fa90fbe754bc5a16be807133146ba7e4467a8a6); verdict not carried over, re-judgement required
> verdicts below describe the pre-change file
- T1 (source check): FINDINGS (classified) — baseline 2026-11-16: exit 1, 9 errors / 1 warn / 1 info (pseudo-ref×9); standing classes dispositioned in register c1 [T1-ROWS row 263; GOSIGN2-LEDGER (b) row 259]
- T2/T3 (render, combined verdict): FINDINGS — [combined T2/T3] report `FINDINGS` — sample credit-modal (preview-form) + page-overflow 337–419px@320/375 (BHL min-width shape); T3 small red-outlined placeholder squares before multiple headings/blocks at 375/320 (both engines; likely an un-uploaded theme marker image, deferred, but visually a breakage). [RENDER-ROWS-2 (RENDER-S2-H (KO3))]
- Engine coverage: full matrix as run by the lane; coverage not separately caveated in the row [RENDER-ROWS-2 row]
- Credit modal: sample credit-modal errors dispositioned preview-form (credit:start-preview has no modal mechanism; GOSIGN-TESTS T2 amendment, 2026-11-16) [RENDER-ROWS-2 (RENDER-S2-H (KO3))]
- T4 (localize patterns + follow-up): FINDINGS — display-affecting findings: 2 [LOCALIZE-ROWS row 258, source LOCALIZE-S2-F]
- T5 (translation text): FINDINGS — the source reports judge T4/T5 jointly; one verdict word covers both [LOCALIZE-ROWS row 258]
- FIX5 re-judgement: none — no OPEN items at the ledger determination [GOSIGN2-LEDGER (b) row 259]
- Computed against: canonical commit b5cb7241f527a44933e45599b41df210690771c4; candidate file pages/theme:doap-bhl-jp.txt sha256:2fd386a32936e596007240f54fa90fbe754bc5a16be807133146ba7e4467a8a6; record: GOSIGN2-LEDGER.md + GOSIGN2-LEDGER-SUPPLEMENT.md as of the FIX5 head 435a6bb
<!-- END GENERATED VERDICT STAMP -->


## Status

| | |
|---|---|
| Verdict | **PASS** — passed at the ledger determination; this theme had no OPEN items and no §(e) register entry (GOSIGN2-LEDGER (b) row 259) |
| Standing items | **DISPOSITIONED** — T1 pseudo-ref ×9 (class (iii)); P5 asset hosting and P11 prose links (register c3). **One defect flag from this package:** the usage snippet's second line names a page that is not this candidate (candidate L32; per-theme record below) |
| Go-sign basis | COMPLETION-REPORT.md §10 (go-sign issued; 81 FIXED / 26 DISPOSITIONED / 0 OPEN across the sweep) |
| Named exception | None for this theme (the sweep's single named exception is theme:amethyst-v2, which has no candidate) |

## Provenance

| | Original | Candidate |
|---|---|---|
| Page | theme:doap-bhl | theme:doap-bhl-jp |
| Wiki | scpko.wikidot.com | SCP-JP Sigma-10 candidate (canonical repo) |
| Reference revision | 128 (first translation; the candidate's credit block records 初訳時参照リビジョン: 128) | — |
| Source of this copy | Campaign cache `gosign2-lanes/lane-oc-gs-localize-s2-F/orig-doap-bhl.txt`, via the mirror store (class COPY, hash-verified against review/sources.tsv) | Canonical file `pages/theme:doap-bhl-jp.txt`, copied at worktree HEAD 1605bbd |
| Lines / bytes | 554 lines / 16,756 bytes | 574 lines / 18,809 bytes |
| SHA-256 | 63a191ab62f06cabecbfc8a17ab82084953a9b79be72d4ab815005a5da3147ed | 9729e26ea923d0ef50c9c27884fefc56f21a4b0788143cf6295a91a56dcd57db |

Wave history: the candidate was created by the Stage 2 KO3 integration (commit 783e87d); FIX-CREDIT-D (1869877) normalized its credit attribution; FIX4-IWB (5559209, interwiki-style priority adjudications KB-07 and skipos fonts KB-17) set its frame to the BHL convention's priority and is the last commit and the stamp's computed-against commit. The original has not been superseded upstream in a way the record flags (the sources.tsv note field is empty for this theme — the only one of this batch without a K5a-i note).

## Summary

A KO Black Highlighter variant for the Department of Analytical Psychology (by Navla), deprecated upstream in favor of its NVL successor. The port rebuilds the delivery stack in the campaign's layered BHL form: a live include of the JP Black Highlighter candidate at the head, the theme's own CSS imported from its own JP code page, and the interwiki frame at priority=3 — the 1 normalize / 2 BHL / 3 theme convention the T4 record found missing and FIX4-IWB installed. The KO info block is replaced by the JP credit block, and its three image license entries move to a JP license box at the tail, joined by two further entries for the theme's logo images. The specimen body (headings, tabs, text boxes, the sun-cross and mandala features) is translated in full; inside the CSS exhibit, the base imports move to the JP BHL distribution (scp-jp.github.io), the Korean font import becomes Noto Serif JP, the `:lang(ko)` root becomes `:lang(ja)`, and the artwork URLs repoint to the JP test bucket. The T4 record praised this candidate's attribution, sources, JP variables, and license table as the best in its batch. Measured churn (diff.md, the generator's count: +197/−186 in 85 change blocks / 10 hunks). One defect flag arises, on the usage snippet's second line (per-theme record).

## Class summary

Auto-classification by review/classify_hunks.py (signature table 2026-11-17.1): 85 change blocks — 44 specific (51.8%), 36 heuristic (42.4%), 5 residue (5.9%), 0 skipped. Pattern citations below name the KB entry; the patterns/ tree state cited throughout is commit 9c5e9079afb01d30cb9fc4ef9d714e5591eb2ffa.

| Label | Blocks |
|---|---|
| TRANS-UNANCHORED | 37 |
| TRANSLATION-ANCHORED | 22 |
| DRAFT-HOST | 11 |
| CSS-BODY | 4 |
| WS-ONLY | 4 |
| SELF-DELIVERY | 3 |
| IFTAGS | 2 |
| INCLUDE-REPOINT | 2 |
| INFO-DEL | 2 |
| CREDIT-PREVIEW | 1 |
| DELIVERY-HOST | 1 |
| ESCAPED-INCLUDE | 1 |
| EXHIBIT-RESTRUCTURE | 1 |
| FONT-IMPORT | 1 |
| HEADERVAR | 1 |
| JPFONT-LOAD | 1 |
| LICENSE-BOX | 1 |
| TASL-FIELDS | 1 |

Adjudication for this README (every block was read against the bytes): the 59 translation labels are the specimen body, counted in section 6; the 11 DRAFT-HOST labels are the delivery and artwork repoints to the JP test bucket (sections 3–4); the 4 CSS-BODY blocks resolve as the `:lang(ko)` → `:lang(ja)` root conversion, the `--header-font` stack (also HEADERVAR-labeled), the 'Nanum Myeongjo' stack, and one exhibit line (sections 4–5); the single EXHIBIT-RESTRUCTURE primary (B84) is the tail component-include repoint, not a restructuring (section 8). The 5 residue blocks are adjudicated in the appendix. After adjudication no block is left unexplained.

## Standing sections

### 0. Header and provenance frame

- **What:** Theme theme:doap-bhl-jp; original theme:doap-bhl on scpko at reference revision 128; candidate `pages/theme:doap-bhl-jp.txt`. Provenance route: derived from the original at the reference revision by the Stage 2 KO3 wave (sources.tsv kind: standard; no production JP counterpart exists). The original opens with its tag gate (`[[iftags +테마]]`, original L1) and a head module importing the upstream BHL distribution; the candidate opens with the BHL base include (candidate L1), its own delivery module, and the frame, and the gate follows at candidate L12.
- **Why:** Section 0 declares the provenance route so every later count is read against the right baseline; the gate tag is P2, the base and frame are sections 2–3.
- **Verify:** The sources.tsv row for doap-bhl-jp; `sha256sum original.txt` against the Provenance table.
- **Disposition:** Standing (the route itself); the gate change is recorded in section 2.

### 1. Credit and attribution

- **What:** The original's attribution furniture is an unprefixed `[[include info:start]]`/`info:end` block (original L8–28, blocks B3 and B6): author Navla, the author's note, and three image license entries (rdbk.png and rdbk_black.png by Navla, CC BY-SA 3.0, with the Red Book source note; mandala.png by TheCreativePenn, CC BY 2.0, with its Openverse source link). The candidate replaces it with the JP credit block (candidate L13–23): a `:scp-jp:credit:start-preview`/`end-preview` pair carrying all eight ruling-3 fields (title 分析心理学部ブラックハイライターテーマ; 翻訳責任者 AI; 翻訳年 2026; 原題 분석심리학부 블랙하이라이터 테마; 著作権者 [[*user Navla]]; 作成年 2022; 初訳時参照リビジョン 128; the source link, section 7). The license entries do not ride in the credit block; they move to a JP license box at the gated tail (block B83, candidate L505–541): `:scp-jp:component:license-box-backend` with `author=Navla`, five entries, and `:scp-jp:component:license-box-end`. The five are the original's three (with summaries translated and SCP-KO source links added) plus two the original's block did not carry — DoAP-blackline.png and DoAP_Black.png (Navla, CC BY-SA 3.0, source-linked to the SCP-KO file area) — so the port's attribution coverage is wider than the original's.
- **Why:** P3/T1 (KB-09) for the credit furniture; T8 (the license-box rule) for the entries' new home — a theme with per-image licenses carries them in the JP license box rather than in prose, and the box's entries keep author, license, and source for each image. The original carried no credit-module CSS, so no T7 question arises.
- **Verify:** Read candidate L13–23 against the eight fields; read candidate L505–541 against the original's entries at original L16–27.
- **Disposition:** FIXED (GOSIGN2-LEDGER §(c3): P3 credit fields FIXED, credit waves, checker-verified).

### 2. Includes and components

- **What:** The candidate's live includes are the BHL base (candidate L1, `:scp-jp:theme:black-highlighter-theme` — the JP BHL candidate, which keeps the base's own name), the frame (section 3), the credit pair, the image-block specimen (candidate L40, unprefixed `component:image-block` as in the original, its `name=` repointed in section 4), the license-box pair, and the two tail component includes repointed from `:scpko:` to `:scp-jp:` (block B84, candidate L545–546: centered-header-bhl, toggle-sidebar-bhl — the components the theme bundles, named in its component list at candidate L36–37). One flag: the usage snippet (block B8, candidate L31–32) repoints both of the original's lines from `:scpko:` to `:scp-jp:`, and the base line is right (`theme:black-highlighter-theme` is the JP base candidate's name), but the theme's own line reads `@@[[include :scp-jp:theme:doap-bhl]]@@` — the original's page name without the `-jp` suffix this candidate carries everywhere else. Flagged, not edited, at build time (per-theme record below); the population sweep has since landed the repair, and the line now names `:scp-jp:theme:doap-bhl-jp`.
- **Why:** P1 (KB-15): includes name the JP page that actually exists; ruling 4's component side is satisfied because the bundled components are the JP candidates the tail includes name.
- **Verify:** `grep -n '\[\[include' candidate.txt` — base, frame, credit pair, image-block, license-box pair, tail components, and the two escaped usage lines.
- **Disposition:** Repoints applied; the usage snippet's second line is the package's defect flag (per-theme record).

### 3. Delivery and code loading

- **What:** The delivery stack is rebuilt. In the original, a head `[[module CSS]]` imported the upstream distribution from jsdelivr (normalize.min.css and black-highlighter.min.css from the Nu-SCPTheme GitHub pages build, plus a NanumBarunCatsi font CSS) and a tail module imported the theme's own code page on scpko.wdfiles.com; the CSS text itself sits in a gated `[[code]]` exhibit. The candidate instead: (1) includes the JP BHL candidate live at candidate L1 — the base arrives as a theme include, not as minified imports; (2) imports its own CSS from its own JP code page (candidate L3–5, `local--code/theme%3Adoap-bhl-jp/1` on the draft host); and (3) inside the exhibit, the code page's own head now opens with the JP BHL distribution imports (`https://scp-jp.github.io/Black-Highlighter/css/min/normalize.min.css` and `black-highlighter.min.css`, candidate L201–202, block B65) — the layer the live include delivers. **Frame paragraph (the M-frame addition):** the candidate's frame (candidate L7–10) carries `priority=3` with `theme=` naming its own code page — the BHL layering convention (1 normalize, 2 BHL, 3 theme) that the T4 record found this candidate's frame violating at its measurement (LOCALIZE-ROWS row 258, pattern 6, display-affecting) and that FIX4-IWB (commit 5559209, KB-07 adjudications) set right; the ledger records P6 FIXED.
- **Why:** P4/T2 for the stack (the JP form delivers the base through the JP base candidate and the theme's own layer through its own code page, so no layer depends on the KO wiki or the upstream build). P6/T3 (KB-07) for the frame's priority value: in a layered BHL port the priority is what orders the layers, so a wrong value is a display defect, not a style point. The draft-host form is KB-41, class (iii).
- **Verify:** Read candidate L1–10; `grep -n 'jsdelivr\|Nu-SCPTheme' candidate.txt` returns nothing; the exhibit's import head is at candidate L201–202.
- **Disposition:** FIXED (P6, FIX4-IWB); the draft-host URLs are DISPOSITIONED (class (iii)).

### 4. Fonts and assets

- **What:** Fonts. The Korean font import at the code page's head (original L214: a Nanum font CSS file on scpko.wdfiles.com) becomes a Google Fonts Noto Serif JP load (candidate L210, block B68, JPFONT-LOAD). Two stacks convert (CSS-BODY blocks): `--header-font: 'UnBatang', serif` → `'Noto Serif JP', 'Hiragino Mincho ProN', …` (block B72, candidate L223–225 region, also HEADERVAR-labeled) and `'Nanum Myeongjo', serif` → `'Noto Serif JP', 'Hiragino Mincho ProN', …` (block B80, candidate L470). The language root converts with them: `:root:lang(ko)` → `:root:lang(ja)` (block B69, candidate L212). The head module's NanumBarunCatsi import disappears with the jsdelivr stack (section 3). Assets: the artwork URLs repoint from scpko.wdfiles.com to the JP test bucket (DRAFT-HOST blocks B10, B63, B71, B75–B79, B81) — the image-block specimen's DoAP_Black.png (candidate L41), the mandala image address quoted in the prose (candidate L190), the `--logo-image` and companion header image variables (candidate L218–220), and the CSS background layers; file names and folders are preserved under the theme's own JP file area.
- **Why:** P7/T5 with KB-16: UnBatang and Nanum Myeongjo have no Japanese coverage, so the stacks land on Noto Serif JP with a Hiragino fallback, and the `:lang()` root must name the language the port serves or the JP variable set never applies. P5/KB-58 for the hosting state; KB-41 for the draft-host form.
- **Verify:** `grep -n 'UnBatang\|Nanum' candidate.txt` returns nothing; `grep -n 'lang(ja)' candidate.txt` — the converted root; `grep -c 'sigma10-jp-test.wdfiles.com' candidate.txt` counts the repointed delivery and asset URLs.
- **Disposition:** Conversions applied; the asset URLs are DISPOSITIONED (class (ii) / KB-58; GOSIGN2-LEDGER §(c3) P5).

### 5. Header, sidebar, and site furniture

- **What:** The header image variables (`--logo-image` and its companions, candidate L218–220) are the section 4 repoints; the `--header-font` conversion is block B72. The theme's BHL furniture (the centered header and toggle-sidebar components) is delivered by the tail includes (section 2). The render row's page overflow (337–419px at 320/375) is the BHL base's min-width shape, shared by every BHL-layered theme and recorded against the base family (KB-33/KB-34), not against this candidate's own CSS.
- **Why:** P9/T6 is a per-theme judgment and none was needed beyond the conversions; P8's mobile shape is the BHL base's, carried by the include.
- **Verify:** `grep -n -- '--logo-image\|--header-font' candidate.txt` — the repointed variable and the converted stack.
- **Disposition:** Standing.

### 6. Text translation

- **What:** The specimen body is translated in full (59 translation labels over blocks B5–B64). In groups: the deprecated-theme notice (candidate L24 — its successor link repointed to [[[theme:doap-nvl-jp]]], section 7); the intro prose (candidate L26, its scpko links kept as branch links with （韓国語版） glosses); the usage prose (candidate L28–34); the specimen sections — headings 1–6, the tabview specimens including the repeated long-tab text (blocks B19–B38), blockquotes, the table, the class specimens, the Department text boxes, the Red Book text box and its Jung pattern note, the sun-cross header specimen, the 幻視 (vision) section, and the mandala section (blocks B39–B64). The author's voice is kept (the すごいでしょう specimen patter, the Jung explanations). Inside the exhibit, the CSS comment header is carried with one added line (block B67, section 10).
- **Why:** P10 (body and specimen translation). The deprecated notice's translation matters beyond completeness: it is the theme's own instruction to prefer the successor, and its link is repointed so a JP reader lands on the JP successor candidate.
- **Verify:** Read candidate L24–199 against original L30–206 (the gated body before the source-code section).
- **Disposition:** Standing (the port itself).

### 7. Links

- **What:** The credit source link (candidate L22) names `https://scpko.wikidot.com/theme:doap-bhl` — the original's recorded host (review/sources.tsv) — with the original's Korean title as its label text; no host defect arises. Body links: the successor link repoints to the JP candidate ([[[theme:doap-nvl-jp]]], candidate L24); the two department links keep their scpko targets with explicit （韓国語版） glosses (candidate L26) — they name the KO branch's department pages as the theme's subject matter, and the ledger dispositions the class as P11 DISPOSITIONED (sibling / batch-posting class). The T4 record notes the [[[theme:doap-nvl-jp]]] link is to an unposted sibling (pattern 1 note) — the pseudo-ref class (iii) of section 11. The license box's source links name the SCP-KO file area and Openverse (candidate L505–541), which are the images' actual sources.
- **Why:** P11: prose links take the JP counterpart or the serving original under the dead-reference evidence standard; subject-matter links to the source branch are glossed so a reader knows they leave the JP wiki.
- **Verify:** Compare candidate L22's host against the sources.tsv row's original_url host (scpko.wikidot.com) — identical; read candidate L24 and L26.
- **Disposition:** Source link standing; the branch links DISPOSITIONED (P11, sibling / batch-posting class).

### 8. Structure

- **What:** The gated body keeps the original's order entire (deprecated notice, intro, usage, components, specimens, source-code exhibit, license box), with two placements worth naming: the license box stands at the gated tail where the original's info block content is answered (section 1), and the two bundled-component includes stand after the gate's close in both versions (original L513–514 → candidate L545–546), repointed only — the classifier's EXHIBIT-RESTRUCTURE primary on block B84 is that repoint, adjudicated against the census: nothing was restructured. The head is where the structure changes (base include, delivery module, frame before the gate; section 3), and the original's tail delivery module is answered by the candidate's head module. An exhibit census of the specimens shows every specimen present in order.
- **Why:** R3's census decides exhibit questions; here label and census disagree and the census governs, per the standing lesson.
- **Verify:** Compare `grep -n '\[\[tab\|\[\[collapsible\|\[\[code\|\[\[include' original.txt candidate.txt` — the sequences correspond.
- **Disposition:** Standing; no structural deletion, no class I item.

### 9. Formatting only

- **What:** Four whitespace-only blocks (B66, B70, B73, B74; WS-ONLY primaries): trailing-space and blank-line differences inside the CSS exhibit, one of them on the exhibit's "Created by Navla" comment line (candidate L206). They ride inside the exhibit's carry-over and change no rendering. No re-indentation blocks exist.
- **Why:** R7: whitespace churn is disclosed as its own class so it is never mistaken for a semantic change.
- **Verify:** Section 9 of the classifier skeleton for this package (WS-ONLY 4, re-indentation 0).
- **Disposition:** None required.

### 10. Porter annotations

- **What:** One annotation, inside the exhibit's CSS comment header (block B67, candidate L208): "Ported for SCP-JP (theme:doap-bhl rev 128)" — added to the original's comment block (which otherwise carries over: theme name, year, Navla's authorship, the Ontology Department and Black Highlighter credits). The candidate has no `[!-- --]` notes and no editor line; its other CSS comments are the original's own (19 comment lines total, all with original counterparts apart from the one added line).
- **Why:** R2: porter-added text is part of the change record; the check was run explicitly because annotations ride inside other labeled blocks (here, inside a carried comment header in the exhibit).
- **Verify:** Read candidate L203–209 against original L208–213; `grep -n '\[!--' candidate.txt` returns nothing.
- **Disposition:** Standing (checked, one item, enumerated).

### 11. Dispositions and exceptions

- **What:** Four items, each with its ground. (1) T1's nine pseudo-ref errors: DISPOSITIONED in register c1 (pseudo-ref, class (iii)) — references to the not-yet-posted JP pages (the base candidate, the successor theme:doap-nvl-jp, the bundled components) that resolve at posting. (2) The render row's items (RENDER-ROWS-2, RENDER-S2-H (KO3)): the sample's credit-modal errors are the preview form's property (KB-32, ruling 5); the page overflow is the BHL min-width shape (KB-33/KB-34); and T3's small red-outlined placeholder squares before headings are the un-uploaded theme marker image, deferred with the asset hosting state (KB-58) — the row calls it visually a breakage but charges it to the deferred upload, not to the candidate's text. All DISPOSITIONED. (3) P5 asset hosting: DISPOSITIONED (class (ii) / KB-58). (4) P1: DISPOSITIONED (posting-procedure convention class, §(c3)). The usage-snippet flag (per-theme record) is not in this list: no ledger line dispositions the snippet's page name.
- **Why:** A disposition is a decision with grounds (AGENTS.md §3 classes (i)/(ii)/(iii); the named KB entries), not an omission.
- **Verify:** Each item names its deciding record above.
- **Disposition:** DISPOSITIONED (items 1–4 as stated).

### 12. Verification

- **What:** (a) T1 source check (T1-ROWS row 263): exit 1, 9 errors / 1 warn / 1 info; all nine errors are pseudo-ref, class (iii); there is no class (i) error. (b) T2/T3 render (RENDER-ROWS-2, RENDER-S2-H (KO3)): FINDINGS, every item dispositioned (section 11 item 2). (c) T4/T5 (LOCALIZE-ROWS row 258): FINDINGS jointly, display-affecting findings 2 — the frame's priority convention (pattern 6, since FIXED by FIX4-IWB) and the KO branch links in the body (pattern 11, dispositioned); the row also notes the unposted successor link (pattern 1) and praises the candidate's attribution, source links, JP variables, and license table as its batch's best. The ledger §(c3) line records the outcomes: P1 DISPOSITIONED, P6 FIXED, P11 DISPOSITIONED. (d) This package is self-verifying: `python3 review/build_review.py --check` regenerates diff.md and the verdict stamp from the two byte-faithful copies in this directory and compares. Counts in this README are the generator's: +197/−186 in 85 change blocks / 10 hunks.
- **Why:** Verification claims name the cheapest deciding check and its result, not a general assurance.
- **Verify:** Re-run the checker on `pages/theme:doap-bhl-jp.txt` and `python3 review/build_review.py --check` in this repo.
- **Disposition:** PASS (GOSIGN2-LEDGER (b) row 259; go-sign, COMPLETION-REPORT §10).

## Appendix — residue blocks

The classifier reports 5 residue blocks; all were adjudicated against the bytes:

| Block | Range (orig → cand) | Classifier state | Resolution |
|---|---|---|---|
| B40 | 125-125 → 118-118 (body → body) | no signature | One-word specimen translation （文字） inside a blockquote specimen; section 6 |
| B56 | 178-178 → 171-171 (body → body) | no signature | Specimen heading translation （幻視）; section 6 |
| B67 | at 213 → 208-208 (code-css → code-css) | no signature | The porter annotation line inside the exhibit's comment header; section 10 |
| B82 | 507-507 → at 502 (code-css → code-css) | no signature | One line removed at the exhibit's tail, pairing residue of the license-box insertion; section 8 |
| B85 | 554-554 → at 575 (body → body) | no signature | The original's final `@@ @@` spacer line, not carried past the candidate's tail module; section 8 |

## Per-theme record — the usage snippet names a different page (defect flag, repaired)

The usage snippet's second line names the original's page, not this candidate. Candidate L32 reads `@@[[include :scp-jp:theme:doap-bhl]]@@`. This candidate is theme:doap-bhl-jp: its canonical file is `pages/theme:doap-bhl-jp.txt`, its delivery import and frame `theme=` URL both name `theme%3Adoap-bhl-jp`, and the port itself applied the `-jp` suffix where the original named a sibling theme — the deprecated notice's successor link is [[[theme:doap-nvl-jp]]] (candidate L24). The snippet's first line is correct because the base candidate genuinely is named theme:black-highlighter-theme; the second line, on the bytes, instructs a reader to include a page that is not this theme's candidate. The same shape appears in this batch's other KO candidate with a usage snippet (dear-dictator-jp, candidate L76), which suggests a KO-wave habit rather than a considered naming decision; the EN and CN candidates in the batch name their own `-jp` pages in their snippets. No ledger line dispositions the snippet's name (the T1 pseudo-ref class (iii) covers references to not-yet-posted pages generally, and the coordinator may judge the snippet covered by it; this package records the byte-level inconsistency and flags it rather than deciding). The candidate is left exactly as it stands, per the standing rule for fix lanes; the repair, if confirmed, is the one-line repoint of candidate L32 to the candidate's own page name. The repair has since been confirmed and has landed as part of the usage-example population sweep (sweep report SWEEP-USAGE.md in the campaign record, R/review-scout/; canonical commit b5cb724), which repaired this shape across all 157 affected candidates: candidate L32 now reads `@@[[include :scp-jp:theme:doap-bhl-jp]]@@`. This package is refreshed on the corrected bytes; its stamp reads STALE against the pre-repair verdict, by design.

## Change set outside the two diffed files

The diff covers two files; the port's record is one file larger. `pages/theme-decoration-sample-doap-bhl-jp.txt` is the decoration sample the render checks ran against (its findings are the sample half of the T2/T3 row); it belongs to this theme's record but carries no port change of its own to explain here. The BHL base is the separate candidate theme:black-highlighter-theme, included, not copied; the bundled components (component:centered-header-bhl, component:toggle-sidebar-bhl) are likewise separate candidates.

## License and attribution

- **Title:** 분석심리학부 블랙하이라이터 테마
- **Author:** Navla
- **Source:** https://scpko.wikidot.com/theme:doap-bhl — revision 128
- **License:** Creative Commons Attribution-ShareAlike 3.0 (CC BY-SA 3.0) — license deed: https://creativecommons.org/licenses/by-sa/3.0/
- **Adaptation:** This package holds a Sigma-10 migration port of the work; changes were made. See "Summary" and "Standing sections" in this README for what changed and why. Translator: AI (Muse and its delegated agents), per the campaign's standing attribution rule.
