# Review package — theme:rpma-jp (KO → JP port)

<!-- BEGIN GENERATED VERDICT STAMP — do not hand-edit; regenerate with review/build_review.py -->
## Verdict stamp
- Theme: theme:rpma-jp — origin KO, population #284 [GOSIGN2-LEDGER (b) row 284]
- Overall: STALE — candidate file changed since the verdict was computed (verdict against 435a6bb-era content, file sha256 now 577801e3ed1ace00424ed57325c0c411793401cfeae553e2eac83b2b31fd11be); verdict not carried over, re-judgement required
> verdicts below describe the pre-change file
- T1 (source check): FINDINGS (classified) — baseline 2026-11-16: exit 1, 7 errors / 0 warns / 1 info (hotlink×6, pseudo-ref×1); standing classes dispositioned in register c1 [T1-ROWS row 254; GOSIGN2-LEDGER (b) row 284]
- T2/T3 (render, combined verdict): FINDINGS — [combined T2/T3] report `FINDINGS` — page runtime-hotlink incl. cdn.jsdelivr.net + scpko.wdfiles.com; sample credit-modal (preview-form) + 884px@768 overflow (one combo http.cat among other hosts); T3 none beyond cross-cutting items. [RENDER-ROWS-2 (RENDER-S2-H (KO8))]
- Engine coverage: full matrix as run by the lane; coverage not separately caveated in the row [RENDER-ROWS-2 row]
- Credit modal: sample credit-modal errors dispositioned preview-form (credit:start-preview has no modal mechanism; GOSIGN-TESTS T2 amendment, 2026-11-16) [RENDER-ROWS-2 (RENDER-S2-H (KO8))]
- T4 (localize patterns + follow-up): FINDINGS — display-affecting findings: 2 [LOCALIZE-ROWS row 283, source LOCALIZE-S2-F]
- T5 (translation text): FINDINGS — the source reports judge T4/T5 jointly; one verdict word covers both [LOCALIZE-ROWS row 283]
- FIX5 re-judgement: none — no OPEN items at the ledger determination [GOSIGN2-LEDGER (b) row 284]
- Computed against: canonical commit b5cb7241f527a44933e45599b41df210690771c4; candidate file pages/theme:rpma-jp.txt sha256:577801e3ed1ace00424ed57325c0c411793401cfeae553e2eac83b2b31fd11be; record: GOSIGN2-LEDGER.md + GOSIGN2-LEDGER-SUPPLEMENT.md as of the FIX5 head 435a6bb
<!-- END GENERATED VERDICT STAMP -->

## Status

