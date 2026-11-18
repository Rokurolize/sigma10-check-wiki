# Review package — theme:rok-gov-theme-jp

<!-- BEGIN GENERATED VERDICT STAMP — do not hand-edit; regenerate with review/build_review.py -->
## Verdict stamp
- Theme: theme:rok-gov-theme-jp — origin KO, population #283 [GOSIGN2-LEDGER (b) row 283]
- Overall: STALE — candidate file changed since the verdict was computed (verdict against 435a6bb-era content, file sha256 now 6952a8fcc5c50b50c02e093edd76b21951820d022bc486bf95efcf8895f698e4); the verdicts below were computed against that pre-change file, and the record verdict stands: a candidate revised through the campaign's recorded repairs is posted like a PASS row, with the change recorded in its package
- T1 (source check): FINDINGS (classified) — baseline 2026-11-16: exit 1, 1 error / 2 warns / 0 infos (pseudo-ref×1); standing classes dispositioned in register c1 [T1-ROWS row 253; GOSIGN2-LEDGER (b) row 283]
- T2/T3 (render, combined verdict): FINDINGS — [combined T2/T3] report `FINDINGS` — page runtime-hotlink site-theme chain only; sample credit-modal (preview-form) + 884px@768 overflow; T3 none beyond cross-cutting items. [RENDER-ROWS-2 (RENDER-S2-H (KO7))]
- Engine coverage: full matrix as run by the lane; coverage not separately caveated in the row [RENDER-ROWS-2 row]
- Credit modal: sample credit-modal errors dispositioned preview-form (credit:start-preview has no modal mechanism; GOSIGN-TESTS T2 amendment, 2026-11-16) [RENDER-ROWS-2 (RENDER-S2-H (KO7))]
- T4 (localize patterns + follow-up): FINDINGS — display-affecting findings: 1 [LOCALIZE-ROWS row 282, source LOCALIZE-S2-F]
- T5 (translation text): FINDINGS — the source reports judge T4/T5 jointly; one verdict word covers both [LOCALIZE-ROWS row 282]
- FIX5 re-judgement: none — no OPEN items at the ledger determination [GOSIGN2-LEDGER (b) row 283]
- Computed against: canonical commit 967ec2f4a240dfaf825b2c3152610ed8c4a23b5a; candidate file pages/theme:rok-gov-theme-jp.txt sha256:6952a8fcc5c50b50c02e093edd76b21951820d022bc486bf95efcf8895f698e4; record: GOSIGN2-LEDGER.md + GOSIGN2-LEDGER-SUPPLEMENT.md as of the FIX5 head 435a6bb
<!-- END GENERATED VERDICT STAMP -->

## Status

