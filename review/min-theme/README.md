# Review package — theme:min-theme-jp (JP original "Min Theme")

This is a **class S / K3 special package**. Its first part is a production mirror, not a
reference-revision fetch, because the theme is a Japanese original: there is no upstream
page and no reference revision to cite. The standard four-part package degrades honestly
here; the places where it does are named in §0 and in "Format strain" below.

## Verdict summary (hand-written — see "Format strain")

- Theme: theme:min-theme-jp — origin JP, population #20 [GOSIGN2-LEDGER (b) row 20]
- Overall: PASS — passed at the ledger determination; no OPEN items [GOSIGN2-LEDGER (b) row 20]; go-sign issued 2026-11-17 [COMPLETION-REPORT §10]
- T1 (source check): PASS — baseline 2026-11-16: exit 0, 0 errors / 3 warns / 2 infos, error-code multiset `—` [T1-ROWS row 20]
- T2/T3 (render, combined verdict): FINDINGS — `[combined T2/T3]` report `FINDINGS` — sidebar×body overlap (possible stale-cache, not a defect), T2 inconclusive (page baseline crashes, sample exit 2 ×2); no other pointable display defect. [RENDER-ROWS-1 (RENDER-B (row 20))]
- T4 (localize patterns + follow-up): **N/A — JP original, no translation and no reference revision** [LOCALIZE-ROWS row 1; GOSIGN2-LEDGER (b) row 20; (d) item 3]
- T5 (translation text): **N/A — JP original, no source language** [LOCALIZE-ROWS row 1; GOSIGN2-LEDGER (b) row 20]
- Structure confirmation: the substitute check for T4/T5 on JP originals [GOSIGN-TESTS.md line 19]
- Standing exception: GOSIGN2-LEDGER (d) item 3 — the KB-10/KB-07 charges are DISPOSITIONED as false positives (FIX4-JPORIG, accepted in full); the `no-interwiki-style` warning is this exception's form.
- Computed against: canonical `pages/theme:min-theme-jp.txt` sha256 `165e6ad9bc9ffb6b48df28cdea99903e89a89913b6934104d6b8ac27533fee9d`; mirror sha256 `b85f2baffad2af6411e49537c178c787d897740b1e9673dc59ae2176f478a533`; sources.tsv row `min-theme-jp` (kind K3, verdict PASS).

## Status

| | |
|---|---|
| Verdict | **PASS** (one of the 286 pass-eligible themes; the single named exception is theme:amethyst-v2) |
| Blocking items at ledger time | None — the theme is not in ledger section (e) |
| T4/T5 | **N/A by construction** — JP original; structure confirmation instead (GOSIGN-TESTS.md line 19, ledger (d) item 3) |
| Standing items | The standing `no-interwiki-style` warning is the K3 exception's form (ledger (d) item 3); the render row's sidebar×body overlap is marked "possible stale-cache, not a defect" and its T2 runs are inconclusive (RENDER-B row 20). |
| Go-sign basis | COMPLETION-REPORT.md §10 (go-sign issued 2026-11-17) |
| Named exception for this theme | None. The go-sign's one named exception is theme:amethyst-v2 [ledger (d) item 1]. |

## Provenance

| | Original (mirror) | Candidate |
|---|---|---|
| Page | theme:min-theme (production page on real SCP-JP) | theme:min-theme-jp (Sigma-10 environment candidate) |
| Wiki | scp-jp.wikidot.com | SCP-JP Sigma-10 candidate (canonical repo) |
| Reference revision | **NONE — JP original, no reference revision by rule.** The production page has revisions of its own (LOCALIZE-A records 17 since 2018-07-23, none designated a translation source), but a JP production revision number used as a "translation source rev" is a category error. Do not invent one. | — |
| Source of this copy | In-repo mirror `pages-existing/existing:theme-min-theme.txt`, named by the sources.tsv row's `source` column; held in the mirror store's PRODUCTION-MIRROR entry (there is no store file). Byte copy — no fresh fetch. | Canonical file `pages/theme:min-theme-jp.txt`, named by the sources.tsv row's `candidate_path`, copied byte-for-byte. |
| Lines / bytes | 189 lines / 3,460 bytes (the mirror file has no trailing newline on its last line) | 182 lines / 2,735 bytes |
| SHA-256 | `b85f2baffad2af6411e49537c178c787d897740b1e9673dc59ae2176f478a533` — equals the row's `mirror_sha256` | `165e6ad9bc9ffb6b48df28cdea99903e89a89913b6934104d6b8ac27533fee9d` |

