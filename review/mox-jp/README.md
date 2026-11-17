# Review package — theme:mox-jp (CN → JP port)

<!-- BEGIN GENERATED VERDICT STAMP — do not hand-edit; regenerate with review/build_review.py -->
## Verdict stamp
- Theme: theme:mox-jp — origin CN, population #206 [GOSIGN2-LEDGER (b) row 206]
- Overall: PASS — passed at the ledger determination; no OPEN items [GOSIGN2-LEDGER (b) row 206]
- T1 (source check): FINDINGS (classified) — baseline 2026-11-16: exit 1, 59 errors / 3 warns / 4 infos (pseudo-ref×59); standing classes dispositioned in register c1 [T1-ROWS row 272; GOSIGN2-LEDGER (b) row 206]
- T2/T3 (render, combined verdict): FINDINGS — [combined T2/T3] report `FINDINGS` — page sidebar-unreachable (4 combos) + runtime-hotlink site-theme chain; sample credit-modal (preview-form) + sidebar-unreachable (4 combos). [RENDER-ROWS-2 (RENDER-S2-F (CN9))]
- Engine coverage: full matrix as run by the lane; coverage not separately caveated in the row [RENDER-ROWS-2 row]
- Credit modal: sample credit-modal errors dispositioned preview-form (credit:start-preview has no modal mechanism; GOSIGN-TESTS T2 amendment, 2026-11-16) [RENDER-ROWS-2 (RENDER-S2-F (CN9))]
- T4 (localize patterns + follow-up): FINDINGS — display-affecting findings: 2 [LOCALIZE-ROWS row 205, source LOCALIZE-S2-D]
- T5 (translation text): FINDINGS — the source reports judge T4/T5 jointly; one verdict word covers both [LOCALIZE-ROWS row 205]
- FIX5 re-judgement: none — no OPEN items at the ledger determination [GOSIGN2-LEDGER (b) row 206]
- Computed against: canonical commit 1869877ffdcd33cb214b8dc421fb39e3de8d7e8d; candidate file pages/theme:mox-jp.txt sha256:d8d7b3bd0567a924d426b5ad7d90ab8822f644abed4eef87bb317c4b028a1239; record: GOSIGN2-LEDGER.md + GOSIGN2-LEDGER-SUPPLEMENT.md as of the FIX5 head 435a6bb
<!-- END GENERATED VERDICT STAMP -->

## Status

