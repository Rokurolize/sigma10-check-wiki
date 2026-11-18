# Review package — scp-jp-storage (FS) site theme: Sigma-9 → Sigma-10

## Status

<!-- BEGIN GENERATED STATUS STAMP — do not hand-edit; regenerate with review/build_review.py -->
| Field | Value |
|---|---|
| Package status | Pilot — the first package of the per-theme review documentation pass; the format for the remaining packages is settled on this example. |
| Candidate status | Authored, not deployed — authored for this package on 2026-11-17; production FS still serves the original. |
| Verification status | Source-level only — the attachment-page render check the governing requirement calls for has not been run, and no part of this package claims that it has. |
| Governing requirement | The FS row of the site-operations table in /start (canonical source: pages/start.txt), quoted verbatim in this section. |
| Canonical commit | c196257f30e20aa8b56c0a7d0bd17083271345be |
<!-- END GENERATED STATUS STAMP -->

Requirement (FS row, requirement cell):

> Sigma-10をベースにします。ヘッダー背景、グラデーション、オーバーレイは、Sigma-10のヘッダーとトップバーと競合するため再表現します。固定「SCP財団」の疑似要素は「SCP-JP ストレージ」に置き換え、モバイルのspan非表示も新しい構造に合わせます。top-bar非表示の調整とprivileged.cssは維持します。添付ファイルページで確認します。

The same requirement, in English:

> Base it on Sigma-10. The header background, the gradient, and the overlay conflict with Sigma-10's header and top bar, so re-express them. Replace the fixed "SCP財団" pseudo-element with "SCP-JP ストレージ", and adapt the mobile span-hiding to the new structure as well. Keep the top-bar hiding adjustments and privileged.css. Verify on an attachment file page.

Current composition (FS row, current-composition cell):

> Sigma-9（/files/theme/sigma-9/sigma-9.css）＋storage上書き（header-bg.png、黒→#002bbd、topbar #535353→#3c3c3c、top140/23pxオーバーレイ、h1 150%、モバイル「SCP-JP ストレージ」）＋privileged.css

