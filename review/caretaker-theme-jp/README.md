# Review package — theme:caretaker-theme-jp

<!-- BEGIN GENERATED VERDICT STAMP — do not hand-edit; regenerate with review/build_review.py -->
## Verdict stamp
- Theme: theme:caretaker-theme-jp — origin EN, population #68 [GOSIGN2-LEDGER (b) row 68]
- Overall: PASS — passed at the ledger determination; no OPEN items [GOSIGN2-LEDGER (b) row 68]
- T1 (source check): FINDINGS (classified) — baseline 2026-11-16: exit 1, 3 errors / 1 warn / 0 infos (hotlink×2, pseudo-ref×1); standing classes dispositioned in register c1 [T1-ROWS row 73; GOSIGN2-LEDGER (b) row 68]
- T2/T3 (render, combined verdict): FINDINGS — [combined T2/T3] report `FINDINGS` (minor) — BHL min-width overflow 337–419px@≤375 on sample; no interwiki port defect; other lines cross-cutting/draft-form/by-design. [RENDER-ROWS-1 (RENDER-S2-A)]
- Engine coverage: full matrix as run by the lane; coverage not separately caveated in the row [RENDER-ROWS-1 row]
- Credit modal: no credit-modal line in this theme's row; no sample credit-modal error recorded [RENDER-ROWS-1 (RENDER-S2-A)]
- T4 (localize patterns + follow-up): FINDINGS — display-affecting findings: 3 [LOCALIZE-ROWS row 68, source LOCALIZE-S2-A]
- T5 (translation text): FINDINGS — the source reports judge T4/T5 jointly; one verdict word covers both [LOCALIZE-ROWS row 68]
- FIX5 re-judgement: none — no OPEN items at the ledger determination [GOSIGN2-LEDGER (b) row 68]
- Computed against: canonical commit 1869877ffdcd33cb214b8dc421fb39e3de8d7e8d; candidate file pages/theme:caretaker-theme-jp.txt sha256:92f205c4654721cce0f4144a5c39a02b6999c6bcba541921744c45ab6644c7d3; record: GOSIGN2-LEDGER.md + GOSIGN2-LEDGER-SUPPLEMENT.md as of the FIX5 head 435a6bb
<!-- END GENERATED VERDICT STAMP -->

## Status

