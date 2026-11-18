# Review package — theme:last-frontier-jp
New to this package's shorthand? Read the notation key first: [How to read a review package](../HOW-TO-READ.md).

<!-- BEGIN GENERATED VERDICT STAMP — do not hand-edit; regenerate with review/build_review.py -->
## Verdict stamp
- Theme: theme:last-frontier-jp — origin EN, population #107 [GOSIGN2-LEDGER (b) row 107]
- Overall: STALE — candidate file changed since the verdict was computed (verdict against 435a6bb-era content, file sha256 now ef88c24f15667a5e58707756df63f10f0b35130da5649802c471935403f629f4); the verdicts below were computed against that pre-change file, and the record verdict stands: a candidate revised through the campaign's recorded repairs is posted like a PASS row, with the change recorded in its package
- T1 (source check): FINDINGS (classified) — baseline 2026-11-16: exit 1, 7 errors / 0 warns / 1 info (pseudo-ref×7); standing classes dispositioned in register c1 [T1-ROWS row 97; GOSIGN2-LEDGER (b) row 107]
- T2/T3 (render, combined verdict): FINDINGS — [combined T2/T3] report `FINDINGS` — page runtime-hotlink site-theme chain only; sample credit-modal (preview-form) + 884px@768 overflow; T3 sample header wordmark "The Beholder Program財団" overprints account/search links and clips at 375/320 (both engines); broken binary-star-loop-link.bmp (deferred). [RENDER-ROWS-2 (RENDER-S2-C (EN13))]
- Engine coverage: full matrix as run by the lane; coverage not separately caveated in the row [RENDER-ROWS-2 row]
- Credit modal: sample credit-modal errors dispositioned preview-form (credit:start-preview has no modal mechanism; GOSIGN-TESTS T2 amendment, 2026-11-16) [RENDER-ROWS-2 (RENDER-S2-C (EN13))]
- T4 (localize patterns + follow-up): FINDINGS — display-affecting findings: 1 [LOCALIZE-ROWS row 107, source LOCALIZE-S2-B]
- T5 (translation text): FINDINGS — the source reports judge T4/T5 jointly; one verdict word covers both [LOCALIZE-ROWS row 107]
- FIX5 re-judgement: none — no OPEN items at the ledger determination [GOSIGN2-LEDGER (b) row 107]
- Computed against: canonical commit b5cb7241f527a44933e45599b41df210690771c4; candidate file pages/theme:last-frontier-jp.txt sha256:ef88c24f15667a5e58707756df63f10f0b35130da5649802c471935403f629f4; record: GOSIGN2-LEDGER.md + GOSIGN2-LEDGER-SUPPLEMENT.md as of the FIX5 head 435a6bb
<!-- END GENERATED VERDICT STAMP -->

Status: complete — skeleton by classify_hunks.py 0.1.0; every SLOT in the skeleton is resolved in the sections below and the Appendix.
Candidate: review/last-frontier-jp/candidate.txt (sha256 ef88c24f15667a5e58707756df63f10f0b35130da5649802c471935403f629f4)
Original: theme:last-frontier — scp-wiki, revision 41 (sha256 4c0abc008bf004b943f648ffb03d1b8c1ccce2bbf18c309617bd50c9af7703a2)
Classifier: classify_hunks.py 0.1.0; signature table 2026-11-17.1; patterns commit 9c5e9079afb01d30cb9fc4ef9d714e5591eb2ffa

## Status

| Check | Verdict |
|---|---|
| Population row | PASS [GOSIGN2-LEDGER (b) row 107] |
| T1 source check | FINDINGS (classified) — 7 errors / 0 warns / 1 info (pseudo-ref ×7) [T1-ROWS row 97] |
| T2/T3 render | FINDINGS — page runtime-hotlink site-theme chain only; sample credit-modal (preview-form) + 884px@768 overflow; T3 sample wordmark "The Beholder Program財団" overprints and clips at 375/320 (both engines); broken binary-star asset deferred [RENDER-ROWS-2 (RENDER-S2-C (EN13))] |
| T4 localize patterns | FINDINGS — display-affecting 1 (P9) [LOCALIZE-ROWS row 107] |
| Generated stamp | STALE — the candidate changed after the ledger determination (one usage line, in the post-determination sweep); the pre-change verdict lines are preserved in the stamp and the change is recorded under Per-theme record below |

