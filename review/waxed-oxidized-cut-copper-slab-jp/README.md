# Review package — theme:waxed-oxidized-cut-copper-slab-jp (CN → JP port)

<!-- BEGIN GENERATED VERDICT STAMP — do not hand-edit; regenerate with review/build_review.py -->
## Verdict stamp
- Theme: theme:waxed-oxidized-cut-copper-slab-jp — origin CN, population #244 [GOSIGN2-LEDGER (b) row 244]
- Overall: STALE — candidate file changed since the verdict was computed (verdict against 435a6bb-era content, file sha256 now bbf49f93e657f4ce6aec9f88d3d14aa4d3c9a3401eaaa14c51560b16b64e4770); the verdicts below were computed against that pre-change file, and the record verdict stands: a candidate revised through the campaign's recorded repairs is posted like a PASS row, with the change recorded in its package
- T1 (source check): FINDINGS (classified) — baseline 2026-11-16: exit 1, 9 errors / 3 warns / 1 info (hotlink×8, pseudo-ref×1); standing classes dispositioned in register c1 [T1-ROWS row 209; GOSIGN2-LEDGER (b) row 244]
- T2/T3 (render, combined verdict): FINDINGS — [combined T2/T3] report `FINDINGS` — page-overflow 445px@320/375 on page and sample + runtime-hotlink site-theme chain + candidate hosts ah-sandbox.wdfiles.com, ah-sandbox.wikidot.com, bhl.scpwikicn.com, hormress.github.io, nu-scptheme.github.io, scp-wiki.wikidot.com; sample credit-modal (preview-form); T3 re-run, no new screenshot-grounded visual finding; chromium-only coverage (no WebKit verdict). [RENDER-ROWS-G (CN17)]
- Engine coverage: chromium-only, both pages (no WebKit verdict) [RENDER-ROWS-G row, findings cell]
- Credit modal: sample credit-modal errors dispositioned preview-form (credit:start-preview has no modal mechanism; GOSIGN-TESTS T2 amendment, 2026-11-16) [RENDER-ROWS-G (CN17)]
- T4 (localize patterns + follow-up): FINDINGS — display-affecting findings: 1 [LOCALIZE-ROWS row 243, source LOCALIZE-S2-E]
- T5 (translation text): FINDINGS — the source reports judge T4/T5 jointly; one verdict word covers both [LOCALIZE-ROWS row 243]
- FIX5 re-judgement: none — no OPEN items at the ledger determination [GOSIGN2-LEDGER (b) row 244]
- Computed against: canonical commit f4488f2d2948824238a2d06479f104f4aab0cf5d; candidate file pages/theme:waxed-oxidized-cut-copper-slab-jp.txt sha256:bbf49f93e657f4ce6aec9f88d3d14aa4d3c9a3401eaaa14c51560b16b64e4770; record: GOSIGN2-LEDGER.md + GOSIGN2-LEDGER-SUPPLEMENT.md as of the FIX5 head 435a6bb
<!-- END GENERATED VERDICT STAMP -->

## Status

