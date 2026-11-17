# Review package — theme:derby-jp (EN → JP port)

<!-- BEGIN GENERATED VERDICT STAMP — do not hand-edit; regenerate with review/build_review.py -->
## Verdict stamp
- Theme: theme:derby-jp — origin EN, population #79 [GOSIGN2-LEDGER (b) row 79]
- Overall: PASS — passed at the ledger determination; no OPEN items [GOSIGN2-LEDGER (b) row 79]
- T1 (source check): FINDINGS (classified) — baseline 2026-11-16: exit 1, 14 errors / 1 warn / 1 info (pseudo-ref×14); standing classes dispositioned in register c1 [T1-ROWS row 79; GOSIGN2-LEDGER (b) row 79]
- T2/T3 (render, combined verdict): FINDINGS — [combined T2/T3] report `FINDINGS` — broken image: `sigma-header-logo.svg` renders as broken on all 8 shots (URL 200 but `content-type: text/plain` — MIME, not 404/stale); `.open-menu` overlaps content at ≤375 both pages, WebKit CC "S", swatch-table overflow. [RENDER-ROWS-1 (RENDER-S2-B)]
- Engine coverage: full matrix as run by the lane; coverage not separately caveated in the row [RENDER-ROWS-1 row]
- Credit modal: no credit-modal line in this theme's row; no sample credit-modal error recorded [RENDER-ROWS-1 (RENDER-S2-B)]
- T4 (localize patterns + follow-up): FINDINGS — display-affecting findings: 4 [LOCALIZE-ROWS row 79, source LOCALIZE-S2-A]
- T5 (translation text): FINDINGS — the source reports judge T4/T5 jointly; one verdict word covers both [LOCALIZE-ROWS row 79]
- FIX5 re-judgement: none — no OPEN items at the ledger determination [GOSIGN2-LEDGER (b) row 79]
- Computed against: canonical commit 666f54356acb463c56016c967dc52464b25ba4a2; candidate file pages/theme:derby-jp.txt sha256:87c77fa717461574a4212e9a78248f58e74f15b0f04c7a451fa28fd9d1590518; record: GOSIGN2-LEDGER.md + GOSIGN2-LEDGER-SUPPLEMENT.md as of the FIX5 head 435a6bb
<!-- END GENERATED VERDICT STAMP -->

## Status

