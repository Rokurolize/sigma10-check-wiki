# Review package — theme:drunken-alley-jp

<!-- BEGIN GENERATED VERDICT STAMP — do not hand-edit; regenerate with review/build_review.py -->
## Verdict stamp
- Theme: theme:drunken-alley-jp — origin CN, population #184 [GOSIGN2-LEDGER (b) row 184]
- Overall: PASS — NOT PASS at the ledger determination (section (e) register); its one OPEN item re-judged FIXED by the FIX5 wave; go-sign issued 2026-11-17 (COMPLETION-REPORT §10) [GOSIGN2-LEDGER (b); GOSIGN2-LEDGER-SUPPLEMENT (d)]
- T1 (source check): FINDINGS (classified) — baseline 2026-11-16: exit 1, 2 errors / 1 warn / 2 infos (hotlink×1, pseudo-ref×1); standing classes dispositioned in register c1 [T1-ROWS row 219; GOSIGN2-LEDGER (b) row 184]
- T2/T3 (render, combined verdict): FINDINGS — [combined T2/T3] report `FINDINGS` — page runtime-hotlink site-theme chain + scp-wiki-cloud.wdfiles.com; sample credit-modal (preview-form) + page-overflow 377–423px@320/375 + 884px@768. [RENDER-ROWS-2 (RENDER-S2-E (CN5))]
- Engine coverage: full matrix as run by the lane; coverage not separately caveated in the row [RENDER-ROWS-2 row]
- Credit modal: sample credit-modal errors dispositioned preview-form (credit:start-preview has no modal mechanism; GOSIGN-TESTS T2 amendment, 2026-11-16) [RENDER-ROWS-2 (RENDER-S2-E (CN5))]
- T4 (localize patterns + follow-up): FINDINGS — display-affecting findings: 3 [LOCALIZE-ROWS row 183, source LOCALIZE-S2-D]
- T5 (translation text): FINDINGS — the source reports judge T4/T5 jointly; one verdict word covers both [LOCALIZE-ROWS row 183]
- FIX5 re-judgement: item 55 (class I) FIXED — FIX5-STRUCTB §2, commit 435a6bb: golden-wind base prerequisite line restored at L34 pointing at theme:golden-wind-jp (original L22, rev 50 fetched); spot-verified for this supplement [GOSIGN2-LEDGER-SUPPLEMENT (a) item 55; (c) check 7]
- Computed against: canonical commit 435a6bb7193bf09bc02fa5bf529280c2a2389ec2; candidate file pages/theme:drunken-alley-jp.txt sha256:e9dcbc6844ded0966e84e43761e9a631ac0db2365e6f56ca244061fe2a084eb8; record: GOSIGN2-LEDGER.md + GOSIGN2-LEDGER-SUPPLEMENT.md as of the FIX5 head 435a6bb
<!-- END GENERATED VERDICT STAMP -->

## Status

