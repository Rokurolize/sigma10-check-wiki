# Review package — theme:night-rush-theme-jp (EN → JP port)
New to this package's shorthand? Read the notation key first: [How to read a review package](../HOW-TO-READ.md).

<!-- BEGIN GENERATED VERDICT STAMP — do not hand-edit; regenerate with review/build_review.py -->
## Verdict stamp
- Theme: theme:night-rush-theme-jp — origin EN, population #24 [GOSIGN2-LEDGER (b) row 24]
- Overall: STALE — candidate file changed since the verdict was computed (verdict against 435a6bb-era content, file sha256 now 307c983cd147b9e397eea817255ebb25fbee41e439ea9a4a9d1cf94b4dc68dd1); the verdicts below were computed against that pre-change file, and the record verdict stands: a candidate revised through the campaign's recorded repairs is posted like a PASS row, with the change recorded in its package
- T1 (source check): FINDINGS (classified) — baseline 2026-11-16: exit 1, 2 errors / 1 warn / 4 infos (http×2); standing classes dispositioned in register c1 [T1-ROWS row 24; GOSIGN2-LEDGER (b) row 24]
- T2/T3 (render, combined verdict): FINDINGS — [combined T2/T3] report `FINDINGS` — T2 incomplete (exit 2 ×6 both pages, webkit cannot reach networkidle, no summary); T3 header tagline double-struck at ≤375, notice×sidebar/clip, sample credit-modal. [RENDER-ROWS-1 (RENDER-C row 24)]
- Engine coverage: full matrix as run by the lane; coverage not separately caveated in the row (the row records inconclusive runs, carried verbatim above) [RENDER-ROWS-1 row]
- Credit modal: sample credit-modal errors dispositioned preview-form (credit:start-preview has no modal mechanism; GOSIGN-TESTS T2 amendment, 2026-11-16; ROWS-1 phrases the line bare and takes the disposition from the part header) [RENDER-ROWS-1 (RENDER-C row 24)]
- T4 (localize patterns + follow-up): FINDINGS — display-affecting findings: 1 [LOCALIZE-ROWS row 24, source LOCALIZE-B]
- T5 (translation text): FINDINGS — the source reports judge T4/T5 jointly; one verdict word covers both [LOCALIZE-ROWS row 24]
- FIX5 re-judgement: none — no OPEN items at the ledger determination [GOSIGN2-LEDGER (b) row 24]
- Computed against: canonical commit 358955eb4013dac2399c414ba8ec2a6e416a3c11; candidate file pages/theme:night-rush-theme-jp.txt sha256:307c983cd147b9e397eea817255ebb25fbee41e439ea9a4a9d1cf94b4dc68dd1; record: GOSIGN2-LEDGER.md + GOSIGN2-LEDGER-SUPPLEMENT.md as of the FIX5 head 435a6bb
<!-- END GENERATED VERDICT STAMP -->

Status: complete — skeleton by classify_hunks.py 0.1.0; every SLOT in the skeleton is resolved in the sections below and the Appendix.
Candidate: review/night-rush-theme-jp/candidate.txt (sha256 0bef43ce6574013f3c30838c36415252e0542ed1d1f53683eac4454f46534004)
Original: theme:night-rush-theme — scp-wiki, revision 31 (sha256 11e5855a6e8f50b4af5218a8f80db3ead9936d0fba2fcf4cabf35dfe60b9b369)
Classifier: classify_hunks.py 0.1.0; signature table 2026-11-17.1; patterns commit 9c5e9079afb01d30cb9fc4ef9d714e5591eb2ffa

## Status

| | |
|---|---|
| Verdict | **PASS** — passed at the ledger determination with no OPEN items (GOSIGN2-LEDGER (b) row 24); one of the 286 of 286 pass-eligible themes |
| Blocking items at ledger time | None — no section (e) items exist for this theme and the supplement carries no night-rush entries |
| Wave edits after the port | Phase 17 added the credit block's frame; Phase 22 incorporated the rev-31 re-translation drift; the T1 fix wave (b816e10) added the six missing credit fields, repointed the info includes and colon-encoded the two storage URLs; the dead-reference repair (4b52123) fixed the image-block file host; FIX3-B (6ae6516) restored the interwiki-style frame the port had dropped |
| Standing items | **DISPOSITIONED** — T1 http×2, class (ii) (ledger (c1)); the P1 usage-example form (ledger (c3)); the render family items (ledger (c2)). **Recorded, not dispositioned by name:** the T5 English exhibit labels (Per-theme record) |
| Go-sign basis | COMPLETION-REPORT.md §10 (go-sign issued; 81 FIXED / 26 DISPOSITIONED / 0 OPEN across the sweep) |
| Named exception | The theme belongs to the labelled paired Rate exhibits set (ledger (c2) preamble item 6): the bare Rate module kept beside the credit block is the sanctioned exhibit form, not a KB-09 duplication |

## Provenance

