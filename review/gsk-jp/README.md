# Review package — theme:gsk-jp (CN → JP port)

<!-- BEGIN GENERATED VERDICT STAMP — do not hand-edit; regenerate with review/build_review.py -->
## Verdict stamp
- Theme: theme:gsk-jp — origin CN, population #195 [GOSIGN2-LEDGER (b) row 195]
- Overall: STALE — candidate file changed since the verdict was computed (verdict against 435a6bb-era content, file sha256 now 1f48167077485be5f9f4c44a536d6eb02ab5c55be5485d56928973f5d2c3b245); verdict not carried over, re-judgement required
> verdicts below describe the pre-change file
- T1 (source check): FINDINGS (classified) — baseline 2026-11-16: exit 1, 11 errors / 4 warns / 1 info (pseudo-ref×11); standing classes dispositioned in register c1 [T1-ROWS row 178; GOSIGN2-LEDGER (b) row 195]
- T2/T3 (render, combined verdict): FINDINGS — [combined T2/T3] report `FINDINGS` — page runtime-hotlink site-theme chain only; sample credit-modal (preview-form), page-overflow 337px@320 + 389px@375 chromium and 416px@320 + 419px@375 webkit (cross-cutting static-credit), runtime-hotlink site-theme chain + sample font host; T3 clean on both pages; the original sample webkit 320x640 capture was a transient 503 (http.cat + hidden-* block), re-run once per rule 2 and the fresh capture carries no 503 signature; site-logo.png 404 (broken alt-text header logo clipped at mobile) = deferred asset. [RENDER-ROWS-RERUN16 (CN7) — supersedes the RENDER-ROWS-2 row for this theme, rule S1]
- Engine coverage: full (chromium+webkit, both pages) [RENDER-ROWS-RERUN16 (CN7)]
- Credit modal: sample credit-modal errors dispositioned preview-form (credit:start-preview has no modal mechanism; GOSIGN-TESTS T2 amendment, 2026-11-16) [RENDER-ROWS-RERUN16 row]
- T4 (localize patterns + follow-up): FINDINGS — display-affecting findings: 3 [LOCALIZE-ROWS row 194, source LOCALIZE-S2-D]
- T5 (translation text): FINDINGS — the source reports judge T4/T5 jointly; one verdict word covers both [LOCALIZE-ROWS row 194]
- FIX5 re-judgement: none — no OPEN items at the ledger determination [GOSIGN2-LEDGER (b) row 195]
- Computed against: canonical commit b5cb7241f527a44933e45599b41df210690771c4; candidate file pages/theme:gsk-jp.txt sha256:1f48167077485be5f9f4c44a536d6eb02ab5c55be5485d56928973f5d2c3b245; record: GOSIGN2-LEDGER.md + GOSIGN2-LEDGER-SUPPLEMENT.md as of the FIX5 head 435a6bb
<!-- END GENERATED VERDICT STAMP -->

## Status

