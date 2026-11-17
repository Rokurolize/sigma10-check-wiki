# Review package — theme:magazine-jp (CN → JP port)

<!-- BEGIN GENERATED VERDICT STAMP — do not hand-edit; regenerate with review/build_review.py -->
## Verdict stamp
- Theme: theme:magazine-jp — origin CN, population #203 [GOSIGN2-LEDGER (b) row 203]
- Overall: STALE — candidate file changed since the verdict was computed (verdict against 435a6bb-era content, file sha256 now 05bd91d95bb22c978f900f578b167221774bed41aeb8fdf47713c26f21da16e3); verdict not carried over, re-judgement required
> verdicts below describe the pre-change file
- T1 (source check): FINDINGS (classified) — baseline 2026-11-16: exit 1, 31 errors / 1 warn / 3 infos (pseudo-ref×30, hotlink×1); standing classes dispositioned in register c1 [T1-ROWS row 269; GOSIGN2-LEDGER (b) row 203]
- T2/T3 (render, combined verdict): FINDINGS — [combined T2/T3] report `FINDINGS` — page-overflow 1415px@1366 + 448px@320 + 525px@375 + 911–996px@768 + runtime-hotlink site-theme chain; sample T2 no machine verdict (exit 2, no summary). [RENDER-ROWS-2 (RENDER-S2-F (CN9))]
- Engine coverage: full matrix as run by the lane; coverage not separately caveated in the row (the row records inconclusive runs, carried verbatim above) [RENDER-ROWS-2 row]
- Credit modal: no credit-modal line recorded [RENDER-ROWS-2 (RENDER-S2-F (CN9))]
- T4 (localize patterns + follow-up): FINDINGS — display-affecting findings: 3 [LOCALIZE-ROWS row 202, source LOCALIZE-S2-D]
- T5 (translation text): FINDINGS — the source reports judge T4/T5 jointly; one verdict word covers both [LOCALIZE-ROWS row 202]
- FIX5 re-judgement: item 65 (class H) FIXED — FIX5-TEXTA §2, commit 6f6b349: untranslated residue at L7121, L7158, L7268/L7272 translated; source-wide grep found no further reader-visible CN residue [GOSIGN2-LEDGER-SUPPLEMENT (a) item 65]
- Computed against: canonical commit f5acc90cbb800f3c0752713589322929dac75821; candidate file pages/theme:magazine-jp.txt sha256:05bd91d95bb22c978f900f578b167221774bed41aeb8fdf47713c26f21da16e3; record: GOSIGN2-LEDGER.md + GOSIGN2-LEDGER-SUPPLEMENT.md as of the FIX5 head 435a6bb
<!-- END GENERATED VERDICT STAMP -->

## Status

