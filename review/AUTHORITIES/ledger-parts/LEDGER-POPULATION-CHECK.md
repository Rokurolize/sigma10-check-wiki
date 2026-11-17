# LEDGER-POPULATION-CHECK — population reconciliation for GOSIGN2-LEDGER.md assembly

Extraction and counting only. No checker was run, no Playwright was run, no canonical file was edited, and no other ledger-parts file was edited. Sources read on 2026-11-17: canonical repo `/home/roku/src/Rokurolize/sigma10-check-wiki` at HEAD `d4524c5` (`start-themes.tsv`, `pages/start.txt`, `pages/start:themes-*.txt`), and `R/ledger-parts/{T1-ROWS,LOCALIZE-ROWS,RENDER-ROWS-1,RENDER-ROWS-2}.md` where R is `/home/roku/.local/state/wikijump/muse-bhl/theme-port-readiness-20261114`. G rows (CN13-CN18) and the rerun rows are being extracted in parallel and are NOT written here; this file defines exactly which population members they must cover.

## 1. Definitive population (287)

`start-themes.tsv` has 288 lines: 1 header + **287 data rows**. Row counts by the TSV `page` column (which is also the generated-subpage grouping):

| TSV page | Subpage | Rows |
|---|---|---:|
| stage1 | `pages/start:themes-stage1.txt` | 44 |
| en-1 | `pages/start:themes-en-1.txt` | 40 |
| en-2 | `pages/start:themes-en-2.txt` | 39 |
| en-3 | `pages/start:themes-en-3.txt` | 38 |
| cn-1 | `pages/start:themes-cn-1.txt` | 43 |
| cn-2 | `pages/start:themes-cn-2.txt` | 44 |
| ko | `pages/start:themes-ko.txt` | 39 |
| **Total** | 7 subpages + hub `pages/start.txt` | **287** |

Branch totals: Stage-1 44, EN 117 (40+39+38), CN 87 (43+44), KO 39. 44+117+87+39 = 287.

Ledger fullname for a row is `theme:<cand_slug>` for 285 rows, plus the two special rows in section 2. The resulting 287 fullnames are all distinct (no duplicates). `theme:creepypasta-jp` and `theme:pacom-jp` are confirmed NOT in the population (they are dependency-base files in the repo, not /start rows), and no ledger part was counted as covering them.

## 2. Bookkeeping exceptions and aliases (read before joining)

| # | Population row (TSV) | Ledger fullname to use | What the sources actually say |
|---|---|---|---|
| E1 | Quand le soleil se couche (stage1; `cand_slug=quand-le-soleil-se-couche`) | `theme:quand-le-soleil-se-couche` | The one ordinary row with no `-jp` suffix. All ledger parts use this exact form. No alias needed. |
| E2 | Sigma-10 (stage1, TSV row 38 in file order; `orig_slug=site`, `cand_slug` EMPTY) | `theme:sigma-10-jp` | The TSV gives no candidate slug at all. Every ledger part consistently uses `theme:sigma-10-jp` (T1 row 37, LOCALIZE-B row 37, RENDER-ROWS-1 via RENDER-D row 37). Join on this supplied fullname, never on the empty TSV cell or on `theme:site`. |
| E3 | Amethyst V2 (cn-1; `orig_slug` and `cand_slug` both EMPTY; original is `theme:amethyst-v2` on scp-wiki-cn per the TSV detail override) | `theme:amethyst-v2` (EXCEPTION, no candidate) | Named exception, no candidate could be produced. Spelling differs by part: T1-ROWS row 144 carries it as a blank fullname cell (`— (EXCEPTION — no candidate)`); LOCALIZE-ROWS row 287 carries it as a blank fullname cell (`— (no candidate; pages/theme:amethyst-v2-jp.txt absent)`, verdict N/A); RENDER-ROWS-2 carries it as a named row `theme:amethyst-v2-jp` with T2/T3 = NOT-RUN. All three are the SAME population row. Do not count `theme:amethyst-v2-jp` as a 288th theme, and do not treat the blank T1/LOCALIZE cells as missing coverage. |
| E4 | Telecommunications Monitoring Office Theme (en-3; `orig_slug=telecom-office-theme`, `cand_slug=telecom-office-theme-jp`) | `theme:telecom-office-theme-jp` in TSV order, alias `theme:telecommunications-monitoring-office-theme-jp` in every ledger part | SURPRISE, see section 5. The canonical file on disk is `pages/theme:telecommunications-monitoring-office-theme-jp.txt` (long form). T1 (row 164), LOCALIZE (row 144) and RENDER-ROWS-2 (RENDER-S2-D, EN20) ALL use the long form; the short TSV form appears in NO ledger part. Join this row through the alias in both directions. |

