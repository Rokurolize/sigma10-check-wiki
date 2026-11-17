# Review package — theme:enlightened-eyes-jp (EN → JP port)

<!-- BEGIN GENERATED VERDICT STAMP — do not hand-edit; regenerate with review/build_review.py -->
## Verdict stamp
- Theme: theme:enlightened-eyes-jp — origin EN, population #85 [GOSIGN2-LEDGER (b) row 85]
- Overall: STALE — candidate file changed since the verdict was computed (verdict against 435a6bb-era content, file sha256 now 305a6443889ad026b6d65b69fe5a95d90f7c3b750b9e059711a34bc13f8898c9); verdict not carried over, re-judgement required
> verdicts below describe the pre-change file
- T1 (source check): FINDINGS (classified) — baseline 2026-11-16: exit 1, 6 errors / 0 warns / 1 info (pseudo-ref×6); standing classes dispositioned in register c1 [T1-ROWS row 85; GOSIGN2-LEDGER (b) row 85]
- T2/T3 (render, combined verdict): FINDINGS — [combined T2/T3] report `FINDINGS` — page-overflow everywhere incl. 1489px@1366, 789px@768, ~440px@≤375; sample credit-modal; 1366 sidebar-collapsed with own ☰; WebKit CC "S". [RENDER-ROWS-1 (RENDER-S2-B)]
- Engine coverage: full matrix as run by the lane; coverage not separately caveated in the row [RENDER-ROWS-1 row]
- Credit modal: sample credit-modal errors dispositioned preview-form (credit:start-preview has no modal mechanism; GOSIGN-TESTS T2 amendment, 2026-11-16; ROWS-1 phrases the line bare and takes the disposition from the part header) [RENDER-ROWS-1 (RENDER-S2-B)]
- T4 (localize patterns + follow-up): FINDINGS — display-affecting findings: 2 [LOCALIZE-ROWS row 85, source LOCALIZE-S2-B]
- T5 (translation text): FINDINGS — the source reports judge T4/T5 jointly; one verdict word covers both [LOCALIZE-ROWS row 85]
- FIX5 re-judgement: none — no OPEN items at the ledger determination [GOSIGN2-LEDGER (b) row 85]
- Computed against: canonical commit 4176cc76aa668e42056010548f62a1db8d06a32e; candidate file pages/theme:enlightened-eyes-jp.txt sha256:305a6443889ad026b6d65b69fe5a95d90f7c3b750b9e059711a34bc13f8898c9; record: GOSIGN2-LEDGER.md + GOSIGN2-LEDGER-SUPPLEMENT.md as of the FIX5 head 435a6bb
<!-- END GENERATED VERDICT STAMP -->

## Status

