# Review package — theme:yossistyle-jp

<!-- BEGIN GENERATED VERDICT STAMP — do not hand-edit; regenerate with review/build_review.py -->
## Verdict stamp
- Theme: theme:yossistyle-jp — origin EN, population #44 [GOSIGN2-LEDGER (b) row 44]
- Overall: STALE — candidate file changed since the verdict was computed (verdict against 435a6bb-era content, file sha256 now 01322714dfe5eb256ad875c396495a9f9a9f5831ed77e0be705edb88f01cb628); verdict not carried over, re-judgement required
> verdicts below describe the pre-change file
- T1 (source check): PASS — baseline 2026-11-16: exit 0, 0 errors / 3 warns / 2 infos (no error codes) [T1-ROWS row 44; GOSIGN2-LEDGER (b) row 44]
- T2/T3 (render, combined verdict): FINDINGS — [combined T2/T3] report `FINDINGS` — webkit-375 `sidebar-not-opening` (screenshots show open; infinite `@keyframes` sidebar drift likely culprit), sample 884px@768 static-credit-replica overflow, GOSIGN "raw wikitext leak" unconfirmed, doubled header subtitle at ≤375, no page credit capture; contrast 2.13 joke link. [RENDER-ROWS-1 (RENDER-D2 row 44)]
- Engine coverage: full matrix as run by the lane; coverage not separately caveated in the row [RENDER-ROWS-1 row]
- Credit modal: no credit-modal line in this theme's row; no sample credit-modal error recorded [RENDER-ROWS-1 (RENDER-D2 row 44)]
- T4 (localize patterns + follow-up): FINDINGS — display-affecting findings: 2 [LOCALIZE-ROWS row 44, source LOCALIZE-B]
- T5 (translation text): FINDINGS — the source reports judge T4/T5 jointly; one verdict word covers both [LOCALIZE-ROWS row 44]
- FIX5 re-judgement: items 13 (class B) FIXED, 14 (class H) FIXED — FIX5-FURNA, commit 9e8931f: duplicate bare Rate block removed (class B); five EN links repointed to existing JP pages (checker fetched their JP titles as proof); component:croqstyle and component:rso links left unchanged with grounds (no JP page or candidate exists in census, repo or population) [GOSIGN2-LEDGER-SUPPLEMENT (a) items 13–14]
- Computed against: canonical commit 87c92400a1bc327a00c056d29f538f62762ce4c5; candidate file pages/theme:yossistyle-jp.txt sha256:01322714dfe5eb256ad875c396495a9f9a9f5831ed77e0be705edb88f01cb628; record: GOSIGN2-LEDGER.md + GOSIGN2-LEDGER-SUPPLEMENT.md as of the FIX5 head 435a6bb
<!-- END GENERATED VERDICT STAMP -->

## 0. Header / provenance

| | |
|---|---|
| Candidate | `theme:yossistyle-jp` — `pages/theme:yossistyle-jp.txt`, 213 lines, 10,560 bytes (sha256 in the stamp) |
| Original | `theme:yossistyle` on scp-wiki (EN), reference revision 9 — `original.txt`, 184 lines, 7,761 bytes, sha256 matches `review/sources.tsv` |
| Class | R-fix — two blocking items (ledger items 13, 14), FIXED in FIX5 |
| Reference-revision record | `start-themes.tsv`: "Complete (reference rev recorded)", delivery "Post the port candidate as a new page", dependency BHL, first-translation rev 9 |

Provenance route: derived from the original at the reference revision (standard kind; no production JP counterpart — the delivery is a new page).

A deliberately unserious personal style theme — the author's own page-style, written in the first person. The port translates the prose, adds the Black Highlighter frame stack and the preview credit block, removes the duplicate bare Rate module (item 13), repoints five prose links to JP production pages (item 14), and extends two CSS selectors for the JP environment in both stylesheet copies. One open defect is flagged in §8: the footnoteblock stands escaped while a live footnote stands in the body. Items 13–14 are re-derived in the per-theme record; the verdict stamp is current (it computes against the FIX5 commit and the candidate's sha is unchanged since).

## Class summary

