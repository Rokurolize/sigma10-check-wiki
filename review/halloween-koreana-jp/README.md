# Review package — theme:halloween-koreana-jp (KO → JP port)

<!-- BEGIN GENERATED VERDICT STAMP — do not hand-edit; regenerate with review/build_review.py -->
## Verdict stamp
- Theme: theme:halloween-koreana-jp — origin KO, population #267 [GOSIGN2-LEDGER (b) row 267]
- Overall: STALE — candidate file changed since the verdict was computed (verdict against 435a6bb-era content, file sha256 now d52dd5866fc749015d7f1d4e1084e746dce816ec0d0a870d346b5c9135d586ff); verdict not carried over, re-judgement required
> verdicts below describe the pre-change file
- T1 (source check): FINDINGS (classified) — baseline 2026-11-16: exit 1, 3 errors / 1 warn / 0 infos (pseudo-ref×3); standing classes dispositioned in register c1 [T1-ROWS row 286; GOSIGN2-LEDGER (b) row 267]
- T2/T3 (render, combined verdict): FINDINGS — [combined T2/T3] report `FINDINGS` — page runtime-hotlink site-theme chain only; sample credit-modal (preview-form) + 884px@768 overflow; T3 none beyond cross-cutting items. [RENDER-ROWS-2 (RENDER-S2-H (KO4))]
- Engine coverage: full matrix as run by the lane; coverage not separately caveated in the row [RENDER-ROWS-2 row]
- Credit modal: sample credit-modal errors dispositioned preview-form (credit:start-preview has no modal mechanism; GOSIGN-TESTS T2 amendment, 2026-11-16) [RENDER-ROWS-2 (RENDER-S2-H (KO4))]
- T4 (localize patterns + follow-up): FINDINGS — display-affecting findings: 1 [LOCALIZE-ROWS row 266, source LOCALIZE-S2-F]
- T5 (translation text): FINDINGS — the source reports judge T4/T5 jointly; one verdict word covers both [LOCALIZE-ROWS row 266]
- FIX5 re-judgement: none — no OPEN items at the ledger determination [GOSIGN2-LEDGER (b) row 267]
- Computed against: canonical commit b5cb7241f527a44933e45599b41df210690771c4; candidate file pages/theme:halloween-koreana-jp.txt sha256:d52dd5866fc749015d7f1d4e1084e746dce816ec0d0a870d346b5c9135d586ff; record: GOSIGN2-LEDGER.md + GOSIGN2-LEDGER-SUPPLEMENT.md as of the FIX5 head 435a6bb
<!-- END GENERATED VERDICT STAMP -->

## Status

