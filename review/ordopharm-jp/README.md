# Review package — theme:ordopharm-jp (EN → JP port)
New to this package's shorthand? Read the notation key first: [How to read a review package](../HOW-TO-READ.md).

<!-- BEGIN GENERATED VERDICT STAMP — do not hand-edit; regenerate with review/build_review.py -->
## Verdict stamp
- Theme: theme:ordopharm-jp — origin EN, population #117 [GOSIGN2-LEDGER (b) row 117]
- Overall: STALE — candidate file changed since the verdict was computed (verdict against 435a6bb-era content, file sha256 now 39848689f953bab38ee93dbf8f4e620d4b2abe9276dcd04e46d6013544ddefc2); the verdicts below were computed against that pre-change file, and the record verdict stands: a candidate revised through the campaign's recorded repairs is posted like a PASS row, with the change recorded in its package
- T1 (source check): FINDINGS (classified) — baseline 2026-11-16: exit 1, 6 errors / 1 warn / 1 info (pseudo-ref×6); standing classes dispositioned in register c1 [T1-ROWS row 117; GOSIGN2-LEDGER (b) row 117]
- T2/T3 (render, combined verdict): FINDINGS — [combined T2/T3] report `FINDINGS` — page page-overflow 506px@320/375 chromium + 518px@320/375 webkit, runtime-hotlink site-theme chain + candidate-own cdn.jsdelivr.net (judgment-required); sample credit-modal (preview-form), same page-overflow, runtime-hotlink incl. candidate-own cdn.jsdelivr.net + cdn.scpwiki.com (judgment-required); T3 clean on both pages; the original page chromium 1366x768 capture was a transient 503 (http.cat + hidden-* block), re-run once per rule 2 and the fresh capture is a clean real page; sample webkit *-full.png missing (32767px screenshot cap). [RENDER-ROWS-RERUN16 (EN15) — supersedes the RENDER-ROWS-2 row for this theme, rule S1]
- Engine coverage: full (chromium+webkit, both pages) [RENDER-ROWS-RERUN16 (EN15)]
- Credit modal: sample credit-modal errors dispositioned preview-form (credit:start-preview has no modal mechanism; GOSIGN-TESTS T2 amendment, 2026-11-16) [RENDER-ROWS-RERUN16 row]
- T4 (localize patterns + follow-up): FINDINGS — display-affecting findings: 3 [LOCALIZE-ROWS row 117, source LOCALIZE-S2-B]
- T5 (translation text): FINDINGS — the source reports judge T4/T5 jointly; one verdict word covers both [LOCALIZE-ROWS row 117]
- FIX5 re-judgement: none — no OPEN items at the ledger determination [GOSIGN2-LEDGER (b) row 117]
- Computed against: canonical commit ecc8c172a02a5c41aec3300b1b99953bdf727f82; candidate file pages/theme:ordopharm-jp.txt sha256:39848689f953bab38ee93dbf8f4e620d4b2abe9276dcd04e46d6013544ddefc2; record: GOSIGN2-LEDGER.md + GOSIGN2-LEDGER-SUPPLEMENT.md as of the FIX5 head 435a6bb
<!-- END GENERATED VERDICT STAMP -->

## Status

