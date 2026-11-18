# Review package — theme:paperstack-jp

<!-- BEGIN GENERATED VERDICT STAMP — do not hand-edit; regenerate with review/build_review.py -->
## Verdict stamp
- Theme: theme:paperstack-jp — origin EN, population #26 [GOSIGN2-LEDGER (b) row 26]
- Overall: STALE — candidate file changed since the verdict was computed (verdict against 435a6bb-era content, file sha256 now 9144ac0a445e361c4ed83178b59bc9ab3c71d3fbf3c13ec5c339db5ba60cdbee); verdict not carried over, re-judgement required
> verdicts below describe the pre-change file
- T1 (source check): FINDINGS (classified) — baseline 2026-11-16: exit 1, 5 errors / 1 warn / 5 infos (http×3, pseudo-ref×2); standing classes dispositioned in register c1 [T1-ROWS row 26; GOSIGN2-LEDGER (b) row 26]
- T2/T3 (render, combined verdict): FINDINGS — [combined T2/T3] report `FINDINGS` — sample T2 incomplete (webkit-320 screenshot >32767px ×4, no summary), notice×sidebar/clip, WebKit CC "S", giant "9999"/"THEME-IEL" demo text over intro, 875px@768 overflow, heading wrap, sample credit-modal. [RENDER-ROWS-1 (RENDER-C row 26)]
- Engine coverage: full matrix as run by the lane; coverage not separately caveated in the row [RENDER-ROWS-1 row]
- Credit modal: sample credit-modal errors dispositioned preview-form (credit:start-preview has no modal mechanism; GOSIGN-TESTS T2 amendment, 2026-11-16; ROWS-1 phrases the line bare and takes the disposition from the part header) [RENDER-ROWS-1 (RENDER-C row 26)]
- T4 (localize patterns + follow-up): FINDINGS — display-affecting findings: 0 [LOCALIZE-ROWS row 26, source LOCALIZE-B]
- T5 (translation text): FINDINGS — the source reports judge T4/T5 jointly; one verdict word covers both [LOCALIZE-ROWS row 26]
- FIX5 re-judgement: none — no OPEN items at the ledger determination [GOSIGN2-LEDGER (b) row 26]
- Computed against: canonical commit 1c96ee4f6dbe58243d8c4ba0136a4a4dde806972; candidate file pages/theme:paperstack-jp.txt sha256:9144ac0a445e361c4ed83178b59bc9ab3c71d3fbf3c13ec5c339db5ba60cdbee; record: GOSIGN2-LEDGER.md + GOSIGN2-LEDGER-SUPPLEMENT.md as of the FIX5 head 435a6bb
<!-- END GENERATED VERDICT STAMP -->

## Status

