# Review package — theme:construct-jp (CN → JP port)

<!-- BEGIN GENERATED VERDICT STAMP — do not hand-edit; regenerate with review/build_review.py -->
## Verdict stamp
- Theme: theme:construct-jp — origin CN, population #176 [GOSIGN2-LEDGER (b) row 176]
- Overall: STALE — candidate file changed since the verdict was computed (verdict against 435a6bb-era content, file sha256 now 226cdf3fdffb1a03eea4b5163234a47c5eb2e125577e795332f1c2a55a2d771b); verdict not carried over, re-judgement required
> verdicts below describe the pre-change file
- T1 (source check): FINDINGS (classified) — baseline 2026-11-16: exit 1, 1 error / 2 warns / 1 info (pseudo-ref×1); standing classes dispositioned in register c1 [T1-ROWS row 201; GOSIGN2-LEDGER (b) row 176]
- T2/T3 (render, combined verdict): FINDINGS — [combined T2/T3] report `FINDINGS` — page runtime-hotlink site-theme chain only; sample hidden-* cluster confined to webkit-1366, whose only hotlink host is http.cat = transient 503 capture, not a result; sample credit-modal (preview-form) + 884px@768 overflow. [RENDER-ROWS-2 (RENDER-S2-E (CN3))]
- Engine coverage: full matrix as run by the lane; coverage not separately caveated in the row [RENDER-ROWS-2 row]
- Credit modal: sample credit-modal errors dispositioned preview-form (credit:start-preview has no modal mechanism; GOSIGN-TESTS T2 amendment, 2026-11-16) [RENDER-ROWS-2 (RENDER-S2-E (CN3))]
- T4 (localize patterns + follow-up): FINDINGS — display-affecting findings: 2 [LOCALIZE-ROWS row 175, source LOCALIZE-S2-D]
- T5 (translation text): FINDINGS — the source reports judge T4/T5 jointly; one verdict word covers both [LOCALIZE-ROWS row 175]
- FIX5 re-judgement: none — no OPEN items at the ledger determination [GOSIGN2-LEDGER (b) row 176]
- Computed against: canonical commit b5cb7241f527a44933e45599b41df210690771c4; candidate file pages/theme:construct-jp.txt sha256:226cdf3fdffb1a03eea4b5163234a47c5eb2e125577e795332f1c2a55a2d771b; record: GOSIGN2-LEDGER.md + GOSIGN2-LEDGER-SUPPLEMENT.md as of the FIX5 head 435a6bb
<!-- END GENERATED VERDICT STAMP -->

## Status

