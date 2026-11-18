# Review package — theme:unusual-cargo-jp (EN → JP port)
New to this package's shorthand? Read the notation key first: [How to read a review package](../HOW-TO-READ.md).

<!-- BEGIN GENERATED VERDICT STAMP — do not hand-edit; regenerate with review/build_review.py -->
## Verdict stamp
- Theme: theme:unusual-cargo-jp — origin EN, population #154 [GOSIGN2-LEDGER (b) row 154]
- Overall: PASS — passed at the ledger determination; no OPEN items [GOSIGN2-LEDGER (b) row 154]
- T1 (source check): FINDINGS (classified) — baseline 2026-11-16: exit 1, 16 errors / 0 warns / 1 info (pseudo-ref×16); standing classes dispositioned in register c1 [T1-ROWS row 139; GOSIGN2-LEDGER (b) row 154]
- T2/T3 (render, combined verdict): FINDINGS — [combined T2/T3] report `FINDINGS` — page-overflow 344–349px@320 (page) and 344–349px@320 + 884px@768 (sample); sample credit-modal (preview-form). [RENDER-ROWS-2 (RENDER-S2-D (EN22))]
- Engine coverage: full matrix as run by the lane; coverage not separately caveated in the row [RENDER-ROWS-2 row]
- Credit modal: sample credit-modal errors dispositioned preview-form (credit:start-preview has no modal mechanism; GOSIGN-TESTS T2 amendment, 2026-11-16) [RENDER-ROWS-2 (RENDER-S2-D (EN22))]
- T4 (localize patterns + follow-up): FINDINGS — display-affecting findings: 1 [LOCALIZE-ROWS row 154, source LOCALIZE-S2-C]
- T5 (translation text): FINDINGS — the source reports judge T4/T5 jointly; one verdict word covers both [LOCALIZE-ROWS row 154]
- FIX5 re-judgement: none — no OPEN items at the ledger determination [GOSIGN2-LEDGER (b) row 154]
- Computed against: canonical commit 666f54356acb463c56016c967dc52464b25ba4a2; candidate file pages/theme:unusual-cargo-jp.txt sha256:755325ecebd48c580111b0c426504c9932dd419a156b096cc10f6dea05ed048c; record: GOSIGN2-LEDGER.md + GOSIGN2-LEDGER-SUPPLEMENT.md as of the FIX5 head 435a6bb
<!-- END GENERATED VERDICT STAMP -->

## Status

