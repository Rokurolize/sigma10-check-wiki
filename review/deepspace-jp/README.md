# Review package — theme:deepspace-jp

<!-- BEGIN GENERATED VERDICT STAMP — do not hand-edit; regenerate with review/build_review.py -->
## Verdict stamp
- Theme: theme:deepspace-jp — origin CN, population #181 [GOSIGN2-LEDGER (b) row 181]
- Overall: STALE — candidate file changed since the verdict was computed (verdict against 435a6bb-era content, file sha256 now 30476e077361ddec42729ef3810297a38f0396fed3457d33759e3be58076208f); verdict not carried over, re-judgement required
> verdicts below describe the pre-change file
- T1 (source check): FINDINGS (classified) — baseline 2026-11-16: exit 1, 2 errors / 1 warn / 2 infos (pseudo-ref×2); standing classes dispositioned in register c1 [T1-ROWS row 216; GOSIGN2-LEDGER (b) row 181]
- T2/T3 (render, combined verdict): FINDINGS — [combined T2/T3] report `FINDINGS` — hidden-rate on both pages (all combos); page-overflow 501–502px@320/375 (page) and 505–506px@320/375 + 789px@768 + 1489px@1366 (sample); runtime-hotlink site-theme chain. [RENDER-ROWS-2 (RENDER-S2-E (CN4))]
- Engine coverage: full matrix as run by the lane; coverage not separately caveated in the row [RENDER-ROWS-2 row]
- Credit modal: no credit-modal line recorded [RENDER-ROWS-2 (RENDER-S2-E (CN4))]
- T4 (localize patterns + follow-up): FINDINGS — display-affecting findings: 4 [LOCALIZE-ROWS row 180, source LOCALIZE-S2-D]
- T5 (translation text): FINDINGS — the source reports judge T4/T5 jointly; one verdict word covers both [LOCALIZE-ROWS row 180]
- FIX5 re-judgement: item 54 (class B) FIXED — FIX5-FURNB, commit 25bb0b4: duplicate bare Rate block removed [GOSIGN2-LEDGER-SUPPLEMENT (a) item 54]
- Computed against: canonical commit 1e34c0b668faf170da8af14c127251af3e35fa26; candidate file pages/theme:deepspace-jp.txt sha256:30476e077361ddec42729ef3810297a38f0396fed3457d33759e3be58076208f; record: GOSIGN2-LEDGER.md + GOSIGN2-LEDGER-SUPPLEMENT.md as of the FIX5 head 435a6bb
<!-- END GENERATED VERDICT STAMP -->

## Status