| | Original | Candidate |
|---|---|---|
| Page | theme:night-rush-theme | theme:night-rush-theme-jp |
| Wiki | scp-wiki.wikidot.com | SCP-JP Sigma-10 candidate (canonical repo) |
| Reference revision | 31 (re-translation revision, created 2022-12-20 21:40:07 UTC); the first-translation reference revision 28 is also recorded, in the candidate's credit block and in sources.tsv | — |
| Source of this copy | Fetched 2026-11-17 at rev 31 (mirror-store class FETCH-REGEN; whitespace-only against the LOCALIZE-B lane's rev-31 cache) | Canonical file `pages/theme:night-rush-theme-jp.txt`, entering the repo in commit d727e92 (canonical sources for the display-check composition); its last content change is commit 6ae6516 (FIX3-B) |
| Production counterpart | — | Production page theme:night-rush-theme exists on SCP-JP (kind K6); the migration is delivered as `pages/phase17-diff-night-rush-theme-jp.txt`; production drift recorded 一致 (matching) in the TSV |

Provenance route: adopted from the production JP translation, then updated in place. The evidence is in the bytes: the credit block names a human translator (pcysl, translation year 2022) rather than the campaign's AI credit; the CSS banner carries the production localizer's own line ("Localized by pcysl5edgo for SCP-JP", cand L147); and the delivery form (a GitHub Pages stylesheet and scp-jp-storage image files, sections 3–4) is the production page's form, not a form the campaign's porting waves produce. The two reference revisions are both real: the production translation was made from rev 28, the original then moved to rev 31 (rev29/30 by the author, a css_rules delta), and Phase 22 incorporated that drift into the candidate (Multi-wave provenance). This package's mirror is rev 31, the revision the candidate now stands on.

## Summary

The original is a Sigma-9-derived aesthetic theme that delivers its stylesheet from its own code exhibit (loaded twice, by module @import and by the EN interwiki frame) and presents a full sample body: paired Rating exhibits with an info pane, headings, an image-block, Lorem ipsum with footnotes, tables and a long tabview. The candidate is the production SCP-JP translation of that page, adopted as the migration candidate: it keeps the sample body entire, in Japanese, delivers instead from the production form (a stylesheet on scp-jp.github.io and image files on scp-jp-storage), and carries the preview credit block naming the production translator. The campaign's own edits to it are the wave edits narrated below: a credit block completed in two passes, a dropped frame restored, a foreign info-include leftover repointed, two storage URLs colon-encoded, and the rev-31 drift incorporated. Measured churn is modest (diff.md: +118/−58 in 7 hunks; the classifier counts 42 change blocks), and most of it is the sample body's translation. The two standing oddities a reviewer will spot, the English "Rating:" exhibit captions and one unregistered CSS line (`margin-right: 2em`), are recorded in the Per-theme record rather than hidden.

## Classification

| Label | Blocks |
|---|---|
| TRANS-UNANCHORED | 23 |
| TRANSLATION-ANCHORED | 7 |
| CSS-BODY | 3 |
| INCLUDE-REPOINT | 3 |
| T7-CREDIT-CSS | 3 |
| DELIVERY-HOST | 2 |
| EXHIBIT-RESTRUCTURE | 2 |
| SELF-DELIVERY | 2 |
| ASSET-REHOST | 1 |
| CREDIT-PREVIEW | 1 |
| IFTAGS | 1 |
| INFO-DEL | 1 |
| RESTORATION | 1 |
| TASL-FIELDS | 1 |

Counts: 42 blocks — 15 specific (35.7%), 25 heuristic (59.5%), 2 residue (4.8%), 0 skipped. Topology: no relocation; both sides carry a head module-css and one code-css exhibit in the same order, and the candidate adds a tail module-css (the T7 correction module, section 1). The classifier records `external_own_delivery: true`: the candidate's stylesheet is delivered from a file on the JP distribution host, not from the page's own fragments (section 3). Labels are sets per block; the per-section lists in the classifier's skeleton show each block once, under its primary label, so this README's sections were written from classification.json's label spans, not from the skeleton's section lists (the skeleton's sections 4 and 10 print "none" although the ASSET-REHOST label fired inside B9 and a porter annotation sits in residue block B36; its section 1 leads with an INFO-DEL claim the bytes contradict — see the Per-theme record).

## Standing sections

### 0. Header and provenance frame

- **What:** The original's header (L1–10) declares self-delivery and gating: a `[[module CSS]]` @import of the page's own local--code /1 (L1–3), the EN interwiki-style include at priority 1 naming the same /1 (L5–8), and the `[[iftags +theme]]` gate (L10). The candidate's header (L1–10) has the same three slots in the same order: the module @import now names the JP distribution stylesheet (L2, block B1), the frame is `:scp-jp:` and names the same stylesheet (L5–8, blocks B2/B3), and the gate is localized to `+テーマ` (L10, the IFTAGS span inside B4). Provenance route: adopted from the production JP counterpart (Provenance above); the header the differ sees is the production frame as the fix waves left it.
- **Why:** The header frame is where the original declares its delivery; P1/P2/P4/P6 rework exactly this frame for the JP environment, and each piece of it is accounted for in sections 1–3.
- **Verify:** Read original L1–10 against candidate L1–10; blocks B1–B4 in classification.json.
- **Disposition:** Recorded; the delivery reading is section 3, the frame's history is the Per-theme record (it was dropped by the port and restored by FIX3-B).

### 1. Credit and attribution

- **What:** The original has no credit block, no info module and no license box; its attribution lives in the CSS banner (orig L132–137: "Created for the SCP Wiki by Nagiros", "Obviously based on the Sigma-9 Theme for the SCP Foundation by Aelanna"). The candidate adds the preview credit block (cand L12–22, block B4): `:scp-jp:credit:start-preview` / `end-preview` carrying the ruling-3 fields — title Night Rushテーマ, translator pcysl, translation year 2022, original title "Night Rush Theme", copyright holder Nagiros, creation year 2020, the source link to the EN page, and two reference-revision lines (first-translation rev 28, re-translation rev 31). The holder matches the banner's creator exactly, and the banner's second attribution (the Sigma-9 basis, Aelanna) is carried verbatim in the candidate's banner (cand L146). The block was completed in two passes: Phase 17 added the include pair with the rev-28 and source-link lines; the T1 fix wave then added the six missing fields the localize check had charged (LOCALIZE-ROWS row 24, item (d)). The translator field names the human production translator and was not normalized to AI: FIX-CREDIT-D's 163-file normalization does not touch this file (git log), because ruling 3 keeps human translator names where they match the live JP creator. Three further blocks are the credit-module CSS (T7): B40, an in-place selector correction inside the exhibit (cand L430: the `.rate-points` selector gains a `div`, `#page-content .rate-box-with-credit-button div.page-rate-widget-box .rate-points`); B41, a credit-module supplement appended inside the exhibit's tail (cand L768–804) restating the `.creditModule` rate-box and credit-button rules in the theme's own purple (#8870df) and adding a sidebar-block background rule, signed in a CSS comment by RTa-technology; and B42, a live `[[module CSS]]` appended after the gate (cand L808–816) whose own comment states its ground: the EN theme styles the credit anchor through a `<p>` wrapper inside `.creditButton`, the JP credit module emits the anchor as a direct child, so the EN rules never match on JP, and the block retargets the anchor rule to the JP structure with the EN declarations unchanged. B42's primary label is RESTORATION; nothing deleted was restored, and this README adjudicates the block as a T7 supplement in live-module form (its label set carries T7-CREDIT-CSS), appended at the end under the localize closing rule. The bare `[[module Rate]]` is **kept** (cand L23–26), inside the body's exhibit sequence exactly as in the original: this theme is in the labelled paired Rate exhibits set (ledger (c2) preamble item 6), the standing exception under which a labelled Rate exhibit beside the rate-bearing preview credit block is a deliberate exhibit pair, not a KB-09 duplication. The info-module includes are likewise **kept**, repointed (section 2): the skeleton's INFO-DEL lead for this section ("info-module residue removed") is contradicted by the candidate's bytes (cand L32–36) and by the fix wave's diff, and is corrected in the Per-theme record.
- **Why:** P3/T1: the preview credit module is the JP environment's credit form and it is rate-bearing. Ruling 3 fixes the field set and the attribution mechanics (campaign translations to AI; human production translators keep their names). T7/KB-11/KB-12 (patterns commit 9c5e9079afb01d30cb9fc4ef9d714e5591eb2ffa): the JP credit module's DOM needs rules the branch original never shipped, or its inherited rules corrected where the JP structure differs, which is what B40–B42 each do in a different position (in place, exhibit tail, live module).
- **Verify:** Read candidate L12–22 against the eight-field list; `grep -n '著作権者\|Created for' candidate.txt original.txt` for the holder/banner match; read cand L768–816 for the two T7 supplements and B42's own comment; `git show b816e10 -- pages/theme:night-rush-theme-jp.txt` for the six-field addition.
- **Disposition:** FIXED (ledger (c3): P3 credit fields FIXED, credit waves, checker-verified). The Rate exhibit pair stands under the pattern-3 exception named in the Status table.

### 2. Includes and components

- **What:** The candidate's complete include list (grep): the JP interwiki-style (L5–8), the credit pair (L12/L22), the info trio `:scp-jp:info:start` / `more` / `end` (L32/34/36), the escaped usage include (L43), and `component:image-block` (L53). The original's list is the EN frame (L5–8), the info trio on `:scp-wiki:` (L20/22/24), the escaped usage include `:scp-wiki:theme:night-rush-theme` (L31), and the same image-block (L41). Changes: (a) the frame repointed `:scp-wiki:` → `:scp-jp:` (B2; its EXHIBIT-RESTRUCTURE primary is the standing false fire for a mere include repoint inside the header, adjudicated here as a repoint — and its history is a drop-and-restore, Per-theme record); (b) the info trio repointed (B5, labels INCLUDE-REPOINT + TRANSLATION-ANCHORED; the placeholder texts under them are translated, cand L33/L35) — this was the localize check's one display-affecting finding (LOCALIZE-ROWS row 24 item (a): P1 leftover `:scp-wiki:info:*`), fixed by the T1 fix wave; (c) the usage include rewritten to the bare same-site form `@@[[include theme:night-rush-theme]]@@` (B8, cand L43): no site prefix, and the fullname is the production page's, which exists on SCP-JP — the form the posting procedure expects for this K6 theme, whose candidate migrates the production page rather than posting beside it; (d) the image-block kept, its file argument repointed to the JP files host (B9, section 4). No `:scp-wiki:` include remains in the candidate; the only scp-wiki string left is the credit block's source-link URL (cand L21), the required ruling-3 back-reference. No component swap (T8) was needed and no foreign include is kept, so KB-15/KB-54 do not engage. Neither side carries a base-theme include: the theme is a standalone Sigma-9 derivative, so the bare sigma-plus shape (KB-64) does not occur.
- **Why:** P1: foreign-site includes are repointed to the JP counterpart that actually exists; the info trio's JP counterparts exist and render, which is why the leftover was a display-affecting defect and not a disposition. The usage form follows the include-forms-by-context convention for a same-site production fullname.
- **Verify:** `grep -n '\[\[include' original.txt candidate.txt` and compare the two lists; `grep -n 'scp-wiki' candidate.txt` (one hit, the credit source link).
- **Disposition:** The info repoint FIXED (T1 fix wave b816e10; ledger (c3) records the theme's P1 line as DISPOSITIONED for the remaining usage-form item, section 11). No include in the candidate points at an EN-wiki page.

### 3. Delivery and code loading

- **What:** The original delivers its stylesheet out of its own code exhibit: the page's single `[[code type="css"]]` block (orig L129–755) is served as its local--code /1 and loaded twice, by the module @import (orig L2) and by the frame theme= URL (orig L7). The candidate loads a file instead: both the module @import (cand L2) and the frame theme= (cand L7) name `https://scp-jp.github.io/files/theme/night-rush-theme/style0.css`, the JP distribution host. The exhibit remains on the page (cand L141–805) as the stylesheet's source text, but no line in the candidate addresses it: `grep -c 'local--code' candidate.txt` = 0, so the candidate carries no self-delivery reference for the FIX-CODEADDR census to classify (the theme is outside the audit's 258 self-delivery files, and no address can be wrong). The priority value is 1 on both sides. The topology pass records no relocation (the exhibit sits in the same position on both sides) and flags the delivery as external. This delivery form is the production page's: the adopted production translation loads the same style0.css, and the Sigma-10 candidate keeps the production delivery rather than re-pointing it at the draft host.
- **Why:** P4/T9: deliveries are served from JP hosts in this environment; scp-jp.github.io is the JP GitHub Pages distribution (the same host family that serves the JP BHL distribution). Keeping the production form is the K6 adoption's ground: the candidate's job is to migrate the production page, whose readers already load this file.
- **Verify:** Read orig L1–8 against cand L1–8; `grep -n 'local--code\|scp-jp.github.io' candidate.txt` (the github.io pair only).
- **Disposition:** Standing (the production delivery form, retained). No draft-host form arises, so no class (iii) item exists for this theme.

### 4. Fonts and assets

- **What:** Fonts: none — neither side declares a `font-family` anywhere (`grep -c 'font-family'` = 0 in both files); the theme inherits its stacks from the site theme, so no P7 supplement was owed and none exists. The skeleton's "none" for this section is right about fonts but incomplete about assets: the ASSET-REHOST label fired inside B9, and two further asset re-hosts sit inside CSS-BODY blocks. Assets: (a) the sample image-block's file (B9, orig L41 → cand L53) repointed from `scp-wiki.wdfiles.com/local--files/scp-4755/containment` to `scp-jp.wdfiles.com/local--files/scp-4755/containment`, caption and alt translated in the same line; an earlier dead-reference repair (commit 4b52123) had already corrected this argument's host form from `http://scp-jp.wikidot.com` to the wdfiles host. (b) The two CSS background images (B37/B38, orig L212/L216 → cand L224/L228): the header and icon images re-hosted from the original page's own `local--files` on scp-wiki.wdfiles.com to file-ID URLs on `scp-jp-storage.wikidot.com` (`file%3A7974444-50-9wqt/night-rush-header.png`, `file%3A7974444-51-jv2x/night-rush-icon.png`) — the production translation's JP storage copies. The classifier classes these two as CSS-BODY heuristic; by shape they are P5 re-hosts, and the ASSET-REHOST signature's failure to fire on CSS `url()` re-hosts (it fired on the image-block form in B9) is recorded as a patterns proposal in the lane report. The T1 fix wave colon-encoded both storage URLs (`file:` → `file%3A`, KB-01), which is the form now in the file. Both storage URLs keep the `http://` scheme: they are the T1 checker's two errors (section 12).
- **Why:** P5/KB-17 (patterns 9c5e907): reader-loaded files are re-hosted to SCP-JP storage; only storage, Google Fonts, BootstrapCDN and cdnjs may be hotlinked, and the original page's EN files host is none of those. KB-01: an unencoded colon in a `local--files` file argument does not serve; the encoded form is the serving form. The http scheme is a posting-procedure rewrite, class (ii), so the candidate keeps it (ledger (c1) http entry).
- **Verify:** `grep -n 'local--files' candidate.txt` (three hits: L53 wdfiles https, L224/L228 storage http, colons encoded); `grep -n 'local--files' original.txt` (the EN forms at L41/L212/L216).
- **Disposition:** Re-hosts standing (production form); colon encoding FIXED (T1 fix wave); the http scheme DISPOSITIONED class (ii) (ledger (c1); LOCALIZE-ROWS row 24 item (e), whose vendored cell truncates at "http storage …" — Per-theme record).

### 5. Header, sidebar, site furniture

- **What:** No HEADERVAR or furniture signature fired, and inspection mostly agrees: the theme declares no `--header-title` / `--header-subtitle` / `--logo` variables on either side (grep: none), and the header, top-bar and sidebar rules inside the exhibit are carried in the original's order. Two furniture-adjacent changes exist and are accounted for where they sit: the rev-31 drift incorporated by Phase 22 added top-bar rules to the exhibit (`#top-bar ul li ul li:last-of-type a` and the sfhover pair — the re-translation revision's own CSS delta, not a JP adaptation), and the T7 supplement block at the exhibit's tail carries one sidebar rule (`#side-bar .side-block { background-color: #121212 !important; }`, cand L803–805, inside B41). No JP-specific layout adaptation (P8) was charged by any register, and the mobile `.open-menu a` rule is carried verbatim inside the exhibit (cand L158–165 region, matching orig L147–154).
- **Why:** P9/T6 variables exist to be overridden where the JP environment requires it; this theme declares none, so there is nothing to override. The two changes above are a follow-up delta (P10's currency rule: the candidate stands on the current reference revision) and a credit-supplement passenger, not furniture rework.
- **Verify:** `grep -n -- '--header-title\|--header-subtitle' candidate.txt original.txt` (none in either); `git show d2a9dc0 -- pages/theme:night-rush-theme-jp.txt` for the drift's top-bar rules.
- **Disposition:** Standing; no furniture item was charged for this theme in any register.

### 6. Text translation

- **What:** The candidate's prose is the production translation, and the diff's translation mass sits in the sample body the original carries as documentation. Anchored pairs (TRANSLATION-ANCHORED, B13–B17): the table header and cell rows (orig L51–52 → cand L63–64: ヘッダー / セル内容）, the link sample (orig L59 → cand L71: "A link." → リンク。, its `href="/night-rush-theme"` kept as the same-site production path), and the remaining heading/cell samples (orig L65/L71/L76–77 → cand L77/L83/L88–89). Unanchored pairs (TRANS-UNANCHORED, 23 blocks): the intro sentence (B6, orig L26 → cand L38) and the usage sentence (B7, orig L28 → cand L40) are one-to-one translations the classifier could not anchor (script delta without the anchor majority — read and confirmed here); the three Lorem ipsum paragraphs are carried verbatim in Latin with only their footnotes translated (B10–B12, orig L43/45/47 → cand L55/57/59); and the tabview's repeated sample strings are translated once and repeated (B18–B34: "To make a point, this is a long tab." → わざわざ長いタブを作っています。 ×11 blocks, "This is also a tab." → これもタブです。 ×6 blocks, plus the two sandbox/tabview remarks B18/B19). The info-pane placeholder texts are translated inside B5 （あなたのページの情報 / 追加情報）. One charged item was never edited: the exhibit captions "**Rating:**" (cand L24) and "**Rating w/ Info Pane:**" (cand L29) remain in English, exactly as in the original (orig L12/L17). The localize lane charged them as a T5 note (LOCALIZE-ROWS row 24 item (c), "T5 EN labels L13/L18" in the lane's numbering); no wave edited them and no register raises them to an OPEN item — they caption the retained labelled exhibits (section 1), and the theme's display-affecting count (1) was the info-include leftover, not these labels. The item is carried in the Per-theme record so the retention is a recorded fact, not an oversight a reviewer has to discover.
- **Why:** P10: headings, usage text and samples are translated, terminology matched to the production translation this candidate adopts. Translation by the production translator is the substance of the K6 adoption; the campaign's T5 pass judged the result (stamp: T5 FINDINGS, jointly with T4; no mistranslation finding stands in the row).
- **Verify:** Read orig L26–47 against cand L38–59; `grep -n 'Rating' candidate.txt` (L24/L29, the retained captions).
- **Disposition:** Standing (the production translation). The EN captions are recorded in the Per-theme record.

### 7. Links

- **What:** No LINK signature fired. The candidate's prose links are the credit block's source link (cand L21, to the EN original — the required ruling-3 back-reference) and the sample table's link (cand L71, `href="/night-rush-theme"`, the production page's own path, kept from orig L59 with its text translated). The original carries no tag-page or hub links in its prose (its intro names no links at all), so no P11 repoint was owed. The two CSS `url()` asset references and the delivery stylesheet are dealt with in sections 3–4, not here.
- **Why:** P11 repoints original-site tag and hub links to their JP counterparts where such links survive; none do here, so the dead-target failure P11 exists to prevent does not arise.
- **Verify:** `grep -n 'href=\|\[http' candidate.txt` and read each hit's role.
- **Disposition:** Standing; no link item was charged for this theme in any register.

### 8. Structure

- **What:** The localize closing rule is honored: the exhibit's rules survive in the original's order, and the JP corrections sit at the end (the exhibit-tail supplement B41 and the live module B42 after the gate) — with two in-place exceptions, each small and visible: the B40 selector correction (cand L430, section 1) and one added declaration, `margin-right: 2em;` inside the `.page-rate-widget-box` rule (B39, orig L362–368 → cand L374–381). No register names the margin line; it is a production-side correction the adopted candidate carries (the rate widget's spacing beside the credit button is its evident role), recorded here so it is not mistaken for part of the original. The sample body is retained entire: headings, image-block, Lorem ipsum, tables and the tabview all survive (sections 2 and 6), so the two EXHIBIT-RESTRUCTURE primaries (B2, the frame include; B9, the image-block line) are the standing false fire — mere include repoints inside exhibit regions, adjudicated against the exhibit census, which shows no exhibit dropped or replaced. The classifier's topology pass finds no relocation between the sides.
- **Why:** Residue class R3: a sanctioned exhibit replacement and a silent deletion have the same diff shape, so the ground is stated — here the ground is that no exhibit changed shape at all; only the includes inside them were repointed. The closing rule (structure and ordering preserved, JP corrections appended) is what makes the rev-31 follow-up diff applicable, and Phase 22's incorporation is the proof it held.
- **Verify:** Compare the exhibit census: `grep -n '\[\[code\|tabview\|image-block\|footnote' original.txt candidate.txt`; read cand L374–381 against orig L362–368 for the margin line.
- **Disposition:** Standing (structure preserved; the two in-place corrections recorded above and in section 1).

### 9. Formatting only

- **What:** The classifier counts 0 WS-ONLY blocks and 0 re-indentation blocks. One formatting-shaped change exists, in residue block B35: the blank line between the exhibit's `[[code type="css"]]` opener and its banner comment (orig L130) is absent in the candidate (cand L141–142 are adjacent). The differ's channel flip on this block (code-css → body) is a tagging artifact of the deletion's position; the change itself is one blank line at the exhibit head, with no content line affected.
- **Why:** Formatting-only churn is disclosed as its own class so it is never mistaken for semantic change; this is neither R7 wholesale re-indentation (content lines keep their indentation) nor a content edit.
- **Verify:** Read orig L129–131 against cand L141–142.
- **Disposition:** None required.

### 10. Porter annotations

- **What:** The skeleton prints "none" for this section; direct inspection finds two, both inside CSS comments in the exhibit. (a) Residue block B36: the line "Localized by pcysl5edgo for SCP-JP" appended to the original's banner comment (cand L147, after the "Obviously based on…" line) — the production localizer's signature, and part of the provenance evidence in the Provenance section. (b) Inside B41: the two-line signature "/* Localized by RTa-technology .*/ /* for SCP-JP */" (cand L769–770) heading the credit-module supplement. The appended live module (B42) carries a third added text, an English explanatory comment stating its retargeting ground, quoted in section 1; it is the supplement's own documentation, not a translator note. No `[!-- … --]` wikitext annotations exist (`grep -c '\[!--' candidate.txt` = 0).
- **Why:** Residue class R2: porter additions are listed so they are never mistaken for original content or for translation; here both signatures are also evidence (the first for the adoption route, the second for the supplement's authorship).
- **Verify:** The greps in What; read cand L142–148 and L768–770.
- **Disposition:** None required.

### 11. Dispositions and exceptions

- **What:** Every finding not fixed in the candidate, in one place. (1) The two `http://` storage URLs (cand L224/L228): T1 errors http×2, DISPOSITIONED class (ii) — the scheme is rewritten at posting (GOSIGN2-LEDGER (c1) http entry; LOCALIZE-ROWS row 24 item (e)). (2) The usage example's bare same-site form (cand L43): DISPOSITIONED under the posting-procedure convention class (ledger (c3): P1 DISPOSITIONED) — it names the production page this candidate migrates, in the form posting expects. (3) The render findings: the T2 run's incompleteness (exit 2 ×6 on both pages, webkit networkidle) is DISPOSITIONED as a coverage caveat, not a theme defect (ledger (c2), citing the (a) note); the T3 items (header tagline double-struck at ≤375, notice×sidebar/clip) are DISPOSITIONED as the narrow-width header clip/collision family, a render-side difference class (FIX3-S2EN §6.5, X1–X9 family; KB-35 family). (4) The sample credit-modal line in the same render row: DISPOSITIONED preview-form — candidate/sample pages use credit:start-preview, which has no modal mechanism (GOSIGN-TESTS T2 amendment, 2026-11-16; KB-32). No item for this theme is left as an unexplained exception; the one charged-but-unedited item (the T5 exhibit captions) is not a disposition and is carried in the Per-theme record instead.
- **Why:** A disposition is a decision with grounds, not an omission; this section exists so the full set can be audited in one place.
- **Verify:** Each item names its deciding register above; the KB IDs resolve in patterns/ at commit 9c5e9079afb01d30cb9fc4ef9d714e5591eb2ffa.
- **Disposition:** DISPOSITIONED (items 1–4).

### 12. Verification

- **What:** (a) T1 source check, baseline 2026-11-16: exit 1, 2 errors / 1 warn / 4 infos; the errors are http×2 (the section 4 storage URLs); the warn and info codes are not itemized in the extracted row (T1-ROWS row 24). Register (c1) dispositions the http class as (ii); the credit-field and colon fixes the same baseline motivated are recorded as checker-verified in (c3). (b) T2/T3 render: FINDINGS, with the T2 coverage caveat and the T3 family disposition in (c2) (section 11, items 3–4); engine coverage is the lane's full matrix as run, with the row's inconclusive runs carried verbatim in the stamp (RENDER-ROWS-1, RENDER-C row 24). (c) T4 localize plus follow-up: FINDINGS with 1 display-affecting item (LOCALIZE-ROWS row 24, LOCALIZE-B); outcomes by item: (a) the info-include leftover FIXED (b816e10), (b) the missing frame FIXED (6ae6516), (d) the six missing credit fields FIXED (b816e10), (e) the http storage item DISPOSITIONED class (ii), (c) the T5 labels recorded unedited (Per-theme record). The follow-up currency check: the mirror is the re-translation revision 31, the follow-up artifact from31 records rev31 → rev31 with no changes, so no unincorporated upstream delta exists. (d) T5: judged jointly with T4 by the localize lane; its findings are the item (c) labels and no mistranslation charge. (e) This package is self-verifying: `python3 review/build_review.py --check` regenerates diff.md from the two byte-faithful copies and compares, and re-derives the verdict stamp. Counts in this README are the classifier's (42 change blocks) and the generator's (diff.md: +118/−58 in 7 hunks); the two count different units over the same pair.
- **Why:** Verification claims name the cheapest deciding check and its result, not a general assurance.
- **Verify:** Re-run the checker on `pages/theme:night-rush-theme-jp.txt`, and `python3 review/build_review.py --check` in this repo.
- **Disposition:** PASS (ledger determination, (b) row 24).

## Per-theme record

### The frame the diff shows as a repoint was a restoration

Read against the original alone, blocks B2/B3 look like a routine P1/P4 repoint of the EN frame. The file's history says otherwise: the port dropped the frame entirely, the localize check charged the absence (LOCALIZE-ROWS row 24 item (b), P6 missing), and FIX3-B (commit 6ae6516, the file's last content change) added the JP frame in one insertion, naming the same style0.css delivery at priority 1. The register's outcome (ledger (c3): P6 FIXED, frame waves, checker-verified) is correct; only the diff's shape understates it. This is the theme's class-U signal in its purest form: the wave edit is invisible as a wave edit in the two-file diff, and only the commit record shows it.

### The skeleton's INFO-DEL claim does not survive the bytes

The classifier's skeleton leads section 1 with INFO-DEL ("info-module residue removed (P3, ledger class C)"). The candidate retains all three info includes, repointed to `:scp-jp:` (cand L32/34/36), and the T1 fix wave's diff shows the repoint as a three-line substitution, not a removal. The block's own label set contains the true labels (INCLUDE-REPOINT, TRANSLATION-ANCHORED); INFO-DEL fired as a co-label and was promoted to primary by precedence. The ledger class C shape (info-module residue) does occur in this campaign, but not in this theme: the JP environment has info:start/more/end counterparts, they exist, and the port uses them. This package follows the bytes; the skeleton text is not reproduced.

### The sources.tsv note and the two reference revisions

sources.tsv's note for this row reads "original superseded upstream since the reference revision" and cites the follow-up artifacts `diff-night-rush-theme-from28, 31.txt`. The artifacts say something narrower: from28 records a real delta (rev28 → rev31, css_rules, the author's rev29/30 edits), and from31 records rev31 → rev31, no changes. So the original was superseded relative to the first-translation revision (28) and that delta is incorporated (Phase 22); relative to the revision this package mirrors (31), nothing supersedes it and upstream latest is still 31. The note survives only under the rev-28 reading; under the mirror's reading it overstates, in the same shape as the ambrose row's note, though here a real inter-revision delta exists underneath it. This package follows the artifacts.

### The vendored LOCALIZE-ROWS cell truncates item (e)

The ledger-parts copy of LOCALIZE-ROWS row 24 ends item (e) mid-phrase: "(e) http storage …". The item's substance is recoverable from the other vendored records (T1-ROWS row 24: http×2; ledger (c1)'s http entry: class (ii), scheme rewrite at posting) and from the candidate's bytes (the two http storage URLs, section 4), and this package cites it on that basis. The truncation is in the vendored extract, recorded here so a reviewer does not have to guess whether the package saw a fuller text.

### The English exhibit captions (LOCALIZE item (c))

Charged by the localize lane as a T5 note and never edited by any wave: "**Rating:**" and "**Rating w/ Info Pane:**" (cand L24/L29) caption the two retained exhibits, in the original's words. The retention is consistent with the exhibits' own standing (the labelled paired Rate exhibits set, whose captions are part of the exhibit form), the placeholder prose beneath the second caption is translated, and the lane's display-affecting count for this theme (1) was the info-include leftover, not the captions. No register dispositions the item by name and none raises it; it stands here as a recorded fact with its charge cited, so a future editor decides with the evidence in hand.

## Change set outside the two diffed files

The diff covers two files; the port's full change set is larger. (1) `pages/theme-decoration-sample-night-rush-theme-jp.txt` — the render sample page (two lines: an include of the candidate and an include of the shared `theme-decoration-sample`); it is the "sample" the T2/T3 checks rendered. (2) `pages/phase17-diff-night-rush-theme-jp.txt` — the Phase 17 migration deliverable: the diff form in which this candidate is applied to the production page theme:night-rush-theme (kind K6). (3) The delivery file itself: `files/theme/night-rush-theme/style0.css` on scp-jp.github.io, the production distribution the candidate's two delivery lines name (section 3); it lives outside this repo, in the JP files distribution, and the exhibit in this package is its on-page source text.

## Multi-wave provenance

The candidate's current state is the product of the production translation and six repo commits, not a single porting pass: the production JP translation (pcysl, 2022, from rev 28) entered the repo as a canonical source in d727e92; the dead-reference repair 4b52123 corrected the image-block file host; Phase 17 (8dcac74) added the credit block's frame with the rev-28 record; Phase 22 (d2a9dc0) incorporated the rev-31 re-translation drift and added the rev-31 record line; the T1 fix wave (b816e10) added the six missing credit fields, repointed the info includes and colon-encoded the storage URLs; and FIX3-B (6ae6516) restored the frame. The check waves that examined it: T1 baseline (row 24), LOCALIZE-B (row 24, five items, one display-affecting), RENDER-C (row 24). Two population waves a reader might expect are absent, for stated reasons: FIX-CREDIT-D's translator normalization does not touch the file (the translator is the human production translator, kept under ruling 3), and the usage-example sweep does not touch it (the candidate's usage form is the bare production fullname, not a `:scp-jp:theme:` reference). Citations, in place of a changelog: GOSIGN2-LEDGER.md (b) row 24, (c1) http entry and unencoded-colon entry, (c2) night-rush entry and preamble item 6, (c3) night-rush entry; GOSIGN2-LEDGER-SUPPLEMENT.md (no night-rush entries); T1-ROWS row 24; LOCALIZE-ROWS row 24; RENDER-ROWS-1 (RENDER-C) row 24. The go-sign re-run over that record is what the Status block certifies.

## Appendix — residue blocks

The classifier emitted two residue blocks and twenty-five heuristic blocks; all are resolved, none required a new signature.

- **R1 — B35 (residue; orig L130 → cand L141, code-css → body).** The blank line after the exhibit's `[[code]]` opener is absent in the candidate. Resolved in section 9 (formatting only).
- **R2 — B36 (residue; orig at L136 → cand L147, body → code-css).** The added banner line "Localized by pcysl5edgo for SCP-JP". Resolved in section 10 (porter annotation) and used as provenance evidence.
- **R3 — B6 (heuristic; orig L26 → cand L38).** The intro sentence, a one-to-one translation the classifier could not anchor. Resolved in section 6.
- **R4 — B7 (heuristic; orig L28 → cand L40).** The usage sentence, same shape. Resolved in section 6.
- **R5 — B10 (heuristic; orig L43 → cand L55).** Lorem ipsum carried verbatim; only the footnote is translated. Resolved in section 6.
- **R6 — B11 (heuristic; orig L45 → cand L57).** Same shape (footnote translation inside kept Latin). Resolved in section 6.
- **R7 — B12 (heuristic; orig L47 → cand L59).** Same shape. Resolved in section 6.
- **R8–R24 — B18–B34 (heuristic; orig L84–123 → cand L96–135).** The tabview sample strings: two remark lines (B18/B19) and the two repeated tab strings (B20–B34), each a one-to-one translation of a repeated original line. Resolved in section 6 by shape.
- **R25 — B37 (heuristic, CSS-BODY; orig L212 → cand L224).** The header-image storage re-host. Resolved in section 4 as a P5 re-host; the ASSET-REHOST signature did not fire on the CSS `url()` form (patterns proposal, lane report).
- **R26 — B38 (heuristic, CSS-BODY; orig L216 → cand L228).** The icon-image storage re-host, same shape. Resolved in section 4.
- **R27 — B39 (heuristic, CSS-BODY; orig L368 → cand L380).** The added `margin-right: 2em;` declaration in the rate-widget rule. Resolved in section 8 (an in-place production-side correction no register names).

## License and attribution

- **Title:** Night Rush Theme
- **Author:** Nagiros
- **Source:** https://scp-wiki.wikidot.com/theme:night-rush-theme — revision 31 (revision date 2022-12-20 21:40:07)
- **License:** Creative Commons Attribution-ShareAlike 3.0 (CC BY-SA 3.0) — license deed: https://creativecommons.org/licenses/by-sa/3.0/
- **Adaptation:** This package holds a Sigma-10 migration port of the work; changes were made. See "Summary" and "Standing sections" in this README for what changed and why. Translator: pcysl — a human translator credited by the live JP page and retained as the package records it (campaign-rule exception); where the campaign translated, the translator is AI.
