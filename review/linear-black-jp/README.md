# Review package — theme:linear-black-jp

<!-- BEGIN GENERATED VERDICT STAMP — do not hand-edit; regenerate with review/build_review.py -->
## Verdict stamp
- Theme: theme:linear-black-jp — origin EN, population #109 [GOSIGN2-LEDGER (b) row 109]
- Overall: STALE — candidate file changed since the verdict was computed (verdict against 435a6bb-era content, file sha256 now 2c820aec4eaf649480ff5b2bb78596fc80a0891ac3666c6aeb35afa5a57a1b31); verdict not carried over, re-judgement required
> verdicts below describe the pre-change file
- T1 (source check): FINDINGS (classified) — baseline 2026-11-16: exit 1, 4 errors / 0 warns / 1 info (pseudo-ref×4); standing classes dispositioned in register c1 [T1-ROWS row 99; GOSIGN2-LEDGER (b) row 109]
- T2/T3 (render, combined verdict): FINDINGS — [combined T2/T3] report `FINDINGS` — body text and headings illegible white-on-white at all 8 combos on both pages (contrast min 1 / 1.61, candidate defect); page-overflow 612–617px@320/375 (page) and 624–629px (sample); runtime-hotlink site-theme chain + scpwiki.github.io; sample credit-modal (preview-form); broken images deferred. [RENDER-ROWS-2 (RENDER-S2-C (EN13))]
- Engine coverage: full matrix as run by the lane; coverage not separately caveated in the row [RENDER-ROWS-2 row]
- Credit modal: sample credit-modal errors dispositioned preview-form (credit:start-preview has no modal mechanism; GOSIGN-TESTS T2 amendment, 2026-11-16) [RENDER-ROWS-2 (RENDER-S2-C (EN13))]
- T4 (localize patterns + follow-up): FINDINGS — display-affecting findings: 1 [LOCALIZE-ROWS row 109, source LOCALIZE-S2-B]
- T5 (translation text): FINDINGS — the source reports judge T4/T5 jointly; one verdict word covers both [LOCALIZE-ROWS row 109]
- FIX5 re-judgement: item 20 (class E) DISPOSITIONED — FIX5-CONTRA (no edit, no commit): candidate vs original colour value sets byte-identical (line citations both sides) [GOSIGN2-LEDGER-SUPPLEMENT (a) item 20]
- Computed against: canonical commit b5cb7241f527a44933e45599b41df210690771c4; candidate file pages/theme:linear-black-jp.txt sha256:2c820aec4eaf649480ff5b2bb78596fc80a0891ac3666c6aeb35afa5a57a1b31; record: GOSIGN2-LEDGER.md + GOSIGN2-LEDGER-SUPPLEMENT.md as of the FIX5 head 435a6bb
<!-- END GENERATED VERDICT STAMP -->

## Status

| | |
|---|---|
| Verdict | **PASS** — go-sign (this theme is one of the 286 of 286 pass-eligible themes) |
| Blocking items at ledger time | GOSIGN2-LEDGER.md §(e) item 20 [E] — body text and headings illegible white-on-white at all 8 combos on both pages, recorded as a candidate defect (KB-28 contrast family) |
| Re-judgment | GOSIGN2-LEDGER-SUPPLEMENT.md item 20: **DISPOSITIONED** (FIX5-CONTRA, no edit), on the colour-identity ground re-derived in the per-theme record below |
| Standing items | **DISPOSITIONED** in their rows — page-overflow 612–617px@320/375 (page) and 624–629px (sample); runtime-hotlink site-theme chain + scpwiki.github.io; sample credit-modal (preview-form); broken images deferred [RENDER-ROWS-2 (RENDER-S2-C (EN13))]; T4 item P1 dispositioned on the posting-procedure convention [LOCALIZE-ROWS row 109] |
| Go-sign basis | COMPLETION-REPORT.md §10 (go-sign issued; 81 FIXED / 26 DISPOSITIONED / 0 OPEN across the sweep) |
| Named exception | None for this theme (the sweep's single named exception is theme:amethyst-v2, which has no candidate) |

## Provenance

| | Original | Candidate |
|---|---|---|
| Page | theme:linear-black | theme:linear-black-jp |
| Wiki | scp-wiki.wikidot.com | SCP-JP Sigma-10 candidate (canonical repo) |
| Reference revision | 10, as recorded in the candidate's credit block (初訳時参照リビジョン: 10, candidate L22) and in review/sources.tsv | — |
| Source of this copy | Mirror store `review-mirrors/orig-linear-black-rev10.txt`, fetched once by the LOCALIZE-S2-B lane at rev 10 (INDEX.tsv class COPY) | Canonical file `pages/theme:linear-black-jp.txt`, copied at worktree HEAD f24b7d0; the file's only change since the FIX5 verdict is commit b5cb724 (the usage-example sweep's one line, candidate L31), which is why the verdict stamp reads STALE |
| Lines / bytes | 399 lines / 9,077 bytes | 431 lines / 12,043 bytes |
| SHA-256 | f4eee22726893db609bd7c9a5eed7a6312cd1d3c1f17559237908c001c552efb | 2c820aec4eaf649480ff5b2bb78596fc80a0891ac3666c6aeb35afa5a57a1b31 |