| | |
|---|---|
| Verdict | **PASS** — passed at the ledger determination; this theme had no OPEN items and no §(e) register entry (GOSIGN2-LEDGER (b) row 79) |
| Standing items | **DISPOSITIONED** — T1 pseudo-ref ×14 (class (ii), section 11); the render row's items (posting-procedure MIME; KB-36; KB-33/KB-34 family, section 11); T4's P1, P9, P10 (section 11). The credit fields the localize lane found missing were **FIXED** by the credit waves. Two defects in the *original's* CSS were fixed by the port and are recorded in the per-theme record for report-back to the EN author |
| Go-sign basis | COMPLETION-REPORT.md §10 (go-sign issued; 81 FIXED / 26 DISPOSITIONED / 0 OPEN across the sweep) |
| Named exception | None for this theme (the sweep's single named exception is theme:amethyst-v2, which has no candidate) |

## Provenance

| | Original | Candidate |
|---|---|---|
| Page | theme:derby | theme:derby-jp |
| Wiki | scp-wiki.wikidot.com | SCP-JP Sigma-10 candidate (canonical repo) |
| Reference revision | 17 (first translation; the candidate's credit block records 初訳時参照リビジョン: 17) | — |
| Source of this copy | Mirror store, class COPY (hash-verified against review/sources.tsv) | Canonical file `pages/theme:derby-jp.txt`, copied at worktree HEAD 1605bbd |
| Lines / bytes | 957 lines / 25,147 bytes | 965 lines / 26,241 bytes |
| SHA-256 | f7c42f5f6b28adb7756fa8b4f1e99950afd5d60ddcfae12626161561e2b36902 | 87c77fa717461574a4212e9a78248f58e74f15b0f04c7a451fa28fd9d1590518 |

Wave history: the candidate was created by the Stage 2 EN7 integration (commit 331ab7e) and last touched by FIX2-CREDIT (commit 666f543, the credit-missing-fields completions over 36 themes). No FIX5 commit touches this file, because the theme had no OPEN items for FIX5 to re-judge.

## Summary

A BHL-based racing theme whose port is the full standard treatment: the base delivery and fonts move to the JP distribution and Google Fonts, the credit block is installed with the eight ruling-3 fields plus a font-credit field, the license furniture is kept but repointed to the JP backend, the sigma-plus include takes its `-jp` component form, and nineteen asset references move to the draft host. Two items distinguish this package. First, the port fixes two malformed `var()` references in the original's own CSS (per-theme record) — upstream defects, recorded exactly so they can be reported to the EN author. Second, the header strings stay English by design: `--header-title: "Horse Girls"` and `--header-subtitle: "DARLING DERBY"` are byte-identical to the original, under the campaign's ruling that header language is translation taste, not a migration defect. The install example (candidate L24) already names `theme:derby-jp`, so the batch's usage-example defect does not apply. Measured churn (diff.md: +68/−60, 128 changed lines in 40 change blocks / 12 diff sections).

## Class summary

Auto-classification by review/classify_hunks.py (signature table 2026-11-17.1): 40 change blocks — 32 specific (80.0%), 7 heuristic (17.5%), 1 residue (2.5%), 0 skipped. Pattern citations below name the KB entry; the patterns/ tree state cited throughout is commit 9c5e9079afb01d30cb9fc4ef9d714e5591eb2ffa.

| Label | Blocks |
|---|---|
| DRAFT-HOST | 19 |
| TRANSLATION-ANCHORED | 6 |
| TRANS-UNANCHORED | 5 |
| EXHIBIT-RESTRUCTURE | 5 |
| INCLUDE-REPOINT | 4 |
| CSS-BODY | 3 |
| COMPONENT-SWAP | 2 |
| LICENSE-BOX | 2 |
| DELIVERY-HOST | 2 |
| SELF-DELIVERY | 2 |
| IFTAGS | 1 |
| CREDIT-PREVIEW | 1 |
| CREDIT-PROSE | 1 |
| TASL-FIELDS | 1 |
| FONT-IMPORT | 1 |
| JPFONT-LOAD | 1 |
| WS-ONLY | 1 |
| SIGMA-PLUS-JP | 1 |

Adjudication for this README (every block was read against the bytes): the five EXHIBIT-RESTRUCTURE labels are the standing false-fire shape — include repoints and host moves inside exhibit regions (the license pair and the sigma-plus include sit in the page's tail exhibits); the exhibit census of section 8 shows no restructuring. The three CSS-BODY heuristic blocks are adjudicated individually: B15 is a P7 font-stack rewrite (the `--oswa` stack gains its JP face, section 4), and B16/B21 are the original-defect fixes of the per-theme record. The one residue block (B40) is the file's tail furniture, adjudicated in the appendix. After adjudication no block is left unexplained.

## Standing sections

### 0. Header and provenance frame

- **What:** Theme theme:derby-jp; original theme:derby on scp-wiki at reference revision 17; candidate `pages/theme:derby-jp.txt`. Provenance route: derived from the original at the reference revision (sources.tsv kind: standard; no production JP counterpart, so the R4 adoption question does not arise). The candidate's head carries the standard frame pair (delivery module plus interwiki-style include) over the BHL base, where the original delivered through the EN distribution.
- **Why:** Section 0 declares the provenance route so every later count is read against the right baseline.
- **Verify:** The sources.tsv row for derby-jp; `sha256sum original.txt` against the Provenance table.
- **Disposition:** Standing (the route itself).

### 1. Credit and attribution

- **What:** The candidate installs the preview credit block at candidate L3–13 with bare includes, carrying the eight ruling-3 fields — title Derby Theme; 翻訳責任者 AI; 翻訳年 2026; 原題 Derby Theme; 著作権者 Fish^12; 作成年 2026; 初訳時参照リビジョン 17; the source link (candidate L11) naming scp-wiki.wikidot.com, the original's recorded host — plus a ninth, theme-specific field: 追加フォント (Noto Sans JP, Zen Kaku Gothic New; SIL OFL 1.1, Google Fonts), the credit for the JP faces the port loads (section 4). The localize lane found the fields missing (LOCALIZE-ROWS row 79); FIX2-CREDIT completed them, and the ledger records P3 as FIXED. No T7 credit-module CSS supplement exists in this theme.
- **Why:** P3/T1 and ruling 3; the font-credit field is P7's credit half (a loaded JP face is credited where it is loaded).
- **Verify:** Read candidate L3–13 against the fields above.
- **Disposition:** FIXED (GOSIGN2-LEDGER §(c3): P3 FIXED).

### 2. Includes and components

- **What:** Four repoints and two component swaps. The license furniture is kept and repointed: `license-box-theme` becomes `:scp-jp:component:license-box-backend` (candidate L914, B30) and `license-box-end` takes its `:scp-jp:` form (candidate L952, B36) — the AGENTS.md §5 standing form, where per-theme license repoints recorded in the ledger stand as they are. The sigma-plus include becomes `component:sigma-plus-jp` (candidate L956, B37, SIGMA-PLUS-JP) — the T8 base-component port this theme depends on. The remaining INCLUDE-REPOINT blocks are the frame pair and the credit pair. The install example (candidate L24) names `theme:derby-jp` in its correct posting form.
- **Why:** P1 (KB-15) for the repoints; T8/KB-64 for the sigma-plus base: a dependent theme imports the base's JP port, never the raw upstream delivery.
- **Verify:** `grep -n '\[\[include' candidate.txt` — no `:scp-wiki:` include remains.
- **Disposition:** Applied; P1 DISPOSITIONED at the ledger (section 11).

### 3. Delivery and code loading

- **What:** The theme layers over Black Highlighter. The base delivery lines move from the EN distribution to the JP one (DELIVERY-HOST ×2, SELF-DELIVERY ×2): the candidate's frame imports its own code from the draft host and names the JP BHL distribution for the base, in the same shape the campaign's BHL ports use (the old-bhl end state: the base is served from scp-jp.github.io, not from the EN CDN). The theme's own CSS stays inline in its module on both sides.
- **Why:** P4/T9 (delivery served from JP hosts) and P6/T3 (the frame). The draft-host form of the own-code lines is KB-41, class (iii).
- **Verify:** `grep -n 'wdfiles\|github.io' candidate.txt` — the delivery lines are the draft host and the JP distribution only.
- **Disposition:** DISPOSITIONED (class (iii) for the draft-host lines).

### 4. Fonts and assets

- **What:** Fonts (P7): the original loads Oswald from fonts.bunny.net; the candidate loads Oswald plus Zen Kaku Gothic New from Google Fonts (candidate L65, FONT-IMPORT/JPFONT-LOAD), and a second import carries Open Sans plus Noto Sans JP (candidate L66). The `--oswa` stack gains its JP face: `"Oswald"` → `"Oswald", "Zen Kaku Gothic New"` (B15 — the classifier's CSS-BODY heuristic, adjudicated here as the P7 font-stack rewrite it is). The localize lane recorded the bunny→Google Fonts move as correct (「フォント移行は良好」, LOCALIZE-ROWS row 79). Assets: nineteen DRAFT-HOST blocks move the theme's images from their original hosts (including smlt.wdfiles.com, the lane-noted re-host) to the draft host's `local--files/theme%3Aderby-jp/` folder, file names unchanged.
- **Why:** P7/T5: Latin display faces stay, a JP face is added to each stack that can render Japanese, and the load moves to Google Fonts (AGENTS.md §5: fonts.bunny.net imports are rewritten to Google Fonts). P5/KB-17 for the assets.
- **Verify:** `grep -n '@import' candidate.txt` — candidate L65–66 are Google Fonts; `grep -n 'bunny' candidate.txt` returns nothing.
- **Disposition:** Applied (fonts); DISPOSITIONED (assets, class (ii)/(iii) posting-procedure family).

### 5. Header, sidebar, and site furniture

- **What:** The header variables are carried byte-identical: `--header-title: "Horse Girls"` and `--header-subtitle: "DARLING DERBY"` (original L75–76 → candidate L83–84). The localize lane charged the English header as P9 (display-affecting, LOCALIZE-ROWS row 79); the campaign's ruling 2 settles header language as case-by-case translation taste, outside Sigma-10 migration correctness, and the ledger dispositions P9 on that ground. No layout adaptation (P8) was needed.
- **Why:** P9's charge and ruling 2's settlement are both recorded so the kept English reads as a decision, not an oversight.
- **Verify:** `grep -n -- '--header-' original.txt candidate.txt` — the two lines, identical.
- **Disposition:** DISPOSITIONED (ruling 2; GOSIGN2-LEDGER §(c3)).

### 6. Text translation

- **What:** The prose body and exhibits are translated throughout (TRANSLATION-ANCHORED ×6, TRANS-UNANCHORED ×5, CREDIT-PROSE ×1). One deliberate keep: the prose link to the EN sigma-plus page is kept as a link to the original and labelled （英語版） (candidate L19, B4) — the reader is told the target is the English page, which is the P11 serving-original form with its label. The localize lane's P10 charge (English headings and Trainer strings standing in the exhibits) is dispositioned at lane severity: the exhibits demonstrate the theme's English display strings, and the ledger records P10 as DISPOSITIONED (lane severity/specimen).
- **Why:** P10 for the body; P11 for the labelled keep; the specimen ground for exhibit strings.
- **Verify:** A CJK scan of candidate.txt outside the credit block's 原題 field and the section-5 header values returns only translated text and labelled specimens.
- **Disposition:** Standing (the port itself); P10 DISPOSITIONED (section 11).

### 7. Links

- **What:** The credit source link (candidate L11) names scp-wiki.wikidot.com, the original's recorded host — the host check passes. The sigma-plus prose link of section 6 is the only other outbound link of note, kept and labelled. No hub link needed a repoint: the theme's prose names no EN hub page as a navigation target.
- **Why:** P11: prose links take the JP counterpart or the serving original, labelled when kept.
- **Verify:** `grep -n 'wikidot.com' candidate.txt` — the source link and the labelled sigma-plus link.
- **Disposition:** Standing; no dead link.

### 8. Structure

- **What:** The closing rule holds: selectors, rule order, and variable names inside the CSS are preserved, with two exceptions that are corrections, not restructures — the malformed `var()` references of the per-theme record. Exhibit census (R3): the original's exhibits (usage, swatch tables, license block, sigma-plus tail) all survive in the candidate in the same order; the five EXHIBIT-RESTRUCTURE labels sit on blocks whose exhibit-region lines are the section-2 repoints and section-4 host moves, and are discharged on that ground.
- **Why:** R3 forces the census because a restructure and a deletion share a diff shape.
- **Verify:** Compare the exhibit sequence in original.txt against candidate.txt; `grep -n 'var(-- white)\|var(-brown)' candidate.txt` returns nothing (per-theme record).
- **Disposition:** Standing; no structural deletion, no class I item.

### 9. Formatting only

- **What:** One WS-ONLY block (a whitespace-only line pair, inside the CSS body) and no re-indentation (0). Nothing else in the diff is formatting churn.
- **Why:** Formatting churn is disclosed as its own class so it is never mistaken for a semantic change (R7).
- **Verify:** The summary counts in classification.json (`reindent_blocks: 0`).
- **Disposition:** None required.

### 10. Porter annotations

- **What:** None — the candidate carries no `[!-- ... --]` translator notes and no editor line (checked explicitly). The credit block's 追加フォント field (section 1) is credit furniture, not an annotation. The two CSS corrections of the per-theme record are silent in the file itself, which is why this package records them in full.
- **Why:** R2: porter-added text is part of the change record; its absence is recorded so a reviewer does not have to wonder whether it was checked.
- **Verify:** `grep -n '\[!--' candidate.txt` returns nothing.
- **Disposition:** Standing (checked, absent).

### 11. Dispositions and exceptions

- **What:** Four items, each with its ground. (1) T1's fourteen pseudo-ref errors: class (ii), posting-procedure — the draft-host delivery and asset lines of sections 3–4. (2) The render row's items: the broken image on all eight shots (sigma-header-logo.svg) is a posting-procedure MIME item, not a candidate defect — the URL returns 200 with content-type text/plain, so the file serves but does not render as an image until the posting procedure serves it with an image type; the .open-menu overlap at ≤375px and the WebKit CC-"S" item are KB-36 (the mobile-menu family); the swatch-table overflow is the KB-33/KB-34 cross-cutting family. (3) T4's P1: DISPOSITIONED — its substance was a staff consult on the sigma-plus base dependency and the license-box backend's existence, both settled by the section-2 forms (the `-jp` component exists as the campaign's own port; the backend include is the §5 standing form). (4) P9 and P10: DISPOSITIONED (ruling 2; lane severity/specimen), sections 5–6.
- **Why:** A disposition is a decision with grounds (AGENTS.md §3 classes (i)/(ii)/(iii); the named KB entries), not an omission.
- **Verify:** Each item names its deciding record above and in the verdict stamp.
- **Disposition:** DISPOSITIONED (items 1–4); P3 FIXED (section 1).

### 12. Verification

- **What:** (a) T1 source check (T1-ROWS row 79): exit 1, 14 errors / 1 warn / 1 info; all fourteen errors are pseudo-ref, class (ii); there is no class (i) error. (b) T2/T3 render (RENDER-ROWS-2, lane RENDER-S2-B (EN7)): FINDINGS, the items of section 11(2), all dispositioned; engine coverage full matrix as run by the lane. (c) T4/T5 (LOCALIZE-ROWS row 79): FINDINGS jointly, display-affecting findings 4 — of which the credit-fields item was FIXED afterwards (section 1) and the rest are section 11's dispositions; the lane recorded the license re-host and the font migration as correct. (d) This package is self-verifying: `python3 review/build_review.py --check` regenerates diff.md and the verdict stamp from the two byte-faithful copies in this directory and compares. Counts in this README are the generator's (difflib, autojunk off): +68/−60 in 40 change blocks / 12 diff sections.
- **Why:** Verification claims name the cheapest deciding check and its result, not a general assurance.
- **Verify:** Re-run the checker on `pages/theme:derby-jp.txt` and `python3 review/build_review.py --check` in this repo.
- **Disposition:** PASS (GOSIGN2-LEDGER (b) row 79; go-sign, COMPLETION-REPORT §10).

## Per-theme record

### Two malformed var() references in the original, fixed by the port

The original's CSS contains two broken variable references, each of which silently voids its declaration in a browser:

1. Original: `--sp_dropdown-link-hover-color: var(-- white);` — a space inside the variable name. Candidate L103 reads `var(--white)`.
2. Original: `color: var(-brown);` — a single dash. Candidate L324 reads `var(--brown)`.

Both are the KB-03 shape (malformed CSS carried in the original). The port corrects them rather than reproducing them, which is the campaign's standing rule for EN technical mistakes: fix them in the JP port and record the exact details so they can be reported to the EN author (theme:derby, by Fish^12). Neither fix changes any other line; both are verifiable by the grep in section 8. The ledger's PASS for this theme stands with these corrections in place — they repair the original, they do not diverge from its intent.

## Appendix — residue blocks adjudicated

| Block | Original → candidate | Adjudication |
|---|---|---|
| B40 | tail lines | The file's closing furniture (the sigma-plus include region's tail): the include itself is B37 (section 2); the residue lines are its surrounding blanks and closers, carried over |

## Change set outside the two diffed files

The diff covers two files; the port's record is two files larger. `pages/theme-decoration-sample-derby-jp.txt` is the decoration sample the render checks ran against (its findings are the sample half of section 11(2)); it belongs to this theme's record but carries no port change of its own to explain here. The theme's base dependency, `component:sigma-plus-jp`, is a campaign component with its own record, not part of this change set. There are no companion fragments and no inbound-link repairs in other candidates for this theme.