Normalisation rule for every set operation below and for the final assembly: map `theme:amethyst-v2-jp` -> `theme:amethyst-v2` and `theme:telecommunications-monitoring-office-theme-jp` -> `theme:telecom-office-theme-jp`. With only those two mappings, every ledger fullname resolves to exactly one population member.

## 3. Per-file coverage and set differences

Row keys were extracted from the table key column only (first fullname cell of each data row), not from prose, because LOCALIZE-ROWS prose alone mentions 296 distinct `theme:` strings (findings quote other themes). Counts below are extracted counts, cross-checked against each file's own stated count.

| File | Stated count | Extracted data rows | Distinct named fullnames | Exception (unnamed) rows | Duplicates inside file | Verdict |
|---|---:|---:|---:|---:|---|---|
| T1-ROWS.md | 287 (286 checks + 1 EXCEPTION) | 287 | 286 | 1 (row 144, amethyst) | 0 | MATCHES stated count |
| LOCALIZE-ROWS.md | 287 | 287 | 286 | 1 (row 287, amethyst) | 0 | MATCHES stated count |
| RENDER-ROWS-1.md | 104 | 104 | 104 | 0 | 0 | MATCHES stated count |
| RENDER-ROWS-2.md | 156 | 156 | 156 raw (156 after normalisation) | 0 (amethyst is named, as `theme:amethyst-v2-jp`, NOT-RUN) | 0 | MATCHES stated count |

Set differences against the 287 population (after the section-2 normalisation):

| Comparison | Result |
|---|---|
| Population missing from T1-ROWS | **None.** Raw diff shows only the two alias artefacts (`theme:amethyst-v2`, covered by the unnamed exception row; `theme:telecom-office-theme-jp`, covered under its long form). Extra names in T1 not in population: none after normalisation (raw extra is only the long telecom form). |
| Population missing from LOCALIZE-ROWS | **None.** Identical alias pattern to T1. Extra names after normalisation: none. |
| RENDER-ROWS-1 overlap RENDER-ROWS-2 | **Zero**, both raw and normalised. No theme appears in both render parts. |
| RENDER-ROWS-1 union RENDER-ROWS-2 | **260** distinct population members (104 + 156, no overlap). |
| Population with NO render row in parts 1+2 | **27**, exactly the G set in section 4. (A naive unnormalised diff gives 28; the 28th, `theme:telecom-office-theme-jp`, is already covered in RENDER-ROWS-2 under its long form and is NOT a G theme.) |
| Population covered only in RENDER-ROWS-2's unmeasured subset | **17**, exactly the rerun set in section 4. No RENDER-ROWS-1 row meets the same strict criterion (both pages exit 2 / no summary, T3 empty). |

Row numbers are NOT a join key. The parts number rows in different orders: amethyst is T1 row 144 but LOCALIZE row 287; the telecom theme is T1 row 164 but LOCALIZE row 144. Always join on the normalised fullname.

## 4. The two remaining render sets (exact)

### 4a. Covered only when G rows are added: 27 themes (all cn-2, CN13-CN18)

