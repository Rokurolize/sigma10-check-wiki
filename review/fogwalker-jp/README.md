# Review package — theme:fogwalker-jp (KO → JP port)

<!-- BEGIN GENERATED VERDICT STAMP — do not hand-edit; regenerate with review/build_review.py -->
## Verdict stamp
- Theme: theme:fogwalker-jp — origin KO, population #263 [GOSIGN2-LEDGER (b) row 263]
- Overall: STALE — candidate file changed since the verdict was computed (verdict against 435a6bb-era content, file sha256 now f1115d525641ea55d195ed3a086a4a990eb82eef27ebb46a831f5999f3c1c64c); verdict not carried over, re-judgement required
> verdicts below describe the pre-change file
- T1 (source check): FINDINGS (classified) — baseline 2026-11-16: exit 1, 6 errors / 0 warns / 1 info (pseudo-ref×6); standing classes dispositioned in register c1 [T1-ROWS row 267; GOSIGN2-LEDGER (b) row 263]
- T2/T3 (render, combined verdict): FINDINGS — [combined T2/T3] report `FINDINGS` — page runtime-hotlink site-theme chain only; sample credit-modal (preview-form) + 884px@768 overflow; T3 none beyond cross-cutting items. [RENDER-ROWS-2 (RENDER-S2-H (KO3))]
- Engine coverage: full matrix as run by the lane; coverage not separately caveated in the row [RENDER-ROWS-2 row]
- Credit modal: sample credit-modal errors dispositioned preview-form (credit:start-preview has no modal mechanism; GOSIGN-TESTS T2 amendment, 2026-11-16) [RENDER-ROWS-2 (RENDER-S2-H (KO3))]
- T4 (localize patterns + follow-up): PASS — display-affecting findings: 0 [LOCALIZE-ROWS row 262, source LOCALIZE-S2-F]
- T5 (translation text): PASS — the source reports judge T4/T5 jointly; one verdict word covers both [LOCALIZE-ROWS row 262]
- FIX5 re-judgement: none — no OPEN items at the ledger determination [GOSIGN2-LEDGER (b) row 263]
- Computed against: canonical commit b5cb7241f527a44933e45599b41df210690771c4; candidate file pages/theme:fogwalker-jp.txt sha256:f1115d525641ea55d195ed3a086a4a990eb82eef27ebb46a831f5999f3c1c64c; record: GOSIGN2-LEDGER.md + GOSIGN2-LEDGER-SUPPLEMENT.md as of the FIX5 head 435a6bb
<!-- END GENERATED VERDICT STAMP -->

## Status

