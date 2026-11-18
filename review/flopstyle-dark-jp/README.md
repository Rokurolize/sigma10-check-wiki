# Review package — theme:flopstyle-dark-jp (EN → JP port)

<!-- BEGIN GENERATED VERDICT STAMP — do not hand-edit; regenerate with review/build_review.py -->
## Verdict stamp
- Theme: theme:flopstyle-dark-jp — origin EN, population #12 [GOSIGN2-LEDGER (b) row 12]
- Overall: STALE — candidate file changed since the verdict was computed (verdict against 435a6bb-era content, file sha256 now a0f7e3e5293f68b680a98c7d653f523616f670b9775426ca45eecadf6eb2c873); verdict not carried over, re-judgement required
> verdicts below describe the pre-change file
- T1 (source check): FINDINGS (classified) — baseline 2026-11-16: exit 1, 74 errors / 13 warns / 2 infos (pseudo-ref×67, foreign-include×4, hotlink×3); standing classes dispositioned in register c1 [T1-ROWS row 12; GOSIGN2-LEDGER (b) row 12]
- T2/T3 (render, combined verdict): FINDINGS — [combined T2/T3] report `FINDINGS` — T2 did not complete (both URLs ×2: webkit target timeout / baseline crash, no summary); T3 no pointable display defect; not BLOCKED-ENV. [RENDER-ROWS-1 (RENDER-B row 12)]
- Engine coverage: full matrix as run by the lane; coverage not separately caveated in the row [RENDER-ROWS-1 row]
- Credit modal: no credit-modal line in this theme's row; no sample credit-modal error recorded [RENDER-ROWS-1 (RENDER-B row 12)]
- T4 (localize patterns + follow-up): FINDINGS — display-affecting findings: 5 [LOCALIZE-ROWS row 13, source LOCALIZE-A]
- T5 (translation text): FINDINGS — the source reports judge T4/T5 jointly; one verdict word covers both [LOCALIZE-ROWS row 13]
- FIX5 re-judgement: none — no OPEN items at the ledger determination [GOSIGN2-LEDGER (b) row 12]
- Computed against: canonical commit b5cb7241f527a44933e45599b41df210690771c4; candidate file pages/theme:flopstyle-dark-jp.txt sha256:a0f7e3e5293f68b680a98c7d653f523616f670b9775426ca45eecadf6eb2c873; record: GOSIGN2-LEDGER.md + GOSIGN2-LEDGER-SUPPLEMENT.md as of the FIX5 head 435a6bb
<!-- END GENERATED VERDICT STAMP -->

## Status

