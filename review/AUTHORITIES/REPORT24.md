# REPORT24 — SB3 / FS site-theme audit

Record: `~/.local/state/wikijump/muse-bhl/theme-port-readiness-20261114/`
Phase 24, 2026-11-15 (Asia/Tokyo). Canonical repo: `/home/roku/src/Rokurolize/sigma10-check-wiki` (commit `d918e95`). Wikidot lane only: no Wikijump builds or promotions. Captures are in `evidence/p24/`; no probe pages were created.

## 1. Capture

The site theme is not exposed as a page. Both wikis serve it from the `internal-style` block, which imports the Wikidot base CSS and one site theme file; the rest of the served site-wide CSS is in additional `<style>` blocks (one site-wide top-bar adjustment per wiki, plus a sidebar-menu block identical on both wikis). Page-specific CSS appears only on some pages and is not part of the theme.

| Item | SB3 (`scp-jp-sandbox3`) | FS (`scp-jp-storage`) |
|---|---|---|
| Captured pages | `/` (home), `nav:side`, `nav:top` | `/` (home), `file:7450069-835-ub3a`, `nav:side` |
| Wikidot base import | `d3g0gp89917ko0.cloudfront.net/.../common--theme/base/css/style.css` | same |
| Site theme import | `https://scp-jp.github.io/files/util/sandbox/styles/theme.css` | `https://scp-jp.github.io/files/util/storage/styles/theme.css` |
| Theme CSS | 32,191 B full Sigma-9 fork (`sb3-theme.css`, sha256 `85a47ba0…`) | 1,161 B override file (`fs-theme.css`) importing `/files/theme/sigma-9/sigma-9.css` (stock) |
| Stock Sigma-9 reference | `sigma-9.css` (30,638 B, sha256 `69d856fe…`), the file FS imports | same |
| Sigma-10 JP composition | `sigma10-jp.css` (20,312 B, the CSS behind `theme:sigma-10-jp`) | same |
| Site-wide top-bar CSS | `scp-jp-sandbox3-sitewide-topbar.css` (93 B) | `scp-jp-storage-sitewide-topbar.css` (209 B) |
| Shared sidebar CSS | `shared-sidebar-menu.css` (1,735 B, byte-identical on both sites) | same |
| Page-list probes | `sb3-sitemap_page_1.xml`; `nav:side`, `nav:top` captures | `fs-sitemap_page_1.xml`; `nav:side` capture |
| Privileged CSS | — | `privileged.css?sid=4548695&required_level=moderator` (1,311 B, fetched as `privileged-fs.css`) |

Evidence: `evidence/p24/captures/` (HTML), `served-styles.json` (imports, hashes, style-block roles), `sb3-vs-sigma9.diff` (58 KB unified diff), and the CSS files named above. The site-wide top-bar block hashes were stable across the three pages of each wiki; the 1,735 B sidebar block was identical across both wikis and all captures, so it is treated as a shared site component, not a per-wiki delta.

## 2. SB3 adjustment inventory

SB3 does not import stock Sigma-9: its 32 KB `theme.css` is a full Sigma-9 fork. A semantic diff against `sigma-9.css` shows ~161 added and ~160 removed declaration keys, but many are base-version/formatting drift (rgba syntax, h2–h6 margins, colmod additions). The site-specific deltas are these:

