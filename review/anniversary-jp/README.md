# Review package — theme:anniversary-jp (KO → JP port)
New to this package's shorthand? Read the notation key first: [How to read a review package](../HOW-TO-READ.md).

<!-- BEGIN GENERATED VERDICT STAMP — do not hand-edit; regenerate with review/build_review.py -->
## Verdict stamp
- Theme: theme:anniversary-jp — origin KO, population #252 [GOSIGN2-LEDGER (b) row 252]
- Overall: STALE — candidate file changed since the verdict was computed (verdict against 435a6bb-era content, file sha256 now 262a2e8f23b96b3af72534081bc727d00dbd7b7361d2833168034b705237e34d); the verdicts below were computed against that pre-change file, and the record verdict stands: a candidate revised through the campaign's recorded repairs is posted like a PASS row, with the change recorded in its package
- T1 (source check): FINDINGS (classified) — baseline 2026-11-16: exit 1, 3 errors / 0 warns / 1 info (pseudo-ref×3); standing classes dispositioned in register c1 [T1-ROWS row 235; GOSIGN2-LEDGER (b) row 252]
- T2/T3 (render, combined verdict): FINDINGS — [combined T2/T3] report `FINDINGS` — page runtime-hotlink site-theme chain only; sample credit-modal (preview-form) + 884px@768 overflow; T3 none beyond cross-cutting items. [RENDER-ROWS-2 (RENDER-S2-H (KO1))]
- Engine coverage: full matrix as run by the lane; coverage not separately caveated in the row [RENDER-ROWS-2 row]
- Credit modal: sample credit-modal errors dispositioned preview-form (credit:start-preview has no modal mechanism; GOSIGN-TESTS T2 amendment, 2026-11-16) [RENDER-ROWS-2 (RENDER-S2-H (KO1))]
- T4 (localize patterns + follow-up): FINDINGS — display-affecting findings: 3 [LOCALIZE-ROWS row 251, source LOCALIZE-S2-F]
- T5 (translation text): FINDINGS — the source reports judge T4/T5 jointly; one verdict word covers both [LOCALIZE-ROWS row 251]
- FIX5 re-judgement: none — no OPEN items at the ledger determination [GOSIGN2-LEDGER (b) row 252]
- Computed against: canonical commit 780e0485dc89a41ccdf8671591c08bc887984edb; candidate file pages/theme:anniversary-jp.txt sha256:262a2e8f23b96b3af72534081bc727d00dbd7b7361d2833168034b705237e34d; record: GOSIGN2-LEDGER.md + GOSIGN2-LEDGER-SUPPLEMENT.md as of the FIX5 head 435a6bb
<!-- END GENERATED VERDICT STAMP -->

## Status

