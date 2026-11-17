# Sigma base audit — is SCP-JP/sigma's total diff against scpwiki/sigma minimal?

This record stands outside the 287 theme-row verdicts: it audits the Sigma-10 base itself (SCP-JP/sigma against scpwiki/sigma). The full lane reports (HALF1-LOCALIZATION.md, HALF1-MACHINERY.md, HALF2-UPSTREAM.md) and the coordinator census live in the campaign record at muse-bhl/theme-port-readiness-20261114/sigma-audit/. No PRs were opened against either sigma repo; publication routes through the owner.

Date: 2026-11-17. Auditor: the Sigma-10 review supervisor fleet (lanes sigma-half1a, sigma-half1b, sigma-half2; coordinator synthesis and spot verification). Repos (read-only clones): JP /home/roku/src/SCP-JP/sigma (main 63a6be9), EN /home/roku/src/scpwiki/sigma (main e1c339f). No PRs opened anywhere; this is an audit.

## Structure of the thing being audited

SCP-JP/sigma is not a fork with shared history. It is a thin wrapper: it pins scpwiki/sigma as the git submodule "origin" at 84d8171abbeb5cc0b4e6c2f80ef553e08a053359 (EN main of 2025-12-30), and its build.sh delivers JP Sigma-10 as: origin/sigma.css, with asset hosts rewritten by sed (cdn.scpwiki.com/theme/en -> scp-jp.github.io, 4 URLs), plus localization.css (224 lines) appended. The delivered diff against EN-at-pin is 5 hunks, 232 changed lines (coordinator census, census/ in this directory). The audit therefore has two non-overlapping halves: what JP adds on top of the pin, and what EN added after the pin that JP has not taken.

## Verdict

**The JP-side diff is nearly minimal, and the port is missing four upstream fixes it needs.** Of 33 distinct JP-side differences, 28 are necessary (16 localization-necessary, 12 functional JP requirements), 4 are unmotivated drift (all harmless, all precisely identified below), and 1 is a defect: the already-adjudicated Info-module hide of issue #3722. In the other direction, EN has moved 52 commits past the pin; of 37 classified drift items, 4 are needed for correctness or parity and JP has taken none of them. The proximate cause is process, not judgment: the weekly sync workflow refuses to open a new sync PR while one is open, and the sync PR of 2026-01-17 was never merged, so the pin has been frozen for about ten months.

## Half 1 — JP's own changes (33 distinct differences)

CSS payload (19 items; full table in HALF1-LOCALIZATION.md): 13 (a), 4 (b), 1 (c), 1 (d).
Machinery (16 items, of which the sed and the append mechanism are the same two differences seen from the build side; full table in HALF1-MACHINERY.md): 5 (a), 8 (b), 3 (c), 0 (d).
Unified: (a) 16, (b) 12, (c) 4, (d) 1.

Method note (calibration): the localization lane's five-step test (base selector census, cascade position, comment-versus-bytes scope check, deletion outcome, class assignment) reaches class (d) for the .creditRate rules from the diff alone: the base has no creditRate rule and the native Info module is visible; the overlay's comment claims a preview-only scope; the bytes hide ul.creditRate > li unconditionally; deleting the rules restores base behavior. That is removal of base-provided behavior, hence (d). The same test classified the other 18 payload items.

The four (c) items, staff-report form:
1. localization.css L13-15, #header background-image: sets the header logo to the scp-jp.github.io URL that the build's sed rewrite already produces from the base rule (base L182). Byte-level no-op; deleting it changes nothing.
2. .github/workflows/deploy.yaml action bumps (checkout v1->v6, upload-pages-artifact v3->v5, deploy-pages v4->v5): dependabot-driven, versions verified to exist and work, no JP ground for diverging from the pin's versions.
3. .github/workflows/lint.yaml checkout v1->v6: same, no JP ground.
4. package-lock.json: the devDependency ranges are identical between JP main and EN-at-pin; the lockfile difference is regeneration shadow (newer npm, lockfileVersion 3 vs 2, within-range patch resolutions). No independent content.

The one (d) item, staff-report form: localization.css L85-100 (.creditRate::before banner + .creditRate > li { display: none }). Stated intent (comment, commit 3f87176): fix preview-time display breakage of the credit and Info modules. Actual effect: the Info module is hidden on every saved page, permanently, and the banner text states the opposite of what is true. Repair: scope the hide to the preview context or remove the two rules; deletion restores the base behavior exactly. Recorded as Rokurolize/wikijump issue #3722.

Machinery (d)-candidates examined and cleared with grounds (full text in HALF1-MACHINERY.md): the composed CSS is never linted (residual risk only; both inputs are linted in their own CIs, the concatenation boundary verified clean); the literal sed pattern would miss a future EN host change (latent risk, correct at the pin); the stale pin (the pin design itself, measured in Half 2); standalone npm run minify on a generated file (usage caveat, the documented build path generates first). Nothing necessary is missing on the machinery axis: fonts/ and images/ are carried byte-identical inside the submodule.

## Half 2 — upstream drift (37 items; full table in HALF2-UPSTREAM.md)

(i) needed 4, (ii) optional 24, (iii) not applicable to JP 9. All 31 sigma.css hunks (zero-context census), the RedactRect.woff2 binary, and 5 config/workflow artifacts are classified; EN build.sh is unchanged over the range, and none of the drift hunks touch the sed-rewritten host strings, so taking any item is mechanically clean.

The (i) take-list:
1. sigma.css body font-family: RedactRect moved to the head of the stack (EN eba6331). Redaction blocks only render with the purpose-built block glyph when RedactRect leads; JP uses the same markup and ships the same font.
2. fonts/RedactRect.woff2 at EN HEAD (4284 -> 4148 bytes; EN e779f4a removes the SVG color-glyph layer and widens the block outline). Pairs with item 1.
3. sigma.css .page-rate-widget-box: margin-right: 2em removed (EN ce2b030). Aligns the right-floating rate module.
4. sigma.css .scp-image-block.block-right: margin 0 2em 1em -> 0 0 1em 2em (EN ce2b030). Gutter belongs on the left of a right-floated block. JP's mobile scp-clear-true rule still wins for cleared blocks at <=767px, as intended.

The (ii) 24 are cosmetic notation churn (rgba() -> rgb() and prettier normalization from EN's stylelint-17 upgrade), visually identical. The (iii) 9 are EN-site-specific: the iOS-cache notification relocation and its comments, the no-drafts button-hiding policy rules, and EN's tooling/dependabot/workflow updates, none of which JP's build needs.

Sync state: the pin history advanced 2025-07-06 -> 2025-11-16 -> 2025-12-20 -> 2026-01-03 with lags of hours to weeks; the next sync branch (origin/sync/260117-020806, pin 748bb0fc) was opened 2026-01-17 and never merged, and sync-submodule.yaml's check_pr step ("Exit if PR exists") has blocked every later sync since. Even that branch is 50 commits behind EN HEAD. Recommendation, staff-report form: merge or close the stalled sync PR to unblock the weekly bot, and take the four (i) items (they can also be applied directly: three one-line CSS changes via a pin advance, plus the font binary the pin advance carries).

## Bottom line

Minimal? On JP's own side, yes except for one defect and four harmless drifts, each named with its repair above. Complete? No: four upstream correctness/parity items are untaken, and the mechanism that should have delivered them has been stalled by one unmerged PR since January. Both statements are exhaustive over the measured surface: every delivered-diff hunk and every drift hunk carries a class and a ground in the lane reports.

SIGMA-AUDIT: COMPLETE