Package files: `original.txt` (the production mirror) and `candidate.txt` (the environment
candidate) as tabled above; `diff.md` generated from those two by `review/build_review.py`;
`classification.json` from `review/classify_hunks.py` 0.1.0, signature table 2026-11-17.1.
The README is hand-written for this class-S row — the classifier skeleton was deliberately
not used (see "Format strain").

## Summary

Min Theme (ミニマリストテーマ) is a Japanese original theme by Nanimono Demonai, published on
real SCP-JP as `theme:min-theme` (production mirror L2 names the title; L6 names the author,
L7 the creation year 2018). It is a deliberately spare design: a hidden header, a 780 px
content column, a sidebar and top bar reduced to essentials, and a small set of custom
elements (`.contents`, `.break`, `.thin`). The production page documents those elements and
delivers its CSS from a `[[code type="CSS"]]` exhibit (L46–178), a `[[module CSS]]` @import of
`https://scp-jp.github.io/files/theme/min-theme/style0.css` (L183–185), and an
`interwiki-style` include pointing at the production `local--code/theme%3Amin-theme/4`
(L186–189).

The Sigma-10 environment carries the theme as candidate `theme:min-theme-jp`. The candidate
is a **single self-contained page**: the CSS is inlined into a live `[[module CSS]]` block
(L1–165), the delivery includes are gone, and the documentation is rewritten to say plainly
that this page no longer depends on an external theme page (L174). What the diff shows,
therefore, is not an upstream-to-port translation but the delta between the live JP
production page and its Sigma-10 environment candidate: supplements and environment
adaptation only. The generator's diff confirms this shape — one hunk spanning the whole
file, +123/−128 (251 changed lines), with zero review-stage comment lines.

Nothing in this package should be read as "the theme was translated from a branch original".
There was no branch original. T4 and T5 do not apply; the substitute is the structure
confirmation recorded for JP originals.

## 0. Header / provenance

- **Provenance route: JP original, no reference revision.** This is neither the ordinary
  "derived from the branch original at the reference revision" route nor R4 production
  adoption (the R4 route is for a candidate whose body was inherited from an existing JP
  production counterpart of a *translated* theme). The sources.tsv row records `origin=jp`,
  `ancestor_role=production-page`, `revision=NONE`, `reference=none — JP original (no source
  to follow)`, and `kind=K3`. Ledger (b) row 20 records T4 = N/A and T5 = N/A; ledger (d)
  item 3 names the row and states the no-reference-revision ground; GOSIGN-TESTS.md line 19
  substitutes structure confirmation for T4/T5. Recorded state is "no reference revision
  (JP original, no follow-up target)" — never 「基準不明」.
- **Mirror provenance (cross-kind honesty rule 2):** wiki scp-jp, fullname theme:min-theme,
  revision not applicable (production page, not a reference-revision fetch), source the
  in-repo mirror `pages-existing/existing:theme-min-theme.txt`, class PRODUCTION-MIRROR.
  The mirror's SHA-256 matches the sources.tsv `mirror_sha256` exactly, so this copy is the
  canonical mirror, not a re-fetch and not a reconstruction.
- **Delivery:** the topology pre-pass in classification.json records two delivery moves
  into the candidate's leading `[[module CSS]]` block (candidate L1–165): a content-matched
  `code-css → module-css` move from the production CSS exhibit (original L46–178,
  similarity 0.794) and a candidate-side-only `external-own-delivery → module-css` move
  (the production @import body is not in the mirror). The signature pass then labels 30
  change blocks `DELIVERY-MOVE`. This is an environment-delivery change, not a relocation
  of the theme to another host.

