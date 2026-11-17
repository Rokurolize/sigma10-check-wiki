# Review package — theme:scp-human-resources-sigma-jp (EN → JP port)

<!-- BEGIN GENERATED VERDICT STAMP — do not hand-edit; regenerate with review/build_review.py -->
## Verdict stamp
- Theme: theme:scp-human-resources-sigma-jp — origin EN, population #133 [GOSIGN2-LEDGER (b) row 133]
- Overall: STALE — candidate file changed since the verdict was computed (verdict against 435a6bb-era content, file sha256 now ff5d7ad4a0af17da922476013e04956bc8e4125bc1bd31e31d579198febac2bd); verdict not carried over, re-judgement required
> verdicts below describe the pre-change file
- T1 (source check): FINDINGS (classified) — baseline 2026-11-16: exit 1, 1 error / 0 warns / 2 infos (pseudo-ref×1); standing classes dispositioned in register c1 [T1-ROWS row 128; GOSIGN2-LEDGER (b) row 133]
- T2/T3 (render, combined verdict): FINDINGS — [combined T2/T3] report `FINDINGS` — page runtime-hotlink site-theme chain only; sample credit-modal (preview-form) + page-overflow 330–335px@320 + 884px@768. [RENDER-ROWS-2 (RENDER-S2-C (EN18))]
- Engine coverage: full matrix as run by the lane; coverage not separately caveated in the row [RENDER-ROWS-2 row]
- Credit modal: sample credit-modal errors dispositioned preview-form (credit:start-preview has no modal mechanism; GOSIGN-TESTS T2 amendment, 2026-11-16) [RENDER-ROWS-2 (RENDER-S2-C (EN18))]
- T4 (localize patterns + follow-up): FINDINGS — display-affecting findings: 1 [LOCALIZE-ROWS row 133, source LOCALIZE-S2-C]
- T5 (translation text): FINDINGS — the source reports judge T4/T5 jointly; one verdict word covers both [LOCALIZE-ROWS row 133]
- FIX5 re-judgement: none — no OPEN items at the ledger determination [GOSIGN2-LEDGER (b) row 133]
- Computed against: canonical commit b5cb7241f527a44933e45599b41df210690771c4; candidate file pages/theme:scp-human-resources-sigma-jp.txt sha256:ff5d7ad4a0af17da922476013e04956bc8e4125bc1bd31e31d579198febac2bd; record: GOSIGN2-LEDGER.md + GOSIGN2-LEDGER-SUPPLEMENT.md as of the FIX5 head 435a6bb
<!-- END GENERATED VERDICT STAMP -->

## Status