| | |
|---|---|
| Verdict | **PASS** — passed at the ledger determination; this theme had no OPEN items and no §(e) register entry (GOSIGN2-LEDGER (b) row 176) |
| Standing items | **DISPOSITIONED** — T1 pseudo-ref ×1 (class (ii), section 11); the render row's items (KB-40 / KB-44 / KB-33+KB-34, section 11); T4's P10 and P11 (section 11). One defect is flagged in the per-theme record: the usage examples name a page that does not exist on scp-jp |
| Go-sign basis | COMPLETION-REPORT.md §10 (go-sign issued; 81 FIXED / 26 DISPOSITIONED / 0 OPEN across the sweep) |
| Named exception | None for this theme (the sweep's single named exception is theme:amethyst-v2, which has no candidate) |

## Provenance

| | Original | Candidate |
|---|---|---|
| Page | theme:construct | theme:construct-jp |
| Wiki | scp-wiki-cn.wikidot.com | SCP-JP Sigma-10 candidate (canonical repo) |
| Reference revision | 24 (first translation; the candidate's credit block records 初訳時参照リビジョン: 24) | — |
| Source of this copy | Mirror store, class COPY (hash-verified against review/sources.tsv) | Canonical file `pages/theme:construct-jp.txt`, copied at worktree HEAD 1605bbd |
| Lines / bytes | 1,739 lines / 79,236 bytes | 1,756 lines / 84,547 bytes |
| SHA-256 | 2a86e59c7c966c07bccf6dc7fc06a7cab511e2317fd70eb5294f2128f1268803 | c223b098ed525f2046a4a4ed386f88259cba9be8b9bddec5b9ff43917858ed7a |

Wave history: the candidate was created by the Stage 2 CN3 integration (commit 6a8eb9d) and last touched by FIX-CREDIT-D (commit 1869877, the translator-attribution normalization over all candidates). No FIX5 commit touches this file, because the theme had no OPEN items for FIX5 to re-judge.

## Summary

The largest port in this batch, and the one whose diff most needs adjudication: the change is a delivery reorder, not a rewrite. The CN original opens with its live CSS module (original L1–1245) and puts its documentation after it — prose, usage, and some twenty small exhibit snippets (original L1246–1739), with a bare Rate in the post-module furniture. The candidate inverts the page: frame, credit block, documentation and exhibits first (candidate L1–509), then the CSS carried once as a `[[code type="CSS"]]` exhibit inside a collapsible (candidate L510 to the file end), self-delivered through the head frame's own-code import — the same delivery form as the cmst package in this batch. Inside the moved CSS, the changes are exactly two classes: twenty blocks of CSS comment translation (the original's comments are porter-visible prose, translated in place) and seven font-stack rewrites giving the CJK stacks their JP faces. The diff's three tail blocks (B30–B32), which map the original's entire documentation span to three candidate lines, are the move's shadow, not deletions — the exhibit census of section 8 decides that. One item was flagged for repair in the per-theme record and has since been repaired by the population sweep: both usage examples (candidate L60, L64) named `:scp-jp:theme:construct`, a page that does not exist (probe evidence there), and now name `:scp-jp:theme:construct-jp`. Measured churn (diff.md, Tier 2: +541/−524, 1,065 changed lines in 32 change blocks / 26 diff sections; the bulk of both numbers is the moved CSS body).

## Class summary

Auto-classification by review/classify_hunks.py (signature table 2026-11-17.1): 32 change blocks — 30 specific (93.8%), 2 heuristic (6.3%), 0 residue, 0 skipped. Pattern citations below name the KB entry; the patterns/ tree state cited throughout is commit 9c5e9079afb01d30cb9fc4ef9d714e5591eb2ffa.

| Label | Blocks |
|---|---|
| DELIVERY-MOVE | 28 |
| COMMENT-TEXT | 20 |
| TRANS-UNANCHORED | 18 |
| FONTLOAD-CJK-STACK | 7 |
| TRANSLATION-ANCHORED | 4 |
| EXHIBIT-RESTRUCTURE | 3 |
| IFTAGS | 2 |
| CREDIT-PREVIEW | 1 |
| DRAFT-HOST | 1 |
| SELF-DELIVERY | 1 |
| TASL-FIELDS | 1 |
| CONTENT-STRING | 1 |
| BARE-RATE-DEL | 1 |

Adjudication for this README (every block was read against the bytes): DELIVERY-MOVE is the reorder of section 3 — the classifier's body matching pairs the original's module CSS with the candidate's code exhibit at high similarity, and the 28 blocks carrying the label are the frame (B1), the CSS-internal change blocks (B2–B29), and the tail (B30). The three EXHIBIT-RESTRUCTURE blocks (B30–B32) are the move's tail shadow, discharged by the census in section 8. The two heuristic blocks are among the comment translations. After adjudication no block is left unexplained, and there is no residue.

## Standing sections

### 0. Header and provenance frame

- **What:** Theme theme:construct-jp; original theme:construct on scp-wiki-cn at reference revision 24; candidate `pages/theme:construct-jp.txt`. Provenance route: derived from the original at the reference revision (sources.tsv kind: standard; no production JP counterpart, so the R4 adoption question does not arise). The candidate's frame (L1–7) heads the documentation; the original has no frame — it opens with the CSS module itself.
- **Why:** Section 0 declares the provenance route so every later count is read against the right baseline; the frame is P6/T3 (section 3).
- **Verify:** The sources.tsv row for construct-jp; `sha256sum original.txt` against the Provenance table.
- **Disposition:** Standing (the route itself).

### 1. Credit and attribution

- **What:** The candidate installs the preview credit block at candidate L37–46 with `:scp-jp:`-prefixed includes, carrying the eight ruling-3 fields: title 構成テーマ; 翻訳責任者 AI; 翻訳年 2026; 原題 构成 主题版式; 著作権者 Mr_J_AND; 作成年 2026; 初訳時参照リビジョン 24; the source link (candidate L45) naming scp-wiki-cn.wikidot.com, the original's recorded host. The original's bare `[[module rate]]`, which sat in its post-module furniture (B30's span), is deleted (BARE-RATE-DEL): the preview block is rate-bearing, and a kept Rate is the KB-09 duplicate. No T7 credit-module CSS supplement exists in this theme.
- **Why:** P3/T1 and ruling 3; KB-09 for the duplicate the deletion prevents.
- **Verify:** `grep -n 'module rate\|module Rate' candidate.txt` returns nothing; read candidate L37–46 against the eight fields.
- **Disposition:** FIXED (the ledger's class outcome for this sweep: credit fields FIXED by the credit waves; this file's last touch is FIX-CREDIT-D).

### 2. Includes and components

- **What:** The candidate's includes are the frame pair (section 3), the credit pair (section 1), and the exhibit buttons: two button includes in the documentation (candidate L83/L90) whose targets the port repoints from the original's internal-wiki addresses to the scp-jp top page and the campaign's sandbox (the localize lane's P11 item, section 11). The two escaped usage examples (candidate L60, L64) named `:scp-jp:theme:construct` as built — the original's slug, not this candidate's posting name, and the per-theme record's flagged defect, since repaired by the population sweep (both now name `:scp-jp:theme:construct-jp`); the second example adds the `bodybg=off` parameter.
- **Why:** P1 (KB-15) for live includes; P11 for the button targets; the usage examples under the campaign's settled rule (AGENTS.md §6: an install example must name the page a user can actually include).
- **Verify:** `grep -n '\[\[include' candidate.txt` — the frame, the credit pair, the two buttons, the two escaped examples.
- **Disposition:** Live includes applied; P11 DISPOSITIONED (section 11); the usage examples are flagged in the per-theme record (not edited here; the coordinator lands repairs).

### 3. Delivery and code loading

- **What:** The reorder described in the Summary (B1–B30). The original delivers through a live `[[module CSS]]` (original L1–1245) and documents afterwards. The candidate's head module (candidate L1–3) imports the page's own `local--code/theme%3Aconstruct-jp/1` from the draft host, the interwiki-style include (candidate L5–7) names the same /1 delivery, and the CSS sits in the `[[code type="CSS"]]` exhibit at candidate L510 (inside a collapsible, candidate L509) — code block 1, so the exhibit is the delivery. The theme needs no asset files: its header comment records that the header, logo, and background graphics are all embedded in the CSS, which is why this 1,700-line theme produces exactly one T1 pseudo-ref error (the frame import) where asset-heavy themes produce many.
- **Why:** P4/T9 (own-code delivery served from JP hosts) and P6/T3 (the frame). The draft-host form is KB-41, class (iii): sanctioned at draft stage, rewritten to the production host at posting.
- **Verify:** `grep -n 'local--code' candidate.txt` — candidate L2 and L7 only; `grep -n '\[\[module CSS\]\]' candidate.txt` returns nothing.
- **Disposition:** DISPOSITIONED (class (iii)).

### 4. Fonts and assets

- **What:** Fonts (P7): seven FONTLOAD-CJK-STACK blocks (B3, B6, B9–B11, B13, B18) rewrite the CJK font stacks inside the moved CSS, giving them their JP form — e.g. candidate L528: `"Noto Sans JP", "Noto Sans CJK JP", "Hiragino Kaku Gothic ProN", "Yu Gothic", Meiryo, Arial, sans-serif`. The original's stacks named the CN faces; the port's stacks lead with the JP faces while keeping the cross-platform fallbacks. No font @import is added: the theme loads no webfont on either side, and the JP faces are system/environment fonts. Assets: none — the theme embeds its graphics in CSS (section 3), so there are no image references to re-host; the single DRAFT-HOST label is the frame import itself.
- **Why:** P7/T5: a stack that can render Japanese leads with a JP face. The classifier's dedicated CJK-stack signature is what makes these seven blocks specific rather than CSS-BODY heuristic.
- **Verify:** `grep -n 'font-family' candidate.txt` — the rewritten stacks; compare against original.txt's.
- **Disposition:** Applied.

### 5. Header, sidebar, and site furniture

- **What:** The theme's site furniture is CSS-embedded graphics and header rules carried inside the moved CSS body, changed only by the section-4 stacks and section-6 comments. No header-variable override block exists as a separate change: the localize lane's terminology note (section 6) touches the theme's name strings, not its header variables. No P8 layout adaptation was needed.
- **Why:** P9/T6 engage through the name strings here; recording the shape is the check.
- **Verify:** `grep -n -- '--header-' candidate.txt` against original.txt — the variable sets match.
- **Disposition:** Standing.

### 6. Text translation

- **What:** Three layers. (a) The documentation prose and exhibits are translated throughout (the TRANS-UNANCHORED blocks inside B1's span and the tail blocks' counterparts). (b) In-CSS comments (R1): twenty COMMENT-TEXT blocks translate the original's CSS comments in place — the original's comments are substantive prose (design notes, the second part's header at candidate L1414–1420, which records that the Construct Blocks CSS was rewritten for this theme rather than ported), and they are porter-visible in the delivered code exhibit, so they are translated like body text; TAXONOMY is explicit that comment translation is not a defect pattern. (c) One CONTENT-STRING block (B20, candidate L1285–1286): the reader-visible footnote-hint string inside the CSS (KB-18). The localize lane's P10 item stands in the bytes as recorded: the theme's name is rendered 構成 in the credit title and some headings, コンストラクト in others (the lane cited candidate L318/L323/L512/L1415/L1420 against L38/L52/L445 at its reading) — a terminology variance between the translated name and the transliterated name, dispositioned at lane severity (section 11).
- **Why:** P10 for the prose; R1's rule that porter-visible comments are body text; KB-18 for the content string.
- **Verify:** `grep -n 'コンストラクト\|構成' candidate.txt` — both name forms, at the lane's cited places; spot-read candidate L511–513 (the CSS header comment) against original L2–4.
- **Disposition:** Standing (the port itself); P10 DISPOSITIONED (section 11).

### 7. Links

- **What:** The credit source link (candidate L45) names scp-wiki-cn.wikidot.com, the original's recorded host — the host check passes. The exhibit buttons of section 2 are includes, not links. No prose hub link needed a repoint: the documentation's references are the buttons and the credit link.
- **Why:** P11's link half is satisfied by the source link's correctness and the buttons' disposition.
- **Verify:** `grep -n 'wikidot.com' candidate.txt` — the source link only.
- **Disposition:** Standing; no dead link.

### 8. Structure

- **What:** The closing rule holds inside the CSS: selectors, rule order, and variable names are preserved through the move (the classifier's body matching pairs the two CSS bodies at the DELIVERY-MOVE similarity, and the internal change blocks are only sections 4 and 6). Exhibit census (R3), which discharges B30–B32: the original's documentation span (original L1246–1739) holds prose plus some twenty small `[[code]]` exhibit snippets; the candidate's documentation span (candidate L48–509) holds the same prose and the same snippets in the same order (the candidate's snippet blocks sit at L74, L88, L471, L496 and their fellows), and the candidate adds the one large exhibit the original did not have — the CSS itself, as the delivery exhibit of section 3. The only true deletions are the bare Rate (section 1) and the live module wrapper, both recorded. Nothing else was dropped, replaced, or merged.
- **Why:** R3 forces the census because a restructure and a deletion share a diff shape; here the diff's tail blocks are the census's whole point.
- **Verify:** Compare `grep -n '\[\[code' original.txt candidate.txt` (snippet counts in the documentation spans) and the CSS rule sequence in original L1–1245 against candidate L510–1755.
- **Disposition:** Standing; no structural deletion beyond the recorded furniture, no class I item.

### 9. Formatting only

- **What:** None — the classifier finds no whitespace-only block pair and no re-indentation (0 and 0). The line-count growth (1,739 → 1,756) is the frame and credit furniture of sections 1–3, not formatting churn.
- **Why:** Formatting churn is disclosed as its own class so it is never mistaken for a semantic change.
- **Verify:** The summary counts in classification.json (`reindent_blocks: 0`).
- **Disposition:** None required.

### 10. Porter annotations

- **What:** None added by the porter — the candidate carries no `[!-- ... --]` translator notes and no editor line (checked explicitly). The translated CSS comments of section 6 are the original's own comments in translation (R1), not annotations; the second part's header comment (candidate L1419–1420) is the original author's note, carried over.
- **Why:** R2: porter-added text is part of the change record; its absence is recorded so a reviewer does not have to wonder whether it was checked.
- **Verify:** `grep -n '\[!--' candidate.txt` returns nothing outside the original's own comment gates, if any; compare comment lines against original.txt.
- **Disposition:** Standing (checked, absent).

### 11. Dispositions and exceptions

- **What:** Three items, each with its ground. (1) T1's single pseudo-ref error: class (ii), posting-procedure — the frame's draft-host import (section 3); the theme's CSS-embedded graphics are why there is only one. (2) The render row's items, all environment or capture layer, not charged to the candidate: the page's runtime-hotlink site-theme chain (KB-40); the sample's hidden-* cluster failing on a webkit-1366 http.cat transient (KB-44); the sample's credit-modal errors and 884px@768 overflow (KB-32 preview form; KB-33/KB-34 cross-cutting families). (3) T4's two display-affecting items, both DISPOSITIONED in the ledger (GOSIGN2-LEDGER §(c3)): P11 (the exhibit buttons' internal-wiki targets — sibling/batch-posting class; the candidate's repointed targets stand as the lane left them) and P10 (the 構成/コンストラクト terminology variance — lane severity/specimen class; section 6). Separately, the usage examples of section 2 are flagged below as a defect the ledger did not record.
- **Why:** A disposition is a decision with grounds (AGENTS.md §3 classes (i)/(ii)/(iii); the named KB entries), not an omission.
- **Verify:** Each item names its deciding record above and in the verdict stamp.
- **Disposition:** DISPOSITIONED (items 1–3); the usage examples are flagged with evidence in the per-theme record.

### 12. Verification

- **What:** (a) T1 source check (T1-ROWS row 201): exit 1, 1 error / 2 warns / 1 info; the single error is pseudo-ref, class (ii); there is no class (i) error. (b) T2/T3 render (RENDER-ROWS-2, lane RENDER-S2-E (CN3)): FINDINGS, the items of section 11(2), all dispositioned; engine coverage full matrix as run by the lane. (c) T4/T5 (LOCALIZE-ROWS row 175): FINDINGS jointly, display-affecting findings 2 (P11 and P10, both dispositioned). (d) This package is self-verifying: `python3 review/build_review.py --check` regenerates diff.md and the verdict stamp from the two byte-faithful copies in this directory and compares. Counts in this README are the generator's (difflib, autojunk off): +541/−524 in 32 change blocks / 26 diff sections (Tier 2 format).
- **Why:** Verification claims name the cheapest deciding check and its result, not a general assurance.
- **Verify:** Re-run the checker on `pages/theme:construct-jp.txt` and `python3 review/build_review.py --check` in this repo.
- **Disposition:** PASS (GOSIGN2-LEDGER (b) row 176; go-sign, COMPLETION-REPORT §10).

## Per-theme record

### The usage examples name a page that does not exist (defect flag, repaired)

Both install examples name the original's slug on scp-jp: candidate L60 `@@[[include :scp-jp:theme:construct]]@@` and candidate L64 `@@[[include :scp-jp:theme:construct | bodybg=off]]@@`. Probe made for this package (2026-11-17): `https://scp-jp.wikidot.com/theme:construct` returns 404; the candidate posts to scp-jp under its own name, theme:construct-jp, so neither example can be followed on the site it instructs for. The campaign's settled rule (AGENTS.md §6) names this exact shape a finding: usage examples inside candidate docs naming `theme:<slug>` instead of `theme:<slug>-jp` break every copy-paste install. The localize lane did not record it, and the ledger's determination for this theme is PASS; this package carries the item as a flagged defect with its probe evidence, for the coordinator's repair wave. The candidate is documented as it stands; no byte of it was edited here. The repair has since landed: the usage-example population sweep (sweep report SWEEP-USAGE.md in the campaign record, R/review-scout/; canonical commit b5cb724), which repaired this shape across all 157 affected candidates; candidate L60 and L64 now name `:scp-jp:theme:construct-jp` (the second with its `bodybg=off` parameter unchanged), and this package documents the corrected candidate (its stamp reads STALE against the pre-repair verdict, by design).

## Change set outside the two diffed files

The diff covers two files; the port's record is two files larger. `pages/theme-decoration-sample-construct-jp.txt` is the decoration sample the render checks ran against (its findings are the sample half of section 11(2)); it belongs to this theme's record but carries no port change of its own to explain here. There are no companion fragments, no shared base file, and no inbound-link repairs in other candidates for this theme.
