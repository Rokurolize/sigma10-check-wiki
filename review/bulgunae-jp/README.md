# Review package — theme:bulgunae-jp

<!-- BEGIN GENERATED VERDICT STAMP — do not hand-edit; regenerate with review/build_review.py -->
## Verdict stamp
- Theme: theme:bulgunae-jp — origin KO, population #255 [GOSIGN2-LEDGER (b) row 255]
- Overall: STALE — candidate file changed since the verdict was computed (verdict against 435a6bb-era content, file sha256 now c99ffb4f209103d9aae06fb7fa9360d2a4b7b20c8d63de570182bb008c54c59b); verdict not carried over, re-judgement required
> verdicts below describe the pre-change file
- T1 (source check): FINDINGS (classified) — baseline 2026-11-16: exit 1, 10 errors / 0 warns / 7 infos (hotlink×6, old-bhl×2, http×1, pseudo-ref×1); standing classes dispositioned in register c1 [T1-ROWS row 238; GOSIGN2-LEDGER (b) row 255]
- T2/T3 (render, combined verdict): FINDINGS — [combined T2/T3] report `FINDINGS` — page sidebar-not-opening + candidate-own runtime hosts (nu-scptheme.github.io, scp-wiki.wikidot.com / www.scp-wiki.net) recorded verbatim; sample credit-modal (preview-form) + page-overflow 493–500px@320/375; T3 custom red/black header lettering collides and is partly illegible at 375/320 (both engines; possibly intended stylization). [RENDER-ROWS-2 (RENDER-S2-H (KO2))]
- Engine coverage: full matrix as run by the lane; coverage not separately caveated in the row [RENDER-ROWS-2 row]
- Credit modal: sample credit-modal errors dispositioned preview-form (credit:start-preview has no modal mechanism; GOSIGN-TESTS T2 amendment, 2026-11-16) [RENDER-ROWS-2 (RENDER-S2-H (KO2))]
- T4 (localize patterns + follow-up): FINDINGS — display-affecting findings: 1 [LOCALIZE-ROWS row 254, source LOCALIZE-S2-F]
- T5 (translation text): FINDINGS — the source reports judge T4/T5 jointly; one verdict word covers both [LOCALIZE-ROWS row 254]
- FIX5 re-judgement: none — no OPEN items at the ledger determination [GOSIGN2-LEDGER (b) row 255]
- Computed against: canonical commit e217dbd448bc7d0cf2f77fe4b5bc63be025341af; candidate file pages/theme:bulgunae-jp.txt sha256:c99ffb4f209103d9aae06fb7fa9360d2a4b7b20c8d63de570182bb008c54c59b; record: GOSIGN2-LEDGER.md + GOSIGN2-LEDGER-SUPPLEMENT.md as of the FIX5 head 435a6bb
<!-- END GENERATED VERDICT STAMP -->

## Status

