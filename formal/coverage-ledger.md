# LINT-WAVE — the theme-porting knowledge base as executable lint

- **Date:** 2026-11-18
- **Brief:** `theme-lint/lane-oc-lint/BRIEF.md`, executed in full.
- **Worktree:** `.../theme-lint/lane-oc-lint/work`, checkout `c26c4c8`. Nothing committed or pushed; the coordinator harvests. No edits to `patterns/`, any package, or `pages/`. `git status` shows exactly one new file: `review/lint_patterns.py`.
- **Deliverable 1:** `review/lint_patterns.py` — new, stdlib-only Python, in the style of `classify_hunks.py` / `build_review.py`.
- **Knowledge base:** `patterns/KB-01.md` … `KB-81.md` plus `NEGATIVE-LEDGER.md` (NL-01 … NL-15). Source of every rule is the pattern's own **Static detection** section, not an invented rule.
- **Corpus:** 305 packages under `review/` holding both `original.*` and `candidate.*` (the 287 theme rows plus component/fragment/sample/base-CSS packages); 285 carry `classification.json`.
- **Supporting artifacts** (outside the canonical worktree, so nothing to commit): `lane-oc-lint/validate_controls.py`, `corpus-run.tsv`, `corpus-run.json`, `control-validation.txt`, `per-rule-packages.txt`.

## 1. Design in brief

`lint_patterns.py` registers 19 rules. Each registration records the KB id, rule name, **scope**, a one-line quotation of the source section, and the suppressions applied. `--list` prints all of this, including the NEGATIVE-LEDGER suppression registry.

- **Scope `candidate:`** — a pure grep or file-local structural check over `candidate.txt`.
- **Scope `pair`** — needs `original.txt` + `candidate.txt` (a cross-file diff or a count compared side by side).
- **Disposition rules** (still `candidate:`) emit INFO/EXCEPTION records rather than defect findings: KB-32, KB-50, KB-55, KB-56, KB-59, KB-80.
- **Two-channel parsing** (`css_channels()`) reads both `[[module CSS]]` and `[[code …]]` CSS; this is the mechanical form of NL-01/NL-02's two-channel ruling. Structural rules operate on the delivered CSS block (named by a self-addressed `local--code/<own>/N`), not on documentation exhibits — that distinction removed the starbasalt-style brace artefacts the campaign records as by-design.
- **Escape/comment scrubbing** (`_scrub()`) masks `@@…@@` examples, Wikidot `{{…}}` inline-code examples that contain wikitext, and CSS `/*…*/` comments before any grep. It also skips the wiki-formatting `/*` tokens in `**word**/**word**` and `__**//--{{x}}--//**__` (madoka L256 / sci-fi L82 models). This is where NL-07 (model case) and NL-15 become executable suppressions.
- **NEGATIVE-LEDGER suppressions are named** in `SUPPRESSIONS` and attached to the rules that use them: `NL-07:xmlns-identifier`, `NL-15:css-source-comment`, `NL-01/02:two-channel`, `NL-11:font-host-repoint`, `KB-07:mutually-exclusive-gate`, `KB-07:original-identical-stack`, `KB-42:inherited-http`, `KB-55:candela-granular`, `KB-56:peroxide-escaped`, `KB-70:inherited-self-import`, `KB-20:own-css-size`, `KB-73:param-gated-channel`.
- **Reporting contract:** per finding the tool prints `package · KB id · rule · scope · location (file:line or range) · evidence line · note`. `--corpus` runs all packages, `--rule KB-xx` filters, `--json` emits JSON, `--strict` exits 1 on findings; a completed reporting run exits 0. A detector exception is emitted as an `ERROR` finding, never silently dropped (there were zero such findings in the final run).

Two honest scope notes:

1. `classify_hunks.py` detectors are **diff-direction** — they label the hunk where a fix happened (e.g. `COLON-ENC` labels the line where a colon was encoded). The new lint rules are **current-bytes-direction** — they flag residual defects in the candidate as it stands. Both are mechanical checks of the same knowledge; the coverage ledger credits the existing tool with ALREADY-AUTOMATED where its signature detector already covers the mechanism (the SIG_META "Why" line cites the KB id), and implements the residual-defect check in the linter only where no such detector exists.
2. Rules that need a live probe, render summary, or external record are NOT-LINTABLE **over this corpus**: the package holds original/candidate text and the classification, not render output or wiki state. Their dispositions argue against their own Static detection text, as the brief requires.

Reproduce:

```
cd .../lane-oc-lint/work
python3 review/lint_patterns.py --list
python3 review/lint_patterns.py --corpus                 # 305 packages, 887 findings
python3 review/lint_patterns.py --corpus --json          # corpus-run.json
python3 review/lint_patterns.py review/y2k-jp --rule KB-21
python3 ../validate_controls.py                          # 31 controls, all PASS
```

## 2. Coverage ledger — 81 patterns

Exactly one disposition per pattern. ALREADY-AUTOMATED names the existing detector/label; LINTED names the rule above; NOT-LINTABLE states what judgment or external state the pattern's own Static detection actually needs; LINTABLE-DEFERRED sketches the design.

