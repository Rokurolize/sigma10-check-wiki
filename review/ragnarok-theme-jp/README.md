# Review package — theme:ragnarok-theme-jp

<!-- BEGIN GENERATED VERDICT STAMP — do not hand-edit; regenerate with review/build_review.py -->
## Verdict stamp
- Theme: theme:ragnarok-theme-jp — origin EN, population #127 [GOSIGN2-LEDGER (b) row 127]
- Overall: STALE — candidate file changed since the verdict was computed (verdict against 435a6bb-era content, file sha256 now 4ff6ac221ed70d6e9100ae53665a0e57761a75664cc6ce0d3f44ecce40ec3a31); verdict not carried over, re-judgement required
> verdicts below describe the pre-change file
- T1 (source check): FINDINGS (classified) — baseline 2026-11-16: exit 1, 4 errors / 2 warns / 1 info (hotlink×4); standing classes dispositioned in register c1 [T1-ROWS row 152; GOSIGN2-LEDGER (b) row 127]
- T2/T3 (render, combined verdict): FINDINGS — [combined T2/T3] report `FINDINGS` — page runtime-hotlink site-theme chain only; sample T2 no machine verdict (exit 2). [RENDER-ROWS-2 (RENDER-S2-C (EN17))]
- Engine coverage: full matrix as run by the lane; coverage not separately caveated in the row (the row records inconclusive runs, carried verbatim above) [RENDER-ROWS-2 row]
- Credit modal: no credit-modal line recorded [RENDER-ROWS-2 (RENDER-S2-C (EN17))]
- T4 (localize patterns + follow-up): FINDINGS — display-affecting findings: 2 [LOCALIZE-ROWS row 127, source LOCALIZE-S2-C]
- T5 (translation text): FINDINGS — the source reports judge T4/T5 jointly; one verdict word covers both [LOCALIZE-ROWS row 127]
- FIX5 re-judgement: none — no OPEN items at the ledger determination [GOSIGN2-LEDGER (b) row 127]
- Computed against: canonical commit 722ceb5c949172bb5185d51ef56ce4119ee4fa91; candidate file pages/theme:ragnarok-theme-jp.txt sha256:4ff6ac221ed70d6e9100ae53665a0e57761a75664cc6ce0d3f44ecce40ec3a31; record: GOSIGN2-LEDGER.md + GOSIGN2-LEDGER-SUPPLEMENT.md as of the FIX5 head 435a6bb
<!-- END GENERATED VERDICT STAMP -->

## Status

