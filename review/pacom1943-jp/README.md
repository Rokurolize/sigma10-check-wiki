# Review package — theme:pacom1943-jp

<!-- BEGIN GENERATED VERDICT STAMP — do not hand-edit; regenerate with review/build_review.py -->
## Verdict stamp
- Theme: theme:pacom1943-jp — origin KO, population #279 [GOSIGN2-LEDGER (b) row 279]
- Overall: STALE — candidate file changed since the verdict was computed (verdict against 435a6bb-era content, file sha256 now 6965955081a0ccc1910b7388d72af79d12f9c5f814cb5a99ffa0aeddf26127cb); verdict not carried over, re-judgement required
> verdicts below describe the pre-change file
- T1 (source check): FINDINGS (classified) — baseline 2026-11-16: exit 1, 8 errors / 1 warn / 1 info (pseudo-ref×8); standing classes dispositioned in register c1 [T1-ROWS row 249; GOSIGN2-LEDGER (b) row 279]
- T2/T3 (render, combined verdict): FINDINGS — [combined T2/T3] report `FINDINGS` — page-overflow 380px@320/375 (page) and 380px@320/375 + 906px@768 (sample); sample credit-modal (preview-form); T3 long headings run past the content column and are clipped at PC/tablet, wrap/cut at mobile. [RENDER-ROWS-2 (RENDER-S2-H (KO7))]
- Engine coverage: full matrix as run by the lane; coverage not separately caveated in the row [RENDER-ROWS-2 row]
- Credit modal: sample credit-modal errors dispositioned preview-form (credit:start-preview has no modal mechanism; GOSIGN-TESTS T2 amendment, 2026-11-16) [RENDER-ROWS-2 (RENDER-S2-H (KO7))]
- T4 (localize patterns + follow-up): FINDINGS — display-affecting findings: 1 [LOCALIZE-ROWS row 278, source LOCALIZE-S2-F]
- T5 (translation text): FINDINGS — the source reports judge T4/T5 jointly; one verdict word covers both [LOCALIZE-ROWS row 278]
- FIX5 re-judgement: item 106 (class F) DISPOSITIONED — FIX5-FUNC §8 (no edit): the two long headings are direct translations of original L30/L35; neither file carries a heading font-size/overflow/width rule; operative typography is inherited from the base in both versions [GOSIGN2-LEDGER-SUPPLEMENT (a) item 106]
- Computed against: canonical commit b4109ab7758a2904b5dbfff500e1438718099212; candidate file pages/theme:pacom1943-jp.txt sha256:6965955081a0ccc1910b7388d72af79d12f9c5f814cb5a99ffa0aeddf26127cb; record: GOSIGN2-LEDGER.md + GOSIGN2-LEDGER-SUPPLEMENT.md as of the FIX5 head 435a6bb
<!-- END GENERATED VERDICT STAMP -->

Status: complete (batch R-disp-9 lane, 2026-11-17)
Candidate: review/pacom1943-jp/candidate.txt (sha256 2e1e962ba6fc103306f63d35a86ba6aa4e312fb9edeab0bf69ba8e3a76f98078)
Original: theme:pacom1943 — scpko, revision 43 (sha256 d7cc9586e11070b0a6ef624f1e4857bcf6891b077dfbfc0bba19c7a383a0624a)
Classifier: classify_hunks.py 0.1.0; signature table 2026-11-17.1; patterns commit 9c5e9079afb01d30cb9fc4ef9d714e5591eb2ffa

| | |
|---|---|
| Original mirror | `review/pacom1943-jp/original.txt` — 2,941 bytes, 115 lines; SHA-256 equals the sources.tsv row (mirror store `orig-pacom1943-rev43.txt`, COPY class) |
| Candidate | `review/pacom1943-jp/candidate.txt` — byte-identical copy of `pages/theme:pacom1943-jp.txt` (4,250 bytes, 134 lines) |
| Diff | Tier 1: +65 / −46 lines (see diff.md) |
| Classification | 24 change blocks: 21 specific, 2 heuristic, 1 residue, 0 skipped (comment text) |
| Disposition re-derived | Ledger item 106 [F] (long-heading overflow) — DISPOSITIONED by FIX5-FUNC §8; ground re-measured on the package bytes and confirmed (per-theme record below) |
| Defect flags | F1 — both credit author carriers are pointers although the original names thd-glasses; F2 — the SCP-987-KO dedication link is a dead bare name in the JP environment (per-theme record) |

