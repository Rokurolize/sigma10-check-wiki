# Review package — theme:monotypical-jp (EN → JP port)

<!-- BEGIN GENERATED VERDICT STAMP — do not hand-edit; regenerate with review/build_review.py -->
## Verdict stamp
- Theme: theme:monotypical-jp — origin EN, population #22 [GOSIGN2-LEDGER (b) row 22]
- Overall: STALE — candidate file changed since the verdict was computed (verdict against 435a6bb-era content, file sha256 now 1ef094da6a3ceddfff2c5abeb0720435ab037f34a0b2b21d5445a14c5621d391); verdict not carried over, re-judgement required
> verdicts below describe the pre-change file
- T1 (source check): FINDINGS (classified) — baseline 2026-11-16: exit 1, 6 errors / 3 warns / 2 infos (pseudo-ref×4, hotlink×2); standing classes dispositioned in register c1 [T1-ROWS row 22; GOSIGN2-LEDGER (b) row 22]
- T2/T3 (render, combined verdict): FINDINGS — [combined T2/T3] report `FINDINGS` — sample credit-modal, page credit modal overflows viewport at ≤375px, cdn.scpwiki.com/digitaloceanspaces direct links (Basalt exception discussion). [RENDER-ROWS-1 (RENDER-B row 22)]
- Engine coverage: full matrix as run by the lane; coverage not separately caveated in the row [RENDER-ROWS-1 row]
- Credit modal: sample credit-modal errors dispositioned preview-form (credit:start-preview has no modal mechanism; GOSIGN-TESTS T2 amendment, 2026-11-16; ROWS-1 phrases the line bare and takes the disposition from the part header) [RENDER-ROWS-1 (RENDER-B row 22)]
- T4 (localize patterns + follow-up): FINDINGS — display-affecting findings: 3 [LOCALIZE-ROWS row 22, source LOCALIZE-A]
- T5 (translation text): FINDINGS — the source reports judge T4/T5 jointly; one verdict word covers both [LOCALIZE-ROWS row 22]
- FIX5 re-judgement: none — no OPEN items at the ledger determination [GOSIGN2-LEDGER (b) row 22]
- Computed against: canonical commit 358955eb4013dac2399c414ba8ec2a6e416a3c11; candidate file pages/theme:monotypical-jp.txt sha256:1ef094da6a3ceddfff2c5abeb0720435ab037f34a0b2b21d5445a14c5621d391; record: GOSIGN2-LEDGER.md + GOSIGN2-LEDGER-SUPPLEMENT.md as of the FIX5 head 435a6bb
<!-- END GENERATED VERDICT STAMP -->

## Status