| | |
|---|---|
| Verdict | **PASS** — passed at the ledger determination; this theme had no OPEN items and no §(e) register entry (GOSIGN2-LEDGER (b) row 284) |
| Standing items | **DISPOSITIONED** — T1 hotlink ×6 + pseudo-ref ×1 (original-state delivery and draft form, section 11); the render row's items (KB-32 / KB-33 / KB-34 / KB-40 family, section 11); T4's charges all DISPOSITIONED (P4, P5, P9, P11, section 11). Two items are flagged in the per-theme record: the dropped curtain divs, which no record names, and the usage exhibits' plain-slug self-references |
| Go-sign basis | COMPLETION-REPORT.md §10 (go-sign issued; 81 FIXED / 26 DISPOSITIONED / 0 OPEN across the sweep) |
| Named exception | None for this theme (the sweep's single named exception is theme:amethyst-v2, which has no candidate) |

## Provenance

| | Original | Candidate |
|---|---|---|
| Page | theme:rpma | theme:rpma-jp |
| Wiki | scpko.wikidot.com | SCP-JP Sigma-10 candidate (canonical repo) |
| Reference revision | 41 (first translation; the candidate's credit block records 初訳時参照リビジョン: 41) | — |
| Source of this copy | Campaign cache `gosign2-lanes/lane-oc-gs-localize-s2-F/orig-rpma.txt`, via the mirror store (class COPY, hash-verified against review/sources.tsv) | Canonical file `pages/theme:rpma-jp.txt`, copied at worktree HEAD 5506feb |
| Lines / bytes | 581 lines / 12,825 bytes | 593 lines / 13,528 bytes |
| SHA-256 | 824ea098d87c4a472eb905210e736be1a7392b13586c91b3a36597098a6f7351 | bcd5518d54c84cac658221daccb39f79b49993b03f4ff91877897331052958cf |

Wave history: the candidate was created by the Stage 2 KO8 integration (commit 28aaab2, the LOCALIZE-S2-F wave's port) and has exactly one later commit, 1869877 (FIX-CREDIT-D), whose rpma hunk is the translator-field normalization （翻訳責任者 taking its ruling-3 form). No FIX5 commit touches this file, because the theme had no OPEN items for FIX5 to re-judge.

## Summary

This port keeps more of the original's state than any other in the batch, by disposition: the Korean display fonts still load from the original's jsDelivr/GitHub CDN, the four CSS background assets still serve from the KO wiki (scheme upgraded to https), the credit block's title fields keep the Korean title, and the ledger dispositions each of those retentions by name (P4 original-state CDN delivery, P5/KB-58, P9 under ruling 2, P11). What the port does change is the machinery: the author's unprefixed info block becomes the preview credit block plus translated credit prose, the original's live in-page CSS module becomes a code exhibit delivered through the standard tail module and frame, and the prose (both usage sections, the credit lists, the headings) is translated. Two flags are recorded in the per-theme record: the original's two decorative curtain divs are dropped with no record naming the drop (their CSS survives), and both usage exhibits name `:scp-jp:theme:rpma`, the plain slug, where the candidate's posting name is theme:rpma-jp.

## Class summary

Auto-classification by review/classify_hunks.py (signature table 2026-11-17.1): 19 change blocks — 11 specific (57.9%), 7 heuristic (36.8%), 1 residue (5.3%), 0 skipped. Pattern citations below name the KB entry; the patterns/ tree state cited throughout is commit 9c5e9079afb01d30cb9fc4ef9d714e5591eb2ffa.

| Label | Blocks |
|---|---|
| TRANS-UNANCHORED | 8 |
| CSS-BODY | 5 |
| IFTAGS | 3 |
| INFO-DEL | 2 |
| SELF-DELIVERY | 2 |
| DRAFT-HOST | 2 |
| TRANSLATION-ANCHORED | 2 |
| CREDIT-PREVIEW | 1 |
| CREDIT-PROSE | 1 |
| ESCAPED-INCLUDE | 1 |
| INCLUDE-REPOINT | 1 |
| TASL-FIELDS | 1 |

Adjudication for this README (every block was read against the bytes): the five CSS-BODY blocks are four http→https scheme upgrades on kept KO-host asset URLs (B13–B16, section 4) and the code exhibit's closing tags (B17, section 3) — none is an unclassified CSS change in substance. The one residue block (B11) is an alignment artefact at the gate close (appendix). The two INFO-DEL primaries are the info includes' deletion with their content carried as prose (section 1). After adjudication no block is left unexplained.

## Standing sections

### 0. Header and provenance frame

- **What:** Theme theme:rpma-jp; original theme:rpma on scpko at reference revision 41; candidate `pages/theme:rpma-jp.txt`. Provenance route: derived from the original at the reference revision by the LOCALIZE-S2-F wave (sources.tsv kind: standard; no production JP counterpart exists for this theme, so the R4 adoption question does not arise). The original's head is unlike the population's: two decorative curtain divs (original L1–7) precede the tag gate (original L9), and the credit sits in an unprefixed `[[include info:start]]` block. The candidate opens with the localized gate `[[iftags +テーマ]]` (candidate L1) and the credit block (L3–12); the curtain divs are absent (per-theme record).
- **Why:** Section 0 declares the provenance route so every later count is read against the right baseline; the gate's tag is P2 (iftags tag localization).
- **Verify:** The sources.tsv row for rpma-jp; `sha256sum original.txt` against the Provenance table.
- **Disposition:** Standing (the route itself); the gate change is P2, applied.

### 1. Credit and attribution

- **What:** The original's credit furniture is the author's own info block: unprefixed `[[include info:start]]` / `info:end` (original L11, L32) carrying the title, the setting credit （設定原案: [[*user ProfoundAbyss]]), the design credit （デザイン・制作: [[*user thd-glasses]]), an image-source list (the RPMA logo built on a pixabay image; all other images by thd-glasses), and a font-source list (two noonnu.cc font pages). There is no Rate module. The candidate deletes the info includes (blocks B4, B9) and installs the JP form: a `:scp-jp:credit:start-preview`/`end-preview` block (candidate L3–12) carrying the eight ruling-3 fields （タイトル 자줏빛 궁정 테마; 翻訳責任者 AI; 翻訳年 2026; 原題 자줏빛 궁정 테마; 著作権者 thd-glasses; 作成年 2020; 初訳時参照リビジョン 41; the source link, host-verified in section 7). The info block's remaining content survives as body prose directly below, translated: the Japanese title heading, both credit lines with their user links (candidate L14–17), the image-source list (L19–24), and the font-source list (L26–28). So no attribution is dropped: the field names the designer the original names, and the setting author's credit stands in prose where the original's own layout puts the credits. The title fields keep the theme's Korean title — the LOCALIZE row's §3 charge — under the title-language disposition of section 11. T7 credit CSS: no supplement was added; the credit-adjacent rules in the CSS are inherited on both sides (five matching lines each).
- **Why:** P3/T1: the preview credit module is the rate-bearing JP form; the author's unprefixed info module is branch furniture that does not render on scp-jp, so its content is carried as prose and its fields as the credit block (the ledger class C shape, residue handled by conversion, not duplication — a kept info pair beside the credit block would be the KB-10 double-furniture failure). Ruling 3 fixes the eight fields.
- **Verify:** `grep -n 'info:start\|info:end' candidate.txt` returns nothing; read candidate L3–12 against the eight fields and L14–28 against original L11–31.
- **Disposition:** Applied. The §3 Korean title is DISPOSITIONED (ruling 2 title language, via the ledger's P9 line, section 11).

### 2. Includes and components

- **What:** Three include changes besides the credit pair. The info pair is deleted (section 1). The interwiki-style frame is added at the tail in its `:scp-jp:` form (candidate L590, section 3). The two usage exhibits are repointed `:scpko:theme:rpma` → `:scp-jp:theme:rpma` (block B10, original L37/L42 → candidate L37/L42), escaped includes inside the two usage sections. No component swap (T8) occurs. The exhibits' target names are flagged in the per-theme record.
- **Why:** P1 (KB-15): an include must name the JP counterpart that actually exists on scp-jp; the author's unprefixed info includes name scpko-side modules with no JP existence, so they are removed with their content carried (section 1), and the frame names its `:scp-jp:` form. Ruling 4 is not engaged: no component had to be ported alongside this theme.
- **Verify:** `grep -n '\[\[include' candidate.txt` — the credit pair (L3, L12), the two exhibits (L37, L42), and the frame (L590).
- **Disposition:** Applied; the exhibits' name form is the flagged item of the per-theme record.

### 3. Delivery and code loading

- **What:** The delivery mechanism is replaced outright, and the replacement is the port's largest structural act. The original has no local--code delivery at all: its CSS is a live `[[module CSS show="true"]]` inside a `display: none` div after the body (original L48–580; the classifier's topology pass finds no original components and `external_own_delivery: false`). The candidate presents the same CSS as a `[[code type="css"]]` exhibit inside a collapsible (candidate L50–583; the closing tags are block B17) and delivers it through the population's standard tail: a `[[module css]]` importing the candidate's own `local--code/theme%3Arpma-jp/1` from the draft host (candidate L587–589, block B19), with the interwiki-style frame at priority 1 naming the same /1 delivery (candidate L590–593, block B18). Inside the CSS, the four asset URLs keep their KO host with the scheme upgraded (section 4), and the font faces keep their CDN (section 4). The CSS content's order is the original's order.
- **Why:** P4/T9 and P6/T3: in the JP environment a theme's live channel is its own local--code delivery framed by interwiki-style; the original's in-page live module is the branch-local mechanism it replaces. The draft-host form of the two delivery lines is KB-41, class (iii).
- **Verify:** `grep -n 'local--code\|module css' candidate.txt` — the tail pair at L587–591; read original L48–50 against candidate L48–53 for the mechanism change.
- **Disposition:** DISPOSITIONED (draft-host lines, class (iii)); the mechanism replacement itself is applied, as the population's form.

