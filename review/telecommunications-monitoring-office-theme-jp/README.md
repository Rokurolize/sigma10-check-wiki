# theme:telecommunications-monitoring-office-theme-jp — Telecommunications Monitoring Office theme (EN → JP port)

## Status

This file is the explanation record for one theme's Sigma-10 port. The
diff it explains is `diff.md` in this directory, generated from
`original.txt` (the frozen mirror) and `candidate.txt` (a byte copy of
the canonical candidate). The verdict stamp below is generated; do not
edit inside the stamp markers.

<!-- VERDICT:BEGIN -->
### Verdict stamp (generated — do not edit inside the markers)

Population #144. Canonical candidate:
`pages/theme:telecommunications-monitoring-office-theme-jp.txt`
(115 lines). Frozen original: scp-wiki revision 10.

| Check | Outcome |
|---|---|
| (b) go-sign ledger | PASS |
| T1 structural / link check | PASS — exit 0, 0 errors / 0 warn / 1 info |
| T2/T3 render check | FINDINGS — see the theme's rows in `review/AUTHORITIES/RENDER-ROWS-2.md` |
| T4/T5 localize check | FINDINGS — credit-notation nits only; no display-affecting findings in the row's text |
<!-- VERDICT:END -->

## Provenance

- Theme: `theme:telecommunications-monitoring-office-theme` on
  scp-wiki (EN branch), revision 10. Author BattleblockB0ss; a
  Black Highlighter layer for Telecommunications Monitoring Office
  articles.
- Frozen mirror: `original.txt`, 63 lines, 2,235 bytes, SHA-256
  `7067a858a684424db14976a3e3278476afd987ea19e19e2da8ed5fc4b35f23de`
  (matches `review/sources.tsv`; mirror-store class COPY).
- Candidate: `candidate.txt`, 115 lines, 4,358 bytes, SHA-256
  `43e9370d1b7f3931ca4e0cc9383ce4eede152bfaff642d4f4532223bc4a033a0`,
  byte-identical to the canonical file.
- Kind (sources.tsv): standard. The candidate layers over the Black
  Highlighter base by import and frame (section 3); it is not a
  K5b-3 code-layer port, so this diff covers the whole theme.
- Naming: `review/sources.tsv` keys the candidate by the short slug
  `telecom-office-theme-jp`, and ledger part (b) row 144 uses the
  short form as its key; the canonical file, this package, and every
  other ledger part use the long form
  `theme:telecommunications-monitoring-office-theme-jp`. The ledger's
  population check records the alias normalization. The per-theme
  record (item 2) notes one tooling consequence.
- The candidate entered the canonical repository in the Stage 2 EN20
  integration (3faf2e1, LOCALIZE-S2-C wave) and was touched once
  since, by the credit attribution normalization (1869877,
  FIX-CREDIT-D).

## Summary

The smallest package in this batch, and the cleanest: a 63-line
original whose whole substance is one `@supports` variable block over
the Black Highlighter base. The port repoints the base from the EN
project's GitHub Pages to the JP project's (in the head module and in
both frame slots), replaces the bare rate and prose-only credit with
a preview credit block, translates the prose and the CSS comments,
repoints the logo to the JP storage host (where it already serves),
inlines the delivery module instead of importing the exhibit's code
URL, and — the one change a careless reader might miss — repairs the
original exhibit's unclosed `@supports` block by adding its missing
closing brace. T1 passes this candidate outright (exit 0), the only
clean T1 in the batch. The findings on record are the render chain's
environment items and a set of credit-notation nits, all
dispositioned.

## Class summary (auto-classification)

