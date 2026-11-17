# Review package — theme:5k-jp (EN → JP port)

<!-- BEGIN GENERATED VERDICT STAMP — do not hand-edit; regenerate with review/build_review.py -->
## Verdict stamp
- Theme: theme:5k-jp — origin EN, population #48 [GOSIGN2-LEDGER (b) row 48]
- Overall: PASS — passed at the ledger determination; no OPEN items [GOSIGN2-LEDGER (b) row 48]
- T1 (source check): FINDINGS (classified) — baseline 2026-11-16: exit 1, 4 errors / 1 warn / 1 info (hotlink×3, unencoded-colon×1); standing classes dispositioned in register c1 [T1-ROWS row 48; GOSIGN2-LEDGER (b) row 48]
- T2/T3 (render, combined verdict): FINDINGS — [combined T2/T3] report `FINDINGS` — candidate-inherent page-overflow 435–437px@320/375 (page) and 1489px@1366 / 789px@768 (sample); hidden-rate by design (no Rate module). [RENDER-ROWS-1 (RENDER-S2-A)]
- Engine coverage: full matrix as run by the lane; coverage not separately caveated in the row [RENDER-ROWS-1 row]
- Credit modal: no credit-modal line in this theme's row; no sample credit-modal error recorded [RENDER-ROWS-1 (RENDER-S2-A)]
- T4 (localize patterns + follow-up): FINDINGS — display-affecting findings: 4 [LOCALIZE-ROWS row 48, source LOCALIZE-S2-A]
- T5 (translation text): FINDINGS — the source reports judge T4/T5 jointly; one verdict word covers both [LOCALIZE-ROWS row 48]
- FIX5 re-judgement: none — no OPEN items at the ledger determination [GOSIGN2-LEDGER (b) row 48]
- Computed against: canonical commit f931619f42a4bfbf6f0962b6c0756217e6991c58; candidate file pages/theme:5k-jp.txt sha256:7263313ea50bd1cb450f8cbb1c571ddd8528804ce23aea4341f3de8cf3e8132d; record: GOSIGN2-LEDGER.md + GOSIGN2-LEDGER-SUPPLEMENT.md as of the FIX5 head 435a6bb
<!-- END GENERATED VERDICT STAMP -->

## Status