| ID | Disposition | Rule / where | Ground (specific) |
|---|---|---|---|
| KB-01 | ALREADY-AUTOMATED | `COLON-ENC` / `det_colon_enc` (SIG_META §4) | Checker encodes only the path-segment colon; the signature detector already tests the mechanism. |
| KB-02 | NOT-LINTABLE | — | Its own Static detection decides by HEAD → GET → descriptive-UA GET against the asset's real home; no package byte can prove "serves nowhere". Extraction only nominates. |
| KB-03 | LINTED | `lint_malformed_url` | Grep of both CSS channels for `url(null)`/`url()`/elided/unbalanced `url(`, with escapes, comments and wikitext inline-code examples suppressed. The four `url(none)` fires are included on KB-71's own FP text, which names `url(none)` as KB-03's shape. |
| KB-04 | ALREADY-AUTOMATED | `FONT-IMPORT` / `det_font_import` (SIG_META §4) | Detects the malformed family parameter; the recipe's deciding evidence is the load probe (400 vs 200), already the detector's Verify line. |
| KB-05 | NOT-LINTABLE | — | Static detection issues a HEAD and records `Content-Type`; MIME type is external state. |
| KB-06 | ALREADY-AUTOMATED | `KB06-DEFAULT` / `det_kb06` (SIG_META §8) | Unsubstituted `{$param}` given an evidenced default is the signature. |
| KB-07 | LINTED | `lint_interwiki_style` | Counts includes and priorities; suppresses mutually exclusive parameter gates and original-identical stacks per the pattern's own False-positive section. |
| KB-08 | ALREADY-AUTOMATED | `IFTAGS` / `det_iftags` (SIG_META §2) | Its Verify line is the KB-08 recipe: every condition names JP tags; a bare `[[iftags]]` is the anomaly. |
| KB-09 | ALREADY-AUTOMATED | `BARE-RATE-DEL` / `det_bare_rate` (+ `RATE-EXHIBIT-KEPT-CANDIDATE`) | Detects the removed bare Rate beside the preview module; labelled paired exhibits are routed to the writer slot. |
| KB-10 | ALREADY-AUTOMATED | `TASL-FIELDS` / `det_tasl`, `CREDIT-PREVIEW` / `det_credit_preview`, `CREDIT-PROSE` / `det_credit_prose` | The eight-field and credit-module checks are the classifier's section-1 signatures. |
| KB-11 | ALREADY-AUTOMATED | `T7-CREDIT-CSS` / `det_t7` | SIG_META cites KB-11/12/62; its Verify line is the KB-11 recipe (production counterpart comparison). |
| KB-12 | ALREADY-AUTOMATED | `T7-CREDIT-CSS` / `det_t7` | Same detector; the "supplement vs inherited" note is exactly this pattern's question. |
| KB-13 | LINTED | `lint_modalbox_pin` | Global (line-initial) `.modalbox { position:fixed + 50%/translate }` with no `.credit-static-view .modalbox` carve-out; both channels. Zero current instances; synthetic control fires. |
| KB-14 | ALREADY-AUTOMATED | `BASE-DELIVERY` / `det_base_cross`, `CROSS-IMPORT`, `DELIVERY-HOST` / `det_delivery_host`, `SELF-DELIVERY` / `det_self_delivery` | Cross-theme and original-delivery repoints are the classifier's section-3 signatures. |
| KB-15 | ALREADY-AUTOMATED | `INCLUDE-REPOINT` / `det_include_repoint`, `COMPONENT-SWAP`, `ESCAPED-INCLUDE` / `det_escaped_include` | Foreign/unprefixed include repointing is already mechanised; role equivalence remains the detector's Verify step. |
| KB-16 | ALREADY-AUTOMATED | `JPFONT-LOAD` / `det_jpfont_load`, `JPFONT-STACK` / `det_font_stacks`, `FONTLOAD-CJK-STACK` | Load-gap and stack-fallback signatures with base subtraction. |
| KB-17 | ALREADY-AUTOMATED | `ASSET-REHOST` / `det_asset_rehost`, `DELIVERY-HOST` | Host allowlist re-host signature; NL-11's well-formed repoint boundary is documented in the suppression registry. |
| KB-18 | ALREADY-AUTOMATED | `TRANSLATION-ANCHORED` / `det_translation`, `TRANS-UNANCHORED`, `GLYPH-FORM` / `det_glyph`, `CONTENT-STRING` / `det_content_string`, `COMMENT-TEXT` / `det_comment_text` | Visible-string, CSS `content:` and porter-visible comment classes are classifier signatures. |
| KB-19 | NOT-LINTABLE | — | Static detection runs `wd_revisions.py diff … --from <rev>` and classifies post-revision hunks; the upstream revision and tool are external state. |
| KB-20 | LINTED | `lint_oversize` | Char-count near 200,000 with the pattern's own FP applied: within 1.2× of the original is the original's size, not inlined base. Zero current instances; synthetic control fires. |
| KB-21 | LINTED | `lint_fragile_param` | Includes `= http://` and `[[image http://` only; plain https draft-bucket assets are excluded. |
| KB-22 | NOT-LINTABLE | — | Its own Static detection ends with "the remainder is the candidate-own host set to adjudicate per theme … with evidence" — per-host posting/render adjudication is external. |
| KB-23 | NOT-LINTABLE | — | The pattern's own recipe is defeated by NL-03: literal grep found none of the 11 confirmed instances because overflow arrives via base-family membership, absent from package bytes; the deciding signal is a render measurement. |
| KB-24 | NOT-LINTABLE | — | Static detection is a triage look for fixed header pixels; "clipping/collision" is decided by screenshot, and preview-notice clipping is KB-34. |
| KB-25 | NOT-LINTABLE | — | Its own text says "Triage signal only … presence of the control in source proves nothing"; WebKit-vs-Chromium absence is a render comparison. |
| KB-26 | NOT-LINTABLE | — | Same triage surface plus open-state cascade; "presence of the control in source proves nothing; the failure is in the open-state cascade". |
| KB-27 | NOT-LINTABLE | — | Static check is a triage suppression/restyle hint; T3 must confirm no toggle is reachable in either engine. |
| KB-28 | NOT-LINTABLE | — | Static detection computes ratios for "the pairs the sample construction actually composes"; the sample composition and computed pair need render, and variable-driven palettes "cannot be settled statically". |
| KB-29 | NOT-LINTABLE | — | Its own Static detection is labelled NON-WORKING: "no working static form is known; render evidence is the only instrument" (render-only status). |
| KB-30 | NOT-LINTABLE | — | Grep only nominates `#login-status`/header hiding; a deliberately relocated login state is "a design question for T3" — render decides. |
| KB-31 | NOT-LINTABLE | — | Static detection is a triage fixed-width scan, but it must first exclude preview-module pages and the module flavour comes from the render setup; overflow is measured. |
| KB-32 | LINTED | `lint_preview_credit` | File-first disposition exactly as written: presence of `credit:start-preview`/`end-preview` makes every `credit-modal` line preview-form. |
| KB-33 | NOT-LINTABLE | — | Disposition is by measured page widths (337/389/416/419/884) read from render output, not present in a package; the BHL attribution is also explicitly open. |
| KB-34 | NOT-LINTABLE | — | Disposition by element identity in a screenshot (preview-notice row vs theme header). |
| KB-35 | NOT-LINTABLE | — | Doubling is observed at ≤375 on render and its attribution is an open contradiction; "no candidate-file check supports charging any other theme". |
| KB-36 | NOT-LINTABLE | — | WebKit-only glyph quirk; "no candidate file content predicts or fixes it". |
| KB-37 | NOT-LINTABLE | — | Disposition by element identity in the shared sample's specimen inventory; the machine line comes from render output. |
| KB-38 | NOT-LINTABLE | — | A `sidebar-position` warn is compared to a Sigma-9 baseline and cleared by visual inspection; no source check exists. |
| KB-39 | NOT-LINTABLE | — | Its own text: "Never charge or clear on the warn alone"; needs the composed pair and design intent. |
| KB-40 | NOT-LINTABLE | — | Static detection subtracts hosts from a render_check `runtime-hotlink` line; that line lives in render summaries, not in a package. Its host set is recorded in the linter's `ENV_HOSTS` for reference, but the subtraction cannot be executed here. |
| KB-41 | ALREADY-AUTOMATED | `DRAFT-HOST` / `det_draft_host` (SIG_META §3) | Draft-host class-(iii)/(ii) disposition is the classifier's signature. |
| KB-42 | LINTED | `lint_http_scheme` | Live `http://` grep with NL-07 namespace and NL-15 CSS-comment suppression; byte-identical-to-original lines are tagged class (ii), not candidate-inherent. |
| KB-43 | NOT-LINTABLE | — | Disposition by the `url-https//` line shape in a render summary; the include set and theme CSS "produce neither line". |
| KB-44 | NOT-LINTABLE | — | Static detection reads a summary's host set and `hidden-*` block — render output, not package text. |
| KB-45 | NOT-LINTABLE | — | Decided by `summary.md` presence and render exit code (0/1/2); no render artifacts in the corpus. |
| KB-46 | NOT-LINTABLE | — | Decided by the capture inventory (`*-full.png` presence/size), external to packages. |
| KB-47 | NOT-LINTABLE | — | Decided by counting engine/viewport combos in render summaries. |
| KB-48 | NOT-LINTABLE | — | "Read the test-wiki page's tags (page HTML or API)" plus cache state — live wiki state. |
| KB-49 | NOT-LINTABLE | — | Decided by a `?nocache=` GET and byte comparison against canonical — live fetch. |
| KB-50 | LINTED | `lint_hidden_rate_shape_a` | File-first disposition of shape (a): no bare Rate and no real (non-preview) credit module settles `hidden-rate`; the operative 254-file Rate-absence set is computed directly. |
| KB-51 | NOT-LINTABLE | — | Its own Static detection requires validating against known reference counts and probing the complete untruncated URL; a scanner flag is only a nomination. The mechanical `@@`/fragment-half checks are used as suppressions in the linter, but cannot disposition a target alone. |
| KB-52 | NOT-LINTABLE | — | Its own Static detection is "None": the state is the absence of a page, and the corpus package's existence is not a signal. Carried as EXCEPTION in reporting, not lintable. |
| KB-53 | NOT-LINTABLE | — | "Carry row 37 as environment-form in every sweep" — a standing disposition by construction, with no candidate-file check. |
| KB-54 | NOT-LINTABLE | — | Defined as the *failed* role-equivalence probe of KB-15 with documented evidence; external probe. |
| KB-55 | LINTED | `lint_candela_parallel` | Detects the granular `fragment:parallel` imports and emits the named exception, suppressing cross-theme-import charges. Zero current instances (FIX3-PC replaced them); synthetic control fires. |
| KB-56 | LINTED | `lint_peroxide_escaped` | `:oxygennine:peroxide:*` hits classified by escape context; escaped = EXCEPTION, live = KB-15 route. Both `@@…@@` and the corpus's `{{…}}` exhibit form are recognised. |
| KB-57 | ALREADY-AUTOMATED | `HEADERVAR` / `det_headervar` (SIG_META §5) | EN header-variable census is the classifier's signature; ruling 2 makes it never-fix. |
| KB-58 | NOT-LINTABLE | — | Distinguishing a deferred 404 from KB-02 requires the KB-02 HEAD probe and a known live home/re-host path. |
| KB-59 | LINTED | `lint_escaped_footnoteblock` | Exact `@@[[footnoteblock]]@@` exhibit → staff-call disposition; other footnoteblock forms are not nominated. |
| KB-60 | ALREADY-AUTOMATED | `LICENSE-BOX` / `det_license_box` (SIG_META §1) | Records the include form verbatim as the detector's notes do; fresh fullname probe is the only new evidence. |
| KB-61 | NOT-LINTABLE | — | Its own Static detection compares ROLES, and says a byte-completeness charge "requires a separate coordinator adjudication that does not exist"; no standard to check against. |
| KB-62 | ALREADY-AUTOMATED | `T7-CREDIT-CSS` / `det_t7` | The classifier's Verify line is KB-62's fa-info/base-subtraction recipe; render confirmation remains its disposition. |
| KB-63 | ALREADY-AUTOMATED | `LICENSE-BOX` / `det_license_box` | Its notes distinguish "restoration (KB-63): the original carried a license box" from supplement — the KB-63 pair test. |
| KB-64 | ALREADY-AUTOMATED | `SIGMA-PLUS-JP` / `SIGMA-PLUS-NONJP` / `det_sigma_plus` | Bare-form grep is the signature's Verify line. |
| KB-65 | ALREADY-AUTOMATED | `DUPIMPORT-DEL` / `det_dupimport` | File-level duplicate-@import recipe is the signature; gated preset copies are kept. |
| KB-66 | ALREADY-AUTOMATED | `LINK-REPOINT` / `det_link_repoint` | Prose-link repointing is the classifier's section-7 signature; the probe is its Verify line. |
| KB-67 | NOT-LINTABLE | — | Exhibit census can nominate an absence, but the charge is "absent or replaced unit with **no ground on record**"; checking the explanation/ledger for a ground and judging teaching-role equivalence is a record-reading judgment. |
| KB-68 | LINTABLE-DEFERRED | design sketched | Three-way similarity census over `pages-existing/` (candidate vs production counterpart vs branch original), both channels parsed; adoption signature = near-identity to production plus drift-marker leg. Requires reading outside `review/` and a similarity threshold, so deferred. |
| KB-69 | LINTABLE-DEFERRED | design sketched | Head diff: original carries a title-image reference with no candidate counterpart + candidate text title coloured from a theme variable + all three exclusions (no new host/live link/substituted asset). Needs a semantic "language-bearing" judgment on the artwork. |
| KB-70 | LINTED | `lint_codeaddr` | Self-addressed `local--code/<own>/N` vs `[[code]]` ordinals, with the original-identical inherited self-import suppressed; the served-size census remains the external deciding probe. |
| KB-71 | LINTED | `lint_block_structure` | Delivered-block-only comment termination and brace-depth profile; documentation exhibits excluded, so the starbasalt wikitext-brace artefact is not charged. |
| KB-72 | LINTED | `lint_doc_default` | Documentation default lines (`デフォルト値`, `default`, `本文フォントは`) compared to `:root` and loaded fonts; CSS selector lines excluded. Nominations, since a recorded port adaptation can explain a difference. |
| KB-73 | LINTED | `lint_param_gate` | Pair inventory of `{$…}` gate tokens, slots and gate bodies; the mutually exclusive preset-gate and different-delivery-path FP forms are recorded. |
| KB-74 | LINTABLE-DEFERRED | design sketched | Per-module top-level selector/variable census, candidate vs original, preferring same-channel pairing; the recipe requires subtracting the resolved base, which is not in a package. |
| KB-75 | LINTABLE-DEFERRED | design sketched | Census the canonical `pages/` for part pages named in a delivery banner; a cited location resolving outside the repo is the hit. Needs a repo-wide page census outside `review/`. |
| KB-76 | LINTED | `lint_dup_tail_block` | Pair census of short `[[div]]` blocks in the two tail windows; candidate count must exceed the original's. |
| KB-77 | LINTABLE-DEFERRED | design sketched | Compare original own-layer variables with the resolved base chain and flag silent candidate regressions; the resolved base chain is external to the package. |
| KB-78 | LINTED | `lint_empty_collapsible` | `[[collapsible]]` open immediately followed by close; paired against the original so an inherited empty pair is not a port hit. |
| KB-79 | LINTED | `lint_exhibit_leak` | Delivered block whose tail holds an exhibit-shaped `:root` and whose brace depth ends above 0; zero current instances, synthetic control fires. |
| KB-80 | LINTED | `lint_footnoteblock_added` | Pair census: original inline `[[footnote]]` with no block + live candidate block → benign supplement disposition. |
| KB-81 | ALREADY-AUTOMATED | `LINK-REPOINT` / `det_link_repoint` | Absolute-URL-vs-bare-wikilink repoint blocks are the signature; the dual HEAD probe is its Verify line. |

