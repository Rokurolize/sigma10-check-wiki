# Review package — theme:retrofutura-jp (EN → JP port)

<!-- BEGIN GENERATED VERDICT STAMP — do not hand-edit; regenerate with review/build_review.py -->
## Verdict stamp
- Theme: theme:retrofutura-jp — origin EN, population #131 [GOSIGN2-LEDGER (b) row 131]
- Overall: STALE — candidate file changed since the verdict was computed (verdict against 435a6bb-era content, file sha256 now 0685277161047ead9ebbd307c6877ee667040068a7bfb8301d1c37b51429e3cb); the verdicts below were computed against that pre-change file, and the record verdict stands: a candidate revised through the campaign's recorded repairs is posted like a PASS row, with the change recorded in its package
- T1 (source check): FINDINGS (classified) — baseline 2026-11-16: exit 1, 2 errors / 1 warn / 1 info (pseudo-ref×2); standing classes dispositioned in register c1 [T1-ROWS row 126; GOSIGN2-LEDGER (b) row 131]
- T2/T3 (render, combined verdict): FINDINGS — [combined T2/T3] report `FINDINGS` — page T2 no machine verdict (exit 2); sample credit-modal (preview-form) + page-overflow 582–592px@320/375 + runtime-hotlink site-theme chain. [RENDER-ROWS-2 (RENDER-S2-C (EN18))]
- Engine coverage: full matrix as run by the lane; coverage not separately caveated in the row (the row records inconclusive runs, carried verbatim above) [RENDER-ROWS-2 row]
- Credit modal: sample credit-modal errors dispositioned preview-form (credit:start-preview has no modal mechanism; GOSIGN-TESTS T2 amendment, 2026-11-16) [RENDER-ROWS-2 (RENDER-S2-C (EN18))]
- T4 (localize patterns + follow-up): FINDINGS — display-affecting findings: 2 [LOCALIZE-ROWS row 131, source LOCALIZE-S2-C]
- T5 (translation text): FINDINGS — the source reports judge T4/T5 jointly; one verdict word covers both [LOCALIZE-ROWS row 131]
- FIX5 re-judgement: none — no OPEN items at the ledger determination [GOSIGN2-LEDGER (b) row 131]
- Computed against: canonical commit b5cb7241f527a44933e45599b41df210690771c4; candidate file pages/theme:retrofutura-jp.txt sha256:0685277161047ead9ebbd307c6877ee667040068a7bfb8301d1c37b51429e3cb; record: GOSIGN2-LEDGER.md + GOSIGN2-LEDGER-SUPPLEMENT.md as of the FIX5 head 435a6bb
<!-- END GENERATED VERDICT STAMP -->

## Status

