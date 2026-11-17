# Review package — theme:aces-and-eights-jp (EN → JP port)

<!-- BEGIN GENERATED VERDICT STAMP — do not hand-edit; regenerate with review/build_review.py -->
## Verdict stamp
- Theme: theme:aces-and-eights-jp — origin EN, population #50 [GOSIGN2-LEDGER (b) row 50]
- Overall: STALE — candidate file changed since the verdict was computed (verdict against 435a6bb-era content, file sha256 now 9473b161d17a4e5bea131eda83ea5e6aa2359a4ae8f0f217896f56391a80c131); verdict not carried over, re-judgement required
> verdicts below describe the pre-change file
- T1 (source check): FINDINGS (classified) — baseline 2026-11-16: exit 1, 3 errors / 1 warn / 1 info (hotlink×3); standing classes dispositioned in register c1 [T1-ROWS row 50; GOSIGN2-LEDGER (b) row 50]
- T2/T3 (render, combined verdict): FINDINGS — [combined T2/T3] report `FINDINGS` — broken `background: url(null)` in candidate CSS (404 every combo of both pages, §3 dead declaration) + ACES wordmark clip at 320. [RENDER-ROWS-1 (RENDER-S2-A)]
- Engine coverage: full matrix as run by the lane; coverage not separately caveated in the row [RENDER-ROWS-1 row]
- Credit modal: no credit-modal line in this theme's row; no sample credit-modal error recorded [RENDER-ROWS-1 (RENDER-S2-A)]
- T4 (localize patterns + follow-up): FINDINGS — display-affecting findings: 1 [LOCALIZE-ROWS row 50, source LOCALIZE-S2-A]
- T5 (translation text): FINDINGS — the source reports judge T4/T5 jointly; one verdict word covers both [LOCALIZE-ROWS row 50]
- FIX5 re-judgement: none — no OPEN items at the ledger determination [GOSIGN2-LEDGER (b) row 50]
- Computed against: canonical commit 5d951775998e4a1eeccf8e8695a6518b328962ee; candidate file pages/theme:aces-and-eights-jp.txt sha256:9473b161d17a4e5bea131eda83ea5e6aa2359a4ae8f0f217896f56391a80c131; record: GOSIGN2-LEDGER.md + GOSIGN2-LEDGER-SUPPLEMENT.md as of the FIX5 head 435a6bb
<!-- END GENERATED VERDICT STAMP -->

## Status