| | |
|---|---|
| Verdict | **PASS** — passed at the ledger determination; this theme had no OPEN items and no §(e) register entry (GOSIGN2-LEDGER (b) row 68) |
| Standing items | **DISPOSITIONED** — T1 hotlink ×2 and pseudo-ref ×1 (class (ii), section 11); the render row's BHL min-width overflow on the sample (inherited base behavior, section 11); T4's three display-affecting items (subtitle wording, two EN-hosted assets, the EN hub link), each with its ledger disposition in section 11 |
| Go-sign basis | COMPLETION-REPORT.md §10 (go-sign issued; 81 FIXED / 26 DISPOSITIONED / 0 OPEN across the sweep) |
| Named exception | None for this theme (the sweep's single named exception is theme:amethyst-v2, which has no candidate) |

## Provenance

| | Original | Candidate |
|---|---|---|
| Page | theme:caretaker-theme | theme:caretaker-theme-jp |
| Wiki | scp-wiki.wikidot.com | SCP-JP Sigma-10 candidate (canonical repo) |
| Reference revision | 13 (first translation; the candidate's credit block records 初訳時参照リビジョン: 13) | — |
| Source of this copy | Campaign cache `gosign2-lanes/lane-oc-gs2-en5/CACHE/orig/caretaker-theme.txt`, via the mirror store (class COPY, hash-verified against review/sources.tsv) | Canonical file `pages/theme:caretaker-theme-jp.txt`, copied at worktree HEAD 1605bbd |
| Lines / bytes | 192 lines / 6,823 bytes | 214 lines / 8,067 bytes |
| SHA-256 | d0ac76a25b326caea6ff85c86353b8458634f341276e9e78a0caa49d2bb4dcd4 | 92f205c4654721cce0f4144a5c39a02b6999c6bcba541921744c45ab6644c7d3 |

Wave history: the candidate was created by the Stage 2 EN5 integration (commit 7e07438, the LOCALIZE-S2-A wave's port) and has exactly one later commit, 1869877 (FIX-CREDIT-D, the translator-attribution normalization that swept all candidates). No FIX5 commit touches this file, because the theme had no OPEN items for FIX5 to re-judge.

## Summary

A small Black Highlighter-based theme for AEED (異常存在接触部) articles, and a port whose delivery work is a host migration rather than a restructuring: the original pulls the BHL base from the upstream nu-scptheme.github.io distribution and its own CSS from its EN page's code/1; the candidate pulls the base from the JP BHL distribution (scp-jp.github.io), adds the JP BHL theme include at the head, mirrors the two base imports as interwiki-style layers at priorities 1 and 2, and serves its own layer from its own local--code on the draft host. The prose, the examples, and the exhibit are translated; the credit block replaces the bare Rate. What the port deliberately did not do is also recorded: the header subtitle stays in English, and the theme's two images stay on the EN wiki's file host — T4 flagged both, and the ledger dispositions both (ruling 2 for the header text; the deferred-asset class for the images). Measured churn is small (diff.md: +135/−115 in 45 change blocks; a GNU-diff count of the same pair gives 158 changed lines, and the difference is alignment choice, not content).

## Class summary

Auto-classification by review/classify_hunks.py (signature table 2026-11-17.1): 45 change blocks — 20 specific (44.4%), 22 heuristic (48.9%), 3 residue (6.7%), 0 skipped. Pattern citations below name the KB entry; the patterns/ tree state cited throughout is commit 9c5e9079afb01d30cb9fc4ef9d714e5591eb2ffa.

| Label | Blocks |
|---|---|
| TRANS-UNANCHORED | 24 |
| TRANSLATION-ANCHORED | 13 |
| DRAFT-HOST | 2 |
| DELIVERY-HOST | 2 |
| IFTAGS | 2 |
| SELF-DELIVERY | 2 |
| COLON-ENC | 1 |
| CREDIT-PREVIEW | 1 |
| CREDIT-PROSE | 1 |
| ESCAPED-INCLUDE | 1 |
| EXHIBIT-RESTRUCTURE | 1 |
| HEADERVAR | 1 |
| INCLUDE-REPOINT | 1 |
| TASL-FIELDS | 1 |

Adjudication for this README (every block was read against the bytes): the 24 heuristic blocks are prose translations (section 6), verified line by line; the 3 residue blocks are the example texts inside the decoration exhibits (the nested-blockquote and table examples, original L119–138 → candidate L139–156), likewise translations whose script delta defeated the anchor test, counted in section 6. The single EXHIBIT-RESTRUCTURE primary adjudicates in section 8: it is the source-code section's frame, not a content restructure. After adjudication no block is left unexplained.

## Standing sections

### 0. Header and provenance frame

- **What:** Theme theme:caretaker-theme-jp; original theme:caretaker-theme on scp-wiki at reference revision 13; candidate `pages/theme:caretaker-theme-jp.txt`. Provenance route: derived from the original at the reference revision by the LOCALIZE-S2-A wave (sources.tsv kind: standard; no production JP counterpart exists for this theme, so the R4 adoption question does not arise). The frame: the original wraps the page in a single `[[iftags +theme]]` gate (L1–188) and delivers its own layer from a tail module outside the gate (L190–192). The candidate splits the frame: an added head wrapper `[[iftags]]` (no tag list) holds the JP BHL theme include alone (candidate L1–3), the main gate is localized to `+テーマ` (candidate L5–206), and the tail delivery module stands outside it as before (candidate L208–210).
- **Why:** Section 0 declares the provenance route so every later count is read against the right baseline; the gate's tag is P2, the frame is P6/T3. The separate BHL wrapper is the campaign's frame form for BHL-based themes: the base include is present on the page without being part of the theme's own gated body.
- **Verify:** The sources.tsv row for caretaker-theme-jp; `sha256sum original.txt` against the Provenance table.
- **Disposition:** Standing (the route itself); the gate and frame changes are recorded in sections 2 and 3.

### 1. Credit and attribution

- **What:** The original's only credit furniture is a bare `[[module rate]]` (original L8–10). The candidate deletes it and installs the JP form: a `:scp-jp:credit:start-preview`/`end-preview` block (candidate L21–30) carrying the eight ruling-3 fields (title Caretaker Theme; 翻訳責任者 AI; 翻訳年 2026; 原題 Caretaker Theme; 著作権者 winkwonkboi; 作成年 2024; 初訳時参照リビジョン 13; the source link, naming scp-wiki.wikidot.com/theme:caretaker-theme, the recorded host, which serves the original). The title is the theme's proper name in English on both fields, which no record flags. T7 credit-module CSS: none added; the theme's CSS (candidate L157–201) carries no credit rules. License box: none on either side, and none added.
- **Why:** P3/T1: the preview credit module is the rate-bearing JP form, so the bare Rate is deleted rather than duplicated (KB-09). Ruling 3 fixes the eight fields.
- **Verify:** `grep -n 'module rate' candidate.txt` returns nothing; read candidate L21–30 against the eight fields.
- **Disposition:** Applied (the swap is in the bytes; the ledger's credit outcome for this theme rides on the same credit-wave record as its siblings).

### 2. Includes and components

- **What:** The candidate's includes: the added `:scp-jp:theme:black-highlighter-theme` include inside the head wrapper (candidate L2); the credit pair (section 1); two interwiki-style includes for the base layers (candidate L11–19, section 3); and the image-block component for the feesh illustration (candidate L51, repointed to the `:scp-jp:` namespace; its asset argument is section 4's item). The escaped usage example (candidate L43–44) teaches the posting form: `:scp-jp:theme:black-highlighter-theme` plus `:scp-jp:theme:caretaker-theme`. The original's only component include is the same image-block, in the bare EN namespace. Every live include in the candidate names a `:scp-jp:` target.
- **Why:** P1 (KB-15): an include must name the JP counterpart that actually exists on scp-jp. The BHL base include is added because the JP form of a BHL-based theme includes the JP base page rather than only importing its CSS (the original relies on the imports alone, which section 3 keeps as well). Ruling 4 is not engaged: no new component had to be ported for this theme.
- **Verify:** `grep -n '\[\[include' candidate.txt` — seven includes, all `:scp-jp:`.
- **Disposition:** Applied; no foreign include kept, no named exception needed.

### 3. Delivery and code loading

- **What:** Three delivery lines change host, and one frame is added. (1) The head module's base imports move from the upstream distribution to the JP distribution: `nu-scptheme.github.io/Black-Highlighter/stable/styles/normalize.min.css` and `.../black-highlighter.min.css` (original L4–5) become `scp-jp.github.io/Black-Highlighter/css/min/normalize.min.css` and `.../black-highlighter.min.css` (candidate L7–8) — host and path form both change (DELIVERY-HOST blocks). (2) The two base imports are mirrored as interwiki-style layers, normalize at priority 1 and the base at priority 2 (candidate L11–19), which the original does not have. (3) The theme's own layer: the original's tail module imports its EN page's own delivery, `https://scp-wiki.wikidot.com/theme:caretaker-theme/code/1` (original L191); the candidate's tail module imports its own `local--code/theme%3Acaretaker-theme-jp/1` from the draft host (candidate L208–210, SELF-DELIVERY), whose body is the code exhibit (candidate L157–201). No interwiki-style include names the own layer (its slot in the layering is the tail module's, after the base's 1 and 2).
- **Why:** P4/T9: delivery is served from JP hosts — the JP BHL distribution for the base, the theme's own code for its layer — never from the original's page or the upstream distribution. P6/T3 supplies the interwiki-style supplement frame and its priority order (1 normalize, 2 base). The draft-host form of the own delivery is KB-41, class (iii): sanctioned at draft stage, rewritten to the production host at posting.
- **Verify:** `grep -n '@import' candidate.txt` — L7, L8 (JP distribution), L209 (own draft-host delivery); no nu-scptheme or scp-wiki code URL remains.
- **Disposition:** DISPOSITIONED (draft-host line, class (iii)).

### 4. Fonts and assets

- **What:** Fonts: none of either kind was changed — the theme names no font stack of its own (its CSS sets variables and layout only), so there is no P7 supplement and no JPFONT signature; the check is the grep below. Assets: the theme's two images stay on the EN wiki's file host, colon-encoded and otherwise untouched — the feesh illustration in the image-block (candidate L51, `scp-wiki.wikidot.com/local--files/theme%3Acaretaker-theme/feesh.png`) and the header logo in the exhibit's `--logo-image` (candidate L169, `.../AEEDLogoWhite.png`). These are T4's Pattern 5 items for this theme and T1's two hotlink errors. The port re-hosted nothing; the ledger dispositions the pair in the deferred-asset class (section 11).
- **Why:** P5 (assets served from JP hosts) is the class the disposition answers: KB-58 records the campaign's standing treatment for original-wiki file hosts (deferred re-host, class (ii)); the images serve today from the EN host, and no JP-hosted copy exists to point at.
- **Verify:** `grep -n 'local--files' candidate.txt` — exactly the two lines above, both scp-wiki.
- **Disposition:** DISPOSITIONED (P5, class (ii) / KB-58).

### 5. Header, sidebar, and site furniture

- **What:** The header-variable block travels with the exhibit CSS nearly untouched (the HEADERVAR block): the gradient colors and link colors are identical, and the one change inside it is the logo URL's colon encoding (section 4). The header subtitle is the recorded exception: `--header-subtitle: "Anomalous Entity Engagement Division"` stands in English at candidate L170, exactly as in the original (L152). T4's row 68 marks this Pattern 9 display-affecting and notes the subtitle should match the page's own translated usage (the prose at candidate L36 names the division 異常存在接触部（AEED)); the ledger dispositions it under ruling 2 (section 11). No sidebar or topbar rule was adapted; the theme does not restyle them beyond the base.
- **Why:** P9's JP-header expectation is what T4 measured; ruling 2 (header text language is translation taste) is the ground the ledger dispositioned it on — recorded here because the subtitle is always displayed, so a reviewer will see English in the header of a JP page.
- **Verify:** `grep -n -- '--header-subtitle' candidate.txt` — L170, English.
- **Disposition:** DISPOSITIONED (P9, ruling 2, GOSIGN2-LEDGER §(c3) line for this theme).

### 6. Text translation

- **What:** The prose is translated throughout (the 24 TRANS-UNANCHORED heuristic primaries and 13 TRANSLATION-ANCHORED blocks, verified line by line): the intro, the usage section (including the note about including the base, whose EN absolute link became the bare posting-form link `[[[theme:black-highlighter-theme|こちら]]]` at candidate L47), the examples, the collapsible labels, and the exhibit-internal example texts — the blockquote and table jokes whose script delta made them the 3 residue blocks (original L119–138 → candidate L139–156). English survives only as quotation: the credit fields (candidate L22, L25, L29), the subtitle (section 5), and the code exhibit's CSS, which is code, not prose.
- **Why:** P10 (body and usage translation is the port's purpose) and KB-18 (reader-visible strings).
- **Verify:** The pairs are diff.md's body sections in order; the residue pairs are the blockquote/table lines cited above.
- **Disposition:** Standing (the port itself).

### 7. Links

- **What:** One prose link names a foreign page deliberately: the AEED hub link in the intro (candidate L36) still names the EN hub (`scp-wiki.wikidot.com/anomalous-entity-engagement-division-hub`), with the port's gloss （AEED、英語版） added so a JP reader knows the target is the English hub — T4's Pattern 11 item for this theme, dispositioned in the sibling / batch-posting class (section 11). The remaining links are sound: the credit source link (candidate L29, recorded host, serves); the base-theme link (candidate L47, bare posting form, section 6). The host check the jiha exemplar taught (candidate host vs recorded host, probe on divergence) finds no unintended divergence: the only scp-wiki links are the recorded source link and the dispositioned hub link.
- **Why:** P11: prose links take the JP counterpart or the serving original, under the dead-reference evidence standard. No JP hub page for the division exists to repoint to, so the serving original stands, glossed.
- **Verify:** `grep -n 'scp-wiki' candidate.txt` — L29 (source), L36 (hub), and the two asset lines of section 4.
- **Disposition:** DISPOSITIONED (P11, sibling / batch-posting class).

### 8. Structure

- **What:** The skeleton corresponds one-to-one: gate, head module, credit position, prose, examples, source-code exhibit in its collapsible, tail delivery. The classifier's one EXHIBIT-RESTRUCTURE primary adjudicates as a false fire of the recorded kind: the source-code section's frame changed around an unchanged exhibit — the collapsible's labels were translated and the section heading localized (+ Source Code → + ソースコード), while the `[[code type="css"]]` body (candidate L157–201 against original L139–183) corresponds rule for rule, its only internal changes being the colon-encoded logo URL (section 4). Exhibit census: one exhibit on each side (the theme's own CSS), no exhibit added, dropped, split, or merged. The frame change of substance is section 0's: the added head wrapper holding the base include.
- **Why:** R3 requires the census before a restructure is narrated; here the census shows correspondence, so the section records correspondence.
- **Verify:** `grep -n '\[\[code' original.txt candidate.txt` — one exhibit each; read the bodies against each other.
- **Disposition:** Standing (correspondence established).

### 9. Formatting only

- **What:** None. The classifier finds no whitespace-only block and no re-indentation (0 and 0), so the R7 follow-up-diff hazard is not triggered.
- **Why:** Formatting churn is disclosed as its own class so it is never mistaken for a semantic change.
- **Verify:** The classifier's section-9 counts in classification.json.
- **Disposition:** None required.

### 10. Porter annotations

- **What:** None. The candidate contains no `[!-- ... --]` comments, no 訳注 footnotes, and no provenance banner; the port's one judgment a reader might want announced (the English subtitle, section 5) is not announced in the page — its record is the T4 row, the ledger line, and this package.
- **Why:** R2: porter-added text is part of the change record; its absence is stated, not assumed.
- **Verify:** `grep -n '訳注\|\[!--' candidate.txt` returns nothing.
- **Disposition:** Standing (as an absence, stated).

### 11. Dispositions and exceptions

- **What:** Three items, each with its ground. (1) T1's three errors: hotlink ×2 — the two EN-hosted images of section 4, class (ii) (KB-58); pseudo-ref ×1 — the candidate's own draft-host local--code line (section 3), class (ii). There is no class (i) error; the 1 warn is recorded verbatim in T1-ROWS row 73 and is not classified. (2) The render row's one theme-adjacent item: a BHL min-width overflow of 337–419px at ≤375 viewports on the sample page — inherited Black Highlighter base behavior (the row's own text: "no interwiki port defect; other lines cross-cutting/draft-form/by-design"), recorded so a reviewer measuring the sample at phone widths is not surprised; it is a property of the base the theme sits on, not of this port. No credit-modal line exists in this theme's render row. (3) T4's three display-affecting items and their ledger dispositions (§(c3) line for this theme): the English subtitle — P9 DISPOSITIONED (ruling 2); the two EN-hosted assets — P5 DISPOSITIONED (class (ii) / KB-58); the EN hub link — P11 DISPOSITIONED (sibling / batch-posting class). The theme's determination is PASS and this package does not re-open it.
- **Why:** A disposition is a decision with grounds (AGENTS.md §3 classes (i)/(ii)/(iii); the named KB entries), not an omission; inherited-base and environment lines are recorded as not-charged.
- **Verify:** Each item names its deciding record above.
- **Disposition:** DISPOSITIONED (all three).

### 12. Verification

- **What:** (a) T1 source check (T1-ROWS row 73): exit 1, 3 errors / 1 warn / 0 infos; the errors are hotlink ×2 and pseudo-ref ×1, all class (ii); there is no class (i) error. (b) T2/T3 render (RENDER-ROWS-1, lane RENDER-S2-A): FINDINGS (minor) — the BHL min-width overflow on the sample (section 11(2)); engine coverage full matrix as run by the lane. (c) T4/T5 (LOCALIZE-ROWS row 68): FINDINGS jointly, display-affecting findings 3; the ledger §(c3) line records the theme's P5/P9/P11 outcomes as DISPOSITIONED. (d) This package is self-verifying: `python3 review/build_review.py --check` regenerates diff.md and the verdict stamp from the two byte-faithful copies in this directory and compares. Counts in this README are the generator's (difflib, autojunk off): +135/−115 in 45 change blocks; the GNU-diff count of the same pair is 158 changed lines, and the difference is alignment choice, not content.
- **Why:** Verification claims name the cheapest deciding check and its result, not a general assurance.
- **Verify:** Re-run the checker on `pages/theme:caretaker-theme-jp.txt` and `python3 review/build_review.py --check` in this repo.
- **Disposition:** PASS (GOSIGN2-LEDGER (b) row 68; go-sign, COMPLETION-REPORT §10).

## Per-theme record

None. This theme's record is complete in the standing sections: its wave history is two commits, it has no §(e) entry, no FIX wave touched it, and its three dispositioned items are stated with their grounds in section 11.

## Change set outside the two diffed files

The diff covers two files; the port's record is one file larger. `pages/theme-decoration-sample-caretaker-theme-jp.txt` is the decoration sample the render checks ran against (its overflow reading is section 11(2)); it belongs to this theme's record but carries no port change of its own to explain here. The original-side sample `pages/theme-decoration-sample-caretaker-theme.txt` is the campaign's mirror-side fixture, likewise outside the port. There are no companion fragments, no shared base file, and no inbound-link repairs in other candidates for this theme.
