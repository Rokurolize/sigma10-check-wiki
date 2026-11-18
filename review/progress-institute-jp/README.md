# Review package — theme:progress-institute-jp

<!-- BEGIN GENERATED VERDICT STAMP — do not hand-edit; regenerate with review/build_review.py -->
## Verdict stamp
- Theme: theme:progress-institute-jp — origin CN, population #219 [GOSIGN2-LEDGER (b) row 219]
- Overall: PASS — NOT PASS at the ledger determination (section (e) register); its one OPEN item re-judged FIXED by the FIX5 wave; go-sign issued 2026-11-17 (COMPLETION-REPORT §10) [GOSIGN2-LEDGER (b); GOSIGN2-LEDGER-SUPPLEMENT (d)]
- T1 (source check): FINDINGS (classified) — baseline 2026-11-16: exit 1, 4 errors / 0 warns / 2 infos (hotlink×3, pseudo-ref×1); standing classes dispositioned in register c1 [T1-ROWS row 244; GOSIGN2-LEDGER (b) row 219]
- T2/T3 (render, combined verdict): FINDINGS — [combined T2/T3] report `FINDINGS` — page T2 no machine verdict (exit 2, no summary); sample credit-modal (preview-form) + page-overflow 337–419px@320/375. [RENDER-ROWS-2 (RENDER-S2-F (CN12))]
- Engine coverage: full matrix as run by the lane; coverage not separately caveated in the row (the row records inconclusive runs, carried verbatim above) [RENDER-ROWS-2 row]
- Credit modal: sample credit-modal errors dispositioned preview-form (credit:start-preview has no modal mechanism; GOSIGN-TESTS T2 amendment, 2026-11-16) [RENDER-ROWS-2 (RENDER-S2-F (CN12))]
- T4 (localize patterns + follow-up): FINDINGS — display-affecting findings: 1 [LOCALIZE-ROWS row 218, source LOCALIZE-S2-E]
- T5 (translation text): FINDINGS — the source reports judge T4/T5 jointly; one verdict word covers both [LOCALIZE-ROWS row 218]
- FIX5 re-judgement: item 72 (class B) FIXED — FIX5-FURNB, commit 25bb0b4: duplicate bare Rate block removed [GOSIGN2-LEDGER-SUPPLEMENT (a) item 72]
- Computed against: canonical commit 25bb0b40f10153f1f8bdda252283bb7aa7a76875; candidate file pages/theme:progress-institute-jp.txt sha256:72129ab8a36160e3baf0694822ef8225cafb454fbb413c41bb4d946c77196ce4; record: GOSIGN2-LEDGER.md + GOSIGN2-LEDGER-SUPPLEMENT.md as of the FIX5 head 435a6bb
<!-- END GENERATED VERDICT STAMP -->

## Status