| Label | Blocks |
|---|---|
| BARE-RATE-DEL | 1 |
| COMMENT-TEXT | 4 |
| CREDIT-PREVIEW | 1 |
| DELIVERY-MOVE | 4 |
| DRAFT-HOST | 1 |
| IFTAGS | 1 |
| SELF-DELIVERY | 1 |
| TASL-FIELDS | 1 |
| TRANS-UNANCHORED | 23 |
| TRANSLATION-ANCHORED | 7 |

Counts: 35 blocks, 13 specific, 20 heuristic, 2 residue, 0 skipped (comment text).


Component topology (classifier): a module-css ↔ code-css "swap" is reported at 0.862 similarity — an artefact, adjudicated in §3 and the appendix: both CSS channels exist on both sides with unchanged roles. The candidate adds the frame components and the credit block.

## 1. Credit and attribution

What: the original carries no credit block and no license box. The candidate adds the preview credit block at the tail, inside its own +テーマ gate (cand L197–208; B35): 著作権者 names Yossipossi. The theme is the author's own first-person page — the body is Yossipossi's voice throughout and the page is named for the author — so the field names the author, sourced from the page's authorship record by the credit waves; no pointer stands in place of a name. No license box is added: the original carries none and the theme loads no third-party assets. The bare Rate block is item 13 (per-theme record): the original's block at orig L42–44 is deleted (B3, BARE-RATE-DEL), and the preview credit block is the only rate carrier in the candidate.
Why: the preview credit is the JP environment's rate-bearing credit form (P3); a bare Rate beside it renders two widgets (patterns/ KB-09, commit 9c5e907).
Verify: `grep -n "module Rate" candidate.txt` returns nothing; read cand L197–208.
Disposition: ledger (c3) row 44 records P3 FIXED by the credit waves.

## 2. Includes and components

What: the candidate's live includes are the two Black Highlighter frames (cand L42–50: priority 1, the BHL normalize CSS; priority 2, the black-highlighter min CSS — both on scp-jp.github.io, patterns/ KB-17's named host), the credit pair (cand L198, L207), and the priority-3 own-code frame (cand L210–213; §3). The original has no live includes at all: its only include-shaped text is the @import specimen (§7), and the word "include" otherwise appears as ordinary prose (orig L54, L62, L78), translated as prose. Item 14's prose links are §7.
Why: the frame stack is the BHL delivery the /start row records as this theme's dependency; the frames are the frame waves' P6 fix.
Verify: `grep -n "include" candidate.txt` against the same grep on `original.txt`.
Disposition: ledger (c3) row 44 records P6 FIXED by the frame waves.

## 3. Delivery and code loading

What: the original delivers its CSS inline through the head [[module CSS]] (orig L1–40) and exhibits the same CSS in one `[[code type="css"]]` block (orig L143–180). The candidate keeps both channels in the same roles — head module at cand L1–40, exhibit at cand L149–186 — and adds the priority-3 frame naming its own /1 on the draft host (cand L212, SELF-DELIVERY, class (iii)). Census: exactly one code block in the candidate; the /1 address names it, and the named block is the stylesheet exhibit — the FIX-CODEADDR audit form: MATCH. The classifier's topology pass reports the two copies as swapped (0.862 similarity): the copies are near-identical on both sides, so the matcher crossed them; no channel changed role, and nothing was moved (appendix, B1/B2/B32/B33).
Why: the exhibit copy is the page's documentation of its own CSS; the frame gives the code address a delivery route in the JP environment.
Verify: count every code-block form (`grep -c "\[\[code" candidate.txt` = 1); read cand L1–8 and L210–213; diff the candidate's two CSS copies against each other — they differ only in the §5 edits' shared form.
Disposition: the T1 baseline for this theme is PASS with 0 errors (§11); no delivery finding stands.

## 4. Fonts and assets

What: none. Neither side loads a font or declares a font-family; the theme's only external reference is the YouTube link in the prose (cand L97, kept from the original). Stated with ground: `grep -n "font-family" original.txt candidate.txt` returns nothing, and the only @import-shaped text on either side is the §7 specimen inside the prose.
Verify: the greps above.
Disposition: none — no font or asset finding is recorded against this theme.

## 5. Header, sidebar, site furniture