| | |
|---|---|
| Verdict | **PASS** — passed at the ledger determination; this theme had no OPEN items and no §(e) register entry (GOSIGN2-LEDGER (b) row 154) |
| Standing items | **DISPOSITIONED** — T1 pseudo-ref ×16 (class (ii), section 11); the render row's items (page and sample overflow at 320 and 768, KB-33/KB-34; credit-modal preview form, KB-32); T4's charges (P1 bare forms, posting-procedure class; P3 credit fields, FIXED; P7 Yu Mincho stacks, dispositioned without a display-affecting mark). The verdict stamp reads PASS, not STALE: the candidate has not changed since the FIX2-CREDIT commit the stamp was computed against |
| Go-sign basis | COMPLETION-REPORT.md §10 (go-sign issued; 81 FIXED / 26 DISPOSITIONED / 0 OPEN across the sweep) |
| Named exception | None for this theme (the sweep's single named exception is theme:amethyst-v2, which has no candidate) |

## Provenance

| | Original | Candidate |
|---|---|---|
| Page | theme:unusual-cargo | theme:unusual-cargo-jp |
| Wiki | scp-wiki.wikidot.com | SCP-JP Sigma-10 candidate (canonical repo) |
| Reference revision | 83 (first translation; the candidate's credit block records 初訳時参照リビジョン: 83) | — |
| Source of this copy | Campaign cache `gosign2-lanes/lane-oc-gs-localize-s2-C/orig-unusual-cargo.txt`, via the mirror store (class COPY, hash-verified against review/sources.tsv) | Canonical file `pages/theme:unusual-cargo-jp.txt`, copied at worktree HEAD e907bdd |
| Lines / bytes | 546 lines / 13,068 bytes | 558 lines / 15,056 bytes |
| SHA-256 | 74674ea24c16fa579982bb89f5b2be77811d12273b324bbbb3f92d78a1409020 | 755325ecebd48c580111b0c426504c9932dd419a156b096cc10f6dea05ed048c |

Wave history: the candidate was created by the Stage 2 EN22 integration (6fa35a9, the LOCALIZE-S2-C wave's port) and touched once since, by FIX2-CREDIT (666f543). The usage-example sweep did not touch this file: its self-references already stand in the forms the sweep leaves alone (section 2), which is also why the verdict stamp is fresh rather than STALE.

## Summary

A commission-themed EN port whose interest is concentrated in its CSS: the documentation translation is routine, but the code block carries four silent validity repairs the reviewer should know about — most consequentially, the original's `#side-bar: target.close-menu` (with a space) parses as a descendant selector and never matched the sidebar it was written for; the candidate's `#side-bar:target.close-menu` is the rule the original meant to ship. The rest is the standard classes done completely: head-module delivery repointed with a frame added, the bare Rate replaced by a preview credit block whose remix attribution (three source themes, three authors) is carried in both the prose and the banner, the font import moved from bunny to Google Fonts in its original v1 API form, a system Mincho inserted into the stacks, the header's ceremonial strings localized, and the theme's images consolidated into its own draft folder — including one image the original served from a *different page's* folder, and two asset URLs whose original folder name is case-inconsistent in the original itself. Measured churn (the generator's difflib count, autojunk off): +201/−195, 396 changed lines in 107 change blocks / 15 diff sections; a GNU-diff count gives 308 changed lines (+160/−148). No item in this package is flagged beyond the ledger's record; the repairs are disclosed in the per-theme record because two of them change rendering.

## Class summary

Auto-classification by review/classify_hunks.py (signature table 2026-11-17.1): 107 change blocks — 49 specific (45.8%), 54 heuristic (50.5%), 4 residue (3.7%), 0 skipped. Pattern citations below name the KB entry; the patterns/ tree state cited throughout is commit 9c5e9079afb01d30cb9fc4ef9d714e5591eb2ffa.

| Label | Blocks |
|---|---|
| TRANS-UNANCHORED | 46 |
| TRANSLATION-ANCHORED | 24 |
| COMMENT-TEXT | 21 |
| DRAFT-HOST | 17 |
| CSS-BODY | 10 |
| WS-ONLY | 7 |
| CONTENT-STRING | 3 |
| IFTAGS | 2 |
| SELF-DELIVERY | 2 |
| BARE-RATE-DEL | 1 |
| COMPONENT-SWAP | 1 |
| CREDIT-PREVIEW | 1 |
| DELIVERY-HOST | 1 |
| FONT-IMPORT | 1 |
| INCLUDE-REPOINT | 1 |
| TASL-FIELDS | 1 |

Adjudication of the heuristic mass: the 54 heuristic blocks are documentation and exhibit translations (46 unanchored blocks across tiers), CSS comment translations (COMMENT-TEXT ×21), and the CSS-BODY blocks — of which the font-stack insertions adjudicate to section 4 (P7) and the validity repairs to the per-theme record. No EXHIBIT-RESTRUCTURE label fires for this pair at all, and the census (section 8) agrees. The four residue blocks (three one-word comment/heading translations; one added blank line) are in the appendix.

## Standing sections

### 0. Header and provenance frame

- **What:** Theme theme:unusual-cargo-jp; original theme:unusual-cargo on scp-wiki at reference revision 83; candidate `pages/theme:unusual-cargo-jp.txt`. Provenance route: derived from the original at the reference revision by the LOCALIZE-S2-C wave (sources.tsv kind: standard). Topology frame: the original delivers from the head — a module importing its own code block from `scp-wiki.wdfiles.com/theme:unusual-cargo/code/1` — and the candidate keeps the head module and adds the frame beside it (section 3). The gate's tag is localized (`+theme` → `+テーマ`, IFTAGS ×2).
- **Why:** Section 0 declares the route and frame; the gate tag is P2.
- **Verify:** The sources.tsv row for unusual-cargo-jp; `sha256sum original.txt` against the Provenance table.
- **Disposition:** Standing (the route itself).

### 1. Credit and attribution

- **What:** The original's bare `[[module Rate]]` is deleted (BARE-RATE-DEL) and the preview credit block is installed in the campaign's bare form (candidate L12/L21). The eight ruling-3 fields include 著作権者 `[[*user CityToast]]` and 元記事リンク naming scp-wiki.wikidot.com — the host sources.tsv records for the original, so the host check passes with no probe needed. This theme is a remix, and its attribution is the fullest in the batch: the prose (candidate ~L29) and the code banner both carry, in translation, the three source works and their authors — the Aces and Eights Theme by rounderhouse, the SCP Sigma 9 Theme by Aelanna and Dr Devan, the MC&D Theme by Randomini. T4's row charged this block with a pattern-3 item （翻訳責任者/翻訳年 fields missing when the row was written); the current bytes answer it — both fields stand at candidate L14–15 — because the credit waves fixed the block after the row was written, and the ledger records P3 FIXED.
- **Why:** P3/T1 and ruling 3; the field-versus-banner check passes in both directions (the field names the theme's author; the remix lines live in prose and banner on both sides). The bare credit form is P1's class (ii), charged by T4's row as pattern 1 with the note "convention, display-neutral; deps exist on scp-jp".
- **Verify:** Read candidate L12–21; `grep -n '翻訳責任者\|翻訳年' candidate.txt` for the two once-missing fields.
- **Disposition:** FIXED (GOSIGN2-LEDGER §(c3): P3 FIXED; P1 DISPOSITIONED, posting-procedure class).

### 2. Includes and components

- **What:** Live includes: the credit pair (section 1, bare form), the head interwiki-style frame (candidate L5, bare form), and the exhibit image-block include (INCLUDE-REPOINT, its `name=` repointed with the assets of section 4). The escaped usage example (candidate L35) names the theme in plain same-wiki form, `@@[[include theme:unusual-cargo-jp]]@@`, which resolves to the candidate's own page on the posting wiki. Together with the delivery lines, these bare forms are exactly what T1's sixteen pseudo-ref errors count — the batch's highest count, and entirely class (ii): every one is a posting-procedure form, not a broken reference.
- **Why:** P1 (KB-15): the includes name the JP counterpart or resolve on the posting wiki; no foreign include is kept.
- **Verify:** `grep -n '\[\[include' candidate.txt` — the full live set.
- **Disposition:** DISPOSITIONED (the bare forms, class (ii)).

### 3. Delivery and code loading

- **What:** Head delivery, dual form. The original's head module imported `https://scp-wiki.wdfiles.com/theme:unusual-cargo/code/1`; the candidate's head module imports the draft host's `local--code/theme%3Aunusual-cargo-jp/1`, and a bare interwiki-style frame (candidate L5–9, priority=1) naming the same /1 is added beside it — the campaign's fixed form for head-delivered themes. Census check: exactly one `[[code]]` block in the candidate, so both /1 addresses name the block that holds the CSS — correct.
- **Why:** P6/T3 (the frame) with the module retained, mirroring the original's head topology; the draft-host form of the live lines is KB-41, class (iii).
- **Verify:** `grep -n 'local--code\|interwiki-style' candidate.txt`; count the `[[code]]` blocks (one).
- **Disposition:** DISPOSITIONED (draft-host lines, class (iii)).

### 4. Fonts and assets

- **What:** The font import moves from fonts.bunny.net to Google Fonts *keeping the original's css v1 API form* (candidate L173: `family=Caladea|IM+Fell+DW+Pica|IM+Fell+DW+Pica+SC|Tangerine`) — the host changes, the request shape does not (FONT-IMPORT). Stacks: each Latin face gains `'Yu Mincho'` after it (the CSS-BODY mass) — a system Mincho, deliberately not loaded: it names the JP serif the reader's OS already has, which is why the ledger dispositions P7 for this theme *without* a display-affecting mark, and why the loaded-not-applied check does not fire (nothing is loaded for these stacks beyond the original's own faces). One honest exception: the `font:` shorthand in `.UC_footing h2` (`font: 2.1em "Tangerine", cursive;`) keeps the original's two-name form with no JP insertion — recorded so the stack claim is exact. Assets: `COUC_logo.png`, `TOAST-PAPER.jpg` (many loci), and `toast_header.png` are repointed to the draft host's own folder; `Unusual9.jpg` is *consolidated* — the original served it from another page's folder (`the-letters-of-the-commission-on-unusual-cargo/`), the candidate serves it from the theme's own draft folder. The original's own asset URLs are case-inconsistent (two `url()`s name the folder `theme:unusual-Cargo` with a capital C); the candidate's single folder supersedes both spellings.
- **Why:** P2/KB-17 for the host; P7 in its system-face form for the stacks; P5/KB-58 for the assets (own-folder re-hosting is the posting-time class, and the consolidation is its tidy application).
- **Verify:** Candidate L173 for the import; `grep -n 'Yu Mincho' candidate.txt` for the stack insertions; `grep -n 'local--files' candidate.txt` for the asset loci.
- **Disposition:** DISPOSITIONED (P7 without display-affecting mark; assets KB-58, class (ii)).

### 5. Header, sidebar, and site furniture

- **What:** The header's ceremonial strings are localized in the CSS (CONTENT-STRING ×3): "The Right Honourable Commission on" and its narrow-width variant "The Rt. Hon. Commission on" both become 正統にして栄光なる， and "Unusual Cargo" becomes 異常貨物委員会 (candidate L232/L244/L252/L267 region) — the commission's name is the theme's furniture text, and it is translated, so no P9 question arises. The sidebar rules are carried apart from the validity repair of the per-theme record (the close-menu selector) and the font lines.
- **Why:** KB-18 (reader-visible strings) with the translation outcome; the strings' originals are quoted so a reviewer can see what was decided.
- **Verify:** `grep -n 'content:' candidate.txt` — the localized strings.
- **Disposition:** Standing.

### 6. Text translation

- **What:** The documentation and exhibits are translated throughout: 24 TRANSLATION-ANCHORED blocks, 46 TRANS-UNANCHORED blocks, and 21 COMMENT-TEXT blocks translating the code block's CSS comments (the batch's highest comment count — the original's CSS is heavily commented, and the comments were translated rather than dropped). The banner is translated with the remix attribution intact (section 1). The hub prose is translated with its link repointed (section 7).
- **Why:** P10 and KB-18; the unanchored mass was read line by line against the mirror for this README.
- **Verify:** diff.md's body sections in order.
- **Disposition:** Standing (the port itself).

### 7. Links

- **What:** The credit source link (section 1) names the recorded host. One prose link is repointed with a form change worth naming: the hub link, a bare same-wiki reference in the original (`[[[the-letters-of-the-commission-on-unusual-cargo|…]]]`), becomes an explicit EN-wiki URL in the candidate (`[*https://scp-wiki.wikidot.com/the-letters-of-the-commission-on-unusual-cargo 異常貨物委員会（英語版）]`) — the link names the English hub *as* the English hub, with the （英語版） qualifier, because the JP readership's counterpart page is not the link's subject. No live link targets a page that does not exist on its named host.
- **Why:** P11: prose links take the JP counterpart *or* the serving original, named as such; this is the second form, done explicitly.
- **Verify:** `grep -n 'the-letters-of-the-commission' candidate.txt`.
- **Disposition:** Standing; no link item is flagged for this theme.

### 8. Structure

- **What:** The localize.md closing rule holds. The code block keeps its position and size class, the exhibits correspond 1:1 (the classifier fires no EXHIBIT-RESTRUCTURE label for this pair, and the census agrees), the gate wraps the page on both sides, and the JP additions arrive as the head frame (section 3) and the credit block (section 1), not interleaved into the inherited CSS — apart from the disclosed repairs of the per-theme record, which are *inside* inherited rules by their nature.
- **Why:** R3's census is the deciding check, and here it is clean.
- **Verify:** Compare `grep -n '\[\[code\|\[\[tab\|\[\[include' original.txt candidate.txt`.
- **Disposition:** Standing; no structural deletion, no class I item.

### 9. Formatting only

- **What:** Seven WS-ONLY blocks (blank-line placement), and the tab-indented `@media` lines inside the code block re-indented to the file's space convention — the re-indentation rides inside the CSS-BODY blocks. The four validity repairs are *not* formatting and are recorded separately (per-theme record), because two of them change rendering.
- **Why:** R7: formatting churn is disclosed as its own class, and semantic repairs are never folded into it.
- **Verify:** The WS-ONLY blocks are listed in classification.json; the repairs are greppable per the per-theme record.
- **Disposition:** None required.

### 10. Porter annotations

- **What:** None. The candidate carries no `[!-- --]` comments, no wave marker comment at its code head (its first content line is the font import of section 4), and no porter comment lines: a scan for comment-only added lines returns only the translated CSS comments of section 6, which are the original's comments in translation.
- **Why:** R2's ground for "none": the annotation classes were searched for explicitly, including inside the multi-label CSS blocks where annotations ride in other packages of this batch.
- **Verify:** `grep -n '=====\|!--' candidate.txt` returns nothing.
- **Disposition:** None required.

### 11. Dispositions and exceptions

- **What:** Three items. (1) T1's sixteen pseudo-ref errors — the batch's highest count — are all class (ii): the bare credit and frame forms, the plain-form usage example, and the draft-host delivery and asset lines (sections 2–4). There is no class (i) error. (2) The render row's items: overflow 344–349px at 320 on the page; 344–349px at 320 and 884px at 768 on the sample (KB-33/KB-34 family); the credit modal in preview form (KB-32 family — the JP preview module has no modal, by design). (3) T4 row 154, display-affecting 1: P1 DISPOSITIONED (pattern 1, the bare forms, "convention, display-neutral; deps exist on scp-jp"), P3 FIXED (section 1), P7 DISPOSITIONED (the Yu Mincho stacks, recorded without a display-affecting mark). No item in this package is flagged beyond the ledger's own record; the per-theme record's repairs are disclosures, not flags — each restores the original's evident intent, and none is charged by any row.
- **Why:** A disposition is a decision with grounds (AGENTS.md §3 classes (i)/(ii)/(iii); the named KB entries), not an omission.
- **Verify:** Each item names its deciding record above.
- **Disposition:** DISPOSITIONED (all three items).

### 12. Verification

- **What:** (a) T1 source check (T1-ROWS row 139): exit 1, 16 errors / 0 warn / 1 info; all sixteen errors are pseudo-ref, class (ii). (b) T2/T3 render (RENDER-ROWS-2, lane RENDER-S2-D (EN22)): FINDINGS — the items of section 11(2). (c) T4/T5 (LOCALIZE-ROWS row 154): FINDINGS jointly, display-affecting 1; the row's pre-fix line citations (L5/L12/L19/L33) are the bare-form loci of sections 1–2 as they stood when the row was written. (d) This package is self-verifying: `python3 review/build_review.py --check` regenerates diff.md and the verdict stamp from the two byte-faithful copies in this directory and compares; the stamp reads PASS because the candidate has not changed since 666f543. Counts in this README are the generator's (difflib, autojunk off): +201/−195 in 107 change blocks / 15 diff sections; the GNU-diff count of the same pair is 308 changed lines.
- **Why:** Verification claims name the cheapest deciding check and its result.
- **Verify:** Re-run the checker on `pages/theme:unusual-cargo-jp.txt` and `python3 review/build_review.py --check` in this repo.
- **Disposition:** PASS (GOSIGN2-LEDGER (b) row 154; go-sign, COMPLETION-REPORT §10).

## Per-theme record

### The four silent validity repairs

Inside the code block, the candidate repairs four declarations/selectors that are invalid or ineffective in the original. They are disclosed here because a repair inside inherited CSS is a change, and two of them change what renders:

1. **The close-menu selector (functional).** Original: `#side-bar: target.close-menu` — with a space, this parses as a *descendant* selector (a `:target` element inside the sidebar), so the rule that was meant to restyle the sidebar itself when it is the target never matched it. Candidate: `#side-bar:target.close-menu`. This is the one repair in the batch that changes a rule's *reach*, not just its validity.
2. **`background-color: none;` → `background-color: transparent;`** — `none` is not a color; the declaration was dropped by browsers. The candidate's value is the intended one.
3. **`font-weight: heavy;` → `font-weight: bold;`** — `heavy` is not a font-weight value; dropped in the original, applied in the candidate.
4. **A missing semicolon supplied** after a `border: none` declaration, so the following declaration parses as its own.

None of the four is charged by any ledger row, and none needs a flag: each restores the original's evident intent (the surrounding rules make the intent unambiguous), and the campaign's port standard treats validity repair of this size as part of carrying CSS across. They are recorded so the next reviewer does not mistake them for drift.

### The asset consolidation

Recorded in section 4: `Unusual9.jpg` moves from the hub page's folder to the theme's own, and the candidate's single `theme%3Aunusual-cargo-jp` folder supersedes the original's two case-variant spellings (`theme:unusual-cargo`, `theme:unusual-Cargo`). On the draft host all of these are KB-58 deferred hosting; at posting, the consolidation means one folder to re-host instead of three.

## Appendix — residue blocks

| Block | Original | Candidate | Adjudication |
|---|---|---|---|
| B18 | L62–63 | L74–75 | The exhibit's "Example:" caption translated to "例：" (R1) |
| B58 | L188–189 | L199–200 | The CSS comment "/* BODY */" translated to "/* 本文 */" (R1) |
| B87 | L393–394 | L404–405 | The CSS comment "/* inputs */" translated to "/* 入力欄 */" (R1) |
| B107 | L544 | L555–556 | A blank line added before `[[/code]]` at the file's tail (R7) |

## Change set outside the two diffed files

The diff covers two files; the port's record is one file larger. `pages/theme-decoration-sample-unusual-cargo-jp.txt` is the decoration sample the render checks ran against (it includes this candidate), and its findings are the sample half of section 11(2). It belongs to this theme's record but carries no port change of its own to explain here. There are no companion fragments, no shared base file, and no inbound-link repairs in other candidates for this theme.

## License and attribution

- **Title:** Unusual Cargo
- **Author:** CityToast
- **Source:** https://scp-wiki.wikidot.com/theme:unusual-cargo — revision 83
- **License:** Creative Commons Attribution-ShareAlike 3.0 (CC BY-SA 3.0) — license deed: https://creativecommons.org/licenses/by-sa/3.0/
- **Adaptation:** This package holds a Sigma-10 migration port of the work; changes were made. See "Summary" and "Standing sections" in this README for what changed and why. Translator: AI (Muse and its delegated agents), per the campaign's standing attribution rule.
