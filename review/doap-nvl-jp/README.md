# Review package — theme:doap-nvl-jp (KO → JP port)

<!-- BEGIN GENERATED VERDICT STAMP — do not hand-edit; regenerate with review/build_review.py -->
## Verdict stamp
- Theme: theme:doap-nvl-jp — origin KO, population #260 [GOSIGN2-LEDGER (b) row 260]
- Overall: STALE — candidate file changed since the verdict was computed (verdict against 435a6bb-era content, file sha256 now 07698a5c9e3b3fb93552424022a1c38e79ed04df9663ec7a213821b2644e6d33); verdict not carried over, re-judgement required
> verdicts below describe the pre-change file
- T1 (source check): FINDINGS (classified) — baseline 2026-11-16: exit 1, 8 errors / 1 warn / 0 infos (pseudo-ref×8); standing classes dispositioned in register c1 [T1-ROWS row 264; GOSIGN2-LEDGER (b) row 260]
- T2/T3 (render, combined verdict): FINDINGS — [combined T2/T3] report `FINDINGS` — page runtime-hotlink site-theme chain only; sample credit-modal (preview-form) + runtime-hotlink; T3 none beyond cross-cutting items. [RENDER-ROWS-2 (RENDER-S2-H (KO3))]
- Engine coverage: full matrix as run by the lane; coverage not separately caveated in the row [RENDER-ROWS-2 row]
- Credit modal: sample credit-modal errors dispositioned preview-form (credit:start-preview has no modal mechanism; GOSIGN-TESTS T2 amendment, 2026-11-16) [RENDER-ROWS-2 (RENDER-S2-H (KO3))]
- T4 (localize patterns + follow-up): FINDINGS — display-affecting findings: 1 [LOCALIZE-ROWS row 259, source LOCALIZE-S2-F]
- T5 (translation text): FINDINGS — the source reports judge T4/T5 jointly; one verdict word covers both [LOCALIZE-ROWS row 259]
- FIX5 re-judgement: none — no OPEN items at the ledger determination [GOSIGN2-LEDGER (b) row 260]
- Computed against: canonical commit b5cb7241f527a44933e45599b41df210690771c4; candidate file pages/theme:doap-nvl-jp.txt sha256:07698a5c9e3b3fb93552424022a1c38e79ed04df9663ec7a213821b2644e6d33; record: GOSIGN2-LEDGER.md + GOSIGN2-LEDGER-SUPPLEMENT.md as of the FIX5 head 435a6bb
<!-- END GENERATED VERDICT STAMP -->

## Status