| | |
|---|---|
| Verdict | **PASS** — passed at the ledger determination; this theme had no OPEN items and no §(e) register entry (GOSIGN2-LEDGER (b) row 244) |
| Standing items | **DISPOSITIONED** — T1 hotlink ×8 + pseudo-ref ×1 (class (ii), section 11); the render row's items (overflow at 320/375, KB-33/KB-34; candidate hosts on the runtime chain, KB-40 / class (ii)); T4 display-affecting 1. **Three items are flagged by this package beyond the ledger's record: the original head module's two margin rules are absent from both the candidate and its base candidate; three documentation prose links name pages that do not exist on scp-jp while the same pages' include examples were correctly repointed; and the breadcrumb trail lost its `pseudocrumbs` wrapper (per-theme record).** The verdict stamp reads STALE because the candidate changed after the verdict in the usage-example sweep commit b5cb724 (section 12) |
| Go-sign basis | COMPLETION-REPORT.md §10 (go-sign issued; 81 FIXED / 26 DISPOSITIONED / 0 OPEN across the sweep) |
| Named exception | None for this theme (the sweep's single named exception is theme:amethyst-v2, which has no candidate) |

## Provenance

| | Original | Candidate |
|---|---|---|
| Page | theme:waxed-oxidized-cut-copper-slab | theme:waxed-oxidized-cut-copper-slab-jp |
| Wiki | scp-wiki-cn.wikidot.com | SCP-JP Sigma-10 candidate (canonical repo) |
| Reference revision | 2 (first translation; the candidate's credit block records 初訳時参照リビジョン: 2) | — |
| Source of this copy | Campaign cache `gosign2-lanes/lane-oc-gs-localize-s2-E/orig-waxed-oxidized-cut-copper-slab.txt`, via the mirror store (class COPY, hash-verified against review/sources.tsv) | Canonical file `pages/theme:waxed-oxidized-cut-copper-slab-jp.txt`, copied at worktree HEAD e907bdd |
| Lines / bytes | 735 lines / 21,575 bytes | 747 lines / 23,626 bytes |
| SHA-256 | ce69d40932d753f168aca221382482186df14dc9e88bdbf97fbd638ea85db41d | 9c97f71d0c881a748e672fb13c377a12c5bcc93ce9bd68d24484ba7fa4d1965b |

Wave history: the candidate was created by the Stage 2 CN17 integration (2e202fc, the LOCALIZE-S2-E wave's port), then touched by rework2-p1 (95fd1d1 — the wave that restored missing base deliveries across 9 DROP pairs; this theme's base include is its work, section 2), by FIX-CREDIT-D (1869877), and by the usage-example sweep (b5cb724 — whose three repairs to this file are the subject of the per-theme record). Provenance note (sources.tsv, class K5a-i): the original is recorded as superseded upstream since the reference revision, with a follow-up diff artifact in the campaign record — that artifact's actual content is reported in section 12, because it does not say what the note implies.

## Summary

A Minecraft-oxidation theme layered over the same author's `theme:parallel`, whose port consolidates a genuinely scattered original — base CSS imported from the author's GitHub Pages, a `@property` registration snippet hidden in the documentation, and a main CSS module that *self-imports* the snippet's code block — into the campaign's single delivered block, with the base's JP candidate included live at the head. The consolidation is done correctly (the `@property` ruleset is appended to the delivered block; the census holds), and the exhibits' five-stage progression is preserved with a subtlety the per-theme record exists to state: two of its stage references are *deliberately* left in plain form because those stages are fictional. Against that care, the package flags three plainer misses: the head module's two margin rules (`#page-content > h1/h2` top margins) survived in neither the candidate nor the base candidate; three prose links in the documentation still name the plain `theme:copper` / `theme:bedrock` / `theme:parallel` pages that do not exist on scp-jp, although the include examples on the same pages were repointed to the -jp candidates; and the breadcrumb trail at candidate L16 lost the `[[div class="pseudocrumbs"]]` wrapper the original wraps it in. Measured churn (the generator's difflib count, autojunk off): +165/−164, 329 changed lines in 63 change blocks / 4 diff sections; a GNU-diff count gives 240 changed lines (+126/−114). This package changes nothing.

## Class summary

Auto-classification by review/classify_hunks.py (signature table 2026-11-17.1): 63 change blocks — 34 specific (54.0%), 28 heuristic (44.4%), 1 residue (1.6%), 0 skipped. Pattern citations below name the KB entry; the patterns/ tree state cited throughout is commit 9c5e9079afb01d30cb9fc4ef9d714e5591eb2ffa.

| Label | Blocks |
|---|---|
| TRANS-UNANCHORED | 32 |
| TRANSLATION-ANCHORED | 18 |
| COMPONENT-SWAP | 5 |
| DELIVERY-MOVE | 5 |
| ESCAPED-INCLUDE | 5 |
| INCLUDE-REPOINT | 5 |
| SELF-DELIVERY | 3 |
| DRAFT-HOST | 2 |
| EXHIBIT-RESTRUCTURE | 2 |
| GLYPH-FORM | 2 |
| IFTAGS | 2 |
| ANNOTATION | 1 |
| CREDIT-PREVIEW | 1 |
| CREDIT-PROSE | 1 |
| LINK-REPOINT | 1 |
| RESTORATION | 1 |
| TASL-FIELDS | 1 |

Adjudication of the heuristic mass: the 28 heuristic blocks are documentation translations (32 unanchored blocks across tiers — the progression exhibits repeat near-identical lines, which is why the mass looks repetitive) and the consolidation's CSS blocks. The five-of-each COMPONENT-SWAP / INCLUDE-REPOINT / ESCAPED-INCLUDE counts are the progression's stage examples (per-theme record), not five separate component decisions. The two EXHIBIT-RESTRUCTURE primaries adjudicate against the census in section 8. The one residue block (the gate-close boundary) is in the appendix.

## Standing sections

### 0. Header and provenance frame

- **What:** Theme theme:waxed-oxidized-cut-copper-slab-jp; original theme:waxed-oxidized-cut-copper-slab on scp-wiki-cn at reference revision 2; candidate `pages/theme:waxed-oxidized-cut-copper-slab-jp.txt`. Provenance route: derived from the original at the reference revision by the LOCALIZE-S2-E wave (sources.tsv kind: standard, with the K5a-i note of the Provenance table). Base: `theme:parallel`, a BHL-family theme by the same author (Dr Hormress). Topology frame (the original): gate at L1; a head module (L2–13) importing the base CSS from the author's GitHub Pages plus two rules of its own (flag A); documentation; a hidden div holding a `[[code]]` snippet (L234–240) with the `@property --rotangle` registration; the gate closes ~L243; the main CSS as a *live module* (L245–735) whose head imports Cutive and the page's own `code/1` — so the hidden snippet is delivered in the original, by self-import. The candidate: live base include at L1, documentation, one code block (L240–736) with the `@property` ruleset appended at its end, tail delivery.
- **Why:** Section 0 declares the route and the full topology, because the consolidation claim of section 3 and flag A are both topology facts.
- **Verify:** The sources.tsv row for waxed-oxidized-cut-copper-slab-jp; `sha256sum original.txt` against the Provenance table.
- **Disposition:** Standing (the route itself).

### 1. Credit and attribution

- **What:** The candidate installs the preview credit block at its head with the eight ruling-3 fields; its author field names Dr Hormress, the author the original's own statements support (he is also the base theme:parallel's author, which the documentation states). The source-link field names the recorded host (scp-wiki-cn), so the host check passes with no probe needed. The original's `[[module rate]]` is deleted; an empty `[[>]]` pair remains where it stood — a vestige, recorded in section 8 rather than silently passed over.
- **Why:** P3/T1 and ruling 3; the field-versus-banner check passes in both directions.
- **Verify:** Read the credit block at the candidate's head; the empty `[[>]]` pair is findable by `grep -n '\[\[>\]\]' candidate.txt` in the docs head region.
- **Disposition:** FIXED (ledger §(c3) class outcomes: credit fields FIXED by the credit waves); no credit item is flagged for this theme.