| | |
|---|---|
| Verdict | **PASS** — passed at the ledger determination; this theme had no OPEN items and no §(e) register entry (GOSIGN2-LEDGER (b) row 85) |
| Standing items | **DISPOSITIONED** — T1 pseudo-ref ×6 (class (ii), section 11); the render row's four items (KB-33/KB-34 overflow family; KB-32 preview-form credit modal; the theme's own hamburger pattern recorded as working; KB-36 WebKit CC glyph, section 11); T4's P4 item dispositioned in the ledger §(c3) line and overtaken in the bytes by FIX-P4 (sections 3 and 11) |
| Package-level flag | **Own-layer delivery addresses the wrong code page** — the candidate's delivery lines import its own /1, but its CSS exhibit is the page's sixth code block, so /1 serves a prose sample and the theme's own CSS is not delivered by its own machinery (probe-verified on the draft host, sections 3 and 11). Unrecorded in the ledger; flagged here and in the batch report for the coordinator. The original's tail-module cursor rules are likewise absent (section 3) |
| Go-sign basis | COMPLETION-REPORT.md §10 (go-sign issued; 81 FIXED / 26 DISPOSITIONED / 0 OPEN across the sweep) |
| Named exception | None for this theme (the sweep's single named exception is theme:amethyst-v2, which has no candidate) |

## Provenance

| | Original | Candidate |
|---|---|---|
| Page | theme:enlightened-eyes | theme:enlightened-eyes-jp |
| Wiki | scp-wiki.wikidot.com | SCP-JP Sigma-10 candidate (canonical repo) |
| Reference revision | 51 (first translation; the candidate's credit block records 初訳時参照リビジョン: 51) | — |
| Source of this copy | Campaign cache `gosign2-lanes/lane-oc-gs-source-s2-2/mirror-enlightened-eyes.txt`, via the mirror store (class COPY, hash-verified against review/sources.tsv) | Canonical file `pages/theme:enlightened-eyes-jp.txt`, copied at worktree HEAD 5ab991e |
| Lines / bytes | 2,722 lines / 79,019 bytes | 2,611 lines / 84,448 bytes |
| SHA-256 | 5e8e7ac7b561bbfc6a56199fff197787e375eedff4afca65ca375f4593bf0de0 | 10c47a8bc61865aea9b1cf5dd73dc8950e856d5444a84fea72183efec2e23cf7 |

Wave history: the candidate was created by the Stage 2 EN9 integration (commit 7aed5b7, the LOCALIZE-S2-B wave's port) with its whitespace normalization follow-up (5b6dbe2), then touched by f1138e4 (FIX-P4: base-theme CSS imports repointed to the JP port candidates — section 3) and last by a497307 (FIX4-MECH: duplicate @import removal, KB-65; the verdict stamp is computed against this commit). Kind note (sources.tsv K5b-3): the candidate layers over theme:basalt-jp, so this package's diff covers the theme's own layer; the base is a separate candidate with its own package.

## Summary

Enlightened Eyes is a Basalt-based theme for Parawatch fiction, and its port has one structural decision that dominates everything else: the original builds its sample posts with an EN component (`component:parawatch-post`, ten start/end include pairs) that SCP-JP does not have, so the candidate writes the component's decorated divs directly and explains the substitution in two translator notes. That single decision accounts for most of the churn (diff.md, Tier 2 format: +541/−652, 1,193 changed lines in 175 change blocks / 7 diff sections), for the 25 EXHIBIT-RESTRUCTURE blocks, and — indirectly — for this package's defect flag: consolidating the sample code blocks moved the CSS exhibit from the tenth code block to the sixth, while the candidate's delivery lines address its own code page as /1, so the framed delivery loads a prose sample instead of the theme's CSS (section 3, probe-verified). The rest of the port is conventional and well-formed: Basalt base repointed to the JP port by FIX-P4, fonts moved from Bunny Fonts to Google Fonts with Noto JP faces added, credit and license furniture in JP form, body translated throughout.

## Class summary

Auto-classification by review/classify_hunks.py (signature table 2026-11-17.1): 175 change blocks — 69 specific (39.4%), 103 heuristic (58.9%), 3 residue (1.7%), 0 skipped. Pattern citations below name the KB entry; the patterns/ tree state cited throughout is commit 9c5e9079afb01d30cb9fc4ef9d714e5591eb2ffa.

| Label | Blocks |
|---|---|
| ANNOTATION | 1 |
| BARE-RATE-DEL | 1 |
| COMMENT-TEXT | 1 |
| CREDIT-PREVIEW | 1 |
| CSS-BODY | 3 |
| DELIVERY-HOST | 2 |
| DRAFT-HOST | 6 |
| ESCAPED-INCLUDE | 1 |
| EXHIBIT-RESTRUCTURE | 25 |
| FONT-IMPORT | 1 |
| IFTAGS | 2 |
| INCLUDE-REPOINT | 2 |
| JPFONT-LOAD | 1 |
| LICENSE-BOX | 2 |
| SELF-DELIVERY | 3 |
| TASL-FIELDS | 1 |
| TRANS-UNANCHORED | 96 |
| TRANSLATION-ANCHORED | 44 |
| WS-ONLY | 14 |

Adjudication for this README (every A/D-tier block and every primary family was read against the bytes): the 25 EXHIBIT-RESTRUCTURE primaries are, for once, real restructurings — the Parawatch component exhibits rebuilt as direct divs (section 8) — not the label's usual false-fire on include repoints. The three residue blocks are seams of that same restructuring (appendix). The TRANS-UNANCHORED mass is the body translation, verified in bulk against the mirror for this README. The one block the classifier could not see as a problem is the delivery addressing (block B175 and the head lines): it is adjudicated from the probe evidence in section 3. After adjudication no block is left unexplained.

## Standing sections

### 0. Header and provenance frame

- **What:** Theme theme:enlightened-eyes-jp; original theme:enlightened-eyes on scp-wiki at reference revision 51; candidate `pages/theme:enlightened-eyes-jp.txt`. Provenance route: derived from the original at the reference revision by the LOCALIZE-S2-B wave (sources.tsv kind: K5b-3, layered — the candidate layers over theme:basalt-jp and this diff covers the theme's own layer only). The frame: the candidate opens with a module CSS importing its own /1 from the draft host (candidate L2), then three `:scp-jp:component:interwiki-style` includes — priorities 1 and 2 both delivering theme:basalt-jp /1 (the two frame slots the original fills with Basalt's normalize and bedrock CDN files, original L3–4), priority 3 delivering its own /1 (candidate L5–17) — then the localized gate `[[iftags +テーマ]]` (candidate L19). The original opens with the gate and a module importing the two Basalt CDN files from cdn.scpwiki.com, and delivers its own CSS at the tail (section 3).
- **Why:** Section 0 declares the route and the layer stack so later counts are read against the right baseline; the gate's tag is P2, the stack is P6/T3 with T9 base delivery (sections 2–3).
- **Verify:** The sources.tsv row for enlightened-eyes-jp; `sha256sum original.txt` against the Provenance table; the frame lines at candidate L1–19.
- **Disposition:** Standing (the route itself); the frame changes are recorded in sections 2 and 3, including the flag that attaches to them.

### 1. Credit and attribution

- **What:** The original's credit furniture is its bare Rate arrangement in the head region; the candidate deletes it (BARE-RATE-DEL ×1) and installs the JP preview block (candidate L20–29) with the eight ruling-3 fields (title エンライトンド・アイズ テーマ; 翻訳責任者 AI; 翻訳年 2026; 原題 Enlightened Eyes Theme; 著作権者 JakdragonX; 作成年 2026; 初訳時参照リビジョン 51; the source link, candidate L28, naming scp-wiki.wikidot.com, the original's recorded host). The candidate also adds the closing license box the original lacks (`:scp-jp:component:license-box-backend` at candidate L704, `license-box-end` at L723; blocks B152, B154), whose entries document the theme's image files (the turbines photograph and the blinded-rook logo, both re-hosted to the draft host in the body exhibits at candidate L71 and L605).
- **Why:** P3/T1: the preview credit module is the rate-bearing JP form, so the bare Rate is deleted rather than duplicated (KB-09); the license box is the JP attribution supplement for a theme with third-party image files.
- **Verify:** `grep -n 'module Rate\|credit:\|license-box' candidate.txt` — no bare Rate, one preview pair, one license-box pair; read candidate L20–29.
- **Disposition:** FIXED (GOSIGN2-LEDGER §(c3): P3 credit fields FIXED, credit waves, checker-verified).

### 2. Includes and components

- **What:** The usage exhibit's escaped includes are repointed as built `:scp-wiki:theme:basalt` → `:scp-jp:theme:basalt` and `:scp-wiki:theme:enlightened-eyes` → `:scp-jp:theme:enlightened-eyes` (block B39, candidate L293–294) — repoints that changed the branch prefix but kept the plain slugs, so both exhibits named pages that do not exist on scp-jp; the usage-example population sweep has since completed both names on the same lines, the cross-reference to `:scp-jp:theme:basalt-jp` (candidate L293) and the self-reference to `:scp-jp:theme:enlightened-eyes-jp` (candidate L294) (SWEEP-USAGE.md; canonical commit b5cb724). The body's two image-block includes keep the bare `component:image-block` form with their `name=` parameters re-hosted to the draft host and their captions translated (candidate L71, L605). The component story of this theme is the Parawatch one, and it is structural rather than a repoint: the original's ten `:scp-wiki:component:parawatch-post` start/end pairs (original L31–322) have no JP counterpart to repoint to, so the candidate drops the component and writes the divs it produced (section 8), documenting the substitution in its translator notes (section 10).
- **Why:** P1 (KB-15) governs the repoints: each names the JP counterpart that exists. The exhibit repoints as built satisfied the branch half of that rule only — their plain slugs named no JP pages — and the sweep's completions to the posting names (basalt's JP port under `theme:basalt-jp`, this candidate itself under `theme:enlightened-eyes-jp`) are what bring them under the rule. The Parawatch case is the same rule's other branch — where no counterpart exists, the port must reproduce the component's reader-visible output by other means or record a named exception; the candidate reproduces the output inline, which is the stronger branch, and says so in-file.
- **Verify:** `grep -n 'parawatch-post' candidate.txt` returns only the translator notes' mentions; `grep -n '\[\[include' candidate.txt` shows the frame, credit, license, image-block, and exhibit lines, all JP forms.
- **Disposition:** Applied; the component substitution is part of the port as integrated (no ledger item charges it).

### 3. Delivery and code loading

- **What:** The original delivers in two places: its head module imports Basalt's two CDN files (original L3–4), and a tail module after the gate (original L2699–2722) imports its own code page /10 — the CSS exhibit, which is the page's tenth code block — and adds inline cursor rules (section 4's tail note). The candidate consolidates delivery at the head (module import of its own /1, candidate L2; frame priorities 1–3, candidate L5–17) and has no tail module. Two byte-level findings attach to this consolidation, both flagged for the coordinator in section 11:
  (1) **The own-layer address is wrong.** The candidate addresses its own code page as /1 in both the head module (candidate L2) and the frame (candidate L15), but its CSS exhibit is the page's **sixth** code block: five sample code blocks (candidate L418, L428, L437, L457, L483, the Parawatch span samples) precede the exhibit at candidate L733. Probe evidence (2026-11-17, one fetch each): `https://sigma10-jp-test.wikidot.com/local--code/theme:enlightened-eyes-jp/1` serves the pw-mention span sample (the candidate L418 block), and `/6` serves the theme's CSS exhibit, banner and imports matching candidate L733–751. So as deployed, the head import and the priority-3 frame slot load sample markup (invalid as CSS, ignored) and the theme's own layer is not delivered by its own machinery. The original's /10 was correct against its own count (nine sample blocks, exhibit tenth, tail import /10). The renumbering is a side effect of the Parawatch consolidation (section 8), which reduced the sample blocks from nine to five without adjusting the address the port had already written as the conventional /1.
  (2) **The tail module's cursor rules are absent.** The original's tail module carries three `cursor: url(data:…)` rules and a `cursor: text` rule (original L2702–2721) — the theme's custom eye cursors. The candidate contains no cursor rule anywhere (`grep -n 'cursor' candidate.txt` returns only `cursor: initial` inside the exhibit, candidate L2586, which the original also has). No record dispositions the cursor loss.
  The base delivery, by contrast, is correct and was repaired where it was not: at T4 time the frame args and the exhibit's Basalt import still named the EN CDN (LOCALIZE-ROWS row 85, item (a)); FIX-P4 (commit f1138e4) repointed both to theme:basalt-jp /1 on the draft host (candidate L7, L11, L742), which is what the current bytes show. The ledger §(c3) line still reads "P4 DISPOSITIONED (delivery class (ii): original-state CDN delivery)" — the pre-repair disposition; the bytes have since overtaken it, and this README follows the bytes.
- **Why:** P4/T9 for the base repoint (the JP port candidate is the delivery source, per ruling 4 and the cross-theme dependency rule). Finding (1) is a delivery-class defect by the campaign's own standard (a candidate whose framed code page does not serve its CSS fails the delivery check the frame exists to satisfy); finding (2) is an unrecorded content loss of reader-visible behavior. Both are recorded here rather than repaired, because this lane does not edit candidates; the repair (repoint the own-layer lines to the exhibit's actual address, or restructure so the exhibit is the first code block, and restore the cursor module) belongs to a coordinator-landed fix wave.
- **Verify:** The two probe URLs above are fetchable from this repo's records alone (the draft host is named in the candidate's own lines); `grep -n 'local--code' candidate.txt` shows the /1 addresses at L2, L7, L11, L15, L742; `grep -n '\[\[code' candidate.txt` shows the six code blocks in order.
- **Disposition:** The base repoint: FIXED (FIX-P4, commit f1138e4; the §(c3) DISPOSITIONED wording is superseded in the bytes). Findings (1) and (2): **flagged, unrecorded** — see section 11.

### 4. Fonts and assets

- **What:** The exhibit's import head is rebuilt (block B156): the four Bunny Fonts imports (Red Hat Text, Reddit Mono, Fragment Mono, Space Mono from fonts.bunny.net, original L833–836) move to Google Fonts at the same families and ranges (candidate L744–747), and two JP faces are added under the exhibit's own `日本語フォント (JP localization)` comment — Noto Sans JP and Noto Serif JP (candidate L750–751, JPFONT-LOAD) — with the stacks gaining 'Noto Sans JP' fallbacks (e.g. `--body-font-primary: 'Red Hat Text', 'Noto Sans JP', sans-serif`). FIX4-MECH (commit a497307) later removed a duplicate @import from this file (KB-65). Assets: the two body images are re-hosted from scp-wiki file storage to the draft host (candidate L71, L605); the header logo variable in the exhibit points at the same re-hosted rook file. The hatch-pattern background is an inline SVG data URI carried on both sides (candidate L1003); its `http://www.w3.org/2000/svg` string is the namespace inside the data URI, not an external reference.
- **Why:** P7/T5 with KB-16: the port loads the JP faces its stacks name, from the same provider family as the original's Latin faces. The Bunny→Google move keeps the four families identical (the T4 bar: a stack rewrite that drops a named face is a defect; none is dropped).
- **Verify:** Read candidate L742–751 against original L832–836 in diff.md; `grep -n 'bunny.net' candidate.txt` returns nothing.
- **Disposition:** Standing (part of the port); no font item dispositioned.

### 5. Header, sidebar, and site furniture

- **What:** The header variables sit in the exhibit's `:root` block: `--header-logo` re-hosted (section 4), `--header-title: "parawatch"` and `--header-subtitle: "ABNORMAL OBSERVATIONS NETWORK"` carried in English — they are the theme's fictional network brand, the name the fiction itself uses, and no T4 header-language item was recorded for this theme beyond the P4 delivery item. The render row's sidebar item belongs here: at 1366 the sidebar renders collapsed behind the theme's own ☰ hamburger, which the ledger records as the theme's own pattern working (T3-recorded), not a defect.
- **Why:** Header language is P9/T6 territory, whose ruling 2 takes title language into case-by-case taste; a fictional brand name is the clearest case for keeping. The hamburger point is recorded so a reviewer does not re-raise a checked behavior as a defect.
- **Verify:** The variables are at the exhibit's head (candidate L733–760 region, served as the /6 content in section 3's probe); the sidebar disposition is the ledger §(c2) block for this theme.
- **Disposition:** DISPOSITIONED (the sidebar item, as a working pattern, in the §(c2) block); the header strings stand as carried.

### 6. Text translation

- **What:** The body is translated throughout: 43 TRANSLATION-ANCHORED primaries and the TRANS-UNANCHORED mass (96 label occurrences), covering the usage prose, the Parawatch post samples' text, the exhibit captions, and the collapsible labels. English survives reader-visible in the header brand strings (section 5), the credit 原題 field, and the CSS comments of the exhibit (carried; the one added comment is the JP-font note, section 4). The Parawatch samples' content is translated inside the rebuilt divs (section 8), including the censor/log/conclude specimen text.
- **Why:** P10 (body, usage, and sample translation is the port's purpose) and KB-18 (reader-visible strings). The unanchored mass was verified in bulk against the mirror for this README.
- **Verify:** The pairs are diff.md's seven sections in order; an English-prose scan of candidate.txt outside the exhibit returns the brand strings and the notes' quoted terms.
- **Disposition:** Standing (the port itself); no untranslated reader-visible text remains outside the items named.

### 7. Links

- **What:** No LINK-REPOINT block fired, and the candidate's one attribution link is the credit source link (candidate L28), naming scp-wiki.wikidot.com — the original's recorded host in review/sources.tsv — so the mis-hosted-link defect class does not occur and no probe was needed for links. (The two fetches reported in section 3 were delivery probes, not link probes.) The license box's source entries name the image files' origins as attribution records.
- **Why:** P11 under the dead-reference evidence standard: a link that already names the serving original needs no change, and attribution sources are provenance data.
- **Verify:** `grep -n 'wikidot.com' candidate.txt` — the credit source link and the draft-host delivery lines are the hits.
- **Disposition:** Standing; no dead or mis-hosted link found.

### 8. Structure

- **What:** The localize.md closing rule holds for the theme's own skeleton (head frame, credit, body, license box, exhibit, gate close, in the original's order), with the one genuine restructuring the classifier's headline label names: the Parawatch exhibits. The original presents its sample posts as component includes with parameter blocks and nine sample code blocks (original L31–604 region); the candidate presents the same posts as directly written divs (`parapost-wrap` → `parapost` → body classes, with `censor`/`log`/`conclude` modifiers) and five sample code blocks, because the component does not exist on SCP-JP (section 2). The 25 EXHIBIT-RESTRUCTURE primaries map to those exhibits one for one; the large collapses (B37: original L205–233 → candidate L261; B54: original L337–397 → candidate L362; B64: original L457–550 → candidate L454–455) are parameter-table exhibits whose whole content the direct-div form states in a line or two, not deleted prose — the posts themselves stand in the candidate at the same positions with their text translated (section 6). The three residue blocks are seams of this restructuring (appendix). The restructuring's side effect on code-block numbering is the delivery flag of section 3.
- **Why:** R3 exists to force exactly this adjudication: a restructure must be shown to preserve the reader-visible content, exhibit by exhibit. Here it does — the posts, their decorations, and their specimen parameters all have candidate counterparts — and the adjudication is also what surfaces the numbering side effect, which a label-level read would have missed.
- **Verify:** Compare the post sequence: `grep -n 'parapost\|parawatch-post' original.txt candidate.txt` — the original's includes against the candidate's div classes, in the same order; the notes at candidate L299 and L355–359 state the mapping in-file.
- **Disposition:** Standing; no structural deletion of carried content, no class I item. The numbering side effect is flagged in section 3, not charged here.

### 9. Formatting only

- **What:** Fourteen whitespace-only blocks (B159–B172 primaries), all inside the CSS exhibit: the EN9 whitespace normalization (commit 5b6dbe2, "normalize whitespace-only lines in code blocks") applied to the exhibit's blank lines. The classifier finds no re-indentation pair (0), so the R7 follow-up-diff hazard is not triggered beyond the normalization itself, which is the commit's stated purpose.
- **Why:** Formatting churn is disclosed as its own class so it is never mistaken for a semantic change; here the class has a named mechanical cause in the wave history.
- **Verify:** The fourteen blocks are listed in classification.json with their exhibit line ranges (original L2187–2266 region).
- **Disposition:** None required.

### 10. Porter annotations

- **What:** Two translator notes, both about the Parawatch substitution, both reader-visible by design. (1) An inline note in the body prose (candidate L299): このテーマにはParawatch投稿の体裁が組み込まれています。//訳注： … — stating that the original assembles the posts with `component:parawatch-post`, that SCP-JP has no such component, and that the JP version writes the decorated divs directly. (2) A fuller note before the parameter exhibit (candidate L355–359, the ANNOTATION-labeled block's region): **訳注:** … — mapping the component's parameters to the div classes (`parapost-wrap` → `parapost` → body; `censor`/`log`/`conclude` corresponding to the original's `_censor=`/`_log=`/`_conclude=`). The exhibit banner's "Ported for SCP-JP (theme:enlightened-eyes rev 51)" line is the third porter mark, in the CSS banner.
- **Why:** R2: porter-added text is part of the change record, and these notes are load-bearing — they are the only in-file explanation of why the exhibits are divs instead of includes, and they teach the JP user the replacement markup.
- **Verify:** Read candidate L299 and L355–359.
- **Disposition:** Standing.

### 11. Dispositions and exceptions

- **What:** Five recorded items and two flagged ones. Recorded: (1) T1's six pseudo-ref errors: class (ii), posting-procedure — the candidate's own draft-host local--code lines and frame references (section 3); the posting procedure rewrites or re-hosts them. (2) Page-overflow everywhere (1489px@1366, 789px@768, ~440px@≤375): the recorded cross-cutting families, static credit replica fixed width (KB-33) and preview chrome (KB-34). (3) The sample credit-modal item: preview-form property (KB-32). (4) The 1366 sidebar item: the theme's own hamburger pattern, T3-recorded as working (section 5). (5) The WebKit CC "S" glyph: KB-36, the WebKit CC-badge stray glyph. Flagged (unrecorded, this package's findings): (6) the own-layer delivery addressing (section 3, finding (1)) — probe-verified, display-affecting in the strong sense that the theme's own CSS does not load through its frame; and (7) the absent cursor rules (section 3, finding (2)). A record caveat attaches to the T4 side: LOCALIZE-ROWS row 85's note is truncated in the record as it stands (it ends mid-sentence after item (a)), so the row's second display-affecting finding cannot be reconstructed from the row alone; both halves of the recorded item (a) concern the Basalt delivery that FIX-P4 repaired.
- **Why:** A disposition is a decision with grounds (AGENTS.md §3 classes (i)/(ii)/(iii); the named KB entries), not an omission. The two flagged items have no grounds recorded anywhere, which is precisely why they are flagged rather than dispositioned here: a review package that silently passed them would misstate the candidate's state.
- **Verify:** Items (1)–(5) name their deciding records above (T1-ROWS row 85; the ledger §(c2) block for this theme, RENDER-S2-B (EN9); §(c3) for the P4 line). Items (6)–(7) verify by section 3's probes and greps.
- **Disposition:** DISPOSITIONED (items 1–5); **flagged for coordinator adjudication** (items 6–7 — a repair wave should repoint or restructure the own-layer delivery and restore the cursor module, or the ledger should record a disposition for both).

