# Review package — theme:cleaning-services-jp (EN → JP port)

<!-- BEGIN GENERATED VERDICT STAMP — do not hand-edit; regenerate with review/build_review.py -->
## Verdict stamp
- Theme: theme:cleaning-services-jp — origin EN, population #71 [GOSIGN2-LEDGER (b) row 71]
- Overall: STALE — candidate file changed since the verdict was computed (verdict against 435a6bb-era content, file sha256 now bb23a404f9ca205b5a818377c7261a167d9bd0c7ba9ba8f0c43f51e01e101312); verdict not carried over, re-judgement required
> verdicts below describe the pre-change file
- T1 (source check): FINDINGS (classified) — baseline 2026-11-16: exit 1, 4 errors / 2 warns / 2 infos (pseudo-ref×4); standing classes dispositioned in register c1 [T1-ROWS row 61; GOSIGN2-LEDGER (b) row 71]
- T2/T3 (render, combined verdict): FINDINGS — [combined T2/T3] report `FINDINGS` (minor) — BHL min-width overflow 337–419px@≤375 on sample; 503/http.cat lines are transient capture, not a defect. [RENDER-ROWS-1 (RENDER-S2-A)]
- Engine coverage: full matrix as run by the lane; coverage not separately caveated in the row [RENDER-ROWS-1 row]
- Credit modal: no credit-modal line in this theme's row; no sample credit-modal error recorded [RENDER-ROWS-1 (RENDER-S2-A)]
- T4 (localize patterns + follow-up): FINDINGS — display-affecting findings: 1 [LOCALIZE-ROWS row 71, source LOCALIZE-S2-A]
- T5 (translation text): FINDINGS — the source reports judge T4/T5 jointly; one verdict word covers both [LOCALIZE-ROWS row 71]
- FIX5 re-judgement: none — no OPEN items at the ledger determination [GOSIGN2-LEDGER (b) row 71]
- Computed against: canonical commit b5cb7241f527a44933e45599b41df210690771c4; candidate file pages/theme:cleaning-services-jp.txt sha256:bb23a404f9ca205b5a818377c7261a167d9bd0c7ba9ba8f0c43f51e01e101312; record: GOSIGN2-LEDGER.md + GOSIGN2-LEDGER-SUPPLEMENT.md as of the FIX5 head 435a6bb
<!-- END GENERATED VERDICT STAMP -->

## Status

