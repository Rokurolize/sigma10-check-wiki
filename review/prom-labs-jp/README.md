# Review package — theme:prom-labs-jp (EN → JP port)

<!-- BEGIN GENERATED VERDICT STAMP — do not hand-edit; regenerate with review/build_review.py -->
## Verdict stamp
- Theme: theme:prom-labs-jp — origin EN, population #124 [GOSIGN2-LEDGER (b) row 124]
- Overall: STALE — candidate file changed since the verdict was computed (verdict against 435a6bb-era content, file sha256 now 6bdfe6e5a680c887a146cc7816c741c05f59947704b8e23df6222b01c68d9f47); verdict not carried over, re-judgement required
> verdicts below describe the pre-change file
- T1 (source check): FINDINGS (classified) — baseline 2026-11-16: exit 1, 3 errors / 1 warn / 1 info (pseudo-ref×3); standing classes dispositioned in register c1 [T1-ROWS row 159; GOSIGN2-LEDGER (b) row 124]
- T2/T3 (render, combined verdict): FINDINGS — [combined T2/T3] report `FINDINGS` — page runtime-hotlink site-theme chain only; sample T2 no machine verdict (exit 2). [RENDER-ROWS-2 (RENDER-S2-C (EN16))]
- Engine coverage: full matrix as run by the lane; coverage not separately caveated in the row (the row records inconclusive runs, carried verbatim above) [RENDER-ROWS-2 row]
- Credit modal: no credit-modal line recorded [RENDER-ROWS-2 (RENDER-S2-C (EN16))]
- T4 (localize patterns + follow-up): FINDINGS — display-affecting findings: 1 [LOCALIZE-ROWS row 124, source LOCALIZE-S2-B]
- T5 (translation text): FINDINGS — the source reports judge T4/T5 jointly; one verdict word covers both [LOCALIZE-ROWS row 124]
- FIX5 re-judgement: none — no OPEN items at the ledger determination [GOSIGN2-LEDGER (b) row 124]
- Computed against: canonical commit b5cb7241f527a44933e45599b41df210690771c4; candidate file pages/theme:prom-labs-jp.txt sha256:6bdfe6e5a680c887a146cc7816c741c05f59947704b8e23df6222b01c68d9f47; record: GOSIGN2-LEDGER.md + GOSIGN2-LEDGER-SUPPLEMENT.md as of the FIX5 head 435a6bb
<!-- END GENERATED VERDICT STAMP -->

## Status

