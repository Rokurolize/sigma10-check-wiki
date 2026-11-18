# Review package — theme:sound-jp

<!-- BEGIN GENERATED VERDICT STAMP — do not hand-edit; regenerate with review/build_review.py -->
## Verdict stamp
- Theme: theme:sound-jp — origin CN, population #230 [GOSIGN2-LEDGER (b) row 230]
- Overall: STALE — candidate file changed since the verdict was computed (verdict against 435a6bb-era content, file sha256 now e5bca474b6dbc7cf14041bcb8c55e57394e0ed5fa644a5ee05a82c51e87899cc); the verdicts below were computed against that pre-change file, and the record verdict stands: a candidate revised through the campaign's recorded repairs is posted like a PASS row, with the change recorded in its package
- T1 (source check): FINDINGS (classified) — baseline 2026-11-16: exit 1, 31 errors / 0 warns / 1 info (pseudo-ref×31); standing classes dispositioned in register c1 [T1-ROWS row 261; GOSIGN2-LEDGER (b) row 230]
- T2/T3 (render, combined verdict): FINDINGS — [combined T2/T3] report `FINDINGS` — sidebar-unreachable at 375/320 (both engines) on page and sample + runtime-hotlink site-theme chain; sample credit-modal (preview-form); T3 missing mobile sidebar toggle confirmed, sample §15/§16 panels near-white on light effectively unreadable; full-engine coverage. [RENDER-ROWS-G (CN14)]
- Engine coverage: full (chromium+webkit, both pages) [RENDER-ROWS-G row, findings cell]
- Credit modal: sample credit-modal errors dispositioned preview-form (credit:start-preview has no modal mechanism; GOSIGN-TESTS T2 amendment, 2026-11-16) [RENDER-ROWS-G (CN14)]
- T4 (localize patterns + follow-up): FINDINGS — display-affecting findings: 1 [LOCALIZE-ROWS row 229, source LOCALIZE-S2-E]
- T5 (translation text): FINDINGS — the source reports judge T4/T5 jointly; one verdict word covers both [LOCALIZE-ROWS row 229]
- FIX5 re-judgement: items 84 (class E) DISPOSITIONED, 85 (class F) DISPOSITIONED — FIX5-CONTRB (no edit, no commit): MOX palette identical to the original (parity diff); the missing toggle is authored by the shared MOX base (.open-menu{display:none} at theme:mox-jp L1212-1214 plus off-canvas hover reveal), reproduced by both original and candidate; the candidate carries no toggle rule of its own [GOSIGN2-LEDGER-SUPPLEMENT (a) items 84–85]
- Computed against: canonical commit fb435643733dfd93d8dfa698861e4a59921d8f0f; candidate file pages/theme:sound-jp.txt sha256:e5bca474b6dbc7cf14041bcb8c55e57394e0ed5fa644a5ee05a82c51e87899cc; record: GOSIGN2-LEDGER.md + GOSIGN2-LEDGER-SUPPLEMENT.md as of the FIX5 head 435a6bb
<!-- END GENERATED VERDICT STAMP -->

## Status

