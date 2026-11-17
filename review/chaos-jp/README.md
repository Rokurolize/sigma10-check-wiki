# Review package — theme:chaos-jp (EN → JP port)

<!-- BEGIN GENERATED VERDICT STAMP — do not hand-edit; regenerate with review/build_review.py -->
## Verdict stamp
- Theme: theme:chaos-jp — origin EN, population #70 [GOSIGN2-LEDGER (b) row 70]
- Overall: STALE — candidate file changed since the verdict was computed (verdict against 435a6bb-era content, file sha256 now 3c7706f1d41177fcd50fe010d32625e579d13b152214b17285482539ac6ee54e); verdict not carried over, re-judgement required
> verdicts below describe the pre-change file
- T1 (source check): FINDINGS (classified) — baseline 2026-11-16: exit 1, 2 errors / 2 warns / 2 infos (pseudo-ref×2); standing classes dispositioned in register c1 [T1-ROWS row 60; GOSIGN2-LEDGER (b) row 70]
- T2/T3 (render, combined verdict): FINDINGS — [combined T2/T3] report `FINDINGS` — candidate-inherent ~500px min-width on page + page-overflow at every viewport on sample. [RENDER-ROWS-1 (RENDER-S2-A)]
- Engine coverage: full matrix as run by the lane; coverage not separately caveated in the row [RENDER-ROWS-1 row]
- Credit modal: no credit-modal line in this theme's row; no sample credit-modal error recorded [RENDER-ROWS-1 (RENDER-S2-A)]
- T4 (localize patterns + follow-up): FINDINGS — display-affecting findings: 2 [LOCALIZE-ROWS row 70, source LOCALIZE-S2-A]
- T5 (translation text): FINDINGS — the source reports judge T4/T5 jointly; one verdict word covers both [LOCALIZE-ROWS row 70]
- FIX5 re-judgement: none — no OPEN items at the ledger determination [GOSIGN2-LEDGER (b) row 70]
- Computed against: canonical commit b5cb7241f527a44933e45599b41df210690771c4; candidate file pages/theme:chaos-jp.txt sha256:3c7706f1d41177fcd50fe010d32625e579d13b152214b17285482539ac6ee54e; record: GOSIGN2-LEDGER.md + GOSIGN2-LEDGER-SUPPLEMENT.md as of the FIX5 head 435a6bb
<!-- END GENERATED VERDICT STAMP -->

Status: complete — skeleton by classify_hunks.py 0.1.0; every SLOT in the skeleton is resolved in the sections below and the Appendix.
Candidate: review/chaos-jp/candidate.txt (sha256 3c7706f1d41177fcd50fe010d32625e579d13b152214b17285482539ac6ee54e)
Original: theme:chaos — scp-wiki, revision 16 (sha256 fc2ca44973091128fe100fe22ac0f55c3b0fddb578b0bd70e8c763b6a1b066b8)
Classifier: classify_hunks.py 0.1.0; signature table 2026-11-17.1; patterns commit 9c5e9079afb01d30cb9fc4ef9d714e5591eb2ffa

## Status