| | |
|---|---|
| Verdict | **PASS** — passed at the ledger determination; this theme had no OPEN items and no §(e) register entry (GOSIGN2-LEDGER (b) row 252). The stamp above is the generated record of that determination and is reproduced as it stands |
| **DEFECT FLAG — REPAIRED** | **A closing brace was displaced in the candidate's code block as built: the `#page-title` rule opened at candidate L93 was never closed, and one extra `}` stood at old candidate L499. A brace-depth scan of the as-built bytes showed depth ≥ 1 continuously from L93 to L498, returning to 0 only at L499 — so every rule after L93 was nested inside the unclosed block and did not take effect as a top-level rule. The localize row flagged the same loci as a suspicion needing staff confirmation, and no (c3) disposition covers it. The flag is now closed: the repair has landed (canonical commit 0c327f3; the sweep lines were re-applied on top in 780e048), a `}` now closes the rule after candidate L94 (new candidate L95), the extra `}` at old L499 is removed, and this package documents the corrected candidate. Full evidence in the per-theme record** |
| Standing items | **DISPOSITIONED** — T1 pseudo-ref ×3 (class (iii)); the render row's hotlink-chain, credit-modal, and overflow items (ledger (c2), section 11); T4's P7 and P9 items per the ledger (c3) line — with the font-name half of P7 confirmed live in the as-built bytes alongside the brace flag and since repaired with it (section 4) |
| Go-sign basis | COMPLETION-REPORT.md §10 (go-sign issued; 81 FIXED / 26 DISPOSITIONED / 0 OPEN across the sweep) |
| Named exception | None for this theme (the sweep's single named exception is theme:amethyst-v2, which has no candidate) |

## Provenance

| | Original | Candidate |
|---|---|---|
| Page | theme:anniversary | theme:anniversary-jp |
| Wiki | scpko.wikidot.com | SCP-JP Sigma-10 candidate (canonical repo) |
| Reference revision | 37 (the candidate's credit block records 初訳時参照リビジョン: 37) | — |
| Source of this copy | Campaign mirror store (class COPY, hash-verified against review/sources.tsv) | Canonical file `pages/theme:anniversary-jp.txt`, copied at worktree HEAD 1605bbd |
| Lines / bytes | 466 lines / 10,027 bytes | 517 lines / 12,674 bytes |
| SHA-256 | ec78031de3ec64b9673476850a303ad599801f37508082216c8eefe08db5da6d | 20cdbc6bd6b4c6f71e9b97523c94e3988133e8f32ee48b13f876294967add2bc |

Wave history: the candidate was created by the Stage 2 KO1 integration (commit 18280b3); FIX-CREDIT-D (1869877, translator attribution normalization; the stamp's computed-against commit) touched it later.

## Summary

A compact KO year-end-event theme (年末競演， "year-end competition") whose original is a parameterized include: its tail module defines color defaults through `{$custom}` fallbacks and a hue-rotate filter from `{$h}`/`{$s}`/`{$b}`, with a hidden self-include supplying defaults. The candidate freezes those parameters to their default values so the theme page stands alone (explained in a porter 訳注）, moves the delivery module to the head, replaces the KO info block with the preview credit block, swaps the noonnu @font-face for Google Fonts imports, adds a license box the original lacks, and translates the short body. Two byte-level defects rode along as built, both flagged in this package and both since repaired: the displaced closing brace that swallowed the code block from L93 onward (per-theme record) and heading stacks that still named the retired @font-face family (section 4). The repairs landed in canonical commit 0c327f3 (fix report FIX-MPURE1.md in the campaign record, R/review-scout/), with the usage-example sweep lines re-applied on top in 780e048; this package documents the corrected candidate. Measured churn (diff.md, the generator's difflib count with autojunk off: +161/−115, 276 changed lines in 70 change blocks; a GNU-diff count of the same pair gives 265 changed lines — the difference is alignment choice, not content).

## Class summary

Auto-classification by review/classify_hunks.py (signature table 2026-11-17.1): 70 change blocks — 65 specific (92.9%), 5 heuristic (7.1%), 0 residue, 0 skipped. The specific share is the batch's highest, and it is carried by one counted class: 57 of the 70 blocks are WS-ONLY, whitespace-only line pairs inside the code block (section 9). Pattern citations below name the KB entry; the patterns/ tree state cited throughout is commit 9c5e9079afb01d30cb9fc4ef9d714e5591eb2ffa.

| Label | Blocks |
|---|---|
| WS-ONLY | 57 |
| CSS-BODY | 4 |
| DRAFT-HOST | 4 |
| SELF-DELIVERY | 3 |
| TRANS-UNANCHORED | 3 |
| IFTAGS | 2 |
| INFO-DEL | 2 |
| LICENSE-BOX | 2 |
| ANNOTATION | 1 |
| COMMENT-TEXT | 1 |
| CREDIT-PREVIEW | 1 |
| DELIVERY-HOST | 1 |
| FONT-IMPORT | 1 |
| JPFONT-LOAD | 1 |
| KB06-DEFAULT | 1 |
| TASL-FIELDS | 1 |
| TRANSLATION-ANCHORED | 1 |

Adjudication for this README: the WS-ONLY mass is genuine whitespace churn (section 9), but two of the five CSS-BODY heuristic blocks are not routine: B6 (original L35–37 → candidate L94) is the hunk where the `#page-title` closing brace disappears, and B67 (original L453–454 → candidate L499–501) is where the extra brace stands. Both are adjudicated in the per-theme record, not in section 9. After adjudication no block is left unexplained.

## Standing sections

### 0. Header and provenance frame

- **What:** Theme theme:anniversary-jp; original theme:anniversary on scpko at reference revision 37; candidate `pages/theme:anniversary-jp.txt`. Provenance route: derived from the original at the reference revision by the Stage 2 KO1 wave (sources.tsv kind: standard; no production JP counterpart exists, so the R4 adoption question does not arise). The frame order differs from the original's: the candidate opens with its delivery module and the interwiki frame (candidate L1–8), then the localized gate (candidate L10); the original opens with its gate and info block, and its delivery module sits at its tail (original L433–454).
- **Why:** Section 0 declares the provenance route so every later count is read against the right baseline; the gate's tag is P2, the frame is P6/T3 (section 3).
- **Verify:** The sources.tsv row for anniversary-jp; `sha256sum original.txt` against the Provenance table.
- **Disposition:** Standing (the route itself); the gate and frame changes are recorded in section 3.

### 1. Credit and attribution

- **What:** The original's furniture is a `:scpko:info:start`/`end` block (original L2–9) naming the theme, its maker and image maker ([[*user thd-glasses]] for both), and a font-information link. The candidate deletes the info block (INFO-DEL ×2, blocks B1–B2) and carries a `:scp-jp:credit:start-preview`/`end-preview` block (candidate L12–21) with the eight ruling-3 fields (タイトル 年末競演 テーマ; 翻訳責任者 AI; 翻訳年 2026; 原題 연말경연 테마; 著作権者 [[*user thd-glasses]]; 作成年 2021; 初訳時参照リビジョン 37; the source link, candidate L20, naming `scpko.wikidot.com/theme:anniversary` — the original's recorded host). The info block's font information is not lost: it returns in the license box's font attribution (section 8). License box (T4): the candidate ADDS one the original lacks (candidate L502–516, `:scp-jp:component:license-box-backend`/`license-box-end`): the header image anniversary_h.png attributed to thd-glasses with its license honestly recorded as not stated in the original (原語版に記載なし（投稿前に著者へ確認してください)) and its source named (scpko.wdfiles.com); and the fonts attributed with their SIL Open Font License and the substitution note of section 10.
- **Why:** P3/T1: KO themes target the info module on their home branch, but the JP candidate form is the preview credit block (the campaign's settled JP furniture), and ruling 3 fixes its fields. The license box addition is T4 applied where the original left its image license unstated: the box records the gap instead of inventing a license.
- **Verify:** Read candidate L12–21 and L502–516 against original L2–9; `grep -n 'info:start' candidate.txt` returns nothing.
- **Disposition:** Applied; the license gap is recorded in the box itself, as found.

### 2. Includes and components

- **What:** The candidate's live includes are the credit pair (section 1), the frame (section 3), the documentation's `component:image-block` exhibit (candidate L36, its image re-hosted to the draft host, section 4), and the license-box pair (section 1). The original's hidden default self-include (original L455–466: a `[[#ifexpr {$custom} == 0 | default | ...]]` construct including `:scpko:theme:anniversary` with custom=0 parameters) is deleted with the parameterization it served (section 5). No live include names a foreign-wiki target.
- **Why:** P1 (KB-15): includes name JP counterparts or bare component names. The default self-include is not an include repoint but a mechanism part, removed with its mechanism and explained by the porter's note (section 10).
- **Verify:** `grep -n '\[\[include' candidate.txt` — every target is `:scp-jp:` or a bare `component:` name.
- **Disposition:** Applied; no foreign include kept, no named exception needed.

### 3. Delivery and code loading

- **What:** The original delivers from its tail: a `[[module CSS]]` (original L433–454) importing its own code block as `scpko.wdfiles.com/local--code/theme:anniversary/1` (original L434) and carrying the parameterized `:root` defaults and filter rule. The candidate moves delivery to the head: a `[[module CSS]]` (candidate L1–3) importing `local--code/theme%3Aanniversary-jp/1` from the draft host, the interwiki frame after it (candidate L5–8, priority 1, same address), and the tail module's `:root` content folded into the code block's own end (candidate L489–498) with its `--header-logo` address repointed to the draft host (candidate L490). The code block itself sits inside the documentation's collapsible (candidate L64–500). T1's three pseudo-ref errors are these draft-host addresses (head import, frame, and the re-hosted exhibit image of section 2).
- **Why:** P4 (own-code delivery served from JP hosts) and P6/T3 (the frame); the draft-host form is KB-41, class (iii), rewritten at posting. Folding the defaults into the code block is what lets the theme page stand alone once the tail module's include-parameter mechanism is retired (section 5).
- **Verify:** `grep -n 'local--code' candidate.txt` — the head import and the frame line, both draft-host; compare original L433–434.
- **Disposition:** DISPOSITIONED (the draft-host lines, class (iii)).

### 4. Fonts and assets

- **What:** The original defines its display face by @font-face: family 'GowunBatang-Bold', a noonnu woff served from jsdelivr (original L12–17), and its heading stacks name that family (original L30, L145, L159). The candidate removes the @font-face and imports three Google Fonts families at the code head (candidate L66–68: Noto Sans JP, Noto Serif JP, and Gowun Batang, each 400;700) — and as built the heading stacks still named 'GowunBatang-Bold' (candidate L89 and, in the as-built numbering, L202 and L216), a family the candidate no longer defined anywhere: the Google Fonts family is "Gowun Batang", a different name. The named family therefore resolved to nothing and headings fell back to the Arial/sans-serif tail of the stack. That is LOCALIZE-ROWS row 251's type-7 item (font-name mismatch causing heading fallback), confirmed in the as-built bytes. The repair has since landed (canonical commit 0c327f3): all three stacks are renamed to 'Gowun Batang' (candidate L89, L203, L217 in the current numbering), and because the import serves Gowun Batang at 400;700 and the three stacks sit on heading selectors whose default weight is bold, the headings reach the served 700 weight — the bold face the retired family name denoted. The license box's font note (candidate L512–515) records the substitution's intent (the noonnu woff has no JP direct-link exception, so the same typeface comes from Google Fonts), which makes the stack residue a naming slip, not a design choice. Assets: the header image anniversary_h.png is re-hosted to the draft host in the code (candidate L489) and in the exhibit (candidate L36); no hotlink errors stand against this theme in T1.
- **Why:** P7/T5 with KB-16: a font substitution is complete only when loads and stacks name the same family; here the load half was done and the stack half kept the retired name. The mechanical repair (rename the three stacks to 'Gowun Batang') has since landed, as recorded in the What above.
- **Verify:** `grep -n 'Gowun' candidate.txt` — the import at L68 names Gowun+Batang; the stacks at L89, L203, L217 name 'Gowun Batang'; `grep -c '@font-face' candidate.txt` returns 0.
- **Disposition:** DISPOSITIONED in the ledger (c3) line as P7 (recorded, in the line's words, without a display-affecting mark; T4 bar) — recorded here with the tension that the row marks the item display-affecting and the as-built bytes confirmed the mismatch; the flag is closed by the repair landed in 0c327f3, alongside the brace flag.

### 5. Header, sidebar, and site furniture

- **What:** The theme's variability is its header: yearly color presets and a subtitle, taken by the original as include parameters (`{$custom}`, `{$subtitle}`, `{$h}`/`{$s}`/`{$b}`) with fallbacks in its tail `:root` (original L436–453) and a hue-rotate filter rule. The candidate freezes the mechanism (KB06-DEFAULT, block B64): the code block's final `:root` (candidate L489–498) carries the literal defaults (―color-bg #B01, ―color-ip #000, ―font #FFF, ―shadow transparent, ―header-sub "年末競演専用テーマ"), and the hidden default self-include is deleted (section 2). The porter's 訳注 at candidate L31 states the change and its reason (the JP candidate stands alone as a theme page, so the defaults are fixed: custom=1-equivalent colors and the Japanese subtitle). LOCALIZE-ROWS row 251's type-9 item (a Korean header string at the row's L209) belongs to this section's family; the shipped subtitle default is Japanese, and the item is dispositioned under ruling 2.
- **Why:** P9/T6 for the furniture; KB-06 for the defaults: a parameterized original ported as a standalone page must have its defaults materialized somewhere, and the candidate materializes them in the code with the change disclosed in-file. Ruling 2 grounds the header-language disposition.
- **Verify:** Read candidate L489–498 against original L436–453, and the 訳注 at candidate L31.
- **Disposition:** DISPOSITIONED (P9, ruling 2: header/title language out of scope); the parameter freeze is standing, disclosed in-file.

### 6. Text translation

- **What:** The body is short and translated whole: the description (candidate L23: a Sigma-9-based year-end theme with per-year color parameters), the usage line and its include exhibit (candidate L27–29, the include shown as `:scp-jp:theme:anniversary-jp` — completed to the posting name by the usage-example sweep; per-theme record), and the standard examples (candidate L34–62). One TRANSLATION-ANCHORED block (in B64's region, the subtitle default 年末競演専用テーマ for 연말경연 전용 테마） and three TRANS-UNANCHORED blocks carry it; one COMMENT-TEXT block is an R1 comment translation inside the code. The credit block's 原題 field keeps the Korean title as the work's name (section 1).
- **Why:** P10 and KB-18 (reader-visible strings).
- **Verify:** The body sections of diff.md in order; a Hangul scan of candidate.txt returns the 原題 field and no prose.
- **Disposition:** Standing (the port itself).

### 7. Links

- **What:** The credit source link (candidate L20) names the original's recorded host (section 1). The original info block's font-information link (noonnu.cc, original L8) leaves with the info block; the font's provenance is carried instead by the license box's attribution (section 1). The license box's source line names scpko.wdfiles.com, where the header image actually lives. No prose link in the candidate targets a KO-wiki page, and no `http://` address remains (the original's import at L434 was scheme-relative in form `url(https://…)` on the candidate side throughout).
- **Why:** P11: links name the serving original or the record's home.
- **Verify:** `grep -n 'http://\|noonnu' candidate.txt` returns nothing for either.
- **Disposition:** Standing; no dead link carried.

### 8. Structure

- **What:** The closing rule is where this package must be precise. The file's architecture is preserved: gate, credit, documentation with the code exhibit, license box, closing `[[/iftags]]` (candidate L517), with delivery moved from tail to head (section 3) and the defaults folded into the code (section 5). The exhibit census is one-to-one. But inside the code block the rule structure was broken as built by the displaced brace: from candidate L93 the rules no longer closed at the top level, so the block's architecture, as parsed, was one unclosed `#page-title` rule containing everything after it. That was not a structural choice; it was the defect of the per-theme record, stated here because section 8 is where a reviewer looks for "is the structure sound?" The repair has since landed (canonical commit 0c327f3): the rule now closes after candidate L94 and the rules after it close at the top level again, so the CSS rule structure is sound in the candidate this package documents.
- **Why:** R3 forces the census (which passes); the brace defect is charged to the per-theme record with its own evidence, and cross-stated here so this section does not certify what the record refutes.
- **Verify:** The brace-depth scan of the per-theme record, re-runnable from the package's candidate.txt alone.
- **Disposition:** Standing as to file structure; the rule-structure defect was flagged, not dispositioned, and is now repaired (0c327f3; per-theme record).

### 9. Formatting only

- **What:** Fifty-seven WS-ONLY blocks: line pairs inside the code block that differ only in whitespace (the KO source carries trailing spaces, space-only blank lines, and a leading space on many rule lines; the candidate normalizes some of each). No re-indentation signature fires (0 blocks), and no WS-ONLY pair changes any token. The count is disclosed as its own class precisely so it is not mistaken for 57 semantic changes — and so the two non-whitespace CSS-BODY blocks (B6, B67) stand out as the exceptions they are: they are not in this section, they are in the per-theme record.
- **Why:** Formatting churn is disclosed as its own class so it is never mistaken for a semantic change, and so a reviewer can skip it safely.
- **Verify:** The WS-ONLY sections of diff.md; classification.json's label counts.
- **Disposition:** None required.

### 10. Porter annotations

- **What:** Two, both doing real work. (1) A `//…//`-form 訳注 at candidate L31, directly under the credit block: it records that the original takes the custom/subtitle/h/s/b parameters and that the JP candidate fixes the defaults so the theme page stands alone (section 5's change, disclosed at the point of use). (2) A 訳注 inside the license box (candidate L514–515): the original reads the Korean Gowun Batang woff directly from jsDelivr, which has no JP direct-link exception, so the same typeface is substituted from Google Fonts (section 4's change, disclosed in the attribution). The classifier labels one ANNOTATION block (B70); both texts are recorded here.
- **Why:** R2: porter-added text is part of the change record; both notes explain a mechanism change a future editor would otherwise have to reverse-engineer.
- **Verify:** Read candidate L31 and L512–516.
- **Disposition:** Standing.

### 11. Dispositions and exceptions

- **What:** Three items, each with its ground — and one item that is NOT dispositioned, stated as such. (1) T1's three pseudo-ref errors: class (iii) draft form (KB-41), the delivery addresses of section 3. (2) The render row's items, all DISPOSITIONED in the ledger (c2) register: the page's runtime-hotlink site-theme chain (environment-layer: runtime hosts arrive via the shared site theme chain, not the candidate — KB-40) and the sample's credit-modal (preview form) with 884px@768 overflow (the recorded cross-cutting families: static credit replica fixed width, KB-33; preview chrome, KB-34). (3) T4's P9 item DISPOSITIONED (ruling 2) and its P7 item DISPOSITIONED per the (c3) line, with section 4's tension recorded. NOT dispositioned anywhere in the (c3) outcomes: the CSS syntax item (the unclosed block at the row's L93–95 and the stray `}` at its L499), which the row itself left as a suspicion needing staff confirmation. This package's depth scan was that confirmation, and the item was carried as a defect flag (per-theme record), not folded into a disposition it never received. The flag is now closed by repair, not by disposition: the brace repair landed in canonical commit 0c327f3 (780e048 re-applied the sweep lines on top).
- **Why:** A disposition is a decision with grounds (AGENTS.md §3 classes (i)/(ii)/(iii); the named KB entries), not an omission; an item no record decided is reported as undecided, with the evidence that now decides its factual half.
- **Verify:** Each item names its deciding record above; the undecided item's evidence is the per-theme record's scan.
- **Disposition:** DISPOSITIONED (items 1–3); the syntax item was flagged, not dispositioned, and has since been repaired (0c327f3).

### 12. Verification

- **What:** (a) T1 source check (T1-ROWS row 235): exit 1, 3 errors / 0 warns / 1 info; the errors are pseudo-ref ×3, the standing class of section 11(1); there is no class (i) error — and no T1 signature exists for brace balance, which is why the defect of the per-theme record is invisible to this row. (b) T2/T3 render (RENDER-ROWS-2, lane RENDER-S2-H): FAIL/FAIL with FINDINGS, the items of section 11(2), all dispositioned; the row reports no unstyled-page finding, which stood in unresolved tension with the brace defect in the as-built bytes — either the render ran against a candidate state before the brace was displaced, or the sample's delivery did not exercise the code block's later rules; this package records the tension and does not adjudicate it. The defect itself has since been repaired (0c327f3), and this package documents the corrected candidate. (c) T4/T5 (LOCALIZE-ROWS row 251): FINDINGS jointly, display-affecting findings 3, dispositioned as in section 11(3) except the syntax item the row itself left open, which has since been repaired (0c327f3). (d) This package is self-verifying: `python3 review/build_review.py --check` regenerates diff.md and the verdict stamp from the two byte-faithful copies in this directory and compares. Counts in this README are the generator's (difflib, autojunk off): +161/−115 in 70 change blocks; the GNU-diff count of the same pair is 265 changed lines.
- **Why:** Verification claims name the cheapest deciding check and its result, not a general assurance; where two records disagree, both are named.
- **Verify:** Re-run the checker on `pages/theme:anniversary-jp.txt`, the brace scan of the per-theme record, and `python3 review/build_review.py --check` in this repo.
- **Disposition:** PASS (GOSIGN2-LEDGER (b) row 252; go-sign, COMPLETION-REPORT §10) — with this package's defect flag now closed by the repair in 0c327f3.

## Per-theme record

### The displaced brace (defect flag, repaired)

Claim: in the candidate's code block, exactly one closing brace is displaced. The `#page-title` rule that opens at candidate L93 (` #page-title {`, carrying `border-color: var(--color-ip);` at L94) is never closed: the original closes the same rule immediately (original L35–37), and the candidate's next lines are the `/* links */` comment and the `a {` rule. At the block's end, after the final `:root` closes at candidate L497, one extra `}` stands alone at candidate L499, immediately before `[[/code]]`.

Evidence, all reproducible from this package's candidate.txt alone: (1) Raw counts balance — the candidate's code block contains 84 `{` and 84 `}`, exactly the original code block's 84/84 — which is why no count-based check sees the defect. (2) A brace-depth scan (depth after each line, candidate L64–500) returns to 0 for the last time at L91, then stays at depth ≥ 1 continuously from L93 through L498, reaching 0 again only at L499. In the original's code block, 166 lines end at depth 0 (rule-by-rule closure). (3) The classifier's hunks localize both ends: B6 (original L35–37 → candidate L94) is where the closing line disappears, and B67 (original L453–454 → candidate L499–501) is where the extra one stands.

Effect: under CSS parsing, the rules from L94 to L498 are nested inside the unclosed `#page-title` block and do not take effect as top-level rules (under pre-nesting parsing they are consumed as malformed declaration content; under nesting-aware parsing they apply, if at all, only as descendants of #page-title). The theme's links, sidebar, and variant rules — the bulk of its CSS — are in the swallowed range. The theme as shipped in this candidate would render largely on its first 90 lines of CSS and its base.

History: LOCALIZE-ROWS row 251 flagged both loci (L93–95 unclosed block; stray `}` at L499) as a display-affecting suspicion with staff confirmation required. The ledger (c3) outcomes for this theme disposition P7 and P9 and do not mention the syntax item; the render row reports no unstyled finding. The candidate's own history is two commits (KO1 integration 18280b3; FIX-CREDIT-D 1869877), and this package does not attribute the displacement to either. What was proven against the as-built bytes is the state above: the suspicion is confirmed, and the item was never dispositioned.

The repair has since landed (fix report FIX-MPURE1.md in the campaign record, R/review-scout/; canonical commit 0c327f3, with the usage-example sweep lines re-applied on top in 780e048): one brace moved — a `}` inserted after candidate L94, closing the `#page-title` rule as new candidate L95, and the extra `}` at old candidate L499 removed. A post-repair depth scan of the code block shows depth returning to 0 immediately after the inserted close, 177 lines ending at depth 0, and a longest continuous span at depth ≥ 1 of 12 lines (an ordinary nested block); the repaired candidate's top-level selectors number 70, matching the original's 70 one-for-one apart from the @font-face substitution of section 4 and the candidate's trailing JP `:root` block. The flag is closed, and this package documents the corrected candidate; its stamp reads STALE against the pre-repair verdict, by design.

### The usage example's posting name

The usage example at candidate L28 as built read `@@[[include :scp-jp:theme:anniversary]]@@`: the porting wave's repoint changed the branch prefix but left the plain name, so the example named a page that does not exist on scp-jp (the campaign's settled rule for usage examples, AGENTS.md §6). The usage-example population sweep has since completed the reference to `:scp-jp:theme:anniversary-jp` (sweep report SWEEP-USAGE.md in the campaign record, R/review-scout/; canonical commit b5cb724), one of its 287 repairs across 157 candidates; after the M-pure-1 repairs landed on top, the sweep line was re-applied in canonical commit 780e048, which is the form this package documents. This package documents the corrected candidate; its stamp reads STALE against the pre-repair verdict, by design.

## Change set outside the two diffed files

The diff covers two files; the port's record is one file larger. `pages/theme-decoration-sample-anniversary-jp.txt` is the decoration sample the render checks ran against (its credit-modal and overflow states are section 11(2)); it belongs to this theme's record but carries no port change of its own to explain here. The candidate layers over the Sigma-9/JP environment base supplied by the composition (no base include of its own); there are no companion fragments and no inbound-link repairs in other candidates for this theme.

## License and attribution

- **Title:** 연말경연 테마
- **Author:** thd-glasses
- **Source:** https://scpko.wikidot.com/theme:anniversary — revision 37
- **License:** Creative Commons Attribution-ShareAlike 3.0 (CC BY-SA 3.0) — license deed: https://creativecommons.org/licenses/by-sa/3.0/
- **Adaptation:** This package holds a Sigma-10 migration port of the work; changes were made. See "Summary" and "Standing sections" in this README for what changed and why. Translator: AI (Muse and its delegated agents), per the campaign's standing attribution rule.