| | |
|---|---|
| Verdict | **PASS** — go-sign re-run (the candidate is one of the 286 pass-eligible themes); both of its ledger-open items were re-judged DISPOSITIONED with grounds, with no edit to the candidate |
| Blocking items at ledger time | GOSIGN2-LEDGER.md §(e) item 84 [E] — sample §15/§16 panels near-white on light, effectively unreadable; item 85 [F] — sidebar unreachable at 375/320 in both engines (mobile toggle missing). Both were OPEN in ledger c2 (L1129, L1131). |
| Re-judgment | GOSIGN2-LEDGER-SUPPLEMENT.md items 84 and 85: both **DISPOSITIONED** by FIX5-CONTRB (no edit, no commit) on original-identical / original-faithful-mechanism grounds, re-derived from this package's two files in the Per-theme record below |
| Standing items | **DISPOSITIONED** — 31 × `pseudo-ref` (draft-host / posting-procedure classes); credit-modal on preview pages (KB-32); runtime-hotlink site-theme chain (KB-40); draft-bucket asset 404s (KB-58); T5 minor text residues (two prose 「版式」 + one comment mistranslation), recorded at the source report's weight. None is charged to the candidate. |
| Go-sign basis | COMPLETION-REPORT.md §10 (go-sign issued; 81 FIXED / 26 DISPOSITIONED / 0 OPEN across the sweep) |
| Named exception | None for this theme (the sweep's single named exception is theme:amethyst-v2, which has no candidate) |

The generated stamp's **STALE** banner is a provenance fact, not a reopened defect: the candidate's last content commit is `fb43564` ("pages: stylesheet-address repairs in four themes", the FIX-NAVLA2 landing), which is later than the FIX5 verdict head `435a6bb` and changes only the two self-delivery addresses from `/1` to `/2` (section 3). The palette and sidebar surfaces on which items 84/85 turn were not touched by that commit, so the re-derivations below apply to the current bytes.

## Provenance

| | Original | Candidate |
|---|---|---|
| Page | theme:sound (虚拟之音 主题版式) | theme:sound-jp |
| Wiki | scp-wiki-cn.wikidot.com (CN) | SCP-JP Sigma-10 candidate (canonical repo) |
| Reference revision | 6 (rev 6 content; the lane's rev-6 note records a revert to rev 4 content) | — |
| Source of this copy | Campaign cache `gosign2-lanes/lane-oc-gs-localize-s2-E/orig-sound.txt`, via the mirror store `review-mirrors/orig-sound-rev6.txt` (class COPY, fetched once by LOCALIZE-S2-E) | Canonical file `pages/theme:sound-jp.txt`, copied at worktree HEAD `18aa3018`; last content commit `fb43564` (navla2 landing) |
| Lines / bytes | 579 lines / 18,898 bytes (last line carries no trailing newline) | 615 lines / 21,853 bytes (last line carries no trailing newline) |
| SHA-256 | `8d16d75b6222aed851a23f75bdddf1505af6cf28c7535973c6e11bc3d78decdd` | `e5bca474b6dbc7cf14041bcb8c55e57394e0ed5fa644a5ee05a82c51e87899cc` |

Package files: `original.txt` and `candidate.txt` as tabled above (candidate byte-identical to the canonical file, `cmp`-verified; original hash equals both the INDEX.tsv and sources.tsv values); `classification.json` and the skeleton behind this README from classify_hunks.py 0.1.0, signature table 2026-11-17.1, patterns commit `9c5e9079afb01d30cb9fc4ef9d714e5591eb2ffa`. `diff.md` is generated, never hand-edited.

## Summary

Sound is a CN-origin theme layered over the MOX base. The port preserves the two-exhibit topology (variables exhibit `/1`, stylesheet exhibit `/2`), the collapsible, and the whole rule set; what changes is the frame, the language, and the hosts. The CN `ThemePreviewer` helper and bare Rate are dropped, the preview credit block and the JP interwiki-style frame are added, `+版式 +原创` becomes `+テーマ`, the CN font host is replaced by Google Fonts with Noto Sans JP, the assets are re-hosted on the draft host, and the usage body is translated in full. The classifier reads 66 change blocks (41 specific / 24 heuristic / 1 residue / 0 skipped), with 31 of them being the draft-host asset rewrites. The theme's two blocking items were never candidate-side defects: the unreadable §15/§16 panels and the missing mobile toggle are the original MOX palette and the MOX base's own off-canvas/hover sidebar, faithfully reproduced — the byte-identity and mechanism arguments are re-derived below from this package alone.

## Standing checks (this brief)

All eight checks ordered by the brief, with the result stated so a reviewer can re-run each from this worktree:

| Check | Result |
|---|---|
| Credit author vs the original's credit carriers | **Clean — no flag.** Candidate `著作権者: [[*user OxygenNine]]` (L19) names the author; the original's credit apparatus is a bare rate (orig L12, names nobody), but the original's own authorship evidence names OxygenNine (`sound.meta.json` `created_by: OxygenNine` at rev 4; `sound.notes.md` "by OxygenNine"; the MOX base by the same author). The pointer names an evidenced author, not nobody; the candidate was not edited. |
| Credit/source link hosts vs sources.tsv, with probes | **Match.** `元記事リンク` (candidate L22) is `https://scp-wiki-cn.wikidot.com/theme:sound`, byte-equal to sources.tsv `original_url`; probe **HTTP 200**. The two body links to CN-only pages (L28 `kawaii-o5-3`, L30 `theme:mox`) also probe **200**. |
| Delivery topology and gates in render-time text | **Clean.** The frame include (L1–4) and head module (L6–9) precede the `[[iftags +テーマ]]` gate (L11–604); the tail credit-CSS module (L606–615) follows `[[/iftags]]` (L604). All delivery is in render-time text, not gated away. |
| Self-delivery addresses (navla2 landing `fb43564`) | **Confirmed.** L3 frame `theme=` and L8 head-module `@import` both name `/2`; before `fb43564` they named `/1` (variables exhibit). The original (rev 6, L5) imports `theme:sound/code/2` (stylesheet). Citation: `R/review-scout/FIX-NAVLA2.md` §4; commit `fb435643733dfd93d8dfa698861e4a59921d8f0f`. Probe: `/2` serves 15,802 B, **HTTP 200**. |
| Content presence (second modules, license entries, footnoteblock) | Three `[[module CSS]]` blocks: L6–9 (head delivery), L87–89 (`#u-logo1 img` filter), L606–615 (JP credit-CSS correction). No `license-box` include; `#license-area` rules (L270–273) are BHL/MOX CSS variables, not a box. No `footnoteblock`, live or escaped (grep: 0). No `[[module Rate]]` remains. |
| Brace balance by depth | Balanced: candidate stylesheet exhibit L123–600, head module L7–8, tail module L607–614, and original stylesheet L114–568 all close at depth 0 with minimum depth 0. No truncated rule. |
| Font loads vs stacks, both directions | Loaded: Noto Sans JP, Oxygen Mono, Raleway, Zen Maru Gothic (L123–124). Stacks name exactly these plus system fallbacks (L129–131, L444, L478, L112); `FontAwesome` appears only in a comment (L136, inert). No unloaded family in a stack; no loaded family unused. Base subtraction holds: MOX base loads Noto Sans **SC** (`pages/theme:mox-jp.txt` L554), not JP. |
| Duplicated includes/imports | No duplicate `@import`. `component:image-block` appears twice (L91, L106) with different assets (`projectfantasy.svg`, `531k.jpg`) — two distinct exhibits, not a repeated delivery (KB-65 clean). |

## 0. Header / provenance

- Delivery: no relocation detected between the sides; each side's components match by kind (the classifier's topology pass finds no moved body). One delivery *address* was corrected after classification (see below).

- **What (this theme):** theme:sound-jp is derived from the branch original `theme:sound` at the TSV reference revision 6, not adopted from a production JP counterpart (R4 does not apply — the classifier's `r4_signal` is absent). The three mutually consistent pieces of evidence are: sources.tsv keys the row `sound-jp` with mirror SHA `8d16d75b…` (class COPY, 18,898 B) at rev 6; the candidate's credit block records `初訳時参照リビジョン: 6` (L21); and the follow-up artifact `diff-sound-from6.txt` records `scp-wiki-cn:theme:sound rev6 → rev6 変更: なし`, so the mirror here is also the current original. R-disp class: the theme carried two §(e) blocking items, both re-judged DISPOSITIONED without an edit.
- **Why:** provenance declaration is standing section 0 (TAXONOMY §3); the R-disp treatment follows ROLLOUT §2 class R-disp, whose packages must let a third party re-derive each disposition from the two sources.
- **Verify (from this repo alone):** `sha256sum review/sound-jp/original.txt` → `8d16d75b…` (matches `review/sources.tsv` and the mirror INDEX); `sha256sum review/sound-jp/candidate.txt` → `e5bca474…` (matches `pages/theme:sound-jp.txt`, `cmp`-identical); read `review/sound-jp/original.txt` L21 of the candidate for the reference revision and the campaign artifact `diff-sound-from6.txt` for the follow-up result.
- **Disposition:** standing. The post-verdict delivery commit `fb43564` (FIX-NAVLA2 §4) is recorded as provenance, not as a new finding; see section 3 and the Per-theme record.

## Class summary

| Label | Blocks |
|---|---|
| COMMENT-TEXT | 3 |
| COMPONENT-SWAP | 1 |
| CREDIT-PREVIEW | 1 |
| CREDIT-PROSE | 1 |
| CSS-BODY | 3 |
| DELIVERY-HOST | 2 |
| DRAFT-HOST | 31 |
| EXHIBIT-RESTRUCTURE | 3 |
| FONT-IMPORT | 1 |
| GLYPH-FORM | 2 |
| IFTAGS | 1 |
| INCLUDE-REPOINT | 3 |
| JPFONT-LOAD | 1 |
| SELF-DELIVERY | 2 |
| T7-CREDIT-CSS | 1 |
| TASL-FIELDS | 1 |
| TRANS-UNANCHORED | 25 |
| TRANSLATION-ANCHORED | 8 |

Counts: 66 blocks, 41 specific, 24 heuristic, 1 residue, 0 skipped (comment text). The skeleton lists each block once under its primary label; the sections below write from `label_spans`, so secondary labels (e.g. T7-CREDIT-CSS inside B66, GLYPH-FORM inside B10/B12, TASL-FIELDS inside B4) are argued where their mechanism belongs, not dropped. The skeleton's `none` in sections 5, 7 and 10 means "no primary maps here", not "no change" — all three are filled below from secondary labels and byte evidence (the EXEMPLAR-AMBROSE strain).

## 1. Credit and attribution

- CREDIT-PREVIEW (A): Credit block swap (P3/T1): the JP environment's preview credit module is the rate-bearing form; the branch-original credit module does not render here.
  Verify: Re-run the T1 checker (check_source.py); the credit includes must resolve on scp-jp.
  - B4: orig 12-12 -> cand 14-23 (body -> body)

- TASL-FIELDS (A): Credit fields (ruling 3, KB-10): the eight attribution fields are required for the TASL record; campaign translations are credited to AI. [secondary label of B4]
- T7-CREDIT-CSS (B): Credit-module CSS supplement (T7, KB-11/KB-12/KB-62). [secondary label of B66]
- CREDIT-PROSE (C): Translated credit prose (P3/P10). [secondary label of B4]

- **What (this theme):** B4 (original L12 → candidate L14–23) is the whole credit swap. The original's bare `[[module rate]]` is deleted and the `:scp-jp:credit:start-preview` / `end-preview` pair takes its place, carrying all eight ruling-3 fields: タイトル (L15), 翻訳責任者 AI (L16), 翻訳年 2026 (L17), 原題 (L18), 著作権者 `[[*user OxygenNine]]` (L19), 作成年 2025 (L20), 初訳時参照リビジョン 6 (L21), 元記事リンク (L22). No live `[[module Rate]]` remains (grep: 0) — the preview module is rate-bearing, so no duplicate widget stands (KB-09 clean). The independent tail module (B66, candidate L606–615) adds the JP-DOM credit correction: the base's `.creditButton p a` rule (`theme:mox-jp.txt` L1711) is re-stated as `.rateBox .rate-box-with-credit-button .creditButton > a` (L610), matching the direct-child anchor the preview module actually emits. No license box on either side; `#license-area` at L270–273 is a MOX variable block, not a box.
- **Why:** P3/T1 and the Rate-module rule (AGENTS.md §5) make the preview module the rate-bearing credit form; ruling 3/KB-10 fix the eight fields and the campaign translator form 「AI」; T7/KB-11/KB-12 (patterns commit `9c5e9079afb…`) require the JP credit module's DOM to be styled, and the R6 in-place form is unnecessary here because the base rule is left intact and a separate tail correction is added. The correction is a supplement, not an adaptation of someone else's translation, so no TASL adaptation line is owed. Commit anchors: FIX2-CREDIT `666f543` (field completion family), FIX5 head `435a6bb` (go-sign record).
- **Verify (from this repo alone):** `grep -n 'credit:start-preview\|credit:end-preview\|module Rate' review/sound-jp/candidate.txt` → L14/L23 and no Rate line; `grep -n 'creditButton' pages/theme:mox-jp.txt review/sound-jp/candidate.txt` → base L1711 vs candidate L608/L610; count the eight field labels in candidate L15–22.
- **Disposition:** Standing (the swap and the tail supplement). Credit author check from the brief: clean — the pointer names the evidenced author OxygenNine, where the original's own apparatus names nobody; no flag, no edit.

## 2. Includes and components

- IFTAGS (A): Tag localization (P2/T2, KB-08): iftags conditions use JP tag names in the JP environment.
  Verify: KB-08 recipe: every iftags condition names JP tags; a bare [[iftags]] line is an anomaly.
  - B3: orig 9-9 -> cand 11-11 (body -> body)

- COMPONENT-SWAP (B): Component swap to a JP port (T8, ruling 4): the campaign component candidate replaces the branch component it ports.
  Verify: The swapped target is in the campaign component inventory and exists on the check wiki.
  - B9: orig 23-23 -> cand 34-34 (body -> body)

- INCLUDE-REPOINT (A): foreign include repointed (P1, KB-15). [secondary labels of B22/B27]

- **What (this theme):** the include census is original 4 → candidate 6. B3 localizes the only gate (`[[iftags +版式 +原创]]` → `[[iftags +テーマ]]`, KB-08 clean — no bare `[[iftags]]`). B9 repoints the escaped install example `{{[[include :scp-wiki-cn:theme:sound]]}}` → `{{[[include theme:sound-jp]]}}` (orig L23 → cand L34); the bare `-jp` name is the working form on the check wikis (AGENTS.md §5), and usage examples must name `-jp` so copy-paste installs resolve. B22/B27 repoint the two `component:image-block` includes from `:scp-wiki-cn:` to `:scp-jp:` (orig L82/L97 → cand L91/L106) and re-host their asset names. The frame include at L1 is the bare campaign-candidate form `[[include component:interwiki-style]]`. No include in the candidate points at a `:scp-wiki:` page (grep-verifiable).
- **Why:** P1/P2/T8 and the include-form table (AGENTS.md §5) require the JP environment's own targets in working sources; the `-jp` posting suffix on self-references is the batch-posting convention (§6). The two image-block includes are *not* duplicates: each wraps a different asset.
- **Verify (from this repo alone):** `grep -n '\[\[include' review/sound-jp/candidate.txt` → L1, L14, L23, L34, L91, L106; `grep -c ':scp-wiki:' review/sound-jp/candidate.txt` → 0; read the gate at L11 against original L9.
- **Disposition:** Standing. No foreign include is kept, so no KB-54/KB-15 named exception is needed.

## 3. Delivery and code loading

- DELIVERY-HOST (A): Base/host repoint (P4/T9): deliveries are served from the JP hosts in this environment.
  Verify: Resolve the new host path; a kept old-host line is a class (ii) posting matter, recorded in section 11.
  - B1: orig 1-1 -> cand 1-4 (body -> body)
  - B2: orig 4-6 -> cand 7-8 (module-css -> module-css)

- SELF-DELIVERY (A): Own code-delivery import changed (P4): the page's own local--code delivery is its live CSS channel. [B1/B2]
- DRAFT-HOST (A): Draft-stage form (KB-41, class (iii)). [B1/B2/B11 + 27 further asset blocks]

- **What (this theme):** three delivery changes. (a) B1 drops the original's CN-only `ThemePreviewer` module (orig L1; the JP-side render check does not use it, per `sound.notes.md`) and adds the priority-1 interwiki-style frame (cand L1–4, `theme=` = own draft-host code `/2`). (b) B2 moves the base delivery: the original's head module @imports `theme:sound/code/2` (orig L5) and its stylesheet exhibit @imports `theme:mox/8` (orig L116); the candidate's head module instead @imports `theme:mox-jp/8` (cand L7) and its own code `/2` (cand L8) — the JP-fixed MOX base candidate (owner ruling 1 / KB-14), not the original branch base. The classifier filed the orig L116 change as B35 CSS-BODY in section 8; by mechanism it is this section's base-delivery move and is argued here. (c) **Navla2 landing:** the two self-delivery addresses now name `/2` (L3, L8). Before commit `fb43564` they named `/1`, the 653-byte variables exhibit, while the original delivered the stylesheet block `/2`. FIX-NAVLA2.md §4 records the census (/1 = L38–59, variables; /2 = L122–600, stylesheet), the two single-address changes, and the draft-host probe (/2 → HTTP 200, 15,802 B; old /1 → 651 B). The other @import on L7 (MOX base) is a cross-page reference and was deliberately left. (d) 31 draft-host asset/URL rewrites (`sigma10-jp-test.wdfiles.com/local--files/...`) carry class (iii)/(ii); they are the T1 baseline's pseudo-ref×31. Priority stack: a single `priority=1` frame, no duplicate and no dropped priority (KB-07 clean).
- **Why:** P4/T9 (JP host delivery), P6/T3 (own-code frame), ruling 1 (JP base port), KB-41 (draft-stage form); the navla2 repair is a delivery-address correction whose rationale is "deliver the block the original delivered", recorded with citation `FIX-NAVLA2.md` §4 / commit `fb435643733dfd93d8dfa698861e4a59921d8f0f`. Posting rewrites the draft host to `scp-jp.wdfiles.com` (class (ii)); the candidate is never "fixed" to pre-empt that.
- **Verify (from this repo alone):** `grep -n 'local--code/theme%3A' review/sound-jp/candidate.txt` → L3, L7, L8; compare with original L5 and L116; `git log -1 --format=%H -- pages/theme:sound-jp.txt` → `fb435643…`; read `R/review-scout/FIX-NAVLA2.md` §4 (vendored citation in the ledger context) and probe `/2` (200, 15,802 B).
- **Disposition:** the base/frame repoints stand as applied; the 31 draft-host lines are class (iii)/(ii) dispositioned in section 11; the navla2 `/1`→`/2` correction is recorded as provenance with its citation, not reopened.

## 4. Fonts and assets

- JPFONT-LOAD (A): JP font load added (P7/T5, KB-16): Japanese text needs a JP typeface loaded, and the resolved base may not load one.
  Verify: KB-16 recipe with base subtraction: the resolved base does not already load the family.
  - B33: orig at 113 -> cand 123-124 (body -> code-css)

- FONT-IMPORT (B): other font-load change (P5, KB-04). [primary secondary of B33]
- ASSET-REHOST-shaped draft-host rewrites: B11, B37–B61 and the image-block name lines (section 3).

- **What (this theme):** the original's CN font import (`fontsapi.zeoseven.com/403/main/result.css`, orig L118, host not on the P5 allowlist) is replaced by two Google Fonts imports at candidate L123–124: Noto Sans JP 400/700 + Oxygen Mono + Raleway 500/700, and Zen Maru Gothic 400/700. B36 replaces that original line in the stylesheet channel; the added Noto Sans JP load is B33. The three custom properties at L129–131 add JP fallbacks (`--mox-ui-font: 'Raleway', 'Noto Sans JP', …`, `--mox-text-font: 'Noto Sans JP', …`, `--mox-mono-font: 'Oxygen Mono', 'Noto Sans JP', …`), and the original's `'摇醒青年黑1.0'` (CN fan-made face) is replaced by `'Zen Maru Gothic'` at L444 and L478 (B62/B63) and in the usage specimen at L112, with the translator's note at L116 recording the substitution. Asset rewrites (projectfantasy.svg, 531k.jpg, icons-1.png, icons8-8416.png → draft-host `local--files`) are the class-(ii) deferred host condition. **Both directions:** every loaded family is named in a stack (or in the specimen line), and every named non-system family is loaded; `FontAwesome` is commented out (L136) and therefore inert. Base subtraction: `pages/theme:mox-jp.txt` L554 loads Noto Sans **SC**, not JP, so the JP load is a real supplement, not a duplicate. Probe: the Google Fonts URL → HTTP 200.
- **Why:** P5 restricts hotlinks to allowlisted hosts (fonts.googleapis.com is allowlisted; zeoseven is not); P7/T5/KB-16 require the JP face to be both loaded and named in stacks; KB-04's malformed-import family is avoided by the well-formed `+`-encoded family parameters. The CN display face cannot be served from the JP direct-link exception host, so the nearest rounded-gothic substitute is a documented porter judgment (P10 訳注), not a defect. Commit anchor: patterns `9c5e9079afb…` (KB-04/16 definitions); the substitution is recorded in `sound.notes.md` from the stage-2 CN14 lane (`12d839e`).
- **Verify (from this repo alone):** `grep -n '@import' review/sound-jp/candidate.txt` → L7, L8, L123, L124; `grep -n 'font-family\|--mox-.*-font' review/sound-jp/candidate.txt` → L112, L129–131, L136, L444, L478; `grep -n '@import' pages/theme:mox-jp.txt` → L3/L554/L556 (SC not JP); probe the L123 URL (200).
- **Disposition:** the font supplementation stands as applied; asset hosts are recorded as original-state/draft-form dispositions (section 11), never fixed in the candidate.

## 5. Header, sidebar, site furniture

The skeleton printed `none` here because no block's *primary* label maps to section 5; the theme does carry header and sidebar changes, argued from secondary labels and byte evidence.

- HEADERVAR (A): header/title variables (P9/T6, KB-57). [B11 — secondary name from the signature set]
- Class F mechanism (ledger item 85): sidebar toggle authored by the shared base.

- **What (this theme):** B11 re-hosts `--mox-header-logo` (orig L43 → cand L54) and translates the two header strings: `--mox-header-subtitle` 「遮蔽无形，统御虚幻」→「無形を覆い、幻影を統べる」 and `--mox-header-title` 「幻象计划」→「幻想計画」 (orig L44–45 → cand L55–56). Header/title language is out of scope for migration correctness under ruling 2 / KB-57; here it was translated, so no language disposition is owed. The header font substitution is argued in section 4. On the sidebar: neither the original nor the candidate defines a `.open-menu` toggle, `position: fixed`, or `z-index` rule of its own (grep on both files: none); the off-canvas sidebar and hover reveal are authored by the shared MOX base (`pages/theme:mox-jp.txt` L1212–1214 `.open-menu{display:none}`, L1228 `left:-22rem`, L1343 `div#side-bar:hover`). The candidate's own `#side-bar` rules (L365–411) are byte-identical to the original's (L332–377) after URL normalization (SHA-256 `784f9006eff26094d62bf287d78b0672bf2fee2bae0653467b35840f1f8f42b9` on both). This is the class-F mechanism, re-derived in the Per-theme record.
- **Why:** P9/T6 define the visible title surface; the missing toggle is the original-faithful MOX-base mechanism (ledger class F, re-judged DISPOSITIONED), not a candidate-side functional defect. The render lane's environment-layer subtitle/hotlink lines are not charged (AGENTS.md §3, KB-40).
- **Verify (from this repo alone):** read candidate L54–56 against original L43–45; `grep -n 'open-menu\|z-index\|left: *-22rem' review/sound-jp/candidate.txt review/sound-jp/original.txt` → no hits; read `pages/theme:mox-jp.txt` L1212/L1228/L1343; re-hash the two normalized sidebar windows as in the Per-theme record.
- **Disposition:** header translation standing; the sidebar-unreachable machine line is DISPOSITIONED as item 85 (section 11, Per-theme record), not fixed.

## 6. Text translation

- TRANSLATION-ANCHORED (B): Prose/usage translation (P10, KB-18): anchored pairs are one-to-one translations.
  Verify: Read the pairs; the anchors (leading token, CSS property, selector, heading level) confirm the pairing.
  - B5: orig 15-15 -> cand 26-26; B10: orig 25-25 -> cand 36-36; B12: orig 50-50 -> cand 61-61; B31: orig 108-108 -> cand 118-118; B32: orig 110-110 -> cand 120-120

- TRANS-UNANCHORED (C): Translation-shaped change without anchors (P10, KB-18). 25 blocks; resolved individually in the Appendix.
- GLYPH-FORM (B): shinjitai conversion (R5). [B10 「变量」→「変数」, B12 「示例」→「例」]
- COMMENT-TEXT (C): CSS comment translation (R1 porter-visible half). [B34 banner, B64 sidebar-fix comment; counted and skipped by design]
- CONTENT-STRING-shaped values: the `--mox-header-*` strings (section 5) are the R1 reader-visible half.

- **What (this theme):** the CN usage body is translated throughout: the 简介/示例/源代码 headings (B5/B12/B31), the `[[collapsible]]` labels (B32), the overview and install note (B6–B8), the modal and heading specimens (B13–B21), the story blurb (B23–B26) and the font/license notes (B28–B30). Two heading conversions are pure glyph-form (R5): CSS变量→CSS変数, 示例→例. In-CSS text is translated in place: the stylesheet banner (B34) and the sidebar-fix comment 「JP侧边栏暴力修复」→「JPサイドバー暴行修復」 (B64). **Recorded T5 residues:** the localize row (LOCALIZE-ROWS row 229, disp 1) counts two residual CN common-noun 「版式」 in the translated prose (candidate L28 「テーマ版式」, L30 「基础版式」/「MOX版式」) and one mistranslation in that comment (暴行 for 暴力, "brute-force"); the 原題 field (L18) keeps 「主题版式」 intentionally, as an original title. Both are minor, not display-affecting, and left byte-unchanged.
- **Why:** P10 is the port's purpose; the failure it prevents is a JP page whose instructions and specimens still read as the CN original. R1 is separated into reader-visible string values (charged by KB-18) and porter-visible comments (a known non-finding in the taxonomy's patterns feedback); R5 separates glyph-form changes from full translations.
- **Verify (from this repo alone):** read the pairs in `diff.md` (generated) or directly at the cited line numbers in `original.txt` / `candidate.txt`; `grep -n '版式\|暴行' review/sound-jp/candidate.txt` → L18, L28, L30, L595; the T5 note is in `review/AUTHORITIES/ledger-parts/LOCALIZE-ROWS.md` row 229.
- **Disposition:** Standing (the port itself). The two 「版式」 and the 暴行 comment are recorded at the source report's weight — not charged as migration defects, not edited.

## 7. Links

The skeleton printed `none` here; two link changes and one standing item sit here.

- LINK-REPOINT-shaped (P11). [B6/B7 — primary label TRANS-UNANCHORED]

- **What (this theme):** B6 converts the CN same-site story link `[[[kawaii-o5-3|这篇故事]]]` (orig L17) into the absolute `https://scp-wiki-cn.wikidot.com/kawaii-o5-3` with a （中国語） label (cand L28); B7 does the same for `[[[theme:mox|一氧化物III基础版式]]]` → `https://scp-wiki-cn.wikidot.com/theme:mox` (orig L19 → cand L30). Both targets are CN-only pages with no JP counterpart, so the absolute link to the serving original is the deliberate form (per `sound.notes.md`: "CN-only page → external link with（中国語）label; MOX theme link likewise"), not a missed repoint. The credit source link (cand L22) points back to the original page as ruling 3 requires.
- **Why:** P11 exists so a link does not die on the JP wiki; under the dead-reference evidence standard both targets were probed **HTTP 200** and serve today, so no ORIGINAL-DEFECT disposition or repoint is owed. Keeping a CN URL where no JP page exists is by-design, not a finding.
- **Verify (from this repo alone):** read candidate L28/L30/L22 against original L17/L19; probe the two `scp-wiki-cn.wikidot.com` URLs and the credit URL (all 200, recorded in the Standing checks table).
- **Disposition:** Standing, by design. No dead-link charge.

## 8. Structure

- EXHIBIT-RESTRUCTURE (C): Usage/sample exhibits dropped or replaced (R3): a sanctioned replacement and a silent deletion have the same diff shape; the ground must be stated.
  Verify: The exhibit-decision slot for this block, argued from the mirror.
  - B22: orig 82-84 -> cand 91-93; B27: orig 97-99 -> cand 106-108; B66: orig 574-580 -> cand 606-615 (body -> module-css)

- CSS-BODY (C): unclassified CSS content change. [B35 — delivery move argued in section 3; B62/B63 — font families argued in section 4]

- **What (this theme):** the localize.md closing rule is respected: same two code exhibits (`/1` variables L38–59, `/2` stylesheet L122–600), same collapsible, same selectors and variable names, substitutions made inline rather than appended. B22/B27 are the two image-block exhibits: their includes are repointed and their assets re-hosted, but both exhibits are intact (logo and header background). B66 is the only real exhibit decision: the original's trailing `[[include :scp-wiki-cn:component:interwiki-style | priority=1 | type=sidebar | theme=…mox/9 | css=…palette…]]` (orig L574–580) is dropped, and the candidate's tail credit-CSS module (L606–615) takes its place in the diff alignment.
- **Why:** the dropped include is *not* a mobile toggle mechanism — it carries the six palette variables (all already defined in the candidate's own `:root` at L41–52/L154–165) and styles sidebar appearance only; `sound.notes.md` records the deliberate stage-2 decision ("interwiki-style trailing block dropped (top-of-page include kept, basalt-jp pattern)"), and FIX5-CONTRB item 85 relies on the same fact. The replacement is a T7 credit-CSS supplement (section 1), not a replacement exhibit. R3's danger — a silent deletion of reader content — does not arise: no exhibit, sample, or rule set was lost. Commit anchors: stage2 CN14 `12d839e` (composition), FIX5 `435a6bb` (item 85 disposition).
- **Verify (from this repo alone):** read orig L574–580 against cand L606–615 and L41–52/L154–165; decode the `css=` parameter's `%3A/%23` escapes to recover the same palette values; `grep -n 'collapsible\|\[\[code type="CSS"\]' review/sound-jp/candidate.txt` → L38/L122/L120/L602.
- **Disposition:** Standing, with the exhibit-decision ground stated above. Nothing was silently dropped; the palette-only include is accounted for.

**Exhibit decision (explicit):** B22 replaced (include repointed to `:scp-jp:`, asset re-hosted, exhibit intact); B27 replaced (same); B66 dropped-with-ground (palette-only `type=sidebar` include, values already in the candidate, not a toggle) + independent T7 supplement added. There is no bare-Rate exhibit in this theme (the original's rate was bare and is deleted, section 1), so the labelled-pair exception does not arise.

## 9. Formatting only

- WS-ONLY blocks: 0
- Re-indentation: 0 blocks pair up after leading-whitespace normalization

No formatting-only change is charged. One residual boundary block (B65) is a single blank line before `[[/code]]` present in the original (L567) and absent in the candidate (at L600); it is a 1-line whitespace artifact of the classifier's block boundary, recorded in the Appendix R1 and disclosed here so the zero-WS-ONLY count is not misread as "no whitespace delta anywhere". R7 disclosure duty is otherwise not triggered.

## 10. Porter annotations

The skeleton printed `none`; there are two porter-side additions.

- **What:** (a) the translator's note at candidate L116 — `（訳注: 原語版のヘッダー／タイトル書体は「摇醒青年黑1.0」ですが、JPの直リンク特例ホストに同書体が無いため、近い丸ゴシック系のZen Maru Gothicに置き換えています。）` — recorded by the classifier as the unanchored translation block B30. (b) the stylesheet banner at candidate L126 — `/* sound-jp 固有の差分 CSS — MoX 基盤は theme:mox-jp/8 を @import で読み込みます。このファイルはその差分のみです。 */` — the B34 comment block, which documents the base-import/differential-layer split. Both have no original counterpart (the original has the CN font claim at L103–105 and a `/* MOX Include */` comment at L114).
- **Why:** P10 sanctions `**訳注:**` footnotes for original-side circumstances; a font unavailable on the JP exception host is exactly such a circumstance. The banner is an R2 editor line that makes the delivery topology auditable. Neither is original content, so neither may be mistaken for translation residue.
- **Verify (from this repo alone):** read candidate L112–116 against original L103–105 and candidate L126 against original L114.
- **Disposition:** Standing.

## 11. Dispositions and exceptions

No derived presence label fired (no kept foreign include, http, or old-BHL line). Every finding not fixed in the candidate is listed here with its class and evidence:

1. **§(e) item 84 [E], sample §15/§16 panel contrast — DISPOSITIONED (no edit).** The candidate's 25 MOX palette declarations are byte-identical to the original's (SHA-256 `28047aa9…` on both); the only added CSS block targets wiki-editor icons, not panels. Ground re-derived in the Per-theme record. [GOSIGN2-LEDGER-SUPPLEMENT item 84; FIX5-CONTRB §5; KB-28 original-identical branch]
2. **§(e) item 85 [F], missing mobile sidebar toggle — DISPOSITIONED (no edit).** The toggle is hidden by the shared MOX base (`.open-menu{display:none}`, `left:-22rem`, hover reveal); the candidate adds no toggle rule and its own sidebar rules match the original after URL normalization (SHA-256 `784f9006…` on both). Re-derived in the Per-theme record. [Supplement item 85; FIX5-CONTRB §5]
3. **31 × `pseudo-ref` (T1 baseline, row 261) — class (ii)/(iii).** Draft-host asset URLs and the two self-delivery addresses: (iii) at draft stage, rewritten to `scp-jp.wdfiles.com` at posting. Never fixed in the candidate.
4. **Sample credit-modal (render c2) — preview-form property**, uniform across themes using `credit:start-preview` which has no modal mechanism (GOSIGN-TESTS T2 amendment, 2026-11-16; KB-32). Not a theme defect.
5. **runtime-hotlink — environment layer.** `rokurolize.github.io`, `rsms.me`, `scp-wiki.wdfiles.com` arrive via the site theme's `sigma.min.css` @import chain (KB-40). The sample's extra host `indestructibletype-fonthosting.github.io` is **not present in the candidate source** (grep: 0) — recorded verbatim, not charged.
6. **Draft-bucket asset 404s** on `sigma10-jp-test.wdfiles.com/local--files/...` — campaign-wide deferred hosting (§4 no-re-uploads / KB-58), uploads owed before posting; not a display defect at draft stage.
7. **T5 minor residues** (two prose 「版式」, one 暴行 comment mistranslation) — recorded at the localize row's weight, not display-affecting and not charged (section 6).
8. **sources.tsv supersession note** — wrong in the ambrose shape; flagged in the Per-theme record, sources.tsv not edited.

## 12. Verification

- **T1 (source check):** recorded baseline 2026-11-16: exit 1, 31 errors / 0 warns / 1 info, all 31 `pseudo-ref` [T1-ROWS row 261], classes (ii)/(iii) in register c1. This package does not re-run the checker: the canonical invocation is `cd /home/roku/src/SCP-JP/claude-plugins-staff/plugins/scp-jp-staff/skills/theme-component-review && uv run scripts/check_source.py review/sound-jp/candidate.txt --kind theme --translation --check-links`; no candidate edit was made in this lane, so the recorded multiset stands.
- **T2/T3 (render):** combined verdict FINDINGS [RENDER-ROWS-G (CN14)], full engine coverage. The one candidate-adjacent item (sidebar) is item 85; the panel item is 84; the remainder are environment/coverage/preview-form items (section 11). No re-render was run for this package — the render record is cited, not re-measured.
- **T4 (follow-up diff):** the campaign artifact `diff-sound-from6.txt` reads `scp-wiki-cn:theme:sound rev6 → rev6 変更: なし` — no post-reference change; the mirror in this package is also the current original. (The `wd_revisions.py diff` form is `uv run scripts/wd_revisions.py diff https://scp-wiki-cn.wikidot.com/theme:sound --from 6` from the skill dir.)
- **T5 (translation text):** FINDINGS [LOCALIZE-ROWS row 229], jointly judged with T4; the recorded 1 display-affecting finding and the minor text residues are carried at their source weight (sections 6, 11).
- **This package:** `python3 review/classify_hunks.py review/sound-jp --repo .` → 66 blocks (41/24/1/0); `python3 review/classify_hunks.py --check review/sound-jp` → `OK: review/sound-jp classification is fresh`; `python3 review/build_review.py` regenerates `diff.md` and the verdict stamp; `python3 review/build_review.py --check` → all diff.md files up to date, all stamps up to date, citations resolve, vendored hashes match. The pristine base stale set (90 unrelated packages, captured before this package's build) is unchanged; `review/sound-jp` is **not** in the stale set. Count discrepancy is expected and stated: `diff.md` counts unified-diff hunks, the classifier counts change blocks; both derive from the same two files.

## Per-theme record

### Disposition 84 (class E) — byte-identity re-derivation

**The charge (ledger §(e) item 84, L1810):** "Sample section 15/16 panels: near-white text on light ground, effectively unreadable (render T3). KB-28 confirmed instance. No fix wave corrected a KB-28 binding and no original-faithful ground is recorded for these surfaces." Class E charges a candidate-side contrast binding, so the question is narrow: did the port change any colour value that feeds those panels?

Re-measured from this package's two files (not transcribed from the supplement):

1. **The MOX palette.** The twelve `--mox-theme-*`, `--mox-bg-color`, `--mox-text-color`, `--mox-layer-dark-1..3`, `--mox-layer-light-1..3`, `--mox-bgblur-front-color` declarations appear **twice per file** (variables exhibit and stylesheet `:root`) plus the `--mox-text-color: #ccc2c9` override (orig L387 / cand L420): **25 declarations on each side**, SHA-256 `28047aa965aeb72ce1a8da9de5fd3f8c01586ab3b4856ccdf37fc8d6a72fce65` on both. Original lines 30–41, 121–132, 387; candidate lines 41–52, 154–165, 420. Byte-identical.
2. **The only three deltas in the exhibit palette block** (orig L29–46 vs cand L40–57) are the header logo URL (asset re-host, class (ii)) and the two header strings (CN→JP translation, ruling 2/KB-57). No colour value moves.
3. **The only added CSS block** (cand L134–151, classifier B36) styles `:where(a.weditor-imagewiz, …)::after` — wiki-editor icon buttons — with `var(--mox-layer-light-1)` / `var(--mox-layer-dark-1)` and a re-hosted icon sprite. It does not select `p`, `panel-body`, `content-panel`, or any sample panel surface.
4. **No new layer.** The candidate introduces no other colour-bearing rule absent from the original on the charged surfaces; the font/asset/host changes are argued in sections 4 and 3 and do not alter a text/background pairing.

**Conclusion:** the rendered `rgb(...)` values that the T3 walk photographed as near-white-on-light are the original's own MOX palette composed on the shared sample's panel classes — a base/sample-construction interaction reproduced faithfully, not a port-introduced KB-28 binding. There is nothing to correct without departing from the original. **Disposition: DISPOSITIONED, no edit** [Supplement item 84; FIX5-CONTRB §5; patterns commit `9c5e9079afb01d30cb9fc4ef9d714e5591eb2ffa`].

### Disposition 85 (class F) — mechanism re-derivation

**The charge (ledger §(e) item 85, L1811):** "Sidebar-unreachable at 375/320 in both engines on page and sample; render T3 confirms the mobile sidebar toggle is missing. No fix, no disposition in the sources." Class F charges a candidate-side functional (sidebar/header) defect, so the question is: did the port remove or hide a toggle the original had?

Re-measured from this package's files and the vendored base candidate:

1. **Neither source defines the toggle.** `grep -n 'open-menu\|z-index\|left: *-22rem' review/sound-jp/original.txt review/sound-jp/candidate.txt` → **zero hits**. There is no candidate-side rule that hides `.open-menu a` and no candidate-side rule that could restore it.
2. **The base authors the behaviour.** `pages/theme:mox-jp.txt` L1212–1214 `.open-menu { display: none; }`, L1217–1228 `#side-bar { position: fixed; left: -22rem; z-index: 10; … }`, L1343 `div#side-bar:hover { left: 0rem; … }`: an off-canvas, hover-revealed sidebar with no JP toggle. The original imports the same base (`theme:mox/8`, orig L116); the candidate imports the JP port (`theme:mox-jp/8`, cand L7) under ruling 1. Both therefore reproduce the same mechanism.
3. **The candidate's own sidebar rules are unchanged.** Original L332–377 vs candidate L365–411, after normalising asset URLs to a constant, are byte-identical: SHA-256 `784f9006eff26094d62bf287d78b0672bf2fee2bae0653467b35840f1f8f42b9` on both windows. The port adds no competing sidebar rule.
4. **The dropped include is not a toggle.** The original's trailing `type=sidebar` include (orig L574–580) carries the six palette variables and sidebar appearance values; its `css=` parameter decodes to exactly the palette already in the candidate's `:root`. Its removal cannot create or remove an `.open-menu` control. The companion MOX-derived theme `theme:starry-jp` shows the same machine line, confirming the cross-cutting base shape.

**Conclusion:** the missing toggle is the MOX base's own off-canvas/hover design, faithfully reproduced by both the original and the candidate; there is no candidate-side cause to fix. **Disposition: DISPOSITIONED, no edit** [Supplement item 85; FIX5-CONTRB §5].

### Second-reviewer walk (third-party perspective)

A reviewer who did not trust the FIX5 lane should be able to refuse every premise and still reach the dispositions from the two files in this package. The walk that was actually performed:

1. *"Maybe the port introduced the unreadable panels."* → Extract the 25 palette declarations from both files and hash them; identical (`28047aa9…`). The only added block is editor-icon CSS (L134–151). No candidate-side contrast change exists. Walk result: premise refused.
2. *"Maybe the port hid the toggle."* → Grep both files for `open-menu`/`z-index`/`left:-22rem`: zero hits in both; the hiding rule lives in the shared base at a named line (`mox-jp.txt` L1212–1214). The candidate's own sidebar window matches the original after URL normalization (`784f9006…`). Walk result: premise refused.
3. *"Maybe the dropped `type=sidebar` include was the toggle."* → Its `css=` parameter decodes to palette values only, all present in the candidate's `:root`; no markup or JS toggle is in that include. `sound.notes.md` records it as a deliberate palette-only drop. Walk result: premise refused.
4. *"Maybe the post-verdict `fb43564` edit invalidates the dispositions."* → `fb43564` changes exactly two lines (L3, L8), both self-delivery addresses `/1`→`/2` (FIX-NAVLA2 §4). The disposition evidence sits in L41–52, L134–165, L365–411 and the palette declarations — none of those lines is in the navla2 diff. The stamp's STALE banner is a commit-provenance artifact, not a defect. Walk result: no effect.
5. *"Maybe the mirror is not the original at the reference revision."* → `diff-sound-from6.txt` records `rev6 → rev6 変更: なし`, and the candidate's reference-revision field (L21) is 6. The mirror is the right and current original. Walk result: premise refused.

All five probes are executable with the two package files plus the vendored base candidate and the cited campaign record; no live render was needed to re-derive the dispositions.

### Record discrepancies flagged by this package

The package follows the bytes and the primary rows; it does not edit the prose records.

1. **sources.tsv's supersession note is wrong in the ambrose shape.** The note for `sound-jp` says "original superseded upstream since the reference revision" (K5a-i) and cites `diff-sound-from6.txt`. The artifact's actual content is `scp-wiki-cn:theme:sound rev6 → rev6  変更: なし` — **no change; upstream is still the reference revision rev 6**. The note keys on the artifact's existence, not its content, exactly as EXEMPLAR-AMBROSE §Acceptance(1) records for `ambrose-chapter-two` (rev19→rev19). **Correct form for this row:** "follow-up diff artifact `diff-sound-from6.txt` records rev6 → rev6, no changes; upstream latest is still the reference revision (the earlier superseded-upstream note was wrong)". sources.tsv was **not** edited; this is recorded here and in the batch report.
2. **"Base inlined" prose vs current bytes.** The stage-2 `sound.notes.md` ("Mox … inlined into the candidate as the bulk of code/1"; "Top module @imports …/1") and FIX5-CONTRB §5's parenthetical ("base inlined from theme:mox/8") describe an earlier composition. The current bytes deliver the base by @import (`theme:mox-jp/8`, candidate L7) and the sound differential layer at `/2` (L122–600, banner L126); `/1` is the 653-byte variables exhibit (L38–59), which is why navla2 repointed delivery to `/2`. The disposition substance (palette parity, base-authored toggle) is unaffected; the composition prose is stale.
3. **Classifier B66 mixes two mechanisms.** The EXHIBIT-RESTRUCTURE label fired on the dropped palette-only include, while the added side (L606–615) is a T7 credit-CSS supplement. Section 8 separates the two; no exhibit content was lost.
4. **Stamp STALE vs go-sign PASS.** The stamp faithfully reports a post-verdict commit; the go-sign verdict describes the pre-change file, and the only change is the delivery-address repair (walk step 4). Not a contradiction in substance.

### Multi-wave provenance

The candidate's state is the product of successive waves: stage-2 CN14 (`12d839e`, translation/composition) produced the port; FIX2-CREDIT (`666f543`) completed the eight credit fields; FIX5-CONTRB (no edit, recorded at `435a6bb`) closed items 84/85 as dispositions; and the navla2 landing (`fb43564`) corrected the two self-delivery addresses. Citations in place of a changelog: GOSIGN2-LEDGER.md §(b) row 230, §(c2) c2 block, §(c3) c3 line, §(e) items 84–85; GOSIGN2-LEDGER-SUPPLEMENT.md items 84–85; REPORT-GOSIGN2-FIX5-CONTRB.md §5; FIX-NAVLA2.md §4; COMPLETION-REPORT.md §10.

## Appendix — residue blocks

### Residue R1 — B65 (residue; orig 567-567 -> cand at 600, code-css -> body)
- Both sides' first lines are blank; the block is the single blank line before `[[/code]]` present in the original (L567) and absent in the candidate (at L600).
- Resolution: section 9 — a 1-line whitespace boundary artifact of the classifier, no content; not a display change and not an R7 re-indentation. Recorded so the zero WS-ONLY count is not misread.

### Residue R2 — B6 (heuristic; orig 17-17 -> cand 28-28, body -> body)
- CN overview/install prose → JP.
- Resolution: section 6, class P10. The link form change (same-site → absolute CN URL) is argued in section 7; the classifier left the block unanchored because no leading token anchors a two-line prose paragraph.

### Residue R3 — B7 (heuristic; orig 19-19 -> cand 30-30, body -> body)
- CN MOX-base description → JP, with `[[[theme:mox|…]]]` → absolute CN URL.
- Resolution: sections 6/7, classes P10/P11. One-to-one translation; the link is to a CN-only page (dead-reference probe 200).

### Residue R4 — B8 (heuristic; orig 21-21 -> cand 32-32, body -> body)
- "我差点忘了写该怎么引用版式了…" → install-note JP prose.
- Resolution: section 6, class P10. The escaped install example itself is B9 (section 2).

### Residue R5 — B13 (heuristic; orig 52-52 -> cand 63-63, body -> body)
- "> 引用块" → "> 引用ブロック".
- Resolution: section 6, class P10; the leading `>` quote marker is the anchor the majority rule missed.

### Residue R6 — B14 (heuristic; orig 56-57 -> cand 67-67, body -> body)
- Modal specimen prose CN → JP.
- Resolution: section 6, class P10; specimen text translated in place.

### Residue R7 — B15 (heuristic; orig at 61 -> cand 71-71, body -> body)
- Added `[ [collapsible show="見出し"] ]` opener (candidate L71).
- Resolution: section 6, class P10. The original's collapsible opener at L62 is aligned with the candidate's heading at L73 by the differ; the real pairing is opener-to-opener (orig L62 → cand L71), a block-boundary artefact, no content lost.

### Residue R8 — B16 (heuristic; orig 62-62 -> cand 73-73, body -> body)
- Original collapsible opener → candidate first heading "1級見出し".
- Resolution: section 6, class P10; see R7 — the classifier's pairing is offset by one line, the specimen content is intact.

### Residues R9–R13 — B17–B21 (heuristic; heading levels 2–6, orig 64-74 -> cand 75-83)
- "2级标题"…"6级标题" → "2級見出し"…"6級見出し".
- Resolution: section 6, class P10 (with the same one-line offset as R7/R8). The heading-level specimens are all present; one CN heading per level translated one-to-one.

### Residue R14 — B23 (heuristic; orig 89-89 -> cand 98-98, body -> body)
- Story-blurb paragraph 1 CN → JP.
- Resolution: section 6, class P10; in-universe proper nouns (O5-3, SCP) intentionally retained.

### Residues R15–R17 — B24–B26 (heuristic; orig 91-95 -> cand 100-104, body -> body)
- Story-blurb paragraphs 2–4 CN → JP.
- Resolution: section 6, class P10; one-to-one translation of the sample prose.

### Residue R18 — B28 (heuristic; orig 103-103 -> cand 112-112, body -> body)
- Font specimen line: 摇醒青年黑 → Zen Maru Gothic (with `[[size]]`/`[[span]]` markup preserved).
- Resolution: sections 4/6, classes P7/P10; the R2 translator's note for the substitution is B30.

### Residue R19 — B29 (heuristic; orig 105-105 -> cand 114-114, body -> body)
- "版头图片为自制，遵循CC-BY-SA 4.0协议" → JP CC-BY-SA notice.
- Resolution: section 6, class P10; TASL-adjacent visible text, translated.

### Residue R20 — B30 (heuristic; orig at 107 -> cand 116-116, body -> body)
- Added `[ [訳注: …] ]` font-substitution note.
- Resolution: section 10, class R2 (porter annotation, P10 訳注); not original content.

### Residue R21 — B34 (heuristic; orig 114-114 -> cand 126-126, code-css -> code-css)
- `/* MOX Include */` → the sound-jp differential-CSS banner.
- Resolution: section 10, class R2 (porter editor line). Its claim that the base is @imported is verified by candidate L7, so it is accurate current-state documentation (cf. discrepancy 2).

### Residue R22 — B35 (heuristic; orig 116-116 -> cand 128-132, code-css -> code-css)
- The original's in-code `theme:mox/8` @import → the candidate's three JP font-stack custom properties.
- Resolution: section 3 (base delivery moved to head-module L7) + section 4 (JP font stacks). The classifier's "no other signature matched" note is expected: two mechanisms were compressed into one alignment block. No CSS body was lost.

### Residues R23–R24 — B62/B63 (heuristic; orig 411/445 -> cand 444/478, code-css -> code-css)
- `font-family: '摇醒青年黑1.0'` → `'Zen Maru Gothic'`.
- Resolution: section 4, classes P7/P10; the JP substitute face is loaded at L124 and named in the specimen at L112 (both-directions check clean).

### Residue R25 — B64 (heuristic; orig 562-562 -> cand 595-595, code-css -> code-css)
- `/* JP侧边栏暴力修复 */` → `/* JPサイドバー暴行修復 */`.
- Resolution: section 6, class R1 (porter-visible comment); comments never render, so the 暴行 mistranslation is a T5 minor residue (section 6), not a display defect. No KB entry proposed.

## License and attribution

- **Title:** 虚拟之音 主题版式
- **Author:** OxygenNine
- **Source:** https://scp-wiki-cn.wikidot.com/theme:sound — revision 6
- **License:** Creative Commons Attribution-ShareAlike 3.0 (CC BY-SA 3.0) — license deed: https://creativecommons.org/licenses/by-sa/3.0/
- **Adaptation:** This package holds a Sigma-10 migration port of the work; changes were made. See "Summary" and "Standing sections" in this README for what changed and why. Translator: AI (Muse and its delegated agents), per the campaign's standing attribution rule.
