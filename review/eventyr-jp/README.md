# Review package — theme:eventyr-jp (EN → JP port)

<!-- BEGIN GENERATED VERDICT STAMP — do not hand-edit; regenerate with review/build_review.py -->
## Verdict stamp
- Theme: theme:eventyr-jp — origin EN, population #86 [GOSIGN2-LEDGER (b) row 86]
- Overall: STALE — candidate file changed since the verdict was computed (verdict against 435a6bb-era content, file sha256 now 9622ac1ffd9ef5dedf5b1a92b8b889f7cffae6d592f681501f295d7183d9498f); the verdicts below were computed against that pre-change file, and the record verdict stands: a candidate revised through the campaign's recorded repairs is posted like a PASS row, with the change recorded in its package
- T1 (source check): FINDINGS (classified) — baseline 2026-11-16: exit 1, 49 errors / 1 warn / 1 info (pseudo-ref×49); standing classes dispositioned in register c1 [T1-ROWS row 86; GOSIGN2-LEDGER (b) row 86]
- T2/T3 (render, combined verdict): FINDINGS — [combined T2/T3] report `FINDINGS` — sample overflow 337–419px@≤375 + credit-modal (shared); page runtime-hotlink; WebKit CC "S"; decoration assets 404 = deferred, not defects. [RENDER-ROWS-1 (RENDER-S2-B)]
- Engine coverage: full matrix as run by the lane; coverage not separately caveated in the row [RENDER-ROWS-1 row]
- Credit modal: no credit-modal line in this theme's row; no sample credit-modal error recorded [RENDER-ROWS-1 (RENDER-S2-B)]
- T4 (localize patterns + follow-up): FINDINGS — display-affecting findings: 1 [LOCALIZE-ROWS row 86, source LOCALIZE-S2-B]
- T5 (translation text): FINDINGS — the source reports judge T4/T5 jointly; one verdict word covers both [LOCALIZE-ROWS row 86]
- FIX5 re-judgement: none — no OPEN items at the ledger determination [GOSIGN2-LEDGER (b) row 86]
- Computed against: canonical commit b5cb7241f527a44933e45599b41df210690771c4; candidate file pages/theme:eventyr-jp.txt sha256:9622ac1ffd9ef5dedf5b1a92b8b889f7cffae6d592f681501f295d7183d9498f; record: GOSIGN2-LEDGER.md + GOSIGN2-LEDGER-SUPPLEMENT.md as of the FIX5 head 435a6bb
<!-- END GENERATED VERDICT STAMP -->

## Status