| # | Selector / rule | What it changes | Sigma-10 JP (`sigma10-jp.css`) | Decision |
|---|---|---|---|---|
| S1 | `#search-top-box-input` background `#003300`, hover/focus `#32a18e`; `#search-top-box-form input[type=submit]` gradient `#226e61→#32a18e→#003300`, hover `#42d4bb→#226e61→#32a18e` | green search field/button instead of stock red | `#search-top-box-input{display:none}`; submit is `#633` with `#966→#633→#300` | **Conflict.** Sigma-10 hides the text input entirely. Re-express by restoring the input and applying the green palette, or accept the button-only search. |
| S2 | `#top-bar ul li.sfhover a, #top-bar ul li:hover a { color:#00aa11; background:#333 }`; `… a:hover { background:#333 }` | green-on-dark top-bar hover | `…{background:#eee; color:#a01}` and `…:hover{background:#fff}` | **Conflict.** Re-express the hover palette on the new top-bar. |
| S3 | `#side-bar { width:17em; left:0; margin:0 0 0 2em }`; drawer background `rgb(50,161,142)` | wider, left-aligned green sidebar | `width:13.75rem; left:1.5rem`; drawer background `#b88686` | **Conflict.** Re-express width/offset/background; the Sigma-10 width is materially narrower. |
| S4 | `div#container-wrap { background:url(/files/util/sandbox/media/component/theme/body_bg.png) … }`; `#header { background:url(/files/util/sandbox/media/component/theme/logo.png) … }` | sandbox-specific header/body art | `div#container-wrap{background:url('https://scp-jp.github.io/sigma/images/body_bg.svg') …}`; `#header{background:url('…/header-logo.svg') 10px 40px no-repeat}` | **Needs re-expression.** Replace the asset URLs in the new header/body rules; do not carry the Sigma-9 selectors unchanged. |
| S5 | `#header h1 a span` text “SCP-JPサンドボックスⅢ”; `#header h2 span` “a.k.a 下書きフォーラム v2” | site name and subtitle | `#header h1 a::before{content:'SCP'}`; `::after{content:'財団'}`; `#header h1 a span{font-size:0}` | **Conflict.** Sigma-10 hides the span and hardcodes “SCP財団”. Re-express the site name/subtitle (override both pseudos and the span rule); otherwise the sandbox name disappears. |
| S6 | `#search-top-box` narrow rule `top:115px; right:2px`; input widths `5em/7em/8em` at the responsive steps | narrow-viewport search placement | base `top:79px; right:9px; width:250px`; ≤767px input `width:7em`; ≤479px input `display:none` | **Conflict at the responsive steps.** Re-express the narrow placement or adopt Sigma-10’s; do not carry the 115/2 values unchanged. |
| S7 | `#top-bar ul { display:inline-block; width:100% }`; `li:nth-of-type(2),(3){float:right}` | full-width top bar with right-aligned items | `#top-bar{position:absolute; top:140px; height:21px; width:100%}`; no equivalent `ul` rule | **Needs re-expression.** The Sigma-10 bar is already absolute/full-width; re-check item alignment rather than copying the old float rules. |
| S8 | `#content-wrap { min-height:2500px }` | extra page height | `min-height:80rem` (desktop) / `120rem` (wide) | **Value conflict.** Re-express only if the sandbox still needs the extra height. |
| S9 | Font Awesome import `4.7.0` | icon set newer than stock | Sigma-10 imports `4.3.0` | **Decision needed:** keep 4.7 by adding the import, or accept 4.3 after an icon-usage audit. |
| S10 | `.top-bar ul:nth-of-type(2), .mobile-top-bar ul:nth-of-type(2){display:none!important}` (site-wide admin block) | hides the second top-bar/mobile menu list | `.top-bar`/`.mobile-top-bar` markup still exists; nth-of-type depends on the final markup | **Carry as-is, then verify.** Re-check the index after the Sigma-10 header markup is in place. |
| S11 | Shared `#side-bar .menu-item` block (1,735 B; identical on both wikis) | sidebar menu spacing, icons, bold links | Sigma-10 has `#side-bar` menu rules and the same menu-item class family | **Carry as-is** (shared component, not a per-site delta); verify the side-bar structure. |

Base-version-only differences (rgba serialization, h2–h6 spacing, colmod rules, extra viewport at-rules) are not treated as SB3 adjustments.

## 3. FS adjustment inventory

FS imports stock Sigma-9 (`/files/theme/sigma-9/sigma-9.css`) and then a 1,161 B override file. Every rule in that file is a site delta:

| # | Selector / rule | What it changes | Sigma-10 JP (`sigma10-jp.css`) | Decision |
|---|---|---|---|---|
| F1 | `#container-wrap { --c-header: linear-gradient(180deg, black 25%, #002bbd 100%); --c-topbar: linear-gradient(180deg, #535353 0%, #3c3c3c 53%) }` | storage header/top-bar colors | no `--c-header`/`--c-topbar` variables; `div#container-wrap` uses `body_bg.svg` | **Conflict.** Re-express as concrete header/top-bar overrides; the variables are not consumed by Sigma-10. |
| F2 | `div#container-wrap { background:url(/files/util/storage/media/component/theme/header-bg.png) top left repeat-x, var(--c-header) …; background-size:100px 141px }` | storage header image + gradient | `background:url('…/sigma/images/body_bg.svg') top left repeat-x` | **Conflict.** The Sigma-10 body/header use different assets; replace/re-layer the storage image on the new header. |
| F3 | `div#container-wrap::after { top:140px; height:23px; box-shadow:3px 2px 25px -2px rgba(0,0,0,.75); background:var(--c-topbar) }` | 23 px top-bar overlay | `#top-bar{position:absolute; top:140px; height:21px; width:100%}` with its own background | **Conflict/duplicate.** Sigma-10 already draws the bar at top 140/21 px; re-express only if the storage gradient/shadow is still wanted, otherwise drop. |
| F4 | `#header h1 a { font-size:150% }` | header title size | `#header h1 a{font-size:1.5em}` | **Carries as-is** (equivalent value; no-op on Sigma-10). |
| F5 | `@media(max-width:768px){ #header h1 a span{font-size:0} #header h1 a::before{content:"SCP-JP ストレージ"; font-size:25px} }` | mobile storage title | `#header h1 a span{font-size:0}` at all widths; `#header h1 a::before{content:'SCP'}` and `::after{content:'財団'}` | **Conflict.** The `::before` content would combine with Sigma-10’s `::after “財団”`. Re-express by overriding both pseudos (or the title markup) so the final title is exactly “SCP-JP ストレージ”. |
| F6 | `@import url("https://manage.scp-jp.com/api/public/privileged.css?sid=4548695&required_level=moderator")` | moderator-scope user-target hiding (`privileged-fs.css`, 1,311 B) | not part of Sigma-10 | **Carry as-is** as a separate admin stylesheet; it is not a theme-base rule. |
| F7 | `#top-bar a.newpage, #top-bar .top-startlink{display:none}`; `#top-bar a.newpage ~ .top-startlink{display:inline}`; `.top-bar div:nth-of-type(2), .mobile-top-bar div:nth-of-type(3){display:none}` (site-wide admin block) | hides new-page/start links and one top-bar div | same top-bar/mobile markup classes exist; nth-of-type depends on the final markup | **Carry as-is, then verify** against the Sigma-10 header markup. |
| F8 | Shared `#side-bar .menu-item` block (1,735 B; identical on both wikis) | sidebar menu spacing/icons | same class family exists | **Carry as-is** (shared component). |

## 4. Per-wiki migration requirements

**SB3**
1. Replace the full `files/util/sandbox/styles/theme.css` fork with the Sigma-10 JP base plus a small site override layer; do not import Sigma-9 beneath it.
2. Re-express the green palette on Sigma-10 selectors: search field/button (S1), top-bar hover (S2), sidebar/drawer background (S3). S1 additionally needs a decision on restoring the text input, which Sigma-10 hides.
3. Replace sandbox header/body art (S4) and re-express the header title/subtitle (S5), because Sigma-10 hides the h1 span and hardcodes “SCP財団”.
4. Re-do the narrow search placement (S6), top-bar item alignment (S7), content min-height (S8), and the Font Awesome decision (S9) against the new layout.
5. Keep the site-wide top-bar hide block (S10) and shared sidebar CSS (S11), then verify both on a draft page after the header markup is final.

**FS**
1. Replace the stock Sigma-9 import in `files/util/storage/styles/theme.css` with the Sigma-10 JP base; keep `privileged.css` as a separate import.
2. Re-express the storage header gradient/background/overlay (F1–F3) on the Sigma-10 header and top bar; do not carry the `--c-*` variables, which Sigma-10 does not consume.
3. Re-express the storage title (F5) so the final text is “SCP-JP ストレージ”, overriding Sigma-10’s “SCP” + “財団” pseudos; keep the h1 size rule (F4, already equivalent).
4. Keep the site-wide top-bar hide rules (F7) and shared sidebar CSS (F8), then verify on an attachment/file page after the header markup is final.

## 5. Questions only site-admin access can settle

- Site Manager → Appearance → theme/custom CSS: confirm that the imported theme file is the only site-theme source and which of the served `<style>` blocks are the admin “Custom CSS” field versus page/include content. We inferred site-wide blocks by cross-page persistence; only the site manager can confirm their storage location and edit path.
- `privileged.css` on `manage.scp-jp.com` (sid 4548695): confirm it is still applied to FS and whether its user-target hiding remains required. The file is fetched and inventoried, but its moderator-scope intent needs the moderator/admin account that owns that service.
- Sigma-10 selection per wiki: confirm the site theme will be selected in Site Manager for each wiki and whether the site override layer will live in the Custom CSS field or in the imported theme file. This determines which of the selectors above staff can edit without a theme-file deploy.

## 6. /start and verification

`/start`’s `サイト運用Wiki` section now carries the concrete per-wiki requirements (green palette/search/top-bar/sidebar and sandbox title/art for SB3; storage header/overlay/title and privileged CSS for FS). Canonical commit: `d918e95` (“start: add the SB3/FS served-theme requirements”), reflected to both check wikis.

- `verify.py`: exited **0**: `OK: 315 pages match on both wikis`.

PHASE24: COMPLETE