### 12. Verification

- **What:** (a) T1 source check (T1-ROWS row 85): exit 1, 6 errors / 0 warns / 1 info; all six errors are pseudo-ref, class (ii); there is no class (i) error. (b) T2/T3 render (RENDER-ROWS-1, lane RENDER-S2-B): FINDINGS, the items of section 11(2–5), all dispositioned; engine coverage is the full matrix as run by the lane. One tension is recorded honestly: the render record describes theme-specific styled rendering, while section 3's probe shows the framed own-layer delivery serving a sample — the render state's styling path is for the coordinator's adjudication of flag (6) to establish. (c) T4/T5 (LOCALIZE-ROWS row 85): FINDINGS jointly, display-affecting findings 2 (the P4 item, since repaired in the bytes by FIX-P4; the row's note is truncated, section 11). (d) This package is self-verifying: `python3 review/build_review.py --check` regenerates diff.md and the verdict stamp from the two byte-faithful copies in this directory and compares. Counts in this README are the generator's (difflib, autojunk off): +541/−652 in 175 change blocks / 7 diff sections (Tier 2 format).
- **Why:** Verification claims name the cheapest deciding check and its result, not a general assurance — including where two checks disagree.
- **Verify:** Re-run the checker on `pages/theme:enlightened-eyes-jp.txt`, `python3 review/build_review.py --check` in this repo, and the two local--code probes of section 3.
- **Disposition:** PASS (GOSIGN2-LEDGER (b) row 85; go-sign, COMPLETION-REPORT §10), with the two flags of section 11 carried forward.