| | |
|---|---|
| Verdict | **PASS** — passed at the ledger determination; this theme had no OPEN items and no §(e) register entry (GOSIGN2-LEDGER (b) row 206) |
| Standing items | **DISPOSITIONED** — T1 pseudo-ref ×59 (section 3); T4's pattern-7 item dispositioned at the T4 bar, its credit nits and the inherited lang(jp) subtag recorded as the row records them (sections 4, 5, 11); the render row's sidebar item (section 11). One observation is carried in the per-theme record: the original credit body's license and version lines have no counterpart in the candidate |
| Go-sign basis | COMPLETION-REPORT.md §10 (go-sign issued; 81 FIXED / 26 DISPOSITIONED / 0 OPEN across the sweep) |
| Named exception | None for this theme (the sweep's single named exception is theme:amethyst-v2, which has no candidate) |

## Provenance

| | Original | Candidate |
|---|---|---|
| Page | theme:mox | theme:mox-jp |
| Wiki | scp-wiki-cn.wikidot.com | SCP-JP Sigma-10 candidate (canonical repo) |
| Reference revision | 53 (first translation; the candidate's credit block records 初訳時参照リビジョン: 53) | — |
| Source of this copy | Campaign cache `gosign2-lanes/lane-oc-gs-localize-s2-D/orig-mox.txt`, via the mirror store (class COPY, hash-verified against review/sources.tsv) | Canonical file `pages/theme:mox-jp.txt`, byte-identical at canonical HEAD c635d01 (this file was not touched by the post-snapshot usage sweep) |
| Lines / bytes | 4,956 lines / 126,848 bytes | 4,949 lines / 129,684 bytes |
| SHA-256 | 49ad0c66cb26eb667b190cba96b67d18f62d21754acd8455b631913c933b4f80 | d8d7b3bd0567a924d426b5ad7d90ab8822f644abed4eef87bb317c4b028a1239 |

Upstream note (sources.tsv, kind standard, K5a-i): the original has been superseded upstream since the reference revision; the follow-up diff artifact `diff-mox-from53.txt` sits in the campaign record. This package's diff is against revision 53, the revision the port was made from, as recorded. Wave history: the candidate was created by the Stage 2 CN9 integration (commit bbd273c), then touched only by 1869877 (FIX-CREDIT-D, translator-attribution normalization). No FIX4/FIX5 commit touches this file, because the theme had no OPEN items for those waves to re-judge. Mox is also a base theme for other candidates in the population (theme:starry-jp's record notes its base import naming theme:mox-jp/8 — this candidate's fragment address in its correct -jp form).

## Summary

The batch's largest file and its most fragmented delivery. Mox is a CN theme by OxygenNine whose CSS is not one stylesheet but a kit of numbered code fragments: the page imports fragment /8 at its head, exhibits the fragments as code blocks through a long documentation body, and closes with an interwiki frame naming fragment /9 and a large tail module. The candidate preserves that architecture entire and re-hosts every fragment and asset address to the JP draft host — which is why its T1 record is pseudo-ref ×59, the largest count in the batch, all of it the sanctioned draft-host class. The credit furniture (the CN credit module with the theme's own title, version, and license body, plus a bare Rate) becomes the JP preview block and no Rate; the body, the exhibits, and the rendered strings (down to the loading-mask text) translate; one CN-only preview module at the head is dropped. The localize row judges the port sound (delivery relocation, credit composition, and body localization all healthy, no display collapse) with three minor items: a pattern-7 font reach gap at named sites, two credit notation nits, and an inherited `lang(jp)` subtag error that the original itself carries. Measured churn (diff.md, the generator's count: +208/−215, 423 changed lines in 165 change blocks; a GNU-diff count of the same pair gives the same 423 — the counts agree exactly). The diff is Tier 2 format, and this README is the adjudicated explanation the Tier 2 header points to.

## Class summary

Auto-classification by review/classify_hunks.py (signature table 2026-11-17.1): 165 change blocks — 127 specific (77.0%), 35 heuristic (21.2%), 3 residue (1.8%), 0 skipped. Pattern citations below name the KB entry; the patterns/ tree state cited throughout is commit 9c5e9079afb01d30cb9fc4ef9d714e5591eb2ffa.

| Label | Blocks |
|---|---|
| DRAFT-HOST | 61 |
| TRANSLATION-ANCHORED | 55 |
| DELIVERY-MOVE | 46 |
| TRANS-UNANCHORED | 37 |
| INCLUDE-REPOINT | 11 |
| COMMENT-TEXT | 10 |
| GLYPH-FORM | 9 |
| COMPONENT-SWAP | 7 |
| DELIVERY-HOST | 3 |
| CREDIT-PREVIEW | 2 |
| CREDIT-PROSE | 2 |
| EXHIBIT-RESTRUCTURE | 2 |
| SELF-DELIVERY | 2 |
| ANNOTATION | 1 |
| BARE-RATE-DEL | 1 |
| CONTENT-STRING | 1 |
| CSS-BODY | 1 |
| IFTAGS | 1 |
| JPFONT-LOAD | 1 |
| TASL-FIELDS | 1 |
| WS-ONLY | 1 |

Adjudication for this README (the blocks were read against the bytes, in groups where the class treatment applies): DRAFT-HOST (61) and DELIVERY-MOVE (46) together are the fragment architecture's churn — the topology record shows the repeated fragment units cross-matching between the body's code exhibits and the tail module (similarities 0.875 throughout), and section 3 adjudicates the mass as address re-hosting inside a preserved architecture, not 46 moves. The 2 EXHIBIT-RESTRUCTURE blocks are include repoints with parameter localization (B98, section 2) and the tail frame's repoint (B118, section 3). The 3 residue blocks are single exhibit lines (B13, B17, B99), resolved by shape. GLYPH-FORM (9) rides on translation blocks: CN glyph forms taking JP forms in translated strings (section 6). After adjudication no block is left unexplained.

## Standing sections

### 0. Header and provenance frame

- **What:** Theme theme:mox-jp; original theme:mox on scp-wiki-cn at reference revision 53; candidate `pages/theme:mox-jp.txt`. Provenance route: derived from the original at the reference revision by the Stage 2 CN9 wave (sources.tsv kind: standard; the upstream-superseded note and its follow-up artifact are recorded in the Provenance table). The original opens with a CN preview module and its head delivery import (original L1–7); the candidate opens with the delivery import alone (candidate L1–5), the preview module gone (section 3), and localizes the tag gate in the body (`+版式` → `+テーマ`, block B4).
- **Why:** Section 0 declares the provenance route and the revision baseline so every later count is read against the right baseline — for this theme, against revision 53 specifically, since the upstream page has moved since.
- **Verify:** The sources.tsv row for mox-jp; `sha256sum original.txt` against the Provenance table.
- **Disposition:** Standing (the route and baseline themselves).

### 1. Credit and attribution

- **What:** The original's credit furniture is the CN credit module with the theme's own body inside it: a `:scp-wiki-cn:credit:start`/`more`/`end` triple whose body is the theme's title block ("+ MOX 版式", "版本 Release 3.0.0", "由 [[*User OxygenNine]]制作") and a license line ("授权协议：CC-BY-SA 4.0 International") (original L20–25, blocks B6–B8), followed by a bare `[[module Rate]]` (original L27). The candidate deletes the Rate (BARE-RATE-DEL — no label pairs it, so the pattern-3 exception does not apply) and installs the JP preview block inside the same right-aligned frame (candidate L17–29): the eight ruling-3 fields （タイトル MOXテーマ; 翻訳責任者 AI; 翻訳年 2026; 原題 MOX 版式； 著作権者 [[*User OxygenNine]]; 作成年 2024; 初訳時参照リビジョン 53; the source link, section 7), with the title block restated as "+ MOXテーマ" ahead of the fields. The author field names OxygenNine with his user link, matching the original's own credit body — no named creator is dropped. Two things the original's credit body carried do not survive into the block: the version line (Release 3.0.0) and the license line (CC-BY-SA 4.0 International) — the candidate carries the license nowhere (grep-verified; no license box is appended either). That is the per-theme record's observation. The localize row's credit comments were two notation nits — the AI translator notation and the source link's 「ソース」 label — recorded as nits, not defects.
- **Why:** P3/T1: the preview credit module is the rate-bearing JP form, so the bare Rate is deleted rather than duplicated (KB-09). Ruling 3 fixes the eight fields; the form has no version or license slot, which is the mechanical cause of the observation — stated here so the loss is attributed to the form, and flagged in the per-theme record because this original, unlike most, actually stated its license in the credit body.
- **Verify:** Read candidate L13–30 against original L16–32; `grep -n 'CC-BY-SA\|CC BY-SA\|Release' candidate.txt` returns nothing.
- **Disposition:** FIXED (GOSIGN2-LEDGER §(c3): P3 credit fields FIXED, credit waves, checker-verified); the nits and the license/version observation are recorded in sections 11 and the per-theme record.

### 2. Includes and components

- **What:** The include repoints (INCLUDE-REPOINT 11, COMPONENT-SWAP 7): the credit includes (section 1); the tail's interwiki-style include (section 3); and the component exhibits through the body — the type case is block B98, where an anomaly-class-bar exhibit's include repoints from `:scp-wiki-cn:component:anomaly-class-bar-source` to `:scp-jp:component:anomaly-class-bar-source`, its `|lang= cn` parameter is dropped (the JP component does not take the CN language parameter in that form), and its sample item number localizes from CN-XXXX-J to JP-XXXX. The remaining swaps are the same shape at other exhibits: CN component targets become their JP counterparts, with sample parameters localized where the parameter is itself sample content.
- **Why:** P1 (KB-15): an include must name the JP counterpart that actually exists on scp-jp; the repointed components have verified JP counterparts, so all are repointed and none is kept as an exception. Ruling 4 is not engaged: no component had to be ported alongside this theme.
- **Verify:** `grep -n '\[\[include' candidate.txt` — every live include names a `:scp-jp:` target; the exhibits' escaped and code-form includes name JP targets too.
- **Disposition:** Applied; no foreign include kept, no named exception needed.

### 3. Delivery and code loading

- **What:** The fragment architecture, preserved entire. The original delivers from numbered code fragments of its own page: a head `[[module CSS]]` importing fragment /8 by its page URL (`https://scp-wiki-cn.wikidot.com/theme:mox/code/8`, original L4–7); a body that exhibits the theme's fragments as code blocks at intervals through the documentation (the repeated ~19-line units the topology record cross-matches); and a tail frame — an interwiki-style include at priority 1 naming fragment /9 on CN storage with the CN form's extra parameters (`type=sidebar`, `override=`, `css=`), followed by a large tail module (original L4404 onward) whose asset addresses point at the author's own wdfiles host (oxygennine.wdfiles.com). The candidate re-hosts every coordinate to the JP draft host and changes nothing about the architecture: the head module imports `local--code/theme%3Amox-jp/8` from the draft host (candidate L1–5, block B2); the logo image at the body head re-hosts likewise (candidate L11); the exhibited fragments' internal addresses re-host (the DRAFT-HOST mass — 61 labeled blocks, including the tail module's icon-sheet address, `local--files/theme%3Amox-jp/icons-2`, where the original named the author's host); and the tail interwiki include names fragment /9 on the draft host in the plain two-parameter form (candidate L4400–4404, block B119) — the CN form's sidebar/override/css parameters do not survive, the JP component's form not taking them. One head element is deleted outright: the original's first line is a `[[module ThemePreviewer]]` naming a cloudfront-hosted base stylesheet (original L1, block B1) — a CN-wiki preview affordance with no JP counterpart in this population's forms, dropped rather than repointed. T1's pseudo-ref ×59 is this section's population: the fragment addresses (head /8, tail /9, and the fragments' internal asset addresses) in their draft-host form.
- **Why:** P4/T9 (delivery served from JP hosts) in the theme's own idiom: mox's delivery *is* its fragment addresses, so re-hosting them is the delivery port, and the architecture (head import, exhibited fragments, tail frame) is the theme's design, kept. The draft-host form is KB-41, class (iii): sanctioned at draft stage, rewritten to the production host at posting — at this theme's scale that rewrite is a population of addresses, not a line. The ThemePreviewer's deletion is the counterpart judgment: a module that exists to preview against a CN CDN base has no function in the JP delivery.
- **Verify:** Read candidate L1–5 and L4396–4410 against original L1–7 and L4404–4412; `grep -c 'sigma10-jp-test' candidate.txt` — the draft-host population; `grep -n 'ThemePreviewer\|cloudfront' candidate.txt` returns nothing.
- **Disposition:** DISPOSITIONED (draft-host lines, class (iii)); the architecture itself is the applied port.

### 4. Fonts and assets

- **What:** Fonts — the batch's most qualified font account, because the theme's typography is fragment-distributed. The one labeled load change (block B110, JPFONT-LOAD): a fragment's import moves from the CN Google-Fonts mirror (fonts.font.im) to fonts.googleapis.com and is rewritten into css2 grammar — but its family list still names **Noto Sans SC** alongside Oxygen Mono and Raleway (original L558 → candidate L554). The theme's documentation names its UI font as "Noto Sans CJK" with Raleway (candidate L517). The localize row's pattern-7 item is exactly this territory: a minor MISSED — the JP body font does not reach at the named sites (the row cites L517–521, L320–322, and L554 in its line numbering) — compounded by an inherited structural error from the original at the same sites. The row records it without a display-affecting mark, and the ledger dispositions P7 at the T4 bar. Assets: the theme's own files (the logo, the icon sheets, the fragments' internal images) re-host to the draft host with their paths' shapes kept (section 3); no EN/CN-storage asset line survives in the candidate, and T1 records no hotlink against this file — its 59 errors are all the draft-host class.
- **Why:** P7/T5: the load that changed hosts kept its SC family because that fragment's stack is built on it, and the checker's judgment — recorded, dispositioned — is that the reach gap is minor and structural-inherited rather than a port-introduced break. This package states the item with its sites and its disposition so the SC name in a candidate load is not mistaken for an unexamined leftover: it was examined, charged as a minor missed item, and dispositioned at the T4 bar. The contrast with this batch's two font defects (laruetheme, laughter-and-knives) is the documentation: there, loads vanished with no record; here, the gap has a record and a disposition.
- **Verify:** `grep -n 'fonts.googleapis\|fonts.font.im' candidate.txt` — the one load, googleapis only; read candidate L554 against original L558.
- **Disposition:** DISPOSITIONED (P7, recorded without a display-affecting mark; T4 bar; GOSIGN2-LEDGER line 1591).

### 5. Header and sidebar furniture

- **What:** Two items. (1) The per-language string tables: the theme keeps its UI strings (the saving-page tips message and its kin) in `:root:lang()` blocks per language, and the candidate's tables carry the JP string under `:root:lang(jp)` (candidate L4058–4062's zone) — an invalid language subtag (jp is a country code; the matching subtag is ja), which the original itself uses for its Japanese entry (the original carries exactly one lang(jp) block, grep-verified in both files, alongside correct lang(ja) blocks elsewhere in its tables). The candidate inherited the subtag byte-for-byte while translating the string it keys. The block therefore never matches on either wiki — an original defect, inherited, noted by T4 as 原語由来 (from the original). (2) The sidebar: the render row records the sidebar as unreachable in four engine/viewport combinations on both the theme page and the sample (section 11) — the theme's layout (its sidebar is a transformed, fragment-delivered element) reproduces its CN behavior on the JP side; the row preserves the reading as the theme's own geometry, not a port break.
- **Why:** Item (1) is the parity principle's hard case stated honestly: live behavior is the spec, and the original's table entry is inert in the original too — "repairing" the subtag would activate a string the original never activated, a behavior change beyond the port's mandate. The conservative carry-over, with the defect named and attributed to the original, is the documented treatment; T4's row makes the same attribution.
- **Verify:** `grep -n 'lang(jp)' candidate.txt original.txt` — one hit in each, the same table entry; `grep -c 'lang(ja)' candidate.txt` — the correct form used elsewhere.
- **Disposition:** Item (1) recorded as an inherited original defect (T4 row, section 11); item (2) is the render row's standing reading.

### 6. Text translation

- **What:** The body and documentation translate throughout (92 translation-labeled blocks): the exhibits, the fragment documentation, the component samples, and the CSS comments (COMMENT-TEXT 10). The rendered-string check lands on block B115 (CONTENT-STRING): the loading mask's CSS content string, `content: '正在加载中……'` → `'読み込み中……'` (original L3371 → candidate L3367) — localized, no source-language text left in a rendered string. The GLYPH-FORM blocks (9) ride on the translation mass: strings whose characters take JP glyph forms （such as the theme's own terminology in the exhibits). The string tables of section 5 translate per language entry, the CN entries staying CN as the table's design requires.
- **Why:** P9/P10 (prose, documentation, comments, and rendered strings into Japanese), with KB-18 for the content string: a `content:` value is reader-visible text and is held to the translation standard, which this candidate meets.
- **Verify:** `grep -n '読み込み中' candidate.txt` — the localized content string; read any exhibit range against its original (for example candidate L483–489 against original L486–493).
- **Disposition:** Applied (the theme's T4 record shows no translation finding; its items are sections 1, 4, and 5).

### 7. Links and references

- **What:** The credit block's source link names the original at its recorded host (scp-wiki-cn.wikidot.com, section 1), with the label 「ソース」 — one of T4's two notation nits (the label is terse where the population's form is fuller; a nit, recorded as such). The usage references name the candidate's fragments in their re-hosted forms (section 3). No usage-example self-reference in the plain-slug form stands in this candidate: its installation references are the fragment addresses themselves, which the port re-hosted to the candidate's own /8 and /9 (and the population's other records confirm the form — theme:starry-jp's ledger entry notes this candidate's base import correctly naming theme:mox-jp/8). The author's-host references in the original's tail CSS (oxygennine.wdfiles.com) are asset addresses, re-hosted in section 3, not prose links. No dead prose link was found in this candidate.
- **Why:** P9 link hygiene: the source link resolves at the recorded host; the fragment references are the theme's delivery, held to the delivery standard of section 3 rather than the example standard.
- **Verify:** `grep -n 'oxygennine.wdfiles\|scp-wiki-cn.wikidot' candidate.txt` — the source link only, no asset or delivery line keeps a CN host.
- **Disposition:** Applied; the label nit is recorded in section 11.

### 8. Structure and exhibits

- **What:** The exhibit census is complete against the original: the fragment exhibits at their intervals, the component exhibits (section 2), the documentation sections, and the tail frame. The classifier's 2 EXHIBIT-RESTRUCTURE blocks are the anomaly-class exhibit's repoint (B98) and the tail frame's repoint (B118) — neither restructures anything. The one CSS-BODY block (B114, original L2460 → candidate L2456) is a single rule change inside a fragment, riding with the fragment's translation-and-address churn around it. The architecture's repetition is the file's dominant visual fact and its dominant classification mass (section 3): the same fragment units appear as exhibits and as delivery, and the aligner's cross-pairing of the copies is expected, adjudicated in the class summary.
- **Why:** P8 (exhibit structure follows the original) governs the census; at this file's scale the census is stated at the level of the architecture's parts, each of which was verified present in both files by the container and fragment greps of section 3.
- **Verify:** The container census: `grep -n '\[\[module\|\[\[code\|interwiki' candidate.txt` against the same grep on original.txt — the same architecture at JP coordinates.
- **Disposition:** Standing (nothing to disposition).

### 9. Formatting only

- **What:** One whitespace-only block (B112, original L1491 → candidate L1487), a single line inside a fragment exhibit. Nothing else in a 423-changed-line diff is formatting-only.
- **Why:** Stated so the formatting mass is separated from content mass, per the class treatment — here, essentially all of the churn is addresses and translation.
- **Verify:** Block B112 in classification.json (label WS-ONLY).
- **Disposition:** Standing (nothing to disposition).

### 10. Porter annotations

- **What:** One annotation-form item, and it is not a porter's note: the page comment at the body head, `[!-- 版式展示 --]` → `[!-- テーマ表示 --]` (original L12 → candidate L9, block B3, the classifier's ANNOTATION hit) — the theme's own exhibit comment, translated with the prose. Checked explicitly for porter annotations proper: the candidate carries no porter comment, no translator's note, and no correction comment of the kind this batch's other themes carry (`grep -n 'SCP-JP port\|credit correction\|訳注' candidate.txt` returns nothing). Its judgment calls are documented in the ledger records instead.
- **Why:** T11 asks that judgment calls stay auditable; here the audit trail is the T4 row and its dispositions, and the section states the in-file absence as a checked fact.
- **Disposition:** Standing (absence recorded).

### 11. Dispositions and exceptions

- **What:** Four standing items, all closed. (1) T1's pseudo-ref ×59 (section 3): class (iii), sanctioned draft-host form, at this theme's fragment scale. (2) T4's pattern-7 item (section 4): DISPOSITIONED, recorded without a display-affecting mark at the T4 bar (GOSIGN2-LEDGER line 1591) — the JP body font's reach gap at the named sites, compounded by an inherited structural error. (3) T4's credit notation nits (section 1): the AI translator notation and the 「ソース」 link label — noted by the row as nits, standing as written. (4) The inherited `lang(jp)` subtag (section 5): an original defect carried over byte-for-byte, attributed to the original by the T4 row itself （原語由来）. Plus the render row's items: the sidebar unreachable in four combinations on both pages (section 5), a runtime-hotlink in the site-theme chain on the theme page (the KB-40 shape — in what the page loads, not in this file), and the sample's credit-modal reading, dispositioned preview-form (the standing GOSIGN-TESTS T2 amendment). The localize row's overall judgment is part of the record: body localization, credit composition, and delivery relocation are sound, and there is no display collapse （表示崩壊はない).
- **Why:** A disposition names its ground: class (iii) for the draft host, the T4 bar for the font item, the row's own "nit" classification for the notation items, and original-authorship for the inherited subtag. Nothing in this theme rests on an unnamed exception.
- **Verify:** The theme's rows in T1-ROWS, LOCALIZE-ROWS, and RENDER-ROWS-2; the disposition line in GOSIGN2-LEDGER (line 1591).
- **Disposition:** DISPOSITIONED (all four, on the grounds named).

### 12. Verification record

- **What:** T1 (source check, T1-ROWS row 272): pseudo-ref ×59 (exit 1, 59 errors / 3 warns / 4 infos), no hotlink and no http errors — the largest pseudo-ref count in the batch, and every error is a draft-host fragment address of section 3. T4 (localize check, LOCALIZE-ROWS row 205, wave LOCALIZE-S2-D): FINDINGS, 2 findings — the pattern-7 minor MISSED (JP body font not reaching at L517–521, L320–322, L554, with an inherited structural error) and the credit notation nits (AI notation, 「ソース」 label), plus the noted inherited `lang(jp)` subtag at L4058; the row's summary judgment is that the port is sound with no display collapse. T2/T3 (render check, RENDER-ROWS-2, wave RENDER-S2-F (CN9)): the readings of sections 5 and 11. The go-sign ledger row (§(b) row 206) aggregates T1 FINDINGS (classified), T2 FINDINGS, T3 FINDINGS, T4 FINDINGS, T5 PASS — every finding classified, none OPEN.
- **Why:** The counts are the acceptance evidence for the sections above: each checker's scope is stated so a clean result is not read past what the checker can see (T1's 59 errors are one class at fragment scale, not 59 problems).
- **Verify:** The three ledger-part files named above, rows 272 and 205 and the theme's render row; GOSIGN2-LEDGER §(b) row 206 for the aggregate.
- **Disposition:** PASS at the ledger determination, with the items of section 11 dispositioned as recorded.