## Provenance

| Item | Value |
|---|---|
| Original page | theme:last-frontier (scp-wiki) |
| Reference revision | 41 — first-translation revision |
| Mirror class | COPY (stored mirror file used as-is) |
| Mirror file | R/review-mirrors/orig-last-frontier-rev41.txt |
| Original SHA-256 | 4c0abc008bf004b943f648ffb03d1b8c1ccce2bbf18c309617bd50c9af7703a2 |
| Candidate file | pages/theme:last-frontier-jp.txt |
| Candidate SHA-256 (this package) | ef88c24f15667a5e58707756df63f10f0b35130da5649802c471935403f629f4 |

Provenance route: standard derivation from the EN branch original at the reference revision (sources.tsv kind `standard`, verdict PASS, notes empty), with one declared dependency: the candidate's exhibit merges the CSS of the base theme (theme:shattered-thoughts, rev 34) ahead of the theme's own CSS, documented in the file itself (cand L149–157) and treated in sections 3 and 8. The candidate entered the canonical repository in the Stage 2 EN13 integration commit d7c1af6, then received the FIX-CREDIT-D attribution normalization in 1869877 (one line in this file) and one usage-line repair in the post-determination sweep commit b5cb724; the acts are verified under Per-theme record.

## Summary

Vivarium's Last Frontier, adapted from Yossipossi's Shattered Thoughts: the original layers over its base by hiding an include of the base theme at its tail and importing its own exhibit from a tail module. The port's defining act is a documented base merge: because the base theme is not on production SCP-JP (the porter's in-file note, cand L149–151), the base's rev-34 CSS is merged into the candidate's single exhibit ahead of the theme's own CSS, under a banner (L157), and delivery moves to the campaign's head form. The candidate is 894 lines against the original's 372 for exactly that reason; the growth is the merge, not churn. The port also creates a JP license box whose entries honestly record "not stated in the original" where the original states nothing, documents a dropped header-logo rule whose source file has vanished, and consolidates the original's author-label component into the credit block while carrying its greeting as body text. This review records no defect flag for the theme; its findings are adjudications (the classifier's RESTORATION and COMPONENT-SWAP primaries do not fit the bytes) and one classifier blind spot (the lowercase rate module's removal carries no label).

## Class summary

| Label | Blocks |
|---|---|
| ANNOTATION | 1 |
| COMMENT-TEXT | 2 |
| COMPONENT-SWAP | 1 |
| CONTENT-STRING | 1 |
| CREDIT-PREVIEW | 1 |
| CSS-BODY | 1 |
| DELIVERY-HOST | 1 |
| DRAFT-HOST | 6 |
| ESCAPED-INCLUDE | 1 |
| EXHIBIT-RESTRUCTURE | 4 |
| FONT-IMPORT | 1 |
| IFTAGS | 2 |
| INCLUDE-REPOINT | 1 |
| JPFONT-LOAD | 1 |
| LICENSE-BOX | 1 |
| LINK-REPOINT | 1 |
| RESTORATION | 1 |
| SELF-DELIVERY | 3 |
| T7-CREDIT-CSS | 1 |
| TASL-FIELDS | 1 |
| TRANS-UNANCHORED | 22 |
| TRANSLATION-ANCHORED | 19 |

Counts: 52 blocks, 29 specific, 21 heuristic, 2 residue, 0 skipped (comment text). Diff size: +591/−69 lines by both the generator's difflib count and GNU diff (original 372 lines, candidate 894) — the surplus is the merged base (block B46 alone spans cand L154–635).

