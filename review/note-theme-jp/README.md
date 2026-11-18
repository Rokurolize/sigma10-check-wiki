# Review package — theme:note-theme-jp (KO → JP port)

<!-- BEGIN GENERATED VERDICT STAMP — do not hand-edit; regenerate with review/build_review.py -->
## Verdict stamp
- Theme: theme:note-theme-jp — origin KO, population #277 [GOSIGN2-LEDGER (b) row 277]
- Overall: PASS — passed at the ledger determination; no OPEN items [GOSIGN2-LEDGER (b) row 277]
- T1 (source check): FINDINGS (classified) — baseline 2026-11-16: exit 1, 6 errors / 0 warns / 1 info (pseudo-ref×6); standing classes dispositioned in register c1 [T1-ROWS row 281; GOSIGN2-LEDGER (b) row 277]
- T2/T3 (render, combined verdict): FINDINGS — [combined T2/T3] report `FINDINGS` — page-overflow 378px@375 (page) and 378px@375 + 884px@768 (sample); sample credit-modal (preview-form); T3 none beyond cross-cutting items. [RENDER-ROWS-2 (RENDER-S2-H (KO6))]
- Engine coverage: full matrix as run by the lane; coverage not separately caveated in the row [RENDER-ROWS-2 row]
- Credit modal: sample credit-modal errors dispositioned preview-form (credit:start-preview has no modal mechanism; GOSIGN-TESTS T2 amendment, 2026-11-16) [RENDER-ROWS-2 (RENDER-S2-H (KO6))]
- T4 (localize patterns + follow-up): PASS — display-affecting findings: 0 [LOCALIZE-ROWS row 276, source LOCALIZE-S2-F]
- T5 (translation text): PASS — the source reports judge T4/T5 jointly; one verdict word covers both [LOCALIZE-ROWS row 276]
- FIX5 re-judgement: none — no OPEN items at the ledger determination [GOSIGN2-LEDGER (b) row 277]
- Computed against: canonical commit 1869877ffdcd33cb214b8dc421fb39e3de8d7e8d; candidate file pages/theme:note-theme-jp.txt sha256:435c9567532c48237f28ba61f7ea97a66cd9bf48103195bb085ab1041d2b60e3; record: GOSIGN2-LEDGER.md + GOSIGN2-LEDGER-SUPPLEMENT.md as of the FIX5 head 435a6bb
<!-- END GENERATED VERDICT STAMP -->

## Status

