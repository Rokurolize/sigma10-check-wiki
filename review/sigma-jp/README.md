# Review package — theme:sigma-jp

<!-- BEGIN GENERATED VERDICT STAMP — do not hand-edit; regenerate with review/build_review.py -->
## Verdict stamp
- Theme: theme:sigma-jp — origin EN, population #36 [GOSIGN2-LEDGER (b) row 36]
- Overall: STALE — candidate file changed since the verdict was computed (verdict against 435a6bb-era content, file sha256 now 3d6603e475bd333d3ee4c8572f61ad21e6abbb6a40e49d975f5d04524892df2a); verdict not carried over, re-judgement required
> verdicts below describe the pre-change file
- T1 (source check): FINDINGS (classified) — baseline 2026-11-16: exit 1, 1 error / 4 warns / 1 info (hotlink×1); standing classes dispositioned in register c1 [T1-ROWS row 36; GOSIGN2-LEDGER (b) row 36]
- T2/T3 (render, combined verdict): FINDINGS — [combined T2/T3] report `FINDINGS` — 884px@768 overflow (static credit replica + code specimen run past frame), notice×sidebar at 768, sample credit-modal; Σ9 port otherwise renders correctly. [RENDER-ROWS-1 (RENDER-D row 36)]
- Engine coverage: full matrix as run by the lane; coverage not separately caveated in the row [RENDER-ROWS-1 row]
- Credit modal: sample credit-modal errors dispositioned preview-form (credit:start-preview has no modal mechanism; GOSIGN-TESTS T2 amendment, 2026-11-16; ROWS-1 phrases the line bare and takes the disposition from the part header) [RENDER-ROWS-1 (RENDER-D row 36)]
- T4 (localize patterns + follow-up): FINDINGS — display-affecting findings: 2 [LOCALIZE-ROWS row 36, source LOCALIZE-B]
- T5 (translation text): FINDINGS — the source reports judge T4/T5 jointly; one verdict word covers both [LOCALIZE-ROWS row 36]
- FIX5 re-judgement: none — no OPEN items at the ledger determination [GOSIGN2-LEDGER (b) row 36]
- Computed against: canonical commit 722ceb5c949172bb5185d51ef56ce4119ee4fa91; candidate file pages/theme:sigma-jp.txt sha256:3d6603e475bd333d3ee4c8572f61ad21e6abbb6a40e49d975f5d04524892df2a; record: GOSIGN2-LEDGER.md + GOSIGN2-LEDGER-SUPPLEMENT.md as of the FIX5 head 435a6bb
<!-- END GENERATED VERDICT STAMP -->

## Status

