# ALLOWLIST — differences accepted between the two check wikis

Scope: CRITERIA.md Check 2 (source agreement). A difference that is not listed here is a Check-2 failure. Every entry names the exact difference and the environment reason.

Wikidot side: `sigma10-jp-test` (archive of the check composition, read live 2026-11-14).
Wikijump side: stafflab site 6000303 `scp-jp-sigma10` (read live 2026-11-14).

Comparison basis: all 121 pages that exist on both wikis (`source_diff.json`; 79 sample pages, 40 local theme pages, `start`, and `scp-002-j`), compared after CRLF normalisation. 6 pairs differ in content; 9 more pairs differ only by end-of-file newlines, which CRITERIA.md already excludes and which are therefore not entries.

## A1 — Attachment host in the sample body's image URLs

Status: allowed. Environment-forced.

Exact difference, in `theme-decoration-sample` (the shared decoration body included by every sample), 10 occurrences:

- Wikidot: `https://sigma10-jp-test.wdfiles.com/local--files/theme-decoration-sample/test-image.png` and `https://sigma10-jp-test.wdfiles.com/local--files/theme:basalt/basalt-theme-logo.svg`
- Wikijump: `https://scp-jp-sigma10.wjfiles.localhost:28443/local--files/theme-decoration-sample/test-image.png` and `https://scp-jp-sigma10.wjfiles.localhost:28443/local--files/theme:basalt/basalt-theme-logo.svg`

Reason: each wiki serves its own attachments from its own file host, and the file host plus its port is deployment configuration (Wikidot `*.wdfiles.com`; Wikijump `*.wjfiles.localhost:<port>`). The referenced bytes are identical on both sides, so this is a host rename, not a content change:

- `test-image.png` sha256 `dc394cf4ae2aea29d9958a1e36246b6683c196ebb107a7e26e2c93973612eba8` (41,658 bytes) on both.
- `basalt-theme-logo.svg` sha256 `3baf62c62621629c69f22433651572da5fd917e276e5953ae4eebd75b7ca99b2` (5,451 bytes) on both.

Evidence: `evidence/allowlist/image-hosts.txt`, `source_diff.json` (`theme-decoration-sample`).

## A2 — Credit author user link in the sample body

Status: allowed. Environment-forced by account namespaces.

Exact difference, in `theme-decoration-sample`, 3 occurrences:

- Wikidot: `**著者:** [[*user voted-fated-smuggler]]` (and `= Written by [[*user voted-fated-smuggler]]` in the info-module exhibit)
- Wikijump: `**著者:** [[*user daveyoufool]]` (and `= Written by [[*user daveyoufool]]`)

Reason: Wikidot accounts are global and both names exist there (user ids 2034230 and 10382659); Wikijump site 6000303 has an imported user record only for `daveyoufool` (user_id −21) and none for `voted-fated-smuggler`, so `[[*user voted-fated-smuggler]]` renders on Wikijump as a non-existent user while the exhibit needs an existing one. The account namespace cannot be mirrored by editing page text; the sample uses an account that exists in each environment.

Evidence: `evidence/allowlist/user-accounts.txt`; rendered user markup in `evidence/*/wikidot-*.html` and `evidence/*/wikijump-*.html`.

## Explicitly not a difference (no entry needed)

- One missing final newline at end of file on `start`, `theme:basalt-jp`, `theme:classic-jp`, `theme:dear-dictator-jp`, `theme:flopstyle-dark-jp`, `theme:hansarp-jp`, `theme-decoration-sample-flopstyle`, `theme-decoration-sample-min-theme`, `theme-decoration-sample-scp-human-resources` (Wikidot strips the trailing newline on save). CRITERIA.md Check 2 excludes trailing-whitespace-only differences.
- Site-name suffix in `<title>` and per-wiki chrome (favicon, edit links, footer) — environment chrome, not page content.
- Time-varying values: ratings, view counts, avatar URLs' `timestamp` parameter, dates.
- Wikijump renders `[[*user staff.operator]]` with different not-found wording than Wikidot. The difference is in software-generated text, not page text; it is recorded as a rendering difference in LEDGER.md defect D8, not as a source difference.

## Known differences that are NOT allowlisted (Check-2 failures, page-side)

These are real, non-environment differences and stay failures until the page text is aligned on both wikis:

- `theme-decoration-sample-blankstyle`: Wikidot `[[include :scp-jp:theme:blankstyle]]` vs Wikijump `[[include theme:blankstyle]]`.
- `theme-decoration-sample-halloween`: Wikidot `[[include :scp-wiki:theme:halloween]]` vs Wikijump `[[include theme:halloween]]`.
- `theme-decoration-sample-just-girly-things`: Wikidot `[[include :scp-wiki:theme:just-girly-things]]` vs Wikijump `[[include theme:just-girly-things]]`.
- `theme-decoration-sample-simple-yonder`: Wikidot `[[include :scp-wiki:theme:simple-yonder]]` vs Wikijump `[[include theme:simple-yonder]]`.
- `theme-decoration-sample-shushuin`: Wikidot `[[include :scp-jp:theme:shushuin | type=1]]` vs Wikijump `[[include theme:shushuin]]` (include form and a lost parameter).
- Titles of pages whose Wikidot title is empty: `theme-decoration-sample`, `theme:basalt`, `theme:sigma-jp`, `theme:skipos-jp` (Wikidot `''`; Wikijump the slug). Wikidot renders no page-title heading for them, Wikijump renders the slug as a heading. Ruling: the title clause is applied to the graded *sample* pages; `theme:basalt`, `theme:sigma-jp` and `theme:skipos-jp` are theme pages whose own title never appears inside a sample render, so their title difference does not fail a graded check (recorded as D15). `theme-decoration-sample` is itself the Sigma-10 port sample, so its title difference is graded — Check 2 for Sigma-10 fails on it.
- `theme-decoration-sample-min-theme` and `theme:min-theme`: titles differ (`Min Theme…` vs `ミニマリストテーマ…`).
- Tag differences on `scp-002-j`, `theme:flopstyle`, `theme:min-theme`, `theme:scp-human-resources` (Wikidot empty vs Wikijump site-vocabulary tags). None is required by a conditional block in the page as rendered, so none qualifies for Check 4's exception.

Evidence: `source_diff.json`, `evidence/allowlist/metadata-diffs.txt`, `evidence/allowlist/title-renders.txt`.
