# Review package — theme:3law-pride-jp (EN → JP port)

<!-- BEGIN GENERATED VERDICT STAMP — do not hand-edit; regenerate with review/build_review.py -->
## Verdict stamp
- Theme: theme:3law-pride-jp — origin EN, population #45 [GOSIGN2-LEDGER (b) row 45]
- Overall: STALE — candidate file changed since the verdict was computed (verdict against 435a6bb-era content, file sha256 now ca340eb2bc2c816e31bb69c27f0f9760d196e038292281564329280009aa17e7); verdict not carried over, re-judgement required
> verdicts below describe the pre-change file
- T1 (source check): FINDINGS (classified) — baseline 2026-11-16: exit 1, 4 errors / 1 warn / 0 infos (hotlink×4); standing classes dispositioned in register c1 [T1-ROWS row 45; GOSIGN2-LEDGER (b) row 45]
- T2/T3 (render, combined verdict): FINDINGS — [combined T2/T3] report `FINDINGS` — candidate-specific THIRD LAW wordmark clips at ≤375 both engines; "ソース" contrast 4.11 warn; other lines cross-cutting/draft-form/by-design. [RENDER-ROWS-1 (RENDER-S2-A)]
- Engine coverage: full matrix as run by the lane; coverage not separately caveated in the row [RENDER-ROWS-1 row]
- Credit modal: no credit-modal line in this theme's row; no sample credit-modal error recorded [RENDER-ROWS-1 (RENDER-S2-A)]
- T4 (localize patterns + follow-up): FINDINGS — display-affecting findings: 1 [LOCALIZE-ROWS row 45, source LOCALIZE-S2-A]
- T5 (translation text): FINDINGS — the source reports judge T4/T5 jointly; one verdict word covers both [LOCALIZE-ROWS row 45]
- FIX5 re-judgement: none — no OPEN items at the ledger determination [GOSIGN2-LEDGER (b) row 45]
- Computed against: canonical commit 722ceb5c949172bb5185d51ef56ce4119ee4fa91; candidate file pages/theme:3law-pride-jp.txt sha256:ca340eb2bc2c816e31bb69c27f0f9760d196e038292281564329280009aa17e7; record: GOSIGN2-LEDGER.md + GOSIGN2-LEDGER-SUPPLEMENT.md as of the FIX5 head 435a6bb
<!-- END GENERATED VERDICT STAMP -->

## Status

