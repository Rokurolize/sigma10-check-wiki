# Review package — theme:xmas-jp (EN → JP port)

<!-- BEGIN GENERATED VERDICT STAMP — do not hand-edit; regenerate with review/build_review.py -->
## Verdict stamp
- Theme: theme:xmas-jp — origin EN, population #161 [GOSIGN2-LEDGER (b) row 161]
- Overall: STALE — candidate file changed since the verdict was computed (verdict against 435a6bb-era content, file sha256 now 33897398a8045e5da5b0eb189f24c5f1b66b69c9b93deb5879e4cb09688d63c8); verdict not carried over, re-judgement required
> verdicts below describe the pre-change file
- T1 (source check): FINDINGS (classified) — baseline 2026-11-16: exit 1, 20 errors / 0 warns / 0 infos (pseudo-ref×20); standing classes dispositioned in register c1 [T1-ROWS row 181; GOSIGN2-LEDGER (b) row 161]
- T2/T3 (render, combined verdict): FINDINGS — [combined T2/T3] report `FINDINGS` — page runtime-hotlink site-theme chain only; sample T2 no machine verdict (exit 2, no summary). [RENDER-ROWS-2 (RENDER-S2-D (EN24))]
- Engine coverage: full matrix as run by the lane; coverage not separately caveated in the row (the row records inconclusive runs, carried verbatim above) [RENDER-ROWS-2 row]
- Credit modal: no credit-modal line recorded [RENDER-ROWS-2 (RENDER-S2-D (EN24))]
- T4 (localize patterns + follow-up): FINDINGS — display-affecting findings: 1 [LOCALIZE-ROWS row 161, source LOCALIZE-S2-C]
- T5 (translation text): FINDINGS — the source reports judge T4/T5 jointly; one verdict word covers both [LOCALIZE-ROWS row 161]
- FIX5 re-judgement: none — no OPEN items at the ledger determination [GOSIGN2-LEDGER (b) row 161]
- Computed against: canonical commit 9b0eb99e5078fae699307945cd45d3f3566f6920; candidate file pages/theme:xmas-jp.txt sha256:33897398a8045e5da5b0eb189f24c5f1b66b69c9b93deb5879e4cb09688d63c8; record: GOSIGN2-LEDGER.md + GOSIGN2-LEDGER-SUPPLEMENT.md as of the FIX5 head 435a6bb
<!-- END GENERATED VERDICT STAMP -->

## Status