| | |
|---|---|
| Verdict | **PASS** at the ledger determination with no OPEN items (GOSIGN2-LEDGER (b) row 70). The generated stamp above reads STALE by design: the only post-verdict change to the candidate is the population sweep's one-line usage-name repair (Per-theme record), and the stamp does not carry a PASS onto changed bytes |
| Wave history | Three commits touch the candidate: the Stage 2 EN6 creation (240c3d2), FIX2-CREDIT (666f543 — one commit carrying the component swap, the six missing credit fields, the duplicate Rate's removal, and the JP font fix), and the usage-example sweep (b5cb724). Each is narrated in the Per-theme record |
| Standing items | **DISPOSITIONED** — T1 pseudo-ref ×2 (class (ii)); the candidate-inherent ~500px min-width overflow (by-design, KB-37 family); P9 header language (ruling 2). One item is **flagged**, not dispositioned, by this package: the prose link to `component:sigma-plus` that the same file's include list already names in its JP form (Per-theme record) |
| Go-sign basis | COMPLETION-REPORT.md §10 (go-sign issued; 81 FIXED / 26 DISPOSITIONED / 0 OPEN across the sweep) |
| Named exception | None for this theme (the sweep's single named exception is theme:amethyst-v2, which has no candidate) |

## Provenance

| | Original | Candidate |
|---|---|---|
| Page | theme:chaos | theme:chaos-jp |
| Wiki | scp-wiki.wikidot.com | SCP-JP Sigma-10 candidate (canonical repo) |
| Reference revision | 16 (first translation; the candidate's credit block records 初訳時参照リビジョン: 16) | — |
| Source of this copy | Campaign cache `gosign2-lanes/lane-oc-gs-localize-s2-A/orig-chaos.txt` (fetched once by the LOCALIZE-S2-A lane), via the campaign mirror store (class COPY, byte-identical) | Canonical file `pages/theme:chaos-jp.txt`, created in commit 240c3d2 (Stage 2 EN6); its last content change is commit b5cb724 (the usage-example sweep) |
| Lines / bytes | 812 lines / 57,884 bytes (the last line carries no trailing newline, so `wc -l` reports 811) | 821 lines / 65,849 bytes (last line unterminated; `wc -l` reports 820) |
| SHA-256 | fc2ca44973091128fe100fe22ac0f55c3b0fddb578b0bd70e8c763b6a1b066b8 | 3c7706f1d41177fcd50fe010d32625e579d13b152214b17285482539ac6ee54e |

Provenance route: derived from the original at the reference revision (sources.tsv kind: standard). No production counterpart was adopted. Reference-revision currency: the follow-up artifact `diff-chaos-from16.txt` in the campaign record records rev16 → rev16, no changes, so revision 16 is still the upstream latest; the sources.tsv note for this row says otherwise and is dealt with in the Per-theme record. The original page's own metadata, fetched by the FIX2-CREDIT lane on 2026-11-16: created by HaydenSaintPascal, created 2026-04-19 (the credit block's 作成年 rests on it).

## Summary

Chaos is a Sigma+ theme: the original sits on the `component:sigma-plus` base, frames its own code exhibit through an interwiki-style include, and carries the usual single-page furniture (bare Rate, usage exhibit, sample body with the tabview stress test, the stylesheet as a code exhibit, a three-entry license box, and a tail module). The candidate keeps that shape entire — the sample body is retained and translated, the exhibit stays an exhibit, the license entries all survive — and the diff is correspondingly small (diff.md: +68/−66 in 4 hunks; the classifier counts 28 change blocks). The port's interest is in what the creation got wrong and one wave commit then fixed in a single pass: the creation shipped the EN sigma-plus component under its plain name, a credit block with only two of the eight fields, the bare Rate still standing beside the rate-bearing preview credit block, and no Japanese font anywhere. FIX2-CREDIT (commit 666f543) repaired all four, and its diff is the theme's whole class-U story. One residual the waves missed is flagged in the Per-theme record: the prose sentence that names the base still links the EN component page, although the include at the file's head already names the JP port.

## Class summary

| Label | Blocks |
|---|---|
| TRANSLATION-ANCHORED | 11 |
| TRANS-UNANCHORED | 10 |
| EXHIBIT-RESTRUCTURE | 4 |
| INCLUDE-REPOINT | 4 |
| DRAFT-HOST | 3 |
| COMPONENT-SWAP | 2 |
| DELIVERY-HOST | 2 |
| LICENSE-BOX | 2 |
| SELF-DELIVERY | 2 |
| COMMENT-TEXT | 1 |
| CREDIT-PREVIEW | 1 |
| CSS-BODY | 1 |
| ESCAPED-INCLUDE | 1 |
| FONT-IMPORT | 1 |
| IFTAGS | 1 |
| JPFONT-LOAD | 1 |
| SIGMA-PLUS-JP | 1 |
| TASL-FIELDS | 1 |

Counts: 28 blocks — 19 specific (67.9%), 9 heuristic (32.1%), 0 residue, 0 skipped. Topology: no relocation; each side's components match by kind (head module, code exhibit, tail module). Labels are sets per block; the skeleton lists each block once under its primary label, so these sections were written from classification.json's label spans. Three adjudications matter. (1) B23's CSS-BODY heuristic label (orig L128–129 → cand L137–138) is the P7 stack supplement itself — the two `font-family` variable lines that gained the Noto Sans JP fallback in FIX2-CREDIT; it is narrated in section 4, not left as unclassified churn. (2) The four EXHIBIT-RESTRUCTURE primaries are the head delivery zone (B1), the image-block exhibit line (B14), and the license box's head and tail (B24/B27); no exhibit content was dropped (section 8). (3) The derived-presence pass reports HTTP-KEPT ×3 for this candidate; all three are adjudicated false positives in section 11 (two W3C namespace strings inside data-URI values, one attribute-selector match string), so no section of this README treats them as kept external references.

## Standing sections

### 0. Header and provenance frame

- **What:** The original's frame zone stands outside the gate (orig L1–9): the sigma-plus include (L1), the interwiki-style frame (L2–5, `priority=1`, theme= the page's own /code/1 in the `scp-wiki.wikidot.com/theme:chaos/code/1` URL form), and a module CSS importing the same /code/1 (L7–9). The gate opens at orig L11, with the bare Rate at L13–15. The candidate's frame zone is the same three pieces in the same positions (cand L1–9), repointed: `component:sigma-plus-jp` (L1), the frame naming its own /1 on the draft host (L2–5), the module importing it (L7–9). Inside the gate, the candidate's head is the credit block (cand L13–22) where the original had the Rate. Provenance route: derived from the original at reference revision 16 (see Provenance); no R4 adoption.
- **Why:** The frame zone is where a Sigma+ theme declares its base and its delivery; P1/P4/P6 and the T8 component swap rework exactly this zone, and each piece is accounted for in sections 1–3.
- **Verify:** Read original L1–15 against candidate L1–22; blocks B1–B6 in classification.json.
- **Disposition:** Recorded; the credit reading is section 1, the base and delivery readings sections 2–3.

### 1. Credit and attribution

- **What:** The original has no credit block and no info module; its attribution is the prose sentence (orig L21: made by HaydenSaintPascal for parenthesis) and its license box (orig L783–801). Its only rating device is the bare `[[module rate]]` (orig L13–15). The creation added the preview credit block but with only two fields （初訳時参照リビジョン 16 and 元記事リンク） and left the bare Rate standing beside it. FIX2-CREDIT (commit 666f543) completed the block to all eight ruling-3 fields (cand L14–21: title Chaos Insurgency Theme, translator AI, translation year 2026, original title, copyright holder `[[*user HaydenSaintPascal]]`, creation year 2026, reference revision 16, source link) and removed the Rate in the same commit. The field values are evidenced: the wave's report records the original page's metadata fetched 2026-11-16 (title 'Chaos Insurgency Theme', created_by HaydenSaintPascal, created_at 2026-04-19) and the body's own attribution line for the holder. The license box: the original's `:scp-wiki:component:license-box-theme` (orig L783) becomes `:scp-jp:component:license-box-backend` with an `|author=HaydenSaintPascal` parameter (cand L792), closed by `:scp-jp:component:license-box-end` (cand L810), already in this form at creation. All three entries survive with their authors and licenses intact (cand L793–808): the topography world map by OpenClipart (CC0, freesvg.org), "CI main" by TwistedGears (CC BY SA 3.0), and the header logo by fine und dandy (CC BY SA 4.0, Wikimedia Commons) — the labels are translated and the two bare source URLs became labeled links, but no attribution line was dropped or altered in substance.
- **Why:** P3/T1: the preview credit module is the JP environment's rate-bearing form, so the creation's bare Rate beside it was the KB-09 duplicate (ledger class B's mechanism), and its removal is part of the same wave act. Ruling 3 fixes the eight fields; the checker's `credit-missing-fields` class (i) rule is "add only the missing fields of the eight, values evidenced", which is exactly the wave's stated method (its report: only added hunks, no existing line rewritten). T4: the license box stands in its settled JP form, and its `author=` parameter names the theme's author, not any entry's.
- **Verify:** Read candidate L13–22 against the eight-field list; `grep -n 'module rate' candidate.txt` (absent) against original L14; `git show 666f543 -- pages/theme:chaos-jp.txt` for the completion and the removal landing together; read candidate L792–810 against original L783–801.
- **Disposition:** Standing. The credit completion and Rate removal are FIXED by FIX2-CREDIT; the ledger determination then found nothing open (section 12).

### 2. Includes and components

- **What:** The candidate's complete include list (grep, 8): `component:sigma-plus-jp` (L1), the interwiki-style frame (L2–5), the credit pair (L13/L22), the escaped usage include (L26), `:scp-jp:component:image-block` (L59), and the license-box pair (L792/L810). Changes against the original: (a) the base component swap — the original includes `:scp-wiki:component:sigma-plus` (orig L1); the creation carried it in the plain form `[[include component:sigma-plus]]`, still the EN component; FIX2-CREDIT swapped it to `component:sigma-plus-jp` (SIGMA-PLUS-JP + COMPONENT-SWAP spans), the campaign's JP port of the component, which exists in the repo as `pages/component:sigma-plus-jp.txt`. The bare form (no site prefix) is the campaign's settled form for this component (KB-64's shape, here with the -jp target, which is the non-defective side of that pattern). (b) The usage include is repointed `:scp-wiki:theme:chaos` → `:scp-jp:theme:chaos-jp` (ESCAPED-INCLUDE / INCLUDE-REPOINT; the -jp name form was written by the sweep). (c) The image-block include is repointed to `:scp-jp:` (orig L51 → cand L59) with its asset re-hosted (section 4). (d) The license-box pair is swapped (section 1). (e) The iftags tag is localized (orig L11 → cand L11). No `:scp-wiki:` include remains (grep: 0). One prose link to the EN component survives and is flagged in section 7.
- **Why:** P1: foreign-site includes are repointed to the JP site. T8 / ruling 4: a theme's component dependency is served by the campaign's JP port of that component where one exists; sigma-plus has one, and leaving the EN include in place would have kept the candidate's base on the EN wiki. P2/T2 (KB-08): iftags conditions name JP tags.
- **Verify:** `grep -n '\[\[include' original.txt candidate.txt` and compare; `ls pages/component:sigma-plus-jp.txt` for the swap target's existence.
- **Disposition:** Standing; the swap is FIXED by FIX2-CREDIT. No foreign include is kept, so KB-15/KB-54 do not engage.

### 3. Delivery and code loading

- **What:** Both sides deliver the stylesheet out of the page's own code exhibit: the exhibit is each side's only `[[code]]` block (orig L89–788 zone; cand L97–790 zone), so it is /1 on both sides, and the self-delivery addresses are correct (SELF-DELIVERY ×2). The original loads its /code/1 twice in the `theme:chaos/code/1` URL form on scp-wiki.wikidot.com (frame theme=, orig L4; module @import, orig L8). The candidate loads its own /1 twice on the draft host in local--code form (frame theme=, cand L4; module @import, cand L8; DELIVERY-HOST + DRAFT-HOST spans). The frame keeps `priority=1` on both sides (orig L3 → cand L3): priority 1 is the theme's own layer value in the Sigma+ stack, the base arriving through the sigma-plus include rather than through the frame. No cross-theme @import exists on either side; the base is an include, not an import (KB-14 does not engage).
- **Why:** P4/T9: deliveries are served from JP-side hosts in this environment, and a candidate's own local--code on the draft host is the sanctioned draft-stage form (class (iii)), rewritten to scp-jp.wdfiles.com at posting. P6: the frame's parameter set (priority, theme) is the surviving pair the JP interwiki-style accepts.
- **Verify:** `grep -n '\[\[code' candidate.txt` (one block, L97) against the two /1 references (cand L4, L8); read original L2–9 against candidate L2–9.
- **Disposition:** The draft-host pair is class (iii) draft form, recorded in section 11.

### 4. Fonts and assets

- **What:** The original imports three faces from fonts.bunny.net at the exhibit's head (orig L91–93: Orbitron, Aldrich, Kode Mono). The creation repointed all three to fonts.googleapis.com with families and weight ranges unchanged (cand L99–101, FONT-IMPORT span). The JP supplement landed later, in FIX2-CREDIT: a Noto Sans JP import (cand L102, JPFONT-LOAD) and `"Noto Sans JP"` inserted into the `--header-font` and `--body-font` stacks (cand L137–138; the classifier's CSS-BODY block B23). The `--monospace-font` stack (cand L139) was not given the fallback and stands as the original's `"Kode Mono", monospace`; the closure's scope is recorded here rather than silently extended (the generic monospace fallback is the original's own form on both sides). The font exhibit in the body (orig L80–84) is translated with the face names kept (cand L88–92 zone: ヘッダーフォントはOrbitron / 本文フォントはAldrich / 等幅フォントはKode Mono), so the exhibit still names what the stacks load. Assets: the one image in play, the image-block's CI Main.png, was re-hosted: the original names `https://scp-wiki.wdfiles.com/local--files/chaos-insurgency-hub/CI%20Main.png` (a hub page's attachment on the EN wiki); the candidate names its own attachment on the draft host, `https://sigma10-jp-test.wdfiles.com/local--files/theme%3Achaos-jp/CI-Main.png` (cand L59), the file name normalized (space removed). The theme's other two graphics are data-URI SVG values inside the CSS (`--sp_header-logo`, cand L142 zone; `--topography`, cand L783 zone), carried byte-identical, licenses recorded in the box (section 1).
- **Why:** P7/T5 (KB-16): no JP typeface was loaded or named at creation, so Japanese text fell back to an OS-dependent generic; the fix loads Noto Sans JP and names it in the two text stacks. P5/KB-17 (patterns 9c5e907): Google Fonts is on the allowed hotlink list and fonts.bunny.net is a mirror outside it, so the three faces moved to the canonical host. The image's re-host follows the same class logic in the other direction: an attachment of another EN page is exactly the hotlink P5 charges, and the candidate's own attachment space is where a port's files live (draft-host form at draft stage, class (ii)/(iii) posting family).
- **Verify:** `grep -n 'fonts.bunny.net\|fonts.googleapis' candidate.txt` (bunny absent; four googleapis imports at L99–102); read candidate L137–139 against original L128–130; read candidate L59 against original L51.
- **Disposition:** Fonts FIXED (ledger (c3): P7 FIXED; the vehicle was FIX2-CREDIT, see the Per-theme record). The image re-host is recorded; the render row records no image finding for this theme.

### 5. Header, sidebar, site furniture

- **What:** The skeleton prints none for this section because the title-variable lines are equal on both sides, but the disposition a reviewer needs lives here: the theme's `:root` sets `--header-title: "Chaos Insurgency"` and `--header-subtitle: "Creating Logic From Illogic"` (orig L97–98), and the candidate keeps both byte-identical (cand L106–107). The Sigma+ furniture variables (`--sp_top-bar-*`, `--sp_header-*`, the rate-module colors) are likewise carried unchanged, and the sidebar/top-bar rules the base consumes are the original's. No P8 adaptation was made or charged.
- **Why:** P9/T6 variables exist to be overridden where the JP environment requires it; these two values are the work's own name and slogan, and ruling 2 (2026-11-16) places header and title language outside migration correctness (KB-57, patterns 9c5e907). The localize lane charged the subtitle under P9 and the ledger dispositioned it on exactly that ground.
- **Verify:** Read orig L96–107 against cand L105–116; the (c3) entry for this theme.
- **Disposition:** DISPOSITIONED (ledger (c3): P9, ruling 2).

### 6. Text translation

- **What:** The sample body is retained entire and translated: 11 TRANSLATION-ANCHORED blocks (the prose sentence B11 zone, the blockquote pair, the table, the collapsible labels and heading samples, the tab labels) and 10 TRANS-UNANCHORED blocks (the tabview's repeated stress lines, the edgelord list, the tail items B25/B26, and the tail module's comment B28). The prose sentence (orig L21 → cand L29) is translated whole, keeping both user links and the furry-art consideration that is the theme's provenance joke; one link inside it is flagged in section 7. The tabview stress test is translated at full length (the repeated これはタブビューです！ lines match the original's repetition counts, including the footnote-bearing line). In-CSS text (residue class R1): the tail module's comment is translated (orig L804 zone → cand L813 zone: "image block example image has no bg so" → 画像ブロックの例示画像に背景がないため), porter-visible only; the logo comment inside the exhibit (orig L132) stays in English as part of the carried CSS. No glyph-form conversions (R5) occur; this port has no CN text.
- **Why:** P10: body and sample text are translated, with the work's name in its EN form where the credit block carries it as the title (the JP title field is the EN title, matching the original page's own title metadata). The stress-test repetitions are the exhibit's substance (a tabview under load), so compressing them would have destroyed the specimen; they were translated at length instead.
- **Verify:** Read original L21–86 against candidate L29–94; count the tabview repetitions on both sides of the long tab.
- **Disposition:** Standing (the port itself). The localize T5 pass judged this theme's text jointly with T4; its two display-affecting items are the font and the subtitle (sections 4–5), not the body text.