**Totals for the 81 patterns:** LINTED 19, ALREADY-AUTOMATED 22, NOT-LINTABLE 35, LINTABLE-DEFERRED 5 = **81**.

### Coverage ledger — NEGATIVE-LEDGER (15 entries)

| ID | Disposition | Rule / where | Ground |
|---|---|---|---|
| NL-01 | LINTED | suppression `NL-01/02:two-channel` in `_scrub()` / `css_channels()` | Both CSS channels are parsed by every structural rule; the retracted single-channel sets cannot recur. |
| NL-02 | LINTED | same suppression | Second independent fabrication from the same method defect; the same two-channel rule prevents both. |
| NL-03 | NOT-LINTABLE | — | Its own record: literal grep found none of the 11 confirmed instances; the deciding signal is base-family membership, which package bytes do not carry. |
| NL-04 | NOT-LINTABLE | — | Its own record: the KB-29 static recipe "FAILS TOTALLY" and the pattern is render-only; no static instrument exists. |
| NL-05 | NOT-LINTABLE | — | Its own record: neither measured instance has the assumed fixed width; the overflow mechanism needs measured render. |
| NL-06 | NOT-LINTABLE | — | Its own record: same-rule pairing misses cross-rule composition, and old-money-theme's pair appears as literals nowhere in its candidate; render/cross-rule judgment required. |
| NL-07 | LINTED | suppression `NL-07:xmlns-identifier` in `lint_http_scheme` | The model example: `http://www.w3.org/…` namespace identifiers are classified by host context and excluded before counting. |
| NL-08 | ALREADY-AUTOMATED | `COMMENT-TEXT` / `det_comment_text` | The classifier already counts and skips translated CSS comments as porter-visible, the recorded non-finding. |
| NL-09 | ALREADY-AUTOMATED | `ANNOTATION` / `det_annotation` | Porter notes and editor lines are the classifier's section-10 signature and are listed, not charged. |
| NL-10 | ALREADY-AUTOMATED | `WS-ONLY` / `det_ws_only` | Whitespace-only/re-indentation blocks are counted and skipped by the classifier; the remedy is disclosure. |
| NL-11 | ALREADY-AUTOMATED | `FONT-IMPORT` / `det_font_import` + `JPFONT-LOAD` / `det_jpfont_load` | A well-formed host repoint or import-only family is simply the absence of those detectors' malformed-parameter/load-gap hits; the boundary is also recorded in the suppression registry. |
| NL-12 | NOT-LINTABLE | — | Its own record classifies these as tooling/process agenda "not promoted to patterns"; they name no candidate-file-checkable defect mechanism. |
| NL-13 | NOT-LINTABLE | — | Supersession notes and wave attribution are documentation disciplines needing git history and protocol judgment, not a source check. |
| NL-14 | ALREADY-AUTOMATED | `ANNOTATION` / `det_annotation` | Extension of NL-09: prose-form notes, banner-closing annotations and annotation-truth claims are additions the classifier already labels. |
| NL-15 | LINTED | suppression `NL-15:css-source-comment` in `lint_http_scheme` | `http://` inside a CSS source-citation comment (andesite L677) is scrubbed; never counted as KB-42 or KB-02. |

