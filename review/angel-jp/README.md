# Review package — theme:angel-jp

<!-- BEGIN GENERATED VERDICT STAMP — do not hand-edit; regenerate with review/build_review.py -->
## Verdict stamp
- Theme: theme:angel-jp — origin EN, population #56 [GOSIGN2-LEDGER (b) row 56]
- Overall: STALE — candidate file changed since the verdict was computed (verdict against 435a6bb-era content, file sha256 now 57215bd0bb8475e1ce6d29714613a630396082d6fb5ff2ed142c288346f2034d); verdict not carried over, re-judgement required
> verdicts below describe the pre-change file
- T1 (source check): FINDINGS (classified) — baseline 2026-11-16: exit 1, 3 errors / 1 warn / 1 info (hotlink×3); standing classes dispositioned in register c1 [T1-ROWS row 56; GOSIGN2-LEDGER (b) row 56]
- T2/T3 (render, combined verdict): FINDINGS — [combined T2/T3] report `FINDINGS` — candidate-specific unreadable near-white top-nav text on light pink (all widths, missed by machine); ≤375 site-header doubling is X1. [RENDER-ROWS-1 (RENDER-S2-A)]
- Engine coverage: full matrix as run by the lane; coverage not separately caveated in the row [RENDER-ROWS-1 row]
- Credit modal: no credit-modal line in this theme's row; no sample credit-modal error recorded [RENDER-ROWS-1 (RENDER-S2-A)]
- T4 (localize patterns + follow-up): FINDINGS — display-affecting findings: 4 [LOCALIZE-ROWS row 56, source LOCALIZE-S2-A]
- T5 (translation text): FINDINGS — the source reports judge T4/T5 jointly; one verdict word covers both [LOCALIZE-ROWS row 56]
- FIX5 re-judgement: item 15 (class E) DISPOSITIONED — FIX5-CONTRA (no edit, no commit): candidate vs original colour value sets byte-identical (line citations both sides; machine colour-token multiset comparison) [GOSIGN2-LEDGER-SUPPLEMENT (a) item 15]
- Computed against: canonical commit 722ceb5c949172bb5185d51ef56ce4119ee4fa91; candidate file pages/theme:angel-jp.txt sha256:57215bd0bb8475e1ce6d29714613a630396082d6fb5ff2ed142c288346f2034d; record: GOSIGN2-LEDGER.md + GOSIGN2-LEDGER-SUPPLEMENT.md as of the FIX5 head 435a6bb
<!-- END GENERATED VERDICT STAMP -->

## Status

| | |
|---|---|
| Verdict | **PASS** — go-sign (this theme is one of the 286 of 286 pass-eligible themes) |
| Blocking items at ledger time | GOSIGN2-LEDGER.md §(e) item 15 [E] — top-nav text near-white on light pink, unreadable at all widths, recorded as candidate-specific (KB-28 contrast family) |
| Re-judgment | GOSIGN2-LEDGER-SUPPLEMENT.md item 15: **DISPOSITIONED** (FIX5-CONTRA, no edit), on the colour-identity ground re-derived in the per-theme record below |
| Standing items | **DISPOSITIONED** — T1 hotlink×3 (P5, class (ii) / KB-58); the ≤375 site-header doubling is X1 (KB-35); P9 header strings kept in English (ruling 2). Two record matters are carried as flags, not dispositions: the sources.tsv supersession note is contradicted by its own cited artifact (per-theme record), and the original's two tail component includes were dropped with the localize lane's staff-consult note standing (section 2) |
| Go-sign basis | COMPLETION-REPORT.md §10 (go-sign issued; 81 FIXED / 26 DISPOSITIONED / 0 OPEN across the sweep) |
| Named exception | None for this theme (the sweep's single named exception is theme:amethyst-v2, which has no candidate) |

## Provenance

| | Original | Candidate |
|---|---|---|
| Page | theme:angel | theme:angel-jp |
| Wiki | scp-wiki.wikidot.com | SCP-JP Sigma-10 candidate (canonical repo) |
| Reference revision | 6, as recorded in the candidate's credit block (初訳時参照リビジョン: 6, candidate L14) and in review/sources.tsv | — |
| Source of this copy | Mirror store `review-mirrors/orig-angel-rev6.txt`, fetched once by the LOCALIZE-S2-A lane at rev 6 | Canonical file `pages/theme:angel-jp.txt`, copied at worktree HEAD 9005272; the file's last content change is commit 722ceb5 (frame self-address remedy, sub-shape (B)), the stamp's computed-against commit |
| Lines / bytes | 538 lines / 10,637 bytes (the last line carries no trailing newline) | 429 lines / 9,070 bytes |
| SHA-256 | 38f4c3164b2b8f5efc08da255009ec273293ee9bcd21a349fd2af73120b672c2 | 57215bd0bb8475e1ce6d29714613a630396082d6fb5ff2ed142c288346f2034d |

Package files: `original.txt` and `candidate.txt` as tabled above; `classification.json` and the skeleton behind this README are from classify_hunks.py 0.1.0, signature table 2026-11-17.1, patterns commit 9c5e9079afb01d30cb9fc4ef9d714e5591eb2ffa.

## Summary

Angel is a Black Highlighter based theme, and the port restructures its delivery into the compact S2 form: an interwiki-style frame include, the preview credit block, three lines of prose, and the theme's own CSS carried inline in a single `[[module CSS]]` (classifier topology: the original's code exhibit moves to the inline module at 0.989 similarity). The original's documentation body (usage prose, Examples, the Source Code showcase) and its tail furniture are not carried; the localize lane recorded that form and charged only the items in section 11. The theme's only blocking item was a contrast charge against the top navigation, dispositioned because the candidate's colour values are the original's own, byte for byte — re-derived from this package's two files in the per-theme record. The verdict stamp reads STALE because one frame parameter line was dropped after the verdict (commit 722ceb5); that delta touches no colour surface, and this package re-judges the current bytes.