Adjudication of the classifier's labels against the bytes, where they diverge: the diff's centre of mass is one mega-block, B46 (orig exhibit head → cand L154–635), which carries seven labels at once (COMMENT-TEXT, CONTENT-STRING, DRAFT-HOST, FONT-IMPORT, JPFONT-LOAD, T7-CREDIT-CSS, TRANS-UNANCHORED) because the merged base's CSS contains all of those features; it is one act (the base merge), narrated in section 8, not seven. RESTORATION (B45, cand L143–152) is the merged exhibit's head comment — the original's banner line carried plus the porter's merge explanation; nothing was "restored" from anywhere. COMPONENT-SWAP (B10) is the usage line's escape-and-repoint, the same three tokens on both sides. The original's lowercase `[[module rate]]` (orig L8) is removed in the candidate, but no BARE-RATE-DEL label fires: the signature evidently expects the capitalized form, a blind spot recorded under Per-theme record as a patterns proposal. EXHIBIT-RESTRUCTURE ×4 resolves against the census: one code exhibit each side, image-block includes 3 = 3, the collapsible and tab samples corresponding — the primaries are the merge's alignment effects.

## Standing sections

### 0. Header / provenance

**What.** The two heads have opposite shapes. The original opens its whole-page `[[iftags +theme]]` gate with furniture (a hidden image-block div, the bare rate, the author-label component; orig L1–19) and puts its delivery at the very tail (orig L366–372). The candidate puts delivery first — head `[[module CSS]]` importing the exhibit (cand L1–3), the priority-1 interwiki frame (cand L5–8) — then opens `[[iftags +テーマ]]` (cand L10) for the credit block (L12–21) and the body. Provenance data is the table above; the base-merge declaration is part of the provenance and stands at cand L149–157, inside the exhibit.

**Why.** The head form is the campaign's delivery standard (P4/T9; gate localization P2/T2, KB-08; patterns commit 9c5e9079afb01d30cb9fc4ef9d714e5591eb2ffa): delivery lines at the head resolve before the body renders, and the self-delivery address can be audited against the page's first code block. The original's tail delivery is its own idiom, not a requirement.

**Verify.** `head -21` both files and `tail -7 original.txt`; `grep -n "iftags" candidate.txt` returns the single gate (L10, closed at L894).

**Disposition.** No header item is charged against this theme in any row.

### 1. Credit and attribution

**What.** The candidate's credit block (cand L12–21, `:scp-jp:credit:start-preview`/`end-preview`) carries all eight TASL fields, complete from creation: タイトル 「ラスト・フロンティア テーマ」, 翻訳責任者 "AI", 翻訳年 2026, 原題 "Last Frontier Theme", 著作権者 "[[*user Vivarium]], [[*user Yossipossi]]" (user-link form), 作成年 2021, 初訳時参照リビジョン 41, and 元記事リンク to https://scp-wiki.wikidot.com/theme:last-frontier — the host recorded in sources.tsv for this theme, so no cross-host probe arises. The author field matches the original's two attribution surfaces: the prose byline (orig L23: "Adapted by [[*user Vivarium]] from [[*user Yossipossi]]'s Shattered Thoughts Theme") and the exhibit banner ("Based on Shattered Thoughts Theme created by Yossipossi.", orig L134, carried at cand L147 and again at the own-CSS section head, cand L640). The candidate additionally creates a JP license box at its tail (cand L867–892, `:scp-jp:component:license-box-backend` with `|author=Vivarium, Yossipossi`, closed by license-box-end) holding four file entries — earth.jpg, diamond.png, binary-star-loop-blink.gif, and the base theme's st-diamondblue.png / st-background.png — whose author and license fields honestly record 原語版に記載なし ("not stated in the original") with checking advice, plus source URLs; the original carries no license box, so nothing was dropped to make room for it (LICENSE-BOX, B51).