## 1. Credit and attribution

- **Production mirror:** a credit block stands at L4–8 — `[[include :scp-jp:credit:start-preview]]`
  (L4), `**タイトル:**` (L5), `**著者:** ©[[*user Nanimono Demonai]]` (L6), `**作成年:** 2018`
  (L7), `[[include :scp-jp:credit:end-preview]]` (L8). It carries three of the eight ruling-3
  fields (タイトル, 著作権者-form 著者, 作成年) and is the production page's own credit furniture.
- **Candidate:** no `credit:start-preview` include. Instead a quote-wrapped rate module at
  L168–170 (`[[>]]` / `[[module Rate]]` / `[[/>]]`), an expanded title at L172, a prose
  description and usage line at L174–176, a credit line `**クレジット:** © Nanimono Demonai
  （2018）。` at L178, and a TASL source line at L181
  (`//出典: https://scp-jp.wikidot.com/theme:min-theme（CC BY-SA 3.0）//`).
- **What this means:** the candidate's credit surface is a self-contained prose block, not
  the preview credit module. The KB-09/KB-10 charges that this shape attracted were
  **adjudicated false positives** by FIX4-JPORIG (accepted in full): production min-theme
  carries both a credit block and an interwiki include, so the candidate is
  production-faithful in the sense that matters for this exception [ledger (d) item 3;
  ledger §(c4) line 1681]. Do not "fix" L168–170 into a `credit:start-preview` block — that
  would be a unilateral departure from a disposition already accepted by the coordinator.
- **Checker discipline:** runs on JP originals omit `--translation` [AGENTS.md §5]. The T1
  baseline was run accordingly and returned exit 0 with zero errors [T1-ROWS row 20].
- **TASL completeness:** the candidate names title, author, year, source URL and license
  (L172, L178, L181). Translation-specific fields (翻訳責任者, 翻訳年, 原題, 参照リビジョン)
  do not apply to a JP original; their absence is the T4/T5 N/A ground, not a
  `credit-missing-fields` finding. No repo-level TASL record is owed for this row beyond the
  one the campaign already carries for CC BY-SA material.

## 2. Includes and components

- **Production mirror includes:** `credit:start-preview` / `credit:end-preview` (L4/L8),
  `:scp-jp:component:toggle-sidebar` (L181), and `:scp-jp:component:interwiki-style` with
  `|priority=1` and a `theme=` argument pointing at `local--code/theme%3Amin-theme/4`
  (L186–189). All use the `:scp-jp:` posting form, correct for a production page on real
  SCP-JP.
- **Candidate includes:** none. The page is self-contained by design (L174 states the
  intent). No foreign (` :scp-wiki:`) include, no `:scp-jp:` include, no bare component, and
  no `component:sigma-plus` variant stands on the candidate side — verified by reading all
  182 lines.
- **Standing `no-interwiki-style` warning:** classified as *this exception's form*, not a
  defect, by ledger (d) item 3 (the three named-exception files are min-theme, shushuin and
  sigma-10; ledger §(c1) line 322). The FIX4-JPORIG adjudication explicitly covers the
  KB-10/KB-07 charges on this row. No interwiki-style include is to be added.
- **Usage example:** the candidate's usage line names `@@[[include theme:min-theme-jp]]@@`
  (L176) — the `-jp` candidate fullname, matching the campaign's convention that a
  copy-paste install must name the candidate. The production mirror's corresponding example
  names `@@[[include :scp-jp:theme:min-theme]]@@` (L12), the production form. The difference
  is the point of the documentation rewrite, not a P11 finding.

## 3. Delivery and code loading

- **Production delivery chain:** CSS exhibit (original L46–178) + `[[module CSS]]` @import of
  `https://scp-jp.github.io/files/theme/min-theme/style0.css` (L183–185) + interwiki-style
  `theme=` delivery of `local--code/theme%3Amin-theme/4` (L186–189). The `scp-jp.github.io`
  host and the `local--files` asset host are already JP-side hosts on the production page.