## 0. Header / provenance

- Delivery: code-css -> module-css (body similarity 0.99)
- Delivery: external-own-delivery -> module-css — companion body unavailable; candidate-side only

- **Provenance route:** derived from the branch original at the reference revision (theme:angel rev 6 on scp-wiki). This is not an R4 production adoption: no production JP counterpart exists in the record for this theme, and the candidate's body is the S2 localization of the EN original. The evidence is threefold and mutually consistent: review/sources.tsv keys the row `standard` with the mirror's SHA-256 equal to this package's original.txt; the candidate's credit block records 初訳時参照リビジョン: 6 (candidate L14); and the T4 follow-up diff shows no change past the reference (rev6 → rev6, LOCALIZE-S2-A EN3 follow-up), so the mirror in this package is also the current original, not a superseded revision. The sources.tsv note claiming the opposite is flagged in the per-theme record.

## Class summary

| Label | Blocks |
|---|---|
| CREDIT-PREVIEW | 1 |
| CSS-BODY | 1 |
| DELIVERY-MOVE | 3 |
| EXHIBIT-RESTRUCTURE | 2 |
| IFTAGS | 1 |
| JPFONT-LOAD | 1 |
| RATE-EXHIBIT-KEPT-CANDIDATE | 1 |
| SELF-DELIVERY | 1 |
| TASL-FIELDS | 1 |
| TRANS-UNANCHORED | 1 |
| WS-ONLY | 36 |

Counts: 42 blocks, 41 specific, 1 heuristic, 0 residue, 0 skipped (comment text).

## 1. Credit and attribution

- CREDIT-PREVIEW (A): Credit block swap (P3/T1): the JP environment's preview credit module is the rate-bearing form; the branch-original credit module does not render here.
  Verify: Re-run the T1 checker (check_source.py); the credit includes must resolve on scp-jp.
  - B1: orig 1-1 -> cand 1-22 (body -> body)

