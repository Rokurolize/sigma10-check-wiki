# Review package — theme:halloween-jp (EN → JP port)

<!-- BEGIN GENERATED VERDICT STAMP — do not hand-edit; regenerate with review/build_review.py -->
## Verdict stamp
- Theme: theme:halloween-jp — origin EN, population #14 [GOSIGN2-LEDGER (b) row 14]
- Overall: PASS — passed at the ledger determination; no OPEN items [GOSIGN2-LEDGER (b) row 14]
- T1 (source check): FINDINGS (classified) — baseline 2026-11-16: exit 1, 1 error / 1 warn / 1 info (hotlink×1); standing classes dispositioned in register c1 [T1-ROWS row 14; GOSIGN2-LEDGER (b) row 14]
- T2/T3 (render, combined verdict): FINDINGS — [combined T2/T3] report `FINDINGS` — page hidden-rate (rating module absent), sample 768px overflow 884px, sample credit-modal, standalone-panel body text near-invisible; contrast 1 = redaction by design. [RENDER-ROWS-1 (RENDER-B row 14)]
- Engine coverage: full matrix as run by the lane; coverage not separately caveated in the row [RENDER-ROWS-1 row]
- Credit modal: sample credit-modal errors dispositioned preview-form (credit:start-preview has no modal mechanism; GOSIGN-TESTS T2 amendment, 2026-11-16; ROWS-1 phrases the line bare and takes the disposition from the part header) [RENDER-ROWS-1 (RENDER-B row 14)]
- T4 (localize patterns + follow-up): FINDINGS — display-affecting findings: 2 [LOCALIZE-ROWS row 15, source LOCALIZE-A]
- T5 (translation text): FINDINGS — the source reports judge T4/T5 jointly; one verdict word covers both [LOCALIZE-ROWS row 15]
- FIX5 re-judgement: none — no OPEN items at the ledger determination [GOSIGN2-LEDGER (b) row 14]
- Computed against: canonical commit 8c62b7b5207f684c8373dfe00f28b90427d28027; candidate file pages/theme:halloween-jp.txt sha256:28ecf1d77bb965e417f17a8646b6ba27c90f56db396a744358d758493389b817; record: GOSIGN2-LEDGER.md + GOSIGN2-LEDGER-SUPPLEMENT.md as of the FIX5 head 435a6bb
<!-- END GENERATED VERDICT STAMP -->

## Status