| | |
|---|---|
| Verdict | **PASS** — passed at the ledger determination; this theme had no OPEN items and no §(e) register entry (GOSIGN2-LEDGER (b) row 263) |
| Standing items | **DISPOSITIONED** — T1 pseudo-ref ×6 (class (iii), section 11); the render row's three items (KB-40 / KB-32 / KB-33+KB-34, section 11) |
| Go-sign basis | COMPLETION-REPORT.md §10 (go-sign issued; 81 FIXED / 26 DISPOSITIONED / 0 OPEN across the sweep) |
| Named exception | None for this theme (the sweep's single named exception is theme:amethyst-v2, which has no candidate) |

## Provenance

| | Original | Candidate |
|---|---|---|
| Page | theme:fogwalker | theme:fogwalker-jp |
| Wiki | scpko.wikidot.com | SCP-JP Sigma-10 candidate (canonical repo) |
| Reference revision | 36 (first translation; the candidate's credit block records 初訳時参照リビジョン: 36) | — |
| Source of this copy | Campaign cache `gosign2-lanes/lane-oc-gs-localize-s2-F/orig-fogwalker.txt`, via the mirror store (class COPY, hash-verified against review/sources.tsv) | Canonical file `pages/theme:fogwalker-jp.txt`, copied at worktree HEAD b3ce875 |
| Lines / bytes | 510 lines / 10,626 bytes | 539 lines / 14,025 bytes |
| SHA-256 | 4b3acb36b894459825b1f1341d2dafe5a368ac48b87b4b1c85bb4a23fefd7be9 | ab6e5965e28e05566e0d2f133c68ea12da3882c805fc1ffd7a8285d2e325d3e6 |

Wave history: the candidate was created by the Stage 2 KO3 integration (commit 783e87d, the LOCALIZE-S2-F wave's port) and has exactly one later commit, 1869877 (FIX-CREDIT-D, the population-wide translator-attribution normalization). No FIX5 commit touches this file, because the theme had no OPEN items for FIX5 to re-judge.

## Summary

A standard KO port whose original has an unusual two-part anatomy: a usage head gated by the tag gate, then the theme's CSS carried in a `[[module CSS show="true"]]` block behind a hidden div, with a blockquoted dark-mode variant module at the tail gated by the original's `{$dark}` iftags hack. The candidate converts the main CSS to the wave-standard delivery (head import plus interwiki-style frame, body in a `[[code]]` exhibit), swaps the credit furniture for the JP preview block, replaces the two noonnu-distributed Korean webfonts with Google Fonts loads (Yuji Syuku for the display role, Gowun Batang for the serif role), re-hosts five images to the draft host, translates the prose, the CSS comments, and the reader-visible strings, and adds the JP license box with a fuller attribution record than the original carried. Measured churn (diff.md, the generator's difflib count with autojunk off: +127/−103, 230 changed lines in 45 change blocks / 16 diff hunks). T4/T5 judged this theme PASS outright, one of only 19 in the population.

## Class summary

Auto-classification by review/classify_hunks.py (signature table 2026-11-17.1): 45 change blocks — 21 specific (46.7%), 23 heuristic (51.1%), 1 residue (2.2%), 0 skipped. Pattern citations below name the KB entry; the patterns/ tree state cited throughout is commit 9c5e9079afb01d30cb9fc4ef9d714e5591eb2ffa.

| Label | Blocks |
|---|---|
| TRANS-UNANCHORED | 18 |
| COMMENT-TEXT | 10 |
| CSS-BODY | 8 |
| DRAFT-HOST | 7 |
| TRANSLATION-ANCHORED | 6 |
| ESCAPED-INCLUDE | 3 |
| IFTAGS | 3 |
| WS-ONLY | 3 |
| INCLUDE-REPOINT | 2 |
| INFO-DEL | 2 |
| SELF-DELIVERY | 2 |
| BARE-RATE-DEL | 1 |
| CONTENT-STRING | 1 |
| CREDIT-PREVIEW | 1 |
| FONT-IMPORT | 1 |
| LICENSE-BOX | 1 |
| LINK-REPOINT | 1 |
| TASL-FIELDS | 1 |

Adjudication for this README (every block was read against the bytes): the single residue block is the original's closing `[[/div]]` (B45), whose opener apparatus was deleted with the delivery conversion (section 8). The 8 heuristic CSS-BODY blocks resolve as four P7 font-stack rewrites (B22, B25, B33, B34; section 4), one `content:` string translation (B24; section 6), two `url(none)` value corrections (B37, B44; section 8), and the module-to-code closer of the delivery conversion (B39; section 3). The 10 COMMENT-TEXT blocks are R1 in-CSS comment translations (section 6). After adjudication no block is left unexplained.

## Standing sections

### 0. Header and provenance frame

- **What:** Theme theme:fogwalker-jp; original theme:fogwalker on scpko at reference revision 36; candidate `pages/theme:fogwalker-jp.txt`. Provenance route: derived from the original at the reference revision by the LOCALIZE-S2-F wave (sources.tsv kind: standard; no production JP counterpart exists for this theme, so the R4 adoption question does not arise). The frame itself is new: the original opens with its tag gate (original L1) and carries no delivery module at the head at all; the candidate opens with the delivery module (candidate L1–3), the interwiki-style frame (L5–8), and the localized gate after it (L10).
- **Why:** Section 0 declares the provenance route so every later count is read against the right baseline; the gate's tag is P2, the frame is P6/T3 (section 3).
- **Verify:** The sources.tsv row for fogwalker-jp; `sha256sum original.txt` against the Provenance table.
- **Disposition:** Standing (the route itself); the gate and frame changes are recorded in section 3.

### 1. Credit and attribution

- **What:** The original's credit furniture is a bare `[[module Rate]]` inside a `[[>]]` wrapper (original L3–5) plus an `:scpko:info:start`/`end` pair (original L7–19) whose body carries the title, 제작 thd-glasses, and two source lists (two Wikimedia Commons photo URLs for the images; two noonnu.cc font pages). The candidate deletes both (B2, B3, B6) and installs the JP form: a `:scp-jp:credit:start-preview`/`end-preview` block (candidate L11–20) carrying the eight ruling-3 fields (タイトル 霧中漫歩テーマ; 翻訳責任者 AI; 翻訳年 2026; 原題 안개를 거니는 테마; 著作権者 thd-glasses; 作成年 2022; 初訳時参照リビジョン 36; the source link to scpko.wikidot.com/theme:fogwalker). The info block's source lists do not reappear as credit prose; their substance moves to the license box (candidate L413–452), whose bg.jpg entry names both Commons photographs with their licenses and whose font line names the replacement faces (section 4). The candidate also gains the JP license box the original never had (B40: `:scp-jp:component:license-box-backend`/`license-box-end` with per-file entries for five images and the fonts, including two "no license stated in the original; confirm with the author before posting" flags the original's record could not have made). T7 credit-module CSS: the theme carries no credit CSS block of its own on either side; nothing was added, and no in-place correction was needed.
- **Why:** P3/T1: the preview credit module is the rate-bearing JP form, so the bare Rate is deleted rather than duplicated (KB-09), and the info pair is ledger class C residue, not JP furniture. Ruling 3 fixes the eight fields; the file's last commit (1869877, FIX-CREDIT-D) is that form arriving population-wide. T4 (license box) is a supplement here, and its per-file entries are where the original's scattered source lists become a single attribution record.
- **Verify:** `grep -n 'info:start\|info:end\|module Rate' candidate.txt` returns nothing; read candidate L11–20 against the eight fields; read candidate L413–452 for the license box.
- **Disposition:** Applied. T4 judged this theme PASS (LOCALIZE-ROWS row 262), so no credit item stands against it.

### 2. Includes and components

- **What:** One live repoint, in the usage exhibit: `@@[[include :scp-jp:theme:fogwalker]]@@` (candidate L27, B6), the escaped form of the original's own-theme include. Two further repoints are exhibit text, not live includes: the preview tab's image-block parameters are re-hosted (section 4), and the sample include forms inside the usage text name `:scp-jp:` targets. The candidate's remaining includes are the frame, credit, and license-box includes of sections 1 and 3; every live include in the candidate names a `:scp-jp:` target. No component swap (T8) occurs on either side.
- **Why:** P1 (KB-15): an include must name the JP counterpart that actually exists on scp-jp. Ruling 4 is not engaged: no component had to be ported alongside this theme.
- **Verify:** `grep -n '\[\[include' candidate.txt` — five includes plus the escaped usage form, all `:scp-jp:`.
- **Disposition:** Applied; no foreign include kept, no named exception needed.

### 3. Delivery and code loading

- **What:** The original's delivery is idiosyncratic: no head module at all; the main CSS sits in a `[[module CSS show="true"]]` (original L84–420) behind a hidden div (`[[div [[iftags -테마]]style="display: none"[[/iftags]]]]`, original L83), and a second module at the tail (original L425–508) carries the dark-mode overrides behind a blockquoted `{$dark}` gate (original L422–424). The candidate converts the main CSS to the wave-standard form: a head `[[module CSS]]` importing the candidate's own `local--code/theme%3Afogwalker-jp/1` from the draft host (candidate L2, B1), the interwiki-style frame at priority=1 naming the same /1 (candidate L5–8, B2), and the CSS body itself in a `[[code type="css"]]` exhibit inside a collapsible (candidate L82–410; the closer conversion is B39, `[[/module]]` → `[[/code]]`). The hidden-div apparatus and the original's `[[/iftags]]` at L81 are deleted with the form they served (B19). The dark-mode module is preserved as a module (candidate L455–538): its gate is translated in place (`+tag` → `+テーマ`, B40's region), and its background image is re-hosted (B41, section 4). The tail's `[!----]` comment is carried over unchanged.
- **Why:** P4/T9 (own-code delivery served from JP hosts) and P6/T3 (the interwiki-style frame, priority 1 for the theme's own layer). The dark module keeps its original channel because its gate is a runtime variant switch, not a delivery copy; converting it to a code exhibit would have broken the variant it exists to serve. The draft-host form of the live lines is KB-41, class (iii).
- **Verify:** `grep -n 'local--code\|\[\[module\|\[\[code' candidate.txt` — head module L1–3, code exhibit L82–410, dark module L455–538; compare original L83–84 and L422–425.
- **Disposition:** DISPOSITIONED (draft-host lines, class (iii)); the delivery-form conversion itself is applied.

### 4. Fonts and assets

- **What:** Loads (B19, with B18's FONT-IMPORT span): the original loads its two Korean faces by `@font-face` from jsdelivr's projectnoonnu mirrors (original L85–98: 'NostalgicPoliceVibe' and 'GowunBatang-Bold', both noonnu-distributed). The candidate deletes both `@font-face` blocks and loads two families in one Google Fonts `@import` at the head of its code exhibit (candidate L85): Gowun Batang (400;700) and Yuji Syuku, preceded by the porter's comment recording the substitution and its ground (the originals were only distributed from noonnu.cc, not an exception host). Stacks (the four CSS-BODY blocks B22, B33, B34, plus B25): the header stacks prepend 'Yuji Syuku' and keep 'NostalgicPoliceVibe' as a following fallback name (candidate L107, L317, L327) — a name with no load behind it in the candidate, retained as a fallback slot; the serif stack is rewritten outright, `'GowunBatang-Bold', Arial, sans-serif` → `'Gowun Batang', 'Yu Mincho', 'Hiragino Mincho ProN', serif` (candidate L120). Each rewritten stack line carries a `/* [JP] */` marker. The candidate's own font prose (candidate L72–74) states the new arrangement and names the original faces as the 原語版 forms. Assets: five image URLs move to the draft host's `theme%3Afogwalker-jp` folder with file names unchanged (B8 site-64k.jpg in the image-block exhibit, candidate L33 — its original path named another page's folder, `secure-facility-dossier-site-64k`; B15 fogwalker-light.png, candidate L63; B16 fogwalker-dark.png, candidate L67; B20 bg.jpg, candidate L90; B41 bg_d.png in the dark module, candidate L457).
- **Why:** P7/T5 with KB-16 (the font load gap) and KB-17 (font hosts): noonnu is not an exception host, so the loads had to move or fall; the porter's choice, recorded in the candidate's own comment, was substitution with the same serif family from Google Fonts and a JP display face for the header role, not a bare deletion. P5: the theme's own images are re-hosted to the JP side; the draft-host form is the class (iii) draft state.
- **Verify:** `grep -n 'font-family\|@import\|@font-face' candidate.txt` — one import line, no @font-face, the stacks as listed; `grep -n 'wdfiles' candidate.txt` against the asset list above.
- **Disposition:** Font substitution applied; the retained 'NostalgicPoliceVibe' fallback name is standing (it resolves only where a viewer has the face locally, and the stack's first entry is the loaded JP face); draft-host asset URLs DISPOSITIONED (class (iii)).

### 5. Header, sidebar, and site furniture

- **What:** No `--header-title`, `--header-subtitle`, or `--logo-image` variable is set on either side; the theme's header text is rendered by CSS `content:` strings, which are translated in section 6 (B24: `content: "무진기담"` → `"霧津奇譚"`). The theme's sidebar and topbar rules are carried over unmodified apart from the font lines of section 4 and the comment translations of section 6. No P8 layout adaptation was needed: the candidate inherits the JP site furniture through the frame.
- **Why:** P9/T6 and P8 are presence-checked classes; for this theme the header surface is a `content:` string, not a variable, and it is counted with the reader-visible strings where it belongs.
- **Verify:** `grep -n -- '--header-\|--logo' candidate.txt original.txt` returns nothing on either file; read candidate L120–121 area against original L131 for the `content:` line's block (B24 is at candidate L121).
- **Disposition:** Standing.

### 6. Text translation

- **What:** Translation runs in four counted groups. Usage and exhibit prose (TRANSLATION-ANCHORED B7, B9, B10, B13, B14, B26 and the unanchored prose blocks B4, B5, B11, B12, B17): tab titles (プレビュー, ダークモード), the heading samples, the collapsible labels, the table sample, the link samples (B12's 空リンク is also the LINK-REPOINT label's instance: a placeholder page name translated as sample text), and the font prose of section 4 — where the original's own line carries corrupted glyphs (`그리운 경찰 ���성체` in the mirror at original L72), an original-side artefact the candidate's rewrite does not reproduce. CSS comments (the 10 COMMENT-TEXT blocks B21, B27–B32, B35, B36, B38): section banners translated in place (ヘッダー, トップバー, サイドバー, スクロールバー, 評価モジュール, 本文 - タイトル, 本文 - リンク, 本文 - 引用ブロックとタブ, モバイル, and the 背景 banner inside B19's region) — R1 in-CSS text, porter-visible only. Reader-visible CSS strings: B24's `content:` (section 5) and B26's quoted `content:` passage, translated with its quotation marks restyled to 「」. The info block's two source lists are deleted as prose and reappear as license-box attribution (section 1). Korean survives in the candidate on exactly two lines, both inside the credit block: the 原題 field (candidate L15) and the source link's label (candidate L19), both quotations.
- **Why:** P10 (body, usage, and sample translation) and KB-18 (reader-visible strings, including `content:`). R1 comment text is counted separately so porter-visible translation is never conflated with reader-visible text.
- **Verify:** A Hangul scan of candidate.txt returns only candidate L15 and L19; the pairs are diff.md's sections in order.
- **Disposition:** Standing (the port itself); no untranslated reader-visible text remains outside the two credit quotations.

### 7. Links

- **What:** The candidate's live outbound links: the credit block's source link (candidate L19), naming scpko.wikidot.com/theme:fogwalker, the original's recorded host in sources.tsv — the serving form, not a defect; and the usage prose's canon link (candidate L24), `[[[https://scpko.wikidot.com/mujin-yarn|霧津奇譚（韓国語版）]]]`, target unchanged, label translated and marked as the Korean version, because the canon hub is the original branch's page and the text says so. The license box's 出典 lines name scpko and Wikimedia Commons URLs as attribution records (section 1), not navigation. No prose link in the candidate targets a page that does not serve.
- **Why:** P11: prose links take the JP counterpart or the serving original; the dead-reference evidence standard is met by the recorded host matching the link host on the one link that carries the port's provenance.
- **Verify:** `grep -n 'wikidot.com\|wikimedia.org' candidate.txt` — the hits are the two live links and the license-box attribution lines.
- **Disposition:** Standing; T4/T5 PASS for this theme (LOCALIZE-ROWS row 262) covers both live links.

### 8. Structure

- **What:** Two structural items beyond the delivery conversion of section 3, both adjudicated here. (1) B45 (the one residue block): the original's last line is a `[[/div]]` (original L510) closing the hidden div whose opener stood at original L83; the candidate deletes the apparatus entire, so the closer has no counterpart and no JP form — a deletion with its ground in the delivery conversion, not a dropped exhibit. (2) Two in-place value corrections inside inherited CSS rules: `background: #EBEBEB url(none) repeat-x` → `#EBEBEB none repeat-x` (B37, candidate L363) and the same form in the dark module (B44, candidate L510). `url(none)` names a relative file fetch that cannot serve; `none` is the valid value for the same rendering intent. Everything else about the closing rule holds: variable names, selectors, and channel order are preserved, the dark module keeps its channel and position at the tail, and the JP additions arrive as the head frame, the credit swap, and the license box, not interleaved into the inherited CSS. An exhibit census confirms the tabview, its tabs, the heading/table/collapsible samples, and both background variants are present on both sides in the same order.
- **Why:** The closing rule exists so a follow-up diff applies cleanly; the two corrections are disclosed here because they edit inherited rules in place (the R6 disclosure shape, though the mechanism is a value form, not a JP-DOM selector). A silent `[[/div]]` deletion would share a diff shape with a structural deletion (ledger class I); the census and the opener's fate are what separate them.
- **Verify:** Read original L83–84 and L508–510 against the candidate's tail; `grep -n 'url(none)' candidate.txt original.txt` — two hits in the original, none in the candidate.
- **Disposition:** Standing; no structural deletion, no class I item.

### 9. Formatting only

- **What:** Three blocks, all WS-ONLY: B23 (original L121 → candidate L110), B42 (original L450 → candidate L480), B43 (original L468 → candidate L498), each a whitespace-only line inside the CSS bodies. The classifier finds no re-indentation anywhere (0 blocks pair up after leading-whitespace normalization), so the R7 follow-up-diff hazard is not triggered.
- **Why:** Formatting churn is disclosed as its own class so it is never mistaken for a semantic change, and so a reviewer can skip it safely.
- **Verify:** The three blocks in diff.md.
- **Disposition:** None required.

### 10. Porter annotations

- **What:** Three annotations, none with an original counterpart. (1) The font-substitution comment at the head of the code exhibit (candidate L83–84), recording that Yuji Syuku and Gowun Batang replace the two noonnu-only faces and why — the load-bearing explanation for section 4's load change. (2) The `/* [JP] */` markers on the rewritten stack lines (candidate L107, L120, L317, L327). (3) The license box's two "no license stated in the original; confirm with the author before posting" flags (section 1) are porter-authored record text in the same sense. No `Ported for SCP-JP` banner line exists in this candidate; the skeleton's "none" for a banner is correct, and the annotations that do exist ride inside font and license blocks, which is why no annotation signature fired.
- **Why:** R2: porter-added text is part of the change record, and annotation (1) is the only in-file explanation of the font substitution.
- **Verify:** Read candidate L83–84; `grep -n '\[JP\]' candidate.txt`.
- **Disposition:** Standing.

### 11. Dispositions and exceptions

- **What:** Three items, each with its ground. (1) T1's six pseudo-ref errors: class (iii), draft-wiki form (GOSIGN-TESTS T1 classification; GOSIGN2-LEDGER §(c1)) — the candidate's own draft-host delivery and asset lines (sections 3–4), rewritten to scp-jp at posting. The run's single info is recorded verbatim in the T1 row and carries no classification. (2) The render row's page item, the runtime-hotlink site-theme chain: environment-layer, not charged to the candidate (KB-40). (3) The render row's sample items: the credit-modal errors (KB-32, ruling 5) and the 884px@768 overflow (KB-33/KB-34 cross-cutting families). No T4/T5 item exists for this theme: both tests judged PASS.
- **Why:** A disposition is a decision with grounds (AGENTS.md §3 classes (i)/(ii)/(iii); the named KB entries), not an omission; environment-layer lines are recorded as not-charged.
- **Verify:** Each item names its deciding record above.
- **Disposition:** DISPOSITIONED (all three items).

### 12. Verification

- **What:** (a) T1 source check (T1-ROWS row 267): exit 1, 6 errors / 0 warns / 1 info; all six errors are pseudo-ref, class (iii); there is no class (i) error. (b) T2/T3 render (RENDER-ROWS-2, lane RENDER-S2-H (KO3)): FINDINGS, the three items of section 11, all dispositioned; engine coverage as run by the lane, not separately caveated in its row. (c) T4/T5 (LOCALIZE-ROWS row 262): PASS jointly, display-affecting findings 0 — one of the 19 outright PASS themes in the localize sweep. (d) This package is self-verifying: `python3 review/build_review.py --check` regenerates diff.md and the verdict stamp from the two byte-faithful copies in this directory and compares. Counts in this README are the generator's (difflib, autojunk off): +127/−103 in 45 change blocks / 16 diff hunks.
- **Why:** Verification claims name the cheapest deciding check and its result, not a general assurance.
- **Verify:** Re-run the checker on `pages/theme:fogwalker-jp.txt` and `python3 review/build_review.py --check` in this repo.
- **Disposition:** PASS (GOSIGN2-LEDGER (b) row 263; go-sign, COMPLETION-REPORT §10).

## Change set outside the two diffed files

The diff covers two files; the port's record is one file larger. `pages/theme-decoration-sample-fogwalker-jp.txt` is the decoration sample the render checks ran against (its findings are the sample half of section 11); it belongs to this theme's record but carries no port change of its own to explain here. There are no companion fragments, no shared base file, and no inbound-link repairs in other candidates for this theme.