### 4. Fonts and assets

- **What:** Fonts: the original's two `@font-face` declarations load the Korean display faces （국립박물관문화재단클래식M and L) from `cdn.jsdelivr.net/gh/projectnoonnu/noonfonts_twelve@1.0/` (original code head; candidate L54–55, byte-identical). The stacks that use them are likewise carried (`'국립박물관문화재단클래식M', Arial, sans-serif` at candidate L96, L193; the L face at L101, L206). No JP font is loaded and no stack gains one — there is no JPFONT block in this pair. This retention is T4's pattern-4 charge (personal-GitHub fonts via jsDelivr/gh, display-affecting, redistribution outside the exception list), dispositioned as original-state CDN delivery (section 11). Assets (blocks B13–B16): the four CSS background URLs keep their scpko.wdfiles paths with only the scheme upgraded http → https — `curtain-right.png` (candidate L69), `curtain-left.png` (L80), `body_bg_0.png` (L137), `violet-logo-500.png` (L143). The pixabay source image is credited in prose (section 1), not loaded.
- **Why:** P5's re-hosting rule is the default; this theme is one of the recorded exceptions where the original-state delivery stands by disposition (KB-58 deferred assets; the (ii) posting class) — the assets serve today from the KO wiki, and the posting procedure, not the candidate, is where re-hosting would occur. The scheme upgrade is the settled http exception's serving half: the same host and file over https is not a new reference. The font retention is P4's original-state delivery disposition; the faces are the theme's identity (a Korean court aesthetic for a KO hub), and no JP face was substituted by any wave.
- **Verify:** `grep -n 'jsdelivr\|scpko.wdfiles' candidate.txt` — two font lines and four asset lines, all https; `grep -n '@import' candidate.txt` returns only the tail delivery import.
- **Disposition:** DISPOSITIONED (P4 delivery class (ii) for the fonts; P5 class (ii) / KB-58 for the assets).

