# Review package — theme:a-midnight-invitation-jp
New to this package's shorthand? Read the notation key first: [How to read a review package](../HOW-TO-READ.md).

<!-- BEGIN GENERATED VERDICT STAMP — do not hand-edit; regenerate with review/build_review.py -->
## Verdict stamp
- Theme: theme:a-midnight-invitation-jp — origin KO, population #250 [GOSIGN2-LEDGER (b) row 250]
- Overall: STALE — candidate file changed since the verdict was computed (verdict against 435a6bb-era content, file sha256 now 4b82f12bd2f42a26dcad94b4d5642e741e8ec0a123c31f1b61c5f5769d65faa7); the verdicts below were computed against that pre-change file, and the record verdict stands: a candidate revised through the campaign's recorded repairs is posted like a PASS row, with the change recorded in its package
- T1 (source check): FINDINGS (classified) — baseline 2026-11-16: exit 1, 4 errors / 2 warns / 1 info (pseudo-ref×4); standing classes dispositioned in register c1 [T1-ROWS row 233; GOSIGN2-LEDGER (b) row 250]
- T2/T3 (render, combined verdict): FINDINGS — [combined T2/T3] report `FINDINGS` — sample credit-modal (preview-form) + page-overflow 324px@320 + 884px@768; T3 stock-header SCP財団 wordmark and nav render in very light gray on near-white at all 8 viewports, nearly illegible (theme-specific, §1 contrast). [RENDER-ROWS-2 (RENDER-S2-H (KO1))]
- Engine coverage: full matrix as run by the lane; coverage not separately caveated in the row [RENDER-ROWS-2 row]
- Credit modal: sample credit-modal errors dispositioned preview-form (credit:start-preview has no modal mechanism; GOSIGN-TESTS T2 amendment, 2026-11-16) [RENDER-ROWS-2 (RENDER-S2-H (KO1))]
- T4 (localize patterns + follow-up): FINDINGS — display-affecting findings: 1 [LOCALIZE-ROWS row 249, source LOCALIZE-S2-F]
- T5 (translation text): FINDINGS — the source reports judge T4/T5 jointly; one verdict word covers both [LOCALIZE-ROWS row 249]
- FIX5 re-judgement: item 100 (class E) DISPOSITIONED — FIX5-CONTRB (no edit, no commit): colour diff vs original consists only of the two sanctioned draft-host asset URLs; the pale wordmark is tied by the render report itself to the deferred logo/background 404s (KB-58) [GOSIGN2-LEDGER-SUPPLEMENT (a) item 100]
- Computed against: canonical commit a729077c4be28c95b81b8c396a7517c51f5176e1; candidate file pages/theme:a-midnight-invitation-jp.txt sha256:4b82f12bd2f42a26dcad94b4d5642e741e8ec0a123c31f1b61c5f5769d65faa7; record: GOSIGN2-LEDGER.md + GOSIGN2-LEDGER-SUPPLEMENT.md as of the FIX5 head 435a6bb
<!-- END GENERATED VERDICT STAMP -->

## Status