| | |
|---|---|
| Verdict | **PASS** — passed at the ledger determination; this theme had no OPEN items and no §(e) register entry (GOSIGN2-LEDGER (b) row 86) |
| Standing items | **DISPOSITIONED** — T1 pseudo-ref ×49 (class (ii), section 11); the render row's items (KB-33/KB-34 sample overflow family; KB-40 page runtime-hotlink; KB-36 WebKit CC glyph; decoration assets 404 as owner-deferred, KB-58, section 11); T4's P9 item dispositioned under ruling 2 in the ledger §(c3) line (section 5) |
| Go-sign basis | COMPLETION-REPORT.md §10 (go-sign issued; 81 FIXED / 26 DISPOSITIONED / 0 OPEN across the sweep) |
| Named exception | None for this theme (the sweep's single named exception is theme:amethyst-v2, which has no candidate) |

## Provenance

| | Original | Candidate |
|---|---|---|
| Page | theme:eventyr | theme:eventyr-jp |
| Wiki | scp-wiki.wikidot.com | SCP-JP Sigma-10 candidate (canonical repo) |
| Reference revision | 79 (first translation; the candidate's credit block records 初訳時参照リビジョン: 79) | — |
| Source of this copy | Campaign cache `gosign2-lanes/lane-oc-gs-source-s2-2/mirror-eventyr.txt`, via the mirror store (class COPY, hash-verified against review/sources.tsv) | Canonical file `pages/theme:eventyr-jp.txt`, copied at worktree HEAD 5ab991e |
| Lines / bytes | 874 lines / 29,270 bytes | 789 lines / 31,023 bytes |
| SHA-256 | cbae9427197e4d66d069feb7cb7428290a574615663e6b5fa5bbdb523eba57fa | 7be4e2e21dda6ea2c16fab9743900ea2e58dacaed587dcda748ef335a3835cbb |

Wave history: the candidate was created by the Stage 2 EN9 integration (commit 7aed5b7, the LOCALIZE-S2-B wave's port) with its whitespace normalization follow-up (5b6dbe2), and touched last by 1869877 (FIX-CREDIT-D). No FIX-P4 or FIX5 commit touches this file. The T4 row records "No unincorporated upstream updates" for this theme, and sources.tsv carries no drift note: the rev-79 mirror is the port's whole baseline.

## Summary

Eventyr is a Black Highlighter theme for a fantasy setting, heavy with artwork: a base logo plus seven pride-variant logos, background textures, and a decorative type program (Cutive, Lavishly Yours, Philosopher). The port re-bases its delivery on the JP BHL distribution, re-hosts its many image assets to the draft host, moves its fonts from Bunny Fonts to Google Fonts and adds Noto JP fallbacks to its stacks, translates the body, and performs the standard EN-theme furniture conversion with one documented omission: the original's info-module usage example is dropped, with a translator note in its place explaining that SCP-JP uses the credit module (the candidate's own credit block is the working example). Its one T4 finding is the header language: the title "Eventyr" and the English subtitle are kept, dispositioned under ruling 2. Measured churn (diff.md, Tier 2 format: +303/−388, 691 changed lines in 86 change blocks / 26 diff sections); the candidate is shorter than the original chiefly because the info example and the tail delivery module do not carry over.

## Class summary

Auto-classification by review/classify_hunks.py (signature table 2026-11-17.1): 86 change blocks — 47 specific (54.7%), 36 heuristic (41.9%), 3 residue (3.5%), 0 skipped. Pattern citations below name the KB entry; the patterns/ tree state cited throughout is commit 9c5e9079afb01d30cb9fc4ef9d714e5591eb2ffa.

| Label | Blocks |
|---|---|
| COMMENT-TEXT | 1 |
| CREDIT-PREVIEW | 1 |
| CSS-BODY | 1 |
| DELIVERY-HOST | 2 |
| DRAFT-HOST | 16 |
| EXHIBIT-RESTRUCTURE | 5 |
| FONT-IMPORT | 1 |
| IFTAGS | 2 |
| INCLUDE-REPOINT | 1 |
| INFO-DEL | 1 |
| JPFONT-LOAD | 1 |
| JPFONT-STACK | 5 |
| LICENSE-BOX | 1 |
| SELF-DELIVERY | 3 |
| TASL-FIELDS | 1 |
| TRANS-UNANCHORED | 42 |
| TRANSLATION-ANCHORED | 15 |
| WS-ONLY | 8 |

Adjudication for this README (every A-tier block and every primary family was read against the bytes): the five EXHIBIT-RESTRUCTURE primaries are the head-region exhibit seams (the frame and credit exhibits at the page head, blocks B2, B4, B5) and the tail (B86, the deleted tail delivery module) — include and furniture changes inside exhibit regions, adjudicated in sections 2, 3, and 8 against the exhibit census, not content restructurings. The three residue blocks resolve in the appendix (an added exhibit heading, the license section's relocation seam, an exhibit-tail blank line). The font-family blocks (B61, B76–B79) are P7 stack rewrites per the standing lesson, narrated in section 4. After adjudication no block is left unexplained.

## Standing sections

### 0. Header and provenance frame

- **What:** Theme theme:eventyr-jp; original theme:eventyr on scp-wiki at reference revision 79; candidate `pages/theme:eventyr-jp.txt`. Provenance route: derived from the original at the reference revision by the LOCALIZE-S2-B wave (sources.tsv kind: standard; no production JP counterpart exists for this theme, so the R4 adoption question does not arise). The frame: the candidate opens with a module CSS importing its own /1 from the draft host (candidate L2), then three `:scp-jp:component:interwiki-style` includes — priorities 1 and 2 delivering BHL's normalize and black-highlighter stylesheets from scp-jp.github.io, priority 3 delivering its own /1 from the draft host (candidate L5–17) — then the credit block and the localized gate arrangement of the JP form. The original's frame is the same shape on EN hosts: `:scp-wiki:component:interwiki-style` includes (original L6, L11) with its head module importing BHL from nu-scptheme.github.io (original L3–4), plus a tail delivery module the candidate does not keep (section 3).
- **Why:** Section 0 declares the route so later counts are read against the right baseline; the gate's tag is P2, the stack is P6/T3 with T9 base delivery (sections 2–3).
- **Verify:** The sources.tsv row for eventyr-jp; `sha256sum original.txt` against the Provenance table; the frame lines at candidate L1–19.
- **Disposition:** Standing (the route itself); the frame changes are recorded in sections 2 and 3.

### 1. Credit and attribution

- **What:** The original's credit furniture is the EN info pair (`:scp-wiki:info:start` at original L23, `info:more` at L31, `info:end` at L33) presented as a fill-in example, with no preview block. The candidate installs the JP preview block at the head (candidate L20–29) with the eight ruling-3 fields (title エヴェンティール テーマ; 翻訳責任者 AI; 翻訳年 2026; 原題 Eventyr Theme; 著作権者 [[*user FlyPurgatorio]]; 作成年 2024; 初訳時参照リビジョン 79; the source link, candidate L28, naming scp-wiki.wikidot.com, the original's recorded host). The info example itself is deleted (block B6, INFO-DEL) and replaced by the translator note of section 10 — the JP reader's working example is the candidate's own credit block, not a specimen of a module SCP-JP does not use. The candidate also adds the closing license box (`license-box-backend` at candidate L662, `license-box-end` at L787; block B85), whose entries document the eight logo files (the base logo and the seven pride variants), each entry carrying the original-language file name alongside the JP file name.
- **Why:** P3/T1: the preview credit module is the rate-bearing JP form (KB-09), and the info pair is the EN form it replaces. The example's deletion follows the same conversion: an example of a module the target wiki does not run would teach a dead form, and the port documents the omission in-file rather than leaving a silent gap (section 8). The license box is the JP attribution supplement for a theme whose artwork set is large.
- **Verify:** `grep -n 'info:start\|credit:\|license-box' candidate.txt` — no info include, one preview pair, one license-box pair; read candidate L20–29 and L37–38 (the note).
- **Disposition:** FIXED (GOSIGN2-LEDGER §(c3): P3 credit fields FIXED, credit waves, checker-verified).

### 2. Includes and components

- **What:** The usage exhibit's two escaped includes are repointed (candidate L34–35, against the original's `:scp-wiki:` forms at original L38–39): candidate L34 names `:scp-jp:theme:black-highlighter-theme`, the production JP page, and stands as built; candidate L35 as built named `:scp-jp:theme:eventyr` — a repoint that changed the branch prefix but kept the plain slug, so that exhibit named a page that does not exist on scp-jp — and the usage-example population sweep has since completed it on the same line to `:scp-jp:theme:eventyr-jp` (SWEEP-USAGE.md; canonical commit b5cb724). The logo image-block include keeps its bare form with its `name=` re-hosted to the draft host and its caption translated (candidate L42); the original's hub-logo image-block near its head (original L20, an `http://` file URL with a placeholder caption) has no candidate counterpart — it was a hub cross-reference specimen, and the candidate's body opens with its own logo exhibit instead. The original's tail `:scp-wiki:component:toggle-sidebar-bhl` include (original L870) is not carried: it belongs to the tail furniture deleted with the tail delivery module (section 3), and no render item charges its absence.
- **Why:** P1 (KB-15) for the repoints: each names the JP counterpart that exists. That holds for the L34 production page as built; the L35 self-reference as built satisfied the branch half of the rule only — its plain slug named no JP page — and the sweep's completion to the posting name is what brings it under the rule. The toggle include is part of the original's page-tail delivery apparatus rather than a user-facing component the port must reproduce; its deletion is recorded here so the census in section 8 is complete.
- **Verify:** `grep -n '\[\[include' candidate.txt` — the frame three, the credit pair, the two exhibit lines, the image-block, and the license-box pair; no `:scp-wiki:` include survives.
- **Disposition:** Applied; no foreign include kept, no named exception needed.

### 3. Delivery and code loading

- **What:** Delivery consolidates at the head, as in the original's own frame design: the head module imports the candidate's own /1 from the draft host (candidate L2), and the frame delivers BHL from scp-jp.github.io at priorities 1–2 and the own /1 at priority 3 (candidate L5–17). The original additionally carries a tail module (original L873) importing its own /1 from scp-wiki (with a double-slash URL, `scp-wiki.wikidot.com//local--code/...`); the candidate deletes that tail module (block B86) — one delivery path, at the head, replaces the original's two. Inside the exhibit, the CSS `url()` references are re-hosted to the draft host throughout (16 DRAFT-HOST label occurrences: the background textures and logo files under theme%3Aeventyr-jp). The candidate's exhibit is its first code block, so its /1 address is correct against its own count — the check section 3 of the enlightened-eyes package in this batch shows failing elsewhere; here it passes by construction and by the same probe shape (the framed delivery is what the render lane measured).
- **Why:** P4/T9: base delivery from the JP BHL distribution, own-code delivery from the JP host; the draft-host form of the own lines is KB-41, class (iii), rewritten at posting. Deleting the redundant tail path is the deduplication the FIX4 waves applied elsewhere (KB-65's instinct): two imports of one code page are a drift hazard, not redundancy.
- **Verify:** `grep -n 'local--code\|github.io' candidate.txt` against the lines above; no nu-scptheme.github.io or scp-wiki local--code line survives.
- **Disposition:** DISPOSITIONED (draft-host lines, class (iii)).

### 4. Fonts and assets

- **What:** The exhibit's import head is rebuilt (block B61): the BHL imports appear at the exhibit's head from scp-jp.github.io (candidate L274–275, matching the frame), the three display faces move from fonts.bunny.net to Google Fonts at identical families (Cutive, Lavishly Yours, Philosopher; candidate L279–281 against original L491–493), and Noto Sans JP / Noto Serif JP are added (candidate L284–285, JPFONT-LOAD). The stacks follow (JPFONT-STACK ×5, blocks B61 and B76–B79): `--header-font: Lavishly Yours, "Noto Serif JP", serif` and `--title-font: Cutive, "Noto Serif JP", serif` (candidate L322–323) are the shape — every Latin display stack gains the JP serif fallback, and the body stacks gain Noto Sans JP. The T4 row notes the EN font-host move was "correctly not followed": the original's Bunny Fonts hosting is a font CDN, not theme delivery, and the port's Google Fonts choice is the JP-standard one. Assets: the logo set and textures are re-hosted to the draft host (section 3); the render row's decoration-asset 404s are the owner-deferred hosting state (KB-58), not mis-pointed lines.
- **Why:** P7/T5 with KB-16: the port loads JP faces and names them in its stacks — the font-stack rewrite shape — while keeping every Latin face the original names. Asset re-hosting is P4/T9; the deferred 404s are KB-58 (owner decision 2026-11-16).
- **Verify:** Read candidate L274–285 against original L491–493; `grep -n 'bunny.net' candidate.txt` returns nothing; the stacks are at candidate L322–323 and their exhibit twins.
- **Disposition:** Standing (part of the port); the decoration assets are DISPOSITIONED (KB-58, owner-deferred).

### 5. Header, sidebar, and site furniture

- **What:** The header variables are set in the exhibit: `--logo-image: var(--eventyr-base)` (candidate L294, the re-hosted base logo by variable), `--header-title: "Eventyr"` and `--header-subtitle: "The cycle continues, set to a new tune"` (candidate L295–296) — both kept in English. That keeping is T4's one display-affecting finding for this theme (P9). Sidebar furniture arrives from the BHL base; the original's tail toggle include is dealt with in section 2.
- **Why:** P9/T6 is the class that would override the header language; the ledger dispositioned this theme's P9 under ruling 2, which takes header and title language out of migration-correctness scope as case-by-case translation taste. "Eventyr" is the setting's name and the subtitle its motto line, which is the circumstance the ruling's reservation exists for.
- **Verify:** Read candidate L294–296 against the original's corresponding variables in diff.md.
- **Disposition:** DISPOSITIONED (GOSIGN2-LEDGER §(c3): P9, ruling 2).

### 6. Text translation

- **What:** The body is translated throughout: 15 TRANSLATION-ANCHORED primaries and the TRANS-UNANCHORED mass (42 label occurrences), covering the usage prose, the setting introduction, the specimen captions (the sample link line at candidate L46 is the original's specimen, translated: 一度は訪れたことのあるリンクでしょう、たぶん), and the license entries. English survives reader-visible in the header strings (section 5), the credit 原題 field, and quoted specimen terms inside the translator note. In-CSS text (R1): the exhibit's comments are the original's, carried, apart from the font-localization marks of section 4.
- **Why:** P10 (body, usage, and sample translation is the port's purpose) and KB-18 (reader-visible strings). The unanchored mass was verified in bulk against the mirror for this README.
- **Verify:** The pairs are diff.md's 26 sections in order; an English-prose scan of candidate.txt outside the exhibit returns the header motto and the credit field.
- **Disposition:** Standing (the port itself); no untranslated reader-visible text remains outside the items named.

### 7. Links

- **What:** No LINK-REPOINT block fired. The candidate's one attribution link is the credit source link (candidate L28), naming scp-wiki.wikidot.com — the original's recorded host in review/sources.tsv — so the mis-hosted-link defect class does not occur and no probe was needed. The body's one prose URL is the link specimen (candidate L46, a google.com example carried from the original as a specimen, not a reference).
- **Why:** P11 under the dead-reference evidence standard: a link that already names the serving original needs no change; specimens are content, not references.
- **Verify:** `grep -n 'wikidot.com' candidate.txt` — the credit source link is the only live hit.
- **Disposition:** Standing; no dead or mis-hosted link found.

### 8. Structure

- **What:** The localize.md closing rule holds with two recorded exceptions, both deliberate. (a) The info-module example (original L23–33) is omitted, with the translator note standing in its place (candidate L37–38): an omission with its ground stated in-file, of a specimen for a module the target wiki does not use — the R3 census counts it as a documented omission, not a silent deletion, and the theme's actual credit furniture is present in working form (section 1). (b) The tail delivery module and its toggle include are deleted (block B86), delivery being consolidated at the head (section 3). Everything else corresponds: an exhibit census (usage exhibits, logo exhibits, the code exhibit, the license region) matches the original's sequence, and the classifier's five EXHIBIT-RESTRUCTURE primaries adjudicate to the head furniture changes (B2, B4, B5) and this tail (B86).
- **Why:** R3 exists to force exactly this adjudication, because a restructure and a deletion share a diff shape and ledger class I charges the silent form; here both candidate deletions carry their grounds in the file or in the delivery design, and the census, not the label, decides.
- **Verify:** Compare `grep -n '\[\[include\|\[\[code\|\[\[collapsible' original.txt candidate.txt` — the sequences correspond apart from the two recorded exceptions.
- **Disposition:** Standing; no silent structural deletion, no class I item.

### 9. Formatting only

- **What:** Eight whitespace-only blocks (WS-ONLY ×8, in the exhibit: the EN9 whitespace normalization, commit 5b6dbe2), plus the exhibit-tail blank-line seam in the appendix (B84). The classifier finds no re-indentation pair (0), so the R7 follow-up-diff hazard is not triggered beyond the normalization itself.
- **Why:** Formatting churn is disclosed as its own class so it is never mistaken for a semantic change.
- **Verify:** The eight blocks are listed in classification.json with their exhibit line ranges (original L540–782 region).
- **Disposition:** None required.

### 10. Porter annotations

- **What:** One translator note, in `//…//` italic-note form at the exact position of the omitted info example (candidate L38): //訳注: 原語版ではこの位置に英語版のinfoモジュール（:scp-wiki:info:start〜end）の記入例があります。SCP-JPではCreditモジュールを使うため、記入例は省いています。// — it tells the JP reader what stood here, why it is gone, and what replaces it. The license box's file entries carry a lighter porter mark of the same kind: each JP file name is annotated with its original-language name （原語版: Eventyr SCP Logo, etc.), keeping the artwork's provenance traceable across the re-hosting. No `[!-- --]` notes and no CSS banner additions exist in the candidate.
- **Why:** R2: porter-added text is part of the change record, and this note is load-bearing — it converts a silent omission into a documented one (section 8(a)).
- **Verify:** Read candidate L37–38; the license entries are at candidate L667–705.
- **Disposition:** Standing.

### 11. Dispositions and exceptions

- **What:** Four items, each with its ground. (1) T1's 49 pseudo-ref errors: class (ii), posting-procedure — the count is this batch's largest because the candidate's exhibit and license box carry many file references (the re-hosted asset URLs and the license entries' source lines) that the checker reads as pseudo-references; they are the draft-host and attribution lines of sections 3 and 1, which the posting procedure rewrites or re-hosts, and fix lanes never "fix" them in the candidate. (2) The sample overflow 337–419px at ≤375 with the shared credit-modal item: the recorded cross-cutting families, static credit replica fixed width (KB-33), preview chrome (KB-34), and the preview-form modal property (KB-32). (3) The page runtime-hotlink item: environment-layer (KB-40) — runtime hosts arrive via the shared site theme chain, not the candidate. (4) The WebKit CC "S" glyph (KB-36) and the decoration assets 404 (KB-58, owner-deferred hosting, expressly not defects in the register's own words). T4's P9 item is argued in section 5.
- **Why:** A disposition is a decision with grounds (AGENTS.md §3 classes (i)/(ii)/(iii); the named KB entries), not an omission; environment-layer lines are recorded as not-charged.
- **Verify:** Each item names its deciding record above; the T1 classes are T1-ROWS row 86's, the render items are the ledger §(c2) block for this theme (RENDER-S2-B (EN9)).
- **Disposition:** DISPOSITIONED (all four).

### 12. Verification

- **What:** (a) T1 source check (T1-ROWS row 86): exit 1, 49 errors / 1 warn / 1 info; all 49 errors are pseudo-ref, class (ii); there is no class (i) error. (b) T2/T3 render (RENDER-ROWS-1, lane RENDER-S2-B): FINDINGS, the items of section 11(2–4), all dispositioned; engine coverage is the full matrix as run by the lane. (c) T4/T5 (LOCALIZE-ROWS row 86): FINDINGS jointly, display-affecting findings 1 (the P9 header item, section 5); the ledger §(c3) line records the theme's T4 outcome as P9 DISPOSITIONED (ruling 2). (d) This package is self-verifying: `python3 review/build_review.py --check` regenerates diff.md and the verdict stamp from the two byte-faithful copies in this directory and compares. Counts in this README are the generator's (difflib, autojunk off): +303/−388 in 86 change blocks / 26 diff sections (Tier 2 format).
- **Why:** Verification claims name the cheapest deciding check and its result, not a general assurance.
- **Verify:** Re-run the checker on `pages/theme:eventyr-jp.txt` and `python3 review/build_review.py --check` in this repo.
- **Disposition:** PASS (GOSIGN2-LEDGER (b) row 86; go-sign, COMPLETION-REPORT §10).

## Per-theme record

### An omission that documents itself

Eventyr is the batch's cleanest example of the difference between a deletion and an omission. The original page teaches its credit furniture by example, showing the EN info module's fill-in form; a mechanical port would have carried that example across (translated, repointed), teaching JP users a module their wiki does not run. The candidate instead deletes the example and leaves a note at the exact spot saying what was there and why it is gone. Every other deletion-shaped block in this diff resolves the same way when read: the tail module (delivery consolidated, section 3), the hub-logo specimen (superseded by the theme's own logo exhibit, section 2). The review value of the package is that each of those resolutions is stated with its ground, so a third party does not have to take the port's completeness on faith.

### The usage example's posting name

The usage example at candidate L35 as built read `@@[[include :scp-jp:theme:eventyr]]@@`: the porting wave's repoint changed the branch prefix from `:scp-wiki:` but left the plain name, so the example named a page that does not exist on scp-jp (the campaign's settled rule for usage examples, AGENTS.md §6). The usage-example population sweep has since completed the reference to `:scp-jp:theme:eventyr-jp` on the same line (sweep report SWEEP-USAGE.md in the campaign record, R/review-scout/; canonical commit b5cb724), one of its 287 repairs across 157 candidates. The exhibit's other line is not a sweep line: candidate L34 names `:scp-jp:theme:black-highlighter-theme`, the production JP page, and stands as built. This package documents the corrected candidate; its stamp reads STALE against the pre-repair verdict, by design.

## Appendix — residue blocks

For class M the residue set is resolved in one table, not per-block slots.

| Block | Shape | Resolution |
|---|---|---|
| B7 (no signature) | Candidate L39–40: the exhibit heading `+ 見本` added where the original passes straight from the credit region into prose (original L34–35) | An added exhibit heading in the candidate's layout of the samples section; no content removed (section 8) |
| B58 (no signature) | Original L268–269 → candidate L266: the `@@ @@` marker lines pair off around the original's `[[collapsible show="+ Image licensing"…]]` opener | The license section's relocation seam: the candidate's license material stands in the tail license box (section 1), so the collapsible opener has no counterpart at this position |
| B84 (no signature) | Original L864–865 → candidate L656: a blank line before the exhibit's `[[/code]]` close | Exhibit-tail formatting seam (section 9) |

## Change set outside the two diffed files

The diff covers two files; the port's record is larger. `pages/theme-decoration-sample-eventyr-jp.txt` is the decoration sample the render checks ran against (its overflow and credit-modal items are section 11(2)). The candidate layers over Black Highlighter delivered from the JP distribution (section 0) — that base is an environment delivery, not a candidate file in this repo's port set, and no base package is owed here. There are no companion fragments and no inbound-link repairs in other candidates for this theme.

## License and attribution

- **Title:** Eventyr Theme
- **Author:** FlyPurgatorio
- **Source:** https://scp-wiki.wikidot.com/theme:eventyr — revision 79
- **License:** Creative Commons Attribution-ShareAlike 3.0 (CC BY-SA 3.0) — license deed: https://creativecommons.org/licenses/by-sa/3.0/
- **Adaptation:** This package holds a Sigma-10 migration port of the work; changes were made. See "Summary" and "Standing sections" in this README for what changed and why. Translator: AI (Muse and its delegated agents), per the campaign's standing attribution rule.