## Per-theme record

Two items belong to this theme alone.

**The original credit body's license and version lines have no counterpart in the candidate (observation, flagged for the coordinator's judgment).** The original's credit body states the theme's version ("版本 Release 3.0.0") and its license ("授权协议：CC-BY-SA 4.0 International") in the credit module's own text (original L20–25). The candidate's preview block, whose ruling-3 form has no version or license field, carries neither, and no license box elsewhere in the candidate records them (grep-verified: the candidate contains no license statement at all). The mechanical cause is the block form, and the localize row charged only notation nits on the credit — so this is recorded as an observation, not a defect: but of the batch's themes, this is the one whose original actually stated its license inside its credit furniture, and a reader of the candidate alone would not learn that the theme is CC-BY-SA 4.0 or that it is at Release 3.0.0. If the coordinator wants the record kept, a license-box supplement of the kind mole-cricket-jp and laughter-and-knives-theme-jp carry is the population's form for it.

**The upstream page has moved since the reference revision.** Sources.tsv records that the original was superseded upstream after revision 53, with the follow-up diff kept as the campaign artifact `diff-mox-from53.txt` (kind K5a-i). The port, this package, and the verdict all stand against revision 53; a future refresh against the newer upstream text is a separate act, and nothing in this package should be read as covering it. (The same note, with its own artifact, stands in the lead-by-example package.)

## Change set outside the two diffed files

| File | Change |
|---|---|
| `pages/theme-decoration-sample-mox-jp.txt` | The theme's decoration sample: a JP page applying the candidate, the surface the T2/T3 render checks measured (section 11's sample readings) |