- **What:** B1 also carries IFTAGS, TASL-FIELDS and TRANS-UNANCHORED in its span (candidate L1–22). The candidate's credit block (candidate L7–16, `credit:start-preview` / `credit:end-preview`) carries all eight TASL fields: タイトル エンジェル・テーマ (L8), 翻訳責任者 AI (L9), 翻訳年 2026 (L10), 原題 Angel Theme (L11), 著作権者 MisterFrown (L12), 作成年 2024 (L13), 初訳時参照リビジョン 6 (L14), 元記事リンク https://scp-wiki.wikidot.com/theme:angel (L15). The original carries no credit block and no license box; its attribution is the intro sentence "This is the Angel Theme, created by [[*user MisterFrown]]" (original L22) and the CSS banner "Angel Theme by MisterFrown" (original L123, retained at candidate L27). The candidate's 著作権者 field names the same author the original names — there is no pointer-instead-of-author defect in this package. The credit link's host (scp-wiki.wikidot.com) is the host sources.tsv records for the original. The 翻訳責任者 value is ruling 3's campaign form (AI), set by FIX-CREDIT-D (commit 1869877); at localize time the field read SCP-JP under the then-current campaign convention, which the localize lane noted without charging.
- **Why:** P3/T1 — the preview credit module is the rate-bearing form in this environment, and TASL attribution (ruling 3) is what makes the port redistributable: title, author, source and license lineage in one block.
- **Verify:** Read candidate L7–16 against original L22 and L123; `grep -n 'info:start\|license-box' candidate.txt` returns nothing; the T1 checker reports no credit error on this file (section 12).
- **Disposition:** No P3 item is charged against this theme in the ledger register; the T1 baseline records no credit-domain error. Standing.

## 2. Includes and components

The skeleton reports no signature for this section; two include facts stand on the bytes and are recorded here.

- **What (frame):** the candidate opens with the translation-module frame, `[[include :scp-jp:component:interwiki-style | priority=1]]` (candidate L1–3). At localize time the candidate had no interwiki-style include at all and the lane charged P6 MISSED; the include was added by commit 1869877 with a `theme=` parameter naming the candidate's own draft-host `local--code/theme%3Aangel-jp/1` address, and commit 722ceb5 then dropped that parameter (sub-shape (B) of the frame self-address remedies): the candidate carries no code block for the address to name (census: zero `[[code]]` forms in candidate.txt; its CSS is the inline module of section 3), so the address was dead. The frame include itself is kept. Record: FIX-FRAMEADDR.md in the campaign scout folder; the remedy is recorded with its citation and is not re-litigated here.
- **What (dropped tail components):** the original's tail carries two component includes outside the gate, `:scp-wiki:component:centered-header-bhl` and `:scp-wiki:component:toggle-sidebar-bhl` (original L533–534). Neither has a candidate counterpart. The localize lane recorded the drop at the time (P1 note: no counterpart in the canonical repo; staff consultation). The components do exist on production scp-jp (the S2-F lane's dependency probes list both `component:centered-header-bhl` and `component:toggle-sidebar-bhl` as EXISTS on scp-jp), so a JP-form include is available at posting; the ledger charges no item for the drop.
- **Why:** P6 is the translation-module frame (the interwiki link frame must render in the theme); the two tail components are furniture of the original theme page itself, not of pages applying the theme.
- **Verify:** `grep -n 'interwiki-style' candidate.txt` returns the single include at L1; `grep -n 'centered-header\|toggle-sidebar' candidate.txt` returns nothing, against original L533–534.
- **Disposition:** P6 FIXED (frame waves; checker-verified) [GOSIGN2-LEDGER.md §(c3), angel row]. The tail-component drop stands as the localize lane recorded it (staff-consult note); this package flags it for the coordinator's attention at posting, at that recorded weight — it is not a blocking item in any register.

## 3. Delivery and code loading

- DELIVERY-MOVE (B): Body relocated between deliveries (topology): where the CSS lives changed (code page to inline module CSS, exhibit to own fragment); the move itself is the change, and internal edits classify separately.
  Verify: Compare the moved body against its counterpart in the mirror or its companion delivery.
  - B5: orig 142-142 -> cand 46-46 (code-css -> module-css)
  - B41: orig 523-529 -> cand 427-427 (code-css -> module-css)

