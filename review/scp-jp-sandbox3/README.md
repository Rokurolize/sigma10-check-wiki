# Review package — scp-jp-sandbox3 (SB3) site theme: Sigma-9 fork → Sigma-10

## Status

<!-- BEGIN GENERATED STATUS STAMP — do not hand-edit; regenerate with review/build_review.py -->
| Field | Value |
|---|---|
| Package status | Second site package of the review documentation pass — the SB3 companion to the settled FS pilot; same generated format and mechanism. |
| Candidate status | Authored, not deployed — authored for this package on 2026-11-17; production SB3 still serves the original full Sigma-9 fork. |
| Verification status | Source-level only — the draft-page render check the governing requirement calls for has not been run, and no part of this package claims that it has. |
| Governing requirement | The SB3 row of the site-operations table in /start (canonical source: pages/start.txt), quoted verbatim in this section. |
| Canonical commit | 70cbeba2c2b309e03bf293e2f10f2b6839bc3d3e |
<!-- END GENERATED STATUS STAMP -->

Requirement (SB3 row, Sigma-10 migration-requirements cell, quoted verbatim from `pages/start.txt`):

> Base it on Sigma-10 and layer the overrides on top. The green accents, the sandbox images, the narrow-width search-box position, the top-bar placement, and the sidebar width are re-expressed with the new selectors (because they conflict with Sigma-10's red, 13.75rem, and the fixed "SCP財団"). Reset the site name "SCP-JPサンドボックスⅢ" and the h2 subtitle in the header. Decide the handling of FontAwesome 4.7. Keep the management CSS's hiding of the top bar. Check on a draft page.

The same requirement, restated in plain English (the /start cell is already English, so this is a paraphrase for review clarity, not a translation):

> Start from Sigma-10 and put the SB3-specific overrides on top of it. Re-express the green accents, the sandbox images, the narrow search-box placement, the top-bar placement and the sidebar width with the new selectors, because they clash with Sigma-10's red palette, its 13.75rem sidebar and its hard-coded "SCP財団" title. Restore the site name "SCP-JPサンドボックスⅢ" and the h2 subtitle in the header. Make and record a decision about FontAwesome 4.7. Keep the management CSS rule that hides the second top bar. Verify on a draft page.

Current composition (SB3 row, current-composition cell, quoted verbatim):

> Sigma-9 full fork (files/util/sandbox/styles/theme.css) + management CSS. Green search box (#003300/#32a18e), top-bar hover (#00aa11), sidebar background rgb(50,161,142), sandbox logo/body_bg, narrow-width search-box position (top 115 / right 2), full-width top bar right-aligned, 17em sidebar, FontAwesome 4.7.

Restated: SB3 serves a complete 32 KB fork of Sigma-9 (`files/util/sandbox/styles/theme.css`), not a small override file, plus a separate management (site-wide) CSS block. The fork's site-specific deltas are the green search field/button, the green top-bar hover, the green 17em sidebar and drawer, the sandbox logo and body art, the narrow search-box position, the full-width right-aligned top bar, and a FontAwesome 4.7 import.

The judgment basis for this package is §2 (the SB3 adjustment inventory, S1–S11) and §4 (the SB3 migration requirements, items 1–5) of `REPORT24.md`, vendored in this repo at `review/AUTHORITIES/REPORT24.md`. Citations of the form "REPORT24 S1" throughout this README resolve there.

**Deployment.** Deploying means replacing the file served at `original.css`'s Source URL (see Provenance) in the SCP-JP GitHub Pages tree with `candidate.css`. That tree is outside this repo and outside campaign authority, so this package is a proposal record until a site admin applies it. Rollback is restoring the mirrored `original.css` in place of the deployed file. The site-wide management CSS block (S10) is a separate served layer and is not touched by this deployment.

## What a reader of the site will notice

The header keeps the words it has today, unlike the FS package. SB3's h1 span already reads "SCP-JPサンドボックスⅢ" and its h2 span reads "a.k.a 下書きフォーラム v2"; Sigma-10 would hide the span and print "SCP財団" instead, so the candidate overrides both header pseudos to restore the sandbox name (change class 3) and restates SB3's subtitle presentation on the h2 span. The visible header text is therefore unchanged by the migration.

Everything else the requirement names is preserved in place: the green search field and button (Sigma-10 would hide the field and show a red button), the green top-bar hover, the green 17em sidebar and drawer, the sandbox logo and body art (Sigma-10 would substitute its own SVG assets), the narrow search-box placement, and the full-width right-aligned top bar. The only non-visual change is the icon font: from 4.7 to the base's 4.3, which the audit in "Judgment calls" shows renders the same glyphs. And until a site admin deploys the candidate, nothing changes at all: production still serves the original fork.

## Provenance

SB3 is not a Wikidot theme page. Its theme is a static CSS file served from SCP-JP's GitHub Pages tree, which the site's internal-style layer loads into every page. So the "original at the reference revision" in this package is not a page revision but a capture of the served files, taken on 2026-11-15 (Asia/Tokyo). Every mirror below is byte-identical to its capture, and anyone can re-verify that against the hashes (the manifest is `evidence/p24/served-styles.json` in the campaign record; the hashes are self-contained here).

| File | Source | Role | Captured | SHA-256 |
|---|---|---|---|---|
| `original.css` | https://scp-jp.github.io/files/util/sandbox/styles/theme.css | The whole 32 KB Sigma-9 fork loaded by the internal-style layer. This is the file the candidate replaces. | Captured 2026-11-15 | `85a47ba0b7f452768c976cabda879407e2a6bd3620697ca6a3bd94a97b78ab4a` |
| `candidate.css` | — (authored here) | The replacement override layer: Sigma-10 base plus the SB3 deltas. Deploying replaces the file at `original.css`'s Source URL above. | Authored 2026-11-17 | — |
| `diff.md` | — (generated) | The Tier 2 unified diff `original.css` → `candidate.css`, generated by `review/build_review.py`. Do not hand-edit it. | Generated 2026-11-17 | — |

The two base captures used for the structural comparisons are in this package, so every Verify step below is executable from this repo alone. Both are evidence captures, distinct from the mirrors above: neither is a file the port replaces.

- `reference-sigma-9.css` — the stock Sigma-9 base (30,638 B), SHA-256 `69d856fed1eb75998b4be68024ff20441d672066660a8c83eaef70db143087b8`. The base the original fork descends from. Captured 2026-11-15, in the same capture set as the mirror.
- `reference-sigma10-jp.css` — the Sigma-10 JP base as captured (20,312 B), SHA-256 `2057dd4383be635bd239716615f3eafa9af036fd6197017efd7ee476c3ab6ab8`. The CSS behind the check wiki's `theme:sigma-10-jp`; its delivery point is https://scp-jp.github.io/sigma/css/sigma.min.css (the URL the candidate imports; canonical repo: `pages/theme:sigma-10-jp.txt`). Captured 2026-11-15.

The served composition includes two admin layers that live outside the theme file; following the FS package, they are described here but not mirrored into the package:

- `scp-jp-sandbox3-internal-style.css` — the internal-style import block that loads the Wikidot base CSS and the theme file (SHA-256 `49f08669aa4df9bc830093b003d501afcee487018ecdb334dd83c43ef69d2f1c`). The base import is a Wikidot CDN file; the only import the port controls is the theme file, mirrored as `original.css`.
- `scp-jp-sandbox3-sitewide-topbar.css` — the site-wide management CSS block that hides the second top-bar list (SHA-256 `259db68b2bf8679f6461a383f3c92f1b95eaf11bb448fa1e123cd2303deb56bc`). This is REPORT24 S10's "Carry as-is, then verify" layer; the candidate neither carries nor deletes it (see "Deliberately unchanged").
- The shared 1,735 B `#side-bar .menu-item` block (REPORT24 S11) is byte-identical on SB3 and FS and is likewise a separate served layer, outside this file.

**No privileged.css for SB3.** Unlike FS, SB3's served `internal_style_imports` contains only the Wikidot base CSS and the theme file — there is no `manage.scp-jp.com` privileged stylesheet in the SB3 composition (verify: `served-styles.json`, site `scp-jp-sandbox3`). Therefore the FS treatment of privileged.css (externally managed, retained as-is, never a candidate) has nothing to apply to here: there is no `original-privileged.css` mirror in this package and no privileged import line in the candidate. This is a load-bearing difference from the FS package, not an omission.

## Summary

SB3 (scp-jp-sandbox3.wikidot.com) is SCP-JP's draft-and-sandbox wiki. Its whole visual identity lived in a 1,735-line full fork of Sigma-9 with a handful of green-accent and asset overrides. The migration retires that fork: the candidate imports the Sigma-10 JP base and re-expresses only the site-specific deltas, in a 136-line override layer. The generated diff (Tier 2) counts +65 / −1664 lines across 24 change blocks in 3 sections; the −1664 is the retired fork itself, not 1,664 individual defects, and the README's change classes enumerate the handful of rules that actually carry site intent (classes 1–7 below). Zero of the +65 added lines are `REVIEW:`-stage comments — every added line, including the base import URL, is in final deployed form. The single decision with a real fork in the requirement is FontAwesome (S9); the candidate accepts the base's 4.3 after the icon-usage audit recorded under "Judgment calls". The diff file is evidence; this README is the readable layer.

## Change classes

### 1. Base: full Sigma-9 fork → Sigma-10 import (diff sections 1–3, the wholesale replacement)

**What changed.** The candidate does not import the 32 KB `/files/util/sandbox/styles/theme.css` fork at all. It imports the production Sigma-10 JP delivery point `https://scp-jp.github.io/sigma/css/sigma.min.css` and carries only the site rules below. The original's `@charset`, its three `@import`s (Bauhaus, FontAwesome 4.7, cc-icons), and all ~1,660 lines of forked base are retired; the base and the other icon sets now come from Sigma-10 (Bauhaus from the base's own `scp-wiki.wdfiles.com` import; cc-icons is not imported by the base — see "Judgment calls").

**Why.** REPORT24 §4 SB3 item 1: "Replace the full `files/util/sandbox/styles/theme.css` fork with the Sigma-10 JP base plus a small site override layer; do not import Sigma-9 beneath it." The /start row opens "Base it on Sigma-10 and layer the overrides on top." Re-basing a full fork rule-by-rule would re-ship all of Sigma-9 under Sigma-10; the requirement is a replacement, not a merge. The chosen URL is the production Sigma-10 JP artifact, the same delivery point the check wiki uses through `theme:sigma-10-jp`.

**Verify.** `grep -n "sigma-9\|maxcdn.bootstrapcdn.com/font-awesome/4.7.0" candidate.css` returns nothing. The import URL matches line 6 of `pages/theme:sigma-10-jp.txt` in this repo. The diff's 3 sections and 24 change blocks are the mechanical shape of a whole-file replacement.

**Delivery-stage forms.** None. The URL is the production delivery point, not a draft or check-wiki host.

### 2. Sandbox art: header logo and body background (S4)

**What changed.** `div#container-wrap` gets `background: url(/files/util/sandbox/media/component/theme/body_bg.png) top left repeat-x;`, and `#header` gets `background: url(/files/util/sandbox/media/component/theme/logo.png) 10px 40px no-repeat;`. The root-relative image URLs are byte-identical to the original.

**Why.** The /start row names "the sandbox images" among the things to re-express, and REPORT24 S4 requires replacing the asset URLs in the new header/body rules rather than carrying the Sigma-9 selectors unchanged. Sigma-10's base draws `body_bg.svg` and `header-logo.svg` from `scp-jp.github.io/sigma/images/`; leaving those in place would swap the sandbox's art for the generic Sigma-10 art. Writing the sandbox URLs on the Sigma-10 selectors puts the same images back. The `background` shorthand is used deliberately: it resets the base's `background-size:100px` and `background-position:10px 64%`, so the logo keeps its natural size and SB3's `10px 40px` placement at every width (the base had a responsive `calc(48px + 5%)` size at ≤767px).

**Verify.** `grep -o "div#container-wrap{[^}]*}" reference-sigma10-jp.css` shows the base's `body_bg.svg`; `grep -o "#header{height:140px[^}]*}" reference-sigma10-jp.css` shows the base's `header-logo.svg` plus the size/position the shorthand resets. Both sandbox URLs appear verbatim in `candidate.css` and in `original.css`.

**Delivery-stage forms.** None. Once the candidate replaces `original.css` at its GitHub Pages path, the root-relative URLs resolve exactly as they do today (the campaign's no-re-upload rule applies; the images are not mirrored here).

### 3. Site name and subtitle (S5)

**What changed.** The Sigma-10 base's two pseudo rules are replaced with `#header h1 a::before { content: "SCP-JPサンドボックスⅢ" }` and `#header h1 a::after { content: none }`, and `#header h2 span` is given SB3's subtitle presentation (block, `max-height:0`, `padding:19px 0`, `font-weight:bold`, `line-height:0`, `color:#f0f0c0`, `text-shadow:1px 1px 1px rgba(0,0,0,.8)`). The base's `h1 a span { font-size:0 }` span-hiding is not overridden: the visible name comes from the `::before` string.

**Why.** The /start row orders "Reset the site name 'SCP-JPサンドボックスⅢ' and the h2 subtitle in the header", and REPORT24 S5 names the trap: Sigma-10 hides the h1 span at all widths and prints `::before{content:'SCP'}` plus `::after{content:'財団'}`, so overriding only `::before` would render "SCP-JPサンドボックスⅢ財団". Both pseudos must be set, unconditionally, because the base's pseudo title is unconditional. The h2 subtitle text "a.k.a 下書きフォーラム v2" is site content in the span (captured home HTML: `<h2><span>a.k.a 下書きフォーラム v2</span></h2>`), so no `content:` string is invented for it; the base already renders that span with values equal to SB3's, and the candidate restates them so the override layer owns the subtitle's presentation. Unlike FS, the visible desktop text does not change: SB3's h1 span already read "SCP-JPサンドボックスⅢ".

**Verify.** `grep -o "#header h1 a::before{content:'SCP'}" reference-sigma10-jp.css`, `grep -o "#header h1 a::after{content:'財団'[^}]*}" reference-sigma10-jp.css`, and `grep -o "#header h1 a span{font-size:0[^}]*}" reference-sigma10-jp.css` show the three base rules; the candidate's two content values are the requirement's string and `none`. `grep -o "#header h2 span{[^}]*}" reference-sigma10-jp.css` shows the base's subtitle values the candidate restates.

**Delivery-stage forms.** None.

### 4. Green search field and button (S1)

**What changed.** `#search-top-box-input` is given `display:inline-block` and the green palette (background `#003300`, hover/focus `#32a18e`, white border and inset shadow on hover/focus). The submit button's red base gradient is replaced with SB3's green gradients (`#226e61 → #32a18e → #003300`, hover `#42d4bb → #226e61 → #32a18e`), with the original colors/borders/shadows preserved.

**Why.** The /start row lists "Green search box (#003300/#32a18e)" and says the green accents are re-expressed "because they conflict with Sigma-10's red". Sigma-10 sets `#search-top-box-input{display:none}` at all widths and paints the submit button `#633` with a `#966→#633→#300` gradient. REPORT24 S1 records the conflict and two options: restore the input with the green palette, or accept Sigma-10's button-only search. The requirement's "green search box" and the /start current-composition cell's emphasis on the green field decide it: the candidate restores the field and applies the green palette, rather than accepting the button-only red search. The `display:inline-block` rule is later than the base's `display:none` in cascade order, so it wins at every width, including ≤479px (the base's narrow `display:none` rule); this matches SB3, which never hid the field.

**Verify.** `grep -o "#search-top-box-input{display:none}" reference-sigma10-jp.css` and `grep -o "#search-top-box-form input[type=submit]{[^}]*}" reference-sigma10-jp.css` show the base's hidden field and red button; the candidate carries the green values. Every color literal is in `original.css` (lines 146–182).

**Delivery-stage forms.** None.

### 5. Green top-bar hover (S2)

**What changed.** `#top-bar ul li.sfhover a` / `:hover a` get `color:#00aa11`, `background:#333333` and opaque `rgba(64,64,64,1)` side borders; the deeper `:hover` keeps `background:#333333`; `#top-bar a:hover` and `#top-bar ul li ul a` get `color:#00aa11`.

**Why.** The /start row lists "top-bar hover (#00aa11)" and REPORT24 S2: Sigma-10 paints the hovered item `background:#eee; color:#a01`. The palette is re-expressed on the identical Sigma-10 selectors so the sandbox keeps its green-on-dark hover. Sigma-10 uses the same `li.sfhover` / `li:hover` class family, so no markup change is involved.

**Verify.** `grep -o "#top-bar ul li.sfhover a,#top-bar ul li:hover a{[^}]*}" reference-sigma10-jp.css` shows the base's `background:#eee;color:#a01`; the candidate's values are `#00aa11` / `#333333`.

**Delivery-stage forms.** None.

### 6. Sidebar width and drawer colour (S3)

**What changed.** `#side-bar` gets `width:17em`, `left:0`, `margin:0 0 0 2em`, overriding the base's `width:13.75rem; left:1.5rem`. Inside `@media (max-width:767px)` the off-canvas drawer gets `width:17em` and `background-color:rgb(50,161,142)`, overriding the base's `width:15rem; background-color:#b88686`.

**Why.** The /start row lists "sidebar background rgb(50,161,142)" and "17em sidebar" and says the sidebar width is re-expressed "because [it conflicts with] Sigma-10's ... 13.75rem". REPORT24 S3 records both the desktop and drawer values. The requirement's numbers are written out on the new selectors; the base's off-canvas `left:-25rem` and transition are left alone (they are base-version geometry, not a site delta), and the drawer's 17em width matches the desktop sidebar as in SB3.

**Verify.** `grep -o "#side-bar{clear:none[^}]*}" reference-sigma10-jp.css` shows `left:1.5rem;width:13.75rem`; `rg -o "background-color:#b88686" reference-sigma10-jp.css` finds the base drawer color. The candidate's `17em`, `left:0`, `margin` and `rgb(50, 161, 142)` are present verbatim.

**Delivery-stage forms.** None.

### 7. Narrow search-box placement (S6)

**What changed.** Inside `@media (max-width:479px)`, `#search-top-box` gets `top:115px; right:2px`.

**Why.** The /start row lists "narrow-width search-box position (top 115 / right 2)" among the re-expressed items, and REPORT24 S6 records SB3's `top:115px; right:2px` at its ≤479px breakpoint against the base's `top:79px; right:9px; width:250px` (narrow `width:7em`). The values are re-expressed on `#search-top-box` at the same breakpoint the original used; no SB3 width declarations are carried, so the base's responsive input width continues to govern.

**Verify.** `rg -n "top: 115px|right: 2px" original.css` finds SB3's values at the ≤479px block (lines 1230–1231); `grep -o "#search-top-box{[^}]*}" reference-sigma10-jp.css` shows the base's `top:79px;right:9px`.

**Delivery-stage forms.** None.

## Deliberately unchanged

- **Management top-bar hiding (S10).** The site-wide block `.top-bar ul:nth-of-type(2), .mobile-top-bar ul:nth-of-type(2) { display:none!important }` is served as a separate admin `<style>` block, not from the theme file. The /start row says "Keep the management CSS's hiding of the top bar" and REPORT24 S10 says "Carry as-is, then verify". The candidate neither carries it into `candidate.css` nor deletes it: it stays a separate served layer and is to be re-checked against the final Sigma-10 header markup at the draft-page render check. The base's `#top-bar ul{float:right}` and `.mobile-top-bar` rules are left intact for the same reason. This is the SB3 analogue of FS's F7 layer-outside-this-file boundary.
- **Shared sidebar CSS (S11).** The 1,735 B `#side-bar .menu-item` block is byte-identical across SB3 and FS, a shared site component rather than an SB3 delta. REPORT24 S11 says "Carry as-is"; like the management block, it is a separate served layer and is outside this file. It is recorded in Provenance, not ported.
- **privileged.css.** Not applicable to SB3: no privileged stylesheet is served (see "No privileged.css for SB3" in Provenance). No mirror, no import, no candidate.
- **Font Awesome version.** Decided in favour of the base's 4.3; no 4.7 import is added (see "Judgment calls").
- **Content min-height (S8).** SB3's `#content-wrap{min-height:2500px}` is not carried. Sigma-10 sets `min-height:80rem` (and `120rem` at wide widths), and REPORT24 S8 permits "Re-express only if the sandbox still needs the extra height". The requirement's re-expression list does not name the min-height, and no evidence establishes that SB3 still needs 2500px under the new layout, so the base's value governs. This is the one S-item from REPORT24 §2 deliberately not re-expressed; it is a layout value, not site identity.
- **cc-icons (original import 4).** The original's `cdnjs.cloudflare.com/.../cc-icons/1.2.1` import is not re-added. Sigma-10's base does not import cc-icons; the captured SB3 pages show no `cc-icons` usage in the theme file or page markup, and the requirement does not name it. It is a base-version import, not a site delta.
- **Base-version-only differences.** rgba serialization, h2–h6 margins, colmod rules and extra viewport at-rules that differ between the full fork and stock Sigma-9 are not SB3 adjustments (REPORT24 §2 preamble) and are not carried; the Sigma-10 base supplies its own equivalents.

## Judgment calls and open questions

- **FontAwesome 4.7 → 4.3 (S9) — decision: accept 4.3.** REPORT24 S9 left two options: keep 4.7 by adding an import, or accept 4.3 after an icon-usage audit. The audit: the only FontAwesome codepoints in the original fork are `\f06a` (`#page-tags-input + .sub::before`, an exclamation-circle) and `\f111` (the inline-diff highlight marker); both are core glyphs present since FontAwesome 4.0 and therefore in the base's 4.3. The captured SB3 pages contain no `fa-` class usage and no 4.7-only glyph. The Sigma-10 base already imports 4.3 from the same host, and the base itself uses `\f111` in its own inline-diff rule. Adding a 4.7 import would load a second copy of the same `FontAwesome` family and the same codepoints for no visible gain, while keeping an extra `maxcdn.bootstrapcdn.com` dependency. The candidate therefore adds no FontAwesome import and inherits 4.3 from the base. This is a decision with grounds, not a deferred question.
- **Search field restoration at ≤479px.** The base hides `#search-top-box-input` at ≤479px; the candidate's unconditional green-field rule restores it at that width too (cascade order, change class 4). That follows the requirement's "green search box" and SB3's own behaviour (which set a 5em field width at ≤479px rather than hiding it). If staff prefer the base's button-only search on the narrowest screens, the change is one `display:none` media rule; it is flagged here rather than silently chosen against the requirement.
- **Logo sizing.** The candidate's `background` shorthand on `#header` resets the base's `background-size:100px`, so the sandbox logo is at natural size, as in SB3, at all widths. If a reviewer wants the base's responsive `calc(48px + 5%)` sizing kept, that is a one-line addition; the requirement names the art, not a size.
- **Questions only site-admin access can settle** (carried over from REPORT24 §5, unresolved): which served `<style>` blocks are the admin "Custom CSS" field versus page/include content, and where the S10 management block is stored; whether the site theme will be selected in Site Manager per wiki; and whether the override layer will live in the Custom CSS field or in the imported theme file. None can be settled from the captures, and none blocks this source-level package.
- **Verification status, restated.** Everything in this package is source-level: capture hashes, the generated Tier 2 diff, rule-by-rule comparison against the two captured bases, and the icon-usage audit. The draft-page render check the requirement calls for (「Check on a draft page」, the re-check of S10/S11 against the final Sigma-10 header markup) has not been performed, because the candidate is not deployed anywhere a browser can load it. No statement in this package claims rendered behaviour.
