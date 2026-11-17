# Review package — theme:navla-style-jp

<!-- BEGIN GENERATED VERDICT STAMP — do not hand-edit; regenerate with review/build_review.py -->
## Verdict stamp
- Theme: theme:navla-style-jp — origin KO, population #276 [GOSIGN2-LEDGER (b) row 276]
- Overall: STALE — candidate file changed since the verdict was computed (verdict against 435a6bb-era content, file sha256 now 84ed07ac65de17165915f777ca784d230badc7201710bf48c30a03072595858d); verdict not carried over, re-judgement required
> verdicts below describe the pre-change file
- T1 (source check): FINDINGS (classified) — baseline 2026-11-16: exit 1, 3 errors / 2 warns / 1 info (pseudo-ref×3); standing classes dispositioned in register c1 [T1-ROWS row 280; GOSIGN2-LEDGER (b) row 276]
- T2/T3 (render, combined verdict): FINDINGS — [combined T2/T3] report `FINDINGS` — page runtime-hotlink site-theme chain only; sample credit-modal (preview-form) + runtime-hotlink (no sample overflow); T3 none beyond cross-cutting items. [RENDER-ROWS-2 (RENDER-S2-H (KO6))]
- Engine coverage: full matrix as run by the lane; coverage not separately caveated in the row [RENDER-ROWS-2 row]
- Credit modal: sample credit-modal errors dispositioned preview-form (credit:start-preview has no modal mechanism; GOSIGN-TESTS T2 amendment, 2026-11-16) [RENDER-ROWS-2 (RENDER-S2-H (KO6))]
- T4 (localize patterns + follow-up): FINDINGS — display-affecting findings: 1 [LOCALIZE-ROWS row 275, source LOCALIZE-S2-F]
- T5 (translation text): FINDINGS — the source reports judge T4/T5 jointly; one verdict word covers both [LOCALIZE-ROWS row 275]
- FIX5 re-judgement: none — no OPEN items at the ledger determination [GOSIGN2-LEDGER (b) row 276]
- Computed against: canonical commit 05dd295f2874b21920630066cf955283d2b77d5d; candidate file pages/theme:navla-style-jp.txt sha256:84ed07ac65de17165915f777ca784d230badc7201710bf48c30a03072595858d; record: GOSIGN2-LEDGER.md + GOSIGN2-LEDGER-SUPPLEMENT.md as of the FIX5 head 435a6bb
<!-- END GENERATED VERDICT STAMP -->

## Status

