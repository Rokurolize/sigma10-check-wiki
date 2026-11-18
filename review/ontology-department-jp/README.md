# Review package — theme:ontology-department-jp
New to this package's shorthand? Read the notation key first: [How to read a review package](../HOW-TO-READ.md).

<!-- BEGIN GENERATED VERDICT STAMP — do not hand-edit; regenerate with review/build_review.py -->
## Verdict stamp
- Theme: theme:ontology-department-jp — origin KO, population #278 [GOSIGN2-LEDGER (b) row 278]
- Overall: PASS — passed at the ledger determination; no OPEN items [GOSIGN2-LEDGER (b) row 278]
- T1 (source check): FINDINGS (classified) — baseline 2026-11-16: exit 1, 2 errors / 0 warns / 0 infos (pseudo-ref×2); standing classes dispositioned in register c1 [T1-ROWS row 282; GOSIGN2-LEDGER (b) row 278]
- T2/T3 (render, combined verdict): FINDINGS — [combined T2/T3] report `FINDINGS` — page-overflow 324px@320 (page) and 337–419px@320/375 (sample); sample credit-modal (preview-form); T3 none beyond cross-cutting items. [RENDER-ROWS-2 (RENDER-S2-H (KO6))]
- Engine coverage: full matrix as run by the lane; coverage not separately caveated in the row [RENDER-ROWS-2 row]
- Credit modal: sample credit-modal errors dispositioned preview-form (credit:start-preview has no modal mechanism; GOSIGN-TESTS T2 amendment, 2026-11-16) [RENDER-ROWS-2 (RENDER-S2-H (KO6))]
- T4 (localize patterns + follow-up): FINDINGS — display-affecting findings: 2 [LOCALIZE-ROWS row 277, source LOCALIZE-S2-F]
- T5 (translation text): FINDINGS — the source reports judge T4/T5 jointly; one verdict word covers both [LOCALIZE-ROWS row 277]
- FIX5 re-judgement: none — no OPEN items at the ledger determination [GOSIGN2-LEDGER (b) row 278]
- Computed against: canonical commit 1869877ffdcd33cb214b8dc421fb39e3de8d7e8d; candidate file pages/theme:ontology-department-jp.txt sha256:74a692789fd0499ce9b3eca4afe76d799dbfdb9f5e64ff7bf69be33aa6691b84; record: GOSIGN2-LEDGER.md + GOSIGN2-LEDGER-SUPPLEMENT.md as of the FIX5 head 435a6bb
<!-- END GENERATED VERDICT STAMP -->

## Status