In English: Sigma-9 (/files/theme/sigma-9/sigma-9.css) + storage overrides (header-bg.png, black → #002bbd, topbar #535353 → #3c3c3c, top140/23px overlay, h1 150%, mobile "SCP-JP ストレージ") + privileged.css.

The judgment basis for this package is §3 (the FS adjustment inventory, F1–F8) and §4 of `REPORT24.md`, vendored in this repo at `review/AUTHORITIES/REPORT24.md`. Citations of the form "REPORT24 F1" throughout this README resolve there.

**Deployment.** Deploying means replacing the file served at `original.css`'s Source URL (see the Provenance table) in the SCP-JP GitHub Pages tree. That tree is outside this repo and outside campaign authority, so this package is a proposal record until a site admin applies it. Rollback is restoring the mirrored `original.css` in place of the deployed file.

## What a reader of the site will notice

One thing, and only in the title text. Under Sigma-9, the desktop header showed the site name, "SCP-JPファイルストレージ", read from the h1 span. Under this port the span is never rendered at any width (the Sigma-10 base hides it unconditionally), so the header reads "SCP-JP ストレージ" at every width, desktop included. That is the replacement string the requirement chose, not an accident of the port (see change class 4). Everything else is visually identical by construction: the same banner image at the same size, the same two gradients (their values are written out literally, with the same color stops), the same overlay band geometry and shadow, and the same title size rule. And until a site admin deploys the candidate, nothing changes at all: production still serves the original.

## Provenance

FS is not a Wikidot theme page. Its theme is a static CSS file served from SCP-JP's GitHub Pages tree, which the site's internal-style layer loads into every page. So the "original at the reference revision" in this package is not a page revision but a capture of the served files, taken on 2026-11-15 (Asia/Tokyo). Every mirror below is byte-identical to its capture, and anyone can re-verify that against the hashes.

| File | Source | Role | Captured | SHA-256 |
|---|---|---|---|---|
| `original.css` | https://scp-jp.github.io/files/util/storage/styles/theme.css | The FS override layer itself. It imports the Sigma-9 base and privileged.css, and every storage-specific rule is set in this file. This is the file the candidate replaces. | Captured 2026-11-15 | `2c6a67f37b8e0293f03f94b153a75611f3e56aba43a17cf7fcd20427cbc82e81` |
| `original-privileged.css` | https://manage.scp-jp.com/api/public/privileged.css?sid=4548695&required_level=moderator | The admin stylesheet the original imports (moderator permission scope; user-target hiding aimed at named staff accounts). A mirror for the record only; no candidate exists for it (see "Deliberately unchanged"). | Captured 2026-11-15 | `ac5488624888359e72d405cb45c447bb377682d7b22d58efb9fccafd9931ab23` |
| `candidate.css` | — (authored here) | The ported override layer. It plays the same role as `original.css`, on the Sigma-10 base. Deploying means replacing the file at `original.css`'s Source URL above with this file. | Authored 2026-11-17 | — |
| `diff.md` | — (generated) | The unified diff `original.css` → `candidate.css`, generated by `review/build_review.py`. Do not hand-edit it. | Generated 2026-11-17 | — |

Reference captures used for the structural comparisons (evidence captures, distinct from the mirrors above: neither is a file the port replaces). Both are in this package, so that every Verify step below is executable from this repo alone:

- `reference-sigma-9.css` — the stock Sigma-9 base (30,638 B), SHA-256 `69d856fed1eb75998b4be68024ff20441d672066660a8c83eaef70db143087b8`. The file that `original.css`'s first `@import` loads. Captured 2026-11-15, in the same capture set as the mirrors.
- `reference-sigma10-jp.css` — the Sigma-10 JP base as captured (20,312 B), SHA-256 `2057dd4383be635bd239716615f3eafa9af036fd6197017efd7ee476c3ab6ab8`. The CSS behind the check wiki's `theme:sigma-10-jp`; its delivery point is https://scp-jp.github.io/sigma/css/sigma.min.css (SCP-JP/sigma; the base cascade is KanekoLiku/sigma). Captured 2026-11-15.

## Summary

FS (scp-jp-storage.wikidot.com) is SCP-JP's attachment-file storage wiki. Its entire visual identity is one 46-line CSS file laid over a stock base: a blue header gradient with the storage banner image, a dark gradient band under the header, an enlarged site title, and a mobile title string. In the migration, the file's underlay changes from Sigma-9 to Sigma-10, and three of its rules collide with the new base. The custom properties the file defines are an interface Sigma-10 does not have, and Sigma-10 prints the header title itself (the "SCP" + "財団" pseudo-elements, with the real site-name span hidden), which breaks the storage title. So the candidate swaps the base import, writes the two gradients out at their use sites, and replaces both title pseudo-elements, so that the header reads exactly "SCP-JP ストレージ". Everything else, including the admin privileged.css import and the title size, is left as it is. The whole diff is 3 hunks, +14 / −16 lines; 6 of the added lines are a review-stage comment that will not ship (see "Delivery-stage forms" under each change class; the port itself is +8 / −16).

## Change classes

### 1. Base import: Sigma-9 → Sigma-10 (diff hunk 1)

**What changed.** The first `@import` now loads the Sigma-10 JP delivery point `https://scp-jp.github.io/sigma/css/sigma.min.css` instead of the copy of Sigma-9 uploaded to the FS wiki, `/files/theme/sigma-9/sigma-9.css`. The change is one line, and it does not touch the privileged.css import directly below it, so the cascade order (base → privileged → this file's own rules) is preserved.

**Why.** By the requirement's first sentence: 「Sigma-10をベースにします」 ("Base it on Sigma-10"). Every later rule in this file is written against Sigma-9's header geometry and title structure; leaving the Sigma-9 import in place would keep the whole site on the old base. The chosen URL is the production Sigma-10 JP artifact, the same delivery point the Sigma-10 check wiki uses through `theme:sigma-10-jp` (canonical repo: `pages/theme:sigma-10-jp.txt`).

**Verify.** Hunk 1 of `diff.md`. `grep -n "sigma-9" candidate.css` returns nothing. The import URL matches the one in `pages/theme:sigma-10-jp.txt`.

**Delivery-stage forms.** None. This line is in its final deployed form; the URL is the production delivery point, not a draft or check-wiki host.

### 2. Header background: storage image re-layered, gradient written out (diff hunk 2, first rule)

**What changed.** The `div#container-wrap` background keeps the storage banner image (`header-bg.png`; the root-relative URL is byte-identical) and `background-size: 100px 141px`, and its second layer is now the literal `linear-gradient(180deg, black 25%, #002bbd 100%)` instead of `var(--c-header)`. The `#container-wrap` rule that defined `--c-header` and `--c-topbar` is deleted.

**Why.** By the requirement: 「ヘッダー背景、グラデーション、オーバーレイは、Sigma-10のヘッダーとトップバーと競合するため再表現します」 ("the header background, gradient, and overlay conflict with Sigma-10's header and top bar, so re-express them"). The `--c-*` variables are the interface of ukwhatn's "Sigma9 Customizable Header" layer, and under Sigma-9 other rules consume them. But the Sigma-10 JP base has no consumer of `--c-header` / `--c-topbar` anywhere (REPORT24 F1), and inside this file each variable has exactly one use site. Keeping the definitions would preserve, inert, a customization interface that does not exist in the new base. Writing each value out at its single use site keeps the drawn gradient identical (from black at the 25% stop to `#002bbd`; the "black → #002bbd" the /start row records).

**Verify.** Compare the gradient's color stops against the `--c-header` definition deleted in hunk 2 of `diff.md`. The image URL and `background-size` lines are context (unchanged) lines in the same hunk. The Sigma-10 capture in this package contains no `--c-` variable at all: `grep -c -- "--c-" reference-sigma10-jp.css` counts 0 lines.

**Delivery-stage forms.** None. Once the candidate replaces the original at its original path on GitHub Pages, the root-relative image URL resolves exactly as the original's does.

### 3. Top-bar overlay band: gradient written out, band kept (diff hunk 2, second rule)

**What changed.** `div#container-wrap::after` keeps every value except its background (position, `top: 140px`, `height: 23px`, and the drop shadow are all unchanged), and the background changes from `var(--c-topbar)` to the literal `linear-gradient(180deg, #535353 0%, #3c3c3c 53%)`. This is the same write-out as change class 2.

**Why.** By the same requirement sentence, and by REPORT24 F3's conditional decision. Sigma-10 already places `#top-bar` at `top: 140px` with a height of 21px, so re-expressing this band is warranted only if the storage gradient and shadow are still wanted, and the /start row lists the overlay ("top140/23px overlay") as a component to re-express, not to delete. This band colors the strip behind the top-bar menu and casts the header's shadow. The Sigma-10 JP base gives `#top-bar` itself no background, so dropping the band would put the menu directly on top of the header gradient and lose the shadow. The header geometry is the same in both bases (`#header` height 140px, padding-bottom 22px), so the original 140px / 23px placement is still the right placement.

**Verify.** Compare the gradient's color stops against the `--c-topbar` definition deleted in hunk 2 of `diff.md`. Every other declaration in the same rule is a context line. The `#top-bar` geometry in the Sigma-10 capture in this package: `grep -o "#top-bar{[^}]*}" reference-sigma10-jp.css` shows `top:140px` and `height:21px`.

**Delivery-stage forms.** None.

### 4. Site title: both pseudo-elements replaced (diff hunk 3)

**What changed.** The Sigma-9 layer's mobile-only block (`@media(max-width:768px)`: hides `h1 a span` and shows `::before { content: "SCP-JP ストレージ"; font-size: 25px }`) is replaced by two unconditional rules: `#header h1 a::before { content: "SCP-JP ストレージ" }` and `#header h1 a::after { content: none }`. The span-hiding rule is not carried over.

**Why.** By the requirement: 「固定「SCP財団」の疑似要素は「SCP-JP ストレージ」に置き換え、モバイルのspan非表示も新しい構造に合わせます」 ("replace the fixed 'SCP財団' pseudo-element with 'SCP-JP ストレージ', and adapt the mobile span-hiding to the new structure"), and by the preamble of the /start section: 「Sigma-10ではどちらのWikiでも、ヘッダーが「SCP財団」を疑似要素で固定し、サイト名のh1 spanを隠します」 ("in Sigma-10, on both wikis, the header fixes 'SCP財団' with pseudo-elements and hides the site name's h1 span"). Concretely, the Sigma-10 JP base sets `#header h1 a span { font-size: 0 }` **at all widths** and carries `#header h1 a::before { content: 'SCP' }` and `#header h1 a::after { content: '財団' }`. The shape of this change follows from three consequences of that:

- The base already hides the span, so a span-hiding rule in the candidate would be dead code. The Sigma-9 layer's "mobile span-hiding" is absorbed into the new structure, exactly as the requirement anticipated.
- Overriding only `::before` (the naive port of the Sigma-9 rule) would render "SCP-JP ストレージ財団". REPORT24 F5 names exactly this failure. Both pseudo-elements must be set, so that the final title is exactly "SCP-JP ストレージ".
- The base shows its pseudo-title at all widths, so the replacement is unconditional too. The visible consequence is that the desktop header's title string changes: under Sigma-9 the desktop header showed the site-name span, "SCP-JPファイルストレージ"; under Sigma-10 the span is never rendered, and the header shows the requirement's chosen string, "SCP-JP ストレージ", at all widths.

**Verify.** Hunk 3 of `diff.md`. The three base rules quoted above are present in the Sigma-10 capture in this package: `grep -o "#header h1 a span{[^}]*}" reference-sigma10-jp.css` gives `font-size:0`, and the matching `::before` / `::after` greps give `content:'SCP'` and `content:'財団'`. The candidate's two content values are the requirement's string and `none`.

**Delivery-stage forms.** Six of the added lines are the `REVIEW:` comment above the `::before` rule (see "Judgment calls"). That is a package-stage annotation, not part of the port; it is resolved when the title-size question is settled, and removed before deployment. No other line in this hunk is a delivery-stage form.

## Deliberately unchanged

- **privileged.css rule.** privileged.css is managed externally, is kept exactly as it is, and never receives a candidate. It is served by `manage.scp-jp.com` at a moderator-permission-scope URL and operated outside the theme system, and the requirement orders it kept (「privileged.cssは維持します」, "keep privileged.css"; REPORT24 F6). The import line in `candidate.css` is byte-identical to the original's, in the same position (immediately after the base import), so its cascade position is preserved. `original-privileged.css` is in this package only as a mirror for the record.
- **Title size rule (REPORT24 F4).** `#header h1 a { font-size: 150% }` is carried over as it is. The Sigma-10 base sets `1.5em` on the same element, so this rule is a no-op on the new base. It stays because the storage title size should be stated by the layer that owns the title, and REPORT24's decision is likewise "carries as-is".
- **Attribution block.** ukwhatn's "Sigma9 Customizable Header" comment (author, source, CC BY-SA 3.0) is carried over as it is. The override layer's design and values still derive from that file, and the license notice is not ours to strip. (The `--c-*` interface itself goes away, per change class 2; the comment remains as the layer's provenance.)
- **Banner image URL and size.** `/files/util/storage/media/component/theme/header-bg.png` and `background-size: 100px 141px` are byte-identical (change class 2).
- **Overlay geometry and shadow.** The `top: 140px`, `height: 23px`, and `box-shadow` values are byte-identical (change class 3).
- **Layers outside this file.** The site-wide top-bar hiding block (REPORT24 F7: `#top-bar a.newpage`, `.top-startlink`, and the hiding of one top-bar div) and the shared `#side-bar .menu-item` block (F8) are served by separate site-wide style layers, and were captured in the same 2026-11-15 capture set (the sitewide top-bar block and the shared sidebar block; REPORT24 F7/F8 record their substance). The requirement keeps them (「top-bar非表示の調整…は維持します」, "keep the top-bar hiding adjustments"; REPORT24 §4, FS item 4), and the port neither carries them over nor deletes them: they are verified at the render check, not edited.

## Judgment calls and open questions

- **REVIEW — title size on mobile.** The only `REVIEW:` comment in `candidate.css`, placed above the `::before` rule. The Sigma-9 layer fixed the mobile title at 25px. The candidate sets no size on the pseudo-elements, so Sigma-10's own `#header h1 a` sizing governs (1.5em on desktop; `calc(.75em + 2vw)` inside the `max-width: 767px` block). The requirement orders the replacement of the title **string** and the adaptation of the span-hiding, not the size, so this is the shape chosen. If the storage title should keep a fixed 25px on mobile, the addition is a single media rule, and it should be decided at the render check, comparing against the current title at real device widths.
- **Band height 23px vs Sigma-10's 21px bar.** The candidate keeps the band at the original 23px instead of shrinking it to Sigma-10's 21px bar. The band is a background strip, not the bar itself; in both bases the header area is 140px plus 22px of bottom padding, and the band's 2px overshoot and its shadow fall into that padding area exactly as they did under Sigma-9. Changing the height would move the shadow, and no requirement asks for that.
- **Desktop title text.** As recorded in change class 4, after the migration the header reads "SCP-JP ストレージ" at all widths, which differs from the "SCP-JPファイルストレージ" (the site name) that the Sigma-9 desktop showed. This is a consequence of the requirement's chosen replacement string combined with Sigma-10's always-on span hiding, stated here explicitly as a reviewed consequence, not a deployment surprise.
- **Questions only site-admin access can settle** (carried over from REPORT24 §5, unresolved). In FS's Site Manager settings, whether the imported theme file is the only site-theme source, and which of the served style blocks are the admin Custom CSS field. Whether privileged.css (sid 4548695) is still applied to FS, and whether its user-target hiding is still needed. Whether the migrated override layer will be placed in the imported theme file or in the Custom CSS field.
- **Verification status, restated.** Everything in this package is source-level: file hashes, the generated diff, rule-by-rule comparison against the two captured bases. The render check the requirement names (「添付ファイルページで確認します」, "verify on an attachment file page"; the check on an attachment file page, the very purpose FS exists for) has not been performed, because the candidate is not yet deployed anywhere a browser can load it. No statement in this package claims rendered behavior.

## License and attribution

- **Title:** Sigma9 Customizable Header — SCP-JP storage site theme.css
- **Author:** ukwhatn
- **Source:** https://scp-jp.github.io/files/util/storage/styles/theme.css — static file captured 2026-11-15 (no Wikidot page revision); original notice cites http://scp-jp-sandbox3.wikidot.com/draft:3396310-168-9905
- **License:** Creative Commons Attribution-ShareAlike 3.0 (CC BY-SA 3.0) — license deed: https://creativecommons.org/licenses/by-sa/3.0/
- **Adaptation:** This package holds a Sigma-10 port of the site's CSS; changes were made. See "Summary" and "Change classes" in this README for what changed and why. Translator: not applicable — static site CSS, no translated prose; the port is a source-level rewrite.
