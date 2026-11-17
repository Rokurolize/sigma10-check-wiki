# Review package — theme:fish-jp

<!-- BEGIN GENERATED VERDICT STAMP — do not hand-edit; regenerate with review/build_review.py -->
## Verdict stamp
- Theme: theme:fish-jp — origin EN, population #89 [GOSIGN2-LEDGER (b) row 89]
- Overall: STALE — candidate file changed since the verdict was computed (verdict against 435a6bb-era content, file sha256 now 91a20c541b8ad97ef2dc73b1db8892174752800704c0be42747c99dceb4b116b); verdict not carried over, re-judgement required
> verdicts below describe the pre-change file
- T1 (source check): FINDINGS (classified) — baseline 2026-11-16: exit 1, 4 errors / 0 warns / 0 infos (pseudo-ref×4); standing classes dispositioned in register c1 [T1-ROWS row 89; GOSIGN2-LEDGER (b) row 89]
- T2/T3 (render, combined verdict): FINDINGS — [combined T2/T3] report `FINDINGS` — §15 series-panel body illegible near-black-on-navy at all 8 shots; `.open-menu` overlap at ≤375, 320px image clip; WebKit CC "S"; assets 404 deferred. [RENDER-ROWS-1 (RENDER-S2-B)]
- Engine coverage: full matrix as run by the lane; coverage not separately caveated in the row [RENDER-ROWS-1 row]
- Credit modal: no credit-modal line in this theme's row; no sample credit-modal error recorded [RENDER-ROWS-1 (RENDER-S2-B)]
- T4 (localize patterns + follow-up): PASS — display-affecting findings: 0 [LOCALIZE-ROWS row 89, source LOCALIZE-S2-B]
- T5 (translation text): PASS — the source reports judge T4/T5 jointly; one verdict word covers both [LOCALIZE-ROWS row 89]
- FIX5 re-judgement: item 18 (class E) DISPOSITIONED — FIX5-CONTRA (no edit, no commit): candidate vs original colour value sets byte-identical (line citations both sides) [GOSIGN2-LEDGER-SUPPLEMENT (a) item 18]
- Computed against: canonical commit b5cb7241f527a44933e45599b41df210690771c4; candidate file pages/theme:fish-jp.txt sha256:91a20c541b8ad97ef2dc73b1db8892174752800704c0be42747c99dceb4b116b; record: GOSIGN2-LEDGER.md + GOSIGN2-LEDGER-SUPPLEMENT.md as of the FIX5 head 435a6bb
<!-- END GENERATED VERDICT STAMP -->


## Status

