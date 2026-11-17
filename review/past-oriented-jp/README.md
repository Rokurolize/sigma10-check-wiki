# Review package — theme:past-oriented-jp (KO → JP port)

<!-- BEGIN GENERATED VERDICT STAMP — do not hand-edit; regenerate with review/build_review.py -->
## Verdict stamp
- Theme: theme:past-oriented-jp — origin KO, population #280 [GOSIGN2-LEDGER (b) row 280]
- Overall: STALE — candidate file changed since the verdict was computed (verdict against 435a6bb-era content, file sha256 now 0e7bbad922e8575a48b4a7c2186c021df0abf5b2b2707d5d5dde0a2725c58722); verdict not carried over, re-judgement required
> verdicts below describe the pre-change file
- T1 (source check): FINDINGS (classified) — baseline 2026-11-16: exit 1, 3 errors / 0 warns / 1 info (pseudo-ref×3); standing classes dispositioned in register c1 [T1-ROWS row 250; GOSIGN2-LEDGER (b) row 280]
- T2/T3 (render, combined verdict): FINDINGS — [combined T2/T3] report `FINDINGS` — page runtime-hotlink site-theme chain only; sample credit-modal (preview-form) + runtime-hotlink (no sample overflow); T3 none beyond cross-cutting items. [RENDER-ROWS-2 (RENDER-S2-H (KO7))]
- Engine coverage: full matrix as run by the lane; coverage not separately caveated in the row [RENDER-ROWS-2 row]
- Credit modal: sample credit-modal errors dispositioned preview-form (credit:start-preview has no modal mechanism; GOSIGN-TESTS T2 amendment, 2026-11-16) [RENDER-ROWS-2 (RENDER-S2-H (KO7))]
- T4 (localize patterns + follow-up): FINDINGS — display-affecting findings: 1 [LOCALIZE-ROWS row 279, source LOCALIZE-S2-F]
- T5 (translation text): FINDINGS — the source reports judge T4/T5 jointly; one verdict word covers both [LOCALIZE-ROWS row 279]
- FIX5 re-judgement: none — no OPEN items at the ledger determination [GOSIGN2-LEDGER (b) row 280]
- Computed against: canonical commit b5cb7241f527a44933e45599b41df210690771c4; candidate file pages/theme:past-oriented-jp.txt sha256:0e7bbad922e8575a48b4a7c2186c021df0abf5b2b2707d5d5dde0a2725c58722; record: GOSIGN2-LEDGER.md + GOSIGN2-LEDGER-SUPPLEMENT.md as of the FIX5 head 435a6bb
<!-- END GENERATED VERDICT STAMP -->

## Status