| | |
|---|---|
| Verdict | **PASS** — passed at the ledger determination; this theme had no OPEN items and no §(e) register entry (GOSIGN2-LEDGER (b) row 255) |
| Standing items | **DISPOSITIONED** — T1 hotlink ×6 / old-bhl ×2 / http ×1 / pseudo-ref ×1 (class (ii), section 11); the render row's items (sidebar, runtime hosts, credit-modal preview form, overflow, header lettering, section 11); T4's credit-title wording (section 1). **FLAGGED, since repaired:** the original's second module (orig L993–1010) was absent from the candidate as built and no record named the drop (sections 8 and 11); the block has since been restored verbatim as a second `[[module css]]` at candidate L1283–1300 (canonical commit 9351aec), and this package documents the corrected candidate |
| Go-sign basis | COMPLETION-REPORT.md §10 (go-sign issued; 81 FIXED / 26 DISPOSITIONED / 0 OPEN across the sweep) |
| Named exception | None for this theme (the sweep's single named exception is theme:amethyst-v2, which has no candidate) |

## Provenance

| | Original | Candidate |
|---|---|---|
| Page | theme:bulgunae | theme:bulgunae-jp |
| Wiki | scpko.wikidot.com | SCP-JP Sigma-10 candidate (canonical repo) |
| Reference revision | 5 (first translation; the candidate's credit block records 初訳時参照リビジョン: 5) | — |
| Source of this copy | Campaign cache `gosign2-lanes/lane-oc-gs-localize-s2-F/orig-bulgunae.txt`, via the mirror store (class COPY, hash-verified against review/sources.tsv) | Canonical file `pages/theme:bulgunae-jp.txt`, copied at worktree HEAD 1605bbd |
| Lines / bytes | 1,283 lines / 42,732 bytes | 1,286 lines / 42,974 bytes |
| SHA-256 | f2abc42b49d6e1ccda26fa9cea97a46c7847d97b0a82460b2ff72191e1a5f552 | 0ef4bd6abf8f984c8c5c13f99db1969d9e7335059e1a66c263bef97cfd9b0773 |

Wave history: the candidate was created by the Stage 2 KO2 integration (commit d72b7b9, the LOCALIZE-S2-F wave's port). Three early commits touch it: 95fd1d1 (rework2-p1, +3 lines — this theme was one of the 9 DROP pairs whose missing base delivery the rework restored), 1869877 (FIX-CREDIT-D, translator-attribution normalization), and 443c608 (FIX4-REPOINT, a one-line change; the commit names bulgunae's item as its KB-07 interwiki-style fix). Two post-verdict repairs followed: 9351aec restored the dropped rating-module block verbatim (FIX-BULGUNAE.md), and e217dbd re-applied the sweep's L19 posting-name completion after 9351aec's whole-file copy had reverted it. No FIX5 commit touches this file, because the theme had no OPEN items for FIX5 to re-judge.

## Summary

A Black Highlighter family theme whose port is mostly a delivery rebuild. The original carries its whole CSS in three sequential `[[module CSS]]` blocks on the page, layered over the EN BHL include, with the sidebar component and the usage text at the tail. The candidate repoints the base include and the sidebar component to their JP forms at the head, adds the preview credit block, consolidates the CSS into the single `[[code]]` exhibit body that the tail delivery serves (own local--code on the draft host, interwiki-style frame at priority 3, the own-layer value for a BHL-based theme), adds the Noto Sans JP load, and percent-encodes the colons in the six inherited foundation-theme asset URLs. Measured churn is small (diff.md, the generator's difflib count with autojunk off: +65/−44, 109 changed lines in 12 change blocks; a GNU-diff count gives 101 changed lines — the difference is alignment choice, not content), because the CSS body travels nearly verbatim. Two things deserve a reviewer's eye: the credit block's title field is the original's Korean title, untranslated (T4's recorded item, section 1); and one whole module of the original — the rating-module variables and rate-widget gradient (orig L993–1010) — was absent from the candidate as built with no record naming the drop, which this package flagged rather than dispositioned (sections 8 and 11). The flag is now closed: the dropped block has been restored verbatim as a second `[[module css]]` at candidate L1283–1300 (canonical commit 9351aec; record FIX-BULGUNAE.md in the campaign record, R/review-scout/), and the subsumption question the flag left open is answered against the restored block (section 8).

## Class summary

Auto-classification by review/classify_hunks.py (signature table 2026-11-17.1): 12 change blocks — 12 specific (100%), 0 heuristic, 0 residue, 0 skipped. Pattern citations below name the KB entry; the patterns/ tree state cited throughout is commit 9c5e9079afb01d30cb9fc4ef9d714e5591eb2ffa.

| Label | Blocks |
|---|---|
| DELIVERY-MOVE | 10 |
| COLON-ENC | 6 |
| IFTAGS | 2 |
| CREDIT-PREVIEW | 1 |
| DRAFT-HOST | 1 |
| EXHIBIT-RESTRUCTURE | 1 |
| INCLUDE-REPOINT | 1 |
| JPFONT-LOAD | 1 |
| SELF-DELIVERY | 1 |
| TASL-FIELDS | 1 |
| TRANS-UNANCHORED | 1 |

Adjudication for this README (every block was read against the bytes): the DELIVERY-MOVE count overstates the relocation — B3–B9 are the module-boundary and import lines of the consolidation (section 3), the six COLON-ENC blocks ride inside them as the same lines' second label, and B10 is not a move at all: the original's second module had no counterpart anywhere in the candidate as built, so B10 adjudicated to a deletion and was flagged in sections 8 and 11. The one EXHIBIT-RESTRUCTURE primary (B11) is the tail reorganization (module close, sidebar relocation, gate), not an exhibit change (section 8). After adjudication, every block is explained, and one block (B10) was explained as an unrecorded deletion — since repaired: the module is restored at candidate L1283–1300 (9351aec), so in the candidate this package documents B10's content is present again, as a live module of its own after the delivery module (section 8).

## Standing sections

### 0. Header and provenance frame

- **What:** Theme theme:bulgunae-jp; original theme:bulgunae on scpko at reference revision 5; candidate `pages/theme:bulgunae-jp.txt`. Provenance route: derived from the original at the reference revision by the LOCALIZE-S2-F wave (sources.tsv kind: standard; no production JP counterpart exists for this theme, so the R4 adoption question does not arise). The frame differs in shape from a Sigma-9 port: the original stacks its delivery on the page itself (BHL include, three module-CSS blocks, sidebar include and gate at the tail, usage inside the gate); the candidate puts the base includes, gate, credit, and usage at the head and the delivery at the tail (section 3).
- **Why:** Section 0 declares the provenance route and the topology baseline; the gate's tag is P2, the base include is P1/T9, the tail frame is P6/T3.
- **Verify:** The sources.tsv row for bulgunae-jp; `sha256sum original.txt` against the Provenance table.
- **Disposition:** Standing (the route itself); the frame changes are recorded in sections 2 and 3.

### 1. Credit and attribution

- **What:** The original carries no credit furniture at all: no credit block, no info pair, and no `[[module Rate]]` anywhere on the page (the rate widget is the BHL base's). The candidate installs the JP form at the head: a `:scp-jp:credit:start-preview`/`end-preview` block (candidate L6–15, block B2) carrying the eight ruling-3 fields (title 불구내 테마; 翻訳責任者 AI; 翻訳年 2026; 原題 불구내 테마; 著作権者 AXOL0TL; 作成年 2024; 初訳時参照リビジョン 5; the source link, naming scpko.wikidot.com/theme:bulgunae, the recorded host, which serves the original). The fields are complete and checker-verified; the one wording item is the title field, which repeats the original's Korean title rather than a Japanese rendering — that is T4's type-3 finding for this theme (LOCALIZE-ROWS row 254: §3 title untranslated, marked 軽微， with attribution itself complete). T7 credit-module CSS: none added — the candidate carries no `.creditButton`/`.creditRate` rules of its own; credit styling is the base's layer. License box: none on either side, and none added (the theme has no file exhibits requiring one).
- **Why:** P3/T1: the preview credit block is the JP environment's credit form, installed where the original had none. Ruling 3 fixes the eight fields; the ledger §(c3) line for this theme records the outcome as "P3 credit fields FIXED (credit waves; checker-verified)", and FIX-CREDIT-D (1869877) is the wave commit in this file's history. The title wording stands as the localize lane recorded it; this package does not silently improve it, because the candidate is documented as it stands.
- **Verify:** Read candidate L6–15 against the eight fields; `grep -n 'module Rate\|license-box' candidate.txt` returns nothing.
- **Disposition:** FIXED (credit fields, credit waves); the title wording is DISPOSITIONED as a recorded minor T4 item.

### 2. Includes and components

- **What:** Three include changes (block B1 and the tail). (1) The base include is repointed: `:scp-wiki:theme:black-highlighter-theme` (original L1) → `:scp-jp:theme:black-highlighter-theme` (candidate L1), the JP port of the BHL base. (2) The sidebar component is repointed and relocated: `:scpko:component:bhl-dark-sidebar` sat at the original's tail (L1275, after the CSS modules); the candidate carries `:scp-jp:component:bhl-dark-sidebar` at the head (L2), ahead of the gate. (3) The usage example is repointed and escaped: `:scpko:theme:bulgunae` → `:scp-jp:theme:bulgunae-jp` (candidate L19, the posting form). The sweep's completion (b5cb724) was briefly reverted by the module-restore landing (9351aec) and re-applied by canonical commit e217dbd; the line stands in its completed posting form today, and the once-OPEN item is closed (per-theme record). The credit includes (section 1) and the interwiki-style include (section 3) complete the list; every include in the candidate names a `:scp-jp:` target.
- **Why:** P1 (KB-15): an include must name the JP counterpart that actually exists on scp-jp; both the base theme and the sidebar component have verified JP ports. The sidebar's move to the head is part of the candidate's head/tail frame shape (section 0), not a separate decision. Ruling 4 is not engaged: no component had to be ported alongside this theme.
- **Verify:** `grep -n '\[\[include' candidate.txt` — six includes, all `:scp-jp:`.
- **Disposition:** Applied; no foreign include kept, no named exception needed.

### 3. Delivery and code loading

- **What:** The delivery is rebuilt. The original serves its CSS from three sequential `[[module CSS]]` blocks on the page (original L3–992, L993–1010, L1011–1273), layered over the BHL include. The candidate consolidates the CSS into one `[[code type="css"]]` exhibit body (candidate L26–1275) and serves it from the tail frame: a `[[module css]]` importing the candidate's own `local--code/theme%3Abulgunae-jp/1` from the draft host (candidate L1280–1282, SELF-DELIVERY block B12), followed by a second live `[[module css]]` carrying the rating-module overrides restored after this package was built (candidate L1283–1300, section 8), and an interwiki-style include at **priority 3** with `theme=` naming the same /1 delivery (candidate L1301–1304). The classifier's DELIVERY-MOVE blocks B3–B9 are the consolidation's boundary lines (the module open/close lines and the head import lines changing channel from module-css to code-css; body similarity 0.99). Two wave commits after the initial port repaired this frame: 95fd1d1 restored the base delivery (+3 lines; this theme was one of the rework's 9 DROP pairs), and 443c608 (FIX4-REPOINT) made a one-line KB-07 correction to the frame.
- **Why:** P4/T9 (own-code delivery served from JP hosts) and P6/T3 (the interwiki-style frame). The priority value is the BHL layering convention (1 normalize / 2 base / 3 own): the base layers arrive through the head BHL include, so the theme's own layer correctly takes 3, where a Sigma-9 port takes 1. The code-exhibit form is the campaign's applied-CSS convention for consolidated themes (the same shape the blood port was given by its own wave commit). The draft-host form of the live lines is KB-41, class (iii).
- **Verify:** `grep -n 'local--code' candidate.txt` — L1281 and L1303, both the candidate's own delivery; `grep -n '\[\[module\|\[\[code' candidate.txt` shows the single code body and two tail modules (the delivery import and the restored overrides module).
- **Disposition:** DISPOSITIONED (draft-host lines, class (iii)); the frame repairs are FIXED as recorded in the wave history.

### 4. Fonts and assets

- **What:** Loads (at the head of the code body, candidate L27–32): the candidate adds the Noto Sans JP `@import` (JPFONT-LOAD) ahead of the original's kept Google Fonts loads (Noto Sans KR, Nanum Gothic Coding). Three of the original's head-module loads are deleted with that module: the Typekit CSS (original L4, serving the franklin-gothic / titling-gothic / hypatia families) and the two `http://` font CSS imports from xcninety.github.io (original L6–7, serving IBMPlexSansKR and Cafe24Ohsquareair). Those family names survive only inside the `:root:lang(ko)` stacks (candidate L36–39), which do not match on the JP site, so nothing reader-visible on scp-jp depends on the deleted loads; the JP rendering takes the BHL base fonts plus Noto Sans JP. Assets: six image URLs inherited with the theme's BHL layering, all pointing into `theme:the-foundation-theme`'s files on the EN wiki (five `https://scp-wiki.wikidot.com`, one `http://www.scp-wiki.net` at candidate L187); the port's change to them is only the colon encoding of section 8. The base CSS also keeps two `-webkit-mask-image` lines naming the old BHL host (nu-scptheme.github.io/.../logo.svg, candidate L298–299; the OLD-BHL-KEPT disposition stub).
- **Why:** P7/T5 with KB-16 (the font load gap): a JP font load is added because the theme's stacks are Latin/Korean-only. P5/KB-17 for hosts: the six foundation URLs and the two mask lines are the *base family's* assets carried inside the inherited CSS, not this theme's own files; the ledger treats such kept base lines as class (ii) posting matters, and fix lanes leave old-bhl lines by rule.
- **Verify:** Read candidate L27–32 against original L4–8; `grep -n 'the-foundation-theme' candidate.txt` — six lines, colon-encoded; `grep -n 'nu-scptheme' candidate.txt` — L298–299 only.
- **Disposition:** Font load applied; the deleted loads standing (their families are lang(ko)-scoped); the six asset URLs and two old-bhl lines DISPOSITIONED (class (ii)).

### 5. Header, sidebar, and site furniture

- **What:** No JP furniture adaptation was made, and the bytes say why none was needed in the port's terms: the candidate overrides no header variable outside the inherited `:root:lang(ko)` block, where `--header-title` ("확보,격리,보호", candidate L41) and `--header-subtitle` ("재단 대한민국 지역사령부 제21K 기지", candidate L1018) keep the original's Korean strings, scoped to lang(ko) and therefore not reader-visible on the JP site. The sidebar arrives through the repointed bhl-dark-sidebar component (section 2). The render row's sidebar item ("sidebar-not-opening") is a render-record item, carried in section 11, not a furniture edit.
- **Why:** P9/T6 variables were checked and are inherited-only; header and title language is ruling-2 territory (out of scope for migration correctness) in any case, and the lang(ko) scoping means the strings cannot surface on scp-jp.
- **Verify:** `grep -n -- '--header-' candidate.txt` — the two lang(ko)-scoped lines above, no others.
- **Disposition:** Standing; the render row's sidebar reading is recorded in section 11.

### 6. Text translation

- **What:** This page is a code page; its prose is one usage section and the exhibit labels, and all of it is translated: the usage heading (original 사용 방법 → candidate 使用方法， L17), the usage sentence, and the collapsible labels （ソースコードを表示 / 閉じる, candidate L25). The classifier's single TRANS-UNANCHORED block is that prose region (inside B11's span). Inside the CSS body, reader-visible text is limited to the lang(ko)-scoped header strings of section 5; the body's Korean survives only there and in the credit block's title fields (section 1), both recorded. R1 in-CSS text: the candidate adds one comment banner, `/* ===== bulgunae ===== */` (candidate L28, section 10); no other comment translation occurs, because the inherited body's comments travel verbatim. R5 glyph-form conversion: none (the source is Korean; retained strings are quotations or lang-scoped).
- **Why:** P10 for the prose; KB-18 for reader-visible strings — the lang(ko) scoping is the fact that keeps the retained Korean strings out of KB-18's scope on this site.
- **Verify:** Read candidate L17–25 against original L1279–1283; a Hangul scan of candidate.txt returns the credit fields, the lang(ko) block, and no prose.
- **Disposition:** Standing (the port itself); the credit title wording is the recorded T4 item of section 1.

### 7. Links

- **What:** One prose link exists: the credit block's source link (candidate L14), naming scpko.wikidot.com/theme:bulgunae — the original's recorded host, which serves the page. The host check the jiha exemplar taught (candidate host vs recorded host, probe on divergence) finds no divergence and no broken link. The usage example's include is an include, not a link (section 2); the CSS asset URLs are section 4.
- **Why:** P11 is satisfied by the serving original on its recorded host.
- **Verify:** `grep -n 'wikidot.com' candidate.txt` — the source link plus the section-4 asset lines.
- **Disposition:** Standing; no link item.

### 8. Structure

- **What:** Two structural facts. (1) The consolidation: three module-CSS blocks become one code body plus a tail delivery (section 3) — a deviation in form from localize.md's closing rule, and the campaign's own applied-CSS convention for such themes; variable names, selectors, and rule order inside the body are preserved (body similarity 0.99), and the six KB-01 colon encodings are the only in-body text edits beyond the font head: the `theme:the-foundation-theme` path colon is percent-encoded in all six inherited asset URLs (blocks B4–B9's second label; e.g. original L163 → candidate L187), because an unencoded colon in a URL path is the class (i) colon defect. (2) **The dropped module, restored:** the original's second module (L993–1010 — `:root` rating-module color variables, a `#page-content > div:nth-child(1)` padding rule, and a `.page-rate-widget-box` gradient rule) had no counterpart anywhere in the candidate as built (block B10, which the classifier labels DELIVERY-MOVE; no moved copy existed). No record named the drop: the T4 row does not mention it, the ledger has no item for it, and the render row records no rate-widget finding. The repair has since landed (record FIX-BULGUNAE.md in the campaign record, R/review-scout/; canonical commit 9351aec): the block is restored verbatim (byte-identical to original L993–1010) as a second `[[module css]]` at candidate L1283–1300, sitting immediately after the candidate's existing delivery module and before the interwiki-style frame — the mirror placement in the candidate's consolidated structure, after the base include and the imported exhibit, so the theme's rating overrides win over the JP BHL base's defaults exactly as the original's second module overrode the EN base's. Its contents are the `:root` assignments of --rating-module-text-color and --rating-module-button-color to var(--swatch-menutxt-light-color), the #page-content > div:nth-child(1) padding rule (0.75rem), and the .page-rate-widget-box margin/background linear-gradient rule. The classifier's one EXHIBIT-RESTRUCTURE primary (B11) is not this: it is the tail reorganization (module close, sidebar relocation, gate placement), and the exhibit census is otherwise clean — the code exhibit and the usage section are present on both sides.
- **Why:** The closing rule and R3 exist so that a consolidation cannot silently absorb a deletion; KB-01 names the colon encodings. For the dropped module, this package stated the fact and the limits of the evidence: the rules it carried style the rate widget, which on a BHL theme is base-provided furniture, and the render checks that ran the candidate against the original recorded no rate-widget divergence — but subsumption by the JP base could not be proven from the two files in this package, so the item was flagged, not dispositioned. The subsumption question is now answered by the base's bytes: theme:highlighter-bhl-jp sets --rating-module-button-color to its own default var(--black-monochrome), and neither the base nor sigma-10-jp carries the gradient or the padding, so the dropped block was the theme's override, not a duplicate — subsumption is disproven, and the restore at candidate L1283–1300 was the correct repair.
- **Verify:** `grep -n 'page-rate-widget-box\|rating-module' candidate.txt` returns the restored block at candidate L1283–1300; read original L993–1010 against it (byte-identical); compare the module/code boundaries via `grep -n '\[\[module\|\[\[code' original.txt candidate.txt`.
- **Disposition:** Consolidation and colon encodings standing; the dropped module was FLAGGED (unrecorded deletion, flagged here and in the lane report for the coordinator) and has since been repaired by the verbatim restore at candidate L1283–1300 (9351aec).

### 9. Formatting only

- **What:** None. The classifier finds no whitespace-only block and no re-indentation (0 and 0), so the R7 follow-up-diff hazard is not triggered; the consolidation preserved the body's internal formatting.
- **Why:** Formatting churn is disclosed as its own class so it is never mistaken for a semantic change.
- **Verify:** The classifier's section-9 counts in classification.json.
- **Disposition:** None required.

### 10. Porter annotations

- **What:** One annotation: the comment banner `/* ===== bulgunae ===== */` at the head of the code body (candidate L28), inserted between the added Noto Sans JP load and the original's first kept load; it has no original counterpart and marks where the port's head edits end and the inherited body begins. There are no `[!-- ... --]` translator notes and no editor lines; the two translator-visible additions besides the banner are the credit block and the frame, which are furniture, not annotations. The skeleton's class summary is the record that no ANNOTATION signature fired — the banner rides inside B3's delivery block, which is why it is listed here from the bytes.
- **Why:** R2: porter-added text is part of the change record, and this banner is the in-file marker of the consolidation boundary.
- **Verify:** Read candidate L26–32.
- **Disposition:** Standing.

### 11. Dispositions and exceptions

- **What:** Four items, each with its ground. (1) T1's ten errors, all class (ii) posting-procedure: hotlink ×6 (the inherited foundation-theme asset URLs of section 4 — base-family files, re-hosted or rewritten at posting, never "fixed" in the candidate), old-bhl ×2 (the mask-image lines of section 4; fix lanes leave old-bhl by rule), http ×1 (candidate L187, the one foundation URL still on http://www.scp-wiki.net), pseudo-ref ×1 (the candidate's own draft-host local--code line, section 3). (2) The render row's items, recorded as environment or triage, not charged as candidate defects: the page's sidebar-not-opening reading; the candidate-own runtime hosts recorded verbatim (nu-scptheme.github.io and the scp-wiki hosts — the same lines as item (1), seen from the render side); the sample's credit-modal errors (KB-32: the preview form has no modal mechanism, ruling 5); the page-overflow 493–500px@320/375 reading; and T3's note that the custom red/black header lettering collides and is partly illegible at 375/320 in both engines, which the row itself qualifies as possibly intended stylization. (3) T4's one display-affecting finding, the credit title's untranslated Korean (section 1), which the ledger §(c3) line closes as P3 fields FIXED with the wording standing as recorded （軽微）. (4) **Flagged, not dispositioned — since repaired:** the dropped second module (section 8) — no record dispositioned it, and this package did not invent one; it was reported to the coordinator with its evidence. The repair has since landed (9351aec): the block is restored verbatim at candidate L1283–1300, and the subsumption question is answered in section 8 (disproven by the base's bytes). The theme's determination is PASS; items (1)–(3) do not re-open it, and item (4) is now a closed documentation flag on a discrepancy the sweep did not record.
- **Why:** A disposition is a decision with grounds (AGENTS.md §3 classes (i)/(ii)/(iii); the named KB entries), not an omission; an item with no grounds is flagged, never dressed as a disposition.
- **Verify:** Each item names its deciding record above; item (4)'s evidence is the grep in section 8.
- **Disposition:** DISPOSITIONED (items 1–3); item 4 was flagged with evidence and has since been repaired (9351aec).

### 12. Verification

- **What:** (a) T1 source check (T1-ROWS row 238): exit 1, 10 errors / 0 warns / 7 infos (hotlink ×6, old-bhl ×2, http ×1, pseudo-ref ×1); every error is class (ii); there is no class (i) error. (b) T2/T3 render (RENDER-ROWS-2, lane RENDER-S2-H (KO2)): FINDINGS, the items of section 11(2), all dispositioned or recorded as triage; engine coverage as run by the lane, not separately caveated in its row. (c) T4/T5 (LOCALIZE-ROWS row 254): FINDINGS jointly, display-affecting findings 1 (the credit title, section 1); the ledger §(c3) line records the theme's P3 outcome as FIXED by the credit waves. (d) This package is self-verifying: `python3 review/build_review.py --check` regenerates diff.md and the verdict stamp from the two byte-faithful copies in this directory and compares. Counts in this README are the generator's (difflib, autojunk off): +65/−44 in 12 change blocks; the GNU-diff count of the same pair is 101 changed lines, and the difference is alignment choice, not content.
- **Why:** Verification claims name the cheapest deciding check and its result, not a general assurance.
- **Verify:** Re-run the checker on `pages/theme:bulgunae-jp.txt` and `python3 review/build_review.py --check` in this repo.
- **Disposition:** PASS (GOSIGN2-LEDGER (b) row 255; go-sign, COMPLETION-REPORT §10), with the section-8 flag now closed by the restore in 9351aec.

## Per-theme record

### The usage example's posting name — completion reverted by a later landing, then re-applied (closed)

The usage example at candidate L19 as built read `> @@[[include :scp-jp:theme:bulgunae]]@@`: the porting wave's repoint changed the branch prefix from `:scpko:` but left the plain name, so the example named a page that does not exist on scp-jp (the campaign's settled rule for usage examples, AGENTS.md §6). The usage-example population sweep completed the reference to `:scp-jp:theme:bulgunae-jp` (sweep report SWEEP-USAGE.md in the campaign record, R/review-scout/; canonical commit b5cb724), one of its 287 repairs across 157 candidates. That completion was then lost: the rating-module restore (commit 9351aec) was landed from a worktree whose base predated the sweep, and its whole-file copy carried the pre-sweep L19 back over the sweep's line — the same landing-collision shape the campaign had already met and repaired for ared (13b5725) and for anniversary, asagao, and atlas-maniacus (780e048), unnoticed here because the restore's own diffstat matched its report. A full-population re-check of all 287 sweep repairs against the current canonical bytes (refresh-2, 2026-11-17) found this line the only one standing reverted; this package recorded the item as OPEN pending re-application. That re-application has now landed: canonical commit e217dbd restores the single `-jp` insertion at candidate L19 (`> @@[[include :scp-jp:theme:bulgunae-jp]]@@`), the same one-line repair as the original sweep. The item is therefore CLOSED; this package documents the corrected candidate, and its stamp reads STALE against the pre-repair verdict, by design.

## Change set outside the two diffed files

The diff covers two files; the port's record is one file larger. `pages/theme-decoration-sample-bulgunae-jp.txt` is the decoration sample the render checks ran against (its findings are the sample half of section 11(2)); it belongs to this theme's record but carries no port change of its own to explain here. The original-side sample `pages/theme-decoration-sample-bulgunae.txt` is the campaign's mirror-side fixture, likewise outside the port. There are no companion fragments and no inbound-link repairs in other candidates for this theme; the base include's target (theme:black-highlighter-theme-jp) is a shared base port with its own record, not part of this theme's change set.

## License and attribution

- **Title:** 불구내 테마
- **Author:** AXOL0TL
- **Source:** https://scpko.wikidot.com/theme:bulgunae — revision 5
- **License:** Creative Commons Attribution-ShareAlike 3.0 (CC BY-SA 3.0) — license deed: https://creativecommons.org/licenses/by-sa/3.0/
- **Adaptation:** This package holds a Sigma-10 migration port of the work; changes were made. See "Summary" and "Standing sections" in this README for what changed and why. Translator: AI (Muse and its delegated agents), per the campaign's standing attribution rule.