**Totals for the 15 NL entries:** LINTED 4, ALREADY-AUTOMATED 5, NOT-LINTABLE 6 = **15**.

## 3. Corpus run results

Command: `python3 review/lint_patterns.py --corpus` (and `--json` for the machine copy). Result: **305 packages, 887 findings, 0 rule errors**. Fire counts include disposition records; the four LINTED rules with zero current instances are KB-13, KB-20, KB-55, KB-79 (all four have positive controls below).

| Rule | Fires | Distinct packages | Package list |
|---|---:|---:|---|
| KB-03 `lint_malformed_url` | 4 | 4 | anniversary-jp, flowergarden-jp, plugsoft-jp, ui-jp (all `url(none)`) |
| KB-07 `lint_interwiki_style` | 20 | 9 | foxtrot-jp, gsk-jp, highlighter-bhl-jp, min-theme, peroxide-jp-base-css, sci-fi-jp, shancheng-jp, skipos-jp, wikifot-jp |
| KB-13 `lint_modalbox_pin` | 0 | 0 | none in the package corpus |
| KB-20 `lint_oversize` | 0 | 0 | none (all historical oversize candidates restructured; FP rule applied) |
| KB-21 `lint_fragile_param` | 1 | 1 | y2k-jp (L43) |
| KB-32 `lint_preview_credit` | 283 | 283 | all preview-module packages — full list in Appendix A / `per-rule-packages.txt` |
| KB-42 `lint_http_scheme` | 110 | 36 | al-slop-jp, black-highlighter-theme-jp, bulgunae-jp, chaos-jp, classic-jp, dark-dealings-jp, eventyr-jp, flopstyle-dark-jp, foxtrot-jp, gsk-jp, internal-affairs-jp, isolated-terminal-jp, jakstyle-jp, last-frontier-jp, magazine-jp, minimalist-bhl-jp, mox-jp, much-cool-jp, night-rush-theme-jp, onko-sinulla-nalka-theme-jp, ontology-department-jp, paperstack-jp, paramycota-jp, pataphysics-jp, penumbra-jp, sci-fi-jp, scplive-jp, share-future-community-jp, spidersfalling-jp, starry-jp, steam-guide-jp, travellers-book-jp, turbo-vision-jp, xmas-jp, y2k-jp, yossistyle-jp |
| KB-50 `lint_hidden_rate_shape_a` | 269 | 269 | all no-Rate/no-real-credit packages — full list in Appendix A / `per-rule-packages.txt` |
| KB-55 `lint_candela_parallel` | 0 | 0 | none (candidate uses the FIX3-PC bundle + override) |
| KB-56 `lint_peroxide_escaped` | 17 | 1 | peroxide-jp (16 exhibit lines + 1 prose inline-code line) |
| KB-59 `lint_escaped_footnoteblock` | 13 | 13 | aesthetic-theme-jp, basalt-jp, bedrock-jp, cosmonaut-jp, isolated-terminal-jp, jakstyle-jp, monotypical-jp, ouroborous-theme-jp, quand-le-soleil-se-couche, saphir-jp, scpedia-jp, space-jp, turbo-vision-jp |
| KB-70 `lint_codeaddr` | 6 | 4 | blackinblack-jp, dark-dealings-jp, flopstyle-dark-jp, tfnac-jp |
| KB-71 `lint_block_structure` | 18 | 9 | ambrose-chapter-two-jp, anon-jp, flopstyle-dark-jp, greystyle-jp, immrama-jp, ink-jp, pastel-skies-jp, rima-jp, wikifot-jp |
| KB-72 `lint_doc_default` | 29 | 29 | basalt-jp, bedrock-jp, blackinblack-jp, broken-world-jp, chaos-jp, dia-de-muertos-jp, dustframe-jp, eigenvector-jp, gp-refresh-jp, isolated-terminal-jp, laruetheme-jp, laughter-and-knives-theme-jp, lumina-jp, magicity-jp, oceanbound-jp, old-money-theme-jp, paradigm-inapplicable-jp, paradigm-inapplicable-sigma-jp, paradigm-reconstruction-jp, ragnarok-theme-jp, raisa-jp, retrofutura-jp, sigma-jp, skipos-jp, starbasalt-jp, stargazer-jp, stellar-jp, waxed-oxidized-cut-copper-slab-jp, winddew-in-hand-jp |
| KB-73 `lint_param_gate` | 86 | 29 | ad-abyssum-penumbra-jp, admo-jp, anniversary-jp, a-problematic-theme-jp, bloodraven-jp, borealis-constant-theme-jp, broken-world-jp, dream-of-the-stars-jp, foundom-jp, foxtrot-jp, frownstyle-jp, greyday-jp, greystyle-jp, marchen-jp, navla-style-jp, oceanbound-jp, our-open-veins-jp, paramycota-jp, peroxide-jp, peroxide-jp-base-css, quand-le-soleil-se-couche, redtape-jp, sci-fi-jp, shushuin, simple-yonder-jp, spidersfalling-jp, steam-guide-jp, tales-of-the-mosaic-jp, xmas-jp |
| KB-76 `lint_dup_tail_block` | 4 | 2 | chatscp-jp, yore-jp |
| KB-78 `lint_empty_collapsible` | 24 | 24 | copper-jp, cosmos-jp, cyber-specter-jp, fogwalker-jp, foundom-jp, frownstyle-jp, greyday-jp, highlighter-bhl-jp, last-frontier-jp, opinions-broadcaster-jp, parablue-jp, paradigm-inapplicable-jp, paradigm-inapplicable-sigma-jp, paradigm-reconstruction-jp, peroxide-jp, sci-fi-jp, shancheng-jp, shattered-thoughts-jp, starry-jp, steam-guide-jp, the-other-side-jp, trauma-jp, waxed-oxidized-cut-copper-slab-jp, winxp-jp |
| KB-79 `lint_exhibit_leak` | 0 | 0 | none in the package corpus |
| KB-80 `lint_footnoteblock_added` | 3 | 3 | deepspace-jp, the-other-side-jp, writing-anomalies-jp |