| | |
|---|---|
| Verdict | **PASS** — passed at the ledger determination; this theme had no OPEN items and no §(e) register entry (GOSIGN2-LEDGER (b) row 127). The stamp reads PASS: no post-verdict change touched this candidate |
| Standing items | **DISPOSITIONED** — the four EN-host hotlinks (P5, class (ii) / KB-58 deferred hosting, sections 4 and 11); the render row's two items (runtime-hotlink chain; sample T2 coverage caveat, section 11). **FIXED** — the missing frame (P6, FIX4-IWA), with the qualification flagged below. **One flag from this package:** the added frame names a code fragment that does not exist, because this theme delivers by a live CSS module and has no `[[code]]` block at all (probe-verified, per-theme record) |
| Go-sign basis | COMPLETION-REPORT.md §10 (go-sign issued; 81 FIXED / 26 DISPOSITIONED / 0 OPEN across the sweep) |
| Named exception | None for this theme (the sweep's single named exception is theme:amethyst-v2, which has no candidate) |

## Provenance

| | Original | Candidate |
|---|---|---|
| Page | theme:ragnarok-theme | theme:ragnarok-theme-jp |
| Wiki | scp-wiki.wikidot.com | SCP-JP Sigma-10 candidate (canonical repo) |
| Reference revision | 20 (first translation; the candidate's credit block records 初訳時参照リビジョン: 20) | — |
| Source of this copy | Campaign cache `gosign2-lanes/lane-oc-gs-render-s2-C/orig-ragnarok-theme.txt`, via the mirror store (class COPY, hash-verified against review/sources.tsv) | Canonical file `pages/theme:ragnarok-theme-jp.txt`, copied at worktree HEAD 2aee861 |
| Lines / bytes | 1,220 lines / 31,690 bytes | 1,226 lines / 33,939 bytes |
| SHA-256 | 35b59c48de15db00e0eb364178ea7b2816d145d6a3161093f1348cf1def169df | 01461624039e3de58f0909b6f8b1db216a743a03b4cbceb7579ba2b310556152 |

Wave history: the candidate was created by the Stage 2 EN17 integration (commit b17d7e4); FIX-CREDIT-D (1869877) normalized its translator attribution; FIX4-IWA (8c62b7b) added the head frame (section 3) and is the last commit to touch the file, which is why the stamp computes against it and reads PASS.

## Summary

MalyceGraves' theme for the Ragnarok canon — an aesthetic variant of estrellayoshte's Penumbra, itself built on Paperstack, Ad Astra, Inkblot, Anderson Robotics, and the BHL collapsible, all credited in the stylesheet's banner. The page is documentation-heavy: two-thirds of it is the standard specimen body, and the stylesheet itself is a live `[[module CSS]]` carried in a hidden div at the tail, not a code exhibit. The port is correspondingly light on the CSS (the module crosses almost verbatim: the font imports move from bunny.net to Google Fonts with Noto Sans JP added, the body stack gains the JP fallbacks, the subtitle default is translated, and one blank line moves) and complete on the prose (every specimen and note translated, the image-attribution collapsible carried with its Flickr sources). Measured churn is +168/−169 in 74 change blocks / 9 hunks, of which 47 blocks are unanchored translation. Two records need a reviewer's attention rather than a skim. The four scp-wiki.wdfiles.com references T1 and T4 charged are still in the file — deliberately: they are the ledger's class (ii) deferred-hosting disposition, stated in sections 4 and 11. And the frame FIX4-IWA added at the head names the candidate's own `local--code/1`, a fragment this page does not contain — the theme works because its live module delivers the CSS, and the frame's request returns "No valid codeblock found." (probe, per-theme record). The frame's presence satisfied the checker's P6 line; its target does not exist, and this package flags that rather than repeating the FIXED line unqualified.

## Class summary

Auto-classification by review/classify_hunks.py (signature table 2026-11-17.1): 74 change blocks — 28 specific (37.8%), 44 heuristic (59.5%), 2 residue, 0 skipped. Pattern citations below name the KB entry; the patterns/ tree state cited throughout is commit 9c5e9079afb01d30cb9fc4ef9d714e5591eb2ffa.

| Label | Blocks |
|---|---|
| TRANS-UNANCHORED | 47 |
| TRANSLATION-ANCHORED | 19 |
| IFTAGS | 3 |
| EXHIBIT-RESTRUCTURE | 2 |
| HEADERVAR | 2 |
| INCLUDE-REPOINT | 2 |
| BARE-RATE-DEL | 1 |
| COMPONENT-SWAP | 1 |
| CREDIT-PREVIEW | 1 |
| CREDIT-PROSE | 1 |
| DRAFT-HOST | 1 |
| FONT-IMPORT | 1 |
| INFO-DEL | 1 |
| JPFONT-LOAD | 1 |
| JPFONT-STACK | 1 |
| LINK-REPOINT | 1 |
| SELF-DELIVERY | 1 |
| TASL-FIELDS | 1 |
| WS-ONLY | 1 |

Adjudication for this README (every block was read against the bytes): the two EXHIBIT-RESTRUCTURE primaries are the image-block specimen repoints (B15) and the toggle-sidebar repoint at the module's head (B70) — include repoints, not exhibit changes, and there is no code exhibit in this page at all (section 3). B1's SELF-DELIVERY label fires on the frame's self-address, whose target census is section 3's subject. The two residue blocks are resolved in the appendix. After adjudication no block is left unexplained.

## Standing sections

### 0. Header and provenance frame

- **What:** Theme theme:ragnarok-theme-jp; original theme:ragnarok-theme on scp-wiki at reference revision 20; candidate `pages/theme:ragnarok-theme-jp.txt`. Provenance route: standard first translation (sources.tsv kind: standard). The candidate opens with the frame (candidate L1–4) ahead of the gate `[[iftags +テーマ]]` (candidate L6); the original opens with the gate `[[iftags +theme]]` (original L1) and has no head furniture at all — its delivery sits at the tail (section 3).
- **Why:** Section 0 declares the provenance route so every later count is read against the right baseline; the gate's tag is P2 and the frame is section 3.
- **Verify:** The sources.tsv row for ragnarok-theme-jp; `sha256sum original.txt` against the Provenance table.
- **Disposition:** Standing (the route itself); the frame's arrival and its target are recorded in section 3.

### 1. Credit and attribution

- **What:** The original's furniture is a floated pair: a bare `[[module Rate]]` under the label "Rating:" and an `[[include :scp-wiki:info:start]]`/`more`/`end` triple under "Rating w/ Credit Module:", both info texts being placeholder sentences (original L3–13). The candidate deletes both (blocks B2, B3) and installs the JP credit block (candidate L8–17) with the eight ruling-3 fields: title Ragnarokテーマ; 翻訳責任者 AI; 翻訳年 2026; 原題 Ragnarok Theme; 著作権者 MalyceGraves; 作成年 2021; 初訳時参照リビジョン 20; the source link (section 7). The author field is exact: the original's prose names [[*user MalyceGraves]] as the creator (original L16), and the stylesheet banner repeats it ("By MalyceGraves", original L275). The banner's full credit chain crosses verbatim in the module (candidate L279–289): Penumbra and Paperstack by EstrellaYoshte, Ad Astra by NatVoltaic and stormbreath, Inkblot and Anderson Robotics by Croquembouche, the BHL collapsible by Monkatraz. The prose attribution section is likewise carried and translated (candidate L22–41): the Penumbra-variant statement and the image-attribution collapsible with both Flickr entries (starfield, CC BY-SA 2.0, sagesolar, 2013; the Ragnarok logo, CC BY-SA 3.0, James Kidd with edits by MalyceGraves, 2009) and the SCP logo's CC BY-SA 3.0 line. There is no license-box include on either side; the collapsible is the license record, and it is complete.
- **Why:** P3/T1 (KB-09) for the furniture swap; ruling 3's fields carry the attribution, and here the prose and banner attributions the field is checked against agree with it — the contrast case to a pointer-form field.
- **Verify:** Read candidate L8–17 against original L16 and L271–283; read candidate L26–41 against original L22–37.
- **Disposition:** Applied; the credit waves' normalization (FIX-CREDIT-D) is in this file's history.

### 2. Includes and components

- **What:** The candidate's live includes are the head frame (candidate L1–4), the credit pair (candidate L8, L17), the toggle-sidebar at the module's head (candidate L275, repointed from `:scp-wiki:` to `:scp-jp:` — block B70), and the two image-block specimens (candidate L67–68, section 4). The usage example names the local form `@@[[include theme:ragnarok-theme-jp]]@@` (candidate L49), the deliverable convention for a same-wiki include. The original's one component include beyond furniture, `component:image-block`, is unprefixed on both sides.
- **Why:** P1 (KB-15) for the toggle-sidebar repoint; ruling 4 is not engaged — no component had to be ported alongside this theme.
- **Verify:** `grep -n '\[\[include' candidate.txt` — frame, credit pair, toggle-sidebar, two specimens, and the escaped usage line.
- **Disposition:** Applied; no foreign include kept, no named exception needed.

### 3. Delivery and code loading

- **What:** This theme's delivery is a live module, and both sides share the mechanism exactly: at the tail, a div conditioned on the negative theme tag (`[[div [[iftags -theme]]...]]`, original L267; candidate L273 with the tag localized) wraps the toggle-sidebar include and a `[[module CSS show="true"]]` holding the entire stylesheet (original L271–1219; candidate L277–1225), banner first. There is no `[[code]]` block on either side (census: zero in both files) and the original has no frame and no separate delivery import — including the theme page transcludes the module, and that is the delivery. **Frame paragraph (the M-frame addition):** the candidate adds one frame at the head (candidate L1–4): `:scp-jp:component:interwiki-style` at `priority=1` with `theme=` naming the candidate's own `local--code/1` on the draft host. FIX4-IWA (commit 8c62b7b) added it under the ledger's P6 line ("missing interwiki frames added to 31 themes", KB-07a), and the ledger records P6 FIXED for this theme. The frame's form is the population standard; its target is not there. Probe made for this package (2026-11-17): the named fragment on the draft host returns the 25-byte plain text "No valid codeblock found." — the same host serves a real fragment for a code-exhibit theme (the control probe returned path-of-jinin-jp's CSS), so the answer is about this page, not the host. The frame therefore contributes a failed stylesheet request to every page that uses the theme, and nothing else; the theme renders because the live module delivers the CSS, as the render row confirms (section 12). The declared-vs-bytes comparison the class calls for is one-sided here: the original declares no frame and delivers by module; the candidate declares the frame and still delivers by module. This package flags the frame's target as a defect (per-theme record) and narrates the module as the delivery of record.
- **Why:** P4/T9 for delivery topology and P6/T3 (KB-07/KB-07a) for the frame: a frame entry is a delivery claim, and a claim naming a fragment the page does not contain is a broken layer even when another mechanism carries the load — it misleads the next editor about which mechanism is load-bearing, and removing the "redundant" module in its favor would break the theme outright.
- **Verify:** `grep -c '\[\[code' candidate.txt` — zero; read candidate L273–277 for the actual delivery; the probe URL is the frame's own `theme=` value at candidate L3.
- **Disposition:** FIXED per the ledger (P6, frame waves, checker-verified) as to the frame's presence; its target is **flagged as a defect** (per-theme record). The module delivery itself is standing, unchanged from the original.

### 4. Fonts and assets

- **What:** Fonts (blocks B71, B72): the original loads three faces from fonts.bunny.net (New Tegomin, Changa, Courier Prime; original L285–287). The candidate loads the same three from Google Fonts and adds Noto Sans JP to the Changa import (candidate L291–293); the body stack then gains the JP fallbacks (candidate L298: `'Changa', 'Noto Sans JP', 'Hiragino Kaku Gothic ProN', 'Yu Gothic', Meiryo, sans-serif`). Every face named in the candidate's stacks is loaded by those imports (Changa and Noto Sans JP directly; the remaining names are platform fonts). A prose note the porter added above the module states the font position (candidate L269: the faces in use are open-license Google Fonts faces, and Japanese glyphs fall back to Noto Sans JP — section 10). Assets: four references to the original's file area remain on scp-wiki.wdfiles.com — the two image-block specimens, whose bare file names the candidate spells out as absolute URLs into the original's file area (candidate L67–68), the starfield background in the live CSS (candidate L307), and the `--lgurl` header logo (candidate L1222). T4 charged exactly these four as a direct-link violation with an EN-availability dependency (LOCALIZE-ROWS row 127, type 5, display-affecting), and T1's four errors are the same four. They are not oversights: the ledger dispositions them (below).
- **Why:** P7 (KB-16) for the font host move and the stack supplement — the bunny.net faces are the same families on Google Fonts, and the JP fallback is the population's standard completion. P5 (KB-17) is the rule the four hotlinks breach; KB-58 is the standing exception that covers them: image hosting for the composition is owner-deferred, so EN-host originals stay until the hosting decision lands, here as in the raisa packages.
- **Verify:** Read candidate L291–298 against original L285–292; `grep -n 'scp-wiki.wdfiles.com' candidate.txt` — exactly the four lines above.
- **Disposition:** DISPOSITIONED (P5, class (ii) / KB-58; GOSIGN2-LEDGER §(c3) for this theme). The font changes are applied.

### 5. Header, sidebar, and site furniture

- **What:** The header defaults live in the module's `:root` and `::before` rules. The candidate translates the subtitle default: `content: var(--header-subtitle, "The End of All Things")` becomes `"万物の終わり"` (original L370 → candidate L376, block B73), while the title default `"R A G N A R O K"` is carried unchanged (candidate L371) — a spaced Latin display string, the theme's wordmark form, kept as the original's display text. The usage-notes specimen of the same variables is translated with it (candidate L55–59). The toggle-sidebar include crosses at the module's head (section 2); no P8 layout adaptation was needed, and the render row's findings are the environment items of section 11, not furniture defects.
- **Why:** P9/T6: a rendered default string is page text and localizes with the prose; the wordmark's letter-spaced Latin form is the design's display form (the ruling-2 family: header language as design, judged per theme — here the subtitle, a sentence, is translated and the wordmark, a logotype, is not).
- **Verify:** Read candidate L371–378 against original L365–372.
- **Disposition:** Standing.

### 6. Text translation

- **What:** The specimen body is translated in full (the 47 TRANS-UNANCHORED blocks and 19 TRANSLATION-ANCHORED blocks are this section's mass): the usage notes, the heading/link/blockquote/table/list specimens, the tabview and collapsible specimens, the footnote and reference specimens, and the closing notes, in the original's order. The attribution prose and the image-attribution collapsible are translated at candidate L20–41 (section 1). The stylesheet's own comments cross untranslated inside the module, as code comments do across the population, apart from the delivery changes of sections 3–4. The two residue blocks are specimen furniture of this same mass (appendix): the "+ Attribution:" heading pair (B5) and a collapsible specimen's label (B60, "Example" → 「例」).
- **Why:** P10: the body is the theme's documentation, and a JP reader gets the whole of it; anchored and unanchored blocks are the same class at different signature strengths, resolved together here and in the appendix.
- **Verify:** Read any specimen span on both sides (for example original L66–120 against candidate L70–124).
- **Disposition:** Standing.

### 7. Links

- **What:** The credit block's source link (candidate L16) names `https://scp-wiki.wikidot.com/theme:ragnarok-theme` — the host review/sources.tsv records for the original; no host defect. The attribution prose's one page link names the base theme: the original's `[[[theme:penumbra]]]` becomes a full-URL link to the EN Penumbra page with translated link text (candidate L24, block B6) — the base theme is referenced, not depended on (this theme is a standalone variant, not a layer over Penumbra's delivery), so the prose link stays a link to the original work. No prose link in the candidate targets a foreign wiki for a mechanism.
- **Why:** P11: prose links take the JP counterpart where the reference is to the ported composition, and the serving original where the reference is historical — the Penumbra credit is the second kind.
- **Verify:** `grep -n 'wikidot.com' candidate.txt` — the source link, the Penumbra link, and the delivery/asset hosts of sections 3–4.
- **Disposition:** Standing.

### 8. Structure

- **What:** The localize.md closing rule holds for the stylesheet: variable names, selectors, and rule order inside the module match the original's, and a brace-depth scan of both files closes at depth 0 with no negative excursion. The page-level structure changes are the furniture swap (section 1), the head frame (section 3), and the porter's font note line above the module (candidate L269). The specimen census (headings, links, blockquotes, tables, lists, tabview, collapsibles, footnotes, image-blocks) is present on both sides in the same order; the module's internal census (banner, imports, `:root` defaults, media queries) likewise. No CSS block was dropped: the diff inside the module is the font imports, the body stack, the subtitle default, and one blank line (section 9).
- **Why:** R3's distinction is met by the census; the two EXHIBIT-RESTRUCTURE primaries adjudicate to include repoints (appendix note in the Class summary), there being no exhibit in this page.
- **Verify:** Compare `grep -n '\[\[tab\|\[\[module\|\[\[include' original.txt candidate.txt`; the depth scan is re-runnable over either file.
- **Disposition:** Standing; no structural deletion, no class I item.

### 9. Formatting only

- **What:** One WS-ONLY block (B74): a single blank line inside the module (original L562–563 → candidate L568–569). It changes no rule and is the whole of this section; the candidate's line growth (+6 net) is furniture and translation, not formatting churn.
- **Why:** Formatting churn is disclosed as its own class so it is never mistaken for a semantic change.
- **Verify:** diff.md's module hunks.
- **Disposition:** None required; disclosed.

### 10. Porter annotations

- **What:** One annotation, in prose form: candidate L269, directly under the "++ ソースコード" heading — **フォント:** 使用している欧文・和文書体はいずれもGoogle Fontsで配信されるオープンライセンスの書体です（SIL Open Font License など）。日本語文字はNoto Sans JPにフォールバックします。 It discloses the font license position and the fallback the port introduced (section 4), in the reader-facing text rather than a comment. No comment-form porter annotation exists in the file; the module's banner is the author's own, carried verbatim.
- **Why:** R2: porter-added text is part of the change record; a disclosure placed in the documentation body is still a porter addition and is recorded as one.
- **Verify:** Read candidate L268–269.
- **Disposition:** Standing.

### 11. Dispositions and exceptions

- **What:** Three items, each with its ground. (1) The four scp-wiki.wdfiles.com hotlinks (candidate L67, L68, L307, L1222): T1's four errors and T4's type-5 finding, dispositioned as class (ii) under KB-58 — image hosting for the composition is owner-deferred, so the original's hosted files stay the source until that decision lands; the dependency on EN-site availability that T4 recorded is the accepted cost of the deferral, stated here rather than softened. (2) The render row's page item: runtime-hotlink site-theme chain only (KB-40 — the hosts arrive via the shared site theme chain, not this candidate). (3) The render row's sample item: the T2 run returned no machine verdict (render_check exit 2), a coverage caveat the ledger dispositions as not a theme defect — the sample's render evidence for this theme is thinner than the population's, and that is on record here. **Not a disposition:** the head frame's nonexistent target — flagged below with its probe evidence; the ledger's P6 FIXED line is quoted there alongside the bytes. The ledger's determination for this theme is PASS and this package does not re-open it.
- **Why:** A disposition is a decision with grounds (AGENTS.md §3 classes (i)/(ii)/(iii); the named KB entries), not an omission; a byte-level defect is flagged, never dispositioned by relabeling.
- **Verify:** Each item names its deciding record above and in the per-theme record.
- **Disposition:** DISPOSITIONED (items 1–3); the frame flag stands as a flag.

### 12. Verification

- **What:** (a) T1 source check (T1-ROWS row 152): exit 1, 4 errors / 2 warns / 1 info; all four errors are the hotlinks of section 11(1), class (ii); there is no class (i) error. (b) T2/T3 render (RENDER-ROWS-2 row 41, lane RENDER-S2-C (EN17)): the raw marks read FAIL/FAIL with the combined report FINDINGS — the two items of section 11(2–3), both dispositioned; the page itself rendered through its live module, which is the delivery evidence section 3 relies on. (c) T4/T5 (LOCALIZE-ROWS row 127): FINDINGS jointly, display-affecting findings 2 (the hotlink set; the missing frame). (d) This package is self-verifying: `python3 review/build_review.py --check` regenerates diff.md and the verdict stamp from the two byte-faithful copies in this directory and compares. Counts in this README are the generator's (difflib, autojunk off): +168/−169 in 74 change blocks / 9 hunks; the brace-depth scan and the fragment probe were run for this package.
- **Why:** Verification claims name the cheapest deciding check and its result, not a general assurance.
- **Verify:** Re-run the checker on `pages/theme:ragnarok-theme-jp.txt`, `python3 review/build_review.py --check` in this repo, and the probe in the per-theme record.
- **Disposition:** PASS (GOSIGN2-LEDGER (b) row 127; go-sign, COMPLETION-REPORT §10).

## Per-theme record

### The added frame names a code fragment this page does not contain (defect flag, probe-verified)

Candidate L1–4 is the standard frame: `:scp-jp:component:interwiki-style`, priority=1, `theme=https://sigma10-jp-test.wdfiles.com/local--code/theme%3Aragnarok-theme-jp/1`. The candidate contains no `[[code]]` block (census: zero; the stylesheet is the live `[[module CSS]]` at candidate L277–1225, as in the original). Probe made for this package (2026-11-17): that URL returns the 25-byte plain text "No valid codeblock found." A control probe on the same host for a code-exhibit theme (theme:path-of-jinin-jp) returned its CSS, so the answer is a property of this page, not of the host. The frame was added by FIX4-IWA (commit 8c62b7b, "missing interwiki frames added to 31 themes", KB-07a), and the ledger records P6 FIXED for this theme — true of the frame's presence, which is what the wave's checker verified. What the wave's template did not check is the delivery topology it was templating onto: for a live-module theme, the standard frame's self-address names nothing. The practical consequences today are small (one failed stylesheet request per page view; the module carries the theme, and the render row passed on that basis), but the hazard is real: the frame asserts that the theme's delivery is its first code block, and an editor who believes the assertion and removes the "duplicate" live module would strip the theme's CSS entirely. The repair is a judgment call for the coordinator's fix lane — remove the frame from live-module themes, or leave it as a deliberate no-op with a comment saying so — and this package makes neither edit, per the review protocol. The same check belongs on the other FIX4-IWA recipients whose delivery is a live module; that sweep is proposed in the batch report.

### The residue blocks, adjudicated

Two blocks carried no label. Both are translation mass of section 6, left unlabeled because neither carries a signature anchor:

| Block | Span | Adjudication |
|---|---|---|
| B5 | original L18–19 → candidate L22–23 | The "+ Attribution:" heading pair, translated to "+ 帰属:" — section 6 prose furniture |
| B60 | original L196 → candidate L200 | A collapsible specimen's label, "Example" → 「例」 — a specimen-string translation inside the documentation body |


### Post-package repairs (REFRESH3-D)

Recopy was a verified no-op: `candidate.txt` is byte-identical to the current canonical `pages/theme:ragnarok-theme-jp.txt`. No repair lands after this package's candidate build, so the record below is the slice's sub-shape and remedy, confirmed present in the built bytes.

- **FIX-FRAMEADDR, sub-shape (B) — Introduced** (report `R/review-scout/FIX-FRAMEADDR.md` §2; landing `722ceb5c949172bb5185d51ef56ce4119ee4fa91`, 2026-11-17): the original carries no interwiki-style frame and no `theme=` self-address in that role; the porting wave introduced the frame with `theme=` naming its own draft-host `local--code/theme%3Aragnarok-theme-jp/1`, a fragment the page does not carry (delivery is the inline `[[module CSS]]`). Remedy: the single `| theme=...` line was deleted; the frame include and its `priority=1` line are kept. Current candidate frame at L1.
- No further post-package repair touches this file.

Stamp treatment follows the jiha-jp / alexylva-university-jp precedents: the regenerated verdict stamp reads STALE, no re-judgement is fabricated, and the frozen GOSIGN2 ledger remains the verdict record.

## Change set outside the two diffed files

The diff covers two files; this theme's record is one file larger. `pages/theme-decoration-sample-ragnarok-theme-jp.txt` is the decoration sample the render checks ran against (its coverage caveat is section 11(3)); it belongs to this theme's record but carries no port change of its own to explain here. There are no companion fragments, no shared base file, and no inbound-link repairs in other candidates for this theme.