| | |
|---|---|
| Verdict | **PASS** — passed at the ledger determination; this theme had no OPEN items and no §(e) register entry (GOSIGN2-LEDGER (b) row 12) |
| Standing items | **DISPOSITIONED** — T1 pseudo-ref ×67 and hotlink ×3 (class (ii)) and foreign-include ×4 (the KB-54 named exception for this theme, section 11); the render row's coverage caveat (T2 did not complete; T3 found no pointable defect, section 11); T4's P1 item dispositioned as a posting-procedure matter in the ledger §(c3) line (section 11) |
| Package-level flag | **The draft-host deployment's /2 code page does not match this candidate** — T4 found ten unterminated `url(` declarations in the deployed /2 (header logo and warning-header illustrations not rendering); the current candidate's /2 content carries the same ten declarations, all terminated (verified by scan for this package), while a fresh probe of the deployed /2 (2026-11-17) still shows the unterminated form. The defect is in the deployment state, not in these bytes; a redeploy or byte comparison is owed before posting (section 3) |
| Go-sign basis | COMPLETION-REPORT.md §10 (go-sign issued; 81 FIXED / 26 DISPOSITIONED / 0 OPEN across the sweep) |
| Named exception | None for this theme (the sweep's single named exception is theme:amethyst-v2, which has no candidate; this theme does carry a KB-54 named exception for four foreign-include lines, section 11) |

## Provenance

| | Original | Candidate |
|---|---|---|
| Page | theme:flopstyle-dark | theme:flopstyle-dark-jp |
| Wiki | scp-wiki.wikidot.com | SCP-JP Sigma-10 candidate (canonical repo) |
| Reference revision | 402 (re-translation; first-translation revision 21 — the candidate's credit block records both: 初訳時参照リビジョン 21, 改訳時参照リビジョン 402) | — |
| Source of this copy | Campaign cache `review-wave2-frozen/k1/mirror-flopstyle-dark.txt`, via the mirror store (class FETCH-MISSING, hash-verified against review/sources.tsv) | Canonical file `pages/theme:flopstyle-dark-jp.txt`, copied at worktree HEAD 5ab991e |
| Lines / bytes | 5,330 lines / 149,095 bytes | 5,371 lines / 159,656 bytes |
| SHA-256 | 7b6275fc28f842d833f169c1996b29abac4bd4d2ef1b5897fe6d846c4819e120 | 49336ea448b833daf2180d21dd53ddc5f745787a66e277ed47c23de97f30eb7e |

Wave history: the candidate's own early commits are theme-specific (ee85465: the theme's attachments referenced by absolute URL; b24dd3b: absolute URLs for the remaining scene-break logos), then the shared waves: 8dcac74 (Phase 17: reference revisions recorded — this theme's two-revision record comes from there), b816e10 (gosign2 T1 fixes), 5c32672 (FIX-CREDIT-C), and last 1869877 (FIX-CREDIT-D; the verdict stamp is computed against this commit). Recorded drift: the original has been superseded upstream since the first-translation revision; the campaign record carries the follow-up diff artifact `diff-flopstyle-dark-from21.txt` (sources.tsv K5a-i note), and the mirror in this package is the later rev-402 state the re-translation was made from.

## Summary

Flopstyle: DARK is the largest port in this batch by block count (594) and the most apparatus-heavy: a Flopstyle variant whose CSS ships as three code pages plus a set of companion stylesheet files, whose documentation occupies most of its body, and whose code specimens are typeset with syntax-highlighting spans that defeat the classifier's tokenization (a quarter of its blocks are unlabeled residue of exactly that shape, resolved by shape in the appendix). The port re-hosts everything to the draft host, translates the documentation and the CSS comments, adds the Noto Sans JP fallbacks, and converts the credit to the ten-field re-translation form. Two record-level complications are stated plainly rather than smoothed over: the T4 row's note is truncated in the record after its second item, and its first item — the broken deployed /2 — turns out to be a deployment-state defect that the current candidate bytes do not contain (section 3). Measured churn (diff.md, Tier 2 format: +904/−863, 1,767 changed lines in 594 change blocks / 119 diff sections).

## Class summary

Auto-classification by review/classify_hunks.py (signature table 2026-11-17.1): 594 change blocks — 298 specific (50.2%), 244 heuristic (41.1%), 52 residue (8.8%), 0 skipped. Pattern citations below name the KB entry; the patterns/ tree state cited throughout is commit 9c5e9079afb01d30cb9fc4ef9d714e5591eb2ffa.

| Label | Blocks |
|---|---|
| ANNOTATION | 1 |
| ASSET-REHOST | 2 |
| COMMENT-TEXT | 54 |
| CONTENT-STRING | 14 |
| CREDIT-PREVIEW | 1 |
| CSS-BODY | 14 |
| DELIVERY-HOST | 2 |
| DRAFT-HOST | 74 |
| EXHIBIT-RESTRUCTURE | 13 |
| FONT-IMPORT | 2 |
| HEADERVAR | 3 |
| IFTAGS | 3 |
| INCLUDE-REPOINT | 13 |
| INFO-DEL | 2 |
| JPFONT-STACK | 1 |
| LICENSE-BOX | 1 |
| LINK-REPOINT | 3 |
| SELF-DELIVERY | 2 |
| T7-CREDIT-CSS | 1 |
| TASL-FIELDS | 1 |
| TRANS-UNANCHORED | 254 |
| TRANSLATION-ANCHORED | 152 |
| WS-ONLY | 63 |

Adjudication for this README (every A-tier block and every primary family was read against the bytes; the heuristic mass was verified by shape): the 13 EXHIBIT-RESTRUCTURE primaries carry INCLUDE-REPOINT secondaries and adjudicate to include repoints inside the documentation's exhibit regions (sections 2 and 8). The 52 residue blocks resolve by shape in the appendix: 26 are the syntax-highlighted code specimens (include repoints and translations inside formatting tokens), 26 are one-line heading and specimen-label translations. The font-family blocks are P7 stack rewrites per the standing lesson (section 4). After adjudication no block is left unexplained.

## Standing sections

### 0. Header and provenance frame

- **What:** Theme theme:flopstyle-dark-jp; original theme:flopstyle-dark on scp-wiki at reference revision 402 (the re-translation reference; the first translation referenced rev 21); candidate `pages/theme:flopstyle-dark-jp.txt`. Provenance route: re-derived from the original at rev 402 by the LOCALIZE-A wave, over the earlier rev-21 translation whose existence the credit block's adaptation field records (sources.tsv kind: standard). The delivery frame is this theme's own design and sits at its tail: a module importing its three code pages /1, /2, /3 from the draft host (candidate L5080–5083) and an `:scp-jp:component:interwiki-style` include at priority 2 delivering /2 (candidate L5086–5088), followed by the gated customization modules. The original's tail is the same apparatus on EN hosts (scp-wiki.wdfiles.com code pages).
- **Why:** Section 0 declares the route so later counts are read against the right baseline; the two-revision record matters because the mirror is rev 402 while the drift artifact and the first-translation record run from rev 21. The frame is P6/T3 with P4 delivery (section 3).
- **Verify:** The sources.tsv row for flopstyle-dark-jp (both revisions recorded); `sha256sum original.txt` against the Provenance table; the tail apparatus at candidate L5080–5088.
- **Disposition:** Standing (the route itself); the delivery changes are recorded in section 3.

### 1. Credit and attribution

- **What:** The candidate's credit block stands at the head (candidate L12–23) in the re-translation form: the eight ruling-3 fields plus the two fields this theme's history requires — 翻訳について ("AI による既存の翻訳を基に改変したものです", the adaptation statement: the re-translation adapts the existing rev-21-era translation) and 改訳時参照リビジョン: 402, alongside 初訳時参照リビジョン: 21. 翻訳責任者 AI (2026); 著作権者 GreenGolem; 作成年 2021; the source link (candidate L22) naming scp-wiki.wikidot.com, the original's recorded host. The theme's paired-Rate exhibit later in the body is the labelled paired-Rate exception shape (the c1 register's labelled paired Rate exhibits list names flopstyle-dark): the escaped Rate specimen in its documentation is an exhibit, not a second live widget. A license box closes the documentation region (block B540's LICENSE-BOX secondary, candidate L5066–5067 region).
- **Why:** P3/T1: the preview credit module is the rate-bearing JP form (KB-09); the two extra fields are the attribution standard applied to a re-translation — the adaptation statement is what the TASL record requires when a port modifies an existing translation, and the dual revision fields keep both reference points auditable.
- **Verify:** Read candidate L12–23 against the fields; `grep -n 'module Rate' candidate.txt` returns the documentation specimen only, in escaped form.
- **Disposition:** FIXED (GOSIGN2-LEDGER §(c3): P3 credit fields FIXED, credit waves, checker-verified).

### 2. Includes and components

- **What:** Live includes are few and all JP forms: the credit pair, the image-block exhibits (`:scp-jp:component:image-block`, candidate L49, L158, L190, L327), the info pair in its JP working form (`:scp-jp:info:start`/`end`, candidate L86–88), the tail's `:scp-jp:component:toggle-sidebar` and the frame (section 3). The documentation's many include specimens are repointed inside their syntax-highlight formatting (candidate L317: `:scp-jp:component:flops-header`). The theme specimens as built took the form `:scp-jp:theme:flopstyle-dark` — a repoint that changed the branch prefix but kept the plain slug, so each specimen named a page that does not exist on scp-jp; the usage-example population sweep has since completed every one of them on its own line to `:scp-jp:theme:flopstyle-dark-jp` (candidate L136, L360, L367, L572, L583, L594, L605, L616, L627, L638, L654, L666, L677, L688, L699, L713, L724, L740, L751, L762, L773, L784, L795, and L806; SWEEP-USAGE.md; canonical commit b5cb724). The info-standalone specimen is handled explicitly (blocks B15, B16): the candidate shows `info:start-standalone`/`info:end-standalone` as a code example only, with the translator note of section 10 explaining that scp-jp has no such pages and that the `:scp-jp:info:start` pair is the form to use. Four foreign-include lines stand as the KB-54 named exception: `snippets:bs-image` ×3 and `:scp-wiki:component:text-style` (T1's foreign-include ×4) — NOTFOUND-probed, no JP equivalent exists.
- **Why:** P1 (KB-15) for the repoints: each names the JP counterpart that exists. The theme specimens as built satisfied the branch half of that rule only — their plain slug named no JP page — and the sweep's completions to the posting name are what bring them under the rule. The standalone specimen and the KB-54 four are the rule's other branch: where no counterpart exists, the port either exhibits the form as documentation with a warning (the standalone case) or stands under a named, probed exception (KB-54), rather than repointing to a page that does not exist.
- **Verify:** `grep -n '\[\[include' candidate.txt` — the live includes are `:scp-jp:` forms; the four exception lines are findable by `grep -n 'bs-image\|text-style' candidate.txt` inside specimen regions.
- **Disposition:** Applied for the repoints; the four foreign-include lines stand as DISPOSITIONED (KB-54 named exception, c1 register).

### 3. Delivery and code loading

- **What:** The theme delivers from three code pages and a set of companion files, all re-hosted to the draft host: the tail module imports /1, /2, /3 (candidate L5081–5083), the frame delivers /2 at priority 2 (candidate L5086–5088), and the companion stylesheets (tabview.css inside the /1 block, candidate L1851; backend.css, candidate L4932; documentation.css, inferno.css, maple.css and the other variant files in the tail modules) are imported from the draft host's local--files. Inside /2, the artwork declarations are re-hosted the same way (candidate L1937: `--lgurl` naming alt_logo_bw.png; the warning-header illustrations at L3470–3598; the border images at L4108–4117), with one kept EN-host file (candidate L3515: miscdept.png on scp-wiki.wdfiles.com, another designer's department logo — the P5 class (ii) shape). **The flag:** T4 (LOCALIZE-ROWS row 13, item (i)) found the *deployed* /2 carrying ten unterminated `url(` declarations, so the header logo and all custom warning-header illustrations did not render, byte-verified by the lane's fetch. For this package the candidate's /2 content (its second code block, candidate L1854–4927) was scanned with a quote-aware `url(` balance check: it contains eleven `url(` declarations (the ten re-hosted artwork declarations plus the kept EN-host one), **all terminated**. A fresh probe of the deployed page (2026-11-17, `https://sigma10-jp-test.wikidot.com/local--code/theme:flopstyle-dark-jp/2`) still shows the unterminated form at its --lgurl line (`url(https://…alt_logo_bw.png;` — no closing parenthesis). The candidate bytes and the deployment therefore disagree, and the defect lives in the deployment state: the draft-host page was not regenerated from the current candidate. The ledger §(c3) line for this theme records only the P1 disposition, so item (i) also lacks a recorded disposition; both halves of that are the coordinator's to close (redeploy from the canonical candidate, then record).
- **Why:** P4/T9 for the re-hosting itself (own-code and own-file delivery from JP hosts; the draft-host form is KB-41, class (iii)). The flag follows the standing evidence rule: where records and bytes disagree, the bytes govern the package and the disagreement is reported, not smoothed over — and here a third source, the live deployment, disagrees with both, which is exactly the state a reviewer must not be allowed to miss.
- **Verify:** The scan is reproducible from this repo alone (any quote-aware `url(` balance check over candidate.txt's second code block); the deployment probe is the URL above, one fetch.
- **Disposition:** DISPOSITIONED (draft-host lines, class (iii)); the /2 deployment mismatch is **flagged, unrecorded** — see section 11.

### 4. Fonts and assets

- **What:** The /1 block carries the font imports (candidate L1834, L1847: Montserrat 800 and Comic Neue from Google Fonts) and the stacks in /2 name the JP fallback throughout: `--header-font: "Montserrat", "Noto Sans JP", sans-serif`, `--body-font: "Inter", "Noto Sans JP", sans-serif`, `--script-font: "Comic Neue", "Noto Sans JP", cursive` — the JPFONT-STACK shape, with the faces' own loading inherited from the Flopstyle base apparatus. Assets are the artwork set of section 3: the logo variants (alt_logo_bw.png, alt_logo_trans.png, alt_logo_tyrian.png in the documentation module), the warning-header illustrations (the .webp set and spc_logo.png, water_ripples.webp), and the border images, all re-hosted to the draft host except the one kept EN-host file (candidate L3515).
- **Why:** P7/T5 with KB-16: the stacks name the JP face as their fallback, which is the font-stack rewrite shape for a theme whose Latin faces are display faces. The kept EN-host artwork is P5 class (ii) (KB-58 family): a third-party file the port does not re-host, recorded as original-state.
- **Verify:** Read candidate L1834–1851 and the /2 variable block (candidate L1935–1950 region); `grep -n 'scp-wiki.wdfiles' candidate.txt` returns the one kept file line.
- **Disposition:** Standing (part of the port); the kept file is DISPOSITIONED (class (ii)).

### 5. Header, sidebar, and site furniture

- **What:** The header defaults are set as CSS `content:` strings in /2 and translated: the title default "SCP財団" and the subtitle default "確保 - 収容 - 保護" (CONTENT-STRING ×14 across the theme's string defaults), while the documentation module's variant variables keep the theme's brand form `--header-title: "FLOPSTYLE: DARK"` with a translated subtitle "転覆的CSS哲学" (candidate L4941–4943 region). HEADERVAR blocks (×3) are the variable-level changes of the same kind. The sidebar toggle is the tail's `:scp-jp:component:toggle-sidebar` include (section 2).
- **Why:** The content-string defaults are reader-visible text, so P10/KB-18 covers their translation; the brand title is the theme's name (a P9-shaped keeping, but no P9 item was recorded for this theme — its T4 items were the /2 defect and the P1 includes). The distinction is recorded so a reviewer does not mistake the translated defaults for an oversight in either direction.
- **Verify:** The strings are at the /2 header region (candidate L2055–2065, blocks B399–B400) and the documentation module (candidate L4935–4943).
- **Disposition:** Standing (part of the port); no header item dispositioned.

### 6. Text translation

- **What:** The documentation body is translated throughout — this theme is mostly documentation, so the translation mass is the port's bulk: 129 TRANSLATION-ANCHORED primaries and 226 TRANS-UNANCHORED primaries (254 label occurrences), plus the CSS comments in the code pages (COMMENT-TEXT ×54: the /2 banner's derivation list is translated, section headers like ヘッダー領域 replace the English, with the courtesy attributions kept) and the content strings (section 5). The specimen texts (ACS color names, warning specimens, the sidebox examples) are translated inside their formatting. English survives reader-visible in the credit fields, the brand title (section 5), and quoted code specimens.
- **Why:** P10 (body, usage, and sample translation is the port's purpose) and KB-18 (reader-visible strings). The unanchored mass was verified by shape against the mirror for this README — on a 5,300-line documentation theme, the anchored/unanchored split is a differ artifact, and the deciding check is the shape census plus the T5 verdict, both recorded.
- **Verify:** The pairs are diff.md's 119 sections in order; a English-prose scan of candidate.txt outside specimens returns the credit and brand lines.
- **Disposition:** Standing (the port itself); T4/T5 judged jointly, FINDINGS on the items of section 11 only.

### 7. Links

- **What:** Three LINK-REPOINT blocks (including B301's secondary, in the documentation's link region at candidate L1483–1498): prose links repointed to their JP counterparts alongside their sentences' translations. The candidate's one attribution link is the credit source link (candidate L22), naming scp-wiki.wikidot.com — the original's recorded host in review/sources.tsv — so the mis-hosted-link defect class does not occur and no probe was needed for links. (The fetch reported in section 3 was a delivery probe, not a link probe.)
- **Why:** P11 under the dead-reference evidence standard: repoint what has a JP counterpart; a link that already names the serving original needs no change.
- **Verify:** `grep -n 'wikidot.com' candidate.txt` — the credit source link, the one kept artwork file (section 4), and specimen text are the hits.
- **Disposition:** Standing; no dead or mis-hosted link found.

### 8. Structure

- **What:** The localize.md closing rule holds. The theme's apparatus — documentation body, three code exhibits in order (candidate L1820, L1854, L4929), the customization module run, the tail delivery module and frame, the gate arrangement — corresponds to the original's, and an exhibit census (the formatting specimens, the sidebox specimens, the code pages, the variant modules) matches in sequence. The classifier's 13 EXHIBIT-RESTRUCTURE primaries all carry INCLUDE-REPOINT secondaries and adjudicate to repoints inside exhibits (sections 2 and 3), so the R3 question does not arise. The two INFO-DEL blocks are the info-standalone specimen conversion of section 2 — a documented form change, with the working JP form present beside it, not a deletion.
- **Why:** R3 exists to force exactly this adjudication, because a restructure and a deletion share a diff shape and ledger class I charges the silent form; here the census, not the label, decides.
- **Verify:** Compare `grep -n '\[\[code\|\[\[module\|\[\[include' original.txt candidate.txt` — the apparatus sequences correspond.
- **Disposition:** Standing; no structural deletion, no class I item.

### 9. Formatting only

- **What:** Sixty-three whitespace-only blocks (WS-ONLY ×63), spread through the code pages and documentation exhibits (blank-line seams where the translated text and re-hosted lines re-flow). The classifier finds no re-indentation pair in the summary census beyond these, and none of the 63 carries a semantic line.
- **Why:** Formatting churn is disclosed as its own class so it is never mistaken for a semantic change, and so a reviewer can skip it safely.
- **Verify:** The blocks are listed in classification.json with their line ranges; spot-reading any of them in diff.md shows blank-line-only pairs.
- **Disposition:** None required.

### 10. Porter annotations

- **What:** One translator note, at the info-standalone specimen (candidate L91): 訳注: scp-jpには `info:start-standalone` / `info:end-standalone` に相当するページが存在しないため、原語版の書式をコード例として示す（このまま include すると404になる）。scp-jpでは `[[include :scp-jp:info:start]]` と `[[include :scp-jp:info:end]]` を使用する。 — it warns the JP reader that the exhibited form would 404 and names the working form. The /2 banner's translated derivation list (candidate L1856–1880 region) keeps the original's attribution structure with the derivation sources named, a carried annotation rather than an added one. No `[!-- --]` notes exist in the candidate.
- **Why:** R2: porter-added text is part of the change record, and this note is load-bearing — it is the difference between a specimen and a trap for the reader who copies it.
- **Verify:** Read candidate L86–93.
- **Disposition:** Standing.

### 11. Dispositions and exceptions

- **What:** Five recorded items and one flagged. Recorded: (1) T1's 67 pseudo-ref errors: class (ii), posting-procedure — the candidate's own draft-host local--code and local--files lines (section 3) at this theme's scale (three code pages plus companion files). (2) T1's 3 hotlink errors: class (ii), the kept EN-host artwork lines (section 4). (3) T1's 4 foreign-include errors: the KB-54 named exception (section 2), NOTFOUND-probed with no JP equivalent. (4) The render row: T2 did not complete (both URLs ×2: webkit target timeout / baseline crash, no summary) — recorded as a measurement limit and coverage caveat, with T3 recording no pointable display defect and the row expressly not BLOCKED-ENV; no candidate defect stands from that segment. (5) T4's P1 item (the EN `:scp-wiki:` includes): DISPOSITIONED as a posting-procedure convention in the §(c3) line — its substance is the same KB-54/specimen complex as item (3). Flagged: (6) the /2 deployment mismatch of section 3 — T4's item (i) has no recorded disposition in the §(c3) line (which records P1 only), the candidate bytes are clean, and the deployment is still broken as probed; it needs a redeploy and a ledger entry, in that order. A record caveat attaches to the T4 row itself: its note is truncated in LOCALIZE-ROWS after item (ii)'s opening, so the row's remaining display-affecting items (5 in total) cannot be reconstructed from the row alone.
- **Why:** A disposition is a decision with grounds (AGENTS.md §3 classes (i)/(ii)/(iii); the named KB entries), not an omission. Item (6) has grounds for neither a fix claim nor a disposition in the records, which is why it is flagged rather than resolved here.
- **Verify:** Items (1)–(3) name their deciding records above (T1-ROWS row 12; the c1 register's foreign-include paragraph, which names flopstyle-dark's four lines explicitly); item (4) is the ledger §(c2) block for this theme (RENDER-B (row 12)); item (5) is the §(c3) line (LOCALIZE-A); item (6) verifies by section 3's scan and probe.
- **Disposition:** DISPOSITIONED (items 1–5); **flagged for coordinator adjudication** (item 6).

### 12. Verification

- **What:** (a) T1 source check (T1-ROWS row 12): exit 1, 74 errors / 13 warns / 2 infos (pseudo-ref ×67, foreign-include ×4, hotlink ×3), all in the dispositioned classes of section 11; there is no class (i) error. (b) T2/T3 render (RENDER-ROWS-1, lane RENDER-B row 12): T2 did not complete (coverage caveat, dispositioned as a measurement limit); T3 no pointable display defect. (c) T4/T5 (LOCALIZE-ROWS row 13): FINDINGS jointly, display-affecting findings 5 (item (i) the /2 deployment defect, item (ii) the P1 includes, the remainder unrecoverable from the truncated row note); the ledger §(c3) line records the P1 disposition. (d) This package is self-verifying: `python3 review/build_review.py --check` regenerates diff.md and the verdict stamp from the two byte-faithful copies in this directory and compares. Counts in this README are the generator's (difflib, autojunk off): +904/−863 in 594 change blocks / 119 diff sections (Tier 2 format). The url( scan of section 3 is this package's own additional check, described there in reproducible terms.
- **Why:** Verification claims name the cheapest deciding check and its result, not a general assurance — including where the checks disagree with each other.
- **Verify:** Re-run the checker on `pages/theme:flopstyle-dark-jp.txt`, `python3 review/build_review.py --check` in this repo, and the section 3 scan and probe.
- **Disposition:** PASS (GOSIGN2-LEDGER (b) row 12; go-sign, COMPLETION-REPORT §10), with the flag of section 11(6) carried forward.

## Per-theme record

### A defect that lives in the deployment, not the file

This package's most useful sentence is the one in section 3, and it is worth restating plainly. The T4 lane fetched the deployed /2 and found it broken; that finding was accurate and remains accurate today — the deployed code page still serves `--lgurl: url(…alt_logo_bw.png;` with no closing parenthesis, and the same presumably holds for the other nine artwork declarations the lane counted. But the canonical candidate — the file this campaign will eventually post — does not contain the defect: its /2 block carries all eleven `url(` declarations terminated. The two states diverged because the draft-host page is a deployment, made at some point from some state of the candidate, and deployments do not track later fixes. Every check in this campaign that fetches the draft host measures the deployment; every check that reads the repo measures the candidate; for this theme the two give opposite answers on the same question, and only a package that compares all three states (record, bytes, deployment) can say so. The repair is operational, not editorial: redeploy theme:flopstyle-dark-jp from the canonical candidate and re-probe /2.

### The usage example's posting name

The usage examples — the documentation's include specimens for this theme, typeset inside their syntax-highlight formatting — as built named this theme by its plain slug on the JP branch, `:scp-jp:theme:flopstyle-dark`, at candidate L136, L360, L367, L572, L583, L594, L605, L616, L627, L638, L654, L666, L677, L688, L699, L713, L724, L740, L751, L762, L773, L784, L795, and L806: the porting wave's repoints changed the branch prefix but left the plain name, so each specimen named a page that does not exist on scp-jp (the campaign's settled rule for usage examples, AGENTS.md §6). The usage-example population sweep has since completed every one of those references on its own line to this candidate's posting name, `:scp-jp:theme:flopstyle-dark-jp` (sweep report SWEEP-USAGE.md in the campaign record, R/review-scout/; canonical commit b5cb724), 24 of its 287 repairs across 157 candidates. This package documents the corrected candidate; its stamp reads STALE against the pre-repair verdict, by design.

## Appendix — residue blocks

For class M the residue set is resolved in one table, not per-block slots. This theme's 52 residue blocks fall into two shapes, both verified by reading the set:

| Shape | Blocks | Resolution |
|---|---|---|
| Syntax-highlighted code specimens | 26 blocks (e.g. B28, B69, B71, B74, B82) | The documentation's code samples are typeset with `##var(--c-…)##` formatting tokens that split the include lines into fragments the classifier cannot tokenize; read directly, they are the same include repoints and specimen translations as sections 2 and 6 (e.g. candidate L136, L360, L367, and the variant specimens at L572–806: `:scp-jp:theme:flopstyle-dark-jp` inside the formatted specimen, as completed by the sweep — section 2) |
| Heading and specimen-label lines | 26 blocks (e.g. B1, B14, B89, B173, B206, B244, B273–B278, B297, B309, B335, B336) | One-line translations the differ left unlabeled: exhibit headings (+* 書式例［基本］, ++++* 設定手順）, the ACS specimen color labels (+++* 赤 / 黄 / 緑 / 青）, and specimen attribution lines (B1's 著者 line, B89's Woedenaz credit line); counted in section 6 |

## Change set outside the two diffed files

The diff covers two files; the port's record is larger. `pages/theme-decoration-sample-flopstyle-dark-jp.txt` is the decoration sample the render lane attempted (its T2 runs are the coverage caveat of section 11(4)). The theme layers over the Flopstyle base apparatus delivered through its own code pages (section 0); its sibling theme:flopstyle-jp is a separate candidate with its own package in this batch. The follow-up diff artifact for the upstream drift since rev 21 (`diff-flopstyle-dark-from21.txt`) sits in the campaign record, outside this repo. The redeploy flagged in section 3 will change the draft-host page, not any file in this repo; when it happens, this package's flag should be closed by the coordinator's note in the batch record.

## License and attribution

- **Title:** Flopstyle: DARK
- **Author:** GreenGolem
- **Source:** https://scp-wiki.wikidot.com/theme:flopstyle-dark — revision 402 (revision date 2026-11-15 21:03:44)
- **License:** Creative Commons Attribution-ShareAlike 3.0 (CC BY-SA 3.0) — license deed: https://creativecommons.org/licenses/by-sa/3.0/
- **Adaptation:** This package holds a Sigma-10 migration port of the work; changes were made. See "Summary" and "Standing sections" in this README for what changed and why. Translator: AI (Muse and its delegated agents), per the campaign's standing attribution rule.