Package files: `original.txt` and `candidate.txt` as tabled above; `classification.json` and the skeleton behind this README are from classify_hunks.py 0.1.0, signature table 2026-11-17.1, patterns commit 9c5e9079afb01d30cb9fc4ef9d714e5591eb2ffa.

## Summary

Linear Black is a small Sigma-Plus based theme whose port keeps the original's full documentation body in translation. The delivery changes are compact: the tail `[[module CSS]]` that imported the theme's own code fragment moves to the head (ungated on both sides), the bare Rate module becomes the preview credit block, a license box is added as a supplement (the original has none), the font load changes host and gains a Japanese mono fallback, and the self-delivery addresses move to the draft host. The theme's only blocking item was a white-on-white contrast charge, dispositioned because the candidate's colour values are the original's own, byte for byte — re-derived from this package's two files in the per-theme record, on the current bytes (the stamp's STALE is one sweep line in the usage exhibit, which touches no colour surface). No defect flag is carried by this package.

## 0. Header / provenance

- Delivery: no relocation detected between the sides; each side's components match by kind.

- **Provenance route:** derived from the branch original at the reference revision (theme:linear-black rev 10 on scp-wiki). This is not an R4 production adoption: no production JP counterpart exists in the record for this theme, and the candidate's body is the S2 localization of the EN original. The evidence is mutually consistent: review/sources.tsv keys the row `standard` with the mirror's SHA-256 equal to this package's original.txt; the candidate's credit block records 初訳時参照リビジョン: 10 (candidate L22); and the mirror is the reference revision of record for the port (the campaign record carries no follow-up supersession claim for this theme — the sources.tsv notes field is empty).


## Class summary

| Label | Blocks |
|---|---|
| BARE-RATE-DEL | 1 |
| COMMENT-TEXT | 1 |
| COMPONENT-SWAP | 2 |
| CREDIT-PREVIEW | 1 |
| CREDIT-PROSE | 1 |
| DELIVERY-HOST | 1 |
| DRAFT-HOST | 5 |
| ESCAPED-INCLUDE | 1 |
| EXHIBIT-RESTRUCTURE | 2 |
| FONT-IMPORT | 1 |
| IFTAGS | 1 |
| INCLUDE-REPOINT | 2 |
| JPFONT-STACK | 2 |
| LICENSE-BOX | 1 |
| LINK-REPOINT | 2 |
| SELF-DELIVERY | 3 |
| SIGMA-PLUS-JP | 1 |
| TASL-FIELDS | 1 |
| TRANS-UNANCHORED | 35 |
| TRANSLATION-ANCHORED | 15 |

Counts: 60 blocks, 27 specific, 32 heuristic, 1 residue, 0 skipped (comment text).

## 1. Credit and attribution

- CREDIT-PREVIEW (A): Credit block swap (P3/T1): the JP environment's preview credit module is the rate-bearing form; the branch-original credit module does not render here.
  Verify: Re-run the T1 checker (check_source.py); the credit includes must resolve on scp-jp.
  - B4: orig 10-12 -> cand 15-24 (body -> body)

- LICENSE-BOX (A): License box (T4, KB-63/KB-60): the license box must be present in its settled JP form, restored where the port dropped it.
  Verify: KB-63 recipe: license-box includes present in the candidate; form judgment per KB-60.
  - B59: orig 394-394 -> cand 410-430 (body -> body)

- **What (this theme):** the original's bare `[[module Rate]]` (original L11) is replaced by the preview credit block (candidate L15–24) carrying the eight TASL fields (B4's TASL-FIELDS span): タイトル リニア・ブラック テーマ / 翻訳責任者 AI / 翻訳年 2026 / 原題 Linear Black Theme / 著作権者 `[[*user Queerious]]` / 作成年 2025 / 初訳時参照リビジョン 10 / 元記事リンク https://scp-wiki.wikidot.com/theme:linear-black. The author field names Queerious, matching the original's own banner (original L14, "This is the Linear Black Theme by [[*user Queerious]]", whose translation is B5's CREDIT-PROSE span) — no pointer-in-place-of-author defect. The source link's host is scp-wiki.wikidot.com, the host sources.tsv records for the original.
- **The license box is a supplement, not a restoration (B59, candidate L410–430):** the original carries no license box (its only license surface is the `#license-area` CSS rules at original L243, which style a box the page never includes). The candidate adds the campaign's settled JP form — `license-box-backend |author=Queerious` plus `license-box-end` — with three image entries (mountain_pattern_stretch.jpg, trianglify-lowres_dark.webp, 9kconSketch.png) whose license fields state plainly that the original does not state a license for them and that the author should be confirmed with before posting. That honesty is the supplement's ground; it invents no license the original did not grant.
- **Disposition:** verdict PASS; no credit defect stands against this candidate.