| | |
|---|---|
| Verdict | **PASS** — passed at the ledger determination; this theme had no OPEN items and no §(e) register entry (GOSIGN2-LEDGER (b) row 161) |
| Standing items | **DISPOSITIONED** — T1 pseudo-ref ×20 (class (ii), section 11); the render row's site-theme chain item (KB-40, section 11); T4's pattern-5 asset finding (class (ii) / KB-58, section 11). One further item is **flagged** in the per-theme record: a later dedupe wave emptied two of the theme's delivery slots, and no ledger line dispositions it (section 3) |
| Go-sign basis | COMPLETION-REPORT.md §10 (go-sign issued; 81 FIXED / 26 DISPOSITIONED / 0 OPEN across the sweep) |
| Named exception | None for this theme (the sweep's single named exception is theme:amethyst-v2, which has no candidate) |

## Provenance

| | Original | Candidate |
|---|---|---|
| Page | theme:xmas | theme:xmas-jp |
| Wiki | scp-wiki.wikidot.com | SCP-JP Sigma-10 candidate (canonical repo) |
| Reference revision | 51 (first translation; the candidate's credit block records 初訳時参照リビジョン: 51) | — |
| Source of this copy | Mirror store `review-mirrors/orig-xmas-rev51.txt` (class COPY, hash-verified against review/sources.tsv) | Canonical file `pages/theme:xmas-jp.txt`, copied at worktree HEAD 662baf3 |
| Lines / bytes | 281 lines / 6,828 bytes | 331 lines / 9,963 bytes |
| SHA-256 | 8eff858d56a260ef4600a1c6d3b2f7153cda2b8ef03067a563e1cfb8c06af104 | 168435a3a14a949c3b91be0039704eedf122aba99e8533a9c9dfc9b06f2a4833 |

Wave history: the candidate was created by the Stage 2 EN24 integration (commit 3c60859) and has three later commits: 1869877 (FIX-CREDIT-D, the translator field taking its ruling-3 form, section 1), a497307 (FIX4-MECH, the duplicate-@import removal whose xmas hunk emptied two delivery slots, section 3 and the per-theme record), and b5cb724 (the usage-example sweep, which put the examples' self-references into the -jp posting form). The verdict stamp reads STALE on the sweep commit alone; the verdict-era bytes already contained the FIX4-MECH state.

## Summary

A small EN seasonal theme: five CSS exhibits (header rules, snowfall layers, the snowfall keyframes, and two Black Highlighter variants) delivered by a tag-gated module, plus a parameterized partial-delivery mechanism — four include slots through which a user page pulls only the header, only the snow, or the Black Highlighter forms. The candidate adds the wave-standard frame and preview credit block, re-hosts the theme's seven image files to the draft host, translates the usage prose, wraps the exhibits in a collapsible, and appends a license box the original does not carry. Measured churn against the current (post-repair) candidate (diff.md, the generator's difflib count: +107/−50 in 6 diff hunks; GNU-diff 135 changed lines). The pre-repair figures were +108/−59 in 6 hunks (32 classifier change blocks); restoring the slot modules makes their lines match the original again, which is why both counts fall. The item that needs a reviewer's eye — FIX4-MECH's file-level duplicate-@import removal that emptied the conditional slot modules — has since been repaired by FIX-XMAS (9b0eb99), as recorded in the per-theme record.

## Class summary

Auto-classification by review/classify_hunks.py (signature table 2026-11-17.1): 32 change blocks — 26 specific (81.3%), 4 heuristic (12.5%), 2 residue (6.3%), 0 skipped. Pattern citations below name the KB entry; the patterns/ tree state cited throughout is commit 9c5e9079afb01d30cb9fc4ef9d714e5591eb2ffa.

| Label | Blocks |
|---|---|
| BARE-RATE-DEL | 1 |
| CREDIT-PREVIEW | 1 |
| DELIVERY-HOST | 3 |
| DRAFT-HOST | 15 |
| ESCAPED-INCLUDE | 6 |
| HEADERVAR | 1 |
| IFTAGS | 2 |
| INCLUDE-REPOINT | 3 |
| LICENSE-BOX | 1 |
| SELF-DELIVERY | 6 |
| TASL-FIELDS | 1 |
| TRANS-UNANCHORED | 7 |

## Standing sections

### 0. Header and provenance frame

- **What:** Theme theme:xmas-jp; original theme:xmas on scp-wiki at reference revision 51; candidate `pages/theme:xmas-jp.txt`. Provenance route: derived from the original at the reference revision by the Stage 2 EN24 integration (sources.tsv kind: standard; no production JP counterpart exists for this theme, so the R4 adoption question does not arise). The frame itself moved: the original opens with its tag gate and bare Rate module (original L1–4); the candidate opens with the interwiki-style frame (candidate L1–4) and places the localized gate after the frame (candidate L6).
- **Why:** Section 0 declares the provenance route so every later count is read against the right baseline; the gate's tag is P2 (iftags tag localization), the frame is P6/T3 (section 3).
- **Verify:** The sources.tsv row for xmas-jp; `sha256sum original.txt` against the Provenance table.
- **Disposition:** Standing (the route itself); the gate and frame changes are recorded in sections 2 and 3.

### 1. Credit and attribution

- **What:** The original's credit is body prose (original L6): created by Dc_Yerko for the Spanish Translation Site, adapted by stormbreath, snowfall code adapted by EstrellaYoshte. There is no credit module and no license box. The candidate installs the JP form at the head of the gated region: a `:scp-jp:credit:start-preview`/`end-preview` block (candidate L8–17) carrying the eight ruling-3 fields — title Xmasテーマ; 翻訳責任者 AI; 翻訳年 2026; 原題 Christmas Theme; 著作権者 Dc_Yerko、stormbreath、EstrellaYoshte (all three roles from the original's prose, not only its first name); 作成年 2020; 初訳時参照リビジョン 51; 元記事リンク https://scp-wiki.wikidot.com/theme:xmas, the host sources.tsv records for the original (no probe needed: the recorded host and the link agree). The original prose survives in translated form directly below the block (candidate L19), carrying the Spanish-branch link (section 7). The bare `[[module Rate]]` and its `[[>]]` wrapper (original L2–4) are deleted. One supplement has no original counterpart: a license box appended at the tail of the gated region (candidate L273–311) — a `component:license-box-backend` include with author=Dc_Yerko, seven file entries, and `component:license-box-end`. The entries attribute GIF-111.gif and logo-xmas.png to Dc_Yerko and logo-xmas-bhl.png, sn.png, sn2.png, n1.png, n2.png to EstrellaYoshte (the sn entries noting the Css-Snow-Fall-Animation basis), each states CC BY-SA 3.0, and each discloses that the original carries no per-file designation, so the per-file authors are the porter's record, not a copied one.
- **Why:** P3/T1: the preview credit module is the rate-bearing JP form, so the bare Rate is deleted rather than duplicated (KB-09). Ruling 3 fixes the eight fields; the translator field's placeholder form that the LOCALIZE row recorded was repaired by FIX-CREDIT-D (commit 1869877). The license box is the T4 supplement (KB-63, form judged per KB-60): the original's file set had no license record at all, and the JP form requires one.
- **Verify:** `grep -n 'module Rate' candidate.txt` returns nothing; read candidate L8–17 against the eight fields; the 原題 was probed against the live page for this package (2026-11-17: the page title is "Christmas Theme").
- **Disposition:** FIXED (GOSIGN2-LEDGER §(c3): "theme:xmas-jp (LOCALIZE-S2-C): P3 credit fields FIXED (credit waves; checker-verified); P5 DISPOSITIONED (class (ii) / KB-58)").

### 2. Includes and components

- **What:** The gate's tag is localized, +theme → +テーマ (block B2 at the head; the closing `[[/iftags]]` likewise, original L256 → candidate L313). The usage exhibits' escaped includes are repointed (B4, B6, B8, with the remaining ESCAPED-INCLUDE labels riding in B10–B12): `:scp-wiki:theme:xmas` → `:scp-jp:theme:xmas-jp`, in the full form and in the header-only, snow-only, and Black Highlighter partial forms; the population sweep (b5cb724) put these self-references into the -jp posting form they now carry. The Black Highlighter companion include is repointed in the three BHL exhibits (B10–B12): `:scp-wiki:theme:black-highlighter-theme` → `:scp-jp:theme:black-highlighter-theme` — the plain name is the correct target because that page exists on production scp-jp under it; not every repoint takes -jp. The credit and license includes are section 1; the frame include is section 3.
- **Why:** P1 (KB-15): an include must name the JP counterpart that actually exists on scp-jp; P2/KB-08 for the gate tag. Escaped examples are judged too, because readers copy them.
- **Verify:** `grep -n '\[\[include' candidate.txt` — every include names a `:scp-jp:` target or a plain JP component.
- **Disposition:** Applied; no foreign include kept, no named exception needed.

### 3. Delivery and code loading

- **What:** Three delivery channels. (1) The frame (candidate L1–4): an interwiki-style include at priority 1 whose `theme=` names the candidate's own `local--code/theme%3Axmas-jp/1` on the draft host. (2) The gated main module (candidate L267–271): imports the candidate's own /1, /2, /3, re-hosted from the original's scp-wiki.wdfiles.com addresses to the same draft host (B27). (3) The four include slots after the gate (candidate L315–330), the partial-delivery mechanism: `{$xmas-header-bhl}` imports /4 (candidate L321–325, the original's own `theme%3Axmas//4` double slash normalized) and `{$xmas-snow-bhl}` imports /5 (candidate L327–330) — but `{$xmas-header}` (candidate L315–316) and `{$xmas-snow}` (candidate L318–319) are empty markers with no module inside, and the snow-bhl slot's /3 import is gone. Self-delivery census: the page's five `[[code]]` blocks in order are 1 header rules (candidate L67), 2 snowfall layers (L89), 3 keyframes (L125), 4 BHL :root and lights (L188), 5 BHL extrac snowfall (L228); every surviving address names the block that actually holds its CSS (frame /1 = block 1, main module /1–/3, header-bhl /4 = block 4, snow-bhl /5 = block 5). The emptied slots are the per-theme record's item, argued there in full.
- **Why:** P4/T9 (own-code delivery served from JP hosts) and P6/T3 (the frame supplement). The draft-host form of the live lines is KB-41, class (iii): sanctioned at draft stage, rewritten to the production host at posting. The slot contents were removed by FIX4-MECH under KB-65's file-level dedupe rule, which carries no exception for conditional-comment delivery modules; the governing precedent is theme:foundom-jp's include-slot mechanism, whose deletion the main chat ruled a restore.
- **Verify:** `grep -n 'local--code' candidate.txt` — the frame (L3), the main module (L268–270), and the two surviving slot imports (L323, L329); read candidate L315–330 against original L258–282.
- **Disposition:** DISPOSITIONED (draft-host lines, class (iii)). The slot emptying is **not** dispositioned by any record — flagged in the per-theme record.

