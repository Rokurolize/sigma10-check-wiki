# AUTHORITIES — vendored governing records for the review packages

The per-theme review explanations (`review/<theme>/README.md`) cite governing
authorities constantly: the rulings their fixes follow, the test definitions
their verdicts were judged under, the register their dispositions come from.
The seven files in this directory are verbatim copies of the frozen campaign
records that otherwise live outside this repo, vendored so that every such
citation resolves inside the repo and can be checked mechanically
(`review/build_review.py --check` recomputes the hashes below and resolves
citation locators against these files).

## Immutability rule

A vendored file is never edited in this repo. If a vendored record is ever
corrected, the correction arrives as a new file beside it, never as an edit:
that is how GOSIGN2-LEDGER-SUPPLEMENT.md superseded section (e) of
GOSIGN2-LEDGER.md without touching the ledger. Hash drift against the table
below is a hard check failure, not something to repair by editing a copy.

## Vendored files

Copied on 2026-11-17. Source path of each file: the campaign directory
`/home/roku/.local/state/wikijump/muse-bhl/theme-port-readiness-20261114/`
plus the file name.

### RULINGS-20261116.md — GOVERNING

- SHA-256: `e1dfa2ac3ad88ec4cb32feab41b06052895955e748fcb4a180552b471ebf5286`
- Role: the owner's five adjudication rulings of 2026-11-16. Rulings 1, 3,
  and 4 govern whole fix classes (cross-theme imports repoint to the JP
  fixed base candidate; TASL attribution for campaign translations; a
  component or fragment a theme needs is ported together with the theme).

### GOSIGN-TESTS.md — GOVERNING

- SHA-256: `8d8504b3bc543107c2428647b21a8b088c3c3c49364c1a0f88b54bc554d339a7`
- Role: the go-sign test definitions (T1 source check, T2 render check, T3
  checklist walk, T4 localize patterns plus follow-up diff, T5 translation
  text), the claim, the population, and the exclusions. Every theme's
  verdict stamp cites T1–T5 against these definitions.

### SKILL-EDIT-20261116.md — GOVERNING

- SHA-256: `d1b3199abf568c29b304a671ecc376deff4c22b128daa5f7cd14a4233b6c1c8c`
- Role: the record of the owner-ordered edit to the staff skill's
  application that made sigma10-jp-test a sanctioned draft host. It is the
  basis of every class (iii) / draft-host disposition and of the
  pseudo-reference reclassification.

### GOSIGN2-LEDGER.md — RECORD

- SHA-256: `c4a0974eef905716b5d56e951257268695f0decb72bf9059ca1d146508d4fe25`
- Role: the findings register: (a) population, (b) the per-theme table,
  (c) registers c1–c4, (d) exceptions, (e) the 107 blocking items. Every
  per-theme disposition cites its (b) row, (c) register entries, or (e)
  items here, and those locators only resolve against the whole file.

### GOSIGN2-LEDGER-SUPPLEMENT.md — RECORD

- SHA-256: `01bfd84a2a77ab0d8263994bf5cee382d9956d7b393a0baa44d25f7b2f5f98b5`
- Role: the re-judgement of all 107 ledger (e) items after the FIX5 wave,
  with the final determination in (d): 81 fixed, 26 dispositioned with
  grounds, 0 still open; 286 of 286 pass-eligible themes pass.

### COMPLETION-REPORT.md — RECORD

- SHA-256: `7bbcefe75d8895ca1555e5636c8a2bf0c8f40ea606238f929d5a32df2f189d05`
- Role: the campaign completion report. Section 9 records the withdrawal
  of the earlier go-sign determination; section 10 issues the go-sign
  itself. See the reader warnings below before citing either.

### REPORT24.md — RECORD

- SHA-256: `694cb3320012c58745b2e9e89b1a417bab2f1815affee5f6070d6ac24db27bea`
- Role: the phase-24 audit of the SB3 (scp-jp-sandbox3) and FS
  (scp-jp-storage) site themes: the capture record (§1), the SB3 and FS
  adjustment inventories (§2 S1–S11, §3 F1–F8), the per-wiki migration
  requirements (§4), and the questions only site-admin access can settle
  (§5). The FS review package's F1–F8 citations resolve here, as will the
  SB3 package's S-citations when that package is built.