15 change blocks: 6 specific (40.0%), 7 heuristic (46.7%), 2 residue
(13.3%), 0 skipped. The generator counts +78 / −26 lines (diff.md is
Tier 1 format for this package: 2 hunks). Label firings:
TRANS-UNANCHORED ×9, COMMENT-TEXT ×8, IFTAGS ×2, ASSET-REHOST ×2,
CONTENT-STRING ×2, HEADERVAR ×2, and single firings of DELIVERY-HOST,
CREDIT-PREVIEW, TASL-FIELDS, COMPONENT-SWAP, ESCAPED-INCLUDE,
INCLUDE-REPOINT, TRANSLATION-ANCHORED, CSS-BODY, DELIVERY-MOVE,
SELF-DELIVERY.

Adjudication notes: the heuristic mass is the CSS comment
translations inside the variable block (blocks B7–B13), resolved by
shape in section 6. The single CSS-BODY block (B14) is adjudicated
in section 8: it is the added closing brace of the `@supports`
block, a structural repair, not a font-stack or body rewrite. The
two residue blocks are the deleted bare rate (B2 — the classifier's
rate signature does not match the original's lowercase
`[[module rate]]`) and an alignment artifact at the frame insertion
(B3); both are resolved in the appendix.

## 0. Tag frame and page furniture

**What.** The candidate's head stands outside the tag gate: the base
module (candidate L1–4), then two interwiki-style frame includes
naming the base's two files at priorities 1 and 2 (candidate
L6–14), then the gate `[[iftags +テーマ]]` (candidate L16, block B4,
IFTAGS) opening over the credit block and body. The original opens
its gate first (`[[iftags +theme]]`, original L1) and has no frames.
The candidate's own delivery module sits at the tail, outside the
gate, as the original's did (section 3).

**Why.** Pattern class P1 (frame and tag furniture; KB-03, KB-04).
Failure prevented: a gate keyed to the EN tag name never opens on
scp-jp, and a BHL-family theme whose frames name the EN project's
bundle applies the wrong base in the check environment.

**Verify.** `grep -n 'iftags\|interwiki-style' candidate.txt` — gate
at L16 with the JP tag name; two frames above it, both
`:scp-jp:component:interwiki-style`, naming the JP BHL files.

**Disposition.** No ledger line charges the frame. The (b) verdict
for this theme is PASS, and T1 passes the file outright.

## 1. Credit block and license (P3, P9)

**What.** The original's only credit furniture is a bare rate in a
right-aligned div (original L8–10, lowercase `[[module rate]]`),
deleted (residue block B2; the candidate has no rate module). The
candidate carries a preview credit block (candidate L18–27, block
B4: CREDIT-PREVIEW, TASL-FIELDS) with eight fields: title
電気通信監視室テーマ; translator of record AI; translation year 2026;
original title Telecommunications Monitoring Office Theme;
copyright holder BattleblockB0ss; creation year 2023; reference
revision 10; and a source link to
`https://scp-wiki.wikidot.com/theme:telecommunications-monitoring-office-theme`
— the host `review/sources.tsv` records, so the host check passes,
and the link names the original's long-form page, matching the
mirror. The author field agrees with the original's prose credit
(original L12, carried at candidate L29).

**Why.** Pattern class P3 (credit furniture swap; KB-16, KB-17) with
P9 (attribution; KB-47). Failure prevented: EN credit components do
not exist on scp-jp, and a bare rate beside the credit block renders
a second rating widget.

**Verify.** `sed -n '18,27p' candidate.txt` against original L8–12;
`grep -ci 'module rate' candidate.txt` returns 0.