| | |
|---|---|
| Verdict | **PASS** — passed at the ledger determination; this theme had no OPEN items and no §(e) register entry (GOSIGN2-LEDGER (b) row 276) |
| Standing items | **DISPOSITIONED** — T1 pseudo-ref ×3 (posting classes, section 11); the render row's items (runtime-hotlink chain, credit-modal preview form, section 11); T4's component-availability item (P1, section 11). **FIXED** — the interwiki frame (P6, FIX4-IWA). **One defect flag from this package:** both delivery lines name the candidate's code fragment /1, which serves the nine-line variables exhibit; the theme's main CSS is fragment /2 (probe-verified; per-theme record) |
| Go-sign basis | COMPLETION-REPORT.md §10 (go-sign issued; 81 FIXED / 26 DISPOSITIONED / 0 OPEN across the sweep) |
| Named exception | None for this theme (the sweep's single named exception is theme:amethyst-v2, which has no candidate) |

## Provenance

| | Original | Candidate |
|---|---|---|
| Page | theme:navla-style | theme:navla-style-jp |
| Wiki | scpko.wikidot.com | SCP-JP Sigma-10 candidate (canonical repo) |
| Reference revision | 162 (first translation; the candidate's credit block records 初訳時参照リビジョン: 162) | — |
| Source of this copy | Campaign cache `gosign2-lanes/lane-oc-gs-localize-s2-F/orig-navla-style.txt`, via the mirror store (class COPY, hash-verified against review/sources.tsv) | Canonical file `pages/theme:navla-style-jp.txt`, copied at worktree HEAD 2aee861 |
| Lines / bytes | 1,028 lines / 25,708 bytes | 1,143 lines / 32,681 bytes |
| SHA-256 | 7b4083d76c9bf95d576ff854fcd1861d0df0823caad806a7382028b63b8697ce | df8ed275ff1c50072ef4ef6a8e207e0d970fcd811e1242eecd9ad78a76593688 |

Wave history: the candidate was created by the Stage 2 KO6 integration (commit 8dd8c2f); the rework2-p2 pass (c65ec92) swapped embedded bases for references across nine inlined pairs, this theme among the receivers, which is the pass that separated the Navla component into its own page; FIX-CREDIT-D (1869877) normalized its credit attribution; FIX4-IWA (8c62b7b) added the interwiki-style frame the T4 record found missing, and is the candidate's last commit. The companion component's reference revision is its own: component:navla rev 119, recorded in the candidate's exhibit comment.

## Summary

Navla's general-purpose Sigma-9-family design system, the base other Navla themes extend. The original page is almost bare machinery: a gate, one 1,012-line code exhibit holding the whole CSS, a one-line pointer to a separate introduction page, and a tail carrying the component includes and the delivery module. The candidate keeps the CSS body nearly verbatim inside its exhibit (measured churn is +130/−21 in 10 change blocks / 4 hunks) and builds the JP page around it: a head delivery module and frame, the separated Navla component included at the head, the preview credit block with two extra disclosure fields (fonts, image sources), a full translated body (introduction, features, usage, the variables exhibit, customization notes) replacing the original's external introduction page, and a license box for the three image files. Two of the original's mechanisms do not cross: the preset import and the pride-logo include, both dependent on KO-wiki pages, and the candidate discloses both omissions in its own text. One defect flag arises, on the delivery address (per-theme record): the variables exhibit the porters placed ahead of the source exhibit is the page's first code block, so the delivery lines' /1 no longer names the CSS.

## Class summary

Auto-classification by review/classify_hunks.py (signature table 2026-11-17.1): 10 change blocks — 6 specific (60.0%), 2 heuristic (20.0%), 2 residue (20.0%), 0 skipped. Pattern citations below name the KB entry; the patterns/ tree state cited throughout is commit 9c5e9079afb01d30cb9fc4ef9d714e5591eb2ffa.

| Label | Blocks |
|---|---|
| TRANS-UNANCHORED | 4 |
| DRAFT-HOST | 3 |
| COMMENT-TEXT | 2 |
| HEADERVAR | 2 |
| LICENSE-BOX | 2 |
| SELF-DELIVERY | 2 |
| ANNOTATION | 1 |
| CREDIT-PREVIEW | 1 |
| CSS-BODY | 1 |
| EXHIBIT-RESTRUCTURE | 1 |
| IFTAGS | 1 |
| TASL-FIELDS | 1 |

Adjudication for this README (every block was read against the bytes): B1 is the whole head arriving as one block (delivery module, component and sidebar includes, frame, gate, credit block, and the translated body down to the source heading) because the original's corresponding span is a single gate line; its labels are adjudicated in sections 1–6. B2 and B3 are the exhibit head (the porter comment, the `:root` variables with the re-hosted logo and translated header strings, the converted stacks). B5 is a porter comment added inside the CSS (section 10). B10's EXHIBIT-RESTRUCTURE primary is the original's tail machinery (component includes, delivery module, pride-logo include) being replaced by the license box and gate close — adjudicated in sections 2, 3, and 8, not an exhibit change. The 2 residue blocks (B6, B7) are blank-line differences at the exhibit's tail, counted in section 9 and the appendix. After adjudication no block is left unexplained.

## Standing sections

### 0. Header and provenance frame

- **What:** Theme theme:navla-style-jp; original theme:navla-style on scpko at reference revision 162; candidate `pages/theme:navla-style-jp.txt`. Provenance route: derived from the original at the reference revision by the LOCALIZE-S2-F wave (sources.tsv kind: K5b-4 — the candidate ships a companion file in-repo, `component:navla-jp`, the separated Navla component). The frame itself moved: the original opens with its tag gate (original L1) and its code exhibit, and carries its delivery module and component includes at the tail after `[[/iftags]]` (original L1019–1028); the candidate carries the delivery module, the component include, and the frame at the head (candidate L1–12) and the gate after them (candidate L14).
- **Why:** Section 0 declares the provenance route so every later count is read against the right baseline; the gate's tag is P2, the head machinery is sections 2–3.
- **Verify:** The sources.tsv row for navla-style-jp; `sha256sum original.txt` against the Provenance table.
- **Disposition:** Standing (the route itself); the machinery moves are recorded in sections 2–3 and 8.

### 1. Credit and attribution

- **What:** The original carries no credit furniture on this page (no Rate, no info block; the banner comment inside its CSS, "Made by Navla from SCP-KO, 2023", is its attribution). The candidate installs the JP form inside its gate (candidate L15–25): a `:scp-jp:credit:start-preview`/`end-preview` block carrying the eight ruling-3 fields (title ナブラスタイル; 翻訳責任者 AI; 翻訳年 2026; 原題 나블라 스타일 코드; 著作権者 [[*user Navla]]; 作成年 2023; 初訳時参照リビジョン 162; the source link, section 7) plus two disclosure fields the eight do not cover: **フォント** (the four families and their Google Fonts / SIL OFL provenance) and **画像の出典** (the emblem's Wikimedia Commons origin and CC BY-SA 3.0, the Cquote mask, and the SCP_logo.svg bundled with the Navla component). The author field matches the original's banner exactly. A JP license box closes the body (candidate L1125–1142): three entries (SCP_Foundation_emblem.svg, SCP_logo.svg, Cquote1_black.svg), each with author, license, and source. No T7 credit-module CSS sits on this page.
- **Why:** P3/T1 for the credit block; T4 for the license box, whose entries are the per-file half of the credit block's image-source field. The two extra fields are porter disclosure, recorded as such rather than mistaken for ruling-3 fields.
- **Verify:** Read candidate L15–25 against the eight fields and original L3–5 (the banner); read candidate L1125–1142 against the credit block's image field.
- **Disposition:** FIXED (GOSIGN2-LEDGER §(c3): P3 credit fields FIXED, credit waves, checker-verified).

### 2. Includes and components

- **What:** The original's tail includes (original L1019–1028, after the gate) are `:scpko:component:toggle-sidebar`, `:scpko:component:navla` (with `dlc=1|center=1|tocbox={$tocbox}|help={$help}`), and `:scpko:component:pride-logo-by-navla-base` (with the flag parameters). The candidate moves the first two to its head and repoints them: toggle-sidebar to `:scp-jp:component:toggle-sidebar` (candidate L7) and the component to the separated JP port in local form, `[[include component:navla-jp dlc=1|center=1|tocbox={$tocbox}|help={$help}]]` (candidate L5, parameters carried verbatim). The pride-logo include is not carried: the candidate's component list states プライドロゴ — JP版では未収録 (candidate L51), and the mechanism section below records why. The credit pair and the license-box pair complete the candidate's include list; the escaped usage lines name this candidate itself (candidate L58, L64, already in `-jp` form). The candidate's body also documents the separation (candidate L50): the Navla component was split out as `component:navla-jp` and is read by include, localized, with a link to the original's introduction page on scpko.
- **Why:** P1 (KB-15) for the repoints; ruling 4 / T8 for the component: the theme's design-system dependency was ported as its own page (1,040 lines in `pages/`, from component:navla rev 119) rather than left as a foreign include or inlined — the rework2-p2 pass (c65ec92) is the commit that separated it. The pride-logo omission is a disclosed reduction, not a repoint: the component has no JP port and its mechanism is the flag system the customization section records as unsupported.
- **Verify:** `grep -n '\[\[include' candidate.txt` — component, sidebar, frame, credit pair, license-box pair, and the two escaped usage lines; compare original L1019–1028.
- **Disposition:** Repoints applied; the pride-logo omission is a disclosed reduction (sections 8 and 11).

### 3. Delivery and code loading

- **What:** The original delivers from its tail module (original L1022–1026): two `@import`s from scpko.wdfiles.com — its own `local--code/theme:navla-style/1` and the preset page's parameterized `local--code/navla-style-preset-and-custom/{$preset}`. Its census is unambiguous: one `[[code]]` block (original L2–1013), so /1 is the CSS. The candidate replaces the tail module with the head pair: a `[[module CSS]]` importing its own `local--code/theme%3Anavla-style-jp/1` from the draft host (candidate L2), and the frame. **Frame paragraph (the M-frame addition):** the candidate's frame (candidate L9–12) carries `priority=1` with `theme=` naming the same /1 delivery on the production host (`https://scp-jp.wdfiles.com/local--code/theme%3Anavla-style-jp/1`). Priority 1 is the theme's own layer, the only layer this self-contained theme delivers (its component arrives by include, not by the frame). T4 found no frame (LOCALIZE-ROWS row 275, type 6); FIX4-IWA (commit 8c62b7b) installed it, and the ledger records P6 FIXED. **The address itself is this package's defect flag:** the candidate has two `[[code]]` blocks — the nine-line `:root:lang(ja)` variables exhibit (candidate L81–89) ahead of the source exhibit (candidate L96–1121) — so /1 names the variables exhibit, not the CSS. Probe evidence and the full statement are in the per-theme record. The preset import has no candidate counterpart (section 8).
- **Why:** P4/T9 and P6/T3 (KB-07) for the forms; the census rule is the same one section 3 of every package in this campaign applies — a `local--code/<own name>/N` reference must name the block that holds the CSS, and here it does not.
- **Verify:** `grep -n '\[\[code' candidate.txt` — two blocks, L81 and L96; the probe pair is in the per-theme record and re-runnable from the URLs there.
- **Disposition:** FIXED (P6, FIX4-IWA) as to the frame's presence; the /1 address is **flagged as a defect** (per-theme record), not dispositioned; the draft-host import line is DISPOSITIONED (class (iii)) and the frame's production-host form is class (ii).

### 4. Fonts and assets

- **What:** Stacks (block B4): the exhibit's `--text-font` loses "Nanum Gothic" for the JP sans set (`verdana, "Noto Sans JP", "Yu Gothic", "Hiragino Kaku Gothic ProN", Meiryo, …`, candidate L123) and `--title-font` loses 'Unbatang' for `"Noto Serif JP", "Yu Mincho", "Hiragino Mincho ProN", serif` (candidate L124). The load for those faces rides on the companion: the candidate carries no font `@import` of its own, and `component:navla-jp`'s header records that its font direct-links were replaced by Google Fonts loads (the credit block's フォント field, candidate L24, names the set: Noto Serif JP, Noto Sans JP, Nanum Myeongjo, Nanum Gothic Coding — the last two are the companion's faces). The companion include is unconditional at the candidate's head (candidate L5), so the load is present wherever the theme is. Assets: the emblem leaves upload.wikimedia.org for the candidate's own draft-host file area (`--logo-image`, candidate L86 in the variables exhibit and L119 in the source exhibit, file name SCP_Foundation_emblem.svg unchanged), with its provenance disclosed in the credit block and the license box (section 1); the SCP_logo.svg and Cquote mask are re-hosted with the companion.
- **Why:** P7/T5 with KB-16: the KO faces cannot render Japanese text; the stacks land on the JP faces, and the load is carried by the component the theme cannot be used without — a dependency this section states rather than hides, since a future editor who removes the companion include removes the fonts too. P5/KB-17 for the emblem's re-hosting (the original hotlinked Wikimedia Commons; the JP form stores the file in the theme's own area with its CC BY-SA 3.0 provenance recorded).
- **Verify:** `grep -n 'font-family\|--text-font\|--title-font' candidate.txt` — the two stacks; `grep -n 'wikimedia' candidate.txt` returns only the license and credit provenance lines, no live reference.
- **Disposition:** Conversions applied; the draft-host asset URLs are DISPOSITIONED (class (iii) draft form).

### 5. Header, sidebar, and site furniture

- **What:** The exhibit's `:root` sets the header tokens (blocks B2–B3): `--logo-image` (section 4), `--header-title: "SCP財団"` and `--header-subtitle: "確保、収容、保護"` (candidate L120–121) — the original's "SCP 재단" and "확보, 격리, 보호" translated, the subtitle taking the JP motto's established form (収容 for 격리). The variables exhibit ahead of the source exhibit (candidate L81–89) restates the same five tokens as the customization surface, with JP comments. The sidebar arrives through the toggle-sidebar include (section 2); the theme's own furniture rules travel verbatim inside the exhibit.
- **Why:** P9/T6 applied, not dispositioned: the header strings were translated, so KB-57 and ruling 2 are not engaged. The `:root:lang(ja)` scoping of the variables exhibit is the theme's own design (the T4 record singles it out as the batch's best), keeping the JP token set addressable as a layer.
- **Verify:** Read candidate L113–124 against original L6–19.
- **Disposition:** Standing.

### 6. Text translation

- **What:** The original has almost no body to translate — its documentation lives on a separate introduction page, pointed to by one line inside the gate (original L1016). The candidate replaces that pointer with the full JP body on this page (candidate L27–93): the introduction （これは何？), the feature list with its footnotes, the design principles, the component list, the usage section with its argument table (tocbox, help), the variables section, and the customization notes — translated and adapted from the introduction material, with the original's pages linked where a reader needs them (the component introduction and the preset/custom page on scpko, candidate L50 and L68, the latter glossed （韓国語）). Inside the exhibit, the CSS comments are carried in Korean where they are the author's own header text and translated where they instruct (the variables exhibit's comments are JP throughout). One in-CSS porter comment is added (block B5, section 10). Korean survives in the candidate in the credit block's original-title field (candidate L19), the exhibit's author banner (candidate L103–105, a quotation), and the linked-page titles quoted in prose.
- **Why:** P10: the body is the port's purpose, and consolidating the introduction onto the theme page is what makes the candidate self-documenting in the way the JP population's other candidates are. KB-18's reader-visible test is met outside the recorded quotations.
- **Verify:** Read candidate L27–93; a Hangul scan of candidate.txt returns the credit field, the banner, and quoted titles only.
- **Disposition:** Standing (the port itself).

### 7. Links

- **What:** The credit block's source link (candidate L23) names `https://scpko.wikidot.com/theme:navla-style` — the host review/sources.tsv records for the original, and the page this package's mirror was taken from; no host defect. The body's branch links name scpko pages deliberately: the Navla component introduction (candidate L50) and the preset-and-custom page (candidate L68, glossed （韓国語）) — both are the original's own documentation pages, kept as serving originals because the JP side has no counterpart pages for them (the preset page's mechanism is not ported, section 8). The toggle-sidebar component link (candidate L39) names the scp-jp production page for the JP component.
- **Why:** P11: prose links take the JP counterpart or the serving original; the two scpko links document mechanisms and material that exist only on the branch, and the candidate says so in the surrounding text rather than leaving the reader to discover it.
- **Verify:** `grep -n 'wikidot.com' candidate.txt` — the source link, the two scpko documentation links, the scp-jp component link, and the delivery hosts of section 3.
- **Disposition:** Standing.

### 8. Structure

- **What:** Three structural facts, each named. (1) The CSS body is preserved: variable names, selectors, and rule order inside the exhibit match the original's code block, and a brace-depth scan of the candidate closes at depth 0 with no negative excursion; the one deliberate in-body edit is the `.ko-footer` comment (section 10), which adds a comment and changes no rule — the dead rule it annotates is kept, as the comment says, to preserve the original's structure. (2) The tail machinery moved to the head (sections 2–3): the component and sidebar includes and the delivery lines sit before the gate in the candidate, after it in the original — the campaign's standard head form, not an interleaved edit. (3) Two original mechanisms are not carried, both disclosed in the candidate's own text: the preset import (`local--code/navla-style-preset-and-custom/{$preset}`, original L1025) — the candidate's 訳注 (candidate L64) and customization section state that `preset` and `flag` are unsupported on the JP side because they depend on KO-wiki pages, and offer variable redeclaration as the equivalent customization route; and the pride-logo include (original L1028), stated as not included in the JP version (candidate L51). These are disclosed reductions with their grounds in-file; they are recorded here so the disclosure, not a skim, is what a reviewer relies on.
- **Why:** R3's distinction (sanctioned replacement vs silent deletion) is met by the disclosures themselves: a reduction the candidate announces, with the reason, is a documented scope decision; the same reduction unannounced would be a class I item. The ledger's P1 DISPOSITIONED line covers the dependency family these mechanisms belong to (posting-procedure / branch-dependency class).
- **Verify:** Compare the exhibit rule sequence (candidate L96–1121) with original L2–1013; read candidate L41 and L62 for the two disclosures.
- **Disposition:** Standing, with the two reductions recorded as disclosed scope (section 11).

### 9. Formatting only

- **What:** The 2 residue blocks (B6, B7) are blank-line differences at the exhibit's tail: the candidate carries one more blank line before `[[/code]]` than the original (candidate L1119–1122 against original L1012–1013). The classifier finds no re-indentation (0), so the R7 follow-up-diff hazard is not triggered.
- **Why:** Formatting churn is disclosed as its own class so it is never mistaken for a semantic change.
- **Verify:** The exhibit tails in diff.md.
- **Disposition:** None required.

### 10. Porter annotations

- **What:** Three annotations. (1) The exhibit's head comment (candidate L97–106): the port provenance block, naming the theme, both reference revisions (theme:navla-style rev 162 / component:navla rev 119), the component's separation, and the font/asset hosting substitution — it rides inside B2, ahead of the author's own banner, which is carried verbatim below it. (2) The in-CSS comment at candidate L630–631 (block B5): explains that `.ko-footer` is an SCP-KO footer class with no SCP-JP counterpart element, that the rule is kept to preserve the original's structure, and that the selector is a dead rule (an empty set) in the original too — the only in-body annotation, and the reason section 8 can call the body preserved with one named exception. (3) The 訳注 at candidate L64 (the preset/flag non-support note, section 8), marked as a translator's note in the text itself.
- **Why:** R2: porter-added text is part of the change record; annotation (1) is load-bearing — it is the only in-file statement of the component's separate revision, and annotation (2) is the only explanation of a kept dead rule.
- **Verify:** Read candidate L97–106, L630–631, and L64.
- **Disposition:** Standing.

### 11. Dispositions and exceptions

- **What:** Four items, each with its ground. (1) T1's three pseudo-ref errors: the candidate's references to not-yet-posted JP addresses (the two delivery lines and the companion include among them) — classes (ii)/(iii) by form; the posting procedure resolves them, and fix lanes never "fix" them in the candidate. (2) T4's type-1 finding: at T4's measurement, `component:navla-jp` returned 404 on scp-jp — the theme's design-system dependency missing at posting is a blocker-class item. The component candidate exists in this repo (`pages/component:navla-jp.txt`, 1,040 lines, ported with the theme under ruling 4) and posts with the theme; the ledger dispositions the family P1 (posting-procedure convention class). The finding is recorded here so the dependency chain is visible. (3) The render row's items, all environment-layer, not charged to the candidate: the page's and sample's runtime-hotlink site-theme chain (KB-40) and the sample's credit-modal errors (KB-32, ruling 5). (4) The two disclosed mechanism reductions of section 8 (preset import, pride-logo include), recorded with their in-file disclosures. **Not a disposition:** the delivery address flag of section 3 — it is a defect in the candidate's bytes, recorded in the per-theme record with probe evidence, and this package makes no edit. The ledger's determination for this theme is PASS; the flag postdates the verdict's evidence, because the render checks' sample did not expose it (the companion's design-system CSS carries much of the page's appearance, which is how a nine-line own-layer delivery went unnoticed).
- **Why:** A disposition is a decision with grounds (AGENTS.md §3 classes (i)/(ii)/(iii); the named KB entries), not an omission; a byte-level defect is flagged, never dispositioned by relabeling.
- **Verify:** Each item names its deciding record above; the ledger §(c3) line for this theme reads P1 DISPOSITIONED / P6 FIXED.
- **Disposition:** DISPOSITIONED (items 1–4); the delivery address is flagged, not dispositioned.

### 12. Verification

- **What:** (a) T1 source check (T1-ROWS row 280): exit 1, 3 errors / 2 warns / 1 info; all three errors are pseudo-ref, classes (ii)/(iii); there is no class (i) error. (b) T2/T3 render (RENDER-ROWS-2, lane RENDER-S2-H (KO6)): FINDINGS, the items of section 11(3), all dispositioned; engine coverage as run by the lane, not separately caveated in its row. (c) T4/T5 (LOCALIZE-ROWS row 275): FINDINGS jointly, display-affecting findings 1 (the component's posting availability); the same row praises the translation, disclosure, and `:root:lang(ja)` design as the batch's best, and the ledger §(c3) line records P1 DISPOSITIONED and the frame FIXED. (d) This package is self-verifying: `python3 review/build_review.py --check` regenerates diff.md and the verdict stamp from the two byte-faithful copies in this directory and compares. Counts in this README are the generator's (difflib, autojunk off): +130/−21 in 10 change blocks / 4 hunks; the brace-depth scan and the delivery probe of section 8 and the per-theme record were run for this package.
- **Why:** Verification claims name the cheapest deciding check and its result, not a general assurance.
- **Verify:** Re-run the checker on `pages/theme:navla-style-jp.txt`, `python3 review/build_review.py --check` in this repo, and the probe pair in the per-theme record.
- **Disposition:** PASS (GOSIGN2-LEDGER (b) row 276; go-sign, COMPLETION-REPORT §10) — with this package's delivery flag standing against the candidate's current bytes.

## Per-theme record

### The delivery address names the wrong code block (defect flag, probe-verified)

The candidate's two delivery lines — the head module's `@import` (candidate L2, draft host) and the frame's `theme=` (candidate L11, production host) — both name `local--code/theme%3Anavla-style-jp/1`. The candidate has two `[[code]]` blocks: the nine-line `:root:lang(ja)` variables exhibit (candidate L81–89), placed by the porters ahead of the source exhibit as the customization summary, and the source exhibit itself (candidate L96–1121). Fragment /1 is therefore the variables exhibit, and fragment /2 is the theme's CSS. Probe made for this package (2026-11-17, draft host, the host the head import names): `https://sigma10-jp-test.wdfiles.com/local--code/theme%3Anavla-style-jp/1` serves 586 bytes — the `:root:lang(ja)` variable block and nothing else; `/2` serves 26,146 bytes opening with the exhibit's porter comment and the full stylesheet. In the original there is one code block, so its /1 was correct; the port's added exhibit renumbered the fragments and the delivery lines were not updated. The consequence at posting: a page applying this theme receives the five variable declarations and none of the theme's rules (the companion component's design-system CSS still arrives by include, which is the likely reason the render checks, whose sample leans on the same component, recorded no unstyled finding). The repair is a one-token change in two lines (/1 → /2 in candidate L2 and L11) or a reordering of the exhibits; this package makes neither edit, per the review protocol — it flags the defect with the evidence for the coordinator's fix lane, in the same family as the enlightened-eyes delivery flag recorded by the M-pure-4 batch.

### The repair has landed — FIX-NAVLA, canonical commit 05dd295

The flagged defect was repaired by FIX-NAVLA (report `R/review-scout/FIX-NAVLA.md`, item 1), landed in canonical commit `05dd295f2874b21920630066cf955283d2b77d5d` ("review+pages: U-7 and R-fix-3 packages; foundom, navla, 07k repairs", 2026-11-17). The repair is exactly the two-address change the flag anticipated, and nothing else: on the current candidate the head module's `@import` (candidate L2) and the interwiki-style frame's `theme=` (candidate L11) both read `local--code/theme%3Anavla-style-jp/2` rather than `/1`. FIX-NAVLA probed both fragment addresses on the draft host (`/1` → 586 B, the variables exhibit; `/2` → 26,146 B, the full stylesheet) and re-ran the T1 checker with the finding set unchanged apart from the L2 pseudo-ref now naming /2; class (i) errors 0 before and after. The report's item 2 re-sweep found the same mechanism in broken-light, gp-refresh, starbasalt and sound; the three in this slice are repaired below/alongside. This package was rebuilt from the post-repair canonical bytes: `candidate.txt` recopied from `pages/theme:navla-style-jp.txt`, `diff.md` and the stamp regenerated against them. The regenerated stamp reads STALE with the current file sha256 — no re-judgement is fabricated and the frozen GOSIGN2 ledger remains the verdict record; the STALE word is the generator's honest statement that the verdict was computed against the pre-repair file.

## Change set outside the two diffed files

The diff covers two files; this port's record is three files larger. `pages/component:navla-jp.txt` (1,040 lines) is the JP port of `:scpko:component:navla` (rev 119), ported with the theme under ruling 4 and separated by the rework2-p2 pass: it carries the design-system CSS the theme depends on, the Google Fonts loads section 4 rides on, and its own header comment recording its provenance and its one judgment call (the original component's conditional Free DLC / Center sections are applied unconditionally, because the cached original does not preserve the conditional split). `pages/theme-decoration-sample-navla-style-jp.txt` is the decoration sample the render checks ran against (its findings are the sample half of section 11(3)). One inbound dependent is recorded in its own package: theme:doap-nvl-jp layers over this candidate (its sources.tsv row states the layering; the doap-nvl package's diff covers that theme's own layer only), so this candidate's delivery addresses are load-bearing for two themes, which is part of why the flag above matters. There are no other companion fragments and no inbound-link repairs in other candidates for this theme.

## Appendix — residue blocks

| Block | Shape | Adjudication |
|---|---|---|
| B6 | orig L1012 → cand L1119–1120, blank-line difference at the exhibit tail | Formatting only (section 9) |
| B7 | orig L1013 → cand L1121–1122, blank-line difference at the exhibit tail | Formatting only (section 9) |
