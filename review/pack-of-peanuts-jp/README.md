# Review package — theme:pack-of-peanuts-jp (EN → JP port)
New to this package's shorthand? Read the notation key first: [How to read a review package](../HOW-TO-READ.md).

<!-- BEGIN GENERATED VERDICT STAMP — do not hand-edit; regenerate with review/build_review.py -->
## Verdict stamp
- Theme: theme:pack-of-peanuts-jp — origin EN, population #119 [GOSIGN2-LEDGER (b) row 119]
- Overall: STALE — candidate file changed since the verdict was computed (verdict against 435a6bb-era content, file sha256 now d7634a849426911841a85454fe432c81b3e61470e2cfdf26f5a4c23700db3770); the verdicts below were computed against that pre-change file, and the record verdict stands: a candidate revised through the campaign's recorded repairs is posted like a PASS row, with the change recorded in its package
- T1 (source check): FINDINGS (classified) — baseline 2026-11-16: exit 1, 5 errors / 0 warns / 1 info (pseudo-ref×5); standing classes dispositioned in register c1 [T1-ROWS row 119; GOSIGN2-LEDGER (b) row 119]
- T2/T3 (render, combined verdict): FINDINGS — [combined T2/T3] report `FINDINGS` — page-overflow 823–829px@768 (page) and 331px@320 + 920px@768 (sample); runtime-hotlink site-theme chain; sample credit-modal (preview-form). [RENDER-ROWS-2 (RENDER-S2-C (EN15))]
- Engine coverage: full matrix as run by the lane; coverage not separately caveated in the row [RENDER-ROWS-2 row]
- Credit modal: sample credit-modal errors dispositioned preview-form (credit:start-preview has no modal mechanism; GOSIGN-TESTS T2 amendment, 2026-11-16) [RENDER-ROWS-2 (RENDER-S2-C (EN15))]
- T4 (localize patterns + follow-up): PASS — display-affecting findings: 0 [LOCALIZE-ROWS row 119, source LOCALIZE-S2-B]
- T5 (translation text): PASS — the source reports judge T4/T5 jointly; one verdict word covers both [LOCALIZE-ROWS row 119]
- FIX5 re-judgement: none — no OPEN items at the ledger determination [GOSIGN2-LEDGER (b) row 119]
- Computed against: canonical commit b5cb7241f527a44933e45599b41df210690771c4; candidate file pages/theme:pack-of-peanuts-jp.txt sha256:d7634a849426911841a85454fe432c81b3e61470e2cfdf26f5a4c23700db3770; record: GOSIGN2-LEDGER.md + GOSIGN2-LEDGER-SUPPLEMENT.md as of the FIX5 head 435a6bb
<!-- END GENERATED VERDICT STAMP -->

## Status