What: two CSS edits, each standing in BOTH copies (head module and code exhibit). (i) The sidebar hover rule's selector is extended — `#side-bar` becomes `#side-bar, iframe.scpnet-interwiki-frame` (cand L17 and L164) — so the theme's sidebar animation also moves the JP environment's interwiki frame (the population's JP-DOM selector-extension shape, taxonomy residue class R6). (ii) The tag attribute selector is localized — `tag/theme#pages` becomes `tag/テーマ#pages` (cand L23 and L170) — the tag the rule bolds is テーマ on JP. The T1 checker's two interwiki-touched warnings (cand L17, L164) attach to edit (i): the change adds the frame to the theme's own animation rule; it neither hides the interwiki module nor rewrites its contents (the warning's own tests), and the render row records no interwiki breakage. The `#license-area` `content: "."` rule stands unchanged.
Why: a port whose CSS lives in two copies must edit both, or the exhibit would document a stylesheet the page does not run; the extensions adapt the rules to the JP DOM.
Verify: `grep -n "scpnet-interwiki\|tag/" original.txt candidate.txt` — each edit appears exactly twice in the candidate, zero times in the original.
Disposition: the warnings are recorded in the T1 baseline row (T1-ROWS row 44); no defect.

## 6. Text translation

What: the prose body is translated throughout (cand L52–146 against orig L50–141), register preserved — the jokes stay jokes. Headings are translated, the code collapsible's labels are translated (orig L141: "+ SHOW CODE (warning, very long and complicated)" / "– OC CODE DO NOT STEAL" → cand L147: "+ コードを表示（警告、とても長く複雑）" / "– OCコード パクらないで"), and the footnote text is translated (cand L84). Observation: the seven review attributions keep their names as plain text (cand L111–135) where the original links them as [[*user …]] (orig L105–129) — names preserved, the user-link form dropped in translation; minor, recorded here (the same shape stands in y2k's intro).
Why: translation is the port's purpose; the attribution names carry the credit even without the link form.
Verify: read cand L52–146 against orig L50–141.
Disposition: ledger (c3) row 44 carries no translation finding; the observation above is new and minor.

## 7. Links

What: item 14's repoints (per-theme record): five prose links now name scp-jp.wikidot.com production pages — theme:magnus-web-format, theme:flopstyle, theme:blankstyle, theme:placestyle (cand L56) and theme:black-highlighter-theme (cand L62); component:croqstyle and component:rso stand on scp-wiki.wikidot.com (cand L56) with the supplement's grounds (no JP page and no candidate exists for either). The credit block's 元記事リンク (cand L206) names the EN original on scp-wiki.wikidot.com — the recorded origin host in `review/sources.tsv`; no candidate link names a different host for the original page, so no host probe was required. The @import specimen at cand L73 keeps the original's `http://scpwiki.com/theme:yossistyle/code/1` text verbatim — it is the page's "do NOT do this" exhibit, quoted text, not a delivery line; it is not repointed and is not a finding.
Why: prose links must name pages that exist for the JP reader; where the JP page exists in production, the link names the production page (the monotypical form).
Verify: `grep -n "wikidot.com" candidate.txt` — the scp-jp forms at L56/L62, the scp-wiki forms at L56 (croqstyle, rso) and L206.
Disposition: item 14 CONFIRMED closed (per-theme record).

## 8. Structure

What: **Defect flag (open)** — the footnoteblock. The original carries a live [[footnote]] in the body (orig L78) and a live [[footnoteblock]] inside the code collapsible (orig L182). The candidate carries the footnote live (cand L84) but the block escaped: cand L188 reads `@@[[footnoteblock]]@@`, so the footnote has no render position. This is the penumbra / scp-offices-theme shape; both earlier instances in this campaign were adjudicated defects and repaired by unescaping (canonical 6660ec5 and c1ba76a). The classifier assigns the block no signature (residue B34), which is how it passed the waves. Flagged for repair; the package is written against the candidate as it stands.
Gate topology: neither side wraps the page in [[iftags]]; the candidate's credit block carries its own +テーマ gate at the tail (cand L197–208), and the SCP-JP correction module (cand L192–195: narrow file-table widths, commented in English) and the frames stand ungated — the original's ungated form preserved. Exhibit census: the heading specimens, the {{}} specimens, the change list, the review quotes, and the code collapsible all stand; nothing the original carries is dropped.
Why: a live footnote without a footnoteblock renders nowhere; the escape is a defect of the same family as the two repaired instances, not a disposition.
Verify: `grep -n "footnote" original.txt candidate.txt` — the original shows both forms live; the candidate shows the footnote live and the block only in @@-escaped form.
Disposition: none — this is a defect recorded for repair, not a disposition.