### 5. Header, sidebar, and site furniture

- **What:** No header variables exist on either side (no `--header-title` / `--header-subtitle` / `--logo-image`), and no P8 adaptation was needed. The language item that belongs to this section's family is T4's pattern-9 charge (KO heading strings): what survives in Korean is the credit title fields (section 1), the code banner comment ("자줏빛 궁정 CSS 테마", porter-visible, section 6), and the font family names (proper nouns, section 4) — the prose headings themselves are translated （使用方法 at candidate L36, L43). The ledger dispositions the pattern-9 item under P9 (ruling 2: header/title language out of scope for migration correctness).
- **Why:** Ruling 2 removes title language from the correctness question; the retained strings are the theme's name and its faces' names, not untranslated prose.
- **Verify:** `grep -n -- '--header-' candidate.txt` returns nothing; the Korean survivals are the lines named above.
- **Disposition:** DISPOSITIONED (P9, ruling 2; GOSIGN2-LEDGER §(c3)).

### 6. Text translation

- **What:** The prose is translated throughout: the credit prose lists (section 1), both usage sections — the Korean one (original L34–38 → candidate L36–40) and the English one (original L40–44 → candidate L43–47), both now Japanese — and the source-code heading and collapsible labels (candidate L49–52). The counted groups are eight TRANS-UNANCHORED blocks and two TRANSLATION-ANCHORED blocks (B6, B8: single-line prose and list items verified line by line). Korean survives in the candidate in exactly the dispositioned places of sections 1, 4, and 5, plus the code banner comment (porter-visible only, R1's comment half — it is the original's own banner, carried). The curtain divs' deletion is not a translation event and is recorded in the per-theme record, not hidden in this section's counts.
- **Why:** P10 (body and usage translation is the port's purpose) and KB-18 (reader-visible strings). The unanchored group is where a silent deletion would hide, which is why the curtain divs were checked explicitly against the census in section 8.
- **Verify:** The pairs are diff.md's body sections in order; a Hangul scan of candidate.txt returns only the sections 1/4/5 survivals and the banner comment.
- **Disposition:** Standing (the port itself).

### 7. Links

- **What:** Two link items. The credit block's source link (candidate L11) names `https://scpko.wikidot.com/theme%3Arpma` — the original's recorded host (review/sources.tsv `original_url`), so the host check passes and no probe was triggered; its label is the theme's Korean title rather than the word ソース, a T5 joint-note shape the ledger's title disposition covers. The hub link in the credit prose: the original's same-site `[[[thd-glasses-hub|…]]]` (original L29) becomes an absolute URL link `[*https://scpko.wikidot.com/thd-glasses-hub …]` (candidate L34). The LOCALIZE row charged this target 404 (pattern 11); as a same-site link on scp-jp it would indeed not resolve, and the candidate's absolute form names the author's hub on its home wiki — probed for this package (2026-11-17), it returns 200. The noonnu.cc font-page links (candidate L27–28) are font-provenance citations, carried as the original carries them.
- **Why:** P11: prose links take the JP counterpart or the serving original, under the dead-reference evidence standard; where the original-side page is the author's own hub with no JP counterpart, the serving original is the right target, and the absolute form is what makes it resolve from scp-jp.
- **Verify:** `grep -n 'thd-glasses-hub' candidate.txt` — one hit, the absolute form; the probe above is re-runnable with any HTTP client.
- **Disposition:** DISPOSITIONED (P11, sibling / batch-posting class; GOSIGN2-LEDGER §(c3)) — with the probe update recorded here: the target serves today in the candidate's form.

### 8. Structure

- **What:** Three structural events, all named, against the localize.md closing rule. (1) The delivery mechanism replacement (section 3): live in-page module → code exhibit plus tail delivery; the CSS content and its order are preserved inside the exhibit. (2) The info block's conversion to credit block plus prose (section 1). (3) The curtain divs' deletion (per-theme record). The exhibit census otherwise corresponds: the two usage sections, the credit lists, and the code exhibit are present on both sides (the original's code is a live module, the candidate's an exhibit — the same content in the population's presentation form). Selector and variable names inside the CSS are preserved.
- **Why:** R3 exists to force exactly this census, because a restructure and a deletion share a diff shape and ledger class I charges the silent form; items (1) and (2) are the population's sanctioned conversions, and item (3) is flagged precisely because no sanction names it.
- **Verify:** Compare `grep -n '\[\[div\|\[\[code\|\[\[module\|\[\[include' original.txt candidate.txt` — the sequences differ at exactly the three named events.
- **Disposition:** Standing for (1) and (2); item (3) flagged in the per-theme record.

### 9. Formatting only

- **What:** None. The classifier finds no whitespace-only block and no re-indentation (0 and 0) in this pair.
- **Why:** Formatting churn is disclosed as its own class so it is never mistaken for a semantic change.
- **Verify:** The classifier summary in classification.json (no WS-ONLY label).
- **Disposition:** None required.

### 10. Porter annotations

- **What:** None. An explicit check of the candidate finds no `[!-- ... --]` porter comment and no editor line with no original counterpart; the classifier's ANNOTATION signature does not fire. The code banner comment is the original's own, carried (section 6).
- **Why:** R2: porter-added text is part of the change record; here there is none to record.
- **Verify:** `grep -n '\[!--' candidate.txt` returns nothing.
- **Disposition:** Standing.

### 11. Dispositions and exceptions

- **What:** Four items, each with its ground. (1) T1's six hotlink errors: class (ii) — they are the two jsDelivr font loads and the four scpko.wdfiles asset URLs of section 4, the original-state delivery family the ledger dispositions (P4/P5); the pages render styled today and no error-box defect arises from these hosts (the render row's own words). (2) T1's one pseudo-ref error: class (iii), the draft-host delivery lines of section 3. (3) The render row's remaining items, environment or capture layer: the sample's credit-modal errors (KB-32, ruling 5), the 884px@768 overflow (KB-33/KB-34 cross-cutting families), and one combo's http.cat host (KB-44 transient capture family). (4) T4's charges, all dispositioned in the ledger §(c3): pattern 4 (fonts) under P4, pattern 5 (KO direct links) under P5/KB-58, pattern 9 (KO heading strings) and the §3 title under P9/ruling 2, pattern 11 (the hub link) under P11.
- **Why:** A disposition is a decision with grounds (AGENTS.md §3 classes (i)/(ii)/(iii); the named KB entries), not an omission; environment-layer lines are recorded as not-charged.
- **Verify:** Each item names its deciding record above and in the per-theme record.
- **Disposition:** DISPOSITIONED (all four items).

### 12. Verification

- **What:** (a) T1 source check (T1-ROWS row 254): exit 1, 7 errors / 0 warns / 1 info; the errors are hotlink ×6 and pseudo-ref ×1, all in the dispositioned classes of section 11; there is no class (i) error. (b) T2/T3 render (RENDER-ROWS-2, lane RENDER-S2-H (KO8)): FINDINGS, the items of section 11(1)/(3), all dispositioned; T3 none beyond cross-cutting items. (c) T4/T5 (LOCALIZE-ROWS row 283): FINDINGS jointly, display-affecting findings 2 (the pattern-4 and pattern-5 families); the ledger §(c3) line records the theme's T4 outcome as P4, P5, P9, and P11 all DISPOSITIONED. (d) This package is self-verifying: `python3 review/build_review.py --check` regenerates diff.md and the verdict stamp from the two byte-faithful copies in this directory and compares. Counts in this README are the generator's (difflib, autojunk off): +55/−44 in 19 classifier change blocks / 5 diff hunks.
- **Why:** Verification claims name the cheapest deciding check and its result, not a general assurance.
- **Verify:** Re-run the checker on `pages/theme:rpma-jp.txt` and `python3 review/build_review.py --check` in this repo.
- **Disposition:** PASS (GOSIGN2-LEDGER (b) row 284; go-sign, COMPLETION-REPORT §10).

## Per-theme record

### The curtain divs (flagged — a drop no record names)

The original opens with two decorative divs, `[[div class="curtain-right"]]` and `[[div class="curtain-left"]]` (original L1–7), which draw the theme's curtains on the theme page itself. The candidate contains neither div (`grep -n 'div class="curtain' candidate.txt` returns nothing), while the CSS that styles them survives in full — the background rules at candidate L69 and L80 and the media-query sizing at the code's tail — so the candidate carries live rules for markup its own page no longer emits. No record names this: the LOCALIZE row's charges are the font, link, heading, and hub items of section 11, the ledger's §(c3) line dispositions those, and the render checks ran against the decoration sample, not the theme page's own decoration. The drop is therefore flagged here with its evidence, neither hidden nor upgraded: the theme's function for pages that include it is unaffected (the divs never travelled with an include; a page can still emit them and the kept CSS will style them), and what is lost is the theme page's own showcase decoration. Whether that loss was a porter's quiet simplification or an unrecorded decision, the documentation's job is to make it visible, which this record does.

### The usage exhibits' self-references (flagged)

Both usage exhibits read `> @@[[include :scp-jp:theme:rpma]]@@` (candidate L37 and L42) — the include a user is told to paste names the theme's plain slug on scp-jp, where the candidate's posting name is theme:rpma-jp. The original's exhibits name `:scpko:theme:rpma` (original L37, L42), that page's real name on its own wiki, so the port's repoint changed the site prefix and kept a name that, on the target wiki, will not be the posted page's name. Probes made for this package (2026-11-17): both `https://scp-jp.wikidot.com/theme:rpma` and `https://scp-jp.wikidot.com/theme:rpma-jp` return 404 today, because the theme is not yet posted in either name; the probe therefore cannot decide the point, and the flag rests on the posting-name convention, the same ground on which the M-pure-3 batch flagged five instances of this shape and a population sweep is repairing the family. This package does not edit the candidate; the flag is recorded so the sweep's list is complete.

## Appendix — residue blocks

| Block | Span | Resolution |
|---|---|---|
| B11 | orig 46-46 → cand 46-46 | Alignment artefact: the aligner pairs the original's gate close (`[[/iftags]]`, original L46) with the candidate's rule line at the corresponding position in its second usage section. The gate structure is narrated in sections 0 and 8; no unexplained content. |

## Change set outside the two diffed files

The diff covers two files; the port's record is one file larger. `pages/theme-decoration-sample-rpma-jp.txt` is the decoration sample the render checks ran against (its findings are the sample half of section 11(3)); it belongs to this theme's record but carries no port change of its own to explain here. There are no companion fragments, no shared base file, and no inbound-link repairs in other candidates for this theme.