## Provenance

- Route: derived from the original at the reference revision. The mirror is the LOCALIZE-S2-F lane's source cache (`gosign2-lanes/lane-oc-gs-localize-s2-F/orig-pacom1943.txt`), hash-verified into the mirror store as a COPY.
- The sources.tsv note for this row is empty; there is no supersession claim to check against a follow-up artifact.

## Summary

A small KO variant theme: theme:pacom1943 is thd-glasses's 1943 palette-and-image variant of the same author's theme:pacom, dedicated to SCP-987-KO. The port is correspondingly small: the base include is repointed to theme:pacom-jp, the theme's own stylesheet moves to the draft host with its assets, the four font imports of the original's code block are dropped because the base candidate loads every one of those faces (with the recorded Gothic A1 substitution for UnJamoBatang), the usage text is translated, and the preview credit block and license box replace the info module. The theme's one blocking item is a render finding about its two long usage headings, dispositioned on the ground that the headings are the original's own, translated one-to-one, under typography neither file defines.

## Class summary

| Label | Blocks |
|---|---|
| BARE-RATE-DEL | 1 |
| COMMENT-TEXT | 1 |
| COMPONENT-SWAP | 3 |
| CREDIT-PREVIEW | 1 |
| CREDIT-PROSE | 1 |
| CSS-BODY | 1 |
| DELIVERY-HOST | 1 |
| DRAFT-HOST | 9 |
| FONT-IMPORT | 1 |
| IFTAGS | 1 |
| INCLUDE-REPOINT | 2 |
| INFO-DEL | 2 |
| LICENSE-BOX | 1 |
| SELF-DELIVERY | 2 |
| TASL-FIELDS | 1 |
| TRANS-UNANCHORED | 4 |
| TRANSLATION-ANCHORED | 2 |
| WS-ONLY | 5 |

Counts: 24 blocks, 21 specific, 2 heuristic, 1 residue, 0 skipped (comment text). Sections below are written from the classifier's per-block label sets, so a section can carry a class the skeleton listed under a different section's block.

## 0. Header / provenance

- Theme fullname: theme:pacom1943-jp. Original: theme:pacom1943, KO branch original on scpko, reference revision 43 (first-translation revision). Candidate file: pages/theme:pacom1943-jp.txt.
- Provenance route: derived from the original at the reference revision (see Provenance above); no production JP counterpart adoption (not an R4 row).
- Verdict: GOSIGN2-LEDGER (b) row 279: T1 FINDINGS (classified), T2/T3 FINDINGS, T4 FINDINGS, T5 FINDINGS, overall NOT PASS — OPEN items (e) at ledger time. The theme is not one of the 17 rerun themes; its render record is RENDER-S2-H (KO7). The single (e) item, 106 [F], was re-judged DISPOSITIONED by the supplement (FIX5-FUNC §8, no edit); sources.tsv verdict PASS.

## 1. Credit and attribution