### 4. Fonts and assets

- **What:** Fonts: none. Neither file names a `font-family` (grep count 0 on both sides); the theme inherits the site stacks, and no stack names a face this layer would have to load. Assets: the theme's seven image files are re-hosted, eleven URL lines in all, from `scp-wiki.wdfiles.com/local--files/theme%3Axmas/` to `sigma10-jp-test.wdfiles.com/local--files/theme%3Axmas-jp/` with file names unchanged — GIF-111.gif (candidate L77), logo-xmas.png (L80), sn2.png (L105), sn.png (L111, L117), logo-xmas-bhl.png (L190, inside the `--logo-image` value, section 5), n1.png (L204), n2.png (L208), and block 5's sn2.png/sn.png set (L241, L247, L253). The T4 lane probed all seven files on the draft host and found 404 for every one: they are not uploaded at draft stage, so at T4 time the background, logo, snow, and lights would not render from these addresses.
- **Why:** P5 with KB-17 (asset hosts) in the KB-41 draft form. The 404 state is the class (ii) deferred-upload property of the draft host, not a wrong address: the folder and file names are the candidate's own.
- **Verify:** `grep -n 'wdfiles' candidate.txt` against the list above; the T4 probe record is REPORT-GOSIGN2-LOCALIZE-S2-C (pattern 5).
- **Disposition:** DISPOSITIONED (GOSIGN2-LEDGER §(c3): P5 DISPOSITIONED, class (ii) / KB-58 — the files are uploaded at posting).