| | |
|---|---|
| Verdict | **PASS** — passed at the ledger determination; this theme had no OPEN items and no §(e) register entry (GOSIGN2-LEDGER (b) row 22) |
| Standing items | **DISPOSITIONED, one later FIXED** — T4's P4 finding (EN CDN base delivery) was dispositioned class (ii) at the ledger and subsequently fixed outright by the FIX3-BF repoint (section 3); T4's P9 finding dispositioned under ruling 2; T1's pseudo-ref ×4 and hotlink ×2 and the render row's items are recorded in sections 3, 4, and 11 |
| Go-sign basis | COMPLETION-REPORT.md §10 (go-sign issued; 81 FIXED / 26 DISPOSITIONED / 0 OPEN across the sweep) |
| Named exception | None for this theme at the determination (its FIX-P4 named exceptions U1/U2 were subsequently fixed, GOSIGN2-LEDGER line 1713; the sweep's single standing named exception is theme:amethyst-v2, which has no candidate) |

## Provenance

| | Original | Candidate |
|---|---|---|
| Page | theme:monotypical | theme:monotypical-jp |
| Wiki | scp-wiki.wikidot.com | SCP-JP Sigma-10 candidate (canonical repo) |
| Reference revision | 142 (re-translation revision; the first-translation revision 135 is also recorded — the mirror is the later, re-translation revision, per sources.tsv) | — |
| Source of this copy | Mirror store, class FETCH-REGEN, fetched 2026-11-17, hash-verified against review/sources.tsv | Canonical file `pages/theme:monotypical-jp.txt`, byte-identical at canonical HEAD c635d01 (this file was not touched by the post-snapshot usage sweep; its example's plain name is adjudicated in section 7) |
| Lines / bytes | 2,680 lines / 109,239 bytes | 2,743 lines / 113,350 bytes |
| SHA-256 | e22c30428cfd169c6200ad687fe95fde84d5447aeab4cf65860a7db37a0e6b06 | 7f7229406bd0a35e6ce44a6ac90d75125712ef38ba854df1dd7be1247adb809e |

Production relationship (sources.tsv kind K5b-3+K6): the candidate layers over theme:basalt-jp (the K5b-3 part — this package's diff covers the theme's own layer only), and a production page theme:monotypical already exists on SCP-JP (the K6 part): the migration is delivered as `pages/phase17-diff-monotypical-jp.txt`, a diff against that production page, and the recorded production drift is 不一致（リテラルの差） — literal-level differences. Wave history: the candidate was created at ffad285, reworked by the Phase 17 production-migration delivery (8dcac74), repaired by d52aa56 (FIX3-BF: the base-import repoint of section 3), and touched by a497307 (FIX4-MECH, duplicate @import removal, KB-65). It was not touched by 1869877 — correctly, as section 1 explains: its translator field records a human translator and was never the normalization's target.

## Summary

The batch's production-migration case, and its second dependent theme. Monotypical is an EN aesthetic theme by EstrellaYoshte built on the Bedrock/Basalt line: the original imports only the base's normalize stylesheet from the EN CDN and carries everything else in its own code fragment, and — unusually — a production JP translation of the theme already exists (translated by nebula2700 in 2024, revised against a later original revision), so this candidate is the Sigma-10 migration of that production page rather than a fresh translation. Its credit block is therefore the production page's own record, not the population's AI/2026 form. The port repoints the base delivery to the basalt JP candidate's normalize fragment (after a disposition-then-fix sequence the per-theme record details), re-hosts the theme's images, restates the theme's extensive credit-area CSS for the JP credit module's structure in six places, translates the body, and keeps the header title and the labeled Rate exhibit as the original and the production page have them. Measured churn (diff.md, the generator's count: +205/−150, 355 changed lines in 93 change blocks / 20 hunks; a GNU-diff count of the same pair gives 287 changed lines — the difference is alignment choice across the file's many near-identical CSS stretches, not content).

## Class summary

Auto-classification by review/classify_hunks.py (signature table 2026-11-17.1): 93 change blocks — 43 specific (46.2%), 45 heuristic (48.4%), 5 residue (5.4%), 0 skipped. Pattern citations below name the KB entry; the patterns/ tree state cited throughout is commit 9c5e9079afb01d30cb9fc4ef9d714e5591eb2ffa.

| Label | Blocks |
|---|---|
| TRANS-UNANCHORED | 37 |
| TRANSLATION-ANCHORED | 25 |
| CSS-BODY | 9 |
| T7-CREDIT-CSS | 6 |
| DRAFT-HOST | 5 |
| DELIVERY-HOST | 2 |
| EXHIBIT-RESTRUCTURE | 2 |
| INCLUDE-REPOINT | 2 |
| SELF-DELIVERY | 2 |
| ANNOTATION | 1 |
| ASSET-REHOST | 1 |
| CREDIT-PREVIEW | 1 |
| CREDIT-PROSE | 1 |
| ESCAPED-INCLUDE | 1 |
| FONT-IMPORT | 1 |
| IFTAGS | 1 |
| INFO-DEL | 1 |
| TASL-FIELDS | 1 |
| WS-ONLY | 1 |

Adjudication for this README (every block was read against the bytes): the 9 CSS-BODY blocks split into the exhibit's deleted normalize import (B74, section 3), the credit-area rule adjustments that ride with the T7 restatements (B77, B80, B82, B84–B87, B89, section 8); the 2 EXHIBIT-RESTRUCTURE blocks are the interwiki include's repoint zone (B3) and the image-block exhibit's re-host (B12), not restructuring — the exhibit census is complete; the 5 residue blocks are single lines inside near-identical CSS stretches and one head-zone line (B2), resolved by shape. After adjudication no block is left unexplained.

## Standing sections

### 0. Header and provenance frame

- **What:** Theme theme:monotypical-jp; original theme:monotypical on scp-wiki at reference revision 142 (the re-translation revision; revision 135, the first translation's, is also recorded in sources.tsv and in the candidate's credit block); candidate `pages/theme:monotypical-jp.txt`. Provenance route: the K5b-3+K6 compound of the Provenance table — a basalt-layered theme (own layer only in this diff) whose JP production page already exists, so the candidate's baseline is double: the EN original at rev 142 for content, and the production JP page for the migration's credit and delivery record (the phase17 diff file is the migration's delivery form). The original opens with its delivery module ahead of everything (original L1–4); the candidate keeps that order (candidate L1–4) and localizes the tag gate in the body (`+theme` → `+テーマ`, block B5).
- **Why:** Section 0 declares the provenance route so every later count is read against the right baseline; for this theme the double baseline is the fact that explains its two non-standard forms (the credit block of section 1 and the example name of section 7).
- **Verify:** The sources.tsv row for monotypical-jp (kind K5b-3+K6 and its note); `sha256sum original.txt` against the Provenance table.
- **Disposition:** Standing (the route itself); the delivery relationships are section 3.

### 1. Credit and attribution

- **What:** The original's credit furniture is a labeled bare Rate ("**Rating w/ Credit Module:**", original L25–27's zone) and an info pair with the placeholder body (original L29–33, INFO-DEL in block B9). The candidate installs the JP preview block (candidate L31–41) — but in the production page's own form, not the population's standard form: its fields are タイトル （モノタイプテーマ), 翻訳責任者 **nebula2700**, 翻訳年 **2024**, 原題 (Monotypical Theme), 著作権者 (EstrellaYoshte), 作成年 (2021), and both revision fields （初訳時参照リビジョン 135 and 改訳時参照リビジョン 142 — a ninth field beyond the standard eight, recording the re-translation), closing with the source link in bare-bracket form (section 7). The differences from the population form are the production relationship made visible: the production page's translation is nebula2700's 2024 work, and the migration preserves its credit rather than overwriting it with the AI/2026 form — which is also why the FIX-CREDIT-D normalization (1869877) does not touch this file. Author check, performed explicitly: the original's prose credits EstrellaYoshte as the theme's maker "with additional help by Woedenaz" (original L35); the candidate's field names EstrellaYoshte, and its prose retains the Woedenaz credit in translation （Woedenaz氏に多大なご協力をいただいています, candidate L43). The theme's own authorship structures (its CSS banner: "Sigma+ by EstrellaYoshte / Bedrock Theme by EstrellaYoshte") name EstrellaYoshte alone as author, so the field follows the original's authorship and the helper's credit survives where the original put it — in the prose. That is a checked non-defect, stated with both sides so the check is auditable. The labeled Rate exhibit: the candidate keeps the Rate live under its label alongside the credit block (candidate L25–30's zone), the labeled paired-exhibit form the ledger's pattern-3 exception list names this theme for (GOSIGN2-LEDGER line 1711).
- **Why:** P3/T1 with the pattern-3 exception for the paired exhibit, and the production-adoption principle for the fields: where a production translation exists, its translator credit is a fact of record, and a migration that silently replaced nebula2700's name with the wave's AI credit would falsify the record the credit block exists to keep. Ruling 3's eight fields are the floor; the production form's extra revision field is this theme's own history, kept.
- **Verify:** Read candidate L25–43 against original L25–37; `grep -n 'nebula2700' candidate.txt` — the credit field and the CSS banner line (section 10).
- **Disposition:** FIXED (GOSIGN2-LEDGER §(c3): P3 credit fields FIXED, credit waves, checker-verified); the field forms stand as the production record.

### 2. Includes and components

- **What:** The include repoints: the head's interwiki-style include, `:scp-wiki:component:interwiki-style` → `:scp-jp:component:interwiki-style` (blocks B3/B4's zone; its theme= parameter is section 3 — the candidate's copy of the include is written with blank lines between its parameters, a byte-level untidiness that changes nothing); the image-block exhibit's include, `component:image-block` → `:scp-jp:component:image-block` (block B12; its asset is section 4); and the credit includes (section 1). The usage example's escaped include is exhibit text (section 7). No other live include changes fire.
- **Why:** P1 (KB-15): an include must name the JP counterpart that actually exists on scp-jp; both repointed targets have verified JP counterparts. Ruling 4 is not engaged: no component had to be ported alongside this theme.
- **Verify:** `grep -n '\[\[include' candidate.txt` — every live include names a `:scp-jp:` target.
- **Disposition:** Applied; no foreign include kept, no named exception needed.

### 3. Delivery and code loading

- **What:** The delivery relationships, stated explicitly because this is a dependent theme. The original's base relationship is partial by design: its head `[[module css]]` imports exactly two things — the base's normalize stylesheet from the EN CDN (`cdn.scpwiki.com/theme/en/basalt/normalize-min.css`) and its own code fragment (`local--code/theme:monotypical/5` from scp-wiki.wdfiles.com) (original L1–4) — with an interwiki-style include at priority 1 naming its own fragment (original L11–13). Everything else the theme needs it carries itself: its CSS (the /5 fragment, mirrored in the page's code exhibit) is a full build whose banner credits the Bedrock line it derives from ("Sigma+ by EstrellaYoshte / Bedrock Theme by EstrellaYoshte"). So the original imports the base's normalize only, and inlines nothing of the base beyond what its own build already contains. The candidate preserves that topology exactly, changing the coordinates: the head module imports `local--code/theme%3Abasalt-jp/7` — the basalt JP port candidate's fragment 7, its normalize fragment — and its own `local--code/theme%3Amonotypical-jp/5`, both from the draft host (candidate L1–4), and the interwiki include at priority 1 names its own /5 on the same host (candidate L10–16). The exhibit's copy of the normalize import (original L321) is deleted rather than repointed (block B74): the exhibit no longer re-imports what the head frame delivers. The path to this state matters and is recorded in full in the per-theme record: at localize-check time the candidate still imported the EN CDN normalize in both places, which was T4's P4 finding; the ledger dispositioned it class (ii); FIX-P4 named it an exception (U1/U2); and FIX3-BF (d52aa56) then repointed both sites to the basalt-jp fragment anyway. The current bytes contain no cdn.scpwiki.com reference at all (grep-verified). The draft-host lines (the two head imports, the interwiki parameter, and the re-hosted image exhibits of section 4) are the pseudo-ref population of T1's record.
- **Why:** Ruling 1 is the governing rule for dependent themes: the dependent theme imports the base theme's JP port candidate delivery rather than the raw upstream branch delivery. Monotypical's form of it is the fragment form — it imports the one fragment of the base it ever imported, now from the base's JP candidate (basalt-jp/7) instead of the EN CDN — and the FIX3-BF repoint is that rule applied after the disposition had already closed the item on weaker grounds. P4/T9 and P6/T3 for the frame; the draft-host form is KB-41, class (iii), sanctioned at draft stage and rewritten at posting.
- **Verify:** Read candidate L1–16 against original L1–13; `grep -n 'cdn.scpwiki' candidate.txt` returns nothing; `git log --oneline -- pages/theme:monotypical-jp.txt` in the canonical repo shows the d52aa56 step.
- **Disposition:** DISPOSITIONED at the ledger (class (ii)) and subsequently FIXED (FIX3-BF) — both records stand, and this package follows the current bytes.

### 4. Fonts and assets

- **What:** Fonts (block B75): the code exhibit's three font imports move from fonts.bunny.net to fonts.googleapis.com with the families and weights unchanged — Urbanist, Ubuntu, and Fira Code (original L323–325 → candidate L331–333). The live delivery's font handling rides inside the theme's own fragment in both files. No JP font load is added anywhere in the candidate, and no stack in its own layer names a JP family (grep-verified: the candidate contains no "Noto" at all): the theme's typography is its three Latin display families, which load, and its Japanese text takes the base fragment's fallbacks. That is stated as a fact of the file, not dressed as a supplement; no ledger record charges it, and the theme's design (a Latin-display aesthetic theme) is the context. The named-but-unloaded check comes out clean: every family the stacks name first (Urbanist, Ubuntu, Fira Code) is loaded by the imports above. Assets: the body's main image (mono.png) is re-hosted from EN storage to the JP storage host in its production file-ID form (`scp-jp-storage.wdfiles.com/local--files/file%3A8260379-77-5jif/mono.png`, block B12, ASSET-REHOST) — the production page's own storage address, consistent with the migration's baseline. Three further image exhibits (mono-nord.png and its kin, blocks B67–B69) are re-hosted from EN storage to the draft host with their file names kept. T1's hotlink ×2 are the baseline's EN CDN import lines of section 3, since removed by the repoint; no EN storage or CDN reference remains in the current file (grep-verified).
- **Why:** P7/T5 for the font host swap (same families, serving host — the bunny-to-Google form this population uses where the grammar allows it, and here it did). P5 with KB-17 for the assets: the theme's own images re-host to the JP side — the main image at its production storage address because this candidate migrates a production page, the exhibits at the draft host in the class-(iii) form.
- **Verify:** `grep -n '@import' candidate.txt` — the head pair and the exhibit's three font imports; `grep -n 'wdfiles' candidate.txt` — the JP storage and draft-host lines only.
- **Disposition:** Fonts applied; assets applied (production form) and DISPOSITIONED (draft-host exhibits, class (iii)).

### 5. Header and sidebar furniture

- **What:** The theme's signature furniture at the head — the `mono-structure` div with its sidebar buttons (the ≡ toggle anchor and the no-more-menu anchor, original L6–14) — is retained byte-identically in the candidate (candidate L5–17's zone), the interwiki include inside it repointed (section 2). The header title: `--header-title: 'SCP FOUNDATION'` is kept in English at both of its sites (candidate L225, L473, matching the original's L225, L474 — the localize row cites the same two lines). That is T4's pattern-9 item.
- **Why:** Ruling 2 takes header and title language out of Sigma-10 migration scope (case-by-case translation taste), and the ledger dispositions the P9 item on exactly that ground. The furniture retention is P8's ordinary form: the theme's own structural inventions are the theme, and the port does not redesign them.
- **Verify:** `grep -n 'SCP FOUNDATION' candidate.txt` — the two kept strings; read candidate L5–17 against original L6–14 for the furniture.
- **Disposition:** DISPOSITIONED (P9, ruling 2; GOSIGN2-LEDGER line 1420).

### 6. Text translation

- **What:** The body translates throughout (62 translation-labeled blocks): the meta-title exhibit, the intro, the usage prose, the horizontal-rule and footnote exhibits (the original's footnote name-checking Placeholder McD survives translation — it is the exhibit's content, not an attribution), the component exhibits, and the documentation. The CSS banner stays in English as code documentation, with the one addition of section 10. The theme's structural labels （クレジットモジュール： and its kin) translate as exhibit prose. No COMMENT-TEXT mass fires separately in this file: its comments are the banner and the section markers inside the CSS, which ride with the CSS blocks.
- **Why:** P9/P10 (prose and documentation into Japanese). The banner's English is the code's own documentation voice, kept as the population keeps CSS banners, with the JP editor's line added (section 10).
- **Verify:** Read candidate L19–50 against original L17–45 for the body head; `grep -n 'Placeholder' candidate.txt` — the footnote exhibit intact.
- **Disposition:** Applied (the theme's T4 record shows no translation finding; its findings are sections 3 and 5).

### 7. Links and references

- **What:** Three link acts, one of them adjudicated at length because it looks like this batch's recurring defect and is not. (1) The credit block's source link names the original at its recorded host (scp-wiki.wikidot.com, section 1), in the production form's bare-bracket syntax — host check clean. (2) The prose links (the author links, the footnote's Placeholder McD reference) keep their relative forms and resolve as the original's did. (3) The usage example (candidate L41): `{{@@[[include :scp-jp:theme:monotypical]]@@}}` — the plain name, not theme:monotypical-jp. In any other candidate in this batch that form names a page that will not exist; here it names the production page that already exists and that this candidate migrates — the migration is delivered as a diff against theme:monotypical (phase17-diff file, Provenance table), so at posting the production page itself is updated and the example's name stays correct. The population sweep, which repaired the plain-form examples in six of this batch's other files, left this one untouched on the same ground (its record: references to existing production pages under plain names are correct and untouched). The example is therefore adjudicated correct as written, with the reasoning stated so a later reader does not "fix" it into a reference to the staging candidate.
- **Why:** The self-reference standard is that the example must name the page a user should include after posting. For a fresh candidate that is the -jp posting name; for a production migration it is the production page's own name, because that is the page that will carry the migrated theme. The ground differs; the standard is the same.
- **Verify:** `grep -n 'theme:monotypical' candidate.txt` — the example and the credit/source references; the sources.tsv note for the production page's existence.
- **Disposition:** Applied; item (3) adjudicated correct (production-name reference), not a flag.

### 8. Structure and exhibits

- **What:** The exhibit census is complete against the original, and the structural mass is the credit-area CSS: six T7-CREDIT-CSS blocks restate the theme's credit and rate styling for the JP credit module's structure. The type cases: a general link rule gains an exclusion for the credit anchors (`a:not(.fa-info, .cc)`, block B76, candidate L557); a stretch of credit-button rules is restated and extended (block B88, candidate L1450–1485, the largest single addition in the diff); and at the tail, two small `[[module CSS]]` supplements carry the modal-flow fix and the creditButton anchor restatement with their porter comments (block B93, candidate L2733–2743, section 10). The remaining CSS-BODY blocks (B77, B80, B82, B84–B87, B89) are rule adjustments in the same credit-and-layout territory, riding with the restatements. Monotypical styles its credit furniture more heavily than any other theme in this batch — its design makes the credit button part of the theme's look — so the JP module's different DOM (its anchor is a direct child of .creditButton, where the EN module wraps it in a `<p>`) forces more restatement than the single block legend-of-blue needed. The exhibit's deleted normalize import (B74) is section 3.
- **Why:** T7: where a theme's CSS targets a module's internal structure and the JP module's structure differs, the rules are restated for the JP structure — the alternative (leaving EN-structure selectors) would silently unstyle the credit furniture the theme exists in part to style. The tail supplements follow the population's form for post-gate corrections, with their reasons in comments.
- **Verify:** Read candidate L1440–1490 against the original's corresponding zone for the restated rules; candidate L2733–2743 for the tail supplements.
- **Disposition:** Applied (the restatements are part of the port as delivered; the ledger's T7-family record for this theme is the credit-CSS treatment itself).

### 9. Formatting only

- **What:** One whitespace-only block (B90, original L1921 → candidate L1975), a single line inside the code exhibit. Nothing else in the diff is formatting-only; the interwiki include's blank-line spacing (section 2) is a byte fact recorded there, not a formatting block.
- **Why:** Stated so the formatting mass is separated from content mass, per the class treatment.
- **Verify:** Block B90 in classification.json (label WS-ONLY).
- **Disposition:** Standing (nothing to disposition).

### 10. Porter annotations

- **What:** Three annotation sites. (1) The CSS banner's editor line: "Edited for SCP-JP by nebula2700" — present in the original's banner (the EN page already carried the JP editor's credit), and added by the candidate to the banner's second copy so both copies of the banner agree (block B73, candidate L327–328). (2) The tail supplements' comments (block B93): "SCP-JP Wikidot monotypical credit correction: keep the modal rating in document flow below the license control." and the creditButton comment explaining the direct-child restatement (quoted in substance in section 8). (3) The credit block itself functions as the port's record (section 1), though it is furniture rather than annotation. No other porter prose stands in the file.
- **Why:** T11: the annotations mark the port's judgment calls at their sites — who edited this for SCP-JP, and why the tail rules exist. The banner line is also a credit fact (it names the production translator inside the code), consistent with the credit block's field.
- **Verify:** `grep -n 'nebula2700\|credit correction' candidate.txt` — the banner lines and the tail comments.
- **Disposition:** Standing (the annotations are part of the port as delivered).

### 11. Dispositions and exceptions

- **What:** Four standing items, all closed. (1) T4's P4 finding (section 3): DISPOSITIONED class (ii) at the ledger (GOSIGN2-LEDGER line 1420: "delivery class (ii): original-state CDN delivery"), named as exceptions U1/U2 at FIX-P4 (line 1713), and subsequently FIXED by FIX3-BF's repoint — the only item in this batch whose disposition was overtaken by a fix, recorded in full in the per-theme record. (2) T4's P9 finding (section 5): DISPOSITIONED under ruling 2. (3) T1's pseudo-ref ×4 (sections 3 and 4): class (iii), sanctioned draft-host form; its hotlink ×2 are the baseline's EN CDN lines, removed by the item-(1) fix. (4) The render row's items: the sample's credit-modal reading (dispositioned preview-form, the standing GOSIGN-TESTS T2 amendment); the theme page's credit modal overflowing the viewport at ≤375px — a display reading on the page's own credit styling, recorded as the row records it (the theme's modal geometry is its design, and the row preserves the reading rather than the port redesigning it); and the loaded chain's cdn.scpwiki.com and digitaloceanspaces direct links, the review-time state of the base delivery (the CDN half is item (1), since repaired; the digitaloceanspaces half is the base theme's own asset host, the subject of the row's "Basalt exception discussion" — the base's delivery choices are the basalt package's record, not this dependent theme's to relitigate).
- **Why:** A disposition names its ground: class (ii) then a fix for the delivery, ruling 2 for the title, class (iii) for the draft host, the preview-form amendment for the modal reading. Nothing in this theme rests on an unnamed exception.
- **Verify:** The theme's rows in T1-ROWS, LOCALIZE-ROWS, and RENDER-ROWS-1; the disposition lines in GOSIGN2-LEDGER (lines 1420, 1711, 1713).
- **Disposition:** DISPOSITIONED (all four, on the grounds named; item 1 also FIXED).

### 12. Verification record

- **What:** T1 (source check, T1-ROWS row 22): pseudo-ref ×4, hotlink ×2 (exit 1, 6 errors / 3 warns / 2 infos) — the baseline's counts, whose error lines are the draft-host population and the since-removed CDN imports. T4 (localize check, LOCALIZE-ROWS row 22, wave LOCALIZE-A): FINDINGS, 3 findings — the row's text details (i) pattern 4, the EN CDN normalize import ×2 at L2 and L330 (display-affecting), and (ii) pattern 9, the `--header-title: 'SCP FOUNDATION'` at L225 and L474, before its text trails off; the ledger's disposition list closes the theme's items under P4 and P9 by name (section 11). T2/T3 (render check, RENDER-ROWS-1, wave RENDER-B (row 22)): the readings of section 11. The go-sign ledger row (§(b) row 22) aggregates T1 FINDINGS (classified), T2 FINDINGS, T3 FINDINGS, T4 FINDINGS, T5 PASS — every finding classified, none OPEN.
- **Why:** The counts are the acceptance evidence for the sections above: each checker's scope and moment are stated (T1's baseline predates the FIX3-BF repoint, which is why its hotlink count names lines the current file no longer has).
- **Verify:** The three ledger-part files named above, row 22 in each; GOSIGN2-LEDGER §(b) row 22 for the aggregate.
- **Disposition:** PASS at the ledger determination, with the items of section 11 dispositioned as recorded.

## Per-theme record

Two items belong to this theme alone.

**The P4 sequence: dispositioned, excepted, then fixed anyway.** This theme's base delivery is the one place in the batch where the paper record and the bytes disagreed in sequence, so the order is stated plainly. (1) The localize check found the candidate still importing the base's normalize from the EN CDN in two places and charged it as a display-affecting pattern-4 finding. (2) The go-sign ledger dispositioned that finding as class (ii), "original-state CDN delivery" — the class for delivery retained in its original state. (3) The FIX-P4 wave named the two sites as exceptions U1/U2 rather than repointing them in that pass. (4) FIX3-BF then repointed both sites to the basalt JP candidate's normalize fragment (canonical commit d52aa56), and the current candidate contains no EN CDN reference. The end state satisfies ruling 1 in its fragment form (section 3); the disposition remains in the ledger as the determination's record. A reader who checks only the ledger would think the CDN delivery stands; a reader who checks only the bytes would not know it was ever charged. This package records both, which is the documentation's job. (The lumina package in this batch shows the same disposition wording against a similar repoint history.)

**The credit block is the production page's own, and that is correct.** Every other candidate in this batch carries the wave's credit form （翻訳責任者 AI, 翻訳年 2026, rev-only fields). This one carries nebula2700, 2024, and two revision fields, because a production translation exists and this candidate is its Sigma-10 migration: overwriting the production translator's credit with the migration wave's would falsify the record. The same production relationship explains the usage example's plain name (section 7) and the main image's production storage address (section 4). Together they make this package the batch's reference for the K6 shape: when a production page exists, the candidate's baseline is the production page, and forms that would be defects in a fresh candidate are correct here for stated reasons.

## Change set outside the two diffed files

| File | Change |
|---|---|
| `pages/theme-decoration-sample-monotypical-jp.txt` | The theme's decoration sample: a JP page applying the candidate, the surface the T2/T3 render checks measured (section 11's sample readings) |
| `pages/phase17-diff-monotypical-jp.txt` | The migration's delivery form: the diff of this candidate against the production page theme:monotypical (recorded production drift: literal-level differences), per the sources.tsv note in the Provenance table |