| | |
|---|---|
| Verdict | **PASS** — go-sign re-run (this theme is one of the 286 of 286 pass-eligible themes) |
| Blocking items at ledger time | GOSIGN2-LEDGER.md §(e) item 54 [B] (duplicate bare Rate) |
| Re-judgment | GOSIGN2-LEDGER-SUPPLEMENT.md row 54: **FIXED** (FIX5-FURNB, commit 25bb0b4); re-derived from this package's bytes in the per-theme record below |
| Standing items | **DISPOSITIONED** — ledger §(c3): P1 DISPOSITIONED (the basalt-jp dependency, posting-procedure convention class); P3 credit fields FIXED (credit waves); P6 FIXED (frame waves); ledger §(c2) render row: hidden-rate recorded only (KB-50), page-overflow (KB-33/KB-34 family), runtime-hotlink site-theme chain (KB-40) |
| Go-sign basis | COMPLETION-REPORT.md §10 (go-sign issued; 81 FIXED / 26 DISPOSITIONED / 0 OPEN across the sweep) |
| Post-verdict change | The codeaddr remedy removed the frame's `theme=` parameter (canonical commit 722ceb5, sub-shape (B) under the main chat's ruling); the stamp therefore reads STALE against the pre-remedy verdict, by design (see section 3) |
| Open flag from this package | The centered usage exhibit still names the plain slug `theme:deepspace` (candidate L287) — see the per-theme record. The candidate was not edited by this package |
| Named exception | None for this theme (the sweep's single named exception is theme:amethyst-v2, which has no candidate) |

## Provenance

| | Original | Candidate |
|---|---|---|
| Page | theme:deepspace | theme:deepspace-jp |
| Wiki | scp-wiki-cn.wikidot.com | SCP-JP Sigma-10 candidate (canonical repo) |
| Reference revision | 3, as recorded in the candidate's credit block: **初訳時参照リビジョン:** 3 | — |
| Source of this copy | Mirror store `orig-deepspace-rev3.txt` (class COPY, byte-true copy of the campaign cache `gosign2-lanes/lane-oc-gs-localize-s2-D/orig-deepspace.txt`, fetched once by the LOCALIZE-S2-D lane) | Canonical file `pages/theme:deepspace-jp.txt`, copied at worktree HEAD e821e37 |
| Lines / bytes | 405 lines / 10,057 bytes | 420 lines / 11,780 bytes |
| SHA-256 | fb7ba7229f71e4e0db37afa971ce549f7693edb194369716aa772b154baeaca6 | a6eeb7f77f041e2847150ccc1119b7209913c932f53727914a66d4fb6a833152 |

One record correction belongs here. The `review/sources.tsv` note for this row claims the original was "superseded upstream since the reference revision", but the follow-up artifact that note itself cites (`diff-deepspace-from3.txt` in the campaign record) records rev 3 → rev 3, no changes: upstream latest remains revision 3 and this mirror is current. The note's wording is the defect (the same wrong-note shape corrected earlier for ambrose, alcur, and inland-empire); it is flagged for central correction and the package proceeds on the artifact's evidence.

## Summary

Deepspace is a Basalt-based page-source theme: a hidden include pulls the base theme in, and one large `[[module CSS]]` carries the theme's own overrides and variables. The port swaps the base include to the JP Basalt candidate, rewrites the font stacks from Noto Sans SC to Noto Sans JP and adds the matching load, adds the preview credit block and the interwiki-style frame, and translates the documentation body. The measured churn (diff.md: +96/−86 in 6 hunks) is small for the file's size because the 260-line CSS module is mostly carried over. The one blocking defect, a duplicated bare Rate, was removed by FIX5 and is re-derived below. Two things a reviewer should not miss: the candidate's dependency on `theme:basalt-jp` is real and is disclosed in the candidate's own translator note (its disposition is restated in the per-theme record), and this package flags one live defect the sweep left behind, the plain slug in the centered usage exhibit.

## Standing sections

### 0. Header and provenance frame

- **What:** The original opens with a hidden div (original L1–5) that includes the CN Basalt theme page as its base, then its single `[[module CSS]]` (original L7–265). There is no ThemePreviewer and no header frame. The candidate keeps the shape exactly: the hidden div now includes `theme:basalt-jp` (candidate L3), and the module follows (candidate L7–266). Provenance route: derived from the original at reference revision 3 (mirror class COPY; see Provenance).
- **Why:** The hidden include is the theme's base layering: the module's `--basalt-*` variables and overrides only make sense on top of Basalt. Section 3 records the delivery form; section 2 the include itself.
- **Verify:** Read original L1–9 against candidate L1–10.
- **Disposition:** Recorded; the base swap is argued in section 2 and its dependency disposition in the per-theme record.

### 1. Credit and attribution

- **What:** The original has no credit block at all; its attribution is the info prose at original L283, which names [[*user Un Party]] as the theme's maker and thanks Dr Roger_F_XL and Kcorena for testing and help with fixes. The candidate adds the preview credit block (`:scp-jp:credit:start-preview`/`end-preview`, candidate L274–283) with the eight standard fields; **著作権者** is [[*user Un Party]], the original's sole authorship statement. The two thanked testers are not authors in the original and do not enter the field; their thanks are carried in the translated info prose (candidate L295). The T4 lane had charged six missing credit fields against the early candidate; the credit waves completed them (ledger §(c3): P3 FIXED).
- **Why:** P3/T1 credit supplement and ruling 3 (2026-11-16) for the eight fields and the 翻訳責任者： AI credit. The author field follows the original's own attribution, including what it does not claim.
- **Verify:** Read candidate L274–283 against original L283; count the eight fields.
- **Disposition:** FIXED (credit waves; ledger §(c3)). The Rate half of that T4 charge is item 54, in the per-theme record.

### 2. Includes and components

- **What:** Original includes: the base include `:scp-wiki-cn:theme:basalt` (L3, inside the hidden div), the centered usage exhibit with its split-markup include (L275), and `:scp-wiki-cn:component:image-block` for the Basalt logo exhibit (L327). Candidate includes: `theme:basalt-jp` in the bare same-wiki form (L3), the interwiki-style frame (L268–270), the credit pair (L274/283), the usage exhibit (L287, see the flag below), and `component:image-block` in the bare form (L341) with the logo file re-hosted as the candidate's own draft-host copy. The classifier's COMPONENT-SWAP on block B1 is the base include: the campaign's JP candidate of Basalt replaces the branch original it ports (T8; ruling 4's component-port principle applied to a base theme).
- **Why:** P1 repoints and the base swap. No include in the candidate points at a CN-wiki page.
- **Verify:** `grep -n '\[\[include' original.txt candidate.txt` and compare the two lists.
- **Disposition:** Standing, except the usage exhibit's slug, which is an open flag (per-theme record), not a disposition.