| | |
|---|---|
| Verdict | **PASS** — go-sign (this theme is one of the 286 of 286 pass-eligible themes) |
| Blocking items at ledger time | GOSIGN2-LEDGER.md §(e) item 18 [E] — §15 series-panel body text near-black on navy, illegible at all 8 shots (KB-28 contrast family) |
| Re-judgment | GOSIGN2-LEDGER-SUPPLEMENT.md item 18: **DISPOSITIONED** (FIX5-CONTRA, no edit), on the colour-identity ground re-derived in the per-theme record below |
| Standing items | **DISPOSITIONED** — T1 pseudo-ref×4 (class (iii) draft-host self-references); render-row items: `.open-menu` overlap and 320px image clip (KB-34/KB-35 mobile chrome family), WebKit CC "S" (KB-36), assets 404 deferred (KB-58) |
| Go-sign basis | COMPLETION-REPORT.md §10 (go-sign issued; 81 FIXED / 26 DISPOSITIONED / 0 OPEN across the sweep) |
| Named exception | None for this theme (the sweep's single named exception is theme:amethyst-v2, which has no candidate) |

## Provenance

| | Original | Candidate |
|---|---|---|
| Page | theme:fish | theme:fish-jp |
| Wiki | scp-wiki.wikidot.com | SCP-JP Sigma-10 candidate (canonical repo) |
| Reference revision | 15, as recorded in the candidate's credit block (初訳時参照リビジョン: 15, candidate L19) and in review/sources.tsv | — |
| Source of this copy | Mirror store `review-mirrors/orig-fish-rev15.txt`, class COPY, fetched once by the LOCALIZE-S2-B lane at rev 15 | Canonical file `pages/theme:fish-jp.txt`, copied at worktree HEAD 71ac75b |
| Lines / bytes | 218 lines / 4,725 bytes | 254 lines / 6,691 bytes |
| SHA-256 | 1f7e84de5a8b916749f1d81112632dbaefd3e80b88caef6a61a383bdb10c58fa | 91a20c541b8ad97ef2dc73b1db8892174752800704c0be42747c99dceb4b116b |

Package files: `original.txt` and `candidate.txt` as tabled above; `classification.json` and the skeleton behind this README are from classify_hunks.py 0.1.0, signature table 2026-11-17.1, patterns commit 9c5e9079afb01d30cb9fc4ef9d714e5591eb2ffa.

## Summary

Fish is a small standalone variant theme (the 2022 April Fool's "SCP Fishing Team" theme) whose whole CSS sits in one code block, delivered by a head module that imports the page's own code/1. The port keeps that topology exactly and changes only the standing classes: the credit furniture becomes the preview credit block plus a license box, the gate tag localizes, the bare Rate exhibit is removed, the font loads move to Google Fonts with a JP supplement (M PLUS Rounded 1c) appended to the two display stacks, and the asset URLs repoint to the draft host's own-attachment paths. The theme's only blocking item was a contrast charge against its series panel, dispositioned because every colour value in the candidate is the original's own, byte for byte — re-derived from this package's two files in the per-theme record. The verdict stamp reads STALE because the usage sweep changed one line after the verdict (commit b5cb724); that line touches no colour surface, and this package re-judges the current bytes.

## 0. Header / provenance

- Delivery: no relocation detected between the sides; each side's components match by kind (head module-css + one code-css block).

- **Provenance route:** derived from the branch original at the reference revision (theme:fish rev 15 on scp-wiki). This is not an R4 production adoption: no production JP counterpart exists in the record for this theme. The evidence is mutually consistent: review/sources.tsv keys the row `standard` with the mirror's SHA-256 equal to this package's original.txt; the candidate's credit block records 初訳時参照リビジョン: 15 (candidate L19); and the sources.tsv note records the first translation at rev 15 with no supersession claim.

## Class summary

| Label | Blocks |
|---|---|
| BARE-RATE-DEL | 1 |
| COMMENT-TEXT | 1 |
| CREDIT-PREVIEW | 1 |
| CREDIT-PROSE | 1 |
| DELIVERY-HOST | 2 |
| DRAFT-HOST | 5 |
| EXHIBIT-RESTRUCTURE | 1 |
| FONT-IMPORT | 1 |
| IFTAGS | 1 |
| INCLUDE-REPOINT | 1 |
| JPFONT-STACK | 2 |
| LICENSE-BOX | 1 |
| SELF-DELIVERY | 2 |
| TASL-FIELDS | 1 |
| TRANS-UNANCHORED | 7 |
| WS-ONLY | 21 |

Counts: 37 blocks, 33 specific, 3 heuristic, 1 residue, 0 skipped (comment text).

## 1. Credit and attribution

- BARE-RATE-DEL (B): Duplicate bare Rate removed (KB-09, ledger class B): the preview credit module is already rate-bearing, so a second bare Rate module double-renders the widget.
  Verify: Grep both sources for [[module Rate]]; the candidate must hold none outside labelled exhibits.
  - B4: orig 10-14 -> cand 10-10 (body -> body)

- CREDIT-PREVIEW (A): Credit block swap (P3/T1): the JP environment's preview credit module is the rate-bearing form; the branch-original credit module does not render here.
  Verify: Re-run the T1 checker (check_source.py); the credit includes must resolve on scp-jp.
  - B5: orig 16-16 -> cand 12-21 (body -> body)

- LICENSE-BOX (A): License box (T4, KB-63/KB-60): the license box must be present in its settled JP form, restored where the port dropped it.
  Verify: KB-63 recipe: license-box includes present in the candidate; form judgment per KB-60.
  - B37: orig at 218 -> cand 232-253 (body -> body)

- **What:** B4 also carries IFTAGS and TRANS-UNANCHORED in its span: the gate tag localizes (`[[iftags +theme]]` → `[[iftags +テーマ]]`, candidate L10) as the original's head furniture (original L10–14: the `[[>]]` div holding `**Rating:**` and `[[module Rate]]`) is removed; the rate function is carried by the preview credit block of B5. The candidate's credit block (candidate L12–21, `credit:start-preview` / `credit:end-preview`) carries all eight TASL fields: タイトル フィッシュ・テーマ (L13), 翻訳責任者 AI (L14), 翻訳年 2026 (L15), 原題 Fish Theme (L16), 著作権者 `[[*user EstrellaYoshte]]` (L17), 作成年 2022 (L18), 初訳時参照リビジョン 15 (L19), 元記事リンク https://scp-wiki.wikidot.com/theme:fish (L20). The original carries no credit block; its attribution is the CSS banner "Created for the SCP Foundation by EstrellaYoshte" (original L32, retained at candidate L46). The candidate's 著作権者 field names the same author the original names — there is no pointer-instead-of-author defect in this package. The credit link's host (scp-wiki.wikidot.com) is the host sources.tsv records for the original. The 翻訳責任者 value is ruling 3's campaign form (AI). B37 is the license box the port adds (the original has none): `component:license-box-backend` with `author=EstrellaYoshte` (candidate L234–235) and three file entries (fishlogo.png, fishbg2.png, tabs.png; candidate L237–250), each stating in its ライセンス field that the original page carries no license statement and advising confirmation with the author before posting; the tabs.png entry records that the file is distributed as theme:plant's attachment in the original.
- **Why:** P3/T1 — the preview credit module is the rate-bearing form in this environment, and TASL attribution (ruling 3) is what makes the port redistributable. The license box's honest "no statement in the original" entries record the licensing posture instead of inventing one.
- **Verify:** Read candidate L12–21 against original L32; `grep -n 'license-box' candidate.txt` returns the two includes at L234 and L252; the T1 checker reports no credit error on this file (section 12).
- **Disposition:** No P3 item is charged against this theme in the ledger register; the T1 baseline records no credit-domain error. Standing.

## 2. Includes and components

The skeleton reports no signature for this section; one include fact stands on the bytes and is recorded here.

- **What:** the candidate's include set is the original's one include plus the credit and license furniture of section 1. The frame include's opening line is repointed `:scp-wiki:` → `:scp-jp:` (original L5 → candidate L5; this is block B2, whose INCLUDE-REPOINT label fires here although the classifier's primary label for the block is EXHIBIT-RESTRUCTURE — adjudicated in section 8). Neither file carries any component include beyond the frame.
- **Why:** P4/P6 — the frame must name the JP environment's component; the include's parameters are treated in section 3.
- **Verify:** `grep -n 'include' candidate.txt` returns the frame (L5), the two credit includes (L12, L21), and the two license-box includes (L234, L252), against the original's single frame include (L5).
- **Disposition:** No ledger item charges this theme's includes. Standing.

## 3. Delivery and code loading

- DELIVERY-HOST (A): Base/host repoint (P4/T9): deliveries are served from the JP hosts in this environment.
  Verify: Resolve the new host path; a kept old-host line is a class (ii) posting matter, recorded in section 11.
  - B1: orig 2-2 -> cand 2-2 (module-css -> module-css)
  - B3: orig 7-7 -> cand 7-7 (body -> body)

- DRAFT-HOST (A): Draft-stage form (KB-41, class (iii)): the candidate's own local--code on the draft host is sanctioned at draft stage.
  Verify: Recorded as a disposition in section 11, not fixed; posting rewrites it (class (ii)).
  - B16: orig 58-58 -> cand 72-72 (code-css -> code-css)
  - B18: orig 63-63 -> cand 77-77 (code-css -> code-css)
  - B36: orig 204-204 -> cand 218-218 (code-css -> code-css)

- **What:** the delivery topology is unchanged (classifier topology: no moves; each side is a head `[[module CSS]]` plus one `[[code type="css"]]` block; code-block census 1 on each side, counting the typed form). B1: the head module's self-import is repointed from the original's own address (original L2, scp-wiki.wdfiles.com/local--code/theme%3Afish/1) to the candidate's own draft-host address (candidate L2, sigma10-jp-test.wdfiles.com/local--code/theme%3Afish-jp/1). B3: the frame's `theme=` parameter is repointed identically (original L7 → candidate L7). The named block /1 is the file's only code block and holds the full stylesheet (candidate L37–231), so the address names the stylesheet itself, not an exhibit. B16/B18/B36 are the three asset URLs inside the CSS, repointed to the candidate's own-attachment paths on the draft host: fishbg2.png (candidate L72), fishlogo.png (candidate L77), tabs.png (candidate L218). The tabs.png case is a re-host, not just a host swap: the original loads theme:plant's attachment (original L204); the candidate loads its own attachment copy, and the license entry (section 1) records the source.
- **Why:** DELIVERY-HOST/SELF-DELIVERY is the self-delivery class: the failure it guards against is a theme page importing another page's (or a dead page's) stylesheet. The draft-host form is class (iii) (KB-41, patterns/ at commit 9c5e9079afb01d30cb9fc4ef9d714e5591eb2ffa): sanctioned at draft stage, rewritten at posting.
- **Verify:** `grep -n 'local--code' candidate.txt` returns L2 and L7, both naming theme%3Afish-jp/1; the code-block census above names the block that address resolves to.
- **Disposition:** The T1 baseline's four errors on this file are exactly these draft-host self-references (pseudo-ref×4, section 12) — class (iii), recorded, not fixed.