## Reader warnings

1. **RULINGS #5 is superseded in application.** The frozen text of ruling 5
   is the pre-investigation wording ("the coordinator's investigation
   continues"). The operative disposition, that credit-modal failures on
   preview-form pages are a property of the preview credit module and not a
   theme defect, is recorded in GOSIGN-TESTS T2's note and in AGENTS.md §4
   ruling 5. Cite RULINGS #1–#4 directly; for the credit-modal disposition
   cite `GOSIGN-TESTS T2` and `AGENTS §4`, never RULINGS #5 alone. The
   vendored file stays byte-verbatim; this warning lives here, not in it.
2. **COMPLETION-REPORT §9 is a withdrawal, §10 is the issuance.** A
   citation to the go-sign is `COMPLETION-REPORT §10`; §9 explains why the
   earlier sign was withdrawn and is context, not a current verdict.

## Citation grammar

Explanations cite in bracketed short form, one grammar per authority,
always with a locator that resolves to a specific place:

| Authority | Form | Example |
|-----------|------|---------|
| Rulings | `RULINGS-20261116 #<n>` | `RULINGS-20261116 #4` |
| Test definitions | `GOSIGN-TESTS T<n>` | `GOSIGN-TESTS T2` |
| Skill-edit record | `SKILL-EDIT-20261116` (whole file; it is 2,261 B) | `SKILL-EDIT-20261116` |
| Ledger | `LEDGER (b) row <n>` / `LEDGER c<1-4>` / `LEDGER (d)` / `LEDGER (e) item <n>` | `LEDGER (e) item 73` |
| Supplement | `SUPPLEMENT item <n>` / `SUPPLEMENT (d)` | `SUPPLEMENT item 73` |
| Completion report | `COMPLETION-REPORT §<n>` | `COMPLETION-REPORT §10` |
| Phase-24 site-theme audit | `REPORT24 §<n>` / `REPORT24 F<n>` / `REPORT24 S<n>` | `REPORT24 F5` |
| AGENTS.md | `AGENTS §<n> "<exact heading text>"` | `AGENTS §5 "JP fonts (pattern 7) and font hosts (pattern 5)"` |
| Patterns | `KB-<nn> @ <commit>` (ID + patterns commit hash; bodies never copied) | `KB-11 @ 0eef991` |
| Supplement types | `SUPPLEMENT-TYPES T<n>` | `SUPPLEMENT-TYPES T7` |
| Staff skill (external) | `SKILL theme-component-review <file> <locator>` | `SKILL theme-component-review localize.md §3` |
| License (external) | `CC BY-SA 3.0 <canonical URL>` | `CC BY-SA 3.0 https://creativecommons.org/licenses/by-sa/3.0/` |

The AGENTS form quotes the heading text, not just the section number,
because AGENTS.md is a living document: a renumbering or retitling then
fails loudly in `--check` instead of silently pointing at the wrong rule.
The KB form pins the patterns commit hash for the same reason. Citations
to the two external authorities (SKILL, CC) are format-linted only and
reported as EXTERNAL-UNVERIFIED, never as passing: the staff skill lives
in another repo and its current text is not visible to the checker.

## Not vendored, by design

- **The staff skill theme-component-review** is SCP-JP staff's plugin,
  maintained in the staff repo and still evolving; copying its text here
  would misattribute ownership and fork a living document. Cite it by name
  + file + item only (grammar above); do not quote its body text beyond a
  locator.
- **The CC BY-SA 3.0 license text** is linked at its canonical URL, never
  reproduced here. The attribution mechanics explanations actually apply
  are the in-repo ones (AGENTS.md §4 ruling 3 and §5).

One adjacent debt, stated so it is not mistaken as discharged: the
repo-level TASL attribution record owed before any public upload of this
repo is separate from this vendoring, and this vendoring does not
discharge it.