- **Candidate delivery:** a single live `[[module CSS]]` block (candidate L1–165) holding the
  same CSS, reformatted and with one rule retargeted (§8). There is no `local--code` reference
  and therefore no draft-host (class (iii)) line to disposition; there is no `@import` to a
  foreign host and therefore no class (ii) posting rewrite on this row.
- **Classifier view:** `DELIVERY-MOVE` is the primary label on 30 blocks, including B1
  (original L1–2 → candidate L1–2), B49 (original L168–173 → candidate L167–170) and B50
  (original L175–178 → candidate L172–181). The label describes the channel change
  (code-css → module-css); the byte-level reasons are given in §§4, 8 and 9.
- **No cross-theme import:** the candidate imports neither a base candidate's delivery nor
  another theme's code page. Ruling 1 (cross-theme delivery) is not engaged by this row.

## 4. Fonts and assets

- **The one asset is unchanged.** The header-logo URL
  `https://scp-jp.wdfiles.com/local--files/theme%3Amin-theme/1.svg` appears at original L95
  and candidate L66 with the identical host, path and `%3A` encoding; the two lines differ
  only in leading indentation (4 spaces vs 2). `classification.json` B16 carries an
  `ASSET-REHOST` label, but the byte comparison settles it: **no re-host occurred**, and the
  label is a channel artifact of the delivery-move block (the detector fired on a
  `scp-jp.wdfiles.com` string inside a block whose other lines moved channels). Nothing is
  owed at posting for this asset.
- **Font stack:** the production `.thin` rule reads
  `font-family: Helvetica Neue, Helvetica, Arial, sans-serif` (original L63); the candidate
  reads `font-family: "Helvetica Neue", "Helvetica", "Arial", sans-serif` (candidate L23).
  The family set and the `sans-serif` fallback are unchanged; only quoting differs. No JP
  face is named, loaded or credited on either side — consistent with T5 = N/A for a JP
  original. Pattern 7 (JP font load) does not apply.
- **No font-load defect:** no `fonts.bunny.net`, no Google Fonts @import and no malformed
  family parameter occurs in either file; KB-04/KB-16/KB-17 have no instance here.

## 5. Header, sidebar, site furniture

- **Preserved surfaces:** the hidden-element rule set (original L67–70 → candidate L27–35),
  the `#header`, `#top-bar`, `.mobile-top-bar`, `#login-status` and `#side-bar` rule groups
  (original L84–161 → candidate L52–158), and the `#top-bar .open-menu a` mobile rules
  (original L133–141 → candidate L117–125) are present on both sides with the same
  declarations (formatting and colour-literal expansions aside).
- **Header/title variables:** none. No `--header-title`, `--header-subtitle` or
  `--logo-image` declaration occurs on either side; ruling 2 (header language) is not
  engaged.
- **Rate widget:** the candidate wraps `[[module Rate]]` in a `[[>]]` quote block
  (L168–170). This is the environment candidate's own rate surface, recorded under §1; it
  is not a second widget beside a preview module (there is no preview module here).

## 6. Text translation

- **N/A — no translation to judge.** T4 = N/A and T5 = N/A in ledger (b) row 20 and
  LOCALIZE-ROWS row 1; the reason on both is "JP original — no translation". There is no
  source language, so APPLIED/MISSED pattern-1..11 judgements and a T5 visible-text check
  have no object. This follows AGENTS.md §3 ("JP-original themes") and GOSIGN-TESTS.md line
  19.
- **Visible text that does change** is environment-candidate documentation, not
  translation: the title gains the qualifiers "（Min Theme）（SCP-JP 移植）" (L172 vs
  original L2); the production usage/custom-element walkthrough (original L10–43) is
  replaced by a two-paragraph self-containment note and usage line (candidate L174–176);
  and the credit/source lines (L178, L181) are added. These are recorded as documentation
  adaptation, with line evidence, and are not charged as mistranslations.
