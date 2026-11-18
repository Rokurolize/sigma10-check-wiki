# Review package — theme:golden-samdaecheon-jp (KO → JP port)
New to this package's shorthand? Read the notation key first: [How to read a review package](../HOW-TO-READ.md).

<!-- BEGIN GENERATED VERDICT STAMP — do not hand-edit; regenerate with review/build_review.py -->
## Verdict stamp
- Theme: theme:golden-samdaecheon-jp — origin KO, population #266 [GOSIGN2-LEDGER (b) row 266]
- Overall: STALE — candidate file changed since the verdict was computed (verdict against 435a6bb-era content, file sha256 now cfc0dd2bfc30b6744558b1c73b03c7b2b17df7217ae9626569b3982ac19eca35); the verdicts below were computed against that pre-change file, and the record verdict stands: a candidate revised through the campaign's recorded repairs is posted like a PASS row, with the change recorded in its package
- T1 (source check): FINDINGS (classified) — baseline 2026-11-16: exit 1, 4 errors / 3 warns / 1 info (pseudo-ref×4); standing classes dispositioned in register c1 [T1-ROWS row 285; GOSIGN2-LEDGER (b) row 266]
- T2/T3 (render, combined verdict): FINDINGS — [combined T2/T3] report `FINDINGS` — page runtime-hotlink site-theme chain only; sample credit-modal (preview-form) + 884px@768 overflow; T3 none beyond cross-cutting items. [RENDER-ROWS-2 (RENDER-S2-H (KO4))]
- Engine coverage: full matrix as run by the lane; coverage not separately caveated in the row [RENDER-ROWS-2 row]
- Credit modal: sample credit-modal errors dispositioned preview-form (credit:start-preview has no modal mechanism; GOSIGN-TESTS T2 amendment, 2026-11-16) [RENDER-ROWS-2 (RENDER-S2-H (KO4))]
- T4 (localize patterns + follow-up): FINDINGS — display-affecting findings: 2 [LOCALIZE-ROWS row 265, source LOCALIZE-S2-F]
- T5 (translation text): FINDINGS — the source reports judge T4/T5 jointly; one verdict word covers both [LOCALIZE-ROWS row 265]
- FIX5 re-judgement: none — no OPEN items at the ledger determination [GOSIGN2-LEDGER (b) row 266]
- Computed against: canonical commit b5cb7241f527a44933e45599b41df210690771c4; candidate file pages/theme:golden-samdaecheon-jp.txt sha256:cfc0dd2bfc30b6744558b1c73b03c7b2b17df7217ae9626569b3982ac19eca35; record: GOSIGN2-LEDGER.md + GOSIGN2-LEDGER-SUPPLEMENT.md as of the FIX5 head 435a6bb
<!-- END GENERATED VERDICT STAMP -->

## Status