### 7. Links

- **What:** Three link facts. (a) The credit block's source link (cand L21) is the required ruling-3 back-reference to the EN original. (b) The sample body's author-page exhibit, `[[[moto42 |Moto42's author page]]]` (orig L39), is kept with its target unchanged and its label translated (cand L47 zone): an exhibit sentence demonstrating a link, naming an EN author page that has no JP counterpart in the campaign set — the same kept-EN-link shape the campaign dispositions for decom-dept's P11 items (sibling / batch-posting class), though no register charges it here. (c) The flagged one: the prose sentence's base link, `[[[component:sigma-plus |Sigma+]]]` (orig L21 → cand L29), still targets the EN component's fullname. On the JP wiki that fullname is not the port; the port is `component:sigma-plus-jp`, which this same file includes at cand L1. The include was swapped by FIX2-CREDIT and the prose link was not — see the Per-theme record.
- **Why:** P11 repoints links to JP counterparts where a counterpart exists. For (b) none exists in the campaign set, so the kept target with a translated label is the honest form. For (c) a counterpart exists and is already this file's own base, which is what makes (c) a flag rather than a disposition.
- **Verify:** `grep -n 'component:sigma-plus' candidate.txt` (two hits: the L1 include in -jp form, the L29 prose link in plain form).
- **Disposition:** (a) standing; (b) recorded; (c) FLAGGED in the Per-theme record, not dispositioned by this package.

