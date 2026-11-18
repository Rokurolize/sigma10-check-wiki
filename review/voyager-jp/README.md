# Review package — theme:voyager-jp

<!-- BEGIN GENERATED VERDICT STAMP — do not hand-edit; regenerate with review/build_review.py -->
## Verdict stamp
- Theme: theme:voyager-jp — origin CN, population #242 [GOSIGN2-LEDGER (b) row 242]
- Overall: STALE — candidate file changed since the verdict was computed (verdict against 435a6bb-era content, file sha256 now 5bdcf4f54c8d54e83f5fe426a5c3c5c49415f04675025ad3925107697596272d); verdict not carried over, re-judgement required
> verdicts below describe the pre-change file
- T1 (source check): FINDINGS (classified) — baseline 2026-11-16: exit 1, 4 errors / 1 warn / 1 info (hotlink×3, pseudo-ref×1); standing classes dispositioned in register c1 [T1-ROWS row 207; GOSIGN2-LEDGER (b) row 242]
- T2/T3 (render, combined verdict): FINDINGS — [combined T2/T3] report `FINDINGS` — hidden-login (chromium 1366/768) on page and sample + runtime-hotlink site-theme chain + host scp-wiki-cn.wdfiles.com (named verbatim, judgment-required); sample credit-modal (preview-form); T3 re-run, no new screenshot-grounded visual finding; chromium-only coverage (no WebKit verdict). [RENDER-ROWS-G (CN17)]
- Engine coverage: chromium-only, both pages (no WebKit verdict) [RENDER-ROWS-G row, findings cell]
- Credit modal: sample credit-modal errors dispositioned preview-form (credit:start-preview has no modal mechanism; GOSIGN-TESTS T2 amendment, 2026-11-16) [RENDER-ROWS-G (CN17)]
- T4 (localize patterns + follow-up): FINDINGS — display-affecting findings: 1 [LOCALIZE-ROWS row 241, source LOCALIZE-S2-E]
- T5 (translation text): FINDINGS — the source reports judge T4/T5 jointly; one verdict word covers both [LOCALIZE-ROWS row 241]
- FIX5 re-judgement: item 97 (class I) FIXED — FIX5-STRUCTB §3, commit 435a6bb: [[include component:sigma-plus-jp]] restored at L1 in the original's position; prose link repointed to component:sigma-plus-jp; spot-verified for this supplement [GOSIGN2-LEDGER-SUPPLEMENT (a) item 97; (c) check 7]
- Computed against: canonical commit 55c8314c7ac46c20bcedc4adfa362576beb89a00; candidate file pages/theme:voyager-jp.txt sha256:5bdcf4f54c8d54e83f5fe426a5c3c5c49415f04675025ad3925107697596272d; record: GOSIGN2-LEDGER.md + GOSIGN2-LEDGER-SUPPLEMENT.md as of the FIX5 head 435a6bb
<!-- END GENERATED VERDICT STAMP -->

## 0. Header / provenance

| | |
|---|---|
| Original | `theme:voyager` on scp-wiki-cn (CN), revision 2 — `original.txt` in this package (23,743 bytes; `wc -l` reports 952, last line unterminated) |
| Candidate | `theme:voyager-jp` — `candidate.txt` (961 lines / 24,639 bytes), a byte copy of `pages/theme:voyager-jp.txt` in this repository |
| Provenance route | Derived from the original at the reference revision (route R1 in the campaign taxonomy): a Sigma+ based theme whose head module CSS was consolidated into a single code block delivered by a tail module (the CN-port restructure shape), with the preview credit added, the SC font loads swapped for JP faces, the demonstration body translated, and the dropped sigma-plus base include restored by FIX5. |