- What: CREDIT-PREVIEW, TASL-FIELDS, CREDIT-PROSE, and INFO-DEL fire in B4 (orig L14 → cand L11-20): the info:start include is replaced by the credit:start-preview pair at cand L11-20 carrying the eight ruling-3 fields. タイトル is the page's own Japanese form 太平洋司令部 1943 テーマ; 原題 carries the original's Korean title; 作成年 2020; 初訳時参照リビジョン 43; 元記事リンク names https://scpko.wikidot.com/theme:pacom1943, the host recorded in sources.tsv. INFO-DEL fires again in B5 (orig L16-21 → cand L22-24): the info body (the image credits: the pixabay paper texture at orig L16-17, and orig L19's statement that all other image files were made by [[*user thd-glasses]]) and the info:end include are removed with the module. BARE-RATE-DEL fires in B6 (orig L26-28): the original's bare Rate ([[>]] [[module Rate]] [[/>]]) is removed; the preview credit module is rate-bearing (KB-09). LICENSE-BOX fires in B24 (orig L114 → cand L125-132): the license box at cand L127-132 carries one note entry (cand L130) stating that image and font sources follow the original page's own record, that the KO attachments are re-hosted on the candidate page, that webfonts are substituted with Google Fonts equivalents, and that images with no license statement in the original need the author's confirmation before posting. The pixabay credit and the thd-glasses image credit are preserved by that reference to the original's record rather than reproduced line by line.
- Why: P3/T1 block swap and the ruling-3 TASL record; KB-09; KB-63/KB-60 (license box in its settled JP form).
- Verify: grep the candidate for credit:start-preview / credit:end-preview / license-box-backend / license-box-end (one pair each) and for info:start / info:end (none remain); grep both files for [[module Rate]] (original 1, candidate 0).
- Disposition: ledger (c3) records P3 credit fields FIXED (credit waves; checker-verified) for this theme. The bytes support the fields' presence but not their content: both author carriers are pointers, flagged as F1 in the per-theme record (the checker verifies field presence, not field content; where the record and the bytes differ, this package follows the bytes). T7 credit CSS: neither side carries credit-button CSS of its own (grep creditButton: 0 in both files).

## 2. Includes and components

- What: the base include is repointed under ruling 1: [[include theme:pacom]] (orig L2, inside the hidden div at orig L1-3) → [[include theme:pacom-jp]] (cand L23, inside the hidden div at cand L22-24), the JP candidate of the same base by the same author. IFTAGS fires in B3: [[iftags +테마]] (orig L12) → [[iftags +テーマ]] (cand L9), closing at cand L134. INCLUDE-REPOINT fires in B7 and B8: the two usage exhibits' include lines, [[include :scpko:theme:pacom1943]] (orig L33 and L38) → [[include :scp-jp:theme:pacom1943-jp]] (cand L33 and L38). The skeleton lists B7/B8 under a COMPONENT-SWAP label; the label set for both blocks also carries INCLUDE-REPOINT and TRANSLATION-ANCHORED, and the substance is the exhibit repoint plus translation — no component swap in the ruling-4 sense occurs in this theme (COMPONENT-SWAP's third block is B5, the hidden-div seam of section 8, likewise a repoint of the base include, not a component port). No duplicated includes: the include census shows each live include once per side; the candidate's two :scp-jp:theme:pacom1943-jp occurrences are the two usage exhibits.
- Why: ruling 1 (cross-theme imports repoint to the JP fixed base candidate); P2/T2 tag localization (KB-08); P1 exhibit repoints.
- Verify: include census on both files; the base candidate theme:pacom-jp exists in the population (pages/theme:pacom-jp.txt) and is the file section 4's font census reads.
- Disposition: ledger (c3) P11 is DISPOSITIONED (sibling / batch-posting class) for this theme; the base repoint itself is the ruling-1 standard form.

## 3. Delivery and code loading