| | |
|---|---|
| Verdict | **PASS** — passed at the ledger determination; this theme had no OPEN items and no §(e) register entry (GOSIGN2-LEDGER (b) row 260) |
| Standing items | **DISPOSITIONED** — T1 pseudo-ref ×8 (class (ii), section 11); the render row's cross-cutting items (KB-40 site-theme chain; KB-32 preview-form credit modal, section 11); T4's one display-affecting item dispositioned as a posting-procedure matter in the ledger §(c3) line (sections 2 and 11) |
| Go-sign basis | COMPLETION-REPORT.md §10 (go-sign issued; 81 FIXED / 26 DISPOSITIONED / 0 OPEN across the sweep) |
| Named exception | None for this theme (the sweep's single named exception is theme:amethyst-v2, which has no candidate) |

## Provenance

| | Original | Candidate |
|---|---|---|
| Page | theme:doap-nvl | theme:doap-nvl-jp |
| Wiki | scpko.wikidot.com | SCP-JP Sigma-10 candidate (canonical repo) |
| Reference revision | 35 (first translation; the candidate's credit block records 初訳時参照リビジョン: 35) | — |
| Source of this copy | Campaign cache `review-wave2-frozen/k3/orig-doap-nvl.txt`, via the mirror store (class COPY, hash-verified against review/sources.tsv) | Canonical file `pages/theme:doap-nvl-jp.txt`, copied at worktree HEAD 5ab991e |
| Lines / bytes | 321 lines / 10,622 bytes | 379 lines / 14,692 bytes |
| SHA-256 | f182da6768fb2c41ae96fdf5472d1e8363c765f54fba2ffb1e120bc66ddb205c | 2bb02e86ab1cd251e4b3c1a7745da4c99f246cc94d72dfad377ab5177bd53e8e |

Wave history: the candidate was created by the Stage 2 KO3 integration (commit 783e87d, the LOCALIZE-S2-F wave's port), reshaped by c65ec92 (rework2-p2: this theme is one of the named receivers — navla/pacom/creepypasta — whose embedded bases were swapped for references), and touched last by 1869877 (FIX-CREDIT-D). No FIX5 commit touches this file. Kind note (sources.tsv K5b-3): the candidate layers over theme:navla-style-jp, so this package's diff covers the theme's own layer; the base is a separate candidate with its own package.

## Summary

DoAP-NVL is the Department of Analytical Psychology's Black Highlighter variant, and in the original it is already a thin overlay: its own CSS sits on the Navla style base (theme:navla-style plus component:navla), delivered from scpko code pages. The candidate rebuilds the same three-layer stack on JP code pages — frame priorities 1, 2, 3 for navla-style-jp, component:navla-jp, and its own layer, all on the draft host — translates the body and the license material, and adds the two JP furniture pieces the original lacks: the preview credit block and the closing license box, whose entries document every image file and both base CSS files with their provenance. The one substantive T4 finding is not in this file's bytes but in its dependency: the base pages it includes do not exist on scp-jp yet, so the theme can only be posted together with them; the ledger dispositioned that as a posting-procedure matter. Measured churn (diff.md, the generator's difflib count with autojunk off: +215/−164, 379 changed lines in 75 change blocks / 6 hunks).

## Class summary

Auto-classification by review/classify_hunks.py (signature table 2026-11-17.1): 75 change blocks — 41 specific (54.7%), 32 heuristic (42.7%), 2 residue (2.7%), 0 skipped. Pattern citations below name the KB entry; the patterns/ tree state cited throughout is commit 9c5e9079afb01d30cb9fc4ef9d714e5591eb2ffa.

| Label | Blocks |
|---|---|
| CREDIT-PREVIEW | 1 |
| COMPONENT-SWAP | 1 |
| DELIVERY-HOST | 1 |
| DRAFT-HOST | 10 |
| ESCAPED-INCLUDE | 1 |
| EXHIBIT-RESTRUCTURE | 1 |
| HEADERVAR | 2 |
| IFTAGS | 2 |
| INCLUDE-REPOINT | 1 |
| INFO-DEL | 2 |
| LICENSE-BOX | 1 |
| LINK-REPOINT | 1 |
| SELF-DELIVERY | 3 |
| TASL-FIELDS | 1 |
| TRANSLATION-ANCHORED | 22 |
| TRANS-UNANCHORED | 38 |
| WS-ONLY | 2 |

Adjudication for this README (every block was read against the bytes): the single EXHIBIT-RESTRUCTURE primary (B75) is the tail furniture swap — the original's closing component includes replaced by the license box and the hidden base include — adjudicated in sections 2 and 8, not a content restructuring. The two residue blocks resolve in the appendix (a one-word translation the differ left unlabeled; the exhibit's porter banner). The TRANS-UNANCHORED mass is the KO body and license-entry translations, the expected heuristic shape on a KO theme, verified in bulk against the mirror for this README. After adjudication no block is left unexplained.

## Standing sections

### 0. Header and provenance frame

- **What:** Theme theme:doap-nvl-jp; ancestor theme:doap-nvl on scpko at reference revision 35; candidate `pages/theme:doap-nvl-jp.txt`. Provenance route: derived from the ancestor at the reference revision by the LOCALIZE-S2-F wave (sources.tsv kind: K5b-3, layered — the candidate layers over theme:navla-style-jp and this diff covers the theme's own layer only). The frame states the layering directly: a head module CSS importing the candidate's own /1 from the draft host (candidate L2), then three `:scp-jp:component:interwiki-style` includes at priorities 1, 2, 3 delivering theme:navla-style-jp /1, component:navla-jp /1, and the candidate's own /1, all from the draft host (candidate L5–17). The original's frame is the same stack in KO form: the gate line, a module CSS importing theme:navla-style /1 from scpko (original L3), and a tail module importing both base and own code pages (original L319–320).
- **Why:** Section 0 declares the route and the layer stack so later counts are read against the right baseline; the stack itself is P6/T3 with T9 delivery (sections 2–3), and the K5b-3 scope statement is what makes the base's absence from this diff a scope fact rather than a deletion.
- **Verify:** The sources.tsv row for doap-nvl-jp; `sha256sum original.txt` against the Provenance table; the frame lines at candidate L1–17.
- **Disposition:** Standing (the route itself); the frame changes are recorded in sections 2 and 3.

### 1. Credit and attribution

- **What:** The original's credit furniture is the KO `info:start`/`info:end` pair (original L6, L16), deleted (blocks B3, B5, INFO-DEL ×2). The candidate installs the JP preview block (candidate L19–28) with the eight ruling-3 fields (title 分析心理学部ブラックハイライターテーマ; translator 翻訳責任者 AI; 翻訳年 2026; 原題 분석심리학부 블랙하이라이터 테마; 著作者 Navla; 作成年 2022; 初訳時参照リビジョン 35; the source link, candidate L27, naming scpko.wikidot.com, the ancestor's recorded host). The candidate also adds the closing license box the original lacks (block B74: `:scp-jp:component:license-box-backend` with author=Navla at candidate L329, `:scp-jp:component:license-box-end` at L374), whose entries — all translated — document each image file (name, author, license, source) and both base CSS files, the latter two carrying the bases' own provenance (theme:navla-style rev 162; component:navla rev 119). The T4 row singles this theme's attribution and license recording out as the batch's best.
- **Why:** P3/T1: the preview credit module is the rate-bearing JP form, so the info pair is deleted rather than duplicated (KB-09); the license box is the JP attribution supplement the T4 license check requires, and its base-file entries are what ruling 4's dependency record looks like in attribution form.
- **Verify:** `grep -n 'info:start\|credit:\|license-box' candidate.txt` — no info pair, one preview pair, one license-box pair; read candidate L19–28 and L329–374.
- **Disposition:** FIXED (GOSIGN2-LEDGER §(c3): P3 credit fields FIXED, credit waves, checker-verified; the license entries are part of the port as integrated).

### 2. Includes and components

- **What:** The usage exhibit's escaped include is repointed `:scpko:theme:doap-nvl` → `:scp-jp:theme:doap-nvl` as built (block B8, candidate L39) — a repoint that changed the branch prefix but kept the plain slug, so the exhibit named a page that does not exist on scp-jp; the usage-example population sweep has since completed the name on the same line to `:scp-jp:theme:doap-nvl-jp` (SWEEP-USAGE.md; canonical commit b5cb724); `component:image-block` is bare on both sides and unchanged. The tail is the structural change (block B75): the original closes with `:scpko:component:toggle-sidebar` and `:scpko:component:navla` includes (original L316–317); the candidate replaces them with the license box (section 1) and a hidden live include of the base, `[[include theme:navla-style-jp tocbox={$tocbox}|help={$help}]]` inside a display-none div (candidate L377–379). The navla component's live function arrives through the frame's priority-2 delivery (section 3) rather than a tail include. T4's finding belongs to this section: the base pages named here (theme:navla-style-jp, component:navla-jp) return 404 on scp-jp — they resolve on the draft host, where the candidates live, but are not yet posted — so the include chain collapses if this theme is posted alone.
- **Why:** P1 (KB-15) for the repoints: each names the JP counterpart that exists as a candidate. The exhibit's repoint as built satisfied the branch half of that rule only — its plain slug named no JP page — and the sweep's completion to the posting name is what brings it under the rule. The tail swap is T8 applied to a layered theme: the base is included as the JP port (ruling 4), and the component's delivery moves into the frame where the original's own frame already put its code. The T4 item is the dependency's posting state, not a wrong name in this file: the names are the correct JP counterparts, and their simultaneous posting is a posting-procedure arrangement.
- **Verify:** `grep -n '\[\[include' candidate.txt` — the frame three, the credit pair, the exhibit, image-block, the license-box pair, and the hidden base include; no `:scpko:` include survives.
- **Disposition:** DISPOSITIONED (GOSIGN2-LEDGER §(c3): P1, posting-procedure convention class) for the dependency item; the repoints themselves are applied.

### 3. Delivery and code loading

- **What:** Delivery consolidates at the head. The original loads code in two places (the head module's navla-style import, original L3; the tail module's two imports, original L319–320); the candidate loads everything at the head: its own /1 by module import from the draft host (block B2, candidate L2) and the three frame deliveries of section 0 (candidate L5–17), and the tail module is deleted with the tail swap (block B75). Inside the source exhibit, the CSS `url()` references are re-hosted to the draft host's local--files (blocks B62, B67–B70, B73: the background and logo artwork under the theme's own and the sibling DoAP theme's file folders). The exhibit itself (candidate L198–326) is the theme's own overlay layer only, under its porter banner (section 10).
- **Why:** P4/T9: own-code and base-code delivery served from JP hosts; the draft-host form of the live lines is KB-41, class (iii) — sanctioned at draft stage, rewritten to the production host at posting. Consolidating the tail module into the head frame is the JP BHL frame convention and changes no cascade order: the priorities (1 base style, 2 component, 3 own) reproduce the original's import order.
- **Verify:** `grep -n 'wdfiles\|local--code' candidate.txt` against the lines above; no scpko.wdfiles.com delivery line survives (the scpko.wdfiles.com strings that remain are license-box source records, section 7).
- **Disposition:** DISPOSITIONED (draft-host lines, class (iii)).

### 4. Fonts and assets

- **What:** No font load and no font-stack rewrite occurs in this layer: the only `font-family` value on either side is `var(--title-font)`, whose stack arrives with the navla base. Image assets are re-hosted inside the exhibit (section 3); the `--suncross` artwork is an inline SVG data URI carried byte-identical on both sides (original L195, candidate L210) — its `http://www.w3.org/2000/svg` string is the SVG namespace inside the data URI, not an external reference, and no HTTP-KEPT question arises. The license box (section 1) is the asset inventory: six image files and two CSS files, each with author, license, and source.
- **Why:** P7/T5: the load gap the class guards against is a layer whose own text has no JP face anywhere in its stack; here the stack is the base's, and no T4 font item was recorded for this theme. The data-URI point is recorded because the namespace string is exactly the shape that false-fires external-reference checks.
- **Verify:** `grep -n 'font-family' candidate.txt` returns the variable only; `grep -n 'suncross' candidate.txt` shows the data URI at L210 matching original L195.
- **Disposition:** Standing; no font or asset item recorded against this theme.

### 5. Header, sidebar, and site furniture

- **What:** The header variables are set in the exhibit's `:root` block and translated: `--header-title: "分析心理学部"` and `--header-subtitle: "思考、感情、感覚、直観"` (candidate L206–207, block B66), the Japanese forms of the ancestor's Korean strings; `--logo-image` is re-hosted to the draft host, pointing into the sibling theme:doap-bhl-jp file folder where the shared DoAP logo artwork lives (candidate L202, block B65). Sidebar furniture arrives from the base (the original's toggle-sidebar include is part of the tail swap, section 2).
- **Why:** Header text translation is P10 applied to furniture strings (the JP site shows a Japanese header); no P9 item was recorded for this theme, because the header language was translated rather than kept. The logo's folder is T9 re-hosting with the file kept in the folder that hosts it for both DoAP themes.
- **Verify:** Read candidate L200–207 against original L188–195 in diff.md.
- **Disposition:** Standing (part of the port); no header item dispositioned.

### 6. Text translation

- **What:** The body is translated throughout: 20 TRANSLATION-ANCHORED primaries (usage prose, exhibit captions, the collapsible labels) and the TRANS-UNANCHORED mass (38 label occurrences across the body and the license entries), plus the one-word translation the differ left unlabeled (appendix, B42). The license-box entries are translated in full, including the Jung 『赤の書』 provenance prose for the background patterns. Korean survives reader-visible only in the credit block's 原題 field (candidate L23). In-CSS text (R1): the exhibit's comments are the ancestor's, carried; the one added comment is the porter banner (section 10).
- **Why:** P10 (body, usage, and sample translation is the port's purpose) and KB-18 (reader-visible strings). The T4 row records this theme's translation quality among the batch's best, and the unanchored group was verified in bulk against the mirror for this README.
- **Verify:** The pairs are diff.md's six hunks in order; a Hangul scan of candidate.txt outside the exhibit returns the credit 原題 field only.
- **Disposition:** Standing (the port itself); no untranslated reader-visible text remains.

### 7. Links

- **What:** One LINK-REPOINT label (inside block B5): the ancestor's credit-region link arrangement is replaced by the preview block's source link (candidate L27), naming scpko.wikidot.com — the ancestor's recorded host in review/sources.tsv — so the mis-hosted-link defect class does not occur and no probe was needed. The license box's 出典 links deliberately keep their scpko.wdfiles.com and commons.wikimedia.org / wordpress.org URLs: they are attribution records of where the files came from, not delivery references, and rewriting them would falsify the record.
- **Why:** P11 under the dead-reference evidence standard; attribution sources are provenance data (the TASL record), which the port preserves verbatim.
- **Verify:** `grep -n 'http' candidate.txt` — the hits are the delivery lines of section 3, the credit source link, the license sources, and the data-URI namespace of section 4.
- **Disposition:** Standing; no dead or mis-hosted link found.

### 8. Structure

- **What:** The localize.md closing rule holds, with one deliberate frame change: the original closes its tag gate early (`[[/iftags]]` at original L314, before the tail furniture), while the candidate keeps the gate open across the license box and closes it at candidate L376, immediately before the hidden base include — the JP form puts the attribution furniture inside the gated theme body. Variable names, selectors, and exhibit order are preserved; the source-code exhibit sits where the original's sits, and an exhibit census (usage exhibits, image exhibits, the code exhibit) corresponds one to one. Block B75's EXHIBIT-RESTRUCTURE primary adjudicates to the tail furniture swap of section 2 — includes exchanged and the license box added — not a restructuring of carried content, so the R3 question does not arise.
- **Why:** R3 exists to force exactly this adjudication; here the census and the tail read, not the label, decide. The gate-close move is recorded because it is the one place the candidate's document skeleton differs from the ancestor's.
- **Verify:** Compare `grep -n 'iftags\|license-box\|\[\[code' original.txt candidate.txt` — the gate pair, the license pair inside it, and the single code exhibit.
- **Disposition:** Standing; no structural deletion, no class I item.

### 9. Formatting only

- **What:** Two whitespace-only blocks (B71, B72: blank-line seams inside the exhibit), the whole of this theme's formatting-only class. The classifier finds no re-indentation pair (0), so the R7 follow-up-diff hazard is not triggered.
- **Why:** Formatting churn is disclosed as its own class so it is never mistaken for a semantic change.
- **Verify:** The two blocks are named in classification.json with their line ranges (original L254–255 and L277–278).
- **Disposition:** None required.

### 10. Porter annotations

- **What:** One annotation with no original counterpart: the exhibit's banner comment, `/* ========< doap-nvl overlay (theme:doap-nvl rev 35) >======== */` (candidate L199, residue block B64), naming the layer and the reference revision it was ported from. It is the exhibit's scope statement — the code below it is the overlay only — and it is the in-file counterpart of this package's K5b-3 scope note. The license box's two base-CSS entries (section 1) carry provenance notes of the same factual kind inside attribution entries. No `[!-- --]` translator notes exist in the candidate.
- **Why:** R2: porter-added text is part of the change record; a banner that fixes the layer boundary and the reference revision is documentation the next maintainer needs.
- **Verify:** Read candidate L198–199 at the exhibit's head.
- **Disposition:** Standing.

### 11. Dispositions and exceptions

- **What:** Three items, each with its ground. (1) T1's eight pseudo-ref errors: class (ii), posting-procedure — they are the candidate's own draft-host local--code lines and the frame's delivery references (section 3); the posting procedure rewrites or re-hosts them, and fix lanes never "fix" them in the candidate. (2) The render row's items: the page runtime-hotlink site-theme chain (KB-40, environment-layer: runtime hosts arrive via the shared site theme chain, not the candidate) and the sample credit-modal item (KB-32, preview-form property: `credit:start-preview` has no modal mechanism, GOSIGN-TESTS.md T2 note) — both recorded by the lane as cross-cutting, with T3 none beyond them. (3) T4's dependency item (the base pages' 404 state on scp-jp): argued in section 2 — display-affecting at posting, dispositioned as a posting-procedure convention, because the remedy (posting the base candidates together with this theme, or arranging the dependency with staff) belongs to the posting procedure, not to any edit of this file.
- **Why:** A disposition is a decision with grounds (AGENTS.md §3 classes (i)/(ii)/(iii); the named KB entries), not an omission; environment-layer and posting-layer lines are recorded as not-charged to the candidate's bytes.
- **Verify:** Each item names its deciding record above; the T1 classes are T1-ROWS row 264's, the render items are the ledger §(c2) block for this theme (RENDER-S2-H (KO3)).
- **Disposition:** DISPOSITIONED (all three).

### 12. Verification

- **What:** (a) T1 source check (T1-ROWS row 264): exit 1, 8 errors / 1 warn / 0 infos; all eight errors are pseudo-ref, class (ii); there is no class (i) error. (b) T2/T3 render (RENDER-ROWS-2, lane RENDER-S2-H (KO3)): FINDINGS, the cross-cutting items of section 11(2) only, all dispositioned; engine coverage is the full matrix as run by the lane, not separately caveated in the row. (c) T4/T5 (LOCALIZE-ROWS row 259): FINDINGS jointly, display-affecting findings 1 (the dependency item, section 2); the ledger §(c3) line records the theme's T4 outcome as P1 DISPOSITIONED. (d) This package is self-verifying: `python3 review/build_review.py --check` regenerates diff.md and the verdict stamp from the two byte-faithful copies in this directory and compares. Counts in this README are the generator's (difflib, autojunk off): +215/−164 in 75 change blocks / 6 hunks.
- **Why:** Verification claims name the cheapest deciding check and its result, not a general assurance.
- **Verify:** Re-run the checker on `pages/theme:doap-nvl-jp.txt` and `python3 review/build_review.py --check` in this repo.
- **Disposition:** PASS (GOSIGN2-LEDGER (b) row 260; go-sign, COMPLETION-REPORT §10).

## Per-theme record

### A layered theme whose only finding lives outside its own bytes

This is the batch's cleanest port by its own records — the T4 row calls its attribution, JP variables, translation quality, and license recording the best in its batch — and its single display-affecting finding is a fact about the repository, not about the file: theme:doap-nvl-jp cannot be posted alone. Its frame and its hidden include name theme:navla-style-jp and component:navla-jp, which exist as candidates in this repo and resolve on the draft host, but return 404 on scp-jp. The posting procedure therefore has to land the three together (or arrange the dependency with staff, as the T4 row puts it). That is why the item is dispositioned rather than fixed: there is no line in this candidate that could be edited to change it, and the names it uses are the correct ones.

### The usage example's posting name

The usage example at candidate L39 as built read `> @@[[include :scp-jp:theme:doap-nvl]]@@`: the porting wave's repoint changed the branch prefix from `:scpko:` but left the plain name, so the example named a page that does not exist on scp-jp (the campaign's settled rule for usage examples, AGENTS.md §6). The usage-example population sweep has since completed the reference to `:scp-jp:theme:doap-nvl-jp` on the same line (sweep report SWEEP-USAGE.md in the campaign record, R/review-scout/; canonical commit b5cb724), one of its 287 repairs across 157 candidates. This package documents the corrected candidate; its stamp reads STALE against the pre-repair verdict, by design.

## Appendix — residue blocks

For class M the residue set is resolved in one table, not per-block slots.

| Block | Shape | Resolution |
|---|---|---|
| B42 (no signature) | Original L112–113 → candidate L126–127: the specimen word 글자 → 文字 inside a blockquote example | A one-word translation the differ left unlabeled; counted in section 6 |
| B64 (no signature) | Candidate L198–199: the code exhibit opens and gains its banner comment line | The porter banner naming the overlay and rev 35, adjudicated in section 10 |

## Change set outside the two diffed files

The diff covers two files; the port's record is larger. `pages/theme-decoration-sample-doap-nvl-jp.txt` is the decoration sample the render checks ran against (its credit-modal item is section 11(2)). The candidate layers over `pages/theme:navla-style-jp.txt` and delivers `component:navla-jp`'s code page through its frame — both are separate candidates with their own review packages, and the K5b-3 scope note in section 0 is the boundary: this package documents the doap-nvl layer and its references to the base, not the base's own port. The posting dependency recorded in section 2 is the operational consequence of that layering. There are no companion fragments and no inbound-link repairs in other candidates for this theme.

## License and attribution

- **Title:** 분석심리학부 블랙하이라이터 테마
- **Author:** Navla
- **Source:** https://scpko.wikidot.com/theme:doap-nvl — revision 35
- **License:** Creative Commons Attribution-ShareAlike 3.0 (CC BY-SA 3.0) — license deed: https://creativecommons.org/licenses/by-sa/3.0/
- **Adaptation:** This package holds a Sigma-10 migration port of the work; changes were made. See "Summary" and "Standing sections" in this README for what changed and why. Translator: AI (Muse and its delegated agents), per the campaign's standing attribution rule.
