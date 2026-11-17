# Review package — theme:skipos-jp

<!-- BEGIN GENERATED VERDICT STAMP — do not hand-edit; regenerate with review/build_review.py -->
## Verdict stamp
- Theme: theme:skipos-jp — origin EN, population #39 [GOSIGN2-LEDGER (b) row 39]
- Overall: STALE — candidate file changed since the verdict was computed (verdict against 435a6bb-era content, file sha256 now 824edf347d11bac1982ad37182806a84dadeab74ad94fadac30c8cb7c92be9fb); verdict not carried over, re-judgement required
> verdicts below describe the pre-change file
- T1 (source check): FINDINGS (classified) — baseline 2026-11-16: exit 1, 8 errors / 1 warn / 1 info (pseudo-ref×6, hotlink×2); standing classes dispositioned in register c1 [T1-ROWS row 39; GOSIGN2-LEDGER (b) row 39]
- T2/T3 (render, combined verdict): FINDINGS — [combined T2/T3] report `FINDINGS` — 453/454px@320/375 fixed-width OS-window overflow, double `interwiki-style` include → `priority{$priority}` console error, cdn.jsdelivr.net/fonts.bunny.net/cdn.scpwiki.com direct links, T2 sample no machine verdict. [RENDER-ROWS-1 (RENDER-D2 row 39)]
- Engine coverage: full matrix as run by the lane; coverage not separately caveated in the row [RENDER-ROWS-1 row]
- Credit modal: no credit-modal line in this theme's row; no sample credit-modal error recorded [RENDER-ROWS-1 (RENDER-D2 row 39)]
- T4 (localize patterns + follow-up): FINDINGS — display-affecting findings: 1 [LOCALIZE-ROWS row 39, source LOCALIZE-B]
- T5 (translation text): FINDINGS — the source reports judge T4/T5 jointly; one verdict word covers both [LOCALIZE-ROWS row 39]
- FIX5 re-judgement: none — no OPEN items at the ledger determination [GOSIGN2-LEDGER (b) row 39]
- Computed against: canonical commit f4488f2d2948824238a2d06479f104f4aab0cf5d; candidate file pages/theme:skipos-jp.txt sha256:824edf347d11bac1982ad37182806a84dadeab74ad94fadac30c8cb7c92be9fb; record: GOSIGN2-LEDGER.md + GOSIGN2-LEDGER-SUPPLEMENT.md as of the FIX5 head 435a6bb
<!-- END GENERATED VERDICT STAMP -->

Status: complete — skeleton by classify_hunks.py 0.1.0; every SLOT in the skeleton is resolved in the sections below and the Appendix.
Candidate: review/skipos-jp/candidate.txt (sha256 c48a03cb49ad988575eea32f8598cd9247439865773586bb458e82cc95bae247)
Original: theme:skipos — scp-wiki, revision 26 (sha256 cf354523c1f546589546177a89e531e6b04e030141b4d020c4c053ed21927f56)
Classifier: classify_hunks.py 0.1.0; signature table 2026-11-17.1; patterns commit 9c5e9079afb01d30cb9fc4ef9d714e5591eb2ffa

## Status