### 3. Delivery and code loading

- **What:** Module-CSS delivery on both sides: neither file has a `[[code]]` block (the topology pass finds one module-css component per side and no moves), so there is no local--code self-delivery address to resolve. The FIX-CODEADDR population audit classes this theme in its no-target class for exactly that reason. The candidate's interwiki-style frame (candidate L268–270, after the module) carries `priority=1` and, in the current bytes, no `theme=` parameter: the frame as first added named the theme's own /1, an address no code block answers, and under the main chat's codeaddr ruling the parameter was removed (canonical commit 722ceb5, sub-shape (B): the original carries no frame self-address in that role). That removal is the post-verdict change behind the stamp's STALE. The base layering is the hidden-div include of section 2, beneath the theme's own module overrides.
- **Why:** P6/T3 frame supplement (KB-07 family; patterns commit 9c5e9079afb01d30cb9fc4ef9d714e5591eb2ffa); the address remedy follows the ruling that a frame pointer must name a block that holds CSS or not be carried.
- **Verify:** Read candidate L266–272; `grep -n 'local--code' candidate.txt` returns nothing.
- **Disposition:** Recorded as the audit and the ruling state it; not re-litigated here.

### 4. Fonts and assets

- **What:** The candidate adds one Google Fonts load at the module head (candidate L8: Orbitron, Inter, Noto Sans JP) where the original loaded nothing in-file. The three primary stacks are rewritten in place (original L12–14 → candidate L13–15): `'Orbitron', 'Inter', 'Noto Sans SC'` → `'Orbitron', 'Inter', 'Noto Sans JP'`, and likewise for the UI and body stacks (P7 stack rewrites; the classifier's JPFONT-LOAD fires on the load line, the stack lines pair as anchored translations). One named font is loaded by neither side: the mono stacks read `var(--mono-font, 'JetBrains Mono', monospace)` byte-identically in both files (original L191/200/262; candidate L192/201/263), and no @import or @font-face in either file loads JetBrains Mono — an inherited state the port did not create, with the generic monospace standing behind it; it is recorded here so the absence is a checked fact, not an oversight. Assets: the `--logo` variable (original L30, pointing at the EN wiki's Basalt darkmode logo file) is re-hosted to the candidate's own draft-host copy (candidate L31), and the image-block exhibit's lightmode logo likewise (candidate L341). The classifier's HTTP-KEPT presence note at candidate L37 is the W3C namespace string inside a data-URI background: a known false-fire of that signature, not an http asset.
- **Why:** P7/T5 font supplement (the load covers exactly the stacks the port rewrote) and P5 asset re-hosting.
- **Verify:** `grep -n '@import\|font-family' candidate.txt`; compare the mono lines on both sides.
- **Disposition:** Standing; the mono fallback is recorded as inherited, not charged.

### 5. Header, sidebar, and site furniture

- **What:** `--header-title: "SITE-CN-209"` is kept byte-identical (candidate L11 = original L10): it is the fictional site designator the theme styles, in the original's own lettering. `--header-subtitle` is glyph-converted, `"学史 · 构造 · 记录"` → `"学史 · 構築 · 記録"` (R5: 构→構， 录→録）, and the candidate's translator note discloses the conversion (candidate L297). No sidebar or topbar structure changes: the furniture rules inside the module are carried over.
- **Why:** The T4 lane recorded the title retention as needing staff approval (LOCALIZE-ROWS row 180); ruling 2 (2026-11-16) places header and title language outside migration correctness (KB-57 family), which is the framework that closed it.
- **Verify:** Read candidate L11–12 against original L10–11.
- **Disposition:** DISPOSITIONED (ruling 2).

### 6. Text translation