**Disposition.** T4 charged this credit block with notation nits
only (LOCALIZE-ROWS row 144): the translator field's `SCP-JP`
placeholder at check time, the unlinked translator/author fields,
and the generic `ソース` link text. The ledger supplement records
them "DISPOSITIONED under the staff-normalization class
(LOCALIZE-S2-C item 9)", and part (c3) records the credit fields
FIXED by the credit waves. The bytes agree on the substantive half:
the translator field now names AI (the fixing commit is in the
file's history, 1869877). The author field remains unlinked plain
text and the link text remains `ソース` — both dispositioned nits of
the population-wide notation class, not defects of this theme.
Neither side carries a license box, so there is no P9 license-box
conversion to record; no credit CSS supplement exists on either
side.

## 2. Includes and component references (P2, P8)

**What.** The usage exhibits (block B5: COMPONENT-SWAP,
ESCAPED-INCLUDE, INCLUDE-REPOINT) repoint both lines of the
original's install snippet: the base line to
`@@[[include :scp-jp:theme:black-highlighter-theme]]@@` — the JP
Black Highlighter page's actual name, which carries no `-jp` suffix
— and the theme's own line to
`@@[[include :scp-jp:theme:telecommunications-monitoring-office-theme-jp]]@@`
(candidate L34–35), the candidate's exact posting name in long form.
This theme is not in the plain-slug sweep family. The frame and
credit includes are sections 0 and 1; there are no other includes.

**Why.** Pattern classes P2 (include repoints; KB-05) and P8
(exhibit fidelity; KB-42, KB-43). Failure prevented: an install
snippet pointing at the origin branch installs the wrong pages, and
a snippet naming a short form that will not be posted installs
nothing.

**Verify.** `sed -n '33,36p' candidate.txt` against original
L16–19.

**Disposition.** No ledger line charges the repoints. The (b)
verdict is PASS.

## 3. Delivery topology (P4)

**What.** The original delivers in two pieces: a head module
importing the Black Highlighter base from the EN project's GitHub
Pages (`nu-scptheme.github.io/Black-Highlighter/stable/styles/…`,
original L3–6), and a tail module importing its own exhibit's code
from the wiki (`https://scp-wiki.wikidot.com/theme:telecommunications-monitoring-office-theme/code/1`,
original L61–63). The candidate repoints the base to the JP
project's GitHub Pages (`scp-jp.github.io/Black-Highlighter/css/min/…`)
in the head module (candidate L1–4, block B1, DELIVERY-HOST) and in
both frame slots (section 0) — the JP BHL port is the base this
candidate will actually be posted beside. For its own layer, the
candidate replaces the tail code-URL import with an inline module
carrying the CSS itself (candidate L79–115, block B15,
DELIVERY-MOVE), textually identical to the source exhibit above it
(candidate L40–75) — the same inline-delivery form the Basalt-layer
ports in this batch use. The exhibit is retained as documentation.

**Why.** Pattern class P4 (delivery topology; KB-23). Failure
prevented: a base imported from the EN project's Pages is the EN
BHL build, not the JP port whose variables and fixes the JP site
runs; and a self-import through the wiki code URL is the fragile
half of the original's topology (it depends on the exhibit's
position in the page).

**Verify.** `sed -n '1,4p' candidate.txt` and
`sed -n '79,82p' candidate.txt`;
`grep -n 'nu-scptheme\|code/1' candidate.txt` returns nothing;
`diff <(sed -n '40,75p' candidate.txt) <(sed -n '81,115p' candidate.txt)`
shows the exhibit and the module carrying the same CSS apart from
the module's heading comment (section 10).

**Disposition.** Ledger part (c3) records this theme's row charges
dispositioned under the class outcomes (header language = ruling 2;
asset hosts = class (ii); credit fields FIXED). No line charges the
topology itself. The (b) verdict is PASS.

## 4. Fonts and assets (P5, P7)

**What.** The theme imports no fonts of its own on either side; the
BHL base supplies the faces, so there is no P7 event in this pair.
The one asset is the header logo. The original's `--logo-image`
names it over plain HTTP on the wiki host
(`http://scp-wiki.wikidot.com/local--files/theme:telecommunications-monitoring-office-theme/TMO%20Logo%20Battle.png`,
original L36). The candidate names the JP storage copy
(`https://scp-jp-storage.wdfiles.com/local--files/file%3A5384396-443-cuyh/TMOwhite.png`,
candidate L53 and L93, blocks B10 and B15, ASSET-REHOST ×2) — the
white variant of the logo, hosted under a file-ID path on the JP
project's storage wiki. Probed once on 2026-11-17, it answers 200:
the file is uploaded and serving, so this repoint is complete, not
deferred.