## Per-theme record

### The Parawatch substitution, and the number it broke

The port's central decision deserves one plain statement. The original theme is a showcase for a component: its sample posts exist to demonstrate `component:parawatch-post`, and the theme's CSS decorates the divs that component emits. SCP-JP has no such component, so a JP user following the original's instructions would produce nothing. The candidate therefore inverts the showcase: it writes the component's output divs directly, translates the posts, and spends two translator notes teaching the mapping. As a porting decision that is right, and the records pass it. But the consolidation quietly changed a number the delivery machinery depends on: Wikidot addresses a page's code blocks by position, the exhibit was the original's tenth block and is the candidate's sixth, and the candidate's delivery lines say /1 — an address that made sense only as the convention "the exhibit is the first code block", which the sample blocks ahead of it falsify. The original author had counted and written /10. The lesson the patterns base should keep (proposed in the batch report) is that a port which adds, removes, or reorders code blocks ahead of its exhibit must recount the exhibit's address from the candidate's own bytes, and the cheapest check is one fetch of the addressed code page.

### The usage example's posting name

The usage examples at candidate L293–294 as built read `@@[[include :scp-jp:theme:basalt]]@@` and `@@[[include :scp-jp:theme:enlightened-eyes]]@@`: the porting wave's repoints changed the branch prefix from `:scp-wiki:` but left the plain names, so both examples named pages that do not exist on scp-jp (the campaign's settled rule for usage examples, AGENTS.md §6). The usage-example population sweep has since completed both references on the same lines, the cross-reference to `:scp-jp:theme:basalt-jp` (candidate L293) and the self-reference to `:scp-jp:theme:enlightened-eyes-jp` (candidate L294) (sweep report SWEEP-USAGE.md in the campaign record, R/review-scout/; canonical commit b5cb724), two of its 287 repairs across 157 candidates. This package documents the corrected candidate; its stamp reads STALE against the pre-repair verdict, by design.