| | |
|---|---|
| Verdict | **PASS** — passed at the ledger determination; this theme had no OPEN items and no §(e) register entry (GOSIGN2-LEDGER (b) row 278) |
| Standing items | **DISPOSITIONED** — T1 pseudo-ref ×2 (posting classes, section 11); the render row's overflow readings (cross-cutting families, section 11); T4's sandbox link (P11, section 7). **FIXED per the ledger** — the frame item (P6); this package records one record-vs-bytes tension about what that fix consists of (per-theme record) |
| Go-sign basis | COMPLETION-REPORT.md §10 (go-sign issued; 81 FIXED / 26 DISPOSITIONED / 0 OPEN across the sweep) |
| Named exception | None for this theme (the sweep's single named exception is theme:amethyst-v2, which has no candidate) |

## Provenance

| | Original | Candidate |
|---|---|---|
| Page | theme:ontology-department | theme:ontology-department-jp |
| Wiki | scpko.wikidot.com | SCP-JP Sigma-10 candidate (canonical repo) |
| Reference revision | 15 (first translation; the candidate's credit block records 初訳時参照リビジョン: 15) | — |
| Source of this copy | Campaign cache `gosign2-lanes/lane-oc-gs-localize-s2-F/orig-ontology-department.txt`, via the mirror store (class COPY, hash-verified against review/sources.tsv) | Canonical file `pages/theme:ontology-department-jp.txt`, copied at worktree HEAD 2aee861 |
| Lines / bytes | 219 lines / 6,195 bytes | 237 lines / 7,439 bytes |
| SHA-256 | 50fcc643c7ab89881858720fc46c6e0efc0ece042e0c9de5b135289c32be8a62 | 74a692789fd0499ce9b3eca4afe76d799dbfdb9f5e64ff7bf69be33aa6691b84 |

Wave history: the candidate was created by the Stage 2 KO6 integration (commit 8dd8c2f) and has exactly one later commit, FIX-CREDIT-D (1869877), whose hunk is the credit attribution normalization. No frame-wave commit touches this file — a fact the per-theme record weighs against the ledger's P6 line.

## Summary

A Black Highlighter variant for the KO Ontology Department, by Denevola, with the department logo by Didic. The port keeps the original's delivery architecture and re-hosts every layer of it: the head module's BHL imports move from the upstream jsdelivr build to the JP distribution on scp-jp.github.io, the font CSS the upstream stack carried disappears with it, the theme's own code import moves from the KO file host to its own JP code fragment, and the exhibit's Korean `@font-face` (GmarketSansBold) is replaced by a Google Fonts Noto Sans JP load with the stacks converted and the `:root:lang(ko)` scope becoming `:root:lang(ja)`. The info block becomes the JP credit block with two disclosure fields (fonts, image source), the two-layer attribution T4 praised — Denevola as author, Didic credited for the logo in the image field and again in the license box. The specimen body is translated in full (the bulk of the 50 blocks is one-line specimen translations). Measured churn (diff.md, the generator's difflib count with autojunk off: +126/−113 in 50 change blocks / 4 hunks). The frame paragraph below states this theme's variant form exactly, and the per-theme record states the one place where the ledger's wording and the file's history do not meet.

## Class summary

Auto-classification by review/classify_hunks.py (signature table 2026-11-17.1): 50 change blocks — 28 specific (56.0%), 20 heuristic (40.0%), 2 residue (4.0%), 0 skipped. Pattern citations below name the KB entry; the patterns/ tree state cited throughout is commit 9c5e9079afb01d30cb9fc4ef9d714e5591eb2ffa.

| Label | Blocks |
|---|---|
| TRANS-UNANCHORED | 19 |
| TRANSLATION-ANCHORED | 18 |
| CSS-BODY | 3 |
| COMPONENT-SWAP | 2 |
| ESCAPED-INCLUDE | 2 |
| IFTAGS | 2 |
| INCLUDE-REPOINT | 2 |
| SELF-DELIVERY | 2 |
| CREDIT-PREVIEW | 1 |
| DELIVERY-HOST | 1 |
| DRAFT-HOST | 2 |
| HEADERVAR | 1 |
| INFO-DEL | 1 |
| JPFONT-LOAD | 1 |
| LICENSE-BOX | 1 |
| TASL-FIELDS | 1 |

Adjudication for this README (every block was read against the bytes): the 37 translation labels are the specimen body, counted in section 6; the 3 CSS-BODY blocks are the P7 font-stack conversions (section 4), not generic CSS edits; the 2 residue blocks are translation boundaries (B4, the intro prose pair, whose diff alignment splits it from its labels; B39, a one-word specimen translation inside a blockquote), both adjudicated in the appendix. The skeleton's "none" readings do not survive for sections 3–4, whose signatures ride inside the delivery blocks. After adjudication no block is left unexplained.

## Standing sections

### 0. Header and provenance frame

- **What:** Theme theme:ontology-department-jp; original theme:ontology-department on scpko at reference revision 15; candidate `pages/theme:ontology-department-jp.txt`. Provenance route: derived from the original at the reference revision by the LOCALIZE-S2-F wave (sources.tsv kind: standard; no production JP counterpart exists). The frame itself moved: the original opens with its tag gate (original L1) ahead of its head module; the candidate opens with the delivery module and the two frames (candidate L1–15) and places the localized gate after them (candidate L17).
- **Why:** Section 0 declares the provenance route so every later count is read against the right baseline; the gate's tag is P2, the delivery stack is section 3.
- **Verify:** The sources.tsv row for ontology-department-jp; `sha256sum original.txt` against the Provenance table.
- **Disposition:** Standing (the route itself); the gate and delivery changes are recorded in section 3.

### 1. Credit and attribution

- **What:** The original's credit furniture is an unprefixed `[[include info:start]]`/`info:end` pair (original L8–11): the title and one field, author [[*user Denevola]]. A second attribution sits in the prose (original L14: the department logo was designed by [[*user Didic]]) and a third in the exhibit's banner comment (the logo "created by Didic and vectorized by Denevola. Licensed under CC BY-SA 3.0"). The candidate replaces the info pair with the JP credit block (candidate L18–28): a `:scp-jp:credit:start-preview`/`end-preview` block carrying all eight ruling-3 fields (title 存在学部ハイライター; 翻訳責任者 AI; 翻訳年 2026; 原題 존재학부 하이라이터; 著作権者 [[*user Denevola]]; 作成年 2021; 初訳時参照リビジョン 15; the source link, section 7) plus two disclosure fields — **フォント** (Noto Sans JP, Google Fonts, SIL OFL) and **画像の出典** (the logo re-hosted from SCP-KO; designed by Didic, vectorized by Denevola, CC BY-SA 3.0). The license box at the tail (candidate L228–236, `author=Denevola`) carries the logo's entry with the same two-name attribution. The author field matches the original's info block; the Didic attribution the original carries outside its author field is preserved in both places the JP form offers, which is the two-layer attribution the T4 record praised. No T7 credit-module CSS sits on this page.
- **Why:** P3/T1 (KB-09) for the furniture swap; the attribution check is the standing one — every name the original credits, in its info block, its prose, or its banner, must survive somewhere in the JP credit apparatus, and here all three do.
- **Verify:** Read candidate L18–28 and L228–236 against original L8–14 and the exhibit banner (original L116–123).
- **Disposition:** FIXED (GOSIGN2-LEDGER §(c3): P3 credit fields FIXED, credit waves, checker-verified).

### 2. Includes and components

- **What:** No live component include exists on either side; the include changes are the credit pair (section 1), the two frames (section 3), the license-box pair, and the usage exhibits (blocks B6, B8). The exhibits preserve the original's two-step usage form with repointed targets: `@@[[include :scp-jp:theme:black-highlighter-theme]]@@` then `@@[[include :scp-jp:theme:ontology-department-jp]]@@` (candidate L37–38), and the dark-sidebar variant adds `@@[[include :scp-jp:component:bhl-dark-sidebar]]@@` (candidate L43). Every include and exhibited include names a `:scp-jp:` target.
- **Why:** P1 (KB-15): the exhibits are instructions a reader copies, so their targets are held to the same standard as live includes — the base line names the JP BHL candidate (which keeps the base's own name), the theme line names this candidate, and the sidebar component names its JP port. Ruling 4 is not engaged: no component had to be ported alongside this theme (bhl-dark-sidebar is an existing JP component).
- **Verify:** `grep -n '\[\[include' candidate.txt` — frames, credit pair, license-box pair, and the five escaped exhibit lines, all `:scp-jp:`.
- **Disposition:** Applied; no foreign include kept, no named exception needed.

### 3. Delivery and code loading

- **What:** The delivery stack is re-hosted layer by layer. The original's head module (original L2–6) imports the BHL distribution from jsdelivr (Nu-SCPTheme's gh-pages build: normalize.min.css and black-highlighter.min.css) plus a NanumBarunCatsi font CSS from a third-party github.io; its own code arrives from a tail module (original L217–219) importing `local--code/theme%3Aontology-department/1` from scpko.wdfiles.com. The candidate's head module (candidate L1–5) imports the same two BHL files from the JP distribution (`scp-jp.github.io/Black-Highlighter/css/min/…`) and its own `local--code/theme%3Aontology-department-jp/1` from the draft host; the font CSS disappears with the upstream stack (its role is section 4's). The candidate has exactly one `[[code]]` block (the exhibit, candidate L134–225), so the /1 address names the block that holds the CSS — verified against the census. **Frame paragraph (the M-frame addition):** this candidate's frame takes the two-entry form (candidate L7–15): a first interwiki-style include at `priority=1` naming the JP distribution's normalize.min.css, and a second at `priority=2` naming its black-highlighter.min.css. There is no third frame entry naming the theme's own code: the own layer is delivered by the head module's `@import` above, not by a frame entry at priority 3. T4's record names exactly that absence (LOCALIZE-ROWS row 277, type 6: the priority=3 own-code entry missing, a frame display problem), and the ledger records P6 FIXED by the frame waves, checker-verified. The per-theme record below states what the file's own history shows about that fix, and this package narrates the delivered form as it stands: a layered delivery in which the frame carries the two base layers and the module import carries the theme's own.
- **Why:** P4/T9 for the stack (the JP distribution replaces the upstream build, so no layer depends on the KO wiki or a third-party host) and P6/T3 (KB-07) for the frame: the priorities are what order the layers, and a BHL port's frame state is a display fact, not a style point. The draft-host form of the own-code import is KB-41, class (iii).
- **Verify:** Read candidate L1–15; `grep -c '\[\[code' candidate.txt` — one; `grep -n 'jsdelivr\|XCninety\|Nu-SCPTheme' candidate.txt` returns nothing.
- **Disposition:** FIXED (P6, per the ledger's c3 line) with the per-theme record's caveat; the draft-host import is DISPOSITIONED (class (iii)).

### 4. Fonts and assets

- **What:** The load (block B44): the original exhibit's `@font-face` for GmarketSansBold (a jsdelivr noonfonts woff, original L125–131) is deleted, and the candidate's exhibit opens with a Google Fonts `@import` of Noto Sans JP (400;700;900) at candidate L143, immediately after the banner comment. The head module's NanumBarunCatsi import disappears with the upstream BHL stack (section 3) — it was the base's font CSS, not this theme's. Stacks (blocks B45, B47, B48, adjudicated here as P7): `--body-font`, `--header-font`, and `--title-font` in the `:root:lang(ja)` block gain 'Noto Sans JP' at the head (candidate L156–158), and the `#header h2` rule's stack likewise (candidate L190); the Latin faces the original named (Poppins, Franklin Gothic, Space Mono) are kept behind it. The language scope converts with the stacks: `:root:lang(ko)` → `:root:lang(ja)` (candidate L145). Assets: the department logo leaves the KO file host for the candidate's own draft-host file area (`--logo-image`, candidate L151, department-logo.svg, name unchanged), with its provenance in the credit block and license box (section 1).
- **Why:** P7/T5 with KB-16: GmarketSansBold has no Japanese coverage and its noonfonts load is not a JP-sanctioned host form, so the load and the stacks change together; Noto Sans JP is the JP face, and the `:lang()` scope must name the language the port serves or the JP variable set never applies.
- **Verify:** `grep -n 'GmarketSans\|NanumBarun' candidate.txt` returns nothing; read candidate L143–158 against original L125–146.
- **Disposition:** Conversions applied; the draft-host logo URL is DISPOSITIONED (class (iii) draft form).

### 5. Header, sidebar, and site furniture

- **What:** The header tokens sit in the exhibit's `:root:lang(ja)` block (block B46): `--logo-image` (section 4), `--header-title: "存在学部"` and `--header-subtitle: "因果、概念、物質"` (candidate L152–153) — the department name and its three-term motto, translated from the original's `:root:lang(ko)` values. The BHL base furniture arrives through the delivery stack (section 3); the theme's own sidebar rules travel inside the exhibit, and the dark-sidebar variant is a usage-time component include (section 2), not part of this page's delivery. The render row's overflow readings (324px@320 on the page; 337–419px@320/375 on the sample) are the cross-cutting BHL-family shapes recorded in section 11, not rules in this file.
- **Why:** P9/T6 applied: the header strings were translated, so KB-57 and ruling 2 are not engaged.
- **Verify:** Read candidate L145–160 against the original's `:root:lang(ko)` block (original L133–150).
- **Disposition:** Standing.

### 6. Text translation

- **What:** The specimen body is translated in full — 37 translation-labeled blocks (B7, B9–B43 passim), each a line or a small group: the intro prose (candidate L30–31, with the sandbox link treated in section 7), the usage sections, and the specimen set (horizontal rules, headings, blockquotes including the one-word B39 item, tables, text boxes, the collapsible labels). The exhibit's banner comment is carried verbatim in English on both sides (it is the author's own credit text, and its logo line is one of section 1's attribution sources). Korean survives in the candidate only in the credit block's original-title field (candidate L22). R5 glyph-form conversion: none — the source is Korean.
- **Why:** P10 (body and specimen translation) and KB-18 (reader-visible strings). The unanchored group was read line by line against the mirror for this README, because that group is where a silent deletion would hide; the census (section 8) confirms none occurred.
- **Verify:** The pairs are diff.md's body hunks in order; a Hangul scan of candidate.txt returns only candidate L22.
- **Disposition:** Standing (the port itself); no untranslated reader-visible text remains outside the one quotation.

### 7. Links

- **What:** The credit block's source link (candidate L24) names `https://scpko.wikidot.com/theme:ontology-department` — the host review/sources.tsv records for the original; no host defect. The intro's one prose link is T4's type-11 item: the Ontology Department's own page on the KO sandbox wiki, `[[[http://scpkosb.wikidot.com/collab:shark-bytes-44-5bde|存在学部]]]` (candidate L31), carried from the original's identical link (original L13) with its `http://` scheme unchanged. The ledger dispositions it P11 (sibling / batch-posting class): the department's hub lives on the KO sandbox, there is no JP counterpart page to repoint to, and the scheme is the posting-procedure class (ii) form.
- **Why:** P11 under the dead-reference evidence standard: the link serves its original page, and both of its apparent faults (foreign host, http scheme) are the recorded disposition classes, not oversights.
- **Verify:** `grep -n 'wikidot.com' candidate.txt` — the source link and the sandbox link.
- **Disposition:** DISPOSITIONED (P11; the scheme is class (ii)).

### 8. Structure

- **What:** The localize.md closing rule holds. Variable names, selectors, and channel order are preserved; the candidate's exhibit sits where the original's sits (original L116–212 → candidate L134–225), and the JP corrections arrive as the head stack (section 3) and the tail license box, not interleaved into the inherited CSS — inside the exhibit, the changes are the font load at its head, the `:root:lang(ja)` token block, the stack lines, and the logo repoint. An exhibit census confirms the shape: the specimen sections are present on both sides in the same order, and a brace-depth scan of the candidate's CSS closes at depth 0 with no negative excursion, so no rule is swallowed by a displaced brace. The classifier's one EXHIBIT-RESTRUCTURE primary (B8) is the dark-sidebar usage exhibit's include repoints, not a restructuring.
- **Why:** R3 exists to force exactly this adjudication; here the census and the depth scan, not the label, decide.
- **Verify:** Compare `grep -n '\[\[code\|\[\[module\|\[\[iftags' original.txt candidate.txt`; the depth scan is re-runnable over candidate.txt's exhibit.
- **Disposition:** Standing; no structural deletion, no class I item.

### 9. Formatting only

- **What:** None as its own class: the classifier finds no whitespace-only block and no re-indentation (0 and 0). The 2 residue blocks are translation boundaries, adjudicated in the appendix, not formatting.
- **Why:** Formatting churn is disclosed as its own class so it is never mistaken for a semantic change.
- **Verify:** diff.md's counts (+126/−113, 4 hunks).
- **Disposition:** None required.

### 10. Porter annotations

- **What:** None as comment-form annotations: the candidate carries no `[!-- --]` note and no CSS comment with no original counterpart (the exhibit's banner is the author's own, carried verbatim; the credit block's two disclosure fields are furniture, counted in section 1, and the 訳注 form does not appear in this candidate). The classifier's ANNOTATION label does not fire for this package, and a direct scan for comment markers confirms the skeleton's reading for once.
- **Why:** R2: porter-added text is part of the change record, and its absence is recorded so a reviewer can tell "checked, absent" from "not considered".
- **Verify:** `grep -n '\[!--' candidate.txt` returns nothing.
- **Disposition:** None — checked, absent.

### 11. Dispositions and exceptions

- **What:** Three items, each with its ground. (1) T1's two pseudo-ref errors: the candidate's delivery references to not-yet-posted JP addresses (the head module's own-code import among them) — classes (ii)/(iii) by form (KB-41 for the draft-host line); fix lanes never "fix" them in the candidate. (2) The render row's items, all cross-cutting, not charged to the candidate: the page-overflow readings at 320/375 (KB-33/KB-34 families: static credit replica and preview chrome shapes) and the sample's credit-modal errors (KB-32: the preview form has no modal mechanism, ruling 5). (3) T4's type-11 sandbox link, dispositioned P11 (section 7). T4's other item, the frame (type 6), is the ledger's FIXED with this package's caveat (per-theme record). The ledger's determination for this theme is PASS and this package does not re-open it.
- **Why:** A disposition is a decision with grounds (AGENTS.md §3 classes (i)/(ii)/(iii); the named KB entries), not an omission; environment-layer lines are recorded as not-charged.
- **Verify:** Each item names its deciding record above; the ledger §(c3) line for this theme reads P6 FIXED / P11 DISPOSITIONED.
- **Disposition:** DISPOSITIONED (items 1–3).

### 12. Verification

- **What:** (a) T1 source check (T1-ROWS row 282): exit 1, 2 errors / 0 warns / 0 infos; both errors are pseudo-ref, classes (ii)/(iii); there is no class (i) error. (b) T2/T3 render (RENDER-ROWS-2, lane RENDER-S2-H (KO6)): FINDINGS, the items of section 11(2), all dispositioned; engine coverage as run by the lane, not separately caveated in its row. (c) T4/T5 (LOCALIZE-ROWS row 277): FINDINGS jointly, display-affecting findings 2 (the frame entry, the sandbox link); the same row calls the BHL delivery source, the two-layer attribution, the `:root:lang(ja)` design, and the JP variables exemplary. (d) This package is self-verifying: `python3 review/build_review.py --check` regenerates diff.md and the verdict stamp from the two byte-faithful copies in this directory and compares. Counts in this README are the generator's (difflib, autojunk off): +126/−113 in 50 change blocks / 4 hunks; the brace-depth scan of section 8 was run for this package.
- **Why:** Verification claims name the cheapest deciding check and its result, not a general assurance.
- **Verify:** Re-run the checker on `pages/theme:ontology-department-jp.txt` and `python3 review/build_review.py --check` in this repo.
- **Disposition:** PASS (GOSIGN2-LEDGER (b) row 278; go-sign, COMPLETION-REPORT §10).

## Per-theme record

### The frame fix the file's history does not show (a record-vs-bytes tension, recorded not resolved)

T4's finding is precise (LOCALIZE-ROWS row 277, type 6): the priority=3 own-code entry was missing from the frame, a frame display problem, and the row adds that both of this theme's findings were easily fixable. The ledger's c3 line answers it: P6 FIXED (frame waves; checker-verified). But this candidate's commit history contains no frame-wave edit: the file was created by the KO6 integration (8dd8c2f) and touched once since, by the credit normalization (1869877), whose hunk is in the credit block. The FIX4-IWA and FIX4-IWB reports, which record the frame waves' per-theme work, do not name this theme. And the bytes still show the form T4 described: frame entries at priorities 1 and 2 naming the base distribution's files, and the own layer delivered by the head module's `@import`, with no priority=3 frame entry. Two readings are possible: the frame waves' checker verification adjudged this delivered form compliant (the layering is complete and ordered — normalize, base, own — with the own layer arriving by import rather than by frame entry), and "FIXED" records that adjudication; or the c3 line is the batch's templated P6 wording applied where no edit occurred. This package cannot decide between them from its own evidence, and it does not need to: the delivered form is stated exactly in section 3, the ledger's disposition is quoted exactly here, and the tension between the FIXED wording and the file's edit history is on record for the coordinator. What the package does not do is narrate a priority=3 entry that the bytes do not contain.

## Change set outside the two diffed files

The diff covers two files; the port's record is one file larger. `pages/theme-decoration-sample-ontology-department-jp.txt` is the decoration sample the render checks ran against (its findings are the sample half of section 11(2)); it belongs to this theme's record but carries no port change of its own to explain here. There are no companion fragments, no shared base file beyond the BHL distribution the delivery stack names, and no inbound-link repairs in other candidates for this theme.

## Appendix — residue blocks

| Block | Shape | Adjudication |
|---|---|---|
| B4 | orig L13–15 → cand L12–16 by the diff's alignment; the intro prose pair (the department sentence and the logo-designer sentence) | Translation (section 6); the alignment splits the pair from its labels, and the sandbox link it carries is section 7 |
| B39 | orig L103–104 → cand L121–122, one word inside a blockquote specimen (글자 → 文字） | Translation (section 6) |

## License and attribution

- **Title:** 존재학부 하이라이터
- **Author:** Denevola
- **Source:** https://scpko.wikidot.com/theme:ontology-department — revision 15
- **License:** Creative Commons Attribution-ShareAlike 3.0 (CC BY-SA 3.0) — license deed: https://creativecommons.org/licenses/by-sa/3.0/
- **Adaptation:** This package holds a Sigma-10 migration port of the work; changes were made. See "Summary" and "Standing sections" in this README for what changed and why. Translator: AI (Muse and its delegated agents), per the campaign's standing attribution rule.