**Why.** Pattern class P5 (assets; KB-25, KB-26). Failure prevented:
a logo loaded over HTTP from the origin wiki is both a mixed-content
risk and outside the port's control; the JP storage copy is the
campaign's own hosting for exactly this.

**Verify.** `grep -n 'logo-image' candidate.txt`;
the probe result above can be re-run with one `curl -sI` against
the candidate's URL.

**Disposition.** Ledger part (c3) records asset hosts for this theme
as class (ii). The (b) verdict is PASS.

## 5. Header, titles and rendered strings (P6)

**What.** The variable block sets two reader-visible strings, both
translated: `--theme-name: "電気通信監視室テーマ"` (candidate L49;
block B9, CONTENT-STRING — the companion `--theme-id` at L47 keeps
its machine value `telecommunications-monitoring-office-theme`
unchanged, correctly, since the base keys on it) and
`--header-subtitle: "電気通信監視室"` (candidate L54; blocks B10 and
B15, HEADERVAR ×2), from the original's "Telecommunications
Monitoring Office Theme" and "Telecommunications Monitoring
Department". The subtitle's JP form shortens "Department" away;
that is a wording choice inside the translated string.

**Why.** Pattern class P6 (header and rendered strings; KB-29,
KB-30, KB-31). Failure prevented: a JP page rendering an EN subtitle
in its masthead because its variable block kept the origin strings.

**Verify.** `grep -n 'theme-name\|header-subtitle' candidate.txt`.

**Disposition.** Ledger part (c3) dispositions this theme's header
language under ruling 2 (header/title language is out of scope for
migration correctness). The translation stands under that
disposition; nothing else in this section is charged.

## 6. Body translation (P10)

**What.** Everything reader-visible is translated: the two prose
paragraphs (blocks B4, B6), the usage instructions, and — the bulk of
the heuristic mass — the CSS comments inside the variable block,
which are the S-CSS-P integration instructions a theme author reads
(blocks B7–B13, COMMENT-TEXT ×8 with TRANS-UNANCHORED ×9 across the
pair): the section markers （統合 / ヘッダー要素 / 標準テーマカラー /
ヘッダーグラデーション / 主要グラデーション） and the per-variable
guidance comments all read in Japanese in both the exhibit and the
delivered module. The variable values themselves (the accent colour
183, 18, 52 in five places, the rules for `h3,h6` and `.blockquote`)
cross unchanged.

**Why.** Pattern class P10 (translation; KB-50, KB-51). Failure
prevented: untranslated documentation — here including the
author-facing instructions embedded in the CSS — makes the
candidate unusable as a JP theme page.

**Verify.** `sed -n '40,75p' candidate.txt` against original
L23–57; `grep -n 'S-CSS-P' candidate.txt` shows the translated
marker in both copies.

**Disposition.** T4/T5 judged this theme FINDINGS jointly, on the
credit nits of section 1 only; no translation finding stands. The
(b) verdict is PASS.

## 7. Link targets (P11)

**What.** The candidate's only links are the credit source link
(section 1, the recorded origin host — correct for a source link),
the author user-links (`[[*user BattleblockB0ss]]`, candidate L23
field and L29 prose), and the usage exhibits (section 2). No prose
link targets the origin branch as navigation, and there are no hub
or component links to repoint.

**Why.** Pattern class P11 (link targets; KB-54). The class has no
defect instance here; the ground is the full read of a 115-line
file, in which every link is accounted for above.

**Verify.** `grep -n 'http' candidate.txt` — the hits are the
delivery imports, the logo, and the credit source link.