### 5. Header, sidebar, and site furniture

- **What:** One variable: the `--logo-image` override is carried (original L175 → candidate L190, inside code block 4's `:root`) with only its host repointed (section 4); the HEADERVAR label on that block is the asset line, not a value change. Neither file sets `--header-title` or `--header-subtitle`. The header and sidebar rules themselves ride inside the exhibits, otherwise byte-identical to the original's.
- **Why:** P9/T6 ground: the theme's furniture is exhibit CSS, and no layout adaptation was needed for it to sit on the JP frame; the candidate inherits the JP site furniture through the frame (section 3).
- **Verify:** `grep -n -- '--header-title\|--header-subtitle\|--logo-image' candidate.txt` — one hit, the carried override.
- **Disposition:** Standing.

### 6. Text translation

- **What:** The usage lead-ins are translated (the three heuristic TRANS-UNANCHORED pairs B5, B7, B9: "If you only want to use the header…" → ヘッダーだけを使う場合は…, and its snow and Black Highlighter counterparts), each verified line by line against the mirror for this README. The credit prose is translated below the credit block (section 1). Inside the CSS, the theme's title banner is carried in English (it is the theme's banner, naming the work and its authors), and the snowfall attribution comment is carried untranslated (it is an attribution with its source link, section 7). The collapsible label is section 8.
- **Why:** P10 (KB-18): reader-visible prose is translated; banner and attribution text are the work's own furniture, not prose addressed to the reader.
- **Verify:** The pairs are diff.md's body sections in order; `grep -n 'If you only' candidate.txt` returns nothing.
- **Disposition:** Standing (the port itself).

### 7. Links

- **What:** Two kept outbound links, both the original's own. The Spanish-branch link survives in the translated credit prose (candidate L19): `http://lafundacionscp.wikidot.com`, label translated (スペイン語翻訳サイト). The snowfall source link (github.com/elena-in-code/Css-Snow-Fall-Animation) survives in code block 2's attribution comment and again in the license box's sn.png/sn2.png entries. The credit block's source link is section 1: its host agrees with the host sources.tsv records for the original, so the broken-host probe does not arise. No other outbound links exist in either file.
- **Why:** P11: prose links take the serving original; both of these do. The ES link's http scheme is the settled class (ii) posting rewrite (right host, serving over both schemes), not a candidate defect.
- **Verify:** `grep -n 'http' candidate.txt` — the ES link, the https GitHub links, and the delivery/asset addresses of sections 3–4.
- **Disposition:** Standing; the scheme item is class (ii).

### 8. Structure