## 4. Fonts and assets

- FONT-IMPORT (B): Other font-load change (P5, KB-04): malformed family parameters (a hyphen for a +) make the load fail.
  Verify: KB-04: the family parameter form; the deciding evidence is the load probe (400 vs 200).
  - B10: orig 26-28 -> cand 33-42 (code-css -> body)

- JPFONT-STACK (B): JP family appended to a stack (P7/T5): the Latin faces have no kana glyphs; the appended JP family is the fallback that renders Japanese.
  Verify: Read the paired font-family lines; Latin families unchanged, JP family appended.
  - B12: orig 37-37 -> cand 51-51 (code-css -> code-css)
  - B20: orig 85-85 -> cand 99-99 (code-css -> code-css)

- **What:** (1) The theme's own load: Short Stack moves from fonts.bunny.net (original L27) to the Google Fonts css2 form (candidate L38), same family, no axis parameter on either side (Short Stack ships a single weight; the family parameter form is the KB-04-correct `family=Short+Stack`). (2) The JP supplement, inside the same block: the porter comment `/* 日本語フォント (JP localization) */` (candidate L40, treated in section 10) and the M PLUS Rounded 1c @import (candidate L41). Both loads sit at the head of the delivered code block — the delivered channel itself, not an exhibit. (3) JPFONT-STACK: 'M PLUS Rounded 1c' is appended to exactly the two stacks that name Short Stack (candidate L51 and L99, against original L37 and L85); the Latin faces and the cursive fallback are unchanged. Load/application census: Short Stack is mentioned twice on each side (the two stacks); M PLUS Rounded 1c is loaded once and applied in both stacks. Every loaded family is applied, and every applied family is loaded. (4) Assets are section 3's three URLs; no original-host hotlink remains in the CSS (the license box's 出典 links name the original host as provenance, which is their function).
- **Why:** P7/KB-16 (patterns/ at commit 9c5e9079afb01d30cb9fc4ef9d714e5591eb2ffa): Japanese header text needs a JP face in the stack, and the load must sit in the delivered channel. The failure prevented is header Japanese falling back to OS-default glyphs.
- **Verify:** `grep -n '@import\|font-family' candidate.txt` against the same grep on original.txt; the stacks at candidate L51/L99 name exactly the families loaded at L38/L41.
- **Disposition:** No ledger item charges this theme's fonts; T4 judged the localize patterns PASS with zero display-affecting findings (section 12). Standing on current bytes.

## 5. Header, sidebar, site furniture

none — no signature for this section fired over 37 change blocks, and the ground is measurable: the header, sidebar, and footer rules are carried byte-identical apart from the WS-ONLY blank lines of section 9 and the asset URLs of section 3. The header wordmark string `content: 'Fish Rising'` (candidate L108 = original L94) is kept in English — a header/title identity string, the class ruling 2 puts out of scope for migration correctness. The one charged phenomenon on these surfaces, the illegible series panel, is the theme's blocking item and is treated in section 11 and the per-theme record, not here.

## 6. Text translation

- TRANS-UNANCHORED (C): Translation-shaped change without anchors (P10, KB-18): restructured lines are the queue where restorations and exhibit changes hide.
  Verify: Writer confirmation against the mirror, line by line.
  - B6: orig 18-18 -> cand 23-23 (body -> body)
  - B7: orig 20-20 -> cand 25-25 (body -> body)
  - B9: orig 24-24 -> cand 29-31 (body -> body)

- **What:** TRANS-UNANCHORED also fires inside the spans of B4 (the gate tag, section 1), B5 (the credit prose, section 1), B10 (the font block's comment region, section 4), and B37 (the license entries, section 1); the section is written from the spans. The candidate's reader prose is fully translated: the intro sentence (candidate L23; "SCP Fishing Team" kept as the event's proper name), the usage instruction (candidate L25), and the specimen headings (candidate L29 見出し1, L31 リンク). The specimen section gains a `+ ソースコード` heading and a collapsible wrapper around the code exhibit (candidate L34–36, closed at L232) that the original does not have (its code block stands bare after the `----` rule) — an exhibit-form supplement, recorded in section 8. CSS comments stay in English on both sides (the banner at original L29–33 is byte-identical at candidate L43–47). No mistranslation, term drift, or untranslated reader prose was found in what the candidate carries.
- **Why:** P10/KB-18: reader-visible text localizes; code-adjacent text (comments, the banner) is not reader prose.
- **Verify:** Read candidate L23–36 against original L16–26; the T5 verdict is cited in section 12.
- **Disposition:** T5 judged jointly with T4: PASS (section 12). Standing.

## 7. Links

none — no signature for this section fired over 37 change blocks. Ground: the candidate carries exactly one external link, the credit's 元記事リンク (candidate L20), whose host is the original's recorded host (section 1). The usage reference is the escaped self-include (candidate L27, appendix R1), which names the candidate's own page. The license entries' 出典 links (candidate L240, L245, L250) name the original host as source provenance. No prose link required a probe.

## 8. Structure

- EXHIBIT-RESTRUCTURE (C): Usage/sample exhibits dropped or replaced (R3): a sanctioned replacement and a silent deletion have the same diff shape; the ground must be stated.
  Verify: The exhibit-decision slot for this block, argued from the mirror.
  - B2: orig 5-5 -> cand 5-5 (body -> body)

- **Exhibit decision, B2 (original L5):** neither replaced nor dropped — a false-fire. B2's EXHIBIT-RESTRUCTURE label span is empty; the block is the frame include's opening line, and its only change is the `:scp-wiki:` → `:scp-jp:` prefix repoint recorded in section 2 (the INCLUDE-REPOINT label in the same block). No exhibit stands at this locus on either side.
- **Exhibit decision, the specimen body (B9 region):** kept, restructured in form only. The heading and link specimens are carried with translations (section 6); the code exhibit gains the collapsible wrapper and the `+ ソースコード` heading (candidate L34–36, L232). Nothing in the specimen body is dropped. The one removal in the head furniture, the bare Rate exhibit (original L11–14), is the BARE-RATE-DEL class of section 1 — its function is carried by the rate-bearing preview credit module — not an exhibit drop.
- **CSS body:** no block carries CSS-BODY; the stylesheet is carried entire with only the section 3 and section 4 deltas, which the colour census in the per-theme record verifies at declaration level.

## 9. Formatting only

- WS-ONLY blocks: 21
- Re-indentation: 0 blocks pair up after leading-whitespace normalization

The 21 WS-ONLY blocks are one shape repeated: inside the code block, the original's blank lines carry a single trailing space (e.g. original L28) where the candidate's are empty — the Stage 2 EN9 whitespace normalization (commit 5b6dbe2). Counted here so the churn is not mistaken for content change; the colour censuses in the per-theme record were run over tokens and declarations, which this whitespace cannot affect.

## 10. Porter annotations

The skeleton prints "none" for this section because it lists each block once under its primary label; COMMENT-TEXT fires inside B10's span, and the section is written from it, checked explicitly because annotations ride inside other blocks.

- **What:** the candidate carries exactly one porter annotation: `/* 日本語フォント (JP localization) */` (candidate L40), heading the JP supplement import. The annotation is true: the M PLUS Rounded 1c @import follows it at L41 and both display stacks name the family (section 4). No other added commentary exists — no [JP] markers, no translator's notes; the license entries' caution sentences are TASL furniture (section 1), and the CSS banner is the original's own (section 6).
- **Why:** an annotation that states something the bytes refute is a record defect; this one states exactly what the next line does.
- **Verify:** `grep -n 'localization\|\[JP\]' candidate.txt` returns the single line L40.
- **Disposition:** Standing.

## 11. Dispositions and exceptions

- **Item 18 (class E), the illegible series panel — DISPOSITIONED.** The full argument is the per-theme record below; its one-sentence form is that every colour value in the candidate is byte-identical to the original's, so the near-black text on the navy panel is the original theme's own colour design (a `.content-panel` that sets a navy background and no text colour), not a defect the port introduced. [GOSIGN2-LEDGER-SUPPLEMENT.md item 18; REPORT-GOSIGN2-FIX5-CONTRA.md §3; KB-28 family, patterns/ at commit 9c5e9079afb01d30cb9fc4ef9d714e5591eb2ffa]
- **The `.open-menu` overlap at ≤375 and the 320px image clip — DISPOSITIONED in the ledger, not charged to the theme.** The mobile menu button is the shared site-theme element; its overlap at ≤375px is the mobile chrome family (KB-34/KB-35), not theme-authored content [GOSIGN2-LEDGER.md §(c2), fish row].
- **WebKit CC "S" — DISPOSITIONED.** WebKit CC-badge stray glyph (KB-36) [GOSIGN2-LEDGER.md §(c2), fish row].
- **Assets 404 deferred — DISPOSITIONED.** Deferred asset hosting state (KB-58) [GOSIGN2-LEDGER.md §(c2), fish row]; the candidate-side asset URLs themselves are the section 3 repoints.
- **The T1 pseudo-ref×4 — class (iii), recorded not fixed:** the draft-host self-references of section 3, which resolve at posting.
- **The verdict stamp's STALE** is explained, not a disposition: the candidate changed after the verdict by exactly one line (the usage sweep's posting-name line, commit b5cb724, candidate L27). The re-judgement on the current bytes is this package; the colour ground of item 18 does not touch the changed line.

## 12. Verification

- **T1 (source check):** baseline 2026-11-16: exit 1, 4 errors / 0 warns / 0 infos — pseudo-ref×4 [T1-ROWS row 89]. FIX5-CONTRA ran the checker before and after its adjudication: 4 / 0 / 0 → 4 / 0 / 0 (no edit). The candidate's only later change is the sweep line (candidate L27), itself one of the sanctioned self-reference forms. No class (i) error stands against this candidate.
- **T2/T3 (render):** combined verdict FINDINGS [RENDER-ROWS-1 (RENDER-S2-B, EN9)]. The one candidate-specific item is item 18 (dispositioned, section 11); the lane's remaining lines are the cross-cutting dispositions of section 11. No re-render was run for this package: the render record is the lane's, cited, not re-measured here.
- **T4 (localize patterns + follow-up):** PASS — display-affecting findings: 0 [LOCALIZE-ROWS row 89, source LOCALIZE-S2-B]. The mirror in this package is the reference revision the follow-up state rests on (sources.tsv records the first translation at rev 15, no supersession claim).
- **T5 (translation text):** PASS, judged jointly with T4 by the source report [LOCALIZE-ROWS row 89].
- **This package:** `python3 review/build_review.py --check` — the verdict stamp regenerates identically from the two files in this package, and the package is not in the pre-existing stale set (the refresh-3 population: 79 packages at base 71ac75b, set-compared). The censuses in the per-theme record were re-derived from this package's two files while this README was written, not transcribed from the supplement.

## Per-theme record

### The colour-identity disposition (ledger §(e) item 18)

The charge, as the ledger states it: item 18 [E] (KB-28 contrast) — the §15 series-panel body text is near-black on navy and illegible at all 8 shots, and the ledger records that "no fix wave corrected a KB-28 binding and no original-faithful ground is recorded for these surfaces" [GOSIGN2-LEDGER.md §(e) item 18; §(c2) fish row]. Class E charges a candidate-side defect, so the question the disposition turns on is narrow and decidable from the two files in this package: did the port change any colour on the charged surface — or anywhere in the file? The supplement's ground is that it did not: "candidate vs original colour value sets byte-identical (line citations both sides)" [GOSIGN2-LEDGER-SUPPLEMENT.md (a) item 18; REPORT-GOSIGN2-FIX5-CONTRA.md §3]. Re-measured from this package's files:

1. **The charged surface itself.** The `.content-panel` rule block — original L144–147 = candidate L158–161 — is byte-identical (SHA-256 `2c577cdba561443a08c27f39299c565fb4627401fb6b6265741b56b6d8eee301` on both sides): `border: solid 1px #5173a3; background-color: #00297e;`. The rule sets no text colour, so the panel's body text inherits the wiki default near-black — the original theme's own pairing of values.
2. **Whole-file colour-token census.** Every colour token in each file (hex values and `rgb()`/`rgba()` functions): 48 tokens, 19 distinct values, on each side; the multisets are identical.
3. **Declaration census.** Every colour/background-bearing declaration: 51 on each side. The multisets differ in exactly three entries, the `background-image` URLs of section 3 (fishbg2.png, fishlogo.png, tabs.png), whose values differ only in the host/attachment path and carry no colour value. Every colour-bearing value is identical.
4. **No structural colour accident.** A brace-depth scan of both files (max depth 2, final depth 0, no negative excursion on either side) excludes a displaced brace silently re-scoping the rules after it.

The conclusion the identity licenses: the candidate renders the series panel with the original's own background, border, and inherited text colour, so the illegibility the T3 walk photographed is a property of the original theme's colour design, and "fixing" it would mean departing from the original — an editorial change, not a migration correction. Disposition: **DISPOSITIONED, no edit** [GOSIGN2-LEDGER-SUPPLEMENT.md item 18; FIX5-CONTRA §3].

### Second-reviewer walk

The class asks for the disposition to be walked once more from the third-party perspective: is the ground stated in terms a reader who did none of the work can check, and does it hold? The ground here is one named rule block, two whole-file censuses, and a depth scan, every one reproducible from `original.txt` and `candidate.txt` alone. The walk re-ran each measurement and each held exactly; FIX5-CONTRA's line citations (candidate L158–161, original L144–147) match this package's bytes line for line, and the one place the declaration census differs at all (the three asset URLs) is named above rather than smoothed over — those lines carry no colour, which is the claim the disposition actually makes. One limit is stated for completeness: the census proves the port introduced no colour change; it does not prove the original's panel is readable — the render evidence says it is not, on the original's design, which is precisely what the disposition records. Walk outcome: **the disposition is sound as stated.**

### Multi-wave provenance

The candidate's current state is the product of successive waves, not one pass: the Stage 2 EN9 port (commit 7aed5b7) produced the file the localize lane audited (LOCALIZE-S2-B, row 89, PASS); commit 5b6dbe2 normalized the whitespace-only lines in its code block (section 9); commit 1869877 (FIX-CREDIT-D, translator attribution normalization over 163 files) settled the credit block's campaign form (section 1); FIX5-CONTRA closed the theme's only blocking item as a no-edit disposition, so no FIX5 commit touches this file; and the usage sweep (commit b5cb724) repointed the usage self-include to its posting name (candidate L27) — the one-line delta behind the stamp's STALE. Citations, in place of a changelog: GOSIGN2-LEDGER.md §(b) row 89, §(c2) (render row), §(e) item 18; GOSIGN2-LEDGER-SUPPLEMENT.md item 18; REPORT-GOSIGN2-RENDER-S2-B.md (EN9, fish); REPORT-GOSIGN2-FIX5-CONTRA.md §3; T1-ROWS row 89; LOCALIZE-ROWS row 89. The go-sign over that record is what the Status block certifies.

## Appendix — residue blocks

### Residue R1 — B8 (residue; orig 22-22 -> cand 27-27, body -> body)
- Removed first line: + Heading 1
- Added first line: > @@[[include :scp-jp:theme:fish-jp]]@@

Resolution: assigned to sections 6 and 8, not a residue. B8 is the usage specimen's self-include line (original L20 → candidate L27): the escaped include is repointed from `:scp-wiki:theme:fish` to `:scp-jp:theme:fish-jp`, the posting-name form the usage sweep (commit b5cb724) applied. The classifier gave the block no signature because the line also sits inside the specimen head that B9 restructures; the shape itself is the ESCAPED-INCLUDE / INCLUDE-REPOINT pair, already in the signature table (it fires on the frownstyle settings exhibits in this same batch). No new signature is proposed.

### Residue R2 — B6 (heuristic; orig 18-18 -> cand 23-23, body -> body)
- Removed first line: To use this theme, put the following syntax on any page:
- Added first line: このバリアントテーマは、2022年のエイプリルフール企画「SCP Fishing Team」で使用されたものです。
- Note: script delta without the anchor majority

Resolution: assigned to section 6. B6 is the intro sentence's translation (the opcode pass pairs it against the usage line because the two prose lines trade order around the restructured specimen head); its content is the translation recorded in section 6. The "script delta without the anchor majority" note is the heuristic's own statement that the pairing is positional, not anchored — the writer confirmation section 6 requires was done line by line against the mirror.

### Residue R3 — B7 (heuristic; orig 20-20 -> cand 25-25, body -> body)
- Removed first line: > @@[[include :scp-wiki:theme:fish]]@@
- Added first line: このテーマを使用するには、ページに以下の構文を置いてください:
- Note: script delta without the anchor majority

Resolution: assigned to section 6, with the include line itself resolved as R1. B7 is the usage instruction's translation, paired positionally against the original's include line for the same reason as R2.

### Residue R4 — B9 (heuristic; orig 24-24 -> cand 29-31, body -> body)
- Removed first line: [# Link]
- Added first line: + 見出し1
- Note: script delta without the anchor majority

Resolution: assigned to sections 6 and 8. B9 is the specimen head: the translated heading/link specimens plus the added `+ ソースコード` heading and collapsible opener (candidate L29–36). Its content is recorded in sections 6 and 8; the heuristic note reflects the same positional pairing as R2/R3.