**Disposition.** No ledger line charges a link target for this
theme.

## 8. Structural fidelity and exhibit census (P8, R3)

**What.** The census is the whole page, and it is preserved: prose,
usage snippet, code exhibit, in the original's order. Two form
changes, both recorded here. First, the delivery module inlines the
CSS where the original imported it (section 3). Second — the
repair — the original's code exhibit never closes its
`@supports(display: grid)` block: a brace-depth scan of
`original.txt` ends at depth 1 (the `:root` block closes at
original L49; the `@supports` opened at L24 does not). CSS parsers
auto-close at end of file, so the original renders, but the
structure is defective as written. The candidate adds the missing
closing brace at the end of both copies (candidate L74 in the
exhibit, L114 in the module; block B14, labeled CSS-BODY), and a
depth scan of `candidate.txt` ends at 0 with no negative dips. The
added brace changes no rule's meaning: every rule the original
effectively placed inside the `@supports` remains inside it.

**Why.** Pattern class P8 (structural fidelity; KB-42, KB-43), and
the brace-depth rule: balance is a depth property, not a count
property — here the counts themselves already disagreed, and the
scan is the deciding check either way. Failure prevented: a port
that copies a latent structural defect into both its exhibit and
its delivered CSS, where a future edit appending rules after the
block would silently change which rules the `@supports` governs.

**Verify.** The depth scan is five lines of Python over either file
(open/close brace delta per line, cumulative); re-run it against
`original.txt` and `candidate.txt` in this package.

**Disposition.** No ledger line charges the structure — the checks
do not scan for this, and T1 passes the candidate. The repair is
recorded here and in the per-theme record (item 1) so it is not
mistaken for drift.

## 9. Formatting-only changes (R4)

**What.** None. The classifier reports no whitespace-only block and
no re-indentation block for this pair. The size delta (+78 / −26) is
content: the credit block, the frames, and the inlined delivery
module on the added side; the bare rate and the code-URL import on
the removed side.

**Why.** Residue class R4 has no instance here; the ground is the
classifier's zero counts for both signatures across 15 blocks.

**Verify.** `grep -c 'WS-ONLY' classification.json` returns 0.

**Disposition.** Nothing to disposition.

## 10. Porter annotations (R2)