**Why.** The credit swap is P3/T1 (KB-21, KB-22). The license box is a supplement of the T-license family: CC BY-SA posting requires per-file attribution, and where the original states nothing the honest entry is "not stated", not an invented license — the entries' restraint is the point a reviewer should check, and it holds. The base theme's files are entered too, with Yossipossi named as their author, because the merge of section 8 makes the candidate a carrier of the base's assets as well as its CSS.

**Verify.** Read cand L12–21 against orig L23 and L134; read the license entries at cand L867–892 and confirm each "not stated" against the original, which contains no per-file license text anywhere (grep for "license" in original.txt returns only exhibit CSS selectors).

**Disposition.** No credit item is charged against this theme (the ledger's (c3) line carries P9 only); population-wide, the ledger's assembly note records credit-missing-fields = 0 after the credit waves. The license box is an uncharged supplement, recorded here as the package's evidence that the theme's file attribution was constructed, not copied.

### 2. Includes and components

**What.** Includes, candidate side: the interwiki frame (L5–8), the credit pair (L12, L21), three image-block includes (the count matches the original's three, including the sample at cand L48), and the license-box pair (L867, L892). Two original components do not survive as components. (i) The author-label-source pair (orig L11, L19, with `|name=Vivarium`) is gone; its payload — the author's greeting and the link to more of their work — is carried as plain centered body text (cand L23–28, translated), so the attribution function consolidates into the credit block while the greeting's text survives unboxed (the end-include's removal is heuristic block B7, appendix R4). (ii) The hidden base include (orig L366–368, `:scp-wiki:theme:shattered-thoughts` inside a display:none div) is replaced by the base merge (sections 3 and 8). The usage line (cand L38) shows the self-include in the span-and-@@ escape form of the original (ESCAPED-INCLUDE + COMPONENT-SWAP + INCLUDE-REPOINT on B10). The original's lowercase bare rate module (orig L7–9) is absent from the candidate (grep: no "module rate" in any case) — the KB-09 removal, unlabeled for the reason given in the Class summary.

**Why.** Repoints are P1/T3. The author-label consolidation rides the P3 swap's logic: the JP environment's attribution surface is the credit block, and a second label component naming the EN site's component library would duplicate it. The rate removal is KB-09's class (the preview credit module is already rate-bearing).

**Verify.** `grep -n "\[\[include" candidate.txt` returns L5, L12, L21, L48 (and the sample lines), L867, L892; `grep -in "author-label\|module rate" candidate.txt` returns nothing.

**Disposition.** Uncharged per-theme; the base include's replacement is the documented merge (section 8), and the render register's items do not include a missing-label or missing-base finding.

### 3. Delivery and code loading

**What.** Self-delivery on the campaign's head form (SELF-DELIVERY ×3 spans; DRAFT-HOST ×6 across the file): the head module's @import (cand L2) and the frame's theme= (cand L7) both name the candidate's own draft-host address local--code/theme%3Alast-frontier-jp/1. The page holds exactly one `[[code]]` block (the merged exhibit at cand L142–864), so /1 names the exhibit: the FIX-CODEADDR population audit lists no mismatch for this theme. The original delivers from its tail (orig L370–372, a module importing the wikidot.com /code/1 URL form) and additionally loads its base by the hidden include (orig L367); the candidate's single exhibit carries both layers, base first (banner at cand L157), the theme's own CSS after (its banner repeated at cand L640), so the cascade order the original achieved by include order is preserved by merge order.

**Why.** Host repoints are P4/T9; the draft host is the class (iii) draft-form (KB-41). The merge order matters mechanically: the base must precede the theme's overrides or the overrides lose, which is why the porter's note (cand L149–151) specifies "merged in ahead of … its own CSS" and why this package verifies the banner positions rather than trusting the note.

**Verify.** `grep -n "local--code" candidate.txt` returns exactly L2 and L7; `grep -n "base: Shattered Thoughts\|Based on Shattered Thoughts" candidate.txt` returns L147, L157, L640, fixing the merge boundary; the FIX-CODEADDR audit is the population cross-check.

**Disposition.** Class (iii) draft-form under T1 disposition class (iii), population-wide (KB-41); no delivery item is charged against this theme individually.

### 4. Fonts and assets

**What.** The merged exhibit carries two font systems: the base's (its imports and stacks came in with the merge, inside B46 — FONT-IMPORT and JPFONT-LOAD fire there) and the theme's own; every face named in the candidate's stacks is loaded by an import inside the same exhibit, which is the delivery unit, so no stack names an unloaded face. Assets: the demonstration image (Binary_Star_Loop_Blink.gif) is repointed in the body sample to the candidate's own draft-host files under a lowercased, hyphenated filename (cand L48: binary-star-loop-blink.gif), while the license entry cites the original filename and its scp-wiki source URL (cand L880–883) — the render register records the binary-star asset as broken and deferred. The original's header-logo rule (orig L160, background-image naming ITTV_LOGO.png on a test wiki, scptestwiki.wikidot.com) is dropped in the candidate's own-CSS section, replaced by a porter comment explaining the drop (cand L665–666, residue R2), and the license box's 訳注 repeats the reason (cand L890): the file has vanished from its host and the original no longer displays it either. That attestation is the porter's, recorded in the file; this package reports it as such.

**Why.** Font loads inside a merged exhibit are part of the merge's fidelity (P5/P7 classes ride inside B46's labels). Asset repoints localize the theme's own files (P5's other half); the deferred broken asset is KB-58's class (an upstream file problem, decided at posting). A dropped rule whose target no longer exists is a restoration-class judgement: keeping it would preserve a 404, and the porter documented the reasoning in two places, which is the standard this review applies.