| | |
|---|---|
| Verdict | **PASS** — passed at the ledger determination; this theme had no OPEN items and no §(e) register entry (GOSIGN2-LEDGER (b) row 26). The stamp reads PASS: no post-verdict change touched this candidate |
| Standing items | **DISPOSITIONED** — the render row's items (the cross-cutting overflow families KB-33/KB-34, the credit-modal preview form KB-32, the T2 screenshot coverage caveat, section 11); T1's pseudo-ref pair (posting class). **Recorded, not charged:** the three legacy-http storage links (T4's nit, section 4). **One flag from this package:** the candidate's head frame names a code fragment this page does not contain — the same live-module topology as ragnarok-theme-jp, with the mitigating fact that the production migration does not carry the frame (per-theme record) |
| Go-sign basis | COMPLETION-REPORT.md §10 (go-sign issued; 81 FIXED / 26 DISPOSITIONED / 0 OPEN across the sweep) |
| Named exception | None for this theme (the sweep's single named exception is theme:amethyst-v2, which has no candidate) |

## Provenance

| | Original | Candidate |
|---|---|---|
| Page | theme:paperstack | theme:paperstack-jp (candidate for the existing production page theme:paperstack) |
| Wiki | scp-wiki.wikidot.com | SCP-JP Sigma-10 candidate (canonical repo) |
| Reference revisions | **Two:** first translation rev 71 / re-translation rev 105 (the mirror is the later, re-translation revision; the candidate's credit block records both) | — |
| Source of this copy | Campaign mirror store (class COPY, hash-verified against review/sources.tsv) | Canonical file `pages/theme:paperstack-jp.txt`, copied at worktree HEAD 2aee861 |
| Lines / bytes | 608 lines / 15,669 bytes | 873 lines / 20,321 bytes |
| SHA-256 | be8532db8e03c98304afe7f94c243bf9bb06124c40aa5f61b76b3a184c6f5872 | b64341764eadf9dafcf741c4ac99f8b64f5746fb298beef9b2d0096d9ed6032b |

**This package has a third source, and the review is three-way.** SCP-JP already has this theme: the production page theme:paperstack (in this repo as `pages-existing/existing:theme-paperstack.txt`, 805 lines; sources.tsv records its drift against live as 一致， agreeing). The production page descends from ukwhatn's 2021 translation of rev 71 and has been maintained on JP since. The candidate is the re-translation vehicle against rev 105, built on the production page's lineage: measured against production, the candidate differs by 173 lines in 11 hunks (the frame, the credit block, specimen host repoints, and the rev-105 incorporations), while measured against the EN rev-105 mirror it differs by +650/−385 — most of that distance is the production lineage itself, not new porting. The migration actually delivered to production this round is smaller still and is a separate artifact: `pages/phase17-diff-paperstack-jp.txt`, whose own text states that upstream's rev 71→105 rewrite (header structure, CSS variables, selectors) cannot be applied as a local diff and needs a re-port, so this round changes **nothing but the credit record** on the production page. sources.tsv also records that the original has been superseded upstream since the reference revision; the follow-up diff artifact (diff-paperstack-from71, in the campaign record) is the K5a-i homework that tracks it. Every section below therefore names which pair it is comparing.

Wave history: the candidate was recorded at the canonical-sources commit (d727e92), carried through the Phase 17 revision recording (8dcac74) and the Phase 22 drift decisions (d2a9dc0), received the T1 credit fixes (b816e10), and was last touched by FIX3-B (6ae6516), the LOCALIZE-B fix wave for its row — which is why the stamp computes against 6ae6516 and reads PASS.

## Summary

EstrellaYoshte's Paperstack — a Containment Breach-inspired theme, and the base under several other themes in this population (ragnarok-theme-jp's banner credits it). Its EN rev-105 page delivers from a code exhibit plus a sigma-plus include and a tail frame; its JP production page delivers from a live CSS module and has grown JP-only corrections over five years of local maintenance. The candidate holds both inheritances at once: the production page's body, header specimen, stylesheet, and correction modules, re-translated and re-checked against rev 105, with the campaign's furniture (head frame, full credit block) added. The honest one-line summary for a reviewer is: against production this is a small, auditable delta; against the EN mirror it is a large diff whose bulk is five years of JP maintenance that predates the campaign, and the package's job is to keep those two statements separate. T4's row found no unincorporated display-affecting upstream updates and zero display-affecting findings, and the ledger passed the theme. The one defect this package adds is the batch's recurring one: the head frame names `local--code/theme%3Apaperstack-jp/1`, and this page has no code block for the fragment to serve (probe: "No valid codeblock found."). Production is not exposed to it — the phase-22 migration diff adds no frame — so the flag is recorded against the candidate vehicle, with the family sweep proposed in the batch report.

## Class summary

Auto-classification by review/classify_hunks.py (signature table 2026-11-17.1), run with the production page declared (`--production`), on the original↔candidate pair: 110 change blocks — 21 specific (19.1%), 68 heuristic (61.8%), 21 residue, 0 skipped. Pattern citations below name the KB entry; the patterns/ tree state cited throughout is commit 9c5e9079afb01d30cb9fc4ef9d714e5591eb2ffa.

| Label | Blocks |
|---|---|
| CSS-BODY | 42 |
| TRANS-UNANCHORED | 27 |
| TRANSLATION-ANCHORED | 7 |
| EXHIBIT-RESTRUCTURE | 5 |
| DRAFT-HOST | 3 |
| HEADERVAR | 3 |
| SELF-DELIVERY | 3 |
| IFTAGS | 2 |
| ESCAPED-INCLUDE | 2 |
| INCLUDE-REPOINT | 2 |
| T7-CREDIT-CSS | 2 |
| CREDIT-PREVIEW | 1 |
| FONT-IMPORT | 1 |
| JPFONT-LOAD | 1 |
| RESTORATION | 1 |
| SIGMA-PLUS-JP | 1 |
| TASL-FIELDS | 1 |

Adjudication for this README (every block was read against the bytes, and the CSS blocks against the production page as well): the 42 CSS-BODY blocks are the production lineage's stylesheet read against the EN mirror — section 8 gives the three-way census that separates inherited JP maintenance from this campaign's changes, and no CSS-BODY block is a campaign edit except where a section below says so. B109's SIGMA-PLUS-JP label fires on the original's tail delivery span (the sigma-plus include the candidate does not carry; section 2 gives the production comparison that adjudicates it). B92's RESTORATION label is the JP header-container ruleset (candidate L747–767), the stylesheet half of the JP header form the body specimen uses — retained production substance, not an EN restoration. The 21 residue blocks collapse into the appendix table. After adjudication no block is left unexplained.

## Standing sections

### 0. Header and provenance frame

- **What:** Theme theme:paperstack-jp; original theme:paperstack on scp-wiki at reference revisions 71 (first translation) and 105 (re-translation; the mirror is rev 105); candidate `pages/theme:paperstack-jp.txt`; production counterpart `pages-existing/existing:theme-paperstack.txt`. Provenance route: kind K6 — a pre-existing JP page with its own translation lineage, the only kind in this batch with a production third source. The candidate opens with the frame (candidate L1–4) ahead of the gate `[[iftags +テーマ]]` (candidate L6); the production page opens with the gate alone (production L1); the original opens with the gate `[[iftags +theme]]` (original L1).
- **Why:** Section 0 declares the provenance route so every later count is read against the right baseline — for this theme there are two baselines, and mixing them is the one error this package exists to prevent.
- **Verify:** The sources.tsv row for paperstack-jp (kind K6, both reference revisions, the production-drift 一致 record); `sha256sum original.txt` against the Provenance table.
- **Disposition:** Standing (the route itself); per-section dispositions follow the pair each section compares.

### 1. Credit and attribution

- **What:** The candidate's credit block (candidate L8–18) carries nine fields — the ruling-3 eight plus the re-translation field this theme's two-revision provenance requires: title Paperstackテーマ; **翻訳責任者 ukwhatn**; 翻訳年 2021; 原題 Paperstack Theme; 著作権者 EstrellaYoshte; 作成年 2020; 初訳時参照リビジョン 71; 改訳時参照リビジョン 105; the source link (section 7). The translator field names the human translator of the production page, not AI: ukwhatn translated the page in 2021 and the production stylesheet's banner still reads "Edited by ukwhatn for SCP-JP" (candidate L224, carried from production) — the attribution rule for pre-existing translations is that the live JP creator's name stands, and this block follows it. The author field is exact against the original's prose (original L40: made by [[*user EstrellaYoshte]]) and banner (original L163). T4 charged the candidate's earlier form with six missing credit fields (LOCALIZE-ROWS row 26, item (b)); the FIX waves completed the block, and the nine fields above are the completed form. The floated bare `[[module Rate]]` at candidate L24–26 is **kept**, as in the original (original L7–9) and production (production L7–9): on this page the Rate is part of the theme's header furniture that users paste with the header block (the usage examples at candidate L63–115 include it), not a duplicate of the credit module. The production migration's credit change is deliberately smaller than the candidate's block: the phase-22 diff adds a three-field record （初訳時参照リビジョン / 改訳時参照リビジョン / 元記事リンク） after production's gate, because production's attribution already lives in its banner and page history, and the diff artifact's scope is the credit record only.
- **Why:** P3/T1 (KB-09) for the block's completion; the campaign's TASL record (ruling 3) with its standing exception for pre-existing human translations, which is what keeps ukwhatn's name in the translator field.
- **Verify:** Read candidate L8–18 against original L40 and L160–169; read the phase-22 diff artifact's code block for the production form.
- **Disposition:** FIXED (the T4 credit finding, by the credit waves and FIX3-B); the translator attribution stands as the production page's own record.

### 2. Includes and components

- **What:** The candidate's live includes are the head frame (candidate L1–4), the credit pair (candidate L8, L18), the image-block specimens (candidate L43, L117–122, L126–131, L135–140), and the escaped usage examples naming `:scp-jp:theme:paperstack` — the **production** page name, without `-jp` (candidate L64, L100): correct for this topology, since the deliverable migrates theme:paperstack itself and a user copying the example must reach the production page. The original's one component dependency beyond furniture is `component:sigma-plus`, included after its gate (original L599) and named in its prose as the theme's base (original L40). The candidate does not carry it — and neither does the production page (census: no sigma-plus in either file). On JP the Sigma base furniture arrives via the site theme chain (the KB-40 layer), as it does for the live production page today; sigma-plus carries no Paperstack rules, so nothing of the theme's own CSS is dropped with it. Block B109's SIGMA-PLUS-JP label marks exactly this span, adjudicated here against the production census rather than narrated as a supplement or a loss.
- **Why:** P1 (KB-15) for repoints; the sigma-plus adjudication follows the standing rule that a mechanism's absence is judged against what carries its load in the target composition — here, production itself is the evidence.
- **Verify:** `grep -n 'sigma-plus' candidate.txt` and the same on `pages-existing/existing:theme-paperstack.txt` — both empty; `grep -n '\[\[include' candidate.txt` for the live set.
- **Disposition:** Applied; the sigma-plus form is adjudicated standing for this topology (production parity), not an exception.

### 3. Delivery and code loading

- **What:** Three topologies, one per source. The **original** delivers from a `[[code]]` exhibit (original L159–596) by three tail mechanisms after its gate: the sigma-plus include (L599), a `[[module CSS]]` importing its own `local--code/1` from scp-wiki.wdfiles (L600–602), and a `[[div_]]`-wrapped frame at priority=1 naming the same fragment (L604–608). The **production page** delivers by one mechanism: a live `[[module css show="true"]]` inside the negative-tag div, carrying the JP stylesheet and its correction modules — no frame, no code block, no tail import. The **candidate** follows production: the live module at candidate L213 (inside the div at L212) carries the main stylesheet to L826, followed by the six JP correction modules (candidate L829–873, section 10). **Frame paragraph (the M-frame addition):** the candidate adds the standard head frame (candidate L1–4, priority=1, `theme=` naming its own `local--code/1` on the draft host) — the form T4's row recorded as missing (LOCALIZE-ROWS row 26, item (a): P6 missing interwiki-style) and the fix waves supplied. The target does not exist: the candidate has no `[[code]]` block (census: zero), and the probe of the frame's own URL returns "No valid codeblock found." (per-theme record). Production is not exposed: the phase-22 migration diff adds no frame to the production page, which keeps its working live-module delivery. The flag therefore lands on the candidate vehicle — a reviewer approving the candidate as a posting text would carry a broken delivery claim into it — and not on the production migration, whose delivered form is frame-free by design.
- **Why:** P4/T9 for topology, P6/T3 (KB-07) for the frame: a frame entry is a delivery claim, and on a live-module page the claim names nothing. The class's declared-vs-bytes comparison runs the other way here from the usual case — the bytes (production's five-year working form) are right and the templated declaration is wrong.
- **Verify:** `grep -c '\[\[code' candidate.txt` — zero; read candidate L212–213 for the actual delivery and original L596–608 for the original's tail; the probe URL is the frame's own `theme=` value at candidate L3.
- **Disposition:** FIXED per the ledger's frame line as to presence; the frame's target is **flagged as a defect** (per-theme record). The live-module delivery is standing (production parity).

### 4. Fonts and assets

- **What:** Fonts (blocks B52, B53): the candidate's stylesheet opens with the production lineage's font set, all Google Fonts (candidate L227–233): Noto Sans JP and Sawarabi Gothic under a "Japanese Font" comment, Josefin Sans and Oxygen under "English Font", and Fira Code for the code stack (candidate L240, L259–260). Against the EN mirror this replaces rev 105's bunny.net IBM Plex Sans import and its jsdelivr-hosted Josefin Sans `@font-face` (original L171–180) — but the replacement is production's, predating the campaign: the JP page never took the EN font set, and T4 recorded no unincorporated display-affecting upstream updates for this theme, the font difference being part of that judgment. Every face named in the candidate's stacks is loaded by its imports. Assets: the logo image moves from the original's scp-wiki.wdfiles URL to the candidate's draft-host file area (candidate L21), where production names the scp-jp.wdfiles form of the same file (production L4) — the candidate's form is the draft state of the same repoint. The header specimen's test.png is re-hosted to the candidate's draft area (candidate L43); production still names the EN host for it (production L26). Three example image-block URLs name real JP storage files over legacy http (candidate L118, L127, L136) — T1's three http errors and T4's item (c), which T4 itself graded a nit; they are the production page's own worked examples, carried unchanged.
- **Why:** P7 (KB-16) for the stacks (complete: every named face loaded); P5 (KB-17) for the re-hosting, with the http trio recorded as the standing nit they were charged as — scheme-only, on the JP storage host, in example text.
- **Verify:** Read candidate L227–240 against original L171–180; `grep -n 'http://' candidate.txt` — exactly the three storage lines.
- **Disposition:** Applied (fonts, as production inheritance); the http trio stands as T4 recorded it (nit, not a defect class).

### 5. Header, sidebar, and site furniture

- **What:** The header specimen is the JP form on both JP sources: the `header-container` with text-item and grid-item blocks (candidate L28–46; production L11–29), where the EN rev-105 body restructured it into `header-container-ex` with a header-info flex (original L11–28). The candidate keeps the JP form — the phase-22 artifact's own reasoning (the upstream restructure cannot be locally diffed; a re-port is a separate decision) — and its stylesheet carries the matching `.header-container` ruleset (candidate L747–767, the RESTORATION-labeled block). The tail correction modules include the JP sidebar and masthead fixes (candidate L851–861: the tablet sidebar overflow containment and the narrow-header top-bar placement), inherited from production's maintenance. The render row's sidebar-adjacent items are the cross-cutting families of section 11, not furniture defects in this file.
- **Why:** P9/T6 judged against the production baseline: the JP header form is the deployed contract JP articles already use, and replacing it with the EN rev-105 form is the re-port decision the phase-22 artifact explicitly defers — recording that deferral is this package's job, not relitigating it.
- **Verify:** Compare candidate L28–46 with production L11–29 and original L11–28; read the phase-22 artifact's preamble.
- **Disposition:** Standing (production parity; the re-port deferral is the phase-22 record's own).

### 6. Text translation

- **What:** Against production, the candidate's body is the production body (already Japanese) with the rev-105 incorporations the Phase 17/22 records made; against the EN mirror, the translation mass is the 27 TRANS-UNANCHORED and 7 TRANSLATION-ANCHORED blocks — the specimen texts, the usage instructions, the font specimen labels (candidate L206: 等幅フォント: Fira Code), and the closing notes. The Lorem ipsum specimen paragraphs are carried as specimen text on all three sources. The one prose difference a reviewer should see: the original's introduction calls the theme a sigma-plus theme (original L40); the candidate's introduction (candidate L60) keeps the Containment Breach attribution and the author, without the sigma-plus clause — consistent with section 2's adjudication, and visible rather than silent because it is stated here.
- **Why:** P10 for the translation; the sigma-plus clause follows section 2 (a mechanism claim the JP composition does not make).
- **Verify:** Read candidate L56–60 against original L40–42 and production's corresponding span.
- **Disposition:** Standing.

### 7. Links

- **What:** The credit block's source link (candidate L17) names `https://scp-wiki.wikidot.com/theme:paperstack` — the host review/sources.tsv records for the original; no host defect. The phase-22 artifact links the production page and the original in its preamble (its own record, not the candidate's). No prose link in the candidate targets a foreign wiki for navigation; the EN-host references that remain are the asset and example forms of section 4.
- **Why:** P11: prose links take the JP counterpart or the serving original; the source link is the attribution record and names the original by design.
- **Verify:** `grep -n 'wikidot.com' candidate.txt` — the source link and the hosts of sections 3–4.
- **Disposition:** Standing.

### 8. Structure

- **What:** A brace-depth scan of both diffed files closes at depth 0 with no negative excursion. The structural story is the three-way census: (i) the candidate's stylesheet equals production's stylesheet plus the campaign delta — the main module's rules (candidate L213–826) are the production module's rules, including the JP font set, the header-container ruleset, and the credit rules the T7-CREDIT-CSS blocks mark (candidate L855–872 region: the narrow-header module and the credit-module correction, whose comment explains the retargeting — the EN theme styles the credit anchor through a `<p>` wrapper the JP credit module does not emit, so the JP page retargeted the selector with the EN declarations unchanged); (ii) against the EN mirror, the same stylesheet reads as 42 CSS-BODY blocks of churn, because rev 105 restructured what the JP page never adopted. No EN rev-105 CSS block was dropped *by the campaign*: the non-adoption is the production lineage's standing state, T4-verified as carrying no display-affecting unincorporated updates. The specimen census (header blocks, code examples, image-block examples, font specimens) is present on all three sources.
- **Why:** R3's distinction is met by the census; the CSS-BODY mass is inheritance measured against the wrong baseline if read naively, which is why this section names the baseline for every count.
- **Verify:** `diff pages-existing/existing:theme-paperstack.txt pages/theme:paperstack-jp.txt` — 173 lines in 11 hunks, against diff.md's +650/−385 for the EN pair.
- **Disposition:** Standing; no structural deletion by the campaign, no class I item.

### 9. Formatting only

- **What:** No WS-ONLY block fired in this pair (label count 0): the candidate's whitespace is production's, and the diff's blank-line pairs sit inside the labeled translation and CSS blocks rather than standing alone. The 21 residue blocks (appendix) are mostly of this character — blank-line and ordering pairs in the specimen region — but none is a pure formatting block the classifier could sign, so this section's count is honestly zero and the residue table carries the detail.
- **Why:** Formatting churn is disclosed as its own class; here the disclosure is that there is none separable from the labeled mass.
- **Verify:** classification.json's label counts (WS-ONLY absent); the appendix table.
- **Disposition:** None required; disclosed.

### 10. Porter annotations

- **What:** The candidate's tail modules carry the production page's own maintenance comments, in English, one per correction module (candidate L830, L840, L847, L852, L859, L864): the navigation correction, the narrow image-block correction, the narrow masthead fit, the tablet sidebar containment, the narrow-header top-bar placement, and the credit-module correction (whose comment, quoted in section 8, is the fullest mechanism note in the file). These are ukwhatn-era and later JP maintenance annotations, inherited by the candidate from production — not campaign porter comments — and they are the reason the JP corrections are auditable at all. The campaign's own additions (frame, credit block) carry no comment, as elsewhere in the population. The stylesheet banner's "Edited by ukwhatn for SCP-JP" line (candidate L224) is the production attribution, carried.
- **Why:** R2: added text is part of the change record; here the record distinguishes inherited annotations from campaign ones so neither is misattributed.
- **Verify:** Read candidate L829–873.
- **Disposition:** Standing.

### 11. Dispositions and exceptions

- **What:** Three items, each with its ground. (1) T1's two pseudo-ref errors: the candidate's references to not-yet-posted JP addresses — classes (ii)/(iii) by form; the posting procedure resolves them. (T1's other three errors are the http trio of section 4, recorded there as T4's nit.) (2) The render row's items, all in the campaign's cross-cutting families rather than this candidate: the sample T2 run incomplete (webkit-320 screenshot exceeding the 32767px height limit four times, no summary — a coverage caveat on a very tall page); notice×sidebar/clip and the 875px@768 overflow in the recorded families (static credit replica fixed width, KB-33; preview chrome, KB-34); the giant demo text and heading wrap, which are the theme's own specimen content rendering as designed; the WebKit CC "S" mark; and the sample credit-modal item (KB-32, ruling 5). (3) The upstream supersession: sources.tsv records that the original has moved past rev 105 upstream; the follow-up diff artifact in the campaign record is where that homework lives, and the ledger's PASS covers the rev-105 pair this package documents. **Not a disposition:** the head frame's nonexistent target — flagged below; and the EN header-form non-adoption, which is not an omission but the phase-22 record's stated decision (section 5). The ledger's determination for this theme is PASS and this package does not re-open it.
- **Why:** A disposition is a decision with grounds (AGENTS.md §3 classes (i)/(ii)/(iii); the named KB entries), not an omission; a byte-level defect is flagged, never dispositioned by relabeling.
- **Verify:** Each item names its deciding record above and in the per-theme record.
- **Disposition:** DISPOSITIONED (items 1–3); the frame flag stands as a flag.

### 12. Verification

- **What:** (a) T1 source check (T1-ROWS row 26): exit 1, 5 errors / 1 warn / 5 infos; the errors are the http trio (section 4) and the pseudo-ref pair (section 11(1)); there is no class (i) error. (b) T2/T3 render (RENDER-ROWS-1 row 40, lane RENDER-C (row 26)): the raw marks read FAIL/FAIL with the combined report FINDINGS — the items of section 11(2), all dispositioned in the ledger. (c) T4/T5 (LOCALIZE-ROWS row 26, lane LOCALIZE-B): FINDINGS jointly, display-affecting findings 0; the row's three items (missing frame; six missing credit fields; the http nit) are the pre-fix state that FIX3-B and the credit waves then closed, as sections 1 and 3 record. (d) This package is self-verifying: `python3 review/build_review.py --check` regenerates diff.md and the verdict stamp from the two byte-faithful copies in this directory and compares. Counts in this README are the generator's (difflib, autojunk off): +650/−385 in 110 change blocks / 5 diff sections; the candidate↔production count (173 lines, 11 hunks) is plain `diff`; the brace-depth scan and the fragment probe were run for this package.
- **Why:** Verification claims name the cheapest deciding check and its result, not a general assurance.
- **Verify:** Re-run the checker on `pages/theme:paperstack-jp.txt`, `python3 review/build_review.py --check` in this repo, the three-way diffs named in section 8, and the probe in the per-theme record.
- **Disposition:** PASS (GOSIGN2-LEDGER (b) row 26; go-sign, COMPLETION-REPORT §10).

## Per-theme record

### The head frame names a fragment this page does not contain (defect flag, probe-verified) After this package was built the head frame's `theme=` was removed (c3e658f), the two snippets re-applied in the `-jp` form (20ce290), and the head bare Rate deleted (1c96ee4); see the post-package repairs item below.

Candidate L1–4 is the standard frame: `:scp-jp:component:interwiki-style`, priority=1, `theme=https://sigma10-jp-test.wdfiles.com/local--code/theme%3Apaperstack-jp/1`. The candidate contains no `[[code]]` block (census: zero; its stylesheet is the live module at candidate L213–826 plus the six correction modules). Probe made for this package (2026-11-17): that URL returns the 25-byte plain text "No valid codeblock found." The history explains how the frame got here: T4 charged the candidate's production-form state with a missing interwiki-style include (LOCALIZE-ROWS row 26, item (a)), and the fix waves supplied the standard frame — the same templated repair as ragnarok-theme-jp's, onto the same live-module topology, with the same result. Two facts bound the flag's weight. First, the theme works: production has run for years on the live module alone, and the candidate inherits that delivery intact. Second, the production migration does not carry the frame: the phase-22 diff artifact adds only the credit record to theme:paperstack, so the broken delivery claim exists only in the candidate vehicle, not in anything scheduled to reach the live wiki. The flag is therefore recorded against the candidate as a posting text — if the candidate were ever posted as-is (for instance as the vehicle of the deferred re-port), its first four lines would assert a delivery that serves nothing — and the repair decision (remove the frame from live-module candidates, or annotate it) belongs to the coordinator's fix lane, together with the family sweep proposed in the batch report. This package makes no edit.

### The residue blocks, adjudicated

Twenty-one blocks carried no label. Read against the three sources, they resolve into three shapes, all inside the specimen body where the candidate follows production's wording and ordering against the EN mirror's:

| Blocks | Shape |
|---|---|
| B5, B8, B13, B15, B16, B19, B22, B25, B26, B27 | Blank-line and paragraph pairs in the header specimen and usage examples — production's spacing read against the mirror's (original L19–89 ↔ candidate L34–110) |
| B50, B51, B55, B60, B65, B69 | Single-line specimen and exhibit-boundary pairs at the source-code heading and inside the stylesheet's opening span (original L161–315 ↔ candidate L215–360) |
| B79, B84, B87, B102, B103 | Single-rule and blank-line pairs deep in the stylesheet (original L364–555 ↔ candidate L583–827), production-lineage ordering against the mirror's |

No residue block carries a delivery, credit, or asset change; each is accounted for by the section its span belongs to (6, 8, or 9).

### Post-package repairs (REFRESH3-C)

The items above describe this package as built. The repairs recorded below postdate the package; `candidate.txt` has been recopied from the current canonical `pages/<fullname>.txt` and `diff.md` and the verdict stamp regenerated with `python3 review/build_review.py`, so this package now documents the post-repair candidate. The regenerated stamp reads **STALE** by design: no re-judgement is fabricated here, and the frozen ledger (`GOSIGN2-LEDGER.md` + supplement, FIX5 head 435a6bb) remains the verdict record.

**FIX-SNIPPET — production-predecessor reference audit (landing 358955e).** `FIX-SNIPPET.md` records two self-reference exhibits as DRIFT ground D1 (own code addresses under `theme%3Apaperstack-jp`). Commit 358955e inserted `-jp` after the target at the then L64 and L100 lines, `theme:paperstack` → `theme:paperstack-jp`.

**Sequelae — c3e658f, 20ce290, 1c96ee4.** Commit c3e658f (frame (D) remedy re-applied to paperstack and penumbra) removed the `theme=` line from the head interwiki-style frame and reverted the two snippets to the plain form; commit 20ce290 (snippet repairs in paperstack and penumbra re-applied) re-applied the `-jp` insertion at the current L59 and L95; commit 1c96ee4 (head-zone bare Rates removed) deleted the 4-line head Rate block. The current candidate therefore has no `theme=` parameter in its head frame, the two snippets in the `-jp` form, and no head bare Rate — three repair layers over the package's as-built copy.

## Change set outside the two diffed files

The diff covers two files; this theme's record is the batch's largest. `pages-existing/existing:theme-paperstack.txt` is the production third source (Provenance; sections 0–8 cite it throughout). `pages/phase17-diff-paperstack-jp.txt` is the production migration deliverable (the credit-only diff of section 1). `pages/theme-decoration-sample-paperstack-jp.txt` is the decoration sample the render checks ran against (its items are section 11(2)); the repo also holds the production-name sample `pages/theme-decoration-sample-paperstack.txt`. The follow-up artifact diff-paperstack-from71 lives in the campaign record outside this repo (section 11(3)). There are no companion fragments for this theme; inbound dependents (themes whose banners credit Paperstack, ragnarok-theme-jp among them) layer over their own bases and are not part of this change set.

## License and attribution

- **Title:** Paperstack Theme
- **Author:** EstrellaYoshte
- **Source:** https://scp-wiki.wikidot.com/theme:paperstack — revision 105 (revision date 2026-04-12 05:15:56)
- **License:** Creative Commons Attribution-ShareAlike 3.0 (CC BY-SA 3.0) — license deed: https://creativecommons.org/licenses/by-sa/3.0/
- **Adaptation:** This package holds a Sigma-10 migration port of the work; changes were made. See "Summary" and "Standing sections" in this README for what changed and why. Translator: ukwhatn — a human translator credited by the live JP page and retained as the package records it (campaign-rule exception); where the campaign translated, the translator is AI.