- What: original: head module-css (orig L4-10) importing own /1 from scpko.wikidot.com/local--code/theme%3Apacom1943/1 and carrying the .comments-box rule inline (orig L7-9); code-css (orig L41-113) holding the stylesheet. Candidate: head module-css (cand L1-3) importing own /1 from the draft host only; an interwiki-style frame the original does not carry (cand L5-8, priority=1, naming the same own /1), the population's standard second delivery channel; code-css (cand L45-124). SELF-DELIVERY fires in B2 and B3; DELIVERY-HOST in B2 (scpko → the JP draft host for the theme's own delivery). DRAFT-HOST fires 9 times: B2/B3 (the delivery address in the module and the frame) and B13, B16, B17, B19-B22, the seven asset URLs inside the code block (body_bg.jpg, report_bg.png, header.png twice, mobile_bg_s.png, mobile_bg.png, pacom.png), re-hosted from scpko.wdfiles.com/local--files/theme%3Apacom1943/ to sigma10-jp-test.wdfiles.com/local--files/theme%3Apacom1943-jp/. CSS-BODY's single block, B23 (orig L113 → cand L120-123), is the .comments-box rule relocated from the head module into the code block's tail: the rule is delivered on both sides, its channel changed from the inline module to the served stylesheet. Brace-depth scan: both files' CSS ends at depth 0 and never goes negative. The code-block bodies are otherwise line-identical modulo URLs (the set difference is exactly the font imports of section 4, the porter banner of section 10, and the relocated .comments-box rule).
- Why: P4/T9 host and local--code repoints (KB-41 draft-host form, class (iii)); KB-07 frame form.
- Verify: the candidate holds exactly one code block (cand L45, 78 content lines), so its /1 address names the stylesheet itself; the FIX-CODEADDR shapes do not occur. The .comments-box rule text is identical on both sides (orig L7-9 against cand L121-123).
- Disposition: the draft-host delivery lines are class (iii) draft-stage form (KB-41), recorded in section 11, not fixed.

## 4. Fonts and assets

- What: FONT-IMPORT fires in B11 (orig L55-58 → deleted). The original's code block imports four font stylesheets: Montserrat/Raleway/Roboto Mono and Nanum Myeongjo and Special Elite from Google Fonts, and UnJamoBatang from scpko.wdfiles.com/local--files/unfont/UnJamoBatang.css (orig L55-58). The candidate's code block imports none. Subsumption check against the base candidate the theme actually includes (pages/theme:pacom-jp.txt): its head module loads Noto Sans JP and Noto Serif JP (its L16-17), Gothic A1 (its L18), Montserrat/Raleway/Roboto Mono (its L19), Nanum Myeongjo (its L20), and Special Elite (its L21) — every face the original imported is loaded by the base candidate, with UnJamoBatang substituted by Gothic A1 under the base's own recorded substitution (its L23 comment states the scpko unfont direct link has no exception, so Google Fonts' Gothic A1 substitutes). Neither pacom file declares a font-family of its own (grep count 0 in both): the stacks that consume these faces live in the base on both sides, so the candidate's drop is a dedupe across the include chain, not a lost load. Assets: the seven re-hosts of section 3; the :root variables (orig L60-68) are carried byte-identical (cand L67-75).
- Why: P5/KB-04 font loads; KB-16's base-subtraction rule (a load the resolved base already makes is not re-made).
- Verify: grep @import in both code blocks (original 4, candidate 0) and in pages/theme:pacom-jp.txt (6 load lines at its L16-21); grep font-family in both pacom files (0 and 0).
- Disposition: the candidate's own banner (section 10) records the Gothic A1 substitution and its sameness with theme:pacom-jp's; the claim verifies against the base candidate's bytes. No font disposition stands against the theme itself; the (c2) record's font-host item is the environment-layer class of section 11.

## 5. Header, sidebar, site furniture

- What: none — no signature for this section fired over 24 change blocks, and the census confirms the ground: neither file carries header, sidebar, or top-bar rules of its own; the three @media blocks in each file (orig L90/97/104, cand L97/104/111) restyle only background images at widths, byte-identical on both sides. Furniture and heading typography are the base theme's on both sides (theme:pacom / theme:pacom-jp), which is also ground (c) of item 106 in the per-theme record.
- Disposition: none recorded against this section.

## 6. Text translation