| | |
|---|---|
| Verdict | **PASS** — go-sign re-run (this theme is one of the 286 of 286 pass-eligible themes) |
| Blocking items at ledger time | GOSIGN2-LEDGER.md §(e) item 55 [I] (golden-wind base prerequisite deleted from the usage procedure) |
| Re-judgment | GOSIGN2-LEDGER-SUPPLEMENT.md row 55: **FIXED** (FIX5-STRUCTB §2, commit 435a6bb); re-derived from this package's bytes in the per-theme record below |
| Standing items | **DISPOSITIONED** — ledger §(c4): the dead `url()` removals carry the (c4) KB-03 entry (FIX4-IWA); ledger §(c3): P3 credit fields FIXED (credit waves); ledger §(c2) render row: page-overflow (KB-33/KB-34 family), runtime-hotlink site-theme chain (KB-40), scp-wiki-cloud header host (T4 special exception), credit-modal preview form (KB-32) |
| Go-sign basis | COMPLETION-REPORT.md §10 (go-sign issued; 81 FIXED / 26 DISPOSITIONED / 0 OPEN across the sweep) |
| Post-verdict change | None recorded: this candidate's bytes are the bytes the supplement judged (its SHA-256 matches the verdict-era file at commit 435a6bb), which is why the stamp reads PASS rather than STALE |
| Named exception | None for this theme (the sweep's single named exception is theme:amethyst-v2, which has no candidate) |

## Provenance

| | Original | Candidate |
|---|---|---|
| Page | theme:drunken-alley | theme:drunken-alley-jp |
| Wiki | scp-wiki-cn.wikidot.com | SCP-JP Sigma-10 candidate (canonical repo) |
| Reference revision | 50, as recorded in the candidate's credit block: **初訳時参照リビジョン:** 50 | — |
| Source of this copy | Mirror store `orig-drunken-alley-rev50.txt` (class COPY, byte-true copy of the campaign cache `gosign2-lanes/lane-oc-gs-localize-s2-D/orig-drunken-alley.txt`, fetched once by the LOCALIZE-S2-D lane) | Canonical file `pages/theme:drunken-alley-jp.txt`, copied at worktree HEAD e821e37 |
| Lines / bytes | 596 lines / 14,301 bytes | 603 lines / 15,043 bytes |
| SHA-256 | eb2c2ae4f06b71ebd9904efbfb2f992e6f9bfe79c72603d24844a5e0cdb37b39 | e9dcbc6844ded0966e84e43761e9a631ac0db2365e6f56ca244061fe2a084eb8 |

One record correction belongs here. The `review/sources.tsv` note for this row claims the original was "superseded upstream since the reference revision", but the follow-up artifact that note itself cites (`diff-drunken-alley-from50.txt` in the campaign record) records rev 50 → rev 50, no changes: upstream latest remains revision 50 and this mirror is current. The note's wording is the defect (the same wrong-note shape corrected earlier for ambrose, alcur, and inland-empire); it is flagged for central correction and the package proceeds on the artifact's evidence.

## Summary

Drunken Alley is a Golden Wind-based theme whose entire stylesheet is one large code exhibit (553 of the original's 596 lines) that the page imports back into itself. The port keeps that topology exactly: the self-import and the new interwiki-style frame both name code block 1, the CSS exhibit, and the base layering is a prose-level prerequisite in the usage procedure, not an include. The measured churn (diff.md: +96/−89 in 65 blocks) is mostly the translation of the exhibit's ~40 CSS section comments plus a small set of argued edits: the http→https scheme upgrade on the header logo, the removal of one dead `background-image: url("")` declaration, and three P7 font-stack rewrites. The one blocking defect, the deleted golden-wind prerequisite line in the usage procedure, was restored by FIX5 and is re-derived below. The theme's lone credit nit and its T1 hotlink were both charged during the sweep and stand dispositioned with their grounds stated.

## Standing sections

### 0. Header and provenance frame

- **What:** The original opens with a `[[module CSS]]` (original L1–3) importing the page's own code block 1 from the CN files host; the page's own bare Rate follows (L5–7). The candidate opens with the same module, re-hosted to the draft host (candidate L1–3), and adds the interwiki-style frame at priority 1 naming the same /1 (candidate L4–7). Provenance route: derived from the original at reference revision 50 (mirror class COPY; see Provenance).
- **Why:** The header frame is where the original declares its delivery; the candidate's replacement delivery is recorded in section 3. The frame is the P6/T3 supplement (patterns/ KB-07 family; patterns commit 9c5e9079afb01d30cb9fc4ef9d714e5591eb2ffa).
- **Verify:** Read original L1–9 against candidate L1–9.
- **Disposition:** Recorded; the delivery change is argued in section 3.

### 1. Credit and attribution

- **What:** The original has no credit block; its authorship is the first tab's prose at original L14, naming [[*user Dr Roger_F_XL]] as the theme's maker. The candidate adds the preview credit block (`:scp-jp:credit:start-preview`/`end-preview`, candidate L10–21) with the eight standard fields; **著作権者** is [[*user Dr Roger_F_XL]], the original's sole authorship statement, with creation year 2023, reference revision 50, and the source link to the CN original. The T4 lane counted the new credit as 8 of 8 with a single nit (the source field's branch label, since corrected in form); the credit waves' completion of this theme's fields is recorded at ledger §(c3).
- **Why:** P3/T1 credit supplement and ruling 3 (2026-11-16) for the eight fields and the 翻訳責任者： AI credit.
- **Verify:** Read candidate L10–21 against original L14; count the eight fields.
- **Disposition:** FIXED (credit waves; ledger §(c3)).

### 2. Includes and components

- **What:** Original includes: the escaped base-prerequisite specimen `@@[[include :scp-wiki-cn:theme:golden-wind]]@@` (L22), the escaped self-include specimen (L26), and `:scp-wiki-cn:component:image-block` for the header-logo exhibit (L32–35). Candidate includes: the interwiki-style frame (L4), the credit pair (L10/21), the escaped base specimen now naming `theme:golden-wind-jp` (L34, the FIX5 restoration — the per-theme record), the escaped self-include specimen naming the bare `theme:drunken-alley-jp` (L38), and `component:image-block` in the bare same-wiki form (L44) with its image re-hosted to the draft host (L45). The usage specimen's float and Rate lines, which the original left unescaped (original L27–29), are escaped in the candidate (L39–41), so the specimen renders as text rather than executing inside the candidate page. The classifier's EXHIBIT-RESTRUCTURE label on block B14 is adjudicated against the exhibit census: the image-block exhibit is retained with the same role and caption (題圖， translated ロゴ) — the change is an include repoint plus an asset re-host, not a dropped or replaced exhibit.
- **Why:** P1 include repoints; specimen escaping keeps an example an example. The base prerequisite's restoration is the item-55 fix, argued in the per-theme record.
- **Verify:** `grep -n '\[\[include' original.txt candidate.txt` and compare the two lists.
- **Disposition:** Standing; the prerequisite line is FIXED (item 55).

### 3. Delivery and code loading

- **What:** Own-code delivery on both sides. The code census in document order has exactly one entry: the `[[code type="css"]]` exhibit (original L42–594; candidate L54–601). The head module's self-import names that block on both sides (original L2 `theme:drunken-alley/1` on the CN host; candidate L2 `theme%3Adrunken-alley-jp/1` on the draft host), and the frame names the same /1 (candidate L5). The FIX-CODEADDR population audit does not list drunken-alley in its no-target class; the address resolves to the block that holds the CSS. The base theme (Golden Wind) is not pulled by any include at page level: the layering is declared in the usage procedure (section 2 and the per-theme record), exactly as the original declares it. Draft-host URLs are the draft-form class (iii), rewritten to the production host at posting. The topology pass confirms the same component kinds on both sides with no relocations.
- **Why:** P4/T9 delivery repointing: the candidate's runtime no longer depends on the CN files host.
- **Verify:** Read candidate L1–7; `grep -n '\[\[code' candidate.txt` (one block) and match /1 to it.
- **Disposition:** Standing.

### 4. Fonts and assets

- **What:** Three font-stack rewrites inside the CSS exhibit, all P7 font-stack rewrites (the classifier labels the surrounding blocks CSS-BODY heuristic; they are narrated here as the P7 class they are): the base text stack gains Yu Gothic, Hiragino Kaku Gothic ProN, and Meiryo behind Courier New (original L62 → candidate L70); the display stack gains the same JP faces behind Impact and Arial Black (original L95 → candidate L103); and the rate-points stack gains Courier New and Yu Gothic behind Digital-7 (original L339 → candidate L346). The theme loads no font by @import or @font-face on either side; its stacks' named faces arrive through the base (the golden-wind-jp candidate loads Noto Sans JP and Noto Serif JP) or are system faces. One named face is loaded by neither layer on either side: Digital-7, first in the rate-points stack — an inherited state the port did not create, recorded here so the absence is a checked fact. Assets: the header logo's URL keeps its original host (`scp-wiki-cloud.wdfiles.com/local--files/roger/drunk-logo`) with only the scheme upgraded, `http://` → `https://` (original L44 → candidate L56) — the T1 baseline's single hotlink error and the T4 lane's recorded special-exception host; the exhibit logo file is re-hosted to the draft host (candidate L45). One declaration was removed outright: the `.code` rule's `background-image: url("");` (original L178), an empty-URL dead declaration, removed by FIX4-IWA and recorded under the ledger's (c4) KB-03 entry; the rule's remaining declarations are byte-identical (candidate L184–190), including its `overflow: hidden` line, which the original also carries.
- **Why:** P7/T5 (stack rewrites for JP faces), P5 (asset re-hosting), and the dead-code removal class: an empty `url("")` resolves against the page URL and fetches the page as its own background, so the declaration is not harmless.
- **Verify:** `grep -n 'font-family' candidate.txt` (three stacks); read candidate L56 and L184–190 against original L44 and L172–179.
- **Disposition:** Standing; the dead-`url()` removal is DISPOSITIONED (ledger §(c4), KB-03), the scheme upgrade closes the T1 hotlink as recorded in section 11.

### 5. Header, sidebar, and site furniture

- **What:** None as a change class. The theme defines no `--header-title`, `--header-subtitle`, or `--logo` variables on either side (grep count 0); its header is styled by the `div#header` rule inside the exhibit, whose only edit is the scheme upgrade recorded in section 4. The header-logo exhibit in the body is retained (section 2).
- **Why:** The ground for "none" is the variable grep on both files, stated so a reviewer can tell checked-absent from not-considered.
- **Verify:** `grep -n -- '--header-title\|--header-subtitle\|--logo' original.txt candidate.txt` returns nothing.
- **Disposition:** None required.

### 6. Text translation

- **What:** The translation mass is mostly inside the CSS exhibit: COMMENT-TEXT labels fire in 40 of the 65 change blocks (for example the section banners at original L60 → candidate L68, L77 → L85, L93 → L101), which is R1 in-CSS comment translation, porter-visible only. The body prose pairs one-to-one in 12 TRANSLATION-ANCHORED blocks (usage text, tab labels, exhibit captions). Two localization touches ride inside specimens: the example article number CN → JP (original L28 `SCP-CN-XXXX` → candidate L40 `SCP-JP-XXXX`), and the T4-recorded credit nit (section 1). The classifier's one residue block, B10, is the usage specimen region: adjudicated against the bytes, its content is the escaping change and the CN→JP example number recorded in section 2 — exhibit mechanics, not unaccounted content.
- **Why:** P10 body translation and R1 for in-CSS text. The comment mass is expected heuristic volume for a theme whose exhibit is heavily commented; it is resolved here by shape (banner and section comments translated in place, selectors and declarations untouched around them).
- **Verify:** Read any three comment pairs (for example original L60/L77/L93 against candidate L68/L85/L101); `grep -n 'SCP-JP-XXXX' candidate.txt`.
- **Disposition:** Standing.

### 7. Links

- **What:** The candidate's source link points back to the original page (credit block, candidate L19, host scp-wiki-cn.wikidot.com, the recorded host in sources.tsv). The body prose carries no other external links on either side; the derivation statement (Golden Wind) is an include specimen, handled in section 2, not a prose link.
- **Why:** P11 repoints govern the port's own reference surface; there is nothing further to repoint in this file.
- **Verify:** `grep -n 'wikidot.com' candidate.txt` (the source link only).
- **Disposition:** Standing.

### 8. Structure

- **What:** The localize.md closing rule holds: component order, selector and variable names, and the single code-css exhibit structure are preserved (the topology pass reports the same component kinds on both sides and no moves). The one structural removal is the original's page-level bare Rate (original L5–7): it is gone from the candidate, whose only Rate is the escaped specimen inside the usage example (candidate L40). This was never a class-B item — the ledger charged no item for it — because the original carried no credit module for the bare Rate to duplicate; the removal rides on the credit-block swap of section 1 (the new preview credit module is rate-bearing, so keeping the page-level module would have created the duplication the B class exists to prevent). The classifier's RATE-EXHIBIT-KEPT-CANDIDATE label on block B2 records the specimen's survival, not the page-level module's. The original defines no include-parameter gates and no `{$...}` slot definitions (grep count 0 on both sides), so there is no documented mechanism whose definitions could be absent.
- **Why:** R3 requires removals to be argued, not merely diffed; the Rate reasoning is stated plainly here because a reviewer comparing the two file heads will otherwise read it as an unexplained drop.
- **Verify:** `grep -n 'module Rate\|module rate' original.txt candidate.txt` (L6 page-level and L28 specimen on the original; L40 specimen only on the candidate).
- **Disposition:** Standing (removal argued; no ledger item was ever charged for it).

### 9. Formatting only

- **What:** Minor. WS-ONLY accounts for 1 of the 65 change blocks, and the classifier reports 0 re-indentation blocks. There is no wholesale re-indentation in this package.
- **Why:** Formatting-only churn is disclosed as its own class so it is never mistaken for semantic change (R7 is not triggered).
- **Verify:** The WS-ONLY row of the class summary in classification.json.
- **Disposition:** None required.

### 10. Porter annotations

- **What:** None. The candidate contains no `[!-- ... --]` comments and no 訳注 lines (grep count 0), and the classifier's ANNOTATION label did not fire over the 65 blocks; annotations riding inside other labeled blocks were checked for explicitly before writing this section. The only added explanatory text is the credit block's standard field set and the restored prerequisite line.
- **Why:** R2 additions must be listed so they are never mistaken for original content; here the ground for "none" is the grep and the classifier together.
- **Verify:** `grep -n '\[!--\|訳注' candidate.txt` returns nothing.
- **Disposition:** None (checked, absent).

### 11. Dispositions and exceptions

- **What:** The standing dispositions for this theme, each argued in its own section: (1) the T1 baseline is 2 errors / 1 warn / 2 infos: one `hotlink` (the header logo's `http://` URL, original L44) and one `pseudo-ref` (the draft-host self-import, class (iii), KB-41). The hotlink is closed in the current bytes by the scheme upgrade (candidate L56); the host itself is the T4 lane's recorded special exception (the file lives in the original author's own file space on scp-wiki-cloud, and the render row lists the same host as a runtime host), so the disposition is: scheme repaired, host kept by exception. (2) The render row's dispositions: page-overflow 110px@320 and 1067px@375/768 on the page, 329–331px@320/375 on the sample (the KB-33/KB-34 families), the runtime-hotlink site-theme chain (KB-40, environment layer), and the sample credit-modal preview form (KB-32; ruling 5). (3) The dead `url()` removal under (c4) KB-03. No item for this theme is left as an unexplained exception.
- **Why:** A disposition is a decision with grounds, not an omission; this section exists so the full set can be audited in one place.
- **Verify:** Each item names its deciding check in its own section.
- **Disposition:** DISPOSITIONED (all items above).

### 12. Verification

- **What:** The evidence behind the stamp: (a) the FIX5 closure is re-derived from this package's own bytes in the per-theme record (grep-based, re-runnable, and repeated by the supplement's own §(c) check 7); (b) the classifier (classify_hunks.py 0.1.0, signature table 2026-11-17.1, patterns commit 9c5e9079afb01d30cb9fc4ef9d714e5591eb2ffa) labels 65 change blocks, 33 specific / 31 heuristic / 1 residue, and the residue (B10, the usage specimen) is resolved in section 6, so no block is unadjudicated; the auto-class split in diff.md reads mechanical 8 blocks / 24 lines, translation 39 / 100, supplement 4 / 22, residual 14 / 39 — the residual lines are the comment-translation mass resolved in section 6; (c) a brace-depth scan of the code-css channel ends at depth 0 on both sides and never goes negative; (d) this package is self-verifying: `python3 review/build_review.py --check` regenerates diff.md from the two byte-faithful copies and compares. Counts in this README are the generator's (Tier 2 unified): +96/−89, 185 changed lines. A GNU-diff count of the same pair gives 187 changed lines; the difference is alignment choice, not content.
- **Why:** Verification claims must name the cheapest deciding check and its result, not a general assurance.
- **Verify:** Re-run the greps cited above and `python3 review/build_review.py --check` in this repo.
- **Disposition:** PASS (go-sign re-run, supplement).

## Per-theme record

### The FIX5 closure (ledger item 55 [I])

The original's usage procedure is two steps: first include the Golden Wind base theme, then include this theme (original L22 and L26, inside the "how to use" tab). At ledger time the candidate's procedure contained no golden-wind reference at all — the base prerequisite had been deleted in the port, so a reader following the candidate's own instructions would apply the theme without its base and get its unstyled fallback. The ledger charged it as item 55, class I (the row had also lost its base include in the port's delivery consolidation), and FIX5-STRUCTB §2 (commit 435a6bb) restored the prerequisite line pointing at the JP base candidate. The supplement re-judged item 55 FIXED, spot-verified, and its §(c) check 7 repeats the spot check across the STRUCTB population.

Re-derived from this package's bytes: candidate L34, the first line of the usage procedure in the "how to use" tab, reads `> **@@[[include:scp-jp:theme:golden-wind-jp]]@@**` — the prerequisite restored, naming `theme:golden-wind-jp`, which exists as a candidate in this repo (`pages/theme:golden-wind-jp.txt`). The self-include specimen follows at candidate L38, so the two-step order matches the original's. The restoration the supplement records is present and complete in the current bytes.

The companion T4 charges in the same row closed as recorded: the credit block the T4 lane counted 8 of 8 stands at candidate L10–21 (section 1), and the header-image host it flagged as a special exception stands dispositioned in section 11. The row's earlier FIX4 history (the interwiki frame and the dead `url()` removals, FIX4-IWA) is part of this file's state, not of item 55, and is recorded in sections 0 and 4.

## Change set outside the two diffed files

The diff covers two files; the port's full change set is slightly larger. (1) `pages/theme-decoration-sample-drunken-alley-jp.txt` — the decoration sample page used by the render checks. (2) The base the usage procedure names: `pages/theme:golden-wind-jp.txt`, another theme's candidate in the canonical repo, recorded as this theme's prerequisite in the per-theme record. The theme is otherwise standalone in `start-themes.tsv`; it has no fragment or component candidate of its own.

## Multi-wave provenance

The candidate's current state is the product of successive waves, not of a single porting pass: the S2 localization wave (LOCALIZE-S2-D) produced the initial port (translation, delivery re-hosting, exhibit structure, and, as later found, the deleted base prerequisite); the credit waves completed the eight credit fields; FIX4-IWA added the interwiki-style frame and removed the dead `url()` declarations; the render checks ran as RENDER-S2-E (CN4); and FIX5-STRUCTB §2 restored the golden-wind prerequisite (item 55), after which no wave has touched the file. Citations, in place of a changelog: GOSIGN2-LEDGER.md §(c3) (localize row), §(c4) (KB-03 entry), §(c2) (render row), §(e) item 55; GOSIGN2-LEDGER-SUPPLEMENT.md row 55 and §(c) check 7; LOCALIZE-ROWS row 183; T1-ROWS row 219. The go-sign re-run over that record is what the Status block certifies.

## License and attribution

- **Title:** 醉巷 版式
- **Author:** Dr Roger_F_XL
- **Source:** https://scp-wiki-cn.wikidot.com/theme:drunken-alley — revision 50
- **License:** Creative Commons Attribution-ShareAlike 3.0 (CC BY-SA 3.0) — license deed: https://creativecommons.org/licenses/by-sa/3.0/
- **Adaptation:** This package holds a Sigma-10 migration port of the work; changes were made. See "Summary" and "Standing sections" in this README for what changed and why. Translator: AI (Muse and its delegated agents), per the campaign's standing attribution rule.