| | |
|---|---|
| Verdict | **PASS** — passed at the ledger determination; this theme had no OPEN items and no §(e) register entry (GOSIGN2-LEDGER (b) row 277). Its T4/T5 row is one of the population's clean PASS/PASS rows |
| Standing items | **DISPOSITIONED** — T1's six pseudo-ref errors (the draft-host delivery and asset addresses, class (iii)); the render row's items (378px@375 overflow on page and sample, 884px@768 on the sample, the credit-modal preview form; section 11). No defect flags and no per-theme record items arise for this theme |
| Go-sign basis | COMPLETION-REPORT.md §10 (go-sign issued; 81 FIXED / 26 DISPOSITIONED / 0 OPEN across the sweep) |
| Named exception | None for this theme (the sweep's single named exception is theme:amethyst-v2, which has no candidate) |

## Provenance

| | Original | Candidate |
|---|---|---|
| Page | theme:note-theme | theme:note-theme-jp |
| Wiki | scpko.wikidot.com | SCP-JP Sigma-10 candidate (canonical repo) |
| Reference revision | 20 (first translation; the candidate's credit block records 初訳時参照リビジョン: 20) | — |
| Source of this copy | Campaign cache `gosign2-lanes/lane-oc-gs-localize-s2-F/orig-note-theme.txt`, via the mirror store (class COPY, hash-verified against review/sources.tsv) | Canonical file `pages/theme:note-theme-jp.txt`, copied at worktree HEAD 4e6b126 |
| Lines / bytes | 202 lines / 5,253 bytes | 245 lines / 8,169 bytes |
| SHA-256 | d623bac0e327638062b3ed22ebff201a01ca89432eddc7e1313a5c49b8e5a036 | 435c9567532c48237f28ba61f7ea97a66cd9bf48103195bb085ab1041d2b60e3 |

Wave history: the candidate was created by the Stage 2 KO6 integration (commit 8dd8c2f, the LOCALIZE-S2-F wave's port) and has one later commit: 1869877 (FIX-CREDIT-D, the credit and license supplement wave; the verdict stamp's computed-against commit), which added the credit block's supplementary lines and the license box of section 1. No FIX5 commit touches this file, because the theme had no OPEN items for FIX5 to re-judge.

## Summary

A small, self-contained KO theme (a single 189-line CSS exhibit) whose port is the batch's cleanest: T4/T5 PASS outright, and every change is one of the standard moves. The head-module import is repointed to the draft host and the interwiki-style frame is added; the bare Rate exhibit is deleted and the JP preview credit block installed, carrying two supplementary lines (fonts, image sources) beyond the eight fields; the exhibit's KO display faces (Kirang Haerang, Poor Story) and its TC serif are replaced by JP faces (Yomogi, Noto Serif JP) while Nanum Myeongjo and Crimson Pro are kept, with the stacks, the banner's font line, and the credit block's font line all telling the same story; the theme's five images, which the original addresses relatively, are re-hosted to the candidate's own draft-host file area; and a license box is appended whose five entries credit the banner's named designers where the banner names them and state honestly where the original gives no license. Measured churn (diff.md: +73/−30 in 13 hunks; classification.json: 25 change blocks) is dominated by the credit block and license box additions.

## Class summary

Auto-classification by review/classify_hunks.py (signature table 2026-11-17.1): 25 change blocks — 13 specific (52%), 11 heuristic (44%), 1 residue (4%), 0 skipped. Pattern citations below name the KB entry; the patterns/ tree state cited throughout is commit 9c5e9079afb01d30cb9fc4ef9d714e5591eb2ffa.

| Label | Blocks |
|---|---|
| CSS-BODY | 11 |
| DRAFT-HOST | 6 |
| SELF-DELIVERY | 2 |
| IFTAGS | 2 |
| TRANS-UNANCHORED | 2 |
| CONTENT-STRING | 2 |
| TRANSLATION-ANCHORED | 2 |
| DELIVERY-HOST | 1 |
| BARE-RATE-DEL | 1 |
| COMPONENT-SWAP | 1 |
| CREDIT-PREVIEW | 1 |
| TASL-FIELDS | 1 |
| JPFONT-LOAD | 1 |
| FONT-IMPORT | 1 |
| WS-ONLY | 1 |
| LICENSE-BOX | 1 |

Adjudication for this README (every block was read against the bytes): the eleven CSS-BODY heuristic blocks are single lines inside the exhibit, and by content they are the P7 font-stack rewrites of section 4 (for example original L32's `'Poor Story', cursive` → candidate L45's `'Yomogi', 'Noto Serif JP', cursive`) — the standing adjudication for this batch, applied here eleven times. The one residue block, B6, is resolved: it is the exhibit banner's font-attribution line (original L27 → candidate L40), rewritten to name the port's font set (section 4); it is R1 in-CSS text, porter-visible only, and it is the banner's only edited line. B3's COMPONENT-SWAP primary is the head block that carries the frame and the credit block together. After adjudication no block is left unexplained; the residue appendix the class M convention provides for is this paragraph, the residue count being one.

## Standing sections

### 0. Header and provenance frame

- **What:** Theme theme:note-theme-jp; original theme:note-theme on scpko at reference revision 20; candidate `pages/theme:note-theme-jp.txt`. Provenance route: derived from the original at the reference revision by the LOCALIZE-S2-F wave (sources.tsv kind: standard; no production JP counterpart exists for this theme, so the R4 adoption question does not arise). The frame moved: the original opens with its delivery module and gate (original L1–4); the candidate opens with the delivery module, the interwiki-style frame (candidate L5–8), and then the localized gate (candidate L10).
- **Why:** Section 0 declares the provenance route and the topology baseline; the gate's tag is P2, the frame is P6/T3.
- **Verify:** The sources.tsv row for note-theme-jp; `sha256sum original.txt` against the Provenance table.
- **Disposition:** Standing (the route itself); the delivery changes are recorded in section 3.

### 1. Credit and attribution

- **What:** The original's credit furniture is a bare `[[module Rate]]` in a centering block (original L5–7) and the exhibit's banner comment (original L20–28: "Created by blackmagpie; Logo designed by thd-glasses; Header designed by TheAlice; Originally based on SCP Sigma 9 Theme created by Aelanna and Dr Devan; CC BY-SA 3.0"); it has no credit module pair at all. The candidate deletes the Rate exhibit and installs the JP form: a `:scp-jp:credit:start-preview`/`end-preview` block directly under the gate (candidate L11–24) carrying the eight ruling-3 fields plus two supplementary lines of the FIX-CREDIT-D form (fonts; image sources). Values: title 真昼の樫の旅回り一座テーマ; 翻訳責任者 AI; 翻訳年 2026; 原題 한낮의 떡갈나무 유랑극단 테마, the original's Korean title kept as the original-title field; 著作権者 [[*user blackmagpie]]; 作成年 2019; 初訳時参照リビジョン 20; the source link (candidate L19) on scpko.wikidot.com, the host sources.tsv records for the original, its label the theme's Korean title. Author check against the original: blackmagpie is the banner's creator; the banner's two further contributors are credited in the candidate in two places — the supplementary 画像の出典 line (candidate L21: ロゴデザイン: thd-glasses、ヘッダーデザイン: TheAlice) and the license box entries (below) — so no creator the original names is dropped, and no flag of the sibling standing arises. License entries: a `:scp-jp:component:license-box-backend` box is appended after the code exhibit, still inside the gate (candidate L216–244), with five entries (header.jpg, logo.png, note-1.png, note-2.png, note-3.png): the two designed files carry their banner designers as 作者 (TheAlice, thd-glasses, each marked 原語版クレジット表記による), the three note images state 原語版に記載なし for author, and every entry states honestly that the original gives no license （原語版に記載なし, with the note 投稿前に著者へ確認してください) and cites its scpko source URL. T7 credit-module CSS: the theme carries no credit-rule group in its CSS on either side, so no T7 item arises.
- **Why:** P3/T1: the preview credit module is the rate-bearing JP form, so the bare Rate is deleted rather than duplicated (a kept Rate would be the KB-09 duplicate). Ruling 3 fixes the eight fields; the supplementary lines and the license box are the FIX-CREDIT-D wave's completion of the credit record (the stamp's computed-against commit), and their honesty about the missing licenses is the point of the form.
- **Verify:** `grep -n 'module Rate\|credit:start\|license-box' candidate.txt` returns the preview pair at L11 and L24 and the license pair at L216 and L244; read candidate L11–24 against the fields above.
- **Disposition:** Applied; no credit item is charged in the theme's T4 row (PASS).

