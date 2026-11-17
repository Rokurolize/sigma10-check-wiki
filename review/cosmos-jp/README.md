# Review package — theme:cosmos-jp (EN → JP port)

<!-- BEGIN GENERATED VERDICT STAMP — do not hand-edit; regenerate with review/build_review.py -->
## Verdict stamp
- Theme: theme:cosmos-jp — origin EN, population #73 [GOSIGN2-LEDGER (b) row 73]
- Overall: STALE — candidate file changed since the verdict was computed (verdict against 435a6bb-era content, file sha256 now 2106ae24be9190a10ff3df0776b93d89f96e82f33a3df099232a5465821fe750); verdict not carried over, re-judgement required
> verdicts below describe the pre-change file
- T1 (source check): FINDINGS (classified) — baseline 2026-11-16: exit 1, 6 errors / 1 warn / 2 infos (pseudo-ref×6); standing classes dispositioned in register c1 [T1-ROWS row 63; GOSIGN2-LEDGER (b) row 73]
- T2/T3 (render, combined verdict): FINDINGS — [combined T2/T3] report `FINDINGS` — candidate-inherent page-overflow at 320/375 + `credit-modal-overflow` at 320 (both engines). [RENDER-ROWS-1 (RENDER-S2-A)]
- Engine coverage: full matrix as run by the lane; coverage not separately caveated in the row [RENDER-ROWS-1 row]
- Credit modal: no credit-modal line in this theme's row; no sample credit-modal error recorded [RENDER-ROWS-1 (RENDER-S2-A)]
- T4 (localize patterns + follow-up): FINDINGS — display-affecting findings: 1 [LOCALIZE-ROWS row 73, source LOCALIZE-S2-A]
- T5 (translation text): FINDINGS — the source reports judge T4/T5 jointly; one verdict word covers both [LOCALIZE-ROWS row 73]
- FIX5 re-judgement: none — no OPEN items at the ledger determination [GOSIGN2-LEDGER (b) row 73]
- Computed against: canonical commit 358955eb4013dac2399c414ba8ec2a6e416a3c11; candidate file pages/theme:cosmos-jp.txt sha256:2106ae24be9190a10ff3df0776b93d89f96e82f33a3df099232a5465821fe750; record: GOSIGN2-LEDGER.md + GOSIGN2-LEDGER-SUPPLEMENT.md as of the FIX5 head 435a6bb
<!-- END GENERATED VERDICT STAMP -->

## Status

