# Review package — theme:the-track-changers-jp

<!-- BEGIN GENERATED VERDICT STAMP — do not hand-edit; regenerate with review/build_review.py -->
## Verdict stamp
- Theme: theme:the-track-changers-jp — origin CN, population #238 [GOSIGN2-LEDGER (b) row 238]
- Overall: STALE — candidate file changed since the verdict was computed (verdict against 435a6bb-era content, file sha256 now e64da2d37be5d2ff250082565d9e74d305b860b785769ce2176c3c777804691f); the verdicts below were computed against that pre-change file, and the record verdict stands: a candidate revised through the campaign's recorded repairs is posted like a PASS row, with the change recorded in its package
- T1 (source check): FINDINGS (classified) — baseline 2026-11-16: exit 1, 7 errors / 2 warns / 1 info (pseudo-ref×5, hotlink×2); standing classes dispositioned in register c1 [T1-ROWS row 203; GOSIGN2-LEDGER (b) row 238]
- T2/T3 (render, combined verdict): FINDINGS — [combined T2/T3] report `FINDINGS` — sidebar-unreachable at 375/320 on page and sample + runtime-hotlink site-theme chain + candidate fastly.jsdelivr.net; sample credit-modal (preview-form); T3 re-run, no new screenshot-grounded visual finding; chromium-only coverage (no WebKit verdict). [RENDER-ROWS-G (CN16)]
- Engine coverage: chromium-only, both pages (no WebKit verdict) [RENDER-ROWS-G row, findings cell]
- Credit modal: sample credit-modal errors dispositioned preview-form (credit:start-preview has no modal mechanism; GOSIGN-TESTS T2 amendment, 2026-11-16) [RENDER-ROWS-G (CN16)]
- T4 (localize patterns + follow-up): FINDINGS — display-affecting findings: 1 [LOCALIZE-ROWS row 237, source LOCALIZE-S2-E]
- T5 (translation text): FINDINGS — the source reports judge T4/T5 jointly; one verdict word covers both [LOCALIZE-ROWS row 237]
- FIX5 re-judgement: items 93 (class H) FIXED, 94 (class H) FIXED — FIX5-TEXTB §1, commit 3f328d8: Chinese edit-lock strings translated with dustframe's reviewed wording, byte-for-byte; belief link (probe 404, no JP counterpart) converted to plain text with a translator's note; theme:old-money-theme link repointed to theme:old-money-theme-jp [GOSIGN2-LEDGER-SUPPLEMENT (a) items 93–94]
- Computed against: canonical commit fd36608a54c17d699155b725e041a75bfd044996; candidate file pages/theme:the-track-changers-jp.txt sha256:e64da2d37be5d2ff250082565d9e74d305b860b785769ce2176c3c777804691f; record: GOSIGN2-LEDGER.md + GOSIGN2-LEDGER-SUPPLEMENT.md as of the FIX5 head 435a6bb
<!-- END GENERATED VERDICT STAMP -->

Status: explanation written (lane rfix16, 2026-11-17); the verdict stamp above is generated and reads STALE by design: it was computed against the 435a6bb-era file, and the candidate has since changed in commit b5cb724 (the usage-example sweep, per-theme record). The explanation below is written against the current bytes. One defect is flagged against the candidate (section 1) and one minor defect (section 4), with two further minor observations (sections 8 and 2); the package is written against the candidate as it stands.
Candidate: review/the-track-changers-jp/candidate.txt (sha256 137195e142fc67e7b1dea4eee268cce057d5f84b59726860f01e2cd4ee79194c)
Original: theme:the-track-changers — scp-wiki-cn, revision 34 (sha256 5b1e7836043fef9174af23cb78084ee94af37c16be24058593bb7cada059a18d)
Classifier: classify_hunks.py 0.1.0; signature table 2026-11-17.1; patterns commit 9c5e9079afb01d30cb9fc4ef9d714e5591eb2ffa

## 0. Header / provenance

| | |
|---|---|
| Original | `theme:the-track-changers` on scp-wiki-cn (CN), revision 34 — `original.txt` in this package |
| Candidate | `theme:the-track-changers-jp` — `candidate.txt`, a byte copy of `pages/theme:the-track-changers-jp.txt` in this repository |
| Provenance route | Derived from the original at the reference revision (route R1 in the campaign taxonomy): the CN Basalt-derived theme carried over with the JP credit form, the inlined component CSS, the translation and the JP font loads applied. |