| | |
|---|---|
| Verdict | **PASS** — passed at the ledger determination; this theme had no OPEN items and no §(e) register entry (GOSIGN2-LEDGER (b) row 266) |
| Standing items | **DISPOSITIONED** — T1 pseudo-ref ×4 (class (iii)); the render row's sample-layer items (section 11). **One defect flag from this package:** the usage snippet names a page that is not this candidate (candidate L28; per-theme record below) |
| Go-sign basis | COMPLETION-REPORT.md §10 (go-sign issued; 81 FIXED / 26 DISPOSITIONED / 0 OPEN across the sweep) |
| Named exception | None for this theme (the sweep's single named exception is theme:amethyst-v2, which has no candidate) |

## Provenance

| | Original | Candidate |
|---|---|---|
| Page | theme:golden-samdaecheon | theme:golden-samdaecheon-jp |
| Wiki | scpko.wikidot.com | SCP-JP Sigma-10 candidate (canonical repo) |
| Reference revision | 14 (first translation; the candidate's credit block records 初訳時参照リビジョン: 14) | — |
| Source of this copy | Campaign cache `gosign2-lanes/lane-oc-gs-localize-s2-F/orig-golden-samdaecheon.txt`, via the mirror store (class COPY, hash-verified against review/sources.tsv) | Canonical file `pages/theme:golden-samdaecheon-jp.txt`, copied at worktree HEAD f9cae19 |
| Lines / bytes | 537 lines / 10,403 bytes | 551 lines / 11,349 bytes |
| SHA-256 | cb76e9d7d070fef90a1be64065b9e12d2fa882d09bf315bb4811e17c7fac58e5 | 0be6ca3f1d0ba2d78baed02bceda93c11e21e542f606f6a1a570aa47d392c622 |

Wave history: the candidate was created by the Stage 2 KO4 integration (commit 56b9d1a, the LOCALIZE-S2-F wave's port); FIX-CREDIT-D (1869877) normalized its translator field; FIX4-IWA (8c62b7b) added the interwiki-style frame, and is the stamp's computed-against commit. No FIX5 commit touches this file, because the theme had no OPEN items for FIX5 to re-judge.

## Summary

A gold-and-black display theme for the Samdaecheon GoI, self-delivered from its own code page with a 489-line CSS exhibit and a short specimen body. The port follows the batch's standard shape — credit swap, frame addition, font substitution (the Korean display face Do Hyeon gives way to Noto Serif JP, load and three stacks together), asset repoints, full specimen translation — with two byte-level details a skim would miss: the original's two malformed `text-shadow` declarations (`…; !important;`, which browsers read as a shadow without the importance flag) are repaired to the well-formed form in the candidate, and the specimen's visited-link example is repointed to this candidate's own `-jp` page even though the usage snippet above it was not. Measured churn (diff.md, the generator's difflib count with autojunk off: +49/−40 in 24 change blocks). One defect flag arises, on the usage snippet's page name (per-theme record).

## Class summary

Auto-classification by review/classify_hunks.py (signature table 2026-11-17.1): 24 change blocks — 13 specific (54.2%), 11 heuristic (45.8%), 0 residue, 0 skipped. Pattern citations below name the KB entry; the patterns/ tree state cited throughout is commit 9c5e9079afb01d30cb9fc4ef9d714e5591eb2ffa.

| Label | Blocks |
|---|---|
| TRANS-UNANCHORED | 8 |
| CSS-BODY | 6 |
| DRAFT-HOST | 5 |
| TRANSLATION-ANCHORED | 5 |
| IFTAGS | 2 |
| SELF-DELIVERY | 2 |
| BARE-RATE-DEL | 1 |
| COMMENT-TEXT | 1 |
| CONTENT-STRING | 1 |
| CREDIT-PREVIEW | 1 |
| CREDIT-PROSE | 1 |
| DELIVERY-HOST | 1 |
| ESCAPED-INCLUDE | 1 |
| EXHIBIT-RESTRUCTURE | 1 |
| FONT-IMPORT | 1 |
| INCLUDE-REPOINT | 1 |
| JPFONT-LOAD | 1 |
| LINK-REPOINT | 1 |
| TASL-FIELDS | 1 |

Adjudication for this README (every block was read against the bytes): the 6 CSS-BODY blocks resolve as 3 P7 font-stack rewrites (B17, B20, B24, section 4), 2 malformed-declaration repairs on otherwise identical `text-shadow` lines (B18, B21, per-theme record), and 1 `content:` string translation (B19, section 6); the single EXHIBIT-RESTRUCTURE primary (B8) is an asset-URL repoint inside the image-block exhibit include, not a restructuring (section 8); the heuristic translation blocks are one-line prose and specimen translations, verified line by line (section 6). After adjudication no block is left unexplained.

## Standing sections

### 0. Header and provenance frame

- **What:** Theme theme:golden-samdaecheon-jp; original theme:golden-samdaecheon on scpko at reference revision 14; candidate `pages/theme:golden-samdaecheon-jp.txt`. Provenance route: derived from the original at the reference revision by the LOCALIZE-S2-F wave (sources.tsv kind: standard; no production JP counterpart exists for this theme, so the R4 adoption question does not arise). The original's shape: a head delivery module (original L1–3), the gate, a prose and specimen body, and the CSS as a `[[code]]` exhibit (original L48–535); the candidate preserves that shape with the frame inserted between the delivery module and the gate (candidate L5–8).
- **Why:** Section 0 declares the provenance route so every later count is read against the right baseline; the gate's tag is P2 and the delivery shape is section 3.
- **Verify:** The sources.tsv row for golden-samdaecheon-jp; `sha256sum original.txt` against the Provenance table.
- **Disposition:** Standing (the route itself); the gate and frame changes are recorded in sections 2–3.

### 1. Credit and attribution

- **What:** The original's credit furniture is a labelled bare `[[module Rate]]` (original L9–12, under its 평가 모듈 label) and the authorship prose at original L14, naming [[*user c_bonefish]] and [[*user Denevola]] as the theme's makers. The candidate deletes the Rate (block B4) and installs the JP form: a `:scp-jp:credit:start-preview`/`end-preview` block (candidate L12–21) carrying the eight ruling-3 fields (title 黄金参大天CSSテーマ; 翻訳責任者 AI; 翻訳年 2026; 原題 황금 삼대천 CSS 테마; 著作権者 c_bonefish, Denevola; 作成年 2021; 初訳時参照リビジョン 14; the source link, section 7) — the 著作権者 field names both authors the original's prose names, so no one is dropped. The authorship prose itself is also carried, translated (candidate L25). The translator field took its ruling-3 form in FIX-CREDIT-D (1869877). The T4 row's second charge was 型 3, image attribution: the bytes show where this theme's image attribution lives — the exhibit's banner comment, carried unchanged on both sides, credits the header code (thd-glasses), the info-bar code (EstrellaYoshte), and the logo (NAVLA) under CC BY-SA 3.0; the image-block caption names no author on either side (original L22, candidate L33, both "logo" captions). The port therefore neither dropped nor added image attribution; the campaign's recorded fix for the charge is the credit-fields completion (ledger §(c3): P3 FIXED, credit waves, checker-verified). There is no T7 credit-module CSS on either side and no license box on either side; the banner's CC BY-SA 3.0 line is the license record, and it survives.
- **Why:** P3/T1 (KB-09) for the furniture swap (the preview credit module is rate-bearing, so the bare Rate is deleted rather than duplicated); ruling 3 for the eight fields. The 型 3 adjudication follows the bytes over the charge's shorthand: attribution that exists in the original (the banner) exists in the candidate, in the same place.
- **Verify:** `grep -n 'module Rate' candidate.txt` returns nothing; read candidate L12–21 against the eight fields; read the banner at candidate L66–74 against original L55–63.
- **Disposition:** FIXED (GOSIGN2-LEDGER §(c3): P3 credit fields FIXED, credit waves, checker-verified).

### 2. Includes and components

- **What:** Two repoints, one kept form, and one flag. (1) The specimen's visited-link example repoints from `[[[theme:golden-samdaecheon|…]]]` to `[[[theme:golden-samdaecheon-jp|…]]]` (block B11, candidate L49) — the candidate's own `-jp` page, correctly named. (2) The image-block exhibit include (block B8, candidate L33) keeps the branch-local unprefixed form `[[include component:image-block …]]` on both sides: unprefixed, it names the local wiki's component, which on scp-jp is the JP image-block, so no P1 repoint applies to the include itself; the change inside it is the `name=` asset URL (section 4) and the translated caption. (3) The usage snippet (block B6, candidate L28): the original's `@@[[include :scpko:theme:golden-samdaecheon]]@@` becomes `@@[[include :scp-jp:theme:golden-samdaecheon]]@@` — prefix repointed, page name not, against the candidate's own identity and against the correct form the same file uses at L49. This is flagged, not edited (per-theme record below). The frame and credit includes are sections 3 and 1.
- **Why:** P1 (KB-15): includes name the JP page that actually exists; the contrast between candidate L49 (right) and L28 (wrong) is the flag's whole evidence.
- **Verify:** `grep -n '\[\[include' candidate.txt` — the frame, the credit pair, the image-block, and candidate L28.
- **Disposition:** Repoints applied; the usage snippet is the package's defect flag (per-theme record).

### 3. Delivery and code loading

- **What:** The theme self-delivers from its own code page in both versions: a head `[[module CSS]]` importing `theme:golden-samdaecheon/code/1` from scpko.wikidot.com (original L2, unquoted URL form) becomes the same import from the candidate's own delivery on the draft host (candidate L2, block B1), and the CSS text itself rides as the `[[code]]` exhibit on both sides (original L48–535 → candidate L59–549) with the port's changes inside it (sections 4, 6, 10). **Frame paragraph (the M-frame addition):** the original carried no interwiki-style frame (LOCALIZE-ROWS row 265, 型 6); the candidate adds one at candidate L5–8 with `priority=1` and `theme=` naming its own /1 delivery on the draft host — the single-layer own-code form, in the spaced parameter style. The ledger records the outcome as P6 FIXED (frame waves; checker-verified); the frame arrived in FIX4-IWA (commit 8c62b7b, "missing interwiki frames added to 31 themes (KB-07a)").
- **Why:** P4/T9 for the own-code repoint (the delivery follows the candidate, not the branch page); P6/T3 (KB-07) for the added frame. KB-41 covers the draft-host form of both live delivery lines (class (iii), rewritten to the production host at posting).
- **Verify:** Read candidate L1–8 and L59; `grep -n 'scpko' candidate.txt` returns only the credit source link (section 7).
- **Disposition:** FIXED (P6); the draft-host URLs are DISPOSITIONED (class (iii)).

### 4. Fonts and assets

- **What:** Fonts, by substitution. The original loads one Korean display face from Google Fonts (original L62: Do Hyeon) and names it first in three stacks (original L100, L123, L220: `'Do Hyeon', sans-serif`). The candidate replaces the load (block B15: candidate L76, Noto Serif JP 400;700 from the same host) and rewrites all three stacks (blocks B17, B20, B24, the CSS-BODY primaries): `'Noto Serif JP', 'Yu Mincho', 'Hiragino Mincho ProN', serif` — the first-named face is the loaded one, so no KB-16 gap arises, and the generic changes from sans-serif to serif with the Mincho fallbacks. Assets: three image URLs repoint to the candidate's own file area — the image-block's logo (candidate L33, production-host form `scp-jp.wdfiles.com`, block B8) and the two CSS backgrounds (blocks B16, B23: background.png at candidate L80, logo.png at candidate L155), the CSS pair in draft-host form; file names unchanged on all three. The original's CSS asset URLs used the `scpko.wikidot.com/local--files` form with an unencoded colon; both candidate forms carry the encoded `theme%3A…` path.
- **Why:** P7/T5 with KB-16, in its substitution form: Do Hyeon cannot render Japanese, so a JP display face takes its role, load and stacks changed together. P5/KB-17 for the asset re-hosting to the JP side.
- **Verify:** `grep -n 'Do Hyeon' candidate.txt` returns nothing; `grep -n 'font-family' candidate.txt` — three lines, all the JP stack; `grep -n 'wdfiles' candidate.txt` against the asset list above.
- **Disposition:** Substitution applied; the draft-host asset URLs are DISPOSITIONED (class (iii)); the image-block URL's production-host form is the posting form (class (ii) mechanics).

### 5. Header, sidebar, and site furniture

- **What:** No header variables are overridden on either side (no `--header-title`, `--header-subtitle`, or `--logo-image`); the theme's header identity is its CSS: the 350px header with the logo background (section 4), the h1 `content:` string and the h2 slogan string (both translated, section 6), and the text-shadow outline pair (per-theme record). No sidebar or topbar adaptation was needed: the candidate inherits the JP site furniture through the environment, and the theme's own furniture rules needed no structural change to sit on it.
- **Why:** P8/P9 are checked and absent as edits: what the theme declares in this area is string content, which is P10/KB-18 and is counted there.
- **Verify:** `grep -n -- '--header-' candidate.txt` returns nothing; read candidate L79–160 against original L65–146.
- **Disposition:** Standing.

### 6. Text translation

- **What:** The specimen body is translated throughout, in the classifier's counts: 5 TRANSLATION-ANCHORED and 8 TRANS-UNANCHORED primary blocks (B3, B5–B7, B9–B14), each verified line by line against the mirror for this README. In groups: the title and authorship prose (candidate L23, L25); the usage prose (candidate L27); the heading specimens (candidate L35–40); the tabview specimens, including the keyboard-mash placeholder text (original L35 `ㅁㄴㅇㄹ` → candidate L46 サンプル本文） and the link specimens (candidate L48–49, L51, with the footnote's onomatopoeia 똑똑 → コンコン）; and the two reader-visible CSS strings (B19: `content: "삼대천"` → `"参大天"`, candidate L121, the header's rendered name in Japanese glyph form; B22: the slogan `content: "셋이 모여 천하를 든다"` → `"三者会して天下を挙ぐ"`, candidate L145). In-CSS comment text (R1): the exhibit's section comments are carried in English on both sides (`/* Header */` and companions); the banner comment's added lines are porter annotations (section 10). Korean survives in the candidate only as quotation: the credit block's original-title field (candidate L16). R5 glyph-form conversion: the 参大天 string is the Japanese rendering of the theme's name (a translation, counted above), not a retained-string glyph conversion.
- **Why:** P10 (body, usage, and sample translation is the port's purpose) and KB-18 (reader-visible strings, including `content:`). The unanchored group is where a silent deletion would hide, which is why each was read individually.
- **Verify:** The pairs are diff.md's body sections in order; a Hangul scan of candidate.txt returns only candidate L16.
- **Disposition:** Standing (the port itself); no untranslated reader-visible text remains outside the quotation.

### 7. Links

- **What:** The candidate's live outbound link is the credit block's source link (candidate L20), naming `https://scpko.wikidot.com/theme:golden-samdaecheon` — the original's recorded host (review/sources.tsv), so it names the serving original and no host defect arises. The specimen's link pair is section 2 (the visited-link example repointed to the candidate's own page; the `[# …]` unvisited form is a placeholder on both sides). The authorship prose's user links ([[*user c_bonefish]], [[*user Denevola]], candidate L25) are wiki-user links, carried with the prose they sit in.
- **Why:** P11: prose links take the JP counterpart or the serving original under the dead-reference evidence standard.
- **Verify:** Compare candidate L20's host against the sources.tsv row's original_url host (scpko.wikidot.com) — identical.
- **Disposition:** Standing.

### 8. Structure

- **What:** The localize.md closing rule holds. The topology pass finds the same two components on both sides in the same order (head module-css, then the code-css exhibit), no relocations; variable names, selectors, and rule order inside the exhibit are preserved, and the JP additions (frame, credit block) sit at the head rather than interleaved into the inherited CSS. The classifier's one EXHIBIT-RESTRUCTURE primary (B8) adjudicates to the image-block exhibit's asset repoint: the include, its caption (translated), and its width survive; only the `name=` URL's host and folder change — the standing false-fire shape for this label (include repoints inside exhibit regions). An exhibit census confirms the shape: the specimen body entire (headings, tabview with both tabs, link specimens) and the full CSS exhibit are present on both sides in the same order — nothing was dropped or replaced, so the R3 question does not arise for this theme. The two `text-shadow` repairs (per-theme record) are in-place declaration fixes, not restructuring.
- **Why:** R3 exists to force exactly this adjudication, because a restructure and a deletion share a diff shape and ledger class I charges the silent form; here the census, not the label, decides.
- **Verify:** Compare `grep -n '\[\[tab\|\[\[code\|\[\[module' original.txt candidate.txt` — the sequences correspond one to one.
- **Disposition:** Standing; no structural deletion, no class I item.

### 9. Formatting only

- **What:** None as a primary class: the classifier finds no whitespace-only block and no re-indentation (0 and 0) among the 24 blocks, so the R7 follow-up-diff hazard is not triggered.
- **Why:** Formatting churn is disclosed as its own class so it is never mistaken for a semantic change.
- **Verify:** Section 9 of the classifier skeleton for this package (WS-ONLY 0, re-indentation 0).
- **Disposition:** None required.

### 10. Porter annotations

- **What:** One annotation, inside the exhibit's banner comment (block B14, candidate L72–73): two lines appended to the original's banner — "SCP-JP版: 2026年に日本語版へ移植。作成者: c_bonefish, Denevola（韓国支部）。翻訳: SCP-JP。" The banner itself (header-code and info-bar adoptions, the logo credit, CC BY-SA 3.0) is the original's, carried unchanged above them (section 1). The annotation is porter-visible only; the TASL record proper is the credit block, whose translator field carries the ruling-3 form (AI) — the banner line's collective wording is the porter's provenance note, not a second credit record, and the two are recorded here so a reviewer is not left to reconcile them unaided. The candidate has no `[!-- --]` notes.
- **Why:** R2: porter-added text is part of the change record and is enumerated wherever it rides, including inside a carried comment block.
- **Verify:** Read candidate L66–74 against original L55–63.
- **Disposition:** Standing.

### 11. Dispositions and exceptions

- **What:** Three items, each with its ground. (1) T1's four pseudo-ref errors: class (iii), draft-form — the candidate's own draft-host lines (the delivery import, the frame `theme=` URL, and the two CSS asset URLs of sections 3–4); the posting procedure rewrites them to the production host, and fix lanes never "fix" them in the candidate. (2) The render row's items (RENDER-ROWS-2, RENDER-S2-H (KO4)): the page's runtime-hotlink site-theme chain (KB-40, environment layer) and the sample's credit-modal errors (KB-32: the preview form has no modal mechanism, ruling 5) plus its 884px@768 overflow reading — sample and environment layer, recorded as not charged to the candidate. (3) The usage-snippet flag (per-theme record) is not in this list: no ledger line dispositions it, which is why it is flagged rather than dispositioned.
- **Why:** A disposition is a decision with grounds (AGENTS.md §3 classes (i)/(ii)/(iii); the named KB entries), not an omission; environment-layer lines are recorded as not-charged.
- **Verify:** Each item names its deciding record above and in the per-theme record.
- **Disposition:** DISPOSITIONED (items 1–2); item 3 flagged with evidence.

### 12. Verification

- **What:** (a) T1 source check (T1-ROWS row 285): exit 1, 4 errors / 3 warns / 1 info; all four errors are pseudo-ref, class (iii); there is no class (i) error. (b) T2/T3 render (RENDER-ROWS-2, lane RENDER-S2-H (KO4)): FINDINGS, the items of section 11(2), all dispositioned; engine coverage as run by the lane, not separately caveated in its row. (c) T4/T5 (LOCALIZE-ROWS row 265): FINDINGS jointly, display-affecting findings 2 — the row's charges are 型 3, image attribution (section 1: the campaign's fix is the credit-fields completion), and 型 6, the absent interwiki-style frame (since FIXED by FIX4-IWA); the same row records the translation, the variable localization, and the attribution prose as good quality. The ledger §(c3) line records the outcomes: P3 FIXED (credit waves, checker-verified), P6 FIXED (frame waves, checker-verified). (d) This package is self-verifying: `python3 review/build_review.py --check` regenerates diff.md and the verdict stamp from the two byte-faithful copies in this directory and compares. Counts in this README are the generator's (difflib, autojunk off): +49/−40 in 24 change blocks.
- **Why:** Verification claims name the cheapest deciding check and its result, not a general assurance.
- **Verify:** Re-run the checker on `pages/theme:golden-samdaecheon-jp.txt` and `python3 review/build_review.py --check` in this repo.
- **Disposition:** PASS (GOSIGN2-LEDGER (b) row 266; go-sign, COMPLETION-REPORT §10).

## Per-theme record

### The usage snippet names a different page (defect flag)

The usage snippet is the one line a reader copies to adopt the theme, and on the bytes it names the wrong page. Candidate L28 reads `> @@[[include :scp-jp:theme:golden-samdaecheon]]@@`. This candidate is theme:golden-samdaecheon-jp: its canonical file is `pages/theme:golden-samdaecheon-jp.txt`, its frame `theme=` URL and its module import both name `theme%3Agolden-samdaecheon-jp`, and the same file's own link specimen (candidate L49) names `theme:golden-samdaecheon-jp` correctly — the port knew the candidate's name and used it in one place but not the other. Probes run for this package (2026-11-17): `https://scp-jp.wikidot.com/theme:golden-samdaecheon` returns 404 and `https://scp-jp.wikidot.com/theme:golden-samdaecheon-jp` returns 404 — neither page is posted yet, so the probe cannot settle intent; what the bytes settle is that the snippet is inconsistent with the candidate's own identity, and if the candidate posts under its canonical name the snippet will point at a page that does not exist. No ledger line dispositions the snippet's name (the T1 pseudo-ref class (iii) covers references to the not-yet-posted page itself, which this is not, on the bytes). The candidate is left exactly as it stands, per the standing rule for fix lanes; the repair, if the coordinator confirms it, is the one-line repoint of candidate L28 to the candidate's own page name, after which this package's diff.md and stamp need no change beyond regeneration (the candidate file's hash in the stamp would change).

### Two malformed `text-shadow` declarations, repaired in place

Blocks B18 and B21 pair lines that look identical at a glance; the difference is at the end of the line. The original's two outline declarations read `text-shadow: 1px 0 #EDD200, …, -1px -1px #EDD200; !important;` (original L105, L128) — the importance flag sits after the closing semicolon, where CSS discards it, so the shadow applies without `!important`. The candidate reads `… #EDD200 !important;` (candidate L119, L142), the well-formed form that gives the declaration the force the original's author evidently intended. This is the KB-03 malformed-declaration shape, repaired in place inside two otherwise unchanged lines; the classifier's CSS-BODY label does not name it, so it is recorded here rather than left inside a heuristic count. No other declaration in the exhibit carries the shape (a scan for `; !important` in original.txt returns exactly these two lines, and candidate.txt returns none).

## Change set outside the two diffed files

The diff covers two files; the port's record is one file larger. `pages/theme-decoration-sample-golden-samdaecheon-jp.txt` is the decoration sample the render checks ran against (its findings are the sample half of section 11(2)); it belongs to this theme's record but carries no port change of its own to explain here. There are no companion fragments, no shared base file, and no inbound-link repairs in other candidates for this theme.

## License and attribution

- **Title:** 황금 삼대천 CSS 테마
- **Author:** c_bonefish, Denevola
- **Source:** https://scpko.wikidot.com/theme:golden-samdaecheon — revision 14
- **License:** Creative Commons Attribution-ShareAlike 3.0 (CC BY-SA 3.0) — license deed: https://creativecommons.org/licenses/by-sa/3.0/
- **Adaptation:** This package holds a Sigma-10 migration port of the work; changes were made. See "Summary" and "Standing sections" in this README for what changed and why. Translator: AI (Muse and its delegated agents), per the campaign's standing attribution rule.