Sum of fires: 4+20+0+0+1+283+110+269+0+17+13+6+18+29+86+4+24+0+3 = **887**, matching the corpus runner's total (machine-extracted from `corpus-run.tsv`).

## 4. Control validation

`validate_controls.py` builds 31 controls; **31 PASS, 0 FAIL** (full log in `control-validation.txt`). Positive controls are either README/`classification.json`-recorded instances that must still fire, or a synthetic reconstruction of pre-repair bytes from the named canonical commit. Negative controls are packages whose candidates changed after their build and must not fire on current bytes.

### 4.1 Positive controls — recorded instances still firing

| Rule | Instance | Evidence | Result |
|---|---|---|---|
| KB-21 | y2k-jp L43 | README §4/§11 records the `name= http://…` image-block exhibit and T1 http×1 | FIRES (1) |
| KB-42 | y2k-jp L43 | Same recorded line; class (ii) scheme rewrite | FIRES (1) |
| KB-56 | peroxide-jp | README §11 records 16 `FOREIGN-KEPT :oxygennine:` exhibits | FIRES (17: 16 exhibits + 1 prose inline-code) |
| KB-59 | cosmonaut-jp L226, basalt-jp L1657, space-jp L135, aesthetic-theme-jp L881 | READMEs record the escaped exhibit; exact `@@[[footnoteblock]]@@` | FIRES (1 each) |
| KB-07 | gsk-jp L37 (priority 2), sci-fi-jp L42, shancheng-jp L25, min-theme (no frame) | README priority/interwiki sections | FIRES (1 each) |
| KB-78 | copper-jp L89-90, cosmos-jp L49-50 | README structure sections record the empty collapsible | FIRES (1 each) |
| KB-76 | yore-jp tail | README records the duplicated `part-nav` divs | FIRES (3) |
| KB-80 | deepspace-jp L419 | README records the inline-footnote → footnoteblock supplement | FIRES (1) |
| KB-73 | anniversary-jp | README §3 records the parameter gate set | FIRES (9 token-level nominations) |

### 4.2 Positive controls — synthetic pre-repair bytes

| Rule | Reconstruction | Result |
|---|---|---|
| KB-70 | 5k-jp with the exact `\| theme=…theme%3A5k-jp/1` line removed by commit `722ceb5` reinserted | FIRES (1); current bytes: 0 |
| KB-55 | candela-jp candidate set to the original's granular `fragment:parallel/code/1` and `/code/3` imports (pre-FIX3-PC) | FIRES (2); current bytes: 0 |
| KB-71 | anniversary-jp with the `}` added by commit `0c327f3` removed (pre-repair unclosed `#page-title` rule) | FIRES (1, depth end 1); current bytes: 0 |
| KB-20 | blankstyle-jp with a 240 KB inlined framework base appended | FIRES (1); current candidates: 0 |
| KB-13 | blankstyle-jp with a global `position:fixed` + 50%/translate `.modalbox` rule and no carve-out | FIRES (1) |
| KB-79 | synthetic candidate with an exhibit `:root` at the tail of the delivered block, depth ending at 1 | FIRES (1) |