| | |
|---|---|
| Verdict | **PASS** — passed at the ledger determination; this theme had no OPEN items and no §(e) register entry (GOSIGN2-LEDGER (b) row 133) |
| Standing items | **One FIXED, one DISPOSITIONED class** — the credit fields were completed by a fix wave (P3 FIXED, section 1); the unprefixed-include items stand under the posting-procedure disposition (P1, sections 2–3); the T1 pseudo-ref is draft form (class (iii)); the render row's items are the cross-cutting families of section 11. One item is flagged in the per-theme record: the usage exhibit's plain-slug self-reference |
| Go-sign basis | COMPLETION-REPORT.md §10 (go-sign issued; 81 FIXED / 26 DISPOSITIONED / 0 OPEN across the sweep) |
| Named exception | None for this theme (the sweep's single named exception is theme:amethyst-v2, which has no candidate) |

## Provenance

| | Original | Candidate |
|---|---|---|
| Page | theme:scp-human-resources-sigma | theme:scp-human-resources-sigma-jp |
| Wiki | scp-wiki.wikidot.com | SCP-JP Sigma-10 candidate (canonical repo) |
| Reference revision | 13 (first translation; the candidate's credit block records 初訳時参照リビジョン: 13) | — |
| Source of this copy | Campaign cache `gosign2-lanes/lane-oc-gs-render-s2-3/mirrors/scp-human-resources-sigma.txt`, via the mirror store (class COPY, hash-verified against review/sources.tsv) | Canonical file `pages/theme:scp-human-resources-sigma-jp.txt`, copied at worktree HEAD 5506feb |
| Lines / bytes | 786 lines / 16,288 bytes | 794 lines / 18,333 bytes |
| SHA-256 | f0d0a8f627a05f780a9cca5945944c5d97d17120a68a8d810c3f91d79e93980e | 558b67c7e99f5cddc595abe0c9e7c6c85fb52f5dfb1aa10df1c1295f8acb0d47 |

Wave history: the candidate was created by the Stage 2 EN18 integration (commit 3c1bcdf, the RENDER-S2-3 wave's port) and has exactly one later commit, 666f543 (FIX2-CREDIT), which completed the credit block of section 1. No FIX5 commit touches this file, because the theme had no OPEN items for FIX5 to re-judge. Note the mirror used here is the sigma variant's (theme:scp-human-resources-sigma, revision 13); the separate non-sigma theme:scp-human-resources has its own mirror row in the store and is not this package's original.

## Summary

A Sigma-9 skin of the SCP Human Resources BHL theme (itself an extension of SCP Offices). The port completes the credit block the localize check found at two of eight fields (ledger P3 FIXED), re-hosts the theme's logo — which the original loads from two different pages' file areas — to a single uploaded file on the JP storage wiki, migrates the font loads from bunny.net to Google Fonts and adds the JP faces (Noto Serif JP in the stacks, Noto Sans JP loaded alongside), and translates the prose, exhibits, and CSS comments. Two forms are carried that a reader should see named: the interwiki frame include is unprefixed (the localize check's pattern-1/6 family, dispositioned under P1), and the usage exhibit names the plain slug, flagged in the per-theme record.

## Class summary

Auto-classification by review/classify_hunks.py (signature table 2026-11-17.1): 98 change blocks — 52 specific (53.1%), 42 heuristic (42.9%), 4 residue (4.1%), 0 skipped. Pattern citations below name the KB entry; the patterns/ tree state cited throughout is commit 9c5e9079afb01d30cb9fc4ef9d714e5591eb2ffa.

| Label | Blocks |
|---|---|
| TRANS-UNANCHORED | 44 |
| JPFONT-STACK | 23 |
| COMMENT-TEXT | 23 |
| TRANSLATION-ANCHORED | 17 |
| ASSET-REHOST | 3 |
| WS-ONLY | 3 |
| DELIVERY-HOST | 2 |
| DRAFT-HOST | 2 |
| EXHIBIT-RESTRUCTURE | 2 |
| INCLUDE-REPOINT | 2 |
| SELF-DELIVERY | 2 |
| CREDIT-PREVIEW | 1 |
| CREDIT-PROSE | 1 |
| ESCAPED-INCLUDE | 1 |
| FONT-IMPORT | 1 |
| IFTAGS | 1 |
| JPFONT-LOAD | 1 |
| TASL-FIELDS | 1 |

Adjudication for this README (every block was read against the bytes): the two EXHIBIT-RESTRUCTURE blocks are a frame repoint (B2) and the image-block exhibit's re-host (B12) — no restructuring in substance. The four residue blocks are a translated credit-prose line and three heading/comment translations (appendix). The three WS-ONLY blocks are §9's whole content. After adjudication no block is left unexplained.

## Standing sections

### 0. Header and provenance frame

- **What:** Theme theme:scp-human-resources-sigma-jp; original theme:scp-human-resources-sigma on scp-wiki at reference revision 13; candidate `pages/theme:scp-human-resources-sigma-jp.txt`. Provenance route: derived from the original at the reference revision by the RENDER-S2-3 wave (sources.tsv kind: standard). Both files open with the delivery module and frame ahead of the tag gate, and the gate localizes as usual (block B4: `[[iftags +theme]]` → `[[iftags +テーマ]]`, candidate L10).
- **Why:** Section 0 declares the provenance route so every later count is read against the right baseline; the gate's tag is P2 (iftags tag localization).
- **Verify:** The sources.tsv row for scp-human-resources-sigma-jp; `sha256sum original.txt` against the Provenance table.
- **Disposition:** Standing (the route itself); the gate change is P2, applied.

### 1. Credit and attribution

- **What:** The original's only credit furniture is a bare rating exhibit: a right-aligned `[[module rate]]` under a "Rating:" heading (original L11–14). The candidate deletes it and installs the preview credit block (candidate L12–21, block B5): the eight ruling-3 fields （タイトル SCP Human Resources Sigma-9 Theme; 翻訳責任者 AI; 翻訳年 2026; 原題 SCP Human Resources Sigma-9 Theme; 著作権者 [[*user macro_au_micro]]; 作成年 2023; 初訳時参照リビジョン 13; the source link, host-verified in section 7). At localize time the block stood at two of eight fields (the LOCALIZE row's pattern-3 charge: six of eight missing — タイトル/翻訳責任者/翻訳年/原題/著作権者/作成年 — the panel rendering but incomplete); the FIX2-CREDIT wave (commit 666f543) completed it, and the ledger records the outcome as P3 FIXED. The author field names macro_au_micro with the user link, the theme's author. The base-work credits stand in the intro sentence, carried translated (candidate L25): the theme is based on the Human Resources theme, itself an extension of the SCP Offices theme — both bases credited, neither dropped. There is no license box on the original and no T7 credit CSS on either side (zero credit-rule lines in both files).
- **Why:** P3/T1: the preview credit module is the rate-bearing JP form, replacing the bare exhibit rather than accumulating beside it (the class C / KB-10 shape), and ruling 3 fixes the eight fields the incomplete panel was missing.
- **Verify:** `grep -n 'module rate' candidate.txt` returns nothing; read candidate L12–21 against the eight fields; `git log --oneline -- pages/theme:scp-human-resources-sigma-jp.txt` shows the FIX2-CREDIT commit.
- **Disposition:** FIXED (P3, credit waves; GOSIGN2-LEDGER §(c3)).

### 2. Includes and components

- **What:** Three include events besides the credit pair. The head frame keeps an unprefixed form (candidate L5: `[[include component:interwiki-style`, its theme target repointed in section 3) — the original's frame is `:scp-wiki:`-prefixed (original L5), so the port drops the prefix rather than repointing it; an unprefixed include resolves on the site that renders it, which on scp-jp is the JP component. This is the localize check's pattern-1/6 family (unprefixed same-site includes), dispositioned under P1 (section 11). The usage exhibit (block B8) repoints the include to `:scp-jp:` with the plain slug — flagged in the per-theme record. The examples exhibit keeps its unprefixed `[[include component:image-block ...]]` (candidate L41, block B12) with the caption translated; the component resolves on scp-jp, and the image it displays is section 4's re-host.
- **Why:** P1 (KB-15): an include must name the JP counterpart that actually exists on scp-jp; the unprefixed form names the same component by the site's own resolution, and the ledger's P1 line dispositions the form for this theme rather than charging it. Ruling 4 is not engaged: the base themes are credited by link (section 7); their stylesheets are not components this theme includes.
- **Verify:** `grep -n '\[\[include' candidate.txt` — frame (L5), credit pair (L12, L21), image-block (L41), and the escaped exhibit (L30).
- **Disposition:** DISPOSITIONED for the unprefixed form (P1, posting-procedure convention class); the exhibit's name form is the flagged item of the per-theme record.

### 3. Delivery and code loading

- **What:** The topology is preserved (the classifier's pass: a head module plus the code exhibit on each side, no moves). The original's delivery is external-form: its module imports its own /1 from the wiki domain itself, `https://scp-wiki.wikidot.com/local--code/theme%3Ascp-human-resources-sigma/1` (original L2; the topology pass records `external_own_delivery: true`), framed at priority 1. The candidate normalizes the same self-delivery to the standard form: `https://sigma10-jp-test.wdfiles.com/local--code/theme%3Ascp-human-resources-sigma-jp/1` (candidate L2, block B1), with the frame at priority 1 naming the same delivery (candidate L5–8, block B3). The CSS is the code exhibit on both sides (665 → 666 lines; the added line is inside the font-load block, section 4).
- **Why:** P4/T9 and P6/T3: a theme's live channel in the JP environment is its own local--code delivery framed by interwiki-style; the candidate's form is the population's, and the draft host is KB-41, class (iii).
- **Verify:** `sed -n '1,8p' candidate.txt` against original L1–8 — one import, one frame, same order.
- **Disposition:** DISPOSITIONED (draft-host form, class (iii)).

### 4. Fonts and assets

- **What:** Fonts (P7): the load migrates hosts and gains the JP faces (block B46: original L130–131 → candidate L137–139). The original loads Basic and IBM Plex Mono from bunny.net in the retired `css?family=` grammar plus Zilla Slab from a bunny css2 URL; the candidate loads IBM Plex Mono and Zilla Slab from Google Fonts css2 and adds a combined `Noto Sans JP + Noto Serif JP` load. The 23 JPFONT-STACK blocks insert the JP serif into the stacks behind the Latin faces (`'Zilla Slab', 'Noto Serif JP', serif` at candidate L199, L212, and throughout) — Noto Serif JP because the theme's display face is a slab serif and the JP serif is its register match. One face from the original's import does not survive: `Basic` is named in the original's bunny import line but in no font stack on either side (checked: the string occurs only in that import), so its absence from the candidate's imports drops nothing that renders. The two font exhibit spans (candidate L120–121) name the Latin faces alone, as the original's do — they document which Latin face does what; the stacks they sit beside carry the JP fallback. Assets (ASSET-REHOST ×3, all applied): the theme's logo is loaded by the original from two different pages' file areas — its own (original L184) and the base Human Resources theme's (original L228) — plus the exhibit's image-block (original L34). The candidate points all three at one uploaded file on the JP storage wiki: `https://scp-jp-storage.wdfiles.com/local--files/file%3A7657035-44-ziy1/hrlogo.png` (candidate L41, L192, L236).
- **Why:** P7 (KB-16): Japanese text must not fall back to a platform default for want of a named JP family; here the family is named in the stacks and loaded. P5: images a theme loads must not depend on the original wiki's file area; the storage-wiki upload is the population's applied form for a file that has no candidate-page file area yet, and unifying the logo's three references on one file removes the original's two-area split.
- **Verify:** `grep -n '@import' candidate.txt` — three Google Fonts lines at L137–139 plus the delivery import at L2; `grep -n 'scp-jp-storage' candidate.txt` — the three logo loci named above; `grep -n 'Basic' candidate.txt` returns nothing.
- **Disposition:** Applied (fonts and re-hosting); no ledger item stands against either.

### 5. Header, sidebar, and site furniture

- **What:** No header variables exist on either side (no `--header-title` / `--header-subtitle` / `--logo-image`), and no P8 adaptation was needed. The one rendered string in this family is a CSS content string in the header zone, `content: "HUMAN RESOURCES DEPARTMENT"` → `content: "人事部門"` (candidate L213). Sidebar behaviour is a render-record item only through the cross-cutting families (section 11).
- **Why:** P8 (KB-19) covers the rendered string: it is reader-visible furniture and is localized.
- **Verify:** `grep -n 'content: "' candidate.txt` — the single string at L213.
- **Disposition:** Applied.

### 6. Text translation

- **What:** The prose is translated throughout: the usage section including the @import warning and the backlinks instructions, the examples' explanatory text, and the headings. The CSS comments are translated as a class (23 COMMENT-TEXT blocks). The counted groups are 44 TRANS-UNANCHORED blocks and 17 TRANSLATION-ANCHORED blocks; the anchored blocks were verified line by line, and the unanchored mass is single-line prose and comment translation of the same shapes, with no content class dropped (the census in section 8). One residue block (B6) is the intro's base-credit sentence, translated; it is resolved in the appendix.
- **Why:** P10 (body and usage translation is the port's purpose) and KB-18 (reader-visible strings); CSS comments are porter-visible only (R1's comment half), counted as a class.
- **Verify:** The pairs are diff.md's body and code sections in order.
- **Disposition:** Standing (the port itself).

### 7. Links

- **What:** The credit block's source link (candidate L20) names `https://scp-wiki.wikidot.com/theme:scp-human-resources-sigma` — the original's recorded host (review/sources.tsv `original_url`), so the host check passes and no probe was triggered; its label is ソース. The intro's two base-work links (candidate L25) keep the unprefixed same-site form the original uses (`[[[theme:scp-human-resources|…]]]`, `[[[theme:scp-offices-theme|…]]]`, original L18), their labels translated （人事部門テーマ, SCPオフィステーマ) — provenance references to the base works, in the form the original carries them; the pattern-1/6 disposition of section 2 covers the unprefixed family for this theme.
- **Why:** P11: prose links take the JP counterpart where one exists; where the original-side page is itself the credited base work, the reference stands as the original makes it, under the recorded disposition.
- **Verify:** `grep -n 'theme:scp-human-resources\|theme:scp-offices' candidate.txt` — the source link (L20) and the two intro links (L25).
- **Disposition:** DISPOSITIONED (the unprefixed family, P1; GOSIGN2-LEDGER §(c3)).

### 8. Structure

- **What:** The exhibit census corresponds: usage section, examples (image-block, headings, font spans), and the code exhibit are present on both sides in the same order. The named conversion is the rating exhibit's replacement by the credit block (section 1). Selector and variable names inside the CSS are preserved.
- **Why:** R3: the census is what separates a conversion (this theme) from a silent restructure or drop (the failure class I charges); here every original region has a named candidate counterpart.
- **Verify:** Compare the heading and include sequences of the two files — they correspond at the loci named in sections 1–4.
- **Disposition:** Standing.

### 9. Formatting only

- **What:** Three whitespace-only blocks (B87, B89, B90), all in the code exhibit's yui-navset zone: trailing spaces after selector commas are removed (e.g. original L524 `.yui-navset .yui-nav a, ` → candidate L532, the same line without the trailing space). No re-indentation occurs (0 reindent blocks).
- **Why:** Formatting churn is disclosed as its own class so it is never mistaken for a semantic change; inside a code exhibit it is also display-inert, since the exhibit's text is documentation.
- **Verify:** The classifier summary in classification.json (WS-ONLY ×3); the sample pair above.
- **Disposition:** Standing.

### 10. Porter annotations

- **What:** None. An explicit check of the candidate finds no `[!-- ... --]` porter comment and no editor line with no original counterpart; the classifier's ANNOTATION signature does not fire.
- **Why:** R2: porter-added text is part of the change record; here there is none to record.
- **Verify:** `grep -n '\[!--' candidate.txt` returns nothing.
- **Disposition:** Standing.

### 11. Dispositions and exceptions

- **What:** Three items, each with its ground. (1) T1's one pseudo-ref error: class (iii), the draft-host delivery of section 3. There are no hotlink errors — the logo is re-hosted (section 4) and the base delivery is the candidate's own. (2) The unprefixed-include family (the frame of section 2 and the intro links of section 7): the ledger's P1 line, DISPOSITIONED as the posting-procedure convention class. (3) The render row's items, all cross-cutting: the sample's credit-modal errors (KB-32, ruling 5), the page-overflow pair 330–335px@320 (KB-33/KB-34 families), the 884px@768 overflow, and the runtime-hotlink site-theme chain (KB-40, environment layer). T4's charges close as: pattern 3 FIXED (section 1), patterns 1/6 DISPOSITIONED (item (2)).
- **Why:** A disposition is a decision with grounds (AGENTS.md §3 classes (i)/(ii)/(iii); the named KB entries), not an omission; environment-layer lines are recorded as not-charged.
- **Verify:** Each item names its deciding record above and in the per-theme record.
- **Disposition:** DISPOSITIONED (items (1)–(3)); FIXED (the credit charge).

### 12. Verification

- **What:** (a) T1 source check (T1-ROWS row 128): exit 1, 1 error / 0 warns / 2 infos — the batch's cleanest T1 row; the single error is the pseudo-ref of section 11(1), and there is no class (i) error. (b) T2/T3 render (RENDER-ROWS-2, lane RENDER-S2-3 (EN18)): FINDINGS, the items of section 11(3), all dispositioned. (c) T4/T5 (LOCALIZE-ROWS row 133): FINDINGS jointly, display-affecting findings 1 (the pattern-3 credit charge, since fixed); the ledger §(c3) line records the theme's T4 outcome as P1 DISPOSITIONED and P3 FIXED. (d) This package is self-verifying: `python3 review/build_review.py --check` regenerates diff.md and the verdict stamp from the two byte-faithful copies in this directory and compares. Counts in this README are the generator's (difflib, autojunk off): +159/−156 in 98 classifier change blocks / 20 diff hunks.
- **Why:** Verification claims name the cheapest deciding check and its result, not a general assurance.
- **Verify:** Re-run the checker on `pages/theme:scp-human-resources-sigma-jp.txt` and `python3 review/build_review.py --check` in this repo.
- **Disposition:** PASS (GOSIGN2-LEDGER (b) row 133; go-sign, COMPLETION-REPORT §10).

## Per-theme record

### The usage exhibit's self-reference (flagged)

The usage exhibit reads `@@[[include :scp-jp:theme:scp-human-resources-sigma]]@@` (candidate L30) — the include a user is told to paste names the theme's plain slug on scp-jp, where the candidate's posting name is theme:scp-human-resources-sigma-jp. The original's exhibit names `:scp-wiki:theme:scp-human-resources-sigma` (original L23), that page's real name on its own wiki, so the port's repoint changed the site prefix and kept a name that, on the target wiki, will not be the posted page's name. Probes made for this package (2026-11-17): both `https://scp-jp.wikidot.com/theme:scp-human-resources-sigma` and `https://scp-jp.wikidot.com/theme:scp-human-resources-sigma-jp` return 404 today, because the theme is not yet posted in either name; the probe therefore cannot decide the point, and the flag rests on the posting-name convention, the same ground on which the M-pure-3 batch flagged five instances of this shape and a population sweep is repairing the family. This package does not edit the candidate; the flag is recorded so the sweep's list is complete.

### Record note — the vendored LOCALIZE row truncates the pattern-1/6 charge

The vendored LOCALIZE-ROWS copy of this theme's row ends its pattern-1/6 item at "unprefixed same-site `component:interwiki-style` …", so the charge's full text is not recoverable from the record. The bytes govern: the candidate's unprefixed references are the frame include (candidate L5), the image-block include (L41), and the two intro links (L25), and the ledger's §(c3) line dispositions P1 without qualification.

## Appendix — residue blocks

Four blocks, resolved here by shape:

| Block | Span | Resolution |
|---|---|---|
| B6 | orig 18-18 → cand 23-23 | The intro's base-credit sentence, translated. Narrated in sections 1 and 7. |
| B11 | orig 32-32 → cand 39-39 | Heading translation: `+ Examples` → `+ 使用例`. |
| B66 | orig 374-374 → cand 382-382 | CSS section comment: `/* BODY */` → `/* 本文 */`. |
| B85 | orig 507-507 → cand 515-515 | CSS section comment: `/* TABLES */` → `/* 表 */`. |

## Change set outside the two diffed files

The diff covers two files; the port's record is one file larger. `pages/theme-decoration-sample-scp-human-resources-sigma-jp.txt` is the decoration sample the render checks ran against (its findings are the sample half of section 11(3)); it belongs to this theme's record but carries no port change of its own to explain here. There are no companion fragments, no shared base file, and no inbound-link repairs in other candidates for this theme. The logo file the candidate references lives on the JP storage wiki (section 4), outside this repo.