### 2. Includes and components

- **What:** The candidate's live includes are five: the interwiki-style frame (candidate L5–8, section 3), the credit pair (section 1), and the license-box pair (section 1). The usage example changes form: the original's bare `@@[[include theme:note-theme]]@@` (original L11) becomes `@@[[include :scp-jp:theme:note-theme-jp]]@@` (candidate L27), naming the candidate's own fullname with the site prefix — the correct page under the posting name, in contrast to the plain-slug shape flagged in sibling packages. No component include exists on either side beyond the frame, credit, and license components, so no P1 repoint and no ruling-4 port arises.
- **Why:** P1 is satisfied by the self-reference naming the page that will exist; the frame, credit, and license includes are sections 3 and 1.
- **Verify:** `grep -n '\[\[include' candidate.txt` — five live includes, all `:scp-jp:`.
- **Disposition:** Applied; no foreign include kept, no named exception needed.

### 3. Delivery and code loading

- **What:** The original delivers its own CSS by importing its code exhibit from the KO wdfiles host: a head `[[module CSS]]` with `@import url(https://scpko.wdfiles.com/local--code/theme%3Anote-theme/1)` (original L1–3). The candidate converts the delivery to the standard JP form: the head module imports the exhibit from the draft host under the candidate's own name (candidate L2), and the interwiki-style frame follows at priority=1 naming the same address (candidate L5–8). The exhibit itself (original L13–201, 189 lines) stands in the candidate at L27–214 (188 lines), its internal changes being sections 4 and 6 only. No appendix module and no second copy exists; the topology is the population's standard one.
- **Why:** P4/T9 (own-code delivery re-hosted to JP hosts: scpko.wdfiles → the JP draft host, class (iii) mechanics) and P6/T3 (the interwiki-style frame).
- **Verify:** `grep -n 'local--code' candidate.txt` returns candidate L2 and L7 only, both on the draft host.
- **Disposition:** Applied (class (iii) mechanics; T1's six pseudo-ref errors are this section's addresses and section 4's, register c1).

### 4. Fonts and assets

- **What:** Loads: the original's exhibit loads five faces in three Google Fonts lines (original L15–17: Kirang Haerang, Noto Serif TC, and Poor Story; Nanum Myeongjo; Crimson Pro). The candidate loads four faces in two lines (candidate L29–30: Crimson Pro, Noto Serif JP, and Yomogi combined; Nanum Myeongjo). The substitutions: the two KO display faces (Kirang Haerang, Poor Story) and the TC serif are dropped, Yomogi (a JP handwriting face) and Noto Serif JP take their places, and Nanum Myeongjo (a KO serif the theme uses for Korean-text passages) and Crimson Pro are kept. Stacks: the display stack `'Poor Story', cursive` becomes `'Yomogi', 'Noto Serif JP', cursive` (original L32 → candidate L45), and the remaining stack lines take the same faces (the eleven CSS-BODY blocks, adjudicated in the class summary as P7). The banner's font line is rewritten to name the new set (original L27 → candidate L40, the package's one residue block, resolved there), and the credit block's フォント line (candidate L20) lists the same four faces with their license note — loads, stacks, banner, and credit field agree. Load-gap check: every first-named face in the candidate's stacks (Yomogi, Noto Serif JP, Nanum Myeongjo, Crimson Pro) is loaded by the exhibit's own imports; there is no KB-16 gap. Assets: the theme's five images are addressed relatively in the original (`/local--files/theme:note-theme/header.jpg`, original L43) and become absolute draft-host addresses under the candidate's own file area in the port (candidate L56: `https://sigma10-jp-test.wdfiles.com/local--files/theme%3Anote-theme-jp/header.jpg`), four more on the same pattern (the DRAFT-HOST blocks B9, B17, B21 and the credit line's list); the credit block's 画像の出典 line records the re-host (candidate L21: SCP-KO より再ホスト, naming all five files). The draft host is class (iii) mechanics, converting to the production host at posting.
- **Why:** P7 (the JP faces replace the KO/TC faces in load and stack together; a kept KO serif with a real function, Nanum Myeongjo, is not a P7 failure) and P5/T9 (the images served from the candidate's own JP file area rather than the KO wiki's).
- **Verify:** `grep -n '@import\|font-family' candidate.txt` against the lines cited; `grep -n 'sigma10-jp-test.wdfiles.com/local--files' candidate.txt` returns the five asset lines.
- **Disposition:** Applied (class (iii) mechanics for the asset host).

### 5. Header, sidebar, and site furniture

- **What:** The theme's header is a designed image (header.jpg, section 4) with a text overlay: the `#header h1 a:before` content string is the theme's name in Korean in the original (original L52) and is translated in the candidate (candidate L65: 「真昼の樫」流浪劇団 — a shorter rendering of the same name than the credit block's full title, both carried in section 6). The theme sets no `--header-title` or `--logo-image` variable on either side. No sidebar furniture exists in this theme. The render row's one layout item is the overflow, recorded in section 11.
- **Why:** P9/T6 do not apply to a theme that sets no header variables; the header string is a KB-18 reader-visible string, counted in section 6.
- **Verify:** `grep -n -- '--header-title\|--logo-image' candidate.txt` returns nothing; the content string is at candidate L65.
- **Disposition:** Standing.

### 6. Text translation

- **What:** The prose is short (a usage paragraph, original L10–11 → candidate L26–27) and is translated in full. Reader-visible CSS strings (the CONTENT-STRING blocks B10 and B12): the header overlay string above and one further display string take Japanese forms (original L52 → candidate L65; original L65 → candidate L78). The title is rendered 真昼の樫の旅回り一座テーマ in the credit block, with the Korean original kept in the 原題 field; the header overlay uses the shorter 「真昼の樫」流浪劇団 form — two renderings of one name, the field carrying the full theme name and the overlay the display short form, recorded here so the difference is visible rather than smoothed over. In-CSS text (R1): the banner comment is carried verbatim except its font line (section 4). Korean survives in the candidate in the credit block's original-title field and its source-link label (candidate L18–19), where it is quotation.
- **Why:** P10 (usage translation) and KB-18 (reader-visible strings, including the header overlay).
- **Verify:** The body sections of diff.md; a Korean-prose scan of candidate.txt outside the credit fields returns nothing.
- **Disposition:** Standing (the port itself); T4/T5 PASS for this theme.

### 7. Links

- **What:** No prose links exist in this theme on either side beyond the credit block's source link (candidate L19), which names scpko.wikidot.com — the host sources.tsv records for the original — and serves the original, its label the theme's Korean title. The license entries' source links (candidate L219–243) name the scpko file pages they cite. Nothing else outbound exists outside the delivery and asset addresses of sections 3 and 4.
- **Why:** P11 has no item where no prose link exists; the source link is the attribution record.
- **Verify:** `grep -n 'wikidot.com' candidate.txt` — the source link and the license citations only.
- **Disposition:** Standing.

### 8. Structure

- **What:** No deviation from the localize.md closing rule: variable names, selectors, and rule order inside the exhibit are preserved, the exhibit stands at its original length within a line (189 → 188 lines, the difference being the merged font-import line of section 4), and the exhibit census (the one code exhibit, the usage prose) corresponds one to one, so no R3 deletion arises. The additions (frame, credit block, license box) stand outside the exhibit, in the furniture zones where the population puts them.
- **Why:** R3's distinction (sanctioned replacement vs silent deletion) is decided by the census, not by the label.
- **Verify:** Compare `grep -n '\[\[code\|\[\[module' original.txt candidate.txt`.
- **Disposition:** Standing; no class I item.

### 9. Formatting only

- **What:** One WS-ONLY block (B24: original L192 → candidate L205), a single whitespace-only line pair inside the exhibit, disclosed so it is not mistaken for semantic change. The classifier finds 0 re-indentation blocks, so there is no wholesale R7 re-indent.
- **Why:** Formatting churn is disclosed as its own class; the follow-up-diff hazard is limited to this one line.
- **Verify:** The WS-ONLY entry in classification.json.
- **Disposition:** None required.

### 10. Porter annotations

- **What:** None — checked, not assumed: the candidate adds no comment-form annotation (no `[!-- --]` note and no added CSS comment; the banner comment is the original's own with its font line updated, section 4, and the license entries' parenthetical notes are credit-record text, section 1, not annotations). The port's judgments are documented in the credit block's supplementary lines instead of in comments.
- **Why:** R2 requires the check to be explicit, because annotations ride inside other labeled blocks in sibling packages; here the grep is the evidence.
- **Verify:** `grep -n '\[!--' candidate.txt` returns nothing; compare the CSS comments on both sides of diff.md.
- **Disposition:** None — checked, absent.

### 11. Dispositions and exceptions

- **What:** Two items, each with its ground. (1) T1's six pseudo-ref errors: the draft-host addresses of sections 3 and 4 (the delivery pair and the five asset lines), class (iii) mechanics, DISPOSITIONED in register c1. (2) The render row's items (RENDER-ROWS-2, lane RENDER-S2-H (KO6)), none charged to the candidate at the ledger determination: the 378px@375 overflow on page and sample and the sample's 884px@768 overflow, recorded verbatim; and the sample's credit-modal errors (KB-32: the preview form has no modal mechanism, ruling 5). T4/T5 charged nothing at all (PASS/PASS), so this theme's disposition list is the batch's shortest.
- **Why:** A disposition is a decision with grounds (AGENTS.md §3 classes (i)/(ii)/(iii); the named KB entries), not an omission; environment-layer lines are recorded as not-charged.
- **Verify:** Each item names its deciding record above.
- **Disposition:** DISPOSITIONED (items 1–2).

### 12. Verification

- **What:** (a) T1 source check (T1-ROWS row 281): exit 1, 6 errors / 0 warns / 1 info; all six errors are pseudo-ref, class (iii); there is no class (i) error. (b) T2/T3 render (RENDER-ROWS-2, RENDER-S2-H (KO6)): FINDINGS, the items of section 11(2), all dispositioned; engine coverage as run by the lane, not separately caveated in its row. (c) T4/T5 (LOCALIZE-ROWS row 276, LOCALIZE-S2-F): PASS / PASS jointly, display-affecting findings 0 — the batch's only clean T4 pass alongside its KO siblings. (d) This package is self-verifying: `python3 review/build_review.py --check` regenerates diff.md and the verdict stamp from the two byte-faithful copies in this directory and compares. Counts in this README are the generator's (diff.md): +73/−30 in 13 hunks, 25 classified change blocks.
- **Why:** Verification claims name the cheapest deciding check and its result, not a general assurance.
- **Verify:** Re-run the checker on `pages/theme:note-theme-jp.txt` and `python3 review/build_review.py --check` in this repo.
- **Disposition:** PASS (GOSIGN2-LEDGER (b) row 277; go-sign, COMPLETION-REPORT §10).

## Change set outside the two diffed files

The diff covers two files; the port's record is one file larger. `pages/theme-decoration-sample-note-theme-jp.txt` is the decoration sample the render checks ran against (its findings are the sample half of section 11(2)). There are no companion fragments, no shared base file, and no inbound-link repairs in other candidates for this theme.

## License and attribution

- **Title:** 한낮의 떡갈나무 유랑극단 테마
- **Author:** blackmagpie
- **Source:** https://scpko.wikidot.com/theme:note-theme — revision 20
- **License:** Creative Commons Attribution-ShareAlike 3.0 (CC BY-SA 3.0) — license deed: https://creativecommons.org/licenses/by-sa/3.0/
- **Adaptation:** This package holds a Sigma-10 migration port of the work; changes were made. See "Summary" and "Standing sections" in this README for what changed and why. Translator: AI (Muse and its delegated agents), per the campaign's standing attribution rule.