| | |
|---|---|
| Verdict | **PASS** — go-sign re-run (this theme is one of the 286 of 286 pass-eligible themes); the generated stamp above reads PASS, not STALE: this candidate has not changed since the verdict-era commit |
| Blocking items at ledger time | GOSIGN2-LEDGER.md §(e) item 72 [B] (duplicate bare `[[module Rate]]` beside the rate-bearing preview credit module) |
| Re-judgment | GOSIGN2-LEDGER-SUPPLEMENT.md row 72: **FIXED** (FIX5-FURNB, commit 25bb0b4); re-derived from this package's bytes in the per-theme record below |
| Standing items | **DISPOSITIONED** — ledger §(c3): P5 (class (ii) / KB-58), P9 (ruling 2: header/title language out of scope); ledger §(c2) render row: page-overflow 337–419px@320/375, sample credit-modal preview form (KB-32), and a page T2 run that produced no machine verdict (recorded verbatim in the stamp, not converted into one) |
| Flagged in this package | **One defect flag**: the JP font names in the candidate's stacks (Noto Sans JP, Noto Serif JP, Noto Sans Mono CJK JP) are loaded neither in the file nor in its probed base delivery chain; every stack's primary face is loaded, so the exposure is JP-glyph fallback quality (section 4). One provenance record is also corrected: the review/sources.tsv supersession note is wrong (section 0) |
| Go-sign basis | COMPLETION-REPORT.md §10 (go-sign issued; 81 FIXED / 26 DISPOSITIONED / 0 OPEN across the sweep) |
| Named exception | None for this theme (the sweep's single named exception is theme:amethyst-v2, which has no candidate) |

## Provenance

| | Original | Candidate |
|---|---|---|
| Page | theme:progress-institute | theme:progress-institute-jp |
| Wiki | scp-wiki-cn.wikidot.com | SCP-JP Sigma-10 candidate (canonical repo) |
| Reference revision | 23, as recorded in the candidate's credit block: **初訳時参照リビジョン:** 23 | — |
| Source of this copy | Campaign cache `gosign2-lanes/lane-oc-gs-localize-s2-E/orig-progress-institute.txt` (fetched once by the LOCALIZE-S2-E lane), via the mirror store (class COPY, hash-verified against review/sources.tsv) | Canonical file `pages/theme:progress-institute-jp.txt`, copied at worktree HEAD 933c416 |
| Lines / bytes | 835 lines / 36,577 bytes (the last line carries no trailing newline, so `wc -l` reports 834) | 918 lines / 41,511 bytes (same convention; `wc -l` reports 917) |
| SHA-256 | bd99ab3ef3b337f02ac1c4217581a377dceb22bb9e5859e5c5e6fd97805523aa | 72129ab8a36160e3baf0694822ef8225cafb454fbb413c41bb4d946c77196ce4 |

One provenance record is wrong and is corrected here, not silently carried: the review/sources.tsv note for this theme claims the original was superseded upstream after the reference revision. The follow-up artifact the note cites (`gosign2-lanes/lane-oc-gs-localize-s2-E/diff-progress-institute-from23.txt`) records rev 23 → rev 23 with no changes. Upstream latest remains revision 23, the revision this mirror freezes. (The coordinator's harvest corrects the note in sources.tsv itself; this package records the correct form.)

## Summary

A Black Highlighter theme by Carl Ryzen and Mercuresphere for the "Progress" research-center hub: a Dustjacket-era BHL layout whose page doubles as its own documentation (color-swatch exhibits, font specimens, and the standard BHL sample body). The candidate repoints the base delivery to the JP BHL distribution, replaces the CN font stylesheet with Google Fonts loads and JP serif faces, inlines the CN header-animation component (which has no JP counterpart) as an appended module with its attribution, and translates the documentation body. Measured churn (diff.md, the generator's difflib count): +198/−120 in 8 hunks; the 533-line code body is carried almost line-for-line (two asset-URL form fixes are its only in-body changes). The one blocking item (the duplicate bare Rate) is closed and re-derived below; one font load gap is flagged.

## Per-theme record — the FIX5 closure of ledger item 72, re-derived

- **The item.** GOSIGN2-LEDGER.md §(e) item 72 [B]: a duplicate bare `[[module Rate]]` standing next to the preview credit module, which embeds its own rating module, so the page rendered two rating widgets. The ledger's snapshot: current L130, bare, immediately before the credit block (assembly-verified; the checker's double-rate info). The defined FIX class (delete the bare module) had been executed for the Stage-1 and EN row sets but never for this row. The shape's origin is visible in the mirror: the original carries the same `[[>]] [[module Rate]] [[/>]]` at L131–133 beside its CN credit module — functional there, because the CN credit:start module is not rate-bearing; the JP preview credit module is, so the ported copy duplicated it.
- **The re-judgement.** GOSIGN2-LEDGER-SUPPLEMENT.md row 72: FIXED, by FIX5-FURNB, commit 25bb0b4: "duplicate bare Rate block removed".
- **What the fix was supposed to change.** Delete the bare Rate module and its `[[>]]` container, leaving the preview credit module as the page's only rating surface; no other line was to move.
- **Re-derivation from this package's bytes.** (1) The fix commit's diff for this file is exactly −4 lines at one locus: `[[>]]`, `[[module Rate]]`, `[[/>]]`, and one blank line, directly above `[[include :scp-jp:credit:start-preview]]`. (2) Current bytes: `grep -c 'module Rate' candidate.txt` returns 0; the credit block stands at candidate L129–141 with no container above it. (3) Completeness: the rating surface that remains is the rate-bearing preview module itself; nothing else in the file rendered a second widget. (4) No post-verdict change exists to explain away: the file's last content change is 25bb0b4 itself, which is why the generated stamp reads PASS rather than STALE. The closure holds on the current bytes.

## 0. Header / provenance

- What: the original's head is two delivery modules ahead of the gate: a gated module importing the EN BHL distribution from jsdelivr (original L1–6) and an ungated module importing its own code fragment from scp-wiki-cn.wdfiles.com (L8–10), separated from the body by a `====` rule (L11, dropped in the candidate; appendix B3). The candidate's head is the JP form of the same stack: the base include (candidate L1), two interwiki frames carrying the JP BHL distribution at priorities 1 and 2 (L3–11), and a module importing its own fragment 1 from the draft host (L13–15), then the localized gate `[[iftags +テーマ]]` (L17). Provenance route: derivation from the original at revision 23 (mirror class COPY); the wrong supersession note is corrected in the Provenance section above.
- Why: P4/T9 base delivery from the JP distribution and P6/T3 frame layering (normalize before base, KB-07 state recorded in section 3).
- Verify: `sha256sum original.txt` against the review/sources.tsv row; read candidate L1–17 against original L1–13.
- Disposition: provenance recorded, with the note correction above.

## 1. Credit and attribution

- What: the original's credit furniture is the CN credit:start/end pair (original L135–139) naming 作者： [[*user Carl Ryzen]]、[[*user Mercuresphere]]. The candidate carries the eight-field preview credit block (candidate L129–141): 著作権者 names both authors, exactly as the original does (no pointer, no omission); 翻訳責任者 AI under ruling 3; 初訳時参照リビジョン 23; the source link names the CN original on scp-wiki-cn.wikidot.com, the host recorded in review/sources.tsv. Two credit-prose lines inside the block carry attribution beyond the author field: the header animation's basis in AI_Mayca's "BHL Header Animation" (component:bhl-animation, CC BY-SA) at candidate L139, and the font line (L140) naming Inter, Recursive, and Shippori Mincho B1 with their license. The original's bare Rate module is removed (item 72, per-theme record). Neither side carries a license box; the TASL record stands in the credit block and the component's CC BY-SA is credited in the prose and in the appended module's own comment (candidate L848–849).
- Why: P3/T1 credit swap; attribution lines beyond the author field are part of the credit record (the animation component is a base work this theme incorporates, and ruling 4's port-by-inlining makes its credit load-bearing).
- Verify: read candidate L129–141 against original L135–139; `grep -c 'module Rate' candidate.txt` returns 0.
- Disposition: standing; ledger §(c3) records P3 FIXED by the credit waves for this row.

## 2. Includes and components

- What: four include-level changes. (a) The base include `:scp-jp:theme:black-highlighter-theme` is added at the head (candidate L1) — the population's base-include form for BHL themes (60 candidate files use the same form; the name is the production BHL page's, per the AGENTS.md §6 distribution convention). (b) The two interwiki frames are added (L3–11). (c) The credit includes swap to the preview pair (section 1). (d) The original's tail include `:scp-wiki-cn:component:bhl-animation` (original L835, after the gate close) is not repointed but inlined: SCP-JP has no equivalent component, so its CSS stands as the appended module of section 3 with attribution (candidate L847–917). The usage example is repointed to match the candidate's own delivery: its two lines now name `:scp-jp:theme:black-highlighter-theme` and `:scp-jp:theme:progress-institute-jp` (candidate L202–203; COMPONENT-SWAP block B12). No include is duplicated (the two frames name different targets at different priorities).
- Why: P1 repointing and T8 component handling; ruling 4 (a component the theme needs is ported with the theme — here by inlining, the only form available).
- Verify: `grep -n '\[\[include' original.txt candidate.txt` and compare the two lists.
- Disposition: standing; no include in the candidate points at scp-wiki-cn.

## 3. Delivery and code loading

- What: three delivery channels, each the JP form of an original channel. (a) Base: the original's gated jsdelivr module (Nu-SCPTheme BHL, original L2–5) becomes the base include plus the two scp-jp.github.io frames (candidate L1–11; priority 1 normalize, priority 2 base — the layering the original's import order expressed). (b) Own CSS: the original's code exhibit (original L297–830) is imported by its head module from scp-wiki-cn.wdfiles.com fragment 1; the candidate's exhibit (candidate L308–842) is imported by its head module (L13–15) from the draft host's fragment 1. Self-delivery census: exactly one code block in the candidate, counting every form (`[[code]]`, `[[code type="CSS"]]`, other typed forms); the single reference names block 1, and block 1 is the stylesheet itself (533 content lines); no entry in FIX-CODEADDR.md or FIX-NAVLA.md names this theme. (c) The header-animation component: the original includes it after the gate (original L835); the candidate appends its CSS as a module at the same relative position, after `[[/iftags]]` (candidate L847–917), with the component's banner and a porter comment recording the inlining and its ground (no JP equivalent). Dropped with the head rework: the hidden styleFrame embed (original L125–129, an iframe to scp-wiki-cn's nav:side styleFrame.html?bhl) — its framing role is taken over by the base include and frames (the KB-43 environment family).
- Why: P4/T9 (JP distribution), P6/T3 (frame layering), ruling 4 (component port by inlining).
- Verify: read candidate L1–15 and L847–849; `grep -n 'styleFrame' candidate.txt` (no matches).
- Disposition: the draft-host fragment import is class (iii) draft form (the T1 register's pseudo-ref×1); the styleFrame drop is recorded above with its ground.

## 4. Fonts and assets

- What: the original loads one font stylesheet, the wanderers-dustjacket typefaces.css from fastly.jsdelivr (original L300, Crimone's font set: Zuijin and the Wanghanzong faces its specimens name), and its title stack is a self-reference (`--title-font: var(--title-font)`, original L310). The candidate replaces the import with three Google Fonts loads at the code head (candidate L311–313: Inter, Recursive, Shippori Mincho B1), replaces the CN faces in the stacks (body/UI on Inter with JP fallbacks; title on Shippori Mincho B1; the swatch module's `zuijinregular` becomes "Shippori Mincho B1", "Noto Serif JP", serif at candidate L35), and repairs the self-referential title variable to a real stack (candidate L323). **Flag (font fallback load gap, KB-16).** Three JP names in the stacks are loaded neither in the file nor in the base chain: "Noto Sans JP" (body, candidate L320; UI, L321), "Noto Serif JP" (title, L323; mono, L324; swatch module, L35), and "Noto Sans Mono CJK JP" (mono, L324, and the specimen prose at L301). The in-file imports load none of them; a probe of the base distribution for this package (https://scp-jp.github.io/Black-Highlighter/css/min/black-highlighter.min.css, HTTP 200) shows it loads Inter, Recursive, and M PLUS 1p — not the Noto faces. The exposure is bounded and stated plainly: every stack's primary face IS loaded (Inter, Shippori Mincho B1, Recursive), and OS JP fonts (Hiragino Kaku Gothic ProN, Yu Gothic, Meiryo, Yu Mincho) stand behind the unloaded names in the same stacks, so JP glyphs render in an OS font rather than in the named webfonts. "Noto Sans Mono CJK JP" is additionally not a Google Fonts family at all (the skipos record: probed 400 in three forms; theme:basalt-jp names it equally unloaded in a fallback stack, the population form this candidate follows). Assets: the three evernight-aquarium.wikidot.com image URLs (the author's own host, both sides) keep their host and paths with http→https and colon encoding applied (logo, candidate L317; header backgrounds, L409 and L813 — the classifier's CSS-BODY heuristic blocks B54/B57 are the two background lines); they are the ledger's P5 disposition and the T1 hotlink×3.
- Why: P7/T5 font supplement and KB-16's load/use census (a font named in a stack but loaded by no import or font-face in the file or its base delivery chain is a flag, with the chain probed rather than assumed); P5/KB-01 for the asset URL forms.
- Verify: `grep -n '@import' candidate.txt` (three Google loads); `grep -n 'Noto' candidate.txt` (the stack and specimen lines); the base-chain probe is re-runnable with one fetch of the URL above.
- Disposition: P5 DISPOSITIONED (class (ii) / KB-58); **the font flag stands for adjudication**: either load the two Noto faces in the code head (the paradigm family's FIX5 form) or record the OS-fallback state as this theme's disposition with the probe evidence above.

## 5. Header, sidebar, site furniture

- What: the `:root` block is re-scoped and given real values: `:root:lang(cn)` → `:root:lang(ja)` (candidate L316); `--theme-base` / `--theme-id` / `--theme-name`, which the original fills with one placeholder string in all three slots （黑色标记笔， original L303–305), become "black-highlighter" / "progress-institute" / "「進歩」研究センター" (candidate L317–319); the header logo variable keeps the author's host with the scheme and encoding fixes of section 4. The header animation itself is the inlined component (section 3). Sidebar and menu variables are carried unchanged (the swatch variable block is byte-identical below the head lines).
- Why: P9/T6 header variables and the lang scoping the JP environment requires; the placeholder repair is recorded because a reviewer comparing the `:root` heads will see three changed values and should know the original's were copies of one string, not three considered values.
- Verify: read candidate L316–324 against original L302–312.
- Disposition: standing; the header-language item is dispositioned P9 under ruling 2 in the ledger, and the candidate's JP theme-name is the port's own form.

## 6. Text translation

- What: the documentation body is translated throughout (original L141–296 → candidate L143–306): the swatch exhibits' captions, the about text naming both authors, the usage instructions, and the standard BHL sample body (headings, collapsibles, font specimens) — TRANSLATION-ANCHORED blocks B8–B49 with the unanchored mass resolved in the appendix. Reader-visible CSS strings (R1/KB-18): the `content:` strings inside the code body are translated (CONTENT-STRING blocks B55, B56, B58), and the string-valued `--theme-name` is section 5's material. GLYPH-FORM blocks B52–B53 are the font-stack lines themselves, where the SC face names become JP forms (section 4). The specimen prose at candidate L300–301 restates the font facts in JP (title: Shippori Mincho B1 / Noto Serif JP; mono: Recursive / Noto Serif JP / Noto Sans Mono CJK JP) where the original named Zuijin / 王汉宗魏碑体 and Recursive / 仿宋及思源宋体 (original L290–291).
- Why: P10 body translation, with R1 separating reader-visible in-CSS strings from porter-visible comments (the code body's English BHL comments are the original's and are retained, as in the original's own distribution form).
- Verify: read candidate L143–306 against original L141–296 section by section; the exhibit order is unchanged.
- Disposition: standing (the port itself).

## 7. Links

- What: the credit source link (candidate L137) names the CN original on scp-wiki-cn.wikidot.com, the host recorded in review/sources.tsv (no host substitution). The about text's author links name Carl Ryzen and Mercuresphere in `[[*user …]]` form on both sides. No prose link in the candidate targets the un-suffixed `theme:progress-institute` name; the usage example's two lines are section 2's repoints.
- Why: P11 link localization; a theme's link surface includes the example it teaches, which is why the example's base line matters (it now teaches the JP base include the candidate itself uses).
- Verify: `grep -n 'theme:progress-institute' candidate.txt` (only the -jp self-reference and the CN source URL).
- Disposition: standing; no dead-target prose link stands in this file.

## 8. Structure

- What: the candidate follows the localize.md closing rule closely: variable names, selectors, and channel order are preserved, and the JP additions stand at the end. Specifically: the code body is carried line-for-line outside its head block (the only in-body changes are the two asset-URL lines of section 4); the swatch module is preserved with one font line changed (candidate L35); the documentation exhibits keep their order; and the one appended element, the animation module, stands after the gate exactly where the original placed its component include. The two deletions are the bare Rate (item 72) and the styleFrame embed (section 3), plus the `====` separator line at the head (appendix B3). A brace-depth scan of both files' CSS regions (comments and strings stripped) ends at depth 0 in every region with no negative excursion: no displaced-brace shape is present.
- Why: the closing rule is what keeps a follow-up diff applicable; this section records that the port obeyed it and names the three deletions so none reads as silent.
- Verify: compare the structural maps: `grep -n '\[\[module\|\[\[code\|\[\[include\|\[\[iftags' original.txt candidate.txt`.
- Disposition: standing (each change grounded above).

## 9. Formatting only

- What: none. The classifier counts 0 re-indentation blocks; the code body retains the original's indentation, and no hunk in diff.md is whitespace-only.
- Why: formatting churn is disclosed as its own class (R7); here there is none to disclose.
- Verify: diff.md's 8 hunks; each carries content.
- Disposition: none required.

## 10. Porter annotations

- What: one annotation: the appended module's header comment (candidate L848–849), which attributes the inlined CSS to component:bhl-animation by AI_Mayca (SCP-CN), shared under CC BY-SA, and states the inlining ground (SCP-JP has no equivalent component). No translator notes or editor lines stand in the body; a direct read for `[!--` and 訳注 markers returns none, which is why this section is not written as "none" from the skeleton alone — the module comment rides inside the EXHIBIT-RESTRUCTURE-labelled block B59 and the classifier's ANNOTATION label did not fire on it.
- Why: R2 (porter annotations are part of the change record, and this one is load-bearing: it is the component's license attribution).
- Verify: read candidate L847–856.
- Disposition: standing.

## 11. Dispositions and exceptions

- What: the standing dispositions for this theme, each argued in its own section: (1) P5 asset hosts on the author's own wiki, class (ii) / KB-58 (section 4); (2) P9 header/title language, ruling 2 (section 5); (3) render-row dispositions: page-overflow at mobile widths and the credit-modal preview form (ruling 5; KB-32), plus the page T2 run that produced no machine verdict, which the stamp carries verbatim rather than as a verdict (section 12); (4) the draft-host fragment import, class (iii) (section 3). The class (i) defect (item 72) was fixed, not dispositioned. The font flag of section 4 is not a disposition; it is reported for adjudication with its probe evidence.
- Why: a disposition is a decision with grounds, not an omission; inconclusive evidence is recorded as inconclusive.
- Verify: each item names its deciding check in its own section.
- Disposition: DISPOSITIONED (items 1–4 above). Patterns cited in this package are patterns/ at commit 9c5e9079afb01d30cb9fc4ef9d714e5591eb2ffa (KB-01, KB-07, KB-16, KB-32, KB-43, KB-58).

## 12. Verification

- What: (a) T1 baseline for this file: exit 1, 4 errors / 0 warnings / 2 infos (hotlink×3, pseudo-ref×1, the standing classes of sections 3–4), recorded in the stamp; (b) T2/T3: the sample produced the dispositions above; the page run was inconclusive (exit 2, no summary) and is carried as such; (c) T4 records 1 display-affecting finding for this row — the pattern-3 Rate charge that became item 72, closed in the per-theme record; the T4 follow-up artifact for the reference revision is the rev23→rev23 no-change record corrected in the Provenance section; (d) this package is self-verifying: `python3 review/build_review.py --check` regenerates diff.md from the two byte-faithful copies and compares, and the stamp reads PASS because no post-verdict change exists. Counts in this README are the generator's (difflib, autojunk off): +198/−120.
- Why: verification claims must name the cheapest deciding check and its result, not a general assurance.
- Verify: re-run `python3 review/build_review.py --check` in this repo; `grep -c 'module Rate' candidate.txt` (0) for the item-72 closure.
- Disposition: PASS (go-sign re-run, supplement), with the section-4 font flag reported for adjudication.

## Appendix — residue blocks and unanchored mass

- R1 — B3 (residue; orig L11 → cand L16): the `====` separator line between the original's delivery head and its gate, dropped in the candidate's head rework. Assigned to section 8.
- Heuristic B54 (orig L397 → cand L409) and B57 (orig L801 → cand L813), labelled CSS-BODY: the two header-background asset URL lines (http→https, colon encoding, same host). Assigned to section 4.
- Heuristic TRANS-UNANCHORED mass (B10–B11, B14–B15, B24, B26–B36, B42–B46): single-line and short-span pairs in the sample body where the script delta defeats the anchor matcher (the classifier lists 14 such blocks, most one line each). Resolved by shape: they are the BHL sample body's translation, exhibit for exhibit in the original's order, with no content class of their own. Assigned to section 6.
- B59 (orig L835 → cand L847–917), labelled EXHIBIT-RESTRUCTURE with HEADERVAR: the differ aligns the original's one-line component include against the appended animation module. The label's exhibit reading does not apply; the block is the component port of sections 2, 3, and 10.

## Change set outside the two diffed files

The diff covers two files; the port's record is slightly larger. (1) `pages/theme-decoration-sample-progress-institute-jp.txt` — the decoration sample page used by the render checks. (2) The base dependency, `pages/theme:black-highlighter-theme-jp.txt` (the JP BHL candidate the head include and frames draw on), is a shared distribution file, not this theme's port artifact; it is named here because the candidate's delivery is incomplete without it. No fragment files belong to this theme itself.

## Multi-wave provenance

The candidate's current state is the product of successive waves: the Stage 2 CN12 integration (72e3efa) produced the initial port (translation, JP base delivery, font replacement, the animation inlining, and, as later found, the duplicated bare Rate it inherited from the original's shape); FIX-CREDIT-D (1869877) normalized the translator attribution; and FIX5-FURNB (25bb0b4) removed the bare Rate (item 72), the file's last content change. Citations, in place of a changelog: GOSIGN2-LEDGER.md §(c3) (localize row), §(c2) (render row), §(e) item 72; GOSIGN2-LEDGER-SUPPLEMENT.md row 72; REPORT-GOSIGN2-FIX5-FURNB.md (progress-institute section). The go-sign re-run over that record is what the Status block certifies.

## License and attribution

- **Title:** 远视 主题版式
- **Author:** Carl Ryzen、Mercuresphere
- **Source:** https://scp-wiki-cn.wikidot.com/theme:progress-institute — revision 23
- **License:** Creative Commons Attribution-ShareAlike 3.0 (CC BY-SA 3.0) — license deed: https://creativecommons.org/licenses/by-sa/3.0/
- **Adaptation:** This package holds a Sigma-10 migration port of the work; changes were made. See "Summary" and "Standing sections" in this README for what changed and why. Translator: AI (Muse and its delegated agents), per the campaign's standing attribution rule.