| | |
|---|---|
| Verdict | **PASS** — go-sign (this theme is one of the 286 of 286 pass-eligible themes) |
| Blocking items at ledger time | GOSIGN2-LEDGER.md §(e) item 100 [E] — stock-header wordmark and nav in very light gray on near-white at all 8 viewports, nearly illegible, recorded as theme-specific (KB-28 contrast family) |
| Re-judgment | GOSIGN2-LEDGER-SUPPLEMENT.md item 100: **DISPOSITIONED** (FIX5-CONTRB, no edit), on the two-URL colour-diff ground re-derived in the per-theme record below |
| Standing items | **DISPOSITIONED** — sample credit-modal errors (preview-form property, ruling 5); page-overflow 324px@320 + 884px@768 (KB-33/KB-34 families); T1 pseudo-ref×4 (class (iii) draft form). Two defect flags are carried by this package, neither dispositioned: the credit block's 著作権者 field and the license box's author parameter name nobody, where the original names its author (section 1); and the visited-link exhibit names a page the T1 checker reports missing on scp-jp (section 7, minor) |
| Go-sign basis | COMPLETION-REPORT.md §10 (go-sign issued; 81 FIXED / 26 DISPOSITIONED / 0 OPEN across the sweep) |
| Named exception | None for this theme (the sweep's single named exception is theme:amethyst-v2, which has no candidate) |

## Provenance

| | Original | Candidate |
|---|---|---|
| Page | theme:a-midnight-invitation | theme:a-midnight-invitation-jp |
| Wiki | scpko.wikidot.com | SCP-JP Sigma-10 candidate (canonical repo) |
| Reference revision | 20, as recorded in the candidate's credit block (初訳時参照リビジョン: 20, candidate L18) and in review/sources.tsv | — |
| Source of this copy | Mirror store `review-mirrors/orig-a-midnight-invitation-rev20.txt`, fetched once by the LOCALIZE-S2-F lane at rev 20 | Canonical file `pages/theme:a-midnight-invitation-jp.txt`, copied at worktree HEAD 9005272; the file's last content change is commit b5cb724 (usage-example sweep, one line), the stamp's computed-against commit |
| Lines / bytes | 600 lines / 11,088 bytes (the last line carries no trailing newline) | 627 lines / 12,734 bytes |
| SHA-256 | 23e4c7e24b45b663b1ef33fa588994421d792b90707c5f0d5ab90aa3dedc6d01 | 9fad8fad8dcae7ff668bd249ed9be56d8933dec4c095176d6aa33ee27519e2a0 |

Package files: `original.txt` and `candidate.txt` as tabled above; `classification.json` and the skeleton behind this README are from classify_hunks.py 0.1.0, signature table 2026-11-17.1, patterns commit 9c5e9079afb01d30cb9fc4ef9d714e5591eb2ffa.

## Summary

A Midnight Invitation is a standalone KO theme (no base theme), and the port preserves its topology exactly: a head `[[module CSS]]` importing the page's own code block, the documentation body, and one large `[[code type="css"]]` exhibit carrying the theme CSS — the classifier's topology pass matches every component by kind and detects no move. What changes is the language and the hosts: the body is translated in full, delivery and the two header assets move to the draft host, the bare Rate and the empty info pair give way to the preview credit block, and a frame include and a license box are added. The theme's only blocking item was the pale stock header, dispositioned because the entire colour diff against the original is the two sanctioned draft-host asset URLs and the wordmark is a transparent placeholder over the deferred logo image — re-derived from this package's two files in the per-theme record. The verdict stamp reads STALE because the usage-example sweep changed one line after the verdict (commit b5cb724); that delta touches no colour surface. Two attribution defects stand against the candidate (section 1); they do not touch the disposition's ground.

## 0. Header / provenance

- Delivery: no relocation detected between the sides; each side's components match by kind.

- **Provenance route:** derived from the branch original at the reference revision (theme:a-midnight-invitation rev 20 on scpko). This is not an R4 production adoption: no production JP counterpart exists in the record for this theme, and the candidate's body is the Stage 2 KO1 localization of the KO original. The evidence is threefold and mutually consistent: review/sources.tsv keys the row `standard` with the mirror's SHA-256 equal to this package's original.txt; the candidate's credit block records 初訳時参照リビジョン: 20 (candidate L18); and the T4 follow-up diff shows no change past the reference — the LOCALIZE-S2-F lane's follow-ups print revN → revN, no change, for all 39 KO originals in its scope — so the mirror in this package is also the current original.

## Class summary

| Label | Blocks |
|---|---|
| BARE-RATE-DEL | 1 |
| COMMENT-TEXT | 1 |
| COMPONENT-SWAP | 1 |
| CREDIT-PREVIEW | 1 |
| CREDIT-PROSE | 1 |
| CSS-BODY | 1 |
| DELIVERY-HOST | 1 |
| DRAFT-HOST | 5 |
| DUPIMPORT-DEL | 1 |
| ESCAPED-INCLUDE | 1 |
| EXHIBIT-RESTRUCTURE | 1 |
| FONT-IMPORT | 2 |
| IFTAGS | 1 |
| INCLUDE-REPOINT | 1 |
| INFO-DEL | 1 |
| JPFONT-LOAD | 1 |
| LICENSE-BOX | 1 |
| SELF-DELIVERY | 2 |
| TASL-FIELDS | 1 |
| TRANS-UNANCHORED | 12 |
| TRANSLATION-ANCHORED | 4 |
| WS-ONLY | 17 |

Counts: 38 blocks, 32 specific, 6 heuristic, 0 residue, 0 skipped (comment text).

## 1. Credit and attribution

- CREDIT-PREVIEW (A): Credit block swap (P3/T1): the JP environment's preview credit module is the rate-bearing form; the branch-original credit module does not render here.
  Verify: Re-run the T1 checker (check_source.py); the credit includes must resolve on scp-jp.
  - B3: orig 7-7 -> cand 11-20 (body -> body)

- BARE-RATE-DEL (B): Duplicate bare Rate removed (KB-09, ledger class B): the preview credit module is already rate-bearing, so a second bare Rate module double-renders the widget.
  Verify: Grep both sources for [[module Rate]]; the candidate must hold none outside labelled exhibits.
  - B4: orig 9-12 -> cand 22-22 (body -> body)

- INFO-DEL (A): Info-module residue removed (P3, ledger class C): the old info module pair is not part of the JP environment's furniture.
  Verify: Grep the candidate for info:start / info:end includes; none may remain.
  - B5: orig 14-18 -> cand 24-24 (body -> body)

- LICENSE-BOX (A): License box (T4, KB-63/KB-60): the license box must be present in its settled JP form, restored where the port dropped it.
  Verify: KB-63 recipe: license-box includes present in the candidate; form judgment per KB-60.
  - B38: orig 598-598 -> cand 620-625 (code-css -> body)

- **What (the block itself):** B3 (which also carries CREDIT-PROSE, TASL-FIELDS and TRANS-UNANCHORED) replaces the original's title line with the preview credit block (candidate L11–20), carrying all eight TASL fields: タイトル 真夜中の招待 テーマ (L12 — the Japanese form of the original's title, also carried as 原題 한밤중의 초대 CSS 테마 at L15), 翻訳責任者 AI (L13, ruling 3), 翻訳年 2026 (L14), 著作権者 (L16 — see the flag below), 作成年 2022 (L17), 初訳時参照リビジョン 20 (L18), 元記事リンク (L19) whose host is the recorded host scpko.wikidot.com and whose link text is the 原題. The original carries no credit block; its attribution is the intro sentence (original L20) and the CSS banner (original L56–67), both discussed below. The bare Rate div (original L9–12) is deleted (B4) because the credit module is rate-bearing; the empty `info:start`/`info:end` pair (original L17–18) is deleted (B5). Their bold labels survive as empty labels — **評価モジュール:** (candidate L24) and **クレジット付き評価モジュール:** (candidate L26) — the vestigial-label residue the localize lane recorded for this theme by name (LOCALIZE-S2-F cross-cutting finding 4: "removed Rate/info but left the empty labels (a-midnight-invitation, …)"); cosmetic, recorded at that weight. The license box (B38; candidate L620–625, `license-box-backend` / `license-box-end`, both components confirmed present on scp-jp by the S2-F lane's probes) is added at the tail; the original carries no license-box markup, its license content being the banner's CC BY-SA 3.0 line and pxhere background credit (original L64–66), which the candidate retains inside the CSS (candidate L85–87).
- **DEFECT FLAG — the author fields name nobody.** The candidate's 著作権者 field (candidate L16) reads 「原語版ページの作成者に同じ（scpko の theme:a-midnight-invitation）」 — "same as the creator of the original-language page". The original names its author in two places: the intro, "한밤중의 초대 CSS 테마는 [[*user c_bonefish]]가 … 제작하였습니다" (original L20), and the banner, "Created by c_bonefish" (original L60), with "Base Code by Denevola" (L61) and "Logo by 035SL" (L62) beside it. The license box repeats the pointer shape in its author parameter, `|author=scpko theme:a-midnight-invitation の作者` (candidate L621, "the author of scpko theme:a-midnight-invitation"), and its attribution prose (candidate L623) likewise defers to the original page's statements for image and font credit. The information is on the page — the candidate's own intro names c_bonefish (candidate L28) and its CSS retains the banner (candidate L81–83) — but both TASL author fields are pointers where the original names a person. The localize lane charged this family at population level, naming this theme (LOCALIZE-S2-F cross-cutting finding 9 lists a-midnight-invitation among the ports whose §3 author is the vague 「原語版ページの作成者に同じ（scpko の …）」 form), and the theme's T4 row records the same item (型3: §3 著作権者 vague, attribution incomplete). The ledger register's "P3 credit fields FIXED (credit waves; checker-verified)" settles field *presence* — the checker verifies the eight fields exist — not author naming; on the bytes, the naming defect stands. This package flags it for the coordinator with both sides' exact text; the candidate is not edited here.
- **Why:** P3/TASL (ruling 3): the credit block is the port's redistribution record; an author field that names nobody fails the A of TASL even when every field is present.
- **Verify:** Read candidate L11–20 and L620–625 against original L20 and L56–67; `grep -n 'module Rate\|info:start' candidate.txt` returns nothing.
- **Disposition:** P3 FIXED per the register as to field presence [GOSIGN2-LEDGER.md §(c3), a-midnight-invitation row]; the author-naming defect is **flagged, not dispositioned** — no record dispositions it, and the (c3) FIXED does not reach it (per-theme record, discrepancy 1).

## 2. Includes and components

- COMPONENT-SWAP (B): Component swap to a JP port (T8, ruling 4): the campaign component candidate replaces the branch component it ports.
  Verify: The swapped target is in the campaign component inventory and exists on the check wiki.
  - B7: orig 22-23 -> cand 28-31 (body -> body)

- **What:** B7 (which also carries ESCAPED-INCLUDE, INCLUDE-REPOINT and TRANS-UNANCHORED) covers the intro and usage lines. The intro's hub link changes from the original's absolute KO URL, `[[[http://scpko.wikidot.com/midnight-club-hub|심야클럽]]]` (original L20), to the same-site JP page name `[[[midnight-club-hub|深夜クラブ]]]` (candidate L28); `midnight-club-hub` is confirmed present on scp-jp (LOCALIZE-S2-F dependency probes), so the repointed link resolves. The usage line changes from `@@[[include :scpko:theme:a-midnight-invitation]]@@` (original L23) to `@@[[include :scp-jp:theme:a-midnight-invitation-jp]]@@` (candidate L31) — the branch prefix by the port, the `-jp` suffix completed by the usage-example sweep (commit b5cb724, the stamp's STALE delta). The remaining includes are treated at their own sections: the frame (section 3), the image-block exhibit (section 8), the credit and license-box includes (section 1).
- **Why:** Ruling 1 — cross-references name the JP environment's pages, not the branch original's; a usage example that names a page which will not exist under that name teaches a broken include.
- **Verify:** Read candidate L28–31 against original L20–23; the hub target's existence is the S2-F probe cited above.
- **Disposition:** No ledger item charges these repoints; the usage line's final form is the population sweep's recorded remedy (b5cb724). Standing.

## 3. Delivery and code loading

- DELIVERY-HOST (A): Base/host repoint (P4/T9): deliveries are served from the JP hosts in this environment.
  Verify: Resolve the new host path; a kept old-host line is a class (ii) posting matter, recorded in section 11.
  - B1: orig 2-2 -> cand 2-2 (module-css -> module-css)

- SELF-DELIVERY (A): Own code-delivery import changed (P4): the page's own local--code delivery is its live CSS channel.
  Verify: The named delivery resolves on the draft host and serves the current candidate body.
  - B2: orig 5-5 -> cand 5-9 (body -> body)

- DRAFT-HOST (A): Draft-stage form (KB-41, class (iii)): the candidate's own local--code on the draft host is sanctioned at draft stage.
  Verify: Recorded as a disposition in section 11, not fixed; posting rewrites it (class (ii)).
  - B18: orig 73-73 -> cand 93-93 (code-css -> code-css)
  - B19: orig 79-79 -> cand 99-99 (code-css -> code-css)

- **What:** the delivery topology is unchanged — the classifier detects no move, and each side's components match by kind (head module-css + one code-css exhibit). B1: the head module's self-delivery import is repointed from the original's host to the draft host, `https://scpko.wikidot.com/local--code/theme%3Aa-midnight-invitation/1` (original L2) → `https://sigma10-jp-test.wdfiles.com/local--code/theme%3Aa-midnight-invitation-jp/1` (candidate L2). The address names code block 1, and block 1 is the stylesheet on both sides: census — exactly one code block in each file, both `[[code type="css"]]` (original L55, candidate L67). This is the settled self-delivery form of the code-address audit, not the orphaned-pointer shape. B2 (which also carries SELF-DELIVERY, DRAFT-HOST and IFTAGS): the candidate adds the translation-module frame before the gate, `[[include :scp-jp:component:interwiki-style | priority=1 | theme=<the same draft-host /1 address>]]` (candidate L5–8), and the gate tag localizes (`+테마` original L5 → `+テーマ` candidate L9). The frame and the head module name the same block; the CSS itself is carried once, in the exhibit. Placement parity, checked explicitly: in both files the head module sits before the gate and the exhibit inside it (original gate L5, exhibit L55; candidate gate L9, exhibit L67) — the S2-F lane recorded this placement across all 39 KO candidates and judged it fine. B18/B19 are the two header asset URLs, treated in section 4 and load-bearing in the per-theme record. The remaining DRAFT-HOST occurrences in the label counts sit inside B1, B2 and B9's spans (the head import, the frame address, and the image-block exhibit's asset).
- **Why:** P4 — the page's own local--code delivery is its live CSS channel; the failure prevented is a delivery address naming a block that does not hold the CSS. The draft host is the sanctioned draft-stage form (KB-41).
- **Verify:** Code-block census as above; read candidate L1–9 against original L1–5; the T1 checker's four pseudo-ref errors are exactly these draft-host addresses (section 12).
- **Disposition:** The draft-host lines are class (iii) draft form, rewritten to the production host at posting (class (ii)); they are recorded as dispositions in section 11, not fixed.

## 4. Fonts and assets

- JPFONT-LOAD (A): JP font load added (P7/T5, KB-16): Japanese text needs a JP typeface loaded, and the resolved base may not load one.
  Verify: KB-16 recipe with base subtraction: the resolved base does not already load the family.
  - B16: orig at 56 -> cand 68-76 (body -> code-css)

- FONT-IMPORT (B): Other font-load change (P5, KB-04): malformed family parameters (a hyphen for a +) make the load fail.
  Verify: KB-04: the family parameter form; the deciding evidence is the load probe (400 vs 200).
  - B17: orig 69-69 -> cand at 90 (code-css -> body)

- **What:** B16 (which also carries FONT-IMPORT, COMMENT-TEXT and TRANS-UNANCHORED) opens the candidate's delivered code block with three Google Fonts imports: Noto Sans JP (candidate L68) and Noto Serif JP (candidate L69) added, and the original's Vollkorn SC (candidate L70) carried. B17 is that Vollkorn SC import's relocation: in the original it sits below the banner comment's opening (original L69); in the candidate it joins the import group at the block head. Census: exactly one Vollkorn SC load on each side — nothing duplicated, nothing dropped (the DUPIMPORT-DEL label fires on the relocation's shape; the current bytes hold no duplication). The measured limit, stated plainly: **neither file contains any `font-family` declaration** (grep: 0 on both sides), so no stack in the theme applies any of the three families — the original's Vollkorn SC load has exactly the same in-file posture. The JP loads sit in the live channel (code block 1, imported by the head module), not in an inert one, and the localize lane judged this population shape — Noto Sans/Serif JP imported but unreferenced in-file — "harmless but sloppy" at cross-cutting level (LOCALIZE-S2-F finding 8). This package records the supplement with its measured limit at that weight, not as a defect. Assets: the two header images are repointed from the KO host to the draft host — background.png (original L73 → candidate L93) and logo.png (original L79 → candidate L99) — the sanctioned draft form of the deferred re-hosting state (KB-58), and the image-block exhibit's logo.png is repointed the same way (original L28 → candidate L36). The banner's pxhere background-image credit (original L64 → candidate L85) is a citation inside a comment, not an embed, and is retained as-is.
- **Why:** P7/KB-16 (patterns/ at commit 9c5e9079afb01d30cb9fc4ef9d714e5591eb2ffa): the JP families are loaded in the delivered channel so the environment's base stacks can reach them; the asset repoints keep the theme's images loading from the JP-side draft host rather than hotlinking the KO branch.
- **Verify:** `grep -n '@import' candidate.txt` (L68–70) against original.txt (L69); `grep -c 'font-family' ` on both files (0 and 0); read candidate L93/L99 against original L73/L79.
- **Disposition:** No ledger item charges the font or asset lines; the two asset URLs are the dispositioned draft-host form (section 11) and are the whole colour diff of the per-theme record.

## 5. Header, sidebar, site furniture

none — no signature for this section fired over 38 change blocks, and the ground is measurable: the furniture rules are carried byte-identically apart from the section 9 whitespace. The header block (original L77–83 → candidate L97–103), the wordmark rules (original L85–107 → candidate L105–127), the login/search set (original L110–151 → candidate L130–171), the top bar (original L178–215 → candidate L198–235) and the sidebar (original L302–360 → candidate L322–380) match declaration for declaration — the census in the per-theme record covers every colour/background-bearing declaration in both files and finds only the two asset URLs different. The charged paleness lives on this surface and is treated in section 11 and the per-theme record, not here.

## 6. Text translation

- TRANS-UNANCHORED (C): Translation-shaped change without anchors (P10, KB-18): restructured lines are the queue where restorations and exhibit changes hide.
  Verify: Writer confirmation against the mirror, line by line.
  - B6: orig 20-20 -> cand 26-26 (body -> body)
  - B11: orig 41-41 -> cand 49-49 (body -> body)
  - B12: orig 43-44 -> cand 51-52 (body -> body)
  - B13: orig 46-46 -> cand 54-54 (body -> body)
  - B15: orig at 55 -> cand 63-66 (body -> body)

- TRANSLATION-ANCHORED (B): Prose/usage translation (P10, KB-18): reader-visible text localizes; anchored pairs are one-to-one translations.
  Verify: Read the pairs; the anchors (leading token, CSS property, selector, heading level) confirm the pairing.
  - B8: orig 26-26 -> cand 34-34 (body -> body)
  - B10: orig 30-35 -> cand 38-43 (body -> body)
  - B14: orig 52-52 -> cand 60-60 (body -> body)

- **What:** the body is translated in full. Anchored pairs: the section headings 페이지 요소 → ページ要素 (B8; original L26 → candidate L34), 제목1–6 → 見出し1–6 (B10; original L30–35 → candidate L38–43), and CSS 테마 코드 → CSSテーマコード (B14; original L52 → candidate L60); the image-block caption 헤더 이미지 → ヘッダー画像 rides inside B9 (section 8). The unanchored mass (12 blocks, most of them riding inside other labels' spans) resolves line by line in the appendix; its substance is the intro (original L20 → candidate L28 — the author named, the hub link repointed, section 2), the usage prose (original L22 → candidate L30), the tabview contents (placeholder text, link labels, footnote — appendix R2–R4), and the credit/license prose (section 1). The page title (candidate L22, "+ A Midnight Invitation CSSテーマ") keeps the theme's English name as its identity string, while the credit title uses the Japanese form （真夜中の招待 テーマ, candidate L12); the original's title is its Korean name (original L7). The CSS banner comment is retained in its original Korean/English form as the attribution record (candidate L77–88), under the porter banner of section 10. No mistranslation or untranslated reader prose was found in the carried body; the one translation-adjacent defect is the credit field's vagueness (section 1), which is an attribution failure, not a translation failure.
- **Why:** P10/KB-18: reader-visible text localizes one-to-one where the structure allows; unanchored blocks are the queue where silent drops hide, so each is resolved by name in the appendix.
- **Verify:** Read the pairs at the lines cited; the appendix resolves every heuristic block in this section.
- **Disposition:** T5 judged jointly with T4: FINDINGS whose one display-affecting item is the section 1 credit item （型3). Standing at that weight.

## 7. Links

The skeleton prints "none" for this section; the candidate's links are few and are recorded here.

- **What:** three link surfaces. (1) The credit's 元記事リンク (candidate L19): host scpko.wikidot.com, the recorded host, link text the 原題 — correct form. (2) The intro's hub link (candidate L28): repointed to a page confirmed present on scp-jp (section 2). (3) **Minor defect flag — the visited-link exhibit (candidate L52).** The tabview's link exhibit pairs `[# 未訪問リンク]` with `[[[theme:a-midnight-invitation|訪問済みリンク]]]`, keeping the original's slug (original L44). In the original the link is a self-reference — it names the theme page the reader is on, which is what makes it "visited". On scp-jp a page of that name does not exist: the T1 checker warns `link-target-missing` at candidate L52 in both the baseline and this package's re-run (section 12), and the port's own page is theme:a-midnight-invitation-jp. The b5cb724 usage sweep repointed the usage line (candidate L31) but not this exhibit. (The canonical composition carries a same-named page for the check environment, so the link resolves on the draft wiki; the checker's scp-jp lookup is the posting-relevant fact.) Flagged at minor weight with the checker's own warning as evidence; not edited.
- **Why:** A usage exhibit that names a page which will not exist under that name teaches a dead reference (the snippet-audit class the b5cb724 sweep applied to usage lines).
- **Verify:** The T1 re-run in section 12 reproduces the `link-target-missing` warn at L52.
- **Disposition:** Not dispositioned by any record; stands as this package's minor flag for the coordinator.

## 8. Structure

- EXHIBIT-RESTRUCTURE (C): Usage/sample exhibits dropped or replaced (R3): a sanctioned replacement and a silent deletion have the same diff shape; the ground must be stated.
  Verify: The exhibit-decision slot for this block, argued from the mirror.
  - B9: orig 28-28 -> cand 36-36 (body -> body)

- CSS-BODY (C): Unclassified CSS content change: CSS churn with no mechanism signature; kept visible and counted rather than silently passed.
  Verify: Writer review; a recurring shape is a new-signature candidate for the patterns loop.
  - B37: orig at 597 -> cand 617-618 (body -> code-css)

- **Exhibit decision, B9 (original L28 → candidate L36):** the exhibit is **kept**, and the label false-fires on the repoint inside it — the standing shape for this label. The image-block exhibit survives with its structure intact; only its asset address moved to the draft host (section 4) and its caption translated (section 6). Nothing was dropped or replaced.
- **The collapsible wrapper (B15/B37):** the candidate wraps the code exhibit in a `[[collapsible]]` with Japanese show/hide labels and adds a `+ ソースコード` heading (candidate L64–66; the close is candidate L618, inside heuristic B37 with the `[[/code]]` line) where the original presents the code block bare under its CSSテーマコード heading (original L52–55). An exhibit-presentation addition; the CSS inside it is untouched by the wrapper, and B37 resolves in the appendix.
- **Everything else structural is identity:** the body order (title, rate/info labels, intro, usage, page-element exhibits, code exhibit, license box) parallels the original's, and the classifier's topology pass finds no relocation (section 0).

## 9. Formatting only

- WS-ONLY blocks: 17
- Re-indentation: 0 blocks pair up after leading-whitespace normalization

The 17 WS-ONLY blocks are the trailing-space blank-line shape, concentrated in the Rate Module CSS section (candidate L447–515, where nearly every blank line carries one trailing space). Counted here so the churn is not mistaken for content change; the censuses in the per-theme record were run over declarations, which this whitespace cannot affect.

## 10. Porter annotations

The skeleton reports no signature for this section; three porter-side texts stand on the bytes and are recorded here.

- **What:** (1) The porter banner comment heading the delivered CSS (candidate L72–74): "한밤중의 초대 / A Midnight Invitation — Ported for SCP-JP (theme:a-midnight-invitation rev 20 on scpko)." (2) The section comment `/* 日本語フォント (JP localization) */` (candidate L75) labelling the JP font imports of section 4. (3) The license box's caution sentence (candidate L623, second half): readers are told to confirm with the author before posting any image the original carries no license statement for.
- **Why:** Porter annotations are the port's own voice inside the deliverable; each must be true against the bytes. (1) states the source page and reference revision — borne out by the credit block (candidate L18) and sources.tsv. (2) labels the supplement it heads (candidate L68–69). (3) is a conditional caution, not a factual claim about this file: the banner does carry a CC BY-SA 3.0 line and the pxhere credit for the background image, while the logo's only credit is "Logo by 035SL" — the caution's condition is therefore neither wholly true nor refuted by this file, and it is recorded as porter prose at that weight. The same license paragraph's first half (the pointer attribution) is section 1's flag, not an annotation matter.
- **Verify:** Read candidate L72–75 and L623 against original L56–67.
- **Disposition:** Standing; no record charges any of the three.

## 11. Dispositions and exceptions

- **Item 100 (class E), the pale stock header — DISPOSITIONED.** The full argument is the per-theme record below; its one-sentence form is that the candidate's entire colour diff against the original is the two sanctioned draft-host asset URLs, and the pale wordmark is the transparent placeholder over the deferred (404) logo artwork, a tie the render report itself makes. [GOSIGN2-LEDGER-SUPPLEMENT.md item 100; FIX5-CONTRB §1; KB-58 deferred asset hosting, patterns/ at commit 9c5e9079afb01d30cb9fc4ef9d714e5591eb2ffa]
- **Sample credit-modal errors — DISPOSITIONED as a preview-form property.** The candidate's credit is the `credit:start-preview` form, which has no modal mechanism; the failure is the preview form's, not the theme's (ruling 5) [GOSIGN2-LEDGER.md §(c2); GOSIGN-TESTS T2 amendment, 2026-11-16].
- **Page-overflow 324px@320 + 884px@768 — DISPOSITIONED** under the KB-33/KB-34 cross-cutting families [GOSIGN2-LEDGER.md §(c2), a-midnight-invitation row].
- **T1 pseudo-ref×4 (candidate L2, L36, L93, L99) — class (iii) draft form**, the draft-host addresses of sections 3 and 4, rewritten to the production host at posting (class (ii)) [register c1 via the verdict stamp].
- **T1 warn `interwiki-touched` (candidate L373) — recorded, not dispositioned.** The `.scpnet-interwiki-frame` filter rule it names (candidate L373–375) is byte-identical to the original's (original L353–355): an inherited design rule that recolours the frame, not a port-introduced touch, and no record charges it. It stands on the record at warn weight.
- **Not dispositions:** the section 1 author-naming defect and the section 7 exhibit flag stand as flags. The verdict stamp's STALE is explained by commit b5cb724's one-line usage repoint (section 2); the re-judgement on the current bytes is this package.

## 12. Verification

- **T1 (source check):** baseline 2026-11-16: exit 1, 4 errors / 2 warns / 1 info — pseudo-ref×4 (candidate L2/L36/L93/L99), warns `link-target-missing` (L52) and `interwiki-touched` (L373), info `!important`×20 [T1-ROWS row 233]. Re-run for this package (2026-11-17, the campaign checker `check_source.py` on this package's candidate.txt, `--kind theme --translation --check-links`): **the baseline reproduces exactly** — same counts, same codes, same lines. The post-baseline change (b5cb724's usage line) touches no checked surface. No class (i) error stands; the four errors are the class (iii) draft forms of section 11.
- **T2/T3 (render):** combined verdict FINDINGS [RENDER-ROWS-2 (RENDER-S2-H (KO1))]: sample credit-modal (preview-form), the two overflow figures, and the T3 contrast observation that became item 100 — each dispositioned in section 11. No re-render was run for this package: the render record is the lane's, cited, not re-measured here.
- **T4 (follow-up diff):** rev20 → rev20, no change — the LOCALIZE-S2-F lane's follow-ups print no-change for all 39 KO originals in scope, this theme among them. The mirror in this package is therefore also the current original.
- **T5 (translation text):** judged jointly with T4: FINDINGS whose one display-affecting item is the section 1 credit vagueness (型3); the lane found no mistranslation in the carried prose (section 6).
- **This package:** `python3 review/build_review.py --check` — the verdict stamp regenerates identically from the two files in this package, and the package is not in the pre-existing stale set (the refresh-3 population). The censuses in the per-theme record were re-derived from this package's two files while this README was written, not transcribed from the supplement.

## Per-theme record

### The two-URL colour disposition (ledger §(e) item 100)

The charge, as the ledger states it: item 100 [E] (KB-28) — "Stock-header wordmark and nav in very light gray on near-white at all 8 viewports, nearly illegible; the render lane records it as theme-specific (checklist section 1 contrast)" [GOSIGN2-LEDGER.md §(e) item 100]. Class E charges a candidate-side defect, so the question the disposition turns on is decidable from the two files in this package: did the port change any colour, or is the paleness a state of the assets the colours were designed to sit on? The supplement's ground has two halves: "colour diff vs original consists only of the two sanctioned draft-host asset URLs; the pale wordmark is tied by the render report itself to the deferred logo/background 404s (KB-58)" [GOSIGN2-LEDGER-SUPPLEMENT.md (a) item 100; REPORT-GOSIGN2-FIX5-CONTRB.md §1]. Re-measured from this package's files:

1. **The declaration census.** Every colour/background-bearing declaration in each file (`color`, `background`, `background-color`, `background-image`, `border-color`, `text-shadow`, `box-shadow`, `outline-color`, `fill`, `stroke`): 102 declarations on each side. The multisets differ in **exactly two** declarations — `background: url(…background.png)` (original L73, scpko host → candidate L93, draft host) and `background-image: url(…logo.png)` (original L79 → candidate L99) — the two sanctioned draft-host asset rewrites of section 4. Every colour value in the file is otherwise identical, including the near-white the charge names: `body { background-color: #F6F6F6; }` (original L243 = candidate L263) is the original's own page ground.
2. **The wordmark surface.** The wordmark is an image slot, not text: `#header h1 a::before { content: " "; color: #00000000; }` (original L96–101 = candidate L116–121; the placeholder colour sits at original L98 = candidate L118, byte-identical), and the visible mark is the logo artwork carried as `#header`'s background image (original L79 → candidate L99) over the container background (original L73 → candidate L93). With both assets in the KB-58 deferred state — the render report records their 404s and itself ties the pale wordmark to them (RENDER-S2-H §2, the cross-cutting deferred-asset item) — what the T3 walk photographed is the transparent placeholder over the near-white ground, which is what the original's CSS also produces with its images missing.
3. **The nav surface.** The login/nav text is white by design, drawn for the dark header artwork: `#login-status { color: #fff; text-shadow: -1px 0 #000, 0 1px #000, 1px 0 #000, 0 -1px #000; }` and the same for its links (original L110–122 = candidate L130–142, byte-identical), with `#account-topbutton { border-color: #ffffff; }` (original L124–126 = candidate L144–146). On the missing artwork the white text sits on the page ground; on the artwork it sits on the image it was designed for. Neither colour is a port change.
4. **No structural colour accident.** A brace-depth scan of both files (max depth 2, final depth 0, no negative excursion on either side) excludes a displaced brace silently re-scoping the rules after it.

The conclusion the census licenses: the port changed no colour value anywhere in the file; the illegibility is the deferred-asset state of the two header images (KB-58), which posting resolves by re-hosting, not a colour defect a candidate edit could fix without departing from the original. Disposition: **DISPOSITIONED, no edit** [GOSIGN2-LEDGER-SUPPLEMENT.md item 100; FIX5-CONTRB §1].

### Second-reviewer walk

The class asks for the disposition to be walked once more from the third-party perspective: is the ground stated in terms a reader who did none of the work can check, and does it hold? The ground is two claims. The first — the colour diff has exactly two members, both named — is reproducible from this package alone in one pass over the two files, and it held exactly under re-measurement (102 declarations, two differences, both URLs). The second — the render report ties the paleness to the deferred assets itself — is a citation the reader can open (RENDER-S2-H §2), and it is the render lane's own sentence rather than the disposition lane's inference, which is what makes the disposition stronger than a re-argument: the lane that raised the charge also recorded its cause. The one thing the bytes alone cannot show is the 404 state at render time; that is stated as the record's evidence, not dressed as a package measurement. Walk outcome: **the disposition is sound as stated.**

### Record discrepancies flagged by this package

1. **The register's "P3 FIXED" and the bytes disagree on the naming half.** GOSIGN2-LEDGER.md §(c3) records this theme's P3 item as FIXED (credit waves; checker-verified). The checker verifies that the eight credit fields exist; the localize lane's §3 charge against this theme was that the author field is vague （原語版ページの作成者に同じ — LOCALIZE-S2-F finding 9 names the theme), and that half stands in the current bytes (section 1's flag, with the license box's author parameter in the same shape). The register and the lane are each true of a different half of the pattern; this package follows the bytes for the naming half and flags the defect rather than dispositioning it.
2. **The stamp's STALE is a one-line sweep delta, not a record conflict.** The candidate's only post-verdict change is the usage-example repoint (commit b5cb724, section 2); it is recorded in the multi-wave provenance rather than flagged.

### Multi-wave provenance

The candidate's current state is the product of successive waves, not one pass: the Stage 2 KO1 integration (commit 18280b3) produced the port the localize lane audited (LOCALIZE-S2-F, KO1); FIX-CREDIT-D (commit 1869877) normalized the translator attribution to ruling 3's form; FIX5-CONTRB closed the theme's only blocking item as a no-edit disposition, so no FIX5 commit touches this file; and the usage-example sweep (commit b5cb724) repointed the usage line to the `-jp` posting name — the one-line delta behind the stamp's STALE. (The file's earlier history, commits d727e92 and 8dcac74, is the composition's canonical-sources and Phase 17 record strata, before the port.) Citations, in place of a changelog: GOSIGN2-LEDGER.md §(c2) (render row), §(c3) (localize row), §(e) item 100; GOSIGN2-LEDGER-SUPPLEMENT.md item 100; REPORT-GOSIGN2-LOCALIZE-S2-F.md (KO1, a-midnight-invitation, and cross-cutting findings 4, 8, 9); REPORT-GOSIGN2-RENDER-S2-H.md §2; REPORT-GOSIGN2-FIX5-CONTRB.md §1. The go-sign over that record is what the Status block certifies.

### Post-package repairs (REFRESH3-L)

The items above describe this package as built. The repair recorded below postdates the package; `candidate.txt` has been recopied from the current canonical `pages/theme:a-midnight-invitation-jp.txt` and `diff.md` and the verdict stamp regenerated with `python3 review/build_review.py`, so this package now documents the post-repair candidate. The regenerated stamp reads **STALE** by design: no re-judgement is fabricated here, and the frozen ledger (`GOSIGN2-LEDGER.md` + supplement, FIX5 head 435a6bb) remains the verdict record.

**FIX-RDISP1, landing `a729077` (report `R/review-scout/FIX-RDISP1.md`).** Two candidate repairs, 3 lines (+3/−3), both postdating this package's build at `b5cb724` (the usage-example sweep, which the as-built `candidate.txt` matches byte-for-byte).
- **Item 1 — credit pointer names nobody (two carriers).** The original names c_bonefish twice (original L20 `[[*user c_bonefish]]`, banner L60 "Created by c_bonefish"; the base/logo attributions at L61–62 survive in the candidate's own banner at L81–83). Both TASL author fields were pointers. The credit block (as-built candidate L16) `**著作権者:** 原語版ページの作成者に同じ（scpko の theme:a-midnight-invitation）` → `**著作権者:** [[*user c_bonefish]]`; the license box (L621) `|author=scpko theme:a-midnight-invitation の作者]]` → `|author=c_bonefish]]`. Both are the population's established forms for this author (theme:some-guider-jp, theme:mr-reprisal-jp). The attribution prose at L623 is a source note and is untouched.
- **Item 2 — visited-link exhibit names the plain form.** Candidate L52 `[[[theme:a-midnight-invitation|訪問済みリンク]]]` → `[[[theme:a-midnight-invitation-jp|訪問済みリンク]]]`, a single `-jp` insertion (the greyday / king-s-palace shape). The exhibit is a self-reference to the port's own page; the usage sweep at build time had repointed the usage line (L31) but not this exhibit.
Checker per the report: exit 1, error 4 / warn 2 / info 1 before and after; the four errors are unchanged class (iii) pseudo-refs, class (i) errors 0 throughout; the only delta is the L52 warn now naming the candidate's own `-jp` page (a not-yet-posted self-reference that resolves at posting).

## Appendix — residue blocks

### Residue R1 — B6 (heuristic; orig 20-20 -> cand 26-26, body -> body)
- Removed first line: 한밤중의 초대 CSS 테마는 [[*user c_bonefish]]가 [[[http://scpko.wikidot.com/midnight-club-hub|심야클럽]]] GoIF 혹은 이와 같은 작품들을 위해 제작하였습니다.
- Added first line: **クレジット付き評価モジュール:**
- Note: script delta without the anchor majority

Resolution: assigned to sections 1, 2 and 6. The block pairs the original's intro line with the candidate's second vestigial label by alignment; the intro's own translation stands at candidate L28, inside B7's span, and is treated there (author named — the fact section 1's flag turns on; hub link repointed, section 2). The label line itself is the INFO-DEL residue of section 1. No new signature proposed: the shape is block misalignment across a deletion, not a mechanism.

### Residue R2 — B11 (heuristic; orig 41-41 -> cand 49-49, body -> body)
- Removed first line: ㅁㄴㅇㄹ
- Added first line: サンプルテキスト
- Note: script delta without the anchor majority

Resolution: assigned to section 6. The original's tabview placeholder is Korean keyboard-mash filler (ㅁㄴㅇㄹ, the home-row keys); the candidate renders it as サンプルテキスト ("sample text"), the functional equivalent for a JP reader. A translation of placeholder filler, not content loss.

### Residue R3 — B12 (heuristic; orig 43-44 -> cand 51-52, body -> body)
- Removed first line: > + Link
- Added first line: > + リンク
- Note: script delta without the anchor majority

Resolution: assigned to sections 6 and 7. The tabview's link-exhibit labels translate (+ Link → + リンク; the unvisited/visited link labels likewise). The visited-link target inside the same lines is section 7's minor flag.

### Residue R4 — B13 (heuristic; orig 46-46 -> cand 54-54, body -> body)
- Removed first line: >> 텍스트[[footnote]]똑똑[[/footnote]]
- Added first line: >> テキスト[[footnote]]コンコン[[/footnote]]
- Note: script delta without the anchor majority

Resolution: assigned to section 6. The exhibit line translates （テキスト) and the footnote's knock-knock onomatopoeia 똑똑 becomes its Japanese counterpart コンコン. The footnote itself is kept; neither file carries a `[[footnoteblock]]`, so there is no orphan on either side — parity.

### Residue R5 — B15 (heuristic; orig at 55 -> cand 63-66, body -> body)
- Note: script delta without the anchor majority

Resolution: assigned to section 8. B15 is the candidate's added `+ ソースコード` heading and `[[collapsible]]` opening around the code exhibit (candidate L64–66); its closing half is B37 (R6 below).

### Residue R6 — B37 (heuristic; orig at 597 -> cand 617-618, body -> code-css)
- Added first line: [[/code]]
- Note: no other signature matched

Resolution: assigned to sections 1 and 8. B37 is the exhibit's close pair — `[[/code]]` (candidate L617) and the `[[/collapsible]]` (candidate L618) that closes B15's wrapper — after which the license box (B38) attaches. The CSS-BODY label on this block is the classifier's catch-all; the content is structural, not CSS churn. No new signature proposed.

## License and attribution

- **Title:** 한밤중의 초대 CSS 테마
- **Author:** c_bonefish
- **Source:** https://scpko.wikidot.com/theme:a-midnight-invitation — revision 20
- **License:** Creative Commons Attribution-ShareAlike 3.0 (CC BY-SA 3.0) — license deed: https://creativecommons.org/licenses/by-sa/3.0/
- **Adaptation:** This package holds a Sigma-10 migration port of the work; changes were made. See "Summary" and "Standing sections" in this README for what changed and why. Translator: AI (Muse and its delegated agents), per the campaign's standing attribution rule.