- No CSS `content:` string is translated on either side; the classifier reports zero
  `CONTENT-STRING` and zero `COMMENT-TEXT` blocks.

## 7. Links

- No P11 tag/hub link occurs in either file. The candidate's only URL in prose is the TASL
  source line at L181, which points back to the production page and is required by ruling 3
  (the Source field) — it is not a navigation link to repoint.
- The logo asset URL (§4) and the (removed) production @import URL are code-delivery
  strings, handled in §§3–4, not reader links.
- No dead-reference adjudication is required: with no upstream original, there is no
  branch asset whose current serving state could be compared. The campaign's
  dead-reference evidence standard has no case on this row.

## 8. Structure

- **What the localize.md closing rule would ask** (preserve variables, selectors and channel
  order so a follow-up diff applies cleanly) has no follow-up target here — the row has no
  reference revision. The substitute is the structure confirmation recorded for JP
  originals (GOSIGN-TESTS.md line 19); this package supplies it by direct comparison of the
  two files in §§3–5 and this section.
- **Selector/property inventory:** the candidate preserves every production rule except two
  interwiki rules. Original L168–177 carries
  `#interwiki .side-block { border-color; border-radius; box-shadow }` and
  `#interwiki .heading { color: #707070 }`. The candidate replaces the first with
  `#side-bar .side-block, #side-bar .scpnet-interwiki-wrapper iframe.scpnet-interwiki-frame`
  carrying the same three declarations (L149–154), and does not carry the second. This is
  the candidate's Sigma-10 sidebar/interwiki-frame adaptation; it is stated plainly so the
  diff's removal of the `#interwiki` block is not read as a silent deletion of the theme's
  look. The `#interwiki .heading` colour is the one production declaration with no
  candidate counterpart.
- **Exhibit decision (R3):** classifier B2 (`EXHIBIT-RESTRUCTURE`, original L4–47 →
  candidate L4) and B51 (`EXHIBIT-RESTRUCTURE` + `SELF-DELIVERY`, original L180–189 →
  candidate L183) both fire on the removal of production exhibits. The ground for B2 is
  that the `[[code type="CSS"]]` exhibit's contents were made live as the candidate's
  `[[module CSS]]` block — the CSS is preserved and activated, not dropped. The ground for
  B51 is that the production delivery tail (@import + interwiki-style include) is replaced
  by the self-contained page; it is the environment form, not a missing dependency.
  `classification.json` records both as heuristic/specific labels from the classifier; the
  byte evidence above is the adjudication.
- **No structural restorations from a sibling source** occur. The one `RESTORATION` label
  (B4, original L67–69 → candidate L8–34) is a diff-only alignment artifact: the candidate
  block is the reformatted `*`/`p`/`.contents`/`.break` rules, not content restored from an
  earlier region of the original.

## 9. Formatting only

- The generator's diff reports **1 hunk, +123 / −128** over the whole file (251 changed
  lines) and **0 review-stage comment lines**. `classification.json` reports 51 change
  blocks: 31 specific, 1 heuristic, 19 residue, 0 skipped (comment text).
- **WS-ONLY labels: 12 blocks** (B6, B8, B12, B14, B16, B18, B22, B24, B27, B31, B35, B37),
  all on code-css → module-css lines whose stripped content is unchanged.
- **Formatting deltas visible in the diff:** 4-space → 2-space indentation throughout the
  CSS; blank lines inserted between rules and after comments; multi-selector rules split
  one selector per line (e.g. original L68 → candidate L29–33); hex literals expanded
  (`#b01` → `#bb0011`, `#fff` → `#ffffff`, `#eee` → `#eeeeee`, `#000` → `#000000`,
  `.39` → `0.39`); `padding: 0 1em 1em 1em` → `padding: 0 1em 1em`; font-family names
  quoted (§4). The classifier's `reindent_blocks` measure is 0 because each side's block
  lengths differ, so this is recorded here rather than hidden in that field.
- These formatting changes do not alter any declared value (colour expansions are equal
  colours; the `padding` shorthand change is equivalent). A follow-up diff against a
  reference revision would be inconvenient, but no reference revision exists.