| | |
|---|---|
| Verdict | **PASS** — passed at the ledger determination; this theme had no OPEN items and no §(e) register entry (GOSIGN2-LEDGER (b) row 36). The stamp reads STALE because the usage sweep changed two lines after the verdict (per-theme record) |
| Standing items | **DISPOSITIONED** — the logo hotlink (P5, class (ii) / KB-58, section 4); the P10 specimen items (the stray marker and the dropped specimen wrappers, lane-recorded severity / specimen class, sections 6 and 8); the render row's items (KB-33 overflow family; credit-modal preview form, section 11). **FIXED** — the missing frames (P6, frame waves). **One flag from this package:** the third frame, at priority=3, names the candidate's own `local--code/1`, and this page contains no code block for the fragment to serve (probe-verified, per-theme record) |
| Go-sign basis | COMPLETION-REPORT.md §10 (go-sign issued; 81 FIXED / 26 DISPOSITIONED / 0 OPEN across the sweep) |
| Named exception | None for this theme (the sweep's single named exception is theme:amethyst-v2, which has no candidate) |

## Provenance

| | Original | Candidate |
|---|---|---|
| Page | theme:sigma | theme:sigma-jp |
| Wiki | scp-wiki.wikidot.com | SCP-JP Sigma-10 candidate (canonical repo) |
| Reference revision | 16 (first translation; the candidate's credit block records 初訳時参照リビジョン: 16) | — |
| Source of this copy | Campaign mirror store (class COPY, hash-verified against review/sources.tsv) | Canonical file `pages/theme:sigma-jp.txt`, copied at worktree HEAD 2aee861 |
| Lines / bytes | 237 lines / 5,620 bytes | 213 lines / 7,295 bytes |
| SHA-256 | ed3a95523fcfad9355fe603b408d0939c832d7c954c6a99be38893b25f5874eb | ac5577f795dddd3c14cc0e7dd11dfa12843bfe80dfbc55c6d53dfcee01822db6 |

Wave history: the candidate was recorded at the canonical-sources commit (d727e92), whitespace-normalized (3010ef7), carried through the Phase 17 revision recording (8dcac74), received the T1 credit fixes (b816e10) and FIX-P4's base-theme import repoints (f1138e4), and was last touched by the usage sweep (b5cb724) — the post-verdict change the stamp reports.

## Summary

aismallard's Sigma-9 theme page: the base theme of the EN wiki, presented as a deadpan sales pitch, testimonials and all. As a port it is an unusual shape — the "theme" carries almost no CSS of its own (one small live module of demo rules: `.color`, `.blink`, a hidden footnotes footer), because its substance is the Black Highlighter base it tells the reader to include first. The candidate converts that two-include usage into the population's frame form: two head frames deliver BHL's normalize and black-highlighter stylesheets from the JP project's own hosting (scp-jp.github.io), a third frame after the gate names the candidate's own code fragment, and the body is the pitch, translated whole — jokes, testimonials, color specimens ("Sunny-D Orange", "Sour Grapes", "Liver", "Threat Level: Black"), the sexy-box specimen, and the font specimens. Measured churn is +162/−185 in 43 change blocks / 2 hunks, most of it unanchored translation (30 blocks). The render row's closing assessment is the campaign's own: "Σ9 port otherwise renders correctly." Two things in this package need stating plainly. The logo specimen still loads from the EN component page's file area — the ledger's deferred-hosting disposition, section 4. And the priority=3 frame names a fragment that does not exist: this page has no `[[code]]` block at all (the original's single code block was a wikitext usage example, not CSS), so the frame's request returns "No valid codeblock found." — the batch's fourth instance of the frame-target family, flagged in the per-theme record.

## Class summary

Auto-classification by review/classify_hunks.py (signature table 2026-11-17.1): 43 change blocks — 9 specific (20.9%), 27 heuristic (62.8%), 7 residue, 0 skipped. Pattern citations below name the KB entry; the patterns/ tree state cited throughout is commit 9c5e9079afb01d30cb9fc4ef9d714e5591eb2ffa.

| Label | Blocks |
|---|---|
| TRANS-UNANCHORED | 30 |
| TRANSLATION-ANCHORED | 5 |
| EXHIBIT-RESTRUCTURE | 4 |
| BARE-RATE-DEL | 1 |
| COMPONENT-SWAP | 1 |
| CREDIT-PREVIEW | 1 |
| DRAFT-HOST | 1 |
| ESCAPED-INCLUDE | 1 |
| IFTAGS | 1 |
| INCLUDE-REPOINT | 1 |
| LINK-REPOINT | 1 |
| SELF-DELIVERY | 1 |
| TASL-FIELDS | 1 |

Adjudication for this README (every block was read against the bytes): there is no code exhibit in this page on either side in the delivery sense — the four EXHIBIT-RESTRUCTURE primaries are specimen-region restructures of the translation (the usage-example compression B6, the source-code heading pair B13, the specimen reflows B24 and B34), adjudicated in sections 6 and 8; B43's SELF-DELIVERY label is the tail frame, section 3's subject. The seven residue blocks collapse into the appendix table. After adjudication no block is left unexplained.

## Standing sections

### 0. Header and provenance frame

- **What:** Theme theme:sigma-jp; original theme:sigma on scp-wiki at reference revision 16; candidate `pages/theme:sigma-jp.txt`. Provenance route: standard first translation (sources.tsv kind: standard). The candidate opens with the two BHL frames (candidate L1–9) ahead of the gate `[[iftags +テーマ]]` (candidate L11); the original opens with the gate (original L1) and a live module, and carries its delivery instructions in prose instead (section 3).
- **Why:** Section 0 declares the provenance route so every later count is read against the right baseline; the gate's tag is P2 and the frames are section 3.
- **Verify:** The sources.tsv row for sigma-jp; `sha256sum original.txt` against the Provenance table.
- **Disposition:** Standing (the route itself); the delivery changes are recorded in section 3.

### 1. Credit and attribution

- **What:** The original carries no credit furniture and no in-file attribution at all: a floated bare `[[module Rate]]` (original L25–27) is its only furniture, and neither an info block, a license box, nor a banner names an author anywhere in its 237 lines. The candidate deletes the bare Rate (block B3) and installs the JP credit block (candidate L13–22) with the eight ruling-3 fields: title Sigma-9 Theme; 翻訳責任者 AI; 翻訳年 2026; 原題 Sigma-9 Theme; 著作権者 **aismallard**; 作成年 2020; 初訳時参照リビジョン 16; the source link (section 7). The author field records the theme's author of record — aismallard, Sigma-9's author on scp-wiki — there being no in-file credit in the mirror for the field to be checked against; this package states that ground explicitly rather than implying a check the file cannot support. The testimonials in the body name six users (Elenee FishTruck, NatVoltaic, Smapti, Ellie3, pxdnbluesoul, Uncle Nicolini) as quoted speakers, on both sides; they are specimen content, not attribution, and are carried as such (section 6).
- **Why:** P3/T1 (KB-09) for the furniture swap (the preview credit module is rate-bearing, so the bare Rate is deleted rather than duplicated); ruling 3's fields are the attribution record, and where the original is silent the field's ground is the authorship of record, stated as such.
- **Verify:** Read candidate L13–22; `grep -n 'aismallard' original.txt` returns nothing — the ground stated above is the checkable fact.
- **Disposition:** Applied (the T1 credit fixes are in this file's history, commit b816e10).

### 2. Includes and components

- **What:** The candidate's live includes are the three frames (section 3), the credit pair (candidate L13, L22), and the image-block specimen (candidate L89, repointed from the bare `component:image-block` to `:scp-jp:component:image-block`, its `name=` unchanged — section 4). The component reference in the prose, `[[[component:theme|Sigma-9]]]` (original L35), is carried unprefixed in the candidate (candidate L48) — a link to the EN component page's documentation, as in the original. The usage examples name the JP forms (candidate L56–63: `:scp-jp:theme:black-highlighter-theme` and `:scp-jp:theme:sigma-jp`, in the original's include-then-delete joke structure, post-sweep).
- **Why:** P1 (KB-15) for the specimen repoint; ruling 4 is not engaged — no component had to be ported alongside this theme, BHL arriving by frame instead (section 3).
- **Verify:** `grep -n '\[\[include' candidate.txt` — three frames, credit pair, specimen, and the escaped usage lines.
- **Disposition:** Applied; no foreign include kept, no named exception needed.

### 3. Delivery and code loading

- **What:** The original delivers nothing itself: its page tells the reader to include Black Highlighter and then this page (original L44–63, as a joke at the reader's expense), and its only CSS is the live `[[module CSS]]` of demo rules at its head (original L2–23). The candidate keeps the demo module verbatim (candidate L23–44) and mechanizes the base delivery. **Frame paragraph (the M-frame addition):** the candidate carries three frames. At the head, priority=1 names BHL's `normalize.min.css` and priority=2 names `black-highlighter.min.css`, both from the JP project's hosting at scp-jp.github.io/Black-Highlighter (candidate L1–9) — the base layers, in the form FIX-P4's repointing standardized (this file's history carries f1138e4). After the gate's close, a third frame at priority=3 names the candidate's own `local--code/1` on the draft host (candidate L210–213). That target does not exist: the candidate contains no `[[code]]` block (census: zero; the original's single code block, original L192–198, was the sexy-box *wikitext* example, whose wrapper the translation drops, section 8), and the probe of the frame's URL returns "No valid codeblock found." (per-theme record). The theme's own layer needs no fragment — its demo rules ride the live module, and BHL rides the two head frames — so the priority=3 entry is a delivery claim with nothing behind it, the same family as this batch's other three frame flags, differing only in that here the missing fragment is the theme's own rather than a base's. The declared-vs-bytes comparison: the original declares its base in prose and delivers by include; the candidate declares the base by frame (correctly) and additionally declares an own-code layer its bytes do not contain (the flag).
- **Why:** P4/T9 for the topology and P6/T3 (KB-07) for the frame stack: priorities order the layers (base normalize, base theme, own layer), and an entry naming a nonexistent fragment is a broken layer even when the remaining layers carry the page.
- **Verify:** Read candidate L1–9 and L210–213; `grep -c '\[\[code' candidate.txt` — zero; the probe URL is the third frame's own `theme=` value at candidate L212.
- **Disposition:** FIXED per the ledger (P6, frame waves, checker-verified) as to the frames' presence; the priority=3 target is **flagged as a defect** (per-theme record).

### 4. Fonts and assets

- **What:** No font load exists on either side: the theme's faces are BHL's, delivered with the base, and the page's own font content is the closing specimen set — four spans naming Verdana, BauhausLTDemi, Trebuchet MS, and Andale Mono as the body/header/subheader/monospace fonts (original L232–235), carried with their specimen sentences translated (candidate L204–207). The spans are specimens of the base theme's typography, not stacks this page loads, so there is no P7 conversion to make and no unloaded-stack flag to raise. The one asset: the logo specimen's image still names the EN component page's file area (candidate L89: `https://scp-wiki.wdfiles.com/local--files/component%3Atheme/logo.png`) — T4's type-5 finding (LOCALIZE-ROWS row 36, item (a), display-affecting) and T1's single error, dispositioned below.
- **Why:** P5 (KB-17) is the rule the hotlink breaches; KB-58 is the standing exception that covers it (owner-deferred image hosting), here as across the LOCALIZE-B population.
- **Verify:** `grep -n 'wdfiles' candidate.txt` — the delivery hosts of section 3 and this one asset line.
- **Disposition:** DISPOSITIONED (P5, class (ii) / KB-58; GOSIGN2-LEDGER §(c3) for this theme).

### 5. Header, sidebar, and site furniture

- **What:** The theme sets no header variables of its own (its header is BHL's, frame-delivered); the page's furniture content is the ACTIVE banner line (original L29 → candidate L45, translated) and the demo rules. No P8 layout adaptation was needed; the render row's sidebar item (notice×sidebar at 768) is the cross-cutting preview-chrome family of section 11, not a rule in this file.
- **Why:** P9/T6 is a per-theme judgment and none was needed: there is no header text of the theme's own to convert, and ruling 2 is not engaged.
- **Verify:** `grep -n -- '--header-' candidate.txt` returns nothing.
- **Disposition:** Standing.

### 6. Text translation

- **What:** The whole pitch is translated (the 30 TRANS-UNANCHORED and 5 TRANSLATION-ANCHORED blocks): the ACTIVE banner, the "What this is" panel (its bordered div wrapper dropped, block B6 — section 8), the usage joke in full (candidate L53–64, including the struck-through includes and the "delete it, that's for nerds" beats), the five color specimens with their names translated or carried (Sunny-Dオレンジ; Sour Grapes → 酸っぱいブドウ form in the specimen set; 肝臓 for Liver, candidate L76; Threat Level: Black; the blinking "You have a new message" specimen), the standard specimen body (headings, links, blockquotes, tables with the footnote, lists), the sexy-box specimen, the six testimonials with their speakers' lines translated and the forum link carried (candidate L175–201), and the font specimens (section 4). Two byte-level notes. (1) The nonexistent-article joke's number changes: the original's SCP-15837 (original L37) reads SCP-11837 in the candidate (candidate L50) — a digit difference inside translated prose, recorded here because digits are not translation; whether slip or deliberate renumbering, no record mentions it, and the joke (a number that does not exist yet) survives either reading. (2) T4 charged a stray `--]` marker in the candidate's earlier form (LOCALIZE-ROWS row 36, item (b), display-affecting); it is absent from the current bytes (the marker at original L181 is the original's own table-specimen artifact, which the candidate's table specimen does not carry), and the ledger dispositions the P10 items as lane-recorded severity / specimen class.
- **Why:** P10 for the translation, jokes included — the page's register is its content, and a flattened pitch would be a worse port than a faithful one. The two notes are the standing residue discipline: what a reviewer would trip on is stated, not smoothed over.
- **Verify:** Read candidate L45–64 against original L29–65; `grep -n -- '--\]' candidate.txt` returns nothing.
- **Disposition:** Standing (the port itself); the P10 items are DISPOSITIONED (ledger §(c3)).

### 7. Links

- **What:** The credit block's source link (candidate L21) names `https://scp-wiki.wikidot.com/theme:sigma` — the host review/sources.tsv records for the original; no host defect. The body's page links name EN articles as specimens and references (SCP-173/682/096, the main page, the Penumbra-line component documentation at candidate L48, Smapti's forum link at candidate L187) — all carried from the original as the content they are, none a mechanism dependency.
- **Why:** P11: prose links take the JP counterpart where the reference is to the ported composition and the serving original where the reference is the content itself; a sales pitch's name-drops are the second kind.
- **Verify:** `grep -n 'wikidot.com' candidate.txt` — the source link and the delivery hosts of section 3.
- **Disposition:** Standing.

### 8. Structure

- **What:** A brace-depth scan of both files closes at depth 0 with no negative excursion (the only CSS is the demo module, verbatim on both sides). The page-level structure changes are the furniture swap (section 1), the frames (section 3), and two specimen-wrapper simplifications T4 recorded as item (c): the bordered div around the introduction panel (original L31) and the `[[div class="code"]]` wrappers around the usage examples (original L46–63) are not carried — the candidate sets the examples as bare escaped lines (candidate L56–63), and the sexy-box example's `[[code]]` wrapper likewise (original L192–198 → candidate L171 as plain text). The specimen census otherwise matches: colors, headings collapsible, image-block, horizontal-rule and title specimens, blockquotes, tables, lists, sexy-box, testimonials, font spans, in the original's order. T4 graded the wrapper drops display-affecting in its row; the ledger's c3 line dispositions the theme's P10 items (lane-recorded severity / specimen class), and the render row found the port otherwise correct — this package records both the drop and the disposition without relitigating either.
- **Why:** R3's distinction is met by the census; the EXHIBIT-RESTRUCTURE primaries adjudicate to these specimen restructures, there being no delivery exhibit in this page.
- **Verify:** Compare `grep -n '\[\[div\|\[\[code\|\[\[include' original.txt candidate.txt`.
- **Disposition:** Standing as dispositioned (P10, ledger §(c3)); no class I item.

### 9. Formatting only

- **What:** No WS-ONLY block fired in this pair (label count 0), and the classifier's reindent count is 0. The candidate is shorter than the original by 24 lines, and the difference is accounted for by the wrapper drops of section 8 and the translation's compression (block B6: 38 original lines → 12 candidate lines), not by formatting churn.
- **Why:** Formatting churn is disclosed as its own class; here the disclosure is that there is none separable from the labeled mass.
- **Verify:** classification.json's label counts (WS-ONLY absent).
- **Disposition:** None required; disclosed.

### 10. Porter annotations

- **What:** None. No porter comment, banner addition, or prose note exists in the candidate; the translation carries no added text beyond the credit block's fields, and the stylesheet module is the author's own, verbatim. The candidate's additions are exactly the furniture of sections 1 and 3.
- **Why:** R2's check is explicit for this theme because its neighbors in the batch do carry annotations: the absence is verified (full read of the 213 lines), not assumed.
- **Verify:** `grep -n 'SCP-JP\|Ported\|移植' candidate.txt` — only the credit block's fields match.
- **Disposition:** Standing (none present).

### 11. Dispositions and exceptions

- **What:** Three items, each with its ground. (1) The logo hotlink (candidate L89): T1's single error and T4's type-5 finding, dispositioned as class (ii) under KB-58 (section 4). (2) The P10 specimen items: the stray marker (absent in current bytes) and the dropped specimen wrappers (section 8), dispositioned as lane-recorded severity / specimen class. (3) The render row's items: the 884px@768 overflow, in the cross-cutting static-credit-replica family (KB-33 — the ledger's own note: the preview credit replica is fixed-width and overflows narrow viewports on every theme that carries it, this figure included); notice×sidebar at 768 (preview chrome, KB-34); and the sample credit-modal item (KB-32, ruling 5). The same row closes: "Σ9 port otherwise renders correctly." **Not a disposition:** the priority=3 frame's nonexistent target — flagged below with its probe evidence; the ledger's P6 FIXED line is quoted there alongside the bytes. The ledger's determination for this theme is PASS and this package does not re-open it.
- **Why:** A disposition is a decision with grounds (AGENTS.md §3 classes (i)/(ii)/(iii); the named KB entries), not an omission; a byte-level defect is flagged, never dispositioned by relabeling.
- **Verify:** Each item names its deciding record above and in the per-theme record.
- **Disposition:** DISPOSITIONED (items 1–3); the frame flag stands as a flag.

### 12. Verification

- **What:** (a) T1 source check (T1-ROWS row 36): exit 1, 1 error / 4 warns / 1 info; the error is the hotlink of section 11(1), class (ii); there is no class (i) error. (b) T2/T3 render (RENDER-ROWS-1 row 50, lane RENDER-D (row 36)): the raw marks read FAIL/FAIL with the combined report FINDINGS — the items of section 11(3), all dispositioned, with the row's closing assessment that the port otherwise renders correctly. (c) T4/T5 (LOCALIZE-ROWS row 36, lane LOCALIZE-B): FINDINGS jointly, display-affecting findings 2 (the hotlink; the stray marker in its earlier form), plus the wrapper and frame items the fix waves and dispositions then closed. (d) This package is self-verifying: `python3 review/build_review.py --check` regenerates diff.md and the verdict stamp from the two byte-faithful copies in this directory and compares. Counts in this README are the generator's (difflib, autojunk off): +162/−185 in 43 change blocks / 2 hunks; the brace-depth scan and the fragment probe were run for this package.
- **Why:** Verification claims name the cheapest deciding check and its result, not a general assurance.
- **Verify:** Re-run the checker on `pages/theme:sigma-jp.txt`, `python3 review/build_review.py --check` in this repo, and the probe in the per-theme record.
- **Disposition:** PASS (GOSIGN2-LEDGER (b) row 36; go-sign, COMPLETION-REPORT §10) — for the pre-sweep file, with this package's flag standing against the current bytes.

## Per-theme record

### The priority=3 frame names a code fragment this page does not contain (defect flag, probe-verified)

Candidate L210–213, after the gate's close, is a third interwiki-style frame: priority=3, `theme=https://sigma10-jp-test.wdfiles.com/local--code/theme%3Asigma-jp/1`. The candidate contains no `[[code]]` block (census: zero). Probe made for this package (2026-11-17): that URL returns the 25-byte plain text "No valid codeblock found." The deeper point is that no version of this page could satisfy the address: the original's only code block is a wikitext usage example (the sexy-box snippet, original L192–198), so a `local--code/1` fragment for this theme would serve example text, not CSS, even if the wrapper had been kept. The theme's actual delivery is complete without it — BHL by the two head frames, the demo rules by the live module — which is why the render row passes and why the defect is quiet. It is the fourth instance of the frame-target family in this batch (navla-style-jp, path-of-jinin-jp, ragnarok-theme-jp, paperstack-jp are the others in their own forms), and it supports the same conclusion: the standard frame paragraph was templated onto pages whose delivery topologies differ, and the checkers verified the frames' presence, not their targets. The repair (removing the entry, or pointing the own-layer entry at a delivery that exists) is the coordinator's; this package makes no edit, per the review protocol.

### The post-verdict lines (why the stamp reads STALE)

The candidate changed once after the FIX5 head: the usage sweep (commit b5cb724) corrected the two escaped usage examples at candidate L56 and L63 from `@@[[include :scp-jp:theme:sigma]]@@` to the `-jp` posting name (the BHL line of each example already named its JP form). That is the whole of the drift the stamp reports: two documentation lines inside the usage joke, no delivery, credit, or CSS change. This package documents the corrected candidate; the verdict lines under the stamp describe the file as judged, two lines earlier.

### The residue blocks, adjudicated

Seven blocks carried no label. All are translation mass of section 6, left unlabeled because none carries a signature anchor:

| Block | Span | Adjudication |
|---|---|---|
| B9 | original L80–81 → candidate L76–77 | The "Liver" color specimen pair, translated （肝臓） |
| B12 | original L91–92 → candidate L87–88 | The "+ Examples" heading pair, translated (+ 例） |
| B16 | original L99–100 → candidate L97–98 | The titles-specimen lead-in pair |
| B17 | original L101–103 → candidate L99–100 | The titles collapsible's opening lines |
| B18 | original L104–105 → candidate L101–102 | Heading specimens inside the collapsible |
| B19 | original L106–107 → candidate L103–104 | Heading specimens, continued |
| B35 | original L203–204 → candidate L175–176 | The "+ Testimonials" heading pair, translated (+ 証言） |


### Post-package repairs (REFRESH3-D)

Recopy was a verified no-op: `candidate.txt` is byte-identical to the current canonical `pages/theme:sigma-jp.txt`. No repair lands after this package's candidate build, so the record below is the slice's sub-shape and remedy, confirmed present in the built bytes.

- **FIX-FRAMEADDR, sub-shape (B) — Introduced** (report `R/review-scout/FIX-FRAMEADDR.md` §2; landing `722ceb5c949172bb5185d51ef56ce4119ee4fa91`, 2026-11-17): the original carries no interwiki-style frame and no `theme=` self-address in that role; the porting wave introduced the frame with `theme=` naming its own draft-host `local--code/theme%3Asigma-jp/1`, a fragment the page does not carry (delivery is the inline `[[module CSS]]`). Remedy: the single `| theme=...` line was deleted; the frame include and its `priority=1` line are kept. Current candidate frame at L1.
- The post-verdict lines already recorded in the per-theme record predate this package's build; no further repair touches the file.

Stamp treatment follows the jiha-jp / alexylva-university-jp precedents: the regenerated verdict stamp reads STALE, no re-judgement is fabricated, and the frozen GOSIGN2 ledger remains the verdict record.

## Change set outside the two diffed files

The diff covers two files; this theme's record is one file larger. `pages/theme-decoration-sample-sigma-jp.txt` is the decoration sample the render checks ran against (its credit-modal item is section 11(3)); it belongs to this theme's record but carries no port change of its own to explain here. There are no companion fragments, no shared base file, and no inbound-link repairs in other candidates for this theme.