These 27 have T1 and T4/T5 rows today, and no T2/T3 row in RENDER-ROWS-1 or -2. Their T2/T3 source in the final ledger is the G supplement (from the updated REPORT-GOSIGN2-RENDER-S2-G, 54/54 machine verdicts, with its disclosed caveat that 36 of its runs are chromium-only with no WebKit verdict; carry that caveat into these rows). Listed in TSV order:

| # | Theme fullname | TSV page | Display name (TSV) |
|---:|---|---|---|
| 1 | `theme:sci-fi-jp` | cn-2 | 科幻小说 版式 |
| 2 | `theme:scpdeclassified-jp` | cn-2 | 版式：SCP 解密 |
| 3 | `theme:scplive-jp` | cn-2 | SCPLive版式 |
| 4 | `theme:shancheng-jp` | cn-2 | 山城 版式 |
| 5 | `theme:share-future-community-jp` | cn-2 | 命运共同体 版式 |
| 6 | `theme:shivering-night-jp` | cn-2 | 夜琉璃 版式 |
| 7 | `theme:sodium-jp` | cn-2 | 钠 版式 |
| 8 | `theme:sodium-pentasulfide-jp` | cn-2 | 五硫化钠 版式 |
| 9 | `theme:sound-jp` | cn-2 | 虚拟之音 主题版式 |
| 10 | `theme:starbasalt-jp` | cn-2 | 星空玄武岩 版式 |
| 11 | `theme:starry-jp` | cn-2 | 流繁星 特种版式 |
| 12 | `theme:steam-guide-jp` | cn-2 | 游戏指南 版式 |
| 13 | `theme:supply-n-demand-jp` | cn-2 | 供求理论 主题版式 |
| 14 | `theme:suprematism-jp` | cn-2 | 至上主义 美学版式 |
| 15 | `theme:tfnac-jp` | cn-2 | 版式：The Foundation Network AssCO11 |
| 16 | `theme:the-other-side-jp` | cn-2 | 我們的彼岸 主題版式 |
| 17 | `theme:the-track-changers-jp` | cn-2 | 变轨 版式 |
| 18 | `theme:trauma-jp` | cn-2 | 创伤 主题版式 |
| 19 | `theme:travellers-book-jp` | cn-2 | 旅行者之书 版式 |
| 20 | `theme:ultimate-reader-jp` | cn-2 | 终极阅读器 版式 |
| 21 | `theme:voyager-jp` | cn-2 | 旅行者 版式 |
| 22 | `theme:walk-in-the-dark-jp` | cn-2 | 圣人夜行 BHL 主题 |
| 23 | `theme:waxed-oxidized-cut-copper-slab-jp` | cn-2 | 涂蜡的氧化切制铜台阶 版式 |
| 24 | `theme:winddew-in-hand-jp` | cn-2 | 掌上风露 版式 |
| 25 | `theme:winxp-jp` | cn-2 | 倒错的新千年 版式 |
| 26 | `theme:wish-for-miracle-jp` | cn-2 | 祈冀 版式 |
| 27 | `theme:yore-jp` | cn-2 | 往昔 版式 |

### 4b. Still lacking a measured T2/T3 verdict after G rows land: 17 themes (the rerun set)

Criterion, applied verbatim to RENDER-ROWS-2 row text: T2 `no machine verdict on either page (exit 2 x2, networkidle, no summary)` AND T3 `nothing pointable recorded`. These rows currently carry a combined FINDINGS verdict with no measurement behind it on either page; in the final ledger their RENDER-ROWS-2 rows are SUPERSEDED by the rerun supplement (REPORT-GOSIGN2-RENDER-S2-RERUN16). The set is **17 themes, not 16**, despite the lane name `rerun16` (see section 5). Listed in RENDER-ROWS-2 order with source tags:

| # | Theme fullname | Current (unmeasured) row source |
|---:|---|---|
| 1 | `theme:old-money-theme-jp` | RENDER-S2-C (EN15) |
| 2 | `theme:ordopharm-jp` | RENDER-S2-C (EN15) |
| 3 | `theme:saphir-jp` | RENDER-S2-C (EN18) |
| 4 | `theme:shark-punching-centre-bhl-jp` | RENDER-S2-D (EN19) |
| 5 | `theme:ared-jp` | RENDER-S2-E (CN1) |
| 6 | `theme:betwixt-jp` | RENDER-S2-E (CN2) |
| 7 | `theme:black-rain-jp` | RENDER-S2-E (CN2) |
| 8 | `theme:brokedown-database-jp` | RENDER-S2-E (CN2) |
| 9 | `theme:broken-world-jp` | RENDER-S2-E (CN3) |
| 10 | `theme:deserted-years-theme-jp` | RENDER-S2-E (CN5) |
| 11 | `theme:fmd-bhl-theme-jp` | RENDER-S2-E (CN6) |
| 12 | `theme:gsk-jp` | RENDER-S2-F (CN7) |
| 13 | `theme:highlighter-bhl-jp` | RENDER-S2-F (CN7) |
| 14 | `theme:kitchen-jp` | RENDER-S2-F (CN8) |
| 15 | `theme:magicity-jp` | RENDER-S2-F (CN9) |
| 16 | `theme:marchen-jp` | RENDER-S2-F (CN9) |
| 17 | `theme:normal-jp` | RENDER-S2-F (CN10) |

Breakdown of the 17 by source report: S2-C 3 (old-money-theme, ordopharm, saphir), S2-D 1 (shark-punching-centre-bhl), S2-E 7 (ared, betwixt, black-rain, brokedown-database, broken-world, deserted-years-theme, fmd-bhl-theme), S2-F 6 (gsk, highlighter-bhl, kitchen, magicity, marchen, normal). 3+1+7+6 = 17. Many further RENDER-ROWS-2 themes have ONE side exit-2 (page or sample only) with a measured verdict on the other side; they are measured and are NOT in this set.

Amethyst V2 is deliberately NOT in the rerun set: it has no candidate and no runs by named exception (T2/T3 = NOT-RUN, dispositioned), which is a final disposition, not a pending measurement.

## 5. Surprise discrepancies found

1. **Telecom fullname split (affects the join).** TSV `cand_slug` is `telecom-office-theme-jp`, but the canonical file is `pages/theme:telecommunications-monitoring-office-theme-jp.txt` and T1, LOCALIZE and RENDER-ROWS-2 all use the long form exclusively (short form occurs 0 times in all four ledger parts). An unnormalised population diff therefore falsely reports this theme as missing from T1/LOCALIZE and as a 28th G theme. Fix in assembly: one alias mapping (section 2, E4); no file needs editing for the ledger to join correctly, but the TSV-versus-canonical slug divergence itself is recorded here for the coordinator.
2. **Rerun set is 17, not 16.** The strict both-pages-unmeasured criterion yields 17 RENDER-ROWS-2 themes (section 4b). The lane/report name `RERUN16` / `gs-render-s2-rerun16` undercounts by one. If the rerun deliverable reports only 16 themes, one of the 17 listed in section 4b will still lack a measured verdict; the assembly must check the rerun supplement against all 17 names.
3. **Amethyst spelled three ways.** Blank exception row in T1 (row 144), blank exception row in LOCALIZE (row 287), and named `theme:amethyst-v2-jp` NOT-RUN row in RENDER-ROWS-2, for one population row whose original fullname is `theme:amethyst-v2` and which has no `-jp` canonical file. Counted naively by fullname strings, the population appears to gain a spurious theme and lose the exception.
4. **Sigma-10 has no TSV candidate slug.** `cand_slug` is empty (the only empty cell besides amethyst). Its ledger fullname `theme:sigma-10-jp` exists only in the ledger parts and the canonical file, not in the TSV. A parser that builds the population purely as `theme:<cand_slug>` produces a spurious `theme:` entry (twice, counting amethyst) and a 286-member population; the correct population is 287 rows with the two supplied fullnames in section 2.
5. **No count mismatches otherwise.** Every ledger part's extracted row count equals its stated count (287 / 287 / 104 / 156), there are no duplicate rows inside any part, and the RENDER-ROWS-1 / RENDER-ROWS-2 overlap is exactly zero. LOCALIZE row numbering starting with `theme:min-theme-jp` at row 1 (not TSV order) confirms row numbers differ across parts (see section 3).