| | |
|---|---|
| Verdict | **PASS** — passed at the ledger determination; this theme had no OPEN items and no §(e) register entry (GOSIGN2-LEDGER (b) row 267) |
| Standing items | **DISPOSITIONED** — T1 pseudo-ref ×3 (class (iii)); the render row's sample-layer items (section 11). **One defect flag from this package:** the usage snippet names the original's page name, not this candidate (candidate L20; per-theme record below) |
| Go-sign basis | COMPLETION-REPORT.md §10 (go-sign issued; 81 FIXED / 26 DISPOSITIONED / 0 OPEN across the sweep) |
| Named exception | None for this theme (the sweep's single named exception is theme:amethyst-v2, which has no candidate) |

## Provenance

| | Original | Candidate |
|---|---|---|
| Page | theme:halloween-koreana | theme:halloween-koreana-jp |
| Wiki | scpko.wikidot.com | SCP-JP Sigma-10 candidate (canonical repo) |
| Reference revision | 35 (first translation; the candidate's credit block records 初訳時参照リビジョン: 35) | — |
| Source of this copy | Campaign cache `gosign2-lanes/lane-oc-gs-localize-s2-F/orig-halloween-koreana.txt`, via the mirror store (class COPY, hash-verified against review/sources.tsv) | Canonical file `pages/theme:halloween-koreana-jp.txt`, copied at worktree HEAD f9cae19 |
| Lines / bytes | 49 lines / 1,259 bytes | 55 lines / 2,388 bytes |
| SHA-256 | 853391c38017816e811d06166a34cca4665fe66b9d0d6b06690061f857bc528d | 4dcb0c71bd04c54063eb7dd4ee3c6bfe7fc5e17eb5bc55809d6215d6cb04ceb3 |

Wave history: the candidate was created by the Stage 2 KO4 integration (commit 56b9d1a, the LOCALIZE-S2-F wave's port); FIX-CREDIT-D (1869877) normalized its translator field; FIX4-IWA (8c62b7b) added the interwiki-style frame, and is the stamp's computed-against commit. No FIX5 commit touches this file, because the theme had no OPEN items for FIX5 to re-judge.

## Summary

The smallest port in this batch: a 49-line layer theme that, in the original, does almost nothing itself — it imports the KO branch's site theme, loads two Korean display faces, and restyles the header over two background images. The candidate keeps that shape and size while changing its allegiance: the KO site-theme import is dropped (the JP environment's own site theme, Sigma-10, is the base now, as the candidate's own first footnote discloses), the Korean faces are replaced by two Google Fonts JP faces with the substitution and its ground stated in a second footnote, the two images move to the candidate's own JP file area, and the head gains the two pieces of JP furniture the original never had — a preview credit block and the interwiki-style frame. Measured churn (diff.md, the generator's difflib count with autojunk off: +30/−24 in 8 change blocks). One defect flag arises, on the usage snippet's page name (per-theme record).

## Class summary

Auto-classification by review/classify_hunks.py (signature table 2026-11-17.1): 8 change blocks — 5 specific (62.5%), 3 heuristic (37.5%), 0 residue, 0 skipped. Pattern citations below name the KB entry; the patterns/ tree state cited throughout is commit 9c5e9079afb01d30cb9fc4ef9d714e5591eb2ffa.

| Label | Blocks |
|---|---|
| DRAFT-HOST | 4 |
| COMMENT-TEXT | 2 |
| CSS-BODY | 2 |
| SELF-DELIVERY | 2 |
| TRANS-UNANCHORED | 2 |
| CREDIT-PREVIEW | 1 |
| DELIVERY-HOST | 1 |
| FONT-IMPORT | 1 |
| IFTAGS | 1 |
| TRANSLATION-ANCHORED | 1 |
| TASL-FIELDS | 1 |

Adjudication for this README (every block was read against the bytes): the 2 CSS-BODY blocks are the P7 font-stack rewrites of section 4, not unclassified churn; the 3 heuristic blocks (B4, B6, B7) resolve as the second @font-face deletion plus a translated CSS comment (B4, sections 4 and 6) and the two stack rewrites (B6, B7, section 4); the FONT-IMPORT primary (B2) is the exhibit's first-line swap, where the dropped KO site-theme import and the added Google Fonts load share one diff position (sections 3 and 4). After adjudication no block is left unexplained.

## Standing sections

### 0. Header and provenance frame

- **What:** Theme theme:halloween-koreana-jp; original theme:halloween-koreana on scpko at reference revision 35; candidate `pages/theme:halloween-koreana-jp.txt`. Provenance route: derived from the original at the reference revision by the LOCALIZE-S2-F wave (sources.tsv kind: standard; no production JP counterpart exists for this theme, so the R4 adoption question does not arise). The original is a pure layer: its exhibit imports the KO site theme's code (`component:theme/code/1`, original L3) and adds fonts and header rules; the candidate's head instead carries the frame (candidate L1–4) ahead of the localized gate (candidate L6).
- **Why:** Section 0 declares the provenance route so every later count is read against the right baseline; the gate's tag is P2, the frame is P6 (section 3), and the dropped site-theme import is the base change recorded in section 3.
- **Verify:** The sources.tsv row for halloween-koreana-jp; `sha256sum original.txt` against the Provenance table.
- **Disposition:** Standing (the route itself); the gate and frame changes are recorded in sections 2–3.

### 1. Credit and attribution

- **What:** The original carries no credit furniture at all — no Rate module, no info block, no license box; nothing in its 49 lines names an author. The candidate installs the JP form from nothing (block B1): a `:scp-jp:credit:start-preview`/`end-preview` block (candidate L8–17) carrying the eight ruling-3 fields (title ハロウィン・コリアナテーマ; 翻訳責任者 AI; 翻訳年 2026; 原題 손 있는 날 테마; 著作権者 Salamander724; 作成年 2022; 初訳時参照リビジョン 35; the source link, section 7). The translator field took its ruling-3 form in FIX-CREDIT-D (1869877). There is no T7 credit-module CSS on either side (the theme styles no credit element, and no supplement adds any), and no license box on either side.
- **Why:** P3/T1: the preview credit block is the rate-bearing JP form, so the theme gains its rating and attribution surface in one include pair rather than by importing the branch furniture the original never had. Ruling 3 fixes the eight fields; because the original names no author in-file, there is no in-file credit for the 著作権者 field to drop anyone from — the field's value is the page's authorship as recorded by the port, and the T4 lane found the attribution exemplary (LOCALIZE-ROWS row 266: the frame's absence is its only charge).
- **Verify:** Read candidate L8–17 against the eight fields; `grep -n 'module Rate\|info:start\|license' candidate.txt` returns nothing.
- **Disposition:** Standing (present from creation; the T4 row charges nothing against this section).

### 2. Includes and components

- **What:** Three include pairs, all `:scp-jp:`: the frame (candidate L1–4, section 3), the credit pair (candidate L8, L17, section 1), and one flag — the usage snippet at candidate L20, `@@[[include :scp-jp:theme:halloween-koreana]]@@`, which names the original's page name without the `-jp` suffix this candidate's own name, file name, frame `theme=` URL, and module import all carry. The original has no usage snippet (its file is CSS only); the snippet is the port's own added prose, so the wrong name was written by the port, not inherited. This is flagged, not edited (per-theme record below). The original's one foreign reference, the `:scpko:component:theme` code import inside the exhibit, is a delivery line, not an include; it is section 3.
- **Why:** P1 (KB-15): an include must name the JP page that actually exists; the snippet is the one line a reader copies to adopt the theme, so its target name is the theme's identity, not a detail.
- **Verify:** `grep -n '\[\[include' candidate.txt` — the frame, the credit pair, and candidate L20.
- **Disposition:** Frame and credit applied; the usage snippet is the package's defect flag (per-theme record).

### 3. Delivery and code loading

- **What:** The original delivers in two lines: the exhibit's first line imports the KO site theme's code (`https://scpko.wikidot.com/component:theme/code/1`, original L3), making this theme a layer over the KO branch's site theme, and the tail module imports the theme's own code page (`.../theme:halloween-koreana/code/1`, original L48). The candidate drops the site-theme import outright: nothing in the file imports a base, because in the JP environment the base is the site theme itself (Sigma-10), which the page already sits on — the candidate's first footnote (candidate L19) states exactly this substitution and its reason. The tail module's own-code import is repointed to the candidate's own delivery on the draft host (candidate L54, block B8). **Frame paragraph (the M-frame addition):** the original carried no interwiki-style frame (LOCALIZE-ROWS row 266, 型 6, its only T4 charge); the candidate adds one at candidate L1–4 with `priority=1` and `theme=` naming its own /1 delivery on the draft host — the single-layer own-code form, in the spaced parameter style. The ledger records the outcome as P6 FIXED (frame waves; checker-verified); the frame arrived in FIX4-IWA (commit 8c62b7b, "missing interwiki frames added to 31 themes (KB-07a)").
- **Why:** P4/T9 for the own-code repoint (the delivery follows the candidate, not the branch page); P6/T3 (KB-07) for the frame. The base change is not a deletion of function: the original's base import existed to pull in a site theme the JP page cannot use, and the JP site theme needs no import. KB-41 covers the draft-host form of both live delivery lines (class (iii), rewritten to the production host at posting).
- **Verify:** Read candidate L1–4 and L53–55; `grep -n 'scpko' candidate.txt` returns only the credit source link and the footnote's quoted component name (section 7).
- **Disposition:** FIXED (P6); the draft-host URLs are DISPOSITIONED (class (iii)).

### 4. Fonts and assets

- **What:** Fonts, by substitution with the ground stated in-file. The original loads two Korean faces by `@font-face` from jsdelivr noonnu distributions (original L5–17: 열사체/Korea_hero and 정선아리랑뿌리체/JSArirangPPURI) and names each first in one header stack (original L35, L40). The candidate deletes both `@font-face` blocks (blocks B3–B4), loads two JP faces from Google Fonts at the exhibit's head (candidate L23: New Tegomin and Yuji Syuku — block B2, the FONT-IMPORT primary, which shares its diff position with the dropped site-theme import of section 3), and rewrites the two stacks (blocks B6, B7, the CSS-BODY primaries): `'New Tegomin', 'Yu Mincho', 'Hiragino Mincho ProN', serif` for the h1 (candidate L41) and `'Yuji Syuku', 'Yu Mincho', 'Hiragino Mincho ProN', serif` for the h2 (candidate L46) — each stack's first-named face is the one the L23 load actually delivers, so no KB-16 gap arises. The candidate's second footnote (candidate L19) discloses the substitution and its ground: the noonnu faces are not carried by any distributor inside the campaign's direct-link exception, so Google Fonts faces take their roles. Assets: the two background images (blocks B3, B5) repoint from `scpko.wdfiles.com/local--files/theme%3Ahalloween-koreana/` to the candidate's own draft-host file area (`sigma10-jp-test.wdfiles.com/local--files/theme%3Ahalloween-koreana-jp/`), file names unchanged (body_1031.png, candidate L26; logo_1031.png, candidate L36).
- **Why:** P7/T5 with KB-16, in its substitution form (the same form as dear-dictator's): the Korean faces cannot render Japanese and their distribution source falls outside the direct-link exception, so named JP faces from an allowed host replace them, load and stacks changed together. P5/KB-17 for the asset re-hosting to the JP side.
- **Verify:** `grep -n '@font-face\|noonnu\|jsdelivr' candidate.txt` returns nothing; `grep -n 'font-family' candidate.txt` — two lines, both JP stacks; `grep -n 'wdfiles' candidate.txt` against the asset list above.
- **Disposition:** Substitution applied; the draft-host asset URLs are DISPOSITIONED (class (iii) draft form; posting rewrites them to the production host).

### 5. Header, sidebar, and site furniture

- **What:** None — no header variable is overridden (no `--header-title`, `--header-subtitle`, or `--logo-image` on either side), no sidebar or topbar rule exists in the original to adapt, and the candidate adds none. The theme's whole furniture content is the `#header` rule pair, carried with only the section 4 changes (asset host, comment language, font stacks); its geometry (height 140px, z-index 10, logo position) is byte-identical to the original's.
- **Why:** P8/P9 are checked and absent: a layer theme over the site theme inherits the JP furniture through the environment, and the original declares no variables for the port to convert.
- **Verify:** `grep -n -- '--header-\|#side-bar\|#top-bar' candidate.txt` returns nothing.
- **Disposition:** None required.

### 6. Text translation

- **What:** The original carries no prose body at all, so there is nothing to translate in place; the candidate's one prose paragraph (candidate L19) is the port's own usage text, written for the JP page: it names the theme, gives the snippet (section 2's flag), and carries the two disclosure footnotes (sections 3, 4, 10). In-CSS text (R1): the exhibit's two comments are translated in place (blocks B4–B5: `/* HEADER */` → `/* ヘッダー */`, candidate L29; `/* FOR MENU */` → `/* メニュー用 */`, candidate L35). Korean survives in the candidate only as quotation: the credit block's original-title field (candidate L12) and the font names quoted inside the second footnote (candidate L19). R5 glyph-form conversion: none — the source is Korean and no retained string changes glyph form.
- **Why:** P10 for the usage text (a theme page with no usage text would fail its readers in the new environment); KB-18/R1 for the comments, which are porter-visible only and are recorded here so they are not mistaken for reader-visible translation. The footnotes follow P10's sanctioned form for original-side circumstances (the `**訳注:**` substance in footnote form).
- **Verify:** A Hangul scan of candidate.txt returns only candidate L12 and the quoted names in L19; read candidate L29 and L35 against original L23 and L29.
- **Disposition:** Standing (the port itself); no untranslated reader-visible text remains outside the quotations.

### 7. Links

- **What:** Two prose links, both inside the first footnote (candidate L19): the KO site theme's page (`https://scpko.wikidot.com/component:theme`), kept as the serving original because the sentence is about what the original loaded, and no second link — the Sigma-10 side is named as text. The candidate's one standing outbound link is the credit block's source link (candidate L16), naming `https://scpko.wikidot.com/theme:halloween-koreana` — the original's recorded host (review/sources.tsv), so it names the serving original and no host defect arises (probed for the jiha package's record: the scpko host serves its originals; the alternate scp-wiki-ko form 404s, and this candidate does not use it).
- **Why:** P11: prose links take the JP counterpart or the serving original under the dead-reference evidence standard; a link whose subject is the original's own mechanism stays on the original.
- **Verify:** Compare candidate L16's host against the sources.tsv row's original_url host (scpko.wikidot.com) — identical.
- **Disposition:** Standing.

### 8. Structure

- **What:** The localize.md closing rule holds. The topology pass finds the same two components on both sides in the same order (code-css exhibit, then module-css), no relocations; selectors, rule order, and declarations inside the exhibit are preserved apart from the sections 3–4 changes, and the JP additions (frame, credit block, usage prose) sit ahead of the exhibit rather than interleaved into it. The exhibit shrinks from 41 to 27 lines by exactly two removals, both disclosed in the candidate's own footnotes: the site-theme import (section 3) and the two `@font-face` blocks (section 4). An exhibit census confirms nothing else was dropped: both background rules, both header rules, and the footnoteblock/gate tail are present on both sides.
- **Why:** R3 exists to force this adjudication, because a restructure and a deletion share a diff shape; here the census and the in-file disclosures, not the labels, decide.
- **Verify:** Compare `grep -n '\[\[code\|\[\[module\|footnoteblock' original.txt candidate.txt` — the sequences correspond.
- **Disposition:** Standing; no structural deletion, no class I item.

### 9. Formatting only

- **What:** None: the classifier finds no whitespace-only block and no re-indentation (0 and 0) among the 8 blocks, so the R7 follow-up-diff hazard is not triggered.
- **Why:** Formatting churn is disclosed as its own class so it is never mistaken for a semantic change.
- **Verify:** Section 9 of the classifier skeleton for this package (WS-ONLY 0, re-indentation 0).
- **Disposition:** None required.

### 10. Porter annotations

- **What:** Two annotations, both footnotes inside the usage prose (candidate L19), and no others: (1) the base-substitution footnote, stating that the original loaded the KO wiki's site theme and the JP version instead overrides on top of Sigma-10 (section 3); (2) the font-substitution footnote, naming the two noonnu faces the original used and the ground for replacing them with New Tegomin and Yuji Syuku (section 4). The candidate has no `[!-- --]` notes and adds no CSS comments (its two comments are translations of the original's, section 6). The skeleton's "none" for this section does not survive contact with the bytes and is corrected here.
- **Why:** R2: porter-added text is part of the change record, and these two footnotes are load-bearing — they are the only in-file explanation of the theme's two substitution decisions.
- **Verify:** Read the two `[[footnote]]` spans at candidate L19.
- **Disposition:** Standing.

### 11. Dispositions and exceptions

- **What:** Three items, each with its ground. (1) T1's three pseudo-ref errors: class (iii), draft-form — they are the candidate's own draft-host lines (the frame `theme=` URL, the tail module import, and the asset URLs of sections 3–4); the posting procedure rewrites them to the production host, and fix lanes never "fix" them in the candidate. (2) The render row's items (RENDER-ROWS-2, RENDER-S2-H (KO4)): the page's runtime-hotlink site-theme chain (KB-40, environment layer), the sample's credit-modal errors (KB-32: the preview form has no modal mechanism, ruling 5), and the sample's 884px@768 overflow reading — all sample or environment layer, recorded as not charged to the candidate. (3) The usage-snippet flag (per-theme record) is not in this list: no ledger line dispositions it, which is why it is flagged rather than dispositioned.
- **Why:** A disposition is a decision with grounds (AGENTS.md §3 classes (i)/(ii)/(iii); the named KB entries), not an omission; environment-layer lines are recorded as not-charged.
- **Verify:** Each item names its deciding record above and in the per-theme record.
- **Disposition:** DISPOSITIONED (items 1–2); item 3 flagged with evidence.

### 12. Verification

- **What:** (a) T1 source check (T1-ROWS row 286): exit 1, 3 errors / 1 warn / 0 infos; all three errors are pseudo-ref, class (iii); there is no class (i) error. (b) T2/T3 render (RENDER-ROWS-2, lane RENDER-S2-H (KO4)): FINDINGS, the three items of section 11(2), all dispositioned; engine coverage as run by the lane, not separately caveated in its row. (c) T4/T5 (LOCALIZE-ROWS row 266): FINDINGS jointly, display-affecting findings 1 — the row's single charge is 型 6, the absent interwiki-style frame, since FIXED by FIX4-IWA; the row's own text records everything else about this port as exemplary (footnote disclosure, font-substitution reasoning, exception handling). The ledger §(c3) line records the theme's T4 outcome as P6 FIXED (frame waves, checker-verified). (d) This package is self-verifying: `python3 review/build_review.py --check` regenerates diff.md and the verdict stamp from the two byte-faithful copies in this directory and compares. Counts in this README are the generator's (difflib, autojunk off): +30/−24 in 8 change blocks.
- **Why:** Verification claims name the cheapest deciding check and its result, not a general assurance.
- **Verify:** Re-run the checker on `pages/theme:halloween-koreana-jp.txt` and `python3 review/build_review.py --check` in this repo.
- **Disposition:** PASS (GOSIGN2-LEDGER (b) row 267; go-sign, COMPLETION-REPORT §10).

## Per-theme record — the usage snippet names a different page (defect flag)

The usage snippet is the one line a reader copies to adopt the theme, and on the bytes it names the wrong page. Candidate L20 reads `> @@[[include :scp-jp:theme:halloween-koreana]]@@`. This candidate is theme:halloween-koreana-jp: its canonical file is `pages/theme:halloween-koreana-jp.txt`, its frame `theme=` URL and its module import both name `theme%3Ahalloween-koreana-jp`, and the batch's other candidates with usage snippets name their own `-jp` pages in theirs. Unlike dear-dictator's instance of this same flag, the snippet here is not even inherited: the original file contains no prose and no snippet, so the port wrote this line itself and used the original's name with the JP prefix. Probes run for this package (2026-11-17): `https://scp-jp.wikidot.com/theme:halloween-koreana` returns 404 and `https://scp-jp.wikidot.com/theme:halloween-koreana-jp` returns 404 — neither page is posted yet, so the probe cannot settle intent; what the bytes settle is that the snippet is inconsistent with the candidate's own identity, and if the candidate posts under its canonical name the snippet will point at a page that does not exist. No ledger line dispositions the snippet's name (the T1 pseudo-ref class (iii) covers references to the not-yet-posted page itself, which this is not, on the bytes). The candidate is left exactly as it stands, per the standing rule for fix lanes; the repair, if the coordinator confirms it, is the one-line repoint of candidate L20 to the candidate's own page name, after which this package's diff.md and stamp need no change beyond regeneration (the candidate file's hash in the stamp would change).

## Change set outside the two diffed files

The diff covers two files; the port's record is one file larger. `pages/theme-decoration-sample-halloween-koreana-jp.txt` is the decoration sample the render checks ran against (its findings are the sample half of section 11(2)); it belongs to this theme's record but carries no port change of its own to explain here. There are no companion fragments, no shared base file, and no inbound-link repairs in other candidates for this theme.
