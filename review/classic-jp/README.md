# Review package — theme:classic-jp (EN → JP port)

<!-- BEGIN GENERATED VERDICT STAMP — do not hand-edit; regenerate with review/build_review.py -->
## Verdict stamp
- Theme: theme:classic-jp — origin EN, population #7 [GOSIGN2-LEDGER (b) row 7]
- Overall: STALE — candidate file changed since the verdict was computed (verdict against 435a6bb-era content, file sha256 now 0798ff7ac8ddc4aa977c0a31a80d1b7a93bd31d5b4bfac4a6b99c331fefadcf6); verdict not carried over, re-judgement required
> verdicts below describe the pre-change file
- T1 (source check): FINDINGS (classified) — baseline 2026-11-16: exit 1, 2 errors / 0 warns / 2 infos (pseudo-ref×2); standing classes dispositioned in register c1 [T1-ROWS row 7; GOSIGN2-LEDGER (b) row 7]
- T2/T3 (render, combined verdict): FINDINGS — [combined T2/T3] report `FINDINGS` — 768px sidebar×preview-notice overlap hiding notice text, 768px overflow 884px, sample credit-modal; 3 runs to complete (network). [RENDER-ROWS-1 (RENDER-A row 7)]
- Engine coverage: full matrix as run by the lane; coverage not separately caveated in the row [RENDER-ROWS-1 row]
- Credit modal: sample credit-modal errors dispositioned preview-form (credit:start-preview has no modal mechanism; GOSIGN-TESTS T2 amendment, 2026-11-16; ROWS-1 phrases the line bare and takes the disposition from the part header) [RENDER-ROWS-1 (RENDER-A row 7)]
- T4 (localize patterns + follow-up): FINDINGS — display-affecting findings: 1 [LOCALIZE-ROWS row 8, source LOCALIZE-A]
- T5 (translation text): FINDINGS — the source reports judge T4/T5 jointly; one verdict word covers both [LOCALIZE-ROWS row 8]
- FIX5 re-judgement: none — no OPEN items at the ledger determination [GOSIGN2-LEDGER (b) row 7]
- Computed against: canonical commit 1c96ee4f6dbe58243d8c4ba0136a4a4dde806972; candidate file pages/theme:classic-jp.txt sha256:0798ff7ac8ddc4aa977c0a31a80d1b7a93bd31d5b4bfac4a6b99c331fefadcf6; record: GOSIGN2-LEDGER.md + GOSIGN2-LEDGER-SUPPLEMENT.md as of the FIX5 head 435a6bb
<!-- END GENERATED VERDICT STAMP -->

## Status