### 8. Structure

- **What:** The closing rule is honored: the stylesheet's rules survive in the original's order inside the exhibit, the JP font supplement sits at the exhibit's head (imports) and in the two stack lines rather than restructuring anything, and the tail module keeps its place after the license box (orig L803–811 → cand L812–820). The four EXHIBIT-RESTRUCTURE primaries adjudicate as: B1 (orig L1–2 → cand L1–2), the head delivery zone (component swap + frame repoint), not an exhibit change; B14 (orig L51 → cand L59), the image-block exhibit line's repoint and asset re-host (sections 2/4); B24/B27 (orig L783–788 / L801 → cand L792–797 / L810), the license box's component swap (section 1). Exhibit decisions proper: every exhibit of the original is retained — blockquotes, table, collapsible, tabview stress test, `[[footnoteblock]]` (orig L76 → cand L84, kept), and the font exhibit — so no R3 drop needs a ground. The one structural deletion in the file is the bare Rate's, decided in section 1 (KB-09 duplicate beside the rate-bearing preview block).
- **Why:** Residue class R3: a sanctioned replacement and a silent deletion have the same diff shape, so each block's ground is stated. The exhibit census is the deciding check, and here it is one-to-one.
- **Verify:** `grep -n 'tabview\|footnoteblock\|collapsible' candidate.txt` against original L42–88 (all present); read candidate L792–820 against original L783–811.
- **Disposition:** Standing (no exhibit restructuring in substance, despite the label's four firings).

### 9. Formatting only

- **What:** none — the classifier counts 0 whitespace-only blocks and 0 re-indentation blocks over 28 change blocks.
- **Why:** Formatting-only churn is disclosed as its own class so it is never mistaken for semantic change; here the ground for "none" is the classifier count above.
- **Verify:** classification.json (summary: reindent_blocks 0; no WS-ONLY label in the label counts).
- **Disposition:** None required.

### 10. Porter annotations

- **What:** none — no signature fired, and direct inspection agrees: the candidate contains no `[!-- ... --]` translator notes and no editor line (`grep -c '\[!--' candidate.txt` = 0). The only added text with no original counterpart is the credit block, the font import and the two stack insertions, each accounted for in its own section.
- **Why:** R2: porter additions are listed so they are never mistaken for original content or for translation; here the ground for "none" is the grep above plus the section-by-section accounting.
- **Verify:** The grep in What.
- **Disposition:** None required.

### 11. Dispositions and exceptions

- **What:** Every finding not fixed in the candidate, in one place. (1) T1 pseudo-ref ×2, DISPOSITIONED class (ii): the two references to pages not yet posted under those names at baseline (the usage include in its then-plain form and the sigma-plus-jp component include); both resolve at posting, and the usage reference has since been written in the -jp posting form by the sweep. (2) The render finding: candidate-inherent ~500px min-width on the page with page-overflow at every viewport on the sample, DISPOSITIONED as by-design wide content (KB-37 family; the lane recorded it as candidate-inherent, and the theme's own wide specimens are its substance). (3) The header/subtitle language kept in English: DISPOSITIONED under ruling 2 (ledger (c3) P9; KB-57). (4) The draft-host delivery pair (cand L4, L8): class (iii) draft form (P4), rewritten at posting; not charged. (5) The derived-presence HTTP-KEPT ×3 (cand L142, L620, L783): adjudicated NOT kept references — L142 and L783 are the W3C namespace string `http://www.w3.org/2000/svg` inside data-URI SVG values, and L620 is an attribute-selector match string (`#footer a[href="http://www.wikidot.com"]`) that selects the platform's own footer link; none of the three loads anything. The classifier's signature false-fires on all three shapes; a signature refinement is proposed in the lane report. One item is NOT dispositioned here: the prose sigma-plus link (section 7), flagged in the Per-theme record.
- **Why:** A disposition is a decision with grounds, not an omission; this section exists so the full set can be audited in one place.
- **Verify:** Each item names its deciding register above; the KB IDs resolve in patterns/ at commit 9c5e9079afb01d30cb9fc4ef9d714e5591eb2ffa; for item 5, read the three lines named.
- **Disposition:** DISPOSITIONED (items 1–4); item 5 recorded as a classifier false positive; the flagged link stands as documentation, not as a verdict item (the theme's ledger verdict has no OPEN items).

### 12. Verification

- **What:** (a) T1 source check, baseline 2026-11-16: exit 1, 2 errors / 2 warns / 2 infos, the errors pseudo-ref ×2 (T1-ROWS row 60). Register (c1) dispositions pseudo-ref as class (ii). The FIX2-CREDIT wave's own post-fix checker run for this file reports the same counts (its report's table: error 2 / warn 2 / info 2), consistent with the remaining items being the class (ii) pair. (b) T2/T3 render: FINDINGS — the candidate-inherent min-width overflow only, dispositioned in (c2) (RENDER-ROWS-1, RENDER-S2-A (EN6)). (c) T4 localize plus follow-up: FINDINGS with 2 display-affecting items (LOCALIZE-ROWS row 70): the missing JP font (P7; FIXED) and the English subtitle (P9; DISPOSITIONED). The row's other two charges (six missing credit fields; the duplicate Rate) were closed by FIX2-CREDIT before the ledger determination and are recorded in that wave's report rather than in (c3)'s outcome line. The follow-up currency check found nothing to follow: the upstream latest is still revision 16 (campaign record, `diff-chaos-from16.txt`). (d) T5: judged jointly with T4 by the localize lane. (e) This package is self-verifying: `python3 review/build_review.py --check` regenerates diff.md from the two byte-faithful copies and compares, and re-derives the verdict stamp. Counts in this README are the classifier's (28 change blocks) and the generator's (diff.md: +68/−66 in 4 hunks).
- **Why:** Verification claims name the cheapest deciding check and its result, not a general assurance.
- **Verify:** Re-run the checker on `pages/theme:chaos-jp.txt`, and `python3 review/build_review.py --check` in this repo.
- **Disposition:** PASS at the ledger determination ((b) row 70), with the stamp STALE for the sweep reason stated in the Status table.

## Per-theme record

### Wave history, edit by edit

The candidate's current state is the product of three commits. (1) Creation, commit 240c3d2 (Stage 2 EN6): the translation, the JP license box, the Google Fonts repoint, and the delivery repoints — but the base include in the EN component's plain form, a two-field credit block, the bare Rate still standing, and no JP font. (2) FIX2-CREDIT, commit 666f543: one commit, four acts — `component:sigma-plus` → `component:sigma-plus-jp`; six credit fields added with values evidenced from the original page's fetched metadata (title, created_by HaydenSaintPascal, created_at 2026-04-19) and its body; the bare Rate deleted; the Noto Sans JP import added and the fallback inserted into the header and body stacks. (3) The usage-example sweep, commit b5cb724: one line, the usage include's name in the -jp posting form (cand L26).

### Record note — the register's wave names vs this file's commits

The ledger's (c3) line for this theme reads "P7 FIXED (font wave); P9 DISPOSITIONED (ruling 2)". Both outcomes are correct in the current bytes, but the file's history contains no font-wave commit: the font fix rode in FIX2-CREDIT, the credit wave, together with the credit completion, the Rate removal and the component swap — and (c3) names none of those three, because its register records pattern outcomes per theme, not commit contents. A reader of (c3) alone would undercount this theme's wave edits by three. This package follows the git record: one wave commit, four acts, all verified in `git show 666f543`.

### Record conflict — the sources.tsv note for this row

sources.tsv's notes column for this theme states that the original was "superseded upstream since the reference revision" and cites the follow-up artifact `diff-chaos-from16.txt` (kind K5a-i). The artifact records the opposite: `rev16 → rev16 変更: なし` (no changes), with an empty intervening-revision list. There is no post-reference delta to classify and no supersession. The note is a population-level convention in sources.tsv (the same shape recorded for the ambrose-chapter-two and caretaker-sigma rows); for this row it does not survive contact with its own citation, and this package follows the artifact.

### Flag — the prose link to the EN component page

The introduction's last sentence names the theme's base as a link: `[[[component:sigma-plus |Sigma+]]]` (cand L29). The target is the EN component's fullname without a site prefix, which on the JP wiki names a page that is not the base port; the port, `component:sigma-plus-jp`, is what the file itself includes at cand L1 (swapped by FIX2-CREDIT) and what the campaign's T8 inventory carries. The wave that swapped the include did not touch the prose link, and no register charges the residue (the localize row's items are the credit fields, the Rate, P7 and P9). It is recorded here as a flag with the deciding grep (`grep -n 'component:sigma-plus' candidate.txt`: L1 in -jp form, L29 in plain form), so a future editor can repoint the link with the evidence in hand. This package does not edit the candidate.

## Change set outside the two diffed files

The diff covers two files; the port's full change set is larger. (1) `pages/component:sigma-plus-jp.txt` — the JP port of the base component, this candidate's actual base since FIX2-CREDIT; the theme's delivery is meaningless without it, and ruling 4's audit-first component port is what made the swap possible. (2) `pages/theme-decoration-sample-chaos-jp.txt` — the render sample page; it is the "sample" the T2/T3 checks rendered, and its every-viewport overflow is the render row's subject. (3) `pages/theme:chaos.txt` — the repo's EN-side copy of the original page, the EN sample's base. (4) The delivery itself: the candidate's own local--code /1 on the draft host, named by the frame and the head module (cand L4, L8), which is the runtime form of the self-delivery; the original side's /1 was the same exhibit in the wikidot.com URL form.

## Multi-wave provenance

The candidate's current state is the product of the S2 port, one fix wave, and the documentation era's sweep: the EN6 creation (commit 240c3d2) translated and repointed but shipped the base, credit and font defects named above; LOCALIZE-S2-A examined that state and charged the credit fields, the duplicate Rate, P7 and P9 (its row is LOCALIZE-ROWS row 70); FIX2-CREDIT (commit 666f543) closed all four charges in one commit, with the credit values evidenced from a fresh fetch of the original page's metadata; the render walk recorded only the by-design overflow; and the ledger determination passed the theme with no OPEN items, so the FIX5 wave had nothing to re-judge. The only later change is the usage-example sweep (commit b5cb724), which is why the generated stamp reads STALE. Citations, in place of a changelog: GOSIGN2-LEDGER.md (b) row 70, (c2) chaos entry, (c3) chaos entry; GOSIGN2-LEDGER-SUPPLEMENT.md (no chaos entries); T1-ROWS row 60; LOCALIZE-ROWS row 70; RENDER-ROWS-1 (RENDER-S2-A) chaos row; REPORT-GOSIGN2-FIX2-CREDIT.md (campaign record), chaos row. The go-sign re-run over that record is what the Status block certifies.

## Appendix — residue blocks

The classifier emitted no residue blocks for this pair (0 residue in classification.json's summary), so there is nothing to resolve here. The nine heuristic blocks are adjudicated in the Class summary and their sections: B23 (the P7 stack supplement, section 4), B25/B26/B28 (tail translation items, section 6), and the TRANS-UNANCHORED set (section 6).