- **What:** the delivery topology is restructured, and the classifier's topology pass states it exactly. The original delivers three ways at once: a head `[[module CSS]]` (original L2–6) importing normalize and the Black Highlighter base from nu-scptheme.github.io (original L4–5); the theme's own CSS as a `[[code type="css"]]` exhibit in the body (original L121–523); and a tail `[[module CSS]]` (original L535–538) importing the page's own `theme:angel/code/1`, which is what makes the exhibit live. The candidate delivers once: the theme's own CSS inline in a single `[[module CSS]]` (candidate L24–427), opened by the Noto Sans JP import (candidate L26). B5 is the `--header-font` line caught mid-move (its stack edit is section 4); B41 is the exhibit's close becoming the module's close. The tail self-import has no counterpart because the module it would import is already the delivery (SELF-DELIVERY fires inside B42, section 8). Two things the candidate does **not** carry: the BHL base CSS itself (the original's two base @imports, original L4–5, end at heuristic block B2 with no counterpart — resolved in the appendix), and any code block (census: original 1 code block, candidate 0). The candidate's prose declares **基盤:** BHL（インライン） (candidate L22). Read against the bytes, that label names the S2 delivery composition's form for this theme — own CSS inline, base supplied by the composition — not a claim that BHL's rules are inside this file: the localize lane judged exactly this file's inline method to be the composition's design (P4 APPLIED, citing REPORT-REWORK2-P1), and the render lane's T3 walk records the pink BHL theme rendering styled, with BHL furniture (JP-left sidebar, page-action pills) in place (REPORT-GOSIGN2-RENDER-S2-A.md §12). The candidate's module sits inside the `[[iftags +テーマ]]` gate (candidate L5–429) where the original's delivery modules sat outside its gate; the render record on sample pages, which include this page, is the deciding evidence that the composition delivers it.
- **Why:** DELIVERY-MOVE is the topology class: the failure it guards against is a silent delivery break (CSS present in the file but never loaded). The evidence that this instance loads is the render record, not the file's shape alone.
- **Verify:** `classification.json` topology (moves: code-css → module-css at 0.989 similarity; external-own-delivery → module-css, candidate-side); `grep -n 'nu-scptheme' original.txt candidate.txt` (original only, L4–5); code-block census as above.
- **Disposition:** No ledger item charges the delivery restructure; P6 is FIXED on the frame record (section 2). Standing on the render evidence cited.

## 4. Fonts and assets

The skeleton prints "none" for this section because it lists each block once under its primary label; the label spans fire twice, and the section is written from them.

- **What:** (1) JPFONT-LOAD, inside B3's span: the candidate's delivered CSS opens with `@import url('https://fonts.googleapis.com/css2?family=Noto+Sans+JP:wght@400;700&display=swap');` (candidate L26), a family the original never loads. (2) A P7 font-stack rewrite, inside B5's span: `--header-font` (original L142 `"Sour Gummy", sans-serif` → candidate L46 `"Sour Gummy", "Noto Sans JP", sans-serif`) — the classifier labels the block DELIVERY-MOVE because the line also moved; its content change is the stack rewrite, narrated here as that class. Both changes landed in commit 1869877. (3) The theme's own loads are unchanged: Sour Gummy (original L127 → candidate L31) and Itim (original L128 → candidate L32), both Google Fonts (a direct-link exception host). Every loaded family is applied — Sour Gummy and Noto Sans JP by `--header-font` (candidate L46), Itim by `--UI-font` (candidate L47) — and no applied family is unloaded. (4) Assets: the three star-asset URLs stay on the original's own host, scp-wiki.wdfiles.com — starcircle.png (original L214 → candidate L118; original L255 → candidate L159) and stars.png (original L227 → candidate L131). Those are the P5 lines, dispositioned in section 11; they are also this package's whole T1 error set (section 12).
- **Why:** P7/KB-16 (patterns/ at commit 9c5e9079afb01d30cb9fc4ef9d714e5591eb2ffa): Japanese header text needs a JP face in the stack, and the load must sit in the delivered channel — here it heads the inline module itself. The failure prevented is header Japanese falling back to OS-default glyphs.
- **Verify:** `grep -n '@import\|--header-font\|--UI-font' candidate.txt` against the same grep on original.txt; the stack at candidate L46 names exactly the families loaded at L26/L31.
- **Disposition:** The localize lane charged P7 MISSED against the 424-line file it read (no JP cover in the theme's own stacks); the current bytes carry the supplement, added after that read (commit 1869877). No ledger item for P7 stands open against this theme. Standing on current bytes.

## 5. Header, sidebar, site furniture

none — no signature for this section fired over 42 change blocks, and the ground is measurable: the furniture rules are carried unchanged. The `#top-bar` blocks (original L234–248 → candidate L138–152) and the palette beneath them are byte-identical at declaration level (the per-theme record gives the windows and hashes); the sidebar and interwiki rules differ only by the trailing-space blank lines counted in section 9. The header title variables are likewise unchanged — `--header-title: "SCP FOUNDATION"` and `--header-subtitle: "SECURE, CONTAIN, PROTECT"` (original L138–139 = candidate L42–43) — kept in English as identity strings; the localize lane's P9 charge on them is DISPOSITIONED under ruling 2 (header/title language is out of scope for migration correctness) [GOSIGN2-LEDGER.md §(c3), angel row]. The one charged phenomenon on this surface, the unreadable top-nav text, is the theme's blocking item and is treated in section 11 and the per-theme record, not here.

## 6. Text translation

The skeleton prints "none" for this section; TRANS-UNANCHORED fires inside B1's span, and the section is written from it.

- **What:** the candidate's reader prose is three lines: the intro (candidate L18, "Black Highlighterを基盤にしたAngelテーマです。"), the usage line (candidate L20, the escaped self-include `@@[[include theme:angel-jp]]@@`), and the base declaration (candidate L22, section 3). The original's intro sentence (original L22) is condensed into the first of these, not translated sentence by sentence; the original's remaining documentation prose (original L19–120) is not carried at all (section 8). The credit title （エンジェル・テーマ, candidate L8) follows the theme name's Japanese form. CSS comments stay in English on both sides (the section banners are identical text). No mistranslation, term drift, or untranslated reader prose was found in what the candidate carries.
- **Why:** P10/KB-18: reader-visible text localizes; code-adjacent text (comments, metadata variables such as `--theme-name: "Angel Theme"`, candidate L40 = original L136) is not reader prose.
- **Verify:** Read candidate L18–22 against original L22 and L26–32; the T5 half of the localize verdict is cited in section 12.
- **Disposition:** T5 judged jointly with T4: FINDINGS, whose items are the P5/P6/P9 charges (section 11) and the thinned usage explanation — the original tells the reader to include the BHL base theme first (original L26–27, L32); the candidate condenses that to the base declaration line. The localize lane recorded the condensation as an information loss at T5 weight, not as a blocking item. Standing at that weight.

## 7. Links

none — no signature for this section fired over 42 change blocks. Ground: the candidate carries exactly one external link, the credit's 元記事リンク (candidate L15), whose host is the original's recorded host (section 1). The original's in-body links — the author user-link (original L22), the `[[[misterfrown|Example Link]]]` exhibit and the borealis-constant-theme asset exhibit (original L43–48) — lived in the documentation body the port does not carry (section 8), so no link target had to be repointed or probed. The usage reference is the escaped self-include (candidate L20), which names the candidate's own page.

## 8. Structure

- EXHIBIT-RESTRUCTURE (C): Usage/sample exhibits dropped or replaced (R3): a sanctioned replacement and a silent deletion have the same diff shape; the ground must be stated.
  Verify: The exhibit-decision slot for this block, argued from the mirror.
  - B3: orig 8-122 -> cand 26-26 (body -> module-css)
  - B42: orig 532-538 -> cand at 430 (body -> body)

- **Exhibit decision, B3 (original L8–122):** replaced in part, dropped in part. Replaced: the bare `[[module Rate]]` in its `[[>]]` div (original L8–10) — its function is carried by the rate-bearing preview credit module (RATE-EXHIBIT-KEPT-CANDIDATE fires inside this block), and the usage instruction survives in condensed form (candidate L20, section 6). Dropped: the Examples showcase (headings, the image-block exhibit, a live footnote, blockquote, table, tabview; original L36–116) and the Source Code section furniture around the exhibit. The ground is the port's recorded form: the localize lane read this exact restructure, recorded that the original's documentation body was removed wholesale and replaced with the short JP lead, and judged the specimen-section omission within the S2 delivery form's tolerance, charging only the usage-explanation thinning (section 6). A footnote consequence, checked explicitly: the original's live `[[footnote]]` (original L48) sits inside the dropped Examples, and the original carries no `[[footnoteblock]]` anywhere; the candidate has neither footnote nor footnoteblock — parity, no orphan.
- **Exhibit decision, B42 (original L532–538):** dropped. The tail holds the two component includes (section 2) and the tail self-delivery module (section 3); both fell with the delivery restructure, on the grounds stated in those sections.
- **CSS-BODY (B2)** is resolved in the appendix and written in section 3 (the original head module's base imports).

## 9. Formatting only

- WS-ONLY blocks: 36
- Re-indentation: 0 blocks pair up after leading-whitespace normalization

The 36 WS-ONLY blocks are one shape repeated: inside the moved CSS, the candidate's blank lines carry a single trailing space where the original's are empty. Counted here so the churn is not mistaken for content change; the colour censuses in the per-theme record were run over tokens and declarations, which this whitespace cannot affect, and the one window where it does touch bytes (the `#top-bar` window) is named there.

## 10. Porter annotations

none — no signature for this section fired over 42 change blocks. Ground, checked explicitly because annotations ride inside other blocks: the candidate carries no porter-note prose — no [JP] markers, no translator's notes, no added commentary in the CSS (its comments are the original's English section banners, byte-identical). The only added non-original prose is the credit block (section 1), the three prose lines (section 6), and the frame include (section 2), each treated at its own section.

## 11. Dispositions and exceptions

- **Item 15 (class E), the unreadable top-nav — DISPOSITIONED.** The full argument is the per-theme record below; its one-sentence form is that every colour value on the charged surface is byte-identical to the original's, so the unreadable nav is the original theme's own colour design (BHL's near-white text variable over the theme's light-pink `--gray-monochrome: 244, 187, 255`), not a defect the port introduced. [GOSIGN2-LEDGER-SUPPLEMENT.md item 15; FIX5-CONTRA §2; KB-28 family, patterns/ at commit 9c5e9079afb01d30cb9fc4ef9d714e5591eb2ffa]
- **P5, the three star-asset hotlinks (candidate L118, L131, L159) — DISPOSITIONED, class (ii) / KB-58.** The URLs are byte-identical to the original's (original L214, L227, L255) and name the original's own files on its own host. Re-hosting to JP storage is deferred to posting under the campaign's deferred-asset-hosting state (KB-58); these lines are the T1 baseline's three errors and this package's re-run's three errors (section 12).
- **The ≤375 site-header doubling — X1, not charged to the theme.** The render row separates it as a site-theme phenomenon (KB-35 family) [GOSIGN2-LEDGER.md §(c2), angel row].
- **P9, header strings in English — DISPOSITIONED (ruling 2).** `--header-title` / `--header-subtitle` are unchanged from the original (section 5); header/title language is out of scope for migration correctness [GOSIGN2-LEDGER.md §(c3), angel row].
- **P6 — FIXED, not a disposition:** the missing translation-module frame the localize lane charged was supplied by the frame waves and stands in its remedied form (section 2) [GOSIGN2-LEDGER.md §(c3), angel row].
- **The verdict stamp's STALE** is explained, not a disposition: the candidate changed after the verdict by exactly one line (the frame `theme=` parameter dropped by commit 722ceb5, section 2). The re-judgement on the current bytes is this package; the colour ground of item 15 does not touch the changed line.

## 12. Verification

- **T1 (source check):** baseline 2026-11-16: exit 1, 3 errors / 1 warn / 1 info — hotlink×3 (at the baseline file's L113/L126/L154), warn `no-interwiki-style`, info `!important`×1 [T1-ROWS row 56]. Re-run for this package (2026-11-17, the campaign checker `check_source.py` on this package's candidate.txt, `--kind theme --translation --check-links`): exit 1, **3 errors / 0 warns / 1 info** — the error multiset is unchanged (hotlink×3, now at candidate L118/L131/L159, the dispositioned P5 lines); the baseline's `no-interwiki-style` warn is gone because the frame include now stands at candidate L1–3; the `!important` info (candidate L325) is inherited from the original's CSS. No class (i) error stands against this candidate.
- **T2/T3 (render):** combined verdict FINDINGS [RENDER-ROWS-1 (RENDER-S2-A §12)]. The one candidate-specific item is item 15 (dispositioned, section 11); the lane's separation assigns the rest to cross-cutting classes (X1 header doubling, X2 preview clipping, X4 credit-modal preview form, X5 bblock contrast, X7 runtime hotlinks, X8 sidebar warn). No re-render was run for this package: the render record is the lane's, cited, not re-measured here.
- **T4 (follow-up diff):** `diff --from 6` → rev6 → rev6, no change; the original's current revision is still 6 [LOCALIZE-S2-A EN3 follow-up]. The mirror in this package is therefore also the current original.
- **T5 (translation text):** judged jointly with T4 by the source report: FINDINGS on the P5/P6/P9 items and the usage-explanation thinning (sections 6 and 11); the lane found no mistranslations or untranslated reader prose in what the candidate carries.
- **This package:** `python3 review/build_review.py --check` — the verdict stamp regenerates identically from the two files in this package, and the package is not in the pre-existing stale set (the refresh-3 population). The censuses in the per-theme record were re-derived from this package's two files while this README was written, not transcribed from the supplement.

## Per-theme record

### The colour-identity disposition (ledger §(e) item 15)

The charge, as the ledger states it: item 15 [E] (KB-28 contrast) — the top-nav text is near-white on light pink and unreadable at all widths, and the render lane records it as candidate-specific [GOSIGN2-LEDGER.md §(e) item 15; RENDER-S2-A §12: "a candidate-specific colour/contrast finding missed by the machine (the machine skips text on background images)"]. Class E charges a candidate-side defect, so the question the disposition turns on is narrow and decidable from the two files in this package: did the port change any colour on the charged surface? The supplement's ground is that it did not: "candidate vs original colour value sets byte-identical (line citations both sides; machine colour-token multiset comparison)" [GOSIGN2-LEDGER-SUPPLEMENT.md (a) item 15; REPORT-GOSIGN2-FIX5-CONTRA.md §2]. Re-measured from this package's files:

1. **Whole-file colour-token census.** Every colour token in each file (hex values, `rgb()`/`rgba()`/`hsl()` functions, and numeric triplets): 49 tokens, 16 distinct values, on each side; the multisets are identical.
2. **Declaration census.** Every colour/background-bearing declaration (`color`, `background`, `background-color`, `background-image`, `border-color`, `text-shadow`, `box-shadow`, `outline-color`, `fill`, `stroke`): 42 declarations on each side; the multisets are identical.
3. **The charged surface itself.** The `:root` palette window — original L145–151 = candidate L49–55 — is byte-identical including its blank line (SHA-256 window prefix `7825876c9c544621` on both sides). The light pink of the charge is `--gray-monochrome: 244, 187, 255`, the original's own value. The `#top-bar` windows (original L234–248 / candidate L138–152) carry the same declarations line for line — `--topmenu-category-hover-color: var(--swatch-text-light)`, `--topmenu-category-color: var(--black-monochrome)`, `background: rgb(var(--gray-monochrome))` — and the window hashes differ only because two blank lines inside the candidate's window carry the trailing space of section 9's WS-ONLY shape; every non-blank line is byte-identical. The near-white foreground is BHL's `--swatch-text-light` variable, defined in neither file; the candidate overrides no colour on this surface.
4. **No structural colour accident.** A brace-depth scan of both files' CSS (max depth 2, final depth 0, no negative excursion on either side) excludes a displaced brace silently re-scoping the rules after it.

The conclusion the identity licenses: the candidate renders the top navigation with the original's own palette, the original's own top-bar rules, and the base theme's own text variable, so the unreadability the T3 walk photographed is a property of the original theme's colour design, and "fixing" it would mean departing from the original — an editorial change, not a migration correction. Disposition: **DISPOSITIONED, no edit** [GOSIGN2-LEDGER-SUPPLEMENT.md item 15; FIX5-CONTRA §2].

### Second-reviewer walk

The class asks for the disposition to be walked once more from the third-party perspective: is the ground stated in terms a reader who did none of the work can check, and does it hold? The ground here is two named windows and two whole-file censuses, every one reproducible from `original.txt` and `candidate.txt` alone with a text editor and a hash tool; no step asks the reader to trust the FIX5 lane's file copies (its line citations were taken on campaign copies whose numbering differs from this package's, and this record re-derived each number from the package files). The walk re-ran each measurement and each held exactly, including the one place the bytes differ at all inside a charged window (the two trailing-space blank lines, named above rather than smoothed over). One limit is stated for completeness: the census proves the port introduced no colour change; it does not prove the original's nav is readable — the render evidence says it is not, on the original's design, which is precisely what the disposition records. Walk outcome: **the disposition is sound as stated.**

### Record discrepancies flagged by this package

1. **The sources.tsv supersession note is wrong.** The angel row's note claims the original was "superseded upstream since the reference revision; follow-up diff artifact diff-angel-from6.txt in the campaign record (K5a-i)". The cited artifact records the opposite: the follow-up diff is rev6 → rev6 with no changes, and the original's current revision is still the reference revision 6 (LOCALIZE-S2-A EN3 follow-up, section 12 above). Where the artifact records revN → revN with no changes, the note cannot stand. The correct form, recorded here for the coordinator's harvest correction (this package does not edit sources.tsv): the note should state that the original has **not** been superseded — current rev == reference rev 6, follow-up diff artifact diff-angel-from6.txt records rev6 → rev6, no changes (K5a-i).
2. **The localize lane's line citations are superseded.** LOCALIZE-S2-A judged a 424-line candidate; the current file is 429 lines, and its credit values differ (section 1). Every citation in this README is to the package files; where a lane's finding is cited, its substance was re-checked against the current bytes before being carried (the P7 case in section 4 is the worked example: charged against the old file, overtaken by commit 1869877).

### Multi-wave provenance

The candidate's current state is the product of successive waves, not one pass: the Stage 2 EN batch 1 port (commit 3205f27) produced the compact delivery form the localize lane audited (LOCALIZE-S2-A, EN3); commit 1869877 (FIX-CREDIT-D, translator attribution normalization over 163 files) also carried this file's frame include and its JP font supplement (sections 2 and 4); FIX5-CONTRA closed the theme's only blocking item as a no-edit disposition, so no FIX5 commit touches this file; and commit 722ceb5 (frame self-address remedies, sub-shape (B)) dropped the frame's dead `theme=` parameter — the one-line delta behind the stamp's STALE. Citations, in place of a changelog: GOSIGN2-LEDGER.md §(c2) (render row), §(c3) (localize row), §(e) item 15; GOSIGN2-LEDGER-SUPPLEMENT.md item 15; REPORT-GOSIGN2-LOCALIZE-S2-A.md (EN3, angel); REPORT-GOSIGN2-RENDER-S2-A.md §12; REPORT-GOSIGN2-FIX5-CONTRA.md §2; FIX-FRAMEADDR.md (scout folder). The go-sign over that record is what the Status block certifies.


### Post-package repairs (REFRESH3-D)

Recopy was a verified no-op: `candidate.txt` is byte-identical to the current canonical `pages/theme:angel-jp.txt`. No repair lands after this package's candidate build, so the record below is the slice's sub-shape and remedy, confirmed present in the built bytes.

- **FIX-FRAMEADDR, sub-shape (B) — Introduced** (report `R/review-scout/FIX-FRAMEADDR.md` §2; landing `722ceb5c949172bb5185d51ef56ce4119ee4fa91`, 2026-11-17): the original carries no interwiki-style frame and no `theme=` self-address in that role; the porting wave introduced the frame with `theme=` naming its own draft-host `local--code/theme%3Aangel-jp/1`, a fragment the page does not carry (delivery is the inline `[[module CSS]]`). Remedy: the single `| theme=...` line was deleted; the frame include and its `priority=1` line are kept. Current candidate frame at L1.
- The frame remedy and its STALE consequence are already narrated in sections 2, 11 and the multi-wave provenance; this subsection records the sub-shape for the slice.

Stamp treatment follows the jiha-jp / alexylva-university-jp precedents: the regenerated verdict stamp reads STALE, no re-judgement is fabricated, and the frozen GOSIGN2 ledger remains the verdict record.

## Appendix — residue blocks

### Residue R1 — B2 (heuristic; orig 4-6 -> cand at 25, module-css -> body)
- Removed first line: @import url("https://nu-scptheme.github.io/Black-Highlighter/stable/styles/normalize.min.css");
- Note: no other signature matched

Resolution: assigned to section 3, not a residue. B2 is the original head module's content — the normalize @import (original L4), the Black Highlighter @import (original L5), and the module close — ending with no candidate counterpart because the candidate's delivery is the inline module plus the composition's base layer (section 3 states the ground and the render evidence). No new signature is proposed: the shape is the delivery restructure the DELIVERY-MOVE topology already names, caught here as a heuristic only because the removed lines sit in the original's head module rather than in the moved exhibit.

## License and attribution

- **Title:** Angel Theme
- **Author:** MisterFrown
- **Source:** https://scp-wiki.wikidot.com/theme:angel — revision 6
- **License:** Creative Commons Attribution-ShareAlike 3.0 (CC BY-SA 3.0) — license deed: https://creativecommons.org/licenses/by-sa/3.0/
- **Adaptation:** This package holds a Sigma-10 migration port of the work; changes were made. See "Summary" and "Standing sections" in this README for what changed and why. Translator: AI (Muse and its delegated agents), per the campaign's standing attribution rule.
