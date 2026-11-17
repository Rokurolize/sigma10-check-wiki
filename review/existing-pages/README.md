# Collapsed-form records — existing production pages (`pages-existing/`)

**Date:** 2026-11-17
**Brief:** `lane-oc-existing/BRIEF.md` (TASK). Scope source: campaign root R
`review-scout/SITE-SCOPE.md`, section "Existing production pages
(pages-existing/, 153 records)" and the per-kind shape table (rows
"Existing production theme page / component page / Old record").
**Canonical repo:** sigma10-check-wiki worktree at commit `01eea37`
(the current lane directory). Deliverable: this file, `review/existing-pages/README.md`
— a new, **uncommitted** file (the coordinator harvests per-file; no commit, no push).
**No checker, render or reflect step applies.** This is a records-build task: it reads
`pages-existing/`, `review/sources.tsv`, the package READMEs and `start-themes.tsv`
and emits one directory with one README. No candidate source is edited, no page is
reflected to either check wiki, and no diff is fabricated.

## The standing note (part 4 of the four-part standard, collapsed)

These 153 records are the production SCP-JP pages with the `テーマ` tag that the
campaign imported into `pages-existing/` on 2026-11-14 (`existing:index.txt` L7,
L13–15 states the acquisition date, the identity of each imported source, and that
Wikidot is the reference while Wikijump is the verification target). They are **not
ported**: at migration the page source does not change; only the environment that
renders it changes, and that record is already kept on a different axis in
`start:wikijump-parity` (SITE-SCOPE.md §"Existing production pages", L100–123).

Per part, for every one of these pages:

- **Part 1 (mirror of the original at the reference revision) — already
  satisfied.** `pages-existing/` *is* the mirror: each `existing:<fullname>.txt`
  was imported byte-identically from the live production page, by construction
  (`existing:index.txt` L14: 「各ページのソースは本番と同一です（`existing:`
  カテゴリへ取り込み）」; SITE-SCOPE.md L108–109: "pages-existing/ IS the mirror,
  byte-identical to production by construction"). No separate mirror file is owed.
- **Part 2 (ported candidate source) — does not apply.** There is no candidate for
  these pages; each continues as itself in the Sigma-10 environment. Where an
  existing theme page is also the production counterpart of a theme-row candidate,
  the real candidate lives in that row's package (SITE-SCOPE.md L111–114); the
  cross-reference column below points to it. That is a pointer, not a part-2
  artifact for this record.
- **Part 3 (readable diff) — does not apply.** Identity is by construction: a diff
  of the mirror against itself is empty. Emitting an empty diff file would falsely
  suggest that a port had been reviewed (SITE-SCOPE.md L115–116). None is created.
- **Part 4 (explanation) — collapses to this note plus the cross-references in the
  table below**, with the parity record living in `start:wikijump-parity`
  (SITE-SCOPE.md L117–121). Where a page served as a supplement source for a
  candidate (e.g. `existing:theme-3law` for FIX4-CREDIT), that citation lives inside
  the theme package that used it, not here; the cross-reference column names the
  package and the line.

A per-kind shape reading of the same four parts is in SITE-SCOPE.md's per-kind
shape table (L130–139): parts 2 and 3 are `N/A` for all three existing-page kinds
and part 4 is `COLLAPSED`. No per-page packages and no diff files are produced —
this single README is the whole record set.

## Count verification (from the listing itself)

Enumerated `pages-existing/*.txt` (154 files) and classified each by the namespace
prefix of its filename stem:

| Class | Count |
|---|---|
| `theme-` (existing theme pages) | 126 |
| `component-` (existing component pages) | 20 |
| `old-` (legacy records) | 7 |
| **Total records** | **153** |
| `existing:index.txt` (import manifest, **not a record**) | 1 |

**126 + 20 + 7 = 153.** This agrees with `existing:index.txt` L13 (「対象 …
153件」) and its per-section headers L17 / L147 / L171 (126 / 20 / 7) and with
SITE-SCOPE.md L102–103. `existing:index.txt` is the import manifest / hub for the
153 records; it is listed here for completeness but is **not** one of the records.

## How to read the cross-reference column

Three values, exactly as the brief specifies:

1. `review/<dir>/ — production counterpart of <candidate>` — the page is the JP
   production counterpart of a candidate; the real review record is that theme-row
   package. The join is `production fullname == sources.tsv orig_fullname`, with the
   on-disk package directory resolved against `review/` (two packages are stored
   without the `-jp` suffix: `min-theme`, `shushuin`; and `quand-le-soleil-se-couche`
   keeps its unsuffixed name); `old:theme:basalt` is keyed by `basalt-jp` per
   `start-themes.tsv` and `review/basalt-jp/README.md`.
2. A **supplement-source / source citation** naming the package README (with line
   numbers) inside which the page was used as a source (e.g. FIX4-CREDIT credit
   CSS). A page that is both a counterpart and a supplement source shows the
   counterpart first and the second role appended after a semicolon.
3. `no theme row; parity record only` — neither applies: no theme-row review
   package in this repo cites the page as a counterpart or as a source. Its only
   record is its Wikijump reproduction state in `start:wikijump-parity`.

The 7 `old-` records are additionally marked **legacy — no action** (SITE-SCOPE.md
L122–123); the one cited inside a package (`old-theme-basalt` in `basalt-jp`) carries
that citation as a note, with no migration action.

**Cross-reference tally (machine-extracted from the table below):** 29
theme pages are production counterparts; 3 are supplement/source-only
citations; 114 have no theme row (parity record only); 7 are legacy
old records — **29 + 3 + 114 + 7 = 153**.

**Scope note on the posted-theme count.** AGENTS.md §1 describes 44 posted themes,
but the repo's own `start-themes.tsv` `exist` column and `sources.tsv` notes record
only **30** /start rows whose production page exists (25 `match` variants —
24 plain `match` + 1 re-measured — and 5 `mismatch` variants). Of those 30,
29 are the theme-page counterparts below and 1 is
`old:theme:basalt`. This is recorded as a repo-vs-brief discrepancy per the
"judge from this repo" rule; it does not change any of the 153 records.

## Full record table (153 records)

| Fullname | Kind | Cross-reference |
|---|---|---|
| `existing:component-abyssal-light-theme` | component | no theme row; parity record only |
| `existing:component-af2017theme` | component | no theme row; parity record only |
| `existing:component-af2018theme` | component | no theme row; parity record only |
| `existing:component-af2019theme` | component | no theme row; parity record only |
| `existing:component-af2020theme` | component | no theme row; parity record only |
| `existing:component-af2021theme-source` | component | no theme row; parity record only |
| `existing:component-af2021theme` | component | no theme row; parity record only |
| `existing:component-af2022theme` | component | no theme row; parity record only |
| `existing:component-af2023theme` | component | no theme row; parity record only |
| `existing:component-af2024theme` | component | no theme row; parity record only |
| `existing:component-af2026theme` | component | no theme row; parity record only |
| `existing:component-black-highlighter-theme-dev` | component | no theme row; parity record only |
| `existing:component-cc-theme` | component | no theme row; parity record only |
| `existing:component-darkbodytheme` | component | no theme row; parity record only |
| `existing:component-i57theme` | component | no theme row; parity record only |
| `existing:component-ny21` | component | no theme row; parity record only |
| `existing:component-oem` | component | no theme row; parity record only |
| `existing:component-theme-saint-patrick` | component | no theme row; parity record only |
| `existing:component-theme` | component | no theme row; parity record only |
| `existing:component-thewayitendstheme` | component | no theme row; parity record only |
| `existing:old-component-ijamea-theme` | old (legacy) | legacy — no action |
| `existing:old-component-mcf-theme` | old (legacy) | legacy — no action |
| `existing:old-component-newscptheme` | old (legacy) | legacy — no action |
| `existing:old-component-resurrection-theme` | old (legacy) | legacy — no action |
| `existing:old-component-spc-theme-2` | old (legacy) | legacy — no action |
| `existing:old-component-spc-theme` | old (legacy) | legacy — no action |
| `existing:old-theme-basalt` | old (legacy) | legacy — no action; cited as the production adaptation source (iti119) in `review/basalt-jp/README.md` L74,L186 — record source only |
| `existing:theme-3law-7ow` | theme | no theme row; parity record only |
| `existing:theme-3law` | theme | supplement source — FIX4-CREDIT credit-module CSS (T7) carried from `pages-existing/existing:theme-3law.txt` L356-365; cited in `review/3law-pride-jp/README.md` L78,L80,L184 and `review/3lawcracked-jp/README.md` L79,L81,L185 |
| `existing:theme-81uo` | theme | no theme row; parity record only |
| `existing:theme-ad-abyssum` | theme | no theme row; parity record only |
| `existing:theme-ad-astra` | theme | no theme row; parity record only |
| `existing:theme-aero-glass` | theme | source cited inside `review/cobalt-aero-glass-jp/README.md` (L3,L49,L60,L86,L132) as the production base page / record source the candidate's `theme:aero-glass` include resolves to; no `theme:aero-glass-jp` candidate exists |
| `existing:theme-aesthetic-theme` | theme | `review/aesthetic-theme-jp/` — production counterpart of `theme:aesthetic-theme-jp` |
| `existing:theme-aonibiiro-theme` | theme | no theme row; parity record only |
| `existing:theme-ar` | theme | no theme row; parity record only |
| `existing:theme-beyondentropy-theme` | theme | no theme row; parity record only |
| `existing:theme-black-highlighter-theme` | theme | `review/black-highlighter-theme-jp/` — production counterpart of `theme:black-highlighter-theme-jp`; also cited as the production BHL base in `review/walk-in-the-dark-jp/README.md` L100 |
| `existing:theme-black-highlightyear` | theme | no theme row; parity record only |
| `existing:theme-blankstyle` | theme | `review/blankstyle-jp/` — production counterpart of `theme:blankstyle-jp` |
| `existing:theme-broken-masquerade` | theme | no theme row; parity record only |
| `existing:theme-calamity` | theme | no theme row; parity record only |
| `existing:theme-calibri-logos` | theme | no theme row; parity record only |
| `existing:theme-classic` | theme | `review/classic-jp/` — production counterpart of `theme:classic-jp` |
| `existing:theme-cosmonaut` | theme | `review/cosmonaut-jp/` — production counterpart of `theme:cosmonaut-jp` |
| `existing:theme-creepypasta` | theme | no theme row; parity record only |
| `existing:theme-crocker-theme` | theme | no theme row; parity record only |
| `existing:theme-cs-theme` | theme | no theme row; parity record only |
| `existing:theme-cyberpunk` | theme | no theme row; parity record only |
| `existing:theme-darkcode` | theme | no theme row; parity record only |
| `existing:theme-deception-theme` | theme | no theme row; parity record only |
| `existing:theme-department-of-tombstone` | theme | no theme row; parity record only |
| `existing:theme-department-of-traces` | theme | no theme row; parity record only |
| `existing:theme-deus-ex-machina` | theme | no theme row; parity record only |
| `existing:theme-dialogue-department` | theme | no theme row; parity record only |
| `existing:theme-dira-theme` | theme | no theme row; parity record only |
| `existing:theme-disrememberment-theme` | theme | no theme row; parity record only |
| `existing:theme-dmam` | theme | no theme row; parity record only |
| `existing:theme-dustjacket-sigma` | theme | no theme row; parity record only |
| `existing:theme-dustjacket` | theme | no theme row; parity record only |
| `existing:theme-elma` | theme | no theme row; parity record only |
| `existing:theme-expose` | theme | no theme row; parity record only |
| `existing:theme-extra-black-highlighter-theme` | theme | `review/extra-black-highlighter-theme-jp/` — production counterpart of `theme:extra-black-highlighter-theme-jp` |
| `existing:theme-flopstyle` | theme | `review/flopstyle-jp/` — production counterpart of `theme:flopstyle-jp` |
| `existing:theme-foundless` | theme | no theme row; parity record only |
| `existing:theme-foxtrot` | theme | `review/foxtrot-jp/` — production counterpart of `theme:foxtrot-jp` |
| `existing:theme-fusouki-theme` | theme | no theme row; parity record only |
| `existing:theme-goc` | theme | no theme row; parity record only |
| `existing:theme-hansarp` | theme | `review/hansarp-jp/` — production counterpart of `theme:hansarp-jp` |
| `existing:theme-horizon-initiative-theme` | theme | no theme row; parity record only |
| `existing:theme-hytoth` | theme | no theme row; parity record only |
| `existing:theme-ijamea-bhl` | theme | no theme row; parity record only |
| `existing:theme-int-bhl` | theme | no theme row; parity record only |
| `existing:theme-isolated-terminal` | theme | `review/isolated-terminal-jp/` — production counterpart of `theme:isolated-terminal-jp` |
| `existing:theme-jakstyle` | theme | `review/jakstyle-jp/` — production counterpart of `theme:jakstyle-jp` |
| `existing:theme-joicl-catalog-theme` | theme | no theme row; parity record only |
| `existing:theme-kamikase` | theme | no theme row; parity record only |
| `existing:theme-kamiyotugi` | theme | no theme row; parity record only |
| `existing:theme-kyouikaireki` | theme | no theme row; parity record only |
| `existing:theme-linkage` | theme | no theme row; parity record only |
| `existing:theme-logos` | theme | no theme row; parity record only |
| `existing:theme-magnus-web-format` | theme | no theme row; parity record only |
| `existing:theme-manhattan-crisis` | theme | no theme row; parity record only |
| `existing:theme-mcd-gray` | theme | no theme row; parity record only |
| `existing:theme-mcd` | theme | no theme row; parity record only |
| `existing:theme-memoria` | theme | no theme row; parity record only |
| `existing:theme-midnight-rush` | theme | no theme row; parity record only |
| `existing:theme-min-theme` | theme | `review/min-theme/` — production counterpart of `theme:min-theme-jp` |
| `existing:theme-minimal` | theme | no theme row; parity record only |
| `existing:theme-minimalist-bhl` | theme | `review/minimalist-bhl-jp/` — production counterpart of `theme:minimalist-bhl-jp` |
| `existing:theme-monotypical` | theme | `review/monotypical-jp/` — production counterpart of `theme:monotypical-jp` |
| `existing:theme-much-cool` | theme | `review/much-cool-jp/` — production counterpart of `theme:much-cool-jp` |
| `existing:theme-mujin-getsudo` | theme | no theme row; parity record only |
| `existing:theme-nebulae` | theme | no theme row; parity record only |
| `existing:theme-neo-linkage` | theme | no theme row; parity record only |
| `existing:theme-new-age` | theme | no theme row; parity record only |
| `existing:theme-newspaper` | theme | no theme row; parity record only |
| `existing:theme-newtouhei` | theme | no theme row; parity record only |
| `existing:theme-night-rush-theme` | theme | `review/night-rush-theme-jp/` — production counterpart of `theme:night-rush-theme-jp` |
| `existing:theme-ouroborous-theme` | theme | `review/ouroborous-theme-jp/` — production counterpart of `theme:ouroborous-theme-jp` |
| `existing:theme-pacom` | theme | no theme row; parity record only |
| `existing:theme-paperstack` | theme | `review/paperstack-jp/` — production counterpart of `theme:paperstack-jp` |
| `existing:theme-pataphysics` | theme | `review/pataphysics-jp/` — production counterpart of `theme:pataphysics-jp` |
| `existing:theme-penumbra-bhl` | theme | no theme row; parity record only |
| `existing:theme-penumbra` | theme | `review/penumbra-jp/` — production counterpart of `theme:penumbra-jp`; also supplement source — FIX4-CREDIT credit CSS (T7) from L758-772, cited in `review/the-other-side-jp/README.md` L90,L188,L201 |
| `existing:theme-pet` | theme | no theme row; parity record only |
| `existing:theme-placestyle` | theme | no theme row; parity record only |
| `existing:theme-plugsoft-theme` | theme | no theme row; parity record only |
| `existing:theme-plvs-vltra` | theme | no theme row; parity record only |
| `existing:theme-poor-foundation` | theme | no theme row; parity record only |
| `existing:theme-present-malice` | theme | no theme row; parity record only |
| `existing:theme-prom-labs-deepsea` | theme | no theme row; parity record only |
| `existing:theme-quand-le-soleil-se-couche` | theme | `review/quand-le-soleil-se-couche/` — production counterpart of `theme:quand-le-soleil-se-couche` |
| `existing:theme-redtape` | theme | `review/redtape-jp/` — production counterpart of `theme:redtape-jp` |
| `existing:theme-revised-ijamea-theme` | theme | no theme row; parity record only |
| `existing:theme-russian-art-hub` | theme | no theme row; parity record only |
| `existing:theme-scp-archive-sigma` | theme | no theme row; parity record only |
| `existing:theme-scp-archive` | theme | no theme row; parity record only |
| `existing:theme-scp-human-resources` | theme | `review/scp-human-resources-jp/` — production counterpart of `theme:scp-human-resources-jp` |
| `existing:theme-scp-jp-10th-anniv` | theme | no theme row; parity record only |
| `existing:theme-scp-offices-theme` | theme | `review/scp-offices-theme-jp/` — production counterpart of `theme:scp-offices-theme-jp` |
| `existing:theme-scp-trans-pride` | theme | no theme row; parity record only |
| `existing:theme-shushuin` | theme | `review/shushuin/` — production counterpart of `theme:shushuin-jp` |
| `existing:theme-shushusoin` | theme | no theme row; parity record only |
| `existing:theme-simple-black-theme` | theme | no theme row; parity record only |
| `existing:theme-simple-yonder` | theme | `review/simple-yonder-jp/` — production counterpart of `theme:simple-yonder-jp` |
| `existing:theme-sinano` | theme | no theme row; parity record only |
| `existing:theme-sotm` | theme | no theme row; parity record only |
| `existing:theme-space` | theme | `review/space-jp/` — production counterpart of `theme:space-jp` |
| `existing:theme-spc` | theme | no theme row; parity record only |
| `existing:theme-sushi-academia` | theme | no theme row; parity record only |
| `existing:theme-swirling-ashes` | theme | no theme row; parity record only |
| `existing:theme-taisho150` | theme | no theme row; parity record only |
| `existing:theme-technoblast` | theme | no theme row; parity record only |
| `existing:theme-teito-keizai` | theme | no theme row; parity record only |
| `existing:theme-thanatomania` | theme | no theme row; parity record only |
| `existing:theme-the-flowing-night-sky` | theme | no theme row; parity record only |
| `existing:theme-the-foundation-theme` | theme | no theme row; parity record only |
| `existing:theme-the-greatest-alley` | theme | no theme row; parity record only |
| `existing:theme-the-way-out` | theme | no theme row; parity record only |
| `existing:theme-touheisha` | theme | no theme row; parity record only |
| `existing:theme-toyoho-web` | theme | no theme row; parity record only |
| `existing:theme-turbo-vision` | theme | `review/turbo-vision-jp/` — production counterpart of `theme:turbo-vision-jp` |
| `existing:theme-unforgettable` | theme | no theme row; parity record only |
| `existing:theme-valravn` | theme | no theme row; parity record only |
| `existing:theme-wanderers` | theme | supplement source — FIX4-CREDIT credit-module CSS (T7) carried from `pages-existing/existing:theme-wanderers.txt` L153; cited in `review/travellers-book-jp/README.md` L58,L165 |
| `existing:theme-war-on-all-fronts-bhl` | theme | no theme row; parity record only |
| `existing:theme-war-on-all-fronts-sigma` | theme | no theme row; parity record only |
| `existing:theme-wilsons` | theme | no theme row; parity record only |
| `existing:theme-word-processor` | theme | no theme row; parity record only |
| `existing:theme-y2k` | theme | `review/y2k-jp/` — production counterpart of `theme:y2k-jp` |
| `existing:theme-yamisushi` | theme | no theme row; parity record only |
| `existing:theme-zattou` | theme | no theme row; parity record only |