- **What:** The five exhibits are present in the original's order (exhibit census 5 = 5), now wrapped in a porter-added collapsible (candidate L66, show/hide both テーマのソース; closes candidate L265). Blocks B13 (the opening line, heuristic) and B26 (the closing line, residue) adjudicate to this one presentation supplement; nothing inside the wrapper was restructured. The license box is appended at the tail of the gated region (section 1). Region order otherwise mirrors the original: gate, credit, usage prose, exhibits, main module, then the slots outside the gate's close. The skeleton's "none" for this section does not survive contact with the bytes (the wrapper) and is corrected here.
- **Why:** R3 exists to force exactly this adjudication, because a restructure and a deletion share a diff shape; here the census, not the label, decides, and the census is complete.
- **Verify:** Compare `grep -n '\[\[code' original.txt candidate.txt` — five blocks on both sides, same order.
- **Disposition:** Standing; no structural deletion, no class I item.

### 9. Formatting only

- **What:** None. The classifier finds 0 whitespace-only blocks and 0 re-indentation pairs over the 32 blocks, so there is no formatting churn to disclose and the R7 follow-up-diff hazard is not triggered.
- **Why:** Formatting churn is disclosed as its own class so it is never mistaken for a semantic change.
- **Verify:** classification.json's summary (`ws_only` and `reindent_blocks` counts).
- **Disposition:** None required.

### 10. Porter annotations

- **What:** One R2 annotation: the banner line "Ported for SCP-JP (theme:xmas rev 51)" added inside code block 1's banner (candidate L73; residue block B14), recording the port's provenance and the reference revision at the head of the delivered CSS. The license entries' disclosure sentences (that the original carries no per-file designation) are porter-authored supplement text, counted in section 1 rather than here. The skeleton's "none" for this section does not survive the bytes and is corrected here.
- **Why:** R2: porter-added text is part of the change record, including when it rides inside another labeled block.
- **Verify:** Read candidate L73.
- **Disposition:** Standing.

### 11. Dispositions and exceptions

- **What:** Four items, each with its ground. (1) T1's twenty pseudo-ref errors: class (ii), posting-procedure — they are the candidate's own draft-host local--code and local--files lines (sections 3–4); the posting procedure rewrites or re-hosts them. The count has a history: FIX4-MECH's removals took four of those very lines out of the file, so a checker run against the current bytes reads 16 errors, not 20 — the reduction is item (4)'s side effect, not a posting fix. (2) The render row's one item, the page's runtime-hotlink site-theme chain: KB-40, the environment layer, not charged to the candidate; the sample's T2 run produced no machine verdict (exit 2, no summary), recorded as-is in RENDER-ROWS-2. (3) T4's pattern-5 finding, the seven re-hosted asset files answering 404 on the draft host: DISPOSITIONED class (ii) / KB-58 by the ledger §(c3) line (section 4). (4) The emptied delivery slots of section 3: no record dispositions them — the ledger §(c3) line for this theme covers P3 and P5 only, FIX5 recorded no OPEN item, and the T4 review predates the wave that caused them. The ledger's determination for this theme is PASS and this package does not re-open it; the item is flagged in the per-theme record because a reader following the page's own usage exhibits today reaches a mechanism that delivers nothing.
- **Why:** A disposition is a decision with grounds (AGENTS.md §3 classes (i)/(ii)/(iii); the named KB entries), not an omission; an item with no disposition is flagged, not silently absorbed.
- **Verify:** Each item names its deciding record above and in the per-theme record.
- **Disposition:** DISPOSITIONED (items 1–3); item 4 flagged with evidence.

### 12. Verification

- **What:** (a) T1 source check (T1-ROWS row 181): exit 1, 20 errors / 0 warns / 0 infos, all pseudo-ref, class (ii); no class (i) error. (b) T2/T3 render (RENDER-ROWS-2, lane RENDER-S2-D (EN24)): FINDINGS — the site-theme chain item of section 11(2) only; the sample T2 run has no machine verdict. (c) T4/T5 (LOCALIZE-ROWS row 161, lane LOCALIZE-S2-C): FINDINGS jointly, display-affecting findings 1 (the pattern-5 asset set). The T4 lane's own delivery verification (REPORT-GOSIGN2-LOCALIZE-S2-C) fetched the draft host's code/1–5 live on 2026-11-16 and matched code/4 byte-for-byte against exhibit block 4 — in the pre-FIX4-MECH state, whose slot line numbers it cites (L317–L337 of a 339-line file); every verification this theme has predates the slot removal. (d) This package's own checks: both copies hash-verified (Provenance table); a brace-depth scan of both files' CSS regions ends at depth 0 with no negative excursion; the self-delivery census of section 3 was counted by hand from the bytes; the live EN page's title was probed (section 1). The count claim above describes the pre-repair candidate; the regenerated diff.md for the current candidate reports +107/−50 in 6 hunks (GNU-diff 135 changed lines), the authoritative count for the bytes now in this package.
- **Why:** Verification claims name the cheapest deciding check and its result, not a general assurance.
- **Verify:** Re-run the checker on `pages/theme:xmas-jp.txt` and `python3 review/build_review.py --check` in this repo.
- **Disposition:** PASS (GOSIGN2-LEDGER (b) row 161; go-sign, COMPLETION-REPORT §10).