| | |
|---|---|
| Verdict | **PASS** — passed at the ledger determination; this theme had no OPEN items and no §(e) register entry (GOSIGN2-LEDGER (b) row 117). Its render verdict rests on the RERUN16 re-run, which supersedes the original ROWS-2 row under rule S1 |
| Standing items | **DISPOSITIONED** — the EN CDN delivery (P4, "delivery class (ii): original-state CDN delivery") and the English header tagline (P9, ruling 2: header/title language out of scope), both at GOSIGN2-LEDGER §(c3); T1's six pseudo-refs (the draft-host addresses, class (iii)); the RERUN16 render items (section 11). T4's third item (17 display-visible English strings in the demo/usage area) is not in the §(c3) list and reads as closed by the translation state of the current candidate (section 12). **FLAGGED by this package** — the candidate page carries only part 1 of the theme's three code files, with parts 2 and 3 absent from the canonical repo (per-theme record, item 1), and the original's second head module is dropped without a note (item 2). **NOTED** — the holder field's value is named nowhere in the frozen original (item 3) |
| Go-sign basis | COMPLETION-REPORT.md §10 (go-sign issued; 81 FIXED / 26 DISPOSITIONED / 0 OPEN across the sweep) |
| Named exception | None for this theme (the sweep's single named exception is theme:amethyst-v2, which has no candidate) |

## Provenance

| | Original | Candidate |
|---|---|---|
| Page | theme:ordopharm | theme:ordopharm-jp |
| Wiki | scp-wiki.wikidot.com | SCP-JP Sigma-10 candidate (canonical repo) |
| Reference revision | 22 (first translation; the candidate's credit block records 初訳時参照リビジョン: 22) | — |
| Source of this copy | Campaign cache `gosign2-lanes/lane-oc-gs-localize-s2-B/orig-ordopharm.txt`, via the mirror store (class COPY, hash-verified against review/sources.tsv) | Canonical file `pages/theme:ordopharm-jp.txt`, copied at worktree HEAD 4e6b126 |
| Lines / bytes | 3,472 lines / 105,945 bytes | 3,068 lines / 97,367 bytes |
| SHA-256 | c656a4762dffab420d93daa3b2f94a054cb4dddcd35d1708ba4415445a443bc7 | e8bd607e248227c6024262bc363d6546694588aeb905825f74658a91a8410205 |

Provenance route: derived from the original at the reference revision by the LOCALIZE-S2-B wave, in the layered form sources.tsv records as kind K5b-3: the candidate layers over theme:basalt-jp, and this package's diff covers the theme's own layer. The candidate's smaller size is mostly structural, not translational: the original page carries all three of the theme's code files as exhibits, and the candidate page carries the first of them (per-theme record, item 1), and the original's second head module has no counterpart (item 2). Wave history: fde02f3 (EN15 integration), f1138e4 (FIX-P4, the base-import repoint), a497307 (FIX4-MECH, the duplicate-import cleanup; the verdict stamp's computed-against commit). No FIX5 commit touches this file.

## Summary

Billith's Ordopharm Agronomics Theme, a very large Basalt/Bedrock derivative whose page is part theme, part design-system documentation: a Basalt CDN import module, a small page-utilities module, over a thousand lines of translated documentation and specimens, and three code exhibits (base, intranet mode, legacy mode) that are the theme's actual delivery files. The port repoints the base layer to basalt-jp (three frame entries: the basalt-jp code at priorities 1 and 2, the theme's own at priority 3), converts the usage contract to a single include (the code file now imports the base itself, and a translator's note in the body explains the change), moves the fonts from bunny.net to Google Fonts with the JP pair added, and appends a license box whose font entry documents that switch. Two completeness items stand against it, both flagged in the per-theme record: the intranet and legacy code files (parts 2 and 3) have no JP text anywhere in the canonical repo, although the candidate's own delivery documentation still points users at their addresses and its exhibit banner directs a three-part upload at posting; and the original's second head module — the map-coordinate variables and the demo utility classes the candidate's documentation still uses — is absent without a note. Measured churn (diff.md: +366/−770, 1,136 changed lines in 195 change blocks / 20 diff sections) reflects those two absences on top of the documentation translation.

## Class summary

Auto-classification by review/classify_hunks.py (signature table 2026-11-17.1): 195 change blocks — 129 specific (66%), 46 heuristic (24%), 20 residue (10%), 0 skipped. Pattern citations below name the KB entry; the patterns/ tree state cited throughout is commit 9c5e9079afb01d30cb9fc4ef9d714e5591eb2ffa.

| Label | Blocks |
|---|---|
| TRANSLATION-ANCHORED | 109 |
| COMMENT-TEXT | 51 |
| TRANS-UNANCHORED | 50 |
| DRAFT-HOST | 8 |
| DELIVERY-HOST | 7 |
| SELF-DELIVERY | 7 |
| LINK-REPOINT | 6 |
| EXHIBIT-RESTRUCTURE | 6 |
| INCLUDE-REPOINT | 4 |
| IFTAGS | 2 |
| COMPONENT-SWAP | 2 |
| ESCAPED-INCLUDE | 2 |
| HEADERVAR | 2 |
| LICENSE-BOX | 2 |
| CONTENT-STRING | 1 |
| CREDIT-PREVIEW | 1 |
| CREDIT-PROSE | 1 |
| TASL-FIELDS | 1 |
| BARE-RATE-DEL | 1 |
| FONT-IMPORT | 1 |
| JPFONT-LOAD | 1 |
| CSS-BODY | 1 |
| ANNOTATION | 1 |

Adjudication for this README (every specific block was read against the bytes; the heuristic mass was resolved by shape): the 210 translation-family blocks are the documentation and exhibit-comment translation (section 6). The seven DELIVERY-HOST / seven SELF-DELIVERY / eight DRAFT-HOST blocks are the delivery addresses of section 3, met repeatedly because the delivery is documented in three places (head, exhibit head, tail documentation). B187's EXHIBIT-RESTRUCTURE primary spans the original's parts 2 and 3 exhibits (original L3082–3434) against a single candidate line: the differ's alignment for the absence recorded as per-theme item 1, not a restructuring of anything present. B4's span (the candidate's credit block against the original's second-module zone) is the differ's alignment for item 2's absence. The twenty residue blocks collapse into the appendix table below, per the class M convention; every one is a translation line in the documentation that the signature table did not label, except B89 (a case-only change) and B123 (a collapsible alignment).

### Residue appendix (20 blocks)

| Blocks | Shape | Resolution |
|---|---|---|
| B23, B25, B28, B30 | Tab titles in the documentation's tabviews (original L134–161) | Translated (Overview → 概要, Disclosure → 開示); section 6 |
| B36, B43, B92, B107, B125, B149 | `s-title` specimen headings (original L190–962) | Translated (Quotes → 引用, Tables → 表, Metrics → 指標, Updates → 更新履歴, Notice → 注意, Modifiers → 修飾子); section 6 |
| B103, B106, B142, B143, B154 | Specimen and section titles (original L475–1037) | Translated (Contained field trial → 隔離圃場試験, Commercial launch → 商用展開, the herbicide caption, Documents → 文書, Map Modifiers zone); section 6 |
| B70, B72, B73 | Numbered heading specimens (original L323–335) | Numerals translated (One → 一, Three → 三, Four → 四); section 6 |
| B89 | A Lorem ipsum specimen line (original L416) | Case-only change (Lorem → lorem); no semantic content; section 9 |
| B123 | A collapsible boundary (original L586) | Alignment of a `[[/collapsible]]` line under translation; section 9 |

## Standing sections

### 0. Header and provenance frame

- **What:** Theme theme:ordopharm-jp; original theme:ordopharm on scp-wiki at reference revision 22; candidate `pages/theme:ordopharm-jp.txt`. Provenance route: derived at the reference revision by the LOCALIZE-S2-B wave, layered over theme:basalt-jp (kind K5b-3; the Provenance note above). The frame moved: the original opens with its gate and its two head modules (original L1–76); the candidate opens with its delivery module (candidate L1–3), the three interwiki-style frames (candidate L5–16), and then the localized gate (candidate L18).
- **Why:** Section 0 declares the provenance route and the topology baseline; the gate's tag is P2, the frames are P6/T3.
- **Verify:** The sources.tsv row for ordopharm-jp (kind K5b-3 and its layering note); `sha256sum original.txt` against the Provenance table.
- **Disposition:** Standing (the route itself); the delivery changes are recorded in section 3 and the two absences in the per-theme record.

### 1. Credit and attribution

- **What:** The original's credit furniture is a bare `[[module Rate]]` in a centering block after the pseudocrumbs line (original L82–84) and nothing else — no credit module pair, no byline in the text, and no banner in its code exhibits (part 1 opens directly with its font import and palette). The candidate deletes the Rate exhibit and installs the JP form: a `:scp-jp:credit:start-preview`/`end-preview` block directly under the gate (candidate L20–29) carrying the eight ruling-3 fields (title オルドファーム アグロノミクス テーマ; 翻訳責任者 AI; 翻訳年 2026; 原題 Ordopharm Agronomics Theme; 著作権者 [[*user Billith]]; 作成年 2026; 初訳時参照リビジョン 22; the source link, candidate L28, on scp-wiki.wikidot.com, the host sources.tsv records for the original, its label the theme's English title). The holder value is recorded as per-theme item 3: the frozen original names no author anywhere, so the field rests on evidence outside this package. License entries: a `:scp-jp:component:license-box-backend` box is appended after the code exhibit, still inside the gate (candidate L3027–3041), with two entries: banner.jpg (author Billith; the honest form stating the original gives no license, 投稿前に著者へ確認してください; its scp-wiki source URL) and the fonts entry (Archivo / Inter / IBM Plex Mono / Abhaya Libre, SIL Open Font License via Google Fonts, with the translator's note of section 10 recording the delivery switch). T7 credit-module CSS: the theme's own layer carries no credit-rule group (its credit styling arrives with the Basalt base), so no T7 item arises.
- **Why:** P3/T1: the preview credit module is the rate-bearing JP form, so the bare Rate is deleted rather than duplicated (a kept Rate would be the KB-09 duplicate). Ruling 3 fixes the eight fields and the translator credit form.
- **Verify:** `grep -n 'module Rate\|credit:start\|license-box' candidate.txt` returns the preview pair at L20 and L29 and the license pair at L3027 and L3041; read candidate L20–29 against the eight fields.
- **Disposition:** Applied; no credit item is charged in the theme's T4 row.

### 2. Includes and components

- **What:** The candidate's live includes are six: the three interwiki-style frames (candidate L5–16, section 3), the credit pair (section 1), and the license-box pair (section 1). The usage contract is rewritten, and the candidate says why in the text: the original documents a two-include contract (theme:bedrock first, then theme:ordopharm, original L97–98, with the `intranet=a` / `legacy=a` parameter forms at original L100–105 and sandbox demo links); the candidate documents the single `@@[[include :scp-jp:theme:ordopharm-jp]]@@` (candidate L46) with the same parameter forms (candidate L50–53), because the JP code file imports the Basalt base itself (section 3) — a translator's note directly under the example states exactly this (candidate L48, section 10). The sandbox demo links do not survive the rewrite (they demonstrated the EN modes on the author's sandbox; the parameter forms they demonstrated are kept). The delivery documentation at the tail (the `[[div_]]` zone both sides carry, original L3438–3472 → candidate L3044–3068) shows the user-side delivery code for all three parts with JP addresses (section 3). The COMPONENT-SWAP blocks (B9, B11) are the body's component demo includes taking their JP forms in the documentation zone.
- **Why:** P1/T2: a self-reference names the page that will exist, and the usage contract is rewritten to match the delivery the candidate actually has, with the reason stated in the file — the honest form of the example. The parameter forms keep their meaning only if parts 2 and 3 exist at posting, which is per-theme item 1.
- **Verify:** `grep -n '\[\[include' candidate.txt` — the frames, the credit and license pairs, and the tail documentation's module/frame lines.
- **Disposition:** Applied; the parameter forms' dependence on item 1 is recorded there.

### 3. Delivery and code loading

- **What:** The original's delivery has three layers. (a) The base: a head module imports Basalt's normalize and bedrock CSS from the EN CDN (original L3–4: `cdn.scpwiki.com/theme/en/basalt/normalize-min.css` and `basalt-bedrock-min.css`). (b) The theme's own CSS: three `[[code type="css"]]` exhibits on the theme page itself — part 1, base (original L1212–3052, 1,841 lines), part 2, intranet mode (original L3054–3247), part 3, legacy mode (original L3248–3433) — served to user pages as the page's local--code /1, /2, /3. (c) The documented user-side form (the tail `[[div_]]` zone): a module import plus interwiki frames at priorities 3 (base), 4 (intranet), and 5 (legacy), naming the exhibits on scp-wiki.wdfiles.com, the mode layers gated by the include parameters. The candidate converts (a) and the form of (c), and carries (b) in part. Its head module imports its own exhibit from the draft host (candidate L2), and its three frames name the basalt-jp candidate's first code block at priorities 1 and 2 (candidate L7, L11 — basalt-jp's own delivery serves both the normalize and bedrock layers from that block, per its package) and its own exhibit at priority 3 (candidate L15). Part 1's exhibit opens with a porter banner and imports basalt-jp/1 itself (candidate L1170–1177), which is what makes the single-include contract of section 2 work. The tail documentation is repointed line for line to the draft host (candidate L3044–3068: /1 at priority 3, /2 at priority 4, /3 at priority 5). What the candidate does not carry is parts 2 and 3 themselves: no JP text of either exists in the canonical repo, so as committed, the documented /2 and /3 addresses resolve to nothing on the candidate page (its only code block is part 1). That absence is per-theme item 1, flagged with its evidence; the exhibit banner's direction (a three-part upload at posting, citing the producing lane's INTEGRATION.md §2) is recorded there as the port's stated mechanism. T4's delivery item, (a) "P4 EN CDN interwiki theme= ×2 (display-affecting)" (LOCALIZE-ROWS row 117), charges the original's CDN form of layer (a); the ledger dispositions it as delivery class (ii) (§(c3)), and the candidate's current form repoints that layer to basalt-jp in any case.
- **Why:** P4/T9 (own-code and base delivery re-hosted to JP addresses, class (iii) mechanics) and P6/T3 (the interwiki-style frames). The parts absence is not narrated as a supplement or a restructuring: it is a completeness flag, stated in the per-theme record with both sides' line ranges.
- **Verify:** `grep -n 'local--code' candidate.txt` — the head import, the three frames, the exhibit's basalt import, and the tail documentation's six lines; `grep -c 'code type="css"' candidate.txt original.txt` returns 1 and 3.
- **Disposition:** DISPOSITIONED (the P4 item, delivery class (ii), GOSIGN2-LEDGER §(c3)); parts 2 and 3 flagged in the per-theme record, item 1.

### 4. Fonts and assets

- **What:** Loads: part 1's exhibit in the original loads Archivo and IBM Plex Mono from fonts.bunny.net (original L1213) and takes Inter in its variable form from a source the original does not state; part 3 additionally loaded Abhaya Libre from bunny.net (original L3251, inside the absent part 3). The candidate's part 1 loads Archivo and IBM Plex Mono from Google Fonts, Inter from Google Fonts, and the JP pair (Noto Sans JP, Noto Serif JP) under a Japanese localization comment (candidate L1179–1185). The license box's font entry documents the switch with a translator's note (candidate L3036: the original took Archivo and IBM Plex Mono / Abhaya Libre from bunny.net and left InterVariable's source unstated; the JP version loads from Google Fonts and adds the Noto pair). Stacks: the theme's stacks name the loaded faces first (Archivo, Inter, IBM Plex Mono), so no KB-16 gap arises in the carried layer; Abhaya Libre's stack lives in part 3 and stands or falls with item 1. Assets: the theme's banner image (banner.jpg, on scp-wiki.wikidot.com's file area) is the license box's first entry; in the original it was also the value of the `--map-image` variable defined in the dropped second module (original L15), while the candidate's exhibit only uses the variable with a `none` fallback (candidate L1851) — that half of the asset story is per-theme item 2. The render row's candidate-own jsdelivr and cdn.scpwiki.com hosts are chain hosts, recorded in section 11 as judgment-required.
- **Why:** P7 (the JP faces added in load; the delivery host for the Latin faces moved to the allowed Google Fonts, KB-17) and P5 (the banner's attribution record completed in the license box).
- **Verify:** `grep -n '@import' candidate.txt` — the head import, the exhibit's four font lines at L1179–1185, and the tail documentation's imports.
- **Disposition:** Applied for the carried layer; the part-3 font load stands with item 1.

### 5. Header, sidebar, and site furniture

- **What:** T4's item (b) is this section's: "P9 `--header-tagline` English (display-affecting)" (LOCALIZE-ROWS row 117) — the theme's header tagline variable keeps its English default in the candidate. Its standing is the ledger's: "P9 DISPOSITIONED (ruling 2: header/title language out of scope)" (§(c3)), and campaign AGENTS.md §6 lists pattern-9 header language among the standard dispositions that are never fix targets (the owner's ruling that header title and tagline language is translation taste, case by case). The HEADERVAR blocks are the palettes' header-variable definitions inside the exhibits. No `--header-title` override is set by the theme on either side; the sidebar furniture arrives with the Basalt base. The render row's layout item is the 506px overflow, recorded in section 11.
- **Why:** P9's disposition is a ruling, recorded here with its ground rather than relitigated; the section exists so a reviewer finds the tagline's standing in one place.
- **Verify:** The §(c3) line for this theme in GOSIGN2-LEDGER.md; `grep -n 'header-tagline' candidate.txt` for the variable itself.
- **Disposition:** DISPOSITIONED (ruling 2, GOSIGN2-LEDGER §(c3)).

### 6. Text translation

- **What:** The documentation body (the design-system specimens between the credit zone and the code exhibit) is translated throughout: the pseudocrumbs line (candidate L32, keeping its Bedrock/Basalt/Eigenmachine/Eigenvector references as labeled EN links with an "いずれも英語版" note), the welcome and hub prose, the font and color specimens, the tabviews, and the specimen articles, in the original's order; the exhibit's section comments are translated with them (COMMENT-TEXT, 51 blocks). The translation mass (TRANSLATION-ANCHORED 109, TRANS-UNANCHORED 50) is resolved here in aggregate per the class M convention, and the residue appendix resolves the twenty unlabeled translation lines individually by shape. T4's item (c) charged 17 display-visible English strings in the demo/usage area; the current candidate's demo/usage area is translated at the points the row listed (spot-verified at the tab titles and specimen headings of the residue appendix), and the item does not appear in the §(c3) disposition list, so it reads as closed by the waves' translation edits, the last of them the stamp's computed-against commit (FIX4-MECH). In-CSS text (R1): part 1's comments are translated; the exhibit's porter banner is the port's own addition (section 10).
- **Why:** P10 (body, usage, and sample translation) and KB-18 (reader-visible strings, including the demo area's).
- **Verify:** The body sections of diff.md in order; the residue appendix's lines against both files.
- **Disposition:** Standing (the port itself); item (c) closed by edit as recorded in section 12.

### 7. Links

- **What:** Six LINK-REPOINT blocks: the pseudocrumbs references (candidate L32) keep their EN targets as labeled links with the branch note, because Bedrock, Basalt, Eigenmachine, and Eigenvector are referenced as the theme's lineage, and Basalt's JP candidate is a delivery dependence (section 3), not the prose's subject; the documentation's remaining branch links take the same labeled form, and the credit source link (candidate L28) names scp-wiki.wikidot.com, the recorded host, and serves the original. The original's sandbox demo links in the usage examples are the one deletion in this section, recorded in section 2 with the contract rewrite that removed their context.
- **Why:** P11: a prose link takes the JP counterpart where the link's subject is the counterpart; lineage references name the works they mean.
- **Verify:** `grep -n 'scp-wiki.wikidot.com' candidate.txt` — the pseudocrumbs line, the source link, and the license citation.
- **Disposition:** Standing.

### 8. Structure

- **What:** The declared deviations are the delivery items of section 3 (the frame set's addition, the exhibit's basalt import, the single-include contract) and the two absences of the per-theme record (parts 2 and 3; the second head module), which are flagged there rather than absorbed here. Within the carried layer, everything corresponds: part 1's exhibit stands at its original length within the banner's growth (1,841 → 1,855 lines), its palettes and rule order preserved (the candidate's `--ordo-azure: 8, 121, 190` at L1196 is part 1's own value, not part 2's, which is how the differ's B187 alignment is adjudicated), the documentation census corresponds one to one in the same order, and the tail delivery documentation corresponds line for line. The six EXHIBIT-RESTRUCTURE primaries outside B187 are that documentation zone's repoints and the license zone's reassembly.
- **Why:** R3's distinction (sanctioned replacement vs silent deletion) is decided by the census; the two absences fail the census openly and are therefore flags, not narrative.
- **Verify:** Compare `grep -n '\[\[code\|\[\[module\|\[\[collapsible' original.txt candidate.txt`.
- **Disposition:** Standing for the carried layer; the absences flagged in the per-theme record.

### 9. Formatting only

- **What:** Two formatting-level residue items: B89 (a Lorem ipsum specimen line whose only change is the capitalization of its first word) and B123 (a `[[/collapsible]]` boundary alignment). No WS-ONLY label fired and the classifier finds 0 re-indentation blocks, so there is no other formatting churn to disclose; the file's large negative line delta is content (the per-theme absences), not formatting.
- **Why:** Formatting churn is disclosed as its own class, and in this file it matters to say the shrinkage is not formatting.
- **Verify:** The B89 and B123 entries in classification.json.
- **Disposition:** None required.

### 10. Porter annotations

- **What:** Four porter annotations, all substantive. (a) The part-1 exhibit's banner (candidate L1170–1177): "Ordopharm Agronomics Theme — part 1 of 3 (base) / Ported for SCP-JP (theme:ordopharm rev 22). / The original page serves three code files: 1 = base, 2 = intranet mode, 3 = legacy mode. / JP版も同じ3分割でアップロードしてください（INTEGRATION.md §2）。" — the port's delivery note, and the only place the three-part design is stated in the repo (per-theme item 1 relies on it). (b) The usage translator's note (candidate L48), explaining the single-include contract (section 2). (c) The license box's font 訳注 (candidate L3036), documenting the bunny.net → Google Fonts switch (section 4). (d) The exhibit's font comment `/* 日本語フォント (JP localization) */` (candidate L1183), marking the JP loads. The classifier's single ANNOTATION label (B185) sits on the license zone; the other three ride inside other labeled blocks, which is why this section is written from the grep, not the labels.
- **Why:** R2: annotations are part of the port's record; here they carry the delivery design (a) and two translation judgments (b, c) that a reviewer would otherwise have to guess at.
- **Verify:** `grep -n 'Ported for SCP-JP\|訳注\|JP localization' candidate.txt` returns candidate L1170–1177, L48, L3036, and L1183.
- **Disposition:** Standing (part of the candidate as reviewed).

### 11. Dispositions and exceptions

- **What:** Four items, each with its ground. (1) The EN CDN delivery (P4): charged by T4 (LOCALIZE-ROWS row 117, item (a)) and DISPOSITIONED at GOSIGN2-LEDGER §(c3) as delivery class (ii); the candidate's current base form is the basalt-jp repoint of section 3. (2) The English header tagline (P9): DISPOSITIONED at §(c3) under ruling 2 (section 5). (3) T1's six pseudo-ref errors: the draft-host delivery addresses of section 3, class (iii) mechanics, DISPOSITIONED in register c1. (4) The RERUN16 render items (RENDER-ROWS-RERUN16 (EN15), superseding ROWS-2 under rule S1), none charged to the candidate at the ledger determination: the 506px@320/375 (chromium) and 518px@320/375 (webkit) overflow on page and sample, recorded verbatim; the runtime-hotlink site-theme chain (KB-40, environment layer); the candidate-own cdn.jsdelivr.net and cdn.scpwiki.com hosts, recorded as judgment-required; the sample's credit-modal errors (KB-32, ruling 5); T3 clean on both pages; the original page's first chromium capture was a transient 503 (an http.cat error page), re-run once per the lane's rule 2, the fresh capture being a clean real page — a capture artifact, recorded so the 503 is not mistaken for a page state; and the sample's missing webkit full-page captures (the 32767px screenshot cap). The two per-theme flags and one note are recorded below, not dispositioned.
- **Why:** A disposition is a decision with grounds (AGENTS.md §3 classes (i)/(ii)/(iii); the named KB entries and rulings), not an omission; environment-layer and capture-artifact lines are recorded as not-charged.
- **Verify:** Each item names its deciding record above and in the per-theme record.
- **Disposition:** DISPOSITIONED (items 1–4 as stated); the per-theme items flagged or noted with evidence.

### 12. Verification

- **What:** (a) T1 source check (T1-ROWS row 117): exit 1, 6 errors / 1 warn / 1 info; all six errors are pseudo-ref, class (iii); there is no class (i) error. (b) T2/T3 render (RENDER-ROWS-RERUN16 (EN15)): FINDINGS, the items of section 11(4), all dispositioned; engine coverage full (chromium+webkit, both pages). (c) T4/T5 (LOCALIZE-ROWS row 117, LOCALIZE-S2-B): FINDINGS / FINDINGS jointly, display-affecting findings 3 — item (a) P4 and item (b) P9 dispositioned at §(c3), item (c) (the 17 demo/usage strings) closed by the translation state of the current candidate as recorded in section 6. (d) This package is self-verifying: `python3 review/build_review.py --check` regenerates diff.md and the verdict stamp from the two byte-faithful copies in this directory and compares. Counts in this README are the generator's (diff.md): +366/−770, 1,136 changed lines in 195 change blocks / 20 diff sections.
- **Why:** Verification claims name the cheapest deciding check and its result, not a general assurance.
- **Verify:** Re-run the checker on `pages/theme:ordopharm-jp.txt` and `python3 review/build_review.py --check` in this repo.
- **Disposition:** PASS (GOSIGN2-LEDGER (b) row 117; go-sign, COMPLETION-REPORT §10) — with the two per-theme flags standing against the file's completeness, not against the ledger's determination.

## Per-theme record

### Item 1 — code parts 2 and 3 are absent from the candidate (flagged) Repaired after this package was built: commit ecc8c17 added parts 2 and 3 in full; see the post-package repairs item below.

The original page serves its theme as three code files: part 1, base (original L1212–3052); part 2, intranet mode (original L3054–3247, opening with its own `:root` palette, `--tab-accent: var(--ordo-azure)`, `--map-mat: var(--ordo-void)`); and part 3, legacy mode (original L3248–3433, opening with its bunny.net Abhaya Libre load and its legacy palette, `--tab-accent: var(--ordo-rust)`). The candidate page carries one code block only (candidate L1169–3023, part 1), and no JP text of parts 2 or 3 exists anywhere in the canonical repo (searched: `pages/` holds only the candidate, the original-name page, and the two samples for this theme). The absence is not silent — part 1's banner states the three-part design and directs the same three-part upload at posting, citing the producing lane's INTEGRATION.md §2 (candidate L1170–1177) — but as committed, the delivery is incomplete: the candidate's own tail documentation invites users to import `local--code/theme%3Aordopharm-jp/2` and `/3` (candidate L3047, L3058) and its usage examples offer the `intranet=a` and `legacy=a` parameters (candidate L50–53), and none of those addresses or modes resolves to anything on the candidate page. The render checks exercised the page and sample as committed (part 1 only) and T3 was clean on both, and T4's three findings do not include this item, so no authority has charged it; the ledger's PASS stands on the record as made. This package flags the gap with both sides' line ranges: before this theme can post, the JP texts of parts 2 and 3 have to be located in the producing lane's record or produced, and this package's diff cannot verify them either way.

### Item 2 — the original's second head module is dropped (flagged) Repaired after this package was built: commit ecc8c17 restored the head module; see the post-package repairs item below.

The original's second head module (original L7–76, a `[[module CSS]]` of 70 lines) defines the theme page's own utilities: a `:root` block with the map's node coordinates (`--x1: 300px; --y1: 44px; --x2: 150px; --y2: 100px; --x3: 250px; --y3: 263px`), `--map-image` (the banner.jpg URL), and `--from`/`--to`; and the rules `.tocy`, `#toc .title`, `.swatchset`, `.chip`, `.chip::before`, `.setname`, and a `@media` block. None of it has a counterpart in the candidate (verified by full-string search: every definition and selector above is absent), and unlike item 1, no banner or note records the omission. The candidate's documentation still uses what the module styled: `[[div class="tocy"]]` wraps its table of contents (candidate L40), `[[div class="swatchset"]]` its color specimens (candidate L648), `class="chip"` appears throughout its tables, the exhibit's map rules read the coordinates through `var(--x1, 50%)` fallbacks (candidate L1934–1945), and its background reads `var(--map-image, none)` (candidate L1851). The fallbacks keep every use site valid, so nothing breaks outright; what is lost is the authored presentation (the floated toc, the swatch grid, the chip badges, the map's authored node positions, the map's banner background). The base-subsumption question was checked before flagging: these are the theme's own demo utilities, not Basalt defaults (the same `.tocy` shape exists in the sibling theme:eigenmachine-jp as that theme's own module, which is where this author's pages keep it), so basalt-jp does not supply them. No authority charges the drop (T4's findings are the three items of section 12; RERUN16's T3 was clean on both pages). This package flags the module with its line range and use sites, and does not edit the candidate.

### Item 3 — the holder field's provenance (note)

The candidate's credit block names [[*user Billith]] as 著作権者 (candidate L25), and the license box's backend include repeats the name (`|author=Billith`, candidate L3028). The frozen original names no author anywhere in its text: no byline, no credit module, no exhibit banner (part 1 opens with its font import). The field's value therefore rests on evidence outside this package — the live page's authorship metadata or the wave's own record — and this package can neither confirm nor contradict it from the bytes. Recorded so a reviewer does not mistake the field for a value checked against the original; the same note is recorded for theme:nameless-jp in this batch, whose original is likewise byline-free.

### Post-package repairs (REFRESH3-C)

The items above describe this package as built. The repairs recorded below postdate the package; `candidate.txt` has been recopied from the current canonical `pages/<fullname>.txt` and `diff.md` and the verdict stamp regenerated with `python3 review/build_review.py`, so this package now documents the post-repair candidate. The regenerated stamp reads **STALE** by design: no re-judgement is fabricated here, and the frozen ledger (`GOSIGN2-LEDGER.md` + supplement, FIX5 head 435a6bb) remains the verdict record.

**FIX-ORDOPHARM — split delivery completed (landing ecc8c17, 2026-11-17).** `FIX-ORDOPHARM.md` records that the candidate shipped with only part 1 of the original's three code files and without the original's second head module. Commit ecc8c17 (pages: ordopharm split delivery completed, head module restored) made two pure-insertion hunks, 3,068 → 3,531 lines, 0 deletions: +71 lines at the head restoring the second head module (original L7–76 verbatim but for the one `--map-image` repoint to the draft-host `theme%3Aordopharm-jp/banner.jpg`), and +392 lines after part 1's exhibit close adding parts 2 (intranet) and 3 (legacy) with the port's banner/base-import/font-host/font-stack transformations (no base self-import in the add-ons, part 3's bunny import repointed to Google Fonts). Every `local--code/ordopharm-jp/{1,2,3}` address the page's own tail zone names now resolves. The earlier record items 1 and 2 describe the as-built gaps; the delivered candidate is the completed delivery. T1 stayed all-pseudo-ref (6 errors, no new class (i)).

## Change set outside the two diffed files

The diff covers two files; the port's record is three files larger. `pages/theme-decoration-sample-ordopharm-jp.txt` is the decoration sample the render checks ran against (its findings are the sample half of section 11(4)); `pages/theme:ordopharm.txt` is the original-name page the composition carries alongside the candidate (its second head module is intact, which is how item 2's loss is visible inside the composition itself); and `pages/theme-decoration-sample-ordopharm.txt` is that page's sample. The base theme's candidate, `pages/theme:basalt-jp.txt`, is a separate theme package in this campaign, not part of this change set; this candidate's dependence on it is recorded in section 3.

## License and attribution

- **Title:** Ordopharm Agronomics Theme
- **Author:** Billith
- **Source:** https://scp-wiki.wikidot.com/theme:ordopharm — revision 22
- **License:** Creative Commons Attribution-ShareAlike 3.0 (CC BY-SA 3.0) — license deed: https://creativecommons.org/licenses/by-sa/3.0/
- **Adaptation:** This package holds a Sigma-10 migration port of the work; changes were made. See "Summary" and "Standing sections" in this README for what changed and why. Translator: AI (Muse and its delegated agents), per the campaign's standing attribution rule.