| | |
|---|---|
| Verdict | **PASS** — passed at the ledger determination; this theme had no OPEN items and no §(e) register entry (GOSIGN2-LEDGER (b) row 131) |
| Standing items | **DISPOSITIONED** — T1 pseudo-ref ×2 (class (iii), section 11); the render row's items (exit-2 coverage caveat, KB-32 / KB-33 / KB-34 / KB-40, section 11); T4's P1 charge DISPOSITIONED (posting-procedure convention class). One item is flagged in the per-theme record: the usage exhibit's self-reference names the plain slug |
| Go-sign basis | COMPLETION-REPORT.md §10 (go-sign issued; 81 FIXED / 26 DISPOSITIONED / 0 OPEN across the sweep) |
| Named exception | None for this theme (the sweep's single named exception is theme:amethyst-v2, which has no candidate) |

## Provenance

| | Original | Candidate |
|---|---|---|
| Page | theme:retrofutura | theme:retrofutura-jp |
| Wiki | scp-wiki.wikidot.com | SCP-JP Sigma-10 candidate (canonical repo) |
| Reference revision | 18 (first translation; the candidate's credit block records 初訳時参照リビジョン: 18) | — |
| Source of this copy | Campaign cache `gosign2-lanes/lane-oc-gs-localize-s2-C/orig-retrofutura.txt`, via the mirror store (class COPY, hash-verified against review/sources.tsv) | Canonical file `pages/theme:retrofutura-jp.txt`, copied at worktree HEAD 5506feb |
| Lines / bytes | 647 lines / 17,029 bytes | 659 lines / 18,069 bytes |
| SHA-256 | 8bd0c83ccf02e4cc2a6bb6cf5e3724f533be99020dc351c730f3dd77062aabc8 | fc0c949477980d93e837e1dda16b77a6f1505615dece4c8667bf679421ad32c6 |

Wave history: the candidate was created by the Stage 2 EN18 integration (commit 3c1bcdf, the LOCALIZE-S2-C wave's port). Two later wave commits touch the file: 666f543 (FIX2-CREDIT, credit-missing-fields completions) added six of the eight credit fields, and 1cdad38 (FIX4-SIGMA) unified the sigma-plus include to its -jp form. No FIX5 commit touches this file, because the theme had no OPEN items for FIX5 to re-judge.

## Summary

A small, standard port (11 classifier change blocks, the fewest in this batch) whose interest concentrates at the head and tail: the original delivers itself from a tail module and carries its credit as a bare Rate plus license-box includes, while the candidate rebuilds the head as the wave-standard frame (sigma-plus-jp include, draft-host self-delivery, interwiki-style frame), installs the preview credit block, and renders the license entries as a plain blockquote div. The CSS body is carried essentially untouched apart from the font-variable stacks. T4's only charge against this theme was the sigma-plus dependency (pattern 1), dispositioned under the posting-procedure convention and later overtaken in part by FIX4-SIGMA, which delivered the JP component port and unified the include. One flag is recorded in the per-theme record: the usage exhibit's include names `:scp-jp:theme:retrofutura`, the plain slug, where the candidate's posting name is theme:retrofutura-jp.

## Class summary

Auto-classification by review/classify_hunks.py (signature table 2026-11-17.1): 11 change blocks — 5 specific (45.5%), 5 heuristic (45.5%), 1 residue (9.1%), 0 skipped. Pattern citations below name the KB entry; the patterns/ tree state cited throughout is commit 9c5e9079afb01d30cb9fc4ef9d714e5591eb2ffa.

| Label | Blocks |
|---|---|
| EXHIBIT-RESTRUCTURE | 3 |
| TRANS-UNANCHORED | 5 |
| CREDIT-PREVIEW | 1 |
| DRAFT-HOST | 2 |
| FONT-IMPORT | 1 |
| IFTAGS | 1 |
| JPFONT-LOAD | 1 |
| SELF-DELIVERY | 2 |
| SIGMA-PLUS-JP | 2 |
| TASL-FIELDS | 1 |
| TRANSLATION-ANCHORED | 1 |
| CSS-BODY | 1 |

Adjudication for this README (every block was read against the bytes): the three EXHIBIT-RESTRUCTURE primaries resolve as a prose translation around a surviving exhibit (B4, section 6), the license entries' form change (B10, section 1), and the tail delivery's relocation to the head (B11, section 3) — none is a dropped exhibit. The one CSS-BODY block (B8) is a P7 font-stack rewrite in the `:root` variable definitions (section 4). The one residue block (B2) is an alignment artefact pairing the deleted bare-Rate line with the usage-exhibit line; the Rate deletion itself is section 1's. After adjudication no block is left unexplained.

## Standing sections

### 0. Header and provenance frame

- **What:** Theme theme:retrofutura-jp; original theme:retrofutura on scp-wiki at reference revision 18; candidate `pages/theme:retrofutura-jp.txt`. Provenance route: derived from the original at the reference revision by the LOCALIZE-S2-C wave (sources.tsv kind: standard; no production JP counterpart exists for this theme, so the R4 adoption question does not arise). The frame itself moved: the original opens with its tag gate `[[iftags +theme]]` (original L1) and delivers its CSS from a tail module (original L641–647); the candidate opens with the delivery frame (candidate L1–11) and places the localized gate `[[iftags +テーマ]]` after it (candidate L13).
- **Why:** Section 0 declares the provenance route so every later count is read against the right baseline; the gate's tag is P2 (iftags tag localization), the frame is P4/P6 (section 3).
- **Verify:** The sources.tsv row for retrofutura-jp; `sha256sum original.txt` against the Provenance table.
- **Disposition:** Standing (the route itself); the gate and frame changes are recorded in section 3.

### 1. Credit and attribution

- **What:** The original's credit furniture is a centered bare `[[module rate]]` (original L2–4) and, at the tail, a `:scp-wiki:component:license-box-theme` / `license-box-end` include pair (original L627, L635) wrapping one image-license entry set (bannerfutura.png, The wub, CC BY-SA 4.0, Wikimedia Commons source). The candidate deletes the Rate and installs the JP form: a `:scp-jp:credit:start-preview`/`end-preview` block (candidate L14–23) carrying the eight ruling-3 fields （タイトル Retro Futura Theme; 翻訳責任者 AI; 翻訳年 2026; 原題 Retro Futura Theme; 著作権者 [[*user Fish^12]]; 作成年 2025; 初訳時参照リビジョン 18; the source link, host-verified in section 7). Two fields （初訳時参照リビジョン and 元記事リンク） date from the creation; the other six were completed by FIX2-CREDIT (commit 666f543, the population credit-missing-fields wave). The named author matches the original's own prose credit ("the theme was created by engineer [[*user Fish^12]]", original L8), so no attribution is dropped or reassigned. The license entries survive with their content translated, but their form changes: the two license-box includes are deleted and the entries render as a plain `[[div class="blockquote"]]` with translated field labels (candidate L649–658). T7 credit CSS: no supplement was added; the one credit-adjacent rule in the CSS (`div.page-rate-widget-box, div.rate-box-with-credit-button`, original L420) is inherited byte-identical (candidate L442).
- **Why:** P3/T1: the preview credit module is the rate-bearing JP form, so the bare Rate is deleted rather than duplicated (the KB-09 duplicate-Rate failure is what a kept Rate would become). Ruling 3 fixes the eight fields; `credit-missing-fields` is a T1 class (i) charge, and FIX2-CREDIT is the wave that closed it population-wide. The license-box form follows KB-60 (license-box form uncertainty): the entries' content is the attribution record, and it is preserved in full; the foreign license-box includes cannot render on scp-jp in their `:scp-wiki:` form.
- **Verify:** `grep -n 'module rate\|license-box' candidate.txt` returns nothing; read candidate L14–23 against the eight fields; read candidate L649–658 against original L627–635.
- **Disposition:** FIXED in substance (credit fields completed by FIX2-CREDIT, commit 666f543). The theme's ledger §(c3) line records no P3 clause for this theme, because no pattern-3 charge stood in its LOCALIZE row; the completion is a population-wave act, evidenced by the commit, not by the (c3) line — recorded here so the two records are not read as contradicting each other.

### 2. Includes and components

- **What:** Four include changes. (1) sigma-plus: the original's tail include `:scp-wiki:component:sigma-plus` (original L638) becomes the head include `[[include component:sigma-plus-jp]]` (candidate L1) — the JP port of the component, delivered in this repo (`pages/component:sigma-plus-jp.txt`). The creation wrote the bare form `component:sigma-plus`; FIX4-SIGMA (commit 1cdad38) unified it to the -jp form per KB-64/KB-15. (2) toggle-sidebar: `:scp-wiki:component:toggle-sidebar` (original L639) → `:scp-jp:component:toggle-sidebar` (candidate L6). (3) interwiki-style: `:scp-wiki:component:interwiki-style` (original L644) → the unprefixed same-site form `[[include component:interwiki-style` (candidate L8), its `theme=` repointed in section 3. (4) The license-box pair is deleted (section 1). The credit includes complete the candidate's list; every live include in the candidate names a `:scp-jp:` target or the unprefixed same-site form of a page the JP environment carries.
- **Why:** P1 (KB-15): an include must name the JP counterpart that actually exists on scp-jp; a kept `:scp-wiki:` include is a foreign-include error, class (i). Ruling 4: the sigma-plus component the theme needs was ported alongside (component:sigma-plus-jp), so the include names the port, not the EN original. The unprefixed interwiki-style form is the same-site convention the LOCALIZE row noted under pattern 1/6; it resolves on the wiki the candidate is posted to.
- **Verify:** `grep -n '\[\[include' candidate.txt` — six includes (L1, L6, L8, L14, L23, and the exhibit at L34); `ls pages/component:sigma-plus-jp.txt`.
- **Disposition:** Applied. T4's pattern-1 charge (the sigma-plus include rendering nothing on scp-jp, LOCALIZE-ROWS row 131) is DISPOSITIONED in the ledger (P1, posting-procedure convention class, GOSIGN2-LEDGER §(c3)); the include half of it was subsequently closed in fact by FIX4-SIGMA. The prose-link half is section 7's.

### 3. Delivery and code loading

- **What:** The original delivers its own CSS from the tail: a `[[module css]]` importing `scp-wiki.wdfiles.com/local--code/theme%3Aretrofutura/1` (original L642), with the interwiki-style include naming the same /1 delivery as its `theme=` (original L644–646). The candidate moves the delivery to the head (blocks B1/B11): a `[[module CSS]]` importing the candidate's own `local--code/theme%3Aretrofutura-jp/1` from the draft host (candidate L3), and the interwiki-style include at priority 1 with `theme=` naming the same draft-host /1 delivery (candidate L8–11). The classifier's topology pass records `external_own_delivery: true` and no component moves: the code block itself stays in place (original L67–624 → candidate L88–646); only the delivery module relocates. The two draft-host lines are the theme's T1 pseudo-ref ×2.
- **Why:** P4/T9 (own-code delivery served from JP hosts) and P6/T3 (the interwiki-style supplement frame, priority 1 for the theme's own layer — the original already carried the frame at priority 1, so the port preserves the original's own layering rather than inventing one). The draft-host form of the live lines is KB-41, class (iii): sanctioned at draft stage, rewritten to the production host at posting.
- **Verify:** `grep -n 'local--code' candidate.txt` — L3 and L10, both draft-host, both the candidate's own /1.
- **Disposition:** DISPOSITIONED (draft-host lines, class (iii)).

### 4. Fonts and assets

- **What:** Load (block B7): the original's four `@import`s from fonts.bunny.net (original L74–77 — Josefin Sans, Nunito, Teachers, Major Mono Display, each `:400`) are replaced by five Google Fonts `@import`s at the head of the code block (candidate L95–99): the same four families, plus Noto Sans JP (400;700). Stacks: every `font-family` declaration in the CSS goes through the four variables `--jose` / `--nuni` / `--teac` / `--majo`, whose definitions are the one CSS-BODY block (B8, original L92–95 → candidate L114–117): each gains `"Noto Sans JP"` and a generic fallback (`sans-serif`; `monospace` for `--majo`, preserving the original's mono role). No other stack changes: the specimen spans in the body name the same variables on both sides. Assets: one image URL moves — the header background `bannerfutura.png`, from `scp-wiki.wikidot.com/local--files/theme:retrofutura/` to the draft host's `local--files/theme%3Aretrofutura-jp/` folder, file name unchanged (block B9, original L252 → candidate L274).
- **Why:** P7/T5 with KB-16 (the font load gap): the Latin display faces have no kana glyphs, so the JP face is loaded and every stack that can render Japanese text gains it — here the stacks live in the variable definitions, which is why the classifier's CSS-BODY heuristic, not its stack signature, fired; the change is a P7 stack rewrite in substance. The bunny.net → Google Fonts host change is P5/KB-17: both are allowlisted font hosts, and the load follows the campaign's standard JP font route. The asset move is P5 (the theme's own image re-hosted to the JP side; draft-host form, class (iii)).
- **Verify:** `grep -n '@import' candidate.txt` — five lines, all fonts.googleapis.com; read candidate L114–117 against original L92–95; `grep -n 'bannerfutura' candidate.txt` — one hit, draft host.
- **Disposition:** Font load and stacks applied; the draft-host asset URL is DISPOSITIONED (class (iii) draft form; posting rewrites it to the production host).

### 5. Header, sidebar, and site furniture

- **What:** No change block fires for this section, and the bytes bear that out with one nuance: the candidate overrides the same two header variables the original does — `--header-title: "Nautilus"` and `--header-subtitle: "Mobilis in Mobili"` (original L97–98 → candidate L119–120) — carried byte-identical, because the lines are unchanged they form no change block. Both values are the theme's proper nouns (the Nautilus and its motto), not prose awaiting translation. The sidebar is the toggle-sidebar component swap of section 2; no P8 layout adaptation was needed.
- **Why:** P9/T6 variables are present in the original and preserved; header and title language as a translation-taste question is ruling 2 territory, out of scope for migration correctness, and these two values are names, not sentences.
- **Verify:** `grep -n -- '--header-' candidate.txt` — two lines, identical to the original's.
- **Disposition:** Standing.

### 6. Text translation

- **What:** The body prose is translated throughout, in the counted groups the classifier gives: five TRANS-UNANCHORED blocks (B3, B4's prose half, B6, and the single-line translations among B1/B10/B11's spans) and one TRANSLATION-ANCHORED block (B5: the four font-specimen spans, original L49–52 → candidate L68–71, family names kept, sentences translated). The heading "+ WHAT THE FUCK ARE YOU LOOKING AT?" becomes "+ 何見てんだよ？" (candidate L25), register preserved. Block B4 (original L8–20 → candidate L37–39) is the prose around the usage exhibit — the "Besides that…" paragraphs, translated and slightly compressed — not an exhibit change: the exhibit itself survives at candidate L34 (section 2's flag concerns its target name, not its presence). No COMMENT-TEXT blocks fire: the CSS carries no translated comments in this theme. No reader-visible string is left in English outside quotations of proper nouns (the team name at candidate L27 is carried as the original's styling writes it, inside a translated sentence).
- **Why:** P10 (body, usage, and sample translation is the port's purpose) and KB-18 (reader-visible strings). The unanchored group is where a silent deletion would hide, which is why B4 was read against the exhibit census rather than waved through under its EXHIBIT-RESTRUCTURE primary.
- **Verify:** The pairs are diff.md's body sections in order; an English-prose scan of candidate.txt returns only the proper nouns named above.
- **Disposition:** Standing (the port itself); no untranslated reader-visible text remains outside the named quotations.

### 7. Links

- **What:** Three link items. (1) The credit block's source link (candidate L21) names `https://scp-wiki.wikidot.com/theme:retrofutura` — the original's recorded host (review/sources.tsv `original_url`), so the host check passes and no probe was triggered. (2) The prose link `[[[component:sigma-plus|Sigma Plus]]]` (candidate L29): the LOCALIZE row charged this link dead (pattern 1 — the EN component page name on the JP wiki); FIX4-SIGMA's commit records that prose links were deliberately left as links when the includes were unified, and the ledger dispositions the theme's P1 under the posting-procedure convention. (3) The prose link `[[[component:toggle-sidebar|トグル式サイドバー]]]` (same line) names the component the candidate itself includes in its `:scp-jp:` form at L6, so its target exists in the JP environment. The contest link in the intro prose (candidate L27) keeps its scp-wiki host: it is an external event reference, not a page dependency, and no record charges it.
- **Why:** P11: prose links take the JP counterpart or the serving original, under the dead-reference evidence standard. Item (2) is the one link whose target page, under its posting name (component:sigma-plus-jp), differs from the name the link writes; the campaign's recorded handling is the FIX4-SIGMA decision plus the P1 disposition, and this package carries both openly rather than silently passing the link.
- **Verify:** `grep -n 'component:sigma-plus' candidate.txt` — the include at L1 (-jp form) and the link at L29 (plain form); `git show 1cdad38` for the wave's stated scope.
- **Disposition:** DISPOSITIONED (item 2: ledger P1, posting-procedure convention class; the FIX4-SIGMA scope note is the operative record). Items 1 and 3 standing.

### 8. Structure

- **What:** The localize.md closing rule holds. Variable names, selectors, and channel order are preserved; the code block sits where the original's sits (original L67–624 → candidate L88–646), and the JP corrections arrive at the head (frame, credit) rather than interleaved into the inherited CSS. Two structural events, both named: the delivery module relocates from the tail to the head (section 3), and the license entries change container (license-box includes → blockquote div, section 1) with their content preserved. An exhibit census confirms the rest: the usage exhibit, the four font-specimen spans, the panelbox exhibits, and the code exhibit are present on both sides in the same order. The three EXHIBIT-RESTRUCTURE primaries adjudicate to B4 (prose translation, section 6), B10 (the license form change), and B11 (the delivery relocation) — no exhibit was dropped or replaced, so the R3 question (sanctioned replacement vs silent deletion) does not arise for this theme.
- **Why:** R3 exists to force exactly this adjudication, because a restructure and a deletion share a diff shape and ledger class I charges the silent form; here the census, not the label, decides.
- **Verify:** Compare `grep -n '\[\[tab\|\[\[code\|\[\[include\|\[\[div' original.txt candidate.txt` — the sequences correspond.
- **Disposition:** Standing; no structural deletion, no class I item.

### 9. Formatting only

- **What:** None. The classifier finds no whitespace-only block and no re-indentation (0 and 0) in this pair, so the R7 follow-up-diff hazard is not triggered.
- **Why:** Formatting churn is disclosed as its own class so it is never mistaken for a semantic change.
- **Verify:** The classifier summary in classification.json (`reindent_blocks: 0`, no WS-ONLY label).
- **Disposition:** None required.

### 10. Porter annotations

- **What:** None. An explicit check of the candidate finds no `[!-- ... --]` porter comment and no editor line with no original counterpart; the classifier's ANNOTATION signature does not fire. (The skeleton's silence for this section survives contact with the bytes.)
- **Why:** R2: porter-added text is part of the change record; here there is none to record.
- **Verify:** `grep -n '\[!--' candidate.txt` returns nothing.
- **Disposition:** Standing.

### 11. Dispositions and exceptions

- **What:** Three items, each with its ground. (1) T1's two pseudo-ref errors: class (iii) draft form shading into (ii) — they are the candidate's own draft-host local--code lines (sections 3–4); the posting procedure rewrites them, and fix lanes never "fix" them in the candidate. (2) The render row's items, all environment or capture layer, not charged to the candidate: the page's T2 run returned no machine verdict (exit 2 — a coverage caveat, not a result); the sample's credit-modal errors (KB-32: the preview form has no modal mechanism, ruling 5); the sample's page-overflow 582–592px at 320/375 (KB-33/KB-34 cross-cutting families); and the runtime-hotlink site-theme chain (KB-40). (3) T4's P1 charge (the sigma-plus dependency, LOCALIZE-ROWS row 131, display-affecting count 2 covering the include and the link): DISPOSITIONED under the posting-procedure convention (GOSIGN2-LEDGER §(c3)); the include half was later closed in fact by FIX4-SIGMA (section 2), the link half stands on the disposition (section 7).
- **Why:** A disposition is a decision with grounds (AGENTS.md §3 classes (i)/(ii)/(iii); the named KB entries), not an omission; environment-layer lines are recorded as not-charged.
- **Verify:** Each item names its deciding record above and in the per-theme record.
- **Disposition:** DISPOSITIONED (all three items).

### 12. Verification

- **What:** (a) T1 source check (T1-ROWS row 126): exit 1, 2 errors / 1 warn / 1 info; both errors are pseudo-ref, class (iii); there is no class (i) error. (b) T2/T3 render (RENDER-ROWS-2, lane RENDER-S2-C (EN18)): FINDINGS, the items of section 11(2), all dispositioned; the page run's exit 2 is recorded as a coverage caveat in the row itself. (c) T4/T5 (LOCALIZE-ROWS row 131): FINDINGS jointly, display-affecting findings 2 (the pattern-1 pair); the ledger §(c3) line records the theme's T4 outcome as P1 DISPOSITIONED. (d) This package is self-verifying: `python3 review/build_review.py --check` regenerates diff.md and the verdict stamp from the two byte-faithful copies in this directory and compares. Counts in this README are the generator's (difflib, autojunk off): +63/−51 in 11 classifier change blocks / 7 diff hunks.
- **Why:** Verification claims name the cheapest deciding check and its result, not a general assurance.
- **Verify:** Re-run the checker on `pages/theme:retrofutura-jp.txt` and `python3 review/build_review.py --check` in this repo.
- **Disposition:** PASS (GOSIGN2-LEDGER (b) row 131; go-sign, COMPLETION-REPORT §10).

## Per-theme record

### The usage exhibit's self-reference (flagged)

The usage exhibit at candidate L34 reads `> {{@@[[include :scp-jp:theme:retrofutura]]@@}}` — the include a user is told to paste names the theme's plain slug on scp-jp, where the candidate's posting name is theme:retrofutura-jp. The original's exhibit names `:scp-wiki:theme:retrofutura` (original L15), which is that page's real name on its own wiki, so the port's repoint changed the site prefix and kept a name that, on the target wiki, will not be the posted page's name. Probes made for this package (2026-11-17): both `https://scp-jp.wikidot.com/theme:retrofutura` and `https://scp-jp.wikidot.com/theme:retrofutura-jp` return 404 today, because the theme is not yet posted in either name; the probe therefore cannot decide the point, and the flag rests on the posting-name convention, the same ground on which the M-pure-3 batch flagged five instances of this shape (cmst, cleaning-services, construct, cosmos, cyber-specter) and a population sweep is repairing the family. This package does not edit the candidate; the flag is recorded so the sweep's list is complete. The ledger's P1 disposition for this theme (posting-procedure convention) predates the sweep's naming finding and does not name this line; the two records are carried together here rather than either being hidden.

### The credit completion the (c3) line does not mention

The theme's §(c3) line records only the P1 disposition, yet the credit block's six missing fields were completed by FIX2-CREDIT (commit 666f543, visible in the diff of that commit for this file). The explanation is the wave's shape: FIX2-CREDIT was a population completion (36 themes) that filled missing fields wherever the checker found them, charged or not, while the (c3) lines record outcomes against each theme's own charged items, and no pattern-3 charge stood in this theme's LOCALIZE row. The bytes and the commit agree; only the (c3) line's silence could mislead, so it is noted here.

## Appendix — residue blocks

| Block | Span | Resolution |
|---|---|---|
| B2 | orig 3-3 → cand 34-34 | Alignment artefact: the aligner pairs the deleted bare-Rate line's position (original L3) with the usage-exhibit line (candidate L34). The Rate deletion is section 1's change; the exhibit line is section 2's. No unexplained content. |

## Change set outside the two diffed files

The diff covers two files; the port's record is larger by the companions the campaign built around this theme. `pages/theme-decoration-sample-retrofutura-jp.txt` is the decoration sample the render checks ran against (its findings are the sample half of section 11(2)); it belongs to this theme's record but carries no port change of its own to explain here. `pages/component:sigma-plus-jp.txt` is the JP port of the component this theme depends on, delivered under ruling 4 and included at candidate L1 (section 2). There are no companion fragments and no inbound-link repairs in other candidates for this theme.

## License and attribution

- **Title:** Retro Futura Theme
- **Author:** Fish^12
- **Source:** https://scp-wiki.wikidot.com/theme:retrofutura — revision 18
- **License:** Creative Commons Attribution-ShareAlike 3.0 (CC BY-SA 3.0) — license deed: https://creativecommons.org/licenses/by-sa/3.0/
- **Adaptation:** This package holds a Sigma-10 migration port of the work; changes were made. See "Summary" and "Standing sections" in this README for what changed and why. Translator: AI (Muse and its delegated agents), per the campaign's standing attribution rule.