## Per-theme record

### The emptied delivery slots (FIX4-MECH, commit a497307)

The original's tail carries four include slots (original L258–282), the theme's partial-delivery mechanism: `[!-- {$xmas-header}` wraps a module importing code/1; `[!-- {$xmas-snow}` a module importing /2 and /3; `[!-- {$xmas-header-bhl}` a module importing /4; `[!-- {$xmas-snow-bhl}` a module importing /3 and /5. The candidate's usage exhibits document exactly these parameters (candidate L21–41: the full form, header-only at L29–34, snow-only at L36–41, and the two Black Highlighter forms). The port as created (commit 3c60859) carried all four slots populated, with the draft host substituted and the original's own `theme%3Axmas//4` double slash repaired; the T4 lane verified that state as the normal delivery path on 2026-11-16. Commit a497307 (FIX4-MECH, charged to KB-65's cross-block tier) then removed the xmas-header slot's whole module (its L316–318), the xmas-snow slot's whole module (L322–325), and the /3 import inside xmas-snow-bhl (L336), on the ground that those @import URLs also appear in the gated main module. The wave's report names what it removed — "duplicated between the unconditional module at L267-271 and `[!-- {$param} ...]` conditional-comment modules" — and records the checker moving 20 → 16 errors as the gain. But the two module sets are not duplicates in effect: the main module fires under the theme page's own tag gate, while the slot modules are the delivery path for parameterized inclusion into other pages, which is the usage the page documents. On the current bytes, a header-only or snow-only inclusion delivers nothing for its parameter, and the Black Highlighter snow form delivers code block 5's rules without code block 3's keyframes (snowOne/snowTwo/snowThree are defined only in block 3), so its snowfall renders static. This is the same family as theme:foundom-jp's deleted include-slot mechanism, which the main chat ruled a restore; it differs in cause — a named wave's dedupe rule, not the port itself — and no ledger line dispositions it (section 11(4)). The repair is mechanical and needs no re-porting: restore the three removals from the pre-wave bytes (commit 1869877), which are the original's slot contents with the draft host and the /4 repair already applied. This package flags the item with its evidence and does not edit the candidate.

The repair has since landed — FIX-XMAS, canonical commit `9b0eb99e5078fae699307945cd45d3f3566f6920` ("pages: xmas delivery slots restored, wish-for-miracle license clause", 2026-11-17; report `R/review-scout/FIX-XMAS.md`, item 1). The three FIX4-MECH removals were restored verbatim from the pre-wave bytes (commit 1869877): on the current candidate the `xmas-header` slot at L315–319 again carries its `[[module css]]` importing block /1 (L317), the `xmas-snow` slot at L321–326 again imports blocks /2 and /3 (L323–324), and the `xmas-snow-bhl` slot at L334–338 again imports block /3 (L336) ahead of /5 — so its snowfall has block 3's keyframes (snowOne/snowTwo/snowThree). The restored file differs from the pre-wave bytes only in the usage-sweep exhibit lines, and the checker's profile returned to the pre-wave baseline (all class (ii), no class (i) before or after). This package was rebuilt from the post-repair canonical bytes: `candidate.txt` recopied from `pages/theme:xmas-jp.txt`, `diff.md` and the stamp regenerated. The regenerated stamp reads STALE with the current file sha256 — no re-judgement is fabricated and the frozen GOSIGN2 ledger remains the verdict record.

## Change set outside the two diffed files

The diff covers two files; the port's record is one file larger. `pages/theme-decoration-sample-xmas-jp.txt` is the decoration sample the render checks ran against (its findings are the sample half of section 11(2)); it belongs to this theme's record but carries no port change of its own to explain here. The theme layers over no base candidate; the Black Highlighter companion named in its examples is the production scp-jp page, not a companion file in this repo.