| | |
|---|---|
| Verdict | **PASS** — passed at the ledger determination; this theme had no OPEN items and no §(e) register entry (GOSIGN2-LEDGER (b) row 48) |
| Standing items | **DISPOSITIONED** — T1 hotlink ×3 (class (ii)) and the single unencoded-colon (KB-01's own 5k precedent, section 11); the render row's overflow and hidden-rate items (KB-37 / KB-50, section 11); T4's four findings dispositioned per the ledger (c3) line and FIX3-S2EN §6.11 (section 11) |
| Go-sign basis | COMPLETION-REPORT.md §10 (go-sign issued; 81 FIXED / 26 DISPOSITIONED / 0 OPEN across the sweep) |
| Named exception | None for this theme (the sweep's single named exception is theme:amethyst-v2, which has no candidate) |

## Provenance

| | Original | Candidate |
|---|---|---|
| Page | theme:5k | theme:5k-jp |
| Wiki | scp-wiki.wikidot.com | SCP-JP Sigma-10 candidate (canonical repo) |
| Reference revision | 13 (the candidate's credit block records 初訳時参照リビジョン: 13) | — |
| Source of this copy | Campaign cache `gosign2-lanes/lane-oc-gs-localize-s2-A/orig-5k.txt`, via the mirror store (class COPY, hash-verified against review/sources.tsv) | Canonical file `pages/theme:5k-jp.txt`, copied at worktree HEAD 1605bbd |
| Lines / bytes | 306 lines / 6,954 bytes | 213 lines / 5,612 bytes |
| SHA-256 | e95f93a9fce1541042c318eb2ce2979162bd14fe727a1d60a084747aa874325f | 7263313ea50bd1cb450f8cbb1c571ddd8528804ce23aea4341f3de8cf3e8132d |

Wave history: the candidate was created by the Stage 2 EN batch 1 wave (commit 3205f27); the rework2-p1 pass (95fd1d1, base-delivery restoration) and FIX2-COLON (f931619, the stamp's computed-against commit) touched it later. The original was superseded upstream after revision 13; a follow-up diff artifact (`diff-5k-from13.txt`) is held in the campaign record (K5a-i, per review/sources.tsv).

## Summary

A small Basalt reskin for the SCP: 5K contest, and the batch's clearest case of a port whose interesting content is in its exceptions. The mechanical part is standard: the hidden basalt include is swapped to theme:basalt-jp, the head gains the frame, the gate, and the preview credit block, the two bunny.net font loads are deleted, and the original's exhibit body is dropped (section 8). The judgment calls are three, and each is documented where it sits: two `local--files` colons were encoded (KB-01) while a third, in a collaborator's file address, was deliberately left unencoded under KB-01's own 5k precedent because the encoded form does not serve (section 4); the AREA-12 variant, whose gate in the original is an escaped joke and therefore inert, is applied unconditionally as the original effectively applies it (section 8); and the Barlow stack keeps its family name with Noto Sans JP appended after its load was cut (section 4). Measured churn (diff.md, the generator's difflib count with autojunk off: +30/−123, 153 changed lines in 11 change blocks / 7 hunks; a GNU-diff count of the same pair gives 155 changed lines — the difference is alignment choice, not content).

## Class summary

Auto-classification by review/classify_hunks.py (signature table 2026-11-17.1): 11 change blocks — 9 specific (81.8%), 1 heuristic (9.1%), 1 residue (9.1%), 0 skipped. Pattern citations below name the KB entry; the patterns/ tree state cited throughout is commit 9c5e9079afb01d30cb9fc4ef9d714e5591eb2ffa.

| Label | Blocks |
|---|---|
| IFTAGS | 3 |
| COLON-ENC | 2 |
| BARE-RATE-DEL | 1 |
| COMPONENT-SWAP | 1 |
| CREDIT-PREVIEW | 1 |
| CSS-BODY | 1 |
| DRAFT-HOST | 1 |
| EXHIBIT-RESTRUCTURE | 1 |
| INCLUDE-REPOINT | 1 |
| JPFONT-LOAD | 1 |
| JPFONT-STACK | 1 |
| SELF-DELIVERY | 1 |
| TASL-FIELDS | 1 |
| TRANS-UNANCHORED | 1 |
| WS-ONLY | 1 |

Adjudication for this README (every block was read against the bytes): the heuristic CSS-BODY block (B4) is the deletion of the two bunny.net `@import` lines, a font-supply cut, and is narrated in section 4, not left as churn. The residue block (B10, original L194–195 → candidate L210) is the merged variant module's tail — a closing-brace and blank-line pair, formatting only (section 9). The EXHIBIT-RESTRUCTURE primary (B11) is the exhibit-body drop of section 8, sharing its block with the bare-Rate deletion (section 1). After adjudication no block is left unexplained.

## Standing sections

### 0. Header and provenance frame

- **What:** Theme theme:5k-jp; original theme:5k on scp-wiki at reference revision 13; candidate `pages/theme:5k-jp.txt`. Provenance route: derived from the original at the reference revision by the Stage 2 EN batch 1 wave (sources.tsv kind: standard; the candidate layers over theme:basalt-jp by include, section 3, but carries its own layer in full, so no K5b composition applies; no production JP counterpart exists, so the R4 adoption question does not arise). The frame order is new: the original opens with the hidden basalt include (original L1–3) and goes straight into its CSS module; the candidate keeps that include first (candidate L1–3), then adds the interwiki-style frame (L5–8) and the localized gate (L10) ahead of the credit block.
- **Why:** Section 0 declares the provenance route so every later count is read against the right baseline; the gate's tag is P2, the frame is P6/T3 (section 3).
- **Verify:** The sources.tsv row for 5k-jp; `sha256sum original.txt` against the Provenance table.
- **Disposition:** Standing (the route itself); the gate and frame changes are recorded in section 3.

### 1. Credit and attribution

- **What:** The original carries no credit block in its head; its credit furniture is the bare `[[module Rate]]` inside the body (original L203, with a second exhibit Rate at L296). The candidate installs the JP form at the head: a `:scp-jp:credit:start-preview`/`end-preview` block (candidate L12–23) carrying the eight ruling-3 fields (タイトル 5Kテーマ; 翻訳責任者 AI; 翻訳年 2026; 原題 5K Theme; 著作権者 Liryn; 作成年 2023; 初訳時参照リビジョン 13; the source link, candidate L20, naming `scp-wiki.wikidot.com/theme:5k` — the original's recorded host). Both bare Rates fell with the body (block B11; the L296 one is a labelled exhibit Rate, deleted with its exhibit, section 8). No credit-module CSS supplement was added (no `.creditButton`/`.creditRate` rules in the candidate; the base carries the family's styling). License box (T4): neither side carries one. One prose-record tension is stated openly: the localize row notes the credit's co-author question (the theme's own banner, carried inside the candidate's CSS at L31–35, credits "Liryn & Placeholder McD", while the credit block's 著作権者 field names Liryn alone); the ledger (c3) line dispositions the row's credit charges under "credit fields FIXED by the credit waves", and the banner line in the bytes still names both authors, so the co-authorship is on the face of the file even though the field names one.
- **Why:** P3/T1: the preview credit module is the rate-bearing JP form, so a bare Rate is deleted rather than duplicated (KB-09). Ruling 3 fixes the eight fields; the single-author field follows the original page's own attribution line (the info the original publishes names Liryn's theme; the banner is the base family's credit line, Liryn & Placeholder McD being Basalt's authors as much as this reskin's).
- **Verify:** `grep -n 'module Rate' candidate.txt` returns nothing; read candidate L12–23 against the eight fields; the banner at candidate L31–35.
- **Disposition:** FIXED (GOSIGN2-LEDGER §(c3): credit fields FIXED by the credit waves); the co-author note is recorded here as the row left it.

### 2. Includes and components

- **What:** One swap (B1, COMPONENT-SWAP with INCLUDE-REPOINT): the hidden delivery include at the head, `:scp-wiki:theme:basalt` → `theme:basalt-jp`, parameters unchanged (`darkmode=a|wide=a`, original L2 → candidate L2). The credit includes (section 1) and the interwiki-style include (section 3) complete the candidate's include list; the usage exhibit naming `:scp-wiki:theme:5k` fell with the body (section 8), and the surviving usage line names the candidate itself (candidate L25).
- **Why:** P1 (KB-15) and T8 (component swap to the JP port, ruling 4): the base theme is the dependency, its JP port exists and is the campaign's own candidate, so the include names it. The swap is the port's load-bearing include change; everything else follows from it.
- **Verify:** `grep -n '\[\[include' candidate.txt` — the basalt-jp include, the frame, the credit pair, and the usage line naming theme:5k-jp.
- **Disposition:** Applied; no foreign include kept, no named exception needed.

### 3. Delivery and code loading

- **What:** The original delivers its own CSS in two `[[module CSS]]` blocks (original L5–161 and L166–196, the second being the AREA-12 variant) and takes its base from the hidden include. The candidate keeps that shape with three changes: the base include is swapped (section 2); the head gains the interwiki-style frame at priority 1 with `theme=` naming the candidate's own `local--code/theme%3A5k-jp/1` on the draft host (candidate L5–8, SELF-DELIVERY/DRAFT-HOST in B2); and the two modules are merged into one (candidate L28–211) with the variant's `:root` carried in the same module (candidate L183–203; its gate is section 8's item). The candidate holds no `[[code]]` block; its first module is the /1 delivery the frame names.
- **Why:** P6/T3 (the interwiki-style frame, priority 1 for the theme's own layer) and P4 (own-code delivery from the JP side). The draft-host form of the frame line is KB-41, class (iii): sanctioned at draft stage, rewritten to the production host at posting. Merging the modules follows the closing rule's JP-form convention for this wave (one delivery unit per candidate); the variant's content is preserved entire, only its container changed.
- **Verify:** `grep -n 'module CSS\|local--code' candidate.txt` — one module, one frame line; compare original L5 and L166.
- **Disposition:** DISPOSITIONED (the draft-host frame line, class (iii)).

### 4. Fonts and assets

- **What:** Loads: the original imports Barlow and Saira from `fonts.bunny.net` (original L16–17). Both imports are deleted (B4, adjudicated from CSS-BODY), and a Google Fonts `@import` for Noto Sans JP (400;700) is added at the merged module's head (candidate L30, B3, JPFONT-LOAD). Stacks: the one literal stack that names a cut face, `.metam`'s `'Barlow', sans-serif` (original L66), becomes `'Barlow', "Noto Sans JP", sans-serif` (candidate L88, B7, JPFONT-STACK) — the family name is kept (it is the theme's design face and the base may supply it) and the JP family is appended as the rendering fallback for Japanese. The `--UI-font-primary: 'Saira'` variable (original L34) is retained unchanged (candidate L56); its load is gone, so the variable resolves through the base's `--UI-font` stack wherever it is used (candidate L84, L102, L122 use `var(--UI-font)`). Colons (KB-01): the `--logo` address's page-name colon is encoded in both `:root` blocks, `theme:5k` → `theme%3A5k` (original L25 → candidate L47, B5; original L169 → candidate L185, B9), repaired by FIX2-COLON (f931619). Assets: three `url()`s stay on foreign hosts — the logo (candidate L47 and L185, `scp-wiki.wikidot.com/local--files/theme%3A5k/a12-logo.webp`) and the memo logo (candidate L100, `smlt.wdfiles.com/local--files/collab:dr-moist:theatre/O4`, a collaborator's file); they are T1's three hotlink errors.
- **Why:** P5: only storage, Google Fonts, BootstrapCDN, and cdnjs may be hotlinked, so the bunny.net loads could not stay regardless of supply; the localize row's "supply cut" (供給断絶) is the same fact from the availability side. P7/T5 with KB-16: the JP load and the appended fallback are what render Japanese. KB-01 for the colons, with the 5k precedent stated in section 11 for the one address that was NOT encoded.
- **Verify:** `grep -n '@import\|font-family' candidate.txt` against the list above; `grep -n 'theme%3A5k\|collab:dr-moist' candidate.txt` for the two colon forms.
- **Disposition:** Font loads and stacks applied; the three foreign-host asset URLs are DISPOSITIONED (class (ii), KB-17/KB-58 form).

### 5. Header, sidebar, and site furniture

- **What:** The theme's header variables are carried in its `:root` blocks: `--title: "SCP: 5K"` (candidate L50) and, in the variant block, `--header-title: "AREA-12"` (candidate L187), both in English as in the original. No `--header-subtitle` or `--logo-image` override beyond the `--logo` variable of section 4. No sidebar or topbar adaptation was needed; the furniture is the base's, and the theme's own rules needed no structural change to sit on basalt-jp.
- **Why:** P9/T6 would name a header change; here the values were kept in the original's language, which is ruling 2 territory, dispositioned in the ledger (c3) line. KB-57 is the standing form of that disposition.
- **Verify:** `grep -n -- '--header-title\|--title:' candidate.txt` — the two lines above.
- **Disposition:** DISPOSITIONED (header language, ruling 2).

### 6. Text translation

- **What:** One TRANS-UNANCHORED block in the head supplement (B2's prose half): the candidate's body prose is the one-sentence description (candidate L24), the usage line (L25), and the base note (L26–27, which explains the basalt-jp layering in Japanese — a porter-written explanation with no original counterpart, counted here as translation-adjacent body text and in section 10's check). The original's body prose (the Info section naming the SCP: 5K game and its makers, original L219 ff.) was not translated into the candidate; it fell with the exhibit body (section 8). R1 (in-CSS text): the CSS banner comments are the base family's own English credit lines, carried unchanged (candidate L31–35). R5: none — the source is English.
- **Why:** P10 covers what was translated; the remainder is the body-shape decision charged to section 8 (R3), not a translation gap.
- **Verify:** Read candidate L24–27; the Info section's absence is diff.md's B11 section.
- **Disposition:** Standing for the translated head; the exhibit body is section 8's item.

### 7. Links

- **What:** The candidate's one live outbound prose link is the credit block's source link (candidate L20), naming `https://scp-wiki.wikidot.com/theme:5k` — the original's recorded host in review/sources.tsv, the host the mirror was taken from. The original Info section's outbound links (the game studio and the SCP: 5K site, original L221–223) fell with the body. The asset `url()`s are section 4's, not prose links.
- **Why:** P11: prose links take the JP counterpart or the serving original, under the dead-reference evidence standard; the source link meets it on the recorded host.
- **Verify:** `grep -n 'wikidot.com' candidate.txt` — the source link and the two logo URLs.
- **Disposition:** Standing; no dead link carried.

### 8. Structure

- **What:** Two adjudications. First, the AREA-12 variant's gate: in the original, the variant module (original L166–196) is preceded by an escaped joke gate, `>[[ift{$area-12}gs -liryn-was-here]]` and `>[[iftags]]` (original L164–165, with the closing pair escaped at L197–198) — blockquote-escaped, therefore inert, so the variant already applies unconditionally in the original's effective behavior. The candidate carries the variant's `:root` inside the single merged module with no gate (candidate L183–203), and B8 is the boundary block where the escaped gate lines fall. The localize row flags the unconditional form as requiring staff approval; the bytes show the approval question is about a form the original itself never enforced, and the ledger (c3) line dispositions the row's charges. Second, the exhibit body: the original's body after the CSS (original L200–304: the Rate, the logo and usage exhibits, the Info section, the Area-12 Variant usage section, a second exhibit Rate) has no counterpart in the candidate, whose body is the credit block plus three lines (candidate L24–27). B11 is the deletion block; the exhibit census is the same shape as theme:512-onwards-jp's (section 8 of that package): the demonstrated CSS survives entire in the merged module, the loss is documentation prose, and no campaign record names the drop.
- **Why:** The closing rule (variable names, selectors, channel order preserved; corrections appended) is deviated from in the module merge, and the deviation is named here rather than hidden in a block count. R3 forces the exhibit adjudication: dropped, not replaced, with the ground stated. For the variant gate, the deciding evidence is the original's own escaped gate lines — an inert gate is not a condition, so carrying the variant unconditionally preserves the original's behavior rather than changing it.
- **Verify:** Read original L163–199 against candidate L182–213; `grep -n '^+ ' original.txt candidate.txt` for the body census.
- **Disposition:** The variant form DISPOSITIONED (ledger (c3) class outcomes; the inert-gate evidence above); the exhibit drop recorded as an R3 drop, not charged against the determination, and not hidden.

### 9. Formatting only

- **What:** One WS-ONLY block (B6, original L43–44 → candidate L65–66) and the residue tail B10 (original L194–195 → candidate L210, the merged module's closing brace and blank line). The classifier finds no re-indentation (0 blocks pair up after leading-whitespace normalization), so the R7 hazard is not triggered.
- **Why:** Formatting churn is disclosed as its own class so it is never mistaken for a semantic change, and so a reviewer can skip it safely.
- **Verify:** The two blocks in diff.md.
- **Disposition:** None required.

### 10. Porter annotations

- **What:** One porter-written text: the base note in the body (candidate L26–27), a two-line Japanese explanation that the theme layers over Basalt, that the include at the head performs it, and that Basalt's CSS lives on the basalt-jp side. It has no original counterpart and is the porter's orientation for a JP reader, written as body prose rather than as a comment. There are no `[!-- ... --]` notes and no provenance comment (`grep -n '\[!--' candidate.txt` returns nothing).
- **Why:** R2: porter-added text is part of the change record, and this note is load-bearing — it is the only in-file explanation of the layering that section 3 records.
- **Verify:** Read candidate L26–27.
- **Disposition:** Standing.

### 11. Dispositions and exceptions

- **What:** Four items, each with its ground. (1) T1's three hotlink errors: class (ii), posting-procedure — the logo and memo-logo asset URLs on foreign hosts (section 4); posting re-hosts them. (2) T1's single unencoded-colon error (candidate L100, the `collab:dr-moist:theatre` file address): DISPOSITIONED under KB-01's own 5k precedent, recorded in the ledger's c1 register — the encoded form of that address does not serve, so the colon is left as the original wrote it; the register names this "the single run-wide occurrence... dispositioned, not a new charge". The theme's other two colons were encoded (section 4), so the precedent is applied per-address, not as a blanket exemption. (3) The render row's items, both DISPOSITIONED in the ledger (c2) register: candidate-inherent page-overflow (435–437px@320/375 on the page; 1489px@1366 and 789px@768 on the sample), recorded by the lane itself as by-design wide content (KB-37 family); and hidden-rate by design (no Rate module on the theme page), whose repair status the register assigns to the source layer (KB-50 note). (4) T4's structural suspicion (theme CSS living only inside the iftags gate, LOCALIZE-ROWS row 48): DISPOSITIONED per FIX3-S2EN §6.11 — the render reports did not confirm it; the theme renders with its CSS applied. The AREA-12 flag from the same row is section 8's item.
- **Why:** A disposition is a decision with grounds (AGENTS.md §3 classes (i)/(ii)/(iii); the named KB entries), not an omission; environment-layer lines are recorded as not-charged.
- **Verify:** Each item names its deciding record above; the byte-level claims are the greps of sections 3, 4, and 8.
- **Disposition:** DISPOSITIONED (items 1–4).

### 12. Verification

- **What:** (a) T1 source check (T1-ROWS row 48): exit 1, 4 errors / 1 warn / 1 info; the errors are hotlink ×3 and unencoded-colon ×1, the standing classes of section 11(1)–(2); there is no class (i) error. (b) T2/T3 render (RENDER-ROWS-1, lane RENDER-S2-A): FINDINGS, the items of section 11(3), all dispositioned; full engine matrix as run by the lane. (c) T4/T5 (LOCALIZE-ROWS row 48): FINDINGS jointly, display-affecting findings 4, dispositioned as in section 11(4), section 8, and the ledger §(c3) line (header language = ruling 2; asset hosts = class (ii); credit fields FIXED by the credit waves). The original having been superseded upstream after revision 13, the follow-up diff artifact `diff-5k-from13.txt` is held in the campaign record (K5a-i). (d) This package is self-verifying: `python3 review/build_review.py --check` regenerates diff.md and the verdict stamp from the two byte-faithful copies in this directory and compares. Counts in this README are the generator's (difflib, autojunk off): +30/−123 in 11 change blocks / 7 hunks; the GNU-diff count of the same pair is 155 changed lines, and the difference is alignment choice, not content.
- **Why:** Verification claims name the cheapest deciding check and its result, not a general assurance.
- **Verify:** Re-run the checker on `pages/theme:5k-jp.txt` and `python3 review/build_review.py --check` in this repo.
- **Disposition:** PASS (GOSIGN2-LEDGER (b) row 48; go-sign, COMPLETION-REPORT §10).

## Per-theme record

### The unencoded colon (KB-01's 5k precedent)

KB-01's rule is mechanical: a raw colon in a `local--files` page address breaks the address, so the port encodes it. This candidate encodes two of its three colon addresses (the logo, twice) and leaves the third — a collaborator's file at `collab:dr-moist:theatre` on smlt.wdfiles.com — exactly as the original wrote it. The ledger's c1 register records why: the encoded form of that address does not serve. Encoding it would satisfy the checker and break the image; leaving it keeps the image and costs one standing checker error, dispositioned once, run-wide, as a named precedent rather than a per-lane judgment. A reviewer can re-derive the whole decision from this package: the two encoded forms are candidate L47 and L185, the unencoded form is candidate L100, and the original's three addresses are original L25, L169, and the memo rule in its first module.

## Change set outside the two diffed files

The diff covers two files; the port's record is one file larger. `pages/theme-decoration-sample-5k-jp.txt` is the decoration sample the render checks ran against (its findings are the sample half of section 11(3)); it belongs to this theme's record but carries no port change of its own to explain here. The candidate layers over `pages/theme:basalt-jp.txt` by the include of section 2; the base's own package is a separate record (class U). There are no companion fragments and no inbound-link repairs in other candidates for this theme.