**Verify.** `grep -n "ITTV" candidate.txt original.txt` returns the original's rule (L160) and the candidate's 訳注 (L890) only; read cand L665–666 for the in-CSS note; `grep -n "binary-star" candidate.txt` returns L48 and L880, the naming split in one view.

**Disposition.** The binary-star asset item is DISPOSITIONED as deferred in the render register (KB-58); the header-logo drop is documented in-file and uncharged; no font item is charged.

### 5. Header, sidebar, site furniture

**What.** The theme's masthead title is a CSS content string in its own-CSS section: `content: "The Beholder Program"` (cand L650; orig L144) — kept in English, which is the ledger's P9 charge for this theme (its one display-affecting finding). The render row's furniture item is the T3 sample wordmark: "The Beholder Program財団" overprints the account/search links and clips at 375/320 in both engines; the sample also carries the credit-modal preview-form item and the 884px-at-768 overflow.

**Why.** Masthead strings are P9/T6 (KB-57), the theme's visible title surface; ruling 2 takes header and title language choice out of migration-correctness scope. The wordmark and overflow items belong to the KB-35/KB-33/34 responsive and preview families, not to the string's language.

**Verify.** `grep -n "Beholder" candidate.txt` returns L650; the wordmark evidence is the RENDER-ROWS-2 row cited in section 12.

**Disposition.** P9 DISPOSITIONED (ruling 2) [ledger (c3), last-frontier line]; the render items are DISPOSITIONED in the render register (KB-33/34, KB-35 families).

### 6. Text translation

**What.** The body is translated in place: the greeting (cand L23–28, from the author-label payload), the byline (L32), the usage prose (L34), the spiel and samples (headings, tabber samples, blockquote and link samples). One sample is adapted rather than translated: the original's lorem-ipsum paragraph (orig L53, with its hub link and footnote) becomes a Japanese dummy-text paragraph demonstrating the same markup — links in bare form, emphasis, italics, a footnote (cand L62; heuristic R5) — a porter's substitution that keeps the sample's function (showing the theme's text styles) in the target language. The exhibit's own comments and the base's carried text stay as the merge brought them (COMMENT-TEXT ×2 fires on the translated subset); the base's English banner line is attribution text and is carried verbatim (section 1).