| | |
|---|---|
| Verdict | **PASS** — go-sign re-run (this theme is one of the 286 of 286 pass-eligible themes); this theme's stamp is not stale, because the FIX5 commit is the candidate's last change |
| Blocking items at ledger time | GOSIGN2-LEDGER.md §(e) item 65 [H] (reader-visible untranslated CN residue at three loci in the documentation) |
| Re-judgment | GOSIGN2-LEDGER-SUPPLEMENT.md item 65: **FIXED** (FIX5-TEXTA §2, commit 6f6b349); re-derived from this package's bytes in the per-theme record |
| Standing items | **DISPOSITIONED** — ledger §(c3): P4 (the documentation source's non-exception host @import is original-state delivery, class (ii)), P10/T5 routed to item 65 [H], P11 (sibling-link class); ledger §(c2) render row: page-overflow at four widths and the runtime-hotlink site-theme chain (KB-40 environment layer), sample T2 no machine verdict (exit 2, no summary) recorded as a coverage caveat |
| Go-sign basis | COMPLETION-REPORT.md §10 (go-sign issued; 81 FIXED / 26 DISPOSITIONED / 0 OPEN across the sweep) |
| Named exception | None for this theme (the sweep's single named exception is theme:amethyst-v2, which has no candidate) |
| Defect flags raised by this package | Two, both minor and both recorded with evidence, neither edited: the attribution line's two EN-host links that return 404 (section 7), and one component rule whose font stack names a face the port loads nowhere (section 4) |

## Provenance

| | Original | Candidate |
|---|---|---|
| Page | theme:magazine | theme:magazine-jp |
| Wiki | scp-wiki-cn.wikidot.com | SCP-JP Sigma-10 candidate (canonical repo) |
| Reference revision | 488, as recorded in the candidate's credit block: **初訳時参照リビジョン:** 488 (candidate L11) | — |
| Source of this copy | Campaign mirror store (hash-verified against review/sources.tsv) | Canonical file `pages/theme:magazine-jp.txt`, copied at worktree HEAD 118306b |
| Lines / bytes | 8,087 lines / 195,464 bytes | 8,096 lines / 203,466 bytes |
| SHA-256 | eaa1e692fe0aa3e6caf4595189dff63f34a3820b8cddf096e1828ce7053fa39f | 782b936384d5f7db00220af5c6d628482effe2909faf54c7e3a112926ddab79b |

Follow-up note (sources.tsv, K5a-i): the original has been superseded upstream since revision 488; the campaign record holds a follow-up diff artifact (`diff-magazine-from488.txt`) for that later movement. This package's mirror stays at revision 488, the revision the port was actually made from; the supersession is recorded here rather than absorbed silently (section 12).

Wave history: the candidate was created by the Stage 2 CN9 integration (commit bbd273c); the Stage 2 rework (c839ec3) externalized the one external CSS file it had initially inlined; FIX-CREDIT-D (1869877) normalized its translator attribution; FIX4-MECH (a497307) removed the original's duplicated @imports (KB-65); FIX5-TEXTA (6f6b349) closed item 65 in three hunks and is the file's last content change.

## Summary

Magazine is a large standalone Sigma-9 theme: an 8,000-line page whose stylesheet is split across five code blocks, delivered to consumers through a live module, three tail imports, and the standard frame, with a long documentation body, worked exhibits, sample articles, and a set of include-parameter-gated variant modules at the tail (a collapsible-sidebar variant, an Ikagai Society variant, a Traditional Chinese edition, and a Wanderers' Library edition). The candidate preserves that topology exactly, repointing every delivery address from the CN hosts to the candidate's own draft-host addresses, translating the documentation, and reworking the font delivery: the original's subset @font-face loads and CN display-face stylesheet imports are replaced by a combined Google Fonts import carrying the JP faces, with the substitution documented in porter notes inside the file. Measured churn (diff.md, the generator's difflib count: +731/−722, 1,453 changed lines in 538 change blocks / 229 sections, Tier 2 format; a GNU-diff count gives 1,455) is dominated by CSS comment translation and documentation translation, not by structural change. The one blocking item was translation residue: three reader-visible spots the first translation pass missed, closed by a three-hunk FIX5 commit that this package re-derives locus by locus.

## Class summary

Auto-classification by review/classify_hunks.py (signature table 2026-11-17.1): 538 change blocks — 192 specific (35.7%), 338 heuristic (62.8%), 8 residue (1.5%), 0 skipped. Pattern citations below name the KB entry; the patterns/ tree state cited throughout is commit 9c5e9079afb01d30cb9fc4ef9d714e5591eb2ffa.

| Label | Blocks |
|---|---|
| ANNOTATION | 2 |
| COMMENT-TEXT | 219 |
| COMPONENT-SWAP | 2 |
| CONTENT-STRING | 4 |
| CREDIT-PREVIEW | 7 |
| CSS-BODY | 7 |
| DELIVERY-HOST | 5 |
| DRAFT-HOST | 24 |
| ESCAPED-INCLUDE | 1 |
| EXHIBIT-RESTRUCTURE | 1 |
| GLYPH-FORM | 48 |
| HEADERVAR | 1 |
| IFTAGS | 2 |
| INCLUDE-REPOINT | 7 |
| JPFONT-LOAD | 2 |
| LINK-REPOINT | 3 |
| SELF-DELIVERY | 7 |
| TASL-FIELDS | 1 |
| TRANS-UNANCHORED | 379 |
| TRANSLATION-ANCHORED | 116 |
| WS-ONLY | 1 |

Labels are sets, so the column sums past 538: the head block (B1) alone carries CREDIT-PREVIEW, IFTAGS, TASL-FIELDS, and TRANS-UNANCHORED spans, and most CSS comment translations carry COMMENT-TEXT and TRANS-UNANCHORED together. The sections below are written from the label spans, not from the primary labels. One derived presence stands outside the block labels: HTTP-KEPT ×5, adjudicated in section 11.

## Standing sections

### 0. Header and provenance frame

- **What:** The tag gate is renamed in place: original L1 `[[iftags +版式]]` → candidate L1 `[[iftags +テーマ]]` (B1, IFTAGS span). The candidate inserts its credit block immediately inside the gate (candidate L3–15, section 1) where the original opened its first code block directly (original L2–3); the collapsible label over the first code block is translated (original L2 → candidate L16). No frame is added at the head: delivery framing sits at the tail, as in the original (section 3).
- **Why:** The gate rename is the population's JP tag form; a gate left naming the CN tag would keep the theme page out of the JP theme listing. The credit block's placement inside the gate keeps the attribution attached to the gated page body, the position the population's preview form requires.
- **Verify:** Read candidate L1–17 against original L1–4; the gate strings and the insertion point are the whole change.
- **Disposition:** PASS (go-sign re-run).

### 1. Credit and attribution

- **What:** The candidate's head credit block (candidate L4–13, B1: CREDIT-PREVIEW + TASL-FIELDS spans) is the JP preview pair carrying eight fields: タイトル 雑誌テーマ， 翻訳責任者 AI, 翻訳年 2026, 原題 杂志 主题， 著作権者 Etinjat, 作成年 2021, 初訳時参照リビジョン 488, and the source link to the CN original. The original has no credit block at its head; its attribution is the code banner (original L7 "by Etinjat", with the tab code credited to MalyceGraves and the semimonth code to hoah2333 at original L9–10), which the candidate carries translated at the head of its first code block. In the documentation body, the original's CN credit pairs (credit:start / credit:end at original L6309–6347, including the standalone forms credit:start-standalone / credit:more-standalone) become JP preview pairs (seven CREDIT-PREVIEW blocks: B1 at the head; B259, B260, B261, B263, B265, B266 among the body exhibits at candidate L6294–6338, one of them the @@-escaped exhibit form, ESCAPED-INCLUDE span in B260). The attribution prose (candidate L6169, section 7) names the same four people the original names (original L6184): Etinjat as designer, MalyceGraves for the newspaper theme it derives from, hoah2333 for the semimonth code, Kcorena for the sidebar logo. No license-box include stands on either side.
- **Why:** The author-field check passes on evidence, not on the field alone: 著作権者 Etinjat is the author the original's banner names, and the secondary credits survive both in the translated banner and in the attribution prose, so no attribution line was dropped or replaced by a pointer. The body exhibits keep the original's specimen structure with the JP preview module substituted for the CN credit module, which is the population's exhibit form.
- **Verify:** Read candidate L4–13 and the banner at the head of candidate's first code block against original L5–10; read candidate L6169 against original L6184 for the four names; census `credit:` includes on both sides.
- **Disposition:** PASS (go-sign re-run). The T4/T5 row's credit-notation details (LOCALIZE-ROWS row 202) were recorded as nits with no separate ledger item; the FIX-CREDIT-D wave (1869877) normalized the translator attribution across the population, this file included.

### 2. Includes and components

- **What:** INCLUDE-REPOINT fires in 7 blocks and COMPONENT-SWAP in 2 (B234 at candidate L6175, B367 at candidate L7160): the documentation's component references are repointed from their CN forms to the JP population's forms, and the credit includes of section 1 are the same repoint at the include level. The one include that constitutes delivery, the interwiki-style frame at the tail, is treated in section 3. The theme imports one external component stylesheet, the author's collapsible sidebar, which is not an include and is dispositioned in section 11. No include is duplicated: each include line in the candidate occurs once (the duplication this file did carry was in its @imports, section 3).
- **Why:** A component reference left naming its CN form resolves on the JP wiki to nothing, or to an unrelated page; the repoint is what makes the documentation's worked references real. The escaped exhibit (B260) keeps its @@ escaping so the exhibit shows the include text instead of executing it.
- **Verify:** Census `[[include` lines on both sides and pair them; check the escaped exhibit at candidate L6307–6309 still carries its @@ markers.
- **Disposition:** PASS (go-sign re-run).

### 3. Delivery and code loading

- **What:** The stylesheet is split across five `[[code type="CSS"]]` blocks on both sides, and the candidate's delivery census names every one of them: block /1 (candidate L17–4823), /2 (L4831–4886), /3 (L4893–4959), /4 (L4965–5139), /5 (L5145–6051). The live module after the documentation head (candidate L6056–6154) @imports /5 (B230, candidate L6058); the tail @imports /1 (B521, candidate L7885), /3 (B526, candidate L7988), and /4 (B529, candidate L8011); and the frame, `[[include component:interwiki-style |priority=1 |theme=…/2]]` in its hidden div (candidate L7972–7976, B524), names /2 — the interwiki stylesheet part, whose CSS stands at candidate L4844–4886. Every named block is a stylesheet part; no reference names a small exhibit while a stylesheet block sits unreferenced. The original's topology is the same shape on CN hosts (live module importing code/5, tail imports of code/1, /3, /4, frame naming /2), with one difference the port removes: the original duplicates three imports (code/3 twice, at original L7954 and L7963; code/5 in both the live module and the tail; the Huiwen-Mincho stylesheet twice, at original L7997 and L8048), and FIX4-MECH (commit a497307, KB-65) deduplicated them — the candidate's @import census has no duplicates. The tail's variant modules keep their include-parameter gates on both sides: the ifexpr gates on {$collapsible-sidebar} (imports /3), {$yxh} (imports /4), {$tradition}, and {$wanderers} stand in the candidate at L7985+, L8004+, L8020+, and L8055+ with their contents inside the gates, neither inlined unconditionally nor dropped; the usage example applies the theme with its parameter form (`[[include theme:magazine-jp extensions=true]]`, in the documentation at candidate L7155–7160). The Stage 2 rework (c839ec3) externalized the one external CSS file the first integration had inlined, restoring the import-based delivery this census describes.
- **Why:** This is the population's self-delivery discipline: a local--code address must name the block that actually holds the CSS, and a gated variant must stay gated, because an ungated variant module would apply its edition's furniture to every consumer. The deduplication matters mechanically: a duplicated @import is a duplicated cascade layer, and KB-65 records the population-wide removal.
- **Verify:** Census `[[code` blocks and `@import` lines on both sides; confirm each of /1–/5 is named exactly once in the candidate's delivery references and that the ifexpr gates wrap the variant modules; `sort | uniq -d` over the candidate's @import URLs returns empty.
- **Disposition:** PASS (go-sign re-run).

### 4. Fonts and assets

- **What:** The candidate replaces the original's font machinery wholesale (JPFONT-LOAD in B4 and B534). The original loads its display faces by @font-face subsets from the author's jsdelivr repository (Huiwen-mincho and HanWang WeiBeiMedium, original L16–41) and by two tail stylesheet imports (whz.css and Huiwen-Mincho.css, the latter duplicated). The candidate drops all of those and loads one combined Google Fonts import at the head of block /1 (candidate L29): Noto Serif JP and Zen Old Mincho added as the JP faces, Noto Sans SC, Noto Serif SC, Zhi Mang Xing, and Oxygen Mono kept, because the theme's magazine design uses the CN calligraphy faces as design elements rather than as language defaults. Stacks are rewritten to match: the teletype and account stacks name Zen Old Mincho (candidate L65, L72), the title and poem stacks name Zen Old Mincho with Noto Serif SC fallback (candidate L4999, L5009; CSS-BODY spans B200, B201, narrated here as the P7 font-stack rewrites they are), and the punctuation stacks are rewritten onto var(--page-tt-font). The two dropped tail imports are not silent: porter comments at candidate L8012 and L8058 state that Zen Old Mincho and Noto Serif JP are the JP defaults and the Weibei / full-face imports are therefore unnecessary, and a translator's note in the documentation (candidate L6210, section 10) explains that the original's $Huiwen-mincho / $Weibei subset options were deleted because Noto Serif JP carries the full glyph set. One stack escaped the rewrite: **flag** — candidate L5028, `.yxh-maxim { font-family: 'Huiwen-Mincho'; }`, a bare stack with no fallback, names the dropped face, and the candidate loads that face nowhere (its @font-face census is 0); the original both loaded it (original L16–25) and used the same rule (original L5043). The maxim exhibit therefore renders in the browser's default serif instead of Huiwen-Mincho. The defect is recorded here and in the batch report; the candidate is not edited. Assets: the base64 image stylesheet the original imported from the EN wiki's files (original L5165, scp-wiki.wikidot.com/local--files/theme:magazine/IMG-source_base64.css) is repointed to the candidate's own draft-host attachment (candidate L5150, B206), and the 24 DRAFT-HOST blocks are the same repoint across the theme's image URLs.
- **Why:** P7 font-stack rewrites exist so no rendered string depends on a face the delivery never loads; the flag is exactly that failure in miniature, left over where a component rule sat outside the stacks the rewrite pass enumerated. The asset repoint is the class (iii) recorded delivery: the theme's own images ride on its own page's attachments, not on another wiki's.
- **Verify:** Census `@font-face` and `@import` lines on both sides; grep the candidate for each face its stacks name and confirm a load for each — the check fails only at candidate L5028, which is the flag.
- **Disposition:** PASS (go-sign re-run) with the flag recorded; the flag is this package's own finding, not a ledger item.

### 5. Header, sidebar, and site furniture

- **What:** HEADERVAR fires once (B7, candidate L48–50), in the head variables of block /1. The theme sets no --header-title / --header-subtitle overrides in its main body on either side; the header strings that do exist sit inside the gated variant modules at the tail, and they are the variants' own: the Traditional Chinese edition module (candidate L8020+) sets its header title and subtitle in Traditional Chinese (SCP基金會 / 控制、收容、保護） because that module is, by construction, a Chinese-language edition of the theme, and the Wanderers' Library module sets its own titles in Chinese as the original does. These strings are carried original content of optional variants, not untranslated residue of the JP port; the residue item 65 was charged and closed on the main documentation (per-theme record). The interwiki sidebar CSS is block /2's whole content (candidate L4844–4886), delivered through the frame (section 3), and the collapsible-sidebar variant is gated on its include parameter (section 3).
- **Why:** Header and title language is out of scope for migration correctness under ruling 2 in any case; for the variant modules the stronger ground is that their strings are the artifact a consumer of that variant is asking for. What migration correctness does require is that the furniture mechanisms (frame, interwiki part, sidebar gate) survive, and they do.
- **Verify:** Read candidate L48–50 against its original counterpart; read the tail variant modules (candidate L8004–8096) and confirm each header string sits inside its ifexpr gate.
- **Disposition:** PASS (go-sign re-run); ruling 2 recorded for the header-language aspect.

### 6. Text translation

- **What:** The translation mass is this package's bulk: COMMENT-TEXT in 219 blocks (the stylesheet's section comments, translated in place throughout the five code blocks), TRANS-UNANCHORED in 379 blocks and TRANSLATION-ANCHORED in 116 (documentation prose, exhibit text, and the sample articles, including the semimonth sample essays in the tail documentation), GLYPH-FORM in 48 blocks (simplified-to-Japanese glyph normalization riding inside those translations), and CONTENT-STRING in 4. The FIX5 residue loci sit inside this mass and are re-derived in the per-theme record (blocks B361, B366, B380, B382). This package's own corroborating scan: a grep of the candidate for the distinctive simplified-only forms （页， 代码， 图片地址， 们， 这） returns no reader-visible hits; the remaining Chinese text in the file is the gated Traditional Chinese variant module of section 5 and the original-language strings the exhibits quote as specimens.
- **Why:** The comments and documentation are part of the deliverable a JP porter-user reads; leaving them in Chinese would leave the theme's own manual unreadable to its audience, which is what T4/T5 measure. The glyph forms matter beyond readability: a simplified glyph in a rendered string is a wrong character to a JP reader, which is why item 65 was display-affecting.
- **Verify:** The per-theme record's three loci, plus the scan described above re-run against candidate.txt; the appendix resolves the heuristic mass by shape.
- **Disposition:** PASS (go-sign re-run); item 65 [H] FIXED (supplement), re-derived below.

### 7. Links

- **What:** LINK-REPOINT fires in 3 blocks (B410 at candidate L7402, B432 at L7483, B454 at L7557), the documentation's cross-references repointed to their JP or canonical forms. One line needs its own paragraph: the attribution prose at candidate L6169 (B232) converts the original's three bare links (original L6184: theme:newspaper, fragment:semimonth-magazine, semimonth-202110-01, all resolving on the CN wiki) into absolute EN-host URLs. **Flag:** two of the three targets do not exist on the EN host — probed 2026-11-17, https://scp-wiki.wikidot.com/fragment:semimonth-magazine and https://scp-wiki.wikidot.com/semimonth-202110-01 both return 404 — while the CN targets the original's links resolved to do exist: scp-wiki-cn.wikidot.com/theme:newspaper and scp-wiki-cn.wikidot.com/fragment:semimonth-magazine both serve (the fragment page itself links semimonth-202110-01 on the CN host). The third link, theme:newspaper on EN, names MalyceGraves' original theme and is a defensible target; the two semimonth links are not, because the semimonth magazine is a CN-branch artifact with no EN page. The candidate is not edited; the flag is recorded here and in the batch report with the probe evidence.
- **Why:** T4 charged this line at ledger time as a wrong-host link (pattern 11, LOCALIZE-ROWS row 202), and the ledger dispositioned the theme's sibling links as a class (P11). The disposition records the class judgment; it does not make the two dead links resolve. Under the campaign's dead-reference standard, a link whose probed target 404s while the original's target serves is a defect in the bytes as they stand, whoever dispositioned the class.
- **Verify:** Fetch the two EN URLs and the two CN URLs above (one fetch each); read candidate L6169 against original L6184.
- **Disposition:** PASS (go-sign re-run) with the flag recorded; P11 disposition noted, the flag standing on the probe evidence.

### 8. Structure

- **What:** The five-block stylesheet split, the live module's position, the documentation's exhibit order, and the tail's gated variant sequence are all carried in the original's order; nothing is relocated between regions. A brace-depth scan over both files (not a count: depth tracked line by line) ends at depth 0 on both sides with maximum depth 3 and no negative excursion, so no displaced brace swallows a rule range in either file. EXHIBIT-RESTRUCTURE fires once (B523, candidate L7972) and is adjudicated a false fire in the appendix: the block is the delivery frame's include line, whose theme= parameter changed host, not an exhibit.
- **Why:** In an 8,000-line stylesheet a single displaced closing brace silently disables every rule after it while keeping naive brace counts equal; the depth scan is the cheapest check that decides the question.
- **Verify:** Re-run a depth scan over original.txt and candidate.txt; compare the block census of section 3 on both sides.
- **Disposition:** PASS (go-sign re-run).

### 9. Formatting only

- **What:** WS-ONLY fires once (B195, candidate L4902, the blank line after the collapsible-sidebar import). No other formatting-only change is claimed: at this diff size, whitespace riding inside translated lines is counted with its line, not separated.
- **Why:** Recorded so the reader does not hunt for a semantic change in a block that has none.
- **Verify:** Read candidate L4900–4903 against the original's counterpart lines.
- **Disposition:** PASS (go-sign re-run).

### 10. Porter annotations

- **What:** Not none. ANNOTATION fires in 2 blocks: B194 (candidate L4900), the bracket comment over the collapsible-sidebar import stating that the sidebar CSS is loaded by @import from the author's component, as in the original; and B239 (candidate L6210–6211), the translator's note （訳注） in the font documentation stating that the original's $Huiwen-mincho / $Weibei subset options were deleted in the JP edition because Noto Serif JP carries the full glyph set. Two further porter comments ride inside other blocks and are recorded here per the standing check: the comments at candidate L8012 and L8058 (inside B529 and B534) explaining the two dropped tail font imports, and the exhibit note at candidate L6372–6373 recording that the typewriter exhibit's original face was the Wang Hansong Weibei face and Zen Old Mincho substitutes for it. The head credit block's 翻訳責任者 field (section 1) is the TASL attribution, not an annotation.
- **Why:** Porter annotations are the port's own voice inside the deliverable; the record names them so a reader can separate the porter's explanations from the original's text, and so the deletions they justify (the font options, the tail imports) are auditable at the locus they describe.
- **Verify:** Read the five loci; each is a comment or note, none alters a rule or a string the page renders as the theme's own.
- **Disposition:** PASS (go-sign re-run).

### 11. Dispositions and exceptions

- **What:** Three standing dispositions and one derived presence. (1) P4: the @import at candidate L4901, `https://etinjat.wikidot.com/component:collapsible-sidebar/code/1`, stands verbatim from the original (original L4916): it is the theme author's own component stylesheet, credited in the porter comment above it (Etinjat, CC BY-SA 3.0), and the ledger dispositioned it as original-state delivery, class (ii) — the T4 row's pattern-4 charge (a non-exception host @import inside the documentation source, with indirect display effect) is answered by that disposition, and the bytes match it: the import is the theme's functional sidebar dependency, not a stray hotlink. (2) P11: the sibling-link class disposition, recorded in section 7 together with the flag the probe evidence raises against two of its instances. (3) The render row's dispositions (RENDER-ROWS-2, RENDER-S2-F (CN9)): the page-overflow measurements (1415px@1366, 448px@320, 525px@375, 911–996px@768) and the runtime-hotlink site-theme chain are dispositioned at the environment layer (KB-40), and the sample's T2 run produced no machine verdict (exit 2, no summary), which the stamp carries as a coverage caveat rather than a pass. (4) HTTP-KEPT derived presence ×5 (candidate L4311, L4317, L5102, L5103, L8045): all five are `#footer a[href="http://www.wikidot.com"]` attribute-selector literals and their kin — selector strings that match the site's own footer links, not resource loads; no fetch occurs, and they stand as the original's selectors.
- **Why:** A disposition is a judgment recorded against a named class; this section exists so the reader can see which charges against this theme were answered by judgment rather than by a change to the bytes, and can re-open exactly those if the class judgment is ever revisited.
- **Verify:** Read candidate L4900–4901 against original L4916; grep the candidate for `wikidot.com"]` selectors to see the HTTP-KEPT instances in place.
- **Disposition:** DISPOSITIONED (ledger §(c2)/(c3) as cited); the section 7 flag stands alongside the P11 disposition.

### 12. Verification

- **What:** The checks this package rests on, all re-runnable from this repo alone except the two probes section 7 cites: original.txt SHA-256 equals the sources.tsv value (eaa1e692…); candidate.txt is byte-identical to canonical pages/theme:magazine-jp.txt at the worktree HEAD (782b9363…); the delivery census and @import duplication census of section 3; the brace-depth scan of section 8; the font-load census of section 4 (which produced the flag); the residue scan of section 6 and the per-theme record; `python3 review/build_review.py --check` passes for the package. The K5a-i supersession (Provenance) is recorded, not absorbed: upstream has moved past revision 488, and the follow-up artifact diff-magazine-from488.txt is where that movement is tracked.
- **Why:** The package's claim is that a reader can re-derive every verdict in it from the two files and the vendored authorities; this section lists the derivations.
- **Verify:** Run the commands named above.
- **Disposition:** PASS (go-sign re-run).

## Per-theme record

### Ledger item 65 [H] — the untranslated residue, re-derived

The T4/T5 row (LOCALIZE-ROWS row 202, LOCALIZE-S2-D) charged reader-visible untranslated residue at three loci — candidate-side L7121, L7158, and L7268/L7272 at measurement time (pattern 10) — three display-affecting findings, mechanically fixable, with no display-breaking defect. The supplement re-judged the item FIXED by FIX5-TEXTA §2, commit 6f6b349, and the commit's diff for this file is exactly three hunks, one per locus:

1. **L7121** — inside an already-Japanese notebook-style note, the mixed string 書页の色 (simplified 页 in a Japanese sentence) becomes ノートページの色. Current bytes: the hunk's block is B361 (candidate L7119–7125), and the translated form stands there.
2. **L7158** — the exhibit heading `++* 代码` ("code") becomes `++* コード`. Current bytes: B366 (candidate L7158).
3. **L7268 and L7272** — the style-attribute exhibit placeholders `url(图片地址)` ("image URL") become `url(画像URL)` at both occurrences. Current bytes: B380 and B382 (candidate L7268, L7272), both carrying GLYPH-FORM spans.

The supplement also reports that the lane's source-wide grep found no further reader-visible CN residue. This package does not take that on trust: the scan of section 6 (distinctive simplified-only forms over the whole candidate) returns no reader-visible hits, and the Chinese text that remains in the file is accounted for — the gated Traditional Chinese variant module (section 5) and quoted specimen strings. One scope note belongs in the record: the FIX5 commit is the candidate's last change (the file's git history runs bbd273c → c839ec3 → 1869877 → a497307 → 6f6b349), so unlike a repaired-after-verdict theme, this package's stamp reads PASS against the very bytes the supplement judged, and the re-derivation above is a check of the fix, not of a drifted file. The fix is present and complete.

### Post-package repairs (REFRESH3-H)

The items above describe this package as built. The repair recorded below postdates the package; `candidate.txt` has been recopied from the current canonical `pages/theme:magazine-jp.txt` and `diff.md` and the verdict stamp regenerated with `python3 review/build_review.py`, so this package now documents the post-repair candidate. The regenerated stamp reads **STALE** by design: no re-judgement is fabricated here, and the frozen ledger (`GOSIGN2-LEDGER.md` + supplement, FIX5 head 435a6bb) remains the verdict record.

**FIX-RFIX6 items 2–3 — attribution links and the maxim face (landing `f5acc90cbb800f3c0752713589322929dac75821`, "pages: king-s-palace exhibit slug, magazine attribution links and maxim face", 2026-11-17; record `FIX-RFIX6.md`).** +17/−1. Item 2: the two dead EN-host attribution links on L6185 are repointed to their CN originals (re-probed 200) — `[*https://scp-wiki-cn.wikidot.com/fragment:semimonth-magazine 半月刊専用部分]` and `[*https://scp-wiki-cn.wikidot.com/semimonth-202110-01 効果はこちら]`; the third link (EN theme:newspaper) is untouched because the prose credits MalyceGraves' original theme. Item 3: the original's two `'Huiwen-mincho'` `@font-face` blocks are restored at new L31–46 immediately after the Google Fonts @import — the `.yxh-maxim` rule (new L5044) names 'Huiwen-Mincho' but the face was loaded nowhere in the candidate; the URLs are trimmed of the original's trailing space inside `url()` (spaced form 404, trimmed form 200 `font/woff2`, SCP-BASE 7,456 B / SCP-ADD 14,036 B). The two sibling Weibei blocks are deliberately NOT restored (no surviving rule names that face). Checker 29/1/3 → 31/1/3: the two new errors are class (ii) hotlinks on the restored fastly.jsdelivr.net URLs; class (i) 0.

## Change set outside the two diffed files

(1) `pages/theme-decoration-sample-magazine-jp.txt` — the decoration sample page the render checks ran against. The theme is standalone (start-themes.tsv row 204: no base, no component dependencies beyond the dispositioned author component of section 11), so the change set is the candidate and its sample, nothing else.

## Appendix — heuristic adjudication

The classifier left 338 heuristic blocks (tier C) and 8 residue blocks (tier None). They resolve by shape, not one by one. The heuristic mass is two shapes: CSS comment translations (the COMMENT-TEXT primaries, one-line section comments inside the five code blocks, each verified against its original line as a one-to-one translation) and unanchored prose translations (the TRANS-UNANCHORED primaries in the documentation body and sample articles, same verification). Where a heuristic block carries substance beyond translation, its section records it: B4 (the head font import, section 4), B194 and B239 (the porter annotations, section 10), B232 (the attribution line, section 7), B523 (below), B527 and B537 (the original-side-only lines of the two dropped tail font imports, section 4), and B534 (the Noto Serif JP porter comment, sections 4 and 10). The 8 residue blocks (B245 at candidate L6239, B309 at L6688, B437 at L7508, B492 at L7766–7769, B501 at L7789–7798, B510 at L7819–7820, B513 at L7842, B515 at L7845–7848) all sit in the tail documentation's sample-text region, where whole paragraphs of the semimonth sample articles were replaced and no signature fired; inspected by range, they are the same prose-translation shape as the tier C mass and carry no structural change. B523's EXHIBIT-RESTRUCTURE label is a false fire: the block is the delivery frame's include line (candidate L7972), whose theme= parameter changed host with the rest of the delivery repoint (section 3); the exhibit census is unchanged there. The HTTP-KEPT derived presence is adjudicated in section 11 (selector literals, not loads). No heuristic or residue block required a new signature, and none conceals a dropped module: the multi-block census of section 3 accounts for all five code blocks and all four gated variant modules on both sides.
