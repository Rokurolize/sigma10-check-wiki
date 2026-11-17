# Review package — theme:chatscp-jp

<!-- BEGIN GENERATED VERDICT STAMP — do not hand-edit; regenerate with review/build_review.py -->
## Verdict stamp
- Theme: theme:chatscp-jp — origin KO, population #256 [GOSIGN2-LEDGER (b) row 256]
- Overall: STALE — candidate file changed since the verdict was computed (verdict against 435a6bb-era content, file sha256 now 9cac88d942d351ab13bcf45c395217a19766bb7ae676a1d305877692a6f46e6b); verdict not carried over, re-judgement required
> verdicts below describe the pre-change file
- T1 (source check): FINDINGS (classified) — baseline 2026-11-16: exit 1, 1 error / 3 warns / 1 info (pseudo-ref×1); standing classes dispositioned in register c1 [T1-ROWS row 239; GOSIGN2-LEDGER (b) row 256]
- T2/T3 (render, combined verdict): FINDINGS — [combined T2/T3] report `FINDINGS` — hidden-license on both pages (all combos) + page sidebar-not-opening; sample credit-modal (preview-form); T3 Wikidot footer/license bar renders as a fixed overlay at left-centre over the body at every viewport (theme-specific; machine hidden-license agrees). [RENDER-ROWS-2 (RENDER-S2-H (KO2))]
- Engine coverage: full matrix as run by the lane; coverage not separately caveated in the row [RENDER-ROWS-2 row]
- Credit modal: sample credit-modal errors dispositioned preview-form (credit:start-preview has no modal mechanism; GOSIGN-TESTS T2 amendment, 2026-11-16) [RENDER-ROWS-2 (RENDER-S2-H (KO2))]
- T4 (localize patterns + follow-up): FINDINGS — display-affecting findings: 2 [LOCALIZE-ROWS row 255, source LOCALIZE-S2-F]
- T5 (translation text): FINDINGS — the source reports judge T4/T5 jointly; one verdict word covers both [LOCALIZE-ROWS row 255]
- FIX5 re-judgement: none — no OPEN items at the ledger determination [GOSIGN2-LEDGER (b) row 256]
- Computed against: canonical commit b5cb7241f527a44933e45599b41df210690771c4; candidate file pages/theme:chatscp-jp.txt sha256:9cac88d942d351ab13bcf45c395217a19766bb7ae676a1d305877692a6f46e6b; record: GOSIGN2-LEDGER.md + GOSIGN2-LEDGER-SUPPLEMENT.md as of the FIX5 head 435a6bb
<!-- END GENERATED VERDICT STAMP -->

## Status