### 4.3 Negative controls — repaired defects do not fire

| Rule | Repaired set | Evidence | Result |
|---|---|---|---|
| KB-70 | the 21 `722ceb5` FIX-FRAMEADDR packages (5k, 3law-pride, 3lawcracked, 512-onwards, admo, alcur, angel, ashes-to-ashes, crayon, crt, deepspace, deserted-years-theme, foundation-paper, king-s-palace, opinions-broadcaster, quand-le-soleil-se-couche, ragnarok, sigma, spidersfalling, the-foundation-sigma, words-of-wisdom) | READMEs record the `theme=` self-address line deleted; the in-repo `git show 722ceb5` diff confirms it | **0 fires across all 21** |
| KB-42 | admo-jp L461 http logo line, repaired by `662baf3` to the https `theme%3Abasalt` URL (README item 4) | no `http://` remains in the candidate | 0 fires |
| KB-55 | candela-jp current candidate (FIX3-PC replaced granular CN imports with the JP bundle + `:root` restoration) | README §3 and §11 describe the repair; bytes confirm | 0 fires |
| KB-20 | betwixt, kitchen, peroxide, magazine (the four oversize candidates) | READMEs record restructure/externalisation; all are ~1.0–1.2× their originals' size | 0 fires |
| KB-71 | anniversary-jp current candidate | README §8 records the brace repaired at `0c327f3`; scan ends at depth 0 | 0 fires |

### 4.4 Honest disagreements and limits of the controls

- **KB-59 count:** the pattern's sweep record is 16 hits; the current corpus has 13 escaped `@@[[footnoteblock]]@@` instances. The linter reports what is in the bytes (13). This is a record-versus-bytes discrepancy, not a rule disagreement; no resolution is invented here.
- **KB-56 count:** the linter's 17 fires are 16 exhibit lines plus the prose line at candidate L463, where the README counts 16 `FOREIGN-KEPT` forms and 20 total `:oxygennine:` references. Both counts are reported; the linter classifies all 17 as the named exception, never as a defect.
- **KB-70 / KB-71 / KB-72 / KB-73 / KB-78 fires are nominations, not verdicts.** Their patterns' own Static detection sections retain an external deciding step (served-size probe, original-side depth comparison, recorded port adaptation, record-ground check, deliberate-placeholder ground). The linter does not claim to close those steps.
- **KB-03's four `url(none)` fires** go slightly beyond the recipe's literal `url(null)`/`url()` list, grounded on KB-71's False-positive section which explicitly names `url(none)` as KB-03's shape. They are candidate-inherent by the pattern's mechanism (`/none` request), and were not repaired.
- A `{{…}}` inline-code escape form had to be added beyond the KB's literal `@@…@@` wording: peroxide's documentation exhibits use `{{[[include …]]}}`. This is recorded in the `KB-56:peroxide-escaped` suppression entry rather than silently assumed.
- `--strict` was not used for the corpus run: findings here are data (most are dispositions), not tool failures.

## 5. Deliberately left, with grounds

- **No edits to patterns, packages or pages.** The brief restricts deliverables to the linter and the report.
- **The five LINTABLE-DEFERRED rules** (KB-68, 69, 74, 75, 77) are not implemented: each needs either an out-of-package file set (`pages-existing/`, canonical `pages/`, resolved base chain) or a semantic judgment the pattern itself leaves open. Their designs are sketched in the ledger; the brief permits deferral in this order.
- **The 35 NOT-LINTABLE patterns** are not stubbed. Each ledger row states the specific external state or judgment its own Static detection requires, so none is left undispositioned by an assertion of difficulty.
- **Existing classifier work was not duplicated.** ALREADY-AUTOMATED rows point to the exact detector/label; reimplementing them as current-bytes checks would have produced a second, disagreeing instrument rather than evidence.
- **Rule errors:** none. Every rule completed on all 305 packages; the runner's ERROR path was exercised in code review but produced no output in the final run.


## Appendix A — complete per-rule package lists (verbatim from `per-rule-packages.txt`)