## 10. Porter annotations

- No `[!-- ... --]` translator note, `**訳注:**` footnote or "Edited for SCP-JP" line occurs
  in the candidate. The classifier reports zero `ANNOTATION` blocks.
- The source line at L181 is a TASL Source field, not a porter annotation; it is recorded
  in §1.

## 11. Dispositions and exceptions

- **K3 no-reference-revision exception (ledger (d) item 3).** JP original; T4/T5 N/A;
  structure confirmation substitutes. The mirror is the production page, labelled as such;
  no reference revision number is invented. The `no-interwiki-style` warning is this
  exception's form, not a candidate defect.
- **FIX4-JPORIG false-positive adjudication (ledger §(c4) line 1681; (d) item 3).** The
  KB-10/KB-07 charges against min-theme were DISPOSITIONED as false positives, accepted in
  full: production min-theme carries both a credit block and an interwiki include, so the
  candidate is production-faithful. No edit is owed.
- **T1 baseline (T1-ROWS row 20): exit 0, 0 errors / 3 warns / 2 infos, `—` error codes.**
  There is no class (i)/(ii)/(iii) error to classify on this row. One of the warnings is the
  standing `no-interwiki-style` named-exception warning; the part files record the counts
  but do not enumerate the other warning codes, so they are carried verbatim rather than
  attributed by guesswork.
- **T2/T3 render row (RENDER-ROWS-1, RENDER-B row 20): FINDINGS**, with the only described
  phenomenon a sidebar×body overlap explicitly marked "possible stale-cache, not a defect",
  and T2 inconclusive (page baseline crashes, sample exit 2 ×2). The row ends "no other
  pointable display defect". This is a render-lane record, cited here, not re-measured by
  this documentation package; it is not charged to the candidate.
- **Environment-layer / campaign-wide deferred items:** no draft-host `local--code` line, no
  asset re-host, no draft-bucket asset 404, no hotlink chain and no credit-modal line is
  recorded for this row. None is invented.
- **Not applicable:** foreign-include exceptions (KB-54), candela granular fragments,
  peroxide escaped exhibits, basalt `/7`, sigma-10 environment form, and all section-6 named
  exceptions other than the K3 one have no instance in this package.

## 12. Verification

- **T1 (source check).** Re-run from the skill directory with the JP-original flag set:
  `uv run scripts/check_source.py <candidate> --kind theme --check-links` (no
  `--translation` — AGENTS.md §5). The recorded baseline is exit 0, 0 errors / 3 warns /
  2 infos [T1-ROWS row 20]. This package did not re-run the checker; it cites the ledger row.
- **T2/T3 (render).** Cited from the render lane: `[combined T2/T3] FINDINGS`, RENDER-B row
  20 in RENDER-ROWS-1, with the stale-cache caveat and inconclusive T2 runs quoted in §11.
  No render re-run was made for a documentation package.
- **T4/T5.** Not run by construction — JP original, no reference revision and no source
  language [LOCALIZE-ROWS row 1; ledger (b) row 20; (d) item 3]. The substitute structure
  confirmation is §§3–5 and §8 of this README.
- **Mirrors and generated files.** `original.txt` SHA-256 equals the sources.tsv
  `mirror_sha256`; `candidate.txt` is byte-identical to `pages/theme:min-theme-jp.txt`.
  `python3 review/build_review.py` regenerates `diff.md` identically;
  `python3 review/build_review.py --check` does not list `min-theme` in its stale set (the
  stale set is the pre-existing 90-package baseline, unchanged by this package);
  `python3 review/classify_hunks.py --check review/min-theme` reports
  `OK: review/min-theme classification is fresh`.

## Per-theme record — what a reviewer can and cannot check here

**Can check, from this package alone:** (a) that `original.txt` is the canonical production
mirror and `candidate.txt` the canonical candidate, by the two SHA-256 values in the
Provenance table; (b) the exact production→environment-candidate delta, in `diff.md`
(one hunk, +123/−128) and in the line-cited sections above; (c) that the CSS rules, the
asset URL and the documentation/credit surfaces are present in the candidate and what
changed in them (§§3–5, 8); (d) the recorded T1 result and the re-run command (§12);
(e) the recorded T2/T3 verdict and its caveats (§11).