## 6. Assembly plan for GOSIGN2-LEDGER.md (exact join)

Population and row order: the 287 TSV rows in TSV file order (stage1, en-1, en-2, en-3, cn-1, cn-2, ko), numbered 1-287 in that order in the final ledger. Join key for every part: normalised fullname (section 2). Never join on any part's internal row number.

| Column(s) | Source for every theme | Notes |
|---|---|---|
| Population identity (fullname, display name, branch/page group, original) | `start-themes.tsv` row (fullname per section 2) | Amethyst identity from its TSV detail override; Sigma-10 fullname supplied as `theme:sigma-10-jp`. |
| T1 | `ledger-parts/T1-ROWS.md`, all 287 | Amethyst from its unnamed exception row 144; telecom from row 164 under the long form. |
| T4 and T5 | `ledger-parts/LOCALIZE-ROWS.md`, all 287 | That part carries the reports' single combined T4/T5 verdict word in both columns; preserve it as-is. Amethyst from its unnamed exception row 287 (N/A, named exception); min-theme and shushuin are N/A (JP originals). Telecom from row 144 under the long form. |
| T2 and T3, 104 themes | `ledger-parts/RENDER-ROWS-1.md` | The 44 Stage-1 themes plus EN1-EN12. Each row's combined verdict fills both T2 and T3, per that part's stated method. Includes Sigma-10 (`theme:sigma-10-jp`, sample page does not exist, as recorded there). |
| T2 and T3, 156 themes | `ledger-parts/RENDER-ROWS-2.md` | EN13-EN24, CN1-CN12, KO1-KO8, including amethyst as NOT-RUN/NOT-RUN (exception disposition, final). Telecom included here under the long form (S2-D, EN20). |
| T2 and T3, 27 themes | G supplement (RENDER-ROWS supplement from updated S2-G report), when it lands | Exactly the section-4a list; carry the chromium-only caveat for 36 runs into the affected rows. |
| T2 and T3, 17 themes (superseding) | Rerun supplement (REPORT-GOSIGN2-RENDER-S2-RERUN16), when it lands | Exactly the section-4b list; these rows REPLACE the unmeasured RENDER-ROWS-2 rows for those themes. A theme the rerun marks BLOCKED-ENV with evidence keeps that disposition instead of a fabricated verdict. |

Final arithmetic that the assembled ledger must satisfy:

| Category | Count |
|---|---:|
| Population | 287 |
| T1 covered | 287 (286 named + 1 exception row) |
| T4/T5 covered | 287 (286 named + 1 exception row) |
| T2/T3 rows before supplements | 260 (104 + 156, overlap 0) |
| T2/T3 rows added by G supplement | 27 |
| T2/T3 total after G | 287 |
| Of those, measured verdicts | 269 (104 in part 1 + 138 measured in part 2 + 27 in G) |
| Of those, pending measured verdict (rerun set) | 17 |
| Of those, NOT-RUN by named exception (amethyst-v2) | 1 |
| Check: 269 + 17 + 1 | 287 |

Assembly gate: before issuing the go-sign in COMPLETION-REPORT.md section 9, re-run this reconciliation against the two supplements: G supplement must contain exactly the 27 section-4a fullnames (no more, no fewer), and the rerun supplement must contain exactly the 17 section-4b fullnames. Any shortfall leaves that theme without a measured T2/T3 verdict and blocks the all-287 claim.

LEDGER-POPULATION-CHECK: COMPLETE