| | |
|---|---|
| Verdict | **PASS** — passed at the ledger determination; this theme had no OPEN items and no §(e) register entry (GOSIGN2-LEDGER (b) row 73) |
| Standing items | **DISPOSITIONED** — T1 pseudo-ref ×6 (class (ii), section 11); the render row's items (KB-32/KB-33 family, section 11); T4's charges under the class outcomes (ruling 2; asset hosts class (ii), section 11). The credit fields the localize lane found missing were **FIXED**, and the live duplicate Rate was **FIXED** (FIX3-S2EN §3); its escaped exhibit is a named keep (AGENTS.md §6.9). One defect is flagged in the per-theme record: the usage example names a page that does not exist on scp-jp |
| Go-sign basis | COMPLETION-REPORT.md §10 (go-sign issued; 81 FIXED / 26 DISPOSITIONED / 0 OPEN across the sweep) |
| Named exception | None for this theme (the sweep's single named exception is theme:amethyst-v2, which has no candidate) |

## Provenance

| | Original | Candidate |
|---|---|---|
| Page | theme:cosmos | theme:cosmos-jp |
| Wiki | scp-wiki.wikidot.com | SCP-JP Sigma-10 candidate (canonical repo) |
| Reference revision | 30 (first translation; the candidate's credit block records 初訳時参照リビジョン: 30) | — |
| Source of this copy | Mirror store, class COPY (hash-verified against review/sources.tsv) | Canonical file `pages/theme:cosmos-jp.txt`, copied at worktree HEAD 1605bbd |
| Lines / bytes | 465 lines / 60,344 bytes | 488 lines / 62,599 bytes |
| SHA-256 | e10f87b2cad14eff028e79d73cca93e676f93a8846e65af06c054fc25d3495ca | c1464931f7d7f601164f965d7b1a2b614aa51417bfef4545c5d9efd1b17ad549 |

Scope note (sources.tsv kind K5b-3): cosmos is a layer over the space theme. This package's diff covers cosmos's own layer only; the base layer is theme:space's own port, a separate package. Wave history: the candidate was created by the Stage 2 EN6 integration (commit 240c3d2), adjusted by commit 0937f45 ("keep the shared static credit in flow"), and last touched by FIX2-CREDIT (commit 666f543). The duplicate-Rate removal was FIX3-S2EN §3, which the ledger (c1) note names for this theme and cleaning-services-jp. No FIX5 commit touches this file, because the theme had no OPEN items for FIX5 to re-judge.

## Summary

An aesthetic layer theme whose port is the standard treatment applied to a thin layer: the frame and delivery are repointed to the JP side, the credit block is installed in preview form with the eight ruling-3 fields, the license furniture is kept and repointed to the JP backend, and the exhibit-heavy prose is translated (62 translation blocks, the batch's highest count after dark-dealings). Three recorded subtleties: the live duplicate Rate the localize lane found was removed by FIX3-S2EN, while an escaped `@@[[module rate]]@@` exhibit line (candidate L182) is deliberately kept as the labelled exhibit of the rate form (the AGENTS.md §6.9 named keep, the same shape as classic-jp's labelled pair in this batch); the body-font line in the font exhibit changes from DM Sans to M PLUS 1p with a translator footnote explaining why (section 10) — a text-level change in this layer, which declares no font stacks of its own; and the base theme's usage example (candidate L59) is correct while cosmos's own (candidate L60) is the per-theme record's flagged defect. Measured churn (diff.md: +159/−143, 302 changed lines in 71 change blocks / 4 diff sections).

## Class summary

Auto-classification by review/classify_hunks.py (signature table 2026-11-17.1): 71 change blocks — 32 specific (45.1%), 39 heuristic (54.9%), 0 residue, 0 skipped. Pattern citations below name the KB entry; the patterns/ tree state cited throughout is commit 9c5e9079afb01d30cb9fc4ef9d714e5591eb2ffa.

| Label | Blocks |
|---|---|
| TRANS-UNANCHORED | 42 |
| TRANSLATION-ANCHORED | 20 |
| EXHIBIT-RESTRUCTURE | 5 |
| DRAFT-HOST | 4 |
| INCLUDE-REPOINT | 4 |
| DELIVERY-HOST | 3 |
| IFTAGS | 2 |
| CREDIT-PREVIEW | 2 |
| LICENSE-BOX | 2 |
| SELF-DELIVERY | 1 |
| CREDIT-PROSE | 1 |
| TASL-FIELDS | 1 |
| ESCAPED-INCLUDE | 1 |
| ASSET-REHOST | 1 |

Adjudication for this README (every block was read against the bytes): the heuristic majority is the one-line exhibit translation mass, the expected class M shape for this page. The five EXHIBIT-RESTRUCTURE labels are the standing false-fire shape (repoints inside exhibit regions); the census of section 8 decides. There is no residue. After adjudication no block is left unexplained.

## Standing sections

### 0. Header and provenance frame

- **What:** Theme theme:cosmos-jp; original theme:cosmos on scp-wiki at reference revision 30; candidate `pages/theme:cosmos-jp.txt`. Provenance route: derived from the original at the reference revision, as a layer over the space base (kind K5b-3, the Scope note above; no production JP counterpart for the cosmos layer itself, so the R4 adoption question does not arise for this layer).
- **Why:** Section 0 declares the provenance route and the layering so every later count is read against the right baseline: this package judges the cosmos layer, not the composed page.
- **Verify:** The sources.tsv row for cosmos-jp; `sha256sum original.txt` against the Provenance table.
- **Disposition:** Standing (the route itself).

### 1. Credit and attribution

- **What:** The candidate installs the preview credit block at candidate L36–45 with `:scp-jp:`-prefixed includes, carrying the eight ruling-3 fields (title Cosmos Theme; 翻訳責任者 AI; 翻訳年 2026; 原題 Cosmos Theme; 著作権者 HaydenSaintPascal; the source link naming scp-wiki.wikidot.com, the original's recorded host). The Rate state needs its two halves stated separately: the LIVE duplicate `[[module rate]]` the localize lane found (its L42 at reading time) was removed by FIX3-S2EN §3 — no live Rate stands in the candidate — and the escaped exhibit line `@@[[module rate]]@@` (candidate L182) is kept deliberately as the labelled exhibit of the rate form, the AGENTS.md §6.9 named keep. Historical note: the localize lane (LOCALIZE-ROWS row 73) found six credit fields missing; FIX2-CREDIT completed them, and the ledger records the credit item as FIXED. No T7 credit-module CSS supplement exists in this layer.
- **Why:** P3/T1 and ruling 3; KB-09 for the live duplicate, with the §6.9 distinction between a live duplicate (a defect) and a labelled escaped exhibit (documentation).
- **Verify:** `grep -n 'module rate\|module Rate' candidate.txt` — only the escaped exhibit at L182; read candidate L36–45 against the eight fields.
- **Disposition:** FIXED (credit fields, FIX2-CREDIT; live duplicate, FIX3-S2EN §3); the escaped exhibit is a named keep.

### 2. Includes and components

- **What:** The frame pair and credit pair are sections 3 and 1. The license pair is section 8's furniture (LICENSE-BOX ×2): `license-box-backend` repointed to `:scp-jp:` with its author parameter kept (candidate L462), `license-box-end` likewise (candidate L487). The image-block include is repointed to `:scp-jp:` (candidate L64) with its image served from the JP storage host (section 4). The two escaped usage examples (ESCAPED-INCLUDE): candidate L59 names `:scp-jp:theme:space` for the base — correct, the production JP page exists (probed for this package, 2026-11-17: 200) — and candidate L60 named `:scp-jp:theme:cosmos` as built, the per-theme record's flagged defect, since repaired by the population sweep (it now names `:scp-jp:theme:cosmos-jp`).
- **Why:** P1 (KB-15) for the live includes; the usage examples under the campaign's settled rule (AGENTS.md §6).
- **Verify:** `grep -n '\[\[include' candidate.txt` — the frame, the credit pair, the license pair, the image-block line, the two escaped examples.
- **Disposition:** Live includes applied; the self-example is flagged in the per-theme record (not edited here; the coordinator lands repairs).

### 3. Delivery and code loading

- **What:** A layered delivery: the candidate's frame imports the base layer's JP delivery and its own code from the JP side (DELIVERY-HOST ×3, SELF-DELIVERY ×1, DRAFT-HOST ×4 across the layer's asset lines). The cosmos layer's own CSS is inline in its module on both sides; what moves is the chain of hosts the composed page loads from — EN hosts out, JP distribution and draft host in — in the same shape as the batch's other BHL-family ports.
- **Why:** P4/T9 and P6/T3. The draft-host form is KB-41, class (iii): sanctioned at draft stage, rewritten to the production host at posting.
- **Verify:** `grep -n 'wdfiles\|github.io' candidate.txt` — JP-side hosts only.
- **Disposition:** DISPOSITIONED (class (ii)/(iii) family).

### 4. Fonts and assets

- **What:** Fonts: this layer declares no `font-family` and no font variables on either side (checked; the composed page's stacks live in the space base layer, outside this package). What the port changes is the font exhibit's descriptive text: the original's "Body font is DM Sans." becomes 「本文フォントはM PLUS 1p。」 with a translator footnote (candidate L207, section 10), while the header face (Urbanist) and mono face (Martian Mono) lines are translated unchanged. The substitution the footnote records is therefore a claim about the composed page whose deciding stack sits in the base layer's package, not this one; this package records the text change and its footnote, and does not adjudicate the base layer. Assets: the layer's background image is re-hosted to the draft host (`--space-body-bg` naming cosmos-body-bg.jpg, candidate L228), and the logo image in the image-block exhibit is served from the JP storage host (candidate L64, ASSET-REHOST).
- **Why:** P7's stack half does not engage in a layer with no stacks; the exhibit text is P10 translation with a recorded substitution (section 10's annotation). P5/KB-17 for the assets.
- **Verify:** `grep -n 'font-family' original.txt candidate.txt` — no hits on either side; read candidate L205–209 against original L182–186.
- **Disposition:** Standing (text change recorded); assets DISPOSITIONED (class (ii)/(iii) family).

### 5. Header, sidebar, and site furniture

- **What:** The header strings of the layer are carried with their English proper nouns standing (the localize lane's P9 note: the subtitle's English proper nouns, LOCALIZE-ROWS row 73); ruling 2 settles header language as translation taste, and the ledger dispositions the charge on that ground. The layer's sidebar and furniture rules are carried inside its CSS with only the section-3/4 host lines changed. No P8 layout adaptation was needed.
- **Why:** P9's charge and ruling 2's settlement are both recorded so the kept English reads as a decision, not an oversight.
- **Verify:** Compare the header-variable lines in original.txt and candidate.txt.
- **Disposition:** DISPOSITIONED (ruling 2; GOSIGN2-LEDGER §(c3) class outcome).

### 6. Text translation

- **What:** The prose and exhibits are translated throughout (TRANSLATION-ANCHORED ×20, TRANS-UNANCHORED ×42, CREDIT-PROSE ×1) — the font specimens, the exhibit tables, and the usage prose. The prose credits both authors with their roles (candidate L56: HaydenSaintPascal as this layer's author, EstrellaYoshte as the space base's), and the sigma-plus/toggle-sidebar component mentions are translated around their bare component links (candidate L62). One substitution inside the translation is the font exhibit's body-font line (section 4), which carries the translator footnote of section 10.
- **Why:** P10 (body and usage translation); KB-18 for reader-visible strings.
- **Verify:** A CJK scan of candidate.txt outside the credit block's 原題 field and the section-5 header values returns only translated text.
- **Disposition:** Standing (the port itself).

### 7. Links

- **What:** The credit source link names scp-wiki.wikidot.com, the original's recorded host — the host check passes. The prose link to the base theme (`[[[theme:space|...]]]`, candidate L56) targets the production JP page for the base, which exists (the same page the usage example names). The component mentions (candidate L62) are bare component links to the campaign's own component pages. No dead link stands.
- **Why:** P11: prose links take the JP counterpart or the serving original.
- **Verify:** `grep -n 'wikidot.com\|\[\[\[theme' candidate.txt` — the source link and the base link above.
- **Disposition:** Standing; no dead link.

### 8. Structure

- **What:** The closing rule holds inside the layer's CSS: selectors, rule order, and variable names are preserved; the changes are the host lines of sections 3–4. Exhibit census (R3): the original's exhibits (usage, font specimens, image specimen, license block) all survive in the candidate in the same order; the five EXHIBIT-RESTRUCTURE labels sit on repoint blocks inside exhibit regions and are discharged on that ground. The license box's file list names `space-body-bg.png` (candidate L483) — the base layer's background file, inherited from the original's license text; the localize lane noted the name as stale against the candidate's own cosmos-body-bg.jpg (candidate L228). The name stands as the lane recorded it, inside a license text that covers the composed work; the ledger's determination is PASS and this package does not re-open it.
- **Why:** R3 forces the census; the license filename is recorded because a reviewer comparing file names across the package will trip on it.
- **Verify:** Compare the exhibit sequence in original.txt against candidate.txt; `grep -n 'body-bg' candidate.txt` — L228 and L483.
- **Disposition:** Standing; no structural deletion, no class I item.

### 9. Formatting only

- **What:** None — the classifier finds no whitespace-only block pair and no re-indentation (0 and 0).
- **Why:** Formatting churn is disclosed as its own class so it is never mistaken for a semantic change.
- **Verify:** The summary counts in classification.json (`reindent_blocks: 0`).
- **Disposition:** None required.

### 10. Porter annotations

- **What:** One, riding inside the font exhibit: the translator footnote at candidate L207 — 「訳注: 原語版ではDM Sansですが、日本語非対応のため変更しています。」 ("Translator note: the original uses DM Sans, which does not support Japanese, so it has been changed") — attached to the body-font line of section 4. It is the porter's own explanation of the substitution, written for the reader of the candidate page, and it is the only porter-added text in the file (no `[!-- ... --]` notes, no editor line).
- **Why:** R2: porter-added text is part of the change record. A 訳注 footnote is the JP theme pages' standing form for exactly this situation (a substitution the reader would otherwise trip on), and recording it here keeps the change set honest: the body-font line is a substitution with a stated reason, not a silent edit.
- **Verify:** `grep -n '訳注' candidate.txt` — candidate L207 only.
- **Disposition:** Standing (recorded; the annotation is part of the candidate as it stands).

### 11. Dispositions and exceptions

- **What:** Three items, each with its ground. (1) T1's six pseudo-ref errors: class (ii), posting-procedure — the draft-host lines of sections 3–4. (2) The render row's items, both candidate-inherent shapes of the preview form rather than defects: the page overflow at 320/375px and the credit-modal overflow at 320px on both engines, dispositioned as the preview form's fixed-width modal shape (KB-32/KB-33 family; KB-31 charges modal overflow only on real-module pages, and this page's rate form is the preview module). (3) T4's charges under the ledger's class outcomes for this theme: header language under ruling 2 (section 5), asset hosts class (ii) (section 4), credit fields FIXED (section 1). Separately, the usage example of section 2 is flagged below as a defect the ledger did not record.
- **Why:** A disposition is a decision with grounds (AGENTS.md §3 classes (i)/(ii)/(iii); the named KB entries), not an omission.
- **Verify:** Each item names its deciding record above and in the verdict stamp.
- **Disposition:** DISPOSITIONED (items 1–3); the usage example is flagged with evidence in the per-theme record.

### 12. Verification

- **What:** (a) T1 source check (T1-ROWS row 63): exit 1, 6 errors / 1 warn / 2 info; all six errors are pseudo-ref, class (ii); there is no class (i) error. (b) T2/T3 render (RENDER-ROWS-2, lane RENDER-S2-A (EN6)): FINDINGS, the items of section 11(2), all dispositioned; engine coverage both engines as run by the lane. (c) T4/T5 (LOCALIZE-ROWS row 73): FINDINGS jointly, display-affecting findings 1 (the credit-fields item, since FIXED); the lane's remaining notes (duplicate Rate, subtitle, license filename) are sections 1, 5, and 8. (d) This package is self-verifying: `python3 review/build_review.py --check` regenerates diff.md and the verdict stamp from the two byte-faithful copies in this directory and compares. Counts in this README are the generator's (difflib, autojunk off): +159/−143 in 71 change blocks / 4 diff sections.
- **Why:** Verification claims name the cheapest deciding check and its result, not a general assurance.
- **Verify:** Re-run the checker on `pages/theme:cosmos-jp.txt` and `python3 review/build_review.py --check` in this repo.
- **Disposition:** PASS (GOSIGN2-LEDGER (b) row 73; go-sign, COMPLETION-REPORT §10).

## Per-theme record

### The usage example names a page that does not exist (defect flag, repaired)

Candidate L60, the second of the two stacked install examples, reads `{{@@[[include :scp-jp:theme:cosmos]]@@}}`. Probe made for this package (2026-11-17): `https://scp-jp.wikidot.com/theme:cosmos` returns 404; the candidate posts to scp-jp under its own name, theme:cosmos-jp, so the example as written cannot be followed. The example directly above it (candidate L59) is correct: it names `:scp-jp:theme:space` for the base layer, and that production page returns 200 — the pair shows the porter applying the production name where the base keeps its name, and the original's slug where the port renames. The campaign's settled rule (AGENTS.md §6) names this exact shape a finding: usage examples inside candidate docs naming `theme:<slug>` instead of `theme:<slug>-jp` break every copy-paste install. The localize lane did not record it, and the ledger's determination for this theme is PASS; this package carries the item as a flagged defect with its probe evidence, for the coordinator's repair wave. The candidate is documented as it stands; no byte of it was edited here. The repair has since landed: the usage-example population sweep (sweep report SWEEP-USAGE.md in the campaign record, R/review-scout/; canonical commit b5cb724), which repaired this shape across all 157 affected candidates; candidate L60 now reads `{{@@[[include :scp-jp:theme:cosmos-jp]]@@}}`, and this package documents the corrected candidate (its stamp reads STALE against the pre-repair verdict, by design).

## Change set outside the two diffed files

The diff covers two files; the port's record is larger in two directions. `pages/theme-decoration-sample-cosmos-jp.txt` is the decoration sample the render checks ran against (its findings are the sample half of section 11(2)). And the composed page depends on the base layer's port (theme:space-jp, with its production counterpart theme:space), which has its own package; nothing in this theme's record edits it. There are no companion fragments and no inbound-link repairs in other candidates for this theme.