| | |
|---|---|
| Verdict | **PASS** — passed at the ledger determination with no OPEN items (GOSIGN2-LEDGER (b) row 39); one of the 286 of 286 pass-eligible themes. The generated stamp above reads STALE: the candidate changed after the verdict-era bytes (the usage-example sweep, commit b5cb724, repointed two exhibit lines to the -jp forms), so the stamp's verdict lines describe the pre-sweep file |
| Blocking items at ledger time | None — no section (e) items exist for this theme and the supplement carries no skipos entries |
| Wave edits after the port | Credit fields completed (Phase 17 skeleton, 8dcac74; gosign2 T1 fixes, b816e10); base delivery repointed to basalt-jp and translator normalized (FIX-P4, f1138e4); bunny fonts reverted and the inner frame's priority supplied (FIX4-IWB, 5559209); duplicated base import removed (FIX4-MOPUP, 379eb44); usage exhibits repointed (population sweep, b5cb724) |
| Open flag from this package | The ledger's P7 FIXED is not borne out by the delivered bytes: the JP font supplement exists only as inert body text (cand L678–697), and the delivered CSS names no JP face and still reads `content: "Terminal"`. Full evidence in section 4 and the Per-theme record |
| Go-sign basis | COMPLETION-REPORT.md §10 (go-sign issued; 81 FIXED / 26 DISPOSITIONED / 0 OPEN across the sweep) |
| Named exception | None for this theme (the sweep's single named exception is theme:amethyst-v2, which has no candidate) |

## Provenance

| | Original | Candidate |
|---|---|---|
| Page | theme:skipos | theme:skipos-jp |
| Wiki | scp-wiki.wikidot.com | SCP-JP Sigma-10 candidate (canonical repo) |
| Reference revision | 26 (created 2025-12-04 14:11:21 per sources.tsv), as recorded in the candidate's credit block: **初訳時参照リビジョン:** 26 | — |
| Source of this copy | Refetched 2026-11-17 at the reference revision (mirror store class FETCH-REGEN), via the campaign mirror store | Canonical file `pages/theme:skipos-jp.txt`, imported in commit d727e92 ("Canonical sources for the Sigma-10 display-check composition"); its last content change is commit b5cb724 (the usage-example sweep) |
| Lines / bytes | 790 lines / 26,793 bytes | 775 lines / 26,081 bytes |
| SHA-256 | cf354523c1f546589546177a89e531e6b04e030141b4d020c4c053ed21927f56 | c48a03cb49ad988575eea32f8598cd9247439865773586bb458e82cc95bae247 |

Provenance route: derived from the original at the reference revision (sources.tsv kind K5b-3). No production counterpart was adopted. The K5b shape matters for reading the diff: the candidate **layers over theme:basalt-jp** — its head module imports the base candidate's /1 — so this package's diff covers the candidate file only, and the base's stylesheet body lives in `pages/theme:basalt-jp.txt` (Change set, item 1), not in either file here.

## Summary

SkipOS is EstrellaYoshte's operating-system parody theme built on the Basalt/Bedrock base: the original imports the base from the EN Basalt CDN, carries its own 603-line stylesheet in a code exhibit served as its own /1, and documents itself with window/box specimen exhibits. The candidate repoints the base delivery to the JP basalt candidate, keeps the code-exhibit delivery intact (603 lines on both sides, two internal edits), translates the prose and the surviving exhibits, drops the specimen set, and appends two JP supplement modules (an action-area correction and a credit-button retarget). Five wave commits then completed its credit fields, repointed its base, reverted its bunny font imports, supplied its inner frame's missing priority, and removed a duplicated base import. The one place the record and the bytes part company is pattern 7: the JP font stacks and the translated "Terminal" string were left as loose text after the code exhibit, outside any delivery block, so the delivered CSS still sets Latin-only stacks — the ledger's P7 FIXED describes work the bytes do not contain (section 4, Per-theme record).

## Classification

| Label | Blocks |
|---|---|
| COMMENT-TEXT | 1 |
| COMPONENT-SWAP | 1 |
| CONTENT-STRING | 1 |
| CREDIT-PREVIEW | 1 |
| DELIVERY-HOST | 3 |
| DELIVERY-MOVE | 1 |
| DRAFT-HOST | 6 |
| ESCAPED-INCLUDE | 1 |
| EXHIBIT-RESTRUCTURE | 2 |
| IFTAGS | 1 |
| INCLUDE-REPOINT | 2 |
| RATE-EXHIBIT-KEPT-CANDIDATE | 1 |
| SELF-DELIVERY | 3 |
| T7-CREDIT-CSS | 1 |
| TASL-FIELDS | 1 |
| TRANSLATION-ANCHORED | 1 |
| TRANS-UNANCHORED | 10 |
| WS-ONLY | 1 |

Counts: 18 blocks — 10 specific (55.6%), 7 heuristic (38.9%), 1 residue (5.6%), 0 skipped. Topology: the original's components are the Basalt CDN module (orig L1–5), the code-css exhibit (orig L175–778, 603 lines) and the own-/1 tail module (orig L781–784); the candidate's are the basalt-jp module (cand L12–15), the same code-css exhibit (cand L74–677, 603 lines), and three appended modules (cand L702–706, L709–712, L719–775). Labels are sets per block; this README's sections were written from classification.json's label spans, not from the skeleton's per-section lists. One label is a false fire and is adjudicated in the Appendix: RATE-EXHIBIT-KEPT-CANDIDATE (the candidate holds no Rate module at all).

## Standing sections

### 0. Header and provenance frame

- **What:** The original's head (L1–10) is the base import module (`[[module css]]` with the two cdn.scpwiki.com Basalt imports, orig L2–4) and a bare `[[module Rate]]` in a right-aligned div (orig L7–10), all inside `[[iftags +theme]]`. The candidate's head (L1–15) is the localized gate (`[[iftags +テーマ]]`, cand L1), the preview credit block (cand L3–12), and the base module repointed to the JP base candidate (cand L13–15). Provenance route: derived from the original at reference revision 26, layered over theme:basalt-jp (see Provenance).
- **Why:** P1/P2/P3/P4 rework exactly this frame for the JP environment; each piece is accounted for in sections 1–4.
- **Verify:** Read original L1–10 against candidate L1–15; block B1 in classification.json.
- **Disposition:** Recorded; the credit reading is section 1, the delivery reading section 3.

### 1. Credit and attribution

- **What:** The original has no credit block; its attribution is the intro prose ("developed by [[*user EstrellaYoshte]]", orig L12) and its only rating device is the bare Rate (orig L8). The candidate adds the preview credit block (cand L3–12, block B1): `:scp-jp:credit:start-preview` / `end-preview` carrying all eight ruling-3 fields — title SkipOS Theme, translator AI, translation year 2026, original title "SkipOS Theme", copyright holder EstrellaYoshte, creation year 2022, reference revision 26, and the source link to the EN page. The author field was checked against the original's prose credit and agrees. The bare Rate is deleted in the same head rework: `grep -n 'module Rate' candidate.txt` finds none (the classifier's RATE-EXHIBIT-KEPT-CANDIDATE label on B2 is a false fire, adjudicated in the Appendix). No license box exists on either side, and none was charged. The block arrived in three steps: Phase 17 (8dcac74) inserted the two-field skeleton (revision + source link), the gosign2 T1 fixes (b816e10) added the other six fields with the translator reading SCP-JP, and FIX-P4 (f1138e4) normalized the translator to AI. The theme's credit-module CSS is the appended retarget module at cand L720–775 (section 3): supplement type T7 by addition, correcting the Bedrock `.creditButton > p > a` selector shape to the frozen JP markup's `.creditButton > a`.
- **Why:** P3/T1: the preview credit module is the JP environment's rate-bearing credit form, so a separate bare Rate beside it would duplicate the rating widget (KB-09's mechanism, patterns commit 9c5e9079afb01d30cb9fc4ef9d714e5591eb2ffa). Ruling 3 fixes the eight fields and credits campaign translations to AI. The T7 addition exists because the base the candidate composes (Bedrock rules inside basalt-jp) styles a credit-button DOM shape the JP credit module does not emit (the module's own comment, cand L721–722, states the mechanism).
- **Verify:** Read candidate L3–12 against the eight-field list; `grep -n 'module Rate' candidate.txt` (absent) against original L8; read cand L720–775 for the T7 module.
- **Disposition:** Standing. Ledger (c3): P3 credit fields FIXED (credit waves; checker-verified) — the outcome is correct in the bytes; the vehicles were the Phase 17 / T1 / FIX-P4 steps above (Per-theme record).

### 2. Includes and components

- **What:** The candidate's include list (grep): the credit pair (L3/L12), `component:image-block` in the examples (cand L22, repointed `:scp-jp:` with its file re-hosted to the candidate's own draft-host attachment), and two `:scp-jp:component:interwiki-style` frames (cand L698–702 inside the source-code collapsible, cand L714–718 in the tail div). The original's includes are the same image-block (orig L44, EN host file) and one EN frame (orig L783–787). The usage exhibits are the escaped includes `@@[[include :scp-jp:theme:bedrock-jp]]@@` and `@@[[include :scp-jp:theme:skipos-jp]]@@` (cand L18–19) — the post-sweep forms; the sweep (b5cb724) is the candidate's last change and the reason the stamp reads STALE. One prose link does not follow the file's own convention: the kernel sentence at cand L21 links `[[[theme:bedrock|Bedrock]]]`, the plain production name, while the file's exhibits name theme:bedrock-jp and its delivery composes basalt-jp. Recorded as a minor flag in the Per-theme record. No foreign include is kept, so KB-15/KB-54 do not engage.
- **Why:** P1: foreign-site includes are repointed to the JP site, and usage examples name the -jp posting names (the sweep's premise, settled from the repo's AGENTS.md). Ruling 4 does not engage: the theme's component dependency is image-block, an exhibit device whose JP form exists.
- **Verify:** `grep -n '\[\[include' original.txt candidate.txt` and compare; `grep -n 'theme:bedrock' candidate.txt` (L18 exhibit vs L21 prose link).
- **Disposition:** Standing, with the L21 prose-link flag carried to the Per-theme record.

