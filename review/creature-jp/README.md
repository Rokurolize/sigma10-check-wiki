# Review package — theme:creature-jp

<!-- BEGIN GENERATED VERDICT STAMP — do not hand-edit; regenerate with review/build_review.py -->
## Verdict stamp
- Theme: theme:creature-jp — origin KO, population #257 [GOSIGN2-LEDGER (b) row 257]
- Overall: PASS — NOT PASS at the ledger determination (section (e) register); its one OPEN item re-judged DISPOSITIONED with grounds by the FIX5 wave; go-sign issued 2026-11-17 (COMPLETION-REPORT §10) [GOSIGN2-LEDGER (b); GOSIGN2-LEDGER-SUPPLEMENT (d)]
- T1 (source check): FINDINGS (classified) — baseline 2026-11-16: exit 1, 4 errors / 3 warns / 1 info (hotlink×2, pseudo-ref×2); standing classes dispositioned in register c1 [T1-ROWS row 240; GOSIGN2-LEDGER (b) row 257]
- T2/T3 (render, combined verdict): FINDINGS — [combined T2/T3] report `FINDINGS` — page runtime-hotlink incl. cdn.jsdelivr.net + scpko.wdfiles.com; sample credit-modal (preview-form) + runtime-hotlink (one combo http.cat among other hosts); T3 oversized circular SCP PARK header art wider than the mobile viewport, lettering cut at the edges at 375/320 (both engines). [RENDER-ROWS-2 (RENDER-S2-H (KO2))]
- Engine coverage: full matrix as run by the lane; coverage not separately caveated in the row [RENDER-ROWS-2 row]
- Credit modal: sample credit-modal errors dispositioned preview-form (credit:start-preview has no modal mechanism; GOSIGN-TESTS T2 amendment, 2026-11-16) [RENDER-ROWS-2 (RENDER-S2-H (KO2))]
- T4 (localize patterns + follow-up): FINDINGS — display-affecting findings: 2 [LOCALIZE-ROWS row 256, source LOCALIZE-S2-F]
- T5 (translation text): FINDINGS — the source reports judge T4/T5 jointly; one verdict word covers both [LOCALIZE-ROWS row 256]
- FIX5 re-judgement: item 104 (class F) DISPOSITIONED — FIX5-FUNC §7 (no edit): header-art rules candidate L67-92 byte-identical to original L70-95 (diff IDENTICAL); fixed-width circular specimen art is the original's design in both versions [GOSIGN2-LEDGER-SUPPLEMENT (a) item 104]
- Computed against: canonical commit 1869877ffdcd33cb214b8dc421fb39e3de8d7e8d; candidate file pages/theme:creature-jp.txt sha256:f63912aa79328aaef3cd2068472b866c49e5307d44555ace945709c5ef471c41; record: GOSIGN2-LEDGER.md + GOSIGN2-LEDGER-SUPPLEMENT.md as of the FIX5 head 435a6bb
<!-- END GENERATED VERDICT STAMP -->


Status: complete — hand-written explanation below; the generated verdict stamp above is the campaign record, and this package's own per-theme record re-derives the theme's one FIX5 disposition from the packaged bytes
Candidate: review/creature-jp/candidate.txt (sha256 f63912aa79328aaef3cd2068472b866c49e5307d44555ace945709c5ef471c41)
Original: theme:creature — scpko, revision 4 (sha256 27967b8a218248b46bc273ae04c68f3e9376111144b09142088dee0b001aead0)
Classifier: classify_hunks.py 0.1.0; signature table 2026-11-17.1; patterns commit 9c5e9079afb01d30cb9fc4ef9d714e5591eb2ffa

## Provenance