| | |
|---|---|
| Verdict | **PASS** — passed at the ledger determination; this theme had no OPEN items and no §(e) register entry (GOSIGN2-LEDGER (b) row 119) |
| Standing items | **DISPOSITIONED** — T1 pseudo-ref ×5 (classes (ii)/(iii), section 11); the render row's items (KB-40 / KB-32 and the page-overflow readings, section 11). **FLAGGED by this package** — the usage exhibit names the plain slug on the JP side (per-theme record) |
| Go-sign basis | COMPLETION-REPORT.md §10 (go-sign issued; 81 FIXED / 26 DISPOSITIONED / 0 OPEN across the sweep) |
| Named exception | None for this theme (the sweep's single named exception is theme:amethyst-v2, which has no candidate) |

## Provenance

| | Original | Candidate |
|---|---|---|
| Page | theme:pack-of-peanuts | theme:pack-of-peanuts-jp |
| Wiki | scp-wiki.wikidot.com | SCP-JP Sigma-10 candidate (canonical repo) |
| Reference revision | 45 (first translation; the candidate's credit block records 初訳時参照リビジョン: 45) | — |
| Source of this copy | Campaign cache `gosign2-lanes/lane-oc-gs-localize-s2-B/orig-pack-of-peanuts.txt`, via the mirror store (class COPY, hash-verified against review/sources.tsv) | Canonical file `pages/theme:pack-of-peanuts-jp.txt`, copied at worktree HEAD 9068bb7 |
| Lines / bytes | 927 lines / 19,189 bytes | 917 lines / 19,799 bytes |
| SHA-256 | 3bbe996d51e5c6b2572d5b2ad5f430b54d96e259bbc76ac9c149be0ee34bc015 | f72bfd33f4df8554a0e73188bbdf79a8997d14f89b7b838a524c60feb097a9a4 |

Wave history: the candidate was created by the Stage 2 EN15 integration (commit fde02f3, the LOCALIZE-S2-B wave's port, lane-dsh-en15) and has exactly one later commit, 1869877 (FIX-CREDIT-D), whose pack-of-peanuts hunk is the translator-field normalization. No FIX5 commit touches this file, because the theme had no OPEN items for FIX5 to re-judge.

## Summary

A Flopstyle-family variant theme (the SCP-173 fifteenth anniversary theme) whose port is the standing classes plus two theme-specific moves worth a reviewer's attention. First, the original's CSS imports a tabview stylesheet out of another theme's file area (theme:flopstyle-dark's tabview.css); the candidate instead imports a copy in its own file area and adds a license-box entry that says exactly that, including that the original states no license for it. Second, the original's tail carries its whole delivery zone (two page-furniture includes, the code module, and the interwiki frame at priority 2) after the tag gate; the candidate rebuilds delivery at the head in the wave-standard form and drops the two furniture includes with that zone, since the JP theme page takes the environment's own header and sidebar furniture. Everything else is the standing set: the centered bare Rate becomes the preview credit block, the header title and subtitle variables are translated, the three bunny.net font loads move to Google Fonts with Noto Sans JP loaded and appended to the title and body stacks, the hand-rolled license module becomes the JP backend box with its entries translated, and the long formatting-sample body is translated exhibit by exhibit. Measured churn (diff.md, the generator's difflib count with autojunk off: +125/−142 in 59 change blocks / 5 hunks).

## Class summary

Auto-classification by review/classify_hunks.py (signature table 2026-11-17.1): 59 change blocks — 29 specific (49.2%), 27 heuristic (45.8%), 3 residue (5.1%), 0 skipped. Pattern citations below name the KB entry; the patterns/ tree state cited throughout is commit 9c5e9079afb01d30cb9fc4ef9d714e5591eb2ffa.

| Label | Blocks |
|---|---|
| TRANS-UNANCHORED | 30 |
| TRANSLATION-ANCHORED | 17 |
| DRAFT-HOST | 5 |
| EXHIBIT-RESTRUCTURE | 4 |
| INCLUDE-REPOINT | 3 |
| SELF-DELIVERY | 2 |
| LICENSE-BOX | 2 |
| CSS-BODY | 2 |
| BARE-RATE-DEL | 1 |
| CREDIT-PREVIEW | 1 |
| CREDIT-PROSE | 1 |
| ESCAPED-INCLUDE | 1 |
| FONT-IMPORT | 1 |
| HEADERVAR | 1 |
| IFTAGS | 1 |
| JPFONT-LOAD | 1 |
| TASL-FIELDS | 1 |
| COMMENT-TEXT | 1 |

Adjudication for this README (every block was read against the bytes): the 3 residue blocks are B10 (a wrapper-pairing alignment at the exhibit head), and B54/B55 (the `[[/=]]` pairing normalization at the license zone, section 8). The 2 CSS-BODY blocks are P7 font-stack rewrites (B51, B52, section 4), not body-CSS churn. The 4 EXHIBIT-RESTRUCTURE primaries adjudicate as: B9 the image-block exhibit's repoint and asset re-host (sections 2, 4), B47 the tabview import replacement and JP font load (sections 3, 4), B58 the license-box swap (section 1), and B59 the tail delivery zone's replacement by the head frame (section 3). The heuristic TRANS-UNANCHORED mass is the formatting-sample body's one-line translations, verified line by line (section 6). After adjudication no block is left unexplained.

## Standing sections

### 0. Header and provenance frame

- **What:** Theme theme:pack-of-peanuts-jp; original theme:pack-of-peanuts on scp-wiki at reference revision 45; candidate `pages/theme:pack-of-peanuts-jp.txt`. Provenance route: derived from the original at the reference revision by the LOCALIZE-S2-B wave (sources.tsv kind: standard; no production JP counterpart exists for this theme, so the R4 adoption question does not arise). The frame itself moved: the original opens with its tag gate (original L1) and carries delivery at the tail, after the gate (original L916–927); the candidate opens with the delivery pair (candidate L1–8) and places the localized gate `[[iftags +テーマ]]` after it (candidate L10).
- **Why:** Section 0 declares the provenance route so every later count is read against the right baseline; the gate's tag is P2, the frame is P6/T3 (section 3).
- **Verify:** The sources.tsv row for pack-of-peanuts-jp; `sha256sum original.txt` against the Provenance table.
- **Disposition:** Standing (the route itself); the gate and frame changes are recorded in section 3.

### 1. Credit and attribution

- **What:** The original's credit furniture is a centered bare `[[module Rate]]` (original L7–9) and, at the tail, a hand-rolled license zone: a module carrying the CC attribution text for the page itself (original L885–891), a "Licensing Disclosures" heading, two blockquote image entries (173-icon.png by EstrellaYoshte, CC BY-SA 3.0; concrete.png by Devanath, CC0, edited by Lt Flops), and a `:scp-wiki:component:license-box-end` include with no matching backend include (original L913). The candidate deletes the bare Rate (BARE-RATE-DEL block B3) and installs the preview credit block (candidate L16–25) carrying the eight ruling-3 fields (title パック・オブ・ピーナッツ テーマ; 翻訳責任者 AI; 翻訳年 2026; 原題 Pack Of Peanuts Theme; 著作権者 [[*user Lt Flops]]; 作成年 2022; 初訳時参照リビジョン 45; the source link https://scp-wiki.wikidot.com/theme:pack-of-peanuts, whose host matches the sources.tsv record). The license zone becomes the settled JP form: `:scp-jp:component:license-box-backend |author=Lt Flops]]` with `:scp-jp:component:license-box-end` (candidate L896–915), the two original entries translated in place (ファイル名 / 作者 / ライセンス / 出典 / 補足; the license links take their Japanese deed forms), and a third entry with no original counterpart, for tabview.css, recording that the original distributed that file as another theme's attachment and stated no license for it (candidate L910–912; the import itself is section 3). The hand-rolled attribution module and the "Licensing Disclosures" heading are not carried: the backend box is their JP replacement, and the page-level attribution lives in the credit block. T7 credit-module CSS: none — neither side styles the credit module, so there is no supplement to add and none was.
- **Why:** P3/T1 with KB-09 (the preview module is rate-bearing; a kept bare Rate would double-render). Ruling 3 fixes the eight fields and the translator form; the file's last commit (1869877) is that form arriving. T4: the license box must be present in its settled JP form (KB-60 covers the original's half-form: an end include and a hand-rolled start); the tabview entry is the TASL record for a file whose provenance changed (ruling 3's attribution standard applied to an asset).
- **Verify:** `grep -n 'module Rate' candidate.txt` returns nothing; read candidate L16–25 against the eight fields; compare the license entries at original L894–912 and candidate L899–915 entry by entry.
- **Disposition:** FIXED by construction at creation (P3 credit fields and the T4 box form; T4 judged the theme PASS with 0 display-affecting findings, LOCALIZE-ROWS row 119).

### 2. Includes and components

- **What:** Three repoint blocks and the tail furniture deletion. B8: the usage exhibit, `:scp-wiki:theme:pack-of-peanuts` → `:scp-jp:theme:pack-of-peanuts` (original L22 → candidate L38); its slug is the plain form, the flagged item of the per-theme record. B9: the image-block exhibit include is repointed to `:scp-jp:component:image-block` and its `name=` asset re-hosted (original L25–30 → candidate L41–46; the asset is section 4). The credit and license includes are section 1, the frame is section 3. The original's two tail furniture includes, `:scp-wiki:component:centered-header-sigma-9` and `:scp-wiki:component:croqstyle` (original L917–918, after the tag gate, in the delivery zone), have no counterpart in the candidate: they styled the theme's own page on the foreign wiki, and the JP theme page takes the JP environment's header and sidebar furniture instead; nothing inside the gate (that is, nothing a page using the theme receives) depended on them. No component swap (T8) was needed.
- **Why:** P1 (KB-15) for the repoints. The furniture deletion is a delivery-zone consequence, recorded here with its ground rather than as an exhibit change: the includes sat outside the gate alongside the delivery module the candidate rebuilds at the head (section 3).
- **Verify:** `grep -n '\[\[include' candidate.txt` — seven includes, all JP-side; `grep -n 'croqstyle\|centered-header' candidate.txt` returns nothing.
- **Disposition:** Applied; the exhibit's slug form is flagged in the per-theme record (not edited by this package).

### 3. Delivery and code loading

- **What:** The original delivers at the tail, after the gate: a `[[module CSS]]` importing its own `local--code/theme%3Apack-of-peanuts/1` from scp-wiki.wdfiles.com (original L920–922) and an interwiki-style frame at priority 2 with `theme=` naming the same /1 (original L924–927). The candidate rebuilds both at the head (blocks B1, B59): a module CSS importing its own `local--code/theme%3Apack-of-peanuts-jp/1` from the draft host (candidate L1–3), and the frame at priority 1 whose `theme=` names the same /1 on the production host form, scp-jp.wdfiles.com (candidate L5–8) — the frame parameter already carries its posting form while the module import is still in draft form, a mixed state the T1 register records by class ((ii) for the frame line, (iii) for the module line). Inside the CSS, one delivery change is theme-specific (block B47): the original imports a tabview stylesheet from another theme's file area, `scp-wiki.wdfiles.com/local--files/theme%3Aflopstyle-dark/tabview.css` (original L138); the candidate imports `tabview.css` from its own draft-host folder `theme%3Apack-of-peanuts-jp/` (candidate L156), so the theme no longer depends on a sibling theme's attachments. Its license record is the added entry of section 1.
- **Why:** P4/T9 and P6/T3 for the frame and module (priority 1: the theme's own layer over the Sigma base). The tabview replacement is KB-14's rule from the asset side: a cross-theme file dependency is a fragile delivery (the sibling's files are outside this theme's control), and the campaign's form is an own-folder copy with its provenance recorded. The draft-host lines are KB-41, class (iii); the frame's production-host line is class (ii) mechanics.
- **Verify:** `grep -n 'local--code\|tabview' candidate.txt` — L2, L7, L156; compare original L138 against candidate L156.
- **Disposition:** DISPOSITIONED (the draft-host lines, class (iii); the frame's production-host form, class (ii)).

### 4. Fonts and assets

- **What:** Loads (block B46): the original's three fonts.bunny.net loads (Sriracha; Comic Neue 700; Inter 400/700/900, original L134–136) move to Google Fonts with families and weights unchanged (candidate L149–151), and a fourth load is added: Noto Sans JP 400/700 from Google Fonts (candidate L154, JPFONT-LOAD). Stacks: 'Noto Sans JP' is appended to the title stack (`--title-font: "Sriracha", "Noto Sans JP", cursive`, candidate L192, block B51) and the body stack (`--body-font: "Inter", "Noto Sans JP", sans-serif`, candidate L194, block B52) — the classifier's two CSS-BODY primaries are these P7 rewrites, not body churn. The subtitle stack (`"Comic Neue", cursive`) is unchanged: it is a Latin display face for the subtitle variable, whose text is translated but whose letterforms the theme keeps. Unlike plant in this batch, the added JP face is loaded in-file, so the KB-16 gap does not arise. Assets: the theme's own images move from `scp-wiki.wdfiles.com/local--files/theme%3Apack-of-peanuts/` to the draft host's `theme%3Apack-of-peanuts-jp/` folder (the image-block's 173-icon.png at candidate L43, the `--lgurl` logo at candidate L174, and the remaining DRAFT-HOST lines inside the CSS), filenames unchanged; the license entries for the externally sourced images (concrete.png's PIXNIO source) keep their serving source links (section 1).
- **Why:** P7/T5 with KB-16: the JP face is loaded and appended together, so Japanese title and body text render in it. P5 with KB-17: fonts.bunny.net is not among the hosts the JP environment keeps, Google Fonts is; the theme's own assets re-host to the JP side.
- **Verify:** `grep -n '@import' candidate.txt` — L2 (self-delivery) and L149–156 (the four font loads and tabview); `grep -n -- '--title-font\|--body-font\|--subtitle-font' candidate.txt` — L192–194.
- **Disposition:** Applied; the draft-host asset URLs are DISPOSITIONED (class (iii)).

### 5. Header, sidebar, and site furniture

- **What:** The header variables are translated, not kept (block B49): `--header-title: "SCP FOUNDATION"` → `"SCP財団"` and `--header-subtitle: "15 Years of Scraping Concrete, Personnel"` → `"コンクリートを削り続けた15年、職員諸君"` (original L152–153 → candidate L170–171), and the `--lgurl` logo in the same block takes the draft-host form (section 4). Because the values were translated, ruling 2 (header language out of scope) is not engaged and KB-57 does not apply. No other furniture change: the sidebar and topbar rules are carried unmodified apart from the font stacks of section 4, and the tail furniture includes' deletion is recorded in section 2 with its ground. No P8 layout adaptation was needed.
- **Why:** P9/T6: the header variables are the theme's visible title surface, and this port localizes them (the campaign's other common outcome, keeping the original's language under ruling 2, is the disposition plant and others in this batch carry; it is not this theme's).
- **Verify:** `grep -n -- '--header-title\|--header-subtitle' candidate.txt` — L170–171.
- **Disposition:** Standing.

### 6. Text translation

- **What:** The body is a formatting-sample exhibit page, and it is translated throughout, in two counted groups. Seventeen TRANSLATION-ANCHORED blocks: the section headings (What Is This? → これは何？, How to Use → 使い方, Example Formatting → 書式例）, the prose paragraphs, and the sample strings. The TRANS-UNANCHORED mass (25 primaries) is the same shape at one-line grain: the formatting samples' labels （太字 / 斜体 / 下線 / 取り消し線 / 等幅 / 上付き / 下付き）, the hyphen-rule instruction, the fake-code sample's text, and the link samples' labels, each verified line by line against the mirror for this README. The pseudocrumbs line is rewritten as well as translated (candidate L13): the original's bare local hub link `[[[sigma-9-themes|Sigma Themes]]]` becomes a full-URL link to the EN hub page with a translated label, `[*https://scp-wiki.wikidot.com/sigma-9-themes Sigmaテーマ]` (its link aspect is section 7). R1 in-CSS text: one section comment is translated inside the CSS; the CSS's remaining comments are structural labels carried in English (the FONTS/COLORS banners), which are porter-visible only. No reader-visible string stays in English outside the credit block's original-title field (candidate L20, a quotation by design) and the theme's proper nouns.
- **Why:** P10 (body, usage, and sample translation is the port's purpose) and KB-18 (reader-visible strings). The unanchored group is where a silent deletion would hide, which is why each was read individually rather than waved through as a class.
- **Verify:** The pairs are diff.md's body sections in order; an English-prose scan of candidate.txt outside the credit fields returns only proper nouns and the CSS banner labels.
- **Disposition:** Standing (the port itself); T4/T5 judged the theme PASS with 0 display-affecting findings (LOCALIZE-ROWS row 119).

### 7. Links

- **What:** The candidate's live outbound link is the credit block's source link (candidate L24), naming the original on scp-wiki.wikidot.com, the host the campaign's provenance records name for it; it serves the original page, and its label carries the original's title. The pseudocrumbs hub link (candidate L13) was rewritten from the original's bare local name to the EN hub's full URL with a translated label: the link therefore lands on the serving original hub rather than on a same-named JP page; the bytes record that choice and T4 raised no item on it. The sample links inside the formatting exhibits (`[https://scp-wiki.wikidot.com/# …]`, `[https://google.com …]`, candidate in the sample zone) are exhibit text with translated labels, not navigation. The license entries' source links are section 1.
- **Why:** P11: prose links take the JP counterpart or the serving original, under the dead-reference evidence standard; exhibit labels follow P10.
- **Verify:** `grep -n 'sigma-9-themes\|scp-wiki.wikidot.com/#' candidate.txt` — the hub link and the sample link.
- **Disposition:** Standing; no dead link was found in this theme.

### 8. Structure

- **What:** The localize.md closing rule holds for everything the candidate carries: variable names, selectors, and the code exhibit's order are preserved, and the JP corrections arrive as the head delivery pair, the credit swap, and the license-box swap. An exhibit census confirms the shape: the usage code div, the image-block exhibit, the formatting samples (table, headings, lists, toc, fake-code, link samples), and the full CSS code exhibit are present on both sides in the same order. Two pairing details are normalized at the license zone (residue B54/B55): the candidate closes its centered wrapper (`[[/=]]`, candidate L894) immediately after the code exhibit's collapsible, where the original ran the wrapper through the license zone and closed it after the end include (original L914); the content inside is unchanged. The classifier's four EXHIBIT-RESTRUCTURE primaries adjudicate to sections 1–4 as listed in the class summary, so the R3 question (sanctioned replacement vs silent deletion) does not arise: the only exhibits that left are the tail furniture includes, whose ground is stated in section 2.
- **Why:** R3 exists to force exactly this adjudication, because a restructure and a deletion share a diff shape and ledger class I charges the silent form; here the census, not the label, decides.
- **Verify:** Compare `grep -n '\[\[code\|image-block\|license-box' original.txt candidate.txt` — the sequences correspond one to one.
- **Disposition:** Standing; no structural deletion, no class I item.

### 9. Formatting only

- **What:** None. The classifier finds no whitespace-only block and no re-indentation anywhere in the pair (0 and 0), so the R7 follow-up-diff hazard is not triggered.
- **Why:** Formatting churn is disclosed as its own class so it is never mistaken for a semantic change.
- **Verify:** The classification summary's WS-ONLY count is 0.
- **Disposition:** None required.

### 10. Porter annotations

- **What:** One annotation, riding inside another labeled block: the license box's third entry (candidate L910–912), which has no original counterpart and records the tabview.css provenance (distributed in the original as theme:flopstyle-dark's attachment; no license stated in the original; the reader is directed to the source theme's license statement). It rides inside the LICENSE-BOX block (B58), which is why no separate annotation signature fired; the skeleton's "none" for this section does not survive contact with the bytes and is corrected here. There are no comment-form annotations (`[!-- … --]`) and no editor lines in the candidate.
- **Why:** R2: porter-added text is part of the change record; this entry is load-bearing, because it is the only in-file attribution record for a file whose distribution changed (section 3).
- **Verify:** Read candidate L910–912; the original's license zone (original L894–912) has two entries, not three.
- **Disposition:** Standing.

### 11. Dispositions and exceptions

- **What:** Two items, each with its ground. (1) T1's five pseudo-ref errors: the candidate's own draft-host local--code and local--files lines (class (iii), sections 3–4) and the frame's production-host theme= line (class (ii) mechanics, section 3); the posting procedure rewrites or re-hosts the draft lines, and fix lanes never "fix" them in the candidate. (2) The render row's items, all environment or capture layer, not charged to the candidate: the runtime-hotlink site-theme chain (KB-40); the sample's credit-modal errors (KB-32: the preview form has no modal mechanism, ruling 5); and the page-overflow readings (823–829px at 768 on the page; 331px at 320 and 920px at 768 on the sample), recorded verbatim from RENDER-ROWS-2 without a candidate-side cause in the row.
- **Why:** A disposition is a decision with grounds (AGENTS.md §3 classes (i)/(ii)/(iii); the named KB entries), not an omission; environment-layer lines are recorded as not-charged.
- **Verify:** Each item names its deciding record above; the T1 classes are T1-ROWS row 119 and register (c1).
- **Disposition:** DISPOSITIONED (items 1–2).

### 12. Verification

- **What:** (a) T1 source check (T1-ROWS row 119): exit 1, 5 errors / 0 warns / 1 info; all five errors are pseudo-ref, classes (ii)/(iii); there is no class (i) error. (b) T2/T3 render (RENDER-ROWS-2, lane RENDER-S2-C (EN15)): FINDINGS, the three items of section 11(2), all dispositioned; engine coverage as run by the lane, not separately caveated in its row. (c) T4/T5 (LOCALIZE-ROWS row 119): PASS jointly, display-affecting findings 0; the ledger (c3) register carries no disposition line for this theme because nothing needed one. (d) This package is self-verifying: `python3 review/build_review.py --check` regenerates diff.md and the verdict stamp from the two byte-faithful copies in this directory and compares. Counts in this README are the generator's (difflib, autojunk off): +125/−142 in 59 change blocks / 5 hunks.
- **Why:** Verification claims name the cheapest deciding check and its result, not a general assurance.
- **Verify:** Re-run the checker on `pages/theme:pack-of-peanuts-jp.txt` and `python3 review/build_review.py --check` in this repo.
- **Disposition:** PASS (GOSIGN2-LEDGER (b) row 119; go-sign, COMPLETION-REPORT §10).

## Per-theme record

### The usage exhibit's slug (flagged by this package)

The usage exhibit (candidate L38) was repointed from `:scp-wiki:theme:pack-of-peanuts` to `:scp-jp:theme:pack-of-peanuts` at creation, keeping the plain slug. The candidate's own posting name is theme:pack-of-peanuts-jp, so the documented syntax names a page that will not exist under that name on scp-jp; the file's own delivery lines use the -jp form throughout (candidate L2, L7). This is the population-sweep family (the same shape is flagged in the plant and parawatch-pumpkin packages in this batch). The ledger's determination for this theme is PASS and this package does not re-open it; the line is flagged here with its locus, and the candidate is left unedited, as the sweep repairing this family is a coordinator matter.

## Change set outside the two diffed files

The diff covers two files; the port's record is one file larger. `pages/theme-decoration-sample-pack-of-peanuts-jp.txt` is the decoration sample the render checks ran against (its findings are the sample half of section 11(2)); it belongs to this theme's record but carries no port change of its own to explain here. The tabview.css copy the candidate imports lives in the candidate's own file area on the draft host (section 3); it is an uploaded asset, not a repo file. There are no companion fragments and no inbound-link repairs in other candidates for this theme.

## License and attribution

- **Title:** Pack Of Peanuts Theme
- **Author:** Lt Flops
- **Source:** https://scp-wiki.wikidot.com/theme:pack-of-peanuts — revision 45
- **License:** Creative Commons Attribution-ShareAlike 3.0 (CC BY-SA 3.0) — license deed: https://creativecommons.org/licenses/by-sa/3.0/
- **Adaptation:** This package holds a Sigma-10 migration port of the work; changes were made. See "Summary" and "Standing sections" in this README for what changed and why. Translator: AI (Muse and its delegated agents), per the campaign's standing attribution rule.