**Cannot check, and why:** (a) T4 localize patterns — no reference revision and no upstream
original exist, so there is no APPLIED/MISSED judgement to make; (b) T5 visible-text
translation — the page is a JP original, so there is no source language; (c) a T4 follow-up
diff (`wd_revisions.py diff --from N`) — there is no N to pass, and the recorded state is
"no reference revision (JP original, no follow-up target)"; (d) live rendering parity —
the render verdict is cited from the render lane, not re-measured here; (e) posting-time
asset re-hosting or draft-bucket 404s — campaign-wide deferred conditions, not a per-row
matter. Saying any of these is "unverified" would be wrong; they are **not applicable**.

## Format strain — where the standard package had to adapt

1. **Part 1 is a production mirror, not a reference-revision fetch.** The sources.tsv row's
   `revision` cell is `NONE` and its `source` cell names `pages-existing/…`. The provenance
   header says so explicitly; no revision number is manufactured (SPECIAL-ROWS, case K3).
2. **Part 3's meaning changes.** The diff measures production page → environment candidate,
   not upstream original → translation. It is mechanically well-defined (251 changed lines,
   matching the K3 scout measurement) but must never be read as a translation diff.
3. **T4/T5 are N/A, not PASS.** A standard package's verdict stamp would print T4/T5 verdict
   words from the LOCALIZE row; here both cells literally read "N/A (JP original — no
   translation)". The hand-written Verdict summary preserves that distinction.
4. **No generated verdict stamp.** `build_review.py` applies its generated stamp only when
   `theme:<dirname>` is a key of `rec.ledger_b`. The brief names this package `min-theme`, so
   the computed fullname is `theme:min-theme`, which is **not** a ledger key (the ledger key
   is `theme:min-theme-jp`). The generator therefore leaves this README's generated regions
   untouched — which is the desired outcome for a bespoke class-S explanation. The
   Verdict summary above is hand-written and deliberately does not carry the
   `BEGIN GENERATED VERDICT STAMP` markers.
5. **Directory-name discrepancy.** The brief names the package directory `review/min-theme/`;
   the sources.tsv row's `dir` column is `min-theme-jp`. This package follows the brief's
   explicit directory name. Consequently `classify_hunks.py` cannot derive the row by
   directory lookup (its fallback would produce `theme:min-theme`), so `classification.json`
   was produced through the classifier's own `classify()`/`write_outputs()` API with the
   row's real K3 theme metadata (`cand_fullname=theme:min-theme-jp`,
   `orig_fullname=theme:min-theme`, `wiki=scp-jp`, `revision=NONE`, `kind=K3`,
   `verdict=PASS`) injected; the classifier skeleton was not written (`skeleton.status =
   not-written`) because this README is bespoke. Both tools' `--check` gates pass.
6. **Classifier labels are channel-shaped.** 30 `DELIVERY-MOVE` and 12 `WS-ONLY` labels, plus
   the `ASSET-REHOST` false signal on B16, reflect the code-exhibit → module-css channel
   move rather than new port mechanisms; §§3–4 and §9 re-adjudicate them from the bytes.
   This is the K3 analogue of the normal packages' judgment slots.

## License and attribution

- **Title:** Min Theme (ミニマリストテーマ)
- **Author:** Nanimono Demonai
- **Source:** https://scp-jp.wikidot.com/theme:min-theme — no reference revision (JP original by rule; production page)
- **License:** Creative Commons Attribution-ShareAlike 3.0 (CC BY-SA 3.0) — license deed: https://creativecommons.org/licenses/by-sa/3.0/
- **Adaptation:** This package holds a Sigma-10 migration port of the work; changes were made. See "Summary" and "Standing sections" in this README for what changed and why. Translator: not applicable — JP original, no source language; no translator is credited.