- Original (theme:creature): https://scpko.wikidot.com/theme:creature — origin scpko, reference revision 4 (revision id not exposed by wikidot.py; the mirror class is the provenance).
- Candidate (theme:creature-jp): pages/theme:creature-jp.txt — no production JP counterpart; the port is the campaign's own.
- Kind: K5b-3 (SPECIAL-ROWS) — the candidate layers over the JP base candidate theme:anniversary-jp; the original layers over theme:anniversary the same way. The package diff covers the theme's own layer only; the base layer is theme:anniversary-jp's own package.
- Mirror: review-mirrors/store/creature__scpko__r4.txt, class COPY (byte-true copy of the S2 cache artifact), SHA-256 verified equal to the sources.tsv row at package build.
- Provenance route: derived from the original at the reference revision. The follow-up diff artifact (diff-creature-from4.txt) records upstream rev 4 to rev 4, no changes; the mirror is the current upstream text as well as the reference text.

## Summary

A small KO contest theme (151 lines) ported onto its JP base candidate. The port swaps the credit block for the JP preview form with a full TASL field set, deletes the info-module pair (its content carried into the body as translated prose), localizes the tag gate, translates the body, repoints the Wikipedia reference from the KO to the JA edition, and restructures delivery: the original's hidden-div inline modules become a code exhibit plus a tail delivery module importing the base and the theme's own code block from the draft host. The theme's CSS body is otherwise byte-identical to the original's, including the header-art rules whose identity is the ground of the theme's one FIX5 disposition (item 104, re-derived in the per-theme record). The byte pass also found four defects the campaign record does not settle (a dropped :root override, a dropped live component include, three dead reference links, a credit title field that ignores the body's own Japanese form) and one minor defect (a duplicated font load across the delivery chain); all five are flagged in the per-theme record with evidence, and the candidate is packaged as it stands.

## 0. Header / provenance

- Delivery: the classifier's topology pass registers no components in the original and reports "no relocation"; the bytes disagree. The original's two delivery modules are `[[module CSS show="true"]]` blocks nested inside a hidden div (orig L31-42 and L42-150), which the component census does not register. The candidate's components are a code-css block (cand L37-147) and a tail module-css (cand L152-155). The restructure is real and is argued from the bytes in section 3; the skeleton's "no relocation" line is a census blind spot, recorded here so no reader relies on it.
- The theme's own layer is small: one @font-face, the header-art rules, and a handful of overrides over the anniversary base. Everything the port changed sits in the page furniture around that layer and in the delivery form.

## Class summary

| Label | Blocks |
|---|---|
| COLON-ENC | 1 |
| CREDIT-PREVIEW | 1 |
| CREDIT-PROSE | 1 |
| DELIVERY-HOST | 1 |
| DRAFT-HOST | 2 |
| EXHIBIT-RESTRUCTURE | 1 |
| IFTAGS | 2 |
| INFO-DEL | 2 |
| JPFONT-LOAD | 1 |
| LINK-REPOINT | 1 |
| SELF-DELIVERY | 2 |
| TASL-FIELDS | 1 |
| TRANS-UNANCHORED | 6 |
| TRANSLATION-ANCHORED | 3 |

Counts: 14 blocks, 9 specific, 3 heuristic, 2 residue, 0 skipped (comment text).

## 1. Credit and attribution

- B2 (orig L3-4 -> cand L3-12, CREDIT-PREVIEW + TASL-FIELDS + CREDIT-PROSE). What: the original's `:scpko:info:start` / `info:end` credit pair is replaced by the JP environment's `credit:start-preview` / `credit:end-preview` pair, and the credit body becomes the eight-field TASL set (cand L4-11): タイトル 괴수공원 테마, 翻訳責任者 AI, 翻訳年 2026, 原題 괴수공원 테마, 著作権者 thd-glasses, 作成年 2023, 初訳時参照リビジョン 4, 元記事リンク https://scpko.wikidot.com/theme:creature.
  Why: pattern 3 (P3/T1) — the branch-original credit module does not render in the JP environment; the preview form is the rate-bearing JP form (KB-32). The field set is the campaign's TASL record (owner ruling 3 of 2026-11-16).
  Verify: grep the candidate for `credit:start-preview`; the T1 checker resolves the include on scp-jp.
  Judgment: the author field is right — 著作権者 thd-glasses matches the original's own credit (製作 [[*user thd-glasses]] at orig L6, repeated in the banner and the image-source line at orig L14). The source link's host is right: scpko.wikidot.com is the recorded host in sources.tsv, not the dead scp-wiki-ko.wikidot.com of the 2a8a125 family. The title field is not right: it copies the Korean title although the candidate's own body gives the Japanese form 怪獣公園テーマ at cand L14; flagged as defect C4 in the per-theme record (the steam-guide / voyager / animal shape: where the body supplies a Japanese form, the field follows it).
  Disposition: ledger (c3) P3 FIXED for this theme; the closure settles the block's presence and form. It does not settle the title field's value, which is why C4 stands as a flag rather than a contradiction of the closure.
