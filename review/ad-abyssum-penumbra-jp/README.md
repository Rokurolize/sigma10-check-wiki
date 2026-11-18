# Review package — theme:ad-abyssum-penumbra-jp

<!-- BEGIN GENERATED VERDICT STAMP — do not hand-edit; regenerate with review/build_review.py -->
## Verdict stamp
- Theme: theme:ad-abyssum-penumbra-jp — origin EN, population #51 [GOSIGN2-LEDGER (b) row 51]
- Overall: STALE — candidate file changed since the verdict was computed (verdict against 435a6bb-era content, file sha256 now 0f69c9f247e63da85c4c018ced1dcdbcd3830c93a229ad4ed663836ce98445fe); verdict not carried over, re-judgement required
> verdicts below describe the pre-change file
- T1 (source check): FINDINGS (classified) — baseline 2026-11-16: exit 1, 1 error / 1 warn / 1 info (hotlink×1); standing classes dispositioned in register c1 [T1-ROWS row 51; GOSIGN2-LEDGER (b) row 51]
- T2/T3 (render, combined verdict): FINDINGS — [combined T2/T3] report `FINDINGS` — untranslated Hebrew CSS `content:` strings (§5, route to text lane), amber-on-black contrast 1.31 by design; no layout-blocking defect. [RENDER-ROWS-1 (RENDER-S2-A)]
- Engine coverage: full matrix as run by the lane; coverage not separately caveated in the row [RENDER-ROWS-1 row]
- Credit modal: no credit-modal line in this theme's row; no sample credit-modal error recorded [RENDER-ROWS-1 (RENDER-S2-A)]
- T4 (localize patterns + follow-up): FINDINGS — display-affecting findings: 1 [LOCALIZE-ROWS row 51, source LOCALIZE-S2-A]
- T5 (translation text): FINDINGS — the source reports judge T4/T5 jointly; one verdict word covers both [LOCALIZE-ROWS row 51]
- FIX5 re-judgement: none — no OPEN items at the ledger determination [GOSIGN2-LEDGER (b) row 51]
- Computed against: canonical commit 5d951775998e4a1eeccf8e8695a6518b328962ee; candidate file pages/theme:ad-abyssum-penumbra-jp.txt sha256:0f69c9f247e63da85c4c018ced1dcdbcd3830c93a229ad4ed663836ce98445fe; record: GOSIGN2-LEDGER.md + GOSIGN2-LEDGER-SUPPLEMENT.md as of the FIX5 head 435a6bb
<!-- END GENERATED VERDICT STAMP -->


## Status

