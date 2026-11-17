# Review package — theme:redtape-jp (EN → JP port)

<!-- BEGIN GENERATED VERDICT STAMP — do not hand-edit; regenerate with review/build_review.py -->
## Verdict stamp
- Theme: theme:redtape-jp — origin EN, population #30 [GOSIGN2-LEDGER (b) row 30]
- Overall: STALE — candidate file changed since the verdict was computed (verdict against 435a6bb-era content, file sha256 now 900c530a6c958de95e535336539ef893e0131d4fab08087dd521b2e93fe37978); verdict not carried over, re-judgement required
> verdicts below describe the pre-change file
- T1 (source check): FINDINGS (classified) — baseline 2026-11-16: exit 1, 4 errors / 1 warn / 1 info (pseudo-ref×4); standing classes dispositioned in register c1 [T1-ROWS row 30; GOSIGN2-LEDGER (b) row 30]
- T2/T3 (render, combined verdict): FINDINGS — [combined T2/T3] report `FINDINGS` — WebKit CC "S", "ソース" low contrast 3.23, sample credit-modal + overflow 337–419px, panel-body contrast 1.23. [RENDER-ROWS-1 (RENDER-C row 30)]
- Engine coverage: full matrix as run by the lane; coverage not separately caveated in the row [RENDER-ROWS-1 row]
- Credit modal: sample credit-modal errors dispositioned preview-form (credit:start-preview has no modal mechanism; GOSIGN-TESTS T2 amendment, 2026-11-16; ROWS-1 phrases the line bare and takes the disposition from the part header) [RENDER-ROWS-1 (RENDER-C row 30)]
- T4 (localize patterns + follow-up): PASS — display-affecting findings: 0 [LOCALIZE-ROWS row 30, source LOCALIZE-B]
- T5 (translation text): PASS — the source reports judge T4/T5 jointly; one verdict word covers both [LOCALIZE-ROWS row 30]
- FIX5 re-judgement: none — no OPEN items at the ledger determination [GOSIGN2-LEDGER (b) row 30]
- Computed against: canonical commit 358955eb4013dac2399c414ba8ec2a6e416a3c11; candidate file pages/theme:redtape-jp.txt sha256:900c530a6c958de95e535336539ef893e0131d4fab08087dd521b2e93fe37978; record: GOSIGN2-LEDGER.md + GOSIGN2-LEDGER-SUPPLEMENT.md as of the FIX5 head 435a6bb
<!-- END GENERATED VERDICT STAMP -->

## Status