**Why.** Body translation is P10 (KB-18). The dummy-text substitution is the same class exercised differently: a lorem ipsum demonstrates nothing about Japanese rendering, so replacing it with Japanese dummy text is the translation's purpose applied to a sample whose content is deliberately meaningless.

**Verify.** Spot-read cand L23–48 against orig L13–40; read cand L62 against orig L53 for the sample substitution.

**Disposition.** T5 FINDINGS under the joint T4/T5 verdict [LOCALIZE-ROWS row 107]; the translation is the port's purpose and is not an open item.

### 7. Links

**What.** The byline's hub link changes from the URL form to the bare page form with a translated anchor (orig L23 `[[[http://scp-wiki.wikidot.com/into-the-void-hub | Into the Void Hub]]]` → cand L32 `[[[into-the-void-hub|Into the Voidハブ]]]`; LINK-REPOINT ×1), and the dummy-text sample's hub link takes the same bare form (cand L62). The author's own external page (vivarium-s-word-hole, cand L27) keeps its scp-wiki URL: it is the author's personal page, linked as an external reference in both versions. The credit link is treated in section 1 (recorded host, exact); the license entries' source URLs are section 1's record.

**Why.** P11: links naming this environment's pages take the form that resolves here; genuinely external author references stay as they are. The hub is an SCP-JP-relevant page (the theme's setting hub), so the bare form is the repoint that keeps the sample inside the JP environment.

**Verify.** `grep -n "into-the-void-hub" candidate.txt` returns L32 and L62, both bare-form.

**Disposition.** No link item is charged against this theme.

### 8. Structure

**What.** The structural acts are the merge and the tail exchange. The merge: one exhibit (cand L142–864) whose head comment carries the original's banner (L147), the porter's merge explanation (L149–151: the base theme, rev 34, is not on SCP-JP, so its CSS is merged in ahead of the original's base import, before the theme's own CSS), and the base section banner (L157); the theme's own CSS follows from its repeated banner (L640) to L864. The classifier's RESTORATION primary on the head comment (B45) and its seven-label mega-block (B46) are alignment readings of this one act. The tail exchange: where the original ends with the hidden base include and the tail delivery module (orig L366–372), the candidate ends with the license box (cand L867–892) inside the gate, its delivery having moved to the head (section 3). CSS brace depth scans clean on both files (final 0, min 0, max 2) — the merge did not unbalance the exhibit. The T7-CREDIT-CSS label inside B46 is the base's own credit-related CSS, carried with the merge, not a candidate-authored supplement.

**Why.** Structure is what delivery addresses and cascade order resolve against (P4); a base merge is the strongest structural act a port can take, and it is justified here by the porter's stated ground (the base's absence from production SCP-JP) and verified by the banner census, not by the note alone. The alternative — including theme:shattered-thoughts-jp — would tie every JP use of this theme to a page whose production existence the porter denies; the composition does hold such a candidate for its own samples, which does not contradict the production claim.

**Verify.** The banner grep of section 3; `grep -c "\[\[code" candidate.txt` returns 1; the depth scan is a five-line brace counter over each file.

**Disposition.** The merge is uncharged in the ledger (its (c3) line carries P9 only) and is recorded here as a documented supplement; no structural item is open.

### 9. Formatting only

**What.** No WS-ONLY label fires for this theme: the diff's size is content (the merge and the license box), not formatting churn. The candidate's exhibit preserves its sources' indentation styles section by section, which is itself evidence the base section was merged, not rewritten.