## 9. Formatting only

What: none as a class — the classifier records no WS-ONLY and no reindent block for this pair. The two CSS copies are verbatim against the original's except the two §5 edits.
Verify: classification.json label counts (WS-ONLY absent); §3's copy diff.

## 10. Porter annotations

What: one annotation — the tail correction module's English comment (cand L193: "SCP-JP Wikidot yossistyle narrow files: keep wide file tables inside the content column on phones."). It is a production-layer annotation (R2) and its statement matches the bytes (the module sets file-table widths at cand L192–195). No annotation stands inside the translated body.
Disposition: annotations of this form are the population's R2 shape.

## 11. Dispositions and exceptions

What: the T1 baseline is PASS (T1-ROWS row 44: 0 errors / 3 warns / 2 infos at the 2026-11-16 snapshot; this lane's plain run gives 0 errors / 2 warns / 1 info — no errors either way; the two interwiki-touched warnings are §5's extension). The render row (RENDER-ROWS-1, RENDER-D2 row 44) gives FINDINGS, all DISPOSITIONED: the webkit-375 sidebar-not-opening line (the row's own screenshots show the sidebar open; patterns/ KB-47 family), the sample's 884px-at-768 static-credit overflow (KB-33 replica family), the doubled header subtitle at ≤375px (replica divergence), and the contrast 2.13 reading on the joke link (KB-39 machine false positive). Ledger (c3) records P3 FIXED and P6 FIXED. The §8 footnoteblock flag is a defect recorded for repair, not a disposition.
Verify: T1-ROWS row 44; RENDER-D2 row 44.

## 12. Verification

- T1 checker (`check_source.py --kind theme --translation`), run by this lane on the current candidate: error 0 / warn 2 / info 1 (§11).
- Brace-depth scan (strip strings and comments, track `{}` depth): both files final depth 0, min 0 — the CSS is balanced on both sides.
- Censuses: code blocks 1; [[module Rate]] 0 in the candidate; footnoteblock live 0 / escaped 1 in the candidate (§8).
- Package checks: candidate.txt is byte-identical to the canonical file; original.txt's sha256 equals the sources.tsv value; `python3 review/build_review.py --check` at acceptance (batch report).

## Per-theme record — the FIX5 closures, re-derived

Item 13 [B] (ledger (e) row; supplement, FIX5-FURNA).
Charged: a duplicate bare [[module Rate]] at (then) L53 standing next to the preview credit module — two rate widgets render.
Fix as recorded: canonical commit 9e8931f (FIX5-FURNA) removed the bare Rate block; `git show 9e8931f` changes this file by 2 insertions / 6 deletions.
Re-derived: the original's block stands at orig L42–44 ([[>]] + [[module Rate]] + [[/>]]); the candidate contains no [[module Rate]] anywhere, and the region now holds the two BHL frames (cand L42–50).
Closure: CONFIRMED.

Item 14 [H] (ledger (e) row; supplement, FIX5-FURNA).
Charged: prose links at (then) L60/L66 naming EN pages where JP pages exist — theme:magnus-web-format, theme:flopstyle, theme:blankstyle, theme:placestyle, component:croqstyle, component:rso, theme:black-highlighter-theme.
Fix as recorded: five links repointed to the scp-jp production pages (the FIX5 lane fetched the JP pages' titles as existence proof); croqstyle and rso left on scp-wiki, on the ground that no JP page and no candidate exists for either.
Re-derived: cand L56 names scp-jp.wikidot.com for magnus-web-format, flopstyle, blankstyle, and placestyle; cand L62 names it for black-highlighter-theme; cand L56 keeps scp-wiki.wikidot.com for component:croqstyle and component:rso. Exactly the supplement's account — five repointed, two left with grounds. The repointed links name the production pages under plain slugs, the monotypical form for a link whose target exists in production.
Closure: CONFIRMED.

### Post-package repairs (REFRESH3-K)

The items above describe this package as built. The repair recorded below postdates the package; `candidate.txt` has been recopied from the current canonical `pages/theme:yossistyle-jp.txt` and `diff.md` and the verdict stamp regenerated with `python3 review/build_review.py`, so this package now documents the post-repair candidate. The regenerated stamp reads **STALE** by design: no re-judgement is fabricated here, and the frozen ledger (`GOSIGN2-LEDGER.md` + supplement, FIX5 head 435a6bb) remains the verdict record.

- **FIX-RFIX21 item 1, landing `87c92400a1bc327a00c056d29f538f62762ce4c5`** ("pages: R-fix-21 flags repaired (yossistyle, y2k)", 2026-11-17, R/review-scout/FIX-RFIX21.md §1; 1 line): candidate L188 `@@[[footnoteblock]]@@` → `[[footnoteblock]]`, unescaped, at the same position (after `[[/code]]`, before `[[/collapsible]]`, matching the original's placement). Evidence: the original carries the `[[footnote]]` live at orig L78 and `[[footnoteblock]]` live at orig L182; the candidate's footnote was live at L84 but its render position was escaped, the only footnoteblock occurrence in the file. Same shape as the penumbra and scp-offices-theme escapes, both adjudicated defects and repaired by unescaping (canonical 6660ec5, c1ba76a). Section 8's "Defect flag for repair" and §11's reference to it are kept as the as-built record; the flag is now repaired in the recopied candidate. Checker (FIX-RFIX21 §3): plain error 0 / warn 2 / info 1 → 0 / 2 / 1 and `--check-links` 0 / 7 / 1 → 0 / 7 / 1, finding sets byte-identical in both runs; class (i) 0 before and after. The multi-wave provenance's "the stamp is current, not stale" is the as-built record; the stamp now reads STALE against this repair.

## Change set outside the two diffed files

- `pages/theme-decoration-sample-yossistyle-jp.txt` — the display-check sample (the render row's page, §11).
- The `start-themes.tsv` row quoted in §0 (the delivery record).

## Multi-wave provenance

- The port was built by the S2 localization wave (LOCALIZE-B lane row); the credit waves (P3) and frame waves (P6) supplied the credit block and the frame stack.
- FIX5-FURNA commit 9e8931f closed items 13–14. The verdict stamp computes against that commit and the candidate's sha is unchanged since, so the stamp is current, not stale.

## Appendix — heuristic and residue adjudication

- B1, B2 (heuristic, DELIVERY-MOVE; module copy) and B32, B33 (heuristic, DELIVERY-MOVE; exhibit copy): the two §5 selector edits — not moves. Both CSS channels exist on both sides with unchanged roles (§3); the topology "swap" is the matcher crossing the near-identical copies.
- B3 (specific, BARE-RATE-DEL): item 13 — §1 and the per-theme record.
- B35 (specific, CREDIT-PREVIEW with DRAFT-HOST, IFTAGS, SELF-DELIVERY, TASL-FIELDS spans): the tail region — the correction module, the gated credit block, and the priority-3 frame (§1, §2, §3, §8).
- B25 (residue; orig L111–113 → cand L117–119): the emoji review line (🦆🍞❤️✡️🙏) and its rule lines — glyph text carried untranslated by design inside a translated block; no signature fires on it.
- B34 (residue; orig L181–182 → cand L187–188): the footnoteblock escape — §8's defect flag. The classifier gives the block no signature, which is how it passed the waves.
- The TRANS-UNANCHORED mass (23 blocks) and TRANSLATION-ANCHORED blocks (7) are the prose translation — §6, by shape; the COMMENT-TEXT spans (B12, B30, B31, B33) ride inside the {{}} specimen and quote blocks and are adjudicated with them.

## License and attribution

- **Title:** YOSSISTYLE CSS THEME
- **Author:** Yossipossi
- **Source:** https://scp-wiki.wikidot.com/theme:yossistyle — revision 9 (revision date 2021-09-11 01:27:54)
- **License:** Creative Commons Attribution-ShareAlike 3.0 (CC BY-SA 3.0) — license deed: https://creativecommons.org/licenses/by-sa/3.0/
- **Adaptation:** This package holds a Sigma-10 migration port of the work; changes were made. See "Summary" and "Standing sections" in this README for what changed and why. Translator: AI (Muse and its delegated agents), per the campaign's standing attribution rule.