- What: TRANSLATION-ANCHORED fires in B7 and B8 (the two usage sections); TRANS-UNANCHORED fires in B4, B9, and B24. The Korean usage section (orig L30-33) becomes + 使い方：太平洋司令部1943 CSSテーマ (cand L30-33) and the English section (orig L35-38) becomes + 使用方法：PACOM1943 CSSテーマ (cand L35-38), each section's bullets translated with it; the dedication line's link is carried byte-identical and is flag F2 (section 7). The code exhibit gains the population's exhibit furniture: the + ソースコード heading and the collapsible wrapper (cand L42-44). COMMENT-TEXT fires in B9: the original code banner (orig L44-49) is carried into the candidate's code block (cand L55-60) with its Korean title line and its English lineage text unchanged (R1 in-CSS text), below the added porter banner of section 10.
- Why: P10 body/usage translation (KB-18); R1 in-CSS text stated separately from reader-visible text.
- Verify: read the pairs in diff.md; heading levels and leading tokens confirm the pairings.
- Disposition: ledger (b) row 279 records T5 FINDINGS for this theme, closed by the (c3) items of section 11; no translation disposition stands beyond them.

## 7. Links

- What: the credit block's source link names the recorded host (section 1). The one prose link is the dedication: [[[scp-987-ko|SCP-987-KO]]] at cand L31, byte-identical to orig L31. In the original's environment that name is the KO article the theme was made for; in the JP environment the bare name resolves on scp-jp, where it does not exist (probe 2026-11-17: https://scp-jp.wikidot.com/scp-987-ko returns 404). Flagged as F2 in the per-theme record.
- Why: P11 — a prose link naming a page with no JP counterpart takes the absolutized-plus-annotation form (pattern 11's annotation branch), as applied to creature-jp's contest link in FIX-RDISP4 (absolutized to scpko with annotation).
- Verify: the probe above; grep the candidate for other bare-name links (none).
- Disposition: none recorded; F2 is this lane's flag.

## 8. Structure

- What: residue B1 (orig L1-3 → cand L1) is the head seam: the hidden base-include div moves from the file's first lines (orig L1-3) to below the credit block (cand L22-24), and the head module takes the head position; no content is lost in the move. Heuristic B9 (orig L41 → cand L41-52) is the code exhibit's restructure: the porter banner added above the carried original banner, under the new heading and collapsible of section 6. CSS-BODY's block B23 is the .comments-box relocation (section 3). Exhibit census: the two usage sections and the code exhibit are present at the aligned positions; nothing else in the original is an exhibit. The gate span: the original's gate opens at orig L12, after its delivery lines; the candidate's delivery lines (module, frame) likewise stand above its gate at cand L9, and both gates close at the file's last line.
- Why: R3 restructuring needs a stated ground per block; the localize.md closing rule (variable names, selectors, channel order preserved) holds — the stylesheet's rule order is unchanged (section 3's line-identity result).
- Verify: the census above, read off diff.md.
- Disposition: no structural disposition is recorded against this theme.

## 9. Formatting only

- What: WS-ONLY fires 5 times (B10, B12, B14, B15, B18): blank separator lines inside the code exhibit that are empty in the original carry a single trailing space in the candidate (cand L61, L65-66, L76, L80, L84, L92 region). No re-indentation blocks pair up.
- Why: R7 whitespace churn is stated so a reviewer can skip it.
- Verify: the five blocks in diff.md are whitespace-only by construction of the label.
- Disposition: none.

## 10. Porter annotations

- What: the code banner note (cand L46-51, inside B9) makes three claims. (a) The original is the same author's 1943 variant of theme:pacom with palette and images swapped: checks against the original's structure (its base include of theme:pacom at orig L2 and its own thin stylesheet layer) and its banner's lineage (orig L48). (b) The base CSS is loaded through the hidden include of theme:pacom-jp and is not contained in this file: checks at cand L22-24. (c) The font substitution (UnJamoBatang → Google Fonts' Gothic A1) is the same substitution theme:pacom-jp makes: checks against pages/theme:pacom-jp.txt L18 and its L23 comment. The license-box note (cand L130) is the TASL-adjacent record of section 1.
- Why: R2 additions are listed so they are never mistaken for original content or for translation; an annotation whose claims the bytes refute would be a flag, and all three claims here verify.
- Verify: read cand L46-51 against orig L2, orig L48, cand L22-24, and the base candidate's L16-23.
- Disposition: none.

## 11. Dispositions and exceptions