| | |
|---|---|
| Verdict | **PASS** — passed at the ledger determination; no OPEN items (GOSIGN2-LEDGER (b) row 280) |
| Standing items | **DISPOSITIONED** — the P9 content strings (ruling 2; sections 5, 11) and the P5 font substitution (KB-58; section 4). **Charged by T4 and still standing in the bytes** — the credit author field's vagueness (§3 of the T4 row; per-theme record). **FLAGGED by this package** — the delivery consolidation removed the original's parameter-gated variant loading while the candidate still documents the `dark` parameter (per-theme record); the two usage exhibits name the plain slug on the JP side |
| Go-sign basis | COMPLETION-REPORT.md §10 (go-sign issued; 81 FIXED / 26 DISPOSITIONED / 0 OPEN across the sweep) |
| Named exception | None for this theme (the sweep's single named exception is theme:amethyst-v2, which has no candidate) |

## Provenance

| | Original | Candidate |
|---|---|---|
| Page | theme:past-oriented | theme:past-oriented-jp |
| Wiki | scpko.wikidot.com | SCP-JP Sigma-10 candidate (canonical repo) |
| Reference revision | 20 (first translation; the candidate's credit block records 初訳時参照リビジョン: 20) | — |
| Source of this copy | Campaign cache `gosign2-lanes/lane-oc-gs2-localize-s2-F/orig-past-oriented.txt`, via the mirror store (class COPY, hash-verified against review/sources.tsv) | Canonical file `pages/theme:past-oriented-jp.txt`, copied at worktree HEAD 9068bb7 |
| Lines / bytes | 527 lines / 15,679 bytes | 516 lines / 16,701 bytes |
| SHA-256 | 4a6d2efb2f2fcbd33d9d7de4aefbc9d47a1e35a30830aab1ef1ec6bce2a35ec | af7129fe586f4a669225a80bb85e50bc2f84510afe6c71d2c2a90de03f33f78e |

Wave history: the candidate was created by the Stage 2 KO7 integration (commit ebd18ee, the LOCALIZE-S2-F wave's port, lane-oc-gs2-localize-s2-F) and has exactly one later commit, 1869877 (FIX-CREDIT-D), whose past-oriented hunk is the translator-field normalization. No FIX5 commit touches this file. (The verdict stamp cites T1-ROWS row 250 and LOCALIZE-ROWS row 279 for this theme; its population number is 280. The offsets are the registers' own, recorded here so the citations can be followed.)

## Summary

A KO branch theme (for the Hongiksa / 弘益寺 group of interest) whose port is the batch's most instructive delivery case. The original delivers its CSS split over three code files with the variant file loaded through two conditional gates, one of them keyed on the include parameter `dark` that the theme's documentation teaches. The candidate consolidates the three files into one, and its porter annotation says so in as many words, but the parameter gate does not survive the consolidation: nothing in the candidate responds to `dark`, while the translated prose still presents the parameter as the variant switch. That gap is flagged in the per-theme record. The rest of the port is complete and in places exemplary: the annotation also records the font substitution (the KO faces replaced by Google's Gowun Batang, a Hangul-capable serif, alongside Noto Sans JP and Noto Serif JP); the floated bare Rate and the KO info module become the preview credit block; a license box is installed where the original had none. Two record items stand open in the bytes: the credit block's author field is a pointer to the original page rather than the author the original names (T4 charged this as "§3 著作権者 vague" and the campaign passed the theme with the charge recorded), and both usage exhibits keep the plain slug on the JP side. Measured churn (diff.md, the generator's difflib count with autojunk off: +131/−148 in 42 change blocks / 8 hunks).

## Class summary

Auto-classification by review/classify_hunks.py (signature table 2026-11-17.1): 42 change blocks — 18 specific (42.9%), 16 heuristic (38.1%), 8 residue (19.0%), 0 skipped. Pattern citations below name the KB entry; the patterns/ tree state cited throughout is commit 9c5e9079afb01d30cb9fc4ef9d714e5591eb2ffa.

| Label | Blocks |
|---|---|
| TRANS-UNANCHORED | 17 |
| TRANSLATION-ANCHORED | 11 |
| DRAFT-HOST | 3 |
| JPFONT-STACK | 3 |
| COMMENT-TEXT | 2 |
| CSS-BODY | 2 |
| BARE-RATE-DEL | 1 |
| CREDIT-PREVIEW | 1 |
| CREDIT-PROSE | 1 |
| DELIVERY-MOVE | 1 |
| ESCAPED-INCLUDE | 1 |
| EXHIBIT-RESTRUCTURE | 1 |
| IFTAGS | 1 |
| INCLUDE-REPOINT | 1 |
| INFO-DEL | 1 |
| JPFONT-LOAD | 1 |
| LICENSE-BOX | 1 |
| SELF-DELIVERY | 1 |
| TASL-FIELDS | 1 |

Adjudication for this README (every block was read against the bytes): the residue share (19.0%) is the batch's highest, and all 8 residue blocks (B7, B14, B15, B16, B19, B29, B39, B40) are translation pairings inside the sample tabs (the info-box deletion's tail, the research-paper format samples with their (探求題名) / (作中著者） placeholders, and one-line prose pairs), resolved in the appendix by shape; none hides a structural change. The single DELIVERY-MOVE block is the delivery consolidation of section 3, adjudicated there and in the per-theme record. The 2 CSS-BODY blocks are single-rule content edits inside the consolidated CSS with no mechanism signature, counted here as charged. The single EXHIBIT-RESTRUCTURE primary is the info-zone replacement (section 1), not an exhibit loss; the exhibit census of section 8 is one-to-one over the tabview samples. After adjudication no block is left unexplained; the two per-theme flags are documentation-versus-mechanism gaps, not unexplained blocks.

## Standing sections

### 0. Header and provenance frame

- **What:** Theme theme:past-oriented-jp; original theme:past-oriented on scpko at reference revision 20; candidate `pages/theme:past-oriented-jp.txt`. Provenance route: derived from the original at the reference revision by the LOCALIZE-S2-F wave (sources.tsv kind: standard; no production JP counterpart exists for this theme, so the R4 adoption question does not arise). The frame order changed: the original opens with its tag gate and floated Rate and delivers from the tail (original L1–3, L509–527); the candidate opens with the delivery pair (candidate L1–8) and places the localized gate `[[iftags +テーマ]]` after it (candidate L9). The original's gate tag is the KO form +테마; the candidate's is the JP form of the same tag.
- **Why:** Section 0 declares the provenance route so every later count is read against the right baseline; the gate's tag is P2, the frame is P6/T3 (section 3).
- **Verify:** The sources.tsv row for past-oriented-jp; `sha256sum original.txt` against the Provenance table.
- **Disposition:** Standing (the route itself); the delivery rebuild is section 3.

### 1. Credit and attribution

- **What:** The original's credit furniture is a right-floated bare `[[module Rate]]` (original L2–4) and the KO info module, `:scpko:info:start` / `:scpko:info:end` (original L6–25), whose block names the maker (**제작:** [[*user thd-glasses]], original L9), the image sources (the Hongiksa logo: original design [[*user AXOL0TL]], produced by [[*user thd-glasses]], original L12), a font source (the noonnu font page, original L15), and a hub link to the maker's works. The candidate deletes the Rate and the info module (INFO-DEL) and installs the preview credit block (candidate L11–20) with the eight ruling-3 fields — except that the author field is not a name: 著作権者 reads "原語版ページの作成者に同じ（scpko の theme:past-oriented）" ("same as the original page's creator"), a pointer to the original page. The license zone repeats the form: the original has no license box; the candidate installs the JP backend box (candidate L507–514) whose author parameter is the same kind of pointer (`|author=scpko theme:past-oriented の作者`) and whose single entry defers to the original page's statements for image and font sources. So the names the original's info block carries (thd-glasses; AXOL0TL for the logo) appear nowhere in the candidate's credit or license furniture; thd-glasses survives only as a body heading inside a sample tab (candidate L63, the research-society sample's byline, with 2misi). The credit block's remaining fields are in order (title 過去志向 テーマ; 翻訳責任者 AI; 翻訳年 2026; 原題 과거지향 테마 — the original's Korean title carried, correctly, as the original-title field; 作成年 2024; 初訳時参照リビジョン 20; the source link https://scpko.wikidot.com/theme:past-oriented, whose host matches the sources.tsv record). T7 credit-module CSS: none on either side.
- **Why:** P3/T1 with KB-09 for the swap itself (the preview module is rate-bearing). Ruling 3 fixes the eight fields; an author field that points instead of naming fails the field's purpose, which is attribution in the page itself. T4's row for this theme charged exactly this ("§3 著作権者 vague", LOCALIZE-ROWS row 279) — the charge is the campaign's own, and the per-theme record below carries it forward with both sides' text.
- **Verify:** Read candidate L16 against original L9; `grep -n 'thd-glasses\|AXOL0TL' candidate.txt` — one body hit (L63), none in the credit or license zones.
- **Disposition:** The swap is FIXED by construction at creation; the author field's form is charged (T4 §3) and flagged in the per-theme record — not dispositioned by any (c3) line for this theme.

### 2. Includes and components

- **What:** One repoint block: the sample tabview's image-block include is repointed (`:scpko:component:image-block` → `:scp-jp:component:image-block`, candidate L34–37), keeping its bare filename parameter `|name=홍익사.png` — the original's own form, a filename rather than a URL; T4's row charged the bare-filename form as its 型5 item, and the (c3) register dispositions the theme's P5 line under KB-58. The frame include is section 3; the credit and license includes are section 1. The original's info-module pair leaves with its zone (section 1). No component swap (T8) was needed.
- **Why:** P1 (KB-15) for the repoint. The filename parameter is the theme's asset convention (the file is an attachment of the theme page itself on both wikis), carried rather than rewritten into a URL.
- **Verify:** `grep -n '\[\[include' candidate.txt` — five includes, all JP-side.
- **Disposition:** Applied; the bare-filename form is DISPOSITIONED (the theme's P5 line, (c3) register, KB-58).

### 3. Delivery and code loading

- **What:** The original delivers from its tail in four modules (original L509–527): code file /0 unconditionally; code file /2 inside a blockquote-wrapped parameter gate, `>[[ift{$dark}gs -테마]]` … `>[[/ift{$dark}gs]]`, which loads the variant layer when the including page passes the theme's documented `dark` parameter; code file /2 again under `[[iftags +테마]]` (the theme's own pages); and code file /3 unconditionally. The candidate rebuilds delivery at the head in the wave-standard form: a module CSS importing its own single code file `local--code/theme%3Apast-oriented-jp/1` from the draft host (candidate L1–3) and the interwiki frame at priority 1 with `theme=` naming the same /1 on the draft host (candidate L5–8). The three original files are consolidated into the one file (its code exhibit is candidate L185–506), and the candidate's own porter annotation at the CSS head states the consolidation plainly (candidate L191–196, section 10). What the consolidation does not carry is any gate: the candidate contains no `[[ift{$dark}gs]]` construct and no other parameter-responsive element, so the variant layer the original loads conditionally is merged into the single unconditional file (its successive `:root` layers stand at candidate L203, L390, L448), and the `dark` parameter the candidate's prose still teaches (candidate L25, L27, L92) changes nothing. Both delivery lines are draft-host form, class (iii).
- **Why:** P4/T9 and P6/T3 for the head pair and the import form; KB-41 for the draft lines. The consolidation itself is a legitimate delivery decision, and it is disclosed in-file; the flag in the per-theme record is narrower — the documented parameter's mechanism did not survive it, and no ledger line charges that.
- **Verify:** `grep -n 'ift{\|local--code' candidate.txt` — the delivery lines only, no parameter gate; compare original L509–527's four modules.
- **Disposition:** DISPOSITIONED (the draft-host lines, class (iii)); the parameter gate's loss is flagged below, not dispositioned.

### 4. Fonts and assets

- **What:** The original's faces are KO webfonts sourced through the noonnu font page named in its info block (original L15; the porter's annotation names them: UnJamoBatang and the Shilla Culture family). The candidate loads three Google Fonts faces at the CSS head (candidate L186–188): Noto Sans JP and Noto Serif JP (the JP companions, JPFONT-LOAD), and Gowun Batang — a Hangul serif — as the substitute for the KO faces, exactly as the annotation records (candidate L195–196). The stacks append the JP faces at three loci (JPFONT-STACK). The theme's own image asset (the Hongiksa symbol, 홍익사.png) keeps its bare filename form (section 2); the license entry records that KO-side attachments were re-hosted to the candidate page and webfonts replaced with Google Fonts equivalents (candidate L511).
- **Why:** P5 with KB-58 (the (c3) register's disposition for this theme's P5 line: branch font sources that the JP environment cannot serve are substituted with equivalents, and the substitution is recorded — here, in the file itself). P7/T5 with KB-16 for the JP loads and stack appends: the added faces are loaded in-file, so the named-but-unloaded gap does not arise.
- **Verify:** `grep -n '@import' candidate.txt` — L2 (self-delivery) and L186–188 (the three font loads); read the annotation at candidate L191–196.
- **Disposition:** DISPOSITIONED (P5, KB-58, (c3) register).

### 5. Header, sidebar, and site furniture

- **What:** No header-variable change: the theme styles its header through rules, not title variables, so no HEADERVAR signature fired and ruling 2 is not engaged by a variable. The theme's rendered strings tell the dispositioned half of the story: three CSS `content:` strings keep the Korean institution names — `content: "사단법인 홍익역사연구회"` (candidate L239), `content: "홍익역사연구회"` (candidate L378), `content: "홍익사"` (candidate L401) — while the candidate's prose localizes the same names throughout （弘益寺 for 홍익사, 弘益歴史研究会 for 홍익역사연구회）. T4 charged this as its 型9 item ("content 内 KO 機関名 ×3、display-affecting", LOCALIZE-ROWS row 279), and the (c3) register dispositions the theme's P9 line under ruling 2. The strings are in-universe institutional names rendered as page furniture (masthead and seal text), which is the ground the disposition rests on; the bytes and the prose's own localization choice are both recorded here so the disposition can be re-judged from this package alone if the coordinator wishes.
- **Why:** P9/T6 with ruling 2 (rendered institutional naming is treated with the header-language class). The flag discipline for this shape (a rendered string in a form the prose itself localizes) is satisfied by recording both forms with loci, which this section does; the campaign's disposition stands until re-judged.
- **Verify:** `grep -n 'content:' candidate.txt` at L239, L378, L401 against the prose forms at candidate L24 and L92.
- **Disposition:** DISPOSITIONED (P9, ruling 2; (c3) register, past-oriented line).

### 6. Text translation

- **What:** The body translates from Korean throughout: the usage prose, the tabview samples （基本構文 / 書式構文 and their contents), the research-paper format samples (their placeholders localized: (탐구 제목) → (探求題名）, (작중 저자) → (作中著者）), and the alt-theme documentation (candidate L92's prose among it), in eleven TRANSLATION-ANCHORED blocks and the one-line TRANS-UNANCHORED grain (17 counts), each verified against the mirror for this README. The group-of-interest's name is localized as a name （홍익사 → 弘益寺； 홍익역사연구회 → 弘益歴史研究会）, consistently in prose; the CSS strings of section 5 are the stated exception. R1 in-CSS text: two section comments are translated inside the CSS, and the porter's head comment is section 10; the remaining comments are structural labels carried in Korean or English, porter-visible only.
- **Why:** P10 and KB-18 (reader-visible strings localize). The unanchored grain is where a silent deletion would hide, which is why each was read individually rather than waved through as a class.
- **Verify:** The pairs are diff.md's body sections in order; a Korean-prose scan of candidate.txt outside the credit fields returns the section 5 strings, the original-title field, and proper nouns.
- **Disposition:** Standing (the port itself); T4/T5 judged the theme FINDINGS with the items of sections 1, 2, and 5 (LOCALIZE-ROWS row 279).

### 7. Links

- **What:** The candidate's live outbound link is the credit block's source link (candidate L19), naming the original on scpko.wikidot.com, the host the campaign's provenance records name for it; it serves the original page, and its label carries the original's Korean title. The original info block's two further links do not carry: the font-source link (noonnu, original L15) is superseded by the substitution of section 4, whose record is the annotation and the license entry; and the maker's hub link (original L21, `[[[thd-glasses-hub|…]]]`) leaves with the info zone — it is a foreign-wiki author hub with no JP counterpart, and the credit block's source link is the candidate's provenance pointer instead. No link in the candidate is dead on the evidence of the mirror.
- **Why:** P11: prose links take the JP counterpart or the serving original; an author-hub link inside a replaced credit zone is part of that zone's record, and its leaving is stated here rather than left silent.
- **Verify:** `grep -n 'scpko.wikidot.com' candidate.txt` — candidate L19 (and the credit pointer's prose mention at L16).
- **Disposition:** Standing.

### 8. Structure

- **What:** The localize.md closing rule holds for the gated body: the exhibit census corresponds one to one (the tabview with its format samples, the image-block exhibit, the collapsible sample, the alt-theme documentation tab, and the CSS code exhibit), and the JP corrections arrive as the head delivery pair, the credit swap, and the license-box installation. The one structural transformation is the delivery consolidation of section 3, which is a topology change the porter disclosed in-file; it is counted here so the census claim is not read as covering it. The classifier's EXHIBIT-RESTRUCTURE primary adjudicates to the info-zone replacement (section 1).
- **Why:** R3: a restructure and a silent deletion share a diff shape; the census decides for the body, and the delivery change is disclosed rather than silent, so it is a flagged mechanism gap (per-theme record), not a class I deletion.
- **Verify:** Compare `grep -n '\[\[tab \|code type' original.txt candidate.txt` — the tab sequences correspond.
- **Disposition:** Standing for the gated body; the delivery gate is flagged below.

### 9. Formatting only

- **What:** None. The classifier finds no whitespace-only block and no re-indentation anywhere in the pair (0 and 0), so the R7 follow-up-diff hazard is not triggered.
- **Why:** Formatting churn is disclosed as its own class so it is never mistaken for a semantic change.
- **Verify:** The classification summary's WS-ONLY count is 0.
- **Disposition:** None required.

### 10. Porter annotations

- **What:** One substantial annotation, riding inside the CSS-BODY zone at the code exhibit's head (candidate L191–196), a bilingual comment that records: the theme's identity and reference revision ("과거지향 / Past-Oriented — Ported for SCP-JP (theme:past-oriented rev 20 on scpko)"); the delivery consolidation (the original split its CSS over code files 0, 2, 3; the JP candidate consolidated them into one code file); and the font substitution (the KO UnJamoBatang / Shilla Culture faces replaced by Google's Gowun Batang). A one-line companion comment ("日本語フォント (JP localization)", candidate L197) heads the JP font section. The skeleton's "none" for this section does not survive contact with the bytes and is corrected here: the annotation exists, and it is the file's own record of its two largest decisions — which is also why the per-theme flag is about the gate the annotation does not mention, not about concealment.
- **Why:** R2: porter-added text is part of the change record; this one carries the delivery and font decisions, and sections 3–4 cite it as their in-file evidence.
- **Verify:** Read candidate L191–197.
- **Disposition:** Standing.

### 11. Dispositions and exceptions

- **What:** Three items, each with its ground. (1) The P9 content strings (section 5): kept in Korean as in-universe institutional names, counted by T4 as display-affecting, dispositioned under ruling 2 in the (c3) register. (2) The P5 font substitution and bare-filename asset form (sections 2, 4): dispositioned under KB-58 in the (c3) register. (3) The render row's items, all environment or capture layer, not charged to the candidate: the page's runtime-hotlink site-theme chain (KB-40) and the sample's credit-modal errors (KB-32: the preview form has no modal mechanism, ruling 5), with no sample overflow and no further T3 items beyond the cross-cutting ones. The T1 register's three pseudo-ref errors are the candidate's own draft-host delivery lines, class (iii). Two items are deliberately not listed here: the credit author pointer (section 1) was charged by T4 but has no (c3) disposition line, and the delivery gate's loss (section 3) was charged by nobody; listing either as dispositioned would manufacture a ground the campaign never gave.
- **Why:** A disposition is a decision with grounds (AGENTS.md §3 classes; ruling 2; the named KB entries), not an omission; environment-layer lines are recorded as not-charged.
- **Verify:** Each item names its deciding record above; the T1 classes are T1-ROWS (cited as row 250 in the stamp) and register (c1).
- **Disposition:** DISPOSITIONED (items 1–3).

### 12. Verification

- **What:** (a) T1 source check (T1-ROWS, cited as row 250 in the verdict stamp): exit 1, 3 errors / 0 warns / 1 info; all three errors are pseudo-ref, class (iii); there is no class (i) error. (b) T2/T3 render (RENDER-ROWS-2, lane RENDER-S2-H (KO7)): FINDINGS, the items of section 11(3), all dispositioned; engine coverage as run by the lane, not separately caveated in its row. (c) T4/T5 (LOCALIZE-ROWS row 279): FINDINGS jointly, display-affecting findings 1, the row's text naming three items （型9 the section 5 strings; 型5 the section 2 filename form; §3 the section 1 author vagueness) — of which the first two carry (c3) dispositions and the third stands charged, as section 1 records. (d) This package is self-verifying: `python3 review/build_review.py --check` regenerates diff.md and the verdict stamp from the two byte-faithful copies in this directory and compares. Counts in this README are the generator's (difflib, autojunk off): +131/−148 in 42 change blocks / 8 hunks.
- **Why:** Verification claims name the cheapest deciding check and its result, not a general assurance.
- **Verify:** Re-run the checker on `pages/theme:past-oriented-jp.txt` and `python3 review/build_review.py --check` in this repo.
- **Disposition:** PASS (GOSIGN2-LEDGER (b) row 280; go-sign, COMPLETION-REPORT §10), with the per-theme flags below standing as this package's addition to the record.

## Per-theme record

### The credit author field names no author (charged by T4; still standing)

T4's row for this theme charged "§3 著作権者 vague" (LOCALIZE-ROWS row 279), and the bytes still show the charged form. Candidate L16: 著作権者 "原語版ページの作成者に同じ（scpko の theme:past-oriented）". The original names its maker in its info block: **제작:** [[*user thd-glasses]] (original L9). The license box repeats the pointer (`|author=scpko theme:past-oriented の作者`, candidate L508 zone), and the original's secondary attribution — the logo's original design by [[*user AXOL0TL]] (original L12) — has no counterpart in the candidate's credit or license furniture at all (the license entry defers wholesale to the original page's statements, candidate L511). The campaign passed the theme with the T4 charge recorded and no (c3) disposition line for it, so this package carries the charge forward rather than discovering it: the repair is mechanical (name [[*user thd-glasses]] in both fields, and carry the logo attribution into the license entry), and it is a coordinator decision whether it lands as a fix lane. The candidate is left unedited here.

### The `dark` parameter's gate did not survive the delivery consolidation (flagged by this package)

The original loads its variant layer through a parameter gate (original L512–518: code file /2 inside `>[[ift{$dark}gs -테마]]` … `>[[/ift{$dark}gs]]`, with a second loading under `[[iftags +테마]]` at original L520–524). The candidate consolidates files 0, 2, 3 into one unconditional file (candidate L1–3; the consolidation is disclosed by the porter's annotation, candidate L191–196) and contains no parameter-responsive element: a search for `ift{` returns nothing. The candidate's translated documentation still teaches the parameter as the variant switch (candidate L25: include with `dark=a`; L27: remove the argument for the interior form; L92: the two forms are controlled by the `dark` argument). A JP author following those instructions changes nothing. No ledger line, T4 item, or (c3) entry for this theme mentions the gate, so the loss is undispositioned; it is the same family as the our-open-veins variation drop in this batch, with the difference that here the consolidation itself was disclosed and only the gate's loss went unrecorded. Flagged with the loci above; the candidate is left unedited.

### The usage exhibits' slug (flagged by this package)

Both usage exhibits were repointed from `:scpko:` to `:scp-jp:` at creation, keeping the plain slug: `> @@[[include :scp-jp:theme:past-oriented dark=a]]@@` (candidate L25) and `> @@[[include :scp-jp:theme:past-oriented]]@@` (candidate L28). The candidate's own posting name is theme:past-oriented-jp, so both documented syntaxes name a page that will not exist under that name on scp-jp; the file's own delivery lines use the -jp form (candidate L2, L7). This is the population-sweep family (the same shape is flagged in the plant, parawatch-pumpkin, pack-of-peanuts, and paramycota packages in this batch). The ledger's determination for this theme is PASS and this package does not re-open it; the lines are flagged here with their loci, and the candidate is left unedited, as the sweep repairing this family is a coordinator matter.

## Change set outside the two diffed files

The diff covers two files; the port's record is one file larger. `pages/theme-decoration-sample-past-oriented-jp.txt` is the decoration sample the render checks ran against (its findings are the sample half of section 11(3)); it belongs to this theme's record but carries no port change of its own to explain here. There are no companion fragments and no inbound-link repairs in other candidates for this theme.