### 3. Delivery and code loading

- **What:** Three layers. (1) **Base:** the head module imports theme:basalt-jp's /1 on the draft host (cand L14). FIX-P4 (f1138e4) replaced the original's two cdn.scpwiki.com imports (normalize-min.css and basalt-bedrock-min.css, orig L3–4) with that single JP address — initially written as two identical @import lines, one of which FIX4-MOPUP (379eb44) removed (the classifier's DELIVERY-HOST spans on B1). (2) **Own layer:** the theme's stylesheet stays in its code exhibit (cand L75–677) served as the candidate's own /1, imported by the tail module (cand L710–712) and framed by the two interwiki-style includes at priority=3 (cand L698–702, L714–718). The address census is sound: the candidate has exactly one `[[code]]` block and it holds the CSS, so /1 names the right block (this theme is not in the FIX-CODEADDR no-target class). The inner frame originally lacked its priority parameter; FIX4-IWB (5559209) supplied `priority=3` — the edit the registers record as the KB-07 missing-priority fix and the KB-06 §13 include-parameters fix. The double frame itself (one inside the collapsible, one in the tail) stands in the current bytes; the render row's `priority{$priority}` console error belongs to the pre-fix state of the inner frame. (3) **Supplements:** two porter modules appended at creation (d727e92): the action-area module (cand L703–706, a JP-environment furniture correction with its own EN rationale comment) and the credit-button retarget module (cand L720–775, section 1). A fourth @import of the candidate's own /1 sits as loose text at cand L697 — it and its neighbouring lines are the inert fragment block of section 8; the ledger's KB-65 entry records this own-/1 split pair (cand L697 + L711) as a deliberate keep, DISPOSITIONED in the FIX4 mop-up report, which is a different duplication from the basalt-jp pair the mop-up removed.
- **Why:** P4/T9: base delivery comes from the JP distribution (basalt-jp) rather than the EN CDN, and a candidate's own local--code on the draft host is the sanctioned draft-stage form (class (iii)). The frame priority orders the layering (normalize 1 / base / own 3 in the BHL stack convention; here the own layer takes 3 over the basalt base).
- **Verify:** Read orig L1–5 and L780–788 against cand L13–15 and L709–719; `git show f1138e4 -- pages/theme:skipos-jp.txt` and `git show 379eb44 -- pages/theme:skipos-jp.txt` for the repoint and the deduplication; `grep -c '\[\[code' candidate.txt` = 1.
- **Disposition:** The (c3) register's P4 line for this theme reads DISPOSITIONED ("delivery class (ii): original-state CDN delivery"); the bytes supersede it — FIX-P4 repointed the delivery to the JP base candidate, so the current state is the repoint, not the disposition (Per-theme record). The draft-host addresses are class (iii), recorded as not-charged in section 11.

### 4. Fonts and assets

- **What:** The code exhibit's font imports (cand L76–77) are Red Hat Display and Fira Code from fonts.googleapis.com, byte-identical to the original's hosts. The port as imported (d727e92) carried them on fonts.bunny.net; LOCALIZE-B charged that (P5, bunny.net at the lane's L71/L72, "exception-list violation") and FIX4-IWB (5559209) reverted both lines to googleapis — the bunny fix the ledger records (pattern-2 preamble; KB-17: skipos by FIX4-IWB). **The pattern-7 supplement, by contrast, is not in the delivery.** The delivered `:root` (cand L95–97) declares `--header-font-primary: "Red Hat Display"`, `--UI-font-primary: "Fira Code"`, `--mono-font-primary: "Fira Code"` — byte-identical to the original's (orig L196–198), Latin-only. The JP forms (`"Noto Sans JP"`, `"Noto Sans Mono CJK JP"`) occur exactly three times in the file, at cand L678–680, as loose body text after the code exhibit, outside any `[[code]]` or `[[module CSS]]` block, where they cannot take effect; no JP face is loaded anywhere in the candidate (`grep -n 'Noto' candidate.txt` returns only those three lines). The same fragment carries the translated terminal string `content: "端末";` (cand L696) while the delivered rule still reads `content: "Terminal"` (cand L554, = orig L655). Assets: `--desktop-wallpaper` is repointed from the EN page's file (orig L231) to the candidate's own draft-host attachment (cand L130), and the image-block exhibit's skipos.png likewise (cand L22) — the P5 re-hosting form. The `--header-logo` value (cand L111) is an inline SVG data URI; the classifier's HTTP-KEPT derived presence on that line is the known W3C-namespace false fire, not an http asset.
- **Why:** P7/T5 exists because Latin-only stacks leave Japanese text to OS fallback; a supplement that never enters the delivered CSS prevents nothing. KB-16 (font load gap) is the standing pattern for a face named but not loaded; this file is the mirror shape — a face loaded nowhere and named only in inert text. The bunny reversion (KB-17) is the part of the font work the bytes do contain.
- **Verify:** `grep -n 'Noto' candidate.txt` (only L678–680); read cand L95–97 against orig L196–198; `grep -n 'content: "Terminal"' candidate.txt` (L554); `git show 5559209 -- pages/theme:skipos-jp.txt` for what the FIX4-IWB commit actually changed (the bunny reversion and the frame priority — no stack edit).
- **Disposition:** Fonts: bunny reversion FIXED (ledger (c3) P2 preamble / KB-17). P7: the ledger (c3) records FIXED ("font wave"), and the FIX4-IWB execution is the named vehicle in the pattern-7 preamble — **the delivered bytes do not bear the FIXED outcome out**. This package records the item as an open flag (Per-theme record), not as a disposition: no JP face is in any delivered stack, and Japanese body text in this theme falls back exactly as the un-supplemented original's does.

### 5. Header, sidebar, site furniture

- **What:** Header and sidebar rules are carried inside the code exhibit unchanged in shape (the exhibit is 603 lines on both sides). Two furniture items are candidate-side additions: the action-area module (cand L703–706), which gives the opened action-area pane the theme's dark glass ground at every width so pane content stays readable — a JP-environment correction whose rationale is its own comment — and the loose fragment's iOS fixed-background lines (cand L684–686), whose delivered counterparts already exist in the code body (cand L151, `height: 100lvh`, with the original's EN comment), so nothing is lost by their inertness. No P9 header variables are overridden; the theme's `--desktop-time` default ('12:30', cand L129) is the author's specimen value, carried.
- **Why:** P8 adaptation is owed where the JP furniture's structure differs; the action-area pane is such a case and the supplement is scoped to it. Header/title language is out of scope under ruling 2 in any case.
- **Verify:** Read cand L703–706; `grep -n '100lvh' candidate.txt` (L151 delivered, L685 inert fragment).
- **Disposition:** Standing; no furniture item was charged for this theme in any register.

### 6. Text translation

- **What:** The body prose and the surviving exhibits are translated (TRANS-UNANCHORED ×10, TRANSLATION-ANCHORED ×1): the intro and install commands (cand L16–20), the titles collapsible, the tabview with its joke tab names recreated in Japanese (タブレーター, スーパー・メガ・タブ, 超特大・超長尺メガタブII アルティメット: 清算）, the blockquote and table exhibits, and the font-specimen block (which survives without its original `[[=]]` wrapper, cand L69–73). In-CSS text (residue class R1): the code body's comments stay in English (porter-visible only), with one exception that matters — the reader-visible `content: "Terminal"` string at cand L554 is untranslated in the delivery, its translation existing only in the inert fragment (section 4). The translated section comments in the fragment (cand L681–695) likewise never entered the delivered CSS, whose comments remain the original's.
- **Why:** P10: body, usage and sample text are translated, and KB-18 covers reader-visible strings including `content:` — the Terminal string is the one reader-visible string the translation missed in the delivery, and it is recorded with the section 4 flag rather than waved through as comment mass.
- **Verify:** Read orig L12–47 against cand L16–22; `grep -n 'content:' candidate.txt` and compare each string against the original's list.
- **Disposition:** Standing, with the Terminal item carried into the section 4 flag.

### 7. Links

- **What:** The candidate's prose links are the credit block's source link (cand L11, to the EN original — the required ruling-3 back-reference) and the kernel link at cand L21 (`[[[theme:bedrock|Bedrock]]]`, the flag of section 2). The original's link set is the same two shapes. No tag-page or hub links occur.
- **Why:** P11 repoints links to their JP counterparts where the link survives; the kernel link's JP counterpart is the bedrock-jp/basalt-jp line the file itself uses everywhere else, which is the ground of the flag.
- **Verify:** `grep -n '\[\[\[' candidate.txt` (the kernel link is the only triple-bracket prose link outside the credit block).
- **Disposition:** Standing, with the L21 flag recorded in the Per-theme record.

### 8. Structure

- **What:** The CSS body honors the localize.md closing rule in the strongest available form: the code exhibit is 603 lines on both sides with exactly two internal edits (the wallpaper repoint, section 4, and one trailing-space removal, section 9), and its brace depth ends at 0 with minimum 0, matching the original's scan. Four structural changes sit outside it. (a) The wallpaper/time customization exhibit is dropped (orig L36–47: the `skip_box terminal` div exhibiting the `:root` override module): the instruction sentence survives (cand L20) but the exhibit it introduces is gone, so the documented mechanism — override `--desktop-time` / `--desktop-wallpaper` in a module after the include — is stated without its example; the variables themselves remain in the delivered CSS with their defaults. (b) The window/box specimen set is dropped (orig L112–175: the skip_window, anchor/side, skip_box and skip_float specimens with their Lorem ipsum bodies; blocks B8–B11). (c) `[[footnoteblock]]` (orig L110) is dropped while the tab exhibit's `[[footnote]]` survives (cand L42): the candidate page's own footnote has no block to render into, though the delivery's footnote CSS survives. (d) The loose fragment block (cand L678–697) is inserted after the code exhibit, inside the source-code collapsible: the porter's JP-adaptation fragments (the three font-var lines, translated section comments, the iOS height lines, `content: "端末";`, and the self @import) left as body text. Items (a)–(c) happened at creation (d727e92) and were visible to every later check; no register charges them (ledger class I was not raised — the live structure, the CSS body, is intact). Item (d) is the physical form of the section 4 flag.
- **Why:** Residue class R3: a sanctioned replacement and a silent deletion have the same diff shape, so the ground for each is stated. The specimen drops are the population's usual documentation-body compression; the customization exhibit is the one drop that removes instruction, and it is recorded as such. For (d): fragments outside any delivery block are not a supplement form any pattern sanctions; they are recorded here so no reader mistakes them for one.
- **Verify:** `grep -n 'skip_window\|skip_float\|footnoteblock' candidate.txt` (all absent) against original L110–175; read cand L678–697 and note the absence of any enclosing `[[code]]` or `[[module CSS]]` (the structure census in section 3).
- **Disposition:** Standing (restructuring recorded; no checker error arises from it), with item (d) carried into the section 4 flag.

### 9. Formatting only

- **What:** 1 WS-ONLY block (B13): a trailing space removed at a rule opener inside the code body (`#header#header h1 a::before {`, cand L186). 0 re-indentation blocks. The residue block B3 is the dropped `~~~~` separator line between the titles collapsible and the tabview (orig L54), a differ boundary artifact resolved here: a formatting separator in the exhibit stream, dropped with no content consequence.
- **Why:** Formatting-only churn is disclosed as its own class so it is never mistaken for semantic change.
- **Verify:** classification.json (1 WS-ONLY block, reindent_blocks 0); diff.md hunk 3.
- **Disposition:** None required.

### 10. Porter annotations

- **What:** The two appended modules carry English explanatory comments (cand L704, the action-area rationale; cand L721–722, the credit-button DOM-shape rationale) — porter annotations in comment form, inside supplement modules, listed here so they are never mistaken for original content. The loose fragment block (section 8, item d) is porter working text of a different kind and is accounted there. No `[!-- ... --]` translator notes exist (`grep -c '\[!--' candidate.txt` = 0).
- **Why:** R2: porter additions are listed so they are never mistaken for original content or for translation.
- **Verify:** The greps and reads in What.
- **Disposition:** None required.

### 11. Dispositions and exceptions

- **What:** Every finding not fixed in the candidate, in one place. (1) The (c3) P4 disposition ("original-state CDN delivery", class (ii)) — superseded by FIX-P4's repoint; the current bytes are the disposition's opposite (section 3). (2) The render findings: 453/454px@320/375 fixed-width OS-window overflow, the double interwiki-style include with its console error, the cdn.jsdelivr.net / fonts.bunny.net / cdn.scpwiki.com direct links — DISPOSITIONED in (c2) under the coverage caveat (this run returned no machine verdict, render_check exit 2; not a theme defect). The direct links named there are the pre-fix state: the current bytes carry none of those three hosts as delivery (the bunny and CDN lines were repointed by 5559209 and f1138e4). (3) The own-/1 split @import pair (cand L697 + L711): DISPOSITIONED as a deliberate keep in the FIX4 mop-up report (ledger (c4) KB-65 entry). (4) The HTTP-KEPT derived presence (cand L111): a classifier false fire on the W3C namespace string inside the SVG data URI, not an http asset. (5) The draft-host delivery addresses (cand L14, L697, L711, L716): class (iii) draft form, rewritten at posting. The section 4 pattern-7 item is **not** in this list: it is an open flag, not a disposition (Per-theme record).
- **Why:** A disposition is a decision with grounds, not an omission; this section exists so the full set can be audited in one place, and so the one item that is not a disposition is visibly absent from it.
- **Verify:** Each item names its deciding register above; the KB IDs resolve in patterns/ at commit 9c5e9079afb01d30cb9fc4ef9d714e5591eb2ffa.
- **Disposition:** DISPOSITIONED (items 1–5).

### 12. Verification

- **What:** (a) T1 source check, baseline 2026-11-16: exit 1, 8 errors / 1 warn / 1 info (pseudo-ref×6, hotlink×2; T1-ROWS row 39). The pseudo-refs are the self-delivery forms (class (ii) per register (c1)); the hotlinks are the pre-fix bunny/CDN lines. (b) T2/T3 render: FINDINGS, dispositioned in (c2) under the coverage caveat (section 11, item 2); no credit-modal error is recorded for this theme (RENDER-ROWS-1, RENDER-D2). (c) T4 localize plus follow-up: FINDINGS with 1 display-affecting item (LOCALIZE-ROWS row 39, source LOCALIZE-B: the P4 CDN imports); outcomes P3 FIXED / P4 DISPOSITIONED (superseded, section 3) / P5 DISPOSITIONED (class (ii) / KB-58) / P6 FIXED / P7 FIXED (not borne out, section 4). No T4 follow-up diff artifact is recorded for this row; the mirror is the 2026-11-17 refetch at the reference revision. (d) T5: judged jointly with T4 by the source lane. (e) This package is self-verifying: `python3 review/build_review.py --check` regenerates diff.md from the two byte-faithful copies and compares, and re-derives the verdict stamp (which reads STALE for the sweep reason in the Status block). Counts in this README are the classifier's (18 change blocks) and the generator's (diff.md: +148/−168 in 4 hunks).
- **Why:** Verification claims name the cheapest deciding check and its result, not a general assurance.
- **Verify:** Re-run the checker on `pages/theme:skipos-jp.txt`, and `python3 review/build_review.py --check` in this repo.
- **Disposition:** PASS (ledger determination, (b) row 39), with the section 4 flag standing against the current bytes.

## Per-theme record

### The pattern-7 supplement that never entered the delivery (open flag)

The localize lane charged pattern 7 (no JP face) against the port as imported. The ledger's closure chain names FIX4-IWB as the executing wave for skipos's pattern 7, and (c3) records the outcome FIXED. The FIX4-IWB commit's actual diff for this file (5559209) is two edits: the bunny→googleapis reversion in the code exhibit's import lines, and `priority=3` added to the inner frame. Neither touches a font stack. The JP stacks themselves (`"Noto Sans JP"`, `"Noto Sans Mono CJK JP"`) exist in the file only at cand L678–680, as loose text after the `[[/code]]` line, inside the collapsible but outside every delivery block — a form in which Wikidot renders them as visible page text, not as CSS. The delivered `:root` (cand L95–97) is byte-identical to the original's Latin-only stacks, and the delivered `content: "Terminal"` (cand L554) is untranslated while its translation sits in the same inert fragment (cand L696). Conclusion a reviewer can re-derive from this package alone: the pattern-7 charge was closed in the record without the remedy reaching the delivered bytes. This package does not edit the candidate (review packages never do); the flag is recorded here and in the batch report so a future fix lane can land the three stack edits and the one string translation in the code exhibit, where they belong.

### The (c3) P4 disposition superseded by FIX-P4's bytes

Register (c3) closes this theme's P4 item as "DISPOSITIONED (delivery class (ii): original-state CDN delivery)". The file's history shows the opposite outcome: FIX-P4 (f1138e4) repointed both cdn.scpwiki.com imports to theme:basalt-jp's /1, and no later commit restored the CDN form. The disposition language describes the localize charge's adjudication at the time it was written; the wave's bytes overtook it. The same shape occurred in bedrock's record (U-3 batch): a (c3) "dispositioned CDN delivery" closure whose FIX-P4 bytes repointed every delivery line. This package follows the bytes.

### Two different duplications

The FIX4 mop-up (379eb44) removed one line from this file: the second of FIX-P4's two identical basalt-jp @imports. Separately, the ledger's KB-65 entry records a **keep** for this theme: "skipos's own /1 split @import pair" — the self-delivery @import appearing both in the inert fragment (cand L697) and in the tail module (cand L711) — DISPOSITIONED as deliberate in the mop-up report. A reader who conflates the two will misread both the commit and the register; they concern different imports (the base's vs the theme's own).

### Wave attribution in the registers vs the file

The (c3) register credits this theme's P6 to "the frame waves" and its P7 to "the font wave". The file's frames were present from the import (d727e92) — what the waves added was the inner frame's priority (FIX4-IWB). The same FIX4-IWB commit is the "font wave" vehicle, but its font content is the bunny reversion (a pattern-2/KB-17 fix), not a pattern-7 supplement (see the flag above). FIX-P4's subject ("pattern-4 repoint of base-theme CSS imports") likewise does not mention that its diff for this file also normalized the credit translator field (SCP-JP → AI). The registers' outcomes are mostly right; their vehicle names are campaign-level, and this package follows the git record where the two differ.

### Post-package repairs (REFRESH3-G)

- **FIX-U9, landing `f4488f2d2948824238a2d06479f104f4aab0cf5d`** ("pages: skipos delivered channel …", 2026-11-17, R/review-scout/FIX-U9.md item 1): the pattern-7 remedy landed in the delivered channel. The three delivered stacks at refreshed candidate L96–98 now carry the porter's own JP values (`"Noto Sans JP"` in the header stack, `"Noto Sans Mono CJK JP"` in the UI and mono stacks); the delivered string at L555 reads `content: "端末";` (no "Terminal" remains anywhere); and the Noto Sans JP googleapis `@import` was inserted at L78 (HTTP 200, probed once 2026-11-17). "Noto Sans Mono CJK JP" was deliberately not loaded — Google Fonts returns HTTP 400 for it in all three API forms — so the stack names it as the base theme:basalt-jp does (equally unloaded); the inert porter memo (L679–698) was kept whole because it carries a KB-65-dispositioned element and does not duplicate the delivered bytes exactly. The "pattern-7 supplement that never entered the delivery (open flag)" subsection above is the as-built record; the flag is now repaired in the recopied candidate. FIX-U9 item 4 is record-only: the kernel prose link at L21, `[[[theme:bedrock|Bedrock]]]`, belongs to the production-predecessor reference class and was left untouched by the landing. Checker: error 5 / warn 1 / info 1 before and after, finding set identical, class (i) 0.

The regenerated stamp reads `Overall: STALE` against the pre-repair verdict, by design; no re-judgement is fabricated and the frozen GOSIGN2 ledger remains the verdict record.

## Change set outside the two diffed files

The diff covers two files; the port's full change set is larger. (1) `pages/theme:basalt-jp.txt` — the base candidate the head module imports (K5b-3 layering); the original's counterpart delivery was the EN Basalt CDN pair, which is not a file in this repo. (2) `pages/theme-decoration-sample-skipos-jp.txt` — the render sample page (an include of the candidate and of the shared `theme-decoration-sample`); it is the "sample" the T2/T3 checks rendered. (3) The delivery itself: the candidate's own local--code /1 on the draft host, the runtime form of the code exhibit (cand L75–677), named by the tail module and both frames.

## Multi-wave provenance

The candidate's current state is the product of one import and six wave touches: d727e92 imported the port (translation, credit skeleton absent, bunny font forms, both supplement modules, the inert fragment block, the double frame with the inner priority missing); Phase 17 (8dcac74) added the two-field credit skeleton; the gosign2 T1 fixes (b816e10) completed the credit fields; FIX-P4 (f1138e4) repointed the base delivery to basalt-jp (duplicated) and normalized the translator field; FIX4-IWB (5559209) reverted the bunny imports and supplied the inner frame's priority; FIX4-MOPUP (379eb44) removed the duplicated base import; the usage-example sweep (b5cb724) repointed the two exhibit lines to the -jp forms, which is why the stamp reads STALE; and the ledger determination passed the theme with no OPEN items, so the FIX5 wave had nothing to re-judge. Citations, in place of a changelog: GOSIGN2-LEDGER.md (b) row 39, (c1) pseudo-ref and hotlink entries, (c2) skipos entry, (c3) skipos entry and the pattern-2 / pattern-7 / KB-06 / KB-07 / KB-17 / KB-65 preambles; T1-ROWS row 39; LOCALIZE-ROWS row 39; RENDER-ROWS-1 (RENDER-D2) skipos row. The go-sign re-run over that record is what the Status block certifies, subject to the section 4 flag.

## Appendix — residue blocks

The classifier emitted one residue block and seven heuristic blocks; all are resolved, none required a new signature.

- **R1 — B3 (residue; orig L52–54 → cand L32, body → body).** The `~~~~` separator line between the titles collapsible and the tabview, dropped in the candidate. Resolved in section 9 as a formatting separator with no content consequence; the block is a differ boundary artifact around it.
- **R2 — B8–B11 (heuristic; orig L84–175 → cand L53–74, body → body).** The specimen-set region: the wallpaper-customization exhibit, the skip_window/skip_side/skip_box/skip_float specimens and their Lorem ipsum bodies, and the surviving translated exhibits the differ interleaved with them. Resolved in sections 6 and 8: the surviving text is translation (TRANS-UNANCHORED in substance; the classifier's "script delta without the anchor majority" note is the honest label for a region where translation and deletion are mixed line by line), and the deletions are the exhibit drops of section 8.
- **R3 — B14 (heuristic in part; the code-exhibit block).** Its label set (COMMENT-TEXT, CONTENT-STRING, DRAFT-HOST, SELF-DELIVERY, TRANS-UNANCHORED) is resolved across sections 3, 4 and 6: the wallpaper repoint, the "Terminal" string, and the EN comments are each accounted there.
- **R4 — the RATE-EXHIBIT-KEPT-CANDIDATE label on B2 (false fire).** The signature fired on the head region that contains the original's bare Rate, but the candidate side of the block contains no Rate module in any form (`grep -n 'module Rate' candidate.txt` — no hits): the bare Rate was deleted, and the preview credit module is the only rating device. The label stands in classification.json as emitted; this adjudication is the correction of record.