A provenance correction is owed on this theme's `review/sources.tsv` note, which claims the original was "superseded upstream since the reference revision" and cites the follow-up artifact `diff-the-track-changers-from34.txt` (campaign record, LOCALIZE-S2-E lane). The artifact records the opposite: `scp-wiki-cn:theme:the-track-changers rev34 → rev34 変更: なし` — re-checked at the current revision, no changes, empty intervening-revision table. The original was not superseded; revision 34 is both the reference and the current revision. The correct standard form for the note is recorded in the lane report for the coordinator's harvest correction; this package's `original.txt` is unaffected (its hash equals the sources.tsv value).

Summary: a CN theme built on Crimone's crimson-anemone (Basalt-derived) CSS. The original delivers through two head modules (the jsdelivr Basalt imports plus EN component imports; then a `local--code` self-import of its single code block) and the code block itself (original L193–753). The candidate keeps the jsdelivr pair verbatim (KB-14), inlines the two EN component stylesheets (betterfootnotes, acs-animation) into its own code block instead of importing them, repoints the self-delivery to its own draft-host address, and grows the code block from 561 to 1,441 lines in consequence. The theme carried two blocking items, both class H: item 93 (untranslated Chinese edit-lock strings) and item 94 (dead prose links to `belief` and `theme:old-money-theme`), both re-judged FIXED by FIX5-TEXTB (commit 3f328d8). The per-theme record re-derives both closures.

## Class summary

| Label | Blocks |
|---|---|
| BARE-RATE-DEL | 1 |
| COMMENT-TEXT | 1 |
| COMPONENT-SWAP | 1 |
| CONTENT-STRING | 4 |
| CREDIT-PREVIEW | 1 |
| CSS-BODY | 1 |
| DRAFT-HOST | 6 |
| EXHIBIT-RESTRUCTURE | 2 |
| FONT-IMPORT | 1 |
| GLYPH-FORM | 1 |
| HEADERVAR | 1 |
| IFTAGS | 2 |
| INCLUDE-REPOINT | 1 |
| JPFONT-LOAD | 1 |
| LICENSE-BOX | 1 |
| LINK-REPOINT | 1 |
| SELF-DELIVERY | 3 |
| T7-CREDIT-CSS | 1 |
| TASL-FIELDS | 1 |
| TRANS-UNANCHORED | 28 |
| TRANSLATION-ANCHORED | 23 |
| WS-ONLY | 13 |

Counts: 73 blocks, 45 specific, 26 heuristic, 2 residue, 0 skipped (comment text).

## 1. Credit and attribution