| | |
|---|---|
| Verdict | **PASS** — passed at the ledger determination; no OPEN items and no §(e) register entry (GOSIGN2-LEDGER (b) row 45) |
| Wave history | Three commits touch the candidate: creation by the Stage 2 EN batch (3205f27), the FIX-P4 commit (f1138e4: frame, translator field, JP font import and stack), and FIX4-CREDIT (9fbcd94: the T7 credit-CSS supplement, +12 lines). Each is narrated in the section it belongs to |
| Standing items | **DISPOSITIONED** — T1 hotlink ×4 (class (ii), section 11); the iftags structural suspicion (FIX3-S2EN §6.11); the render row's wordmark clip (KB-35 family) and contrast warn (KB-39) |
| Go-sign basis | COMPLETION-REPORT.md §10 (go-sign issued; 81 FIXED / 26 DISPOSITIONED / 0 OPEN across the sweep) |
| Named exception | None for this theme (the sweep's single named exception is theme:amethyst-v2, which has no candidate) |

## Provenance

| | Original | Candidate |
|---|---|---|
| Page | theme:3law-pride | theme:3law-pride-jp |
| Wiki | scp-wiki.wikidot.com | SCP-JP Sigma-10 candidate (canonical repo) |
| Reference revision | 7 (first translation; the candidate's credit block records 初訳時参照リビジョン: 7) | — |
| Source of this copy | Campaign cache `gosign2-lanes/lane-oc-gs-localize-s2-A/orig-3law-pride.txt`, via the mirror store (class COPY, hash-verified against review/sources.tsv) | Canonical file `pages/theme:3law-pride-jp.txt`, copied at worktree HEAD 1605bbd; the file's last content change is commit 9fbcd94 (FIX4-CREDIT) |
| Lines / bytes | 36 lines / 959 bytes (the last line carries no trailing newline, so `wc -l` reports 35) | 389 lines / 8,216 bytes |
| SHA-256 | a551f8633159e87453d2ac513f53d5494171a587eb753243e51832d3092f9434 | f59fc9fa8227247d713c4c2f70d3149689dddeaf0467d03e834095f455a986c9 |

The size gap is the story of this port: the original is a 36-line variant page that imports its base theme's stylesheet; the candidate carries the base stylesheet inline (section 3). There is no `pages/theme:3law-jp.txt` in the canonical repo: the base has no standalone JP candidate, and both Third Law variants inline it instead.

## Summary

The original declares itself a variant: it gates on `+theme`, imports the base Third Law code delivery (`local--code/theme%3A3law/1`) in a head module, shows a bare Rate module, gives two include lines (base + variant) as its usage, exhibits its own 17 lines of CSS in a `[[code]]` block, and imports its own code delivery in a tail module. The candidate keeps that shape's intent and rebuilds every joint: the credit furniture becomes the JP preview credit block with the eight ruling-3 fields; the base stylesheet is inlined into the candidate's single live `[[module CSS]]` (it has been inline since the creation commit, 371 lines at 3205f27); the variant's own CSS follows the base inside the same module; delivery is the campaign frame (interwiki-style at priority 1 naming the candidate's own draft-host delivery, added by f1138e4); the JP font supplement arrives in the same f1138e4 commit (a Noto Sans JP @import and one stack); and FIX4-CREDIT appends the credit-module CSS the production JP base page carries, which the candidate had dropped (section 1). Measured churn (diff.md, the generator's difflib count with autojunk off: +374/−21 in 10 classifier change blocks; a GNU-diff count of the same pair gives +370/−17 — the difference is alignment choice, not content). Almost all of the +374 is the inlined base body, not new writing.

## Class summary

Auto-classification by review/classify_hunks.py (signature table 2026-11-17.1): 10 change blocks — 9 specific (90.0%), 1 heuristic (10.0%), 0 residue, 0 skipped. Pattern citations below name the KB entry; the patterns/ tree state cited throughout is commit 9c5e9079afb01d30cb9fc4ef9d714e5591eb2ffa.

| Label | Blocks |
|---|---|
| DELIVERY-MOVE | 5 |
| SELF-DELIVERY | 2 |
| WS-ONLY | 2 |
| BARE-RATE-DEL | 1 |
| CREDIT-PREVIEW | 1 |
| CSS-BODY | 1 |
| DRAFT-HOST | 1 |
| EXHIBIT-RESTRUCTURE | 1 |
| IFTAGS | 1 |
| JPFONT-LOAD | 1 |
| T7-CREDIT-CSS | 1 |
| TASL-FIELDS | 1 |
| TRANS-UNANCHORED | 1 |

Adjudication for this README (every block was read against the bytes): the one heuristic block (B2, the original's base-delivery @import line) is resolved in section 3 — it is the declared base's delivery line, and the port's answer to it is the inlining, so no include-graph question remains. Two of the five DELIVERY-MOVE primaries (B4, B5) are topology-matcher artefacts: they pair the original's prose and usage lines with lines of the inlined base's comment header, which shares vocabulary with them; the prose itself is translated at candidate L20 and counted in section 6. The EXHIBIT-RESTRUCTURE primary (B6) is the module-CSS body pairing, adjudicated in section 8. After adjudication no block is left unexplained.

## Standing sections

### 0. Header and provenance frame

- **What:** Theme theme:3law-pride-jp; original theme:3law-pride on scp-wiki at reference revision 7; candidate `pages/theme:3law-pride-jp.txt`. Provenance route: derived from the original at the reference revision by the Stage 2 EN batch (commit 3205f27), with the base theme:3law stylesheet inlined as part of that derivation (the candidate's own prose declares it: **基盤:** 3law（インライン）, candidate L24). The candidate is not adopted from the production JP counterpart (the R4 question): the production page for the variant does not exist as a separate record, and the inlined base body is the EN base's text (its header comment is the EN credit text), not the production page's. The production counterpart enters this port at exactly one point, the T7 supplement of section 1, whose porter comment names its source lines. The frame order also changed: the original opens with its tag gate and delivery module; the candidate opens with the interwiki-style frame (candidate L1–5), then the gate (L7).
- **Why:** Section 0 declares the provenance route so the +374 added lines are read as base inlining, not as authorship; the gate's tag is P2, the frame is P6/T3 (section 3).
- **Verify:** The sources.tsv row for 3law-pride-jp; `sha256sum original.txt` against the Provenance table; read candidate L20–28.
- **Disposition:** Standing (the route itself).

### 1. Credit and attribution

- **What:** The original's credit furniture is a bare `[[module Rate]]` (original L6–8) and nothing else: no credit block, no license box. The candidate deletes the Rate (block B3) and installs the JP preview credit block (candidate L9–18) with the eight ruling-3 fields (title 第三法プライド・テーマ; 翻訳責任者 AI; 翻訳年 2026; 原題 Third Law Pride CSS Theme; 著作権者 GreenWolf; 作成年 2021; 初訳時参照リビジョン 7; the source link, host-verified in section 7). The translator field took its ruling-3 form in f1138e4 (SCP-JP → AI). The section's second half is the wave edit this theme is in class U for: FIX4-CREDIT (commit 9fbcd94, +12 lines) appended the credit-module CSS at candidate L376–386 — a porter comment (L376–378) and two rules (`.creditModule .rate-box-with-credit-button .creditButton` and its `:hover`, in the 3law palette #222e59 / #0c1121 / #404d7e). The comment names its source: the production counterpart `pages-existing/existing:theme-3law.txt` lines 356–365, and the bytes bear it out — those production lines carry the identical two rules in the identical palette. The candidate as created had no credit-module CSS at all, while the production base page styles the credit button; the repo-level review recorded exactly this defect shape for this theme (candidate lacks credit-module CSS its production counterpart styles), and FIX4-CREDIT is the repair. The classifier's T7 block sits at candidate L374–389, with the rule spans at L379–381 and L383–385.
- **Why:** P3/T1: the preview credit module is the rate-bearing JP form, so the bare Rate is deleted rather than duplicated (KB-09). T7 (KB-11): the JP credit module's DOM needs the button rules the branch original never shipped; where a production counterpart carries them, the supplement is carried from it verbatim, palette included, rather than invented. Ruling 3 fixes the eight fields and the translator credit form.
- **Verify:** `grep -n 'module Rate' candidate.txt` returns nothing; read candidate L9–18 against the eight fields; read `pages-existing/existing:theme-3law.txt` L356–365 against candidate L379–385 — the two rule bodies are identical.
- **Disposition:** FIXED (the credit fields by the credit waves per GOSIGN2-LEDGER §(c3); the T7 supplement by FIX4-CREDIT, commit 9fbcd94). No license box exists on either side, so the T4/KB-63 question does not arise.

### 2. Includes and components

- **What:** The candidate's includes are the frame (candidate L1), the credit pair (L9/L18), and no others. The original's usage text names two includes a user must write (`theme:3law` then `theme:3law-pride`, original L12–13); the candidate's usage names one (`theme:3law-pride-jp`, candidate L22), because the base include's content is inline (section 3). No foreign include survives in the candidate, and no component had to be ported alongside (ruling 4 not engaged): the base is CSS text, and it travels as text.
- **Why:** P1 (KB-15) governs include targets; here the operative fact is the base's delivery form, which is section 3's subject. A kept `:scp-wiki:` include would be a class (i) foreign-include error; there are none.
- **Verify:** `grep -n '\[\[include' candidate.txt` — three includes, all `:scp-jp:`.
- **Disposition:** Applied; no foreign include kept, no named exception needed.

### 3. Delivery and code loading

- **What:** The original delivers by @import twice: the base's code (`local--code/theme%3A3law/1` on scp-wiki.wdfiles.com, original L3, the classifier's heuristic block B2) in the head module, and its own code (`local--code/theme%3A3law-pride/1`, original L35) in the tail module. The candidate delivers once: the interwiki-style frame at candidate L1–5 (added by f1138e4) at priority 1, `theme=` naming the candidate's own `local--code/theme%3A3law-pride-jp/1` on the draft host; the original's tail self-import module was not carried over at all (the creation version ends at its `[[/module]]` with no tail import, verified against 3205f27), and the candidate's single `[[module CSS]]` (L26–387) holds the JP font import (L27), the base's station-font import (L28, section 4), the inlined base body (L30–358), the variant's own rules (L359–374), and the T7 supplement (L376–386). The inlining itself predates every fix wave: the creation commit's file is already 371 lines with the base body in place. The FIX-P4 wave's title ("pattern-4 repoint of base-theme CSS imports to JP port candidates") describes its 39-file family; in this file its diff is the frame addition, the translator field, and the font supplement — there was no base @import left to repoint, because the base was inline. That is a title-vs-diff mismatch in the wave's own record, flagged here and in the batch report; the bytes are as stated.
- **Why:** P4/T9 (own-code delivery from JP-side hosts) and P6/T3 (the interwiki-style supplement frame, priority 1 for the theme's own layer). Inlining the base is the port's answer to the base-delivery question the classifier could not decide: the variant cannot @import a JP base candidate that does not exist, and importing the EN base's delivery would keep a foreign delivery line live. The draft-host form of the frame's `theme=` URL is KB-41, class (iii): sanctioned at draft stage, rewritten to the production host at posting.
- **Verify:** `grep -n 'local--code' candidate.txt` — one hit, the frame's `theme=` line; `git show 3205f27:pages/theme:3law-pride-jp.txt | wc -l` returns 371, proving the inlining is original to the port.
- **Disposition:** DISPOSITIONED (the draft-host frame line, class (iii)); the base-delivery form is the port's standing shape, recorded here.

### 4. Fonts and assets

- **What:** Font load (arrived in f1138e4): candidate L27 adds the Google Fonts Noto Sans JP @import at the head of the module, and candidate L123 adds `"Noto Sans JP"` to the one stack that renders the header title (`'stationmedium', Arial, "Noto Sans JP", sans-serif`). The base's own font file import is kept verbatim on the EN host (candidate L28: `station-font.css` from scp-wiki.wdfiles.com `theme%3A3law`) — the Station face is the base's display face and its file lives with the base. Assets: three image URLs stay on scp-wiki.wdfiles.com — the base's `body_bg_7.png` (candidate L68) and `PL_3Law_Logo_2.png` (L73), and the variant's own `PL_3Law_Logo_Pride_Gradient3.png` (L368). Together with the station-font import these four lines are the T1 checker's hotlink ×4.
- **Why:** P7/T5 with KB-16 (the font load gap): the LOCALIZE row charged "no Japanese font specified"; the fix is the import plus the stack that actually renders Japanese header text, not a blanket stack rewrite — the base's remaining stacks are Latin display stacks whose glyphs are the design. P5 with KB-17 (asset hosts): the four EN-host file lines are posting-procedure re-hosting, class (ii), per the ledger §(c3) outcome for this row ("asset hosts = class (ii)").
- **Verify:** `grep -n 'Noto Sans JP' candidate.txt` — two hits (L27, L123); `grep -n 'wdfiles' candidate.txt` — the frame line plus the four class (ii) lines listed above.
- **Disposition:** Font supplement applied (f1138e4); the four EN-host file lines DISPOSITIONED (class (ii) / KB-58 family).

### 5. Header, sidebar, and site furniture

- **What:** No header variable is overridden: there is no `--header-title`, `--header-subtitle`, or `--logo-image` in the candidate; the header is the inlined base's rules, including its `content:` strings (`"Third Law "`, candidate L129; `'Scientia Potentia Est '`, L140) and the variant's slogan (`'Be Gay, Do Crimes '`, L372), all kept in English. The render row's one candidate-specific item is the THIRD LAW wordmark clipping at ≤375 in both engines.
- **Why:** The ledger §(c3) outcome for this row dispositions header language under ruling 2 (header and title language is out of scope for migration correctness); the kept strings are the base's design text (KB-57 family). The wordmark clip is the narrow-width header clip/collision family (KB-35; FIX3-S2EN §6.5, observations X1–X9), a render-side difference class, not a source defect.
- **Verify:** `grep -n -- '--header-' candidate.txt` returns nothing; the clip's record is RENDER-ROWS-1 (RENDER-S2-A (EN1)).
- **Disposition:** DISPOSITIONED (ruling 2 for the strings; KB-35 family for the clip).

### 6. Text translation

- **What:** The translated text is small and fully countable: the intro prose (original L10–13 → candidate L20, one line, with the usage and base lines restated as candidate L22 and L24), and the credit block's fields (section 1). The inlined base's CSS comments stay in English (they are the base's own header and section comments, porter-visible only), and its `content:` strings stay as designed (section 5). The original's hub link `[[[third-law-hub|Third Law]]]` does not survive into the candidate's compressed intro: the JP prose names the canon without linking a hub page, and no JP hub counterpart is named anywhere in the file. R5 glyph-form conversion: none (the source is English). R1 in-CSS text: the base's comments are untranslated, recorded here so the fact is stated rather than passed over; no string-valued variable carries reader-visible text in this theme.
- **Why:** P10 for the prose and fields; KB-18 covers reader-visible strings, and the comments are not reader-visible. The hub link falls under P11's evidence standard: no verified JP counterpart is recorded, and the port chose compression over an unverified repoint.
- **Verify:** Read candidate L20–24 against original L10–13; a CJK scan of the candidate's CSS comments returns nothing because they are the base's English comments, verifiable against the inlined body.
- **Disposition:** Standing (the port itself); the dropped hub link is recorded, not hidden.

### 7. Links

- **What:** The candidate's one live outbound link is the credit block's source link (candidate L16): `[*https://scp-wiki.wikidot.com/theme:3law-pride ソース]`. Its host is the original's recorded host in review/sources.tsv (scp-wiki.wikidot.com), so the jiha-class defect (a source link naming a non-serving host form) does not arise and no probe was needed. The usage include line is section 2's; the CSS file URLs are section 4's.
- **Why:** P11: prose links take the JP counterpart or the serving original, under the dead-reference evidence standard.
- **Verify:** `grep -n 'wikidot.com' candidate.txt` — the source link is the only hit.
- **Disposition:** Standing; no dead reference found in this file.

### 8. Structure

- **What:** The localize.md closing rule holds in the form this port allows: the inlined base keeps its variable names, selectors, and internal order (it is the EN base's body, carried whole), and every JP correction arrives outside it — the frame before it, the credit block before it, the font import at the module's head, and the T7 supplement appended at the module's tail (the FIX4-CREDIT +12 lines are the module's last rules, candidate L376–386). The classifier's EXHIBIT-RESTRUCTURE primary (B6) adjudicates as follows: the original's one exhibit (its own CSS in a `[[code]]` block, original L15–31) is not dropped and not replaced by other content — the variant's rules survive verbatim inside the candidate's live module (candidate L359–374, comment header included). What changed is the exhibit's status: the CSS is delivered live from the module instead of being displayed as a code exhibit, because the candidate is a self-delivering page. The exhibit census therefore reads: exhibits 1 → 0, live modules 2 → 1, and the variant CSS present on both sides.
- **Why:** R3 exists to force exactly this adjudication, because a restructure and a deletion share a diff shape and ledger class I charges the silent form; here the census, not the label, decides.
- **Verify:** Compare original L15–31 against candidate L359–374 — the comment header and both rules correspond line for line.
- **Disposition:** Standing; no structural deletion, no class I item.

### 9. Formatting only

- **What:** Two WS-ONLY blocks (B7, B8), each a single line inside the inlined base that differs only in trailing whitespace (the base body's two `" "` separator lines). The classifier finds no re-indentation anywhere (0 blocks pair up after leading-whitespace normalization), so the R7 follow-up-diff hazard is not triggered.
- **Why:** Formatting churn is disclosed as its own class so it is never mistaken for a semantic change, and so a reviewer can skip it safely.
- **Verify:** Blocks B7 and B8 in classification.json; the corresponding diff sections in diff.md.
- **Disposition:** None required.

### 10. Porter annotations

- **What:** One annotation: the T7 supplement's comment at candidate L376–378, naming the production source lines the two rules were carried from and the palette ground. It rides inside the T7 block, which is why no separate annotation signature fired. There are no `[!-- --]` translator notes and no editor lines in this candidate; the skeleton's "none" for this section does not survive contact with the bytes and is corrected here.
- **Why:** R2: porter-added text is part of the change record, and this comment is load-bearing — it is the only in-file statement of where the supplement came from, and section 1's verification depends on it.
- **Verify:** Read candidate L376–378.
- **Disposition:** Standing.

### 11. Dispositions and exceptions

- **What:** Four items, each with its ground. (1) T1's four hotlink errors: class (ii), posting-procedure — the station-font import and the three image URLs on scp-wiki.wdfiles.com (section 4); posting re-hosts them, and fix lanes never "fix" them in the candidate. (2) The LOCALIZE row's structural suspicion (theme CSS lives only inside the iftags gate, so it might not reach including pages): DISPOSITIONED per FIX3-S2EN §6.11, recorded in the ledger's register — the render reports did not confirm it; the theme renders with its CSS applied. (3) The render row's wordmark clip at ≤375 (KB-35 family, section 5) and the "ソース" contrast 4.11 warn (KB-39: machine contrast values include false positives on themed surfaces and the T3 walk did not confirm it as a defect). (4) Header and slogan language kept in English: ruling 2, per the ledger §(c3) outcome for this row.
- **Why:** A disposition is a decision with grounds (AGENTS.md §3 classes (i)/(ii)/(iii); the named KB entries), not an omission.
- **Verify:** Each item names its deciding record above; the T1 lines are enumerable by the grep in section 4.
- **Disposition:** DISPOSITIONED (all four items).

### 12. Verification

- **What:** (a) T1 source check (T1-ROWS row 45): exit 1, 4 errors / 1 warn / 0 infos; all four errors are hotlink, class (ii); there is no class (i) error. (b) T2/T3 render (RENDER-ROWS-1, lane RENDER-S2-A (EN1)): FINDINGS, the two items of section 11(3), both dispositioned; engine coverage the full matrix as run by the lane. (c) T4/T5 (LOCALIZE-ROWS row 45): FINDINGS jointly, display-affecting findings 1; the ledger §(c3) line closes the row's charges as DISPOSITIONED under the class outcomes, with the credit fields FIXED by the credit waves — and the file's own history adds the two later wave edits the §(c3) line predates in form: f1138e4 (frame, translator field, font) and 9fbcd94 (T7 supplement). (d) This package is self-verifying: `python3 review/build_review.py --check` regenerates diff.md and the verdict stamp from the two byte-faithful copies in this directory and compares. Counts in this README are the generator's (difflib, autojunk off): +374/−21 in 10 change blocks; the GNU-diff count of the same pair is +370/−17, and the difference is alignment choice, not content.
- **Why:** Verification claims name the cheapest deciding check and its result, not a general assurance.
- **Verify:** Re-run the checker on `pages/theme:3law-pride-jp.txt` and `python3 review/build_review.py --check` in this repo.
- **Disposition:** PASS (GOSIGN2-LEDGER (b) row 45; go-sign, COMPLETION-REPORT §10).

## Per-theme record

### The base that is not there

A reviewer opening the canonical repo will look for the base first: the original's prose says the variant requires the base Third Law Theme, and the FIX-P4 wave's title says base-theme CSS imports were repointed to JP port candidates. Neither a `pages/theme:3law-jp.txt` nor an @import of one exists. The record, from the bytes: the creation commit (3205f27) already inlines the EN base's stylesheet body into the candidate's module (371 lines at creation, the base body at the same position it holds today), the candidate's prose declares the shape (**基盤:** 3law（インライン）), and f1138e4's actual diff in this file is the frame, the translator field, and the font supplement — no base repoint was left for it to make. The same shape holds for theme:3lawcracked-jp. Whether inlining or a standalone base candidate is the better long-term form is a posting-procedure question; this package documents the form the port actually takes, and flags the wave title as broader than this file's diff.

### Wave edits, in the order they landed

1. **3205f27** (Stage 2 EN batch 1, creation): the whole port — credit block, inlined base, variant CSS in the live module. The original's tail self-import module was not carried over; until the frame arrived, the candidate's delivery rested on its own module CSS applying to its own page.
2. **f1138e4** (FIX-P4): interwiki-style frame added at the head (candidate L1–5); translator field SCP-JP → AI; Noto Sans JP @import added (L27); `"Noto Sans JP"` added to the header-title stack (L123). The frame's `theme=` names the candidate's own /1 delivery, the same delivery form the original's tail module imported for the EN page.
3. **9fbcd94** (FIX4-CREDIT): the T7 credit-CSS supplement appended (candidate L376–386, +12 lines), carried from the production base page's JP-localize rules.


### Post-package repairs (REFRESH3-D)

Recopy brought one post-package repair in: the candidate was built at `f1c2cd0`, before the 722ceb5 landing, and its `candidate.txt` still carried the dead frame parameter; the recopy removed exactly that line (8,216 → 8,136 bytes).

- **FIX-FRAMEADDR, sub-shape (B) — Introduced** (report `R/review-scout/FIX-FRAMEADDR.md` §2; landing `722ceb5c949172bb5185d51ef56ce4119ee4fa91`, 2026-11-17): the original carries no interwiki-style frame and no `theme=` self-address in that role; the porting wave introduced the frame with `theme=` naming its own draft-host `local--code/theme%3A3law-pride-jp/1`, a fragment the page does not carry (delivery is the inline `[[module CSS]]`). Remedy: the single `| theme=...` line was deleted; the frame include and its `priority=1` line are kept. Current candidate frame at L1.
- **Original evidence:** the original has no frame; its self-address is an `@import` at original L35 only (FIX-FRAMEADDR §2 worked table). No other repair touches this file.

Stamp treatment follows the jiha-jp / alexylva-university-jp precedents: the regenerated verdict stamp reads STALE, no re-judgement is fabricated, and the frozen GOSIGN2 ledger remains the verdict record.

## Change set outside the two diffed files

The diff covers two files; the port's record is larger. `pages/theme-decoration-sample-3law-pride-jp.txt` is the decoration sample the render checks ran against (its findings are the sample half of the render record). `pages-existing/existing:theme-3law.txt` is the production base page the T7 supplement was carried from (section 1); it is a record source, not a port output. The base theme:3law has no JP candidate file (see the per-theme record). There are no companion fragments and no inbound-link repairs in other candidates for this theme.