- B6 (orig L13-15 -> cand L23-24, INFO-DEL). What: the info pair's closing half is deleted; the pair's content (the font source at orig L10-12, the image authorship at orig L13-14) is carried into the candidate body as translated plain prose (cand L20-24), outside any module.
  Why: pattern 3's second half — the info module is not part of the JP environment's furniture; its content is attribution data, so it is preserved as prose rather than dropped.
  Verify: grep the candidate for `info:start` / `info:end` (zero); read cand L20-24 against orig L10-14 (the noonnu.cc font-page link and the thd-glasses image credit both survive).
  Disposition: part of the same (c3) P3 closure as B2.

## 2. Includes and components

- B1 (orig L1 -> cand L1, IFTAGS). What: the page gate localizes, `[[iftags +테마]]` -> `[[iftags +テーマ]]`.
  Why: pattern 2 (KB-08) — iftags conditions name JP tags in the JP environment; a KO tag condition would never fire on scp-jp.
  Verify: KB-08 recipe — every iftags condition in the candidate names JP tags (the one surviving gate does; the original's second, negative gate is gone with the hidden div, below).
  Disposition: pattern 2 applied by the localize lane (LOCALIZE-S2-F verdicts); no separate ledger item.
- The include census, from the bytes: the candidate's includes are the credit pair (section 1), the tail interwiki-style include (section 3), and nothing else. The original carries one further live include the candidate does not: `:scpko:component:collapsible-topbar` with three parameters (orig L25-29). Its deletion is classifier block B10 and is argued as a structure question in section 8; it is defect C2 in the per-theme record. The original's hidden div also carried a negative tag gate (`[[iftags -테마]]` inside the div tag at orig L31) that has no counterpart; it gated only the original's inline delivery, which the candidate replaces wholesale (section 3), so its absence is part of that restructure, not a separate drop.

## 3. Delivery and code loading

- B11 (orig L31-42 -> cand L36-39, DELIVERY-HOST primary; IFTAGS and JPFONT-LOAD spans inside). What: the original's first inline module (orig L32-40: an @import of theme:anniversary/1 from scpko.wdfiles.com, then a :root override block) is replaced at the head of the candidate's code exhibit by the porter's Noto Sans JP @import (cand L38) and a section banner comment (cand L39). The anniversary import itself reappears in the tail delivery module (B13), repointed to theme:anniversary-jp/1 on the draft host.
  Why (the repoint): pattern 4 — delivery is served from the JP environment's hosts, and the base is the JP base candidate under owner ruling 1 of 2026-11-16 (cross-theme imports repoint to the JP fixed base candidate).
  Verify: the tail module's two @imports (cand L153-154) name theme%3Aanniversary-jp/1 and theme%3Acreature-jp/1 on sigma10-jp-test.wdfiles.com; both are the population's draft-stage form (section 11).
  Judgment, and a defect: the repoint is right, but the original module's second half did not survive it. The :root override at orig L35-39 (`--color-bg: #222; --color-ip: #222; --font: #FFF;`) has no counterpart anywhere in the candidate (grep-verified). It is not subsumed by the base: theme:anniversary-jp defines --color-bg as #B01 (its L492) and --color-ip as #000 (its L493), so the candidate renders the base's red background variable where the original's design is charcoal #222. The localize lane charged exactly this as a display-affecting regression (配色退行) under its structural verdict; the ledger's P10 disposition ground does not address it. Flagged as defect C1 in the per-theme record.
- B13 (orig L150 -> cand L152-155, SELF-DELIVERY). What: the candidate's live delivery is a tail `[[module css]]` importing the base's and its own code blocks from the draft host; the original has no tail module (its delivery was the inline modules of B11/B12's region).
  Why: the population's delivery form for a ported theme — the CSS lives in a [[code]] exhibit and is delivered by module import, where the original delivered inline from a hidden div.
  Verify: the candidate has exactly one code block (cand L37-147, `[[code type="css"]]`, counted over every code-block form); the tail module's own address /1 names it, and it is the stylesheet (the theme's whole CSS layer), so the navla-style mis-address (a small exhibit named while the stylesheet sits elsewhere) does not arise. Brace-depth scan: the code block's CSS ends at depth 0 and never goes negative.
  Disposition: the draft-host form is class (iii), posting rewrites it (section 11).
- B14 (orig L151 -> cand L156-159, SELF-DELIVERY). What: the interwiki-style frame include is added in the candidate's form (priority=1, theme=theme%3Acreature-jp/1 on the draft host); the original's last line is the hidden div's close.
  Why: the population's dual-channel form — the frame carries the same code block for the interwiki rendering path.
  Verify: read cand L156-159; the theme argument names the same /1 block as B13's import.

## 4. Fonts and assets

- The JPFONT-LOAD span inside B11 (cand L38). What: `@import url('https://fonts.googleapis.com/css2?family=Noto+Sans+JP:wght@400;700&display=swap')` is added at the head of the delivered code block.
  Why: pattern 7 (KB-16) — a JP font load for the JP environment.
  Verify and judgment: the load sits in the delivered channel (the head of code block /1), not in an inert exhibit. Two qualifications, both recorded rather than charged. First, no font-family stack in creature's own CSS names Noto Sans JP — the theme does not override the body font, so the load is a supplement the base chain may or may not consume; the localize lane marked pattern 7 APPLIED-partial with "unused" noted, and the ledger charged no P7 item for this theme. Second, the identical URL is also loaded by theme:anniversary-jp's own code block (its L66, inside the block creature's tail module imports), so the delivered chain loads the same stylesheet twice; flagged as minor defect C5 (the vanguard-supplement shape).
- B12 (orig L96 -> cand L93, COLON-ENC). What: inside the delivered CSS, the creature.png URL's page name is colon-encoded: `theme:creature` -> `theme%3Acreature`.
  Why: KB-01 — a raw colon in a local--files path segment breaks the address.
  Verify: the pair differs only by the %3A encoding.
  Disposition: the asset's host stays scpko.wdfiles.com; that is the (c3) P5 disposition, class (ii) / KB-58 (section 11).
- The FUNFLOWSURVIVORKR @font-face (orig L43-48 = cand L40-45, unchanged region). The theme's display face stays on its cdn.jsdelivr.net/gh delivery in both versions; the (c3) P4 disposition covers it as delivery class (ii) (section 11). It is named by the header-art rules and loads in both versions identically.

## 5. Header, sidebar, site furniture

none — no signature for this section fired over 14 change blocks, and the ground is checkable: the theme has no header-variable surface and no sidebar rules of its own. Its header surface is the header-art rule set (the circular SCP PARK wordmark), which is byte-identical on both sides; that identity is measured in the per-theme record, because it is the ground of item 104. The one header-adjacent loss, the :root color override, is a dropped CSS block and is argued where the classifier put its lines, in section 3 (defect C1).

## 6. Text translation

- B3 (orig L6 -> cand L14, TRANSLATION-ANCHORED). What: the info block's title line and its 製作 (by) line become the body's title line **怪獣公園テーマ** (cand L14) and **作者:** [[*user thd-glasses]] (cand L16, paired by the aligner into residue B4).
  Why: pattern 10 (KB-18) — reader-visible text localizes; the pairings are one-to-one.
  Verify: read the pairs; the author value is unchanged, only its label localizes.
- B8 (orig L19-21 -> cand L28-30, TRANSLATION-ANCHORED with a LINK-REPOINT span). What: the reference-themes list heading and its two entries are translated (参考テーマとコンポーネント：, 年末コンテストテーマ, 折り畳み式トップバー). The link targets do not change; the LINK-REPOINT signature fired because link-bearing lines changed. The targets are the subject of section 7.
- B5 (orig L10 -> cand L18-20, TRANS-UNANCHORED). What: the font-source heading and its noonnu.cc link line translate, and the Jurassic Park inspiration line (orig L8) lands here in the alignment (cand L18) with its Wikipedia target repointed from the KO edition to the JA edition.
  Why: pattern 10 translation; the repoint is pattern 11's JP-counterpart rule applied to a reference encyclopedia (the JA article is the same film's article).
  Verify: read cand L18-21 against orig L8-12; the noonnu.cc/font_page/1037 link is byte-identical.
- B7 (orig L17 -> cand L26, TRANS-UNANCHORED). What: the contest line translates: [[[11thanniversarycontest|韓国語版SCP財団11周年年末コンテスト]]]専用CSSテーマです。 The label now says what the link is (the Korean branch's contest); the target does not change. The target is probed in section 7.
- The remaining TRANS-UNANCHORED mass is the CSS-comment and prose translation inside the restructured regions, resolved by shape in the appendix. No untranslated reader-visible KO prose remains in the candidate body (the credit title field at cand L4 is the one Korean string left standing, and it is defect C4, not untranslated prose: the field's own 原題 twin at cand L7 carries the same string deliberately).

## 7. Links

- The Jurassic Park repoint (orig L8 -> cand L18): ko.wikipedia.org -> ja.wikipedia.org, argued in section 6 (B5). Stands.
- The credit source link (cand L11): https://scpko.wikidot.com/theme:creature — host matches the original's recorded host in sources.tsv. Stands; not the dead-host family.
- Three reference links name pages that do not exist on scp-jp (probed 2026-11-17 for this package; the localize lane probed the same three on 2026-11-16 with the same result):

  | Candidate line | Target as written | scp-jp | scpko (same name) |
  |---|---|---|---|
  | cand L26 | 11thanniversarycontest | 404 | 200 |
  | cand L29 | theme:anniversary | 404 | 200 |
  | cand L30 | component:collapsible-topbar | 404 | 200 |

  Why this is a flag and not a disposition: the ledger's (c3) P11 ground is "sibling / batch-posting class" — references that resolve when a sibling port is posted. None of the three is that shape. The anniversary reference names the plain page while the candidate's own delivery imports theme:anniversary-jp (drift: the file's delivery layer uses the -jp page). The contest page is a KO-branch page with no JP counterpart in the population, and its own label already calls it the Korean version, so the population's form is the absolutized, annotated link (the pattern 11 annotation branch, as applied to fandom's Fandation link). The topbar reference names the component whose include was dropped (defect C2). Flagged together as defect C3 in the per-theme record; the candidate is packaged as it stands.

## 8. Structure

- B10 (orig L25-29 -> cand L34, EXHIBIT-RESTRUCTURE primary, heuristic). Exhibit decision, argued from the mirror: DROPPED, not replaced — and the classifier's label misdescribes the block. The removed lines are not an exhibit; they are the original's live include of `:scpko:component:collapsible-topbar` with its maxw / top-color / top-bg parameters (orig L25-29), standing outside the gate in the page body. The candidate body still lists the component as a dependency (cand L30) but no include of it exists anywhere in the candidate. No `component:collapsible-topbar-jp` exists in the repo to repoint to (the only collapsible-topbar-adjacent page is fragment:collapsible-sidebar-jp-base-css). The localize lane marked its pattern 1 N-A while recording this deletion as an unreported type-1 staff-consultation item; the ledger carries no P1 or P8 line for this theme, so no disposition names the drop. Owner ruling 4 of 2026-11-16 (a component a theme needs is ported together with the theme) was the remedy applied to the same shape elsewhere (rima's excerpts-tool); it was not applied here. Defect C2 in the per-theme record.
- B9 (orig L23 -> cand L32, residue). What: the original closes its page gate mid-file (orig L23) and delivers the rest ungated; the candidate keeps the whole page inside one gate and closes it at cand L150, and the added side of the pair is the `----` separator before the source-code section (cand L32).
  Why: a consequence of the delivery restructure (section 3): the code exhibit and its collapsible sit inside the gate with the body they document.
  Verify: grep the candidate for `[[/iftags]]` (one occurrence, cand L150); the original has its close at L23.
  Judgment: the gate's coverage changed (the original's include and delivery stood outside it), but everything the candidate gates is theme-page furniture that only a theme page renders, so the wider gate is the population's form and is not charged.

## 9. Formatting only

- WS-ONLY blocks: 0. Re-indentation pairs: 0. There are no formatting-only blocks; every whitespace difference rides inside a block argued above.

## 10. Porter annotations

- One annotation, riding inside B11: the section banner comment `/* ===== creature ===== */` at cand L39, at the head of the delivered CSS where the original's module 2 opened directly with the @font-face. It is a porter-added signpost inside the delivered channel; it states nothing about the port, so there is nothing for the bytes to refute. No other porter annotations exist in the candidate (checked explicitly over the whole file, per the standing rule that annotations hide inside other labeled blocks).

## 11. Dispositions and exceptions

- Item 104 (class F) DISPOSITIONED — the theme's one (e) item; re-derived and argued in full in the per-theme record. Ground in one line: the header-art rules the T3 check charged are byte-identical on both sides, and fixed-width circular specimen art is the original's design in both versions.
- (c3) P4 DISPOSITIONED, delivery class (ii): the FUNFLOWSURVIVORKR @font-face delivery via cdn.jsdelivr.net/gh is the original's own channel, kept identically (section 4). Posting does not rewrite a third-party CDN the original itself chose.
- (c3) P5 DISPOSITIONED, class (ii) / KB-58: creature.png stays on scpko.wdfiles.com (section 4, B12). The asset host is a posting matter under the campaign's asset rules, recorded, not edited.
- (c3) P10 DISPOSITIONED, "lane-recorded severity / specimen class": the ground holds for the specimen half (the header art, item 104) and fails for the structural half — the lane's own structural verdict charged the :root color regression as display-affecting, and the disposition's stated ground does not address it. The package therefore carries the disposition for the art and defect C1 for the override; the two halves are separable because the art's identity is measured independently (per-theme record).
- (c3) P11 DISPOSITIONED, "sibling / batch-posting class": the ground does not produce the three plain-name references at posting (section 7); carried as defect C3 rather than as a disposition the bytes support.
- T1 standing classes (register c1): the baseline's 2 hotlink errors are the jsDelivr font delivery and the scpko asset above (class (ii)); its 2 pseudo-ref errors are the draft-host local--code imports (the sanctioned draft-stage form). No class (i) error stands.
- T2 credit-modal line: the sample's credit-modal errors are the preview form's property (credit:start-preview has no modal mechanism; GOSIGN-TESTS T2 amendment, 2026-11-16; KB-32) — uniform across the population, not a theme defect.
- T2 runtime-hotlink line: class (ii), the same hosts as the P4/P5 dispositions.

## 12. Verification

- T1 (source check): baseline 2026-11-16, exit 1, 4 errors / 3 warns / 1 info (hotlink x2, pseudo-ref x2) [T1-ROWS row 240]. FIX5-FUNC re-ran the checker for item 104 and recorded before error 4 / warn 3 / info 1, after identical — the disposition's no-edit claim is itself checker-verified.
- T2/T3 (render): FINDINGS with two DISPOSITIONED members (runtime-hotlink; credit-modal preview-form) and item 104 [RENDER-ROWS-2, RENDER-S2-H (KO2)]. The re-derivation of item 104 from this package's bytes is in the per-theme record.
- T4 (localize patterns): FINDINGS, display-affecting findings 2 [LOCALIZE-ROWS row 256, source LOCALIZE-S2-F]; verdicts in the ledger (c3) row and section 11 above.
- T4 follow-up diff: the S2 artifact records upstream rev 4 to rev 4, no changes; the mirror is current.
- T5 (translation text): judged jointly with T4 by the source lane; the candidate-side residue is defect C4 (a field value, not prose).
- Package checks, run at build: candidate.txt byte-identical to pages/theme:creature-jp.txt (cmp); original.txt SHA-256 equal to the sources.tsv row; CSS brace-depth scan ends at depth 0 in every block on both sides; `python3 review/build_review.py --check` passes for this package.

## Per-theme record — theme:creature-jp

### Verdict chain

- Ledger (b) row 257: NOT PASS. (c2) RENDER-S2-H (KO2): two DISPOSITIONED (runtime-hotlink class (ii); credit-modal preview-form) and one OPEN item, (e) item 104. (c3) LOCALIZE-S2-F: P3 FIXED; P4, P5, P10, P11 DISPOSITIONED.
- FIX5 re-judgement (supplement (a) item 104, class F): DISPOSITIONED with grounds — FIX5-FUNC section 7 (no edit).
- Go-sign: issued 2026-11-17 (COMPLETION-REPORT section 10) over the population with this item dispositioned. The generated stamp above reads PASS for this theme, and it is not STALE: the candidate's bytes are the verdict's bytes (the stamp's computed-against commit 1869877 is the last commit touching the candidate).

### Item 104 re-derived from this package's bytes

The disposition's claim (FIX5-FUNC section 7): the header-art rules at candidate L67-92 are byte-identical to original L70-95 (its checker line: before error 4 / warn 3 / info 1, after identical, because no edit was made).

Measured here: the two regions were extracted from original.txt (L70-95) and candidate.txt (L67-92) and hashed. Both are 26 lines; SHA-256 eb9be173614079a4889f490cb649b2543a681d28cd7608122b3fdf6aa02c0318 on both sides. The region is the `div#header-extra-div-2` rule set: the fixed-width circular frame (width 20rem, border-radius 50%) carrying the SCP PARK wordmark (the `content: "SCP PARK"` rule stands inside it). The T3 finding was that this art is wider than the mobile viewport with its lettering cut at 375/320 in both engines; since the charged rules are byte-identical and neither version carries a mobile scale-down, the finding describes the original's design, not a port regression. CONFIRMED, exactly as stated.

### Second-reviewer walk

The walk re-read the disposition as a reader who did none of the work. Item 104's ground passes that test: it names exact lines on both sides, the claim is byte-identity, and anyone with this package can re-measure it in one command (done above). The walk then checked the disposition's neighborhood, which is where it stopped passing: the ledger's P10 line bundles the lane's structural verdict under "lane-recorded severity / specimen class", a ground a third party cannot re-derive, and the structural verdict's own text charges a color regression the bundle never mentions. The P11 line has the same shape (a class name where a checkable claim should be). The walk's outcome: item 104's disposition stands on its own measured ground; the P10 and P11 bundles do not, and their unsupported halves are the defects below. That split is the honest state of the record, and the package states it rather than smoothing it over.

### Defect flags (candidate packaged as it stands; no edits made by this lane)

- C1 — the :root override is dropped. Original L35-39 sets --color-bg #222, --color-ip #222, --font #FFF over the base. The candidate has no counterpart (grep: zero occurrences of --color-bg in the candidate). The base candidate theme:anniversary-jp defines --color-bg #B01 (its L492) and --color-ip #000 (its L493); only --font agrees (#FFF, its L494). So the port renders the base's red where the original designs charcoal. The localize lane charged this as a display-affecting regression (LOCALIZE-S2-F, KO2-4, pattern 10/structural); the ledger's P10 disposition ground states no value evidence and does not address it. Restore shape, for the coordinator: the three declarations re-enter the candidate's delivered CSS ahead of the theme's own rules, at the position the original's module 1 gave them relative to the base import.
- C2 — the collapsible-topbar include is dropped with no disposition. Original L25-29 (live include, three parameters); candidate: no include, although its body still names the component as a reference dependency (cand L30). No component:collapsible-topbar-jp exists in the repo. The localize lane recorded the deletion as an unreported type-1 staff-consultation item and marked pattern 1 N-A; the ledger has no line for it. Under owner ruling 4 the component would be ported with the theme (the rima precedent); under any reading, the drop needed a recorded disposition and has none.
- C3 — three reference links are dead on scp-jp. Cand L26 (11thanniversarycontest), L29 (theme:anniversary), L30 (component:collapsible-topbar): probed 2026-11-17, all 404 on scp-jp, all 200 on scpko under the same names (the localize lane's 2026-11-16 probes agree). The P11 "batch-posting" ground does not cover them: anniversary is drift (the file's own delivery uses theme:anniversary-jp), the contest link's label already says Korean version (the absolutized annotated form is the population's), and the topbar link names C2's dropped component.
- C4 — the credit title field ignores the body's Japanese form. Cand L4 タイトル reads 괴수공원 테마, identical to the 原題 field (cand L7), while the candidate's own body title (cand L14) is 怪獣公園テーマ. The population's rule (steam-guide, voyager, animal): where the body supplies a Japanese form, the field follows it.
- C5 (minor) — Noto Sans JP is loaded twice across the delivery chain. Cand L38 loads the css2 URL (family=Noto+Sans+JP:wght@400;700) at the head of creature's code block; theme:anniversary-jp's code block loads the identical URL at its L66, and creature's tail module imports anniversary-jp/1 before creature-jp/1, so both loads fire on every delivery. The vanguard-supplement shape; the remedy there was removal of the supplement's duplicated loads after verifying the parent chain delivers them.

### Record items (verified, not flags)

- The Noto Sans JP load is named by no font-family stack in creature's own CSS; the theme does not set the body font. Recorded by the localize lane (pattern 7 APPLIED-partial, "unused" noted); no ledger item charges it. It is not a wholesale font-program substitution: the theme's one display face (FUNFLOWSURVIVORKR) is carried identically.
- The candidate's self-delivery address /1 names its only code block, which is the stylesheet; the FIX-CODEADDR audit's classes do not touch this theme.
- The sources.tsv supersession note for this row is in the correct standard form and its cited artifact agrees with it (rev 4 to rev 4, no changes); no correction is recorded for the coordinator.

## Appendix — residue blocks

- R1 = B4 (orig L8 -> cand L16, no signature). Resolution: an alignment artifact of the credit swap. The aligner cross-paired the original's Jurassic Park line with the candidate's 作者 line; the true pairs are orig L6 -> cand L16 (製作 -> 作者, argued in section 6 as B3's pair) and orig L8 -> cand L18 (the Jurassic Park line, translated and repointed, argued in sections 6-7 as part of B5). No content is unaccounted for.
- R2 = B9 (orig L23 -> cand L32, no signature). Resolution: the gate-close relocation, argued in section 8.
- R3 = B5 (orig L10 -> cand L18-20, heuristic). Resolution: section 6 — the font-source heading pair plus the Jurassic Park pair the aligner folded into the same block. The "script delta without the anchor majority" note is the KO-to-JA script change doing what it should.
- R4 = B7 (orig L17 -> cand L26, heuristic). Resolution: section 6 — the contest line's translation; its target is probed in section 7.
- R5 = B10 (orig L25-29 -> cand L34, heuristic). Resolution: section 8 — the dropped collapsible-topbar include (defect C2). The classifier's "no translated counterpart" note is correct in form and wrong in implication: there is no counterpart because the include was deleted, not because it was translated away.
