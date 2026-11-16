# INDEX — pattern knowledge base

Every pattern the Sigma-10 reviews have confirmed, as a mechanism with
an executable static detection recipe. Read SWEEP-PROTOCOL.md before
running a sweep. SUPPLEMENT-TYPES.md is the reference catalogue of JP
localization supplement types (A13) behind KB-11, KB-16, KB-63 and
KB-64.

**Detection-cost derivation rule.** Each pattern's cost class is
derived from its own recipe: **pure grep** when a single-file grep or
selector scan of the candidate decides the cell; **cross-file diff**
when the recipe needs the candidate compared against another text (its
branch original, its resolved base, the production counterpart, or the
shared sample source); **needs live probe** when static evidence
cannot decide the cell, i.e. the recipe's deciding step is a HEAD or
fullname probe, a live follow-up diff, a wiki-state read, or a render
confirmation (all TRIAGE patterns land here, as do file-provable
patterns whose proof is a probe, e.g. KB-02 and KB-05). Sweeps run
cheapest first (see SWEEP-PROTOCOL.md).

| ID | File | Title | Class | Detection cost | Provability |
|---|---|---|---|---|---|

| KB-01 | [KB-01.md](KB-01.md) | Unencoded colon in an asset URL path segment | A. Theme defect, file-provable | pure grep | FILE-PROVABLE |
| KB-02 | [KB-02.md](KB-02.md) | Genuinely dead asset reference | A. Theme defect, file-provable | needs live probe | FILE-PROVABLE |
| KB-03 | [KB-03.md](KB-03.md) | Malformed CSS resource declaration: `url(null)`, unterminated `url(`, elided placeholder | A. Theme defect, file-provable | pure grep | FILE-PROVABLE |
| KB-04 | [KB-04.md](KB-04.md) | Malformed Google Fonts @import (hyphens where `+` is required) | A. Theme defect, file-provable | cross-file diff | FILE-PROVABLE |
| KB-05 | [KB-05.md](KB-05.md) | Asset served with a non-CSS MIME type (one defect, two engine faces) | A. Theme defect, file-provable | needs live probe | FILE-PROVABLE |
| KB-06 | [KB-06.md](KB-06.md) | Unsubstituted include variable rendered literally | A. Theme defect, file-provable | cross-file diff | FILE-PROVABLE |
| KB-07 | [KB-07.md](KB-07.md) | Interwiki-style include defect family (duplicate priority, missing priority, double include, missing include) | A. Theme defect, file-provable | pure grep | FILE-PROVABLE |
| KB-08 | [KB-08.md](KB-08.md) | iftags gate anomaly (bare `[[iftags]]` with no condition) | A. Theme defect, file-provable | pure grep | FILE-PROVABLE |
| KB-09 | [KB-09.md](KB-09.md) | Duplicate bare `[[module Rate]]` beside the rate-bearing preview credit module | A. Theme defect, file-provable | pure grep | FILE-PROVABLE |
| KB-10 | [KB-10.md](KB-10.md) | Credit furniture missing or incomplete (no-credit, no-rate, credit-missing-fields) | A. Theme defect, file-provable | pure grep | FILE-PROVABLE |
| KB-11 | [KB-11.md](KB-11.md) | JP credit-module localization supplement missing from the candidate (3law-pride class) | A. Theme defect, file-provable | cross-file diff | FILE-PROVABLE |
| KB-12 | [KB-12.md](KB-12.md) | JP credit-module supplement present but ineffective (night-rush class) | A. Theme defect, file-provable | cross-file diff | FILE-PROVABLE |
| KB-13 | [KB-13.md](KB-13.md) | Global `.modalbox` fixed centering pins the static credit replica at viewport centre (space class) | A. Theme defect, file-provable | pure grep | FILE-PROVABLE |
| KB-14 | [KB-14.md](KB-14.md) | Cross-theme / original-delivery code import (localize pattern 4) | A. Theme defect, file-provable | pure grep | FILE-PROVABLE |
| KB-15 | [KB-15.md](KB-15.md) | Foreign include kept where a verified JP counterpart exists (pattern 1, live form); wrong-form and wrong-slug variants | A. Theme defect, file-provable | needs live probe | FILE-PROVABLE |
| KB-16 | [KB-16.md](KB-16.md) | JP font load gap (localize pattern 7) | A. Theme defect, file-provable | cross-file diff | FILE-PROVABLE |
| KB-17 | [KB-17.md](KB-17.md) | Font and asset host violations (localize pattern 5) | A. Theme defect, file-provable | pure grep | FILE-PROVABLE |
| KB-18 | [KB-18.md](KB-18.md) | Untranslated visible text, including CSS `content:` strings (pattern 10 / T5) | A. Theme defect, file-provable | cross-file diff | FILE-PROVABLE |
| KB-19 | [KB-19.md](KB-19.md) | Follow-up delta unincorporated (T4 follow-up half) | A. Theme defect, file-provable | needs live probe | FILE-PROVABLE |
| KB-20 | [KB-20.md](KB-20.md) | Oversize candidate from inlined base material | A. Theme defect, file-provable | cross-file diff | FILE-PROVABLE |
| KB-21 | [KB-21.md](KB-21.md) | Fragile asset reference form (stray space and http scheme inside an include parameter) | A. Theme defect, file-provable | pure grep | FILE-PROVABLE |
| KB-22 | [KB-22.md](KB-22.md) | Candidate-own runtime hotlink hosts (judgment-required signal) | A. Theme defect, file-provable | needs live probe | TRIAGE |
| KB-23 | [KB-23.md](KB-23.md) | Candidate fixed min-width page-overflow | B. Theme defect, triage only | needs live probe | TRIAGE |
| KB-24 | [KB-24.md](KB-24.md) | Narrow-width header clipping / collision | B. Theme defect, triage only | needs live probe | TRIAGE |
| KB-25 | [KB-25.md](KB-25.md) | WebKit-only absence of the mobile sidebar-open control (betwixt class) | B. Theme defect, triage only | needs live probe | TRIAGE |
| KB-26 | [KB-26.md](KB-26.md) | WebKit sidebar-not-opening with the control present (marchen class) | B. Theme defect, triage only | needs live probe | TRIAGE |
| KB-27 | [KB-27.md](KB-27.md) | Mobile sidebar toggle missing in BOTH engines | B. Theme defect, triage only | needs live probe | TRIAGE |
| KB-28 | [KB-28.md](KB-28.md) | Unreadable color pair (theme palette applied to the wrong surface) | B. Theme defect, triage only | needs live probe | TRIAGE |
| KB-29 | [KB-29.md](KB-29.md) | Hidden interwiki frame at render (`hidden-interwiki` on all combos) | B. Theme defect, triage only | needs live probe | TRIAGE |
| KB-30 | [KB-30.md](KB-30.md) | Hidden login-status at render (`hidden-login`) | B. Theme defect, triage only | needs live probe | TRIAGE |
| KB-31 | [KB-31.md](KB-31.md) | Credit-modal overflow on real-module pages | B. Theme defect, triage only | needs live probe | TRIAGE |
| KB-32 | [KB-32.md](KB-32.md) | Credit-modal error on preview-module pages (preview-form) | C. Cross-cutting, not a defect | pure grep | FILE-PROVABLE |
| KB-33 | [KB-33.md](KB-33.md) | Static credit replica fixed-width overflow on samples (337-419px and 884px shapes) | C. Cross-cutting, not a defect | cross-file diff | FILE-PROVABLE |
| KB-34 | [KB-34.md](KB-34.md) | Preview-notice row clipping / overprint at narrow widths | C. Cross-cutting, not a defect | cross-file diff | FILE-PROVABLE |
| KB-35 | [KB-35.md](KB-35.md) | Site-header subtitle doubling at ≤375px | C. Cross-cutting, not a defect | pure grep | FILE-PROVABLE |
| KB-36 | [KB-36.md](KB-36.md) | WebKit stray "S" glyph for the CC badge | C. Cross-cutting, not a defect | pure grep | FILE-PROVABLE |
| KB-37 | [KB-37.md](KB-37.md) | Deliberate specimen shapes on display-check samples | C. Cross-cutting, not a defect | cross-file diff | FILE-PROVABLE |
| KB-38 | [KB-38.md](KB-38.md) | `sidebar-position` warn against the Sigma-9 baseline | C. Cross-cutting, not a defect | pure grep | FILE-PROVABLE |
| KB-39 | [KB-39.md](KB-39.md) | Machine contrast warn false positives | C. Cross-cutting, not a defect | cross-file diff | FILE-PROVABLE |
| KB-40 | [KB-40.md](KB-40.md) | Site-theme sigma.min.css runtime-hotlink chain | D. Environment-layer | pure grep | FILE-PROVABLE |
| KB-41 | [KB-41.md](KB-41.md) | Draft-host references (pseudo-ref / draft-host info) | D. Environment-layer | pure grep | FILE-PROVABLE |
| KB-42 | [KB-42.md](KB-42.md) | http-scheme URLs (posting scheme rewrite) | D. Environment-layer | pure grep | FILE-PROVABLE |
| KB-43 | [KB-43.md](KB-43.md) | Interwiki-frame stylesheet 404 from shared styleFrame.html infrastructure | D. Environment-layer | pure grep | FILE-PROVABLE |
| KB-44 | [KB-44.md](KB-44.md) | Transient Wikidot 503 capture (http.cat + hidden-* signature) | E. Capture/measurement artefact | pure grep | FILE-PROVABLE |
| KB-45 | [KB-45.md](KB-45.md) | Measurement non-completion (exit 2 / no summary.md; networkidle baseline failure) | E. Capture/measurement artefact | pure grep | FILE-PROVABLE |
| KB-46 | [KB-46.md](KB-46.md) | Screenshot ceiling incompleteness (32,767px cap, Chromium white-out) | E. Capture/measurement artefact | pure grep | FILE-PROVABLE |
| KB-47 | [KB-47.md](KB-47.md) | Single-combo ORB / load-failed flakiness (asset-host artefact) | E. Capture/measurement artefact | pure grep | FILE-PROVABLE |
| KB-48 | [KB-48.md](KB-48.md) | Blank body from test-wiki page tag state (iftags gate vs page tags) | E. Capture/measurement artefact | needs live probe | FILE-PROVABLE |
| KB-49 | [KB-49.md](KB-49.md) | Stale static-cache phantom rendering | E. Capture/measurement artefact | needs live probe | FILE-PROVABLE |
| KB-50 | [KB-50.md](KB-50.md) | `hidden-rate` machine line false shapes | E. Capture/measurement artefact | pure grep | FILE-PROVABLE |
| KB-51 | [KB-51.md](KB-51.md) | Scanner and extraction artefacts in include/dead-reference scans | E. Capture/measurement artefact | needs live probe | FILE-PROVABLE |
| KB-52 | [KB-52.md](KB-52.md) | amethyst-v2: no candidate can be produced | F. Named exception / standing disposition | pure grep | FILE-PROVABLE |
| KB-53 | [KB-53.md](KB-53.md) | Sigma-10 itself: environment-form, no sample by construction | F. Named exception / standing disposition | pure grep | FILE-PROVABLE |
| KB-54 | [KB-54.md](KB-54.md) | Foreign includes with no JP equivalent (FIX-MECH six / opinions-broadcaster) | F. Named exception / standing disposition | needs live probe | FILE-PROVABLE |
| KB-55 | [KB-55.md](KB-55.md) | Candela granular parallel imports (bundle would change the palette) | F. Named exception / standing disposition | pure grep | FILE-PROVABLE |
| KB-56 | [KB-56.md](KB-56.md) | Peroxide escaped documentation family | F. Named exception / standing disposition | pure grep | FILE-PROVABLE |
| KB-57 | [KB-57.md](KB-57.md) | Header and title language kept in English (pattern 9, ruling 2) | F. Named exception / standing disposition | pure grep | FILE-PROVABLE |
| KB-58 | [KB-58.md](KB-58.md) | Deferred asset 404s (draft-bucket hosting state) | F. Named exception / standing disposition | needs live probe | FILE-PROVABLE |
| KB-59 | [KB-59.md](KB-59.md) | `@@[[footnoteblock]]@@` literal exhibits (staff-call, pending) | F. Named exception / standing disposition | pure grep | FILE-PROVABLE |
| KB-60 | [KB-60.md](KB-60.md) | Production license-box form uncertainty (do not convert forms) | F. Named exception / standing disposition | pure grep | FILE-PROVABLE |
| KB-61 | [KB-61.md](KB-61.md) | Basalt /7 normalize fragment completeness (role, not bytes) | F. Named exception / standing disposition | cross-file diff | FILE-PROVABLE |
| KB-62 | [KB-62.md](KB-62.md) | fa-info rule absence in OWN credit candidates (A4 sub-pattern) | B. Theme defect, triage only | cross-file diff | TRIAGE |
| KB-63 | [KB-63.md](KB-63.md) | JP license box dropped by a candidate whose original carried one | A. Theme defect, file-provable | cross-file diff | FILE-PROVABLE |
| KB-64 | [KB-64.md](KB-64.md) | Bare component:sigma-plus include bypassing the JP port | A. Theme defect, file-provable | pure grep | FILE-PROVABLE |
| KB-65 | [KB-65.md](KB-65.md) | Duplicated @import lines | A. Theme defect, file-provable | pure grep | FILE-PROVABLE |

Total: 65 patterns (KB-01 to KB-65), plus SWEEP-PROTOCOL.md and SUPPLEMENT-TYPES.md.