**Why.** Stating the empty formatting class with its ground keeps the +591-line diff from being discounted as churn by a reader who expects a formatting share (KB-18's census discipline).

**Verify.** classification.json's label table for this package contains no WS-ONLY row; `diff -w` on the packaged pair retains essentially the full diff.

**Disposition.** None required; not a ledger item.

### 10. Porter annotations

**What.** Three porter annotations, all in the file's own voice, none in wikitext `[!--` form (grep count 0 on both sides). (i) The merge explanation comment at the exhibit's head (cand L149–151). (ii) The header-logo drop note in the own-CSS section (cand L665–666). (iii) The license box's 訳注 (cand L890, ANNOTATION ×1), restating (ii) for the attribution surface. Each names its act and its reason; together they are why this package can narrate the theme's two boldest acts (the merge, the rule drop) from the file alone.

**Why.** Annotations are T12; in comment and 訳注 form inside the artefacts they annotate, they are part of the port's documentation, and their presence is the difference between a supplement a reviewer can adjudicate and one they can only suspect.

**Verify.** `grep -n "JP port\|訳注\|not on SCP-JP" candidate.txt` returns the three loci.

**Disposition.** None; the annotated acts are treated in sections 4 and 8.

### 11. Dispositions and exceptions

**What.** The theme's disposition set: P9 (the English masthead string) DISPOSITIONED under ruling 2 [ledger (c3)]; the T1 baseline class (pseudo-ref ×7 — the @@-escaped exhibits) dispositioned in register (c1); the render items DISPOSITIONED in the render register (runtime-hotlink chain, KB-40; credit-modal and overflow, KB-33/34; wordmark, KB-35; the broken binary-star asset deferred, KB-58); the head draft-host lines are class (iii) draft-form (KB-41). The base merge, the license box, and the header-logo drop are not dispositions — they are documented acts of the port, recorded in sections 1, 4, and 8, and no row charges them.

**Why.** Dispositions separate "wrong here" from "wrong at posting" and "decided out of scope"; documented acts are a different category — choices the porter made and explained — and the package keeps the two apart so neither is mistaken for the other.

**Verify.** The theme's lines in ledger registers (c1), (c2), (c3) under review/AUTHORITIES/ledger-parts/, against sections 3–5 above.

**Disposition.** As stated per item; the population verdict is PASS [GOSIGN2-LEDGER (b) row 107] with FIX5: none.

### 12. Verification

**What.** The stamp's evidence chain: T1 baseline 2026-11-16, exit 1, 7 errors / 0 warns / 1 info (pseudo-ref ×7) [T1-ROWS row 97] — notably no hotlink class, consistent with a candidate whose assets were repointed or dispositioned from creation; T2/T3 combined FINDINGS [RENDER-ROWS-2 (RENDER-S2-C (EN13))] as tabled above; T4 FINDINGS with display-affecting 1 [LOCALIZE-ROWS row 107]; FIX5: none. The generated stamp reads STALE because the candidate changed after the determination (the sweep line, below); its pre-change verdict lines stand as the ledger's judgement of the file.

**Why.** The four test layers are independent instruments (source, render, localize patterns, translation); the package's job is to let a third party re-derive each verdict from the cited record without trusting this README's prose.

**Verify.** Re-run the T1 checker on candidate.txt (7 classified findings expected at baseline classes); read the RENDER-ROWS-2 and LOCALIZE-ROWS rows named above; `python3 review/build_review.py --check` confirms this package's generated files match the canonical candidate.

**Disposition.** Population PASS at the ledger determination; the STALE stamp is a freshness marker, not a re-judgement.

## Per-theme record

Wave narration, each act verified against the diff and the file's git history (canonical repository):

1. **Stage 2 EN13 integration, commit d7c1af6** — the whole port in one act: the base merge (Shattered Thoughts rev 34 CSS in ahead of the theme's own, banner-marked, with the porter's explanation), head delivery, the credit block with all eight fields (attribution value "SCP-JP" at this point), the author-label consolidation with its greeting carried as text, the lowercase rate removal, the license box created with its honest entries, the header-logo rule dropped with its reasons recorded twice, the body translated with the dummy-text substitution. The commit subject ("Stage 2 EN13: integrate lane lane-dsh-en13") claims an integration, which is what the bytes show: a finished lane port landed whole.
2. **FIX-CREDIT-D, commit 1869877** — one line in this file: 翻訳責任者 "SCP-JP" → "AI". The subject matches the bytes exactly.
3. **Post-determination usage sweep, commit b5cb724** — one line: the usage exhibit's self-include `[[include :scp-jp:theme:last-frontier]]` → `theme:last-frontier-jp` (cand L38). This act postdates the ledger determination and is the whole cause of the stamp's STALE reading: the verdict lines judge the pre-sweep file, and the sweep line is a repair in the campaign's own direction, recorded here rather than treated as a defect.

No defect flag is recorded for this theme. The checks that could have produced one were run and cleared on evidence: the credit link names the recorded host; the author field matches both of the original's attribution surfaces; the single code block is the delivery target the audit expects; the brace depth is clean; the merged base is banner-marked and its order verified; the one dropped CSS rule is documented in two places with its reason.

Discrepancies between record and bytes: (i) the ledger's (c3) line charges only P9, yet the file contains the batch's largest supplement (the base merge), a created license box, and a documented rule drop — all benign and all in-file documented, so the silence is the register's compression, not concealment; the package exists to close exactly this gap. (ii) The classifier's RESTORATION (B45) and COMPONENT-SWAP (B10) primaries do not fit the bytes, adjudicated in the Class summary. (iii) The BARE-RATE-DEL signature missed the original's lowercase `[[module rate]]`: the removal is real and correct (KB-09) but invisible to the signature table — proposed for the table's next version in the lane report (case-insensitive module-name matching for the rate signature). (iv) The binary-star asset travels under three names (the original's Binary_Star_Loop_Blink.gif, the candidate sample's binary-star-loop-blink.gif, the render row's "binary-star-loop-link.bmp"); the license entry's citation of the original name and URL is the form a reader can resolve, and the row's .bmp form appears to be the register's own shorthand — recorded so the coordinator can align them.

## Change set outside the two diffed files

None for this package: the theme's port, wave, and sweep act are all inside pages/theme:last-frontier-jp.txt (1869877 and b5cb724 are population commits; their other files belong to other themes' packages). The merged base's source (theme:shattered-thoughts at rev 34) is an input to the port, not a change: no canonical file for the base was created or altered by this theme's acts.

## Appendix — residue blocks

The two residue blocks resolve by shape; the 21 heuristic entries that follow them in the skeleton are translation pairs and component-removal alignments of the body, each read against the diff and resolved in the sections named.

- R1 (B26, orig L72 → cand L81): the sample string "Words" → 「言葉」 — section 6, P10.
- R2 (B48, orig L159–163 → cand L665–666): the header-logo rule's replacement by the porter's drop note — sections 4 and 10; the residue class exists because a rule-to-comment replacement matches no signature in the table.
- R3 (B5, orig L14–15 → cand L24–25): the greeting's translation ("Hey there! You should read some of the other stuff I made... or not!" → 「こんにちは！他の作品も読んでみてください……読まなくても構いません！」) — section 6.
- R4 (B7, orig L19 → cand L29): the author-label end-include's removal, the component consolidation of section 2 — the skeleton's note ("no translated counterpart; the writer's replaced-vs-dropped call is forced") is answered there: replaced, its payload carried as text.
- R5 (B19, orig L53 → cand L62): the lorem-ipsum sample replaced by Japanese dummy text — section 6.
- R6–R23 (the remaining heuristic entries): body prose and sample translation pairs (headings, tabber samples, link and footnote samples) — section 6, P10 by shape; no new signature is proposed for any of them.

## License and attribution

- **Title:** Last Frontier Theme
- **Author:** Vivarium, Yossipossi
- **Source:** https://scp-wiki.wikidot.com/theme:last-frontier — revision 41
- **License:** Creative Commons Attribution-ShareAlike 3.0 (CC BY-SA 3.0) — license deed: https://creativecommons.org/licenses/by-sa/3.0/
- **Adaptation:** This package holds a Sigma-10 migration port of the work; changes were made. See "Summary" and "Standing sections" in this README for what changed and why. Translator: AI (Muse and its delegated agents), per the campaign's standing attribution rule.