| | |
|---|---|
| Verdict | **PASS** — passed at the ledger determination; this theme had no OPEN items and no §(e) register entry (GOSIGN2-LEDGER (b) row 195) |
| Standing items | **DISPOSITIONED** — T1 pseudo-ref ×11; the rerun render row's items (section 11); P7 (font loads unreferenced, T4 bar), P9 (language-variant header blocks, ruling 2), P11 (sibling-page links). **Two defect flags from this package:** the base theme and this theme are named without their `-jp` suffix in four places (candidate L48, L54, L55, L163), and the exhibit banner declares a base delivery (code files 1 and 2) the bytes make only in part (candidate L173–175 against L4 and L18; per-theme record) |
| Go-sign basis | COMPLETION-REPORT.md §10 (go-sign issued; 81 FIXED / 26 DISPOSITIONED / 0 OPEN across the sweep) |
| Named exception | None for this theme (the sweep's single named exception is theme:amethyst-v2, which has no candidate) |

## Provenance

| | Original | Candidate |
|---|---|---|
| Page | theme:gsk | theme:gsk-jp |
| Wiki | scp-wiki-cn.wikidot.com | SCP-JP Sigma-10 candidate (canonical repo) |
| Reference revision | 7 (the candidate's credit block records 初訳時参照リビジョン: 7) | — |
| Source of this copy | Campaign cache `gosign2-lanes/lane-oc-gs-localize-s2-D/orig-gsk.txt`, via the mirror store (class COPY, hash-verified against review/sources.tsv) | Canonical file `pages/theme:gsk-jp.txt`, copied at worktree HEAD f9cae19 |
| Lines / bytes | 565 lines / 17,077 bytes | 600 lines / 19,849 bytes |
| SHA-256 | a982cfefc8a50ed7a4c1ea8ef8d47e4d9c7cabf6c54cf8ec00dfa2f5c | 071e86657e725613989d6686725bccc23b60a8101d267b6313336b8911c55cd3 |

Wave history (git log for the candidate file): created by the Stage 2 CN7 integration (6d745e5); rework2-p2 (c65ec92) swapped its embedded base for references; FIX-CREDIT-D (1869877) normalized the credit block's translator field; FIX4-IWA (8c62b7b) is in its history; and the last commit touching the file, FIX4-IWB (5559209, the stamp's computed-against commit), adjudicated its frame priorities (section 3). The original has been superseded upstream since revision 7; the campaign's follow-up diff artifact is diff-gsk-from7.txt (class K5a-i). The port layers over theme:jakstyle-jp (sources.tsv kind: K5b-3); this package's diff covers the theme's own layer only, and the base's delivery is read through the resolved base where a section says so.

## Summary

A project skin (for the CN branch's GSK project and Site-514) built as a thin layer over Black Highlighter and the CN jakstyle theme: a small variable layer, a full specimen body, and its CSS carried twice on the original page, once as a display exhibit and once as the live module. The port consolidates that delivery into the JP BHL form (a base include, a head module importing the JP base's block 1 and its own block 1, a four-frame interwiki-style stack, and one code block that is both the exhibit and the delivery), translates the specimen entire (including the original specimen's own repeated lines, translated as found), and adds a license box the original never carried. The T4 lane charged this theme more heavily than most (three display-affecting findings), and each charge has a visible outcome in the bytes or an adjudication on record: the frame duplication was adjudicated by a dedicated wave (FIX4-IWB), the font and header-language items are dispositioned, and the sibling-page links are the standing P11 class. Two flags arise from this package's own checks (per-theme record). Measured churn (diff.md, the generator's difflib count with autojunk off: +191/−163 in 58 change blocks); the count is inflated by the delivery consolidation, which re-sites the whole CSS layer (section 8).

## Class summary

Auto-classification by review/classify_hunks.py (signature table 2026-11-17.1): 58 change blocks — 24 specific (41.4%), 31 heuristic (53.4%), 3 residue, 0 skipped. Pattern citations below name the KB entry; the patterns/ tree state cited throughout is commit 9c5e9079afb01d30cb9fc4ef9d714e5591eb2ffa.

| Label | Blocks |
|---|---|
| TRANS-UNANCHORED | 35 |
| TRANSLATION-ANCHORED | 12 |
| DRAFT-HOST | 8 |
| DELIVERY-MOVE | 6 |
| EXHIBIT-RESTRUCTURE | 6 |
| HEADERVAR | 4 |
| IFTAGS | 2 |
| INCLUDE-REPOINT | 2 |
| SELF-DELIVERY | 2 |
| BARE-RATE-DEL | 1 |
| COMMENT-TEXT | 1 |
| CREDIT-PREVIEW | 1 |
| CSS-BODY | 1 |
| DELIVERY-HOST | 1 |
| ESCAPED-INCLUDE | 1 |
| JPFONT-LOAD | 1 |
| LICENSE-BOX | 1 |
| RESTORATION | 1 |
| TASL-FIELDS | 1 |

Adjudication for this README (every block was read against the bytes): the six DELIVERY-MOVE and six EXHIBIT-RESTRUCTURE primaries are the delivery consolidation of section 8, not six separate events; the RESTORATION primary (B50) is the classifier's name for the same consolidation's main block. The 35 TRANS-UNANCHORED blocks are the specimen translation (section 6), each verified line by line, including the original's repeated specimen lines. After adjudication no block is left unexplained.

## Standing sections

### 0. Header and provenance frame

- **What:** Theme theme:gsk-jp; original theme:gsk on scp-wiki-cn at reference revision 7; candidate `pages/theme:gsk-jp.txt`. Provenance route: derived from the original at the reference revision by the CN7 wave (sources.tsv kind: K5b-3, layer theme over a ported base; no production JP counterpart exists for this theme, so the R4 adoption question does not arise). The theme's anatomy decides how the diff reads: it is a variable layer over two bases (Black Highlighter directly, jakstyle as its working base), its body is a specimen, and its CSS exists on the original page in two copies (section 8).
- **Why:** Section 0 declares the provenance route so every later count is read against the right baseline; the layer anatomy decides sections 3 and 8.
- **Verify:** The sources.tsv row for gsk-jp; `sha256sum original.txt` against the Provenance table.
- **Disposition:** Standing (the route itself); the layering is recorded in section 3.

### 1. Credit and attribution

- **What:** The original's credit furniture is a right-aligned block (original L16–26): the label **评分：**, a bare `[[module Rate]]`, the label **评分模块与著作信息模块：**, and the CN credit trio (`:scp-wiki-cn:credit:start` / `more` / `end` with their 页面信息 / 更多页面信息 link texts). The candidate deletes the trio and the bare Rate (block B6) and installs the JP form inside its `[[iftags +テーマ]]` gate: a `:scp-jp:credit:start-preview`/`end-preview` block (candidate L26–35) carrying the eight ruling-3 fields (title GSKプロジェクト テーマ; 翻訳責任者 AI; 翻訳年 2026; 原題 GSK项目主题版式; 著作権者 in the same-creator form, "原語版ページの作成者に同じ（scp-wiki-cn の theme:gsk）"; 作成年 2022; 初訳時参照リビジョン 7; the source link, section 7). The same-creator form is exact here, not a gap: the original names no individual author anywhere (no banner, no info block, no license box — its prose credits the two base themes, not a person), so the field drops nobody. Two additions ride with the section. The two furniture labels survive the modules they headed: **評価：** (candidate L44) now stands over nothing (the Rate it labeled is inside the credit module), and **評価モジュールと著作情報モジュール：** (candidate L46) heads the intro prose — the T4 lane charged both as orphan labels (LOCALIZE-ROWS row 194), and they stand in the candidate as charged; they cost a reader a moment's confusion and nothing else. And the candidate adds a license box the original never carried (block B57, candidate L593–599): a `:scp-jp:component:license-box-backend` pair whose note states that image and font sources follow the original theme:gsk's record, that externally hosted attachments were re-hosted onto the candidate page, and that images with no license notation in the original need author confirmation before posting.
- **Why:** P3/T1 (KB-09) for the swap (the preview module is rate-bearing; the CN trio is ledger class C residue); ruling 3 for the fields. The license-box addition is porter hygiene of the same family: the theme re-hosts assets (section 4), and the box records the terms under which it does so.
- **Verify:** `grep -n 'module Rate\|credit:start' candidate.txt` returns only the preview pair; read candidate L26–35 against the eight fields, L44–49 against original L16–29, and L593–599 for the added box.
- **Disposition:** Swap standing; labels charged by T4 and retained as charged (minor, recorded here); license box added by the port.

### 2. Includes and components

- **What:** The include census divides four ways. (1) The base include: the candidate opens with `[[include :scp-jp:theme:black-highlighter-theme]]` (candidate L1), the Sigma-10 base include of the JP BHL form; the original has no counterpart line (its BHL arrived by direct @import from the CN mirror host, section 3). (2) Subsumed by the base: the original's two furniture components, `:scp-wiki:component:centered-header-bhl` and `:scp-wiki:component:toggle-sidebar-bhl` (original L352–353), have no counterpart lines in the candidate, because theme:jakstyle-jp carries both itself (its L885–886, in the `:scp-jp:` form) and this theme's chain includes that base — a layer theme does not re-include what its base includes. (3) A declared omission: the original's usage snippet leads with `:scp-wiki:component:fade-in` (original L32, explained at L37); SCP-JP has no such component, so the candidate omits it from the snippet and says so twice, in two near-duplicate translator's notes (candidate L52 and L57, section 10). (4) Flagged: the base and self names inside the prose, the snippet, and the exhibit example (candidate L48, L54, L55, L163) name theme:jakstyle and theme:gsk without the `-jp` suffix (per-theme record).
- **Why:** P1 (KB-15): includes and references name the JP page that actually exists; item (2) is the same rule's other side (a reference the base already makes is not duplicated), and item (3) is a component with no JP counterpart, handled by declaration rather than by a dangling include.
- **Verify:** `grep -n '\[\[include' candidate.txt` against original.txt's list; `grep -n 'centered-header' pages/theme:jakstyle-jp.txt` (L885–886).
- **Disposition:** Repoints and subsumption applied; the fade-in omission declared in-file; the name references are the package's first defect flag.

### 3. Delivery and code loading

- **What:** The original's delivery is spread over five mechanisms: a head module importing normalize and black-highlighter from the CN mirror host (bhl.scpwikicn.com, original L2–5), a sidebar frame delivering the CN interwiki style sheet (frame A, original L7–12), a mid-page module importing jakstyle's block 1 from scp-wiki-cn.wdfiles.com (original L354–356), a second frame delivering jakstyle's block 2 (frame B, original L358–362), and the live variable module (original L363–565). The candidate consolidates to the JP BHL form: the base include (section 2); a head module importing jakstyle-jp's block 1 and its own block 1, both from the draft host (candidate L3–6); and the frame stack below. **Frame paragraph (the M-frame addition):** the candidate carries five interwiki-style frames. Four form the standard stack at candidate L8–23 (priority 1: normalize.min.css; 2: black-highlighter.min.css, both from scp-jp.github.io; 3: jakstyle-jp/1; 4: own /1, both from the draft host) — the stack is present and verified against the bytes, in the BHL family's split form. The fifth (candidate L37–42, below the credit block) is not a wave addition but the original's own frame A carried over: the same override=1, type=sidebar shape, its `theme=` repointed from the CN interwiki sheet to the JP BHL sheet (block B3), and its priority renumbered. The T4 lane charged exactly this frame as a duplication with a priority-2 conflict (LOCALIZE-ROWS row 194, its top fix target). The charge was adjudicated by a dedicated wave: FIX4-IWB (commit 5559209, "interwiki-style priority adjudications (KB-07)") records "gsk sidebar override aligned to its BHL leg" and its diff moves this frame's priority from 1 to 2, deliberately aligning the sidebar override with the head stack's BHL leg (candidate L12–15, also priority 2) that it overrides, later in document order so the override wins its cascade. The ledger records the outcome as P6 FIXED. The original's frame B (jakstyle block 2) has no counterpart frame: the JP base's consumer delivery is its block 1 alone (theme:jakstyle-jp's own frame names /1), so block 2 has no JP delivery to repoint to — which is also the context for the banner flag in the per-theme record. The head module's two @imports and frames 3–4 deliver the same two blocks by both mechanisms, the BHL family's belt-and-braces form, as in the base's own page.
- **Why:** P4/T9 for the delivery repoints (CN mirror and branch hosts to the JP hosts); P6/T3 (KB-07) for the frame stack, with KB-07's priority adjudication (FIX4-IWB) deciding the fifth frame's number. A frame count read without the adjudication record looks like a defect; with it, it is the decided form.
- **Verify:** Read candidate L1–42 against original L1–12 and L352–362; `git show 5559209 -- pages/theme:gsk-jp.txt` shows the one-line adjudication; `grep -n 'interwiki-style' pages/theme:jakstyle-jp.txt` shows the base's own /1 contract.
- **Disposition:** FIXED (P6, by the FIX4 waves with the IWB adjudication on record).

### 4. Fonts and assets

- **What:** Fonts, in the state the T4 lane charged and the ledger dispositioned. The port added two JP font loads to the exhibit (block B50's JPFONT-LOAD span, candidate L177–178: Noto Sans JP and Noto Serif JP from Google Fonts). No stack in the candidate references either face: the layer's four font variables, in both variable sets, name `'Times New Roman', '黑体'` (candidate L272–275 and L481–484), carried from the original, so the CJK fallback a JP reader's machine is offered is SimHei, a Chinese system font, and the loaded JP faces are decorative. The T4 lane charged this as 型 7 (a JP font declared but unreferenced); the ledger dispositions it P7 DISPOSITIONED, the row carrying no display-affecting mark for it (the theme renders through its variables and the base's stacks, and the sweep's bar for a P7 fix is a display effect). The bytes stand as charged, and this package records them so the disposition is read against the fact, not instead of it. Assets: the logo variables' URLs repoint from the CN sandbox host (scpsandboxcn.wikidot.com, eastcountry-center) to the candidate's own draft-host file area, name unchanged (site-logo.png; blocks B51–B54, four lines across the two variable sets), and the specimen's image-block example repoints the same way (candidate L61). The rerun render row records site-logo.png as a 404 on the draft host, a deferred asset: the header logo the variables name is not yet among the candidate's uploaded files.
- **Why:** P7/T5 with KB-16 states the completed form (load and stacks change together); this theme's P7 is the dispositioned incomplete form, recorded under its disposition. P5/KB-17 for the asset re-hosting; a re-hosted name whose file is not yet uploaded is the deferred-asset state the rerun row records.
- **Verify:** `grep -n 'Noto' candidate.txt` returns only L177–178; `grep -n '黑体' candidate.txt` returns the variable lines; the rerun row (RENDER-ROWS-RERUN16, CN7) records the logo's 404.
- **Disposition:** DISPOSITIONED (P7 at the T4 bar); the logo file is a deferred asset on the render record.

### 5. Header, sidebar, and site furniture

- **What:** Header variables (HEADERVAR spans in blocks B50–B53): the default `:root` set keeps the original's English header strings by the original's own design — `--header-title: "GSK Project"`, `--header-subtitle: "Supervise, Cooperation, Protect"` (candidate L182–184, carried from original L365–366, whose own comment notes the lines are for English readers). The two `:root:lang(cn)` variant blocks survive in both variable sets (candidate L261–266 and L470–475), setting the Chinese title and subtitle and the repointed logo URLs: on scp-jp (lang=ja) they never match, so they are inert, and the T4 lane charged their retention as 型 9. The ledger dispositions the class P9 DISPOSITIONED (ruling 2: header and title language is out of scope for migration correctness, and a language-variant block is the original's mechanism, not a leftover). The sidebar furniture is the base's (section 2, item 2); the frame that styles it is section 3's fifth frame. The orphan credit labels are recorded in section 1.
- **Why:** Ruling 2 and P9 for the language variants; P8 for the furniture subsumption.
- **Verify:** Read candidate L180–186, L261–266, L470–475 against original L363–367 and L443–447.
- **Disposition:** DISPOSITIONED (P9); furniture standing via the base.

### 6. Text translation

- **What:** The specimen body is translated entire: 12 TRANSLATION-ANCHORED and 35 TRANS-UNANCHORED primary blocks (B5–B49), each verified line by line — the intro prose, the usage instructions, the heading/collapsible/tab/table specimens, and the closing sections. Two specimen facts a reviewer should know. First, the translation is faithful to the original's own accidents: the original's tab specimen repeats one line eight times (original L83–99, a copy-paste stutter) and an empty-tab label five times, and the candidate translates every repetition (candidate L101–119, L121–129) rather than silently tidying the specimen — the specimen is evidence of what the theme renders, and the port does not edit the evidence. Second, one specimen line is localized, not translated: the example link's target changes from baidu.com to google.com with its sentence (block B14's zone, candidate L65), the CN search-engine example replaced by the one a JP reader has visited. The two translator's notes about the omitted fade-in component are porter annotations (section 10), counted there, not here. Simplified Chinese survives in the candidate only where it is data: the credit block's original-title field (candidate L30), the `:lang(cn)` variant blocks (section 5), the exhibit banner's title line, and the original's English-readers comment inside the carried `:root` (candidate L185).
- **Why:** P10 (the specimen is the theme's documentation of itself; translating it entire is the port's purpose) and KB-18 (reader-visible strings). The stutter's faithful carry follows the same rule as a specimen's content anywhere: the port translates the page that exists.
- **Verify:** The pairs are diff.md's body sections in order; a Hanzi scan of candidate.txt returns only the survivals listed.
- **Disposition:** Standing (the port itself).

### 7. Links

- **What:** Three link matters. (1) The credit block's source link (candidate L34) names `https://scp-wiki-cn.wikidot.com/theme:gsk` — the original's recorded host (review/sources.tsv), so it names the serving original and no host defect arises. (2) The intro's prose links: the original's absolute CN URLs (original L28–29) become unprefixed relative links (candidate L48–49): `theme:black-highlighter-theme` resolves (a production JP page), while `theme:jakstyle`, `gsk-center`, and `site-514` name pages scp-jp does not have — the T4 lane charged the hub link as 型 11, and the ledger dispositions the class P11 DISPOSITIONED (sibling/batch-posting). The jakstyle instance differs from the hub instances in one respect: its correct target exists in this campaign (theme:jakstyle-jp), so it is counted in the per-theme record's flag rather than left inside the P11 class. (3) The specimen's example link (baidu → google) is a content localization, recorded in section 6.
- **Why:** P11 under the dead-reference evidence standard for items (1) and (2)'s hub pair; P1 for the jakstyle reference.
- **Verify:** Compare candidate L34's host against the sources.tsv row's original_url host (scp-wiki-cn.wikidot.com) — identical; read candidate L48–49 against original L28–29.
- **Disposition:** DISPOSITIONED (P11, hub links); the jakstyle prose link is inside the per-theme record's flag.

### 8. Structure

- **What:** One consolidation, declared by the topology pass. The original carries its CSS twice: a display exhibit (`[[code]]`, original L144–347) and the live module (original L363–565), the two copies already diverged on the CN side. The candidate carries the layer once, in a single `[[code]]` block (candidate L168–590) that is both the exhibit and the delivery: the head module imports it as the candidate's block /1 (candidate L5), and both variable sets survive inside it in the original's order (the DELIVERY-MOVE match, module-css → code-css at 0.96 similarity; blocks B50 and B58 are this event's two faces). One line exists only in the original's display copy and not in its live module — a background-image naming the CN sandbox host (original L256, block B55) — and the port follows the live module, so the line has no counterpart; a divergence between the original's own copies, resolved for the operative one, not a port deletion. The gating also changes form: the original wraps its first 350 lines in `[[iftags +版式]]` (its delivery tail sits outside the gate), while the candidate leaves its delivery ungated and gates the credit-through-license-box body under `[[iftags +テーマ]]` (candidate L24–600), the JP form. The classifier's six EXHIBIT-RESTRUCTURE primaries adjudicate to this consolidation and the section 2 omission; an exhibit census confirms the specimen, the variable documentation, and the full CSS are present on both sides.
- **Why:** R3 forces the adjudication, and the census plus the topology match answer it: nothing the original delivers or documents is missing from the candidate; the restructure is the delivery form changing, with the content carried. KB-20's inverse (a delivery the port needs must arrive) is satisfied by the head module's /1 import.
- **Verify:** Compare `grep -n '\[\[code\]\|\[\[module\|iftags' original.txt candidate.txt`; read candidate L166–180 (the exhibit's porter banner, section 10) for the in-file statement of the form.
- **Disposition:** Standing; no structural deletion, no class I item.

### 9. Formatting only

- **What:** None as a primary class: the classifier finds no whitespace-only block and no re-indentation (0 and 0) among the 58 blocks, so the R7 follow-up-diff hazard is not triggered. (The 3 residue blocks are content, adjudicated in the appendix.)
- **Why:** Formatting churn is disclosed as its own class so it is never mistaken for a semantic change.
- **Verify:** Section 9 of the classifier skeleton for this package (WS-ONLY 0, re-indentation 0).
- **Disposition:** None required.

### 10. Porter annotations

- **What:** Four annotations. (1) The exhibit banner (candidate L170–175): a porter-written header in Chinese and Japanese stating the port's provenance (theme:gsk rev 7 on scp-wiki-cn), that this file holds only the GSK-specific customization, that the base's code files are read from theme:jakstyle-jp by @import, and that the BHL delivery was replaced with the scp-jp.github.io distribution — the in-file statement of sections 3 and 8, with one inaccuracy flagged in the per-theme record (it says code files 1 and 2; the bytes import file 1, which is the JP base's whole consumer delivery). (2) and (3) The two translator's notes on the omitted fade-in component (candidate L52, inside the usage quote, and L57, after it): near-duplicates of each other, both retained as the port left them; together they declare the omission and carry the original's speed-parameter note. (4) The license-box note (candidate L596, section 1): the re-hosting and author-confirmation statement. The candidate has no `[!-- --]` notes.
- **Why:** R2: porter-added text is part of the change record; annotations (2)–(3) are load-bearing (they are the only in-file ground for the fade-in omission).
- **Verify:** Read candidate L52, L57, L170–175, L596.
- **Disposition:** Standing; annotation (1)'s delivery count is the per-theme record's second flag.

### 11. Dispositions and exceptions

- **What:** Five items, each with its ground. (1) T1's eleven pseudo-ref errors: the candidate's own not-yet-posted references (its head imports, frames 3–4, its file URLs, and the base references of the draft form) — classes (ii)/(iii), posting-procedure and draft-form. (2) The rerun render row's items (RENDER-ROWS-RERUN16, CN7, which supersedes the first render row for this theme under rule S1): the sample's credit-modal errors (KB-32, preview form, ruling 5), the page-overflow readings recorded against the cross-cutting static-credit item, the runtime-hotlink site-theme chain (the environment's own chain, not this candidate's text), and the site-logo.png 404 (section 4, deferred asset). (3) P7 DISPOSITIONED: the unreferenced JP font loads and the SimHei stacks (section 4). (4) P9 DISPOSITIONED: the retained `:lang(cn)` header variants (section 5). (5) P11 DISPOSITIONED: the gsk-center and site-514 sibling links (section 7). The frame duplication is not in this list because it is not a disposition: it was FIXED by adjudication (FIX4-IWB, section 3). The two per-theme flags are not in this list either: no ledger line dispositions them.
- **Why:** A disposition is a decision with grounds (AGENTS.md §3 classes (i)/(ii)/(iii); the named KB entries; ruling 2 for item 4), not an omission; environment-layer lines are recorded as not-charged.
- **Verify:** Each item names its deciding record above and in the per-theme record.
- **Disposition:** DISPOSITIONED (items 1–5).

### 12. Verification

- **What:** (a) T1 source check (T1-ROWS row 178): exit 1, 11 errors / 4 warns / 1 info; all eleven errors are pseudo-ref, classes (ii)/(iii); there is no class (i) error. (b) T2/T3 render (RENDER-ROWS-RERUN16, lane CN7 — the rerun record, which the stamp follows under supersession rule S1 in place of RENDER-ROWS-2): FINDINGS, the items of section 11(2), all dispositioned; engine coverage full (chromium and webkit, both pages); the row also records that the original sample's webkit capture was a transient 503, re-run once per rule 2, the fresh capture carrying no 503 signature. (c) T4/T5 (LOCALIZE-ROWS row 194): FINDINGS jointly, display-affecting findings 3 — the frame duplication (since adjudicated, section 3), the retained `:lang(cn)` blocks, and the unprefixed hub link; the row's remaining charges （型 7 fonts, the orphan labels, the cross-candidate dependency on jakstyle-jp) are the sections 4, 1, and 3 records. The ledger §(c3) line records the outcomes: P6 FIXED, P7 DISPOSITIONED, P9 DISPOSITIONED, P11 DISPOSITIONED. (d) This package is self-verifying: `python3 review/build_review.py --check` regenerates diff.md and the verdict stamp from the two byte-faithful copies in this directory and compares. Counts in this README are the generator's (difflib, autojunk off): +191/−163 in 58 change blocks.
- **Why:** Verification claims name the cheapest deciding check and its result, not a general assurance.
- **Verify:** Re-run the checker on `pages/theme:gsk-jp.txt` and `python3 review/build_review.py --check` in this repo.
- **Disposition:** PASS (GOSIGN2-LEDGER (b) row 195; go-sign, COMPLETION-REPORT §10).

## Appendix — residue blocks

The classifier reports 3 residue blocks; all were adjudicated against the bytes:

| Block | Range (orig → cand) | Classifier state | Resolution |
|---|---|---|---|
| B3 | 11-11 → 41-41 (body → body) | no signature | Frame A's `theme=` line: the CN interwiki sheet repointed to the JP BHL sheet; section 3 |
| B4 | (added) → 44-44 (body) | no signature | The **評価：** label surviving its module; section 1 |
| B56 | 346-346 → 590-590 (code-css → body) | no signature | A blank-line pairing at the exhibit's tail, an alignment artifact of the section 8 consolidation; no content |

The 31 heuristic blocks are the specimen translations counted in section 6, the delivery-consolidation blocks counted in section 8 (B50–B54's DELIVERY-MOVE primaries), and the comment and banner text of section 10.

## Per-theme record

### The base theme and this theme are referenced by their CN names (defect flag)

Four references name pages that will not exist under the names given. Candidate L48 (intro prose): `[[[theme:jakstyle|JAKSTYLE]]]` — an unprefixed link to the base theme's CN name; the base's JP candidate is theme:jakstyle-jp, the very page whose delivery this candidate imports. Candidate L54 (usage snippet): `> [[include :scp-jp:theme:jakstyle]]` — the snippet a reader copies to adopt the theme includes a page that will not exist. Candidate L55 (same snippet): `> [[include :scp-jp:theme:gsk]]` — the theme's own name without its suffix. Candidate L163 (exhibit prose): `@@[[include :scp-jp:theme:jakstyle]]@@` — the base named plainly a second time. The candidate's own identity is not in doubt anywhere else in the file (its file name, its head imports at L4–5, and its frame URLs at L18 and L22 all use the `-jp` forms), so these four are inconsistent with the file's own convention, and the snippet pair (L54–55) is the operative one: followed literally, the adoption instructions fail at the second line. No ledger line dispositions these references (the P11 disposition covers the hub links of section 7, whose targets are sibling content pages; jakstyle-jp is a theme of this same campaign). The candidate is left exactly as it stands, per the standing rule for fix lanes; the repair, if the coordinator confirms it, is the repoint of the four references to theme:jakstyle-jp and theme:gsk-jp.

### The exhibit banner declares a base delivery the bytes make only in part (defect flag)

The porter banner at the exhibit's head (candidate L173–175) states that the base (CN theme:jakstyle, code files 1 and 2) is read from theme:jakstyle-jp's code files by @import. The bytes import jakstyle-jp's block 1 only: at candidate L4 (head module) and L18 (frame 3). No line in the candidate imports a jakstyle-jp block 2, and the original's block-2 delivery (its frame B, original L361) has no counterpart. The adjudication matters, and it is favorable to the delivery: theme:jakstyle-jp's own consumer contract is its block 1 (its own frame names block 1, and its head module imports the BHL sheets directly), so no base CSS the JP base offers its consumers is undelivered to this theme — the CN base's two-block anatomy simply has no second block on the JP side. What is wrong is the prose: the banner describes the CN base's anatomy as if it were the JP delivery's, and a reviewer trusting it would look for a block-2 import that does not exist. Flagged as a documentation inaccuracy inside the candidate, with the delivery itself verified sound; the candidate is left as it stands.

### Charged items whose bytes stand as charged (for the record)

Three T4 charges remain visible in the candidate under their dispositions, recorded here so the package does not read as if they had been repaired. (1) The JP font loads at candidate L177–178 are referenced by no stack, and the font variables name SimHei (section 4; P7 DISPOSITIONED). (2) The two `:root:lang(cn)` blocks stand in both variable sets (section 5; P9 DISPOSITIONED). (3) The labels **評価：** and **評価モジュールと著作情報モジュール：** stand over content their modules no longer occupy (section 1; charged by LOCALIZE-ROWS row 194, no separate ledger line). None of the three is re-flagged as a defect: each was seen by the sweep, charged or noted, and closed at the ledger determination. They are listed because a reviewer comparing this package against the T4 row will find them, and the package should say why they are still there.

## Change set outside the two diffed files

The diff covers the theme's own layer. (1) `pages/theme-decoration-sample-gsk-jp.txt` is the decoration sample the render checks ran against (its findings are the sample half of section 11(2)); it belongs to this theme's record but carries no port change of its own to explain here. (2) The declared base, theme:jakstyle-jp, is another row's candidate with its own review package; this package reads its delivery contract (block 1) and its furniture includes from that file where sections 2–3 say so, and explains no part of it. There is no companion file of this theme's own.