| | |
|---|---|
| Verdict | **PASS** — passed at the ledger determination; this theme had no OPEN items and no §(e) register entry (GOSIGN2-LEDGER (b) row 14) |
| Standing items | **DISPOSITIONED** — T1 hotlink ×1 (class (ii) / KB-58, the header image on the original's host, section 4); the render row's items (section 11); P7 font stacks (recorded without a display-affecting mark, section 4). No defect flag from this package; the specimen body's replacement is argued in the per-theme record |
| Go-sign basis | COMPLETION-REPORT.md §10 (go-sign issued; 81 FIXED / 26 DISPOSITIONED / 0 OPEN across the sweep) |
| Named exception | None for this theme (the sweep's single named exception is theme:amethyst-v2, which has no candidate) |

## Provenance

| | Original | Candidate |
|---|---|---|
| Page | theme:halloween | theme:halloween-jp |
| Wiki | scp-wiki.wikidot.com | SCP-JP Sigma-10 candidate (canonical repo) |
| Reference revision | 23 (first translation; the candidate's credit block records 初訳時参照リビジョン: 23) | — |
| Source of this copy | Fresh fetch for this review (mirror class FETCH-REGEN, fetched 2026-11-17; hash-verified against review/sources.tsv) | Canonical file `pages/theme:halloween-jp.txt`, copied at worktree HEAD f9cae19 |
| Lines / bytes | 629 lines / 11,529 bytes | 580 lines / 11,280 bytes |
| SHA-256 | 21d05a9e1e3f79dd52c801ef1445b25a47a633a385e5d90ce2bf85d138512f13 | 28ecf1d77bb965e417f17a8646b6ba27c90f56db396a744358d758493389b817 |

Wave history: this candidate predates the Sigma-10 waves' shape — it was created as one of eight standalone JP theme ports (commit b0cfebd), whitespace-normalized in 3010ef7, recorded in Phase 17 (8dcac74), given its credit fields and furniture by the T1-fix wave (b816e10, rows 1–44) and FIX-CREDIT-C (5c32672), translator-normalized by FIX-CREDIT-D (1869877), and given its JP frame by FIX4-IWA (8c62b7b), the stamp's computed-against commit. No FIX5 commit touches this file, because the theme had no OPEN items for FIX5 to re-judge.

## Summary

The batch's structural outlier, and the package where the topology pass earns its keep. The original delivers its CSS from a `[[code]]` exhibit at its tail (original L78–628, its own code block 3), imported by a head module and an EN interwiki-style frame, over a full English specimen body. The candidate instead carries the same CSS inline in a single head `[[module CSS]]` (candidate L1–550; the topology pass matches the two bodies at 0.995 similarity, the difference being two trailing-whitespace lines), appends the JP frame, gate, and credit block after it, and replaces the specimen body with an eleven-line porter's page that states the port's intent in its own words: a standalone application of the theme that does not depend on the external site's theme page. Measured churn (diff.md, the generator's difflib count with autojunk off: +33/−80 in 5 change blocks — small because the relocation aligns the 551-line CSS body as matched content). The one live external reference, the header image on the original's own host, is a ledger disposition (class (ii) / KB-58), not a flag; the specimen replacement is argued in the per-theme record.

## Class summary

Auto-classification by review/classify_hunks.py (signature table 2026-11-17.1): 5 change blocks — 5 specific (100%), 0 heuristic, 0 residue, 0 skipped. Pattern citations below name the KB entry; the patterns/ tree state cited throughout is commit 9c5e9079afb01d30cb9fc4ef9d714e5591eb2ffa.

| Label | Blocks |
|---|---|
| DELIVERY-MOVE | 5 |
| IFTAGS | 2 |
| SELF-DELIVERY | 2 |
| WS-ONLY | 2 |
| BARE-RATE-DEL | 1 |
| CREDIT-PREVIEW | 1 |
| DRAFT-HOST | 1 |
| EXHIBIT-RESTRUCTURE | 1 |
| TASL-FIELDS | 1 |
| TRANS-UNANCHORED | 1 |

Adjudication for this README (every block was read against the bytes): the DELIVERY-MOVE labels are the substance — the CSS body's relocation from exhibit to live module (sections 3 and 8); the EXHIBIT-RESTRUCTURE primary (B1) is that same relocation seen from the head, not an exhibit change (the exhibits' fate is the per-theme record's subject); the 2 WS-ONLY spans inside the moved body are trailing-whitespace removals (section 9). After adjudication no block is left unexplained.

## Standing sections

### 0. Header and provenance frame

- **What:** Theme theme:halloween-jp; original theme:halloween on scp-wiki at reference revision 23; candidate `pages/theme:halloween-jp.txt`. Provenance route: derived from the original at the reference revision, but by the earlier standalone-port pass (commit b0cfebd), not by a Sigma-10 localize wave (sources.tsv kind: standard; no production JP counterpart exists for this theme, so the R4 adoption question does not arise). That origin explains the candidate's shape: where the localize waves keep the original's body and delivery form, this port was written to stand alone, and the later waves (credit, frame) were applied to it in place.
- **Why:** Section 0 declares the provenance route so every later count is read against the right baseline; here the route is what makes sections 3 and 8 intelligible.
- **Verify:** The sources.tsv row for halloween-jp; `sha256sum original.txt` against the Provenance table; the candidate's own intro (candidate L571) states the standalone intent.
- **Disposition:** Standing (the route itself); its consequences are recorded in sections 3 and 8 and the per-theme record.

### 1. Credit and attribution

- **What:** The original's credit furniture is a bare `[[module Rate]]` (original L12–14) and nothing else — no info block, no license box, no in-file author line. The candidate deletes the Rate (block B1) and installs the JP form at its tail: a `:scp-jp:credit:start-preview`/`end-preview` block (candidate L558–567) carrying the eight ruling-3 fields (title Halloween Theme（SCP-JP）; 翻訳責任者 AI; 翻訳年 2026; 原題 Halloween Theme; 著作権者 Uncle Nicolini; 作成年 2018; 初訳時参照リビジョン 23; the source link, section 7), followed by porter prose that repeats the credit in text form (candidate L575–579: thanks to the original's author and to the SCP Foundation Wiki, the reference revision restated, and a source line naming the original URL with CC BY-SA 3.0). The fields arrived through the credit waves (b816e10, 5c32672) and the translator field took its ruling-3 form in FIX-CREDIT-D (1869877). The T4 row's lead charge was exactly this section (P3: no credit:start-preview, no rating module, plain-text credit, §3 mostly missing) and the ledger records it FIXED (credit waves, checker-verified). Because the original names no author in-file, there is no in-file credit for the 著作権者 field to drop anyone from. There is no T7 credit-module CSS on either side.
- **Why:** P3/T1 (KB-09): the preview credit module is rate-bearing, so the bare Rate is deleted rather than duplicated; ruling 3 fixes the eight fields and the translator credit form.
- **Verify:** `grep -n 'module Rate' candidate.txt` returns nothing; read candidate L558–567 against the eight fields.
- **Disposition:** FIXED (GOSIGN2-LEDGER §(c3): P3 credit fields FIXED, credit waves, checker-verified).

### 2. Includes and components

- **What:** Three includes, all in the candidate's tail: the frame (candidate L552–555, section 3) and the credit pair (candidate L558, L567, section 1). The usage line is prose, not an include pair: candidate L573, `@@[[include theme:halloween-jp]]@@` — the unprefixed local form naming this candidate's own page with its `-jp` suffix, which is the correct name (contrast the batch's snippet flags, where the name itself is wrong). The original's one component specimen, the image-block example at original L20 (`name=example.png`, a placeholder), has no candidate counterpart; it belongs to the replaced specimen body (per-theme record). No foreign include survives: the original's `:scp-wiki:` frame prefix is gone with the EN frame it belonged to (section 3).
- **Why:** P1 (KB-15): includes name the JP page that actually exists; the candidate's usage line does, in the local form appropriate to a page that will live on the same wiki.
- **Verify:** `grep -n '\[\[include' candidate.txt` — the frame, the credit pair, and the prose usage line at L573.
- **Disposition:** Applied; no foreign include kept, no named exception needed.

### 3. Delivery and code loading

- **What:** The delivery form changes kind. The original delivers indirectly: a head module imports the page's own code block 3 (original L2), an EN interwiki-style frame names the same /3 (original L5–8), and block 3 is the `[[code type="CSS"]]` exhibit at the tail (original L78–628) — the CSS a reader sees as an exhibit is the CSS the page loads. The candidate delivers directly: the same CSS text sits inline in one head `[[module CSS]]` (candidate L1–550), which is the page's only code block, and the frame names that block (`theme=` …/theme%3Ahalloween-jp/1, candidate L552–555). The topology pass matches exhibit to module at 0.995 similarity; the only in-body differences are the two whitespace lines of section 9. **Frame paragraph (the M-frame addition):** unlike the batch's other themes, this original already carried a frame (the EN form above); the standalone port dropped it, the T4 row charged the absence (P6: no interwiki-style), and FIX4-IWA restored it in the JP form at candidate L552–555 with `priority=1` and `theme=` naming its own /1 delivery on the draft host — the single-layer own-code form, in the spaced parameter style. The ledger records the outcome as P6 FIXED (frame waves; checker-verified).
- **Why:** P4/T9 in its relocation form: the CSS the candidate serves is the original's CSS entire, served from the candidate's own page; nothing is loaded from the EN page or its code blocks. P6/T3 (KB-07) for the restored frame; KB-41 covers its draft-host form (class (iii)).
- **Verify:** Read candidate L1–2 and L550–555 against original L1–8 and L78; `grep -n 'scp-wiki.wdfiles' candidate.txt` returns only the header-image line (section 4).
- **Disposition:** FIXED (P6); the relocation itself is the per-theme record's subject; the draft-host frame URL is DISPOSITIONED (class (iii)).

### 4. Fonts and assets

- **What:** Fonts: no load on either side, and the theme's two stacks are carried byte-identical (candidate L338: `"Consolas", "Courier New", "Roboto Mono", monospace`; candidate L451: `"Verdana", sans-serif`). Both are Latin system stacks; the T4 row charged P7 (Latin-only), and the ledger dispositions it (recorded without a display-affecting mark; T4 bar): monospace and Verdana-class stacks fall back to system Japanese faces for Japanese text, and no JP face was added. Assets: the theme's one image, the header's `scp-halloween.png`, is still loaded from the original's own file area on scp-wiki.wdfiles.com (candidate L96, byte-identical to original L173) — the T4 row's P5 charge and T1's single error (hotlink ×1). The ledger dispositions it class (ii) / KB-58: the asset is re-hosted to SCP-JP storage at posting, and fix lanes do not re-host it in the candidate.
- **Why:** P7's disposition is the T4 bar applied to system stacks (a named JP supplement is for faces a theme actually loads or names for text roles; this theme names none). P5/KB-58 for the asset: a serving outside host is a posting-procedure re-host, not a candidate defect, under the settled hotlink sub-case rules.
- **Verify:** `grep -n 'font-family' candidate.txt` — the two stacks above; `grep -n 'wdfiles' candidate.txt` — the frame URL and candidate L96.
- **Disposition:** DISPOSITIONED (P7, T4 bar; P5, class (ii) / KB-58).

### 5. Header, sidebar, and site furniture

- **What:** No header variables are overridden on either side; the theme's furniture rules (header backgrounds, sidebar headings, topbar) are inside the moved CSS body and are carried with it unchanged (the one furniture-adjacent in-body change is a trailing-whitespace line at the sidebar heading selector, section 9). No P8 adaptation was made or needed: the candidate inherits the JP site furniture through the environment. The render row's sample readings in this area (the 768px sample overflow, the standalone panel's near-invisible body text with its contrast note "redaction by design") are sample-layer items, recorded in section 11.
- **Why:** P8/P9 are checked and absent as edits: the port changed where the CSS lives, not what it declares.
- **Verify:** `grep -n -- '--header-' candidate.txt` returns nothing; the CSS body comparison is diff.md's matched content.
- **Disposition:** Standing.

### 6. Text translation

- **What:** There is almost no translated text, because there is almost no carried text: the original's prose is a usage line and a specimen body (original L16–77), and the candidate replaces both with its own short JP prose (candidate L569–579): a title (+ Halloween Theme（SCP-JP 移植）), the standalone-intent sentence, the usage line, and the credit prose of section 1. That prose is porter-written, not translated — it says what the port is, in the port's voice, and its claims are the per-theme record's evidence. The CSS body's comments are carried in English unchanged (they ride inside the 0.995-similarity move). No reader-visible string from the original survives untranslated, because no reader-visible string from the original survives at all outside the CSS.
- **Why:** P10 is the class this port answers differently: its specimen body was documentation of the EN page's rendering, and the port's declared form (section 0) replaces it rather than translating it. The replacement is argued, with the sweep's examination of this exact shape, in the per-theme record — it is not waved through here.
- **Verify:** Read candidate L569–579 against original L16–77; the exhibit census is section 8.
- **Disposition:** Standing as the port's declared form; the ledger's T4 row examined this candidate and charged its credit form, its hotlink, its frame, and its fonts — not its body (per-theme record).

### 7. Links

- **What:** The candidate's live outbound link is the credit block's source link (candidate L566), naming `https://scp-wiki.wikidot.com/theme:halloween` — the original's recorded host (review/sources.tsv), so it names the serving original and no host defect arises; the porter prose repeats the same URL as its source line with the CC BY-SA 3.0 attribution (candidate L579). The original body's two specimen links (a google.com example pair at original L64) belong to the replaced specimen body. No prose link in the candidate targets a foreign wiki page.
- **Why:** P11: prose links take the JP counterpart or the serving original under the dead-reference evidence standard.
- **Verify:** Compare candidate L566's host against the sources.tsv row's original_url host (scp-wiki.wikidot.com) — identical.
- **Disposition:** Standing.

### 8. Structure

- **What:** This is the theme where the closing rule's exception must be written out in full. Preserved: the CSS entire — every variable, selector, and rule of the original's exhibit body, at 0.995 similarity, in the original's order (the topology pass's content match). Changed in kind: the delivery (exhibit → inline module, section 3) and the body (the original's specimen body, original L16–77 — usage prose, an image-block specimen, heading/table/toc specimens, a C# code sample, a CSS sample, a link specimen, a collapsible — has no candidate counterpart; the candidate's body is the eleven-line porter's page of section 6). The classifier's EXHIBIT-RESTRUCTURE primary (B1) is the head-side view of the relocation, not a separate event. The ground for the body replacement, and the record of the sweep's examination of it, are the per-theme record below; this section's census is the fact both stand on.
- **Why:** R3: a dropped or replaced exhibit needs its ground stated, because ledger class I charges the silent form. Here the replacement is declared in the candidate's own prose and was examined by the sweep; the census separates the theme's substance (the CSS, entire) from its documentation (replaced).
- **Verify:** Compare `grep -n '\[\[code\|\[\[module\|\[\[tab\|collapsible' original.txt candidate.txt` — the original's specimen sequence against the candidate's single module; the similarity figure is the topology pass in classification.json.
- **Disposition:** Standing as a declared replacement (per-theme record); no silent deletion, no class I item charged by the sweep.

### 9. Formatting only

- **What:** Two lines inside the moved CSS body, both trailing-whitespace removals (blocks B2, B3: candidate L58, where the original's line ends with trailing spaces, and candidate L181, a trailing space after the sidebar heading selector's comma) — the 3010ef7 normalization commit's work. The classifier finds no other whitespace-only block and no re-indentation, so the R7 hazard is confined to these two lines.
- **Why:** Formatting churn is disclosed as its own class so it is never mistaken for a semantic change; inside a relocated body it is also the whole of the 0.005 dissimilarity, which is why it is named exactly.
- **Verify:** Blocks B2 and B3 in classification.json; diff.md's matched-body sections at those lines.
- **Disposition:** None required.

### 10. Porter annotations

- **What:** The candidate's tail prose (candidate L569–579) is porter text entire: the title line, the standalone-intent sentence, the usage line, and the credit prose with its source line. It is counted as the port's body in section 6 and enumerated here so it is never mistaken for translated original content — the original has no counterpart text. Inside the CSS body there are no porter annotations: its comments are the original's own, carried unchanged, and no `[!-- --]` notes exist anywhere in the file.
- **Why:** R2: porter-added text is part of the change record, and here it is load-bearing — the intent sentence is the declared ground for sections 3 and 8.
- **Verify:** Read candidate L569–579; `grep -n '\[!--' candidate.txt` returns nothing.
- **Disposition:** Standing.

### 11. Dispositions and exceptions

- **What:** Four items, each with its ground. (1) T1's one error, hotlink ×1: class (ii) / KB-58 — the header image on the original's serving host (candidate L96), re-hosted at posting (section 4). (2) The render row's items (RENDER-ROWS-1, RENDER-B row 14): the page's hidden-rate reading (the rating module's state as the lane measured it; the credit block that now carries the rate arrived through the credit waves), the sample's 768px overflow (884px), the sample's credit-modal errors (KB-32: the preview form has no modal mechanism, ruling 5), and the standalone panel's near-invisible body text, whose contrast item the row itself records as redaction by design — sample and environment layer, recorded as not charged to the candidate beyond what the credit waves already fixed. (3) P7 font stacks: DISPOSITIONED (recorded without a display-affecting mark; T4 bar; section 4). (4) The specimen body's replacement: declared in the candidate and examined by the sweep (per-theme record), not a silent deletion.
- **Why:** A disposition is a decision with grounds (AGENTS.md §3 classes (i)/(ii)/(iii); the named KB entries), not an omission; environment-layer lines are recorded as not-charged.
- **Verify:** Each item names its deciding record above and in the per-theme record.
- **Disposition:** DISPOSITIONED (items 1–3); item 4 argued in the per-theme record.

### 12. Verification

- **What:** (a) T1 source check (T1-ROWS row 14): exit 1, 1 error / 1 warn / 1 info; the one error is the hotlink of section 4, class (ii); there is no class (i) error. (b) T2/T3 render (RENDER-ROWS-1, RENDER-B row 14): FINDINGS, the items of section 11(2), all dispositioned; engine coverage as run by the lane, not separately caveated in its row. (c) T4/T5 (LOCALIZE-ROWS row 15): FINDINGS jointly, display-affecting findings 2 — the row's charges are P3 (credit form; since FIXED by the credit waves), P5 (the header-image hotlink; dispositioned), P6 (no JP interwiki-style; since FIXED by FIX4-IWA), and P7 (Latin-only stacks; dispositioned at the T4 bar). The ledger §(c3) line records the outcomes: P3 FIXED, P5 DISPOSITIONED, P6 FIXED, P7 DISPOSITIONED. (d) This package is self-verifying: `python3 review/build_review.py --check` regenerates diff.md and the verdict stamp from the two byte-faithful copies in this directory and compares. Counts in this README are the generator's (difflib, autojunk off): +33/−80 in 5 change blocks.
- **Why:** Verification claims name the cheapest deciding check and its result, not a general assurance.
- **Verify:** Re-run the checker on `pages/theme:halloween-jp.txt` and `python3 review/build_review.py --check` in this repo.
- **Disposition:** PASS (GOSIGN2-LEDGER (b) row 14; go-sign, COMPLETION-REPORT §10).

## Per-theme record — the specimen body is replaced, not translated

The honest summary of this port is that it keeps the theme and replaces its page. The original's body (original L16–77) is a full specimen: how to apply the theme, an image-block example, heading and table specimens, a table of contents, a C# code sample, a CSS sample, a link specimen, and a collapsible. The candidate carries none of it; its body is eleven lines of porter prose (candidate L569–579) whose second sentence declares the form: the theme was ported "in a shape that applies standalone, without depending on an external site's theme page". Three grounds keep this from being the silent deletion ledger class I charges. First, the theme's substance is its CSS, and the CSS is carried entire (0.995 similarity; the residue is two whitespace lines) — nothing a page *using* the theme renders is lost. Second, the replacement is declared in the artifact itself, not discovered by this review: a reader of the candidate learns from the candidate what form the port took. Third, the campaign record examined this exact candidate: the LOCALIZE lane's row (LOCALIZE-ROWS row 15) describes its body sections as "§3 mostly missing" — the lane saw the minimal body — and charged the credit form, the hotlink, the frame, and the fonts, all four of which the ledger then closed (P3 FIXED, P5 DISPOSITIONED, P6 FIXED, P7 DISPOSITIONED) with the determination PASS. This package therefore records the replacement with its census (section 8) and does not re-open the determination; a reviewer who judges specimen bodies essential to a theme page has, in this package, the full evidence for that judgment and the record of the contrary one.

## Change set outside the two diffed files

The diff covers two files; the port's record is one file larger. `pages/theme-decoration-sample-halloween-jp.txt` is the decoration sample the render checks ran against (its findings are the sample half of section 11(2)); it belongs to this theme's record but carries no port change of its own to explain here. There are no companion fragments, no shared base file, and no inbound-link repairs in other candidates for this theme.