## 2. Includes and components

- IFTAGS (A): Tag localization (P2/T2, KB-08): iftags conditions use JP tag names in the JP environment.
  Verify: KB-08 recipe: every iftags condition names JP tags; a bare [[iftags]] line is an anomaly.
  - B3: orig 8-8 -> cand 13-13 (body -> body)

- COMPONENT-SWAP (B): Component swap to a JP port (T8, ruling 4): the campaign component candidate replaces the branch component it ports.
  Verify: The swapped target is in the campaign component inventory and exists on the check wiki.
  - B7: orig 19-19 -> cand 31-31 (body -> body)

- **What (this theme):** the head include set localizes in place. `component:sigma-plus` becomes the bare `component:sigma-plus-jp` (B1's COMPONENT-SWAP and SIGMA-PLUS-JP spans; only the -jp form resolves in this environment, KB-64); `component:toggle-sidebar` takes the `:scp-jp:` prefixed form; the interwiki frame include takes the `:scp-jp:` prefixed form with its `theme=` parameter naming the theme's own /1 on the draft host (section 3). The iftags gate (B3) is unchanged in form — `[[iftags +theme]]` on both sides (original L8, candidate L13): the `theme` tag is the same tag in the JP environment, so KB-08 is satisfied with no rewrite. The body carries the image-block demonstration include repointed to the candidate's own file area (B9, section 8). The two address forms (bare for sigma-plus-jp, prefixed for the others) are the file's own; each resolves on scp-jp.
- **Disposition:** verdict PASS.


## 3. Delivery and code loading

- DELIVERY-HOST (A): Base/host repoint (P4/T9): deliveries are served from the JP hosts in this environment.
  Verify: Resolve the new host path; a kept old-host line is a class (ii) posting matter, recorded in section 11.
  - B2: orig 5-5 -> cand 10-10 (body -> body)

- DRAFT-HOST (A): Draft-stage form (KB-41, class (iii)): the candidate's own local--code on the draft host is sanctioned at draft stage.
  Verify: Recorded as a disposition in section 11, not fixed; posting rewrites it (class (ii)).
  - B54: orig 307-307 -> cand 324-324 (code-css -> code-css)
  - B55: orig 340-340 -> cand 357-357 (code-css -> code-css)

- SELF-DELIVERY (A): Own code-delivery import changed (P4): the page's own local--code delivery is its live CSS channel.
  Verify: The named delivery resolves on the draft host and serves the current candidate body.
  - B60: orig 396-399 -> cand at 432 (body -> body)

- **What (this theme):** the original delivers its CSS through one `[[code type="CSS"]]` block (original L137–390, fragment /1) and a tail `[[module CSS]]` importing that fragment, placed *after* the closing `[[/iftags]]` (original L397–399) — ungated. The candidate keeps the same single code block as fragment /1 (its type lowercased to `css`, section 9) and moves the importing module to the head (candidate L4–6), still ungated, importing its own /1 on the draft host. The relocation changes no gating and no target: the module was outside the tag gate in the original and remains outside it. Self-delivery census: the original names its own delivery twice (the frame `theme=` at original L5, the module `@import` at L398); the candidate likewise twice (the module `@import` at candidate L5, the frame `theme=` at L10) — and on both sides the named fragment /1 is the block that actually holds the stylesheet, so no FIX-CODEADDR mismatch stands (the census counts every code-block form; there is exactly one on each side). The two DRAFT-HOST spans inside the CSS (B54, B55: candidate L324, L357) are `url()` repoints of the theme's two background images to its own draft-host file area — class (iii) draft-stage forms that posting rewrites (KB-41), recorded in section 11.
- **Disposition:** verdict PASS; the draft-host forms are dispositioned class (ii)/(iii), not defects.


## 4. Fonts and assets

- FONT-IMPORT (B): Other font-load change (P5, KB-04): malformed family parameters (a hyphen for a +) make the load fail.
  Verify: KB-04: the family parameter form; the deciding evidence is the load probe (400 vs 200).
  - B53: orig 142-142 -> cand 156-159 (code-css -> code-css)

- JPFONT-STACK (B): JP family appended to a stack (P7/T5): the Latin faces have no kana glyphs; the appended JP family is the fallback that renders Japanese.
  Verify: Read the paired font-family lines; Latin families unchanged, JP family appended.
  - B56: orig 349-349 -> cand 366-366 (code-css -> code-css)
  - B57: orig 358-358 -> cand 375-375 (code-css -> code-css)

- **What (this theme):** B53 is one load line becoming two. The original loads Martian Mono (weights 100–800) from bunny.net (original L142); the candidate loads the same family and the same weight axis from Google Fonts (candidate L156) and adds an M PLUS 1 Code import (candidate L159) announced by its own comment (section 10). The JPFONT-STACK spans (B56, B57) append `'M PLUS 1 Code'` after `'Martian Mono'` in the theme's two mono stacks (candidate L366, L375) — pattern 7: the Latin face carries no kana glyphs, and the appended JP face is the fallback that renders Japanese. The load/apply check closes in both directions: every family named in a stack is loaded (Martian Mono at L156, M PLUS 1 Code at L159), every loaded family is applied, the loads sit in the delivered code block (not an inert channel), and no load is duplicated.
- **Disposition:** verdict PASS.


## 5. Header, sidebar, site furniture

none — no signature for this section fired over 60 change blocks, and the ground is checkable: the theme defines no header or sidebar variables and no header furniture of its own (its `:root` block, original L148–183, is palette and font variables only, carried byte-identically in the candidate); all header/sidebar rendering comes from the Sigma-Plus base, whose JP form section 2 records.

## 6. Text translation

- TRANS-UNANCHORED (C): Translation-shaped change without anchors (P10, KB-18): restructured lines are the queue where restorations and exhibit changes hide.
  Verify: Writer confirmation against the mirror, line by line.
  - B6: orig 16-16 -> cand 28-28 (body -> body)
  - B10: orig 29-29 -> cand 41-41 (body -> body)
  - B11: orig 32-32 -> cand 44-44 (body -> body)
  - B20: orig 59-59 -> cand 71-71 (body -> body)
  - B22: orig 64-64 -> cand 76-76 (body -> body)
  - B23: orig 66-66 -> cand 78-78 (body -> body)
  - B24: orig 68-68 -> cand 80-80 (body -> body)
  - B25: orig 70-70 -> cand 82-82 (body -> body)
  - B26: orig 72-72 -> cand 84-84 (body -> body)
  - B27: orig 74-74 -> cand 86-86 (body -> body)
  - B28: orig 76-76 -> cand 88-88 (body -> body)
  - B30: orig 82-82 -> cand 94-94 (body -> body)
  - B31: orig 84-84 -> cand 96-96 (body -> body)
  - B32: orig 86-86 -> cand 98-98 (body -> body)
  - B33: orig 88-88 -> cand 100-100 (body -> body)
  - B34: orig 90-90 -> cand 102-102 (body -> body)
  - B35: orig 92-92 -> cand 104-104 (body -> body)
  - B36: orig 94-94 -> cand 106-106 (body -> body)
  - B37: orig 96-96 -> cand 108-108 (body -> body)
  - B38: orig 98-98 -> cand 110-110 (body -> body)
  - B39: orig 100-100 -> cand 112-112 (body -> body)
  - B40: orig 102-102 -> cand 114-114 (body -> body)
  - B41: orig 104-104 -> cand 116-116 (body -> body)
  - B42: orig 106-106 -> cand 118-118 (body -> body)
  - B44: orig 114-114 -> cand 126-126 (body -> body)
  - B45: orig 116-116 -> cand 128-128 (body -> body)
  - B46: orig 118-118 -> cand 130-130 (body -> body)
  - B47: orig 120-120 -> cand 132-132 (body -> body)
  - B49: orig 129-129 -> cand 141-141 (body -> body)
  - B50: orig at 133 -> cand 145-146 (body -> body)

- TRANSLATION-ANCHORED (B): Prose/usage translation (P10, KB-18): reader-visible text localizes; anchored pairs are one-to-one translations.
  Verify: Read the pairs; the anchors (leading token, CSS property, selector, heading level) confirm the pairing.
  - B12: orig 36-37 -> cand 48-49 (body -> body)
  - B13: orig 39-39 -> cand 51-51 (body -> body)
  - B14: orig 41-41 -> cand 53-53 (body -> body)
  - B15: orig 43-43 -> cand 55-55 (body -> body)
  - B16: orig 45-45 -> cand 57-57 (body -> body)
  - B17: orig 47-47 -> cand 59-59 (body -> body)
  - B18: orig 53-54 -> cand 65-66 (body -> body)
  - B19: orig 56-57 -> cand 68-69 (body -> body)
  - B21: orig 61-62 -> cand 73-74 (body -> body)
  - B29: orig 79-80 -> cand 91-92 (body -> body)
  - B43: orig 109-109 -> cand 121-121 (body -> body)
  - B48: orig 123-125 -> cand 135-137 (body -> body)
  - B51: orig 135-135 -> cand 149-149 (body -> body)
  - B52: orig 137-137 -> cand 151-151 (code-css -> code-css)

- **What (this theme):** the documentation body translates in full: 35 TRANS-UNANCHORED and 15 TRANSLATION-ANCHORED spans, adjudicated line by line against the mirror in the appendix. Two spans carry more than translation: B51 (original L135 → candidate L149) is the font note, whose translation gains the porter supplement sentence recorded in section 10; B50 (original L133 → candidate L145–146) is the same note's heading line pair. B52 (original L137 → candidate L151) is the code block's opener line, whose only change is the `CSS` → `css` type case (section 9). No untranslated reader prose remains in the candidate, and no exhibit string is left in English.
- **Disposition:** verdict PASS (T5 judged jointly with T4: FINDINGS on the section 11 items only).


## 7. Links

- LINK-REPOINT (C): Link target repointed (P11): prose links take the JP counterpart or the serving original, under the dead-reference evidence standard.
  Verify: Probe the target; a repoint needs sameness evidence.
  - B5: orig 14-14 -> cand 26-26 (body -> body)
  - B8: orig 24-25 -> cand 36-37 (body -> body)

- **What (this theme):** two link blocks. B5 (the banner, original L14 → candidate L26): the SCP-9900 reference, a plain page link in the original, becomes an absolute URL to https://scp-wiki.wikidot.com/scp-9900 with the （英語版） annotation — the dead-reference standard applied correctly: the JP site has no same page, so the original is served by URL and marked as the English version. B8 (original L24–25 → candidate L36–37) is the theme's *dead link exhibit* — a demonstration of a dead link, whose label translates (リンク1) with the exhibit; it is an exhibit of a dead link, not a reference, and flagging it as one would be a category error.
- **Disposition:** verdict PASS.


## 8. Structure

- EXHIBIT-RESTRUCTURE (C): Usage/sample exhibits dropped or replaced (R3): a sanctioned replacement and a silent deletion have the same diff shape; the ground must be stated.
  Verify: The exhibit-decision slot for this block, argued from the mirror.
  - B1: orig 1-3 -> cand 1-8 (body -> body)
  - B9: orig 27-27 -> cand 39-39 (body -> body)

- **What (this theme):** B1 (original L1–3 → candidate L1–8) is the head restructure of sections 2–3 (the delivery relocation and the include localizations), not an exhibit change; EXHIBIT-RESTRUCTURE false-fires on it because the head block also carries the frame include. The exhibit census closes the section: the usage exhibit (the `@@`-escaped include of the theme itself, candidate L31) and the image-block demonstration (B9) are present on both sides, and the documentation's example blocks survive in translation (section 6).


- **Exhibit decisions:** B9 (original L27 → candidate L39), the image-block demonstration include — **replaced, not dropped**: the demonstration survives with its `name=` repointed from the original's file to the candidate's own draft-host file (9kconSketch.png), the same demonstration with the localized asset address. The bare `[[module Rate]]` (original L11, B4's BARE-RATE-DEL span) — **removed with replacement**: the preview credit block that replaces it (candidate L15–24) is the rate-bearing form in this environment (P3), so no rating surface is lost.


## 9. Formatting only

- WS-ONLY blocks: 0
- Re-indentation: 0 blocks pair up after leading-whitespace normalization

## 10. Porter annotations

No ANNOTATION signature fired, but two porter annotations ride inside other labeled blocks (checked explicitly, per the standing lesson):

- The CSS comment `/* 日本語フォント (JP localization) */` at candidate L158 (inside B53, section 4), announcing the added M PLUS 1 Code import on the next line.
- The prose supplement sentence at candidate L149 (inside B51, section 6): the translated font note gains 「和文にはM PLUS 1 Codeを併記しています。」 ("for Japanese text, M PLUS 1 Code is listed alongside"), which states exactly what the bytes do — the stacks at candidate L366 and L375 carry the family — so the annotation is accurate, not a flag.

The license box's per-image notes (candidate L411–427, section 1) are porter-supplied attribution text of the same kind. No annotation in this candidate states anything the bytes refute.

## 11. Dispositions and exceptions

- **Item 20 (class E), the white-on-white charge — DISPOSITIONED.** The full argument is the per-theme record below; its one-sentence form is that every colour value in the candidate is the original's own, byte for byte (whole-file colour-token multisets exactly equal; the charged windows byte-identical), so the illegibility the render walk photographed is a property of the original theme's colour design — white text over its own translucent black panel — not a defect the port introduced. [GOSIGN2-LEDGER-SUPPLEMENT.md item 20; REPORT-GOSIGN2-FIX5-CONTRA.md §4; KB-28 family, patterns/ at commit 9c5e9079afb01d30cb9fc4ef9d714e5591eb2ffa]
- **Page-overflow (612–617px@320/375 on the page, 624–629px on the sample) — DISPOSITIONED** in the render row's separation, with the runtime-hotlink site-theme chain and the scpwiki.github.io references (the draft-stage and environment classes, KB-41/KB-54 families) and the broken images (deferred asset hosting, KB-58) [RENDER-ROWS-2 (RENDER-S2-C (EN13))].
- **Sample credit-modal errors — DISPOSITIONED, preview-form:** credit:start-preview has no modal mechanism (GOSIGN-TESTS T2 amendment, 2026-11-16; KB-32).
- **T1 pseudo-ref ×4 — DISPOSITIONED, class (ii)/(iii):** the four draft-host references (candidate L5, L39, L324, L357) are the sanctioned draft-stage forms; posting rewrites them to the production host (register c1) [T1-ROWS row 99].
- **T4 item P1 — DISPOSITIONED** on the posting-procedure convention [LOCALIZE-ROWS row 109, source LOCALIZE-S2-B].
- **The verdict stamp's STALE** is explained, not a disposition: the candidate changed after the verdict by exactly one line (commit b5cb724's usage-exhibit -jp insertion, candidate L31). The re-judgement on the current bytes is this package; the colour ground of item 20 does not touch the changed line (per-theme record).


## 12. Verification

- **T1 (source check):** baseline 2026-11-16: exit 1, 4 errors / 0 warns / 1 info (pseudo-ref×4) [T1-ROWS row 99]. Re-run for this package (2026-11-17, the campaign checker `check_source.py` on this package's candidate.txt, `--kind theme --translation --check-links`): exit 1, **4 errors / 0 warns / 1 info** — the error multiset is unchanged (pseudo-ref×4, now at candidate L5/L39/L324/L357, the dispositioned draft-host forms of section 11); the info is `!important` ×2 (candidate L231, L271), inherited from the original's CSS. No class (i) error stands against this candidate.
- **T2/T3 (render):** combined verdict FINDINGS [RENDER-ROWS-2 (RENDER-S2-C (EN13))]. The one candidate-specific item is item 20 (dispositioned, section 11); the row's separation assigns the rest to the standing classes named there. No re-render was run for this package: the render record is the lane's, cited, not re-measured here.
- **T4 (localize patterns + follow-up):** FINDINGS — 1 display-affecting item (P1, dispositioned, section 11) [LOCALIZE-ROWS row 109, source LOCALIZE-S2-B].
- **T5 (translation text):** judged jointly with T4 by the source report: FINDINGS on the P1 item; the lane found no mistranslations or untranslated reader prose in what the candidate carries (section 6 confirms against the mirror).
- **This package:** `python3 review/build_review.py --check` — the verdict stamp regenerates identically from the two files in this package, and the package is not in the pre-existing stale set (the refresh-3 population). The censuses in the per-theme record were re-derived from this package's two files while this README was written, not transcribed from the supplement.


## Per-theme record

### The colour-identity disposition (ledger §(e) item 20)

The charge, as the ledger states it: item 20 [E] (KB-28 contrast) — body text and headings are illegible white-on-white at all 8 width/engine combos on both pages (contrast min 1 / 1.61), recorded as a candidate defect [GOSIGN2-LEDGER.md §(e) item 20; the stamp's T2/T3 line]. Class E charges a candidate-side defect, so the question the disposition turns on is narrow and decidable from the two files in this package: did the port change any colour? The supplement's ground is that it did not: "candidate vs original colour value sets byte-identical (line citations both sides)" [GOSIGN2-LEDGER-SUPPLEMENT.md (a) item 20; REPORT-GOSIGN2-FIX5-CONTRA.md §4]. Re-measured from this package's files:

1. **Whole-file colour-token census.** Every colour token in each file (hex values and `rgb()`/`rgba()`/`hsl()` functions, whitespace-normalized): 17 distinct values on each side, and the *multisets are exactly equal* — not merely the same set, but the same count of every value. The ground holds in a stronger form than the supplement states.
2. **Declaration census.** Every colour/background-bearing declaration (`color`, `background`, `background-color`, `background-image`, `border-color`, `text-shadow`, `box-shadow`, `outline-color`, `fill`, `stroke`): 55 declarations on each side. The only raw differences are the two background-image URL host repoints (original L307/L340 → candidate L324/L357, the draft-host forms of section 3); with the URLs normalized, the multisets are identical.
3. **The charged surfaces themselves.** The `:root` palette window — original L148–183 = candidate L165–200 — is byte-identical (SHA-256 window prefix `835b2763210a6692` on both sides); it carries `--vividAccentColor: #ACACD2`, the heading colour of the charge. The `#page-content` background window (original L271–275 = candidate L288–292, prefix `2bd96dfd2f27183c`) and the `h1` colour window (original L189–191 = candidate L206–208, prefix `a113bfba6cc4c202`) are likewise byte-identical. The body-text rule (original L347–351 / candidate L364–368) is identical except its `font-family` line, which gains the `'M PLUS 1 Code'` fallback of section 4; its `color: white` line and the panel's `background: rgba(0,0,0,0.35)` are the original's own values. The white-on-white the render walk photographed is white text over the theme's own translucent black panel over the site background — the original's design values, unchanged.
4. **No structural colour accident.** A brace-depth scan of both files ends at depth 0 with no negative excursion on either side, excluding a displaced brace silently re-scoping the rules after it. The footnote census also closes: `[[footnote]]` appears once on each side and `[[footnoteblock]]` on neither — nothing was dropped under a live footnote.

The conclusion the identity licenses: the candidate renders body text and headings with the original's own palette, the original's own panel, and the original's own rules, so the illegibility is a property of the original theme's colour design, and "fixing" it would mean departing from the original — an editorial change, not a migration correction. Disposition: **DISPOSITIONED, no edit** [GOSIGN2-LEDGER-SUPPLEMENT.md item 20; FIX5-CONTRA §4].

### Second-reviewer walk

The class asks for the disposition to be walked once more from the third-party perspective: is the ground stated in terms a reader who did none of the work can check, and does it hold? The ground here is two whole-file censuses and three named windows, every one reproducible from `original.txt` and `candidate.txt` alone with a text editor and a hash tool; no step asks the reader to trust the FIX5 lane's file copies (its line citations were taken against the theme's /1 code asset, whose internal numbering differs from this package's page mirror, and this record re-derived each number from the package files). The walk re-ran each measurement on the *current* candidate bytes — including the one post-verdict change, commit b5cb724's usage-exhibit line (candidate L31), which touches no colour surface, so the disposition covers the file as it now stands. Each measurement held exactly, in one case (the token census) in a stronger form than the supplement claims. One limit is stated for completeness: the census proves the port introduced no colour change; it does not prove the original's text is readable — the render evidence says it is not, on the original's design, which is precisely what the disposition records. Walk outcome: **the disposition is sound as stated.**

### Record discrepancies flagged by this package

1. **The FIX5 report's line citations do not address this package's mirror.** REPORT-GOSIGN2-FIX5-CONTRA.md §4 cites the candidate and original by the line numbers of the theme's /1 code asset (a served-fragment copy), not of the page sources in this package; a reader checking its numbers against `original.txt`/`candidate.txt` will not find the rules at those lines. The values agree at the package loci cited in the record above; the package's numbers govern.
2. No sources.tsv discrepancy stands for this theme: the row's notes field is empty, and its recorded host (scp-wiki) matches the candidate's credit link (section 1).

### Multi-wave provenance

The candidate's current state is the product of successive waves, not one pass: the Stage 2 EN batch port (LOCALIZE-S2-B) produced the localization the T4 lane audited; FIX5-CONTRA closed the theme's only blocking item as a no-edit disposition, so no FIX5 commit touches this file; and commit b5cb724 (the population usage-example sweep) inserted the `-jp` posting name into the usage exhibit — the one-line delta behind the stamp's STALE. Citations, in place of a changelog: GOSIGN2-LEDGER.md §(e) item 20 and the theme's render/localize rows; GOSIGN2-LEDGER-SUPPLEMENT.md item 20; REPORT-GOSIGN2-FIX5-CONTRA.md §4. The go-sign over that record is what the Status block certifies.

## Appendix — heuristic and residue adjudication

60 blocks: 27 specific, 32 heuristic, 1 residue. **Residue B58** (original L389 → candidate at L406, code-css → body): the original's code block ends with a blank line before its `[[/code]]` (original L389–390); the candidate's block closes without that blank line (candidate L405). The block's last rule (the `#search-top-box-form` rule, original L384–388) is byte-identical in the candidate (L401–405 area); no rule text is involved. A form-only tail difference at the block boundary — assigned to section 9. **Heuristic mass:** the TRANS-UNANCHORED spans (35) and the single-line appendix pairs (R2–R33 of the skeleton's listing: the banner B5, the dead-link exhibit B8, and the documentation lines B6, B10, B11, B20–B51) are the documentation body's one-to-one translation lines, each verified against the mirror while section 6 was written; B5 and B8 carry the additional LINK-REPOINT spans adjudicated in section 7. The COMMENT-TEXT span is the font-import comment of section 10. No heuristic block conceals a drop: the include census (5 distinct includes in the original; the candidate adds the credit pair and the license-box pair and drops none) and the footnote census (per-theme record, item 4) close the content-presence check.