| | |
|---|---|
| Verdict | **PASS** — passed at the ledger determination; this theme had no OPEN items and no §(e) register entry (GOSIGN2-LEDGER (b) row 51) |
| Standing items | **DISPOSITIONED** — T1 hotlink ×1 (class (ii)); the Hebrew `content:` strings and the amber-on-black contrast (render row); P1 and P5 (register c3). No defect flag from this package: the base the prose names is included at candidate L1, so the notation question the ashes package flags does not arise here (section 3) |
| Go-sign basis | COMPLETION-REPORT.md §10 (go-sign issued; 81 FIXED / 26 DISPOSITIONED / 0 OPEN across the sweep) |
| Named exception | None for this theme (the sweep's single named exception is theme:amethyst-v2, which has no candidate) |

## Provenance

| | Original | Candidate |
|---|---|---|
| Page | theme:ad-abyssum-penumbra | theme:ad-abyssum-penumbra-jp |
| Wiki | scp-wiki.wikidot.com | SCP-JP Sigma-10 candidate (canonical repo) |
| Reference revision | 25 (first translation; the candidate's credit block records 初訳時参照リビジョン: 25) | — |
| Source of this copy | Campaign cache `gosign2-lanes/lane-oc-gs-localize-s2-A/orig-ad-abyssum-penumbra.txt`, via the mirror store (class COPY, hash-verified against review/sources.tsv) | Canonical file `pages/theme:ad-abyssum-penumbra-jp.txt`, copied at worktree HEAD 1605bbd |
| Lines / bytes | 882 lines / 45,019 bytes | 708 lines / 41,564 bytes |
| SHA-256 | 09f859a4fa2eec0d63b1e9d2f41f1c5a2e7a6e2b3e62d07e5c3dfb5db63b5b4c | 2947d334aa21e8cd275aafd95b2791df1ee83fe9b821e9b2e7e5cafe2e74ac62 |

Wave history: the candidate was created by the Stage 2 EN batch 1 integration (commit 3205f27) and its last commit is FIX-CREDIT-D (1869877, credit-attribution normalization), which is also the stamp's computed-against commit. The original has been superseded upstream since revision 25; the follow-up diff artifact `diff-ad-abyssum-penumbra-from25.txt` sits in the campaign record (sources.tsv note, class K5a-i / KB-19), and this package judges the port against the reference revision only.

## Summary

An EN Department of Tactical Theology theme layered on the Penumbra base. The original page is mostly demonstration: a gated head exhibit of some 180 lines (rating module, a Milton epigraph, usage prose with division presets, and four specimen modals) and a 664-line `[[code]]` exhibit holding the theme's CSS text, while the live delivery was a hidden include of the Penumbra theme plus a one-line code-page @import. The port inverts that shape: the Penumbra include is repointed to its JP port and stands at the head, the frame is repointed to the candidate's own code URL, the credit block and a three-line JP usage head replace the demonstration body, and the CSS exhibit's text moves into the live `[[module CSS]]` (similarity: the module's body is the exhibit's body, with only the font lines of section 4 and three whitespace lines differing). The original's tail mechanism — a division-driven logo/subtitle override built on a `{$division}` include variable — is dropped with its documentation. Measured churn (diff.md, the generator's count: +38/−210 in 15 change blocks / 5 hunks); the net −174 lines are the demonstration body and the tail, not CSS loss.

## Class summary

Auto-classification by review/classify_hunks.py (signature table 2026-11-17.1): 15 change blocks — 14 specific (93.3%), 1 heuristic (6.7%), 0 residue, 0 skipped. Pattern citations below name the KB entry; the patterns/ tree state cited throughout is commit 9c5e9079afb01d30cb9fc4ef9d714e5591eb2ffa.

| Label | Blocks |
|---|---|
| DELIVERY-MOVE | 6 |
| IFTAGS | 4 |
| WS-ONLY | 3 |
| EXHIBIT-RESTRUCTURE | 2 |
| JPFONT-STACK | 2 |
| CREDIT-PREVIEW | 1 |
| CREDIT-PROSE | 1 |
| DELIVERY-HOST | 1 |
| DRAFT-HOST | 1 |
| FONT-IMPORT | 1 |
| HEADERVAR | 1 |
| INCLUDE-REPOINT | 1 |
| JPFONT-LOAD | 1 |
| RATE-EXHIBIT-KEPT-CANDIDATE | 1 |
| SELF-DELIVERY | 2 |
| TASL-FIELDS | 1 |
| TRANSLATION-ANCHORED | 1 |
| TRANS-UNANCHORED | 2 |

Adjudication for this README (every block was read against the bytes): the 6 DELIVERY-MOVE primaries and near-primaries are one event, the exhibit-to-module move (section 3); the RATE-EXHIBIT-KEPT-CANDIDATE label on block B2 is the paired-exhibit heuristic firing on the head region — the original's `[[module Rate]]` stood inside the dropped demonstration body and no bare rate module exists in the candidate (`grep -c 'module Rate' candidate.txt` returns 0); rating reaches pages through the rate-bearing preview credit block (section 1), so the label's underlying claim holds in substance but not in form, and it is recorded here rather than narrated as a kept exhibit. The single heuristic block (B6) is the added JP intro line, counted in section 6. After adjudication no block is left unexplained.

## Standing sections

### 0. Header and provenance frame

- **What:** Theme theme:ad-abyssum-penumbra-jp; original theme:ad-abyssum-penumbra on scp-wiki at reference revision 25; candidate `pages/theme:ad-abyssum-penumbra-jp.txt`. Provenance route: derived from the original at the reference revision by the Stage 2 EN2 wave (sources.tsv kind: standard; no production JP counterpart exists). The original's delivery core sits between two gates — the demonstration body under `[[iftags +theme]]` (original L1) and the CSS exhibit under a second `[[iftags +theme]]` (original L187) — and the candidate keeps one gate, localized (candidate L8).
- **Why:** Section 0 declares the provenance route so every later count is read against the right baseline; the gate tag is P2 and the delivery shape is section 3.
- **Verify:** The sources.tsv row for ad-abyssum-penumbra-jp; `sha256sum original.txt` against the Provenance table.
- **Disposition:** Standing (the route itself); the gate change is recorded in section 2.

### 1. Credit and attribution

- **What:** The original has no credit block: its head exhibit carries author prose (the theme is built on EstrellaYoshte's Penumbra; the blockquote specimen credits Yossipossi and Aftokrator) but no credit module. The candidate installs the JP form at the head (block B5, candidate L10–19): a `:scp-jp:credit:start-preview`/`end-preview` block with all eight ruling-3 fields (title Ad Abyssum（Penumbra）; 翻訳責任者 AI; 翻訳年 2026; 原題 Ad Abyssum Theme (Penumbra); 著作権者 Yossipossi; 作成年 2023; 初訳時参照リビジョン 25; the source link, section 7). The original's `[[module Rate]]` (original L5, inside the demonstration body) is deleted with that body; the preview credit block is rate-bearing, so rating is present exactly once. The original carries no image license entries to preserve (its one exhibit image is a component:image-block hotlink to the theme's own EN file area, dropped with the body).
- **Why:** P3/T1 (KB-09): the JP credit form replaces the original's prose-only attribution, and the rate function folds into it rather than duplicating. The Penumbra authorship is carried by the 基盤 line and the base include (section 3), not by the credit fields, which name this theme's author.
- **Verify:** Read candidate L10–19 against the eight fields; `grep -c 'module Rate' candidate.txt` returns 0.
- **Disposition:** FIXED (GOSIGN2-LEDGER §(c3): P3 credit fields FIXED, credit waves, checker-verified).

### 2. Includes and components

- **What:** Three include events. (1) The base include: the original's hidden delivery div included `:scp-wiki:theme:penumbra` (original L184 region); the candidate's first line is `[[include :scp-jp:theme:penumbra]]` (block B1) — the JP port of the same base. (2) The frame include, repointed (block B3, section 3). (3) The candidate's usage line names itself in the bare form: `@@[[include theme:ad-abyssum-penumbra-jp]]@@` (candidate L23). The original's usage prose also documented a `division=` include variable with seven named presets ({{abrahamics}}, {{east_asian}}, {{indus_vedic}}, {{shamanism_animism}}, {{neopaganism}}, {{parareligions}}, {{demonology}}); that mechanism lived in the tail block deleted at original L870–882 (section 8), so no include variable survives into the candidate. Every named include in the candidate is `:scp-jp:` or the bare local form.
- **Why:** P1 (KB-15) for the base repoint and the usage line; the division variable's removal is a structural deletion, recorded in section 8 with its ledger coverage.
- **Verify:** `grep -n '\[\[include' candidate.txt` — base, frame, credit pair, and the one escaped usage line.
- **Disposition:** Applied; no foreign include kept, no named exception needed.

### 3. Delivery and code loading

- **What:** The port's central event is a delivery move (blocks B5, B7–B8, B11–B12, B14). In the original, the live CSS arrived by @import from the theme's own code page (`@import url(https://scp-wiki.wikidot.com/theme:ad-abyssum-penumbra/code/1)` inside a hidden `[[module CSS]]`), and the same CSS text was displayed in a `[[code type="css"]]` exhibit (original L205–868). The candidate deletes the code-page import and moves the exhibit's text into the live module (candidate L31–706): the module's body is the exhibit's body, differing only in the font lines of section 4 and three whitespace lines (section 9). The hidden delivery div and the original's `show="true"` second module (the tail's) disappear with their regions. **Frame paragraph (the M-frame addition):** this theme's original already carried an interwiki-style frame (priority=1, `theme=` naming the EN page URL); the candidate keeps the frame form and priority and repoints `theme=` to its own `local--code/theme%3Aad-abyssum-penumbra-jp/1` on the draft host (candidate L3–6). The ledger records the outcome as P6 FIXED (frame waves; checker-verified). The candidate's prose declares 基盤： Penumbra（インライン） (candidate L25), and the bytes support it: the base is included at candidate L1 and the theme's own CSS is inline in the module — the contrast with the ashes package, whose prose names a base its bytes never deliver, is recorded there.
- **Why:** P4/T2 for the move (KB-02, the code-page delivery class): the JP candidate self-delivers its CSS in the module rather than depending on an EN code page that has no JP counterpart. P6/T3 (KB-07) for the frame repoint; the draft-host form is KB-41, class (iii), sanctioned at draft stage and rewritten at posting.
- **Verify:** `grep -n 'code/1\|@import url(https' candidate.txt` — no code-page import remains; the only @imports are the four font loads of section 4. Read candidate L1–6 for the base and frame.
- **Disposition:** Move applied; frame FIXED (P6); the draft-host URL is DISPOSITIONED (class (iii)).

### 4. Fonts and assets

- **What:** Four @imports head the moved module (candidate L29–35). The Noto Sans JP load is added (`family=Noto+Sans+JP:wght@400;700`, candidate L29, label JPFONT-LOAD), and the original's three display-face loads repoint from fonts.bunny.net to fonts.googleapis.com with family parameters unchanged (New Rocker, Nova Cut, Finlandica; candidate L33–35; block B8, FONT-IMPORT label). Two stacks gain the JP face as fallback (blocks B11–B12, JPFONT-STACK): `"Nova Cut", sans-serif` → `"Nova Cut", "Noto Sans JP", sans-serif` (candidate L159) and `"New Rocker", sans-serif` → `"New Rocker", "Noto Sans JP", sans-serif` (candidate L174); the remaining stacks, including the :root `--header-font: "Finlandica", serif` and `--body-font: "verdana", sans-serif`, are carried as the original wrote them. Assets: the theme's CSS references no image files of its own besides the dropped tail's `--lgurl` (section 8); the T1 baseline's single hotlink error is the original-state file reference in the dropped exhibit body.
- **Why:** P7/T5 with KB-16: the Latin display faces have no Japanese coverage, so the JP face is loaded and named in the display stacks that render theme furniture text; stacks the original built on generic families are left as designed. The bunny.net → googleapis move is a host repoint of a well-formed load (the crayon package's shape), not a KB-04 malformation repair.
- **Verify:** `grep -n 'fonts.bunny' candidate.txt` returns nothing; `grep -n 'Noto Sans JP' candidate.txt` counts the load and the two stack mentions.
- **Disposition:** Applied (font localization); the T1 hotlink is DISPOSITIONED (class (ii)).

### 5. Header, sidebar, and site furniture

- **What:** The theme's header identity is set in the moved CSS's :root (candidate L37–38): `--header-title: "TACTICAL THEOLOGY"` and `--header-subtitle: "INVENIENT NOVUM NUMEN"`, carried unchanged from the exhibit. The original's tail block additionally overrode `--header-subtitle` with `var(--{$division})` so a page could switch subtitle and logo per division preset; that override is deleted with the tail (block B15, HEADERVAR label; section 8), so the candidate's subtitle is the fixed :root value. No other header variable is added or removed.
- **Why:** P9/T6 is a per-theme judgment: the fixed values are the theme's default identity and are carried; the division override is not a header-variable translation issue but part of the dropped mechanism, and it is recorded where the mechanism is.
- **Verify:** `grep -n -- '--header-' candidate.txt` — the two :root assignments and no `{$division}` reference; `grep -n 'lgurl' candidate.txt` returns nothing.
- **Disposition:** Standing for the carried values; the override's deletion is recorded in section 8.

### 6. Text translation

- **What:** The candidate's JP text is a compressed head (blocks B6–B7): the intro line Penumbraを基盤にしたAd Abyssum向けテーマです。 (candidate L21), the usage line (L23), and the 基盤 line (L25). The original's usage prose (the Tactical Theology paragraph, the import instructions, the preset documentation) is not translated; it is replaced by those three lines, and the specimen texts (the Milton epigraph, the lorem ipsum, the classified-document tab) are dropped with the demonstration body (section 8). Inside the moved CSS, reader-visible strings are carried as the original wrote them, including `content: "Date of Damnation:"` (candidate L627) and its companion "Date of Creation:", and the Hebrew blessing string (candidate L663). The T4 record judges the translation itself unproblematic while listing the surviving English content (T5) among its findings; the render record dispositions the Hebrew strings (route to text lane).
- **Why:** P10 for the head prose; KB-18 for the `content:` strings — they are liturgical and form-label text inside a theme whose JP prose layer is the head, and both records that examined them left them standing with dispositions rather than requiring conversion.
- **Verify:** `grep -n 'content:' candidate.txt` — the strings named above; read candidate L21–25 for the whole JP prose layer.
- **Disposition:** Standing (the port itself, with the T4/T5 FINDINGS verdict recorded in section 12); the Hebrew strings are DISPOSITIONED (render row).

### 7. Links

- **What:** The candidate's only live outbound link is the credit source link (candidate L18), naming `https://scp-wiki.wikidot.com/theme:ad-abyssum-penumbra` — the original's recorded host (review/sources.tsv), so it names the serving original and no host defect arises. The original's prose links (the Tactical Theology tag page, the Penumbra theme page on scpwiki.com, the specimen links) all stood inside the dropped demonstration body and have no candidate counterpart.
- **Why:** P11's evidence standard is met by the source link naming the recorded host; dropped-body links need no repointing decision because their text is gone.
- **Verify:** Compare candidate L18's host against the sources.tsv row's original_url host (scp-wiki.wikidot.com) — identical.
- **Disposition:** Standing.

### 8. Structure

- **What:** Two deletions and one preservation. Deletion 1, the demonstration body (block B2, EXHIBIT-RESTRUCTURE; original L3–182): the rating module, epigraph, usage prose, and the four specimen modals (specimen text, blockquote test, Akiva table, tabview) are dropped wholesale; the candidate's head (frame, gate, credit, three prose lines) stands in their place. The T4 record lists the missing usage/demo section among its findings, and the candidate's compressed usage lines are the campaign's standard replacement shape for a theme page (the theme's documentation function moves to this review package). Deletion 2, the tail mechanism (block B15; original L870–882): the negative-gate div holding the porter-visible note ("This bit down here controls the logo and subtitle changes…") and the second CSS module defining `--lgurl` with the `{$division}` logo URL and the subtitle override — the division-preset feature does not survive the port, and no candidate text claims it does. Preservation: the CSS itself moves without structural loss (section 3); an exhibit census of the moved text against the original exhibit shows selector and declaration order preserved, the only differences being sections 4 and 9.
- **Why:** R3's census decides exhibit questions; here the census separates the two shapes cleanly — the demonstration exhibits were furniture for the EN theme page, while the CSS exhibit was the delivery text and is preserved by the move. The tail deletion removes a feature, not furniture; it is recorded plainly so a future porter can restore the preset mechanism from original.txt if JP demand appears.
- **Verify:** `wc -l original.txt candidate.txt` (882 vs 708); read original L870–882 against candidate L703–708 (the module close and gate close, nothing after).
- **Disposition:** Recorded; the theme's ledger verdict is PASS with these deletions inside the adjudicated record (T4 row 51; §(c3) P1 DISPOSITIONED, posting-procedure convention class).

### 9. Formatting only

- **What:** Three whitespace-only blocks (B9, B10, B13; WS-ONLY primaries at candidate L40, L44, L694): blank lines inside the moved CSS that carried no characters in the exhibit carry four spaces in the module. They ride inside the delivery move and change no rendering. No re-indentation blocks exist.
- **Why:** R7: whitespace churn is disclosed as its own class; here it is also the move's fingerprint, confirming the module text came from the exhibit rather than being retyped.
- **Verify:** Section 9 of the classifier skeleton for this package (WS-ONLY 3, re-indentation 0); diff.md shows the three `-\n+    ` line pairs.
- **Disposition:** None required.

### 10. Porter annotations

- **What:** None added by the port. The candidate carries no `[!-- --]` translator notes and no editor line. One annotation-like text existed in the original and was deleted, not carried: the tail's porter-visible note about the logo/subtitle mechanism (original L872, inside the block deleted at section 8) — it explained a mechanism the candidate does not contain, so carrying it would have annotated nothing.
- **Why:** R2: porter-added text is part of the change record; the check was run explicitly, and the original's own note is accounted for rather than silently dropped from the record.
- **Verify:** `grep -n '\[!--' candidate.txt` returns nothing; the deleted note is at original L872.
- **Disposition:** Standing (checked, absent).

### 11. Dispositions and exceptions

- **What:** Four items, each with its ground. (1) T1's single hotlink error: DISPOSITIONED in register c1 (hotlink, class (ii)) — the original-state file reference, inside a region the port drops. (2) The render row's two items (RENDER-ROWS-1, RENDER-S2-A (EN2)): the untranslated Hebrew `content:` strings (dispositioned, §5 of that record, route to text lane) and the amber-on-black contrast of 1.31, which is the theme's design (KB-39); the row records no layout-blocking defect. (3) The T4 row's base question (pattern 1, the Penumbra base suppression with undefined base variables and display-collapse risk): the ledger's §(c3) line for this theme records P1 DISPOSITIONED (posting-procedure convention class) and P5 DISPOSITIONED (class (ii) / KB-58); against the current bytes the base is included at candidate L1 and the theme's own :root defines its header variables, so the collapse shape the finding feared is not present in the file this package ships. (4) The frame's draft-host URL: class (iii), section 3.
- **Why:** A disposition is a decision with grounds (AGENTS.md §3 classes (i)/(ii)/(iii); the named KB entries), not an omission.
- **Verify:** Each item names its deciding record above.
- **Disposition:** DISPOSITIONED (items 1–4 as stated).

### 12. Verification

- **What:** (a) T1 source check (T1-ROWS row 51): exit 1, 1 error / 1 warn / 1 info; the one error is hotlink, class (ii); there is no class (i) error. (b) T2/T3 render (RENDER-ROWS-1, RENDER-S2-A (EN2)): FINDINGS, both items dispositioned (section 11 item 2); no credit-modal line in this theme's row. (c) T4/T5 (LOCALIZE-ROWS row 51): FINDINGS jointly, display-affecting findings 1; the row's findings are the base-suppression question (section 11 item 3), the then-absent interwiki-style (since FIXED), the original-site local--files direct link (pattern 5, dispositioned), the 基盤 notation question (section 3: the current bytes support the notation), surviving English content (section 6), and the missing usage/demo section (section 8); the row states the translation itself is unproblematic. The ledger §(c3) line records the outcomes: P1 DISPOSITIONED, P5 DISPOSITIONED, P6 FIXED. (d) This package is self-verifying: `python3 review/build_review.py --check` regenerates diff.md and the verdict stamp from the two byte-faithful copies in this directory and compares. Counts in this README are the generator's: +38/−210 in 15 change blocks / 5 hunks.
- **Why:** Verification claims name the cheapest deciding check and its result, not a general assurance.
- **Verify:** Re-run the checker on `pages/theme:ad-abyssum-penumbra-jp.txt` and `python3 review/build_review.py --check` in this repo.
- **Disposition:** PASS (GOSIGN2-LEDGER (b) row 51; go-sign, COMPLETION-REPORT §10).

## Appendix — residue blocks

The classifier reports no residue blocks for this package. Its single heuristic block, adjudicated above, is:

| Block | Range (orig → cand) | Classifier state | Resolution |
|---|---|---|---|
| B6 | at 191 → 21-21 (body → body) | heuristic TRANS-UNANCHORED | The added JP intro line; section 6 |

## Per-theme record — the division presets

One feature question deserves its own paragraph because neither the class summary nor the ledger rows name it directly. The EN theme offered subheader/logo presets: a page including the theme could pass `division=` and receive a different subtitle and logo (original tail, L870–882, driven by the `{$division}` variable and a logo URL template). The port drops the mechanism and its documentation together, so a JP page cannot select a division preset. This is recorded as a structural deletion in section 8 rather than flagged as a defect: the ledger's T4 examination saw the same file, listed the missing usage/demo material among its findings, and determined PASS with the §(c3) outcomes above; the mechanism is fully recoverable from original.txt in this package if a JP porter restores it.

### Post-package repairs (REFRESH3-E)

The items above describe this package as built. The repair recorded below postdates the package; `candidate.txt` has been recopied from the current canonical `pages/theme:ad-abyssum-penumbra-jp.txt` and `diff.md` and the verdict stamp regenerated with `python3 review/build_review.py`, so this package now documents the post-repair candidate. The regenerated stamp reads **STALE** by design: no re-judgement is fabricated here, and the frozen ledger (`GOSIGN2-LEDGER.md` + supplement, FIX5 head 435a6bb) remains the verdict record.

**FIX-FRAMED — frame sub-shape (D) treated as (B), own-address pointer dropped (landing 5d95177).** `FIX-FRAMED.md` records this theme's frame as sub-shape (D): the frame's `theme=` named the theme's own code block (/1) on the draft host, but the candidate carries no `[[code]]` block in any form (its CSS is live `[[module CSS]]`), so the named block does not exist — a dead pointer, verified in the report. The original's once-live form is a variant: its @import (L178) names its own code/1 in `/code/` URL form and its frame `theme=` (L184) names the original page URL itself; block 1, `[[code type="css"]]` L189–868, is the CSS source. The coordinator's ruling treats (D) as (B) and applies the minimal remedy: drop the single `| theme=https://sigma10-jp-test.wdfiles.com/local--code/theme%3Aad-abyssum-penumbra-jp/1` line, keep the `[[include :scp-jp:component:interwiki-style]]` frame, its priority, and every other byte unchanged. Commit 5d95177 deleted exactly that one line at candidate L5. The checker finding set is unchanged (1 error / 0 warn / 1 info before and after; the dropped line was not a class (i) finding), as tabulated in FIX-FRAMED.md.

## Change set outside the two diffed files

The diff covers two files; the port's record is one file larger. `pages/theme-decoration-sample-ad-abyssum-penumbra-jp.txt` is the decoration sample the render checks ran against (its findings are the sample half of the T2/T3 row); it belongs to this theme's record but carries no port change of its own to explain here. There are no companion fragments and no shared base file; the Penumbra base is the separate candidate theme:penumbra (theme:penumbra-jp's own package), included, not copied.

## License and attribution

- **Title:** Ad Abyssum Theme (Penumbra)
- **Author:** Yossipossi
- **Source:** https://scp-wiki.wikidot.com/theme:ad-abyssum-penumbra — revision 25
- **License:** Creative Commons Attribution-ShareAlike 3.0 (CC BY-SA 3.0) — license deed: https://creativecommons.org/licenses/by-sa/3.0/
- **Adaptation:** This package holds a Sigma-10 migration port of the work; changes were made. See "Summary" and "Standing sections" in this README for what changed and why. Translator: AI (Muse and its delegated agents), per the campaign's standing attribution rule.