| | |
|---|---|
| Verdict | **PASS** — passed at the ledger determination; this theme had no OPEN items and no §(e) register entry (GOSIGN2-LEDGER (b) row 30) |
| Standing items | **Nothing charged** — this is the batch's only theme whose T4/T5 record is PASS / PASS with zero display-affecting findings, and the ledger carries no §(c3) line for it because no pattern charge ever stood. The T1 pseudo-refs are draft form (class (iii)); the render row's items are the cross-cutting contrast and overflow families of section 11, all dispositioned. No defect is flagged for this theme |
| Go-sign basis | COMPLETION-REPORT.md §10 (go-sign issued; 81 FIXED / 26 DISPOSITIONED / 0 OPEN across the sweep) |
| Named exception | None for this theme (the sweep's single named exception is theme:amethyst-v2, which has no candidate) |

## Provenance

| | Original | Candidate |
|---|---|---|
| Page | theme:redtape | theme:redtape-jp |
| Wiki | scp-wiki.wikidot.com | SCP-JP Sigma-10 candidate (canonical repo) |
| Reference revision | 147 (first translation 2024-10-02; the candidate's credit block records 初訳時参照リビジョン: 147) | — |
| Source of this copy | Campaign cache `gosign2-lanes/lane-oc-gs-render-c/mirrors/redtape.txt`, via the mirror store (class COPY, hash-verified against review/sources.tsv) | Canonical file `pages/theme:redtape-jp.txt`, copied at worktree HEAD 5506feb |
| Lines / bytes | 1,385 lines / 33,100 bytes | 1,471 lines / 38,378 bytes |
| SHA-256 | 0e4c4ffb46d34d4787f4c9144315d5e2627e5586f7effe0ab9d6294b826fb80b | 7ac4edf80c601ad46a83c3b027274dc5b355663b91132f3f97fe6b90fe42362e |

Wave history: this candidate was not produced by a Stage 2 integration wave. A production JP page, theme:redtape, already exists on scp-jp (review/sources.tsv records "production page theme:redtape exists"), translated in 2024 by nebula2700 — the translator the candidate's own credit block names — and the candidate is that production lineage carried into the Sigma-10 set (sources.tsv kind: branch-original). In this repo the file enters with the canonical sources composition (commit d727e92) and has exactly one later commit, d3e541e ("REDTAPE: reference the live newtempest.png asset"), an asset reference fix. The diff for this pair is Tier 2 (diff.md, 42 diff sections): the classifier's 129 blocks are the unit the sections below cite.

## Summary

REDTAPE, ROUNDERHOUSE's Black Highlighter theme for the REDTAPE // ALLCAPS timeline, is the batch's most elaborate delivery design: the theme ships in light and dark fragments (fragment:redtape-light / fragment:redtape-dark), assembled at render time by a ListPages module, with a per-page `{$years}` template module setting the "Minutes to Midnight" subtitle. The candidate preserves that machinery entire — fragment gate, comment-toggled dark delivery, fragment assembly, template module — while repointing every host to the JP environment: the BHL base to the JP mirror and the ported base theme, the theme's 27 image references to uploaded files on the JP storage wiki, the tail deliveries to the candidate's own draft-host /1 and /2. It converts the bare Rate exhibit into a preview credit block that also carries the CC4 credit component (with the caution-box module that component needs, added in the body), and it appends five small live modules at the tail, each with an English comment naming the JP-environment defect it fixes (mobile history form, mobile submenu, credit heritage pill, dialog headings, credit back-link). The translation is the production one, and the localize check judged it PASS on both T4 and T5 — the only clean sheet in this batch.

## Class summary

Auto-classification by review/classify_hunks.py (signature table 2026-11-17.1): 129 change blocks — 95 specific (73.6%), 25 heuristic (19.4%), 9 residue (7.0%), 0 skipped. Pattern citations below name the KB entry; the patterns/ tree state cited throughout is commit 9c5e9079afb01d30cb9fc4ef9d714e5591eb2ffa.

| Label | Blocks |
|---|---|
| DELIVERY-MOVE | 37 |
| TRANSLATION-ANCHORED | 36 |
| TRANS-UNANCHORED | 28 |
| ASSET-REHOST | 27 |
| EXHIBIT-RESTRUCTURE | 7 |
| WS-ONLY | 7 |
| DELIVERY-HOST | 6 |
| INCLUDE-REPOINT | 6 |
| DRAFT-HOST | 5 |
| SELF-DELIVERY | 3 |
| IFTAGS | 2 |
| ANNOTATION | 1 |
| BARE-RATE-DEL | 1 |
| CREDIT-PREVIEW | 1 |
| CREDIT-PROSE | 1 |
| ESCAPED-INCLUDE | 1 |
| FONT-IMPORT | 1 |
| HEADERVAR | 1 |
| RESTORATION | 1 |
| T7-CREDIT-CSS | 1 |
| TASL-FIELDS | 1 |

Adjudication for this README (every block was read against the bytes): the 37 DELIVERY-MOVE blocks are this theme's signature artefact, adjudicated in section 3 — the classifier's channel-overlap signature fires across the code exhibit of a fragment-delivered theme, and in substance those blocks are carried exhibit lines bearing re-hosts (21 of them also carry ASSET-REHOST), whitespace touches, and one font import; the topology pass's two "moves" are 0.667-similarity pairings between the 857-line exhibit and 6-line modules, not real moves. The seven EXHIBIT-RESTRUCTURE blocks are repoints and re-hosts inside exhibits (the census in section 8). The RESTORATION primary (B17) is the added CC4 caution module of section 1. The nine residue blocks are link repoints, a heading, and in-universe exhibit headings (appendix). After adjudication no block is left unexplained.

## Standing sections

### 0. Header and provenance frame

- **What:** Theme theme:redtape-jp; original theme:redtape on scp-wiki at reference revision 147; candidate `pages/theme:redtape-jp.txt`. Provenance route: the production-lineage route of the Provenance table (sources.tsv kind: branch-original) — the candidate descends from the existing scp-jp production translation rather than from a campaign wave's fresh port, which is why its credit block names a human translator and a 2024 translation year, and why several of its forms (the credit block's double-space field form, the tail supplements of section 10) are production forms rather than wave forms. The original opens with its FRAGMENTS comment (original L1–4) ahead of the gate; the candidate opens with the fragment gate itself (candidate L1–3, section 2) and the translated comment below it (candidate L5–8). The gate localizes as usual (`[[iftags +theme]]` → `[[iftags +テーマ]]`).
- **Why:** Section 0 declares the provenance route so every later count is read against the right baseline — for this theme, against a production translation's conventions, not a wave port's. The gate's tag is P2 (iftags tag localization).
- **Verify:** The sources.tsv row for redtape-jp (kind and note columns); `sha256sum original.txt` against the Provenance table.
- **Disposition:** Standing (the route itself); the gate change is P2, applied.

### 1. Credit and attribution

- **What:** The original's only credit furniture is a bare rating exhibit: a centred `[[module Rate]]` with no heading (original L26–28). The candidate deletes it (block B9, BARE-RATE-DEL) and installs the preview credit block (candidate L34–45): the eight ruling-3 fields in the production form （タイトル REDTAPE THEME; 翻訳責任者 nebula2700; 翻訳年 2024; 原題 REDTAPE THEME; 著作権者 Rounderhouse; 作成年 2022; 初訳時参照リビジョン 147; the source link, host-verified in section 7), with one addition no other theme in the batch has: a `[[:scp-jp:credit:cc4]]` include inside the block (candidate L44), the CC4 credit component — this theme's license form is CC BY 4.0, and the block carries the component that renders it. The author field names Rounderhouse, the author the original's own intro names (the REDTAPE timeline is "by ROUNDERHOUSE", original L38). Supporting the CC4 component, the candidate adds a live module in the body carrying the `.cc4-caution` rules (candidate L96–107, block B17 — the classifier's RESTORATION: the caution-box styling the component's markup requires, present in the candidate though the frozen original does not carry it as a live module). The credit heritage styling at the tail is section 10's third supplement. No T7 supplement was needed beyond that heritage module: the credit block's own presentation is the CC4 component's.
- **Why:** P3/T1: the preview credit module is the rate-bearing JP form, replacing the bare exhibit (the class C / KB-10 shape). Ruling 3 fixes the eight fields; the CC4 include is this theme's license mechanism, and a component whose styles are absent renders unstyled — the failure the caution module prevents.
- **Verify:** `grep -n 'module Rate' candidate.txt` returns nothing; read candidate L34–45 against the eight fields and the cc4 include; the caution module reads at candidate L96–107.
- **Disposition:** Applied (no ledger P3 item stands for this theme; T4/T5 judged the credit PASS, section 12).

### 2. Includes and components

- **What:** The candidate's first three lines are its fragment gate: `[[iftags]] [[include :scp-jp:theme:black-highlighter-theme]] [[/iftags]]` (candidate L1–3) — the base theme included for the fragment host pages, the JP port's name for the base the original's exhibits name as `:scp-wiki:theme:black-highlighter-theme`. The head frames are repointed to `:scp-jp:component:interwiki-style` (blocks B4, B6, candidate L20, L25). The thumbnail exhibit's image-block is repointed `:scp-jp:` with its image re-hosted (block B8, candidate L31, section 4). At the tail, the BHL components are repointed (blocks B123, B126: `centered-header-bhl` and `toggle-sidebar-bhl`, candidate L1420–1421) and the frame follows (candidate L1431). The usage exhibits (block B19: original L81–84 → candidate L119–122) repoint both includes to `:scp-jp:` and name `theme:redtape` — the production page's name, which exists on scp-jp (section 0): the exhibits document the include a user actually pastes in production, so the plain name here is the correct target, not the plain-slug defect family (whose defining condition is that the named page will not exist). The exhibits' argument comments (`|dark=--`, `|years=XX`) are translated with their explanations.
- **Why:** P1 (KB-15): an include must name the JP counterpart that actually exists on scp-jp — for the base and components, the `:scp-jp:` forms; for the theme itself, the production name under which users include it. Ruling 4 is satisfied by the base's own JP port, which the fragment gate includes.
- **Verify:** `grep -n '\[\[include' candidate.txt` — the gate (L2), frames (L20, L25), image-block (L31), credit trio (L34, L44, L45), BHL components (L1420, L1421), tail frame (L1431), and the escaped exhibits (L119–120).
- **Disposition:** Applied.

### 3. Delivery and code loading

- **What:** The delivery design is preserved entire, and its preservation is this package's main structural fact. The original delivers in four channels: the head module importing the BHL base pair (original L7–10); two code exhibits (857 and 108 lines) whose text is the light and dark fragment sources; the tail self-delivery modules /1 and /2 (original L1360–1367), the /2 wrapped in a `[!-- {$dark} … --]` comment toggle; and the fragment assembly — a ListPages module inside a second tag gate that injects the chosen fragment's content (original L1379–1385 area, with the `{$years}` template module). The candidate keeps every channel: the head module's imports are repointed to the JP BHL mirror (blocks B3, B5, B7) and the module gains one rule (candidate L15–17, a template-dialog link colour — a production supplement inside the module); the exhibits stand at 889 and 108 lines (the growth is section 4's re-hosts, section 6's comments, and the font import); the tail modules are repointed to the candidate's own draft-host /1 and /2 with the dark toggle intact (blocks B124, B125, B127, candidate L1422–1434); the ListPages assembly is carried with its gate tag localized (block B128); and the `{$years}` template module is carried byte-identical (original L1379–1385 = candidate L1439–1445). The classifier's topology pass counts 6 components in the original and 12 in the candidate; the six additions are the CC4 caution module (section 1) and the five tail supplements (section 10) — no original component is dropped, split, or merged. The 37 DELIVERY-MOVE labels are adjudicated in the class summary: on a theme whose exhibit text is also its delivered fragment text, the channel-overlap signature fires on carried lines; the real delivery changes are the ones enumerated in this section.
- **Why:** P4/T9 and P6/T3: the live channels must be the ones that exist in the JP environment, at the original's priorities (base frames 1–2, own frame 3); the fragment mechanism is the theme's own design (its light/dark variants are separate deliveries, not a formatting choice), so the port's job is to re-host it, not to flatten it into a single module.
- **Verify:** Compare the component sequences (`grep -n '\[\[module\|\[\[code' original.txt candidate.txt`) — every original channel has its candidate counterpart at the loci named above; the dark toggle reads at candidate L1425–1429.
- **Disposition:** DISPOSITIONED (draft-host tail deliveries, class (iii)); the mechanism preservation is applied.

### 4. Fonts and assets

- **What:** Fonts: the pair's one font-load change is an addition inside the code exhibit (block B85, candidate L432): `@import url('https://fonts.googleapis.com/css2?family=M+PLUS+1p:wght@800;900&display=swap')` — the JP display face the production translation loads for the theme's headings; the original loads no JP face (its faces arrive with the BHL base). Assets (ASSET-REHOST ×27, all applied): the theme's image references move to uploaded files on the JP storage wiki, each under its own file page in the `file:8260379-*` series — among them the thumbnail (candidate L31), the logo variable's midnightwhite.png (block B86, candidate L441), topolight.png (L710), Untitled2.png (L725), topotrans.png (L764), redtapes.png (L780), and newtempest.png (candidate L239 — the reference the repo's one asset commit, d3e541e, fixed). Two body images are re-hosted instead to the candidate page's own draft-host file area (blocks B11, B13: the BHL logo at candidate L52 and redtapeexample.png at L60), the class (iii) form. No image reference to the EN wiki's file area remains.
- **Why:** P5: images a theme loads must not depend on the original wiki's file area in the JP environment; the storage-wiki uploads are the production lineage's applied form. P7 (KB-16) for the font load: the headings' JP glyphs need a named, loaded JP face, and M PLUS 1p at its display weights is the production choice.
- **Verify:** `grep -n 'scp-wiki.wdfiles\|scp-wiki.wikidot.com/local--files' candidate.txt` returns nothing; `grep -c 'scp-jp-storage' candidate.txt` counts the storage references; the font import reads at candidate L432.
- **Disposition:** Applied (re-hosting and font load); the two draft-area images are DISPOSITIONED as class (iii) form.

### 5. Header, sidebar, and site furniture

- **What:** The header variables sit inside the code exhibit (candidate L442–443): `--header-title: "REDTAPE"` — the timeline's name, a proper noun, carried — and `--header-subtitle: "{$years} Minutes to Midnight"`, the templated fixed string whose `{$years}` placeholder the tail template module fills per page (candidate L1442); its English is the timeline's fixed subtitle, and the usage exhibit translates the explanation of the mechanism (section 2) rather than the string. The logo variable is section 4's re-host (block B86, HEADERVAR). Sidebar furniture arrives with the BHL components of section 2 (toggle-sidebar-bhl) and the mobile submenu supplement of section 10.
- **Why:** P8 (KB-19): header strings are localized where they are prose; a proper name and a templated title string are the two carried exceptions, and both are the theme's identity rather than untranslated documentation.
- **Verify:** `grep -n -- '--header-' candidate.txt` — L442, L443, and the template module's L1442.
- **Disposition:** Applied.

### 6. Text translation

- **What:** The translation is the production translation, and its coverage is complete: the usage documentation, the exhibits — including the theme's in-universe document exhibits, whose headings translate as prose (the residue blocks B58, B61, B62, B64: "ATTACHED TRANSCRIPT - JUNE 1983" → 添付記録 - 1983年 6月; the FOUNDATION NOTICE headings → 財団通達， with their codenames 'SNOW' and 'GUERRE' kept) — and the FRAGMENTS header comment (フラグメント, candidate L5). The counted groups are 36 TRANSLATION-ANCHORED blocks and 28 TRANS-UNANCHORED blocks; the anchored blocks were verified line by line. The five tail supplements' comments are English porter comments, recorded in section 10, not translation gaps: they document JP-environment fixes for the porters, in the production file's own convention.
- **Why:** P10 (body and usage translation is the port's purpose) and KB-18 (reader-visible strings). T4/T5 judged this translation PASS on both checks (section 12) — the only theme in the batch with no localize finding at all.
- **Verify:** The pairs are diff.md's body sections in order.
- **Disposition:** Standing (the port itself; judged PASS / PASS by LOCALIZE-B).

### 7. Links

- **What:** The credit block's source link (candidate L43) names `https://scp-wiki.wikidot.com/theme:redtape` — the original's recorded host (review/sources.tsv `original_url`), so the host check passes and no probe was triggered; its label is ソース， in the single-bracket link form the production file uses. The LIGHT / DARK selector links at the head (residue block B10: original L31 → candidate L48) repoint from the EN page's offsets to the production JP page's: `https://scp-jp.wikidot.com/theme:redtape/offset/0` and `/offset/1` — the variant switcher targets the page that actually serves the variants in production. Inside the exhibits, three raw-HTML link lines repoint their targets from scp-wiki to scp-jp (residue blocks B74, B76, B78: the rounderhouse-gold-proposal and airgap exhibit buttons, candidate L335, L356, L365).
- **Why:** P11: prose links take the JP counterpart where one exists; the offset links are functional (they switch the reader's own view between the fragments), so their target is the serving production page, not a citation.
- **Verify:** `grep -n 'offset/0\|rounderhouse-gold-proposal\|airgap' candidate.txt` — the loci named above, all scp-jp hosts.
- **Disposition:** Applied.

### 8. Structure

- **What:** The exhibit census corresponds, with three named additions and no deletions: the usage and examples exhibits, both code exhibits, the fragment assembly, and the template module are present on both sides in the same order; the additions are the fragment gate at the head (section 2), the CC4 caution module (section 1), and the five tail supplements (section 10). The seven EXHIBIT-RESTRUCTURE labels are repoints and re-hosts inside exhibits (the thumbnail, the frames, the BHL components), adjudicated in the class summary. Selector and variable names inside the CSS are preserved.
- **Why:** R3: the census is what separates an addition (this theme, each one named) from a silent restructure or drop (the failure class I charges); here every original region has a named candidate counterpart and every candidate addition has a named purpose.
- **Verify:** Compare the heading, include, and module sequences of the two files — they correspond at the loci named in sections 1–3 and 10.
- **Disposition:** Standing.

### 9. Formatting only

- **What:** Seven whitespace-only blocks (WS-ONLY ×7: B59, B81, and five riding inside the DELIVERY-MOVE group at the exhibit's tail, B84 and B116–B119), single lines in the body and the code exhibit differing only in whitespace. No re-indentation occurs (0 reindent blocks).
- **Why:** Formatting churn is disclosed as its own class so it is never mistaken for a semantic change.
- **Verify:** The classifier summary in classification.json (WS-ONLY ×7).
- **Disposition:** Standing.

### 10. Porter annotations

- **What:** Two annotation forms, both recorded. (1) The FRAGMENTS header comment (block B1, the ANNOTATION label): the original's own `[!-- FRAGMENTS … --]` comment listing its two fragment URLs, carried in translation with the URLs repointed to the scp-jp fragment pages (candidate L5–8) — the original's annotation, not a porter's addition, and its repoint is what makes the fragment list true in the JP environment. (2) The five tail supplement modules (block B129, candidate L1446–1471), each a live `[[module CSS]]` with an English comment naming its purpose: the history-form mobile viewport fix; the mobile submenu single-column fix; the credit heritage rating module's dark pill ground (the T7 credit CSS of this theme); the dialog headings colour fix; and the BHL credit back-link nowrap fix. These are production-lineage environment corrections, added as separate modules so each can be read, and removed, on its own merits.
- **Why:** R2: porter-added text is part of the change record; here it is unusually well labelled by its own authors, and this section's job is to point at it and group it, which the diff's single T7-CREDIT-CSS label (it names only the third module's family) does not do on its own.
- **Verify:** `sed -n '1446,1471p' candidate.txt` — the five commented modules; the header comment reads at candidate L5–8 against original L1–4.
- **Disposition:** Standing (recorded; each supplement's stated purpose is verifiable against the rule it carries).

### 11. Dispositions and exceptions

- **What:** Two items, each with its ground. (1) T1's four pseudo-ref errors: class (iii) — the draft-host references of sections 3 and 4 (the tail /1 and /2 imports, the tail frame's theme target, and the two draft-area body images). There are no hotlink errors: every EN-host reference is re-hosted or repointed. (2) The render row's items, all cross-cutting families: on the sample and page, the credit-modal errors (KB-32, ruling 5) and the page-overflow range 337–419px (KB-33/KB-34 families); and two contrast lines the row names individually — the WebKit CC pair ("S" and "ソース") at contrast 3.23 and the panel-body contrast 1.23 — recorded as the row records them, in the cross-cutting contrast family the campaign dispositions with the row. No T4/T5 item exists to disposition: LOCALIZE-B judged the theme PASS / PASS.
- **Why:** A disposition is a decision with grounds (AGENTS.md §3 classes (i)/(ii)/(iii); the named KB entries), not an omission.
- **Verify:** Each item names its deciding record above and in the per-theme record.
- **Disposition:** DISPOSITIONED (both items).

### 12. Verification

- **What:** (a) T1 source check (T1-ROWS row 30): exit 1, 4 errors / 1 warn / 1 info; all four errors are pseudo-ref, the class (iii) item of section 11(1); there is no class (i) error. (b) T2/T3 render (RENDER-ROWS-1, lane RENDER-C (row 30)): FINDINGS, the items of section 11(2), all dispositioned. (c) T4/T5 (LOCALIZE-ROWS, the LOCALIZE-B set): **PASS / PASS, display-affecting findings 0** — this theme is one of the 19 full passes in the population and the only one in this batch; consequently the ledger carries no §(c3) line for it. (d) This package is self-verifying: `python3 review/build_review.py --check` regenerates diff.md and the verdict stamp from the two byte-faithful copies in this directory and compares. Counts in this README are the generator's (difflib, autojunk off): +247/−161 in 129 classifier change blocks / 42 diff sections.
- **Why:** Verification claims name the cheapest deciding check and its result, not a general assurance; a PASS record is cited with the same precision as a findings record.
- **Verify:** Re-run the checker on `pages/theme:redtape-jp.txt` and `python3 review/build_review.py --check` in this repo.
- **Disposition:** PASS (GOSIGN2-LEDGER (b) row 30; go-sign, COMPLETION-REPORT §10).

## Per-theme record

No defect flag and no prose-versus-bytes discrepancy arose for this theme. Two record facts are worth a reader's attention. First, the theme's candidate is the batch's only production-lineage file (section 0): its divergences from the wave-port form elsewhere in the batch — the human translator credit, the double-space field form, the English porter comments on the tail supplements — are the production file's own conventions, and the localize check's PASS / PASS judgement was made on the file in exactly this form. Second, the sources.tsv note records that no phase17 diff page exists for this theme and that the TSV existence check agrees （一致） — the candidate's provenance rests on the production page and the mirror, not on a phase-17 comparison artifact.

## Appendix — residue blocks

Nine blocks, resolved here by shape:

| Block | Span | Resolution |
|---|---|---|
| B10 | orig 31-31 → cand 48-48 | The LIGHT / DARK offset link line, repointed to the production JP page (section 7). |
| B20 | orig 88-88 → cand 126-126 | Heading translation: `+ Examples` → `+ 例`. |
| B58 | orig 187-187 → cand 225-225 | In-universe exhibit heading: "ATTACHED TRANSCRIPT - JUNE 1983" → 添付記録 - 1983年 6月 (section 6). |
| B61 | orig 206-206 → cand 244-244 | In-universe exhibit heading: "FOUNDATION NOTICE" → 財団通達. |
| B62 | orig 213-213 → cand 251-251 | Same shape: "FOUNDATION NOTICE 'SNOW'" → 財団通達 'SNOW'. |
| B64 | orig 227-227 → cand 265-265 | Same shape: "FOUNDATION NOTICE 'GUERRE'" → 財団通達 'GUERRE'. |
| B74 | orig 297-297 → cand 335-335 | Raw-HTML exhibit link line, host repointed to scp-jp (rounderhouse-gold-proposal; section 7). |
| B76 | orig 321-321 → cand 356-356 | Raw-HTML exhibit link line, host repointed to scp-jp (airgap; section 7). |
| B78 | orig 330-330 → cand 365-365 | Raw-HTML exhibit link line, host repointed to scp-jp (airgap; section 7). |

## Change set outside the two diffed files

The diff covers two files; the port's record is one file larger in the repo and several files larger in the world. `pages/theme-decoration-sample-redtape-jp.txt` is the decoration sample the render checks ran against (its findings are the sample half of section 11(2)); it belongs to this theme's record but carries no port change of its own to explain here. Outside the repo, the theme's delivery depends on the two fragment pages (fragment:redtape-light / fragment:redtape-dark on scp-jp, named in the header comment) and on the storage-wiki uploads of section 4; both are part of the production lineage's standing state, not changes made by this package. There are no companion fragments inside the repo, no shared base file, and no inbound-link repairs in other candidates for this theme.