**What.** One annotation, in CSS-comment form: the delivered
module's heading comment (candidate L80) —
「電気通信監視室テーマ — SCP-JP版。以下のコードは、上記のコード表示と同一です。」
("Telecommunications Monitoring Office theme — SCP-JP edition. The
code below is identical to the code exhibit above."). It is the
in-file explanation of the section-3 duplication (exhibit plus
inline module), and it is accurate: the two copies match. The
candidate contains no `[!-- --]` comments.

**Why.** Residue class R2 (porter annotations). This one is
load-bearing documentation for the delivery form: without it, the
duplicated CSS reads as an accident.

**Verify.** `sed -n '80p' candidate.txt`;
`grep -c '\[!--' candidate.txt` returns 0.

**Disposition.** No ledger line charges the annotation.

## 11. Dispositioned deviations (class (ii) / (iii) summary)

**What.** The deviations a reader of the diff might otherwise charge
against the candidate, with their dispositions:

- T1 passes this candidate outright (T1-ROWS row 164: exit 0,
  0 errors, 0 warnings, 1 info) — the only T1 PASS in this batch,
  and there is nothing to disposition.
- The render check's items (RENDER-ROWS-2, EN20) are DISPOSITIONED
  in ledger part (c2): for the page, the runtime-hotlink site-theme
  chain only (KB-40, environment layer — the runtime hosts arrive
  via the shared site theme chain, not the candidate); for the
  sample, a hidden rate widget in all 8 engine/viewport
  combinations plus the same chain, recorded under the same
  environment-layer entry. No overflow and no credit-modal item is
  recorded for this theme.
- The credit nits are dispositioned under the staff-normalization
  class (section 1); the header language under ruling 2 and the
  asset host under class (ii) (sections 4–5).

**Why.** These classes exist so a reviewer does not re-litigate
environment properties as candidate defects; each item above names
its record so the disposition can be re-checked at its source.

**Verify.** The theme's rows in `review/AUTHORITIES/ledger-parts/`
(T1-ROWS row 164, RENDER-ROWS-2) and its blocks in
`GOSIGN2-LEDGER.md` part (c2) and the supplement.

**Disposition.** All items above are DISPOSITIONED in the cited
records. No defect flag stands against this candidate.

## 12. Verification history

**What.** T1 (source check): PASS, exit 0 — T1-ROWS row 164.
T2/T3 (render check): FINDINGS, both items dispositioned in (c2) —
RENDER-ROWS-2 (EN20). T4/T5 (localize check): FINDINGS on the
credit-notation nits only — LOCALIZE-ROWS row 144 (LOCALIZE-S2-C);
the row's display-affecting column counts 1 while its own text
states "No display-affecting findings", a count-versus-text
mismatch in the vendored row that the supplement's disposition
(nits, staff-normalization class) resolves in favour of the text.
Ledger part (c3) records the row charges dispositioned under the
class outcomes. The (b) verdict is PASS (row 144: T1 PASS, the
other checks FINDINGS, overall PASS), with no OPEN items and no
FIX5 re-judgement.

**Why.** The verification section exists so the reader can see which
checks ran, what they found, and what became of each finding,
without re-running the campaign.

**Verify.** The cited rows; the stamp at the head of this file is
generated from the same records by `review/build_review.py`.

**Disposition.** Verdict: PASS (go-sign ledger part (b)).

## Per-theme record: telecommunications-monitoring-office-theme-jp

**Item 1 — the `@supports` brace repair (repair, recorded).** The
original exhibit's `@supports` block is unclosed (depth scan ends
at 1); the candidate closes it in both CSS copies (candidate L74,
L114; depth scan ends at 0). No rule changed meaning. Recorded in
section 8 so the added brace is not mistaken for drift, and so a
future editor knows the original's form was defective rather than
idiomatic.

**Item 2 — the naming split (record note).** The campaign's records
key this theme two ways: sources.tsv's candidate slug and ledger
part (b) use the short form `theme:telecom-office-theme-jp`; the
canonical file, the other ledger parts, and this package use the
long form. The ledger's population check records the alias
normalization, so the verdict attaches to the right theme; but the
split has one visible tooling consequence in this package — the
skeleton README generated for this package carried no verdict stamp
(the generator's lookup missed the alias), and the stamp above was
written in the standard format by hand. If `build_review.py --check`
later regenerates stamps under a single key, this package's stamp
should be re-checked then.

## Change set

Delivered with this candidate in the canonical repository: the
candidate page itself
(`pages/theme:telecommunications-monitoring-office-theme-jp.txt`)
and its decoration sample
(`pages/theme-decoration-sample-telecom-office-theme-jp.txt`). The
candidate's own history is two commits: the Stage 2 EN20 integration
and the FIX-CREDIT-D normalization.

## Appendix: residue resolution

The classifier left 2 blocks unlabeled (13.3%). Per the class-M
convention they are resolved here by shape, one row per block.

| Block | Lines (orig → cand) | Resolution |
|---|---|---|
| B2 | 8–10 → 6–9 | The original's bare-rate div (`[[>]]` / lowercase `[[module rate]]` / `[[/>]]`) is deleted; the candidate lines at the paired position are the priority-1 frame. The classifier's rate signature expects the capitalised form and did not fire (section 1, P3). |
| B3 | 12 → 11–14 | Alignment artifact at the frame insertion: the original's author-prose line pairs with the inserted priority-2 frame lines; the prose line's translation stands at candidate L29 inside block B4's span (sections 0, 6). |