- What: the candidate holds the JP preview credit block at L13–22 (CREDIT-PREVIEW and TASL-FIELDS labels, block B3): タイトル 「変軌 テーマ」, 原題 「变轨 版式」, 作成年 2022, 初訳時参照リビジョン 34, 翻訳責任者 AI, 翻訳年 2026, 元記事リンク to the CN original — and, as its 著作権者 field, a pointer that names nobody: `原語版ページの作成者に同じ（scp-wiki-cn の theme:the-track-changers）` (candidate L18). The license box repeats the shape: `license-box-backend |author=scp-wiki-cn theme:the-track-changers の作者` (candidate L1612–1613; LICENSE-BOX block B73, the box itself present at L1612–1617 with a JP-form source note). The original names the author in both corresponding places: its credit block reads `**作者：**[[*user Mercuresphere]]` (original L29, inside the `:scp-wiki-cn:credit:start` apparatus at L27–33), and its code-block banner reads "By Mercuresphere" with the base credits "Based on Basalt Theme by Liryn & Placeholder McD and Old Money Theme by Woedenaz" (original L196–198). The candidate's own prose also names him: candidate L42 states the theme was made by `[[*user Mercuresphere]]` at `[[*user HuanianQWQ]]`'s request. The original's labelled bare Rate (original L23–25) does not stand in the candidate (BARE-RATE-DEL block B4; the preview credit is rate-bearing, KB-09). The T7-CREDIT-CSS label rides on the giant block B52: the candidate's code block carries the JP credit module's styling inside its integrated CSS, the supplement form for a theme whose credit apparatus is the JP module.
- Why: class P3/T1 (credit swap) and T4 (license box) — and the pointer is a defect of the credit family: the campaign's TASL standard requires the field to name the author the original names, and a pointer in place of the name breaks attribution exactly where a reader looks for it. The named author is not obscure: he is named in the original's credit block, in its banner, and in the candidate's own prose.
- Verify: candidate L18 and L1613 against original L29 and L196–198; `grep -n "Mercuresphere" candidate.txt` returns the prose occurrence at L42 and the translated banner inside the code block — every occurrence except the two attribution fields.
- Disposition: **DEFECT FLAG (open)** — the 著作権者 field (candidate L18) and the license-box author parameter (candidate L1613) name nobody, where the original names Mercuresphere. No ledger item charges it (the theme's items are 93/94); it is flagged here and in the lane report with both loci for a repair lane. The package is written against the candidate as it stands. The remainder of this section's classes (preview swap, license-box presence, bare-Rate removal) are in their settled forms.

## 2. Includes and components

- What: the live includes are the frame (candidate L7–10), the credit pair (L13, L22) and the license pair (L1612, L1617) — all `:scp-jp:`. The usage example is the COMPONENT-SWAP / INCLUDE-REPOINT block B11 (original L73 → candidate L46): `> {{[[include :scp-jp:theme:the-track-changers-jp]]}}`, the candidate naming itself in the `{{ }}` form (its post-sweep state; per-theme record). The image-block include at candidate L50 is covered in section 8. One original include does not stand in the candidate: the palette exhibit component `:scp-wiki:component:theme-squares` with its ~27 colour parameter lines (original L39–65), replaced by a translator's note at candidate L39 stating that the original reads an SCP Wiki component that does not exist on SCP-JP and that it is omitted (EXHIBIT-RESTRUCTURE block B7). No component `theme-squares` exists in this repository's candidate set or in the production record (`pages/`, `pages-existing/`), so no repoint target was available; porting the component with the theme would have been the ruling-4 route, and the porter instead omitted it with the omission disclosed on the page itself. The colour values themselves are not lost: they are the theme's `:root` variables, present in the code block on both sides.
- Why: class P1 (repoint) for the standing includes; for the dropped exhibit, the ground is KB-54's family (a foreign component with no JP equivalent) applied by omission-with-disclosure rather than by a kept foreign include.
- Verify: `grep -n "\[\[include" candidate.txt` returns five `:scp-jp:` includes and no foreign one; original L39–65 against candidate L35–39 for the exhibit locus.
- Disposition: the theme-squares omission is dispositioned here on the stated ground (no JP equivalent exists; omission disclosed in-file at candidate L39; palette data preserved in the CSS variables). It is recorded in the lane report as an adjudicated disposition, since no ledger record names this instance; if the coordinator prefers the ruling-4 route, the remedy is a component port, not a text fix.

## 3. Delivery and code loading

- What: the original's delivery: head module 1 (L1–6) importing the jsdelivr collapsible-sidebar and basalt.css, plus the EN `component:betterfootnotes/1` and `component%3Aacs-animation/1` local--code imports; head module 2 (L17–19) importing its own `/code/1` from `scp-wiki-cn.wdfiles.com`; the code block (L193–753) as the delivered stylesheet. The candidate's delivery: one head module (L1–5) importing the same jsdelivr pair verbatim and its own `/1` from the draft host (`sigma10-jp-test.wdfiles.com/local--code/theme%3Athe-track-changers-jp/1`, candidate L4; SELF-DELIVERY blocks B2–B4, DRAFT-HOST labels on B2, B3, B13, B53–B55); the frame include at priority 1 with `theme=` naming that same address (candidate L7–10); and the code block (candidate L169–1609) as the stylesheet. The address census is clean: the file contains exactly one code block in each side (original L193, candidate L169, both `[[code type="css"]]`), so `/1` names the block that actually holds the CSS — not the navla shape. The EN component imports are gone from the head module (CSS-BODY block B1, original L3–4 → candidate L3) because their content moved: the candidate's code block inlines the betterfootnotes CSS (the `.fnnum` footnote apparatus is visible from candidate L195) and the acs-animation CSS, per the porter's banner annotation in the block (candidate L184–190, section 10). That integration, plus the font import group and the JP stack work, is why the code block grows from 561 to 1,441 lines. Brace depth of the code block: final 0, minimum 0, on both sides (measured).
- Why: class P4 (delivery) with KB-14 (the jsdelivr pair is third-party code with no JP candidate, kept verbatim — ledger (c3) pattern-4 line names this theme in the KB-14 set) and KB-41 (draft-host self-addresses are the sanctioned draft-stage form). Inlining the two component stylesheets is the porter's delivery judgment: their EN local--code sources have no JP counterparts, and the styles are small, static CSS; the banner annotation records the choice in the file.
- Verify: `grep -n "@import" candidate.txt` returns the head module's three lines and the code block's font group; the code-block census above; candidate L184–190 for the integration note.
- Disposition: pattern 4 DISPOSITIONED as KB-14 verbatim-import for this theme [GOSIGN2-LEDGER (c3), FIX4-REPOINT / FIX4-IWA §3]; the draft-host forms are class (iii), dispositioned in section 11. No delivery item stands open.

## 4. Fonts and assets

- What: because delivery runs through the code block, the font loads live inside it (FONT-IMPORT and JPFONT-LOAD labels on B52): candidate L171–181 imports Noto Sans JP and Noto Serif JP (L171–172, the JP loads), Inter, Josefin Sans, Oxygen, Fira Code, Work Sans, Roboto, and Noto Sans SC (L180 — the CN face, retained for the Chinese strings the theme keeps, section 5). The stacks name the loaded faces (the font prose at candidate L156–158: body Noto Sans JP; header/見出し Work Sans / Noto Sans JP / 游ゴシック; mono Fira Code / Noto Sans Mono CJK JP / 游ゴシック）. Two duplications stand in the import group: Fira Code is imported twice (candidate L176 bare `family=Fira+Code` and L179 `family=Fira+Code:wght@300..700`) and Inter twice (L173 `wght@400;700` and L181 full-range), and three of the group’s URLs carry the HTML-escaped `&amp;` form (L177, L178, L179, L181) where the bare `&` is the CSS form — the escaped parameter name is ignored by the font server, so the faces load without their `display=swap` parameter. Assets: the theme's logo is re-hosted to the candidate's own attachments on the draft host — the image-block at candidate L50 and the `--logo` variable (candidate L1071; DRAFT-HOST blocks B53–B55 cover the in-CSS asset addresses at L1071, L1225, L1264) — against the original's jsdelivr file URL (original L77, L216). The jsdelivr stylesheet imports themselves are KB-14 (section 3), not assets in this sense.
- Why: pattern 7 / KB-16 for the JP loads (present and preceding the stacks that name the faces); the duplication is the standing minor-defect class (a duplicated import is dead weight in the delivered stylesheet and evidence of an unedited merge of two import lists).
- Verify: `grep -n "@import" candidate.txt` inside the code block returns the eleven lines L171–181; the Fira Code and Inter pairs are visible in that list.
- Disposition: **MINOR DEFECT FLAG (open)** — duplicated font imports at candidate L176/L179 (Fira Code) and L173/L181 (Inter), with the `&amp;` forms in the same group. No ledger item charges it; flagged here and in the lane report. The JP loads themselves are complete; no stack names an unloaded face.

## 5. Header, sidebar, site furniture

- What: the header variables stand in the code block's `:root`: `--title: " 变轨者"` and `--subtitle: " 点燃烛火 划破夜幕"` (candidate L1069–1070; HEADERVAR label on B52), byte-identical to the original's (L214–215) — the theme's Chinese title and its slogan kept as identity strings. The furniture markup at the head of the body (candidate L24–30: the `header-link` anchor, the `sb-button` anchor with its `≡` glyph, the logo div) is the original's Basalt furniture carried in form. The collapsible-sidebar behaviour arrives through the jsdelivr import (section 3).
- Why: ruling 2 takes header/title language out of scope as a defect class, and the subtitle is a slogan functioning as a mark (the KB-06 shape), not a prose sentence — so the boundary that translated tales-of-the-mosaic's sentence-subtitle does not reach this one. The retained Chinese strings are also why the Noto Sans SC load of section 4 exists.
- Verify: candidate L1069–1070 against original L214–215, byte-for-byte.
- Disposition: no header item was charged against this theme (its T4 charges are items 93/94); the kept forms stand under ruling 2 / KB-06 as recorded here.

## 6. Text translation

- What: the documentation body is translated from Chinese throughout: TRANSLATION-ANCHORED 23 blocks and TRANS-UNANCHORED 28, the standard usage/examples text (headings, the horizontal-rule and blockquote instructions, the font specimens at candidate L156–158 against original L184–186). CONTENT-STRING fires 4 times; three of the four are item 93's edit-lock strings (blocks B62, B66, B68 — the per-theme record), and the fourth rides on B52 (the code-block head region, where string-valued variables and the banner sit). GLYPH-FORM fires once (B12, original L75 → candidate L48): the 終無信仰 hub name in the image caption region, simplified forms （终无信仰） rendered in the Japanese traditional forms （終無信仰) — the same conversion the caption at candidate L50 shows (`caption=終無信仰 ロゴ`, against original L77's `终无信仰 标志`, also translated 标志→ロゴ).
- Why: class P10 (translation) and KB-18's reader-visible half for the CSS strings: `content:` text renders for readers, so untranslated lock messages are a display defect (item 93), while the hub name's glyph forms follow the Japanese convention for the name.
- Verify: the lock-string pairs are quoted in the per-theme record; the caption pair is at original L77 / candidate L50.
- Disposition: items 93/94 FIXED (per-theme record); T5 judged jointly with T4 in LOCALIZE-ROWS row 237 (the table's row for population row 238).

## 7. Links

- What: item 94's locus is candidate L42 (LINK-REPOINT block B9, original L69 → candidate L42), re-derived in the per-theme record: the `belief` hub link stands as plain text （終無信仰設定） with a translator's note preserving the reference and stating the ground, and the Old Money link reads `[[[theme:old-money-theme-jp|Old Moneyテーマ]]]`. The remaining prose links are the user links in the same sentence (Mercuresphere, HuanianQWQ — section 1) and the credit block's source link to the CN original (a quotation, section 1). No other prose link names a JP-nonexistent target: the S2-E lane's cross-cutting dead-target list charged this theme's two, and both are resolved.
- Why: class P11: a repoint where the JP candidate exists (old-money-theme-jp does; it is a candidate in this repository), plain text with the reference preserved where none exists (belief: probe 404, no JP counterpart — the supplement's record).
- Verify: candidate L42 against original L69 (the sentence in the original's credit prose naming both targets); `ls pages/ | grep old-money` returns the -jp candidate.
- Disposition: item 94 FIXED (FIX5-TEXTB §1, commit 3f328d8), re-derived below.

## 8. Structure

- What: the gate structure is preserved (`[[iftags +版式]]` original L21 → `[[iftags +テーマ]]` candidate L11; IFTAGS blocks B3, B4). Two exhibit-region items. (1) B13 (original L77 → candidate L50) carries EXHIBIT-RESTRUCTURE but is the classifier's false-fire shape: the change at that locus is the image-block include's re-hosting and caption translation (sections 4 and 6); the exhibit stands. (2) B7 is the theme-squares exhibit drop, dispositioned in section 2. One structural blemish stands at the code-display seam (residue block B5, original L186–192 → candidate L161–168): the original wraps its code block in a single collapsible （显示代码）; the candidate has an emptied collapsible pair at L163–164 (show/hide translated, immediately closed, wrapping nothing), then a `+ ソースコード` heading and a second collapsible that does wrap the code block (candidate L168–169). The code exhibit is preserved and reachable; the empty pair renders a stray toggle above it. Residue B72 (original L753 → candidate L1608) is the code block's closing seam — the `[[/code]]` line itself, unchanged in role, isolated by the differ because everything above it moved.
- Why: class R3's replaced-vs-dropped question is answered per item above; the empty collapsible is an assembly leftover, not a content change.
- Verify: candidate L161–169 against original L186–193.
- Disposition: **MINOR OBSERVATION (open)** — the empty collapsible husk at candidate L163–164, flagged in the lane report; it costs a stray toggle on the page and nothing else. No structure item was charged in the ledger.

## 9. Formatting only

- What: WS-ONLY fires 13 times (B56–B61, B63–B65, B67, B69–B71), all inside the code block: lines whose only change is whitespace, riding on the integration of section 3. Re-indentation pairings: 0.
- Why / Verify / Disposition: formatting-only by the classifier's normalization; any one of them can be spot-checked in diff.md. No disposition needed.

## 10. Porter annotations

- What: three annotation sites, all in Japanese. (1) The code-block banner (candidate L184–190): records that the original imports crimson-anemone's Basalt-derived CSS and the EN component CSS, that collapsible-sidebar and the Basalt base stay as imports while betterfootnotes and acs-animation are integrated into the file, and that images are re-hosted to the candidate's attachments — the audit trail for sections 3 and 4. (2) The `日本語フォント (JP localization)` comment at candidate L191, heading the JP font section of the block. (3) The two `//訳注://` notes in the body: candidate L39 (the theme-squares omission, section 2) and the note inside candidate L42 (the belief link conversion, section 7). The COMMENT-TEXT label (B52) is the banner region's comment mass.
- Why: each annotation sits at the locus of the judgment it records, which is what lets this package verify the judgments from the file alone.
- Verify: candidate L184–191, L39, L42.
- Disposition: annotations present and accurate against the diff.

## 11. Dispositions and exceptions

- HTTP-KEPT (derived presence, 1 occurrence, candidate L1128): adjudicated a classifier false fire. The line is `--old-money-mask-image:` with a `data:image/svg+xml` URI; the `http://` strings inside it are the W3C SVG namespace declarations (`xmlns='http://www.w3.org/2000/svg'`) inside the data URI, not an asset address. No http asset stands in the candidate.
- The jsdelivr stylesheet pair (candidate L2–3): KB-14 verbatim-import, DISPOSITIONED [GOSIGN2-LEDGER (c3) pattern-4 line; FIX4-REPOINT / FIX4-IWA §3] — third-party code with no JP candidate, kept at the original's addresses.
- The draft-host self-addresses (candidate L4, L9, L50, L1071, L1225, L1264): KB-41 class (iii) draft-stage forms of the candidate's own delivery and attachments; posting rewrites them (class (ii)).
- The theme-squares omission: dispositioned in section 2 on the KB-54-family ground stated there.
- The T2/T3 record for this theme (RENDER-ROWS-G (CN16)): sidebar-unreachable at 375/320 on page and sample, the runtime-hotlink site-theme chain (the KB-14 imports rendering), the candidate's fastly.jsdelivr.net reference (the same KB-14 pair), the sample credit-modal preview-form entry (standing disposition, GOSIGN-TESTS T2), and a T3 re-run with no new visual finding; coverage chromium-only (no WebKit verdict). These stand as classified render evidence; no item in (e) charges them beyond items 93/94.

## 12. Verification

- Package integrity: `original.txt` SHA-256 equals the `review/sources.tsv` mirror hash (5b1e7836…) and `candidate.txt` is byte-identical to `pages/theme:the-track-changers-jp.txt` (sha256 137195e1…); both verified at assembly and re-verified by `python3 review/build_review.py --check`. The stamp's STALE reading is expected (per-theme record) and is not a package defect.
- T1: baseline exit 1, 7 errors / 2 warns / 1 info (pseudo-ref×5, hotlink×2) [T1-ROWS row 203]. The pseudo-refs are the self-delivery address family of section 3 (the census there shows the named block is the stylesheet); the hotlinks are the KB-14 pair. FIX5-TEXTB records zero new checker errors.
- T2/T3: FINDINGS as in section 11 [RENDER-ROWS-G (CN16)], chromium-only coverage as recorded.
- T4 follow-up: the per-theme record re-derives items 93 and 94 from the bytes; both pass. The open flags from this package are the section-1 credit pointer (defect), the section-4 duplicated imports (minor), and the section-8 empty collapsible (minor observation).

## Per-theme record — the FIX5 closures, re-derived

Item 93 (class H) — untranslated Chinese edit-lock text in the candidate's CSS (ledger-time candidate L1567/L1588; the Basalt-derived lock messages, KB-18 surface).

- The re-judgement: GOSIGN2-LEDGER-SUPPLEMENT (a) item 93 — FIXED, wave FIX5-TEXTB §1, commit 3f328d8: the strings were translated with dustframe's reviewed wording, byte-for-byte.
- Verification against the bytes: the three strings stand in the candidate's lock region. (1) `div#lock-info::before` at candidate L1567: `あなたは15分間の占有ロックを保持しています。これにより、他の人が編集中のページを編集するのを防げます。\Aこのロックは ` — byte-identical to the reviewed wording in `pages/theme:dustframe-jp.txt` (its L3097), against original L712's Chinese. (2) `div#lock-info::after` at candidate L1582: ` 秒で失効します。` against original L727's ` 秒后失效。`. (3) The wait-state `::before` at candidate L1588: `ページを保存中……\Aこの表示が長時間続く場合は…` against original L733's Chinese. A census for the original strings (`锁定`, `正在编辑`) in the candidate returns nothing: no Chinese lock text remains. The fix is present and complete, in dustframe's wording as the supplement states.

Item 94 (class H) — dead prose links at ledger-time candidate L42: `belief` and `theme:old-money-theme`, neither existing on scp-jp (the candidate is theme:old-money-theme-jp), charged under P11.

- The re-judgement: supplement (a) item 94 — FIXED, FIX5-TEXTB §1, commit 3f328d8: belief (probe 404, no JP counterpart) converted to plain text with a translator's note; the old-money link repointed to theme:old-money-theme-jp.
- Verification against the bytes: candidate L42 carries both resolutions in one sentence — the hub reference stands as plain text （終無信仰設定） with the `//訳注://` note stating it was a link in the original and that no JP counterpart exists, and the design credit reads `[[[theme:old-money-theme-jp|Old Moneyテーマ]]]`. Commit 3f328d8's message confirms the wave's per-target treatment (repoint where the JP candidate exists, note where none exists). The fix is present and complete.

Post-FIX5 change: commit b5cb724 (the usage sweep) repointed this file's `{{ }}`-form usage example from `:scp-jp:theme:the-track-changers` to `:scp-jp:theme:the-track-changers-jp` (candidate L46) — a remaining plain-form reference of item 94's family, repaired by the sweep; it is the stamp's STALE cause and closes the last plain-name self-reference in the file.

## Post-package repairs (REFRESH3-J)

The items above describe this package as built. The repairs recorded below postdate the package build; `candidate.txt` has been recopied from the current canonical `pages/theme:the-track-changers-jp.txt` and `diff.md` and the verdict stamp regenerated with `python3 review/build_review.py`, so this package now documents the post-repair candidate. The regenerated stamp reads **STALE** by design: no re-judgement is fabricated here, and the frozen ledger (`GOSIGN2-LEDGER.md` + supplement, FIX5 head 435a6bb) remains the verdict record.

**FIX-RFIX16 Item 2 — credit pointer, both carriers named (landing fd36608, "pages: R-fix-16 flags repaired (foundation-sigma, track-changers)"; record FIX-RFIX16.md).** As built, the credit block's 著作権者 field read `原語版ページの作成者に同じ（scp-wiki-cn の theme:the-track-changers）` and the license box read `|author=scp-wiki-cn theme:the-track-changers の作者]]`; neither named anybody. The original names Mercuresphere in both corresponding places (credit block `**作者：**[[*user Mercuresphere]]`, original L29; banner "By Mercuresphere", original L196–198), and the candidate's own prose names him (L42). The remedy: credit field → `**著作権者:** [[*user Mercuresphere]]` (the file's own user-reference form), license-box parameter → `|author=Mercuresphere]]` (the population's plain-name form). The license-box author stays at candidate L1613, as the as-built sections 1/2 cite; the credit field's verified pre-edit locus was L18, not the L17 the batch recorded — the section-1 line reference above is corrected accordingly in this refresh.

**FIX-RFIX16 Item 3 — duplicated font imports removed (landing fd36608; record FIX-RFIX16.md).** As built, Inter was imported at old L173 (`wght@400;700`) and L181 (`wght@100..900`), and Fira Code at old L176 (bare `family=Fira+Code`, i.e. wght 400) and L179 (`wght@300..700`). In both pairs the first occurrence was the strict subset of the second, so the brief's "keep the first occurrence" and "keep the delivered set identical" could not both hold; the delivered-set invariant was kept by removing the two subset lines (old L173 and L176). The nine surviving imports deliver exactly the pre-edit union (Inter 100–900; Fira Code 300–700), each family once. The `&amp;` forms on the surviving lines (old L177–L180) were deliberately left — recorded in section 4, not a repair item here.

**FIX-RFIX16 Item 4 — empty collapsible husk removed (landing fd36608; record FIX-RFIX16.md).** As built, an emptied collapsible pair (`+ コードを表示` / `コードを隠す`, immediately closed) stood above the `+ ソースコード` heading and the load-bearing collapsible wrapping the code block (section 8, residue B5). The remedy removed exactly those two husk lines (verified pre-edit locus L163–164; the batch's L165–166 citation is corrected above in section 8 and here), leaving everything around them byte-identical. Per FIX-RFIX16.md the T1 finding set is unchanged (error 7 / warn 0 / info 1 before and after; the 2 jsdelivr hotlinks, 5 pseudo-refs and one `!important` info), with line numbers below the removals shifted by −4; class (i) 0 → 0. The section-1, section-4 and section-8 open flags are now resolved on current bytes.

## Change set outside the two diffed files

- The item-93 verification reads one external file: `pages/theme:dustframe-jp.txt` in this repository, whose reviewed lock wording is the supplement's stated source for the translation. No other file is part of this theme's change set; the KB-14 imports and the frame are shared infrastructure, other packages' subjects.

## Multi-wave provenance

- S2 port (LOCALIZE-S2-E): the translation, credit swap, component integration and delivery repointing.
- FIX4-REPOINT / FIX4-IWA §3: the KB-14 disposition of the jsdelivr pair (no file change).
- FIX5-TEXTB §1 (commit 3f328d8, 2026-11-17): items 93 and 94.
- Usage sweep (commit b5cb724, 2026-11-17): the `{{ }}`-form example repoint — the candidate's last change and the stamp's STALE cause.
- GOSIGN2 determination and go-sign (COMPLETION-REPORT §10, 2026-11-17): the ledger verdict the stamp records.

## Appendix — heuristic and residue adjudication

26 heuristic blocks and 2 residue blocks, resolved by shape:

- Shape 1 — body prose translation without anchors: the TRANS-UNANCHORED-only blocks B10, B14, B15, B23, B25, B27, B28, B29, B30, B31, B32, B33, B34, B35, B36, B37, B38, B45, B46, B47, B48, B49, B51. The examples body (headings, rule/blockquote/table instructions, specimen lines) translated from Chinese; the differ lost pairings where the Japanese sentence structure broke its anchors. Read against the mirror, each is the same content in Japanese; nothing was added, dropped or restructured. (B3, B7, B9, B52 and B73 also carry TRANS-UNANCHORED but are specific-labeled and adjudicated in sections 1, 2, 7, 4 and 1 respectively.)
- Shape 2 — residue B5 (original L186–192 → candidate L161–168): the code-display seam restructure adjudicated in section 8 (the emptied first collapsible and the added heading); the code exhibit itself is intact.
- Shape 3 — residue B72 (original L753 → candidate L1608): the code block's closing seam; the `[[/code]]` line, unchanged in role, isolated because the block above it grew (section 3). No content change.
- The WS-ONLY blocks (13) are specific-labeled formatting, counted in section 9; the TRANSLATION-ANCHORED blocks (23) are the anchored half of section 6's translation mass.

## License and attribution

- **Title:** 变轨 版式
- **Author:** Mercuresphere
- **Source:** https://scp-wiki-cn.wikidot.com/theme:the-track-changers — revision 34
- **License:** Creative Commons Attribution-ShareAlike 3.0 (CC BY-SA 3.0) — license deed: https://creativecommons.org/licenses/by-sa/3.0/
- **Adaptation:** This package holds a Sigma-10 migration port of the work; changes were made. See "Summary" and "Standing sections" in this README for what changed and why. Translator: AI (Muse and its delegated agents), per the campaign's standing attribution rule.
