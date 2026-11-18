# sigma10-check-wiki — canonical sources for the Sigma-10 display-check composition

This repository is the single source of truth for the page sources of the
Sigma-10 display-check composition used by the SCP-JP theme-porting work:

- Wikidot check wiki: `sigma10-jp-test.wikidot.com`
- Wikijump check wiki: stafflab site 6000303 (`scp-jp-sigma10`), served at
  `https://codex-wsl-maintenance.tail3a09a5.ts.net:8443/`

For the shorthand used in the review packages (KB ids, P-numbers, T1–T5,
class (i)/(ii)/(iii), wave names), see
[`review/HOW-TO-READ.md`](review/HOW-TO-READ.md).

`pages/<fullname>.txt` holds the canonical text of each page (1,013 pages:
the `start` index and its eight generated table subpages, every theme
sample, the shared decoration body `theme-decoration-sample`, the locally
held theme pages, and the SCP sample pages; the imported existing articles
live under `pages-existing/`). The canonical text is the Wikidot-side text. The Wikijump side is the
same text after the environment transforms documented in `ALLOWLIST.md`
(entries A1 and A2, which apply only inside `theme-decoration-sample`), plus
at most a trailing-newline difference, which is not a difference.

## The discipline

1. **Edit here first.** A composition change starts as an edit to a file in
   this repository, committed like any other change.
2. **Then apply to both wikis in the same step** (Wikidot via the wikidot.py
   tooling, Wikijump via the Deepwell RPC page_edit route), so the mirrors
   never drift apart.
3. **Run `verify.py`** after applying. It fetches both wikis' current sources
   and fails if any page differs from this repository (modulo the ALLOWLIST
   transforms and the trailing-newline exemption). Drift means a wiki was
   edited out of band: reconcile it back into the repository deliberately,
   never by silently re-dumping one side over the other.

For `pages/start.txt` specifically: it is the canonical source of the top
page. Edit and commit here first, then reflect the same text to both wikis;
do not edit from the wiki side first. (This maintainer instruction used to
sit on the porter-facing top page; it belongs with the maintainers here.)

Before this repository existed, the same texts lived scattered across
campaign state directories (`muse-bhl/theme-sample-*`,
`theme-lab-playwright-factory/body.txt`, JSON dumps in the sigma10-unify and
theme-port-readiness records) and as the live wiki pages only. Those copies
are history; this repository supersedes them as the place to read or change
the composition.

## Authoring constraints learned from live Wikidot behavior

- **No block constructs inside `||` table cells.** A `[[collapsible]]` (or a
  similar block) written inside a table row is hoisted out of the table by
  Wikidot's parser: the collapsible's body spills as a plain paragraph after
  the table and the row's closing `||` renders as literal text. ftml breaks
  the same way. To combine the two, put the table inside the collapsible,
  never the collapsible inside a cell. (Measured on the live sandbox wiki,
  probe pages `muse-probe-cellcol-v1`…`v4`, 2026-11-14; this is why the
  decoration body's section-26 exhibit is shaped the way it is.)
- The decoration sample's exhibits are the grading surface for theme
  porting: a broken exhibit quietly degrades every theme's check. Keep
  exhibits in forms both engines render as intended, and re-check the
  rendered pages (not only the sources) after any body edit.

## The /start index is split, and its theme table is generated

`pages/start.txt` is a hub: the introduction, how to read the tables,
the table of contents, the site-operations wikis and the comparison
references. The 287-row theme table lives on ten subpages
(`start:themes-jp`, `start:themes-en-1` to `start:themes-en-4`,
`start:themes-cn-1` to `start:themes-cn-3`, `start:themes-ko`,
`start:themes-fr`), grouped the way a reader looks a theme up: by the
branch the theme was created in (its origin), in sample-slug order
within a subpage. A theme posted on SCP-JP as a translation sits in its
origin branch's table; whether it is posted is per-row information.

The same generator also renders `start:wikijump-parity`, the Wikijump reproduction ledger for the 153 existing articles (kept separate from the theme tables: the tables carry porting/migration state, the ledger is the secondary Wikijump verification record). The subpages are generated. Their source of truth is `start-themes.tsv`
(one line per row: name, the three status fields, base, reference
revision, existing page, sample slugs). To change a row, edit the TSV
and run:

    python3 build_start.py

then commit the TSV, the regenerated subpages and any hub edit together.
`python3 build_start.py --check` fails if a subpage differs from the
TSV, if a table is not one contiguous block of `||` lines (a blank line
inside a Wikidot table splits it), or if a subpage exceeds 40,000
characters. Do not edit the `start:themes-*` files by hand. The wave data
itself is untouched in `start-themes.tsv` — the generator only renders it
in plain words (integration-wave codes and the retired Check 5 outcome are
not shown in rows).

## Scope notes

- Pages mirrored from other wikis (the `theme:` copies of SCP-Wiki / SCP-JP /
  other branches held on the check wikis) are snapshots for the check; their
  upstream is the named home wiki, recorded in the theme-port ledger.
- Titles and tags are page metadata, not source text; they are graded and
  recorded in the theme-port-readiness ledger, not in this repository.