## Appendix — residue blocks

For class M the residue set is resolved in one table, not per-block slots.

| Block | Shape | Resolution |
|---|---|---|
| B32 (no signature) | Original L168 → candidate L194–200: a `[[/div]]` group closing a rebuilt Parawatch post | A seam of the direct-div restructuring (section 8): the candidate's post needs more closing lines than the component form |
| B60 (no signature) | Original L445 → candidate L403–404: a `[[/collapsible]]` seam between exhibits | Exhibit-boundary formatting inside the restructured Parawatch region (section 8) |
| B72 (no signature) | Original L597–598 → candidate L501–507: a `[[/div]]` group | The same restructuring seam shape as B32 (section 8) |

## Change set outside the two diffed files

The diff covers two files; the port's record is larger. `pages/theme-decoration-sample-enlightened-eyes-jp.txt` is the decoration sample the render checks ran against (its credit-modal item is section 11(3)). The candidate layers over `pages/theme:basalt-jp.txt` (frame priorities 1–2 and the exhibit's import) — that base is its own candidate with its own review package, and the K5b-3 scope note in section 0 is the boundary. The two defect flags of section 11, when repaired, will change this candidate file and will require this package's stamp and diff to be refreshed by the coordinator's harvest procedure. There are no companion fragments for this theme.