- Item 106 [F] (long-heading overflow): DISPOSITIONED by FIX5-FUNC §8 — re-derived in the per-theme record below.
- (c2) RENDER-S2-H (KO7): page-overflow 380px@320/375 (page) and 380px@320/375 + 906px@768 (sample), DISPOSITIONED in the cross-cutting families (KB-33/KB-34); sample credit-modal, DISPOSITIONED as the preview form's property (KB-32) [GOSIGN2-LEDGER (c2)].
- (c3) P1 DISPOSITIONED (posting-procedure convention class); P10 DISPOSITIONED (lane-recorded severity / specimen class); P11 DISPOSITIONED (sibling / batch-posting class) [GOSIGN2-LEDGER (c3)].
- The candidate's own draft-host delivery and asset lines (section 3) are class (iii) draft-stage form (KB-41): recorded here, not fixed; posting rewrites them (class (ii)).
- HTTP-KEPT: no instance derived for this package.

## 12. Verification

- T1: FINDINGS (classified) per the stamp's baseline (GOSIGN2-LEDGER (b) row 279). T2/T3: FINDINGS per RENDER-S2-H (KO7) with the (c2) dispositions of section 11. T4: FINDINGS, closed by the (c3) items; T5: FINDINGS, same closure.
- Lane re-runs (2026-11-17, this package's bytes): original SHA-256 against sources.tsv (equal); candidate byte-identity against pages/theme:pacom1943-jp.txt (cmp, equal); the heading-pair and heading-rule censuses behind item 106 (section per-theme record); the font load/apply census against the base candidate (section 4); the code-block line-identity comparison modulo URLs (section 3); brace-depth scans (end 0, min 0, both files); include, footnote (0 on both sides; no footnoteblock on either side), and creditButton censuses; the scp-987-ko probe behind flag F2. Package acceptance (build_review.py --check set comparison, classify freshness) is recorded in the batch report BATCH-RDISP9.md.

## Per-theme record — FIX5 item re-derived

### Item 106 [F] — DISPOSITIONED (FIX5-FUNC §8, no edit)

- The charge: long headings run past the content column and are clipped at PC/tablet widths, and wrap/cut at mobile (render T3). At ledger time no disposition ground was recorded in the row and no fix wave had addressed the heading overflow.
- The disposition's ground (GOSIGN2-LEDGER-SUPPLEMENT, item 106): the two long headings are direct translations of original L30/L35; neither file carries a heading font-size/overflow/width rule; operative typography is inherited from the base in both versions.
- Re-measurement on this package's bytes (2026-11-17): (a) the heading pairs are one-to-one at the same positions in the same sections: orig L30 "+ 사용 방법: 태평양사령부 1943 CSS 테마" → cand L30 "+ 使い方：太平洋司令部1943 CSSテーマ"; orig L35 "+ How to use: PACOM 1943 CSS THEME" → cand L35 "+ 使用方法：PACOM1943 CSSテーマ". The candidate's headings are the original's two usage headings translated, neither lengthened by added wording nor shortened. (b) The rule census: grep for font-size, overflow, h1, and width over both files returns only the three @media width conditions on each side (orig L90/97/104, cand L97/104/111), which are viewport conditions on background-image rules and are byte-identical across the port; no heading font-size, overflow, or width rule exists in either file, and neither file declares a font-family anywhere (grep count 0 on both sides). (c) Base inheritance: the original hidden-includes theme:pacom (orig L2); the candidate hidden-includes its JP candidate theme:pacom-jp (cand L23); heading typography comes from that base in both versions, and the base swap is the ruling-1 repoint, not a typography change.
- Second-reviewer walk: the ground is checkable from this package alone — read the two heading pairs and run the grep census; every element of the ground is a byte fact, not a judgment call. The overflow is a property of the original's own long headings under the base's typography, present in the original's rendering on the same terms; a port-side repair (a heading font-size or overflow rule of the port's own invention) would add CSS the original does not carry, to fix the original's own text at the original's own sizes. The disposition holds.

### Defect flags (candidate not edited by this lane)