| | |
|---|---|
| Verdict | **PASS** — passed at the ledger determination; this theme had no OPEN items and no §(e) register entry (GOSIGN2-LEDGER (b) row 256) |
| Standing items | **DISPOSITIONED** — T1 pseudo-ref ×1 (class (ii), section 11); the render row's items (hidden-license on both pages, the footer/license overlay, sidebar, credit-modal preview form, section 11); T4's items (deleted inline samples, four red links, credit title wording, exhibit placeholders), each with its ledger disposition in section 11 |
| Go-sign basis | COMPLETION-REPORT.md §10 (go-sign issued; 81 FIXED / 26 DISPOSITIONED / 0 OPEN across the sweep) |
| Named exception | None for this theme (the sweep's single named exception is theme:amethyst-v2, which has no candidate) |

## Provenance

| | Original | Candidate |
|---|---|---|
| Page | theme:chatscp | theme:chatscp-jp |
| Wiki | scpko.wikidot.com | SCP-JP Sigma-10 candidate (canonical repo) |
| Reference revision | 4 (first translation; the candidate's credit block records 初訳時参照リビジョン: 4) | — |
| Source of this copy | Campaign cache `gosign2-lanes/lane-oc-gs-localize-s2-F/orig-chatscp.txt`, via the mirror store (class COPY, hash-verified against review/sources.tsv) | Canonical file `pages/theme:chatscp-jp.txt`, copied at worktree HEAD 1605bbd |
| Lines / bytes | 456 lines / 9,209 bytes | 466 lines / 9,929 bytes |
| SHA-256 | aa5a82eff6f31ac4085e8f55146e6a79c87edd7d4dcdfeaba6f85e17f630ccac | f53ca2d47e926e24698e54b0be5b7487e17808cc883566754db8832081d69d7a |

Wave history: the candidate was created by the Stage 2 KO2 integration (commit d72b7b9, the LOCALIZE-S2-F wave's port) and has exactly one later commit, 1869877 (FIX-CREDIT-D, the translator-attribution normalization that swept all candidates). No FIX5 commit touches this file, because the theme had no OPEN items for FIX5 to re-judge.

## Summary

A joke theme (a ChatGPT parody skin for the KO wiki's 2023 April Fools event) whose page is written as a fake chat: question and answer divs all the way down, with the theme's CSS carried in a shown module. The port translates the conversation, swaps the bare Rate and the empty info pair for the preview credit block, moves the CSS body into the source-code exhibit form and serves it from the tail frame (own local--code on the draft host, interwiki-style at priority 1), and repoints the one usage include. Two recorded costs stand in the open: the three small sample code blocks inside the Q&A were deleted, leaving the code bars the prose introduces empty (T4's type-10 item, dispositioned by the ledger as a specimen-class P10 outcome); and four bare prose links name pages that do not exist on scp-jp, so they render as red links (T4's type-11 item, P11 dispositioned). Measured churn (diff.md, the generator's difflib count with autojunk off: +121/−111 in 32 change blocks; a GNU-diff count of the same pair gives 132 changed lines — here the generator's count is the loose one, because the relocated CSS body defeats its alignment where GNU's tighter matching finds the moved lines; the difference is alignment, not content).

## Class summary

Auto-classification by review/classify_hunks.py (signature table 2026-11-17.1): 32 change blocks — 16 specific (50.0%), 15 heuristic (46.9%), 1 residue (3.1%), 0 skipped. Pattern citations below name the KB entry; the patterns/ tree state cited throughout is commit 9c5e9079afb01d30cb9fc4ef9d714e5591eb2ffa.

| Label | Blocks |
|---|---|
| TRANS-UNANCHORED | 17 |
| DELIVERY-MOVE | 8 |
| EXHIBIT-RESTRUCTURE | 4 |
| IFTAGS | 3 |
| INCLUDE-REPOINT | 2 |
| BARE-RATE-DEL | 1 |
| CREDIT-PREVIEW | 1 |
| CREDIT-PROSE | 1 |
| DRAFT-HOST | 1 |
| ESCAPED-INCLUDE | 1 |
| INFO-DEL | 1 |
| LINK-REPOINT | 1 |
| SELF-DELIVERY | 1 |
| TASL-FIELDS | 1 |
| TRANSLATION-ANCHORED | 1 |

Adjudication for this README (every block was read against the bytes): the 15 heuristic blocks are the Q&A prose translations (TRANS-UNANCHORED primaries, section 6), verified exchange by exchange; the one residue block is a Q&A exchange the anchor test could not pair, counted in section 6 with its fellows. The 8 DELIVERY-MOVE blocks are the CSS body's move from the shown module to the code-exhibit-plus-tail-delivery form (section 3). The 4 EXHIBIT-RESTRUCTURE primaries are real and are adjudicated in section 8: the three deleted inline samples and the Q&A frame's reshaping. After adjudication no block is left unexplained.

## Standing sections

### 0. Header and provenance frame

- **What:** Theme theme:chatscp-jp; original theme:chatscp on scpko at reference revision 4; candidate `pages/theme:chatscp-jp.txt`. Provenance route: derived from the original at the reference revision by the LOCALIZE-S2-F wave (sources.tsv kind: standard; no production JP counterpart exists for this theme, so the R4 adoption question does not arise). The frame: the original opens with the gate (L1), Rate and info pair, and runs its Q&A inside the gate to the end of the file, with a second gate wrapping the closing coda; the candidate opens with the localized gate (L1), the credit block, and the Q&A, and closes with the code exhibit and the tail delivery frame (section 3).
- **Why:** Section 0 declares the provenance route so every later count is read against the right baseline; the gate's tag is P2, the frame is P6/T3.
- **Verify:** The sources.tsv row for chatscp-jp; `sha256sum original.txt` against the Provenance table.
- **Disposition:** Standing (the route itself); the gate and frame changes are recorded in section 3.

### 1. Credit and attribution

- **What:** The original's credit furniture is a bare `[[module Rate]]` in a right-aligned div (original L3–5) plus an empty `:scpko:info:start`/`end` pair (original L7–8) carrying no prose at all. The candidate deletes both (BARE-RATE-DEL and INFO-DEL blocks) and installs the JP form: a `:scp-jp:credit:start-preview`/`end-preview` block (candidate L3–12) carrying the eight ruling-3 fields (title ChatSCP 테마; 翻訳責任者 AI; 翻訳年 2026; 原題 ChatSCP 테마; 著作権者 thd-glasses; 作成年 2023; 初訳時参照リビジョン 4; the source link, naming scpko.wikidot.com/theme:chatscp, the recorded host, which serves the original). As with bulgunae, the title field keeps the original's Korean word (테마) — T4's type-3 finding for this theme (LOCALIZE-ROWS row 255), with the row also noting empty-label residue in the Q&A frame (section 8). The ledger §(c3) line records the credit outcome as "P3 credit fields FIXED (credit waves; checker-verified)". T7 credit-module CSS: none added; the theme's CSS carries no credit rules. License box: none on either side, and none added — but see the render row's license item in section 11, which is about the site license bar the theme's CSS hides, not about a license box.
- **Why:** P3/T1: the preview credit module is the rate-bearing JP form, so the bare Rate is deleted rather than duplicated (KB-09), and the empty info pair is ledger class C residue, not JP furniture. Ruling 3 fixes the eight fields.
- **Verify:** `grep -n 'module Rate\|info:start' candidate.txt` returns nothing; read candidate L3–12 against the eight fields.
- **Disposition:** FIXED (credit fields, credit waves); the title wording stands as a recorded T4 item (section 11).

### 2. Includes and components

- **What:** One live include change and the frame includes. The usage example inside the Q&A (candidate L29, escaped) is repointed `:scpko:theme:chatscp` → `:scp-jp:theme:chatscp` as built: that repoint changed the branch prefix but kept the plain slug, so the example named a page that does not exist on scp-jp. The usage-example population sweep has since completed the reference to this candidate's posting name, `:scp-jp:theme:chatscp-jp` (per-theme record). The credit includes (section 1) and the interwiki-style include (section 3) complete the candidate's include list; every include names a `:scp-jp:` target. The original's info pair is deleted, not repointed (section 1). No component include exists on either side beyond those.
- **Why:** P1 (KB-15): an include must name the JP counterpart that actually exists on scp-jp. As built, the repoint satisfied the branch half of that rule only; the sweep's completion is what brings the example under it, the counterpart being this candidate itself under its posting name. Ruling 4 is not engaged: no component had to be ported alongside this theme.
- **Verify:** `grep -n '\[\[include' candidate.txt` — four includes, all `:scp-jp:`.
- **Disposition:** Applied; no foreign include kept, no named exception needed.

### 3. Delivery and code loading

- **What:** The original applies its CSS from a shown module on the page itself (`[[module CSS show="true"]]`, original L111–441) — the page's code is simultaneously its delivery and its display. The candidate separates the two in the campaign's applied-CSS form: the CSS body sits in a `[[code type="css"]]` exhibit (candidate L107–455), and the live delivery is the tail frame — a `[[module css]]` importing the candidate's own `local--code/theme%3Achatscp-jp/1` from the draft host (candidate L460–462, SELF-DELIVERY) and an interwiki-style include at priority 1 with `theme=` naming the same /1 delivery (candidate L463–466). The classifier's 8 DELIVERY-MOVE blocks are this relocation (the body travels nearly verbatim; the channel change is the change). The original has no local--code import and no interwiki frame at all, so both tail lines are additions, not repoints.
- **Why:** P4/T9 (own-code delivery served from JP hosts) and P6/T3 (the interwiki-style supplement frame, priority 1 for the theme's own layer on a Sigma-9-based page). The draft-host form of the live lines is KB-41, class (iii): sanctioned at draft stage, rewritten to the production host at posting.
- **Verify:** `grep -n 'local--code' candidate.txt` — L461 and L465, both the candidate's own delivery; compare `grep -n '\[\[module\|\[\[code' original.txt candidate.txt` for the relocation.
- **Disposition:** DISPOSITIONED (draft-host lines, class (iii)).

### 4. Fonts and assets

- **What:** None of either kind was changed. Neither side loads a webfont (the theme inherits the site fonts; its CSS names no `@font-face` and no font import), so there is no P7 supplement and no JPFONT signature — checked, not overlooked: the grep below is the check. The theme has no image assets of its own; its visual joke is typographic (the chat-bubble divs), and no asset URL appears in either file outside the delivery lines of section 3.
- **Why:** P5/P7 are the classes that would carry such changes; both are absent on the bytes.
- **Verify:** `grep -n '@font-face\|@import\|wdfiles' candidate.txt` — only the tail delivery import of section 3.
- **Disposition:** None required.

### 5. Header, sidebar, and site furniture

- **What:** No header variables are overridden on either side, and no sidebar or topbar rule was adapted: the theme's furniture is its chat divs (section 8), styled in the moved CSS body without structural change. The render row's two furniture-adjacent readings — the page's sidebar-not-opening and the Wikidot footer/license bar rendering as a fixed overlay at left-centre over the body at every viewport — are render-record items: the overlay is theme-specific and the machine check agrees with it, and the license bar's hidden state is the theme's own design on both pages (the original hides it identically; the render row records "hidden-license on both pages (all combos)"). Both are carried in section 11 as recorded behavior of the theme, not as port defects.
- **Why:** P8/P9 checked and absent as edits; the render readings belong to the disposition register because they describe what a reviewer will see, on the original as much as on the candidate.
- **Verify:** `grep -n -- '--header-' candidate.txt` returns nothing; the render row is RENDER-ROWS-2 (RENDER-S2-H (KO2)).
- **Disposition:** Standing; the render readings are recorded in section 11.

### 6. Text translation

- **What:** The Q&A conversation is translated throughout (the 17 TRANS-UNANCHORED primaries and the residue block, verified exchange by exchange against the mirror): the questions, the answers, the usage explanations, and the closing exchange. Two translation-adjacent facts are stated separately because they are not translations. (1) The theme's fiction strings inside the code exhibit's tail — the Q/A template placeholders and the error message (candidate L441–455 region) — remain Korean: they are the theme's own sample text (what a user pastes to fake a chat), and T4 recorded them as the exhibit-placeholder item. (2) One answer in the Q&A is hidden with `style="display: none"` in the candidate, matching the joke's structure of a concealed answer. Korean survives elsewhere only as quotation: the credit fields (candidate L4, L7, L11) and the exhibit tail above.
- **Why:** P10 (body and usage translation is the port's purpose) and KB-18 (reader-visible strings). The exhibit placeholders are sample content a user copies verbatim, which is why they were left in the original's language and recorded, rather than translated into text that would no longer match the fiction.
- **Verify:** The pairs are diff.md's body sections in order; read candidate L441–455 against original L443–456 for the retained exhibit text.
- **Disposition:** Standing (the port itself); the retained exhibit Korean is a recorded T4 item (section 11).

### 7. Links

- **What:** Four bare prose links name pages that do not exist on scp-jp and therefore render as red (404) links — T4's type-11 item, counted exactly: `april-fools-2023-ko` twice (candidate L17, L38, the event page the theme was made for) and `chat-guide` twice (candidate L40, L66). Both names are carried over from the original's bare links, which resolve on scpko; on scp-jp there is no counterpart page under either name. The remaining links are sound: the EN hub link (candidate L40, `https://scp-wiki.wikidot.com/secure-facilities-locations`, kept from the original, serves); the theme's forum thread (candidate L98, scpko.wikidot.com — the recorded host, serves; the original's http:// form was scheme-upgraded, the LINK-REPOINT block); the credit source link (candidate L11, recorded host, serves). Inside the code exhibit, the error sample's `[[[url|help.chatscp.com]]]` is placeholder sample text, not a live link. The host check the jiha exemplar taught (candidate host vs recorded host, probe on divergence) finds no divergence: every host-named link names scpko or the EN wiki, both serving.
- **Why:** P11: prose links take the JP counterpart or the serving original, under the dead-reference evidence standard. For these four there is no JP counterpart to repoint to and no serving form of the same name, so the port kept the names and the ledger dispositions P11 for this theme in the sibling / batch-posting class (section 11) — the same class as blackinblack's EN-link residue, with the difference that these do not resolve at all until a JP page exists under the name.
- **Verify:** `grep -n '\[\[\[' candidate.txt` — the four bare links above plus the serving links; each bare name can be checked against the scp-jp page list.
- **Disposition:** DISPOSITIONED (P11, sibling / batch-posting class, GOSIGN2-LEDGER §(c3) line for this theme); recorded here because a reviewer following them today reaches a red link.

### 8. Structure

- **What:** The Q&A frame survives (question divs, answer divs, code-header/code-body bars, the error-wait div), the code exhibit and tail coda correspond, and the CSS body's internal order is preserved through its relocation (section 3). The classifier's 4 EXHIBIT-RESTRUCTURE primaries adjudicate to three facts. (1) **The deleted inline samples:** the original's three small `[[code]]` blocks inside the Q&A — the title-hiding CSS sample (original L44–50), the Q/A template sample (original L63–71), and the error-template sample (original L84–92) — are absent from the candidate; the code bars the prose introduces stand empty at those points (candidate L44–47, L56–59, and the third bar pair), which is T4's type-10 item ("sample code all deleted → empty bars", display-visible). The samples' content is not lost to the record: the same template and error texts survive at the code exhibit's tail (section 6), and the title-hiding rule survives there too as exhibit text (candidate L436–440). But in the Q&A itself, a reader who follows "the code is as follows" finds an empty bar. (2) The first question's frame: the original wraps it in a Q div (original L10–12); the candidate renders it as bare text (candidate L14) ahead of the first answer div — a small frame change inside the same exchange. (3) The closing coda: the original wraps it in a second iftags gate (original L443); the candidate carries the coda inside the code exhibit's tail, ungated, as exhibit text. The ledger §(c3) line dispositions this theme's P10 in the lane-recorded severity / specimen class (the KB-37 deliberate-specimen family): the deletion is a recorded, dispositioned outcome, not a silent one — and it is recorded here in full because the disposition does not change what the page shows.
- **Why:** R3 exists to force exactly this adjudication, because a restructure and a deletion share a diff shape and ledger class I charges the silent form; here the record (T4 row 255 + the ledger's P10 disposition) is what separates the two, and the package states both the record and the visible result.
- **Verify:** Read original L44–50, L63–71, L84–92 against the candidate's corresponding bars; read candidate L436–455 for the surviving exhibit copies.
- **Disposition:** DISPOSITIONED (P10, specimen class, GOSIGN2-LEDGER §(c3) line for this theme); the empty bars are the visible residue of that disposition.

### 9. Formatting only

- **What:** None. The classifier finds no whitespace-only block and no re-indentation (0 and 0), so the R7 follow-up-diff hazard is not triggered.
- **Why:** Formatting churn is disclosed as its own class so it is never mistaken for a semantic change.
- **Verify:** The classifier's section-9 counts in classification.json.
- **Disposition:** None required.

### 10. Porter annotations

- **What:** None. The candidate contains no `[!-- ... --]` translator notes, no 訳注 footnotes, and no provenance comment of the kind the other KO ports carry; the deletions of section 8 are announced nowhere in the page itself (their record is the T4 row and this package). The skeleton's "none" for this section survives contact with the bytes — and the absence is itself worth stating, because the sibling ports (jiha, blackinblack) announce their content decisions in-page and this one does not.
- **Why:** R2: porter-added text is part of the change record; its absence, where decisions were taken, is a fact about the record.
- **Verify:** `grep -n '訳注\|\[!--' candidate.txt` returns nothing.
- **Disposition:** Standing (as an absence, stated).

### 11. Dispositions and exceptions

- **What:** Four items, each with its ground. (1) T1's single error: pseudo-ref ×1, class (ii), posting-procedure — the candidate's own draft-host local--code line (section 3); the posting procedure rewrites it, and fix lanes never "fix" it in the candidate. The 3 warns / 1 info are recorded verbatim in T1-ROWS row 239 and are not classified. (2) The render row's items: the hidden-license state on both pages and the footer/license bar's fixed overlay at every viewport (theme-specific; the theme's own design, present identically in the original — a by-design behavior a reviewer should not mistake for a port break); the page's sidebar-not-opening reading; and the sample's credit-modal errors (KB-32: the preview form has no modal mechanism, ruling 5). (3) T4's items and their ledger dispositions (§(c3) line for this theme): the deleted inline samples — P10 DISPOSITIONED (lane-recorded severity / specimen class); the four red links — P11 DISPOSITIONED (sibling / batch-posting class); the credit title's Korean word and the exhibit placeholders — recorded with the P3 FIXED outcome and the T4 row's own text. (4) The credit fields themselves: FIXED by the credit waves, checker-verified. The theme's determination is PASS and this package does not re-open it; items (2)–(3) are stated in full because they are what a reviewer opening the page will actually see.
- **Why:** A disposition is a decision with grounds (AGENTS.md §3 classes (i)/(ii)/(iii); the named KB entries), not an omission; environment-layer and by-design lines are recorded as not-charged.
- **Verify:** Each item names its deciding record above.
- **Disposition:** DISPOSITIONED (items 1–3); item 4 FIXED.

### 12. Verification

- **What:** (a) T1 source check (T1-ROWS row 239): exit 1, 1 error / 3 warns / 1 info; the one error is pseudo-ref, class (ii); there is no class (i) error. (b) T2/T3 render (RENDER-ROWS-2, lane RENDER-S2-H (KO2)): FINDINGS, the items of section 11(2), all dispositioned or by-design; engine coverage as run by the lane, not separately caveated in its row. (c) T4/T5 (LOCALIZE-ROWS row 255): FINDINGS jointly, display-affecting findings 2 (the deleted samples and the red links); the ledger §(c3) line records the theme's P3 outcome as FIXED and its P10/P11 outcomes as DISPOSITIONED. (d) This package is self-verifying: `python3 review/build_review.py --check` regenerates diff.md and the verdict stamp from the two byte-faithful copies in this directory and compares. Counts in this README are the generator's (difflib, autojunk off): +121/−111 in 32 change blocks; the GNU-diff count of the same pair is 132 changed lines (the tighter count here, per the Summary's note), and the difference is alignment choice, not content.
- **Why:** Verification claims name the cheapest deciding check and its result, not a general assurance.
- **Verify:** Re-run the checker on `pages/theme:chatscp-jp.txt` and `python3 review/build_review.py --check` in this repo.
- **Disposition:** PASS (GOSIGN2-LEDGER (b) row 256; go-sign, COMPLETION-REPORT §10).

## Per-theme record

### The usage example's posting name

The usage example at candidate L29 as built read `@@[[include :scp-jp:theme:chatscp]]@@`: the porting wave's repoint changed the branch prefix from `:scpko:` but left the plain name, so the example named a page that does not exist on scp-jp (the campaign's settled rule for usage examples, AGENTS.md §6). The usage-example population sweep has since completed the reference to `:scp-jp:theme:chatscp-jp` (sweep report SWEEP-USAGE.md in the campaign record, R/review-scout/; canonical commit b5cb724), one of its 287 repairs across 157 candidates. This package documents the corrected candidate; its stamp reads STALE against the pre-repair verdict, by design.

## Change set outside the two diffed files

The diff covers two files; the port's record is one file larger. `pages/theme-decoration-sample-chatscp-jp.txt` is the decoration sample the render checks ran against (its findings are the sample half of section 11(2)); it belongs to this theme's record but carries no port change of its own to explain here. The original-side sample `pages/theme-decoration-sample-chatscp.txt` is the campaign's mirror-side fixture, likewise outside the port. There are no companion fragments, no shared base file, and no inbound-link repairs in other candidates for this theme.