```
KB-03: anniversary-jp flowergarden-jp plugsoft-jp ui-jp 
KB-07: foxtrot-jp gsk-jp highlighter-bhl-jp min-theme peroxide-jp-base-css sci-fi-jp shancheng-jp skipos-jp wikifot-jp 
KB-21: y2k-jp 
KB-32: 07k-jp 3lawcracked-jp 3law-pride-jp 512-onwards-jp 5k-jp aces-and-eights-jp ad-abyssum-penumbra-jp admo-jp aesthetic-theme-jp alcur-theme-jp alexylva-university-jp al-slop-jp ambrose-chapter-two-jp a-midnight-invitation-jp andesite-jp angel-jp animal-instead-of-beast-jp anniversary-jp anon-jp another-night-jp a-problematic-theme-jp ared-jp art-deco-jp asagao-jp ashes-to-ashes-jp atlas-maniacus-jp back-jan-fire-jp basalt-jp bedbugs-theme-jp bedrock-jp betwixt-jp black-diamond-jp black-highlighter-theme-jp blackinblack-jp black-market-jp black-rain-jp black-serpent-jp blankstyle-jp blood-jp bloodraven-jp borealis-constant-theme-jp brokedown-database-jp broken-light-jp broken-world-jp bulgunae-jp candela-jp caretaker-sigma-jp caretaker-theme-jp chaos-jp chatscp-jp ch-scp-theme-jp classic-jp cleaning-services-jp clock-tower-jp cmst-jp cobalt-aero-glass-jp construct-jp copper-jp cosmonaut-jp cosmos-jp crayon-jp creature-jp crt-jp cyber-specter-jp darkblue-jp dark-dealings-jp dark-jp darkqueer-jp dear-dictator-jp decay-jp decom-dept-jp deepspace-jp derby-jp deserted-years-theme-jp dia-de-muertos-jp diamond-highlighter-jp doap-bhl-jp doap-nvl-jp dream-of-the-stars-jp drunken-alley-jp dustframe-jp dynamikron-jp eigenmachine-jp eigenvector-jp emotion-division-jp enlightened-eyes-jp ethic-committee-jp eventyr-jp extra-black-highlighter-theme-jp fandom-jp febris-pharmaceuticals-theme-jp fish-jp flopstyle-dark-jp flopstyle-jp flowergarden-jp fmaf-theme-jp fmd-bhl-theme-jp fogwalker-jp food-jp fossil-jp foundation-paper-jp foundom-jp foxtrot-jp frownstyle-jp frutiger-aero-jp fuladh-theme-jp galactic-theme-jp garak-the-magazine-jp golden-feast-jp golden-samdaecheon-jp golden-wind-jp gp-refresh-jp greyday-jp greystyle-jp gsk-jp halloween-jp halloween-koreana-jp hansarp-jp helix-jp highlighter-bhl-jp highroller-jp horn-jp hytoth-two-jp i57-jp i57-theme-jp immrama-jp inkblot-jp ink-jp inland-empire-jp internal-affairs-jp isolated-terminal-jp it-pillar-of-industry-jp jakstyle-jp janitor-closet-jp jiha-jp just-girly-things-jp kcia10-jp king-s-palace-jp kiryu-labs-theme-jp kitchen-jp lampeter-warm-jp laruetheme-jp last-frontier-jp laughter-and-knives-theme-jp lead-by-example-jp legend-of-blue-jp linear-black-jp lumina-jp madoka-jp magazine-jp magicity-jp magpie-swoops-jp marchen-jp maxwell-s-silver-hammer-jp mcf-jp minimalist-bhl-jp minimal-scp-foundation-by-cocoonist-jp mole-cricket-jp monotypical-jp mox-jp mr-reprisal-jp much-cool-jp nameless-jp navla-style-jp night-rush-theme-jp normal-jp note-theme-jp obflow-jp oceanbound-jp old-money-theme-jp oneiroi-west-jp onko-sinulla-nalka-theme-jp ontology-department-jp opinions-broadcaster-jp ordopharm-jp ouroborous-theme-jp our-open-veins-jp pack-of-peanuts-jp pacom1943-jp paperstack-jp parablue-jp paradigm-inapplicable-jp paradigm-inapplicable-sigma-jp paradigm-reconstruction-jp parallel-jp paramycota-jp parawatch-pumpkin-jp pastel-skies-jp past-oriented-jp pataphysics-jp path-of-jinin-jp penumbra-jp peroxide-jp petrifaction-jp plant-jp plugsoft-jp progress-institute-jp prom-labs-jp quand-le-soleil-se-couche queen-s-gambit-jp queerstyle-jp ragnarok-theme-jp raisa-jp raisa-sigma-jp redsquare-jp redtape-jp retro-aiad-theme-jp retrofutura-jp rima-jp rok-gov-theme-jp rpma-jp saphir-jp scheme-jp sci-fi-jp scpdeclassified-jp scpedia-jp scp-human-resources-jp scp-human-resources-sigma-jp scplive-jp scp-offices-sigma-jp scp-offices-theme-jp shancheng-jp share-future-community-jp shark-punching-centre-bhl-jp shattered-thoughts-jp shivering-night-jp shoebill-jp sigma-jp simple-yonder-jp skiesmadestrange-jp skipos-jp sodium-jp sodium-pentasulfide-jp some-guider-jp sound-jp space-jp spidersfalling-jp starbasalt-jp stargazer-jp starry-jp steam-guide-jp stellar-jp sunside-jp supply-n-demand-jp suprematism-jp tales-of-the-mosaic-jp telecommunications-monitoring-office-theme-jp tfnac-jp thalassophobia-jp thalassophobia-sigma-jp the-buck-stops-here-jp the-coalition-theme-jp the-foundation-sigma-jp the-greatest-education-jp the-other-side-jp the-smell-of-smoke-jp the-track-changers-jp trauma-jp travellers-book-jp turbo-vision-dark-jp turbo-vision-jp twin-files-jp ui-jp uiu-bhl-theme-jp ultimate-reader-jp unusual-cargo-jp vanguard-jp vanguard-supplement-jp voyager-jp walk-in-the-dark-jp waxed-oxidized-cut-copper-slab-jp wikifot-jp wilderness-jp winddew-in-hand-jp winxp-jp wish-for-miracle-jp wondertainment-jp words-of-wisdom-jp writing-anomalies-jp xmas-jp y2k-jp yore-jp yossistyle-jp 
KB-42: al-slop-jp black-highlighter-theme-jp bulgunae-jp chaos-jp classic-jp dark-dealings-jp eventyr-jp flopstyle-dark-jp foxtrot-jp gsk-jp internal-affairs-jp isolated-terminal-jp jakstyle-jp last-frontier-jp magazine-jp minimalist-bhl-jp mox-jp much-cool-jp night-rush-theme-jp onko-sinulla-nalka-theme-jp ontology-department-jp paperstack-jp paramycota-jp pataphysics-jp penumbra-jp sci-fi-jp scplive-jp share-future-community-jp spidersfalling-jp starry-jp steam-guide-jp travellers-book-jp turbo-vision-jp xmas-jp y2k-jp yossistyle-jp 
KB-50: 07k-jp 3lawcracked-jp 3law-pride-jp 512-onwards-jp 5k-jp aces-and-eights-jp ad-abyssum-penumbra-jp admo-jp aesthetic-theme-jp alcur-theme-jp alexylva-university-jp al-slop-jp ambrose-chapter-two-jp a-midnight-invitation-jp andesite-jp angel-jp animal-instead-of-beast-jp anniversary-jp anon-jp another-night-jp a-problematic-theme-jp ared-jp art-deco-jp asagao-jp atlas-maniacus-jp back-jan-fire-jp basalt-jp bedbugs-theme-jp bedrock-jp betterbetterfootnote-jp black-diamond-jp black-highlighter-theme-jp blackinblack-jp black-market-jp black-rain-jp black-serpent-jp blankstyle-jp blood-jp bloodraven-jp borealis-constant-theme-jp broken-light-jp bulgunae-jp candela-jp caretaker-sigma-jp caretaker-theme-jp centered-header-bhl-jp-base-css chaos-jp chatscp-jp ch-scp-theme-jp classic-jp cleaning-services-jp clock-tower-jp cmst-jp cobalt-aero-glass-jp collapsible-sidebar-jp-base-css construct-jp copper-jp cosmonaut-jp crayon-jp creature-jp crt-jp cyber-specter-jp darkblue-jp dark-dealings-jp dark-jp darkqueer-jp dear-dictator-jp decay-jp decom-dept-jp deepspace-jp derby-jp deserted-years-theme-jp dia-de-muertos-jp diamond-highlighter-jp doap-bhl-jp doap-nvl-jp dream-of-the-stars-jp dustframe-jp dynamikron-jp eigenvector-jp emotion-division-jp enlightened-eyes-jp ethic-committee-jp eventyr-jp excerpts-tool-jp extra-black-highlighter-theme-jp fandom-jp febris-pharmaceuticals-theme-jp fish-jp flopstyle-jp flowergarden-jp fmaf-theme-jp fmd-bhl-theme-jp fogwalker-jp food-jp fossil-jp foundation-paper-jp foundom-jp foxtrot-jp fragment-broken-world-jp frownstyle-jp frutiger-aero-jp fuladh-theme-jp galactic-theme-jp garak-the-magazine-jp golden-feast-jp golden-samdaecheon-jp gp-refresh-jp greyday-jp greystyle-jp gsk-jp halloween-jp halloween-koreana-jp hansarp-jp helix-jp highlighter-bhl-jp highroller-jp horn-jp hytoth-two-jp i57-jp i57-theme-jp immrama-jp inkblot-jp inland-empire-jp internal-affairs-jp isolated-terminal-jp it-pillar-of-industry-jp jakstyle-jp janitor-closet-jp jiha-jp just-girly-things-jp kcia10-jp kiryu-labs-theme-jp kitchen-jp lampeter-warm-jp laruetheme-jp last-frontier-jp laughter-and-knives-theme-jp legend-of-blue-jp license-box-theme-jp linear-black-jp lumina-jp madoka-jp magicity-jp magpie-swoops-jp marchen-jp maxwell-s-silver-hammer-jp mcf-jp minimalist-bhl-jp minimal-scp-foundation-by-cocoonist-jp mole-cricket-jp mr-reprisal-jp nameless-jp navla-jp navla-style-jp normal-jp note-theme-jp obflow-jp oceanbound-jp old-money-theme-jp oneiroi-west-jp onko-sinulla-nalka-theme-jp ontology-department-jp ordopharm-jp ouroborous-theme-jp our-open-veins-jp pack-of-peanuts-jp pacom1943-jp parablue-jp paradigm-inapplicable-jp paradigm-inapplicable-sigma-jp paradigm-reconstruction-jp parallel-jp paramycota-jp parawatch-pumpkin-jp pastel-skies-jp past-oriented-jp path-of-jinin-jp peroxide-jp peroxide-jp-base-css plant-jp plugsoft-jp progress-institute-jp prom-labs-jp quand-le-soleil-se-couche queen-s-gambit-jp queerstyle-jp ragnarok-theme-jp raisa-jp raisa-sigma-jp redsquare-jp redtape-jp retro-aiad-theme-jp retrofutura-jp rima-jp rok-gov-base-jp rok-gov-theme-jp rpma-jp sci-fi-jp scpdeclassified-jp scp-human-resources-jp scp-human-resources-sigma-jp scp-jp-sandbox3 scp-jp-storage scplive-jp scp-offices-sigma-jp scp-offices-theme-jp shancheng-jp share-future-community-base-css-jp share-future-community-jp shattered-thoughts-jp shivering-night-jp shoebill-jp sigma-10-jp sigma-jp simple-yonder-jp skiesmadestrange-jp skipos-jp sodium-jp sodium-jp-base-css sodium-pentasulfide-jp some-guider-jp sound-jp space-jp spidersfalling-jp starbasalt-jp stargazer-jp stellar-jp sunside-jp supply-n-demand-jp suprematism-jp suprematism-jp-base-css telecommunications-monitoring-office-theme-jp tfnac-jp thalassophobia-jp thalassophobia-sigma-jp the-buck-stops-here-base-1-jp the-buck-stops-here-jp the-coalition-theme-jp the-foundation-sigma-jp the-greatest-education-jp the-smell-of-smoke-jp the-track-changers-jp trauma-jp travellers-book-jp turbo-vision-dark-jp turbo-vision-jp twin-files-jp ui-jp uiu-bhl-theme-jp ultimate-reader-jp u-navstyle-jp-base-css unusual-cargo-jp vanguard-jp vanguard-supplement-jp voyager-jp walk-in-the-dark-jp waxed-oxidized-cut-copper-slab-jp waylandlaurencepan-jp wilderness-jp winddew-in-hand-jp winxp-jp wish-for-miracle-jp wondertainment-jp words-of-wisdom-jp writing-anomalies-jp xmas-jp yore-jp yossistyle-jp 
KB-56: peroxide-jp 
KB-59: aesthetic-theme-jp basalt-jp bedrock-jp cosmonaut-jp isolated-terminal-jp jakstyle-jp monotypical-jp ouroborous-theme-jp quand-le-soleil-se-couche saphir-jp scpedia-jp space-jp turbo-vision-jp 
KB-70: blackinblack-jp dark-dealings-jp flopstyle-dark-jp tfnac-jp 
KB-71: ambrose-chapter-two-jp anon-jp flopstyle-dark-jp greystyle-jp immrama-jp ink-jp pastel-skies-jp rima-jp wikifot-jp 
KB-72: basalt-jp bedrock-jp blackinblack-jp broken-world-jp chaos-jp dia-de-muertos-jp dustframe-jp eigenvector-jp gp-refresh-jp isolated-terminal-jp laruetheme-jp laughter-and-knives-theme-jp lumina-jp magicity-jp oceanbound-jp old-money-theme-jp paradigm-inapplicable-jp paradigm-inapplicable-sigma-jp paradigm-reconstruction-jp ragnarok-theme-jp raisa-jp retrofutura-jp sigma-jp skipos-jp starbasalt-jp stargazer-jp stellar-jp waxed-oxidized-cut-copper-slab-jp winddew-in-hand-jp 
KB-73: ad-abyssum-penumbra-jp admo-jp anniversary-jp a-problematic-theme-jp bloodraven-jp borealis-constant-theme-jp broken-world-jp dream-of-the-stars-jp foundom-jp foxtrot-jp frownstyle-jp greyday-jp greystyle-jp marchen-jp navla-style-jp oceanbound-jp our-open-veins-jp paramycota-jp peroxide-jp peroxide-jp-base-css quand-le-soleil-se-couche redtape-jp sci-fi-jp shushuin simple-yonder-jp spidersfalling-jp steam-guide-jp tales-of-the-mosaic-jp xmas-jp 
KB-76: chatscp-jp yore-jp 
KB-78: copper-jp cosmos-jp cyber-specter-jp fogwalker-jp foundom-jp frownstyle-jp greyday-jp highlighter-bhl-jp last-frontier-jp opinions-broadcaster-jp parablue-jp paradigm-inapplicable-jp paradigm-inapplicable-sigma-jp paradigm-reconstruction-jp peroxide-jp sci-fi-jp shancheng-jp shattered-thoughts-jp starry-jp steam-guide-jp the-other-side-jp trauma-jp waxed-oxidized-cut-copper-slab-jp winxp-jp 
KB-80: deepspace-jp the-other-side-jp writing-anomalies-jp
```

LINT-WAVE: COMPLETE