### 2. Includes and components

- **What:** The base include stands live at candidate L1: `[[include theme:parallel-jp]]`, in bare same-wiki form — added by the rework2-p1 wave (95fd1d1), which restored base deliveries that the first port had dropped across 9 theme pairs; the classifier's RESTORATION label sits on this block, correctly. It replaces the original's GitHub-Pages `@import`s of the base CSS (section 3). The credit pair (section 1) and the tail frame (section 3) complete the live set. The remaining include-shaped lines are the exhibits' usage examples — the five-stage progression, whose repoints (INCLUDE-REPOINT ×5, ESCAPED-INCLUDE ×5) are the per-theme record's subject: bedrock, copper, and parallel examples name the real -jp candidates; the two intermediate stages keep their plain names on purpose.
- **Why:** P1 (KB-15) and KB-01's family: a dependent theme imports the base's JP candidate delivery — here by live include, the restored form. The bare form of the include is the class (ii) population form.
- **Verify:** Candidate L1; the progression examples are candidate L40–72.
- **Disposition:** Applied (the base restoration is the rework wave's recorded work).

### 3. Delivery and code loading

- **What:** The consolidation: the original delivers three pieces — the base CSS by GitHub-Pages import (head module), the `@property` snippet by the main module's self-import of `code/1`, and the main CSS as a live module. The candidate delivers one block: the main CSS as `[[code]]` (candidate L240–736, headed by the porter comment of section 10) with the `@property --rotangle` ruleset appended at its end (candidate L731–735), served by a tail module plus interwiki-style frame naming `local--code/theme%3Awaxed-oxidized-cut-copper-slab-jp/1`. Census check: the original has exactly one `[[code]]` block (the snippet) and the candidate exactly one (the consolidated block), so the /1 address names the block that holds the CSS — correct, and the snippet's content is inside it, at its end, where the differ's residue block B57 marks the gate boundary moving. The base is delivered by the live include of section 2, not by this block. DELIVERY-MOVE ×5 records the topology change.
- **Why:** P6/T3 and the conversion class: a live module cannot be framed, and a self-imported snippet is consolidated into the block it serves. The census and the `@property` placement are the deciding checks, and both pass.
- **Verify:** `grep -n '@property' candidate.txt` (L731–735, inside the code block); count the `[[code]]` blocks (one).
- **Disposition:** DISPOSITIONED (draft-host lines, class (iii)); the consolidation itself is applied and verified. Flag A (the head module's two rules) is recorded in section 8 — it belongs to the head module, not to this delivery.

### 4. Fonts and assets

- **What:** The font variables localize: "Noto Sans SC" → "Noto Sans JP" in `--mono-font`, `--header-font`, and `--body-font`. Cutive is imported at the code block's head (candidate L242), as the original imported it. 'JetBrains Mono' is named in a stack but imported nowhere — *original-identical* (the original names it the same way, and its delivery, if any, is the base chain's): recorded so the fact is known, and not flagged, because the candidate neither adds the name nor claims it in a specimen (the contrast with the walk-in package's flag is exactly the specimen claim). `--header-logo` keeps the original's sandbox host (`https://ah-sandbox.wikidot.com/local--files/pictures/PixelSCP_3D.svg`) — kept foreign delivery, class (ii). The image-block example (candidate L147) keeps `name=https://bhl.scpwikicn.com/img/logo.svg` unchanged with only its caption translated — original-state delivery, class (ii).
- **Why:** P7 for the variable localization (the faces named are the base chain's to load, as in the original); the kept hosts are P5's class (ii) form (sandbox and author hosts the posting procedure owns).
- **Verify:** `grep -n -- '--body-font\|--header-font\|--mono-font' candidate.txt`; candidate L242 for the Cutive import.
- **Disposition:** DISPOSITIONED (kept hosts, class (ii)); the variable localization is applied.

### 5. Header, sidebar, and site furniture

- **What:** One rendered `content:` string remains in Chinese in the delivered CSS: "控制，收容，保护" (candidate L436) — the Foundation motto, in-fiction text standing under the ledger's ruling-2 family for this theme's row charges, recorded and not flagged. The breadcrumb trail at the documentation head is this theme's signature furniture, and it carries flag C (section 8): the trail's links stand at candidate L16 without the `[[div class="pseudocrumbs"]]` wrapper the original wraps them in.
- **Why:** P9 / ruling 2 for the motto; the wrapper is a structure fact, adjudicated in section 8.
- **Verify:** Candidate L436 for the string; candidate L16 against the original's trail region for the wrapper.
- **Disposition:** DISPOSITIONED (the motto, ruling 2 family); the wrapper is FLAGGED (minor, section 8).

### 6. Text translation

- **What:** The documentation and exhibits are translated throughout (18 TRANSLATION-ANCHORED blocks, 32 TRANS-UNANCHORED — the progression's repeated stage lines), with GLYPH-FORM ×2 localizing glyph forms in samples. The specimens are the theme's jokes and are translated as jokes: the "empty" tab's 蛋糕是个谎言 becomes ケーキは嘘です ("the cake is a lie"); the body specimen admits 本文フォントは結局パラレル既定と同じです ("the body font ends up the same as Parallel's default anyway"); the mono specimen confesses 等幅フォントの名前は私も忘れました ("I've forgotten the mono font's name too"). The header specimen names "Noto Serif JP / Cutive" as the original named its pair. These are faithful translations of the original's specimen text, recorded here because specimens in this batch are claims in other packages — here they are jokes in both files, and the joke is the content.
- **Why:** P10 and KB-18; the discrimination (joke versus claim) is made from the original's own text, not from charity.
- **Verify:** The tabview specimens in the candidate's documentation against the mirror's.
- **Disposition:** Standing (the port itself).

### 7. Links

- **What:** The credit source link (section 1) names the recorded host. **Flag B (minor):** three documentation prose links name pages that do not exist on scp-jp — `[[[theme:copper|銅テーマ]]]` in the breadcrumb trail (candidate L16), `[[[theme:bedrock|岩盤]]]` in the intro (candidate L23), and `[[[theme:parallel|パラレル]]]` in the size note (candidate L57) — while the *include examples* in the same documentation were correctly repointed to `theme:bedrock-jp`, `theme:copper-jp`, and `theme:parallel-jp`, which exist as candidates. The prose links were simply missed by the repoint pass: on the posting wiki they will resolve to nonexistent pages (and offer page creation) where the -jp pages are meant. The classifier's one LINK-REPOINT block (B4) spans this same documentation head (original L14–16 → candidate L15–26): the repoint pass demonstrably touched this block — its include examples were repointed — and still left the three prose links plain.
- **Why:** P11: a prose link names the JP counterpart where one exists; here counterparts exist and the examples prove the porter knew them. This is not the per-theme record's fictional-stage case — bedrock, copper, and parallel are real stages with real candidates.
- **Verify:** Candidate L16, L23, L57 against the name sets (`pages/theme:bedrock-jp.txt` etc. exist; no `theme:bedrock` page exists on scp-jp).
- **Disposition:** **FLAGGED** (minor; the three prose links, per-theme record).

### 8. Structure

- **What:** The localize.md closing rule holds for the delivered body, with three recorded exceptions. **Flag A:** the original head module's two rules — `#page-content > h1 { margin-top: 3rem; }` and `#page-content > h2 { margin-top: 2rem; }` (original L6–12, inside the module at L2–13) — are absent from the candidate *and* from the base candidate (`review/parallel-jp/candidate.txt`, searched: no `#page-content > h1`). The candidate's `--main-content-top-margin: 3rem;` (candidate L276) is a base *variable*, a different mechanism from the dropped rules — it does not subsume them, because nothing in either file applies that variable to `h1`/`h2` margins in the module's place. **Flag C (minor):** the breadcrumb trail (candidate L16) lost its `[[div class="pseudocrumbs"]]` wrapper; the trail's link forms otherwise mirror the original (anchor links for stages 1/3/4, a real link for copper — which is flag B's first locus). Two vestiges, recorded rather than flagged: an empty hidden div remains where the `@property` snippet was extracted from the documentation, and the empty `[[>]]` pair of section 1 remains where the Rate was deleted. The two EXHIBIT-RESTRUCTURE primaries adjudicate against the census: the progression exhibits, tabview, and code exhibit are present on both sides in the same order.
- **Why:** R3 and the silent-drop rule, with the subsumption check the standing lessons require (a base default is not the theme's override — here checked against the base candidate's actual text, not assumed).
- **Verify:** Original L2–13 against `grep -n '#page-content > h1' candidate.txt` and the same grep on the base candidate (both absent).
- **Disposition:** **FLAGGED** (flags A and C, per-theme record); the vestiges are standing disclosures.

### 9. Formatting only

- **What:** None at block level: no WS-ONLY block and no pure re-indent block (reindent_blocks 0) — the consolidation's blocks all carry content changes.
- **Why:** R7's ground for "none".
- **Verify:** classification.json's label counts for this package.
- **Disposition:** None required.

### 10. Porter annotations

- **What:** Two annotation loci. The wave marker comment `/* ===== waxed-oxidized-cut-copper-slab ===== */` heads the candidate's code block (candidate L241) — porter-added. And an `[!-- --]` note at candidate L84 (the switch note: ここまでがスイッチです — "this is the whole switch; copy it anywhere in the page") is the *original's own* annotation carried in translation — inherited text, localized, not porter-added; the classifier's ANNOTATION block is one of these, and both are recorded here with the discrimination.
- **Why:** R2, with the same discrimination as the turbo-vision package's L14 comment: added versus inherited.
- **Verify:** Candidate L241 and L84.
- **Disposition:** Standing.

### 11. Dispositions and exceptions

- **What:** The ledger items: (1) T1's nine errors — hotlink ×8 (the sandbox, GitHub-Pages, and author hosts of sections 3–4) and pseudo-ref ×1 — all class (ii). (2) The render row's items: overflow 445px at 320/375 (KB-33/KB-34 family); the candidate hosts appearing on the runtime chain (ah-sandbox.wdfiles.com, ah-sandbox.wikidot.com, bhl.scpwikicn.com, hormress.github.io, nu-scptheme.github.io, scp-wiki.wikidot.com — KB-40 environment layer plus the class (ii) foreign/sandbox delivery, KB-41/KB-54 family). (3) T4 row 243: display-affecting 1. (4) The ledger §(c3) class outcomes for the LOCALIZE-S2-E rows (header language ruling 2; asset hosts class (ii); credit fields FIXED) and the population-check row (LEDGER-POPULATION-CHECK row 23). **Flagged by this package:** flag A (the two margin rules), flag B (the three prose links), flag C (the pseudocrumbs wrapper). None is covered by a ledger disposition — the class outcomes address wording and hosts, not rule survival or prose-link targets — and none disturbs the verdict: all three are small candidate repairs for the coordinator to land with a package refresh. The two intermediate-stage references of the per-theme record are *not* flags; they are the sweep's recorded decision, and this package endorses it with the reasoning stated there.
- **Why:** A disposition is a decision with grounds; undispositioned misses are reported as flags, and deliberate decisions are reported as decisions — the two must not be blurred in either direction.
- **Verify:** Each item names its deciding record above; the flags' evidence is the per-theme record.
- **Disposition:** DISPOSITIONED (items 1–3); **flags A, B, and C are FLAGGED**.

### 12. Verification

- **What:** (a) T1 source check (T1-ROWS row 209): exit 1, 9 errors / 3 warn / 1 info — hotlink ×8 and pseudo-ref ×1, all class (ii); no class (i) error. (b) T2/T3 render (RENDER-ROWS-G, CN17): FINDINGS — the items of section 11(2). (c) T4/T5 (LOCALIZE-ROWS row 243): FINDINGS, display-affecting 1. (d) The K5a-i follow-up artifact (`gosign2-lanes/lane-oc-gs-localize-s2-E/diff-waxed-oxidized-cut-copper-slab-from2.txt`, read for this package): a six-line record whose content is "scp-wiki-cn:theme:waxed-oxidized-cut-copper-slab rev2 → rev2 変更： なし" with an empty intervening-revision table — it records **no upstream change after the reference revision**, against sources.tsv's "superseded upstream" wording; the artifact's bytes are followed here and the tension is reported in the batch report. (e) This package's own checks: the delivery census and `@property` placement (section 3), the base-candidate grep behind flag A (section 8), and the name-set check behind flag B (section 7). (f) This package is self-verifying: `python3 review/build_review.py --check` regenerates diff.md and the verdict stamp from the two byte-faithful copies in this directory and compares; the stamp reads STALE because the candidate changed after the verdict in the sweep commit b5cb724 (the three self-reference repairs of the per-theme record). Counts in this README are the generator's (difflib, autojunk off): +165/−164 in 63 change blocks / 4 diff sections; the GNU-diff count of the same pair is 240 changed lines.
- **Why:** Verification claims name the cheapest deciding check and its result, including reading the artifact instead of its description.
- **Verify:** Re-run the checker on `pages/theme:waxed-oxidized-cut-copper-slab-jp.txt`; read the follow-up artifact at the path in (d).
- **Disposition:** PASS (GOSIGN2-LEDGER (b) row 244; go-sign, COMPLETION-REPORT §10).

## Per-theme record

### The Minecraft progression, and why two of its references keep their plain names

The theme's exhibits walk a Minecraft oxidation progression, one stage per example: **bedrock → copper → cut-copper-slab → oxidized-cut-copper-slab → waxed-oxidized-cut-copper-slab** (the theme itself). Each stage's usage example includes that stage's theme over the previous one, so the documentation is a five-step chain of includes, and the theme's own name in the final steps is assembled from `@@##color|segment##@@` spans, which the candidate preserves segment for segment.

The usage-example sweep (review-scout/SWEEP-USAGE.md) repaired this theme's three self-references: the waxed self-name in the three final-step examples (candidate L54, L61, L72) gained `-jp` on its final color-markup segment, becoming `-slab-jp`. It deliberately left the two intermediate-stage references untouched — `theme:cut-copper-slab` (candidate L40) and `theme:oxidized-cut-copper-slab` (candidate L47) keep their plain names — and this package records the reasoning, because a future sweep could mistake the pair for misses: **those stages are fictional.** They exist in neither the candidate name set nor the production name set; no porter will ever create them, because the progression's middle steps are illustrative inventions of the theme's documentation, not themes. A `-jp` repoint would name pages that will never exist, which is worse than the plain form: the plain form at least names the (equally nonexistent, but honestly presented) fictional stage the exhibit means. The other stages are real and were repointed: the bedrock examples (×5), copper, and parallel name `theme:bedrock-jp`, `theme:copper-jp`, and `theme:parallel-jp`, all of which exist as candidates in this campaign. (The repeated bedrock includes an automated census might count are the progression's steps, not duplication.) Flag B in section 7 is the complementary miss: the *prose* links for the three real stages were not repointed even though the *examples* were — the sweep's scope was examples, and the prose links are this package's flag, not a contradiction of the sweep's decision.

### Flags A, B, C — evidence summary

- **A (dropped rules):** original module L2–13, rules at L6–12 (`#page-content > h1 { margin-top: 3rem; }`, `#page-content > h2 { margin-top: 2rem; }`). Absent from the candidate and from `review/parallel-jp/candidate.txt` (both grepped). The candidate's `--main-content-top-margin: 3rem;` (L276) is a base variable and does not apply the margins.
- **B (prose links, minor):** candidate L16 `[[[theme:copper|銅テーマ]]]`, L23 `[[[theme:bedrock|岩盤]]]`, L57 `[[[theme:parallel|パラレル]]]` — plain forms naming nonexistent scp-jp pages, against the same documentation's correctly repointed examples.
- **C (wrapper, minor):** the breadcrumb trail at candidate L16 lacks the original's `[[div class="pseudocrumbs"]]` wrapper; the trail text and link forms otherwise correspond.

## Appendix — residue blocks

| Block | Original | Candidate | Adjudication |
|---|---|---|---|
| B57 | L242–243 | L234–235 | The `[[/iftags]]` gate close and a `----` divider at the source section's head, displaced by the consolidation (R3; section 3) |

### Post-package repairs (REFRESH3-H)

The items above describe this package as built. The repair recorded below postdates the package; `candidate.txt` has been recopied from the current canonical `pages/theme:waxed-oxidized-cut-copper-slab-jp.txt` and `diff.md` and the verdict stamp regenerated with `python3 review/build_review.py`, so this package now documents the post-repair candidate. The regenerated stamp reads **STALE** by design: no re-judgement is fabricated here, and the frozen ledger (`GOSIGN2-LEDGER.md` + supplement, FIX5 head 435a6bb) remains the verdict record.

**FIX-MP12 item 4 (a)(b)(c) — margin rules, prose links, breadcrumb wrapper (landing `f4488f2d2948824238a2d06479f104f4aab0cf5d`, "pages: skipos delivered channel, the-other-side fonts and subtitle, M-pure-12 repairs", 2026-11-17; record `FIX-MP12.md`).** +13/−3 by git numstat. (a) The original head module's two margin rules, absent from the candidate and from the parallel-jp base (the `--main-content-top-margin` variable is a different mechanism), are restored at the code block head after the @import (new L246–253): `#page-content > h1 { margin-top: 3rem; }` and `#page-content > h2 { margin-top: 2rem; }`. (b) Three prose links are repointed to their `-jp` posting names: L17 `theme:copper` → `theme:copper-jp`, L25 `theme:bedrock` → `theme:bedrock-jp`, L59 `theme:parallel` → `theme:parallel-jp` (all three exist as candidates; the two fictional Minecraft progression stages at L40/L47 stay plain, per the package record). (c) The breadcrumb trail is wrapped in `[[div class="pseudocrumbs"]]` … `[[/div]]` (new L16/L18), the original's form. Checker 9/3/1 before and after; the three link-target-missing warnings persist but now name the `-jp` posting names that resolve at posting; no new class (i). (FIX-MP12's acceptance summary quotes +13/−5; git numstat is +13/−3.)

## Change set outside the two diffed files

The diff covers two files; the port's record is two files larger. `pages/theme-decoration-sample-waxed-oxidized-cut-copper-slab-jp.txt` is the decoration sample the render checks ran against (it includes this candidate), and its findings are the sample half of section 11(2). The follow-up diff artifact `gosign2-lanes/lane-oc-gs-localize-s2-E/diff-waxed-oxidized-cut-copper-slab-from2.txt` (campaign record, not repo) is part of this theme's provenance record and is reported in section 12(d). The theme's delivery depends on the base candidate `pages/theme:parallel-jp.txt` (section 2), whose package is part of this campaign's record; the progression siblings (`theme:bedrock-jp`, `theme:copper-jp`) are referenced by the exhibits only.

## License and attribution

- **Title:** 涂蜡的氧化切制铜台阶 版式
- **Author:** Dr Hormress
- **Source:** https://scp-wiki-cn.wikidot.com/theme:waxed-oxidized-cut-copper-slab — revision 2
- **License:** Creative Commons Attribution-ShareAlike 3.0 (CC BY-SA 3.0) — license deed: https://creativecommons.org/licenses/by-sa/3.0/
- **Adaptation:** This package holds a Sigma-10 migration port of the work; changes were made. See "Summary" and "Standing sections" in this README for what changed and why. Translator: AI (Muse and its delegated agents), per the campaign's standing attribution rule.