| | |
|---|---|
| Verdict | **PASS** — passed at the ledger determination; this theme had no OPEN items and no §(e) register entry (GOSIGN2-LEDGER (b) row 7) |
| Standing items | **DISPOSITIONED** — T1 pseudo-ref ×2 (class (ii), section 11); the render row's items (KB-33/KB-34; network item, section 11); T4's P5 (class (ii)/KB-58) and P7 (no display-affecting mark, T4 bar, section 11). The credit fields were **FIXED** by the credit waves. No usage-example defect: the examples name the production page theme:classic, which exists. The headline fact of this package is its provenance route (section 0): the candidate adopts the JP production stylesheet, so most of its CSS diff is production drift, not port editing |
| Go-sign basis | COMPLETION-REPORT.md §10 (go-sign issued; 81 FIXED / 26 DISPOSITIONED / 0 OPEN across the sweep) |
| Named exception | None for this theme (the sweep's single named exception is theme:amethyst-v2, which has no candidate). The labelled Rate + credit pair (section 1) is the AGENTS.md §5 named precedent, not an exception |

## Provenance

| | Original | Candidate |
|---|---|---|
| Page | theme:classic | theme:classic-jp |
| Wiki | scp-wiki.wikidot.com | SCP-JP Sigma-10 candidate (canonical repo) |
| Reference revision | 95 (re-translation reference; the first-translation reference is revision 77 — both are recorded in the candidate's credit block) | — |
| Source of this copy | Mirror store, class COPY (hash-verified against review/sources.tsv) | Canonical file `pages/theme:classic-jp.txt`, copied at worktree HEAD 1605bbd |
| Lines / bytes | 727 lines / 15,069 bytes | 568 lines / 13,738 bytes |
| SHA-256 | 5f6e5a9c73a23ea8aab6be024bdcde257c1d43abddc5b2d7e1aec76d92850931 | 9bc0237a45873606c3e0c1997a42cd899fe3a1af3d19c19a3eccba8e75466d66 |

Third source (the R4 route): the JP production page, held in this repo at `pages-existing/existing:theme-classic.txt`. Classic is one of the themes that already has a live JP translation (first translated 2022, reference revision 77), so the candidate's CSS body is the production page's stylesheet, adopted as it stands, and the diff against the EN revision-95 mirror measures two things at once: the port's furniture changes, and the accumulated drift between the EN original's current CSS and the JP production CSS. The production page's own migration deliverable is `pages/phase17-diff-classic-jp.txt` (per-theme record). Wave history: the candidate was assembled through Phase 17 (reference-revision recording) and Phase 22 (drift incorporation), and last touched by FIX-CREDIT-C (commit 5c32672, the translator-pair completion in the credit blocks).

## Summary

Classic is the batch's R4 case, and this README is written so the drift is never mistaken for editing. The candidate's delivery names the production JP distribution directly: the head module imports `https://scp-jp.github.io/files/theme/classic/style0.css` (candidate L2) and the interwiki frame names the same file (candidate L7). Its CSS body is the production stylesheet — reorganized section comments, and its header line reads "Edited for SCP財団 by MikuKaneko" (candidate L177) where the EN mirror's reads "Forked From Shiny Theme by Gabrys" — so the 21 CSS-BODY blocks are the production-drift measurement, adjudicated as a class in the Class summary, not 21 port edits. What the port itself does is the furniture: the credit block is completed with both reference revisions recorded (77 first translation, 95 re-translation) and the production translator's name kept; the Rate and the preview credit block stand side by side as a labelled pair (the §5 precedent this theme itself sets); the original's standalone info module furniture is converted into a documented code exhibit (candidate L63–106) instead of a live module; and the page's assets are split between the draft host and the production storage host. Measured churn (diff.md, Tier 2: +479/−638, 1,117 changed lines in 53 change blocks — the batch's largest count and its least editable, because most of it is the drift between two living stylesheets).

## Class summary

Auto-classification by review/classify_hunks.py (signature table 2026-11-17.1): 53 change blocks — 14 specific (26.4%), 35 heuristic (66.0%), 4 residue (7.5%), 0 skipped. Pattern citations below name the KB entry; the patterns/ tree state cited throughout is commit 9c5e9079afb01d30cb9fc4ef9d714e5591eb2ffa.

| Label | Blocks |
|---|---|
| CSS-BODY | 21 |
| TRANS-UNANCHORED | 18 |
| EXHIBIT-RESTRUCTURE | 4 |
| INFO-DEL | 3 |
| DELIVERY-HOST | 2 |
| SELF-DELIVERY | 2 |
| IFTAGS | 2 |
| CREDIT-PREVIEW | 2 |
| TASL-FIELDS | 2 |
| DRAFT-HOST | 2 |
| T7-CREDIT-CSS | 2 |
| INCLUDE-REPOINT | 1 |
| BARE-RATE-DEL | 1 |
| TRANSLATION-ANCHORED | 1 |
| ASSET-REHOST | 1 |
| CONTENT-STRING | 1 |

Adjudication for this README (every block was read against the bytes): the CSS-BODY mass (B29–B53's region) is production drift under the R4 route — the candidate body is the production stylesheet (section 0), so a CSS-BODY block here records where the EN rev-95 CSS and the production JP CSS differ, and no block in that region is a port edit; the two T7-CREDIT-CSS labels inside it mark the credit-module CSS regions, present in both bodies. The four EXHIBIT-RESTRUCTURE labels are adjudicated individually in section 8: one region is a genuine exhibit conversion (the info module becoming a code exhibit, section 1/8) and the rest are the standing false-fire shape. The four residue blocks are adjudicated in the appendix, including B27, the CSS header comment that is itself the R4 evidence. After adjudication no block is left unexplained.

## Standing sections

### 0. Header and provenance frame

- **What:** Theme theme:classic-jp; original theme:classic on scp-wiki at reference revision 95; candidate `pages/theme:classic-jp.txt`. Provenance route: **production-counterpart adoption (R4)** — the candidate derives from the JP production page (first translation at revision 77) with the revision-95 mirror as its reference for the re-translation record, not from the EN page directly. Two reference revisions therefore stand in this package, and both are recorded in the candidate's credit block (初訳時参照リビジョン: 77; 改訳時参照リビジョン: 95). Every CSS count below is read against this route.
- **Why:** Section 0 declares the provenance route so the drift is read as drift; R4 exists precisely for themes with a living production translation, where pretending the EN page is the sole baseline would manufacture a thousand fake edits.
- **Verify:** The sources.tsv row for classic-jp; the production page at `pages-existing/existing:theme-classic.txt`; `sha256sum original.txt` against the Provenance table.
- **Disposition:** Standing (the route itself, declared).

### 1. Credit and attribution

- **What:** The candidate's credit region (candidate L20–45) is the production page's credit form carried into the candidate and completed by FIX-CREDIT-C: the preview credit block records title Classic SCP Foundation Theme; 翻訳責任者 KanekoLiku — the production translation's human translator, kept under ruling 3's rule that a human translator's name stands where it matches the live JP creator (this is not an AI translation and is not credited as one); 翻訳年 2022; 原題 Classic SCP Foundation Theme; 著作権者 Lt Flops; 作成年 2020; both reference revisions (77 and 95, section 0); and the source link (candidate L44 region) naming scp-wiki.wikidot.com, the original's recorded host. The Rate state is the labelled pair: `[[module Rate]]` (candidate L23) under its 評価モジュール label and the preview credit block (candidate L25) under its クレジットモジュール label, standing side by side as a documented pair — the AGENTS.md §5 labelled-exhibit exception, for which Classic is the named precedent, so the pair is not the KB-09 duplicate. The original's standalone info module furniture is deleted as live blocks (INFO-DEL ×3, B9/B13/B14's region) and converted into the exhibit of section 8. The T7 credit-module CSS labels (×2) mark credit CSS present in both bodies (production and EN); no supplement was added or dropped.
- **Why:** P3/T1 and ruling 3, including its human-translator clause; §5's labelled-pair precedent for the Rate state.
- **Verify:** Read candidate L20–45; `grep -n 'module Rate\|credit:start-preview' candidate.txt` — the labelled pair at L23/L25.
- **Disposition:** FIXED (credit fields completed by the credit waves, FIX-CREDIT-C last; GOSIGN2-LEDGER §(c3) class outcome: P3 FIXED).

### 2. Includes and components

- **What:** The frame pair (section 3) and the credit pair (section 1). The usage examples inside the info exhibit name the production page: `@@[[include:scp-jp:theme:classic]]@@` (candidate L65) and the parameterized form `@@[[include:scp-jp:theme:classic engtitle=a]]@@` (candidate L71). Both are correct as written — the production page exists under that name (probed for this package, 2026-11-17: scp-jp.wikidot.com/theme:classic returns 200) — because the candidate's subject is the production theme, whose install name has no `-jp` suffix. The batch's usage-example defect (an example naming a nonexistent page) does not apply, and the contrast is recorded so a population sweep does not flag this theme by shape alone: the deciding test is the probe, not the suffix.
- **Why:** P1 (KB-15) for the live includes; the usage examples under the campaign's settled rule (AGENTS.md §6), whose substance is that the named page must exist and be includable.
- **Verify:** `grep -n '\[\[include' candidate.txt`; the probe result above.
- **Disposition:** Applied; no defect.

### 3. Delivery and code loading

- **What:** The candidate delivers from the production JP distribution: the head module imports `scp-jp.github.io/files/theme/classic/style0.css` (candidate L2) and the interwiki-style frame names the same URL as its theme (candidate L7; DELIVERY-HOST ×2, SELF-DELIVERY ×2). The EN original delivered the same role from its own local--code module. There is no draft-host delivery line in this theme: the delivery already names its production host, because the adopted stylesheet is the production file (section 0). The T1 pseudo-ref ×2 are the draft-host asset lines of section 4, not delivery lines.
- **Why:** P4/T9 and P6/T3, in their production form: for an R4 theme the JP host is not a draft-stage promise but the standing distribution.
- **Verify:** `grep -n 'github.io\|local--code' candidate.txt` — candidate L2 and L7.
- **Disposition:** Standing (production delivery); the pseudo-ref items are section 11's.

### 4. Fonts and assets

- **What:** Fonts (P7): the localize lane's P7 item was dispositioned with no display-affecting mark found (the T4 bar, GOSIGN2-LEDGER §(c3)); the candidate's font stacks are the production stylesheet's own, adopted with the body (section 0), so there is no port-side stack rewrite to narrate — any stack difference from the EN mirror is inside the drift region of the Class summary. Assets: the logo is re-hosted to the draft host (candidate L45, scp_foundation_logo.png on sigma10-jp-test) and the image exhibit's frame image likewise (candidate L90, base_image_frame.png), while the body background already sits on the production storage host (candidate L182, body_bg.png on scp-jp-storage) — the mixed state is the production page's own asset arrangement carried into the candidate, and the localize lane's P5 item (images on the draft host) is dispositioned class (ii)/KB-58.
- **Why:** P5/KB-17 and KB-58 for the assets; P7 recorded with its disposition ground rather than narrated as a rewrite that did not happen.
- **Verify:** `grep -n 'wdfiles' candidate.txt` — the draft-host pair and the storage-host line above.
- **Disposition:** DISPOSITIONED (P5, class (ii)/KB-58; P7, no display-affecting mark).

### 5. Header, sidebar, and site furniture

- **What:** The header and sidebar rules are inside the adopted CSS body, so their differences from the EN mirror are drift (Class summary), not furniture edits. No header-variable block stands as a separate change, and no P8 layout adaptation was made by the port. The render row's furniture findings (the sidebar×preview-notice overlap at 768px) are environment-layer items, section 11.
- **Why:** Recording the absence of a furniture change is the check, for an R4 theme especially: the furniture is the production page's, already JP-shaped.
- **Verify:** Compare the header rules in `pages-existing/existing:theme-classic.txt` against candidate.txt — the candidate's furniture is the production page's.
- **Disposition:** Standing.

### 6. Text translation

- **What:** The prose body is the production translation's text, carried and completed: the usage prose, the info exhibit's documentation (including the parameter trick `>[[ift{$engtitle}gs -テーマ]]`, candidate L63–106's region, B45), and the exhibit specimens are translated (TRANS-UNANCHORED ×18, TRANSLATION-ANCHORED ×1, CONTENT-STRING ×1). One specimen is kept in its original scheme deliberately: the link specimen `[[[http://scp-jp.wikidot.com/#|リンク]]]` (candidate L130, B19) demonstrates the link styling with an http URL, as the original's specimen did. In-CSS comments (R1): the adopted body's section comments are the production stylesheet's own (its reorganized `---- SECTION ----` markers), part of the adopted text, not porter annotations.
- **Why:** P10 for the prose; the specimen rule for the http link; R1's distinction between a body's own comments and added text.
- **Verify:** Spot-read candidate L110–135 against the mirror's corresponding prose; the specimen at candidate L130.
- **Disposition:** Standing (the port itself).

### 7. Links

- **What:** The credit source link names scp-wiki.wikidot.com, the original's recorded host — the host check passes. The usage examples' target (theme:classic on scp-jp) is section 2's probed production page. The http link specimen (section 6) is an exhibit, not a navigation link. No hub link needed a repoint.
- **Why:** P11: prose links take the JP counterpart or the serving original; specimens are judged as specimens.
- **Verify:** `grep -n 'wikidot.com' candidate.txt` — the source link, the usage target, and the specimen.
- **Disposition:** Standing; no dead link.

### 8. Structure

- **What:** The structural change is the info conversion: the original's standalone info module blocks (three INFO-DEL blocks) become a single documented code exhibit, "Standalone Info Module" (candidate L63–106), which shows the module's source — including the engtitle parameter trick — as documentation rather than running it live, because the preview credit block of section 1 is the page's credit form. That is the one genuine exhibit restructuring in this package, and it is a conversion, not a deletion: the module's text survives entire inside the exhibit. Exhibit census (R3) for the rest: the original's remaining exhibits (usage, image, link and style specimens) all survive in the candidate in the same order; the other EXHIBIT-RESTRUCTURE labels sit on repoint and drift blocks inside exhibit regions and are discharged on that ground. Inside the CSS, the closing rule is not the port's to apply: the body is the production stylesheet as it stands (section 0).
- **Why:** R3 forces the census; the info conversion is recorded as a conversion because a deletion reading would lose the module's documentation, which the bytes keep.
- **Verify:** Read candidate L63–106 against the original's info blocks; compare the exhibit sequence.
- **Disposition:** Standing; no structural deletion, no class I item.

### 9. Formatting only

- **What:** None separable — the classifier finds no whitespace-only block pair and no re-indentation (0 and 0). The adopted body's internal formatting is the production stylesheet's own and is inside the drift region, not formatting churn by this port.
- **Why:** Formatting churn is disclosed as its own class so it is never mistaken for a semantic change.
- **Verify:** The summary counts in classification.json (`reindent_blocks: 0`).
- **Disposition:** None required.

### 10. Porter annotations

- **What:** None added by the campaign porter. The one editor line in the file — "Edited for SCP財団 by MikuKaneko" (candidate L177, residue B27) — is the production stylesheet's own attribution, standing where the EN mirror's header reads "Forked From Shiny Theme by Gabrys" (original L221–222's region); it is R4 evidence (the candidate body is the production file, edited for SCP-JP by its production editor), not a campaign annotation. No `[!-- ... --]` translator notes exist in the candidate.
- **Why:** R2: porter-added text is part of the change record; an adopted body's own attribution is distinguished from an annotation by its provenance, and here it is also the proof of the route in section 0.
- **Verify:** `sed -n '176,178p' candidate.txt` against original.txt's CSS header; `grep -n '\[!--' candidate.txt` returns nothing.
- **Disposition:** Standing (checked; the editor line is inherited production text).

### 11. Dispositions and exceptions

- **What:** Three items, each with its ground. (1) T1's two pseudo-ref errors: class (ii), posting-procedure — the draft-host asset lines of section 4 (the delivery lines name the production host and are not pseudo-refs). (2) The render row's items, all environment or cross-cutting, not charged to the candidate: the 768px sidebar×preview-notice overlap and the 884px@768 sample overflow (KB-33/KB-34 families), the sample credit-modal item (KB-32 preview form), and the 3-runs network item (a capture-layer transient). (3) T4's P5 and P7: DISPOSITIONED (class (ii)/KB-58 for the asset hosts; no display-affecting mark for the font item, the T4 bar), section 4. The localize row's display-affecting count of 1 was the credit item at its reading, since FIXED (section 1).
- **Why:** A disposition is a decision with grounds (AGENTS.md §3 classes (i)/(ii)/(iii); the named KB entries), not an omission.
- **Verify:** Each item names its deciding record above and in the verdict stamp.
- **Disposition:** DISPOSITIONED (items 1–3); P3 FIXED (section 1).

### 12. Verification

- **What:** (a) T1 source check (T1-ROWS row 7): exit 1, 2 errors / 0 warns / 2 info; both errors are pseudo-ref, class (ii); there is no class (i) error. (b) T2/T3 render (RENDER-ROWS-2, lane RENDER-A): FINDINGS, the items of section 11(2), all dispositioned; engine coverage full matrix as run by the lane. (c) T4/T5 (LOCALIZE-ROWS row 8, lane LOCALIZE-A): FINDINGS jointly, display-affecting findings 1 at reading time (the credit item, since FIXED). (d) This package is self-verifying: `python3 review/build_review.py --check` regenerates diff.md and the verdict stamp from the two byte-faithful copies in this directory and compares. Counts in this README are the generator's (difflib, autojunk off): +479/−638 in 53 change blocks (Tier 2 format).
- **Why:** Verification claims name the cheapest deciding check and its result, not a general assurance.
- **Verify:** Re-run the checker on `pages/theme:classic-jp.txt` and `python3 review/build_review.py --check` in this repo.
- **Disposition:** PASS (GOSIGN2-LEDGER (b) row 7; go-sign, COMPLETION-REPORT §10).

## Per-theme record

### Two reference revisions, and what the production page's own deliverable says

Classic is the only theme in this batch with two reference revisions, and the record matters for anyone who later re-checks the provenance. The production JP page was first translated against EN revision 77 (2022, translator KanekoLiku). Upstream then rewrote the theme wholesale from revision 78 onward — CSS variables, structure, and selectors all changed — so the production page cannot be brought to revision 95 by a local diff: `pages/phase17-diff-classic-jp.txt`, the production page's migration deliverable, records exactly that ("local diff impossible, re-port needed") and settles the production page's own migration as: no change this time; credit only — its sole edit adds the 改訳時参照リビジョン: 95 line to the production credit. The candidate in this package is the Sigma-10 form of that settlement: it adopts the production body (which is why its CSS is the rev-77-lineage stylesheet, not a rev-95 port), and its credit block records both revisions so the lineage is never misread as a missing update. A reviewer who diffs the candidate against the rev-95 mirror and counts a thousand changed lines is measuring the upstream rewrite plus seven years of production drift; the port's own change set is the furniture of sections 1–4.

## Appendix — residue blocks adjudicated

| Block | Original → candidate | Adjudication |
|---|---|---|
| B5 | L13–16 → L11–13 | Head furniture alignment around the frame and gate (the delivery lines themselves are section 3) |
| B16 | L57–61 → L112 | A prose passage whose counterpart sits after the inserted info exhibit (section 8): position shift from the conversion, text translated |
| B27 | L221–222 → L176–177 | The CSS header comment: the EN fork line → the production editor line (section 10; the R4 evidence) |
| B40 | L331–334 → L443–465 | A drift region inside the adopted CSS body (Class summary): the production stylesheet's expanded rules against the mirror's shorter form |

### Post-package repairs (REFRESH3-C)

The items above describe this package as built. The repairs recorded below postdate the package; `candidate.txt` has been recopied from the current canonical `pages/<fullname>.txt` and `diff.md` and the verdict stamp regenerated with `python3 review/build_review.py`, so this package now documents the post-repair candidate. The regenerated stamp reads **STALE** by design: no re-judgement is fabricated here, and the frozen ledger (`GOSIGN2-LEDGER.md` + supplement, FIX5 head 435a6bb) remains the verdict record.

**FIX-SNIPPET — production-predecessor reference audit (landing 358955e).** `FIX-SNIPPET.md` records this theme's two usage exhibits as DRIFT ground D2 (name-neutral static CSS payload; the file's own page-level assets are under the candidate name). Commit 358955e inserted `-jp` after the target on both lines (`:scp-jp:theme:classic` → `:scp-jp:theme:classic-jp`); after the sequelae the lines stand at current candidate L63 and L69 (the `engtitle=a` variant is the second).

**Sequela — head-zone bare Rate removal (landing 1c96ee4).** Commit 1c96ee4 (pages: head-zone bare Rates removed in five themes) deleted the two lines `**評価モジュール:**` and `[[module Rate]]` from the head block, leaving the preview credit module as the single rate-bearing form (AGENTS.md §5 Rate rule). This is 2 deletions, nothing else; it is why the candidate is 2 lines shorter than the package's as-built copy.

## Change set outside the two diffed files

The diff covers two files; this theme's record is the batch's widest. `pages/theme-decoration-sample-classic-jp.txt` is the decoration sample the render checks ran against (its findings are the sample half of section 11(2)). `pages-existing/existing:theme-classic.txt` is the production counterpart (third source, section 0), and `pages/phase17-diff-classic-jp.txt` is its migration deliverable (per-theme record). Neither is edited by this package; both are part of the theme's record. There are no companion fragments and no inbound-link repairs in other candidates for this theme.

## License and attribution

- **Title:** Classic SCP Foundation Theme
- **Author:** Lt Flops
- **Source:** https://scp-wiki.wikidot.com/theme:classic — revision 95 (revision date 2026-07-12 20:13:59)
- **License:** Creative Commons Attribution-ShareAlike 3.0 (CC BY-SA 3.0) — license deed: https://creativecommons.org/licenses/by-sa/3.0/
- **Adaptation:** This package holds a Sigma-10 migration port of the work; changes were made. See "Summary" and "Standing sections" in this README for what changed and why. Translator: KanekoLiku — a human translator credited by the live JP page and retained as the package records it (campaign-rule exception); where the campaign translated, the translator is AI.