- **What:** The documentation body is translated throughout (22 TRANSLATION-ANCHORED blocks; the info prose, usage text, and exhibit labels pair one-to-one). Inside the CSS module, four COMMENT-TEXT blocks (B4–B7) are the original's Chinese section comments translated in place (R1 in-CSS text, porter-visible only; e.g. the Logo comment at original L29 → candidate L30). One charged residue stands in the translated prose: the word 漏洞 survives at candidate L295, inside the thanks sentence translating the original's 修补漏洞 (help fixing loopholes). LOCALIZE-ROWS row 180 charged it as T5 residue; it is still in the bytes, recorded here as standing residue that the row's classified FINDINGS closed with (this theme's only §(e) item was 54). The 「版式」 terminology variance charged in the same row stands with it: the candidate uses 版式 throughout, including the credit title field 深空 美学版式.
- **Why:** P10 body translation and R1 for in-CSS text; KB-18 for reader-visible strings. Residue is named, not passed over, because a reviewer checking "was this string translated or left?" needs the answer from the package.
- **Verify:** `grep -n '漏洞' candidate.txt` (L295); read the comment pairs at original L28–30 / candidate L29–31.
- **Disposition:** DISPOSITIONED as charged residue (LOCALIZE-ROWS row 180; the ledger closed this theme on item 54 with the row's findings classified).

### 7. Links

- **What:** The candidate's source link points back to the original page (credit block, candidate L282, host scp-wiki-cn.wikidot.com, the recorded host in sources.tsv). The info prose's derivation link keeps pointing at the CN Basalt page (candidate L295, as in original L283): it is a quotation of where the base lives in the original's world, while the delivery itself uses `theme:basalt-jp` (section 2). No other prose links exist in the file.
- **Why:** P11 repoints govern the port's own reference surface; a derivation link in credit prose is a quotation, and repointing it would misstate the original's derivation.
- **Verify:** `grep -n 'wikidot.com' candidate.txt`.
- **Disposition:** Standing.

### 8. Structure

- **What:** The localize.md closing rule holds: the single module, the variable order, and the body order follow the original (topology: same component kinds, no moves). Additions are the supplements (credit block, frame, translator note) and one functional completion: `[[footnoteblock]]` at candidate L419, just before `[[/iftags]]` (the classifier's residue block B44, resolved here). The original's body carries a footnote exhibit (original L380, a tab whose text holds a `[[footnote]]`) but no footnoteblock anywhere, so the exhibit's footnote has no rendering target in the original; the candidate adds the block so the exhibit it translated renders complete. The classifier's EXHIBIT-RESTRUCTURE label on block B14 is adjudicated against the exhibit census: the image-block exhibit is retained with the same caption role — the change is the include repoint and asset re-host of section 2, not a dropped or replaced exhibit. The original defines no include-parameter gates and no `{$...}` slot definitions (grep count 0 on both sides); its documented mechanism is the Basalt layering itself, whose state is the per-theme record's dependency disposition.
- **Why:** R3 requires the ground for exhibit-shaped changes to be stated; the footnoteblock is a supplement that completes the original's own exhibit mechanism, recorded because the diff alone does not explain it.
- **Verify:** `grep -n 'footnoteblock' original.txt candidate.txt` (absent / L419); `grep -n '\[\[footnote\]\]' original.txt` (L380).
- **Disposition:** Standing.

### 9. Formatting only

- **What:** None. The classifier reports no WS-ONLY blocks and 0 re-indentation blocks over the 44 change blocks; every block in this package carries content or a supplement.
- **Why:** The ground for "none" is the classifier's label census, stated so a reviewer can tell checked-absent from not-considered.
- **Verify:** The label counts in classification.json.
- **Disposition:** None required.

### 10. Porter annotations

- **What:** One porter annotation, and it is load-bearing: the `**訳注:**` at candidate L297 (the classifier's ANNOTATION label, block B12), placed immediately after the info prose. It discloses two things to a future editor: that the JP candidate depends on `theme:basalt-jp` (the JP candidate of the EN Basalt), that no Basalt-equivalent theme is posted on production scp-jp, and that the dependency must be re-checked at posting; and that the header subtitle's kanji were converted to Japanese glyph forms. There are no `[!-- ... --]` comments.
- **Why:** R2 additions are part of the change record; this one is the in-file half of the P1 disposition (the ledger holds the other half), in the P10-sanctioned 訳注 form.
- **Verify:** Read candidate L297.
- **Disposition:** Standing (the dependency it discloses is dispositioned in the per-theme record).

### 11. Dispositions and exceptions

- **What:** The standing dispositions for this theme, each argued in its own section or the per-theme record: (1) the basalt-jp dependency, P1 DISPOSITIONED (posting-procedure convention class) — restated in the per-theme record; (2) the T1 baseline is 2 errors / 1 warn / 2 infos, both errors `pseudo-ref` — the draft-host lines of the baseline file, class (iii) (KB-41); the current candidate's draft-host lines are its two re-hosted file copies (candidate L31, L341), the same class; (3) the render row's dispositions: hidden-rate on both pages (KB-50: machine values recorded only; the rate repair status is owned by the source layer, where item 54 closed it), page-overflow 501–502px@320/375 on the page and up to 1489px@1366 on the sample (KB-33/KB-34 families), and the runtime-hotlink site-theme chain (KB-40, environment layer); no credit-modal line is recorded for this theme; (4) the `--header-title` retention under ruling 2; (5) the T5 residue （漏洞， 版式 terminology) as charged in LOCALIZE-ROWS row 180. Separately, and not a disposition: the usage-exhibit slug flag in the per-theme record is an open item this package hands to the coordinator.
- **Why:** A disposition is a decision with grounds, not an omission; this section exists so the full set can be audited in one place.
- **Verify:** Each item names its deciding check in its own section.
- **Disposition:** DISPOSITIONED (items 1–5 above).

### 12. Verification

- **What:** The evidence behind the stamp: (a) the FIX5 closure is re-derived from this package's own bytes in the per-theme record (grep-based, re-runnable); (b) the classifier (classify_hunks.py 0.1.0, signature table 2026-11-17.1, patterns commit 9c5e9079afb01d30cb9fc4ef9d714e5591eb2ffa) labels 44 change blocks, 28 specific / 15 heuristic / 1 residue, and the residue (B44, the footnoteblock) is resolved in section 8, so no block is unadjudicated; (c) a brace-depth scan of the module-css channel ends at depth 0 on both sides and never goes negative; (d) this package is self-verifying: `python3 review/build_review.py --check` regenerates diff.md from the two byte-faithful copies and compares. Counts in this README are the generator's (difflib): +96/−86. A GNU-diff count of the same pair gives 133 changed lines; the difference is alignment choice, not content.
- **Why:** Verification claims must name the cheapest deciding check and its result, not a general assurance.
- **Verify:** Re-run the greps cited above and `python3 review/build_review.py --check` in this repo.
- **Disposition:** PASS (go-sign re-run, supplement).

## Per-theme record

### The FIX5 closure (ledger item 54 [B])

At ledger time this candidate rendered two rating widgets: the preview credit module plus a bare `[[module Rate]]` in a `[[>]]` float inside the tag gate, the shape the LOCALIZE-S2-D row recorded as Rate 二重化 (type 3). The ledger's item 54 charged it as a defined FIX class executed for other row sets but never for this row, assembly-verified still present in the then-current file (cited at its L286). FIX5-FURNB (commit 25bb0b4) removed the bare Rate block, and the supplement re-judged item 54 FIXED.

Re-derived from this package's bytes: the original carries its own bare Rate at original L271, inside the float at L270–272 — normal for an original. In the candidate, `grep -n 'module Rate' candidate.txt` returns nothing: no bare module and no float wrapper; the gate at candidate L272 opens directly onto the credit block, and the only rating surface is the preview credit module at candidate L274. The removal the supplement records is present and complete in the current bytes.

The companion charges in the same T4 row closed as recorded: the six missing credit fields by the credit waves (ledger §(c3): P3 FIXED; the current block carries all eight, section 1), and the missing interwiki-style frame by the frame waves (ledger §(c3): P6 FIXED; the frame stands at candidate L268–270 in its post-ruling form, section 3).

### The basalt dependency (the P1 disposition, restated)

The candidate's first act is to include `theme:basalt-jp` (candidate L3). That page is this campaign's JP candidate of the EN Basalt theme; it is not a page on production scp-jp, and LOCALIZE-ROWS row 180 charged the dependency as unresolved on production (type 1, a posting-time blocker, with the translator note already consulting staff). The ledger's resolution is §(c3): P1 DISPOSITIONED, posting-procedure convention class — the candidate set is posted as a set, and this theme's dependency resolves when the Basalt candidate it names is posted with it; until then the candidate's own 訳注 (candidate L297) tells any editor exactly that. A reviewer can re-derive the whole state from this package plus one repo check: the include at candidate L3, the note at candidate L297, and `pages/theme:basalt-jp.txt` present in the canonical repo. Nothing about the dependency is hidden, and no edit to this file could remove it without removing the theme's base.

### Flag — the usage example's posting name (open)

The centered install example at candidate L287 reads, in its split-markup form, `[[include :scp-jp:theme:deepspace]]`: the branch prefix was repointed from the original's `:scp-wiki-cn:` (original L275), but the slug kept the original's plain form instead of this candidate's posting name, `theme:deepspace-jp`. Under the campaign's settled rule for usage examples (AGENTS.md §6), the example should name the posting name — the same completion the usage-example sweep applied to decay's and suprematism's equivalents. The sweep did not take this instance, plausibly because the token is split by nested span markup (`@@:scp-jp:@@[[/span]]@@theme:deepspace`), which its extractor did not join. Whether a production `theme:deepspace` exists on scp-jp is not decidable from this repo; on the campaign's own rule the line is wrong either way, since it teaches the reader to include a name this port does not post under. This package documents the candidate as it stands and flags the line for the coordinator (the repair is the single `-jp` insertion inside the exhibit); it is not covered by any ledger disposition.


### Post-package repairs (REFRESH3-D)

FIX-FRAMEADDR (`722ceb5`, sub-shape (B)) lands *before* this package's candidate build (`05dd295`), so the frame at L268 was already remedied in the built candidate; the recopy confirms no byte change from it.

- **FIX-FRAMEADDR, sub-shape (B) — Introduced** (report `R/review-scout/FIX-FRAMEADDR.md` §2; landing `722ceb5c949172bb5185d51ef56ce4119ee4fa91`, 2026-11-17): the original carries no interwiki-style frame and no `theme=` self-address in that role; the porting wave introduced the frame with `theme=` naming its own draft-host `local--code/theme%3Adeepspace-jp/1`, a fragment the page does not carry (delivery is the inline `[[module CSS]]`). Remedy: the single `| theme=...` line was deleted; the frame include and its `priority=1` line are kept. Current candidate frame at L268.
- **FIX-U7 — deepspace usage specimen slug** (report `R/review-scout/FIX-U7.md`; landing `1e34c0b668faf170da8af14c127251af3e35fa26`, 2026-11-17): the split-span specimen at candidate L284 renamed `theme:deepspace` → `theme:deepspace-jp`, completing the posting name. This is the one post-package repair; recopy changed this line only (11,780 → 11,783 bytes).

Stamp treatment follows the jiha-jp / alexylva-university-jp precedents: the regenerated verdict stamp reads STALE, no re-judgement is fabricated, and the frozen GOSIGN2 ledger remains the verdict record.

## Change set outside the two diffed files

The diff covers two files; the port's full change set is slightly larger. (1) `pages/theme-decoration-sample-deepspace-jp.txt` — the decoration sample page used by the render checks. (2) The dependency itself: `pages/theme:basalt-jp.txt`, the JP Basalt candidate this theme layers over (another theme's candidate, in the canonical repo; recorded as this theme's base in section 0). The theme is otherwise standalone in `start-themes.tsv`; it has no fragment or component candidate of its own.

## Multi-wave provenance

The candidate's current state is the product of successive waves, not of a single porting pass: the S2 localization wave (LOCALIZE-S2-D) produced the initial port (base swap, translation, font stacks, and, as later found, the surviving bare Rate and the basalt dependency the T4 lane then charged); the credit waves completed the eight credit fields; the frame waves added the interwiki-style frame; the render checks ran as RENDER-S2-E (CN4); FIX5-FURNB removed the bare Rate (item 54); and the codeaddr remedy later removed the frame's dead `theme=` parameter (722ceb5). Citations, in place of a changelog: GOSIGN2-LEDGER.md §(c3) (localize row), §(c2) (render row), §(e) item 54; GOSIGN2-LEDGER-SUPPLEMENT.md row 54; LOCALIZE-ROWS row 180; T1-ROWS row 216; FIX-CODEADDR.md (population audit). The go-sign re-run over that record is what the Status block certifies.

## License and attribution

- **Title:** 深空 美学版式
- **Author:** Un Party
- **Source:** https://scp-wiki-cn.wikidot.com/theme:deepspace — revision 3
- **License:** Creative Commons Attribution-ShareAlike 3.0 (CC BY-SA 3.0) — license deed: https://creativecommons.org/licenses/by-sa/3.0/
- **Adaptation:** This package holds a Sigma-10 migration port of the work; changes were made. See "Summary" and "Standing sections" in this README for what changed and why. Translator: AI (Muse and its delegated agents), per the campaign's standing attribution rule.