| | |
|---|---|
| Verdict | **PASS** — passed at the ledger determination; this theme had no OPEN items and no §(e) register entry (GOSIGN2-LEDGER (b) row 71) |
| Standing items | **DISPOSITIONED** — T1 pseudo-ref ×4 (class (ii), section 11); the render row's items (KB-33/KB-34; KB-44, section 11); T4's charges under the class outcomes (ruling 2; asset hosts class (ii), section 11). The credit fields the localize lane found missing were **FIXED**, and the duplicate Rate it found was **FIXED** (FIX3-S2EN §3). One defect is flagged in the per-theme record: the usage example names a page that does not exist on scp-jp |
| Go-sign basis | COMPLETION-REPORT.md §10 (go-sign issued; 81 FIXED / 26 DISPOSITIONED / 0 OPEN across the sweep) |
| Named exception | None for this theme (the sweep's single named exception is theme:amethyst-v2, which has no candidate) |

## Provenance

| | Original | Candidate |
|---|---|---|
| Page | theme:cleaning-services | theme:cleaning-services-jp |
| Wiki | scp-wiki.wikidot.com | SCP-JP Sigma-10 candidate (canonical repo) |
| Reference revision | 10 (first translation; the candidate's credit block records 初訳時参照リビジョン: 10) | — |
| Source of this copy | Mirror store, class COPY (hash-verified against review/sources.tsv) | Canonical file `pages/theme:cleaning-services-jp.txt`, copied at worktree HEAD 1605bbd |
| Lines / bytes | 466 lines / 11,209 bytes | 474 lines / 12,639 bytes |
| SHA-256 | c1800e5a9bc0a0df8d956bf2ef6df3878c19dc53b9db2a3bb8d69b6108b9d240 | 5e79417cf31f28243aa81d99846feca68acba3ffec154c6568c6aa021a6cf117 |

Wave history: the candidate was created by the Stage 2 EN6 integration (commit 240c3d2) and last touched by FIX2-CREDIT (commit 666f543, the credit-missing-fields completions over 36 themes); the duplicate-Rate removal was FIX3-S2EN §3, which the ledger (c1) note names for this theme and cosmos-jp. No FIX5 commit touches this file, because the theme had no OPEN items for FIX5 to re-judge.

## Summary

A Black Highlighter theme whose port moves the whole delivery chain to the JP side: the base CSS imports leave the EN CDN for the JP BHL distribution on scp-jp.github.io, the interwiki frame's theme URLs follow, the fonts leave bunny.net for Google Fonts with the Noto Sans JP load the original declared but never imported, and the tail self-delivery closes the file. The credit block is installed in preview form with the eight ruling-3 fields, and the live `[[module rate]]` the original carried beside it is deleted (the FIX3-S2EN duplicate-Rate removal). The prose is exhibit-heavy — some thirty one-line specimen translations, including the same anomaly sentence repeated thirteen times — and two lane-noted items stand in the bytes as recorded: the header strings stay English by design, and the image exhibit's joke caption is replaced by a neutral specimen label. One item was flagged for repair in the per-theme record and has since been repaired by the population sweep: the self-referential usage example at candidate L38 named `:scp-jp:theme:cleaning-services`, a page that does not exist (probe evidence there), and now names `:scp-jp:theme:cleaning-services-jp`; its companion example for the base theme (candidate L37) is correct. Measured churn (diff.md: +155/−149, 304 changed lines in 67 change blocks / 10 diff sections).

## Class summary

Auto-classification by review/classify_hunks.py (signature table 2026-11-17.1): 67 change blocks — 33 specific (49.3%), 32 heuristic (47.8%), 2 residue (3.0%), 0 skipped. Pattern citations below name the KB entry; the patterns/ tree state cited throughout is commit 9c5e9079afb01d30cb9fc4ef9d714e5591eb2ffa.

| Label | Blocks |
|---|---|
| TRANS-UNANCHORED | 32 |
| TRANSLATION-ANCHORED | 22 |
| DRAFT-HOST | 4 |
| EXHIBIT-RESTRUCTURE | 3 |
| INCLUDE-REPOINT | 3 |
| DELIVERY-HOST | 3 |
| IFTAGS | 1 |
| CSS-BODY | 1 |
| CREDIT-PREVIEW | 1 |
| CREDIT-PROSE | 1 |
| TASL-FIELDS | 1 |
| ESCAPED-INCLUDE | 1 |
| FONT-IMPORT | 1 |
| JPFONT-LOAD | 1 |
| SELF-DELIVERY | 1 |

Adjudication for this README (every block was read against the bytes): the heuristic share is the one-line exhibit translation mass of section 6, the expected class M shape for an exhibit-heavy page. The single CSS-BODY block (B2) is adjudicated in section 3: it is the base-delivery host move, a delivery change the classifier has no signature for. The three EXHIBIT-RESTRUCTURE labels are the standing false-fire shape (repoints inside exhibit regions); the census of section 8 decides. The two residue blocks are adjudicated in the appendix: both are heading translations adjacent to furniture changes. After adjudication no block is left unexplained.

## Standing sections

### 0. Header and provenance frame

- **What:** Theme theme:cleaning-services-jp; original theme:cleaning-services on scp-wiki at reference revision 10; candidate `pages/theme:cleaning-services-jp.txt`. Provenance route: derived from the original at the reference revision (sources.tsv kind: standard; no production JP counterpart, so the R4 adoption question does not arise). The candidate carries the interwiki-style frame twice (candidate L8 and L13, the theme's two frame slots), where the original's frame named the EN theme URLs.
- **Why:** Section 0 declares the provenance route so every later count is read against the right baseline.
- **Verify:** The sources.tsv row for cleaning-services-jp; `sha256sum original.txt` against the Provenance table.
- **Disposition:** Standing (the route itself).

### 1. Credit and attribution

- **What:** The candidate installs the preview credit block at candidate L18–27 with `:scp-jp:`-prefixed includes, carrying the eight ruling-3 fields: title Cleaning Services Theme; 翻訳責任者 AI; 翻訳年 2026; 原題 Cleaning Services Theme; 著作権者 winkwonkboi; 作成年 2024; 初訳時参照リビジョン 10; the source link (candidate L26) naming scp-wiki.wikidot.com, the original's recorded host. The original's live `[[module rate]]` (original L19) is deleted: with the preview block rate-bearing, a kept Rate is the KB-09 duplicate; the ledger (c1) note records this theme's duplicate-Rate removal under FIX3-S2EN §3. Historical note, prose against bytes: the localize lane (LOCALIZE-ROWS row 71) found six credit fields missing and the duplicate Rate standing; both were the pre-fix state, closed by FIX2-CREDIT and FIX3-S2EN respectively, and the ledger's (c3) outcome records the credit fields as FIXED. No T7 credit-module CSS supplement exists in this theme.
- **Why:** P3/T1 and ruling 3; KB-09 for the duplicate-Rate failure the deletion prevents.
- **Verify:** `grep -n 'module rate\|module Rate' candidate.txt` returns nothing; read candidate L18–27 against the eight fields.
- **Disposition:** FIXED (credit fields, FIX2-CREDIT; duplicate Rate, FIX3-S2EN §3).

### 2. Includes and components

- **What:** The frame pair and credit pair are section 3's and section 1's. The image-block include inside the exhibits is repointed (`:scp-jp:component:image-block`, candidate L61, B15) with its image re-hosted in the same line (section 4). The two escaped usage examples (B11, ESCAPED-INCLUDE) are repointed to `:scp-jp:`: candidate L37 names `theme:black-highlighter-theme`, the production JP page for the base (probed for this package, 2026-11-17: scp-jp.wikidot.com/theme:black-highlighter-theme returns 200 — correct), and candidate L38 named `:scp-jp:theme:cleaning-services` as built — the original's slug, not this candidate's posting name, and the per-theme record's flagged defect, since repaired by the population sweep (the line now names `:scp-jp:theme:cleaning-services-jp`).
- **Why:** P1 (KB-15) for the live includes; the usage examples are governed by the campaign's settled rule that a copy-paste install example must name the page a user can actually include (AGENTS.md §6).
- **Verify:** `grep -n '\[\[include' candidate.txt` — the frame pair, the credit pair, the image-block line, and the two escaped examples.
- **Disposition:** Live includes applied; the self-example is flagged in the per-theme record (not edited here; the coordinator lands repairs).

### 3. Delivery and code loading

- **What:** The base-delivery move (B2, the classifier's CSS-BODY block, adjudicated here): the original imports Black Highlighter from `cdn.scpwiki.com/theme/en/black-highlighter/...`; the candidate imports `normalize.min.css` and `black-highlighter.min.css` from `scp-jp.github.io/Black-Highlighter/css/min/` (candidate L4–5) — the sanctioned JP distribution, the old-bhl class (ii) end state. The frame's theme URLs follow the same move: `nu-scptheme.github.io` → `scp-jp.github.io` in both interwiki-style includes (B4/B6, candidate L8/L13). The file closes with the tail self-delivery, an @import of the page's own /1 from the draft host (candidate L473, B67, SELF-DELIVERY).
- **Why:** P4/T9 (delivery served from JP hosts) and P6/T3 (the frame). The draft-host form of the tail line is KB-41, class (iii).
- **Verify:** `grep -n 'scpwiki.com\|nu-scptheme' candidate.txt` returns nothing; `grep -n 'scp-jp.github.io' candidate.txt` returns the delivery and frame lines.
- **Disposition:** DISPOSITIONED (base distribution, class (ii) end state; tail line, class (iii)).

### 4. Fonts and assets

- **What:** Fonts (P7): the original loads Oswald and Roboto Mono from fonts.bunny.net; the candidate loads both from Google Fonts (candidate L260–261, FONT-IMPORT) and adds the Noto Sans JP load (candidate L262, JPFONT-LOAD). The stacks themselves are unchanged — `--header-font: 'Oswald'`, `--title-font: 'Roboto Mono'`, `--body-font: 'Noto Sans JP'` are identical on both sides (original L278–280, candidate L286–288) — because the original already declared Noto Sans JP as its body font without ever importing it; the port completes the load the declaration always needed (the T5 load-completion shape). Assets: the exhibit image 173canon.jpg moves from the EN wdfiles host to the draft host (candidate L61), and the remaining DRAFT-HOST blocks move the theme's CSS asset URLs the same way, file names unchanged.
- **Why:** P7/T5 for the fonts (AGENTS.md §5: bunny.net imports are rewritten to Google Fonts); P5/KB-17 for the assets, in the class (iii) draft-host form.
- **Verify:** `grep -n '@import' candidate.txt` — candidate L260–262 are Google Fonts; `grep -n 'bunny' candidate.txt` returns nothing.
- **Disposition:** Applied (fonts); DISPOSITIONED (assets, class (ii)/(iii) family).

### 5. Header, sidebar, and site furniture

- **What:** The header variables are carried unchanged: `--logo-image: unset`, `--header-title: "SAFE CLEANUP PROFESSIONALS"`, `--header-subtitle: "Sanitize, Cleanse, Polish"` (candidate L293–295, identical to the original). The localize lane itself recorded the subtitle as design-intended English (LOCALIZE-ROWS row 71), and ruling 2 settles header language as translation taste outside migration correctness; the ledger dispositions the theme's header charge on that ground. No P8 layout adaptation was needed.
- **Why:** P9's charge and ruling 2's settlement are both recorded so the kept English reads as a decision, not an oversight.
- **Verify:** `grep -n -- '--header-\|--logo' original.txt candidate.txt` — the three lines, identical.
- **Disposition:** DISPOSITIONED (ruling 2; GOSIGN2-LEDGER §(c3) class outcome).

### 6. Text translation

- **What:** The prose and exhibits are translated throughout: 22 TRANSLATION-ANCHORED and 32 TRANS-UNANCHORED blocks, most of them one-line exhibit specimens — the anomaly-description sentence ("The sculpture is the only canon anomaly.") alone recurs thirteen times across the exhibit tables (B25–B38's region), each instance translated. One recorded exception inside the exhibits: the image-block specimen's caption. The original's caption is a profane joke ("Holy fucking bingle"); the candidate's exhibit line sets `caption=画像。` (candidate L61) — a neutral specimen label in place of the joke. The localize lane recorded this as the caption being flattened to 画像。 (LOCALIZE-ROWS row 71); it stands in the bytes as a deliberate caption neutralization of a specimen, not a translation of it, and this package records it as such rather than presenting it as translated text.
- **Why:** P10 for the body; the caption is recorded separately because a replaced specimen label is neither a translation nor an oversight.
- **Verify:** Spot-read candidate L240–258 (the font specimens, translated) against original L232–250; the caption at candidate L61 against original L53.
- **Disposition:** Standing (the port itself); the caption item stands as the lane recorded it.

### 7. Links

- **What:** The credit source link (candidate L26) names scp-wiki.wikidot.com, the original's recorded host — the host check passes. One practice difference worth recording: the link-styling exhibit keeps its target on the original page (the `[[[theme:cleaning-services|...]]]` specimen, label translated, target unchanged), where the dark-jp port in this same batch repointed its corresponding exhibit to the JP page. The kept target resolves (the EN page exists) and the exhibit demonstrates styling, not navigation, so this is recorded as an inconsistency of practice between ports, not a defect; no hub or tag link in this theme needed a repoint.
- **Why:** P11: prose links take the JP counterpart or the serving original; a styling specimen on a resolving target satisfies the rule either way, and the difference is noted for the patterns record.
- **Verify:** `grep -n 'theme:cleaning-services' candidate.txt` — the exhibit target and the section-2 usage example are different lines with different dispositions.
- **Disposition:** Standing; no dead link.

### 8. Structure

- **What:** The closing rule holds: selectors, rule order, and variable names inside the CSS are preserved; the changes inside the CSS body are the section-3 delivery lines, the section-4 asset lines, and the font imports. Exhibit census (R3): the original's exhibits (usage, font specimens, anomaly tables, image specimen) all survive in the candidate in the same order and count; the three EXHIBIT-RESTRUCTURE labels sit on blocks whose exhibit-region lines are include repoints and host moves, and are discharged on that ground. The only deletion is the furniture of section 1 (the duplicate Rate).
- **Why:** R3 forces the census because a restructure and a deletion share a diff shape.
- **Verify:** Compare the exhibit sequence in original.txt against candidate.txt; `grep -c 'canon anomaly\|唯一の正典' candidate.txt` for the repeated specimen.
- **Disposition:** Standing; no structural deletion beyond the recorded furniture fix, no class I item.

### 9. Formatting only

- **What:** None — the classifier finds no whitespace-only block pair and no re-indentation (0 and 0).
- **Why:** Formatting churn is disclosed as its own class so it is never mistaken for a semantic change.
- **Verify:** The summary counts in classification.json (`reindent_blocks: 0`).
- **Disposition:** None required.

### 10. Porter annotations

- **What:** None — the candidate carries no `[!-- ... --]` translator notes and no editor line (checked explicitly). The caption replacement of section 6 is exhibit content, not an annotation.
- **Why:** R2: porter-added text is part of the change record; its absence is recorded so a reviewer does not have to wonder whether it was checked.
- **Verify:** `grep -n '\[!--' candidate.txt` returns nothing.
- **Disposition:** Standing (checked, absent).

### 11. Dispositions and exceptions

- **What:** Three items, each with its ground. (1) T1's four pseudo-ref errors: class (ii), posting-procedure — the draft-host lines of sections 3–4. (2) The render row's items, both sample-side or transient, not charged to the candidate: the sample's BHL min-width overflow (337–419px of content at ≤375px viewports, KB-33/KB-34 cross-cutting families) and the 503/http.cat transient (KB-44, a capture-layer failure that does not reproduce as a page property). (3) T4's charges, dispositioned under the ledger's class outcomes for this theme: header language under ruling 2 (section 5), asset hosts class (ii) (section 4), credit fields FIXED (section 1). Separately, the usage example of section 2 is flagged below as a defect the ledger did not record.
- **Why:** A disposition is a decision with grounds (AGENTS.md §3 classes (i)/(ii)/(iii); the named KB entries), not an omission; transient capture failures are recorded as not-charged.
- **Verify:** Each item names its deciding record above and in the verdict stamp.
- **Disposition:** DISPOSITIONED (items 1–3); the usage example is flagged with evidence in the per-theme record.

### 12. Verification

- **What:** (a) T1 source check (T1-ROWS row 61): exit 1, 4 errors / 2 warns / 2 info; all four errors are pseudo-ref, class (ii); there is no class (i) error. (b) T2/T3 render (RENDER-ROWS-2, lane RENDER-S2-A (EN6)): FINDINGS, the items of section 11(2), all dispositioned; engine coverage full matrix as run by the lane. (c) T4/T5 (LOCALIZE-ROWS row 71): FINDINGS jointly, display-affecting findings 1 (the credit-fields item, since FIXED); the lane's remaining notes (duplicate Rate, header, caption) are sections 1, 5, and 6. (d) This package is self-verifying: `python3 review/build_review.py --check` regenerates diff.md and the verdict stamp from the two byte-faithful copies in this directory and compares. Counts in this README are the generator's (difflib, autojunk off): +155/−149 in 67 change blocks / 10 diff sections.
- **Why:** Verification claims name the cheapest deciding check and its result, not a general assurance.
- **Verify:** Re-run the checker on `pages/theme:cleaning-services-jp.txt` and `python3 review/build_review.py --check` in this repo.
- **Disposition:** PASS (GOSIGN2-LEDGER (b) row 71; go-sign, COMPLETION-REPORT §10).

## Per-theme record

### The usage example names a page that does not exist (defect flag, repaired)

Candidate L38, inside the escaped install examples, reads `@@[[include :scp-jp:theme:cleaning-services]]@@`. Probe made for this package (2026-11-17): `https://scp-jp.wikidot.com/theme:cleaning-services` returns 404; the candidate posts to scp-jp under its own name, theme:cleaning-services-jp, so the example as written cannot be followed on the site it instructs for. The companion example on the line above (candidate L37, the base theme) is correct: `theme:black-highlighter-theme` returns 200 on scp-jp, because the base's JP page keeps the base's name. The campaign's settled rule (AGENTS.md §6) names this exact shape a finding: usage examples inside candidate docs naming `theme:<slug>` instead of `theme:<slug>-jp` break every copy-paste install. The localize lane did not record it, and the ledger's determination for this theme is PASS; this package carries the item as a flagged defect with its probe evidence, for the coordinator's repair wave. The candidate is documented as it stands; no byte of it was edited here. The repair has since landed: the usage-example population sweep (sweep report SWEEP-USAGE.md in the campaign record, R/review-scout/; canonical commit b5cb724), which repaired this shape across all 157 affected candidates; candidate L38 now reads `@@[[include :scp-jp:theme:cleaning-services-jp]]@@`, and this package documents the corrected candidate (its stamp reads STALE against the pre-repair verdict, by design).

## Appendix — residue blocks adjudicated

| Block | Original → candidate | Adjudication |
|---|---|---|
| B8 | L21–22 → L28 | The heading translation (+ What's This? → + これは何？) with the blank-line adjustment left by the section-1 Rate deletion |
| B16 | L54–55 → L62–63 | The heading translation (+ Examples → + 例) following the image-block line of section 2 |

## Change set outside the two diffed files

The diff covers two files; the port's record is two files larger. `pages/theme-decoration-sample-cleaning-services-jp.txt` is the decoration sample the render checks ran against (its findings are the sample half of section 11(2)); it belongs to this theme's record but carries no port change of its own to explain here. There are no companion fragments, no shared base file, and no inbound-link repairs in other candidates for this theme.

## License and attribution

- **Title:** Cleaning Services Theme
- **Author:** winkwonkboi
- **Source:** https://scp-wiki.wikidot.com/theme:cleaning-services — revision 10
- **License:** Creative Commons Attribution-ShareAlike 3.0 (CC BY-SA 3.0) — license deed: https://creativecommons.org/licenses/by-sa/3.0/
- **Adaptation:** This package holds a Sigma-10 migration port of the work; changes were made. See "Summary" and "Standing sections" in this README for what changed and why. Translator: AI (Muse and its delegated agents), per the campaign's standing attribution rule.