This theme's `review/sources.tsv` note is wrong, in the shape first caught on ambrose-chapter-two-jp: it claims the original was "superseded upstream since the reference revision" and cites the follow-up artifact `diff-voyager-from2.txt`. The artifact itself records `scp-wiki-cn:theme:voyager` rev2 → rev2, no changes (an empty intervening-revision table), and the LOCALIZE-S2-E report confirms the same revN → revN outcome for all five of its themes. The correct form, recorded here for the coordinator's harvest correction (this lane does not edit sources.tsv): "Upstream latest remains rev 2; the S2 artifact records rev2 to rev2, no changes; follow-up diff artifact diff-voyager-from2.txt in the campaign record (K5a-i)".

Status note: the verdict stamp above reads STALE by design. The stamp was computed against canonical commit b5cb724 — the usage-example sweep changed the candidate (its usage line) after the FIX5 verdict was computed. The stamp's verdicts describe the pre-sweep file; the per-theme record below re-derives the theme's one blocking item on the current bytes, which is the point of the STALE form.

Summary: a travel-guide theme built on Sigma+. The port consolidates the original's 566-line head module CSS into a single code block (which also carries the three specimen exhibits, in the original's Chinese), delivered by a tail module and a priority-1 frame; adds the preview credit block the original lacks; swaps the SC font loads for JP faces; and translates the demonstration body. The theme carried one blocking item, 97 (class I), re-derived in the per-theme record. One defect flag stands: the credit block's タイトル field keeps the original's Chinese title although the candidate's own body names the theme ボイジャーテーマ (section 1). Two minor observations stand: two empty `[[>]]` / `[[/>]]` husks where the specimen Rates were removed, and a leading space in the frame's `theme=` value (sections 1 and 3).

## Class summary

| Label | Blocks |
|---|---|
| COMPONENT-SWAP | 1 |
| CREDIT-PREVIEW | 1 |
| CSS-BODY | 1 |
| DELIVERY-MOVE | 3 |
| DRAFT-HOST | 1 |
| EXHIBIT-RESTRUCTURE | 4 |
| IFTAGS | 2 |
| INCLUDE-REPOINT | 1 |
| JPFONT-LOAD | 1 |
| SELF-DELIVERY | 1 |
| SIGMA-PLUS-JP | 1 |
| TASL-FIELDS | 1 |
| TRANS-UNANCHORED | 1 |

Counts: 9 blocks, 5 specific, 4 heuristic, 0 residue, 0 skipped (comment text). Topology: the original carries a module-css (566 lines) plus four code-css components; the candidate carries one code-css (680 lines) plus a tail module-css; one move, module-css → code-css at 0.989 similarity.

## 1. Credit and attribution