- F1 — both credit author carriers are pointers although the original names the author. Candidate cand L16: 著作権者： 原語版ページの作成者に同じ（scpko の theme:pacom1943）; license-box author parameter, cand L128: |author=scpko theme:pacom1943 の作者. The frozen original names thd-glasses in two carriers: the info body at orig L19 ("기타 이미지 파일은 모두 [[*user thd-glasses]]가 제작함" — all other image files were made by thd-glasses) and the code banner at orig L47 ("Edited by thd-glasses."). This is the credit-pointer family: the original names them, the fields name nobody. The population's remedy form is on record in many landed repairs (e.g. theme:07k-jp, whose credit field and license-box author parameter were both set to thd-glasses in FIX-07K). The ledger (c3) formula "P3 credit fields FIXED (credit waves; checker-verified)" is the prose the bytes overtake: the fields are present and checker-verified, their content is the pointer.
- F2 — the dedication link is a dead bare name in the JP environment. Cand L31: "* [[[scp-987-ko|SCP-987-KO]]]のための専用テーマです。", byte-identical to orig L31. Probe (2026-11-17): https://scp-jp.wikidot.com/scp-987-ko returns 404; no JP counterpart page exists under that name, and no pacom-style counterpart name is in the population. The remedy form is pattern 11's annotation branch (absolutize to the scpko original with the （韓国語版） annotation), as applied to creature-jp's contest link in FIX-RDISP4.

### Post-package repairs (REFRESH3-L)

The items above describe this package as built. The repair recorded below postdates the package; `candidate.txt` has been recopied from the current canonical `pages/theme:pacom1943-jp.txt` and `diff.md` and the verdict stamp regenerated with `python3 review/build_review.py`, so this package now documents the post-repair candidate. The regenerated stamp reads **STALE** by design: no re-judgement is fabricated here, and the frozen ledger (`GOSIGN2-LEDGER.md` + supplement, FIX5 head 435a6bb) remains the verdict record.

**FIX-RDISP9, landing `b4109ab` (report `R/review-scout/FIX-RDISP9.md`).** Three candidate lines (+3/−3 on this file), postdating this package's build at `b5cb724`.
- **F1 — both credit carriers name thd-glasses.** The frozen original names thd-glasses in its info body (L19) and code banner (L47 "Edited by thd-glasses."). The candidate's two carriers held pointers: credit block (L16) → `**著作権者:** [[*user thd-glasses]]` and license box (L128) → `|author=thd-glasses]]`, the population's forms for this author (FIX-07K).
- **F2 — dedication link absolutized with the Korean-version annotation.** L31 (formerly byte-identical to original L31) named `[[[scp-987-ko|SCP-987-KO]]]`, which probes 404 on scp-jp and has no JP counterpart. Pattern 11's annotation branch (the creature contest-link precedent) gives `[[[https://scpko.wikidot.com/scp-987-ko|SCP-987-KO]]]（韓国語版）`, target unchanged in substance.
Checker per the report: plain error 8 / warn 0 / info 1 unchanged (all class (iii) pseudo-refs, class (i) 0); links error 8 / warn 1 / info 1 → 8 / 0 / 1, the removed warn being the dead dedication link's own finding; no new finding of any class.

## Appendix — residue blocks

The 2 heuristic blocks and the single residue block are the delivery seams of sections 3 and 8; there is no unassigned translation mass (the translation blocks are specific-labeled).

- B1 (residue; orig L1-3 → cand L1): the hidden base-include div's relocation from the file head to below the credit block. Assigned to section 8 (and the repoint itself to section 2).
- B9 (heuristic; orig L41 → cand L41-52): the code exhibit's opening restructure — porter banner added, original banner carried, heading and collapsible added. Assigned to sections 6, 8, and 10. The classifier's "porter-visible only; labeled and skipped by design" note refers to the banner's visibility class, not to missing content.
- B23 (heuristic; orig L113 → cand L120-123): the .comments-box rule's relocation into the code block's tail. Assigned to section 3 (its CSS-BODY label is the skeleton's primary; the substance is the delivery-channel move).
