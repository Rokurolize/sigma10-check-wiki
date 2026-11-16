# sigma10-check-wiki — canonical sources for the Sigma-10 display-check composition

This repository is the single source of truth for the page sources of the
Sigma-10 display-check composition used by the SCP-JP theme-porting work:

- Wikidot check wiki: `sigma10-jp-test.wikidot.com`
- Wikijump check wiki: stafflab site 6000303 (`scp-jp-sigma10`), served at
  `https://codex-wsl-maintenance.tail3a09a5.ts.net:8443/`

`pages/<fullname>.txt` holds the canonical text of each page (122 pages: the
`start` index, every theme sample, the shared decoration body
`theme-decoration-sample`, the locally held theme pages, and the SCP sample
pages). The canonical text is the Wikidot-side text. The Wikijump side is the
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

`pages/start.txt` is a hub (about 13,000 characters): the introduction,
how to read the tables, the table of contents, the existing articles
without a theme row, the site-operations wikis and the comparison
references. The 287-row theme table lives on seven subpages
(`start:themes-stage1`, `start:themes-en-1` to `start:themes-en-3`,
`start:themes-cn-1` to `start:themes-cn-2`, `start:themes-ko`; about
21,000 to 26,000 characters each), grouped the way a reader looks a theme
up: the 44 themes posted on real SCP-JP first, then the unposted
originals by branch (EN, CN, KO), in sample-slug order within a subpage.

The subpages are generated. Their source of truth is `start-themes.tsv`
(one line per row: name, the three status fields, base, reference
revision, existing page, sample slugs). To change a row, edit the TSV
and run:

    python3 build_start.py

then commit the TSV, the regenerated subpages and any hub edit together.
`python3 build_start.py --check` fails if a subpage differs from the
TSV, if a table is not one contiguous block of `||` lines (a blank line
inside a Wikidot table splits it), or if a subpage exceeds 40,000
characters. Do not edit the `start:themes-*` files by hand.

## Scope notes

- Pages mirrored from other wikis (the `theme:` copies of SCP-Wiki / SCP-JP /
  other branches held on the check wikis) are snapshots for the check; their
  upstream is the named home wiki, recorded in the theme-port ledger.
- Titles and tags are page metadata, not source text; they are graded and
  recorded in the theme-port-readiness ledger, not in this repository.