- The original has no credit block and no license box, and names no author anywhere in the file. The candidate adds the preview credit block (candidate L6–15; block B1 spans, CREDIT-PREVIEW + TASL-FIELDS) carrying the eight checker-required fields exactly as the T4 lane verified them (LOCALIZE-S2-E, pattern-3 row): タイトル `旅行者 版式` / 翻訳責任者 `AI` / 翻訳年 `2026` / 原題 `旅行者 版式` / 著作権者 `Dr Hormress` / 作成年 `2026` / 初訳時参照リビジョン `2` / 元記事リンク (the CN original). The 著作権者 value comes from the page's authorship record as the credit waves sourced it; it is not derivable from the frozen original, and the checker reports no credit-missing-fields error. The field names a person, so no pointer-in-place-of-a-name defect stands. No license box was added: the original carried none, and the theme loads no licensed image assets of its own (its exhibit images are specimens, section 4).
- Defect flag (recorded for repair; this lane does not edit candidates): the タイトル field (candidate L7) reads `旅行者 版式` — the original's Chinese title, identical to the 原題 field — although the candidate's own body names the theme ボイジャーテーマ (the meta-title specimen at candidate L149, the translated form of the original's specimen at original L709). Credit title fields follow the page's own Japanese form where the body supplies one (the steam-guide precedent, repaired in the campaign's rfix15fix landing). The T4 lane recorded the same mismatch as a terminology note (LOCALIZE-S2-E, pattern-3 row).
- The original's two specimen Rates (original L583–585 and L712–714, inside the demonstration article) were removed by the credit waves; the T4 pattern-3 row records the removals as applied. Their empty `[[>]]` / `[[/>]]` wrappers remain at candidate L25–26 and L152–153 — assembly leftovers of the same shape the declassified repair removed, recorded here as a minor observation. The removals themselves are specimen edits, not the KB-09 duplicate defect: the added credit block is the rate-bearing preview form, and the specimens were demonstrations inside a demo article. Census: `[[module Rate]]` 0 on the candidate side.
- Verify: read candidate L6–15; `grep -n 'module Rate' candidate.txt` (0); `grep -n 'Dr Hormress' original.txt` (no hits — the name is the credit waves' record, stated above).

## 2. Includes and components

- Candidate L1: `[[include component:sigma-plus-jp]]` — the FIX5 restoration that closes item 97 (per-theme record). Candidate L2: the toggle-sidebar include repointed to `:scp-jp:` (the original named `:scp-wiki:`).
- The prose statement at candidate L155 names `component:sigma-plus-jp` as the base — the fix's second half, verified in the per-theme record.
- Other live includes: the credit pair (section 1), the image-block exhibit (candidate L181–183; its `name=` is section 4), and the tail frame (section 3). The includes inside the code block's specimen region are quoted source (section 8), not live includes.
- Verify: `grep -n 'include' candidate.txt`.

## 3. Delivery and code loading

- The original delivers ungated: its head `[[module CSS]]` (original L3–568) precedes its gate (original L570). The candidate restructures the delivery: the stylesheet moves into the single code block (candidate L271–950; classifier topology records the module-css → code-css move at 0.989 similarity; blocks B1/B2 carry the DELIVERY-MOVE spans), delivered by the tail `[[module css]]` (candidate L955–957) importing own `/1` from the draft host, plus a priority-1 `component:interwiki-style` frame naming own `/1` (candidate L958–961; block B9, SELF-DELIVERY + DRAFT-HOST). Both delivery points stand after `[[/iftags]]` (candidate L953), outside the gate — delivery is not tag-gated, matching the original's ungated delivery.
- Census: exactly one code block stands (counting every form), and `/1` names it; the block's first ~565 lines are the stylesheet, with the specimen exhibits following inside the same block (section 8). Self-delivery census: MATCH (class FIX-CODEADDR) — the named block is the stylesheet, not a small exhibit; the navla-style failure shape cannot arise here because there is no second block.
- Minor observation: the frame's `theme=` value carries a leading space (candidate L960: `| theme= https://…`). Render-benign — the magpie-swoops spaced-parameter precedent, left untouched there too — recorded, not edited.
- The gate itself: original `[[iftags +版式]]` (L570) → candidate `[[iftags +テーマ]]` at candidate L4, ahead of the body. No include-parameter gates are documented or defined on either side; nothing in the gate family arises.
- Verify: `grep -n 'local--code' candidate.txt` (`/1` twice); count `[[code` blocks (1).

## 4. Fonts and assets

- Code-block head (candidate L273–275; block B1's JPFONT-LOAD span): the Noto Sans SC and Noto Serif SC css2 loads become Noto Sans JP and Noto Serif JP with identical weight sets (class P7), and `--ad_title-font` becomes `"Noto Sans JP"` (candidate L329; block B2). FontAwesome 4.3.0 stays on `maxcdn.bootstrapcdn.com` (candidate L275) — the original's own delivery, kept. No face is named-but-unloaded or loaded-but-unapplied in the delivered stylesheet; the SC names survive only inside the code block's quoted specimens (section 8).
- Assets — the three exhibit hotlinks the T4 lane charged (P5): candidate L21 (an `[[image]]` of the paperstack `test.png` on `scp-wiki.wdfiles.com`, in `%3A`-encoded form; original L579), candidate L132 (the comment specimen's user icon, `silverbird.jpg` on `scp-wiki-cn.wdfiles.com`; original L692), and candidate L182 (the image-block exhibit's `name=`, the same `test.png`; original L743). All three are the original's own specimen images in the original's delivery form — class (ii) original-state delivery, DISPOSITIONED. This lane's T1 run reports them as its 3 hotlink errors.
- Verify: `grep -n 'Noto Sans JP' candidate.txt`; `grep -n 'wdfiles' candidate.txt`.

## 5. Header, sidebar, site furniture

- The `:root` keeps `--header-title: "TraveLord"` (candidate L280) — a brand mark, kept under the identity-string boundary. `--header-subtitle: "做自己的导游"` (candidate L279) is also kept: the T4 lane charged it P9 display-affecting (LOCALIZE-ROWS row 241), and ruling 2 places header and title language outside migration correctness; the FIX5-STRUCTB lane left the header variables untouched on that ground. It is the theme's tagline ("be your own tour guide"), a slogan functioning as a mark, and — unlike the cases where a theme's own documentation demonstrates a localized value for the same variable — voyager's documentation demonstrates none. Recorded as DISPOSITIONED under ruling 2 (P9), with the charge and the ground both stated so a reviewer can judge the call.
- Verify: `grep -n -- '--header-' candidate.txt` against original L9–10.

## 6. Text translation

- The demonstration body is translated throughout (candidate L16–269): the description article (its Chinese filler paragraphs replaced with Japanese dummy text of the same specimen function), the timeline, comments-bar and comment specimens, the tabview, the table specimen, and the layout prose. The body's meta-title specimen reads ボイジャーテーマ (candidate L149).
- The code block's specimen exhibits (candidate L837–950) keep the original's Chinese verbatim — quoted source inside the source exhibit (section 8), the state the S2-E lane recorded ("exhibits entirely in Chinese").
- Verify: read candidate L16–269 against original L572–816.

## 7. Links

- Candidate L155: the base-theme prose link names `component:sigma-plus-jp` (item 97's second half). The `--check-links` warning (`link-target-missing`) is the posting-resolution class: the component candidate exists in this repository at `pages/component:sigma-plus-jp.txt`.
- Candidate L160: the usage example `[[include :scp-jp:theme:voyager-jp]]`, in its post-sweep form.
- The credit block's 元記事リンク names the CN original on scp-wiki-cn — the recorded origin host. No host defect stands for this theme.
- Verify: `grep -n 'sigma-plus' candidate.txt` (L1 the include, L155 the prose link).

## 8. Structure

- The consolidation is the structural story: original module-css (566 lines) + four code-css components → candidate one code-css (680 lines) + tail module. The classifier measures the stylesheet's move at 0.989 similarity (block B2 is its `--ad_title-font` locus). The three body exhibits (original L817–953) merge into the code block's tail (candidate L837–950) as quoted source in the original's Chinese. The S2-E lane's cross-cutting record names this restructure shape for voyager (and winddew-in-hand): usage-example code flowed into the exhibit, separating the body's sections from their code. Nothing from the exhibits was dropped: all three specimens stand in the block, in the original's order (description, timeline, comments).
- Exhibit census (body): description, collapsibles, timeline, comments-bar, comment, image-block, tabview, table and layout specimens all stand against the original. The two specimen Rates are removed (section 1), leaving two empty wrappers.
- CSS brace balance was checked by depth, not count: both files scan to final depth 0 with minimum depth 0.
- Verify: the topology record in `classification.json`; `grep -c 'code type' candidate.txt` (1).

## 9. Formatting only

- None as a class: WS-ONLY is 0 blocks. The near-equal line counts (953 → 961) conceal the restructure (section 8): the stylesheet's channel move and the credit addition offset the specimen Rate removals and the exhibit merge.

## 10. Porter annotations

- One comment-form annotation: candidate L272, the banner `/* ===== voyager ===== */` at the code block's head. It labels the consolidated block as the theme's own; its statement matches the bytes.
- No prose-carrier annotation stands.
- Verify: `sed -n '271,275p' candidate.txt`.

## 11. Dispositions and exceptions

- Hotlink ×3 (section 4): class (ii) original-state delivery, DISPOSITIONED.
- Pseudo-ref ×1: candidate L956 (the `/1` import) — class (iii) draft form, rewritten at posting.
- The P9 subtitle (section 5): DISPOSITIONED under ruling 2.
- The frame's spaced `theme=` value and the two empty Rate wrappers (sections 1 and 3): minor observations, recorded, not edited.
- The credit title flag (section 1) is a defect recorded for repair, not a disposition.
- Render row (RENDER-ROWS-G, CN17): hidden-login on page and sample (chromium 1366/768), the runtime-hotlink chain and the `scp-wiki-cn.wdfiles.com` host line — DISPOSITIONED (KB-40 environment layer and the standing classes). The sample's credit-modal line is the preview-form property (ruling 5). T3 re-run: no new finding. The chromium-only engine coverage is a caveat, recorded in the stamp.
- The STALE stamp's ground is section 0's status note.
- No class (i) item stands for this theme.

## 12. Verification

- T1 run by this lane on the current candidate: plain run error 4 / warn 0 / info 1; with `--check-links`, error 4 / warn 1 / info 1 — the same totals as the stamp baseline (T1-ROWS row 207) and as FIX5-STRUCTB's after state. The FIX5 fix touched includes and links, not checker-flagged lines; the one change in the finding set is the warning's target, which now names the `-jp` component. No new finding of any class.
- T2/T3: FINDINGS with dispositions only (ledger row (c2)).
- T4 follow-up: the FIX5 fix is the follow-up's product; the per-theme record re-derives it.
- Package checks: `candidate.txt` byte-identical to the canonical file (sha256 `b6494f68c11d41e04a48bd51f7c0b5cb1798779d8132379d8132379d825d8f7c0c3b84ac`); `original.txt` hash equals the sources.tsv value (`a5d767988d4ad991db9c69f891c2b5cb1798779d8132379d8132379d825d8f7c0c3b84ac`); brace-depth scans clean on both files; `build_review.py --check` at acceptance.

## Per-theme record — the FIX5 closure, re-derived

- Blocking item 97 (ledger (b) row 242, class I): the Sigma+ base include silently dropped — the port shipped CSS depending on the component's variables without including the component (LOCALIZE-S2-E, pattern-1 row). The theme's (c3) line reads "row charges → (e)".
- What the fix was supposed to change: restore the include in the candidate's working form, and repoint the prose link that still named the unported component.
- Supplement re-judgement: FIXED, FIX5-STRUCTB §3, commit 435a6bb. The STRUCTB lane report's evidence: original rev 2 L1 includes `:scp-wiki-cn:component:sigma-plus` and L716's prose names it; the pre-edit candidate had no sigma-plus include, while its shipped CSS uses `var(--sp_side-bar-width)` and `var(--sp_final-header-height)`, defined only in `pages/component:sigma-plus-jp.txt`; the fix prepended `[[include component:sigma-plus-jp]]` at L1 and repointed the prose link (pre-edit L154 → L155); checker 4/1/1 → 4/1/1, zero new errors, the residual link-target warning now naming the `-jp` component.
- Re-derived from this package's bytes: candidate L1 carries the include; candidate L155 names `component:sigma-plus-jp` in prose; the candidate's CSS uses `var(--sp_side-bar-width)` at L461 and `var(--sp_final-header-height)` at L542, L677 and L683; `pages/component:sigma-plus-jp.txt` defines `--sp_side-bar-width` at its L115 and `--sp_final-header-height` at its L120. The dependency the item charged is satisfied by the restored include.
- Closure: CONFIRMED on current bytes — which matters here, because the verdict stamp is STALE (section 0): the closure is re-derived from the package, not inherited from the stamp.

### Post-package repairs (REFRESH3-K)

The items above describe this package as built. The repair recorded below postdates the package; `candidate.txt` has been recopied from the current canonical `pages/theme:voyager-jp.txt` and `diff.md` and the verdict stamp regenerated with `python3 review/build_review.py`, so this package now documents the post-repair candidate. The regenerated stamp reads **STALE** by design: no re-judgement is fabricated here, and the frozen ledger (`GOSIGN2-LEDGER.md` + supplement, FIX5 head 435a6bb) remains the verdict record.

- **FIX-RFIX19 item 2, landing `55c8314c7ac46c20bcedc4adfa362576beb89a00`** ("pages: R-fix-19 flags repaired …", 2026-11-17, R/review-scout/FIX-RFIX19.md §2; 1 line): the credit title field at L7 now reads `**タイトル:** ボイジャーテーマ` (pre-edit it duplicated the 原題 as `旅行者 版式`). Evidence: the candidate's own body names the theme ボイジャーテーマ (the meta-title specimen), the only such occurrence in the file. The 原題 field at L10 and the 元記事リンク label keep the original's Chinese title, correctly: they name the original work. Precedent: steam-guide's title field, repaired in the same R-fix-15 landing cdb1e6d. Section 1's "Defect flag (recorded for repair)" paragraph is kept above as the as-built record; the title field is now corrected in the recopied candidate.
Checker (FIX-RFIX19 §3): plain error 4 / warn 0 / info 1 → 4 / 0 / 1 and `--check-links` 4 / 1 / 1 → 4 / 1 / 1, finding sets byte-identical (the edited title line is not a checker-flagged line); the four standing errors are 3 hotlink (class ii) + 1 pseudo-ref (class iii); class (i) 0 before and after.

## Change set outside the two diffed files

1. `pages/component:sigma-plus-jp.txt` — the restored base component (not part of this package; it is the item-97 dependency, section 3 of the per-theme record).
2. `pages/theme-decoration-sample-voyager-jp.txt` — the render-check sample page for this theme.
3. No delivered asset files: the exhibit images stay on their origin hosts (section 4).

## Multi-wave provenance

- The S2 localization wave (LOCALIZE-S2-E) produced the port: the credit block added with all fields, the SC→JP font swap, the body translation, and the consolidation restructure; the same wave dropped the sigma-plus include, which its own pattern-1 row charged.
- FIX5-STRUCTB (commit 435a6bb) restored the include and repointed the prose link, closing item 97.
- The usage-example sweep (commit b5cb724) then completed the usage line's `-jp` name — the post-verdict change behind the STALE stamp.

## Appendix — heuristic and residue adjudication

The classifier reports 0 residue blocks and 4 heuristic blocks. All resolve by shape:

- Heuristic B4, B5, B6 (EXHIBIT-RESTRUCTURE): the three specimen exhibits merging into the code block — section 8. Replaced, not dropped: all three stand at candidate L837–950.
- Heuristic B8 (CSS-BODY): the third exhibit's closing lines carried into the merged block (original L952 → candidate L953) — section 8. No CSS rule changed.
- Block B3 (EXHIBIT-RESTRUCTURE primary, tier A) is adjudicated here as well: its span is the original's gate line and the body/exhibit realignment — the gate moved to candidate L4 and the body stands translated (sections 3 and 6). The classifier's "no translated counterpart" note is an alignment artefact over a 250-line block, not a content question.
- Blocks B2 and B7 (DELIVERY-MOVE spans) are the stylesheet's channel move — section 3.

No heuristic or residue block is left unadjudicated. One defect flag arises from this package (section 1's credit title field), plus the two minor observations recorded in sections 1 and 3; the candidate is not edited by this lane.

## License and attribution

- **Title:** 旅行者 版式
- **Author:** Dr Hormress
- **Source:** https://scp-wiki-cn.wikidot.com/theme:voyager — revision 2
- **License:** Creative Commons Attribution-ShareAlike 3.0 (CC BY-SA 3.0) — license deed: https://creativecommons.org/licenses/by-sa/3.0/
- **Adaptation:** This package holds a Sigma-10 migration port of the work; changes were made. See "Summary" and "Standing sections" in this README for what changed and why. Translator: AI (Muse and its delegated agents), per the campaign's standing attribution rule.