| | |
|---|---|
| Verdict | **PASS** — passed at the ledger determination; this theme had no OPEN items and no §(e) register entry (GOSIGN2-LEDGER (b) row 283). The stamp reads STALE because one line changed after the verdict (the usage sweep, per-theme record below); the verdict lines describe the pre-change file |
| Standing items | **DISPOSITIONED** — T1 pseudo-ref ×1 (class (iii), section 11); the render row's items (runtime-hotlink chain, credit-modal preview form, sample overflow, section 11); T4's component-availability and default-title items (P1 / P9, sections 7 and 5). **FIXED** — the missing interwiki-style frame (P6, FIX4-IWA, section 3) |
| Go-sign basis | COMPLETION-REPORT.md §10 (go-sign issued; 81 FIXED / 26 DISPOSITIONED / 0 OPEN across the sweep) |
| Named exception | None for this theme (the sweep's single named exception is theme:amethyst-v2, which has no candidate) |

## Provenance

| | Original | Candidate |
|---|---|---|
| Page | theme:rok-gov-theme | theme:rok-gov-theme-jp |
| Wiki | scpko.wikidot.com | SCP-JP Sigma-10 candidate (canonical repo) |
| Reference revision | 81 (first translation; the candidate's credit block records 初訳時参照リビジョン: 81) | — |
| Source of this copy | Campaign cache `gosign2-lanes/lane-oc-gs-localize-s2-F/orig-rok-gov-theme.txt`, via the mirror store (class COPY, hash-verified against review/sources.tsv) | Canonical file `pages/theme:rok-gov-theme-jp.txt`, copied at worktree HEAD 2aee861 |
| Lines / bytes | 8 lines / 280 bytes | 93 lines / 4,043 bytes |
| SHA-256 | 915d334aba8727adc155b08baa656b6e735cd02065362f67fd013fb9180e2bb8 | 1bcbe3b79f9ccb599624be5602ec400b068d867b0639f4877ef4f15a937fb64d |

Wave history: the candidate was created by the Stage 2 KO7 integration (commit 6889a0a); the rework2-p5 pass (b89741d) built the Sigma-9 base family receivers including this theme's companion component; FIX-CREDIT-D (1869877) normalized its credit attribution; FIX4-IWA (8c62b7b) added the interwiki-style frame the T4 record found missing; the usage sweep (b5cb724) made the one post-verdict line change recorded below.

## Summary

A shell theme: the original page's entire body is one parameterized include of a component, and the component carries all of the CSS. The candidate keeps that two-layer structure exactly — the include target becomes the JP port of the component (ported with the theme, ruling 4) and every parameter line is byte-identical — and adds the JP page furniture around it: the interwiki-style frame, the tag gate, the preview credit block, a translated introduction and specimen body, and a license box whose entries disclose what the original left unstated (the images' license is not recorded in the original; the font substitution is named). The substantive CSS port lives in the companion file, not in this diff (change-set section). Measured churn (diff.md, the generator's difflib count with autojunk off: +81/−1 in 2 change blocks / 2 hunks; the −1 is the include line itself, replaced).

## Class summary

Auto-classification by review/classify_hunks.py (signature table 2026-11-17.1): 2 change blocks — 2 specific (100%), 0 heuristic, 0 residue, 0 skipped. Pattern citations below name the KB entry; the patterns/ tree state cited throughout is commit 9c5e9079afb01d30cb9fc4ef9d714e5591eb2ffa.

| Label | Blocks |
|---|---|
| COMPONENT-SWAP | 1 |
| CREDIT-PREVIEW | 1 |
| DRAFT-HOST | 1 |
| EXHIBIT-RESTRUCTURE | 1 |
| IFTAGS | 1 |
| INCLUDE-REPOINT | 1 |
| LICENSE-BOX | 1 |
| TASL-FIELDS | 1 |
| TRANS-UNANCHORED | 1 |

Adjudication for this README (both blocks were read against the bytes): B1's EXHIBIT-RESTRUCTURE primary is the include line's repoint (COMPONENT-SWAP / INCLUDE-REPOINT), not a restructuring — the original has no exhibits. B2 is the entire supplement body arriving as one block because the original has no body to diff against; its labels (CREDIT-PREVIEW, TASL-FIELDS, IFTAGS, LICENSE-BOX, DRAFT-HOST, TRANS-UNANCHORED) are adjudicated section by section below. The skeleton's "none" for section 2 does not survive contact with the bytes: the include repoint is this package's central change and is recorded in section 2. After adjudication no block is left unexplained.

## Standing sections

### 0. Header and provenance frame

- **What:** Theme theme:rok-gov-theme-jp; original theme:rok-gov-theme on scpko at reference revision 81; candidate `pages/theme:rok-gov-theme-jp.txt`. Provenance route: derived from the original at the reference revision by the Stage 2 KO7 wave (sources.tsv kind: K5b-1 — the theme page is a shell whose whole body is one cross-wiki component include, `:scpko:component:rok-gov-base`; the component is the substantive original and was ported with the theme as `component:rok-gov-base-jp`). The original is eight lines: the include head (original L1) and six parameter lines (L2–7) with their defaults, the last left open (`|page-title={$page-title}`, L7) ahead of the include close (L8). The candidate preserves those eight lines in place (candidate L1–8) and puts the frame before the gate (candidate L10–15).
- **Why:** Section 0 declares the provenance route so every later count is read against the right baseline; for a shell theme it also declares where the substance lives, so the small diff is not mistaken for a small port.
- **Verify:** The sources.tsv row for rok-gov-theme-jp; `sha256sum original.txt` against the Provenance table; read original L1–8 against candidate L1–8.
- **Disposition:** Standing (the route itself); the frame is section 3, the gate is P2 (section 2's include list completes the furniture).

### 1. Credit and attribution

- **What:** The original carries no credit furniture on this page at all — no Rate module, no info block; its credit lives inside the component. The candidate adds the JP form inside its gate: a `:scp-jp:credit:start-preview`/`end-preview` block (candidate L17–26) carrying all eight ruling-3 fields (title 大韓民国政府 テーマ（国家初像防災院）; 翻訳責任者 AI; 翻訳年 2026; 原題 대한민국 정부 테마 (국가초상방재원 테마); 著作権者 [[*user thd-glasses]]; 作成年 2020; 初訳時参照リビジョン 81; the source link, section 7). A JP license box closes the body (candidate L78–91, `:scp-jp:component:license-box-backend` with `author=thd-glasses`): three entries — the four image files (author thd-glasses; license recorded honestly as not stated in the original, with a confirm-with-the-author note; source the scpko file area), the component entry (the CSS lives in `component:rok-gov-base-jp`; license follows the original component's statement), and the font entry (the original's noonnu-distributed faces and jsDelivr woff are replaced on the JP side by Gothic A1 and Noto Sans/Serif JP — the loads themselves are in the companion). No T7 credit-module CSS sits on this page; the companion carries its own inherited credit-box rules as part of its CSS port.
- **Why:** P3/T1 for the credit block (the preview module is the rate-bearing JP form; the original had no Rate here to delete, so KB-09 does not arise). T4 for the license box: the original states no per-image license, and the box records that absence as a pre-posting confirmation item instead of inventing one — attribution the reviewer can check, not attribution theatre. The author field matches the only attribution the original side makes (thd-glasses, in the component's header and its image note).
- **Verify:** Read candidate L17–26 against the eight fields; read candidate L78–91; the companion's header comment (`pages/component:rok-gov-base-jp.txt` L1–7) names the same author and the same font substitution.
- **Disposition:** FIXED (GOSIGN2-LEDGER §(c3): P3 credit fields FIXED, credit waves, checker-verified); the license box's two "confirm before posting" notes are standing pre-posting items, recorded here and in section 11.

### 2. Includes and components

- **What:** One repoint, and it is the port: original L1 `[[include :scpko:component:rok-gov-base` → candidate L1 `[[include :scp-jp:component:rok-gov-base-jp`. The six parameter lines and the include close are byte-identical on both sides (alt, format-disable, header=npes, title, subtitle, page-title). The candidate's remaining includes are the frame (candidate L10, section 3), the credit pair (L17, L26), and the license-box pair (L78, L91) — every include in the candidate names a `:scp-jp:` target, and the usage example (candidate L33) names this candidate itself in its post-sweep form.
- **Why:** P1 (KB-15) for the include form; ruling 4 / T8 for the substance: a theme whose body is a component include is not ported until the component is, so `component:rok-gov-base-jp` was ported alongside (614 lines in `pages/`) rather than left as a foreign include. T4's type-1 finding (the component candidate 404 on scp-jp at measurement time) is the posting-state half of the same point and is recorded in section 11.
- **Verify:** `grep -n '\[\[include' candidate.txt` — five includes plus the escaped usage line, all `:scp-jp:`; `ls pages/component:rok-gov-base-jp.txt` in this repo.
- **Disposition:** Applied; the component's posting state is section 11, item 2.

### 3. Delivery and code loading

- **What:** This page holds no CSS of its own, and its delivery arrives by two routes. (1) The include itself: the companion's live `[[module CSS]]` (companion L21) applies to any page that includes the component, with the include's parameters substituted into its variables (the companion's `--title: "{$title}"` form). (2) **Frame paragraph (the M-frame addition):** the candidate's frame (candidate L10–13) is an interwiki-style include at `priority=1` whose `theme=` names the companion's code address on the draft host, `https://sigma10-jp-test.wdfiles.com/local--code/component%3Arok-gov-base-jp/1`. That address is the companion's only `[[code]]` block (companion L482–546): the GoI-format additional CSS, whose conditional live copy is the companion's `show="false"` module immediately after it. The frame's form differs from the sibling themes' for a structural reason: the theme page has no code page of its own to name, so the frame names the companion's. The T4 record found no frame at all (LOCALIZE-ROWS row 282, type 6); FIX4-IWA (commit 8c62b7b) installed this one, and the ledger records P6 FIXED. The T3 catalogue's listing of this theme as a frame exception refers to the target being the companion's code rather than the page's own, not to a missing frame.
- **Why:** P6/T3 (KB-07): the frame is what lets a page using this theme pull the theme layer through the interwiki-style mechanism with an explicit priority; priority 1 because this port adds exactly one layer and there is no base-theme layer beneath it to order against. The draft-host form of the `theme=` URL is KB-41, class (iii): sanctioned at draft stage, rewritten to the production host at posting.
- **Verify:** Read candidate L10–13; count the companion's code blocks (`grep -n '\[\[code' pages/component:rok-gov-base-jp.txt` — one, at L482); the frame's presence is the FIX4-IWA hunk in commit 8c62b7b.
- **Disposition:** FIXED (P6, FIX4-IWA); the draft-host URL is DISPOSITIONED (class (iii)).

### 4. Fonts and assets

- **What:** None on this page, by structure: the page holds no font load and one image. The specimen body shows the NPES logo from the candidate's own draft-host file area (candidate L43, `npes-logo-small0.png`). The font change itself — the original component's noonnu-distributed EBSHMJESaeronRA face and jsDelivr woff replaced by Google Fonts loads of Gothic A1, Noto Sans JP, and Noto Serif JP — is executed in the companion (its module head) and disclosed on this page in the license box's font entry (candidate L89). The four image files the theme uses are listed in the license box (candidate L81) with their scpko source area; their JP-side hosting is the companion's repoint work.
- **Why:** P7/T5 and P5 are component-side changes for this theme; recording them here as pointers (rather than re-narrating the companion's diff) keeps this package's claims checkable from its own two files plus the named companion lines.
- **Verify:** `grep -n 'font\|@import' candidate.txt` returns nothing; the companion's module head carries the three Google Fonts imports.
- **Disposition:** Standing (pointer); the draft-host specimen image is DISPOSITIONED (class (iii) draft form).

### 5. Header, sidebar, and site furniture

- **What:** The header is the component's, and it is parameterized: the include's defaults are `header=npes`, `title=국가초상방재원` (Korean), `subtitle=National Paranormal Emergency Service` (English), carried byte-identical from the original (candidate L4–6 = original L4–6). There are no `--header-*` variable overrides on this page. T4 measured the Korean default title as its one display-affecting finding for this theme (LOCALIZE-ROWS row 282, type 9); the candidate's own 訳注 (candidate L36, section 10) tells a JP user that the defaults are the NPES set and that another agency's use means overriding `header` / `title` / `subtitle` — and warns that non-NPES header logos are not among the JP attachments, so the image must be attached first.
- **Why:** P9, dispositioned under ruling 2: header and title language is out of scope for migration correctness, and these defaults are the component's interface, not prose — changing them would change what an unparameterized include renders, away from the original's NPES default. The ledger's c3 line records P9 DISPOSITIONED on exactly this ground.
- **Verify:** Compare candidate L1–8 with original L1–8 (identical but for the include target); the c3 line is in review/AUTHORITIES/GOSIGN2-LEDGER.md §(c3) for theme:rok-gov-theme-jp.
- **Disposition:** DISPOSITIONED (P9; ruling 2).

### 6. Text translation

- **What:** The original has no body text to translate (eight lines of include machinery). The candidate's body inside the gate is the port's own JP text: the introduction (candidate L28: the theme is for Korean government agencies beginning with the NPES; all images by thd-glasses; fonts from noonnu), the usage instruction (L30) and its example (L32–34), the parameter 訳注 (L36, section 10), and the specimen set (L38–76: header sample with the logo image, horizontal-rule note, headings 1–6, blockquote, table, and the source-code collapsible at L74–76, which states that the CSS lives in the component — the honest specimen for a shell theme). Korean survives in the candidate in three places, each a quotation or an interface default: the credit block's original-title field (L21), the include's `title=` default (L5, section 5), and the license box's naming of the original component (L86, in Latin form). One translation-text observation is recorded in the per-theme record (the 防災院 rendering).
- **Why:** P10 for the body the port adds; KB-18's reader-visible test is met because every reader-visible string the port itself writes is Japanese, and the surviving Korean strings are the two recorded exceptions above.
- **Verify:** Read candidate L28–76; a Hangul scan of candidate.txt returns only L5, L21, and the credit block's original-title line.
- **Disposition:** Standing (the port itself); the default-title exception is section 5's disposition.

### 7. Links

- **What:** Three outbound links, all serving. The credit block's source link (candidate L25) names `https://scpko.wikidot.com/theme:rok-gov-theme` — the host review/sources.tsv records for the original, and the page this package's mirror was taken from; no host defect. The introduction's NPES hub link (candidate L28) names the KO branch's `npes-hub` page on scpko: the hub is a Korean-branch page with no JP counterpart, and the sentence frames it as the Korean group's page, so the link is kept as the serving original under P11's counterpart rule. The license box's source link (candidate L84) names the scpko file area the images came from.
- **Why:** P11: a prose link takes the JP counterpart where one exists and otherwise the serving original; the dead-reference standard is not engaged because nothing here is dead. T4's type-1 item was not a link on this page but the component's availability on scp-jp, recorded in section 11.
- **Verify:** `grep -n 'wikidot.com' candidate.txt` — the three links above plus the frame's draft-host URL (section 3).
- **Disposition:** Standing.

### 8. Structure

- **What:** The localize.md closing rule holds in its strongest form: the original's whole structure (one parameterized include) is preserved line for line, and everything the port adds sits outside it — the frame above the gate, the credit block, body, and license box inside it. No exhibit was dropped or replaced (the original has none); the specimen set the candidate adds is the port's own construction, and its source-code specimen deliberately points at the component instead of copying CSS into this page, so the two-layer structure the original documents is the structure the candidate keeps.
- **Why:** R3's distinction (sanctioned replacement vs silent deletion) does not arise: nothing was deleted, and the one-line diff hunk is the include target.
- **Verify:** The diff in diff.md is two hunks: the include line, and the added body.
- **Disposition:** Standing; no structural deletion, no class I item.

### 9. Formatting only

- **What:** None. The classifier finds no whitespace-only block (0 WS-ONLY), and the two change blocks are the include line and the added body; the R7 follow-up-diff hazard is not triggered.
- **Why:** Formatting churn is disclosed as its own class so it is never mistaken for a semantic change.
- **Verify:** diff.md's counts (+81/−1, 2 hunks).
- **Disposition:** None required.

### 10. Porter annotations

- **What:** One annotation, and it is load-bearing: the 訳注 at candidate L36, written by the porter and marked as a translator's note in the text itself. It explains the two-layer structure (the page includes `component:rok-gov-base-jp` with parameters, as the original does), lists the parameters and their meanings, states the NPES defaults, instructs users of other agencies to set `header` / `title` / `subtitle`, and warns that non-NPES header logos are not in the JP attachments. It rides inside B2, which is why no separate annotation signature fired for this package. The license box's component and font entries (candidate L86–89) are porter disclosure text of the same kind, placed in the license box's form.
- **Why:** R2: porter-added text is part of the change record; this note is also the only place the candidate documents its own parameter interface, which the original documented on the component side.
- **Verify:** Read candidate L36 and L86–89.
- **Disposition:** Standing.

### 11. Dispositions and exceptions

- **What:** Four items, each with its ground. (1) T1's one pseudo-ref error: the frame's draft-host `local--code` URL (candidate L12) — class (iii), draft form (KB-41); the posting procedure re-hosts it, and fix lanes never "fix" it in the candidate. (2) T4's type-1 finding: at T4's measurement, `component:rok-gov-base-jp` returned 404 on scp-jp — the theme's CSS carrier missing is a posting blocker, not a wording issue. The component candidate exists in this repo (`pages/component:rok-gov-base-jp.txt`, 614 lines, ported with the theme under ruling 4) and posts with the theme; the finding is a posting-state measurement, recorded here so the dependency is visible rather than because the candidate bytes are wrong. (3) T4's type-9 finding, the Korean default title: P9 DISPOSITIONED under ruling 2 (section 5). (4) The render row's items, all environment or cross-cutting, not charged to the candidate: the page's runtime-hotlink site-theme chain (KB-40); the sample's credit-modal errors (KB-32: the preview form has no modal mechanism, ruling 5); and the sample's 884px@768 overflow (KB-33 static credit replica family). The ledger's determination for this theme is PASS and this package does not re-open it.
- **Why:** A disposition is a decision with grounds (AGENTS.md §3 classes (i)/(ii)/(iii); the named KB entries), not an omission; environment-layer lines are recorded as not-charged.
- **Verify:** Each item names its deciding record above; the ledger §(c3) line for this theme reads P1 DISPOSITIONED / P6 FIXED / P9 DISPOSITIONED.
- **Disposition:** DISPOSITIONED (items 1–4); the frame item is FIXED (section 3).

### 12. Verification

- **What:** (a) T1 source check (T1-ROWS row 253): exit 1, 1 error / 2 warns / 0 infos; the one error is pseudo-ref, class (iii); there is no class (i) error. (b) T2/T3 render (RENDER-ROWS-2, lane RENDER-S2-H (KO7)): FINDINGS, the three items of section 11(4), all dispositioned; engine coverage as run by the lane, not separately caveated in its row. (c) T4/T5 (LOCALIZE-ROWS row 282): FINDINGS jointly, display-affecting findings 1 (the default title, dispositioned in section 5); the component-availability and frame items are sections 11(2) and 3. (d) This package is self-verifying: `python3 review/build_review.py --check` regenerates diff.md and the verdict stamp from the two byte-faithful copies in this directory and compares. Counts in this README are the generator's (difflib, autojunk off): +81/−1 in 2 change blocks / 2 hunks.
- **Why:** Verification claims name the cheapest deciding check and its result, not a general assurance.
- **Verify:** Re-run the checker on `pages/theme:rok-gov-theme-jp.txt` and `python3 review/build_review.py --check` in this repo.
- **Disposition:** PASS (GOSIGN2-LEDGER (b) row 283; go-sign, COMPLETION-REPORT §10) — for the pre-sweep file; see the per-theme record for the one later line.

## Per-theme record

### The post-verdict line (why the stamp reads STALE)

The candidate changed once after the FIX5 head: the usage sweep (commit b5cb724) corrected the escaped usage example at candidate L33 from `@@[[include :scp-jp:theme:rok-gov-theme]]@@` to `@@[[include :scp-jp:theme:rok-gov-theme-jp]]@@`, naming this candidate's actual posting name. That is the whole of the drift the stamp reports: one documentation line, no delivery, credit, or CSS change. This package documents the corrected candidate; its diff and stamp are computed against the corrected bytes, and the verdict lines under the stamp describe the file as judged, one line earlier.

### The agency name's rendering (a T5 observation, recorded not charged) Corrected after this package was built: commit 967ec2f replaced the glyphs with 国家超常防災院 in both loci; see the post-package repairs item below.

The candidate renders 국가초상방재원 as 国家初像防災院 (candidate L18, L28). The Korean is 超常 (초상: supernormal — the file's own English subtitle, candidate L6, says "National Paranormal Emergency Service"), and another candidate in this repo renders the same name 国家超常防災院 (theme:atlas-maniacus-jp). The two renderings cannot both be the established form; 初像 does not correspond to the Korean morphemes. T4/T5 judged this theme FINDINGS on the three items recorded above and the ledger determined PASS without naming this string, so this package records the observation with its evidence and makes no edit: if the coordinator's translation standard confirms 超常， the correction is two lines on this page (and the same check belongs on the sample and any page quoting the title field).

### Post-package repairs (REFRESH3-C)

The items above describe this package as built. The repairs recorded below postdate the package; `candidate.txt` has been recopied from the current canonical `pages/<fullname>.txt` and `diff.md` and the verdict stamp regenerated with `python3 review/build_review.py`, so this package now documents the post-repair candidate. The regenerated stamp reads **STALE** by design: no re-judgement is fabricated here, and the frozen ledger (`GOSIGN2-LEDGER.md` + supplement, FIX5 head 435a6bb) remains the verdict record.

**FIX-JININ — agency-name glyphs (landing 967ec2f, 2026-11-17).** `FIX-JININ.md` records that the candidate rendered 국가초상방재원 with the wrong glyphs 国家初像防災院. Commit 967ec2f corrected 2 occurrences to the population's established 国家超常防災院 (as in theme:atlas-maniacus-jp, agreeing with the file's own English subtitle "National Paranormal Emergency Service"): candidate L18 (credit title field) and L28 (NPES hub link text). The earlier record item that records the wrong rendering describes the as-built state; the delivered candidate carries the correction. T1 before/after identical (1/0/0).

## Change set outside the two diffed files

The diff covers two files; this port's substance lives in a third. `pages/component:rok-gov-base-jp.txt` (614 lines) is the JP port of `:scpko:component:rok-gov-base`, ported with the theme under ruling 4: it carries the live module CSS (with the font substitution and asset repoints recorded in section 4), the GoI-format code block the frame names (section 3), and its own header comment recording its provenance (the original component, via theme:rok-gov-theme rev 81's include). `pages/theme-decoration-sample-rok-gov-theme-jp.txt` is the decoration sample the render checks ran against (its findings are the sample half of section 11(4)); it applies this candidate over the sample furniture. The repo also holds the original shell itself at `pages/theme:rok-gov-theme.txt` (7 lines, the `:scpko:` include form) as part of the check composition. There are no other companion fragments and no inbound-link repairs in other candidates for this theme.

## License and attribution

- **Title:** 대한민국 정부 테마 (국가초상방재원 테마)
- **Author:** thd-glasses
- **Source:** https://scpko.wikidot.com/theme:rok-gov-theme — revision 81
- **License:** Creative Commons Attribution-ShareAlike 3.0 (CC BY-SA 3.0) — license deed: https://creativecommons.org/licenses/by-sa/3.0/
- **Adaptation:** This package holds a Sigma-10 migration port of the work; changes were made. See "Summary" and "Standing sections" in this README for what changed and why. Translator: AI (Muse and its delegated agents), per the campaign's standing attribution rule.