| | |
|---|---|
| Verdict | **PASS** — passed at the ledger determination; this theme had no OPEN items and no §(e) register entry (GOSIGN2-LEDGER (b) row 124) |
| Standing items | **DISPOSITIONED** — T1 pseudo-ref ×3 (class (iii), section 11); the render row's items (KB-40 site-theme chain; the sample's exit-2 coverage caveat, section 11); T4's one item (P7-minor) DISPOSITIONED under the T4 bar. One item is flagged in the per-theme record: the usage exhibit's self-reference names the plain slug |
| Go-sign basis | COMPLETION-REPORT.md §10 (go-sign issued; 81 FIXED / 26 DISPOSITIONED / 0 OPEN across the sweep) |
| Named exception | None for this theme (the sweep's single named exception is theme:amethyst-v2, which has no candidate) |

## Provenance

| | Original | Candidate |
|---|---|---|
| Page | theme:prom-labs | theme:prom-labs-jp |
| Wiki | scp-wiki.wikidot.com | SCP-JP Sigma-10 candidate (canonical repo) |
| Reference revision | 44 (first translation; the candidate's credit block records 初訳時参照リビジョン: 44) | — |
| Source of this copy | Campaign cache `gosign2-lanes/lane-oc-gs-localize-s2-B/orig-prom-labs.txt`, via the mirror store (class COPY, hash-verified against review/sources.tsv) | Canonical file `pages/theme:prom-labs-jp.txt`, copied at worktree HEAD 5506feb |
| Lines / bytes | 306 lines / 5,824 bytes | 317 lines / 6,705 bytes |
| SHA-256 | 51f3ebbf2ae9bd05afe1496ade332641160850dcd996a0c53bbbc3f4538a950c | c11153278e52450526afe96f916d5f8e76276e1d8fe43dbdaabd2948f57b66fe |

Wave history: the candidate was created by the Stage 2 EN16 integration (commit 6d5fc81, the LOCALIZE-S2-B wave's port) and has exactly one later commit, 1869877 (FIX-CREDIT-D), whose prom-labs hunk is the one-line translator-field normalization （翻訳責任者: SCP-JP → AI, section 1). No FIX5 commit touches this file, because the theme had no OPEN items for FIX5 to re-judge.

## Summary

A standard port whose diff is dominated by two mechanical masses: the translation of the body and CSS comments, and a 23-block whitespace normalization inside the code block (the original's blank lines carry a trailing space; the candidate's do not). The structural content is the usual set, applied once each: the bare Rate becomes the preview credit block (with a font-credit line beyond the eight fields), the delivery frame moves to the very head and gains the interwiki tint as a `css=` parameter, the bunny.net font loads become Google Fonts loads, the two stacks gain Noto Sans JP, and the two background assets move to the draft host. T4's single item is the P7-minor: Noto Sans JP is credited in the credit block and named in both stacks, but this file never loads it — dispositioned under the T4 bar, with the argument restated in the per-theme record. One flag is recorded there too: the usage exhibit's include names `:scp-jp:theme:prom-labs`, the plain slug, where the candidate's posting name is theme:prom-labs-jp.

## Class summary

Auto-classification by review/classify_hunks.py (signature table 2026-11-17.1): 43 change blocks — 35 specific (81.4%), 8 heuristic (18.6%), 0 residue, 0 skipped. Pattern citations below name the KB entry; the patterns/ tree state cited throughout is commit 9c5e9079afb01d30cb9fc4ef9d714e5591eb2ffa.

| Label | Blocks |
|---|---|
| WS-ONLY | 23 |
| TRANS-UNANCHORED | 9 |
| COMMENT-TEXT | 6 |
| DRAFT-HOST | 4 |
| SELF-DELIVERY | 3 |
| TRANSLATION-ANCHORED | 2 |
| CONTENT-STRING | 2 |
| IFTAGS | 2 |
| JPFONT-STACK | 2 |
| BARE-RATE-DEL | 1 |
| CREDIT-PREVIEW | 1 |
| CREDIT-PROSE | 1 |
| DELIVERY-HOST | 1 |
| ESCAPED-INCLUDE | 1 |
| EXHIBIT-RESTRUCTURE | 1 |
| FONT-IMPORT | 1 |
| INCLUDE-REPOINT | 1 |
| TASL-FIELDS | 1 |
| CSS-BODY | 1 |

Adjudication for this README (every block was read against the bytes): the 23 WS-ONLY blocks are one shape (section 9); the 8 heuristic blocks resolve as the intro prose translation (B5, section 6), the banner-comment translation (B7, section 6), three CSS comment translations (B26–B28, section 6), the interwiki selector extension (B31, section 3), and two comment-plus-whitespace pairs (B39, B43, sections 6 and 9). The one EXHIBIT-RESTRUCTURE primary (B3) is an alignment artefact of the head reordering, not an exhibit change (section 8). After adjudication no block is left unexplained.

## Standing sections

### 0. Header and provenance frame

- **What:** Theme theme:prom-labs-jp; original theme:prom-labs on scp-wiki at reference revision 44; candidate `pages/theme:prom-labs-jp.txt`. Provenance route: derived from the original at the reference revision by the LOCALIZE-S2-B wave (sources.tsv kind: standard; no production JP counterpart exists for this theme, so the R4 adoption question does not arise). The head is reordered: the original runs delivery module (L1–3), frame (L5–8), tag gate (L10), Rate (L11–13); the candidate runs frame (L1–5), delivery module (L7–9), tag gate (L11), credit block (L13–23).
- **Why:** Section 0 declares the provenance route so every later count is read against the right baseline; the gate's tag is P2, the frame is P6/T3 (section 3).
- **Verify:** The sources.tsv row for prom-labs-jp; `sha256sum original.txt` against the Provenance table.
- **Disposition:** Standing (the route itself); the gate and frame changes are recorded in section 3.

### 1. Credit and attribution

- **What:** The original's credit furniture is a centered bare `[[module Rate]]` (original L11–13). The candidate deletes it (block B4) and installs the JP form: a `:scp-jp:credit:start-preview`/`end-preview` block (candidate L13–23) carrying the eight ruling-3 fields （タイトル プロメテウス研究所テーマ; 翻訳責任者 AI; 翻訳年 2026; 原題 Prometheus Labs Theme; 著作権者 [[*user MrPines]]; 作成年 2018; 初訳時参照リビジョン 44; the source link, host-verified in section 7) plus a ninth line, the font credit: `**フォント:** Homenaje・Lato・Noto Sans JP（ともに Google Fonts、SIL Open Font License）`. The translator field took its ruling-3 form in 1869877 (FIX-CREDIT-D: SCP-JP → AI). The named author matches the original's banner comment ("Theme created by MrPines", original L21). The banner's second attribution — the base work, "the Sigma 9 theme created by Aelanna and Dr Devan", with the logo's CC0 licence and source URL — is not dropped: it survives in the same place the original puts it, the code block's banner comment, translated (candidate L30–33). T7 credit CSS: none on either side (no credit-module selectors occur in either file).
- **Why:** P3/T1: the preview credit module is the rate-bearing JP form, so the bare Rate is deleted rather than duplicated (KB-09). Ruling 3 fixes the eight fields and the translator credit form. The font line is P7's credit half (the added font's credit written into the credit block); its content is argued in the per-theme record, because one of the three fonts it names is not loaded by this file.
- **Verify:** `grep -n 'module Rate' candidate.txt` returns nothing; read candidate L13–23 against the eight fields plus the font line; read candidate L30–33 against original L20–24.
- **Disposition:** Applied; the font-credit content is DISPOSITIONED with the P7-minor item (section 11, per-theme record).

### 2. Includes and components

- **What:** Two include changes besides the credit pair. The interwiki-style frame: `:scp-wiki:component:interwiki-style` (original L5) → the unprefixed same-site form (candidate L1), its parameters in section 3. The usage exhibit: `:scp-wiki:theme:prom-labs` → `:scp-jp:theme:prom-labs` (block B6, original L17 → candidate L27), an escaped include inside the usage text. No component swap (T8) occurs; the theme includes no components beyond the frame and the credit pair. The exhibit's target name is flagged in the per-theme record.
- **Why:** P1 (KB-15): an include must name the JP counterpart that actually exists on scp-jp; the frame's unprefixed form is the same-site convention, resolving on the wiki the candidate is posted to. Ruling 4 is not engaged: no component had to be ported alongside this theme.
- **Verify:** `grep -n '\[\[include' candidate.txt` — three live includes (L1, L13, L23) plus the escaped exhibit at L27.
- **Disposition:** Applied; the exhibit's name form is the flagged item of the per-theme record.

### 3. Delivery and code loading

- **What:** The original delivers its own CSS by a head `[[module CSS]]` importing `scp-wiki.wdfiles.com/local--code/theme%3Aprom-labs/1` (original L2), with the interwiki-style frame behind it naming the same /1 delivery (original L5–8, priority 1). The candidate moves the frame to the very head (candidate L1–5, block B1) and repoints both delivery lines to the candidate's own draft-host delivery: the frame's `theme=` names `local--code/theme%3Aprom-labs-jp/1` on sigma10-jp-test.wdfiles.com, and the module import follows it (candidate L8, block B2). One parameter is new: the frame gains a `css=` parameter carrying the rule `#interwiki .menu-item img, #interwiki .menu-item > .image {filter:hue-rotate(250deg)}` — the tint value is the original's own (its in-page rule at original L211 applies `hue-rotate(250deg)` to the menu-item image), restated where it can act, since the page's CSS cannot reach inside the interwiki frame. The matching in-page selector is extended in the same spirit (block B31, original L209–210 → candidate L219–221): `.side-block .menu-item > .image` gains `iframe.scpnet-interwiki-frame` as a second selector, declarations unchanged.
- **Why:** P4/T9 (own-code delivery served from JP hosts) and P6/T3 (the interwiki-style frame; only `priority`/`theme`/`css` parameters survive, and the `css=` parameter is the frame's sanctioned channel for styling the interwiki frame itself). The draft-host form of the live lines is KB-41, class (iii).
- **Verify:** `grep -n 'local--code' candidate.txt` — L4 and L8, both draft-host, both the candidate's own /1; read candidate L219–222 against original L209–211.
- **Disposition:** DISPOSITIONED (draft-host lines, class (iii)); the frame tint is an applied supplement, argued above from the original's own value.

### 4. Fonts and assets

- **What:** Load (block B8): the original's two fonts.bunny.net `@import`s (original L26–27 — Homenaje, Lato, bare family parameters) become two Google Fonts css2 `@import`s (candidate L36–37) with `display=swap` and Lato's axis specification spelled out (`ital,wght@0,400;0,700;1,400`). Stacks (blocks B21, B23): the two `font-family` lines gain the JP family — `'Homenaje', 'Noto Sans JP', sans-serif` (candidate L133) and `'Lato', 'Noto Sans JP', sans-serif` (candidate L151). The file loads no Noto Sans JP `@import` of its own; that gap is T4's P7-minor item, dispositioned in section 11 and argued in the per-theme record. Assets (blocks B12, B14): the two background images move from `scp-wiki.wdfiles.com/local--files/theme%3Aprom-labs/` to the draft host's `local--files/theme%3Aprom-labs-jp/` folder, file names unchanged — `pl_bg2.png` (candidate L66) and `logo_temp.png` (candidate L70).
- **Why:** P7/T5 with KB-16 (the font load gap): the Latin faces have no kana glyphs, so the stacks gain the JP family; the load-side half of that rule is the dispositioned item. The bunny.net → Google Fonts change is P5/KB-17 (allowlisted font hosts; the css2 parameter form is the KB-04 shape, a load that resolves). P5 for the assets: the theme's own images re-hosted to the JP side, in draft-host form.
- **Verify:** `grep -n '@import' candidate.txt` — two lines, both fonts.googleapis.com; `grep -n 'Noto Sans JP' candidate.txt` — the credit line (L22) and the two stacks (L133, L151), no load; `grep -n 'local--files' candidate.txt` — the two draft-host asset lines.
- **Disposition:** Loads and stacks applied; the unloaded-but-credited JP font is DISPOSITIONED (P7-minor, section 11); the draft-host asset URLs are DISPOSITIONED (class (iii)).

### 5. Header, sidebar, and site furniture

- **What:** None. No signature for this section fires, and the bytes bear it out: neither file overrides a header variable (no `--header-title`, `--header-subtitle`, or `--logo-image` on either side), and the theme's sidebar rules are carried unmodified apart from the font lines of section 4 and the whitespace of section 9. The interwiki tint that touches site furniture is the frame's, recorded in section 3.
- **Why:** A standing section is present even when empty, so a reviewer can tell "checked, absent" from "not considered".
- **Verify:** `grep -n -- '--header-\|--logo-image' original.txt candidate.txt` returns nothing on either side.
- **Disposition:** None required.

### 6. Text translation

- **What:** The body and the in-CSS text are translated throughout, in the counted groups: the intro prose (B5, original L15 → candidate L25, the GoI sentence with the hub link's text translated); the banner comment (B7, original L20–23 → candidate L30–33 — the attribution comment of section 1, porter-visible only, R1's comment half); three one-line CSS comment translations (B26–B28: the tab-state comments at candidate L170, L175, L177); and the comment halves of B39/B43 ("page stuff" → ページ要素, "mobile" → モバイル）. Two reader-visible CSS strings are TRANSLATION-ANCHORED with CONTENT-STRING labels (B22, B24): the header `content:` "PROMETHEUS LABS" → "プロメテウス研究所" (candidate L139) and the motto `content:` "With study and intuition, the mystical becomes common." → "研究と洞察により、神秘はありふれたものとなる。" (candidate L153). No untranslated reader-visible text remains; the English that survives is proper nouns inside translated sentences (the font and licence names of sections 1 and 4).
- **Why:** P10 (body and usage translation is the port's purpose) and KB-18 (reader-visible strings, including `content:`). CSS comments are porter-visible only (R1); they are stated separately here so their translation is not mistaken for reader-visible coverage, and so the attribution comment's survival is on record.
- **Verify:** The pairs are diff.md's sections in order; a Hangul/CJK scan is not applicable (EN source) — an English-prose scan of candidate.txt returns only the proper nouns named above.
- **Disposition:** Standing (the port itself).

### 7. Links

- **What:** Two link items. The hub link in the intro prose keeps its page name and translates its text: `[[[prometheus-labs-hub|Prometheus Labs]]]` → `[[[prometheus-labs-hub|プロメテウス研究所]]]` (candidate L25) — a same-site link whose target is the GoI hub's JP counterpart under the same name. The credit block's source link (candidate L21) names `https://scp-wiki.wikidot.com/theme:prom-labs` — the original's recorded host (review/sources.tsv `original_url`), so the host check passes and no probe was triggered. The logo source URL inside the banner comment (svgsilh.com, candidate L33) is an attribution citation, not a load, and is carried as the original carries it.
- **Why:** P11: prose links take the JP counterpart or the serving original, under the dead-reference evidence standard; attribution citations follow the credit record, not the link rules.
- **Verify:** `grep -n 'wikidot.com' candidate.txt` — the source link is the only hit.
- **Disposition:** Standing.

### 8. Structure

- **What:** The localize.md closing rule holds with one named event: the head reordering of section 0 (frame before delivery module), which is the wave-standard head form, not an interleaving of the inherited CSS. Variable names, selectors, and channel order inside the code block are preserved (original L19–305 → candidate L29–316). An exhibit census confirms the shape: the usage exhibit and the code exhibit are present on both sides in the same order — nothing was dropped or replaced. The classifier's one EXHIBIT-RESTRUCTURE primary (B3) pairs the original's frame lines with the candidate's gate line and adjudicates to the head reordering; the R3 question does not arise.
- **Why:** R3 exists to force exactly this adjudication, because a restructure and a deletion share a diff shape and ledger class I charges the silent form; here the census, not the label, decides.
- **Verify:** Compare `grep -n '\[\[code\|\[\[include' original.txt candidate.txt` — the sequences correspond.
- **Disposition:** Standing; no structural deletion, no class I item.

### 9. Formatting only

- **What:** 23 WS-ONLY blocks, all one shape: inside the code block, the original's blank lines carry a single trailing space and the candidate's are empty (visible in diff.md as ` ` → `` pairs, e.g. original L46–60 against candidate L56–70). The comment blocks B39/B43 each carry one such line beside their translated comment. There is no re-indentation (0 blocks pair up after leading-whitespace normalization) and no line-order change. The mass is disclosed so the +75/−64 line count is not mistaken for semantic churn: 23 of the 43 blocks are this one whitespace shape.
- **Why:** Formatting churn is disclosed as its own class (R7) so a reviewer can skip it safely and so the follow-up-diff property is on record: a future diff against the original will show these lines once, here, and not again.
- **Verify:** `grep -c ' $' original.txt` against `grep -c ' $' candidate.txt` inside the code block ranges; the WS-ONLY list in classification.json.
- **Disposition:** None required.

### 10. Porter annotations

- **What:** None. An explicit check of the candidate finds no `[!-- ... --]` porter comment and no editor line with no original counterpart; the classifier's ANNOTATION signature does not fire. The banner comment at candidate L30–33 is the original's own comment, translated (section 6), not a porter addition.
- **Why:** R2: porter-added text is part of the change record; here there is none to record.
- **Verify:** `grep -n '\[!--' candidate.txt` returns nothing.
- **Disposition:** Standing.

### 11. Dispositions and exceptions

- **What:** Three items, each with its ground. (1) T1's three pseudo-ref errors: class (iii) — they are the candidate's own draft-host lines (the frame `theme=`, the module import, the asset URLs of sections 3–4); the posting procedure rewrites or re-hosts them, and fix lanes never "fix" them in the candidate. (2) The render row's two items, both environment or capture layer, not charged to the candidate: the page's runtime-hotlink site-theme chain (KB-40), and the sample's T2 run returning no machine verdict (exit 2 — a coverage caveat recorded in the row, not a result). (3) T4's one item, the P7-minor: Noto Sans JP is named in the credit block's font line and in both font stacks but is never loaded by this file. The ledger dispositions it (GOSIGN2-LEDGER §(c3): P7 DISPOSITIONED, recorded without a display-affecting mark under the T4 bar); the argument is restated in the per-theme record.
- **Why:** A disposition is a decision with grounds (AGENTS.md §3 classes (i)/(ii)/(iii); the named KB entries), not an omission; environment-layer lines are recorded as not-charged.
- **Verify:** Each item names its deciding record above and in the per-theme record.
- **Disposition:** DISPOSITIONED (all three items).

### 12. Verification

- **What:** (a) T1 source check (T1-ROWS row 159): exit 1, 3 errors / 1 warn / 1 info; all three errors are pseudo-ref, class (iii); there is no class (i) error. (b) T2/T3 render (RENDER-ROWS-2, lane RENDER-S2-C (EN16)): FINDINGS, the two items of section 11(2), both dispositioned; the sample's exit 2 is recorded as a coverage caveat in the row itself. (c) T4/T5 (LOCALIZE-ROWS row 124): FINDINGS jointly; the ledger §(c3) line records the theme's T4 outcome as the P7 item DISPOSITIONED. (d) This package is self-verifying: `python3 review/build_review.py --check` regenerates diff.md and the verdict stamp from the two byte-faithful copies in this directory and compares. Counts in this README are the generator's (difflib, autojunk off): +75/−64 in 43 classifier change blocks / 16 diff hunks.
- **Why:** Verification claims name the cheapest deciding check and its result, not a general assurance.
- **Verify:** Re-run the checker on `pages/theme:prom-labs-jp.txt` and `python3 review/build_review.py --check` in this repo.
- **Disposition:** PASS (GOSIGN2-LEDGER (b) row 124; go-sign, COMPLETION-REPORT §10).

## Per-theme record

### The P7-minor, restated (dispositioned)

LOCALIZE-ROWS row 124 charges, in the lane's words: "P7-minor (named/credited JP font never loaded)". The bytes bear it out exactly. The credit block's font line names three fonts as the theme's (candidate L22); both `font-family` stacks name Noto Sans JP as their Japanese fallback (candidate L133, L151); and `grep -n '@import' candidate.txt` returns only the Homenaje and Lato loads — no line of this file loads Noto Sans JP, and neither does the theme's delivery (its only delivery is its own code). The disposition's ground, restated so it can be re-derived: P7's failure mode (KB-16) is kana falling back to an unstyled default because no JP family is *named*; here a JP family is named in every stack that renders body text, so Japanese text renders in the platform's default Japanese face wherever the named webfont is absent — a cosmetic gap (the theme's chosen JP face is not the one that renders), not the KB-16 failure (no JP face named at all). That is why the ledger records the item without a display-affecting mark under the T4 bar while still recording it. This package carries the disposition and its ground; it does not upgrade the item to a fix, and it does not hide it. One record tension is noted for accuracy: the LOCALIZE row's count column reads 1 for this theme while the §(c3) gloss says the item was recorded without a display-affecting mark; the (c3) line is the determination record and governs the reading here.

### The usage exhibit's self-reference (flagged)

The usage exhibit at candidate L27 reads `> @@[[include :scp-jp:theme:prom-labs]]@@` — the include a user is told to paste names the theme's plain slug on scp-jp, where the candidate's posting name is theme:prom-labs-jp. The original's exhibit names `:scp-wiki:theme:prom-labs` (original L17), that page's real name on its own wiki, so the port's repoint changed the site prefix and kept a name that, on the target wiki, will not be the posted page's name. Probes made for this package (2026-11-17): both `https://scp-jp.wikidot.com/theme:prom-labs` and `https://scp-jp.wikidot.com/theme:prom-labs-jp` return 404 today, because the theme is not yet posted in either name; the probe therefore cannot decide the point, and the flag rests on the posting-name convention, the same ground on which the M-pure-3 batch flagged five instances of this shape (cmst, cleaning-services, construct, cosmos, cyber-specter) and a population sweep is repairing the family. This package does not edit the candidate; the flag is recorded so the sweep's list is complete.

## Appendix — heuristic blocks

For class M, the heuristic blocks collapse into one table rather than per-block slots; each was resolved in the section named.

| Block | Span | Resolution |
|---|---|---|
| B5 | orig 15-15 → cand 25-25 | Intro prose translation (section 6) |
| B7 | orig 20-23 → cand 30-33 | Banner attribution comment, translated (sections 1, 6) |
| B26 | orig 160-160 → cand 170-170 | CSS comment translation (section 6) |
| B27 | orig 165-165 → cand 175-175 | CSS comment translation (section 6) |
| B28 | orig 167-167 → cand 177-177 | CSS comment translation (section 6) |
| B31 | orig 209-210 → cand 219-221 | Interwiki selector extension, the frame tint's in-page half (section 3) |
| B39 | orig 265-266 → cand 276-277 | CSS comment translation + one whitespace line (sections 6, 9) |
| B43 | orig 293-295 → cand 304-306 | CSS comment translation + whitespace lines (sections 6, 9) |

## Change set outside the two diffed files

The diff covers two files; the port's record is one file larger. `pages/theme-decoration-sample-prom-labs-jp.txt` is the decoration sample the render checks ran against (its findings are the sample half of section 11(2)); it belongs to this theme's record but carries no port change of its own to explain here. There are no companion fragments, no shared base file, and no inbound-link repairs in other candidates for this theme.