| | |
|---|---|
| Verdict | **PASS** — passed at the ledger determination; no OPEN items and no §(e) register entry (GOSIGN2-LEDGER (b) row 50) |
| Wave history | Two commits touch the candidate: creation by the Stage 2 EN batch (3205f27) and one later commit, 1869877 (FIX-CREDIT-D), which carries every subsequent wave edit this file received — the frame, the JP font supplement, the translator field, and the dead-declaration removal the ledger attributes to FIX3-S2EN §5. The concentration is itself a finding; see the per-theme record |
| Standing items | **DISPOSITIONED** — T1 hotlink ×3 (class (ii), section 11); the header wordmark and subtitle kept in English (ruling 2 family, section 5). One credit-field item is **flagged**, not dispositioned by this package: the dropped co-author name (per-theme record) |
| Go-sign basis | COMPLETION-REPORT.md §10 (go-sign issued; 81 FIXED / 26 DISPOSITIONED / 0 OPEN across the sweep) |
| Named exception | None for this theme (the sweep's single named exception is theme:amethyst-v2, which has no candidate) |

## Provenance

| | Original | Candidate |
|---|---|---|
| Page | theme:aces-and-eights | theme:aces-and-eights-jp |
| Wiki | scp-wiki.wikidot.com | SCP-JP Sigma-10 candidate (canonical repo) |
| Reference revision | 26 (first translation; the candidate's credit block records 初訳時参照リビジョン: 26) | — |
| Source of this copy | Campaign cache `gosign2-lanes/lane-oc-gs-localize-s2-A/orig-aces-and-eights.txt`, via the mirror store (class COPY, hash-verified against review/sources.tsv) | Canonical file `pages/theme:aces-and-eights-jp.txt`, copied at worktree HEAD 1605bbd; the file's last content change is commit 1869877 (FIX-CREDIT-D) |
| Lines / bytes | 228 lines / 4,762 bytes (the last line carries no trailing newline, so `wc -l` reports 227) | 231 lines / 5,131 bytes |
| SHA-256 | eebce8a7669023b3df948fc8b8340c493762f4de9e496fff7e6a0b62114fe208 | 13cbd176aa385e5a491b34b0f5fbff3cd7fe954a7e1af8364aab246ef3d16e27 |

## Summary

This is the near-parity end of class U: the candidate is the original's page with its delivery re-pointed, its credit furniture swapped, its prose translated, and one wave commit's worth of repairs. The original already had the modern shape — a self-import module, an interwiki-style frame in EN form, a bare Rate, and its CSS in a `[[code]]` exhibit. The port re-created that shape on the JP side: the frame names the candidate's own draft-host delivery, the exhibit's CSS became the live module CSS, the Playfair Display import moved from fonts.bunny.net to fonts.googleapis.com, and the credit block took the JP preview form. The wave commit 1869877 then added the JP font load and stacks, normalized the translator field, and removed the original's dead `background: url(null)` declaration, the one candidate-inherent render defect the sweep found in this theme. Measured churn (diff.md, the generator's difflib count with autojunk off: +36/−33 in 17 classifier change blocks; a GNU-diff count gives +27/−24 — alignment choice, not content). Two records in the ledger do not match the bytes and are flagged rather than repeated: the wave attribution of this file's fixes (per-theme record, item 1) and the credit holder field (item 2).

## Class summary

Auto-classification by review/classify_hunks.py (signature table 2026-11-17.1): 17 change blocks — 15 specific (88.2%), 1 heuristic (5.9%), 1 residue (5.9%), 0 skipped. Pattern citations below name the KB entry; the patterns/ tree state cited throughout is commit 9c5e9079afb01d30cb9fc4ef9d714e5591eb2ffa.

| Label | Blocks |
|---|---|
| DELIVERY-MOVE | 8 |
| TRANS-UNANCHORED | 4 |
| JPFONT-STACK | 3 |
| EXHIBIT-RESTRUCTURE | 2 |
| IFTAGS | 2 |
| SELF-DELIVERY | 2 |
| WS-ONLY | 2 |
| BARE-RATE-DEL | 1 |
| CREDIT-PREVIEW | 1 |
| CREDIT-PROSE | 1 |
| DELIVERY-HOST | 1 |
| DRAFT-HOST | 1 |
| FONT-IMPORT | 1 |
| INCLUDE-REPOINT | 1 |
| JPFONT-LOAD | 1 |
| TASL-FIELDS | 1 |

Adjudication for this README (every block was read against the bytes): the eight DELIVERY-MOVE primaries are the exhibit-to-module relocation of the CSS body (section 3), inside which the font blocks (B9–B14) classify separately. The one heuristic block (B6) and the one residue block (B7) are the prose pair at original L17–19: together they are the intro translation and the usage/base restatement (candidate L19–23), adjudicated in section 6. The two EXHIBIT-RESTRUCTURE primaries (B1, B8) are the head frame swap and the exhibit opening, not exhibit content changes; the exhibit census is in section 8. After adjudication no block is left unexplained.

## Standing sections

### 0. Header and provenance frame

- **What:** Theme theme:aces-and-eights-jp; original theme:aces-and-eights on scp-wiki at reference revision 26; candidate `pages/theme:aces-and-eights-jp.txt`. Provenance route: derived from the original at the reference revision by the Stage 2 EN batch (commit 3205f27); no production JP counterpart exists for this theme, so the R4 adoption question does not arise. The frame moved one step: the original opens with its self-import module and then its EN interwiki-style include; the candidate opens with the JP frame (candidate L1–4) and drops the separate self-import module, because the frame's `theme=` names the same own-code delivery.
- **Why:** Section 0 declares the route so later counts are read against the right baseline; the gate's tag is P2, the frame is P6/T3 (section 3).
- **Verify:** The sources.tsv row for aces-and-eights-jp; `sha256sum original.txt` against the Provenance table.
- **Disposition:** Standing (the route itself).

### 1. Credit and attribution

- **What:** The original's credit furniture is a bare `[[module Rate]]` (original L14–16) plus the CSS header comment (original L23–32) naming "rounderhouse, with help from Uncle Nicolini". The candidate deletes the Rate (block B5) and installs the JP preview credit block (candidate L8–17) with the eight ruling-3 fields (title エースとエイト・テーマ; 翻訳責任者 AI; 翻訳年 2026; 原題 Aces and Eights Theme; 著作権者 Rounderhouse; 作成年 2018; 初訳時参照リビジョン 26; the source link, host-verified in section 7). The translator field took its ruling-3 form in 1869877 (SCP-JP → AI). The CSS header comment is carried verbatim (candidate L28–34), so Nicolini's name survives in the candidate — in the comment, not in the credit block. The LOCALIZE row charged exactly that gap (pattern 3: the holder field drops Uncle Nicolini), and the ledger §(c3) line closes the row's P3 as "FIXED (credit waves; checker-verified)"; the bytes show the credit waves' only credit-block edit to this file is the translator field. The discrepancy is flagged in the per-theme record; this package does not re-open the PASS determination, and it does not repeat the FIXED claim for the holder field either.
- **Why:** P3/T1 (the preview credit module is rate-bearing, so the bare Rate is deleted, KB-09); ruling 3 fixes the eight fields and the translator form. The checker verifies the fields' presence and form, which is what "checker-verified" can honestly cover; a holder-field content addition is a different act, and no commit performs it.
- **Verify:** `grep -n 'module Rate' candidate.txt` returns nothing; `grep -n 'Nicolini' candidate.txt` returns exactly one hit, candidate L31, inside the CSS comment; read candidate L8–17 against the eight fields.
- **Disposition:** The block swap and translator field are FIXED (1869877). The holder-field item is **flagged** with evidence in the per-theme record. No license box exists on either side, so the T4/KB-63 question does not arise. This theme has no T7 credit-CSS supplement and none was needed: the candidate carries no credit-module rules and the production-counterpart defect shape recorded for other themes does not apply (no production counterpart exists).

### 2. Includes and components

- **What:** Candidate includes: the frame (candidate L1), the credit pair (L8/L17), and no others. The original's one include is its EN interwiki-style frame (`:scp-wiki:component:interwiki-style`, original L5–8), repointed in kind to the JP component with the delivery URL rewritten (section 3) — the classifier's INCLUDE-REPOINT block (B1). The usage exhibit's include line is restated as the candidate's own (`theme:aces-and-eights-jp`, candidate L21). No foreign include survives; no component port was needed alongside (ruling 4 not engaged).
- **Why:** P1 (KB-15): an include must name the JP counterpart that exists on scp-jp; the frame component's JP form is the campaign standard.
- **Verify:** `grep -n '\[\[include' candidate.txt` — three includes, all `:scp-jp:`.
- **Disposition:** Applied; no foreign include kept, no named exception needed.

### 3. Delivery and code loading

- **What:** The original delivers its CSS two ways at once: a head `[[module CSS]]` importing its own `local--code/theme%3Aaces-and-eights/1` from scp-wiki.wdfiles.com (original L1–3), and the EN interwiki-style frame at priority 1 naming the same delivery (original L5–8); the CSS text itself sits in a `[[code]]` exhibit (original L21–226). The candidate delivers once: the JP frame at candidate L1–4, priority 1, `theme=` naming the candidate's own `local--code/theme%3Aaces-and-eights-jp/1` on the draft host; the CSS text moved from the exhibit into the live `[[module CSS]]` (candidate L25–229), which is what the classifier's eight DELIVERY-MOVE blocks measure. The frame arrived in 1869877 — before that commit the candidate still carried the creation form (self-import head module in JP form). The Playfair Display SC import inside the CSS moved hosts at creation: fonts.bunny.net (original L31) → fonts.googleapis.com (candidate L36).
- **Why:** P4/T9 (own-code delivery from JP-side hosts) and P6/T3 (the interwiki-style frame, priority 1 for the theme's own layer). The bunny.net → googleapis move is the P5/KB-17 host rule (Google Fonts is an allowed hotlink host; bunny.net is not in the allowed set). The frame's draft-host URL is KB-41, class (iii), rewritten to the production host at posting.
- **Verify:** `grep -n 'local--code\|bunny' candidate.txt` — the frame line only, and no bunny.net anywhere; compare original L1–8 against candidate L1–4.
- **Disposition:** DISPOSITIONED (the draft-host frame line, class (iii)); the delivery shape itself is applied and standing.

### 4. Fonts and assets

- **What:** Font load: candidate L27 adds the Google Fonts Noto Sans JP @import at the head of the module (1869877), and the same commit adds `"Noto Sans JP"` to the three stacks that render the theme's display text — the two header `content:` rules and the h1 rule (candidate L83, L95, L171), each keeping `'Playfair Display SC'` first. The Playfair import itself is section 3's host move. Assets: three image URLs stay on scp-wiki.wdfiles.com — `chip.png` (candidate L49), `paper.jpg` (L69), `header.png` (L79), all `local--files/theme%3Aaces-and-eights/` — and these three lines are the T1 checker's hotlink ×3, matching the LOCALIZE row's pattern-5 charge (原語サイト local--files 直リンク3件) one for one.
- **Why:** P7/T5 with KB-16 (the font load gap): the LOCALIZE row charged "no Japanese font"; the fix is the import plus the stacks that render Japanese-bearing text, arrived in 1869877 (the ledger §(c3) names it "P7 FIXED (font wave)"; the commit that carries it is FIX-CREDIT-D — see the per-theme record). P5 with KB-17: the three EN-host images are posting-procedure re-hosting, class (ii) / KB-58, per the §(c3) outcome ("P5 DISPOSITIONED (class (ii) / KB-58)").
- **Verify:** `grep -n 'Noto Sans JP' candidate.txt` — the import is the `family=Noto+Sans+JP` URL at L27; the three stacks at L83, L95, L171. `grep -n 'wdfiles' candidate.txt` — the frame line plus the three class (ii) image lines.
- **Disposition:** Font supplement applied (1869877); the three EN-host image lines DISPOSITIONED (class (ii) / KB-58).

### 5. Header, sidebar, and site furniture

- **What:** No header variable is overridden. The header's design strings stay in English: `content: "Aces and Eights"` (candidate L84) and `content: "Astounding Tales: Fresh from the west!"` (L96) — the LOCALIZE row's T5 charge (ヘッダー副題英語のまま, the header subtitle left in English). The render row's second item is the ACES wordmark clip at 320, recorded inside the row's [FIXED] bracket (section 12).
- **Why:** The subtitle is the theme's masthead design text; the campaign's standing answer to header-language charges is ruling 2 (header and title language is out of scope for migration correctness), applied to this row's sibling charges in §(c3) — this row's §(c3) line does not name the T5 item separately, and this package records the ruling-2 ground as the class outcome rather than as a per-theme line, which is the honest strength of the evidence. The wordmark clip is the KB-35 narrow-width family; its FIXED bracket rests on the url(null) removal named in the same ledger sentence, and no geometry edit exists in this file's history (both facts stated in section 12).
- **Verify:** `grep -n 'content:' candidate.txt` for the two strings; the render record is RENDER-ROWS-1 (RENDER-S2-A (EN2)).
- **Disposition:** DISPOSITIONED (ruling 2 family for the strings); the clip's status is the ledger's, recorded with its basis in section 12.

### 6. Text translation

- **What:** The prose is translated in full: the intro (original L17 → candidate L19, one line: 西部劇とギャンブルをモチーフにしたテーマです), the usage line (candidate L21, with the 使い方 label), and the base declaration the candidate adds (**基盤:** 単体, candidate L23 — the original has no base line because its usage text carried the fact). The classifier's heuristic B6 and residue B7 are this prose zone (original L17–19): B6 is the intro line, B7 pairs the original's usage exhibit line with the candidate's base line, an alignment artefact of the prose restatement; both are adjudicated here, not in the appendix. The CSS header comment stays in English (porter-visible only), including its license line. R5 glyph-form conversion: none (English source). The LOCALIZE row records "翻訳自体の質（訳出文）は問題なし" — the translation's quality was not charged.
- **Why:** P10 for the prose; KB-18 for reader-visible strings. The unanchored/residue pair is where a silent deletion would hide, which is why both blocks were read individually.
- **Verify:** Read candidate L19–23 against original L17–19; the pairs are diff.md's first body sections.
- **Disposition:** Standing (the port itself).

### 7. Links

- **What:** The candidate's one live outbound link is the credit block's source link (candidate L16): `[*https://scp-wiki.wikidot.com/theme:aces-and-eights ソース]`. Its host is the original's recorded host in review/sources.tsv (scp-wiki.wikidot.com), so the jiha-class defect does not arise and no probe was needed. One prose link of the original disappears in translation: the intro's `[[[aces-and-eights|Aces and Eights]]]` canon link (original L17) has no counterpart in the candidate's compressed intro, and no JP counterpart page is named in the file. The CSS comment's Noun Project URL (candidate L33) is a license attribution line carried verbatim, not a navigation link.
- **Why:** P11, under the dead-reference evidence standard: links take the JP counterpart or the serving original; the canon hub has no recorded JP counterpart, and the port chose compression over an unverified repoint.
- **Verify:** `grep -n 'wikidot.com' candidate.txt` — the source link is the only hit.
- **Disposition:** Standing; the dropped canon link is recorded, not hidden.

### 8. Structure

- **What:** The localize.md closing rule holds: variable names, selectors, and the CSS's internal order are preserved (the body moved from exhibit to live module without reordering — the DELIVERY-MOVE blocks pair original and candidate lines one to one across the whole body), and the JP corrections arrive at the edges (frame before, font import at the module head, the dead declaration removed in place). The classifier's two EXHIBIT-RESTRUCTURE primaries adjudicate as: B1 is the head zone (frame swap plus credit), B8 is the exhibit opening line pairing with the module opening — the exhibit census decides: the original has one `[[code]]` exhibit holding the whole CSS; the candidate has no code exhibit, and the same CSS is its live module. Nothing was dropped or replaced; the exhibit's *status* changed, which is the delivery decision of section 3.
- **Why:** R3 forces this adjudication because a restructure and a deletion share a diff shape; here the census, not the label, decides.
- **Verify:** Compare `grep -n '\[\[code\|\[\[module' original.txt candidate.txt` and the one-to-one line pairing in diff.md.
- **Disposition:** Standing; no structural deletion, no class I item.

### 9. Formatting only

- **What:** Two WS-ONLY blocks (B15, B16), single blank-line/whitespace differences inside the CSS body. The classifier finds no re-indentation (0 blocks pair up after leading-whitespace normalization), so the R7 hazard is not triggered.
- **Why:** Formatting churn is disclosed as its own class so it is never mistaken for a semantic change.
- **Verify:** Blocks B15 and B16 in classification.json.
- **Disposition:** None required.

### 10. Porter annotations

- **What:** None. The candidate carries no `[!-- --]` translator notes, no editor lines, and no porter comments; a direct scan for annotation forms returns nothing. The skeleton's "none" for this section survives contact with the bytes, with the ground stated: the only added text is the credit block, the frame, and the 基盤 line, all counted in their own sections.
- **Why:** R2: porter-added text is part of the change record; here the record is that there is none.
- **Verify:** `grep -n '\[!--\|訳注\|Edited for\|JP localize' candidate.txt` returns nothing.
- **Disposition:** Standing (none, with the ground stated).

### 11. Dispositions and exceptions

- **What:** Three items. (1) T1's three hotlink errors: class (ii), posting-procedure — the three image URLs on scp-wiki.wdfiles.com (section 4). (2) The header subtitle and wordmark strings kept in English: ruling 2 family (section 5). (3) The credit holder field: **not** dispositioned here — it is flagged in the per-theme record, because the ledger's closure language and the bytes disagree and a disposition must rest on grounds a reviewer can re-derive.
- **Why:** A disposition is a decision with grounds (AGENTS.md §3 classes (i)/(ii)/(iii); the named KB entries), not an omission; item 3 is carried openly precisely because it does not meet that standard yet.
- **Verify:** Each item names its deciding record above or in the per-theme record.
- **Disposition:** DISPOSITIONED (items 1–2); item 3 flagged with evidence.

### 12. Verification

- **What:** (a) T1 source check (T1-ROWS row 50): exit 1, 3 errors / 1 warn / 1 info; all three errors are hotlink, class (ii); there is no class (i) error. (b) T2/T3 render (RENDER-ROWS-1, lane RENDER-S2-A (EN2)): the row's single item is bracketed [FIXED] — "broken `background: url(null)` in candidate CSS (404 every combo of both pages, §3 dead declaration) + ACES wordmark clip at 320" — with the fix named as "FIX3-S2EN section 5: the dead `background: url(null)` declaration was removed". The bytes bear the removal out: the original's `#header{ background: url(null) }` (original L34–36) is `#header{}` in the candidate (L39), and `grep -n 'url(null)' candidate.txt` returns nothing. The removal's commit is 1869877, not a FIX3 commit (per-theme record, item 1). (c) T4/T5 (LOCALIZE-ROWS row 50): FINDINGS jointly, display-affecting findings 1; the ledger §(c3) line closes P3 FIXED, P5 DISPOSITIONED, P6 FIXED, P7 FIXED. (d) This package is self-verifying: `python3 review/build_review.py --check` regenerates diff.md and the verdict stamp from the two byte-faithful copies in this directory and compares. Counts in this README are the generator's (difflib, autojunk off): +36/−33 in 17 change blocks; the GNU-diff count is +27/−24, alignment choice, not content.
- **Why:** Verification claims name the cheapest deciding check and its result, not a general assurance.
- **Verify:** Re-run the checker on `pages/theme:aces-and-eights-jp.txt`, the greps above, and `python3 review/build_review.py --check` in this repo.
- **Disposition:** PASS (GOSIGN2-LEDGER (b) row 50; go-sign, COMPLETION-REPORT §10).

## Per-theme record

### Item 1 — one commit wearing four wave names

The ledger distributes this file's repairs across four names: FIX3-S2EN §5 (the url(null) removal, §(c2)), the credit waves (P3, §(c3)), the frame waves (P6, §(c3)), and the font wave (P7, §(c3)). The file's git history has exactly two commits: creation (3205f27) and 1869877, whose message names it FIX-CREDIT-D (translator attribution normalization). That one commit's diff contains all of it: the frame addition (its first hunk), the translator field (second hunk), the Noto Sans JP @import (third), the `#header{ background: url(null) }` → `#header{}` removal (fourth), and the three stack additions. The likely history is that the FIX-CREDIT-D lane executed several wave families in one pass over this file; the ledger's per-pattern closure lines then recorded the outcomes under each pattern's own wave name. Nothing about the outcomes is wrong — every claimed edit is in the bytes — but a reviewer tracing any one of them by wave name will not find it. This package therefore cites the commit, and flags the wave-name layer as attribution prose, not as a per-file record.

### Item 2 — the holder field and Uncle Nicolini

LOCALIZE-ROWS row 50 charges: クレジット著作権者から Uncle Nicolini 欠落 (the credit holder field drops Uncle Nicolini, pattern 3). The original's CSS comment credits "rounderhouse, with help from Uncle Nicolini" — Nicolini as a helper, not the author of record; the page's authorship is Rounderhouse's. The candidate's credit block names Rounderhouse alone (candidate L13), and no commit adds Nicolini to the field; the credit waves' edit to this file is the translator field only. The ledger §(c3) line closes the row's P3 as FIXED (credit waves; checker-verified). The two records can be reconciled only by reading "FIXED" as covering the eight fields' presence and form, which is what the checker verifies — the holder field was already present and well-formed at creation, with the value the port chose. Whether the value should also name the helper is a credit-content judgment the campaign record does not argue anywhere for this theme (for theme:alexylva-university-jp the same lane charged Nicolini as 原作者, original author, a different relation). This package flags the gap with its evidence and leaves the determination where the ledger put it: PASS, with the flag on record for any future credit-content pass. The credit-content repair has since landed (canonical commit 2437825): the field now reads Rounderhouse & Uncle Nicolini, and this package documents the corrected candidate (its stamp reads STALE against the pre-repair verdict).

### Post-package repairs (REFRESH3-E)

The items above describe this package as built. The repair recorded below postdates the package; `candidate.txt` has been recopied from the current canonical `pages/theme:aces-and-eights-jp.txt` and `diff.md` and the verdict stamp regenerated with `python3 review/build_review.py`, so this package now documents the post-repair candidate. The regenerated stamp reads **STALE** by design: no re-judgement is fabricated here, and the frozen ledger (`GOSIGN2-LEDGER.md` + supplement, FIX5 head 435a6bb) remains the verdict record.

**FIX-FRAMED — frame sub-shape (D) treated as (B), own-address pointer dropped (landing 5d95177).** `FIX-FRAMED.md` records this theme's frame as sub-shape (D): the frame's `theme=` named the theme's own code block (/1) on the draft host, but the candidate carries no `[[code]]` block in any form (its CSS is live `[[module CSS]]`), so the named block does not exist — a dead pointer, verified in the report. The original's once-live form: its head module @import (L2) and frame (L7) name its own /1; block 1, `[[code type="css"]]` L21–226, banner "Aces and Eights Theme". The coordinator's ruling treats (D) as (B) and applies the minimal remedy: drop the single `| theme=https://sigma10-jp-test.wdfiles.com/local--code/theme%3Aaces-and-eights-jp/1` line, keep the `[[include :scp-jp:component:interwiki-style]]` frame, its priority, and every other byte unchanged. Commit 5d95177 deleted exactly that one line at candidate L3. The checker finding set is unchanged (3 errors / 0 warn / 1 info before and after; the dropped line was not a class (i) finding), as tabulated in FIX-FRAMED.md.

## Change set outside the two diffed files

The diff covers two files; the port's record is one file larger. `pages/theme-decoration-sample-aces-and-eights-jp.txt` is the decoration sample the render checks ran against (the render row's "both pages" phrasing refers to the candidate and this sample). There are no companion fragments, no shared base file (the candidate declares 基盤: 単体, standalone), and no inbound-link repairs in other candidates for this theme.
