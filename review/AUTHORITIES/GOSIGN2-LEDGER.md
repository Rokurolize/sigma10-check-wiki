# GOSIGN2 go-sign ledger — Sigma-10 theme campaign

Assembled 2026-11-17 from the full evidence stack: GOSIGN-TESTS.md (test definitions), the four ledger parts (population, T1, T2/T3 render rows including the 17-theme rerun, T4/T5 localize rows), all FIX-wave reports (FIX-MECH, FIX-CREDIT-A/B/C/D, FIX-P4, FIX2-*, FIX3-*, FIX4-*), the credit verification report, the patterns layer (KB-01..KB-65, SWEEP-RESULTS.tsv, NEGATIVE-LEDGER.md), the supervisor state file, and the owner’s five rulings of 2026-11-16. A current-state check_source.py run over all 287 population files (2026-11-17, ledger assembly) is used to verify which baseline error classes still stand. Evidence work only: no canonical page was edited for this ledger.

## (a) Population

The population is the 287 rows of `start-themes.tsv` (canonical repo, origin grouping per commit 9d1f2b8), joined on normalized fullname. By origin (TSV `page` column): EN 157, CN 87, KO 40, JP 2, FR 1 — total 287.

Render measurement arithmetic: 269 themes measured in the first pass (RENDER-ROWS-1: 104, RENDER-ROWS-2: 148 of its 156, RENDER-ROWS-G: 27, with the parts’ own overlaps resolved in the population check) + 17 themes re-measured in RENDER-ROWS-RERUN16 (superseding the 17 unmeasured RENDER-ROWS-2 rows) + 1 NOT-RUN (theme:amethyst-v2, the named exception) = 287. T1 and T4/T5 rows cover 287/287 after the alias normalization recorded in LEDGER-POPULATION-CHECK.md (telecom long/short forms; amethyst’s three spellings are one population row; the Sigma-10 row’s fullname is theme:sigma-10-jp).

Coverage caveats (measurement limits, not theme defects): (1) In RENDER-ROWS-G, 36 of 54 runs are Chromium-only, so those themes carry no WebKit verdict; the caveat is recorded per theme in the register where it applies. (2) Several sample-page runs returned no machine verdict (render_check exit 2, no summary): the affected rows are named in the register; T3 screenshot walks still apply where the row reports them. (3) One width of one blankstyle capture hit a transient Wikidot 503 and is unjudgeable (KB-44 family).

## (b) Per-theme table

T1 = source check (current-state run; FINDINGS (classified) means every standing error belongs to a dispositioned class in register c1). T2/T3 = combined render verdict from the render rows. T4/T5 = combined localize verdict from LOCALIZE-ROWS. Overall = PASS only when every finding for the theme is fixed or dispositioned with grounds in register (c); NOT PASS names the blocking OPEN items in section (e).

| # | Theme | Origin | T1 | T2/T3 | T4 | T5 | Overall |
|---|---|---|---|---|---|---|---|
| 1 | theme:aesthetic-theme-jp | EN | FINDINGS (classified) | FINDINGS | FINDINGS | FINDINGS | PASS |
| 2 | theme:al-slop-jp | EN | FINDINGS (classified) | FINDINGS | FINDINGS | FINDINGS | PASS |
| 3 | theme:basalt-jp | EN | FINDINGS (classified) | FINDINGS | FINDINGS | FINDINGS | PASS |
| 4 | theme:bedrock-jp | EN | FINDINGS (classified) | FINDINGS | FINDINGS | FINDINGS | PASS |
| 5 | theme:black-highlighter-theme-jp | EN | FINDINGS (classified) | FINDINGS | FINDINGS | FINDINGS | PASS |
| 6 | theme:blankstyle-jp | EN | PASS | FINDINGS | FINDINGS | FINDINGS | NOT PASS — OPEN items (e) |
| 7 | theme:classic-jp | EN | FINDINGS (classified) | FINDINGS | FINDINGS | FINDINGS | PASS |
| 8 | theme:cosmonaut-jp | EN | FINDINGS (classified) | FINDINGS | FINDINGS | FINDINGS | PASS |
| 9 | theme:dear-dictator-jp | KO | FINDINGS (classified) | FINDINGS | FINDINGS | FINDINGS | PASS |
| 10 | theme:extra-black-highlighter-theme-jp | EN | FINDINGS (classified) | FINDINGS | FINDINGS | FINDINGS | PASS |
| 11 | theme:flopstyle-jp | EN | FINDINGS (classified) | FINDINGS | FINDINGS | FINDINGS | PASS |
| 12 | theme:flopstyle-dark-jp | EN | FINDINGS (classified) | FINDINGS | FINDINGS | FINDINGS | PASS |
| 13 | theme:foxtrot-jp | EN | FINDINGS (classified) | FINDINGS | FINDINGS | FINDINGS | PASS |
| 14 | theme:halloween-jp | EN | FINDINGS (classified) | FINDINGS | FINDINGS | FINDINGS | PASS |
| 15 | theme:hansarp-jp | EN | FINDINGS (classified) | FINDINGS | FINDINGS | FINDINGS | PASS |
| 16 | theme:inkblot-jp | EN | FINDINGS (classified) | FINDINGS | FINDINGS | FINDINGS | PASS |
| 17 | theme:isolated-terminal-jp | EN | FINDINGS (classified) | FINDINGS | FINDINGS | FINDINGS | PASS |
| 18 | theme:jakstyle-jp | EN | FINDINGS (classified) | FINDINGS | FINDINGS | FINDINGS | PASS |
| 19 | theme:just-girly-things-jp | EN | FINDINGS (classified) | FINDINGS | FINDINGS | FINDINGS | PASS |
| 20 | theme:min-theme-jp | JP | PASS | FINDINGS | N/A | N/A | PASS |
| 21 | theme:minimalist-bhl-jp | EN | FINDINGS (classified) | FINDINGS | PASS | PASS | NOT PASS — OPEN items (e) |
| 22 | theme:monotypical-jp | EN | FINDINGS (classified) | FINDINGS | FINDINGS | FINDINGS | PASS |
| 23 | theme:much-cool-jp | EN | FINDINGS (classified) | FINDINGS | FINDINGS | FINDINGS | PASS |
| 24 | theme:night-rush-theme-jp | EN | FINDINGS (classified) | FINDINGS | FINDINGS | FINDINGS | PASS |
| 25 | theme:ouroborous-theme-jp | EN | FINDINGS (classified) | FINDINGS | FINDINGS | FINDINGS | PASS |
| 26 | theme:paperstack-jp | EN | FINDINGS (classified) | FINDINGS | FINDINGS | FINDINGS | PASS |
| 27 | theme:pataphysics-jp | EN | PASS | FINDINGS | FINDINGS | FINDINGS | NOT PASS — OPEN items (e) |
| 28 | theme:penumbra-jp | EN | FINDINGS (classified) | FINDINGS | FINDINGS | FINDINGS | NOT PASS — OPEN items (e) |
| 29 | theme:quand-le-soleil-se-couche | FR | FINDINGS (classified) | FINDINGS | FINDINGS | FINDINGS | NOT PASS — OPEN items (e) |
| 30 | theme:redtape-jp | EN | FINDINGS (classified) | FINDINGS | PASS | PASS | PASS |
| 31 | theme:scheme-jp | EN | FINDINGS (classified) | FINDINGS | FINDINGS | FINDINGS | PASS |
| 32 | theme:scp-human-resources-jp | EN | PASS | FINDINGS | FINDINGS | FINDINGS | NOT PASS — OPEN items (e) |
| 33 | theme:scp-offices-theme-jp | EN | FINDINGS (classified) | FINDINGS | FINDINGS | FINDINGS | NOT PASS — OPEN items (e) |
| 34 | theme:scpedia-jp | EN | FINDINGS (classified) | FINDINGS | FINDINGS | FINDINGS | PASS |
| 35 | theme:shushuin-jp | JP | PASS | FINDINGS | N/A | N/A | PASS |
| 36 | theme:sigma-jp | EN | FINDINGS (classified) | FINDINGS | FINDINGS | FINDINGS | PASS |
| 37 | theme:sigma-10-jp | EN | FINDINGS (classified) | FINDINGS | PASS | PASS | PASS |
| 38 | theme:simple-yonder-jp | EN | FINDINGS (classified) | FINDINGS | FINDINGS | FINDINGS | PASS |
| 39 | theme:skipos-jp | EN | FINDINGS (classified) | FINDINGS | FINDINGS | FINDINGS | PASS |
| 40 | theme:space-jp | EN | FINDINGS (classified) | FINDINGS | FINDINGS | FINDINGS | NOT PASS — OPEN items (e) |
| 41 | theme:turbo-vision-jp | EN | FINDINGS (classified) | FINDINGS | FINDINGS | FINDINGS | PASS |
| 42 | theme:wikifot-jp | EN | FINDINGS (classified) | FINDINGS | FINDINGS | FINDINGS | PASS |
| 43 | theme:y2k-jp | EN | FINDINGS (classified) | FINDINGS | FINDINGS | FINDINGS | NOT PASS — OPEN items (e) |
| 44 | theme:yossistyle-jp | EN | PASS | FINDINGS | FINDINGS | FINDINGS | NOT PASS — OPEN items (e) |
| 45 | theme:3law-pride-jp | EN | FINDINGS (classified) | FINDINGS | FINDINGS | FINDINGS | PASS |
| 46 | theme:3lawcracked-jp | EN | FINDINGS (classified) | FINDINGS | FINDINGS | FINDINGS | PASS |
| 47 | theme:512-onwards-jp | EN | FINDINGS (classified) | FINDINGS | FINDINGS | FINDINGS | PASS |
| 48 | theme:5k-jp | EN | FINDINGS (classified) | FINDINGS | FINDINGS | FINDINGS | PASS |
| 49 | theme:a-problematic-theme-jp | EN | FINDINGS (classified) | PASS-WITH-NOTES | FINDINGS | FINDINGS | PASS |
| 50 | theme:aces-and-eights-jp | EN | FINDINGS (classified) | FINDINGS | FINDINGS | FINDINGS | PASS |
| 51 | theme:ad-abyssum-penumbra-jp | EN | FINDINGS (classified) | FINDINGS | FINDINGS | FINDINGS | PASS |
| 52 | theme:admo-jp | EN | FINDINGS (classified) | FINDINGS | FINDINGS | FINDINGS | PASS |
| 53 | theme:alcur-theme-jp | EN | FINDINGS (classified) | FINDINGS | FINDINGS | FINDINGS | PASS |
| 54 | theme:alexylva-university-jp | EN | FINDINGS (classified) | FINDINGS | FINDINGS | FINDINGS | PASS |
| 55 | theme:ambrose-chapter-two-jp | EN | FINDINGS (classified) | FINDINGS | FINDINGS | FINDINGS | PASS |
| 56 | theme:angel-jp | EN | FINDINGS (classified) | FINDINGS | FINDINGS | FINDINGS | NOT PASS — OPEN items (e) |
| 57 | theme:anon-jp | EN | FINDINGS (classified) | PASS-WITH-NOTES | FINDINGS | FINDINGS | PASS |
| 58 | theme:art-deco-jp | EN | PASS | FINDINGS | FINDINGS | FINDINGS | PASS |
| 59 | theme:ashes-to-ashes-jp | EN | FINDINGS (classified) | PASS-WITH-NOTES | FINDINGS | FINDINGS | PASS |
| 60 | theme:bedbugs-theme-jp | EN | FINDINGS (classified) | FINDINGS | FINDINGS | FINDINGS | PASS |
| 61 | theme:black-diamond-jp | EN | FINDINGS (classified) | FINDINGS | FINDINGS | FINDINGS | PASS |
| 62 | theme:black-market-jp | EN | FINDINGS (classified) | FINDINGS | FINDINGS | FINDINGS | PASS |
| 63 | theme:black-serpent-jp | EN | FINDINGS (classified) | FINDINGS | FINDINGS | FINDINGS | PASS |
| 64 | theme:blood-jp | EN | FINDINGS (classified) | FINDINGS | FINDINGS | FINDINGS | PASS |
| 65 | theme:bloodraven-jp | EN | FINDINGS (classified) | FINDINGS | FINDINGS | FINDINGS | PASS |
| 66 | theme:borealis-constant-theme-jp | EN | FINDINGS (classified) | PASS-WITH-NOTES | FINDINGS | FINDINGS | PASS |
| 67 | theme:caretaker-sigma-jp | EN | FINDINGS (classified) | FINDINGS | FINDINGS | FINDINGS | PASS |
| 68 | theme:caretaker-theme-jp | EN | FINDINGS (classified) | FINDINGS | FINDINGS | FINDINGS | PASS |
| 69 | theme:ch-scp-theme-jp | EN | FINDINGS (classified) | FINDINGS | FINDINGS | FINDINGS | PASS |
| 70 | theme:chaos-jp | EN | FINDINGS (classified) | FINDINGS | FINDINGS | FINDINGS | PASS |
| 71 | theme:cleaning-services-jp | EN | FINDINGS (classified) | FINDINGS | FINDINGS | FINDINGS | PASS |
| 72 | theme:clock-tower-jp | EN | FINDINGS (classified) | FINDINGS | FINDINGS | FINDINGS | PASS |
| 73 | theme:cosmos-jp | EN | FINDINGS (classified) | FINDINGS | FINDINGS | FINDINGS | PASS |
| 74 | theme:crayon-jp | EN | FINDINGS (classified) | PASS-WITH-NOTES | FINDINGS | FINDINGS | PASS |
| 75 | theme:dark-jp | EN | FINDINGS (classified) | FINDINGS | FINDINGS | FINDINGS | PASS |
| 76 | theme:dark-dealings-jp | EN | FINDINGS (classified) | FINDINGS | FINDINGS | FINDINGS | PASS |
| 77 | theme:darkqueer-jp | EN | FINDINGS (classified) | FINDINGS | FINDINGS | FINDINGS | PASS |
| 78 | theme:decom-dept-jp | EN | FINDINGS (classified) | FINDINGS | FINDINGS | FINDINGS | PASS |
| 79 | theme:derby-jp | EN | FINDINGS (classified) | FINDINGS | FINDINGS | FINDINGS | PASS |
| 80 | theme:dia-de-muertos-jp | EN | FINDINGS (classified) | FINDINGS | FINDINGS | FINDINGS | PASS |
| 81 | theme:diamond-highlighter-jp | EN | FINDINGS (classified) | FINDINGS | FINDINGS | FINDINGS | PASS |
| 82 | theme:dynamikron-jp | EN | FINDINGS (classified) | FINDINGS | FINDINGS | FINDINGS | PASS |
| 83 | theme:eigenmachine-jp | EN | FINDINGS (classified) | FINDINGS | FINDINGS | FINDINGS | NOT PASS — OPEN items (e) |
| 84 | theme:eigenvector-jp | EN | FINDINGS (classified) | FINDINGS | FINDINGS | FINDINGS | PASS |
| 85 | theme:enlightened-eyes-jp | EN | FINDINGS (classified) | FINDINGS | FINDINGS | FINDINGS | PASS |
| 86 | theme:eventyr-jp | EN | FINDINGS (classified) | FINDINGS | FINDINGS | FINDINGS | PASS |
| 87 | theme:fandom-jp | EN | FINDINGS (classified) | FINDINGS | FINDINGS | FINDINGS | PASS |
| 88 | theme:febris-pharmaceuticals-theme-jp | EN | FINDINGS (classified) | FINDINGS | PASS | PASS | NOT PASS — OPEN items (e) |
| 89 | theme:fish-jp | EN | FINDINGS (classified) | FINDINGS | PASS | PASS | NOT PASS — OPEN items (e) |
| 90 | theme:fossil-jp | EN | FINDINGS (classified) | FINDINGS | FINDINGS | FINDINGS | PASS |
| 91 | theme:frownstyle-jp | EN | FINDINGS (classified) | FINDINGS | FINDINGS | FINDINGS | NOT PASS — OPEN items (e) |
| 92 | theme:fuladh-theme-jp | EN | FINDINGS (classified) | FINDINGS | FINDINGS | FINDINGS | PASS |
| 93 | theme:galactic-theme-jp | EN | FINDINGS (classified) | FINDINGS | FINDINGS | FINDINGS | PASS |
| 94 | theme:golden-feast-jp | EN | FINDINGS (classified) | FINDINGS | FINDINGS | FINDINGS | PASS |
| 95 | theme:greystyle-jp | EN | FINDINGS (classified) | FINDINGS | FINDINGS | FINDINGS | PASS |
| 96 | theme:helix-jp | EN | FINDINGS (classified) | FINDINGS | FINDINGS | FINDINGS | PASS |
| 97 | theme:highroller-jp | EN | FINDINGS (classified) | FINDINGS | FINDINGS | FINDINGS | PASS |
| 98 | theme:hytoth-two-jp | EN | FINDINGS (classified) | FINDINGS | FINDINGS | FINDINGS | PASS |
| 99 | theme:i57-jp | EN | FINDINGS (classified) | FINDINGS | FINDINGS | FINDINGS | PASS |
| 100 | theme:i57-theme-jp | EN | FINDINGS (classified) | FINDINGS | FINDINGS | FINDINGS | PASS |
| 101 | theme:immrama-jp | EN | FINDINGS (classified) | FINDINGS | FINDINGS | FINDINGS | PASS |
| 102 | theme:internal-affairs-jp | EN | FINDINGS (classified) | FINDINGS | FINDINGS | FINDINGS | PASS |
| 103 | theme:janitor-closet-jp | EN | FINDINGS (classified) | FINDINGS | FINDINGS | FINDINGS | PASS |
| 104 | theme:kiryu-labs-theme-jp | EN | FINDINGS (classified) | FINDINGS | FINDINGS | FINDINGS | PASS |
| 105 | theme:lampeter-warm-jp | EN | FINDINGS (classified) | FINDINGS | FINDINGS | FINDINGS | PASS |
| 106 | theme:laruetheme-jp | EN | FINDINGS (classified) | FINDINGS | FINDINGS | FINDINGS | PASS |
| 107 | theme:last-frontier-jp | EN | FINDINGS (classified) | FINDINGS | FINDINGS | FINDINGS | PASS |
| 108 | theme:laughter-and-knives-theme-jp | EN | FINDINGS (classified) | FINDINGS | FINDINGS | FINDINGS | PASS |
| 109 | theme:linear-black-jp | EN | FINDINGS (classified) | FINDINGS | FINDINGS | FINDINGS | NOT PASS — OPEN items (e) |
| 110 | theme:lumina-jp | EN | FINDINGS (classified) | FINDINGS | FINDINGS | FINDINGS | PASS |
| 111 | theme:magpie-swoops-jp | EN | FINDINGS (classified) | FINDINGS | FINDINGS | FINDINGS | PASS |
| 112 | theme:maxwell-s-silver-hammer-jp | EN | FINDINGS (classified) | FINDINGS | FINDINGS | FINDINGS | PASS |
| 113 | theme:mcf-jp | EN | FINDINGS (classified) | FINDINGS | FINDINGS | FINDINGS | PASS |
| 114 | theme:oceanbound-jp | EN | FINDINGS (classified) | FINDINGS | FINDINGS | FINDINGS | PASS |
| 115 | theme:old-money-theme-jp | EN | FINDINGS (classified) | FINDINGS | PASS | PASS | NOT PASS — OPEN items (e) |
| 116 | theme:onko-sinulla-nalka-theme-jp | EN | FINDINGS (classified) | FINDINGS | PASS | PASS | PASS |
| 117 | theme:ordopharm-jp | EN | FINDINGS (classified) | FINDINGS | FINDINGS | FINDINGS | PASS |
| 118 | theme:our-open-veins-jp | EN | FINDINGS (classified) | FINDINGS | FINDINGS | FINDINGS | PASS |
| 119 | theme:pack-of-peanuts-jp | EN | FINDINGS (classified) | FINDINGS | PASS | PASS | PASS |
| 120 | theme:paramycota-jp | EN | FINDINGS (classified) | FINDINGS | PASS | PASS | PASS |
| 121 | theme:parawatch-pumpkin-jp | EN | FINDINGS (classified) | FINDINGS | PASS | PASS | PASS |
| 122 | theme:pastel-skies-jp | EN | FINDINGS (classified) | FINDINGS | FINDINGS | FINDINGS | PASS |
| 123 | theme:plant-jp | EN | FINDINGS (classified) | FINDINGS | FINDINGS | FINDINGS | PASS |
| 124 | theme:prom-labs-jp | EN | FINDINGS (classified) | FINDINGS | FINDINGS | FINDINGS | PASS |
| 125 | theme:queen-s-gambit-jp | EN | FINDINGS (classified) | FINDINGS | FINDINGS | FINDINGS | PASS |
| 126 | theme:queerstyle-jp | EN | FINDINGS (classified) | FINDINGS | FINDINGS | FINDINGS | NOT PASS — OPEN items (e) |
| 127 | theme:ragnarok-theme-jp | EN | FINDINGS (classified) | FINDINGS | FINDINGS | FINDINGS | PASS |
| 128 | theme:raisa-jp | EN | FINDINGS (classified) | FINDINGS | FINDINGS | FINDINGS | NOT PASS — OPEN items (e) |
| 129 | theme:raisa-sigma-jp | EN | FINDINGS (classified) | FINDINGS | FINDINGS | FINDINGS | PASS |
| 130 | theme:retro-aiad-theme-jp | EN | FINDINGS (classified) | FINDINGS | FINDINGS | FINDINGS | NOT PASS — OPEN items (e) |
| 131 | theme:retrofutura-jp | EN | FINDINGS (classified) | FINDINGS | FINDINGS | FINDINGS | PASS |
| 132 | theme:saphir-jp | EN | FINDINGS (classified) | FINDINGS | FINDINGS | FINDINGS | NOT PASS — OPEN items (e) |
| 133 | theme:scp-human-resources-sigma-jp | EN | FINDINGS (classified) | FINDINGS | FINDINGS | FINDINGS | PASS |
| 134 | theme:scp-offices-sigma-jp | EN | FINDINGS (classified) | FINDINGS | FINDINGS | FINDINGS | PASS |
| 135 | theme:shark-punching-centre-bhl-jp | EN | FINDINGS (classified) | FINDINGS | FINDINGS | FINDINGS | PASS |
| 136 | theme:shattered-thoughts-jp | EN | FINDINGS (classified) | FINDINGS | FINDINGS | FINDINGS | NOT PASS — OPEN items (e) |
| 137 | theme:shoebill-jp | EN | FINDINGS (classified) | FINDINGS | FINDINGS | FINDINGS | PASS |
| 138 | theme:skiesmadestrange-jp | EN | FINDINGS (classified) | FINDINGS | FINDINGS | FINDINGS | NOT PASS — OPEN items (e) |
| 139 | theme:spidersfalling-jp | EN | FINDINGS (classified) | FINDINGS | FINDINGS | FINDINGS | NOT PASS — OPEN items (e) |
| 140 | theme:stargazer-jp | EN | FINDINGS (classified) | FINDINGS | FINDINGS | FINDINGS | PASS |
| 141 | theme:stellar-jp | EN | FINDINGS (classified) | FINDINGS | FINDINGS | FINDINGS | PASS |
| 142 | theme:sunside-jp | EN | FINDINGS (classified) | FINDINGS | FINDINGS | FINDINGS | NOT PASS — OPEN items (e) |
| 143 | theme:tales-of-the-mosaic-jp | EN | FINDINGS (classified) | FINDINGS | FINDINGS | FINDINGS | NOT PASS — OPEN items (e) |
| 144 | theme:telecom-office-theme-jp | EN | PASS | FINDINGS | FINDINGS | FINDINGS | PASS |
| 145 | theme:thalassophobia-jp | EN | FINDINGS (classified) | FINDINGS | FINDINGS | FINDINGS | PASS |
| 146 | theme:thalassophobia-sigma-jp | EN | FINDINGS (classified) | FINDINGS | FINDINGS | FINDINGS | PASS |
| 147 | theme:the-coalition-theme-jp | EN | FINDINGS (classified) | FINDINGS | FINDINGS | FINDINGS | PASS |
| 148 | theme:the-foundation-sigma-jp | EN | FINDINGS (classified) | FINDINGS | FINDINGS | FINDINGS | NOT PASS — OPEN items (e) |
| 149 | theme:the-smell-of-smoke-jp | EN | FINDINGS (classified) | FINDINGS | FINDINGS | FINDINGS | PASS |
| 150 | theme:turbo-vision-dark-jp | EN | FINDINGS (classified) | FINDINGS | FINDINGS | FINDINGS | PASS |
| 151 | theme:twin-files-jp | EN | FINDINGS (classified) | FINDINGS | FINDINGS | FINDINGS | NOT PASS — OPEN items (e) |
| 152 | theme:ui-jp | EN | FINDINGS (classified) | FINDINGS | FINDINGS | FINDINGS | NOT PASS — OPEN items (e) |
| 153 | theme:uiu-bhl-theme-jp | EN | FINDINGS (classified) | FINDINGS | FINDINGS | FINDINGS | NOT PASS — OPEN items (e) |
| 154 | theme:unusual-cargo-jp | EN | FINDINGS (classified) | FINDINGS | FINDINGS | FINDINGS | PASS |
| 155 | theme:vanguard-jp | EN | FINDINGS (classified) | FINDINGS | FINDINGS | FINDINGS | NOT PASS — OPEN items (e) |
| 156 | theme:vanguard-supplement-jp | EN | FINDINGS (classified) | FINDINGS | FINDINGS | FINDINGS | NOT PASS — OPEN items (e) |
| 157 | theme:wilderness-jp | EN | FINDINGS (classified) | FINDINGS | FINDINGS | FINDINGS | NOT PASS — OPEN items (e) |
| 158 | theme:wondertainment-jp | EN | FINDINGS (classified) | FINDINGS | FINDINGS | FINDINGS | NOT PASS — OPEN items (e) |
| 159 | theme:words-of-wisdom-jp | EN | FINDINGS (classified) | FINDINGS | FINDINGS | FINDINGS | NOT PASS — OPEN items (e) |
| 160 | theme:writing-anomalies-jp | EN | FINDINGS (classified) | FINDINGS | FINDINGS | FINDINGS | NOT PASS — OPEN items (e) |
| 161 | theme:xmas-jp | EN | FINDINGS (classified) | FINDINGS | FINDINGS | FINDINGS | PASS |
| 162 | theme:amethyst-v2 | CN | EXCEPTION | NOT-RUN | N/A | N/A | EXCEPTION (named) |
| 163 | theme:andesite-jp | CN | FINDINGS (classified) | FINDINGS | FINDINGS | FINDINGS | NOT PASS — OPEN items (e) |
| 164 | theme:another-night-jp | CN | FINDINGS (classified) | FINDINGS | FINDINGS | FINDINGS | PASS |
| 165 | theme:ared-jp | CN | FINDINGS (classified) | FINDINGS | FINDINGS | FINDINGS | PASS |
| 166 | theme:asagao-jp | CN | FINDINGS (classified) | FINDINGS | FINDINGS | FINDINGS | PASS |
| 167 | theme:betwixt-jp | CN | FINDINGS (classified) | FINDINGS | FINDINGS | FINDINGS | NOT PASS — OPEN items (e) |
| 168 | theme:black-rain-jp | CN | FINDINGS (classified) | FINDINGS | FINDINGS | FINDINGS | PASS |
| 169 | theme:blackinblack-jp | CN | FINDINGS (classified) | FINDINGS | FINDINGS | FINDINGS | PASS |
| 170 | theme:brokedown-database-jp | CN | FINDINGS (classified) | FINDINGS | FINDINGS | FINDINGS | NOT PASS — OPEN items (e) |
| 171 | theme:broken-light-jp | CN | FINDINGS (classified) | FINDINGS | FINDINGS | FINDINGS | PASS |
| 172 | theme:broken-world-jp | CN | FINDINGS (classified) | FINDINGS | FINDINGS | FINDINGS | PASS |
| 173 | theme:candela-jp | CN | FINDINGS (classified) | FINDINGS | FINDINGS | FINDINGS | PASS |
| 174 | theme:cmst-jp | CN | FINDINGS (classified) | FINDINGS | FINDINGS | FINDINGS | PASS |
| 175 | theme:cobalt-aero-glass-jp | CN | FINDINGS (classified) | FINDINGS | PASS | PASS | NOT PASS — OPEN items (e) |
| 176 | theme:construct-jp | CN | FINDINGS (classified) | FINDINGS | FINDINGS | FINDINGS | PASS |
| 177 | theme:copper-jp | CN | FINDINGS (classified) | FINDINGS | FINDINGS | FINDINGS | NOT PASS — OPEN items (e) |
| 178 | theme:crt-jp | CN | FINDINGS (classified) | FINDINGS | FINDINGS | FINDINGS | NOT PASS — OPEN items (e) |
| 179 | theme:darkblue-jp | CN | FINDINGS (classified) | FINDINGS | FINDINGS | FINDINGS | NOT PASS — OPEN items (e) |
| 180 | theme:decay-jp | CN | FINDINGS (classified) | FINDINGS | FINDINGS | FINDINGS | NOT PASS — OPEN items (e) |
| 181 | theme:deepspace-jp | CN | FINDINGS (classified) | FINDINGS | FINDINGS | FINDINGS | NOT PASS — OPEN items (e) |
| 182 | theme:deserted-years-theme-jp | CN | FINDINGS (classified) | FINDINGS | FINDINGS | FINDINGS | PASS |
| 183 | theme:dream-of-the-stars-jp | CN | FINDINGS (classified) | FINDINGS | FINDINGS | FINDINGS | PASS |
| 184 | theme:drunken-alley-jp | CN | FINDINGS (classified) | FINDINGS | FINDINGS | FINDINGS | NOT PASS — OPEN items (e) |
| 185 | theme:dustframe-jp | CN | PASS | FINDINGS | PASS | PASS | PASS |
| 186 | theme:emotion-division-jp | CN | FINDINGS (classified) | FINDINGS | FINDINGS | FINDINGS | PASS |
| 187 | theme:ethic-committee-jp | CN | FINDINGS (classified) | FINDINGS | FINDINGS | FINDINGS | PASS |
| 188 | theme:fmd-bhl-theme-jp | CN | FINDINGS (classified) | FINDINGS | FINDINGS | FINDINGS | NOT PASS — OPEN items (e) |
| 189 | theme:food-jp | CN | FINDINGS (classified) | FINDINGS | FINDINGS | FINDINGS | PASS |
| 190 | theme:foundom-jp | CN | FINDINGS (classified) | FINDINGS | FINDINGS | FINDINGS | PASS |
| 191 | theme:frutiger-aero-jp | CN | FINDINGS (classified) | FINDINGS | FINDINGS | FINDINGS | NOT PASS — OPEN items (e) |
| 192 | theme:golden-wind-jp | CN | FINDINGS (classified) | FINDINGS | FINDINGS | FINDINGS | NOT PASS — OPEN items (e) |
| 193 | theme:gp-refresh-jp | CN | FINDINGS (classified) | FINDINGS | FINDINGS | FINDINGS | NOT PASS — OPEN items (e) |
| 194 | theme:greyday-jp | CN | FINDINGS (classified) | FINDINGS | FINDINGS | FINDINGS | NOT PASS — OPEN items (e) |
| 195 | theme:gsk-jp | CN | FINDINGS (classified) | FINDINGS | FINDINGS | FINDINGS | PASS |
| 196 | theme:highlighter-bhl-jp | CN | FINDINGS (classified) | FINDINGS | FINDINGS | FINDINGS | PASS |
| 197 | theme:horn-jp | CN | FINDINGS (classified) | FINDINGS | FINDINGS | FINDINGS | PASS |
| 198 | theme:ink-jp | CN | FINDINGS (classified) | FINDINGS | FINDINGS | FINDINGS | NOT PASS — OPEN items (e) |
| 199 | theme:inland-empire-jp | CN | FINDINGS (classified) | FINDINGS | FINDINGS | FINDINGS | PASS |
| 200 | theme:kitchen-jp | CN | FINDINGS (classified) | FINDINGS | FINDINGS | FINDINGS | NOT PASS — OPEN items (e) |
| 201 | theme:lead-by-example-jp | CN | FINDINGS (classified) | FINDINGS | FINDINGS | FINDINGS | PASS |
| 202 | theme:madoka-jp | CN | FINDINGS (classified) | FINDINGS | FINDINGS | FINDINGS | PASS |
| 203 | theme:magazine-jp | CN | FINDINGS (classified) | FINDINGS | FINDINGS | FINDINGS | NOT PASS — OPEN items (e) |
| 204 | theme:magicity-jp | CN | FINDINGS (classified) | FINDINGS | FINDINGS | FINDINGS | NOT PASS — OPEN items (e) |
| 205 | theme:marchen-jp | CN | FINDINGS (classified) | FINDINGS | FINDINGS | FINDINGS | NOT PASS — OPEN items (e) |
| 206 | theme:mox-jp | CN | FINDINGS (classified) | FINDINGS | FINDINGS | FINDINGS | PASS |
| 207 | theme:nameless-jp | CN | FINDINGS (classified) | FINDINGS | FINDINGS | FINDINGS | PASS |
| 208 | theme:normal-jp | CN | FINDINGS (classified) | FINDINGS | FINDINGS | FINDINGS | PASS |
| 209 | theme:obflow-jp | CN | FINDINGS (classified) | FINDINGS | FINDINGS | FINDINGS | PASS |
| 210 | theme:oneiroi-west-jp | CN | FINDINGS (classified) | FINDINGS | FINDINGS | FINDINGS | PASS |
| 211 | theme:opinions-broadcaster-jp | CN | FINDINGS (classified) | FINDINGS | FINDINGS | FINDINGS | PASS |
| 212 | theme:parablue-jp | CN | FINDINGS (classified) | FINDINGS | FINDINGS | FINDINGS | PASS |
| 213 | theme:paradigm-inapplicable-jp | CN | FINDINGS (classified) | FINDINGS | FINDINGS | FINDINGS | NOT PASS — OPEN items (e) |
| 214 | theme:paradigm-inapplicable-sigma-jp | CN | FINDINGS (classified) | FINDINGS | FINDINGS | FINDINGS | NOT PASS — OPEN items (e) |
| 215 | theme:paradigm-reconstruction-jp | CN | FINDINGS (classified) | FINDINGS | FINDINGS | FINDINGS | NOT PASS — OPEN items (e) |
| 216 | theme:parallel-jp | CN | FINDINGS (classified) | FINDINGS | FINDINGS | FINDINGS | PASS |
| 217 | theme:peroxide-jp | CN | FINDINGS (classified) | FINDINGS | FINDINGS | FINDINGS | NOT PASS — OPEN items (e) |
| 218 | theme:petrifaction-jp | CN | FINDINGS (classified) | FINDINGS | FINDINGS | FINDINGS | PASS |
| 219 | theme:progress-institute-jp | CN | FINDINGS (classified) | FINDINGS | FINDINGS | FINDINGS | NOT PASS — OPEN items (e) |
| 220 | theme:redsquare-jp | CN | FINDINGS (classified) | FINDINGS | FINDINGS | FINDINGS | PASS |
| 221 | theme:rima-jp | CN | FINDINGS (classified) | FINDINGS | FINDINGS | FINDINGS | NOT PASS — OPEN items (e) |
| 222 | theme:sci-fi-jp | CN | FINDINGS (classified) | FINDINGS | FINDINGS | FINDINGS | NOT PASS — OPEN items (e) |
| 223 | theme:scpdeclassified-jp | CN | FINDINGS (classified) | FINDINGS | FINDINGS | FINDINGS | NOT PASS — OPEN items (e) |
| 224 | theme:scplive-jp | CN | FINDINGS (classified) | FINDINGS | FINDINGS | FINDINGS | NOT PASS — OPEN items (e) |
| 225 | theme:shancheng-jp | CN | FINDINGS (classified) | FINDINGS | FINDINGS | FINDINGS | NOT PASS — OPEN items (e) |
| 226 | theme:share-future-community-jp | CN | FINDINGS (classified) | FINDINGS | FINDINGS | FINDINGS | NOT PASS — OPEN items (e) |
| 227 | theme:shivering-night-jp | CN | FINDINGS (classified) | FINDINGS | FINDINGS | FINDINGS | NOT PASS — OPEN items (e) |
| 228 | theme:sodium-jp | CN | FINDINGS (classified) | FINDINGS | FINDINGS | FINDINGS | NOT PASS — OPEN items (e) |
| 229 | theme:sodium-pentasulfide-jp | CN | FINDINGS (classified) | FINDINGS | FINDINGS | FINDINGS | PASS |
| 230 | theme:sound-jp | CN | FINDINGS (classified) | FINDINGS | FINDINGS | FINDINGS | NOT PASS — OPEN items (e) |
| 231 | theme:starbasalt-jp | CN | FINDINGS (classified) | FINDINGS | FINDINGS | FINDINGS | NOT PASS — OPEN items (e) |
| 232 | theme:starry-jp | CN | FINDINGS (classified) | FINDINGS | FINDINGS | FINDINGS | NOT PASS — OPEN items (e) |
| 233 | theme:steam-guide-jp | CN | FINDINGS (classified) | FINDINGS | FINDINGS | FINDINGS | NOT PASS — OPEN items (e) |
| 234 | theme:supply-n-demand-jp | CN | FINDINGS (classified) | FINDINGS | FINDINGS | FINDINGS | NOT PASS — OPEN items (e) |
| 235 | theme:suprematism-jp | CN | FINDINGS (classified) | FINDINGS | FINDINGS | FINDINGS | NOT PASS — OPEN items (e) |
| 236 | theme:tfnac-jp | CN | FINDINGS (classified) | FINDINGS | FINDINGS | FINDINGS | PASS |
| 237 | theme:the-other-side-jp | CN | FINDINGS (classified) | FINDINGS | FINDINGS | FINDINGS | PASS |
| 238 | theme:the-track-changers-jp | CN | FINDINGS (classified) | FINDINGS | FINDINGS | FINDINGS | NOT PASS — OPEN items (e) |
| 239 | theme:trauma-jp | CN | FINDINGS (classified) | FINDINGS | FINDINGS | FINDINGS | NOT PASS — OPEN items (e) |
| 240 | theme:travellers-book-jp | CN | FINDINGS (classified) | FINDINGS | FINDINGS | FINDINGS | NOT PASS — OPEN items (e) |
| 241 | theme:ultimate-reader-jp | CN | FINDINGS (classified) | FINDINGS | FINDINGS | FINDINGS | PASS |
| 242 | theme:voyager-jp | CN | FINDINGS (classified) | FINDINGS | FINDINGS | FINDINGS | NOT PASS — OPEN items (e) |
| 243 | theme:walk-in-the-dark-jp | CN | FINDINGS (classified) | FINDINGS | FINDINGS | FINDINGS | PASS |
| 244 | theme:waxed-oxidized-cut-copper-slab-jp | CN | FINDINGS (classified) | FINDINGS | FINDINGS | FINDINGS | PASS |
| 245 | theme:winddew-in-hand-jp | CN | FINDINGS (classified) | FINDINGS | FINDINGS | FINDINGS | NOT PASS — OPEN items (e) |
| 246 | theme:winxp-jp | CN | FINDINGS (classified) | FINDINGS | FINDINGS | FINDINGS | PASS |
| 247 | theme:wish-for-miracle-jp | CN | FINDINGS (classified) | FINDINGS | FINDINGS | FINDINGS | PASS |
| 248 | theme:yore-jp | CN | FINDINGS (classified) | FINDINGS | FINDINGS | FINDINGS | PASS |
| 249 | theme:07k-jp | KO | FINDINGS (classified) | FINDINGS | FINDINGS | FINDINGS | NOT PASS — OPEN items (e) |
| 250 | theme:a-midnight-invitation-jp | KO | FINDINGS (classified) | FINDINGS | FINDINGS | FINDINGS | NOT PASS — OPEN items (e) |
| 251 | theme:animal-instead-of-beast-jp | KO | FINDINGS (classified) | FINDINGS | FINDINGS | FINDINGS | NOT PASS — OPEN items (e) |
| 252 | theme:anniversary-jp | KO | FINDINGS (classified) | FINDINGS | FINDINGS | FINDINGS | PASS |
| 253 | theme:atlas-maniacus-jp | KO | FINDINGS (classified) | FINDINGS | FINDINGS | FINDINGS | PASS |
| 254 | theme:back-jan-fire-jp | KO | FINDINGS (classified) | FINDINGS | FINDINGS | FINDINGS | NOT PASS — OPEN items (e) |
| 255 | theme:bulgunae-jp | KO | FINDINGS (classified) | FINDINGS | FINDINGS | FINDINGS | PASS |
| 256 | theme:chatscp-jp | KO | FINDINGS (classified) | FINDINGS | FINDINGS | FINDINGS | PASS |
| 257 | theme:creature-jp | KO | FINDINGS (classified) | FINDINGS | FINDINGS | FINDINGS | NOT PASS — OPEN items (e) |
| 258 | theme:cyber-specter-jp | KO | FINDINGS (classified) | FINDINGS | FINDINGS | FINDINGS | PASS |
| 259 | theme:doap-bhl-jp | KO | FINDINGS (classified) | FINDINGS | FINDINGS | FINDINGS | PASS |
| 260 | theme:doap-nvl-jp | KO | FINDINGS (classified) | FINDINGS | FINDINGS | FINDINGS | PASS |
| 261 | theme:flowergarden-jp | KO | FINDINGS (classified) | FINDINGS | PASS | PASS | PASS |
| 262 | theme:fmaf-theme-jp | KO | FINDINGS (classified) | FINDINGS | PASS | PASS | PASS |
| 263 | theme:fogwalker-jp | KO | FINDINGS (classified) | FINDINGS | PASS | PASS | PASS |
| 264 | theme:foundation-paper-jp | KO | FINDINGS (classified) | FINDINGS | FINDINGS | FINDINGS | PASS |
| 265 | theme:garak-the-magazine-jp | KO | FINDINGS (classified) | FINDINGS | FINDINGS | FINDINGS | PASS |
| 266 | theme:golden-samdaecheon-jp | KO | FINDINGS (classified) | FINDINGS | FINDINGS | FINDINGS | PASS |
| 267 | theme:halloween-koreana-jp | KO | FINDINGS (classified) | FINDINGS | FINDINGS | FINDINGS | PASS |
| 268 | theme:it-pillar-of-industry-jp | KO | FINDINGS (classified) | FINDINGS | PASS | PASS | PASS |
| 269 | theme:jiha-jp | KO | FINDINGS (classified) | FINDINGS | FINDINGS | FINDINGS | PASS |
| 270 | theme:kcia10-jp | KO | FINDINGS (classified) | FINDINGS | FINDINGS | FINDINGS | PASS |
| 271 | theme:king-s-palace-jp | KO | FINDINGS (classified) | FINDINGS | FINDINGS | FINDINGS | NOT PASS — OPEN items (e) |
| 272 | theme:legend-of-blue-jp | KO | FINDINGS (classified) | FINDINGS | FINDINGS | FINDINGS | PASS |
| 273 | theme:minimal-scp-foundation-by-cocoonist-jp | KO | FINDINGS (classified) | FINDINGS | FINDINGS | FINDINGS | PASS |
| 274 | theme:mole-cricket-jp | KO | FINDINGS (classified) | FINDINGS | PASS | PASS | PASS |
| 275 | theme:mr-reprisal-jp | KO | FINDINGS (classified) | FINDINGS | PASS | PASS | PASS |
| 276 | theme:navla-style-jp | KO | FINDINGS (classified) | FINDINGS | FINDINGS | FINDINGS | PASS |
| 277 | theme:note-theme-jp | KO | FINDINGS (classified) | FINDINGS | PASS | PASS | PASS |
| 278 | theme:ontology-department-jp | KO | FINDINGS (classified) | FINDINGS | FINDINGS | FINDINGS | PASS |
| 279 | theme:pacom1943-jp | KO | FINDINGS (classified) | FINDINGS | FINDINGS | FINDINGS | NOT PASS — OPEN items (e) |
| 280 | theme:past-oriented-jp | KO | FINDINGS (classified) | FINDINGS | FINDINGS | FINDINGS | PASS |
| 281 | theme:path-of-jinin-jp | KO | FINDINGS (classified) | FINDINGS | FINDINGS | FINDINGS | PASS |
| 282 | theme:plugsoft-jp | KO | FINDINGS (classified) | FINDINGS | FINDINGS | FINDINGS | NOT PASS — OPEN items (e) |
| 283 | theme:rok-gov-theme-jp | KO | FINDINGS (classified) | FINDINGS | FINDINGS | FINDINGS | PASS |
| 284 | theme:rpma-jp | KO | FINDINGS (classified) | FINDINGS | FINDINGS | FINDINGS | PASS |
| 285 | theme:some-guider-jp | KO | FINDINGS (classified) | FINDINGS | FINDINGS | FINDINGS | PASS |
| 286 | theme:the-buck-stops-here-jp | KO | PASS | FINDINGS | FINDINGS | FINDINGS | PASS |
| 287 | theme:the-greatest-education-jp | KO | FINDINGS (classified) | FINDINGS | FINDINGS | FINDINGS | PASS |

## (c) Findings register

### c1. T1 (source check) — baseline classes, fix outcomes, standing classes

Baseline (T1-ROWS, pre-fix measurement): 276 files with errors, 2357 errors / 413 warnings / 353 infos. By code: pseudo-ref 1355, hotlink 912, http 46, foreign-include 36 (baseline count in T1-ROWS; SOURCE2 counted 40 lines including escaped examples), old-bhl 5, no-credit 1, no-rate 1, unencoded-colon 1.

Ledger-assembly verification (check_source.py re-run over the current canonical files, 2026-11-17): **credit-missing-fields = 0 population-wide** — the dominant baseline class (pattern 3 section 3 fields) is fully fixed by the credit waves (FIX-CREDIT-A/B/C/D, FIX2-CREDIT 36 files, FIX4-CREDIT KB-11 set), and CREDIT-VERIFY confirms the 11 audited credit themes render their supplements live. The classes that still stand, per class:

- **pseudo-ref** (1337 lines standing): DISPOSITIONED, class (iii) — draft-wiki form. These are references to the draft/check wikis (sigma10-jp-test, scp-jp sandbox hosts) that are the normal form at draft stage and are rewritten to scp-jp at posting (GOSIGN-TESTS.md T1 classification; the rewrite procedure is recorded in /start’s common procedure).
- **hotlink** (887 lines standing): DISPOSITIONED, class (ii) — posting-time rewrites and original-state asset hosts. The campaign’s standing analysis: foreign hosts are rewritten at posting or are the original’s own asset hosts kept as original state; re-upload is barred by owner order, and missing/404 decorative assets are the owner-deferred hosting state (KB-58). Where a fix wave repointed a specific host (FIX-P4 Basalt EN-CDN set, FIX2-DEADREF, FIX4-REPOINT bunny set), the item is FIXED and cited in c3.
- **http** (45 lines standing): DISPOSITIONED, class (ii) — scheme rewrite at posting. The fetched-http CSS subset (7 files / 25 assets, KB-42) is recorded there; w3.org namespace identifiers inside the class are false positives (NEGATIVE-LEDGER NL-07). One theme-level fix executed: steam-guide avatar http→https (FIX4-REPOINT).
- **foreign-include** (36 lines standing, exactly 10 files): DISPOSITIONED per file, matching FIX2-INCLUDE / FIX-MECH / KB-54 one-for-one — peroxide 17 (escaped documentation examples, named exception in FIX2-INCLUDE section 5; the theme’s own delivery is the fragment:peroxide-jp-* candidate set, batch-posted), opinions-broadcaster 3 (KB-54 named exception), flopstyle-dark 4 (KB-54 named exception: snippets:bs-image x3 + :scp-wiki:component:text-style, NOTFOUND-probed, no JP equivalent), foxtrot 2 (KB-54: author-label-source x2, no JP equivalent), dark-dealings 2 + decom-dept 2 (KB-54 named exception, author-label-source; porting the component is a separate staff call per FIX3-S2EN section 6.7), tales-of-the-mosaic 1, parablue 1, parallel 1 (escaped documentation examples, FIX2-INCLUDE). **Exception within the class: rima 3 — OPEN, see section (e) item A2.**
- **old-bhl** (5 lines: suprematism 1, tfnac 2, bulgunae 2): DISPOSITIONED, KB-17 class (ii) — posting-time rewrite to scp-jp.github.io/Black-Highlighter (FIX4-REPOINT).
- **no-credit 1 + no-rate 1**: theme:sigma-10-jp only. DISPOSITIONED as the environment-form named exception (KB-53; FIX-CREDIT-B row 37 exclusion, coordinator-dispositioned). See (d).
- **unencoded-colon 1**: theme:5k-jp L100 only. DISPOSITIONED under KB-01’s own 5k precedent (the encoded form does not serve; do not encode — SWEEP-A1 amendment records this single run-wide occurrence as dispositioned, not a new charge). The 15 theme-level unencoded-colon errors FIX-MECH repaired (blankstyle, flopstyle-dark, foxtrot, minimalist-bhl, night-rush-theme, paperstack, y2k) are FIXED.
- **Warnings standing**: link-target-missing 167 and link-label 113 (sibling-candidate targets that 404 on scp-jp pre-posting are the batch-posting class — LOCALIZE-S2-C checklist item 16: all candidates post at once; every sibling target named in the rows was verified present as a campaign candidate in the canonical repo at assembly), interwiki-touched 53 / interwiki-style-param 6 (parameter-shape notes on otherwise present frames; the charged instances were fixed by FIX4-IWB/LICENSE or carry counter-evidence there), wikidot-static 5, no-interwiki-style 3 (exactly the three named-exception files: min-theme, shushuin, sigma-10 — see (d)), credit-not-preview 1 (**pataphysics — OPEN, section (e) item A3**), inline-transform 1. **Infos standing**: double-rate 51 files (adjudicated per theme in c3: labelled paired exhibits are the pattern-3 exception; the charged bare duplicates that remain are OPEN, section (e) class B), important 226 (legacy !important density, hygiene only), legacy-css 55, storage-host 10, bare-rate 2.

### c2. T2/T3 (render) — per-theme findings, each item dispositioned

Verdict PASS-WITH-NOTES themes (5: a-problematic-theme, anon, ashes-to-ashes, borealis-constant-theme, crayon) carry notes only, all in the dispositioned classes below. Every FINDINGS theme’s items follow. Items marked OPEN are the blocking items of section (e).

- **theme:aesthetic-theme-jp** (RENDER-A (row 1)):
  - [DISPOSITIONED] page-overflow at 320/375 (337–419px), TOC highlight staircase overlap, mobile preview-notice left-clip, sample credit-modal (shared showcase) — page-overflow in the recorded cross-cutting families: static credit replica fixed width at mobile widths (KB-33) / preview chrome (KB-34); the per-theme figures match the campaign-wide shapes
  - [DISPOSITIONED] runtime-hotlink site-theme chain. — environment-layer: runtime hosts arrive via the shared site theme chain, not the candidate (KB-40; RENDER-S2-G cross-cutting 1)
- **theme:al-slop-jp** (RENDER-A (row 2)):
  - [DISPOSITIONED] body blank + hidden-rate (test-wiki `[[iftags +テーマ]]` tag mismatch, not stale cache), mobile overflow 512/881px, code-line overflow, sample credit-modal — page-overflow in the recorded cross-cutting families: static credit replica fixed width at mobile widths (KB-33) / preview chrome (KB-34); the per-theme figures match the campaign-wide shapes
  - [DISPOSITIONED] fonts.bunny.net direct link. — delivery-host class (T1 class (ii)): posting-time rewrite or original-state host; theme-level items are adjudicated in c3
- **theme:basalt-jp** (RENDER-A (row 3)):
  - [DISPOSITIONED] body blank (test-wiki tag mismatch), page-overflow on PC 1489px + all mobile 441/788px, content-overflow (code/table/floatbox), sample credit-modal — page-overflow in the recorded cross-cutting families: static credit replica fixed width at mobile widths (KB-33) / preview chrome (KB-34); the per-theme figures match the campaign-wide shapes
  - [DISPOSITIONED] jsdelivr-gh + fonts.bunny.net direct links. — delivery-host class (T1 class (ii)); the theme-level items are adjudicated in c3
- **theme:bedrock-jp** (RENDER-A (row 4)):
  - [DISPOSITIONED] mobile header/page overflow 440/445px both engines (logo + menu clipped), sample credit-modal, contrast 1.66 undetermined visually — page-overflow in the recorded cross-cutting families: static credit replica fixed width at mobile widths (KB-33) / preview chrome (KB-34); the per-theme figures match the campaign-wide shapes
  - [DISPOSITIONED] cdn.scpwiki.com Basalt-logo reference. — original-state asset reference; the FIX3-A1 section 4 record leaves the basaltlogo references as re-upload-barred leftovers (KB-58 family)
- **theme:black-highlighter-theme-jp** (RENDER-A (row 5)):
  - [DISPOSITIONED] preview-notice rating widget「価:0」missing, mobile overflow 337–419px, sidebar x=0, sample credit-modal — page-overflow in the recorded cross-cutting families: static credit replica fixed width at mobile widths (KB-33) / preview chrome (KB-34); the per-theme figures match the campaign-wide shapes
  - [DISPOSITIONED] two network-caused first runs recovered. — network-caused run retries during measurement; not a theme property
- **theme:blankstyle-jp** (RENDER-A (row 6)):
  - [OPEN] credit-modal contrast-credit 1.07 (near-white × unreadable), sample chromium-1366 shows Wikidot 503 (one width unjudgeable), ≡ toggle overlaps body at 320, mobile overflow, sample credit-modal. — section (e), theme item 4
- **theme:classic-jp** (RENDER-A (row 7)):
  - [DISPOSITIONED] 768px sidebar×preview-notice overlap hiding notice text, 768px overflow 884px, sample credit-modal — page-overflow in the recorded cross-cutting families: static credit replica fixed width at mobile widths (KB-33) / preview chrome (KB-34); the per-theme figures match the campaign-wide shapes
  - [DISPOSITIONED] 3 runs to complete (network). — network-caused run retries during measurement; not a theme property
- **theme:cosmonaut-jp** (RENDER-A (row 8)):
  - [DISPOSITIONED] page-overflow 934px@768 / 327px@320, header/account clip, sidebar x=24, contrast 3.2 (readable—machine warn), sample credit-modal. — narrow-width header clip/collision family, dispositioned as a render-side difference class (FIX3-S2EN section 6.5, observations X1-X9 family; KB-35 family)
- **theme:dear-dictator-jp** (RENDER-A (row 9)):
  - [DISPOSITIONED] webkit-768 header background image HTTP 503, large source-code content-overflow warn (transcribed only), sample credit-modal. — content-overflow machine warns are specimen shapes (code/table/demo content wider than the viewport by design), RENDER-S2-G cross-cutting 6 / KB-37 family
- **theme:extra-black-highlighter-theme-jp** (RENDER-A (row 10)):
  - [DISPOSITIONED] preview-notice rating widget「価:0」missing, mobile overflow 337–419px, sidebar x=0, sample credit-modal. — page-overflow in the recorded cross-cutting families: static credit replica fixed width at mobile widths (KB-33) / preview chrome (KB-34); the per-theme figures match the campaign-wide shapes
- **theme:flopstyle-jp** (RENDER-A (row 11)):
  - [DISPOSITIONED] 768px sidebar×preview-notice overlap (both unreadable), 768px overflow 884px, sample credit-modal — page-overflow in the recorded cross-cutting families: static credit replica fixed width at mobile widths (KB-33) / preview chrome (KB-34); the per-theme figures match the campaign-wide shapes
  - [DISPOSITIONED] large source-code content-overflow warns. — content-overflow machine warns are specimen shapes (code/table/demo content wider than the viewport by design), RENDER-S2-G cross-cutting 6 / KB-37 family
- **theme:flopstyle-dark-jp** (RENDER-B (row 12)):
  - [DISPOSITIONED] T2 did not complete (both URLs ×2: webkit target timeout / baseline crash, no summary) — coverage caveat: this theme’s T2 machine runs did not complete (target timeouts / baseline crash); the row’s own verdict is not BLOCKED-ENV and its T3 walk records no pointable display defect. Recorded as a measurement limit, see (a)
  - [DISPOSITIONED] T3 no pointable display defect — the row’s own closing assessment: no candidate defect stands from this segment
  - [DISPOSITIONED] not BLOCKED-ENV. — the row’s own closing assessment: no candidate defect stands from this segment
- **theme:foxtrot-jp** (RENDER-B (row 13)):
  - [DISPOSITIONED] T2 exit 2 ×2 both pages (chromium-320 `.open-menu a` click intercepted by `login-status`, deterministic) — coverage caveat: this run returned no machine verdict (render_check exit 2); not a theme defect — see (a)
  - [DISPOSITIONED] T3 320px ≡/sign-in overlap + SP overflow 729/754px. — page-overflow in the recorded cross-cutting families: static credit replica fixed width at mobile widths (KB-33) / preview chrome (KB-34); the per-theme figures match the campaign-wide shapes
- **theme:halloween-jp** (RENDER-B (row 14)):
  - [DISPOSITIONED] page hidden-rate (rating module absent), sample 768px overflow 884px, sample credit-modal, standalone-panel body text near-invisible — page-overflow in the recorded cross-cutting families: static credit replica fixed width at mobile widths (KB-33) / preview chrome (KB-34); the per-theme figures match the campaign-wide shapes
  - [DISPOSITIONED] contrast 1 = redaction by design. — machine contrast value not confirmed as a defect by the T3 walk (KB-39: machine contrast warns include false positives on themed surfaces)
- **theme:hansarp-jp** (RENDER-B (row 15)):
  - [DISPOSITIONED] T2 page no summary (baseline crash ×2), sample credit-modal + SP overflow 338–421px + runtime-hotlink — environment-layer: runtime hosts arrive via the shared site theme chain, not the candidate (KB-40; RENDER-S2-G cross-cutting 1)
  - [DISPOSITIONED] BHL double-include noted source-side only. — source-side hygiene note only (duplicate include, KB-65 family); the render lane recorded no display defect from it
- **theme:inkblot-jp** (RENDER-B (row 16)):
  - [DISPOSITIONED] page body blank (possible stale-cache, not counted as defect), hidden-rate, sample credit-modal, 768px overflow 884px, webkit CSS non-CSS-MIME reject — page-overflow in the recorded cross-cutting families: static credit replica fixed width at mobile widths (KB-33) / preview chrome (KB-34); the per-theme figures match the campaign-wide shapes
  - [DISPOSITIONED] re-check after purge recommended. — stale-cache caution: the lane recommends a post-purge re-check; recorded under the KB-49 caution class, not a proven defect
- **theme:isolated-terminal-jp** (RENDER-B (row 17)):
  - [DISPOSITIONED] sample lower half blank white (possible stale-cache, not a defect), T2 sample incomplete (exit 2, no summary), runtime-hotlink — coverage caveat: this run returned no machine verdict (render_check exit 2); not a theme defect — see (a)
  - [DISPOSITIONED] page credit modal opens. — positive confirmation recorded in the row (the credit modal opens on this page); no finding stands
- **theme:jakstyle-jp** (RENDER-B (row 18)):
  - [DISPOSITIONED] T2 page no summary (baseline crash + webkit timeout), sample credit-modal + SP overflow 434–498px (rate widget far wider than column) + runtime-hotlink. — environment-layer: runtime hosts arrive via the shared site theme chain, not the candidate (KB-40; RENDER-S2-G cross-cutting 1)
- **theme:just-girly-things-jp** (RENDER-B (row 19)):
  - [DISPOSITIONED] T2 page incomplete (exit 2→exit 1 baseline, no summary), sample credit-modal + 768px overflow 884px + cdn.jsdelivr.net/fonts.bunny.net direct links. — coverage caveat: this run returned no machine verdict (render_check exit 2); not a theme defect — see (a)
- **theme:min-theme-jp** (RENDER-B (row 20)):
  - [DISPOSITIONED] sidebar×body overlap (possible stale-cache, not a defect), T2 inconclusive (page baseline crashes, sample exit 2 ×2) — coverage caveat: this run returned no machine verdict (render_check exit 2); not a theme defect — see (a)
  - [DISPOSITIONED] no other pointable display defect. — positive T3 assessment recorded in the row; no finding stands from this segment
- **theme:minimalist-bhl-jp** (RENDER-B (row 21)):
  - [OPEN] §15/parallel panel body near-black-on-black unreadable (theme-specific), sample credit-modal, SP overflow 337–419px, CSS load aborted at chromium-375. — section (e), theme item 5
- **theme:monotypical-jp** (RENDER-B (row 22)):
  - [DISPOSITIONED] sample credit-modal, page credit modal overflows viewport at ≤375px, cdn.scpwiki.com/digitaloceanspaces direct links (Basalt exception discussion). — page-overflow in the recorded cross-cutting families: static credit replica fixed width at mobile widths (KB-33) / preview chrome (KB-34); the per-theme figures match the campaign-wide shapes
- **theme:much-cool-jp** (RENDER-C (row 23)):
  - [DISPOSITIONED] WebKit CC-badge stray "S" (cross-cutting), mobile notice left-clip, sidebar x=24, sample overflow 324/884px, sample credit-modal, contrast warn. — cross-cutting static credit replica width (KB-33): the preview credit replica is fixed-width and overflows narrow viewports on every theme that carries it, including the 884px@768 figure
- **theme:night-rush-theme-jp** (RENDER-C (row 24)):
  - [DISPOSITIONED] T2 incomplete (exit 2 ×6 both pages, webkit cannot reach networkidle, no summary) — coverage caveat: this run returned no machine verdict (render_check exit 2); not a theme defect — see (a)
  - [DISPOSITIONED] T3 header tagline double-struck at ≤375, notice×sidebar/clip, sample credit-modal. — narrow-width header clip/collision family, dispositioned as a render-side difference class (FIX3-S2EN section 6.5, observations X1-X9 family; KB-35 family)
- **theme:ouroborous-theme-jp** (RENDER-C (row 25)):
  - [DISPOSITIONED] 320px page overflow, notice left-clip, header logo clipped, WebKit CC "S", dark-on-dark table/title, sample credit-modal + overflow 337–419px. — narrow-width header clip/collision family, dispositioned as a render-side difference class (FIX3-S2EN section 6.5, observations X1-X9 family; KB-35 family)
- **theme:paperstack-jp** (RENDER-C (row 26)):
  - [DISPOSITIONED] sample T2 incomplete (webkit-320 screenshot >32767px ×4, no summary), notice×sidebar/clip, WebKit CC "S", giant "9999"/"THEME-IEL" demo text over intro, 875px@768 overflow, heading wrap, sample credit-modal. — page-overflow in the recorded cross-cutting families: static credit replica fixed width at mobile widths (KB-33) / preview chrome (KB-34); the per-theme figures match the campaign-wide shapes
- **theme:pataphysics-jp** (RENDER-C (row 27)):
  - [DISPOSITIONED] WebKit CC "S", 768px notice×sidebar overlap, sample credit-modal, 884px@768 overflow, notice left-clip, contrast warn, code-token overflow. — page-overflow in the recorded cross-cutting families: static credit replica fixed width at mobile widths (KB-33) / preview chrome (KB-34); the per-theme figures match the campaign-wide shapes
- **theme:penumbra-jp** (RENDER-C (row 28)):
  - [DISPOSITIONED] sample T2 incomplete (webkit screenshot pixel-cap ×3, no summary), notice left-clip, faint WebKit CC badge, sample credit-modal — preview-form property: candidate/sample pages use credit:start-preview, which has no modal mechanism (GOSIGN-TESTS.md T2 note, 2026-11-16 ruling; KB-32)
  - [DISPOSITIONED] no candidate-CSS defect. — the row’s own closing assessment: no candidate defect stands from this segment
- **theme:quand-le-soleil-se-couche** (RENDER-C (row 29)):
  - [OPEN] literal unsubstituted `{$sous-titre}` in header on all views of both pages (real defect), WebKit CC "S", 768px notice×sidebar overlap, 884px@768 overflow, notice/code clip, sample credit-modal. — section (e)
- **theme:redtape-jp** (RENDER-C (row 30)):
  - [DISPOSITIONED] WebKit CC "S", "ソース" low contrast 3.23, sample credit-modal + overflow 337–419px, panel-body contrast 1.23. — page-overflow in the recorded cross-cutting families: static credit replica fixed width at mobile widths (KB-33) / preview chrome (KB-34); the per-theme figures match the campaign-wide shapes
- **theme:scheme-jp** (RENDER-C (row 31)):
  - [DISPOSITIONED] T2 incomplete (exit 2 both pages ×6, webkit timeout), 768px second notice instance clipped over sidebar, mobile logo clipped, tagline/footer word-split, code block clipped, gold hamburger overlays body/rate, sample credit-modal, 884px@768. — coverage caveat: this run returned no machine verdict (render_check exit 2); not a theme defect — see (a)
- **theme:scp-human-resources-jp** (RENDER-C (row 32)):
  - [DISPOSITIONED] sidebar x=0, mobile notice/logo clip, WebKit CC "S", page credit modal overflows at 320, sample credit-modal + overflow 337–419px, near-black section swallows its text. — page-overflow in the recorded cross-cutting families: static credit replica fixed width at mobile widths (KB-33) / preview chrome (KB-34); the per-theme figures match the campaign-wide shapes
- **theme:scp-offices-theme-jp** (RENDER-C (row 33)):
  - [DISPOSITIONED] header logo clipped at ≤768, notice left-clip, WebKit rate「価:0」missing + stray "S", sidebar x=0, "ソース" washed out (1.84), sample credit-modal + overflow 337–419px, interwiki box absent. — narrow-width header clip/collision family, dispositioned as a render-side difference class (FIX3-S2EN section 6.5, observations X1-X9 family; KB-35 family)
- **theme:scpedia-jp** (RENDER-D (row 34)):
  - [DISPOSITIONED] page body empty (tag gate `[[iftags +テーマ]]`, possible stale-cache, not a defect), SCPedia fixed-width EN wordmark clips at ≤768 both engines, notice/sidebar/code overflow, sample credit-modal — narrow-width header clip/collision family, dispositioned as a render-side difference class (FIX3-S2EN section 6.5, observations X1-X9 family; KB-35 family)
  - [DISPOSITIONED] T2 sample exit 2 retried once. — coverage caveat: this run returned no machine verdict (render_check exit 2); not a theme defect — see (a)
- **theme:shushuin-jp** (RENDER-D (row 35)):
  - [DISPOSITIONED] paper frame 340px at 320px viewport (20px over, both engines), hidden-rate by design, sample credit-modal, preview-notice overlaps body at PC. — preview-form property: candidate/sample pages use credit:start-preview, which has no modal mechanism (GOSIGN-TESTS.md T2 note, 2026-11-16 ruling; KB-32)
- **theme:sigma-jp** (RENDER-D (row 36)):
  - [DISPOSITIONED] 884px@768 overflow (static credit replica + code specimen run past frame), notice×sidebar at 768, sample credit-modal — cross-cutting static credit replica width (KB-33): the preview credit replica is fixed-width and overflows narrow viewports on every theme that carries it, including the 884px@768 figure
  - [DISPOSITIONED] Σ9 port otherwise renders correctly. — the row’s own closing assessment: no candidate defect stands from this segment
- **theme:sigma-10-jp** (RENDER-D (row 37)):
  - [DISPOSITIONED] sample page does not exist (404, nothing to verify), Σ10 site-header subtitle doubles at ≤375 (candidate's own site-theme artifact), hidden-rate by design (bare import). — hidden-rate machine values are recorded only; the rate module’s repair status is owned by the source layer, and the current checker run shows no-rate standing only on the Sigma-10 exception file (KB-50; RENDER-B cross-cutting 5)
- **theme:simple-yonder-jp** (RENDER-D2 (row 38)):
  - [DISPOSITIONED] page-overflow 474–494px@320/375 (candidate fixed min-width), rate-preview ⓘ/× glyphs near-invisible (contrast 1.03), T2 sample no machine verdict (webkit never completes), notice×sidebar at 768. — coverage caveat: this run returned no machine verdict (render_check exit 2); not a theme defect — see (a)
- **theme:skipos-jp** (RENDER-D2 (row 39)):
  - [DISPOSITIONED] 453/454px@320/375 fixed-width OS-window overflow, double `interwiki-style` include → `priority{$priority}` console error, cdn.jsdelivr.net/fonts.bunny.net/cdn.scpwiki.com direct links, T2 sample no machine verdict. — coverage caveat: this run returned no machine verdict (render_check exit 2); not a theme defect — see (a)
- **theme:space-jp** (RENDER-D2 (row 40)):
  - [DISPOSITIONED] starfield overflow 575–859px@≤768 — candidate-inherent wide specimen (the theme’s starfield canvas), KB-37 family
  - [OPEN] real candidate defect: static credit replica pinned at viewport center (theme↔sample interaction, both engines), credit-modal-overflow at 320, sample credit-modal. — section (e), theme item 2
- **theme:turbo-vision-jp** (RENDER-D2 (row 41)):
  - [DISPOSITIONED] T2 sample no machine verdict (webkit screenshot pixel-cap, deterministic) — coverage caveat: this run returned no machine verdict (render_check exit 2); not a theme defect — see (a)
  - [DISPOSITIONED] page error only runtime-hotlink — environment-layer: runtime hosts arrive via the shared site theme chain, not the candidate (KB-40; RENDER-S2-G cross-cutting 1)
  - [DISPOSITIONED] JFDot pixel-font stylesheet ORB-blocked at chromium-768 (candidate-inherent flakiness) — ORB/load-block artifact class: single-combo or delivery-MIME symptom (KB-47 family); where the blocked asset is a candidate asset its remedy is the posting-time re-hosting class, and no source defect is identified
  - [DISPOSITIONED] offset blocks by design. — recorded by the lane as by-design (KB-37 family)
- **theme:wikifot-jp** (RENDER-D2 (row 42)):
  - [DISPOSITIONED] page-overflow 1449/851/458/362px at all four widths — page-overflow in the recorded cross-cutting families: static credit replica fixed width at mobile widths (KB-33) / preview chrome (KB-34); the per-theme figures match the campaign-wide shapes
  - [FIXED] font-awesome 4.3.0 `@import` broken as authored (icons never load — real defect) — FIX4-CREDIT (9fbcd94) section 9: the candidate carries the FontAwesome re-import correction (current file L333-338, assembly-verified); the render measurement predates the fix
  - [DISPOSITIONED] GOSIGN "raw wikitext leak" unconfirmed in current renders — an earlier suspicion the current renders do not confirm; the row records it as unconfirmed
  - [DISPOSITIONED] sidebar x=0, invisible ×. — the sidebar is off-canvas at load by design (closed state); a position reading is not an opening defect
- **theme:y2k-jp** (RENDER-D2 (row 43)):
  - [DISPOSITIONED] `logo.png` broken in chromium at ≤768 (load-failed/ORB, real broken asset), custom header tagline clips at ≤375 both edges, mobile sidebar handle overlaps body text at 320 — ORB/load-block artifact class: single-combo or delivery-MIME symptom (KB-47 family); where the blocked asset is a candidate asset its remedy is the posting-time re-hosting class, and no source defect is identified
  - [DISPOSITIONED] T2 sample no machine verdict (webkit never completes). — coverage caveat: this run returned no machine verdict (render_check exit 2); not a theme defect — see (a)
- **theme:yossistyle-jp** (RENDER-D2 (row 44)):
  - [DISPOSITIONED] webkit-375 `sidebar-not-opening` (screenshots show open — single-engine or single-combo machine line, not confirmed by the T3 walk (KB-47 family: single-combo ORB/machine flakiness); where T3 checked the drawer it is recorded opening
  - [DISPOSITIONED] infinite `@keyframes` sidebar drift likely culprit), sample 884px@768 static-credit-replica overflow, GOSIGN "raw wikitext leak" unconfirmed, doubled header subtitle at ≤375, no page credit capture — cross-cutting static credit replica width (KB-33): the preview credit replica is fixed-width and overflows narrow viewports on every theme that carries it, including the 884px@768 figure
  - [DISPOSITIONED] contrast 2.13 joke link. — machine contrast value not confirmed as a defect by the T3 walk (KB-39: machine contrast warns include false positives on themed surfaces)
- **theme:3law-pride-jp** (RENDER-S2-A (EN1)):
  - [DISPOSITIONED] candidate-specific THIRD LAW wordmark clips at ≤375 both engines — narrow-width header clip/collision family, dispositioned as a render-side difference class (FIX3-S2EN section 6.5, observations X1-X9 family; KB-35 family)
  - [DISPOSITIONED] "ソース" contrast 4.11 warn — machine contrast value not confirmed as a defect by the T3 walk (KB-39: machine contrast warns include false positives on themed surfaces)
  - [DISPOSITIONED] other lines cross-cutting/draft-form/by-design. — the row’s own closing assessment: no candidate defect stands from this segment
- **theme:3lawcracked-jp** (RENDER-S2-A (EN1)):
  - [DISPOSITIONED] inherited Third-Law header clipping at ≤375 — narrow-width header clip/collision family, dispositioned as a render-side difference class (FIX3-S2EN section 6.5, observations X1-X9 family; KB-35 family)
  - [DISPOSITIONED] font-bauhaus ORB single-combo artifact (X7 family) — ORB/load-block artifact class: single-combo or delivery-MIME symptom (KB-47 family); where the blocked asset is a candidate asset its remedy is the posting-time re-hosting class, and no source defect is identified
  - [DISPOSITIONED] no new candidate-specific defect. — the row’s own closing assessment: no candidate defect stands from this segment
- **theme:512-onwards-jp** (RENDER-S2-A (EN1)):
  - [DISPOSITIONED] candidate-inherent page-overflow 1415px@1366 + 425–428px@320/375 both engines (fixed min-width), floatbox right +142px — the ~1415-1449px figure is shared by unrelated themes (wikifot, gp-refresh, magazine) and is a draft-wiki page-form measurement shape; the render lanes recorded no defect call on it. Residual mobile-width figures fall in the KB-33 static-replica family
  - [DISPOSITIONED] runtime-hotlink cdn.scpwiki.com. — environment-layer: runtime hosts arrive via the shared site theme chain, not the candidate (KB-40; RENDER-S2-G cross-cutting 1)
- **theme:5k-jp** (RENDER-S2-A (EN1)):
  - [DISPOSITIONED] candidate-inherent page-overflow 435–437px@320/375 (page) and 1489px@1366 / 789px@768 (sample) — recorded by the lane itself as candidate-inherent (by-design wide content), KB-37 family
  - [DISPOSITIONED] hidden-rate by design (no Rate module). — hidden-rate machine values are recorded only; the rate module’s repair status is owned by the source layer, and the current checker run shows no-rate standing only on the Sigma-10 exception file (KB-50; RENDER-B cross-cutting 5)
- **theme:aces-and-eights-jp** (RENDER-S2-A (EN2)):
  - [FIXED] broken `background: url(null)` in candidate CSS (404 every combo of both pages, §3 dead declaration) + ACES wordmark clip at 320. — FIX3-S2EN section 5: the dead `background: url(null)` declaration was removed
- **theme:ad-abyssum-penumbra-jp** (RENDER-S2-A (EN2)):
  - [DISPOSITIONED] untranslated Hebrew CSS `content:` strings (§5, route to text lane), amber-on-black contrast 1.31 by design — machine contrast value not confirmed as a defect by the T3 walk (KB-39: machine contrast warns include false positives on themed surfaces)
  - [DISPOSITIONED] no layout-blocking defect. — the row’s own closing assessment: no candidate defect stands from this segment
- **theme:admo-jp** (RENDER-S2-A (EN2)):
  - [DISPOSITIONED] candidate-inherent page-overflow 454–470px@320/375 (page) and 399–412px (sample), fixed-width layout — recorded by the lane itself as candidate-inherent (by-design wide content), KB-37 family
  - [DISPOSITIONED] contrast 1.1 credit ghost by design. — machine contrast value not confirmed as a defect by the T3 walk (KB-39: machine contrast warns include false positives on themed surfaces)
- **theme:alcur-theme-jp** (RENDER-S2-A (EN2)):
  - [DISPOSITIONED] candidate-inherent page-overflow 435–437px@320/375 + Alcur Hospital wordmark clipped at 320 — narrow-width header clip/collision family, dispositioned as a render-side difference class (FIX3-S2EN section 6.5, observations X1-X9 family; KB-35 family)
  - [DISPOSITIONED] cdn.scpwiki.com direct link. — delivery-host class (T1 class (ii)): posting-time rewrite or original-state host; theme-level items are adjudicated in c3
- **theme:alexylva-university-jp** (RENDER-S2-A (EN2)):
  - [DISPOSITIONED] candidate-inherent header collision/clip at 320 (wordmark overlaps logo and 検索, tagline clipped) — narrow-width header clip/collision family, dispositioned as a render-side difference class (FIX3-S2EN section 6.5, observations X1-X9 family; KB-35 family)
  - [DISPOSITIONED] "+" contrast 1.16 washed-out rate token (theme design). — machine contrast value not confirmed as a defect by the T3 walk (KB-39: machine contrast warns include false positives on themed surfaces)
- **theme:ambrose-chapter-two-jp** (RENDER-S2-A (EN3)):
  - [DISPOSITIONED] candidate-inherent 328px@320 page overflow (8px) + 320 header clip (wordmark/account links clipped, 検索 overlaps) — narrow-width header clip/collision family, dispositioned as a render-side difference class (FIX3-S2EN section 6.5, observations X1-X9 family; KB-35 family)
  - [DISPOSITIONED] 503/http.cat transient capture, not a defect. — transient Wikidot 503 capture, not a result (KB-44)
- **theme:angel-jp** (RENDER-S2-A (EN3)):
  - [OPEN] candidate-specific unreadable near-white top-nav text on light pink (all widths, missed by machine) — section (e), theme item 5
  - [DISPOSITIONED] ≤375 site-header doubling is X1. — site-header subtitle doubling at <=375px, shared site-theme shape (KB-35)
- **theme:art-deco-jp** (RENDER-S2-A (EN3)):
  - [FIXED] malformed Google Fonts `@import` URLs (fonts never load, HTTP 400/ORB, §3) + gold-frame×default-header collisions at PC and 320. — FIX4-LICENSE (c2a8bee) KB-04: art-deco’s font imports repaired, live-probed 400 -> 200
- **theme:bedbugs-theme-jp** (RENDER-S2-A (EN4)):
  - [FIXED] port defect: duplicate `interwiki-style` priority=1 (console error every combo — FIX4-IWB (5559209): the duplicate-priority interwiki-style includes were split/fixed for the charged set (animal-instead-of-beast, path-of-jinin, sci-fi, bedbugs, black-market, black-serpent, doap-bhl, trauma, gsk)
  - [DISPOSITIONED] fix to 3) + BHL min-width overflow 337–419px@≤375 on sample. — page-overflow in the recorded cross-cutting families: static credit replica fixed width at mobile widths (KB-33) / preview chrome (KB-34); the per-theme figures match the campaign-wide shapes
- **theme:black-diamond-jp** (RENDER-S2-A (EN4)):
  - [DISPOSITIONED] candidate-inherent large page-overflow 567/577px@320/375 (page) and 579/589px (sample) + white ☰ toggle overlapping body text at 320. — recorded by the lane itself as candidate-inherent (by-design wide content), KB-37 family
- **theme:black-market-jp** (RENDER-S2-A (EN4)):
  - [FIXED] port defect: duplicate `interwiki-style` priority=1 — FIX4-IWB (5559209): the duplicate-priority interwiki-style includes were split/fixed for the charged set (animal-instead-of-beast, path-of-jinin, sci-fi, bedbugs, black-market, black-serpent, doap-bhl, trauma, gsk)
  - [DISPOSITIONED] sample machine verdict missing after one retry (page-open failure, documented), sample T3 from surviving screenshots only. — coverage caveat: the sample machine verdict is missing after a documented page-open failure; the row’s T3 rests on the surviving screenshots. Not a theme defect
- **theme:black-serpent-jp** (RENDER-S2-A (EN4)):
  - [FIXED] port defect: duplicate `interwiki-style` priority=1 + BHL min-width overflow 337–419px@≤375 on sample — FIX4-IWB (5559209): the duplicate-priority interwiki-style includes were split/fixed for the charged set (animal-instead-of-beast, path-of-jinin, sci-fi, bedbugs, black-market, black-serpent, doap-bhl, trauma, gsk)
  - [DISPOSITIONED] webkit-375 hidden-*/http.cat cluster = transient 503 capture, not a defect. — transient Wikidot 503 capture, not a result (KB-44)
- **theme:blood-jp** (RENDER-S2-A (EN4)):
  - [DISPOSITIONED] candidate-inherent page-overflow 328px@320 both engines and 799px@chromium-768 — recorded by the lane itself as candidate-inherent (by-design wide content), KB-37 family
  - [DISPOSITIONED] large code dump / red-swatch `div.cell` +59px warn. — content-overflow machine warns are specimen shapes (code/table/demo content wider than the viewport by design), RENDER-S2-G cross-cutting 6 / KB-37 family
- **theme:bloodraven-jp** (RENDER-S2-A (EN5)):
  - [DISPOSITIONED] port defect: `interwiki-style` rejected (missing `priority` parameter, every combo) + dead `fondo-code.png` asset (404 every combo) — missing/404 decorative assets are the owner-deferred hosting state, not theme defects (KB-58; LOCALIZE-S2-C checklist item 1, owner decision 2026-11-16)
  - [DISPOSITIONED] webkit-375 503 transient. — transient Wikidot 503 capture (KB-44)
- **theme:caretaker-sigma-jp** (RENDER-S2-A (EN5)):
  - [FIXED] port defect: `interwiki-style` rejected (missing `priority` parameter) — FIX4-LICENSE (c2a8bee): caretaker-sigma received its missing priority=1
  - [DISPOSITIONED] no other candidate-specific defect. — the row’s own closing assessment: no candidate defect stands from this segment
- **theme:caretaker-theme-jp** (RENDER-S2-A (EN5)):
  - [DISPOSITIONED] BHL min-width overflow 337–419px@≤375 on sample — page-overflow in the recorded cross-cutting families: static credit replica fixed width at mobile widths (KB-33) / preview chrome (KB-34); the per-theme figures match the campaign-wide shapes
  - [DISPOSITIONED] no interwiki port defect — the row’s own closing assessment: no candidate defect stands from this segment
  - [DISPOSITIONED] other lines cross-cutting/draft-form/by-design. — the row’s own closing assessment: no candidate defect stands from this segment
- **theme:ch-scp-theme-jp** (RENDER-S2-A (EN5)):
  - [DISPOSITIONED] severe candidate-inherent page-overflow 2534px@320 / 2968px@375 (both engines) and 779px@webkit-768. — recorded by the lane itself as candidate-inherent (by-design wide content), KB-37 family
- **theme:chaos-jp** (RENDER-S2-A (EN6)):
  - [DISPOSITIONED] candidate-inherent ~500px min-width on page + page-overflow at every viewport on sample. — recorded by the lane itself as candidate-inherent (by-design wide content), KB-37 family
- **theme:cleaning-services-jp** (RENDER-S2-A (EN6)):
  - [DISPOSITIONED] BHL min-width overflow 337–419px@≤375 on sample — page-overflow in the recorded cross-cutting families: static credit replica fixed width at mobile widths (KB-33) / preview chrome (KB-34); the per-theme figures match the campaign-wide shapes
  - [DISPOSITIONED] 503/http.cat lines are transient capture, not a defect. — transient Wikidot 503 capture, not a result (KB-44)
- **theme:clock-tower-jp** (RENDER-S2-A (EN6)):
  - [DISPOSITIONED] BHL min-width overflow 337–419px@≤375 on sample — page-overflow in the recorded cross-cutting families: static credit replica fixed width at mobile widths (KB-33) / preview chrome (KB-34); the per-theme figures match the campaign-wide shapes
  - [DISPOSITIONED] mangled `url-https//…` stylesheet is a runtime artifact (recorded verbatim). — migration infrastructure form, per the row’s own note (draft-host addressing, posting-time rewrite class)
- **theme:cosmos-jp** (RENDER-S2-A (EN6)):
  - [DISPOSITIONED] candidate-inherent page-overflow at 320/375 + `credit-modal-overflow` at 320 (both engines). — preview-form fixed-width modal shape on preview-module pages (KB-32/KB-33 family; KB-31 charges only real-module pages and its own sweep amendment records the confirmed mechanism is not a candidate fixed width)
- **theme:dark-jp** (RENDER-S2-B (EN7)):
  - [DISPOSITIONED] T2 runtime-hotlink + dark credit-modal heading contrast-credit 1.46 faint-gray-on-gray (chromium verified) — preview-form property: candidate/sample pages use credit:start-preview, which has no modal mechanism (GOSIGN-TESTS.md T2 note, 2026-11-16 ruling; KB-32)
  - [DISPOSITIONED] notice clip ≤375 and sidebar×notice at 768 are shared preview chrome — preview-notice clipping/overprint at narrow widths (KB-34)
  - [DISPOSITIONED] 884px@768 sample overflow. — page-overflow in the recorded cross-cutting families: static credit replica fixed width at mobile widths (KB-33) / preview chrome (KB-34); the per-theme figures match the campaign-wide shapes
- **theme:dark-dealings-jp** (RENDER-S2-B (EN7)):
  - [DISPOSITIONED] T2 sample exit 2 (target networkidle ×3 attempts, no machine verdict, chromium OK) — coverage caveat: this run returned no machine verdict (render_check exit 2); not a theme defect — see (a)
  - [DISPOSITIONED] T3 sample overflow 351/392px@320/375 with footer clipping and dim ACS-bar cell at 1366 — page-overflow in the recorded cross-cutting families: static credit replica fixed width at mobile widths (KB-33) / preview chrome (KB-34); the per-theme figures match the campaign-wide shapes
  - [DISPOSITIONED] page runtime-hotlink. — environment-layer: runtime hosts arrive via the shared site theme chain, not the candidate (KB-40; RENDER-S2-G cross-cutting 1)
- **theme:darkqueer-jp** (RENDER-S2-B (EN7)):
  - [DISPOSITIONED] footer nav "Powered by Wikidot.com"/links illegible on near-black at every width/engine (theme's dark palette) + 375px license line clipped — narrow-width chrome clipping family (KB-34)
  - [DISPOSITIONED] hidden-rate contradicted by eye — hidden-rate machine values are recorded only; the rate module’s repair status is owned by the source layer, and the current checker run shows no-rate standing only on the Sigma-10 exception file (KB-50; RENDER-B cross-cutting 5)
  - [DISPOSITIONED] 382–428px sample overflow — page-overflow in the recorded cross-cutting families: static credit replica fixed width at mobile widths (KB-33) / preview chrome (KB-34); the per-theme figures match the campaign-wide shapes
  - [DISPOSITIONED] `url-https//` 404 = migration infra. — migration infrastructure form, per the row’s own note (draft-host addressing, posting-time rewrite class)
- **theme:decom-dept-jp** (RENDER-S2-B (EN7)):
  - [DISPOSITIONED] candidate-header defect: theme's own gray-dept header logo/site-name collision and 検索 overprint of "財団" at ≤375 both engines (768px clean) — narrow-width header clip/collision family, dispositioned as a render-side difference class (FIX3-S2EN section 6.5, observations X1-X9 family; KB-35 family)
  - [DISPOSITIONED] 884px@768 sample overflow, notice clip, WebKit CC "S". — page-overflow in the recorded cross-cutting families: static credit replica fixed width at mobile widths (KB-33) / preview chrome (KB-34); the per-theme figures match the campaign-wide shapes
- **theme:derby-jp** (RENDER-S2-B (EN7)):
  - [DISPOSITIONED] broken image: `sigma-header-logo.svg` renders as broken on all 8 shots (URL 200 but `content-type: text/plain` — MIME, not 404/stale) — posting-procedure: the logo asset is served text/plain from the draft wiki’s code path; asset re-hosting at posting serves it with the correct MIME (same delivery-form class as the twin-files /1 and the-foundation-sigma /1 items, LOCALIZE-S2-C items 6/11). Not a candidate source defect
  - [DISPOSITIONED] `.open-menu` overlaps content at ≤375 both pages, WebKit CC "S", swatch-table overflow. — WebKit CC-badge stray glyph (KB-36)
- **theme:dia-de-muertos-jp** (RENDER-S2-B (EN8)):
  - [DISPOSITIONED] webkit-320 page-overflow 322px, sample overflow 337–419px@≤375, anom-bar specimen unreadable dark-magenta-on-black at 1366 both engines — page-overflow in the recorded cross-cutting families: static credit replica fixed width at mobile widths (KB-33) / preview chrome (KB-34); the per-theme figures match the campaign-wide shapes
  - [DISPOSITIONED] decoration assets 404 = EN8 owner-deferred, not defects. — missing/404 decorative assets are the owner-deferred hosting state, not theme defects (KB-58; LOCALIZE-S2-C checklist item 1, owner decision 2026-11-16)
- **theme:diamond-highlighter-jp** (RENDER-S2-B (EN8)):
  - [DISPOSITIONED] chromium-320 header wordmark clipped + webkit-320 footer license clipped — narrow-width header clip/collision family, dispositioned as a render-side difference class (FIX3-S2EN section 6.5, observations X1-X9 family; KB-35 family)
  - [DISPOSITIONED] engine-divergent wordmark vs canonical = stale test-wiki page state (noted, not a defect) — stale static-cache phantom suspicion, recorded as a caution, not a proven signature (KB-49)
  - [DISPOSITIONED] sample overflow 337–419px — page-overflow in the recorded cross-cutting families: static credit replica fixed width at mobile widths (KB-33) / preview chrome (KB-34); the per-theme figures match the campaign-wide shapes
  - [DISPOSITIONED] assets 404 deferred. — deferred asset hosting state (KB-58)
- **theme:dynamikron-jp** (RENDER-S2-B (EN8)):
  - [DISPOSITIONED] credit modal wider than 320px viewport both engines + WebKit CC "S" + notice clip ≤375 — WebKit CC-badge stray glyph (KB-36)
  - [DISPOSITIONED] assets 404/ORB = EN8 deferred — ORB/load-block artifact class: single-combo or delivery-MIME symptom (KB-47 family); where the blocked asset is a candidate asset its remedy is the posting-time re-hosting class, and no source defect is identified
  - [DISPOSITIONED] sample T3 none seen. — the row’s own closing assessment: no candidate defect stands from this segment
- **theme:eigenmachine-jp** (RENDER-S2-B (EN8)):
  - [DISPOSITIONED] page-overflow 581px@320/375 both engines — page-overflow in the recorded cross-cutting families: static credit replica fixed width at mobile widths (KB-33) / preview chrome (KB-34); the per-theme figures match the campaign-wide shapes
  - [DISPOSITIONED] T2 sample exit 2 (networkidle ×3, no machine verdict, chromium partial) — coverage caveat: this run returned no machine verdict (render_check exit 2); not a theme defect — see (a)
  - [OPEN] §29 warning-block text unreadable chromium-375 — section (e)
  - [DISPOSITIONED] assets deferred. — deferred asset hosting state (KB-58)
- **theme:eigenvector-jp** (RENDER-S2-B (EN8)):
  - [DISPOSITIONED] page-overflow 483/502px@320/375 + sample overflow everywhere incl. desktop 1427–1441px@1366 — page-overflow in the recorded cross-cutting families: static credit replica fixed width at mobile widths (KB-33) / preview chrome (KB-34); the per-theme figures match the campaign-wide shapes
  - [DISPOSITIONED] WebKit CC "S" — WebKit CC-badge stray glyph (KB-36)
  - [DISPOSITIONED] cdn.jsdelivr.net/fonts.bunny.net direct links — delivery-host class (T1 class (ii)); the theme-level items are adjudicated in c3
  - [DISPOSITIONED] no candidate-CSS defect. — the row’s own closing assessment: no candidate defect stands from this segment
- **theme:enlightened-eyes-jp** (RENDER-S2-B (EN9)):
  - [DISPOSITIONED] page-overflow everywhere incl. 1489px@1366, 789px@768, ~440px@≤375 — page-overflow in the recorded cross-cutting families: static credit replica fixed width at mobile widths (KB-33) / preview chrome (KB-34); the per-theme figures match the campaign-wide shapes
  - [DISPOSITIONED] sample credit-modal — preview-form property: candidate/sample pages use credit:start-preview, which has no modal mechanism (GOSIGN-TESTS.md T2 note, 2026-11-16 ruling; KB-32)
  - [DISPOSITIONED] 1366 sidebar-collapsed with own ☰ — the theme’s own hamburger pattern at desktop width, T3-recorded as working; not a defect
  - [DISPOSITIONED] WebKit CC "S". — WebKit CC-badge stray glyph (KB-36)
- **theme:eventyr-jp** (RENDER-S2-B (EN9)):
  - [DISPOSITIONED] sample overflow 337–419px@≤375 + credit-modal (shared) — page-overflow in the recorded cross-cutting families: static credit replica fixed width at mobile widths (KB-33) / preview chrome (KB-34); the per-theme figures match the campaign-wide shapes
  - [DISPOSITIONED] page runtime-hotlink — environment-layer: runtime hosts arrive via the shared site theme chain, not the candidate (KB-40; RENDER-S2-G cross-cutting 1)
  - [DISPOSITIONED] WebKit CC "S" — WebKit CC-badge stray glyph (KB-36)
  - [DISPOSITIONED] decoration assets 404 = deferred, not defects. — missing/404 decorative assets are the owner-deferred hosting state, not theme defects (KB-58; LOCALIZE-S2-C checklist item 1, owner decision 2026-11-16)
- **theme:fandom-jp** (RENDER-S2-B (EN9)):
  - [DISPOSITIONED] candidate's purple header wordmark overprints account links at ≤375 both engines (notice ends clipped at right) — narrow-width header clip/collision family, dispositioned as a render-side difference class (FIX3-S2EN section 6.5, observations X1-X9 family; KB-35 family)
  - [DISPOSITIONED] chameleon.gif 404 = owner-deferred EN9. — owner-deferred hosting state (KB-58)
- **theme:febris-pharmaceuticals-theme-jp** (RENDER-S2-B (EN9)):
  - [DISPOSITIONED] theme header wordmark clipped at both edges at ≤375 (candidate-header width defect) — narrow-width header clip/collision family, dispositioned as a render-side difference class (FIX3-S2EN section 6.5, observations X1-X9 family; KB-35 family)
  - [OPEN] §15 panel body unreadable at 375 — section (e)
  - [DISPOSITIONED] sample overflow 337–419px — page-overflow in the recorded cross-cutting families: static credit replica fixed width at mobile widths (KB-33) / preview chrome (KB-34); the per-theme figures match the campaign-wide shapes
  - [DISPOSITIONED] assets 404 deferred. — deferred asset hosting state (KB-58)
- **theme:fish-jp** (RENDER-S2-B (EN9)):
  - [OPEN] §15 series-panel body illegible near-black-on-navy at all 8 shots — section (e), theme item 3
  - [DISPOSITIONED] `.open-menu` overlap at ≤375, 320px image clip — the mobile menu button is the shared site-theme element; its overlap at <=375px is the mobile chrome family (KB-34/KB-35 family), not theme-authored content
  - [DISPOSITIONED] WebKit CC "S" — WebKit CC-badge stray glyph (KB-36)
  - [DISPOSITIONED] assets 404 deferred. — deferred asset hosting state (KB-58)
- **theme:fossil-jp** (RENDER-S2-B (EN10)):
  - [DISPOSITIONED] page-overflow 533–536px@≤375 and 847–856px@768 both engines — page-overflow in the recorded cross-cutting families: static credit replica fixed width at mobile widths (KB-33) / preview chrome (KB-34); the per-theme figures match the campaign-wide shapes
  - [DISPOSITIONED] sample 545–548px@≤375 + 898px@768 — page-overflow in the recorded cross-cutting families: static credit replica fixed width at mobile widths (KB-33) / preview chrome (KB-34) / wide specimen content (KB-37); desktop-width figures shared across unrelated themes are the draft-wiki page-form shape
  - [DISPOSITIONED] credit-modal heading pale tan on gray (contrast 1.03). — preview-form property: candidate/sample pages use credit:start-preview, which has no modal mechanism (GOSIGN-TESTS.md T2 note, 2026-11-16 ruling; KB-32)
- **theme:frownstyle-jp** (RENDER-S2-B (EN10)):
  - [OPEN] PC-width header broken at 1366 both engines (JP nav absent, wordmark clipped to "IN…", auth buttons overprint theme header) + blank `.open-menu` button + navy-on-navy opened-sidebar overprint — section (e)
  - [DISPOSITIONED] 383–419px sample overflow. — page-overflow in the recorded cross-cutting families: static credit replica fixed width at mobile widths (KB-33) / preview chrome (KB-34); the per-theme figures match the campaign-wide shapes
- **theme:fuladh-theme-jp** (RENDER-S2-B (EN10)):
  - [DISPOSITIONED] T2 page pending (batch exit 1 pre-analysis baseline timeout) — coverage caveat: this run stayed pending on a baseline timeout; a measurement limit, not a theme defect — see (a)
  - [DISPOSITIONED] sample overflow 337–419px@≤375 + credit-modal — page-overflow in the recorded cross-cutting families: static credit replica fixed width at mobile widths (KB-33) / preview chrome (KB-34); the per-theme figures match the campaign-wide shapes
  - [DISPOSITIONED] §24 sticky note and §30 static credit panel illegible pale-on-pale both engines. — static credit replica rendering note; the replica’s cross-cutting shapes are KB-33/KB-34
- **theme:galactic-theme-jp** (RENDER-S2-B (EN10)):
  - [DISPOSITIONED] WebKit CC "S" (cross-cutting), notice clip ≤375, 1366 sidebar-collapsed with theme's own ☰ — WebKit CC-badge stray glyph (KB-36)
  - [DISPOSITIONED] runtime-hotlink — environment-layer: runtime hosts arrive via the shared site theme chain, not the candidate (KB-40; RENDER-S2-G cross-cutting 1)
  - [DISPOSITIONED] assets 404 deferred. — deferred asset hosting state (KB-58)
- **theme:golden-feast-jp** (RENDER-S2-B (EN10)):
  - [DISPOSITIONED] page-overflow 328px@320 + sample 884px@768 — page-overflow in the recorded cross-cutting families: static credit replica fixed width at mobile widths (KB-33) / preview chrome (KB-34); the per-theme figures match the campaign-wide shapes
  - [DISPOSITIONED] chromium rate-pill label wrap-and-clip at ≤768 — rate-module label shape at narrow widths: the preview rate module’s label rendering, cross-cutting across themes (preview-form family, KB-32/KB-34)
  - [DISPOSITIONED] WebKit CC "S" — WebKit CC-badge stray glyph (KB-36)
  - [DISPOSITIONED] notice clip. — preview-notice clipping/overprint at narrow widths (KB-34)
- **theme:greystyle-jp** (RENDER-S2-B (EN11)):
  - [DISPOSITIONED] page-overflow at 1366/320/375 both engines — page-overflow in the recorded cross-cutting families: static credit replica fixed width at mobile widths (KB-33) / preview chrome (KB-34); the per-theme figures match the campaign-wide shapes
  - [DISPOSITIONED] sample 1569px@1366 + 789px@768 — page-overflow in the recorded cross-cutting families: static credit replica fixed width at mobile widths (KB-33) / preview chrome (KB-34) / wide specimen content (KB-37); desktop-width figures shared across unrelated themes are the draft-wiki page-form shape
  - [DISPOSITIONED] WebKit CC "S" — WebKit CC-badge stray glyph (KB-36)
  - [DISPOSITIONED] license-box include error = test-wiki resolution, not defect. — the row itself records this is not a theme defect
- **theme:helix-jp** (RENDER-S2-B (EN11)):
  - [DISPOSITIONED] header gear logo clipped at left ≤768 both engines — narrow-width header clip/collision family, dispositioned as a render-side difference class (FIX3-S2EN section 6.5, observations X1-X9 family; KB-35 family)
  - [DISPOSITIONED] credit-modal heading white-on-yellow ≈1.4 — preview-form property: candidate/sample pages use credit:start-preview, which has no modal mechanism (GOSIGN-TESTS.md T2 note, 2026-11-16 ruling; KB-32)
  - [DISPOSITIONED] WebKit CC "S" — WebKit CC-badge stray glyph (KB-36)
  - [DISPOSITIONED] i57logo 503 = EN11 deferred host. — owner-deferred hosting state (KB-58)
- **theme:highroller-jp** (RENDER-S2-B (EN11)):
  - [DISPOSITIONED] 768px sidebar×notice overprint + ≤375 notice left-clip + WebKit CC "S" (all cross-cutting) — WebKit CC-badge stray glyph (KB-36)
  - [DISPOSITIONED] sample 320px right-floated image clipped at left edge. — content-overflow machine warns are specimen shapes (code/table/demo content wider than the viewport by design), RENDER-S2-G cross-cutting 6 / KB-37 family
- **theme:hytoth-two-jp** (RENDER-S2-B (EN11)):
  - [DISPOSITIONED] hidden-rate contradicted by eye — hidden-rate machine values are recorded only; the rate module’s repair status is owned by the source layer, and the current checker run shows no-rate standing only on the Sigma-10 exception file (KB-50; RENDER-B cross-cutting 5)
  - [DISPOSITIONED] massive page-overflow 533/548px@320/375 and desktop 1433–1438px@1366 + 972px@768 — page-overflow in the recorded cross-cutting families: static credit replica fixed width at mobile widths (KB-33) / preview chrome (KB-34); the per-theme figures match the campaign-wide shapes
  - [DISPOSITIONED] header tagline/財団 clipped ≤375 — narrow-width header clip/collision family, dispositioned as a render-side difference class (FIX3-S2EN section 6.5, observations X1-X9 family; KB-35 family)
  - [DISPOSITIONED] WebKit-only IMMRAMA header clip ≤375 — narrow-width header clip/collision family, dispositioned as a render-side difference class (FIX3-S2EN section 6.5, observations X1-X9 family; KB-35 family)
  - [DISPOSITIONED] cdn.scpwiki.com carried over (Basalt exception). — Basalt-base delivery adjudicated in FIX-P4 (repoint to the JP basalt-jp base) / the row’s own exception note
- **theme:i57-jp** (RENDER-S2-B (EN11)):
  - [DISPOSITIONED] runtime-hotlink incl. scp-wiki.wikidot.com, 1366 content-overflow fncon/a up to +104px, 1366 sidebar-collapsed with own ☰ — environment-layer: runtime hosts arrive via the shared site theme chain, not the candidate (KB-40; RENDER-S2-G cross-cutting 1)
  - [DISPOSITIONED] notice/panel items cross-cutting. — recorded by the lane as cross-cutting (the campaign-wide shapes of register c2’s class entries)
- **theme:i57-theme-jp** (RENDER-S2-B (EN12)):
  - [DISPOSITIONED] credit-modal title white-on-light-gray (contrast 1.61) — preview-form property: candidate/sample pages use credit:start-preview, which has no modal mechanism (GOSIGN-TESTS.md T2 note, 2026-11-16 ruling; KB-32)
  - [DISPOSITIONED] chromium/webkit disagree on 翻訳責任者 = possible stale-cache/page-state (noted) — stale static-cache phantom suspicion, recorded as a caution, not a proven signature (KB-49)
  - [DISPOSITIONED] theme header wordmark overprints logo + search at ≤375, `.open-menu` overlaps body. — narrow-width header clip/collision family, dispositioned as a render-side difference class (FIX3-S2EN section 6.5, observations X1-X9 family; KB-35 family)
- **theme:immrama-jp** (RENDER-S2-B (EN12)):
  - [DISPOSITIONED] notice clip ≤375 + 768px sidebar×notice + WebKit CC "S" (all cross-cutting) — WebKit CC-badge stray glyph (KB-36)
  - [DISPOSITIONED] sample h1 clipped at 320, 評価 label crush (6 shots), `.open-menu` overprint — rate-module label shape at narrow widths: the preview rate module’s label rendering, cross-cutting across themes (preview-form family, KB-32/KB-34)
  - [DISPOSITIONED] page-overflow 367–552px. — page-overflow in the recorded cross-cutting families: static credit replica fixed width at mobile widths (KB-33) / preview chrome (KB-34); the per-theme figures match the campaign-wide shapes
- **theme:internal-affairs-jp** (RENDER-S2-B (EN12)):
  - [DISPOSITIONED] page-overflow 328px@320 + sample 884px@768 — page-overflow in the recorded cross-cutting families: static credit replica fixed width at mobile widths (KB-33) / preview chrome (KB-34); the per-theme figures match the campaign-wide shapes
  - [DISPOSITIONED] 768px sidebar overprint of notice — narrow-width chrome overprint family (KB-34)
  - [DISPOSITIONED] chromium rate-pill wrap-and-clip at ≤768 — rate-module label shape at narrow widths: the preview rate module’s label rendering, cross-cutting across themes (preview-form family, KB-32/KB-34)
  - [DISPOSITIONED] WebKit CC "S". — WebKit CC-badge stray glyph (KB-36)
- **theme:janitor-closet-jp** (RENDER-S2-B (EN12)):
  - [DISPOSITIONED] page-overflow everywhere incl. 1683px@1366, 806px@768, 350–419px@≤375 both engines — page-overflow in the recorded cross-cutting families: static credit replica fixed width at mobile widths (KB-33) / preview chrome (KB-34); the per-theme figures match the campaign-wide shapes
  - [DISPOSITIONED] runtime-hotlink incl. scp-wiki.wikidot.com — environment-layer: runtime hosts arrive via the shared site theme chain, not the candidate (KB-40; RENDER-S2-G cross-cutting 1)
  - [DISPOSITIONED] WebKit CC "S". — WebKit CC-badge stray glyph (KB-36)
- **theme:kiryu-labs-theme-jp** (RENDER-S2-B (EN12)):
  - [DISPOSITIONED] notice clip ≤375 + 768px sidebar×notice + WebKit CC "S" (all cross-cutting) — WebKit CC-badge stray glyph (KB-36)
  - [DISPOSITIONED] sample 884px@768 static-credit-replica overflow — cross-cutting static credit replica width (KB-33): the preview credit replica is fixed-width and overflows narrow viewports on every theme that carries it, including the 884px@768 figure
  - [DISPOSITIONED] webkit `url-https` 404 = shared artifact — migration infrastructure form, per the row’s own note (draft-host addressing, posting-time rewrite class)
  - [DISPOSITIONED] no candidate-CSS defect. — the row’s own closing assessment: no candidate defect stands from this segment
- **theme:lampeter-warm-jp** (RENDER-S2-C (EN13)):
  - [DISPOSITIONED] page T2 no machine verdict (exit 2, networkidle, no summary) — coverage caveat: this run returned no machine verdict (render_check exit 2); not a theme defect — see (a)
  - [DISPOSITIONED] sample credit-modal (preview-form), sample overflow 576–583px@320/375, runtime-hotlink site-theme chain — environment-layer: runtime hosts arrive via the shared site theme chain, not the candidate (KB-40; RENDER-S2-G cross-cutting 1)
  - [DISPOSITIONED] T3 sample notice left-clip ≤375, broken lampeterlogo.png (deferred asset). — preview-notice clipping/overprint at narrow widths (KB-34)
- **theme:laruetheme-jp** (RENDER-S2-C (EN13)):
  - [DISPOSITIONED] page runtime-hotlink site-theme chain only — environment-layer: runtime hosts arrive via the shared site theme chain, not the candidate (KB-40; RENDER-S2-G cross-cutting 1)
  - [DISPOSITIONED] sample T2 no machine verdict (exit 2) — coverage caveat: this run returned no machine verdict (render_check exit 2); not a theme defect — see (a)
  - [DISPOSITIONED] T3 page credit modal opens, preview-notice left-clip (shared chrome). — positive confirmation recorded in the row (the credit modal opens on this page); no finding stands
- **theme:last-frontier-jp** (RENDER-S2-C (EN13)):
  - [DISPOSITIONED] page runtime-hotlink site-theme chain only — environment-layer: runtime hosts arrive via the shared site theme chain, not the candidate (KB-40; RENDER-S2-G cross-cutting 1)
  - [DISPOSITIONED] sample credit-modal (preview-form) + 884px@768 overflow — page-overflow in the recorded cross-cutting families: static credit replica fixed width at mobile widths (KB-33) / preview chrome (KB-34); the per-theme figures match the campaign-wide shapes
  - [DISPOSITIONED] T3 sample header wordmark "The Beholder Program財団" overprints account/search links and clips at 375/320 (both engines) — narrow-width header clip/collision family, dispositioned as a render-side difference class (FIX3-S2EN section 6.5, observations X1-X9 family; KB-35 family)
  - [DISPOSITIONED] broken binary-star-loop-link.bmp (deferred). — owner-deferred hosting state (KB-58)
- **theme:laughter-and-knives-theme-jp** (RENDER-S2-C (EN13)):
  - [DISPOSITIONED] page runtime-hotlink site-theme chain + sidebar-not-opening [webkit 768/375] — environment-layer: runtime hosts arrive via the shared site theme chain, not the candidate (KB-40; RENDER-S2-G cross-cutting 1)
  - [DISPOSITIONED] sample T2 no machine verdict (exit 2) — coverage caveat: this run returned no machine verdict (render_check exit 2); not a theme defect — see (a)
  - [DISPOSITIONED] T3 "MAN ZOO LEAGUE" subtitle faint/overlapping at 375 (minor). — recorded as minor by the T3 walk itself
- **theme:linear-black-jp** (RENDER-S2-C (EN13)):
  - [OPEN] body text and headings illegible white-on-white at all 8 combos on both pages (contrast min 1 / 1.61, candidate defect) — section (e), theme item 5
  - [DISPOSITIONED] page-overflow 612–617px@320/375 (page) and 624–629px (sample) — page-overflow in the recorded cross-cutting families: static credit replica fixed width at mobile widths (KB-33) / preview chrome (KB-34); the per-theme figures match the campaign-wide shapes
  - [DISPOSITIONED] runtime-hotlink site-theme chain + scpwiki.github.io — candidate-own foreign/sandbox delivery hosts: posting-time rewrite or original-state delivery class (T1 class (ii); KB-41/KB-54 family). The pages render styled today; no error-box defect arises from these hosts
  - [DISPOSITIONED] sample credit-modal (preview-form) — preview-form property: candidate/sample pages use credit:start-preview, which has no modal mechanism (GOSIGN-TESTS.md T2 note, 2026-11-16 ruling; KB-32)
  - [DISPOSITIONED] broken images deferred. — deferred asset hosting state (KB-58)
- **theme:lumina-jp** (RENDER-S2-C (EN14)):
  - [DISPOSITIONED] page-overflow 512–519px@320/375 (page) and 512–519px@≤375 + 859px@768 (sample) — page-overflow in the recorded cross-cutting families: static credit replica fixed width at mobile widths (KB-33) / preview chrome (KB-34); the per-theme figures match the campaign-wide shapes
  - [DISPOSITIONED] runtime-hotlink site-theme chain + cdn.jsdelivr.net (page), one sample combo http.cat among hosts — candidate-own foreign/sandbox delivery hosts: posting-time rewrite or original-state delivery class (T1 class (ii); KB-41/KB-54 family). The pages render styled today; no error-box defect arises from these hosts
  - [DISPOSITIONED] sample credit-modal (preview-form) — preview-form property: candidate/sample pages use credit:start-preview, which has no modal mechanism (GOSIGN-TESTS.md T2 note, 2026-11-16 ruling; KB-32)
  - [DISPOSITIONED] T3 clean on both pages. — positive T3 assessment recorded in the row; no finding stands from this segment
- **theme:magpie-swoops-jp** (RENDER-S2-C (EN14)):
  - [DISPOSITIONED] page runtime-hotlink site-theme chain + scp-wiki.wikidot.com — environment-layer: runtime hosts arrive via the shared site theme chain, not the candidate (KB-40; RENDER-S2-G cross-cutting 1)
  - [DISPOSITIONED] sample T2 no machine verdict (exit 2) — coverage caveat: this run returned no machine verdict (render_check exit 2); not a theme defect — see (a)
  - [DISPOSITIONED] T3 page wordmark "MAGPIE SWOOPS財団" overprints account links and clips at 375/320 (both engines). — narrow-width header clip/collision family, dispositioned as a render-side difference class (FIX3-S2EN section 6.5, observations X1-X9 family; KB-35 family)
- **theme:maxwell-s-silver-hammer-jp** (RENDER-S2-C (EN14)):
  - [DISPOSITIONED] page runtime-hotlink site-theme chain + scp-wiki.wikidot.com — environment-layer: runtime hosts arrive via the shared site theme chain, not the candidate (KB-40; RENDER-S2-G cross-cutting 1)
  - [DISPOSITIONED] sample credit-modal (preview-form) + 884px@768 overflow (one combo http.cat among hosts) — page-overflow in the recorded cross-cutting families: static credit replica fixed width at mobile widths (KB-33) / preview chrome (KB-34); the per-theme figures match the campaign-wide shapes
  - [DISPOSITIONED] T3 header logo overprints subtitle/account links at 375/320 on both pages, h1 wraps to two lines at 320. — narrow-width header shape family (KB-35 family); no defect call recorded by the lane
- **theme:mcf-jp** (RENDER-S2-C (EN14)):
  - [DISPOSITIONED] page runtime-hotlink site-theme chain only — environment-layer: runtime hosts arrive via the shared site theme chain, not the candidate (KB-40; RENDER-S2-G cross-cutting 1)
  - [DISPOSITIONED] sample credit-modal (preview-form) + 884px@768 overflow (one combo http.cat among hosts) — page-overflow in the recorded cross-cutting families: static credit replica fixed width at mobile widths (KB-33) / preview chrome (KB-34); the per-theme figures match the campaign-wide shapes
  - [DISPOSITIONED] T3 clean on both pages. — positive T3 assessment recorded in the row; no finding stands from this segment
- **theme:oceanbound-jp** (RENDER-S2-C (EN14)):
  - [DISPOSITIONED] page-overflow 340px@320 on page and sample — page-overflow in the recorded cross-cutting families: static credit replica fixed width at mobile widths (KB-33) / preview chrome (KB-34); the per-theme figures match the campaign-wide shapes
  - [DISPOSITIONED] runtime-hotlink site-theme chain + scp-wiki.wikidot.com — environment-layer: runtime hosts arrive via the shared site theme chain, not the candidate (KB-40; RENDER-S2-G cross-cutting 1)
  - [DISPOSITIONED] sample credit-modal (preview-form) — preview-form property: candidate/sample pages use credit:start-preview, which has no modal mechanism (GOSIGN-TESTS.md T2 note, 2026-11-16 ruling; KB-32)
  - [DISPOSITIONED] T3 clean on both pages. — positive T3 assessment recorded in the row; no finding stands from this segment
- **theme:old-money-theme-jp** (RERUN16 (EN15)):
  - [DISPOSITIONED] page runtime-hotlink site-theme chain only — environment-layer: runtime hosts arrive via the shared site theme chain, not the candidate (KB-40; RENDER-S2-G cross-cutting 1)
  - [DISPOSITIONED] sample credit-modal (preview-form), page-overflow 337px@320 + 389px@375 chromium and 416px@320 + 419px@375 webkit (cross-cutting static-credit), runtime-hotlink site-theme chain + sample font host — environment-layer: runtime hosts arrive via the shared site theme chain, not the candidate (KB-40; RENDER-S2-G cross-cutting 1)
  - [OPEN] T3 REAL FINDING: sample "15. コンテンツパネル" notice panel and left/right column panel body text render near-white #F7F8F9 on light-gray/white #F4F4F4, effectively unreadable (chromium 1366 + 375, webkit 1366 + 375) — section (e)
  - [DISPOSITIONED] broken OldMoney_Logo.png = deferred asset. — missing/404 decorative assets are the owner-deferred hosting state, not theme defects (KB-58; LOCALIZE-S2-C checklist item 1, owner decision 2026-11-16)
- **theme:onko-sinulla-nalka-theme-jp** (RENDER-S2-C (EN15)):
  - [DISPOSITIONED] page runtime-hotlink site-theme chain only — environment-layer: runtime hosts arrive via the shared site theme chain, not the candidate (KB-40; RENDER-S2-G cross-cutting 1)
  - [DISPOSITIONED] sample credit-modal (preview-form) + page-overflow 337–419px@320/375. — page-overflow in the recorded cross-cutting families: static credit replica fixed width at mobile widths (KB-33) / preview chrome (KB-34); the per-theme figures match the campaign-wide shapes
- **theme:ordopharm-jp** (RERUN16 (EN15)):
  - [DISPOSITIONED] page page-overflow 506px@320/375 chromium + 518px@320/375 webkit, runtime-hotlink site-theme chain + candidate-own cdn.jsdelivr.net (judgment-required) — candidate-own foreign/sandbox delivery hosts: posting-time rewrite or original-state delivery class (T1 class (ii); KB-41/KB-54 family). The pages render styled today; no error-box defect arises from these hosts
  - [DISPOSITIONED] sample credit-modal (preview-form), same page-overflow, runtime-hotlink incl. candidate-own cdn.jsdelivr.net + cdn.scpwiki.com (judgment-required) — candidate-own foreign/sandbox delivery hosts: posting-time rewrite or original-state delivery class (T1 class (ii); KB-41/KB-54 family). The pages render styled today; no error-box defect arises from these hosts
  - [DISPOSITIONED] T3 clean on both pages — positive T3 assessment recorded in the row; no finding stands from this segment
  - [DISPOSITIONED] the original page chromium 1366x768 capture was a transient 503 (http.cat + hidden-* block), re-run once per rule 2 and the fresh capture is a clean real page — transient Wikidot 503 capture, not a result (KB-44)
  - [DISPOSITIONED] sample webkit *-full.png missing (32767px screenshot cap). — screenshot ceiling: the capture is incomplete above 32767px, a measurement limit (KB-46)
- **theme:our-open-veins-jp** (RENDER-S2-C (EN15)):
  - [DISPOSITIONED] page runtime-hotlink site-theme chain only — environment-layer: runtime hosts arrive via the shared site theme chain, not the candidate (KB-40; RENDER-S2-G cross-cutting 1)
  - [DISPOSITIONED] sample credit-modal (preview-form) — preview-form property: candidate/sample pages use credit:start-preview, which has no modal mechanism (GOSIGN-TESTS.md T2 note, 2026-11-16 ruling; KB-32)
  - [DISPOSITIONED] T3 broken OurDark20Mode.png (deferred), "使用方法" heading wraps one char/line at 320 (cosmetic). — owner-deferred hosting state (KB-58)
- **theme:pack-of-peanuts-jp** (RENDER-S2-C (EN15)):
  - [DISPOSITIONED] page-overflow 823–829px@768 (page) and 331px@320 + 920px@768 (sample) — page-overflow in the recorded cross-cutting families: static credit replica fixed width at mobile widths (KB-33) / preview chrome (KB-34); the per-theme figures match the campaign-wide shapes
  - [DISPOSITIONED] runtime-hotlink site-theme chain — environment-layer: runtime hosts arrive via the shared site theme chain, not the candidate (KB-40; RENDER-S2-G cross-cutting 1)
  - [DISPOSITIONED] sample credit-modal (preview-form). — preview-form property: candidate/sample pages use credit:start-preview, which has no modal mechanism (GOSIGN-TESTS.md T2 note, 2026-11-16 ruling; KB-32)
- **theme:paramycota-jp** (RENDER-S2-C (EN16)):
  - [DISPOSITIONED] page runtime-hotlink site-theme chain only — environment-layer: runtime hosts arrive via the shared site theme chain, not the candidate (KB-40; RENDER-S2-G cross-cutting 1)
  - [DISPOSITIONED] sample credit-modal (preview-form) — preview-form property: candidate/sample pages use credit:start-preview, which has no modal mechanism (GOSIGN-TESTS.md T2 note, 2026-11-16 ruling; KB-32)
  - [DISPOSITIONED] T3 broken SCP logo image (deferred asset), content readable. — missing/404 decorative assets are the owner-deferred hosting state, not theme defects (KB-58; LOCALIZE-S2-C checklist item 1, owner decision 2026-11-16)
- **theme:parawatch-pumpkin-jp** (RENDER-S2-C (EN16)):
  - [DISPOSITIONED] page runtime-hotlink site-theme chain only (T3: credit modal opens) — positive confirmation recorded in the row (the credit modal opens on this page); no finding stands
  - [DISPOSITIONED] sample credit-modal (preview-form) + page-overflow 325px@320 + 884px@768. — page-overflow in the recorded cross-cutting families: static credit replica fixed width at mobile widths (KB-33) / preview chrome (KB-34); the per-theme figures match the campaign-wide shapes
- **theme:pastel-skies-jp** (RENDER-S2-C (EN16)):
  - [DISPOSITIONED] page-overflow 467–478px@320/375 + 792–803px@768 (page) and 479–490px@320/375 + 953px@768 (sample) — page-overflow in the recorded cross-cutting families: static credit replica fixed width at mobile widths (KB-33) / preview chrome (KB-34); the per-theme figures match the campaign-wide shapes
  - [DISPOSITIONED] T3 overflow visually confirmed as content extending past the pastel frame — positive T3 confirmation recorded in the row; no finding stands from this segment
  - [DISPOSITIONED] sample credit-modal (preview-form) — preview-form property: candidate/sample pages use credit:start-preview, which has no modal mechanism (GOSIGN-TESTS.md T2 note, 2026-11-16 ruling; KB-32)
  - [DISPOSITIONED] broken logo deferred. — deferred asset hosting state (KB-58)
- **theme:plant-jp** (RENDER-S2-C (EN16)):
  - [DISPOSITIONED] page-overflow 851px@webkit-768 (page only) + runtime-hotlink site-theme chain — environment-layer: runtime hosts arrive via the shared site theme chain, not the candidate (KB-40; RENDER-S2-G cross-cutting 1)
  - [DISPOSITIONED] sample T2 no machine verdict (exit 2). — coverage caveat: this run returned no machine verdict (render_check exit 2); not a theme defect — see (a)
- **theme:prom-labs-jp** (RENDER-S2-C (EN16)):
  - [DISPOSITIONED] page runtime-hotlink site-theme chain only — environment-layer: runtime hosts arrive via the shared site theme chain, not the candidate (KB-40; RENDER-S2-G cross-cutting 1)
  - [DISPOSITIONED] sample T2 no machine verdict (exit 2). — coverage caveat: this run returned no machine verdict (render_check exit 2); not a theme defect — see (a)
- **theme:queen-s-gambit-jp** (RENDER-S2-C (EN17)):
  - [DISPOSITIONED] page runtime-hotlink site-theme chain only — environment-layer: runtime hosts arrive via the shared site theme chain, not the candidate (KB-40; RENDER-S2-G cross-cutting 1)
  - [DISPOSITIONED] sample credit-modal (preview-form) + 884px@768 overflow. — page-overflow in the recorded cross-cutting families: static credit replica fixed width at mobile widths (KB-33) / preview chrome (KB-34); the per-theme figures match the campaign-wide shapes
- **theme:queerstyle-jp** (RENDER-S2-C (EN17)):
  - [DISPOSITIONED] page hidden-rate (all combos) + runtime-hotlink site-theme chain — environment-layer: runtime hosts arrive via the shared site theme chain, not the candidate (KB-40; RENDER-S2-G cross-cutting 1)
  - [DISPOSITIONED] sample T2 no machine verdict (exit 2) — coverage caveat: this run returned no machine verdict (render_check exit 2); not a theme defect — see (a)
  - [OPEN] T3 rainbow pride logo overprints the SCP財団 header wordmark and account/search links at 375/320 (both engines, candidate header interference) — section (e), theme item 2
  - [OPEN] credit panel dark/blank at 1366. — section (e), theme item 3
- **theme:ragnarok-theme-jp** (RENDER-S2-C (EN17)):
  - [DISPOSITIONED] page runtime-hotlink site-theme chain only — environment-layer: runtime hosts arrive via the shared site theme chain, not the candidate (KB-40; RENDER-S2-G cross-cutting 1)
  - [DISPOSITIONED] sample T2 no machine verdict (exit 2). — coverage caveat: this run returned no machine verdict (render_check exit 2); not a theme defect — see (a)
- **theme:raisa-jp** (RENDER-S2-C (EN17)):
  - [DISPOSITIONED] page-overflow 328px@320 + 380px@375 + runtime-hotlink site-theme chain — environment-layer: runtime hosts arrive via the shared site theme chain, not the candidate (KB-40; RENDER-S2-G cross-cutting 1)
  - [DISPOSITIONED] sample T2 no machine verdict (exit 2) — coverage caveat: this run returned no machine verdict (render_check exit 2); not a theme defect — see (a)
  - [OPEN] T3 RAISA ring logo overprints header wordmark/account links at 375/320 (both engines) — section (e)
  - [DISPOSITIONED] broken black-highlighter-logo.svg (deferred). — owner-deferred hosting state (KB-58)
- **theme:raisa-sigma-jp** (RENDER-S2-C (EN17)):
  - [DISPOSITIONED] page T2 no machine verdict (exit 2) — coverage caveat: this run returned no machine verdict (render_check exit 2); not a theme defect — see (a)
  - [DISPOSITIONED] sample credit-modal (preview-form) + 884px@768 overflow + runtime-hotlink site-theme chain. — environment-layer: runtime hosts arrive via the shared site theme chain, not the candidate (KB-40; RENDER-S2-G cross-cutting 1)
- **theme:retro-aiad-theme-jp** (RENDER-S2-C (EN18)):
  - [DISPOSITIONED] page T2 no machine verdict (exit 2) — coverage caveat: this run returned no machine verdict (render_check exit 2); not a theme defect — see (a)
  - [DISPOSITIONED] sample credit-modal (preview-form) + 884px@768 overflow + runtime-hotlink site-theme chain. — environment-layer: runtime hosts arrive via the shared site theme chain, not the candidate (KB-40; RENDER-S2-G cross-cutting 1)
- **theme:retrofutura-jp** (RENDER-S2-C (EN18)):
  - [DISPOSITIONED] page T2 no machine verdict (exit 2) — coverage caveat: this run returned no machine verdict (render_check exit 2); not a theme defect — see (a)
  - [DISPOSITIONED] sample credit-modal (preview-form) + page-overflow 582–592px@320/375 + runtime-hotlink site-theme chain. — environment-layer: runtime hosts arrive via the shared site theme chain, not the candidate (KB-40; RENDER-S2-G cross-cutting 1)
- **theme:saphir-jp** (RERUN16 (EN18)):
  - [DISPOSITIONED] page page-overflow 682/685px@320/375 + 989px@768 chromium and 672/675px + 996px@768 webkit (T3: visually confirmed, driven by cross-cutting preview-chrome rate module), runtime-hotlink site-theme chain only — environment-layer: runtime hosts arrive via the shared site theme chain, not the candidate (KB-40; RENDER-S2-G cross-cutting 1)
  - [DISPOSITIONED] sample credit-modal (preview-form), page-overflow 706/708px@320/375 + 1031/1036px@768 (706/708 = cross-cutting static-credit shape) — cross-cutting static credit replica width (KB-33): the preview credit replica is fixed-width and overflows narrow viewports on every theme that carries it, including the 884px@768 figure
  - [DISPOSITIONED] T3 otherwise clean (sample section 27 bibliography-not-found = possible stale static-cache, not a theme defect) — stale static-cache phantom suspicion, recorded as a caution, not a proven signature (KB-49)
  - [DISPOSITIONED] saphir-header/sapphire-logo missing = deferred assets. — missing/404 decorative assets are the owner-deferred hosting state, not theme defects (KB-58; LOCALIZE-S2-C checklist item 1, owner decision 2026-11-16)
- **theme:scp-human-resources-sigma-jp** (RENDER-S2-C (EN18)):
  - [DISPOSITIONED] page runtime-hotlink site-theme chain only — environment-layer: runtime hosts arrive via the shared site theme chain, not the candidate (KB-40; RENDER-S2-G cross-cutting 1)
  - [DISPOSITIONED] sample credit-modal (preview-form) + page-overflow 330–335px@320 + 884px@768. — page-overflow in the recorded cross-cutting families: static credit replica fixed width at mobile widths (KB-33) / preview chrome (KB-34); the per-theme figures match the campaign-wide shapes
- **theme:scp-offices-sigma-jp** (RENDER-S2-C (EN18)):
  - [DISPOSITIONED] page runtime-hotlink site-theme chain + sidebar-not-opening — environment-layer: runtime hosts arrive via the shared site theme chain, not the candidate (KB-40; RENDER-S2-G cross-cutting 1)
  - [DISPOSITIONED] sample T2 no machine verdict (exit 2). — coverage caveat: this run returned no machine verdict (render_check exit 2); not a theme defect — see (a)
- **theme:shark-punching-centre-bhl-jp** (RERUN16 (EN19)):
  - [DISPOSITIONED] page runtime-hotlink site-theme chain only (sidebar-position machine warn at 1366 is a Sigma-9 baseline mismatch — environment-layer: runtime hosts arrive via the shared site theme chain, not the candidate (KB-40; RENDER-S2-G cross-cutting 1)
  - [DISPOSITIONED] T3 confirms sidebar visibly at left JP position, mobile button opens) — positive T3 confirmation recorded in the row; no finding stands from this segment
  - [DISPOSITIONED] sample credit-modal (preview-form), page-overflow 337px@320 + 389px@375 (cross-cutting static-credit), runtime-hotlink site-theme chain + sample font host — environment-layer: runtime hosts arrive via the shared site theme chain, not the candidate (KB-40; RENDER-S2-G cross-cutting 1)
  - [DISPOSITIONED] T3 clean on both pages (specimens 1–31 render — positive T3 assessment recorded in the row; no finding stands from this segment
  - [DISPOSITIONED] decorative logo 404s owner-deferred — owner-deferred hosting state (KB-58)
  - [DISPOSITIONED] WebKit stray glyph cross-cutting). — WebKit CC-badge stray glyph (KB-36)
- **theme:shattered-thoughts-jp** (RENDER-S2-D (EN19)):
  - [DISPOSITIONED] page runtime-hotlink site-theme chain only (T3: credit modal opens) — positive confirmation recorded in the row (the credit modal opens on this page); no finding stands
  - [DISPOSITIONED] sample credit-modal (preview-form) + 884px@768 overflow — page-overflow in the recorded cross-cutting families: static credit replica fixed width at mobile widths (KB-33) / preview chrome (KB-34); the per-theme figures match the campaign-wide shapes
  - [DISPOSITIONED] T3 broken explanet.png (deferred asset). — missing/404 decorative assets are the owner-deferred hosting state, not theme defects (KB-58; LOCALIZE-S2-C checklist item 1, owner decision 2026-11-16)
- **theme:shoebill-jp** (RENDER-S2-D (EN19)):
  - [DISPOSITIONED] page runtime-hotlink site-theme chain only — environment-layer: runtime hosts arrive via the shared site theme chain, not the candidate (KB-40; RENDER-S2-G cross-cutting 1)
  - [DISPOSITIONED] sample credit-modal (preview-form) + runtime-hotlink site-theme chain. — preview-form property: candidate/sample pages use credit:start-preview, which has no modal mechanism (GOSIGN-TESTS.md T2 note, 2026-11-16 ruling; KB-32)
- **theme:skiesmadestrange-jp** (RENDER-S2-D (EN19)):
  - [DISPOSITIONED] page runtime-hotlink site-theme chain only — environment-layer: runtime hosts arrive via the shared site theme chain, not the candidate (KB-40; RENDER-S2-G cross-cutting 1)
  - [DISPOSITIONED] sample credit-modal (preview-form) + 884px@768 overflow. — page-overflow in the recorded cross-cutting families: static credit replica fixed width at mobile widths (KB-33) / preview chrome (KB-34); the per-theme figures match the campaign-wide shapes
- **theme:spidersfalling-jp** (RENDER-S2-D (EN19)):
  - [DISPOSITIONED] page runtime-hotlink site-theme chain only — environment-layer: runtime hosts arrive via the shared site theme chain, not the candidate (KB-40; RENDER-S2-G cross-cutting 1)
  - [DISPOSITIONED] sample credit-modal (preview-form) + 884px@768 overflow. — page-overflow in the recorded cross-cutting families: static credit replica fixed width at mobile widths (KB-33) / preview chrome (KB-34); the per-theme figures match the campaign-wide shapes
- **theme:stargazer-jp** (RENDER-S2-D (EN20)):
  - [DISPOSITIONED] page-overflow 457–522px@320/375 on page and sample — page-overflow in the recorded cross-cutting families: static credit replica fixed width at mobile widths (KB-33) / preview chrome (KB-34); the per-theme figures match the campaign-wide shapes
  - [DISPOSITIONED] runtime-hotlink site-theme chain — environment-layer: runtime hosts arrive via the shared site theme chain, not the candidate (KB-40; RENDER-S2-G cross-cutting 1)
  - [DISPOSITIONED] sample credit-modal (preview-form). — preview-form property: candidate/sample pages use credit:start-preview, which has no modal mechanism (GOSIGN-TESTS.md T2 note, 2026-11-16 ruling; KB-32)
- **theme:stellar-jp** (RENDER-S2-D (EN20)):
  - [DISPOSITIONED] page-overflow 498–503px@320/375 + runtime-hotlink site-theme chain — environment-layer: runtime hosts arrive via the shared site theme chain, not the candidate (KB-40; RENDER-S2-G cross-cutting 1)
  - [DISPOSITIONED] sample T2 no machine verdict (exit 2, no summary). — coverage caveat: this run returned no machine verdict (render_check exit 2); not a theme defect — see (a)
- **theme:sunside-jp** (RENDER-S2-D (EN20)):
  - [DISPOSITIONED] page-overflow 502–510px@320/375 + 828–833px@768 (page) and 514–522px@320/375 + 828–833px@768 (sample) — page-overflow in the recorded cross-cutting families: static credit replica fixed width at mobile widths (KB-33) / preview chrome (KB-34); the per-theme figures match the campaign-wide shapes
  - [DISPOSITIONED] sample credit-modal (preview-form). — preview-form property: candidate/sample pages use credit:start-preview, which has no modal mechanism (GOSIGN-TESTS.md T2 note, 2026-11-16 ruling; KB-32)
- **theme:tales-of-the-mosaic-jp** (RENDER-S2-D (EN20)):
  - [DISPOSITIONED] page runtime-hotlink site-theme chain only — environment-layer: runtime hosts arrive via the shared site theme chain, not the candidate (KB-40; RENDER-S2-G cross-cutting 1)
  - [DISPOSITIONED] sample credit-modal (preview-form) + 884px@768 overflow. — page-overflow in the recorded cross-cutting families: static credit replica fixed width at mobile widths (KB-33) / preview chrome (KB-34); the per-theme figures match the campaign-wide shapes
- **theme:telecom-office-theme-jp** (RENDER-S2-D (EN20)):
  - [DISPOSITIONED] page runtime-hotlink site-theme chain only — environment-layer: runtime hosts arrive via the shared site theme chain, not the candidate (KB-40; RENDER-S2-G cross-cutting 1)
  - [DISPOSITIONED] sample hidden-rate (all 8 combos) + runtime-hotlink site-theme chain. — environment-layer: runtime hosts arrive via the shared site theme chain, not the candidate (KB-40; RENDER-S2-G cross-cutting 1)
- **theme:thalassophobia-jp** (RENDER-S2-D (EN21)):
  - [DISPOSITIONED] page-overflow 322px@320 + runtime-hotlink site-theme chain — environment-layer: runtime hosts arrive via the shared site theme chain, not the candidate (KB-40; RENDER-S2-G cross-cutting 1)
  - [DISPOSITIONED] sample T2 no machine verdict (exit 2, no summary). — coverage caveat: this run returned no machine verdict (render_check exit 2); not a theme defect — see (a)
- **theme:thalassophobia-sigma-jp** (RENDER-S2-D (EN21)):
  - [DISPOSITIONED] page hidden-* cluster + sidebar-unreachable confined to chromium-375, whose only hotlink host is http.cat = transient 503 capture, not a result — transient Wikidot 503 capture, not a result (KB-44)
  - [DISPOSITIONED] page runtime-hotlink site-theme chain otherwise — environment-layer: runtime hosts arrive via the shared site theme chain, not the candidate (KB-40; RENDER-S2-G cross-cutting 1)
  - [DISPOSITIONED] sample T2 no machine verdict (exit 2, no summary). — coverage caveat: this run returned no machine verdict (render_check exit 2); not a theme defect — see (a)
- **theme:the-coalition-theme-jp** (RENDER-S2-D (EN21)):
  - [DISPOSITIONED] page runtime-hotlink site-theme chain only — environment-layer: runtime hosts arrive via the shared site theme chain, not the candidate (KB-40; RENDER-S2-G cross-cutting 1)
  - [DISPOSITIONED] sample T2 no machine verdict (exit 2, no summary). — coverage caveat: this run returned no machine verdict (render_check exit 2); not a theme defect — see (a)
- **theme:the-foundation-sigma-jp** (RENDER-S2-D (EN21)):
  - [DISPOSITIONED] page-overflow 474–506px@320/375 (page) and 474–557px@320/375 (sample) — page-overflow in the recorded cross-cutting families: static credit replica fixed width at mobile widths (KB-33) / preview chrome (KB-34); the per-theme figures match the campaign-wide shapes
  - [DISPOSITIONED] sample credit-modal (preview-form). — preview-form property: candidate/sample pages use credit:start-preview, which has no modal mechanism (GOSIGN-TESTS.md T2 note, 2026-11-16 ruling; KB-32)
- **theme:the-smell-of-smoke-jp** (RENDER-S2-D (EN21)):
  - [DISPOSITIONED] page runtime-hotlink site-theme chain only — environment-layer: runtime hosts arrive via the shared site theme chain, not the candidate (KB-40; RENDER-S2-G cross-cutting 1)
  - [DISPOSITIONED] sample credit-modal (preview-form) + 884px@768 overflow. — page-overflow in the recorded cross-cutting families: static credit replica fixed width at mobile widths (KB-33) / preview chrome (KB-34); the per-theme figures match the campaign-wide shapes
- **theme:turbo-vision-dark-jp** (RENDER-S2-D (EN22)):
  - [DISPOSITIONED] page-overflow 365–372px@320 on page and sample — page-overflow in the recorded cross-cutting families: static credit replica fixed width at mobile widths (KB-33) / preview chrome (KB-34); the per-theme figures match the campaign-wide shapes
  - [DISPOSITIONED] sample credit-modal (preview-form). — preview-form property: candidate/sample pages use credit:start-preview, which has no modal mechanism (GOSIGN-TESTS.md T2 note, 2026-11-16 ruling; KB-32)
- **theme:twin-files-jp** (RENDER-S2-D (EN22)):
  - [DISPOSITIONED] page runtime-hotlink site-theme chain only — environment-layer: runtime hosts arrive via the shared site theme chain, not the candidate (KB-40; RENDER-S2-G cross-cutting 1)
  - [DISPOSITIONED] sample credit-modal (preview-form) + page-overflow 337–419px@320/375. — page-overflow in the recorded cross-cutting families: static credit replica fixed width at mobile widths (KB-33) / preview chrome (KB-34); the per-theme figures match the campaign-wide shapes
- **theme:ui-jp** (RENDER-S2-D (EN22)):
  - [DISPOSITIONED] hidden-* cluster (header-link, hidden-footer/license/login/pageContent/rate, sidebar-unreachable) across most combos on both pages — hidden-* machine cluster confined to a transient/503-tainted or single-engine capture, or not reproduced visually (KB-44/KB-49/KB-50 family); the row records no T3 defect from it
  - [DISPOSITIONED] sample credit-modal (preview-form) + 884px@768 overflow — page-overflow in the recorded cross-cutting families: static credit replica fixed width at mobile widths (KB-33) / preview chrome (KB-34); the per-theme figures match the campaign-wide shapes
  - [DISPOSITIONED] T3 nothing pointable beyond the machine lines. — machine lines not reproduced by the T3 walk (the row’s own T3 note); KB-49/KB-50 family
- **theme:uiu-bhl-theme-jp** (RENDER-S2-D (EN22)):
  - [DISPOSITIONED] page-overflow 470px@320 + 525px@375 + 918px@768 + runtime-hotlink site-theme chain — environment-layer: runtime hosts arrive via the shared site theme chain, not the candidate (KB-40; RENDER-S2-G cross-cutting 1)
  - [DISPOSITIONED] sample T2 no machine verdict (exit 2, no summary). — coverage caveat: this run returned no machine verdict (render_check exit 2); not a theme defect — see (a)
- **theme:unusual-cargo-jp** (RENDER-S2-D (EN22)):
  - [DISPOSITIONED] page-overflow 344–349px@320 (page) and 344–349px@320 + 884px@768 (sample) — page-overflow in the recorded cross-cutting families: static credit replica fixed width at mobile widths (KB-33) / preview chrome (KB-34); the per-theme figures match the campaign-wide shapes
  - [DISPOSITIONED] sample credit-modal (preview-form). — preview-form property: candidate/sample pages use credit:start-preview, which has no modal mechanism (GOSIGN-TESTS.md T2 note, 2026-11-16 ruling; KB-32)
- **theme:vanguard-jp** (RENDER-S2-D (EN23)):
  - [DISPOSITIONED] page-overflow 330px@320 + 385px@375 + runtime-hotlink site-theme chain — environment-layer: runtime hosts arrive via the shared site theme chain, not the candidate (KB-40; RENDER-S2-G cross-cutting 1)
  - [DISPOSITIONED] sample T2 no machine verdict (exit 2, no summary). — coverage caveat: this run returned no machine verdict (render_check exit 2); not a theme defect — see (a)
- **theme:vanguard-supplement-jp** (RENDER-S2-D (EN23)):
  - [DISPOSITIONED] page T2 no machine verdict (exit 2, no summary) — coverage caveat: this run returned no machine verdict (render_check exit 2); not a theme defect — see (a)
  - [DISPOSITIONED] sample hidden-rate (all combos) + page-overflow 330–335px@320 + 884px@768 + runtime-hotlink site-theme chain. — environment-layer: runtime hosts arrive via the shared site theme chain, not the candidate (KB-40; RENDER-S2-G cross-cutting 1)
- **theme:wilderness-jp** (RENDER-S2-D (EN23)):
  - [DISPOSITIONED] page runtime-hotlink site-theme chain only — environment-layer: runtime hosts arrive via the shared site theme chain, not the candidate (KB-40; RENDER-S2-G cross-cutting 1)
  - [DISPOSITIONED] sample T2 no machine verdict (exit 2, no summary). — coverage caveat: this run returned no machine verdict (render_check exit 2); not a theme defect — see (a)
- **theme:wondertainment-jp** (RENDER-S2-D (EN23)):
  - [DISPOSITIONED] page runtime-hotlink site-theme chain only — environment-layer: runtime hosts arrive via the shared site theme chain, not the candidate (KB-40; RENDER-S2-G cross-cutting 1)
  - [DISPOSITIONED] sample T2 no machine verdict (exit 2, no summary). — coverage caveat: this run returned no machine verdict (render_check exit 2); not a theme defect — see (a)
- **theme:words-of-wisdom-jp** (RENDER-S2-D (EN23)):
  - [DISPOSITIONED] page hidden-* cluster + sidebar-unreachable confined to chromium-375, whose only hotlink host is http.cat = transient 503 capture, not a result — transient Wikidot 503 capture, not a result (KB-44)
  - [DISPOSITIONED] sample credit-modal (preview-form) + 884px@768 overflow + runtime-hotlink site-theme chain. — environment-layer: runtime hosts arrive via the shared site theme chain, not the candidate (KB-40; RENDER-S2-G cross-cutting 1)
- **theme:writing-anomalies-jp** (RENDER-S2-D (EN24)):
  - [DISPOSITIONED] page runtime-hotlink site-theme chain only — environment-layer: runtime hosts arrive via the shared site theme chain, not the candidate (KB-40; RENDER-S2-G cross-cutting 1)
  - [DISPOSITIONED] sample T2 no machine verdict (exit 2, no summary). — coverage caveat: this run returned no machine verdict (render_check exit 2); not a theme defect — see (a)
- **theme:xmas-jp** (RENDER-S2-D (EN24)):
  - [DISPOSITIONED] page runtime-hotlink site-theme chain only — environment-layer: runtime hosts arrive via the shared site theme chain, not the candidate (KB-40; RENDER-S2-G cross-cutting 1)
  - [DISPOSITIONED] sample T2 no machine verdict (exit 2, no summary). — coverage caveat: this run returned no machine verdict (render_check exit 2); not a theme defect — see (a)
- **theme:andesite-jp** (RENDER-S2-E (CN1)):
  - [DISPOSITIONED] page-overflow 500–501px@320/375 (page) and 512–513px@320/375 (sample) — page-overflow in the recorded cross-cutting families: static credit replica fixed width at mobile widths (KB-33) / preview chrome (KB-34); the per-theme figures match the campaign-wide shapes
  - [DISPOSITIONED] runtime-hotlink site-theme chain — environment-layer: runtime hosts arrive via the shared site theme chain, not the candidate (KB-40; RENDER-S2-G cross-cutting 1)
  - [DISPOSITIONED] sample credit-modal (preview-form). — preview-form property: candidate/sample pages use credit:start-preview, which has no modal mechanism (GOSIGN-TESTS.md T2 note, 2026-11-16 ruling; KB-32)
- **theme:another-night-jp** (RENDER-S2-E (CN1)):
  - [DISPOSITIONED] page hidden-rate + sidebar-not-opening (all combos) + runtime-hotlink site-theme chain with cdn.jsdelivr.net — candidate-own foreign/sandbox delivery hosts: posting-time rewrite or original-state delivery class (T1 class (ii); KB-41/KB-54 family). The pages render styled today; no error-box defect arises from these hosts
  - [DISPOSITIONED] sample T2 no machine verdict (exit 2, no summary). — coverage caveat: this run returned no machine verdict (render_check exit 2); not a theme defect — see (a)
- **theme:ared-jp** (RERUN16 (CN1)):
  - [DISPOSITIONED] page page-overflow 328px@320 only (8px), runtime-hotlink site-theme chain + candidate-own ah-sandbox.wdfiles.com, ah-sandbox.wikidot.com (judgment-required) — candidate-own foreign/sandbox delivery hosts: posting-time rewrite or original-state delivery class (T1 class (ii); KB-41/KB-54 family). The pages render styled today; no error-box defect arises from these hosts
  - [DISPOSITIONED] sample credit-modal (preview-form), page-overflow 328px@320 + 884px@768 (cross-cutting static-credit), runtime-hotlink incl. the ah-sandbox hosts + sample font host — candidate-own foreign/sandbox delivery hosts: posting-time rewrite or original-state delivery class (T1 class (ii); KB-41/KB-54 family). The pages render styled today; no error-box defect arises from these hosts
  - [DISPOSITIONED] T3 clean on both pages (sidebar at left JP position, opens in both engines — positive T3 confirmation recorded in the row; no finding stands from this segment
  - [DISPOSITIONED] subtitle doubling + preview-notice clipping cross-cutting). — site-header subtitle doubling at <=375px, shared site-theme shape (KB-35)
- **theme:asagao-jp** (RENDER-S2-E (CN1)):
  - [DISPOSITIONED] page hidden-* cluster at chromium ≤768 (the chromium-768/375 captures carry an http.cat-only hotlink line = transient 503 — transient Wikidot 503 capture, not a result (KB-44)
  - [DISPOSITIONED] the chromium-320 cluster is recorded as-is) + sidebar-unreachable at chromium ≤375 — single-engine or single-combo machine line, not confirmed by the T3 walk (KB-47 family: single-combo ORB/machine flakiness); where T3 checked the drawer it is recorded opening
  - [DISPOSITIONED] sample credit-modal (preview-form) + page-overflow 842px@768. — page-overflow in the recorded cross-cutting families: static credit replica fixed width at mobile widths (KB-33) / preview chrome (KB-34); the per-theme figures match the campaign-wide shapes
- **theme:betwixt-jp** (RERUN16 (CN2)):
  - [OPEN] REAL WebKit-specific FINDING on both pages: the top-left mobile sidebar-open hamburger renders in chromium but is entirely absent in webkit at 375x812 and 320x640, leaving no visible way to open the sidebar in webkit (screenshot-confirmed — section (e)
  - [OPEN] machine `sidebar-unreachable` on all four mobile combos) — section (e)
  - [DISPOSITIONED] page-overflow 434px chromium / 438px webkit @320/375 — page-overflow in the recorded cross-cutting families: static credit replica fixed width at mobile widths (KB-33) / preview chrome (KB-34); the per-theme figures match the campaign-wide shapes
  - [DISPOSITIONED] runtime-hotlink incl. candidate-own ah-sandbox hosts, hormress.github.io, nu-scptheme.github.io (judgment-required) — candidate-own foreign/sandbox delivery hosts: posting-time rewrite or original-state delivery class (T1 class (ii); KB-41/KB-54 family). The pages render styled today; no error-box defect arises from these hosts
  - [DISPOSITIONED] sample adds credit-modal (preview-form) — preview-form property: candidate/sample pages use credit:start-preview, which has no modal mechanism (GOSIGN-TESTS.md T2 note, 2026-11-16 ruling; KB-32)
  - [DISPOSITIONED] decorative 404/ORB assets leave a flat light-blue header (deferred). — ORB/load-block artifact class: single-combo or delivery-MIME symptom (KB-47 family); where the blocked asset is a candidate asset its remedy is the posting-time re-hosting class, and no source defect is identified
- **theme:black-rain-jp** (RERUN16 (CN2)):
  - [DISPOSITIONED] page runtime-hotlink site-theme chain only — environment-layer: runtime hosts arrive via the shared site theme chain, not the candidate (KB-40; RENDER-S2-G cross-cutting 1)
  - [DISPOSITIONED] sample credit-modal (preview-form), page-overflow 337px@320 + 389px@375 chromium and 416px@320 + 419px@375 webkit (cross-cutting static-credit), runtime-hotlink site-theme chain + sample font host — environment-layer: runtime hosts arrive via the shared site theme chain, not the candidate (KB-40; RENDER-S2-G cross-cutting 1)
  - [DISPOSITIONED] T3 complete in the final report (pending in the partial) and clean on both pages (sidebar left JP position, mobile hamburger present in both engines and opens — positive T3 confirmation recorded in the row; no finding stands from this segment
  - [DISPOSITIONED] sample 503 warnings were stylesheet resources only, page rendered normally) — transient 503 on stylesheet resources only; the page rendered normally (KB-44 family)
  - [DISPOSITIONED] black-rain-logo 404 = deferred asset. — missing/404 decorative assets are the owner-deferred hosting state, not theme defects (KB-58; LOCALIZE-S2-C checklist item 1, owner decision 2026-11-16)
- **theme:blackinblack-jp** (RENDER-S2-E (CN2)):
  - [DISPOSITIONED] page runtime-hotlink site-theme chain only — environment-layer: runtime hosts arrive via the shared site theme chain, not the candidate (KB-40; RENDER-S2-G cross-cutting 1)
  - [DISPOSITIONED] sample credit-modal (preview-form) + 884px@768 overflow. — page-overflow in the recorded cross-cutting families: static credit replica fixed width at mobile widths (KB-33) / preview chrome (KB-34); the per-theme figures match the campaign-wide shapes
- **theme:brokedown-database-jp** (RERUN16 (CN2)):
  - [DISPOSITIONED] page page-overflow 328px@320 chromium (8px), runtime-hotlink site-theme chain only — environment-layer: runtime hosts arrive via the shared site theme chain, not the candidate (KB-40; RENDER-S2-G cross-cutting 1)
  - [DISPOSITIONED] sample credit-modal (preview-form), page-overflow 341px@320 + 389px@375 chromium and 416px@320 + 419px@375 webkit (cross-cutting static-credit), runtime-hotlink site-theme chain + sample font host — environment-layer: runtime hosts arrive via the shared site theme chain, not the candidate (KB-40; RENDER-S2-G cross-cutting 1)
  - [DISPOSITIONED] T3 complete in the final report (pending in the partial) and clean on both pages (sidebar collapsed at PC width with left-edge toggle tab present, mobile hamburger opens in both engines, cyan-on-black readable) — positive T3 confirmation recorded in the row; no finding stands from this segment
  - [DISPOSITIONED] missing decorative logos = deferred assets. — missing/404 decorative assets are the owner-deferred hosting state, not theme defects (KB-58; LOCALIZE-S2-C checklist item 1, owner decision 2026-11-16)
- **theme:broken-light-jp** (RENDER-S2-E (CN2)):
  - [DISPOSITIONED] page runtime-hotlink site-theme chain only — environment-layer: runtime hosts arrive via the shared site theme chain, not the candidate (KB-40; RENDER-S2-G cross-cutting 1)
  - [DISPOSITIONED] sample credit-modal (preview-form) + page-overflow 337–419px@320/375. — page-overflow in the recorded cross-cutting families: static credit replica fixed width at mobile widths (KB-33) / preview chrome (KB-34); the per-theme figures match the campaign-wide shapes
- **theme:broken-world-jp** (RERUN16 (CN3)):
  - [DISPOSITIONED] `hidden-interwiki` on all 8 combos on both pages (translation module hidden, theme-level — original-faithful: the row itself documents the hidden interwiki as the original’s quirk, described in the page text
  - [DISPOSITIONED] T3: explicitly documented in the page text as an original quirk), page-overflow 374px@320 + 425px@375 + 810px@768 chromium and 450px@320 + 478px@375 webkit, runtime-hotlink site-theme chain only — environment-layer: runtime hosts arrive via the shared site theme chain, not the candidate (KB-40; RENDER-S2-G cross-cutting 1)
  - [DISPOSITIONED] sample adds credit-modal (preview-form) — preview-form property: candidate/sample pages use credit:start-preview, which has no modal mechanism (GOSIGN-TESTS.md T2 note, 2026-11-16 ruling; KB-32)
  - [DISPOSITIONED] T3 complete in the final report (pending in the partial), no further finding (desktop sidebar collapsed with no visible reopen tab, mobile hamburger opens in both engines — positive T3 confirmation recorded in the row; no finding stands from this segment
  - [DISPOSITIONED] low-contrast credit title and 404 logos intended/deferred). — machine contrast value not confirmed as a defect by the T3 walk (KB-39: machine contrast warns include false positives on themed surfaces)
- **theme:candela-jp** (RENDER-S2-E (CN3)):
  - [DISPOSITIONED] page-overflow 515–525px@320/375 on page and sample (+ 853–854px@768 on sample) — page-overflow in the recorded cross-cutting families: static credit replica fixed width at mobile widths (KB-33) / preview chrome (KB-34); the per-theme figures match the campaign-wide shapes
  - [DISPOSITIONED] page hidden-* cluster confined to webkit-320, whose only hotlink host is http.cat = transient 503 capture, not a result — transient Wikidot 503 capture, not a result (KB-44)
  - [DISPOSITIONED] sample credit-modal (preview-form) + sidebar-not-opening at webkit-768. — preview-form property: candidate/sample pages use credit:start-preview, which has no modal mechanism (GOSIGN-TESTS.md T2 note, 2026-11-16 ruling; KB-32)
- **theme:cmst-jp** (RENDER-S2-E (CN3)):
  - [DISPOSITIONED] page runtime-hotlink site-theme chain only — environment-layer: runtime hosts arrive via the shared site theme chain, not the candidate (KB-40; RENDER-S2-G cross-cutting 1)
  - [DISPOSITIONED] sample credit-modal (preview-form) + 884px@768 overflow. — page-overflow in the recorded cross-cutting families: static credit replica fixed width at mobile widths (KB-33) / preview chrome (KB-34); the per-theme figures match the campaign-wide shapes
- **theme:cobalt-aero-glass-jp** (RENDER-S2-E (CN3)):
  - [DISPOSITIONED] page hidden-* cluster confined to chromium-768, whose only hotlink host is http.cat = transient 503 capture, not a result — transient Wikidot 503 capture, not a result (KB-44)
  - [OPEN] page sidebar-unreachable at ≤375 (both engines) — section (e), theme item 2
  - [DISPOSITIONED] sample T2 no machine verdict (exit 2, no summary). — coverage caveat: this run returned no machine verdict (render_check exit 2); not a theme defect — see (a)
- **theme:construct-jp** (RENDER-S2-E (CN3)):
  - [DISPOSITIONED] page runtime-hotlink site-theme chain only — environment-layer: runtime hosts arrive via the shared site theme chain, not the candidate (KB-40; RENDER-S2-G cross-cutting 1)
  - [DISPOSITIONED] sample hidden-* cluster confined to webkit-1366, whose only hotlink host is http.cat = transient 503 capture, not a result — transient Wikidot 503 capture, not a result (KB-44)
  - [DISPOSITIONED] sample credit-modal (preview-form) + 884px@768 overflow. — page-overflow in the recorded cross-cutting families: static credit replica fixed width at mobile widths (KB-33) / preview chrome (KB-34); the per-theme figures match the campaign-wide shapes
- **theme:copper-jp** (RENDER-S2-E (CN4)):
  - [DISPOSITIONED] page runtime-hotlink site-theme chain only — environment-layer: runtime hosts arrive via the shared site theme chain, not the candidate (KB-40; RENDER-S2-G cross-cutting 1)
  - [DISPOSITIONED] sample credit-modal (preview-form) + page-overflow 340px@320 + 896px@768. — page-overflow in the recorded cross-cutting families: static credit replica fixed width at mobile widths (KB-33) / preview chrome (KB-34); the per-theme figures match the campaign-wide shapes
- **theme:crt-jp** (RENDER-S2-E (CN4)):
  - [DISPOSITIONED] page runtime-hotlink site-theme chain only — environment-layer: runtime hosts arrive via the shared site theme chain, not the candidate (KB-40; RENDER-S2-G cross-cutting 1)
  - [DISPOSITIONED] sample credit-modal (preview-form) + page-overflow 327px@320 + 908px@768. — page-overflow in the recorded cross-cutting families: static credit replica fixed width at mobile widths (KB-33) / preview chrome (KB-34); the per-theme figures match the campaign-wide shapes
- **theme:darkblue-jp** (RENDER-S2-E (CN4)):
  - [DISPOSITIONED] page T2 no machine verdict (exit 2, no summary) — coverage caveat: this run returned no machine verdict (render_check exit 2); not a theme defect — see (a)
  - [OPEN] sample page-overflow 387–389px@320/375 + sidebar-unreachable at ≤375 (both engines) + runtime-hotlink site-theme chain. — section (e), theme item 2
- **theme:decay-jp** (RENDER-S2-E (CN4)):
  - [DISPOSITIONED] page-overflow 331px@320 (page) and 331px@320 + 884px@768 (sample) — page-overflow in the recorded cross-cutting families: static credit replica fixed width at mobile widths (KB-33) / preview chrome (KB-34); the per-theme figures match the campaign-wide shapes
  - [DISPOSITIONED] runtime-hotlink site-theme chain — environment-layer: runtime hosts arrive via the shared site theme chain, not the candidate (KB-40; RENDER-S2-G cross-cutting 1)
  - [DISPOSITIONED] sample credit-modal (preview-form). — preview-form property: candidate/sample pages use credit:start-preview, which has no modal mechanism (GOSIGN-TESTS.md T2 note, 2026-11-16 ruling; KB-32)
- **theme:deepspace-jp** (RENDER-S2-E (CN4)):
  - [DISPOSITIONED] hidden-rate on both pages (all combos) — hidden-rate machine values are recorded only; the rate module’s repair status is owned by the source layer, and the current checker run shows no-rate standing only on the Sigma-10 exception file (KB-50; RENDER-B cross-cutting 5)
  - [DISPOSITIONED] page-overflow 501–502px@320/375 (page) and 505–506px@320/375 + 789px@768 + 1489px@1366 (sample) — page-overflow in the recorded cross-cutting families: static credit replica fixed width at mobile widths (KB-33) / preview chrome (KB-34); the per-theme figures match the campaign-wide shapes
  - [DISPOSITIONED] runtime-hotlink site-theme chain. — environment-layer: runtime hosts arrive via the shared site theme chain, not the candidate (KB-40; RENDER-S2-G cross-cutting 1)
- **theme:deserted-years-theme-jp** (RERUN16 (CN5)):
  - [DISPOSITIONED] page runtime-hotlink site-theme chain only (cleanest run of the 17) — environment-layer: runtime hosts arrive via the shared site theme chain, not the candidate (KB-40; RENDER-S2-G cross-cutting 1)
  - [DISPOSITIONED] sample credit-modal (preview-form), page-overflow 335px@320 chromium + 334px@320 webkit + 884px@768 both engines (cross-cutting static-credit), runtime-hotlink site-theme chain + sample font host — environment-layer: runtime hosts arrive via the shared site theme chain, not the candidate (KB-40; RENDER-S2-G cross-cutting 1)
  - [DISPOSITIONED] T3 complete in the final report (pending in the partial) and clean on both pages (page credit modal opens — positive confirmation recorded in the row (the credit modal opens on this page); no finding stands
  - [DISPOSITIONED] sample black-on-black redaction by design — deliberate specimen shape (redaction blocks render as designed), KB-37; RENDER-B cross-cutting 1
  - [DISPOSITIONED] subtitle doubling + preview-notice clipping cross-cutting). — site-header subtitle doubling at <=375px, shared site-theme shape (KB-35)
- **theme:dream-of-the-stars-jp** (RENDER-S2-E (CN5)):
  - [DISPOSITIONED] page-overflow 337px@320 + 996–999px@320/375 + 1018px@768 (page) and 581–584px@320/375 + 996–1018px (sample) — page-overflow in the recorded cross-cutting families: static credit replica fixed width at mobile widths (KB-33) / preview chrome (KB-34); the per-theme figures match the campaign-wide shapes
  - [DISPOSITIONED] sample credit-modal (preview-form). — preview-form property: candidate/sample pages use credit:start-preview, which has no modal mechanism (GOSIGN-TESTS.md T2 note, 2026-11-16 ruling; KB-32)
- **theme:drunken-alley-jp** (RENDER-S2-E (CN5)):
  - [DISPOSITIONED] page runtime-hotlink site-theme chain + scp-wiki-cloud.wdfiles.com — environment-layer: runtime hosts arrive via the shared site theme chain, not the candidate (KB-40; RENDER-S2-G cross-cutting 1)
  - [DISPOSITIONED] sample credit-modal (preview-form) + page-overflow 377–423px@320/375 + 884px@768. — page-overflow in the recorded cross-cutting families: static credit replica fixed width at mobile widths (KB-33) / preview chrome (KB-34); the per-theme figures match the campaign-wide shapes
- **theme:dustframe-jp** (RENDER-S2-E (CN5)):
  - [DISPOSITIONED] page-overflow 332px@320 + 387px@375 (page) and 337px@320 + 387px@375 (sample) — page-overflow in the recorded cross-cutting families: static credit replica fixed width at mobile widths (KB-33) / preview chrome (KB-34); the per-theme figures match the campaign-wide shapes
  - [DISPOSITIONED] sample credit-modal (preview-form). — preview-form property: candidate/sample pages use credit:start-preview, which has no modal mechanism (GOSIGN-TESTS.md T2 note, 2026-11-16 ruling; KB-32)
- **theme:emotion-division-jp** (RENDER-S2-E (CN5)):
  - [DISPOSITIONED] page-overflow 497–504px@320/375 on page and sample (+ 884px@768 on sample) — page-overflow in the recorded cross-cutting families: static credit replica fixed width at mobile widths (KB-33) / preview chrome (KB-34); the per-theme figures match the campaign-wide shapes
  - [DISPOSITIONED] page hidden-* cluster (no sidebar-unreachable) confined to chromium-1366, whose only hotlink host is http.cat = transient 503 capture, not a result — transient Wikidot 503 capture, not a result (KB-44)
  - [DISPOSITIONED] sample credit-modal (preview-form). — preview-form property: candidate/sample pages use credit:start-preview, which has no modal mechanism (GOSIGN-TESTS.md T2 note, 2026-11-16 ruling; KB-32)
- **theme:ethic-committee-jp** (RENDER-S2-E (CN6)):
  - [DISPOSITIONED] page runtime-hotlink site-theme chain only — environment-layer: runtime hosts arrive via the shared site theme chain, not the candidate (KB-40; RENDER-S2-G cross-cutting 1)
  - [DISPOSITIONED] sample T2 no machine verdict (exit 2, no summary). — coverage caveat: this run returned no machine verdict (render_check exit 2); not a theme defect — see (a)
- **theme:fmd-bhl-theme-jp** (RERUN16 (CN6)):
  - [DISPOSITIONED] page runtime-hotlink site-theme chain + candidate-own scpsandboxcn.wdfiles.com (judgment-required) — candidate-own foreign/sandbox delivery hosts: posting-time rewrite or original-state delivery class (T1 class (ii); KB-41/KB-54 family). The pages render styled today; no error-box defect arises from these hosts
  - [DISPOSITIONED] sample credit-modal (preview-form), runtime-hotlink incl. scpsandboxcn.wdfiles.com + sample font host — preview-form property: candidate/sample pages use credit:start-preview, which has no modal mechanism (GOSIGN-TESTS.md T2 note, 2026-11-16 ruling; KB-32)
  - [DISPOSITIONED] no page-overflow on either page — page-overflow in the recorded cross-cutting families: static credit replica fixed width at mobile widths (KB-33) / preview chrome (KB-34); the per-theme figures match the campaign-wide shapes
  - [DISPOSITIONED] T3 clean on both pages, with the caveat that the mobile *-full.png (and sample *-credit.png) are blank transient 503 captures while the same-viewport sidebar/credit shots are real and show the left sidebar opening in both engines (no rule-2 http.cat + hidden-* machine signature on this target). — transient Wikidot 503 capture, not a result (KB-44)
- **theme:food-jp** (RENDER-S2-E (CN6)):
  - [DISPOSITIONED] page runtime-hotlink site-theme chain only — environment-layer: runtime hosts arrive via the shared site theme chain, not the candidate (KB-40; RENDER-S2-G cross-cutting 1)
  - [DISPOSITIONED] sample credit-modal (preview-form) + page-overflow 337–419px@320/375. — page-overflow in the recorded cross-cutting families: static credit replica fixed width at mobile widths (KB-33) / preview chrome (KB-34); the per-theme figures match the campaign-wide shapes
- **theme:foundom-jp** (RENDER-S2-E (CN6)):
  - [DISPOSITIONED] page-overflow 509–519px@320/375 + runtime-hotlink site-theme chain — environment-layer: runtime hosts arrive via the shared site theme chain, not the candidate (KB-40; RENDER-S2-G cross-cutting 1)
  - [DISPOSITIONED] sample T2 no machine verdict (exit 2, no summary). — coverage caveat: this run returned no machine verdict (render_check exit 2); not a theme defect — see (a)
- **theme:frutiger-aero-jp** (RENDER-S2-E (CN6)):
  - [DISPOSITIONED] page hidden-login (6 combos) + sidebar-not-opening (webkit) + runtime-hotlink site-theme chain — environment-layer: runtime hosts arrive via the shared site theme chain, not the candidate (KB-40; RENDER-S2-G cross-cutting 1)
  - [DISPOSITIONED] sample T2 no machine verdict (exit 2, no summary). — coverage caveat: this run returned no machine verdict (render_check exit 2); not a theme defect — see (a)
- **theme:golden-wind-jp** (RENDER-S2-F (CN7)):
  - [DISPOSITIONED] page runtime-hotlink site-theme chain only — environment-layer: runtime hosts arrive via the shared site theme chain, not the candidate (KB-40; RENDER-S2-G cross-cutting 1)
  - [DISPOSITIONED] sample credit-modal (preview-form) + 884px@768 overflow. — page-overflow in the recorded cross-cutting families: static credit replica fixed width at mobile widths (KB-33) / preview chrome (KB-34); the per-theme figures match the campaign-wide shapes
- **theme:gp-refresh-jp** (RENDER-S2-F (CN7)):
  - [DISPOSITIONED] page-overflow 1449px@1366 (page, desktop width) + hidden-login (4 combos) + runtime-hotlink site-theme chain — environment-layer: runtime hosts arrive via the shared site theme chain, not the candidate (KB-40; RENDER-S2-G cross-cutting 1)
  - [DISPOSITIONED] sample T2 no machine verdict (exit 2, no summary). — coverage caveat: this run returned no machine verdict (render_check exit 2); not a theme defect — see (a)
- **theme:greyday-jp** (RENDER-S2-F (CN7)):
  - [DISPOSITIONED] hidden-login (4 combos) on page and sample + runtime-hotlink site-theme chain — environment-layer: runtime hosts arrive via the shared site theme chain, not the candidate (KB-40; RENDER-S2-G cross-cutting 1)
  - [DISPOSITIONED] sample credit-modal (preview-form). — preview-form property: candidate/sample pages use credit:start-preview, which has no modal mechanism (GOSIGN-TESTS.md T2 note, 2026-11-16 ruling; KB-32)
- **theme:gsk-jp** (RERUN16 (CN7)):
  - [DISPOSITIONED] page runtime-hotlink site-theme chain only — environment-layer: runtime hosts arrive via the shared site theme chain, not the candidate (KB-40; RENDER-S2-G cross-cutting 1)
  - [DISPOSITIONED] sample credit-modal (preview-form), page-overflow 337px@320 + 389px@375 chromium and 416px@320 + 419px@375 webkit (cross-cutting static-credit), runtime-hotlink site-theme chain + sample font host — environment-layer: runtime hosts arrive via the shared site theme chain, not the candidate (KB-40; RENDER-S2-G cross-cutting 1)
  - [DISPOSITIONED] T3 clean on both pages — positive T3 assessment recorded in the row; no finding stands from this segment
  - [DISPOSITIONED] the original sample webkit 320x640 capture was a transient 503 (http.cat + hidden-* block), re-run once per rule 2 and the fresh capture carries no 503 signature — transient Wikidot 503 capture, not a result (KB-44)
  - [DISPOSITIONED] site-logo.png 404 (broken alt-text header logo clipped at mobile) = deferred asset. — missing/404 decorative assets are the owner-deferred hosting state, not theme defects (KB-58; LOCALIZE-S2-C checklist item 1, owner decision 2026-11-16)
- **theme:highlighter-bhl-jp** (RERUN16 (CN7)):
  - [DISPOSITIONED] page page-overflow 467px@320 + 495px@375 chromium and 430px@320 + 458px@375 webkit, runtime-hotlink site-theme chain only — environment-layer: runtime hosts arrive via the shared site theme chain, not the candidate (KB-40; RENDER-S2-G cross-cutting 1)
  - [DISPOSITIONED] sample credit-modal (preview-form), page-overflow 467px@320 + 495px@375 chromium and 430px@320 + 419px@375 webkit, runtime-hotlink site-theme chain + sample font host — environment-layer: runtime hosts arrive via the shared site theme chain, not the candidate (KB-40; RENDER-S2-G cross-cutting 1)
  - [DISPOSITIONED] T3 clean on both pages (sidebar left JP position, opens in both engines — positive T3 confirmation recorded in the row; no finding stands from this segment
  - [DISPOSITIONED] preview-notice clipping and overflow cross-cutting) — preview-notice clipping/overprint at narrow widths (KB-34)
  - [DISPOSITIONED] sample webkit *-full.png absent (screenshot set incomplete, 32767px cap). — screenshot ceiling: the capture is incomplete above 32767px, a measurement limit (KB-46)
- **theme:horn-jp** (RENDER-S2-F (CN8)):
  - [DISPOSITIONED] page runtime-hotlink site-theme chain only — environment-layer: runtime hosts arrive via the shared site theme chain, not the candidate (KB-40; RENDER-S2-G cross-cutting 1)
  - [DISPOSITIONED] sample hidden-* cluster confined to webkit-1366, whose only hotlink host is http.cat = transient 503 capture, not a result — transient Wikidot 503 capture, not a result (KB-44)
  - [DISPOSITIONED] sample credit-modal (preview-form) + 884px@768 overflow. — page-overflow in the recorded cross-cutting families: static credit replica fixed width at mobile widths (KB-33) / preview chrome (KB-34); the per-theme figures match the campaign-wide shapes
- **theme:ink-jp** (RENDER-S2-F (CN8)):
  - [DISPOSITIONED] page-overflow 606–610px@320/375 + 931px@768 + runtime-hotlink site-theme chain — environment-layer: runtime hosts arrive via the shared site theme chain, not the candidate (KB-40; RENDER-S2-G cross-cutting 1)
  - [DISPOSITIONED] sample T2 no machine verdict (exit 2, no summary). — coverage caveat: this run returned no machine verdict (render_check exit 2); not a theme defect — see (a)
- **theme:inland-empire-jp** (RENDER-S2-F (CN8)):
  - [DISPOSITIONED] page hidden-login (4 combos) + runtime-hotlink site-theme chain — environment-layer: runtime hosts arrive via the shared site theme chain, not the candidate (KB-40; RENDER-S2-G cross-cutting 1)
  - [DISPOSITIONED] sample T2 no machine verdict (exit 2, no summary). — coverage caveat: this run returned no machine verdict (render_check exit 2); not a theme defect — see (a)
- **theme:kitchen-jp** (RERUN16 (CN8)):
  - [DISPOSITIONED] page runtime-hotlink incl. candidate-own ah-sandbox.wdfiles.com, ah-sandbox.wikidot.com, bhl.scpwikicn.com, hormress.github.io, nu-scptheme.github.io, scpsandboxcn.wdfiles.com (judgment-required), no page-overflow — candidate-own foreign/sandbox delivery hosts: posting-time rewrite or original-state delivery class (T1 class (ii); KB-41/KB-54 family). The pages render styled today; no error-box defect arises from these hosts
  - [DISPOSITIONED] sample credit-modal (preview-form), runtime-hotlink incl. the same candidate-own hosts + sample font host — preview-form property: candidate/sample pages use credit:start-preview, which has no modal mechanism (GOSIGN-TESTS.md T2 note, 2026-11-16 ruling; KB-32)
  - [OPEN] T3 REAL FINDING on both pages: body text (headings, paragraphs, lists, table cells, labels) renders near-white rgb(254,254,254) on the pale pink --BG (244,240,240) background and is effectively unreadable (chromium 1366/375/320, webkit 1366/375 — section (e), theme item 2
  - [DISPOSITIONED] machine contrast warn min 1.06 corroborates — machine contrast value not confirmed as a defect by the T3 walk (KB-39: machine contrast warns include false positives on themed surfaces)
  - [OPEN] canonical source has no white body-text rule, not an intended aesthetic) — section (e) — part of the KB-28 item for this theme (the port’s binding, not an intended aesthetic)
  - [DISPOSITIONED] sidebar/credit/footer otherwise intact. — positive T3 assessment recorded in the row; no finding stands from this segment
- **theme:lead-by-example-jp** (RENDER-S2-F (CN8)):
  - [DISPOSITIONED] page runtime-hotlink site-theme chain only — environment-layer: runtime hosts arrive via the shared site theme chain, not the candidate (KB-40; RENDER-S2-G cross-cutting 1)
  - [DISPOSITIONED] sample credit-modal (preview-form) + runtime-hotlink site-theme chain. — preview-form property: candidate/sample pages use credit:start-preview, which has no modal mechanism (GOSIGN-TESTS.md T2 note, 2026-11-16 ruling; KB-32)
- **theme:madoka-jp** (RENDER-S2-F (CN9)):
  - [DISPOSITIONED] page sidebar-unreachable (4 combos, ≤375) + runtime-hotlink site-theme chain — environment-layer: runtime hosts arrive via the shared site theme chain, not the candidate (KB-40; RENDER-S2-G cross-cutting 1)
  - [DISPOSITIONED] sample hidden-* cluster at 5 combos (the webkit-1366 capture carries an http.cat-only hotlink line = transient 503 — transient Wikidot 503 capture, not a result (KB-44)
  - [DISPOSITIONED] the remaining combos are recorded as-is) + credit-modal (preview-form) + sidebar-unreachable. — preview-form property: candidate/sample pages use credit:start-preview, which has no modal mechanism (GOSIGN-TESTS.md T2 note, 2026-11-16 ruling; KB-32)
- **theme:magazine-jp** (RENDER-S2-F (CN9)):
  - [DISPOSITIONED] page-overflow 1415px@1366 + 448px@320 + 525px@375 + 911–996px@768 + runtime-hotlink site-theme chain — environment-layer: runtime hosts arrive via the shared site theme chain, not the candidate (KB-40; RENDER-S2-G cross-cutting 1)
  - [DISPOSITIONED] sample T2 no machine verdict (exit 2, no summary). — coverage caveat: this run returned no machine verdict (render_check exit 2); not a theme defect — see (a)
- **theme:magicity-jp** (RERUN16 (CN9)):
  - [DISPOSITIONED] page `hidden-interwiki` (chromium 375/320, webkit 768/375/320), runtime-hotlink site-theme chain only — environment-layer: runtime hosts arrive via the shared site theme chain, not the candidate (KB-40; RENDER-S2-G cross-cutting 1)
  - [DISPOSITIONED] sample credit-modal (preview-form), `hidden-interwiki` (same 5 combos), `sidebar-not-opening` [webkit 768x1024] (machine line — preview-form property: candidate/sample pages use credit:start-preview, which has no modal mechanism (GOSIGN-TESTS.md T2 note, 2026-11-16 ruling; KB-32)
  - [DISPOSITIONED] T3: not reproduced in the webkit 768 sidebar screenshot, drawer open), runtime-hotlink site-theme chain + sample font host — environment-layer: runtime hosts arrive via the shared site theme chain, not the candidate (KB-40; RENDER-S2-G cross-cutting 1)
  - [OPEN] T3 REAL FINDING (sample): table-cell, blockquote and tab-panel body text renders near-black on dark navy panels (the classed-wrapper table cells, "7. 引用と区切り" quotes, "10. タブ" body) and is effectively unreadable at chromium 1366x768 — section (e), theme item 2
  - [DISPOSITIONED] page T3 clean (hamburger present both engines at ≤375, drawer opens) — positive T3 confirmation recorded in the row; no finding stands from this segment
  - [DISPOSITIONED] magicity.svg/shujia.png broken = deferred assets — missing/404 decorative assets are the owner-deferred hosting state, not theme defects (KB-58; LOCALIZE-S2-C checklist item 1, owner decision 2026-11-16)
  - [DISPOSITIONED] sample webkit 375/320 *-full.png missing (32767px cap). — screenshot ceiling: the capture is incomplete above 32767px, a measurement limit (KB-46)
- **theme:marchen-jp** (RERUN16 (CN9)):
  - [OPEN] page page-overflow 435px chromium / 436px webkit @320/375, runtime-hotlink site-theme chain + candidate-own cdn.jsdelivr.net (judgment-required), `sidebar-not-opening` [webkit 1366x768] — section (e)
  - [OPEN] sample credit-modal (preview-form), same page-overflow (sample T3: cross-cutting static-credit shape), same runtime-hotlink + sample font host, `sidebar-not-opening` [webkit 1366x768] — section (e)
  - [OPEN] T3 REAL FINDING on both pages: at webkit 1366x768 the hamburger open control is present but pressing it does not bring the sidebar on-screen, no drawer appears, whereas chromium shows the sidebar open at left (machine line corroborates) — section (e)
  - [DISPOSITIONED] mobile ≤375 hamburger opens in both engines — positive T3 assessment recorded in the row; no finding stands from this segment
  - [DISPOSITIONED] rate/credit/footer/license/JP font fine. — positive T3 assessment recorded in the row; no finding stands from this segment
- **theme:mox-jp** (RENDER-S2-F (CN9)):
  - [DISPOSITIONED] page sidebar-unreachable (4 combos) + runtime-hotlink site-theme chain — environment-layer: runtime hosts arrive via the shared site theme chain, not the candidate (KB-40; RENDER-S2-G cross-cutting 1)
  - [DISPOSITIONED] sample credit-modal (preview-form) + sidebar-unreachable (4 combos). — preview-form property: candidate/sample pages use credit:start-preview, which has no modal mechanism (GOSIGN-TESTS.md T2 note, 2026-11-16 ruling; KB-32)
- **theme:nameless-jp** (RENDER-S2-F (CN10)):
  - [DISPOSITIONED] page-overflow 344px@320 on page and sample — page-overflow in the recorded cross-cutting families: static credit replica fixed width at mobile widths (KB-33) / preview chrome (KB-34); the per-theme figures match the campaign-wide shapes
  - [DISPOSITIONED] candidate-own runtime hosts (fastly.jsdelivr.net, p.typekit.net / use.typekit.net, pokm.wdfiles.com, wanderers-library and scp-wiki-cn chains) recorded verbatim — candidate-own foreign delivery hosts: posting-time rewrite or original-state delivery class (T1 class (ii); KB-41/KB-54 family); the pages render styled today
  - [DISPOSITIONED] sample credit-modal (preview-form). — preview-form property: candidate/sample pages use credit:start-preview, which has no modal mechanism (GOSIGN-TESTS.md T2 note, 2026-11-16 ruling; KB-32)
- **theme:normal-jp** (RERUN16 (CN10)):
  - [DISPOSITIONED] page runtime-hotlink incl. candidate-own ah-sandbox.wdfiles.com, fontsapi.zeoseven.com, hormress.github.io (judgment-required) — candidate-own foreign/sandbox delivery hosts: posting-time rewrite or original-state delivery class (T1 class (ii); KB-41/KB-54 family). The pages render styled today; no error-box defect arises from these hosts
  - [DISPOSITIONED] sample credit-modal (preview-form), runtime-hotlink incl. the same candidate-own hosts + sample font host — preview-form property: candidate/sample pages use credit:start-preview, which has no modal mechanism (GOSIGN-TESTS.md T2 note, 2026-11-16 ruling; KB-32)
  - [DISPOSITIONED] no page-overflow on either page — page-overflow in the recorded cross-cutting families: static credit replica fixed width at mobile widths (KB-33) / preview chrome (KB-34); the per-theme figures match the campaign-wide shapes
  - [DISPOSITIONED] T3 clean on both pages (PC sidebar collapsed with the theme's own hamburger visible top-left — positive T3 assessment recorded in the row; no finding stands from this segment
  - [DISPOSITIONED] machine contrast warn is a false positive, dark text on light blue readable — machine contrast value not confirmed as a defect by the T3 walk (KB-39: machine contrast warns include false positives on themed surfaces)
  - [DISPOSITIONED] em overflow and hl-code overflow are intentional specimens) — intentional specimen shapes (KB-37)
  - [DISPOSITIONED] sample webkit 375/320 *-full.png missing (32767px cap). — screenshot ceiling: the capture is incomplete above 32767px, a measurement limit (KB-46)
- **theme:obflow-jp** (RENDER-S2-F (CN10)):
  - [DISPOSITIONED] page-overflow 323–325px@320 + runtime-hotlink site-theme chain — environment-layer: runtime hosts arrive via the shared site theme chain, not the candidate (KB-40; RENDER-S2-G cross-cutting 1)
  - [DISPOSITIONED] sample T2 no machine verdict (exit 2, no summary). — coverage caveat: this run returned no machine verdict (render_check exit 2); not a theme defect — see (a)
- **theme:oneiroi-west-jp** (RENDER-S2-F (CN10)):
  - [DISPOSITIONED] page runtime-hotlink site-theme chain only — environment-layer: runtime hosts arrive via the shared site theme chain, not the candidate (KB-40; RENDER-S2-G cross-cutting 1)
  - [DISPOSITIONED] sample credit-modal (preview-form) + 884px@768 overflow + candidate-side hosts kaktuskontainer.wdfiles.com, scpsandboxcn.wdfiles.com. — page-overflow in the recorded cross-cutting families: static credit replica fixed width at mobile widths (KB-33) / preview chrome (KB-34); the per-theme figures match the campaign-wide shapes
- **theme:opinions-broadcaster-jp** (RENDER-S2-F (CN10)):
  - [DISPOSITIONED] page sidebar-not-opening + candidate-own runtime hosts (cdn.jsdelivr.net, fontsapi.zeoseven.com, sigma9.scpwikicn.com, scp-wiki-cn / scpsandboxcn chains) recorded verbatim — single-engine or single-combo machine line, not confirmed by the T3 walk (KB-47 family: single-combo ORB/machine flakiness); where T3 checked the drawer it is recorded opening
  - [DISPOSITIONED] sample T2 no machine verdict (exit 2, no summary). — coverage caveat: this run returned no machine verdict (render_check exit 2); not a theme defect — see (a)
- **theme:parablue-jp** (RENDER-S2-F (CN11)):
  - [DISPOSITIONED] page-overflow 331px@320 (page) and 366–380px@320/375 (sample) — page-overflow in the recorded cross-cutting families: static credit replica fixed width at mobile widths (KB-33) / preview chrome (KB-34); the per-theme figures match the campaign-wide shapes
  - [DISPOSITIONED] page sidebar-not-opening — single-engine or single-combo machine line, not confirmed by the T3 walk (KB-47 family: single-combo ORB/machine flakiness); where T3 checked the drawer it is recorded opening
  - [DISPOSITIONED] runtime-hotlink incl. candidate host paraarc-sandbox.wikidot.com on both pages — candidate-own foreign/sandbox delivery hosts: posting-time rewrite or original-state delivery class (T1 class (ii); KB-41/KB-54 family). The pages render styled today; no error-box defect arises from these hosts
  - [DISPOSITIONED] sample credit-modal (preview-form). — preview-form property: candidate/sample pages use credit:start-preview, which has no modal mechanism (GOSIGN-TESTS.md T2 note, 2026-11-16 ruling; KB-32)
- **theme:paradigm-inapplicable-jp** (RENDER-S2-F (CN11)):
  - [DISPOSITIONED] page-overflow 996–999px@320/375 + 1018px@768 (page) and 581–584px@320/375 + 996–1018px (sample) — page-overflow in the recorded cross-cutting families: static credit replica fixed width at mobile widths (KB-33) / preview chrome (KB-34); the per-theme figures match the campaign-wide shapes
  - [DISPOSITIONED] sample credit-modal (preview-form). — preview-form property: candidate/sample pages use credit:start-preview, which has no modal mechanism (GOSIGN-TESTS.md T2 note, 2026-11-16 ruling; KB-32)
- **theme:paradigm-inapplicable-sigma-jp** (RENDER-S2-F (CN11)):
  - [DISPOSITIONED] page-overflow 332px@320 + 387px@375 (page) and 337px@320 + 387px@375 (sample) — page-overflow in the recorded cross-cutting families: static credit replica fixed width at mobile widths (KB-33) / preview chrome (KB-34); the per-theme figures match the campaign-wide shapes
  - [DISPOSITIONED] sample credit-modal (preview-form). — preview-form property: candidate/sample pages use credit:start-preview, which has no modal mechanism (GOSIGN-TESTS.md T2 note, 2026-11-16 ruling; KB-32)
- **theme:paradigm-reconstruction-jp** (RENDER-S2-F (CN11)):
  - [DISPOSITIONED] page-overflow 996–999px@320/375 + 1018px@768 (page) and 581–584px@320/375 + 996–1018px (sample) — page-overflow in the recorded cross-cutting families: static credit replica fixed width at mobile widths (KB-33) / preview chrome (KB-34); the per-theme figures match the campaign-wide shapes
  - [DISPOSITIONED] sample credit-modal (preview-form). — preview-form property: candidate/sample pages use credit:start-preview, which has no modal mechanism (GOSIGN-TESTS.md T2 note, 2026-11-16 ruling; KB-32)
- **theme:parallel-jp** (RENDER-S2-F (CN11)):
  - [DISPOSITIONED] page-overflow 502–506px@320/375 + runtime-hotlink site-theme chain — environment-layer: runtime hosts arrive via the shared site theme chain, not the candidate (KB-40; RENDER-S2-G cross-cutting 1)
  - [DISPOSITIONED] sample T2 no machine verdict (exit 2, no summary). — coverage caveat: this run returned no machine verdict (render_check exit 2); not a theme defect — see (a)
- **theme:peroxide-jp** (RENDER-S2-F (CN12)):
  - [DISPOSITIONED] page-overflow 360–366px@320 + sidebar-unreachable (4 combos) + runtime-hotlink site-theme chain — environment-layer: runtime hosts arrive via the shared site theme chain, not the candidate (KB-40; RENDER-S2-G cross-cutting 1)
  - [DISPOSITIONED] sample T2 no machine verdict (exit 2, no summary). — coverage caveat: this run returned no machine verdict (render_check exit 2); not a theme defect — see (a)
- **theme:petrifaction-jp** (RENDER-S2-F (CN12)):
  - [DISPOSITIONED] hidden-login (4 combos) on page and sample + runtime-hotlink site-theme chain — environment-layer: runtime hosts arrive via the shared site theme chain, not the candidate (KB-40; RENDER-S2-G cross-cutting 1)
  - [DISPOSITIONED] sample credit-modal (preview-form) + page-overflow 332–335px@320. — page-overflow in the recorded cross-cutting families: static credit replica fixed width at mobile widths (KB-33) / preview chrome (KB-34); the per-theme figures match the campaign-wide shapes
- **theme:progress-institute-jp** (RENDER-S2-F (CN12)):
  - [DISPOSITIONED] page T2 no machine verdict (exit 2, no summary) — coverage caveat: this run returned no machine verdict (render_check exit 2); not a theme defect — see (a)
  - [DISPOSITIONED] sample credit-modal (preview-form) + page-overflow 337–419px@320/375. — page-overflow in the recorded cross-cutting families: static credit replica fixed width at mobile widths (KB-33) / preview chrome (KB-34); the per-theme figures match the campaign-wide shapes
- **theme:redsquare-jp** (RENDER-S2-F (CN12)):
  - [DISPOSITIONED] page runtime-hotlink site-theme chain only — environment-layer: runtime hosts arrive via the shared site theme chain, not the candidate (KB-40; RENDER-S2-G cross-cutting 1)
  - [DISPOSITIONED] sample credit-modal (preview-form) + 884px@768 overflow + candidate-side host lestday-lab.wdfiles.com. — page-overflow in the recorded cross-cutting families: static credit replica fixed width at mobile widths (KB-33) / preview chrome (KB-34); the per-theme figures match the campaign-wide shapes
- **theme:rima-jp** (RENDER-S2-F (CN12)):
  - [OPEN] page-overflow 325px@320 + sidebar-unreachable (4 combos) + candidate-own runtime hosts (cdn.mer.run, oxygennine.wdfiles.com / oxygennine.wikidot.com, scpsandboxcn chain) recorded verbatim — section (e), theme item 2
  - [DISPOSITIONED] sample T2 no machine verdict (exit 2, no summary). — coverage caveat: this run returned no machine verdict (render_check exit 2); not a theme defect — see (a)
- **theme:sci-fi-jp** (RENDER-S2-G (CN13)):
  - [DISPOSITIONED] page-overflow 452–471px@320/375 + 771px@768 (both engines) + runtime-hotlink site-theme chain — environment-layer: runtime hosts arrive via the shared site theme chain, not the candidate (KB-40; RENDER-S2-G cross-cutting 1)
  - [DISPOSITIONED] sample credit-modal (preview-form) + page-overflow incl. 884px@768 — page-overflow in the recorded cross-cutting families: static credit replica fixed width at mobile widths (KB-33) / preview chrome (KB-34); the per-theme figures match the campaign-wide shapes
  - [DISPOSITIONED] T3 .open-menu toggle overlaps code text at ≤375 on both pages — the mobile menu button is the shared site-theme element; its overlap at <=375px is the mobile chrome family (KB-34/KB-35 family), not theme-authored content
  - [DISPOSITIONED] full-engine (chromium+webkit) coverage. — coverage statement for this theme (see (a) caveats); not a finding
- **theme:scpdeclassified-jp** (RENDER-S2-G (CN13)):
  - [DISPOSITIONED] page runtime-hotlink site-theme chain only — environment-layer: runtime hosts arrive via the shared site theme chain, not the candidate (KB-40; RENDER-S2-G cross-cutting 1)
  - [DISPOSITIONED] sample credit-modal (preview-form) + page-overflow 333px@320 + 851px@768 (one sample hotlink line also lists http.cat among other hosts, no hidden-* cluster) — page-overflow in the recorded cross-cutting families: static credit replica fixed width at mobile widths (KB-33) / preview chrome (KB-34); the per-theme figures match the campaign-wide shapes
  - [DISPOSITIONED] T3 .open-menu toggle overlaps body text at ≤375 on both pages, webkit-768 sample render unstyled from a transient 503 (not theme) — transient Wikidot 503 capture, not a result (KB-44)
  - [DISPOSITIONED] full-engine coverage. — coverage statement for this theme (see (a) caveats); not a finding
- **theme:scplive-jp** (RENDER-S2-G (CN13)):
  - [DISPOSITIONED] page runtime-hotlink site-theme chain only — environment-layer: runtime hosts arrive via the shared site theme chain, not the candidate (KB-40; RENDER-S2-G cross-cutting 1)
  - [DISPOSITIONED] sample credit-modal (preview-form) + page-overflow 884px@768 — page-overflow in the recorded cross-cutting families: static credit replica fixed width at mobile widths (KB-33) / preview chrome (KB-34); the per-theme figures match the campaign-wide shapes
  - [DISPOSITIONED] T3 none seen, no candidate-specific visual defect — the row’s own closing assessment: no candidate defect stands from this segment
  - [DISPOSITIONED] broken board.png (deferred asset) — missing/404 decorative assets are the owner-deferred hosting state, not theme defects (KB-58; LOCALIZE-S2-C checklist item 1, owner decision 2026-11-16)
  - [DISPOSITIONED] full-engine coverage. — coverage statement for this theme (see (a) caveats); not a finding
- **theme:shancheng-jp** (RENDER-S2-G (CN13)):
  - [DISPOSITIONED] page-overflow 505–519px@≤375 + 854–859px@768 (page) and 517–531px@≤375 + 951px@768 (sample), both engines, + runtime-hotlink site-theme chain — environment-layer: runtime hosts arrive via the shared site theme chain, not the candidate (KB-40; RENDER-S2-G cross-cutting 1)
  - [DISPOSITIONED] sample credit-modal (preview-form) — preview-form property: candidate/sample pages use credit:start-preview, which has no modal mechanism (GOSIGN-TESTS.md T2 note, 2026-11-16 ruling; KB-32)
  - [DISPOSITIONED] T3 page overflow confirmed, decorative images 404 (deferred) — positive T3 confirmation recorded in the row; no finding stands from this segment
  - [DISPOSITIONED] full-engine coverage (sample via the full-engine re-run, over-ceiling WebKit full-page screenshots skipped). — coverage statement for this theme (see (a) caveats); not a finding
- **theme:share-future-community-jp** (RENDER-S2-G (CN13)):
  - [DISPOSITIONED] page-overflow 505–507px@≤375 (page) and 517–519px@≤375 + 881px@768 (sample), both engines, + runtime-hotlink site-theme chain + candidate host hoah.backroomswiki.cn (judgment-required) — environment-layer: runtime hosts arrive via the shared site theme chain, not the candidate (KB-40; RENDER-S2-G cross-cutting 1)
  - [DISPOSITIONED] sample credit-modal (preview-form) — preview-form property: candidate/sample pages use credit:start-preview, which has no modal mechanism (GOSIGN-TESTS.md T2 note, 2026-11-16 ruling; KB-32)
  - [DISPOSITIONED] T3 page overflow confirmed, penumbra-tb.png 404 (deferred) — positive T3 confirmation recorded in the row; no finding stands from this segment
  - [DISPOSITIONED] full-engine coverage (sample via the full-engine re-run, over-ceiling WebKit full-page screenshots skipped). — coverage statement for this theme (see (a) caveats); not a finding
- **theme:shivering-night-jp** (RENDER-S2-G (CN14)):
  - [DISPOSITIONED] hidden-login (chromium 1366/768) on page and sample + runtime-hotlink site-theme chain — environment-layer: runtime hosts arrive via the shared site theme chain, not the candidate (KB-40; RENDER-S2-G cross-cutting 1)
  - [DISPOSITIONED] sample credit-modal (preview-form) — preview-form property: candidate/sample pages use credit:start-preview, which has no modal mechanism (GOSIGN-TESTS.md T2 note, 2026-11-16 ruling; KB-32)
  - [DISPOSITIONED] T3 re-run, no new screenshot-grounded visual finding — the re-run T3 walk recorded no new visual finding for this theme
  - [DISPOSITIONED] chromium-only coverage (no WebKit verdict). — coverage statement for this theme (see (a) caveats); not a finding
- **theme:sodium-jp** (RENDER-S2-G (CN14)):
  - [DISPOSITIONED] hidden-login (desktop, both engines) on page and sample + runtime-hotlink site-theme chain — environment-layer: runtime hosts arrive via the shared site theme chain, not the candidate (KB-40; RENDER-S2-G cross-cutting 1)
  - [DISPOSITIONED] sample credit-modal (preview-form) — preview-form property: candidate/sample pages use credit:start-preview, which has no modal mechanism (GOSIGN-TESTS.md T2 note, 2026-11-16 ruling; KB-32)
  - [OPEN] T3 login-state absence confirmed, rating clear-vote × near-white on white effectively invisible — section (e), theme item 3
  - [DISPOSITIONED] full-engine coverage. — coverage statement for this theme (see (a) caveats); not a finding
- **theme:sodium-pentasulfide-jp** (RENDER-S2-G (CN14)):
  - [DISPOSITIONED] page runtime-hotlink site-theme chain only — environment-layer: runtime hosts arrive via the shared site theme chain, not the candidate (KB-40; RENDER-S2-G cross-cutting 1)
  - [DISPOSITIONED] sample credit-modal (preview-form) + page-overflow 331px@320 + 909px@768 — page-overflow in the recorded cross-cutting families: static credit replica fixed width at mobile widths (KB-33) / preview chrome (KB-34); the per-theme figures match the campaign-wide shapes
  - [DISPOSITIONED] T3 re-run, no new screenshot-grounded visual finding — the re-run T3 walk recorded no new visual finding for this theme
  - [DISPOSITIONED] chromium-only coverage (no WebKit verdict). — coverage statement for this theme (see (a) caveats); not a finding
- **theme:sound-jp** (RENDER-S2-G (CN14)):
  - [OPEN] sidebar-unreachable at 375/320 (both engines) on page and sample + runtime-hotlink site-theme chain — section (e), theme item 4
  - [DISPOSITIONED] sample credit-modal (preview-form) — preview-form property: candidate/sample pages use credit:start-preview, which has no modal mechanism (GOSIGN-TESTS.md T2 note, 2026-11-16 ruling; KB-32)
  - [OPEN] T3 missing mobile sidebar toggle confirmed, sample §15/§16 panels near-white on light effectively unreadable — section (e), theme item 5
  - [DISPOSITIONED] full-engine coverage. — coverage statement for this theme (see (a) caveats); not a finding
- **theme:starbasalt-jp** (RENDER-S2-G (CN14)):
  - [DISPOSITIONED] hidden-rate on all combos on both pages (T3: script false positive, rate widget visible) + page-overflow at every viewport (437–506px mobile — page-overflow in the recorded cross-cutting families: static credit replica fixed width at mobile widths (KB-33) / preview chrome (KB-34); the per-theme figures match the campaign-wide shapes
  - [DISPOSITIONED] sample 1489px@1366) + runtime-hotlink site-theme chain + candidate cdn.jsdelivr.net (one sample hotlink line also lists http.cat among other hosts, no hidden-* cluster) — candidate-own foreign/sandbox delivery hosts: posting-time rewrite or original-state delivery class (T1 class (ii); KB-41/KB-54 family). The pages render styled today; no error-box defect arises from these hosts
  - [DISPOSITIONED] sample carries NO credit-modal machine line (T3: modal N/A, preview form) — preview-form property: candidate/sample pages use credit:start-preview, which has no modal mechanism (GOSIGN-TESTS.md T2 note, 2026-11-16 ruling; KB-32)
  - [OPEN] T3 sample §15 content panels unstyled plain text on black — section (e)
  - [DISPOSITIONED] full-engine coverage. — coverage statement for this theme (see (a) caveats); not a finding
- **theme:starry-jp** (RENDER-S2-G (CN15)):
  - [DISPOSITIONED] page sidebar-unreachable at 375/320 (both engines) + runtime-hotlink site-theme chain + candidate hosts oxygennine.wdfiles.com, scpsandboxcn.wdfiles.com, stsandbox.wdfiles.com — candidate-own foreign/sandbox delivery hosts: posting-time rewrite or original-state delivery class (T1 class (ii); KB-41/KB-54 family). The pages render styled today; no error-box defect arises from these hosts
  - [DISPOSITIONED] sample credit-modal (preview-form) + sidebar-unreachable (chromium 375/320) — preview-form property: candidate/sample pages use credit:start-preview, which has no modal mechanism (GOSIGN-TESTS.md T2 note, 2026-11-16 ruling; KB-32)
  - [DISPOSITIONED] T3 page not separately walked, no additional visual finding — the re-run T3 walk recorded no new visual finding for this theme
  - [DISPOSITIONED] mixed coverage: page full-engine, sample chromium-only (no WebKit verdict). — coverage statement for this theme (see (a) caveats); not a finding
- **theme:steam-guide-jp** (RENDER-S2-G (CN15)):
  - [DISPOSITIONED] page-overflow 371–372px@320 (both engines) + runtime-hotlink site-theme chain + candidate cdn.jsdelivr.net — candidate-own foreign/sandbox delivery hosts: posting-time rewrite or original-state delivery class (T1 class (ii); KB-41/KB-54 family). The pages render styled today; no error-box defect arises from these hosts
  - [DISPOSITIONED] sample credit-modal (preview-form) + page-overflow 371px@320 — page-overflow in the recorded cross-cutting families: static credit replica fixed width at mobile widths (KB-33) / preview chrome (KB-34); the per-theme figures match the campaign-wide shapes
  - [DISPOSITIONED] T3 page not separately walked, no additional visual finding — the re-run T3 walk recorded no new visual finding for this theme
  - [DISPOSITIONED] mixed coverage: page full-engine, sample chromium-only (no WebKit verdict). — coverage statement for this theme (see (a) caveats); not a finding
- **theme:supply-n-demand-jp** (RENDER-S2-G (CN15)):
  - [DISPOSITIONED] page-overflow 507px@320/375 (page) and 519px@320/375 (sample) + runtime-hotlink site-theme chain + candidate hosts cdn.jsdmirror.com, cdn.scpwiki.com, scp-wiki-cdn.nyc3.cdn.digitaloceanspaces.com — environment-layer: runtime hosts arrive via the shared site theme chain, not the candidate (KB-40; RENDER-S2-G cross-cutting 1)
  - [DISPOSITIONED] sample credit-modal (preview-form) — preview-form property: candidate/sample pages use credit:start-preview, which has no modal mechanism (GOSIGN-TESTS.md T2 note, 2026-11-16 ruling; KB-32)
  - [DISPOSITIONED] T3 re-run, no new screenshot-grounded visual finding — the re-run T3 walk recorded no new visual finding for this theme
  - [DISPOSITIONED] chromium-only coverage (no WebKit verdict). — coverage statement for this theme (see (a) caveats); not a finding
- **theme:suprematism-jp** (RENDER-S2-G (CN15)):
  - [DISPOSITIONED] page-overflow 454px@320/375 on page and sample + sidebar-unreachable at 375/320 + runtime-hotlink site-theme chain + candidate hosts cdn.jsdelivr.net, lemoncat233.github.io, nu-scptheme.github.io — candidate-own foreign/sandbox delivery hosts: posting-time rewrite or original-state delivery class (T1 class (ii); KB-41/KB-54 family). The pages render styled today; no error-box defect arises from these hosts
  - [DISPOSITIONED] sample credit-modal (preview-form) — preview-form property: candidate/sample pages use credit:start-preview, which has no modal mechanism (GOSIGN-TESTS.md T2 note, 2026-11-16 ruling; KB-32)
  - [DISPOSITIONED] T3 re-run, no new screenshot-grounded visual finding — the re-run T3 walk recorded no new visual finding for this theme
  - [DISPOSITIONED] chromium-only coverage (no WebKit verdict). — coverage statement for this theme (see (a) caveats); not a finding
- **theme:tfnac-jp** (RENDER-S2-G (CN15)):
  - [DISPOSITIONED] page-overflow 507px@320/375 + 782px@768 (page) and 519px@320/375 + 883px@768 (sample) + runtime-hotlink site-theme chain + candidate hosts nu-scptheme.github.io, s1.ax1x.com — candidate-own foreign/sandbox delivery hosts: posting-time rewrite or original-state delivery class (T1 class (ii); KB-41/KB-54 family). The pages render styled today; no error-box defect arises from these hosts
  - [DISPOSITIONED] sample credit-modal (preview-form) — preview-form property: candidate/sample pages use credit:start-preview, which has no modal mechanism (GOSIGN-TESTS.md T2 note, 2026-11-16 ruling; KB-32)
  - [DISPOSITIONED] T3 re-run, no new screenshot-grounded visual finding — the re-run T3 walk recorded no new visual finding for this theme
  - [DISPOSITIONED] chromium-only coverage (no WebKit verdict). — coverage statement for this theme (see (a) caveats); not a finding
- **theme:the-other-side-jp** (RENDER-S2-G (CN16)):
  - [DISPOSITIONED] page-overflow 325px@320 on page and sample (+ 884px@768 on sample) + runtime-hotlink site-theme chain — environment-layer: runtime hosts arrive via the shared site theme chain, not the candidate (KB-40; RENDER-S2-G cross-cutting 1)
  - [DISPOSITIONED] sample credit-modal (preview-form) — preview-form property: candidate/sample pages use credit:start-preview, which has no modal mechanism (GOSIGN-TESTS.md T2 note, 2026-11-16 ruling; KB-32)
  - [DISPOSITIONED] T3 re-run, no new screenshot-grounded visual finding — the re-run T3 walk recorded no new visual finding for this theme
  - [DISPOSITIONED] chromium-only coverage (no WebKit verdict). — coverage statement for this theme (see (a) caveats); not a finding
- **theme:the-track-changers-jp** (RENDER-S2-G (CN16)):
  - [DISPOSITIONED] sidebar-unreachable at 375/320 on page and sample + runtime-hotlink site-theme chain + candidate fastly.jsdelivr.net — candidate-own foreign/sandbox delivery hosts: posting-time rewrite or original-state delivery class (T1 class (ii); KB-41/KB-54 family). The pages render styled today; no error-box defect arises from these hosts
  - [DISPOSITIONED] sample credit-modal (preview-form) — preview-form property: candidate/sample pages use credit:start-preview, which has no modal mechanism (GOSIGN-TESTS.md T2 note, 2026-11-16 ruling; KB-32)
  - [DISPOSITIONED] T3 re-run, no new screenshot-grounded visual finding — the re-run T3 walk recorded no new visual finding for this theme
  - [DISPOSITIONED] chromium-only coverage (no WebKit verdict). — coverage statement for this theme (see (a) caveats); not a finding
- **theme:trauma-jp** (RENDER-S2-G (CN16)):
  - [DISPOSITIONED] page-overflow 517–520px@≤375 + 831px@768 (page) and 530–533px@≤375 + 831px@768 (sample) + runtime-hotlink site-theme chain + candidate hosts cdn.jsdelivr.net, lemoncat233.github.io — candidate-own foreign/sandbox delivery hosts: posting-time rewrite or original-state delivery class (T1 class (ii); KB-41/KB-54 family). The pages render styled today; no error-box defect arises from these hosts
  - [DISPOSITIONED] sample credit-modal (preview-form) — preview-form property: candidate/sample pages use credit:start-preview, which has no modal mechanism (GOSIGN-TESTS.md T2 note, 2026-11-16 ruling; KB-32)
  - [DISPOSITIONED] T3 re-run, no new screenshot-grounded visual finding — the re-run T3 walk recorded no new visual finding for this theme
  - [DISPOSITIONED] chromium-only coverage (no WebKit verdict). — coverage statement for this theme (see (a) caveats); not a finding
- **theme:travellers-book-jp** (RENDER-S2-G (CN16)):
  - [DISPOSITIONED] page runtime-hotlink site-theme chain only — environment-layer: runtime hosts arrive via the shared site theme chain, not the candidate (KB-40; RENDER-S2-G cross-cutting 1)
  - [DISPOSITIONED] sample credit-modal (preview-form) + page-overflow 323px@320 + 960px@768 — page-overflow in the recorded cross-cutting families: static credit replica fixed width at mobile widths (KB-33) / preview chrome (KB-34); the per-theme figures match the campaign-wide shapes
  - [DISPOSITIONED] T3 re-run, no new screenshot-grounded visual finding — the re-run T3 walk recorded no new visual finding for this theme
  - [DISPOSITIONED] chromium-only coverage (no WebKit verdict). — coverage statement for this theme (see (a) caveats); not a finding
- **theme:ultimate-reader-jp** (RENDER-S2-G (CN16)):
  - [DISPOSITIONED] page-overflow 778px at 320/375/768 (page) and 790px at 320/375/768 (sample) + runtime-hotlink site-theme chain — environment-layer: runtime hosts arrive via the shared site theme chain, not the candidate (KB-40; RENDER-S2-G cross-cutting 1)
  - [DISPOSITIONED] sample credit-modal (preview-form) — preview-form property: candidate/sample pages use credit:start-preview, which has no modal mechanism (GOSIGN-TESTS.md T2 note, 2026-11-16 ruling; KB-32)
  - [DISPOSITIONED] T3 re-run, no new screenshot-grounded visual finding — the re-run T3 walk recorded no new visual finding for this theme
  - [DISPOSITIONED] chromium-only coverage (no WebKit verdict). — coverage statement for this theme (see (a) caveats); not a finding
- **theme:voyager-jp** (RENDER-S2-G (CN17)):
  - [DISPOSITIONED] hidden-login (chromium 1366/768) on page and sample + runtime-hotlink site-theme chain + host scp-wiki-cn.wdfiles.com (named verbatim, judgment-required) — environment-layer: runtime hosts arrive via the shared site theme chain, not the candidate (KB-40; RENDER-S2-G cross-cutting 1)
  - [DISPOSITIONED] sample credit-modal (preview-form) — preview-form property: candidate/sample pages use credit:start-preview, which has no modal mechanism (GOSIGN-TESTS.md T2 note, 2026-11-16 ruling; KB-32)
  - [DISPOSITIONED] T3 re-run, no new screenshot-grounded visual finding — the re-run T3 walk recorded no new visual finding for this theme
  - [DISPOSITIONED] chromium-only coverage (no WebKit verdict). — coverage statement for this theme (see (a) caveats); not a finding
- **theme:walk-in-the-dark-jp** (RENDER-S2-G (CN17)):
  - [DISPOSITIONED] page-overflow 350px@320 + 382px@375 + 814px@768 (page — page-overflow in the recorded cross-cutting families: static credit replica fixed width at mobile widths (KB-33) / preview chrome (KB-34); the per-theme figures match the campaign-wide shapes
  - [DISPOSITIONED] sample 884px@768) + runtime-hotlink site-theme chain + candidate hosts fastly.jsdelivr.net, scp-wiki-cn.wdfiles.com — candidate-own foreign/sandbox delivery hosts: posting-time rewrite or original-state delivery class (T1 class (ii); KB-41/KB-54 family). The pages render styled today; no error-box defect arises from these hosts
  - [DISPOSITIONED] sample credit-modal (preview-form) — preview-form property: candidate/sample pages use credit:start-preview, which has no modal mechanism (GOSIGN-TESTS.md T2 note, 2026-11-16 ruling; KB-32)
  - [DISPOSITIONED] T3 re-run, no new screenshot-grounded visual finding — the re-run T3 walk recorded no new visual finding for this theme
  - [DISPOSITIONED] chromium-only coverage (no WebKit verdict). — coverage statement for this theme (see (a) caveats); not a finding
- **theme:waxed-oxidized-cut-copper-slab-jp** (RENDER-S2-G (CN17)):
  - [DISPOSITIONED] page-overflow 445px@320/375 on page and sample + runtime-hotlink site-theme chain + candidate hosts ah-sandbox.wdfiles.com, ah-sandbox.wikidot.com, bhl.scpwikicn.com, hormress.github.io, nu-scptheme.github.io, scp-wiki.wikidot.com — candidate-own foreign/sandbox delivery hosts: posting-time rewrite or original-state delivery class (T1 class (ii); KB-41/KB-54 family). The pages render styled today; no error-box defect arises from these hosts
  - [DISPOSITIONED] sample credit-modal (preview-form) — preview-form property: candidate/sample pages use credit:start-preview, which has no modal mechanism (GOSIGN-TESTS.md T2 note, 2026-11-16 ruling; KB-32)
  - [DISPOSITIONED] T3 re-run, no new screenshot-grounded visual finding — the re-run T3 walk recorded no new visual finding for this theme
  - [DISPOSITIONED] chromium-only coverage (no WebKit verdict). — coverage statement for this theme (see (a) caveats); not a finding
- **theme:winddew-in-hand-jp** (RENDER-S2-G (CN17)):
  - [DISPOSITIONED] page runtime-hotlink site-theme chain + candidate hosts scpsandboxcn.wdfiles.com, scpsandboxcn.wikidot.com, scptestwiki.wdfiles.com — candidate-own foreign/sandbox delivery hosts: posting-time rewrite or original-state delivery class (T1 class (ii); KB-41/KB-54 family). The pages render styled today; no error-box defect arises from these hosts
  - [DISPOSITIONED] sample credit-modal (preview-form) + page-overflow 884px@768 — page-overflow in the recorded cross-cutting families: static credit replica fixed width at mobile widths (KB-33) / preview chrome (KB-34); the per-theme figures match the campaign-wide shapes
  - [DISPOSITIONED] T3 re-run, no new screenshot-grounded visual finding — the re-run T3 walk recorded no new visual finding for this theme
  - [DISPOSITIONED] chromium-only coverage (no WebKit verdict). — coverage statement for this theme (see (a) caveats); not a finding
- **theme:winxp-jp** (RENDER-S2-G (CN17)):
  - [DISPOSITIONED] page runtime-hotlink site-theme chain + candidate hosts scpsandboxcn.wdfiles.com, scpsandboxcn.wikidot.com — candidate-own foreign/sandbox delivery hosts: posting-time rewrite or original-state delivery class (T1 class (ii); KB-41/KB-54 family). The pages render styled today; no error-box defect arises from these hosts
  - [DISPOSITIONED] sample credit-modal (preview-form) + runtime-hotlink incl. scp-wiki-cn.wdfiles.com — preview-form property: candidate/sample pages use credit:start-preview, which has no modal mechanism (GOSIGN-TESTS.md T2 note, 2026-11-16 ruling; KB-32)
  - [DISPOSITIONED] T3 re-run, no new screenshot-grounded visual finding — the re-run T3 walk recorded no new visual finding for this theme
  - [DISPOSITIONED] chromium-only coverage (no WebKit verdict). — coverage statement for this theme (see (a) caveats); not a finding
- **theme:wish-for-miracle-jp** (RENDER-S2-G (CN18)):
  - [DISPOSITIONED] page-overflow 579px@320/375 on page and sample + sidebar-unreachable at 375/320 on both pages + runtime-hotlink site-theme chain + candidate hosts cdn.jsdelivr.net, uploadfile.wdfiles.com, uploadfile.wikidot.com — candidate-own foreign/sandbox delivery hosts: posting-time rewrite or original-state delivery class (T1 class (ii); KB-41/KB-54 family). The pages render styled today; no error-box defect arises from these hosts
  - [DISPOSITIONED] sample carries NO credit-modal machine line and the report verdict likewise omits it (recorded as-is, unlike the other samples) — preview-form property: candidate/sample pages use credit:start-preview, which has no modal mechanism (GOSIGN-TESTS.md T2 note, 2026-11-16 ruling; KB-32)
  - [DISPOSITIONED] T3 re-run, no new screenshot-grounded visual finding — the re-run T3 walk recorded no new visual finding for this theme
  - [DISPOSITIONED] chromium-only coverage (no WebKit verdict). — coverage statement for this theme (see (a) caveats); not a finding
- **theme:yore-jp** (RENDER-S2-G (CN18)):
  - [DISPOSITIONED] page-overflow 513px@320/375 on page and sample (+ 899px@768 on sample) + sidebar-unreachable at 375/320 on both pages + runtime-hotlink site-theme chain + candidate hosts ah-sandbox.wdfiles.com, ah-sandbox.wikidot.com, hormress.github.io, scpsandboxcn.wdfiles.com — candidate-own foreign/sandbox delivery hosts: posting-time rewrite or original-state delivery class (T1 class (ii); KB-41/KB-54 family). The pages render styled today; no error-box defect arises from these hosts
  - [DISPOSITIONED] sample credit-modal (preview-form) — preview-form property: candidate/sample pages use credit:start-preview, which has no modal mechanism (GOSIGN-TESTS.md T2 note, 2026-11-16 ruling; KB-32)
  - [DISPOSITIONED] T3 re-run, no new screenshot-grounded visual finding — the re-run T3 walk recorded no new visual finding for this theme
  - [DISPOSITIONED] chromium-only coverage (no WebKit verdict). — coverage statement for this theme (see (a) caveats); not a finding
- **theme:07k-jp** (RENDER-S2-H (KO1)):
  - [DISPOSITIONED] page runtime-hotlink site-theme chain + scpko.wdfiles.com — candidate-own foreign/sandbox delivery hosts: posting-time rewrite or original-state delivery class (T1 class (ii); KB-41/KB-54 family). The pages render styled today; no error-box defect arises from these hosts
  - [DISPOSITIONED] sample credit-modal (preview-form) + runtime-hotlink — preview-form property: candidate/sample pages use credit:start-preview, which has no modal mechanism (GOSIGN-TESTS.md T2 note, 2026-11-16 ruling; KB-32)
  - [DISPOSITIONED] T3 none beyond cross-cutting items. All 78 H targets produced a summary.md (no exit-2 incompleteness in this lane). — recorded by the lane as cross-cutting (the campaign-wide shapes of register c2’s class entries)
- **theme:a-midnight-invitation-jp** (RENDER-S2-H (KO1)):
  - [DISPOSITIONED] sample credit-modal (preview-form) + page-overflow 324px@320 + 884px@768 — page-overflow in the recorded cross-cutting families: static credit replica fixed width at mobile widths (KB-33) / preview chrome (KB-34); the per-theme figures match the campaign-wide shapes
  - [OPEN] T3 stock-header SCP財団 wordmark and nav render in very light gray on near-white at all 8 viewports, nearly illegible (theme-specific, §1 contrast). — section (e), theme item 4
- **theme:animal-instead-of-beast-jp** (RENDER-S2-H (KO1)):
  - [DISPOSITIONED] runtime-hotlink site-theme chain + scpko.wdfiles.com / scpko.wikidot.com on both pages — candidate-own foreign/sandbox delivery hosts: posting-time rewrite or original-state delivery class (T1 class (ii); KB-41/KB-54 family). The pages render styled today; no error-box defect arises from these hosts
  - [DISPOSITIONED] sample credit-modal (preview-form) + 884px@768 overflow — page-overflow in the recorded cross-cutting families: static credit replica fixed width at mobile widths (KB-33) / preview chrome (KB-34); the per-theme figures match the campaign-wide shapes
  - [OPEN] T3 header wordmark faint gray-on-white (machine contrast 1.03). — section (e), theme item 5
- **theme:anniversary-jp** (RENDER-S2-H (KO1)):
  - [DISPOSITIONED] page runtime-hotlink site-theme chain only — environment-layer: runtime hosts arrive via the shared site theme chain, not the candidate (KB-40; RENDER-S2-G cross-cutting 1)
  - [DISPOSITIONED] sample credit-modal (preview-form) + 884px@768 overflow — page-overflow in the recorded cross-cutting families: static credit replica fixed width at mobile widths (KB-33) / preview chrome (KB-34); the per-theme figures match the campaign-wide shapes
  - [DISPOSITIONED] T3 none beyond cross-cutting items. — recorded by the lane as cross-cutting (the campaign-wide shapes of register c2’s class entries)
- **theme:atlas-maniacus-jp** (RENDER-S2-H (KO1)):
  - [DISPOSITIONED] page runtime-hotlink site-theme chain only — environment-layer: runtime hosts arrive via the shared site theme chain, not the candidate (KB-40; RENDER-S2-G cross-cutting 1)
  - [DISPOSITIONED] sample credit-modal (preview-form) + runtime-hotlink — preview-form property: candidate/sample pages use credit:start-preview, which has no modal mechanism (GOSIGN-TESTS.md T2 note, 2026-11-16 ruling; KB-32)
  - [DISPOSITIONED] T3 none beyond cross-cutting items. — recorded by the lane as cross-cutting (the campaign-wide shapes of register c2’s class entries)
- **theme:back-jan-fire-jp** (RENDER-S2-H (KO2)):
  - [DISPOSITIONED] runtime-hotlink site-theme chain + scpko.wdfiles.com / scpko.wikidot.com on both pages — candidate-own foreign/sandbox delivery hosts: posting-time rewrite or original-state delivery class (T1 class (ii); KB-41/KB-54 family). The pages render styled today; no error-box defect arises from these hosts
  - [DISPOSITIONED] sample credit-modal (preview-form) + 884px@768 overflow — page-overflow in the recorded cross-cutting families: static credit replica fixed width at mobile widths (KB-33) / preview chrome (KB-34); the per-theme figures match the campaign-wide shapes
  - [DISPOSITIONED] T3 none beyond cross-cutting items. — recorded by the lane as cross-cutting (the campaign-wide shapes of register c2’s class entries)
- **theme:bulgunae-jp** (RENDER-S2-H (KO2)):
  - [DISPOSITIONED] page sidebar-not-opening + candidate-own runtime hosts (nu-scptheme.github.io, scp-wiki.wikidot.com / www.scp-wiki.net) recorded verbatim — single-engine or single-combo machine line, not confirmed by the T3 walk (KB-47 family: single-combo ORB/machine flakiness); where T3 checked the drawer it is recorded opening
  - [DISPOSITIONED] sample credit-modal (preview-form) + page-overflow 493–500px@320/375 — page-overflow in the recorded cross-cutting families: static credit replica fixed width at mobile widths (KB-33) / preview chrome (KB-34); the per-theme figures match the campaign-wide shapes
  - [DISPOSITIONED] T3 custom red/black header lettering collides and is partly illegible at 375/320 (both engines — the row itself records the shape as possibly intended stylization (the theme’s decorative header lettering; see the row’s continuation); no defect call stands
  - [DISPOSITIONED] possibly intended stylization). — the row itself records the shape as possibly intended stylization (the theme’s decorative header lettering); no defect call stands
- **theme:chatscp-jp** (RENDER-S2-H (KO2)):
  - [DISPOSITIONED] hidden-license on both pages (all combos) + page sidebar-not-opening — hidden-* machine cluster confined to a transient/503-tainted or single-engine capture, or not reproduced visually (KB-44/KB-49/KB-50 family); the row records no T3 defect from it
  - [DISPOSITIONED] sample credit-modal (preview-form) — preview-form property: candidate/sample pages use credit:start-preview, which has no modal mechanism (GOSIGN-TESTS.md T2 note, 2026-11-16 ruling; KB-32)
  - [DISPOSITIONED] T3 Wikidot footer/license bar renders as a fixed overlay at left-centre over the body at every viewport (theme-specific — positive T3 confirmation recorded in the row; no finding stands from this segment
  - [DISPOSITIONED] machine hidden-license agrees). — hidden-* machine cluster confined to a transient/503-tainted or single-engine capture, or not reproduced visually (KB-44/KB-49/KB-50 family); the row records no T3 defect from it
- **theme:creature-jp** (RENDER-S2-H (KO2)):
  - [DISPOSITIONED] page runtime-hotlink incl. cdn.jsdelivr.net + scpko.wdfiles.com — candidate-own foreign/sandbox delivery hosts: posting-time rewrite or original-state delivery class (T1 class (ii); KB-41/KB-54 family). The pages render styled today; no error-box defect arises from these hosts
  - [DISPOSITIONED] sample credit-modal (preview-form) + runtime-hotlink (one combo http.cat among other hosts) — preview-form property: candidate/sample pages use credit:start-preview, which has no modal mechanism (GOSIGN-TESTS.md T2 note, 2026-11-16 ruling; KB-32)
  - [OPEN] T3 oversized circular SCP PARK header art wider than the mobile viewport, lettering cut at the edges at 375/320 (both engines). — section (e)
- **theme:cyber-specter-jp** (RENDER-S2-H (KO2)):
  - [DISPOSITIONED] sample credit-modal (preview-form) + 884px@768 overflow + runtime-hotlink incl. scpko hosts (one combo http.cat among other hosts) — candidate-own foreign/sandbox delivery hosts: posting-time rewrite or original-state delivery class (T1 class (ii); KB-41/KB-54 family). The pages render styled today; no error-box defect arises from these hosts
  - [DISPOSITIONED] T3 none beyond cross-cutting items. — recorded by the lane as cross-cutting (the campaign-wide shapes of register c2’s class entries)
- **theme:doap-bhl-jp** (RENDER-S2-H (KO3)):
  - [DISPOSITIONED] sample credit-modal (preview-form) + page-overflow 337–419px@320/375 (BHL min-width shape) — page-overflow in the recorded cross-cutting families: static credit replica fixed width at mobile widths (KB-33) / preview chrome (KB-34); the per-theme figures match the campaign-wide shapes
  - [DISPOSITIONED] T3 small red-outlined placeholder squares before multiple headings/blocks at 375/320 (both engines — an un-uploaded candidate asset (the row’s own reading, see its continuation: “likely an un-uploaded theme marker image, deferred”) — the owner-deferred hosting state (KB-58)
  - [DISPOSITIONED] likely an un-uploaded theme marker image, deferred, but visually a breakage). — an un-uploaded candidate asset (the row’s own reading: “likely an un-uploaded theme marker image, deferred”) — the owner-deferred hosting state (KB-58); the placeholder squares are the standard broken-image presentation of a deferred asset
- **theme:doap-nvl-jp** (RENDER-S2-H (KO3)):
  - [DISPOSITIONED] page runtime-hotlink site-theme chain only — environment-layer: runtime hosts arrive via the shared site theme chain, not the candidate (KB-40; RENDER-S2-G cross-cutting 1)
  - [DISPOSITIONED] sample credit-modal (preview-form) + runtime-hotlink — preview-form property: candidate/sample pages use credit:start-preview, which has no modal mechanism (GOSIGN-TESTS.md T2 note, 2026-11-16 ruling; KB-32)
  - [DISPOSITIONED] T3 none beyond cross-cutting items. — recorded by the lane as cross-cutting (the campaign-wide shapes of register c2’s class entries)
- **theme:flowergarden-jp** (RENDER-S2-H (KO3)):
  - [DISPOSITIONED] page sidebar-not-opening + runtime-hotlink site-theme chain — environment-layer: runtime hosts arrive via the shared site theme chain, not the candidate (KB-40; RENDER-S2-G cross-cutting 1)
  - [DISPOSITIONED] sample credit-modal (preview-form) + runtime-hotlink — preview-form property: candidate/sample pages use credit:start-preview, which has no modal mechanism (GOSIGN-TESTS.md T2 note, 2026-11-16 ruling; KB-32)
  - [DISPOSITIONED] T3 none beyond cross-cutting items. — recorded by the lane as cross-cutting (the campaign-wide shapes of register c2’s class entries)
- **theme:fmaf-theme-jp** (RENDER-S2-H (KO3)):
  - [DISPOSITIONED] page runtime-hotlink site-theme chain only — environment-layer: runtime hosts arrive via the shared site theme chain, not the candidate (KB-40; RENDER-S2-G cross-cutting 1)
  - [DISPOSITIONED] sample credit-modal (preview-form) + 884px@768 overflow (one sample combo http.cat among other hosts) — page-overflow in the recorded cross-cutting families: static credit replica fixed width at mobile widths (KB-33) / preview chrome (KB-34); the per-theme figures match the campaign-wide shapes
  - [DISPOSITIONED] T3 none beyond cross-cutting items. — recorded by the lane as cross-cutting (the campaign-wide shapes of register c2’s class entries)
- **theme:fogwalker-jp** (RENDER-S2-H (KO3)):
  - [DISPOSITIONED] page runtime-hotlink site-theme chain only — environment-layer: runtime hosts arrive via the shared site theme chain, not the candidate (KB-40; RENDER-S2-G cross-cutting 1)
  - [DISPOSITIONED] sample credit-modal (preview-form) + 884px@768 overflow — page-overflow in the recorded cross-cutting families: static credit replica fixed width at mobile widths (KB-33) / preview chrome (KB-34); the per-theme figures match the campaign-wide shapes
  - [DISPOSITIONED] T3 none beyond cross-cutting items. — recorded by the lane as cross-cutting (the campaign-wide shapes of register c2’s class entries)
- **theme:foundation-paper-jp** (RENDER-S2-H (KO4)):
  - [DISPOSITIONED] sample credit-modal (preview-form) + sidebar-not-opening + page-overflow 371–378px@320/375 + 780px@768 — page-overflow in the recorded cross-cutting families: static credit replica fixed width at mobile widths (KB-33) / preview chrome (KB-34); the per-theme figures match the campaign-wide shapes
  - [DISPOSITIONED] page runtime-hotlink site-theme chain only — environment-layer: runtime hosts arrive via the shared site theme chain, not the candidate (KB-40; RENDER-S2-G cross-cutting 1)
  - [DISPOSITIONED] T3 none beyond cross-cutting items. — recorded by the lane as cross-cutting (the campaign-wide shapes of register c2’s class entries)
- **theme:garak-the-magazine-jp** (RENDER-S2-H (KO4)):
  - [DISPOSITIONED] page hidden-* cluster confined to chromium-768, whose only hotlink host is http.cat = transient 503 capture, not a result — transient Wikidot 503 capture, not a result (KB-44)
  - [DISPOSITIONED] page-overflow 363–397px@320/375 on page and sample — page-overflow in the recorded cross-cutting families: static credit replica fixed width at mobile widths (KB-33) / preview chrome (KB-34); the per-theme figures match the campaign-wide shapes
  - [DISPOSITIONED] sample credit-modal (preview-form) — preview-form property: candidate/sample pages use credit:start-preview, which has no modal mechanism (GOSIGN-TESTS.md T2 note, 2026-11-16 ruling; KB-32)
  - [DISPOSITIONED] T3 none beyond cross-cutting items. — recorded by the lane as cross-cutting (the campaign-wide shapes of register c2’s class entries)
- **theme:golden-samdaecheon-jp** (RENDER-S2-H (KO4)):
  - [DISPOSITIONED] page runtime-hotlink site-theme chain only — environment-layer: runtime hosts arrive via the shared site theme chain, not the candidate (KB-40; RENDER-S2-G cross-cutting 1)
  - [DISPOSITIONED] sample credit-modal (preview-form) + 884px@768 overflow — page-overflow in the recorded cross-cutting families: static credit replica fixed width at mobile widths (KB-33) / preview chrome (KB-34); the per-theme figures match the campaign-wide shapes
  - [DISPOSITIONED] T3 none beyond cross-cutting items. — recorded by the lane as cross-cutting (the campaign-wide shapes of register c2’s class entries)
- **theme:halloween-koreana-jp** (RENDER-S2-H (KO4)):
  - [DISPOSITIONED] page runtime-hotlink site-theme chain only — environment-layer: runtime hosts arrive via the shared site theme chain, not the candidate (KB-40; RENDER-S2-G cross-cutting 1)
  - [DISPOSITIONED] sample credit-modal (preview-form) + 884px@768 overflow — page-overflow in the recorded cross-cutting families: static credit replica fixed width at mobile widths (KB-33) / preview chrome (KB-34); the per-theme figures match the campaign-wide shapes
  - [DISPOSITIONED] T3 none beyond cross-cutting items. — recorded by the lane as cross-cutting (the campaign-wide shapes of register c2’s class entries)
- **theme:it-pillar-of-industry-jp** (RENDER-S2-H (KO4)):
  - [DISPOSITIONED] page runtime-hotlink site-theme chain only — environment-layer: runtime hosts arrive via the shared site theme chain, not the candidate (KB-40; RENDER-S2-G cross-cutting 1)
  - [DISPOSITIONED] sample credit-modal (preview-form) + 884px@768 overflow — page-overflow in the recorded cross-cutting families: static credit replica fixed width at mobile widths (KB-33) / preview chrome (KB-34); the per-theme figures match the campaign-wide shapes
  - [DISPOSITIONED] T3 none beyond cross-cutting items. — recorded by the lane as cross-cutting (the campaign-wide shapes of register c2’s class entries)
- **theme:jiha-jp** (RENDER-S2-H (KO5)):
  - [DISPOSITIONED] page runtime-hotlink site-theme chain only — environment-layer: runtime hosts arrive via the shared site theme chain, not the candidate (KB-40; RENDER-S2-G cross-cutting 1)
  - [DISPOSITIONED] sample hidden-* cluster + sidebar-unreachable confined to chromium-320, whose only hotlink host is http.cat = transient 503 capture, not a result — transient Wikidot 503 capture, not a result (KB-44)
  - [DISPOSITIONED] sample credit-modal (preview-form) — preview-form property: candidate/sample pages use credit:start-preview, which has no modal mechanism (GOSIGN-TESTS.md T2 note, 2026-11-16 ruling; KB-32)
  - [DISPOSITIONED] T3 none beyond cross-cutting items. — recorded by the lane as cross-cutting (the campaign-wide shapes of register c2’s class entries)
- **theme:kcia10-jp** (RENDER-S2-H (KO5)):
  - [DISPOSITIONED] sample credit-modal (preview-form) + page-overflow 532–537px@320/375 + 884px@768 — page-overflow in the recorded cross-cutting families: static credit replica fixed width at mobile widths (KB-33) / preview chrome (KB-34); the per-theme figures match the campaign-wide shapes
  - [DISPOSITIONED] page runtime-hotlink site-theme chain only — environment-layer: runtime hosts arrive via the shared site theme chain, not the candidate (KB-40; RENDER-S2-G cross-cutting 1)
  - [DISPOSITIONED] T3 none beyond cross-cutting items. — recorded by the lane as cross-cutting (the campaign-wide shapes of register c2’s class entries)
- **theme:king-s-palace-jp** (RENDER-S2-H (KO5)):
  - [DISPOSITIONED] page runtime-hotlink site-theme chain only — environment-layer: runtime hosts arrive via the shared site theme chain, not the candidate (KB-40; RENDER-S2-G cross-cutting 1)
  - [DISPOSITIONED] sample credit-modal (preview-form) + 884px@768 overflow — page-overflow in the recorded cross-cutting families: static credit replica fixed width at mobile widths (KB-33) / preview chrome (KB-34); the per-theme figures match the campaign-wide shapes
  - [DISPOSITIONED] T3 none beyond cross-cutting items. — recorded by the lane as cross-cutting (the campaign-wide shapes of register c2’s class entries)
- **theme:legend-of-blue-jp** (RENDER-S2-H (KO5)):
  - [DISPOSITIONED] page-overflow 361–362px@320 on page and sample — page-overflow in the recorded cross-cutting families: static credit replica fixed width at mobile widths (KB-33) / preview chrome (KB-34); the per-theme figures match the campaign-wide shapes
  - [DISPOSITIONED] sample credit-modal (preview-form) — preview-form property: candidate/sample pages use credit:start-preview, which has no modal mechanism (GOSIGN-TESTS.md T2 note, 2026-11-16 ruling; KB-32)
  - [DISPOSITIONED] T3 theme-color swatch table wider than the content column, right-hand cells cut at 375/320 (both pages). — content-overflow machine warns are specimen shapes (code/table/demo content wider than the viewport by design), RENDER-S2-G cross-cutting 6 / KB-37 family
- **theme:minimal-scp-foundation-by-cocoonist-jp** (RENDER-S2-H (KO5)):
  - [DISPOSITIONED] page page-overflow 341–342px@320 + 389–535px@375 + hidden-footer + sidebar-unreachable — page-overflow in the recorded cross-cutting families: static credit replica fixed width at mobile widths (KB-33) / preview chrome (KB-34); the per-theme figures match the campaign-wide shapes
  - [DISPOSITIONED] sample hidden-* cluster across combos (4 of 8 combos carry an http.cat-only hotlink line = transient 503 captures — transient Wikidot 503 capture, not a result (KB-44)
  - [DISPOSITIONED] the rest recorded as-is) + credit-modal (preview-form) + page-overflow 341px@320 + sidebar-unreachable — page-overflow in the recorded cross-cutting families: static credit replica fixed width at mobile widths (KB-33) / preview chrome (KB-34); the per-theme figures match the campaign-wide shapes
  - [DISPOSITIONED] T3 none beyond cross-cutting items. — recorded by the lane as cross-cutting (the campaign-wide shapes of register c2’s class entries)
- **theme:mole-cricket-jp** (RENDER-S2-H (KO6)):
  - [DISPOSITIONED] page runtime-hotlink site-theme chain only — environment-layer: runtime hosts arrive via the shared site theme chain, not the candidate (KB-40; RENDER-S2-G cross-cutting 1)
  - [DISPOSITIONED] sample credit-modal (preview-form) + 884px@768 overflow — page-overflow in the recorded cross-cutting families: static credit replica fixed width at mobile widths (KB-33) / preview chrome (KB-34); the per-theme figures match the campaign-wide shapes
  - [DISPOSITIONED] T3 none beyond cross-cutting items. — recorded by the lane as cross-cutting (the campaign-wide shapes of register c2’s class entries)
- **theme:mr-reprisal-jp** (RENDER-S2-H (KO6)):
  - [DISPOSITIONED] page runtime-hotlink site-theme chain only — environment-layer: runtime hosts arrive via the shared site theme chain, not the candidate (KB-40; RENDER-S2-G cross-cutting 1)
  - [DISPOSITIONED] sample credit-modal (preview-form) + 884px@768 overflow — page-overflow in the recorded cross-cutting families: static credit replica fixed width at mobile widths (KB-33) / preview chrome (KB-34); the per-theme figures match the campaign-wide shapes
  - [DISPOSITIONED] T3 none beyond cross-cutting items. — recorded by the lane as cross-cutting (the campaign-wide shapes of register c2’s class entries)
- **theme:navla-style-jp** (RENDER-S2-H (KO6)):
  - [DISPOSITIONED] page runtime-hotlink site-theme chain only — environment-layer: runtime hosts arrive via the shared site theme chain, not the candidate (KB-40; RENDER-S2-G cross-cutting 1)
  - [DISPOSITIONED] sample credit-modal (preview-form) + runtime-hotlink (no sample overflow) — environment-layer: runtime hosts arrive via the shared site theme chain, not the candidate (KB-40; RENDER-S2-G cross-cutting 1)
  - [DISPOSITIONED] T3 none beyond cross-cutting items. — recorded by the lane as cross-cutting (the campaign-wide shapes of register c2’s class entries)
- **theme:note-theme-jp** (RENDER-S2-H (KO6)):
  - [DISPOSITIONED] page-overflow 378px@375 (page) and 378px@375 + 884px@768 (sample) — page-overflow in the recorded cross-cutting families: static credit replica fixed width at mobile widths (KB-33) / preview chrome (KB-34); the per-theme figures match the campaign-wide shapes
  - [DISPOSITIONED] sample credit-modal (preview-form) — preview-form property: candidate/sample pages use credit:start-preview, which has no modal mechanism (GOSIGN-TESTS.md T2 note, 2026-11-16 ruling; KB-32)
  - [DISPOSITIONED] T3 none beyond cross-cutting items. — recorded by the lane as cross-cutting (the campaign-wide shapes of register c2’s class entries)
- **theme:ontology-department-jp** (RENDER-S2-H (KO6)):
  - [DISPOSITIONED] page-overflow 324px@320 (page) and 337–419px@320/375 (sample) — page-overflow in the recorded cross-cutting families: static credit replica fixed width at mobile widths (KB-33) / preview chrome (KB-34); the per-theme figures match the campaign-wide shapes
  - [DISPOSITIONED] sample credit-modal (preview-form) — preview-form property: candidate/sample pages use credit:start-preview, which has no modal mechanism (GOSIGN-TESTS.md T2 note, 2026-11-16 ruling; KB-32)
  - [DISPOSITIONED] T3 none beyond cross-cutting items. — recorded by the lane as cross-cutting (the campaign-wide shapes of register c2’s class entries)
- **theme:pacom1943-jp** (RENDER-S2-H (KO7)):
  - [DISPOSITIONED] page-overflow 380px@320/375 (page) and 380px@320/375 + 906px@768 (sample) — page-overflow in the recorded cross-cutting families: static credit replica fixed width at mobile widths (KB-33) / preview chrome (KB-34); the per-theme figures match the campaign-wide shapes
  - [DISPOSITIONED] sample credit-modal (preview-form) — preview-form property: candidate/sample pages use credit:start-preview, which has no modal mechanism (GOSIGN-TESTS.md T2 note, 2026-11-16 ruling; KB-32)
  - [OPEN] T3 long headings run past the content column and are clipped at PC/tablet, wrap/cut at mobile. — section (e)
- **theme:past-oriented-jp** (RENDER-S2-H (KO7)):
  - [DISPOSITIONED] page runtime-hotlink site-theme chain only — environment-layer: runtime hosts arrive via the shared site theme chain, not the candidate (KB-40; RENDER-S2-G cross-cutting 1)
  - [DISPOSITIONED] sample credit-modal (preview-form) + runtime-hotlink (no sample overflow) — environment-layer: runtime hosts arrive via the shared site theme chain, not the candidate (KB-40; RENDER-S2-G cross-cutting 1)
  - [DISPOSITIONED] T3 none beyond cross-cutting items. — recorded by the lane as cross-cutting (the campaign-wide shapes of register c2’s class entries)
- **theme:path-of-jinin-jp** (RENDER-S2-H (KO7)):
  - [DISPOSITIONED] page hidden-* cluster confined to webkit-768, whose only hotlink host is http.cat = transient 503 capture, not a result — transient Wikidot 503 capture, not a result (KB-44)
  - [DISPOSITIONED] page runtime-hotlink site-theme chain otherwise — environment-layer: runtime hosts arrive via the shared site theme chain, not the candidate (KB-40; RENDER-S2-G cross-cutting 1)
  - [DISPOSITIONED] sample credit-modal (preview-form) + runtime-hotlink — preview-form property: candidate/sample pages use credit:start-preview, which has no modal mechanism (GOSIGN-TESTS.md T2 note, 2026-11-16 ruling; KB-32)
  - [DISPOSITIONED] T3 none beyond cross-cutting items. — recorded by the lane as cross-cutting (the campaign-wide shapes of register c2’s class entries)
- **theme:plugsoft-jp** (RENDER-S2-H (KO7)):
  - [DISPOSITIONED] sample credit-modal (preview-form) + 884px@768 overflow + runtime-hotlink incl. scpko.wdfiles.com on both pages — candidate-own foreign/sandbox delivery hosts: posting-time rewrite or original-state delivery class (T1 class (ii); KB-41/KB-54 family). The pages render styled today; no error-box defect arises from these hosts
  - [DISPOSITIONED] T3 none beyond cross-cutting items. — recorded by the lane as cross-cutting (the campaign-wide shapes of register c2’s class entries)
- **theme:rok-gov-theme-jp** (RENDER-S2-H (KO7)):
  - [DISPOSITIONED] page runtime-hotlink site-theme chain only — environment-layer: runtime hosts arrive via the shared site theme chain, not the candidate (KB-40; RENDER-S2-G cross-cutting 1)
  - [DISPOSITIONED] sample credit-modal (preview-form) + 884px@768 overflow — page-overflow in the recorded cross-cutting families: static credit replica fixed width at mobile widths (KB-33) / preview chrome (KB-34); the per-theme figures match the campaign-wide shapes
  - [DISPOSITIONED] T3 none beyond cross-cutting items. — recorded by the lane as cross-cutting (the campaign-wide shapes of register c2’s class entries)
- **theme:rpma-jp** (RENDER-S2-H (KO8)):
  - [DISPOSITIONED] page runtime-hotlink incl. cdn.jsdelivr.net + scpko.wdfiles.com — candidate-own foreign/sandbox delivery hosts: posting-time rewrite or original-state delivery class (T1 class (ii); KB-41/KB-54 family). The pages render styled today; no error-box defect arises from these hosts
  - [DISPOSITIONED] sample credit-modal (preview-form) + 884px@768 overflow (one combo http.cat among other hosts) — page-overflow in the recorded cross-cutting families: static credit replica fixed width at mobile widths (KB-33) / preview chrome (KB-34); the per-theme figures match the campaign-wide shapes
  - [DISPOSITIONED] T3 none beyond cross-cutting items. — recorded by the lane as cross-cutting (the campaign-wide shapes of register c2’s class entries)
- **theme:some-guider-jp** (RENDER-S2-H (KO8)):
  - [DISPOSITIONED] runtime-hotlink site-theme chain + scpko.wdfiles.com / scpko.wikidot.com on both pages — candidate-own foreign/sandbox delivery hosts: posting-time rewrite or original-state delivery class (T1 class (ii); KB-41/KB-54 family). The pages render styled today; no error-box defect arises from these hosts
  - [DISPOSITIONED] sample credit-modal (preview-form), no sample overflow — positive record (no sample overflow); the credit-modal part is the preview-form property (KB-32)
  - [DISPOSITIONED] T3 none beyond cross-cutting items. — recorded by the lane as cross-cutting (the campaign-wide shapes of register c2’s class entries)
- **theme:the-buck-stops-here-jp** (RENDER-S2-H (KO8)):
  - [DISPOSITIONED] page runtime-hotlink site-theme chain only — environment-layer: runtime hosts arrive via the shared site theme chain, not the candidate (KB-40; RENDER-S2-G cross-cutting 1)
  - [DISPOSITIONED] sample credit-modal (preview-form) + 884px@768 overflow — page-overflow in the recorded cross-cutting families: static credit replica fixed width at mobile widths (KB-33) / preview chrome (KB-34); the per-theme figures match the campaign-wide shapes
  - [DISPOSITIONED] T3 none beyond cross-cutting items. — recorded by the lane as cross-cutting (the campaign-wide shapes of register c2’s class entries)
- **theme:the-greatest-education-jp** (RENDER-S2-H (KO8)):
  - [DISPOSITIONED] sample credit-modal (preview-form) + page-overflow 324px@320 + 884px@768 + runtime-hotlink incl. scpko hosts on both pages — candidate-own foreign/sandbox delivery hosts: posting-time rewrite or original-state delivery class (T1 class (ii); KB-41/KB-54 family). The pages render styled today; no error-box defect arises from these hosts
  - [DISPOSITIONED] T3 none beyond cross-cutting items. — recorded by the lane as cross-cutting (the campaign-wide shapes of register c2’s class entries)

### c3. T4/T5 (localize patterns 1-11 + translation text) — per-theme outcomes by pattern

Class outcomes used below, per GOSIGN2-T45-FIXPREP.md’s adjudication of the LOCALIZE classes and the fix waves that executed them:
- Pattern 3 credit fields (§3 completeness): FIXED population-wide by the credit waves (FIX-CREDIT-A/B/C/D, FIX2-CREDIT, FIX4-CREDIT); assembly verification: check_source.py reports credit-missing-fields = 0 on all 287 files today. CREDIT-VERIFY renders the 11 audited supplements live.
- Pattern 6 (missing interwiki-style frame): FIXED by FIX3-A1/A2/B, FIX3-S2EN §2 and FIX4-IWA (29 files); assembly verification: the no-interwiki-style warning stands only on the three exception files (min-theme, shushuin, sigma-10). Duplicate-priority and split variants were fixed by FIX4-IWB / FIX4-LICENSE, with the counter-evidence dispositions recorded there (gsk’s genuine 4-layer stack; normal / dia-de-muertos parameter-gated Parallel presets).
- Pattern 9 (header/title language): DISPOSITIONED for every theme — owner ruling 2 (2026-11-16): header/title language is out of scope for migration correctness. This covers EN/CN/KO header strings, slogans, taglines and subtitles charged under pattern 9.
- Pattern 5 (original-site asset hotlinks): DISPOSITIONED, T1 class (ii) / KB-58 (posting-time rewrite or original-state host; re-upload barred). Named fixes inside the class: FIX2-DEADREF repoints (bloodraven, eigenmachine), FIX-P4 delivery repoints.
- Pattern 4 (foreign CDN/base delivery): FIXED for the FIX-P4 repoint set (below in the per-theme lines); DISPOSITIONED as KB-14 verbatim-import where no JP candidate exists for the imported third-party code (dream-of-the-stars’ Crimone, the paradigm themes, the-track-changers, winxp — FIX4-REPOINT / FIX4-IWA §3); DISPOSITIONED as KB-54 named exception for opinions-broadcaster’s CN components.
- Pattern 7 (JP fonts): FIXED for the themes named in FIX3-A1/A2/B, FIX3-S2EN §4 (21 themes), FIX4-LICENSE KB-04 (art-deco, oceanbound), FIX4-REPOINT KB-16 (aesthetic-theme), FIX4-IWB (skipos). DISPOSITIONED where the base delivers the face (stargazer, stellar: FIX-P4 repoint to basalt-jp, whose file loads Noto Sans JP at L113; LOCALIZE-S2-C item 12 ties stargazer’s base-inherited properties to that migration) and where the charge stands answered in the current file (words-of-wisdom: JP face loaded and referenced, L143/L269). OPEN where a lane charged it display-affecting and it stands unloaded — section (e) class D. All other pattern-7 notes were recorded by their lanes without a display-affecting mark; T4’s pass bar is display-affecting misses (GOSIGN-TESTS.md T4), so they are recorded, not blocking.
- Pattern 1 (include prefix forms): DISPOSITIONED as the posting-procedure convention class (class (ii)) except where a wave rewrote the lines (FIX-MECH, FIX2-INCLUDE, FIX3-PC candela, FIX3-SP sigma-plus port) or the lines are KB-54 named exceptions. Usage examples whose target is a campaign candidate under its posted name are the batch-posting class (LOCALIZE-S2-C item 16). Usage examples pointing at names that will never exist on scp-jp are OPEN — section (e) class H.
- Pattern 2 (bunny.net font delivery): FIXED where named (al-slop, basalt, inkblot, just-girly-things, foxtrot, scheme, scpedia, simple-yonder, skipos); otherwise DISPOSITIONED under the T1 hotlink class (ii).
- Pattern 10 / T5 wording: FIXED where a wave names the theme’s text fixes (foxtrot, retrofutura via FIX4-SIGMA); DISPOSITIONED where the lane itself marked the item minor, cosmetic, in-fiction specimen text, or not display-blocking (cosmonaut, thalassophobia-sigma, hytoth-two’s in-fiction samples, bulgunae, uiu-bhl-theme’s convention items, sigma’s code-box structure note — the render walk records the code specimen rendering and the port otherwise correct); OPEN for the standing untranslated/deleted reader-visible text in section (e) class H. Residual credit label variants (ソース link text, 著者/著作権者 forms) are the staff-normalization item named in LOCALIZE-S2-C checklist item 9 — DISPOSITIONED as a posting-procedure normalization, recorded per theme in the LOCALIZE rows.
- Pattern 11 (links to original-branch pages / hub links): DISPOSITIONED as the sibling/batch-posting class except the two prose-link items in section (e) class H (space, yossistyle), where JP pages exist and the lane charged the EN links display-affecting.
- Pattern 8 (usage-example forms not covered above): DISPOSITIONED under the same batch-posting / posting-procedure classes.

Per-theme pattern outcomes (only themes whose LOCALIZE row carries pattern charges; “→ (e)” cross-references a blocking OPEN item for that theme):

- **theme:aesthetic-theme-jp** (LOCALIZE-A): P7 FIXED (font wave); P9 DISPOSITIONED (ruling 2: header/title language out of scope); P10 DISPOSITIONED (lane-recorded severity / specimen class).
- **theme:al-slop-jp** (LOCALIZE-A): P1 DISPOSITIONED (posting-procedure convention class); P3 credit fields FIXED (credit waves; checker-verified); P5 DISPOSITIONED (class (ii) / KB-58).
- **theme:basalt-jp** (LOCALIZE-A): P4 DISPOSITIONED (delivery class (ii): original-state CDN delivery); P5 DISPOSITIONED (class (ii) / KB-58).
- **theme:bedrock-jp** (LOCALIZE-A): P4 DISPOSITIONED (delivery class (ii): original-state CDN delivery); P5 DISPOSITIONED (class (ii) / KB-58).
- **theme:black-highlighter-theme-jp** (LOCALIZE-A): P3 credit fields FIXED (credit waves; checker-verified); P10 DISPOSITIONED (lane-recorded severity / specimen class).
- **theme:blankstyle-jp** (LOCALIZE-A): P3 credit fields FIXED (credit waves; checker-verified); P6 FIXED (frame waves; checker-verified); P7 FIXED (font wave).
- **theme:classic-jp** (LOCALIZE-A): P3 credit fields FIXED (credit waves; checker-verified); P5 DISPOSITIONED (class (ii) / KB-58); P7 DISPOSITIONED (recorded without a display-affecting mark; T4 bar).
- **theme:cosmonaut-jp** (LOCALIZE-A): row charges DISPOSITIONED under the class outcomes above (header language = ruling 2; asset hosts = class (ii); credit fields FIXED by the credit waves).
- **theme:dear-dictator-jp** (LOCALIZE-A): P3 credit fields FIXED (credit waves; checker-verified); P5 DISPOSITIONED (class (ii) / KB-58); P6 FIXED (frame waves; checker-verified); P10 DISPOSITIONED (lane-recorded severity / specimen class).
- **theme:extra-black-highlighter-theme-jp** (LOCALIZE-A): P3 credit fields FIXED (credit waves; checker-verified); P5 DISPOSITIONED (class (ii) / KB-58); P7 DISPOSITIONED (recorded without a display-affecting mark; T4 bar).
- **theme:flopstyle-jp** (LOCALIZE-A): P1 DISPOSITIONED (posting-procedure convention class); P3 credit fields FIXED (credit waves; checker-verified); P4 DISPOSITIONED (delivery class (ii): original-state CDN delivery); P5 DISPOSITIONED (class (ii) / KB-58).
- **theme:flopstyle-dark-jp** (LOCALIZE-A): P1 DISPOSITIONED (posting-procedure convention class).
- **theme:foxtrot-jp** (LOCALIZE-A): P1 DISPOSITIONED (posting-procedure convention class); P3 credit fields FIXED (credit waves; checker-verified); P4 DISPOSITIONED (delivery class (ii): original-state CDN delivery); P5 DISPOSITIONED (class (ii) / KB-58).
- **theme:halloween-jp** (LOCALIZE-A): P3 credit fields FIXED (credit waves; checker-verified); P5 DISPOSITIONED (class (ii) / KB-58); P6 FIXED (frame waves; checker-verified); P7 DISPOSITIONED (recorded without a display-affecting mark; T4 bar).
- **theme:hansarp-jp** (LOCALIZE-A): P3 credit fields FIXED (credit waves; checker-verified); P9 DISPOSITIONED (ruling 2: header/title language out of scope).
- **theme:inkblot-jp** (LOCALIZE-A): P1 DISPOSITIONED (posting-procedure convention class); P3 credit fields FIXED (credit waves; checker-verified); P4 DISPOSITIONED (delivery class (ii): original-state CDN delivery).
- **theme:isolated-terminal-jp** (LOCALIZE-A): P3 credit fields FIXED (credit waves; checker-verified); P9 DISPOSITIONED (ruling 2: header/title language out of scope).
- **theme:jakstyle-jp** (LOCALIZE-A): P3 credit fields FIXED (credit waves; checker-verified); P9 DISPOSITIONED (ruling 2: header/title language out of scope).
- **theme:just-girly-things-jp** (LOCALIZE-A): P3 credit fields FIXED (credit waves; checker-verified); P4 DISPOSITIONED (delivery class (ii): original-state CDN delivery); P5 DISPOSITIONED (class (ii) / KB-58).
- **theme:monotypical-jp** (LOCALIZE-A): P4 DISPOSITIONED (delivery class (ii): original-state CDN delivery); P9 DISPOSITIONED (ruling 2: header/title language out of scope).
- **theme:much-cool-jp** (LOCALIZE-B): P3 credit fields FIXED (credit waves; checker-verified).
- **theme:night-rush-theme-jp** (LOCALIZE-B): P1 DISPOSITIONED (posting-procedure convention class); P3 credit fields FIXED (credit waves; checker-verified); P6 FIXED (frame waves; checker-verified).
- **theme:ouroborous-theme-jp** (LOCALIZE-B): P3 credit fields FIXED (credit waves; checker-verified).
- **theme:paperstack-jp** (LOCALIZE-B): P3 credit fields FIXED (credit waves; checker-verified); P6 FIXED (frame waves; checker-verified).
- **theme:pataphysics-jp** (LOCALIZE-B): P3 credit fields FIXED (credit waves; checker-verified) → (e); P7 DISPOSITIONED (recorded without a display-affecting mark; T4 bar).
- **theme:penumbra-jp** (LOCALIZE-B): P3 credit fields FIXED (credit waves; checker-verified); P6 FIXED (frame waves; checker-verified); P7 → (e) D.
- **theme:quand-le-soleil-se-couche** (LOCALIZE-B): P3 credit fields FIXED (credit waves; checker-verified); P6 FIXED (frame waves; checker-verified).
- **theme:scheme-jp** (LOCALIZE-B): P3 credit fields FIXED (credit waves; checker-verified); P5 DISPOSITIONED (class (ii) / KB-58).
- **theme:scp-human-resources-jp** (LOCALIZE-B): P3 credit fields FIXED (credit waves; checker-verified); P6 FIXED (frame waves; checker-verified); P7 → (e) D.
- **theme:scp-offices-theme-jp** (LOCALIZE-B): P3 credit fields FIXED (credit waves; checker-verified); P7 → (e) D.
- **theme:scpedia-jp** (LOCALIZE-B): P5 DISPOSITIONED (class (ii) / KB-58); P6 FIXED (frame waves; checker-verified); P7 DISPOSITIONED (recorded without a display-affecting mark; T4 bar).
- **theme:sigma-jp** (LOCALIZE-B): P5 DISPOSITIONED (class (ii) / KB-58); P6 FIXED (frame waves; checker-verified); P10 DISPOSITIONED (lane-recorded severity / specimen class).
- **theme:simple-yonder-jp** (LOCALIZE-B): P5 DISPOSITIONED (class (ii) / KB-58); P6 FIXED (frame waves; checker-verified).
- **theme:skipos-jp** (LOCALIZE-B): P3 credit fields FIXED (credit waves; checker-verified); P4 DISPOSITIONED (delivery class (ii): original-state CDN delivery); P5 DISPOSITIONED (class (ii) / KB-58); P6 FIXED (frame waves; checker-verified); P7 FIXED (font wave).
- **theme:space-jp** (LOCALIZE-B): P1 DISPOSITIONED (posting-procedure convention class); P11 → (e) H.
- **theme:turbo-vision-jp** (LOCALIZE-B): P3 credit fields FIXED (credit waves; checker-verified).
- **theme:wikifot-jp** (LOCALIZE-B): P3 credit fields FIXED (credit waves; checker-verified).
- **theme:y2k-jp** (LOCALIZE-B): P3 credit fields FIXED (credit waves; checker-verified) → (e); P7 → (e) D; P10/T5 → (e) H.
- **theme:yossistyle-jp** (LOCALIZE-B): P3 credit fields FIXED (credit waves; checker-verified) → (e); P6 FIXED (frame waves; checker-verified); P11 → (e) H.
- **theme:3law-pride-jp** (LOCALIZE-S2-A): row charges DISPOSITIONED under the class outcomes above (header language = ruling 2; asset hosts = class (ii); credit fields FIXED by the credit waves).
- **theme:3lawcracked-jp** (LOCALIZE-S2-A): row charges DISPOSITIONED under the class outcomes above (header language = ruling 2; asset hosts = class (ii); credit fields FIXED by the credit waves).
- **theme:512-onwards-jp** (LOCALIZE-S2-A): row charges DISPOSITIONED under the class outcomes above (header language = ruling 2; asset hosts = class (ii); credit fields FIXED by the credit waves).
- **theme:5k-jp** (LOCALIZE-S2-A): row charges DISPOSITIONED under the class outcomes above (header language = ruling 2; asset hosts = class (ii); credit fields FIXED by the credit waves).
- **theme:a-problematic-theme-jp** (LOCALIZE-S2-A): row charges DISPOSITIONED under the class outcomes above (header language = ruling 2; asset hosts = class (ii); credit fields FIXED by the credit waves).
- **theme:aces-and-eights-jp** (LOCALIZE-S2-A): P3 credit fields FIXED (credit waves; checker-verified); P5 DISPOSITIONED (class (ii) / KB-58); P6 FIXED (frame waves; checker-verified); P7 FIXED (font wave).
- **theme:ad-abyssum-penumbra-jp** (LOCALIZE-S2-A): P1 DISPOSITIONED (posting-procedure convention class); P5 DISPOSITIONED (class (ii) / KB-58); P6 FIXED (frame waves; checker-verified).
- **theme:admo-jp** (LOCALIZE-S2-A): P3 credit fields FIXED (credit waves; checker-verified); P4 DISPOSITIONED (delivery class (ii): original-state CDN delivery); P5 DISPOSITIONED (class (ii) / KB-58); P6 FIXED (frame waves; checker-verified); P7 FIXED (font wave).
- **theme:alcur-theme-jp** (LOCALIZE-S2-A): P3 credit fields FIXED (credit waves; checker-verified); P4 DISPOSITIONED (delivery class (ii): original-state CDN delivery); P5 DISPOSITIONED (class (ii) / KB-58); P6 FIXED (frame waves; checker-verified).
- **theme:alexylva-university-jp** (LOCALIZE-S2-A): P3 credit fields FIXED (credit waves; checker-verified); P5 DISPOSITIONED (class (ii) / KB-58); P6 FIXED (frame waves; checker-verified); P7 FIXED (font wave).
- **theme:ambrose-chapter-two-jp** (LOCALIZE-S2-A): P5 DISPOSITIONED (class (ii) / KB-58); P6 FIXED (frame waves; checker-verified); P7 FIXED (font wave); P9 DISPOSITIONED (ruling 2: header/title language out of scope).
- **theme:angel-jp** (LOCALIZE-S2-A): P5 DISPOSITIONED (class (ii) / KB-58); P6 FIXED (frame waves; checker-verified); P9 DISPOSITIONED (ruling 2: header/title language out of scope).
- **theme:anon-jp** (LOCALIZE-S2-A): P3 credit fields FIXED (credit waves; checker-verified); P5 DISPOSITIONED (class (ii) / KB-58); P6 FIXED (frame waves; checker-verified).
- **theme:art-deco-jp** (LOCALIZE-S2-A): row charges DISPOSITIONED under the class outcomes above (header language = ruling 2; asset hosts = class (ii); credit fields FIXED by the credit waves).
- **theme:ashes-to-ashes-jp** (LOCALIZE-S2-A): P4 DISPOSITIONED (delivery class (ii): original-state CDN delivery); P5 DISPOSITIONED (class (ii) / KB-58); P6 FIXED (frame waves; checker-verified).
- **theme:bedbugs-theme-jp** (LOCALIZE-S2-A): row charges DISPOSITIONED under the class outcomes above (header language = ruling 2; asset hosts = class (ii); credit fields FIXED by the credit waves).
- **theme:black-diamond-jp** (LOCALIZE-S2-A): P1 DISPOSITIONED (posting-procedure convention class).
- **theme:black-market-jp** (LOCALIZE-S2-A): row charges DISPOSITIONED under the class outcomes above (header language = ruling 2; asset hosts = class (ii); credit fields FIXED by the credit waves).
- **theme:black-serpent-jp** (LOCALIZE-S2-A): row charges DISPOSITIONED under the class outcomes above (header language = ruling 2; asset hosts = class (ii); credit fields FIXED by the credit waves).
- **theme:blood-jp** (LOCALIZE-S2-A): row charges DISPOSITIONED under the class outcomes above (header language = ruling 2; asset hosts = class (ii); credit fields FIXED by the credit waves).
- **theme:bloodraven-jp** (LOCALIZE-S2-A): P5 DISPOSITIONED (class (ii) / KB-58); P6 FIXED (frame waves; checker-verified); P11 DISPOSITIONED (sibling / batch-posting class).
- **theme:borealis-constant-theme-jp** (LOCALIZE-S2-A): P5 DISPOSITIONED (class (ii) / KB-58); P9 DISPOSITIONED (ruling 2: header/title language out of scope); P11 DISPOSITIONED (sibling / batch-posting class).
- **theme:caretaker-sigma-jp** (LOCALIZE-S2-A): P5 DISPOSITIONED (class (ii) / KB-58); P6 FIXED (frame waves; checker-verified).
- **theme:caretaker-theme-jp** (LOCALIZE-S2-A): P5 DISPOSITIONED (class (ii) / KB-58); P9 DISPOSITIONED (ruling 2: header/title language out of scope); P11 DISPOSITIONED (sibling / batch-posting class).
- **theme:ch-scp-theme-jp** (LOCALIZE-S2-A): P5 DISPOSITIONED (class (ii) / KB-58); P9 DISPOSITIONED (ruling 2: header/title language out of scope).
- **theme:chaos-jp** (LOCALIZE-S2-A): P7 FIXED (font wave); P9 DISPOSITIONED (ruling 2: header/title language out of scope).
- **theme:cleaning-services-jp** (LOCALIZE-S2-A): row charges DISPOSITIONED under the class outcomes above (header language = ruling 2; asset hosts = class (ii); credit fields FIXED by the credit waves).
- **theme:clock-tower-jp** (LOCALIZE-S2-A): P4 DISPOSITIONED (delivery class (ii): original-state CDN delivery); P7 FIXED (font wave).
- **theme:cosmos-jp** (LOCALIZE-S2-A): row charges DISPOSITIONED under the class outcomes above (header language = ruling 2; asset hosts = class (ii); credit fields FIXED by the credit waves).
- **theme:crayon-jp** (LOCALIZE-S2-A): P6 FIXED (frame waves; checker-verified); P7 DISPOSITIONED (recorded without a display-affecting mark; T4 bar).
- **theme:dark-jp** (LOCALIZE-S2-A): P1 DISPOSITIONED (posting-procedure convention class); P3 credit fields FIXED (credit waves; checker-verified).
- **theme:dark-dealings-jp** (LOCALIZE-S2-A): P1 DISPOSITIONED (posting-procedure convention class); P3 credit fields FIXED (credit waves; checker-verified); P9 DISPOSITIONED (ruling 2: header/title language out of scope); P11 DISPOSITIONED (sibling / batch-posting class).
- **theme:darkqueer-jp** (LOCALIZE-S2-A): P1 DISPOSITIONED (posting-procedure convention class); P3 credit fields FIXED (credit waves; checker-verified); P11 DISPOSITIONED (sibling / batch-posting class).
- **theme:decom-dept-jp** (LOCALIZE-S2-A): P1 DISPOSITIONED (posting-procedure convention class); P3 credit fields FIXED (credit waves; checker-verified); P11 DISPOSITIONED (sibling / batch-posting class).
- **theme:derby-jp** (LOCALIZE-S2-A): P1 DISPOSITIONED (posting-procedure convention class); P3 credit fields FIXED (credit waves; checker-verified); P9 DISPOSITIONED (ruling 2: header/title language out of scope); P10 DISPOSITIONED (lane-recorded severity / specimen class).
- **theme:dia-de-muertos-jp** (LOCALIZE-S2-A): P7 DISPOSITIONED (recorded without a display-affecting mark; T4 bar); P9 DISPOSITIONED (ruling 2: header/title language out of scope).
- **theme:diamond-highlighter-jp** (LOCALIZE-S2-A): P9 DISPOSITIONED (ruling 2: header/title language out of scope); P11 DISPOSITIONED (sibling / batch-posting class).
- **theme:dynamikron-jp** (LOCALIZE-S2-A): P6 FIXED (frame waves; checker-verified); P7 FIXED (font wave).
- **theme:eigenmachine-jp** (LOCALIZE-S2-A): P1 DISPOSITIONED (posting-procedure convention class); P4 DISPOSITIONED (delivery class (ii): original-state CDN delivery); P5 DISPOSITIONED (class (ii) / KB-58); P6 FIXED (frame waves; checker-verified); P9 DISPOSITIONED (ruling 2: header/title language out of scope).
- **theme:eigenvector-jp** (LOCALIZE-S2-A): P1 DISPOSITIONED (posting-procedure convention class); P4 DISPOSITIONED (delivery class (ii): original-state CDN delivery); P7 FIXED (font wave); P9 DISPOSITIONED (ruling 2: header/title language out of scope).
- **theme:enlightened-eyes-jp** (LOCALIZE-S2-B): P4 DISPOSITIONED (delivery class (ii): original-state CDN delivery).
- **theme:eventyr-jp** (LOCALIZE-S2-B): P9 DISPOSITIONED (ruling 2: header/title language out of scope).
- **theme:fandom-jp** (LOCALIZE-S2-B): P1 DISPOSITIONED (posting-procedure convention class).
- **theme:fossil-jp** (LOCALIZE-S2-B): P1 DISPOSITIONED (posting-procedure convention class); P5 DISPOSITIONED (class (ii) / KB-58).
- **theme:frownstyle-jp** (LOCALIZE-S2-B): P5 DISPOSITIONED (class (ii) / KB-58); P9 DISPOSITIONED (ruling 2: header/title language out of scope); P11 DISPOSITIONED (sibling / batch-posting class).
- **theme:fuladh-theme-jp** (LOCALIZE-S2-B): P5 DISPOSITIONED (class (ii) / KB-58).
- **theme:galactic-theme-jp** (LOCALIZE-S2-B): P5 DISPOSITIONED (class (ii) / KB-58); P9 DISPOSITIONED (ruling 2: header/title language out of scope).
- **theme:golden-feast-jp** (LOCALIZE-S2-B): P5 DISPOSITIONED (class (ii) / KB-58).
- **theme:greystyle-jp** (LOCALIZE-S2-B): P5 DISPOSITIONED (class (ii) / KB-58); P7 FIXED (font wave).
- **theme:helix-jp** (LOCALIZE-S2-B): P5 DISPOSITIONED (class (ii) / KB-58); P6 FIXED (frame waves; checker-verified).
- **theme:highroller-jp** (LOCALIZE-S2-B): P5 DISPOSITIONED (class (ii) / KB-58); P7 FIXED (font wave).
- **theme:hytoth-two-jp** (LOCALIZE-S2-B): P4 DISPOSITIONED (delivery class (ii): original-state CDN delivery); P5 DISPOSITIONED (class (ii) / KB-58); P7 FIXED (font wave).
- **theme:i57-jp** (LOCALIZE-S2-B): P5 DISPOSITIONED (class (ii) / KB-58); P7 FIXED (font wave).
- **theme:i57-theme-jp** (LOCALIZE-S2-B): P5 DISPOSITIONED (class (ii) / KB-58); P9 DISPOSITIONED (ruling 2: header/title language out of scope).
- **theme:immrama-jp** (LOCALIZE-S2-B): P5 DISPOSITIONED (class (ii) / KB-58); P9 DISPOSITIONED (ruling 2: header/title language out of scope).
- **theme:internal-affairs-jp** (LOCALIZE-S2-B): P5 DISPOSITIONED (class (ii) / KB-58); P9 DISPOSITIONED (ruling 2: header/title language out of scope).
- **theme:janitor-closet-jp** (LOCALIZE-S2-B): P5 DISPOSITIONED (class (ii) / KB-58); P9 DISPOSITIONED (ruling 2: header/title language out of scope).
- **theme:kiryu-labs-theme-jp** (LOCALIZE-S2-B): P3 credit fields FIXED (credit waves; checker-verified); P5 DISPOSITIONED (class (ii) / KB-58).
- **theme:lampeter-warm-jp** (LOCALIZE-S2-B): P1 DISPOSITIONED (posting-procedure convention class); P11 DISPOSITIONED (sibling / batch-posting class).
- **theme:laruetheme-jp** (LOCALIZE-S2-B): P9 DISPOSITIONED (ruling 2: header/title language out of scope).
- **theme:last-frontier-jp** (LOCALIZE-S2-B): P9 DISPOSITIONED (ruling 2: header/title language out of scope).
- **theme:laughter-and-knives-theme-jp** (LOCALIZE-S2-B): P9 DISPOSITIONED (ruling 2: header/title language out of scope).
- **theme:linear-black-jp** (LOCALIZE-S2-B): P1 DISPOSITIONED (posting-procedure convention class).
- **theme:lumina-jp** (LOCALIZE-S2-B): P4 DISPOSITIONED (delivery class (ii): original-state CDN delivery); P5 DISPOSITIONED (class (ii) / KB-58).
- **theme:magpie-swoops-jp** (LOCALIZE-S2-B): P5 DISPOSITIONED (class (ii) / KB-58).
- **theme:maxwell-s-silver-hammer-jp** (LOCALIZE-S2-B): P5 DISPOSITIONED (class (ii) / KB-58).
- **theme:mcf-jp** (LOCALIZE-S2-B): P4 DISPOSITIONED (delivery class (ii): original-state CDN delivery); P5 DISPOSITIONED (class (ii) / KB-58).
- **theme:oceanbound-jp** (LOCALIZE-S2-B): P5 DISPOSITIONED (class (ii) / KB-58).
- **theme:ordopharm-jp** (LOCALIZE-S2-B): P4 DISPOSITIONED (delivery class (ii): original-state CDN delivery); P9 DISPOSITIONED (ruling 2: header/title language out of scope).
- **theme:our-open-veins-jp** (LOCALIZE-S2-B): P9 DISPOSITIONED (ruling 2: header/title language out of scope).
- **theme:pastel-skies-jp** (LOCALIZE-S2-B): P9 DISPOSITIONED (ruling 2: header/title language out of scope).
- **theme:plant-jp** (LOCALIZE-S2-B): P7 DISPOSITIONED (recorded without a display-affecting mark; T4 bar); P9 DISPOSITIONED (ruling 2: header/title language out of scope).
- **theme:prom-labs-jp** (LOCALIZE-S2-B): P7 DISPOSITIONED (recorded without a display-affecting mark; T4 bar).
- **theme:queen-s-gambit-jp** (LOCALIZE-S2-C): P3 credit fields FIXED (credit waves; checker-verified); P5 DISPOSITIONED (class (ii) / KB-58).
- **theme:queerstyle-jp** (LOCALIZE-S2-C): P1 DISPOSITIONED (posting-procedure convention class).
- **theme:ragnarok-theme-jp** (LOCALIZE-S2-C): P5 DISPOSITIONED (class (ii) / KB-58); P6 FIXED (frame waves; checker-verified).
- **theme:raisa-jp** (LOCALIZE-S2-C): P5 DISPOSITIONED (class (ii) / KB-58); P11 → (e) H.
- **theme:raisa-sigma-jp** (LOCALIZE-S2-C): P5 DISPOSITIONED (class (ii) / KB-58); P11 DISPOSITIONED (sibling / batch-posting class).
- **theme:retro-aiad-theme-jp** (LOCALIZE-S2-C): P1 DISPOSITIONED (posting-procedure convention class); P3 credit fields FIXED (credit waves; checker-verified).
- **theme:retrofutura-jp** (LOCALIZE-S2-C): P1 DISPOSITIONED (posting-procedure convention class).
- **theme:saphir-jp** (LOCALIZE-S2-C): P3 credit fields FIXED (credit waves; checker-verified) → (e); P11 DISPOSITIONED (sibling / batch-posting class).
- **theme:scp-human-resources-sigma-jp** (LOCALIZE-S2-C): P1 DISPOSITIONED (posting-procedure convention class); P3 credit fields FIXED (credit waves; checker-verified).
- **theme:scp-offices-sigma-jp** (LOCALIZE-S2-C): P1 DISPOSITIONED (posting-procedure convention class); P3 credit fields FIXED (credit waves; checker-verified).
- **theme:shark-punching-centre-bhl-jp** (LOCALIZE-S2-C): P3 credit fields FIXED (credit waves; checker-verified).
- **theme:shattered-thoughts-jp** (LOCALIZE-S2-C): P3 credit fields FIXED (credit waves; checker-verified) → (e).
- **theme:shoebill-jp** (LOCALIZE-S2-C): P1 DISPOSITIONED (posting-procedure convention class).
- **theme:skiesmadestrange-jp** (LOCALIZE-S2-C): P1 DISPOSITIONED (posting-procedure convention class); P3 credit fields FIXED (credit waves; checker-verified) → (e).
- **theme:spidersfalling-jp** (LOCALIZE-S2-C): P3 credit fields FIXED (credit waves; checker-verified) → (e); P6 FIXED (frame waves; checker-verified).
- **theme:stargazer-jp** (LOCALIZE-S2-C): P4 DISPOSITIONED (delivery class (ii): original-state CDN delivery).
- **theme:stellar-jp** (LOCALIZE-S2-C): P4 DISPOSITIONED (delivery class (ii): original-state CDN delivery).
- **theme:sunside-jp** (LOCALIZE-S2-C): P6 FIXED (frame waves; checker-verified); P7 → (e) D.
- **theme:tales-of-the-mosaic-jp** (LOCALIZE-S2-C): P5 DISPOSITIONED (class (ii) / KB-58); P7 → (e) D.
- **theme:telecom-office-theme-jp** (LOCALIZE-S2-C): row charges DISPOSITIONED under the class outcomes above (header language = ruling 2; asset hosts = class (ii); credit fields FIXED by the credit waves).
- **theme:thalassophobia-jp** (LOCALIZE-S2-C): P3 credit fields FIXED (credit waves; checker-verified); P5 DISPOSITIONED (class (ii) / KB-58).
- **theme:thalassophobia-sigma-jp** (LOCALIZE-S2-C): P11 DISPOSITIONED (sibling / batch-posting class).
- **theme:the-coalition-theme-jp** (LOCALIZE-S2-C): P5 DISPOSITIONED (class (ii) / KB-58).
- **theme:the-foundation-sigma-jp** (LOCALIZE-S2-C): P9 DISPOSITIONED (ruling 2: header/title language out of scope).
- **theme:the-smell-of-smoke-jp** (LOCALIZE-S2-C): P1 DISPOSITIONED (posting-procedure convention class); P5 DISPOSITIONED (class (ii) / KB-58).
- **theme:turbo-vision-dark-jp** (LOCALIZE-S2-C): P5 DISPOSITIONED (class (ii) / KB-58).
- **theme:twin-files-jp** (LOCALIZE-S2-C): row charges → (e).
- **theme:ui-jp** (LOCALIZE-S2-C): P7 → (e) D; P9 DISPOSITIONED (ruling 2: header/title language out of scope).
- **theme:uiu-bhl-theme-jp** (LOCALIZE-S2-C): P1 DISPOSITIONED (posting-procedure convention class).
- **theme:unusual-cargo-jp** (LOCALIZE-S2-C): P1 DISPOSITIONED (posting-procedure convention class); P3 credit fields FIXED (credit waves; checker-verified); P7 DISPOSITIONED (recorded without a display-affecting mark; T4 bar).
- **theme:vanguard-jp** (LOCALIZE-S2-C): P3 credit fields FIXED (credit waves; checker-verified) → (e); P6 FIXED (frame waves; checker-verified).
- **theme:vanguard-supplement-jp** (LOCALIZE-S2-C): P3 credit fields FIXED (credit waves; checker-verified) → (e); P6 FIXED (frame waves; checker-verified).
- **theme:wilderness-jp** (LOCALIZE-S2-C): P1 DISPOSITIONED (posting-procedure convention class); P3 credit fields FIXED (credit waves; checker-verified) → (e).
- **theme:wondertainment-jp** (LOCALIZE-S2-C): P5 DISPOSITIONED (class (ii) / KB-58).
- **theme:words-of-wisdom-jp** (LOCALIZE-S2-C): P3 credit fields FIXED (credit waves; checker-verified) → (e); P5 DISPOSITIONED (class (ii) / KB-58); P6 FIXED (frame waves; checker-verified); P7 DISPOSITIONED (recorded without a display-affecting mark; T4 bar).
- **theme:writing-anomalies-jp** (LOCALIZE-S2-C): P1 DISPOSITIONED (posting-procedure convention class).
- **theme:xmas-jp** (LOCALIZE-S2-C): P3 credit fields FIXED (credit waves; checker-verified); P5 DISPOSITIONED (class (ii) / KB-58).
- **theme:andesite-jp** (LOCALIZE-S2-D): row charges → (e).
- **theme:another-night-jp** (LOCALIZE-S2-D): P5 DISPOSITIONED (class (ii) / KB-58).
- **theme:ared-jp** (LOCALIZE-S2-D): P5 DISPOSITIONED (class (ii) / KB-58); P6 FIXED (frame waves; checker-verified).
- **theme:asagao-jp** (LOCALIZE-S2-D): P3 credit fields FIXED (credit waves; checker-verified); P5 DISPOSITIONED (class (ii) / KB-58).
- **theme:betwixt-jp** (LOCALIZE-S2-D): P11 DISPOSITIONED (sibling / batch-posting class).
- **theme:black-rain-jp** (LOCALIZE-S2-D): P9 DISPOSITIONED (ruling 2: header/title language out of scope).
- **theme:blackinblack-jp** (LOCALIZE-S2-D): P11 DISPOSITIONED (sibling / batch-posting class).
- **theme:brokedown-database-jp** (LOCALIZE-S2-D): row charges → (e).
- **theme:broken-light-jp** (LOCALIZE-S2-D): P7 DISPOSITIONED (recorded without a display-affecting mark; T4 bar); P9 DISPOSITIONED (ruling 2: header/title language out of scope).
- **theme:broken-world-jp** (LOCALIZE-S2-D): P4 DISPOSITIONED (delivery class (ii): original-state CDN delivery).
- **theme:candela-jp** (LOCALIZE-S2-D): P4 DISPOSITIONED (delivery class (ii): original-state CDN delivery); P7 DISPOSITIONED (recorded without a display-affecting mark; T4 bar).
- **theme:cmst-jp** (LOCALIZE-S2-D): P4 DISPOSITIONED (delivery class (ii): original-state CDN delivery).
- **theme:construct-jp** (LOCALIZE-S2-D): P10 DISPOSITIONED (lane-recorded severity / specimen class); P11 DISPOSITIONED (sibling / batch-posting class).
- **theme:copper-jp** (LOCALIZE-S2-D): P3 credit fields FIXED (credit waves; checker-verified) → (e); P7 DISPOSITIONED (recorded without a display-affecting mark; T4 bar).
- **theme:crt-jp** (LOCALIZE-S2-D): P3 credit fields FIXED (credit waves; checker-verified) → (e); P6 FIXED (frame waves; checker-verified).
- **theme:darkblue-jp** (LOCALIZE-S2-D): P3 credit fields FIXED (credit waves; checker-verified) → (e); P7 → (e) D.
- **theme:decay-jp** (LOCALIZE-S2-D): P3 credit fields FIXED (credit waves; checker-verified) → (e); P10 DISPOSITIONED (lane-recorded severity / specimen class).
- **theme:deepspace-jp** (LOCALIZE-S2-D): P1 DISPOSITIONED (posting-procedure convention class); P3 credit fields FIXED (credit waves; checker-verified) → (e); P6 FIXED (frame waves; checker-verified).
- **theme:deserted-years-theme-jp** (LOCALIZE-S2-D): P5 DISPOSITIONED (class (ii) / KB-58); P6 FIXED (frame waves; checker-verified); P11 DISPOSITIONED (sibling / batch-posting class).
- **theme:dream-of-the-stars-jp** (LOCALIZE-S2-D): P4 DISPOSITIONED (delivery class (ii): original-state CDN delivery); P5 DISPOSITIONED (class (ii) / KB-58); P6 FIXED (frame waves; checker-verified); P7 DISPOSITIONED (recorded without a display-affecting mark; T4 bar).
- **theme:drunken-alley-jp** (LOCALIZE-S2-D): row charges → (e).
- **theme:emotion-division-jp** (LOCALIZE-S2-D): P1 DISPOSITIONED (posting-procedure convention class); P4 DISPOSITIONED (delivery class (ii): original-state CDN delivery); P5 DISPOSITIONED (class (ii) / KB-58); P6 FIXED (frame waves; checker-verified); P11 DISPOSITIONED (sibling / batch-posting class).
- **theme:ethic-committee-jp** (LOCALIZE-S2-D): P5 DISPOSITIONED (class (ii) / KB-58); P7 DISPOSITIONED (recorded without a display-affecting mark; T4 bar); P9 DISPOSITIONED (ruling 2: header/title language out of scope).
- **theme:fmd-bhl-theme-jp** (LOCALIZE-S2-D): P5 DISPOSITIONED (class (ii) / KB-58); P7 → (e) D; P9 DISPOSITIONED (ruling 2: header/title language out of scope).
- **theme:food-jp** (LOCALIZE-S2-D): P5 DISPOSITIONED (class (ii) / KB-58); P7 DISPOSITIONED (recorded without a display-affecting mark; T4 bar); P9 DISPOSITIONED (ruling 2: header/title language out of scope).
- **theme:foundom-jp** (LOCALIZE-S2-D): P1 DISPOSITIONED (posting-procedure convention class); P2 DISPOSITIONED (T1 class (ii)); P7 DISPOSITIONED (recorded without a display-affecting mark; T4 bar).
- **theme:frutiger-aero-jp** (LOCALIZE-S2-D): P5 DISPOSITIONED (class (ii) / KB-58); P7 → (e) D; P9 DISPOSITIONED (ruling 2: header/title language out of scope).
- **theme:golden-wind-jp** (LOCALIZE-S2-D): row charges → (e).
- **theme:gp-refresh-jp** (LOCALIZE-S2-D): P4 DISPOSITIONED (delivery class (ii): original-state CDN delivery); P9 DISPOSITIONED (ruling 2: header/title language out of scope).
- **theme:greyday-jp** (LOCALIZE-S2-D): row charges → (e).
- **theme:gsk-jp** (LOCALIZE-S2-D): P6 FIXED (frame waves; checker-verified); P7 DISPOSITIONED (recorded without a display-affecting mark; T4 bar); P9 DISPOSITIONED (ruling 2: header/title language out of scope); P11 DISPOSITIONED (sibling / batch-posting class).
- **theme:highlighter-bhl-jp** (LOCALIZE-S2-D): P4 DISPOSITIONED (delivery class (ii): original-state CDN delivery); P6 FIXED (frame waves; checker-verified).
- **theme:horn-jp** (LOCALIZE-S2-D): P5 DISPOSITIONED (class (ii) / KB-58); P11 DISPOSITIONED (sibling / batch-posting class).
- **theme:ink-jp** (LOCALIZE-S2-D): P3 credit fields FIXED (credit waves; checker-verified) → (e); P5 DISPOSITIONED (class (ii) / KB-58); P11 DISPOSITIONED (sibling / batch-posting class).
- **theme:inland-empire-jp** (LOCALIZE-S2-D): P5 DISPOSITIONED (class (ii) / KB-58); P11 DISPOSITIONED (sibling / batch-posting class).
- **theme:kitchen-jp** (LOCALIZE-S2-D): P1 DISPOSITIONED (posting-procedure convention class); P3 credit fields FIXED (credit waves; checker-verified) → (e); P5 DISPOSITIONED (class (ii) / KB-58); P9 DISPOSITIONED (ruling 2: header/title language out of scope).
- **theme:lead-by-example-jp** (LOCALIZE-S2-D): P5 DISPOSITIONED (class (ii) / KB-58); P7 DISPOSITIONED (recorded without a display-affecting mark; T4 bar); P11 DISPOSITIONED (sibling / batch-posting class).
- **theme:madoka-jp** (LOCALIZE-S2-D): P6 FIXED (frame waves; checker-verified); P7 DISPOSITIONED (recorded without a display-affecting mark; T4 bar).
- **theme:magazine-jp** (LOCALIZE-S2-D): P4 DISPOSITIONED (delivery class (ii): original-state CDN delivery); P10/T5 → (e) H; P11 DISPOSITIONED (sibling / batch-posting class).
- **theme:magicity-jp** (LOCALIZE-S2-D): row charges → (e).
- **theme:marchen-jp** (LOCALIZE-S2-D): P4 DISPOSITIONED (delivery class (ii): original-state CDN delivery); P5 DISPOSITIONED (class (ii) / KB-58).
- **theme:mox-jp** (LOCALIZE-S2-D): P7 DISPOSITIONED (recorded without a display-affecting mark; T4 bar).
- **theme:nameless-jp** (LOCALIZE-S2-E): P2 DISPOSITIONED (T1 class (ii)); P4 DISPOSITIONED (delivery class (ii): original-state CDN delivery); P5 DISPOSITIONED (class (ii) / KB-58).
- **theme:normal-jp** (LOCALIZE-S2-E): P4 DISPOSITIONED (delivery class (ii): original-state CDN delivery).
- **theme:obflow-jp** (LOCALIZE-S2-E): P4 DISPOSITIONED (delivery class (ii): original-state CDN delivery).
- **theme:oneiroi-west-jp** (LOCALIZE-S2-E): P5 DISPOSITIONED (class (ii) / KB-58).
- **theme:opinions-broadcaster-jp** (LOCALIZE-S2-E): P4 DISPOSITIONED (delivery class (ii): original-state CDN delivery).
- **theme:parablue-jp** (LOCALIZE-S2-E): P4 DISPOSITIONED (delivery class (ii): original-state CDN delivery); P5 DISPOSITIONED (class (ii) / KB-58); P9 DISPOSITIONED (ruling 2: header/title language out of scope).
- **theme:paradigm-inapplicable-jp** (LOCALIZE-S2-E): P4 DISPOSITIONED (delivery class (ii): original-state CDN delivery); P5 DISPOSITIONED (class (ii) / KB-58); P7 → (e) D; P11 DISPOSITIONED (sibling / batch-posting class).
- **theme:paradigm-inapplicable-sigma-jp** (LOCALIZE-S2-E): P1 DISPOSITIONED (posting-procedure convention class); P5 DISPOSITIONED (class (ii) / KB-58); P7 → (e) D.
- **theme:paradigm-reconstruction-jp** (LOCALIZE-S2-E): P4 DISPOSITIONED (delivery class (ii): original-state CDN delivery); P5 DISPOSITIONED (class (ii) / KB-58); P7 → (e) D; P11 DISPOSITIONED (sibling / batch-posting class).
- **theme:parallel-jp** (LOCALIZE-S2-E): P1 DISPOSITIONED (posting-procedure convention class); P4 DISPOSITIONED (delivery class (ii): original-state CDN delivery); P5 DISPOSITIONED (class (ii) / KB-58); P10 DISPOSITIONED (lane-recorded severity / specimen class); P11 DISPOSITIONED (sibling / batch-posting class).
- **theme:peroxide-jp** (LOCALIZE-S2-E): P1 DISPOSITIONED (posting-procedure convention class); P5 DISPOSITIONED (class (ii) / KB-58).
- **theme:petrifaction-jp** (LOCALIZE-S2-E): P5 DISPOSITIONED (class (ii) / KB-58); P9 DISPOSITIONED (ruling 2: header/title language out of scope).
- **theme:progress-institute-jp** (LOCALIZE-S2-E): P3 credit fields FIXED (credit waves; checker-verified) → (e); P5 DISPOSITIONED (class (ii) / KB-58); P9 DISPOSITIONED (ruling 2: header/title language out of scope).
- **theme:redsquare-jp** (LOCALIZE-S2-E): P5 DISPOSITIONED (class (ii) / KB-58).
- **theme:rima-jp** (LOCALIZE-S2-E): P5 DISPOSITIONED (class (ii) / KB-58).
- **theme:sci-fi-jp** (LOCALIZE-S2-E): row charges → (e).
- **theme:scpdeclassified-jp** (LOCALIZE-S2-E): row charges → (e).
- **theme:scplive-jp** (LOCALIZE-S2-E): row charges → (e).
- **theme:shancheng-jp** (LOCALIZE-S2-E): row charges → (e).
- **theme:share-future-community-jp** (LOCALIZE-S2-E): row charges → (e).
- **theme:shivering-night-jp** (LOCALIZE-S2-E): P3 credit fields FIXED (credit waves; checker-verified) → (e).
- **theme:sodium-jp** (LOCALIZE-S2-E): P3 credit fields FIXED (credit waves; checker-verified).
- **theme:sodium-pentasulfide-jp** (LOCALIZE-S2-E): P3 credit fields FIXED (credit waves; checker-verified).
- **theme:sound-jp** (LOCALIZE-S2-E): row charges → (e).
- **theme:starbasalt-jp** (LOCALIZE-S2-E): row charges → (e).
- **theme:starry-jp** (LOCALIZE-S2-E): P3 credit fields FIXED (credit waves; checker-verified); P4 DISPOSITIONED (delivery class (ii): original-state CDN delivery); P5 DISPOSITIONED (class (ii) / KB-58); P9 DISPOSITIONED (ruling 2: header/title language out of scope).
- **theme:steam-guide-jp** (LOCALIZE-S2-E): P4 DISPOSITIONED (delivery class (ii): original-state CDN delivery); P9 DISPOSITIONED (ruling 2: header/title language out of scope).
- **theme:supply-n-demand-jp** (LOCALIZE-S2-E): P4 DISPOSITIONED (delivery class (ii): original-state CDN delivery); P5 DISPOSITIONED (class (ii) / KB-58); P7 DISPOSITIONED (recorded without a display-affecting mark; T4 bar); P9 DISPOSITIONED (ruling 2: header/title language out of scope).
- **theme:suprematism-jp** (LOCALIZE-S2-E): P1 DISPOSITIONED (posting-procedure convention class); P3 credit fields FIXED (credit waves; checker-verified) → (e); P4 DISPOSITIONED (delivery class (ii): original-state CDN delivery); P5 DISPOSITIONED (class (ii) / KB-58); P9 DISPOSITIONED (ruling 2: header/title language out of scope).
- **theme:tfnac-jp** (LOCALIZE-S2-E): P1 DISPOSITIONED (posting-procedure convention class); P4 DISPOSITIONED (delivery class (ii): original-state CDN delivery); P5 DISPOSITIONED (class (ii) / KB-58); P9 DISPOSITIONED (ruling 2: header/title language out of scope); P11 DISPOSITIONED (sibling / batch-posting class).
- **theme:the-other-side-jp** (LOCALIZE-S2-E): row charges DISPOSITIONED under the class outcomes above (header language = ruling 2; asset hosts = class (ii); credit fields FIXED by the credit waves).
- **theme:the-track-changers-jp** (LOCALIZE-S2-E): row charges → (e).
- **theme:trauma-jp** (LOCALIZE-S2-E): row charges → (e).
- **theme:travellers-book-jp** (LOCALIZE-S2-E): row charges → (e).
- **theme:ultimate-reader-jp** (LOCALIZE-S2-E): row charges DISPOSITIONED under the class outcomes above (header language = ruling 2; asset hosts = class (ii); credit fields FIXED by the credit waves).
- **theme:voyager-jp** (LOCALIZE-S2-E): row charges → (e).
- **theme:walk-in-the-dark-jp** (LOCALIZE-S2-E): row charges DISPOSITIONED under the class outcomes above (header language = ruling 2; asset hosts = class (ii); credit fields FIXED by the credit waves).
- **theme:waxed-oxidized-cut-copper-slab-jp** (LOCALIZE-S2-E): row charges DISPOSITIONED under the class outcomes above (header language = ruling 2; asset hosts = class (ii); credit fields FIXED by the credit waves).
- **theme:winddew-in-hand-jp** (LOCALIZE-S2-E): row charges → (e).
- **theme:winxp-jp** (LOCALIZE-S2-E): row charges DISPOSITIONED under the class outcomes above (header language = ruling 2; asset hosts = class (ii); credit fields FIXED by the credit waves).
- **theme:wish-for-miracle-jp** (LOCALIZE-S2-E): row charges DISPOSITIONED under the class outcomes above (header language = ruling 2; asset hosts = class (ii); credit fields FIXED by the credit waves).
- **theme:yore-jp** (LOCALIZE-S2-E): row charges DISPOSITIONED under the class outcomes above (header language = ruling 2; asset hosts = class (ii); credit fields FIXED by the credit waves).
- **theme:07k-jp** (LOCALIZE-S2-F): P3 credit fields FIXED (credit waves; checker-verified) → (e); P5 DISPOSITIONED (class (ii) / KB-58); P7 DISPOSITIONED (recorded without a display-affecting mark; T4 bar); P9 DISPOSITIONED (ruling 2: header/title language out of scope).
- **theme:a-midnight-invitation-jp** (LOCALIZE-S2-F): P3 credit fields FIXED (credit waves; checker-verified).
- **theme:animal-instead-of-beast-jp** (LOCALIZE-S2-F): P3 credit fields FIXED (credit waves; checker-verified) → (e); P4 DISPOSITIONED (delivery class (ii): original-state CDN delivery); P6 FIXED (frame waves; checker-verified); P9 DISPOSITIONED (ruling 2: header/title language out of scope).
- **theme:anniversary-jp** (LOCALIZE-S2-F): P7 DISPOSITIONED (recorded without a display-affecting mark; T4 bar); P9 DISPOSITIONED (ruling 2: header/title language out of scope).
- **theme:atlas-maniacus-jp** (LOCALIZE-S2-F): P3 credit fields FIXED (credit waves; checker-verified); P5 DISPOSITIONED (class (ii) / KB-58); P9 DISPOSITIONED (ruling 2: header/title language out of scope).
- **theme:back-jan-fire-jp** (LOCALIZE-S2-F): P3 credit fields FIXED (credit waves; checker-verified); P4 DISPOSITIONED (delivery class (ii): original-state CDN delivery); P5 DISPOSITIONED (class (ii) / KB-58); P9 DISPOSITIONED (ruling 2: header/title language out of scope).
- **theme:bulgunae-jp** (LOCALIZE-S2-F): P3 credit fields FIXED (credit waves; checker-verified).
- **theme:chatscp-jp** (LOCALIZE-S2-F): P3 credit fields FIXED (credit waves; checker-verified); P10 DISPOSITIONED (lane-recorded severity / specimen class); P11 DISPOSITIONED (sibling / batch-posting class).
- **theme:creature-jp** (LOCALIZE-S2-F): P3 credit fields FIXED (credit waves; checker-verified); P4 DISPOSITIONED (delivery class (ii): original-state CDN delivery); P5 DISPOSITIONED (class (ii) / KB-58); P10 DISPOSITIONED (lane-recorded severity / specimen class); P11 DISPOSITIONED (sibling / batch-posting class).
- **theme:cyber-specter-jp** (LOCALIZE-S2-F): P1 DISPOSITIONED (posting-procedure convention class); P5 DISPOSITIONED (class (ii) / KB-58); P9 DISPOSITIONED (ruling 2: header/title language out of scope); P10 DISPOSITIONED (lane-recorded severity / specimen class); P11 DISPOSITIONED (sibling / batch-posting class).
- **theme:doap-bhl-jp** (LOCALIZE-S2-F): P1 DISPOSITIONED (posting-procedure convention class); P6 FIXED (frame waves; checker-verified); P11 DISPOSITIONED (sibling / batch-posting class).
- **theme:doap-nvl-jp** (LOCALIZE-S2-F): P1 DISPOSITIONED (posting-procedure convention class).
- **theme:foundation-paper-jp** (LOCALIZE-S2-F): P6 FIXED (frame waves; checker-verified); P10 DISPOSITIONED (lane-recorded severity / specimen class); P11 DISPOSITIONED (sibling / batch-posting class).
- **theme:garak-the-magazine-jp** (LOCALIZE-S2-F): P1 DISPOSITIONED (posting-procedure convention class); P4 DISPOSITIONED (delivery class (ii): original-state CDN delivery); P6 FIXED (frame waves; checker-verified).
- **theme:golden-samdaecheon-jp** (LOCALIZE-S2-F): P3 credit fields FIXED (credit waves; checker-verified); P6 FIXED (frame waves; checker-verified).
- **theme:halloween-koreana-jp** (LOCALIZE-S2-F): P6 FIXED (frame waves; checker-verified).
- **theme:jiha-jp** (LOCALIZE-S2-F): P3 credit fields FIXED (credit waves; checker-verified).
- **theme:kcia10-jp** (LOCALIZE-S2-F): P3 credit fields FIXED (credit waves; checker-verified); P11 DISPOSITIONED (sibling / batch-posting class).
- **theme:king-s-palace-jp** (LOCALIZE-S2-F): P3 credit fields FIXED (credit waves; checker-verified) → (e); P6 FIXED (frame waves; checker-verified).
- **theme:legend-of-blue-jp** (LOCALIZE-S2-F): P3 credit fields FIXED (credit waves; checker-verified).
- **theme:minimal-scp-foundation-by-cocoonist-jp** (LOCALIZE-S2-F): P3 credit fields FIXED (credit waves; checker-verified); P6 FIXED (frame waves; checker-verified); P11 DISPOSITIONED (sibling / batch-posting class).
- **theme:navla-style-jp** (LOCALIZE-S2-F): P1 DISPOSITIONED (posting-procedure convention class); P6 FIXED (frame waves; checker-verified).
- **theme:ontology-department-jp** (LOCALIZE-S2-F): P6 FIXED (frame waves; checker-verified); P11 DISPOSITIONED (sibling / batch-posting class).
- **theme:pacom1943-jp** (LOCALIZE-S2-F): P1 DISPOSITIONED (posting-procedure convention class); P3 credit fields FIXED (credit waves; checker-verified); P10 DISPOSITIONED (lane-recorded severity / specimen class); P11 DISPOSITIONED (sibling / batch-posting class).
- **theme:past-oriented-jp** (LOCALIZE-S2-F): P5 DISPOSITIONED (class (ii) / KB-58); P9 DISPOSITIONED (ruling 2: header/title language out of scope).
- **theme:path-of-jinin-jp** (LOCALIZE-S2-F): P3 credit fields FIXED (credit waves; checker-verified); P6 FIXED (frame waves; checker-verified).
- **theme:plugsoft-jp** (LOCALIZE-S2-F): P3 credit fields FIXED (credit waves; checker-verified) → (e); P5 DISPOSITIONED (class (ii) / KB-58); P7 DISPOSITIONED (recorded without a display-affecting mark; T4 bar); P9 DISPOSITIONED (ruling 2: header/title language out of scope).
- **theme:rok-gov-theme-jp** (LOCALIZE-S2-F): P1 DISPOSITIONED (posting-procedure convention class); P6 FIXED (frame waves; checker-verified); P9 DISPOSITIONED (ruling 2: header/title language out of scope).
- **theme:rpma-jp** (LOCALIZE-S2-F): P4 DISPOSITIONED (delivery class (ii): original-state CDN delivery); P5 DISPOSITIONED (class (ii) / KB-58); P9 DISPOSITIONED (ruling 2: header/title language out of scope); P11 DISPOSITIONED (sibling / batch-posting class).
- **theme:some-guider-jp** (LOCALIZE-S2-F): P3 credit fields FIXED (credit waves; checker-verified); P5 DISPOSITIONED (class (ii) / KB-58); P9 DISPOSITIONED (ruling 2: header/title language out of scope).
- **theme:the-buck-stops-here-jp** (LOCALIZE-S2-F): P1 DISPOSITIONED (posting-procedure convention class).
- **theme:the-greatest-education-jp** (LOCALIZE-S2-F): P3 credit fields FIXED (credit waves; checker-verified); P5 DISPOSITIONED (class (ii) / KB-58); P9 DISPOSITIONED (ruling 2: header/title language out of scope).

Zero-tag rows (LOCALIZE worst-finding phrased without pattern numbers): 40 — each is covered by the class outcomes above or cross-referenced to (e); none carries a charge outside the adjudicated classes.

### c4. Patterns layer (KB-01..KB-65) — sweep outcomes

Rule applied (campaign record, 2026-11-17): a file-provable HIT is defect evidence and must be fixed or dispositioned; an UNDECIDABLE-FROM-REPO cell is a triage state, never a failure and never a pass; a clean static sweep never upgrades a row beyond production-complete. Sweep totals (canonical patterns/SWEEP-RESULTS.tsv): 65 patterns, 2038 hits, 1861 undecidable cells.

- KB-01 (unencoded-colon and URL-encoding shapes): 1 standing hit = the 5k L100 occurrence, DISPOSITIONED under the pattern’s own 5k precedent (the encoded form does not serve). 2 baseline hits FIXED by FIX-MECH’s colon wave. See c1.
- KB-02 (asset delivery probes): 0 repo-provable by design; the probe queue (80 themes / 343 URLs) is a recorded triage state, not a defect set. The one render-measured instance in the population (derby’s text/plain SVG) is dispositioned in c2 as a posting-procedure delivery form.
- KB-03 (dead url() declarations): drunken-alley’s instances removed by FIX4-IWA (original-identical dead declarations). No standing charge.
- KB-04 (font loads failing / named-not-loaded at the delivery layer): FIXED for lumina (FIX4-MECH) and art-deco + oceanbound (FIX4-LICENSE, live-probed 400→200).
- KB-05 (asset MIME/delivery): 0 repo-provable by design; 251-theme probe queue recorded as triage.
- KB-06 (include parameters unsupplied): confirmed hits quand + skipos. Skipos FIXED (FIX4-IWB §13). **Quand OPEN — section (e) item A1.** bloodraven + caretaker-sigma were triage and were closed by their KB-07b priority fixes (FIX4-IWB, FIX4-LICENSE).
- KB-07 family (interwiki-style frame defects; charged union 52 themes): missing-entirely ×29 FIXED by FIX4-IWA (plus the FIX3-wave additions); missing-priority ×3 FIXED (bloodraven FIX4-IWB, caretaker-sigma FIX4-LICENSE, skipos FIX4-IWB); duplicate-priority ×7 FIXED by FIX4-IWB (shancheng’s form adjudicated posting-correct, supervisor record); BHL splits ×8 FIXED by FIX4-IWB; the A13-5 variant (highlighter-bhl croqstyle include) restored by FIX4-IWA, its split top/tail left per SWEEP-A1 clearance; gsk’s own-at-4 and normal / dia-de-muertos gated stacks stand on recorded counter-evidence (genuine layered/parameter-gated stacks, original-identical). blackinblack was examined and NOT charged.
- KB-08 (include-order shape): 20 hits, identical head shape; T2 renders show the base applied, so the shape is a benign candidate idiom — adjudicated DISPOSITIONED at ledger time per the sweep’s own note; the pattern stays triage.
- KB-09 / KB-10 (JP-original false-positive shapes): the charges on min-theme and shushuin are DISPOSITIONED as false positives for JP originals (FIX4-JPORIG adjudication, accepted in full; production min-theme carries a credit block and an interwiki include, production shushuin a credit block and no interwiki include, so both candidates are production-faithful). Checker runs on JP originals must omit --translation.
- KB-11 (credit-module CSS supplement): the sweep classification reproduces exactly (OWN 160 / INHERIT 26 / INHERIT-EXT 45 / NONE 56). The confirmed hit set is exactly the 5 FIX4-CREDIT themes (3law-pride, 3lawcracked, the-other-side, travellers-book, share-future-community) — FIXED (9fbcd94), and CREDIT-VERIFY renders all 11 audited credit themes’ supplements live with exact computed-style matches. The 47 undecidable cells (45 INHERIT-EXT + blackinblack + skiesmadestrange) are recorded triage states; the superseded A4 figure of 80 is not used.
- KB-12 (border-omission shape): 0 charged; 36 themes carry the shape, all UNDECIDABLE (the JP anchor source is outside the repo). Triage state, recorded.
- KB-13 (global .modalbox centering): 1 confirmed theme, space. **OPEN — section (e) item G1** (its render manifestation).
- KB-14 (third-party code imports with no JP candidate): DISPOSITIONED verbatim-import set (dream-of-the-stars, paradigm-inapplicable, paradigm-reconstruction, the-track-changers, winxp; marchen’s Basalt import was instead FIXED by repoint, FIX4-REPOINT).
- KB-16 (JP font fallbacks missing on a Latin display theme): aesthetic-theme FIXED by the FIX4-REPOINT form.
- KB-17 (font-delivery hosts / old BHL delivery): bunny set FIXED (scheme, scpedia, simple-yonder by FIX4-REPOINT; skipos by FIX4-IWB); nu-scptheme set (bulgunae, suprematism, tfnac) DISPOSITIONED class (ii) posting-time rewrite; bulgunae’s split form recorded no-edit with grounds in FIX4-REPOINT.
- KB-18 (edit-lock / posting notices untranslated): petrifaction FIXED (FIX4-REPOINT; its notice is translated).
- KB-19 (population-wide undecidable by design): 287 undecidable cells recorded as the pattern’s design state; no charges.
- KB-23..KB-31 (render triage family): the overflow/modal/sidebar shapes are dispositioned in c2 by class (KB-23/33 replica widths, KB-31 real-module modal rule with its sweep amendment, KB-32 preview form). KB-28 is the one class-B defect pattern in this family with standing confirmed instances — **all OPEN, section (e) class E**. KB-25/26/27 (sidebar/hamburger shapes): their render-confirmed instances are betwixt and marchen — **OPEN, section (e) class F**; the remaining machine-line instances are dispositioned in c2 under the KB-47 single-combo practice.
- KB-32..KB-51 (render cross-cutting family): every instance is dispositioned in c1/c2 by class — preview form (KB-32), static replica (KB-33), notice clipping (KB-34), header doubling (KB-35), WebKit badge glyph (KB-36), by-design specimens (KB-37), Sigma-9 baseline warn (KB-38), machine contrast false positives (KB-39), runtime host chain (KB-40), draft-host forms (KB-41), fetched-http assets (KB-42, in c1), transient 503 (KB-44), screenshot ceiling (KB-46), single-combo flakiness (KB-47), tag-state blank bodies (KB-48, 287 undecidable by design at the static layer), stale-cache caution (KB-49), hidden-rate recorded-only (KB-50). KB-53: the Sigma-10 environment form — see (d). KB-54: foreign-include named exceptions — see (d); the one carrier outside the named set is rima, **OPEN, section (e) item A2**. KB-57: pattern-9 = ruling 2. KB-58: deferred asset hosting. KB-59 (escaped @@[[footnoteblock]]@@ exhibit): 16 carriers (3 named + 13 port-convention); DISPOSITIONED as PENDING T2/T3 render evidence — a disposition with grounds, not a pass: no render row records a footnoteblock failure for any carrier, and the exhibit shape renders as the original’s documentation specimen where walked. KB-60: production license-box form uncertainty — do not convert (recorded). KB-62 (interwiki priority exposure): 62 exposed triage / 1 base-supplied (thalassophobia-sigma) / 44 undecidable — the charged instances were closed by the KB-07 fix waves; the residue is triage. KB-63 (license-box include forms): 7 FIXED by FIX4-LICENSE. KB-64: no standing charged instance beyond the KB-63/65 waves. KB-65 (duplicate @import lines, file-level hygiene): 40 hit files; FIXED by FIX4-MECH (29 files) and the mop-up commit 379eb44 (10 files, 16 lines), with the recorded keeps (skipos’s own /1 split pair; normal’s gated widget_layout_plus copies) DISPOSITIONED as deliberate.

Refinements to the zero-tag rows above (the generic line is replaced by these for the named themes):

- **theme:3law-pride-jp, theme:3lawcracked-jp, theme:512-onwards-jp, theme:5k-jp, theme:a-problematic-theme-jp**: the "theme CSS lives only inside iftags" structural suspicion is DISPOSITIONED per FIX3-S2EN §6.11 — the render reports did not confirm it; the themes render with their CSS applied. 512-onwards’ candidate-added hide rules were removed by FIX3-S2EN §5; a-problematic-theme’s XHTML 404 specimen page was removed by the same section.
- **theme:cleaning-services-jp, theme:cosmos-jp**: the duplicate Rate charges are FIXED (FIX3-S2EN §3 removals; assembly verification: cleaning-services no longer triggers the double-rate info, and cosmos’s standing info is its labelled @@ exhibit, deliberately kept per §6.9).
- **theme:twin-files-jp**: the local--code /1 delivery item is DISPOSITIONED — RENDER-S2-D §17’s later measurement shows both pages styled with no delivery defect, superseding the pre-reflect probe state behind LOCALIZE-S2-C item 6; the repoint to /8 was not executed and is recorded as not executed (a one-line posting-time check). Its pattern-7 item is OPEN → (e) D.
- **theme:telecom-office-theme-jp** (population fullname; ledger parts use the long form theme:telecommunications-monitoring-office-theme-jp): credit-notation nits only — DISPOSITIONED under the staff-normalization class (LOCALIZE-S2-C item 9).
- **theme:art-deco-jp**: the silently dropped sigma-plus base was restored and its false foundation line corrected (FIX3-S2EN §5); the toggle-sidebar note is DISPOSITIONED (no render-layer failure recorded for this theme’s sidebar).
- **theme:bedbugs-theme-jp, theme:black-market-jp, theme:black-serpent-jp**: the #6 interwiki registration-form items are DISPOSITIONED as staff-confirmation form items (the display-relevant interwiki defects for these themes — duplicate priority — were FIXED by FIX4-IWB; the frames render). Their #9 header items fall under ruling 2.
- **theme:blood-jp**: #9 header text → ruling 2; #7 font note marked 軽微 by the lane → recorded minor; the T5 stray-bracket items are recorded wording items without a display-affecting mark.
- **theme:cosmonaut-jp**: the lane heads its own row "display-unbreaking"; its items (a footer-sample credit line, a header-only JP font) are DISPOSITIONED on the lane’s own severity framing.

## (d) Exceptions list

1. **theme:amethyst-v2** — the named exception (GOSIGN-TESTS.md): the original is a shell of [[module ThemePreviewer]] plus external components and no standalone candidate could be produced. Excluded from the pass count; stated here explicitly. Its render row is NOT-RUN and its T1/LOCALIZE rows are the blank exception rows.
2. **theme:sigma-10-jp** — the Sigma-10 environment’s own row: no sample by construction (environment form); its standing no-credit / no-rate checker errors are the environment-form exception (KB-53; FIX-CREDIT-B row 37 exclusion, coordinator-dispositioned). It is counted as passing on the strength of that disposition.
3. **theme:min-theme-jp and theme:shushuin-jp** (JP originals) — T4/T5 are N/A by construction (structure confirmation instead, GOSIGN-TESTS.md). The KB-10/KB-07 charges against them are adjudicated false positives (FIX4-JPORIG, accepted in full): production min-theme carries a credit block and an interwiki include; production shushuin carries a credit block and no interwiki include, so both candidates are production-faithful. Their standing no-interwiki-style warnings are this exception’s form.
4. **KB-54 foreign-include named exceptions** — flopstyle-dark’s four lines (snippets:bs-image ×3, :scp-wiki:component:text-style; NOTFOUND-probed, no JP equivalent), foxtrot’s two author-label-source lines (no JP equivalent), opinions-broadcaster’s CN component set, dark-dealings’ and decom-dept’s author-label-source pairs (component port is a separate staff call, FIX3-S2EN §6.7), and peroxide’s 17 escaped documentation examples (FIX2-INCLUDE §5; its live delivery is the fragment:peroxide-jp-* candidate set). Rima is NOT in this set — see (e) A2.
5. **Credit-modal on preview pages** — a class disposition, not a per-theme exception: candidate/sample pages use credit:start-preview, which has no modal mechanism, so credit-modal errors there are the preview form’s property (GOSIGN-TESTS.md T2 note; ruling 5; KB-32; 282 sweep hits).
6. **Labelled paired Rate exhibits** — the pattern-3 exception (FIXPREP; FIX3-A1 §1.1): classic, flopstyle-dark, monotypical, much-cool, night-rush-theme, scheme, scpedia, y2k, cosmos (escaped @@ form, FIX3-S2EN §6.9), crayon (checker false positive inside the hidden iftags div, §6.10), shark-punching-centre-bhl, broken-world, horn, inland-empire, lead-by-example, the-other-side, pataphysics (its Rate only; its credit FORM is OPEN, (e) A3).
7. **KB-01 5k precedent** — theme:5k-jp’s single unencoded-colon occurrence is dispositioned under the pattern’s own precedent (the encoded form does not serve).
8. **FIX-P4 §9 named exceptions as adjudicated** — monotypical’s U1/U2 and broken-world’s U3 were named exceptions at FIX-P4 and were subsequently FIXED (FIX3-BF repoint to the basalt-jp normalize fragment; FIX3-BW fragment port + rewire); opinions-broadcaster’s U4 stands as a KB-54 exception; internal-affairs → theme:jakstyle/1 and shancheng → theme:fossil/1 were adjudicated posting-correct by the supervisor.
9. **Recorded keeps from the FIX4 mop-up (379eb44)** — skipos’s own /1 split @import pair and normal’s parameter-gated widget_layout_plus copies are deliberate, DISPOSITIONED with grounds in the mop-up report; shancheng’s un-deduplicated sigma-plus lines were accepted by the coordinator as behavior-identical.
10. **KB-59 footnoteblock exhibits** — 16 carriers of the @@[[footnoteblock]]@@ exhibit shape carry a PENDING-render-evidence disposition (a disposition with grounds, not a pass): no render row records a footnoteblock failure for any carrier.

## (e) Determination

Register totals: across c2 and c3 the ledger records 166 FIXED entries and 1075 DISPOSITIONED entries (segment/pattern-level entries; the class-level fix and disposition records of c1 and c4 stand on top of these). Against them stand **107 OPEN items over 88 themes**, enumerated verbatim below. Every OPEN item is BLOCKING under the go-sign standard (GOSIGN-TESTS.md: a theme passes only when every finding is fixed or dispositioned with grounds; the go-sign requires all themes to pass).

**Determination: the go-sign standard is NOT met.** Of the 286 pass-eligible themes (287 minus the amethyst-v2 named exception), 198 pass on this ledger and 88 carry at least one blocking OPEN item. The earlier withdrawal of the go-sign (2026-11-16, issued on the withdrawn '/start completion picture' standard) therefore stands: no go-sign can be issued until the items below are fixed or dispositioned with grounds by the coordinator.

OPEN items by class: A. Source-level blockers — 3; B. Duplicate bare Rate modules (pattern-3 FIX class, executed for other row sets only) — 19; C. Info-module residue / double credit furniture — 5; D. Pattern-7 JP font misses charged display-affecting — 20; E. KB-28 contrast pairings on candidate surfaces — 14; F. Sidebar/header functional defects — 12; G. Static credit replica misplacement — 1; H. Translation text, dead links and usage examples — 24; I. Structural deletions and non-sanctioned live delivery — 9.

### Blocking OPEN items (verbatim, in population order)

1. **[E] theme:blankstyle-jp** — Credit block text contrast 1.07 (near-white on near-white), machine-measured and recorded in the render row. KB-28 confirmed instance. No fix wave corrected a KB-28 binding and no original-faithful ground is recorded for these surfaces. [patterns/KB-28.md (class B theme defect; fix = correct the variable binding in the candidate); R/ledger-parts/RENDER-ROWS-RERUN16.md / RENDER-ROWS-1.md / RENDER-ROWS-2.md / RENDER-ROWS-G.md (per-theme rows)]
2. **[E] theme:minimalist-bhl-jp** — Section-15/parallel panel body text near-black on black, unreadable; the render lane records it as theme-specific. Same mechanism as KB-28. No fix wave corrected a KB-28 binding and no original-faithful ground is recorded for these surfaces. [patterns/KB-28.md (class B theme defect; fix = correct the variable binding in the candidate); R/ledger-parts/RENDER-ROWS-RERUN16.md / RENDER-ROWS-1.md / RENDER-ROWS-2.md / RENDER-ROWS-G.md (per-theme rows)]
3. **[A] theme:pataphysics-jp** — Wrong credit-module form: the candidate uses `credit:start` instead of `credit:start-preview`; the checker's `credit-not-preview` warning stands on this file alone in the whole population, and at posting the credit breaks inside the iftags block. LOCALIZE-B charged it display-affecting; FIX-CREDIT-B recorded the warning as out of its scope; no wave corrected the form. [R/REPORT-GOSIGN2-LOCALIZE-B.md (pataphysics row); R/REPORT-GOSIGN2-FIX-CREDIT-B.md (row 26 note); current checker run: credit-not-preview warn x1, population-unique]
4. **[D] theme:penumbra-jp** — LOCALIZE-B row: pattern 7, no JP face in any stack (display-affecting). Current file: 0 JP font stack references, no JP font load. Pattern 7 is a defined FIX class; the fix waves executed it for the Stage-1 rows, EN1-EN12 rows and the themes named in FIX4-LICENSE/REPOINT/IWB only. No disposition ground in the sources covers a missing JP face (it is not pattern 9, not an asset-host item, not a preview-form item). [R/GOSIGN2-T45-FIXPREP.md (pattern-7 FIX class); fix executions at FIX3-A1/A2/B, FIX3-S2EN.md section 4, FIX4-LICENSE (KB-04), FIX4-REPOINT (KB-16), FIX4-IWB (skipos); current canonical file (assembly-verified)]
5. **[A] theme:quand-le-soleil-se-couche** — KB-06 parameter defect: the candidate's own include passes no `sous-titre` argument and sets no default, so the literal text `{$sous-titre}` renders in the header on all views of both pages (render T3: 'real defect'). Still present at L107 of the current canonical file. The candidate's porter comment records that the SCP-JP hub documents the parameter contract; no fix wave supplied the argument, a default, or a removal, and SWEEP-A1 adjudicated quand the exception to the parameter-interface false-positive rule. [patterns/KB-06.md; R/sweep/SWEEP-A1.md; R/ledger-parts/RENDER-ROWS-1.md (quand row); current file pages/theme:quand-le-soleil-se-couche.txt L97-107]
6. **[D] theme:scp-human-resources-jp** — LOCALIZE-B row: pattern 7, header subtitle in a Latin-only face (display-affecting). Current file: no JP font named or loaded. Pattern 7 is a defined FIX class; the fix waves executed it for the Stage-1 rows, EN1-EN12 rows and the themes named in FIX4-LICENSE/REPOINT/IWB only. No disposition ground in the sources covers a missing JP face (it is not pattern 9, not an asset-host item, not a preview-form item). [R/GOSIGN2-T45-FIXPREP.md (pattern-7 FIX class); fix executions at FIX3-A1/A2/B, FIX3-S2EN.md section 4, FIX4-LICENSE (KB-04), FIX4-REPOINT (KB-16), FIX4-IWB (skipos); current canonical file (assembly-verified)]
7. **[D] theme:scp-offices-theme-jp** — LOCALIZE-B row: pattern 7, JP body text set in a Latin-only mono stack (display-affecting). Current file: no JP font named or loaded. Pattern 7 is a defined FIX class; the fix waves executed it for the Stage-1 rows, EN1-EN12 rows and the themes named in FIX4-LICENSE/REPOINT/IWB only. No disposition ground in the sources covers a missing JP face (it is not pattern 9, not an asset-host item, not a preview-form item). [R/GOSIGN2-T45-FIXPREP.md (pattern-7 FIX class); fix executions at FIX3-A1/A2/B, FIX3-S2EN.md section 4, FIX4-LICENSE (KB-04), FIX4-REPOINT (KB-16), FIX4-IWB (skipos); current canonical file (assembly-verified)]
8. **[G] theme:space-jp** — Static credit replica pinned at the viewport center on the sample (theme-sample interaction, both engines); the render lane calls it a real candidate defect. The candidate’s global .modalbox centering (KB-13) reaches the static replica. No fix wave touched this theme’s modalbox rules. [R/ledger-parts/RENDER-ROWS-1.md (space row); patterns/KB-13.md; patterns/KB-31.md sweep amendment (mechanism note)]
9. **[H] theme:space-jp** — Reader-visible prose carries an empty-text link to the unported name `component:sigma-plus` (current L31: 普遍的宇宙テーマは[[[component:sigma-plus|]]]テーマです), rendering a hole/red link in the sentence. Charged as the P11 untitled link (display-affecting) and listed as a leftover in FIX3-B section 5; FIX4-SIGMA repaired this theme’s sigma-plus include (the layout dependency) but not this prose link. [R/REPORT-GOSIGN2-LOCALIZE-B.md (space row); R/REPORT-GOSIGN2-FIX3-B.md section 5; current canonical file L31 (assembly-verified)]
10. **[D] theme:y2k-jp** — LOCALIZE-B row: pattern 7, no JP face anywhere (display-affecting). Current file: no font imports at all, no JP font named. Pattern 7 is a defined FIX class; the fix waves executed it for the Stage-1 rows, EN1-EN12 rows and the themes named in FIX4-LICENSE/REPOINT/IWB only. No disposition ground in the sources covers a missing JP face (it is not pattern 9, not an asset-host item, not a preview-form item). [R/GOSIGN2-T45-FIXPREP.md (pattern-7 FIX class); fix executions at FIX3-A1/A2/B, FIX3-S2EN.md section 4, FIX4-LICENSE (KB-04), FIX4-REPOINT (KB-16), FIX4-IWB (skipos); current canonical file (assembly-verified)]
11. **[H] theme:y2k-jp** — T5: untranslated English heading at L35 and untranslated collapsible labels at L116 stand in reader-visible text (pattern 10, charged display-affecting). FIX3-B’s edit to this file was the interwiki frame only. [R/REPORT-GOSIGN2-LOCALIZE-B.md (y2k row); R/REPORT-GOSIGN2-FIX3-B.md]
12. **[C] theme:y2k-jp** — Stray `info:start` line at L20 left in the credit area (pattern 3 residue, charged in the same row). No wave removed it. [R/REPORT-GOSIGN2-LOCALIZE-B.md (y2k row); current canonical file]
13. **[B] theme:yossistyle-jp** — Duplicate bare [[module Rate]] standing next to the preview credit module, which embeds its own rating module: the page renders two rating widgets. This is a defined FIX class (delete the bare module) that was executed for the Stage-1 and EN1-EN12 row sets but never for this row; the bare module is still in the current canonical file (assembly-verified, check_source.py double-rate info + file context). LOCALIZE-B row 44 (duplicate [[module Rate]], pattern 3, display-affecting); REPORT-GOSIGN2-FIX3-B.md section 5 lists it among items left for other lanes; no later wave removed it. Current L53. [R/GOSIGN2-T45-FIXPREP.md (FIX class: duplicate bare [[module Rate]]); fix executions at R/REPORT-GOSIGN2-FIX3-A1.md section 1, FIX3-A2, FIX3-S2EN.md section 3 (other row sets only); current file + ledger-assembly checker run]
14. **[H] theme:yossistyle-jp** — Reader-visible prose still links to EN scp-wiki pages where JP pages/candidates exist (current L60, L66: theme:magnus-web-format, theme:flopstyle, theme:blankstyle, theme:placestyle, component:croqstyle, component:rso, theme:black-highlighter-theme on scp-wiki.wikidot.com). Charged display-affecting (P11) and listed as a leftover in FIX3-B section 5; no wave repointed them. [R/REPORT-GOSIGN2-LOCALIZE-B.md (yossistyle row); R/REPORT-GOSIGN2-FIX3-B.md section 5; current canonical file L60/L66 (assembly-verified)]
15. **[E] theme:angel-jp** — Top-nav text near-white on light pink, unreadable at all widths; the render lane records it as candidate-specific and missed by the machine checks. Same mechanism as KB-28. No fix wave corrected a KB-28 binding and no original-faithful ground is recorded for these surfaces. [patterns/KB-28.md (class B theme defect; fix = correct the variable binding in the candidate); R/ledger-parts/RENDER-ROWS-RERUN16.md / RENDER-ROWS-1.md / RENDER-ROWS-2.md / RENDER-ROWS-G.md (per-theme rows)]
16. **[E] theme:eigenmachine-jp** — Section-29 warning-block text unreadable at chromium-375 (render T3). T3-recorded illegibility of candidate text; no fix wave corrected it and no original-faithful ground is recorded. (Recorded at one combo only; stated exactly so.) [patterns/KB-28.md (mechanism); R/ledger-parts/RENDER-ROWS-1.md (eigenmachine row)]
17. **[E] theme:febris-pharmaceuticals-theme-jp** — Section-15 panel body text unreadable at 375 (render T3). The section-15 specimen panel is the KB-28 confirmed surface class (magicity, sound). No fix wave corrected the pairing and no original-faithful ground is recorded. [patterns/KB-28.md; R/ledger-parts/RENDER-ROWS-G.md (febris-pharmaceuticals row)]
18. **[E] theme:fish-jp** — Section-15 series-panel body text near-black on navy, illegible at all 8 shots (render T3). Same mechanism as KB-28. No fix wave corrected a KB-28 binding and no original-faithful ground is recorded for these surfaces. [patterns/KB-28.md (class B theme defect; fix = correct the variable binding in the candidate); R/ledger-parts/RENDER-ROWS-RERUN16.md / RENDER-ROWS-1.md / RENDER-ROWS-2.md / RENDER-ROWS-G.md (per-theme rows)]
19. **[F] theme:frownstyle-jp** — PC-width header broken at 1366 in both engines: JP nav absent, wordmark clipped to “IN…”, auth buttons overprint the theme header; plus a blank .open-menu button and navy-on-navy opened-sidebar overprint (render T3). No fix, no disposition in the sources. [R/ledger-parts/RENDER-ROWS-RERUN16.md / RENDER-ROWS-1.md / RENDER-ROWS-2.md (per-theme rows)]
20. **[E] theme:linear-black-jp** — Body text and headings illegible white-on-white at all 8 combos on both pages (contrast min 1 / 1.61); the render lane calls it a candidate defect. Same mechanism as KB-28 (candidate’s own surface pairing). No fix wave corrected a KB-28 binding and no original-faithful ground is recorded for these surfaces. [patterns/KB-28.md (class B theme defect; fix = correct the variable binding in the candidate); R/ledger-parts/RENDER-ROWS-RERUN16.md / RENDER-ROWS-1.md / RENDER-ROWS-2.md / RENDER-ROWS-G.md (per-theme rows)]
21. **[E] theme:old-money-theme-jp** — Sample content panels: body text #F7F8F9 on #F4F4F4 (contrast ~1.0), both engines. RERUN16 T3 REAL FINDING (checklist section 1). KB-28 confirmed instance. No fix wave corrected a KB-28 binding and no original-faithful ground is recorded for these surfaces. [patterns/KB-28.md (class B theme defect; fix = correct the variable binding in the candidate); R/ledger-parts/RENDER-ROWS-RERUN16.md / RENDER-ROWS-1.md / RENDER-ROWS-2.md / RENDER-ROWS-G.md (per-theme rows)]
22. **[F] theme:queerstyle-jp** — Candidate header interference: the rainbow pride logo overprints the SCP財団 header wordmark and the account/search links at 375/320 in both engines (render T3). No fix, no disposition in the sources. [R/ledger-parts/RENDER-ROWS-RERUN16.md / RENDER-ROWS-1.md / RENDER-ROWS-2.md (per-theme rows)]
23. **[F] theme:queerstyle-jp** — Credit panel renders dark/blank at 1366 on the candidate page (render T3). The measurement predates FIX4-IWA’s interwiki-frame addition for this theme, but no wave addressed the blank credit panel by name and no re-measurement is recorded. [R/ledger-parts/RENDER-ROWS-2.md (queerstyle row); R/REPORT-GOSIGN2-FIX4-IWA.md (frame fix only)]
24. **[F] theme:raisa-jp** — Header interference: the RAISA ring logo overprints the header wordmark and account links at 375/320 in both engines (render T3) — the same candidate-header-interference shape as queerstyle’s. No fix, no disposition in the sources. [R/ledger-parts/RENDER-ROWS-1.md (raisa row)]
25. **[H] theme:retro-aiad-theme-jp** — Usage-example includes point at non-port page names on scp-jp (current L36 `theme:y2k`, L37 `theme:retro-aiad-theme`; the candidates are theme:y2k-jp and theme:retro-aiad-theme-jp): display-affecting for copy-paste, as charged. Still in the current file. [R/REPORT-GOSIGN2-LOCALIZE-S2-C.md (retro-aiad-theme row); current canonical file L36-37 (assembly-verified)]
26. **[B] theme:saphir-jp** — Duplicate bare [[module Rate]] standing next to the preview credit module, which embeds its own rating module: the page renders two rating widgets. This is a defined FIX class (delete the bare module) that was executed for the Stage-1 and EN1-EN12 row sets but never for this row; the bare module is still in the current canonical file (assembly-verified, check_source.py double-rate info + file context). LOCALIZE-S2-C row (live duplicate [[module Rate]] L204, display-affecting). Position note: the bare Rate sits inside the theme’s GoI format example block (current L210), away from the credit module at L24; the charging lane classed it a live duplicate and no wave removed it or recorded the specimen disposition. [R/GOSIGN2-T45-FIXPREP.md (FIX class: duplicate bare [[module Rate]]); fix executions at R/REPORT-GOSIGN2-FIX3-A1.md section 1, FIX3-A2, FIX3-S2EN.md section 3 (other row sets only); current file + ledger-assembly checker run]
27. **[B] theme:shattered-thoughts-jp** — Duplicate bare [[module Rate]] standing next to the preview credit module, which embeds its own rating module: the page renders two rating widgets. This is a defined FIX class (delete the bare module) that was executed for the Stage-1 and EN1-EN12 row sets but never for this row; the bare module is still in the current canonical file (assembly-verified, check_source.py double-rate info + file context). LOCALIZE-S2-C cross-cutting observation 3 (10 liveRate-duplicate rows): bare [[module Rate]] immediately after credit:end-preview, current L25. [R/GOSIGN2-T45-FIXPREP.md (FIX class: duplicate bare [[module Rate]]); fix executions at R/REPORT-GOSIGN2-FIX3-A1.md section 1, FIX3-A2, FIX3-S2EN.md section 3 (other row sets only); current file + ledger-assembly checker run]
28. **[D] theme:shattered-thoughts-jp** — LOCALIZE-S2-C checklist item 8: no JP font at all. Current file: no JP font named or loaded. Pattern 7 is a defined FIX class; the fix waves executed it for the Stage-1 rows, EN1-EN12 rows and the themes named in FIX4-LICENSE/REPOINT/IWB only. No disposition ground in the sources covers a missing JP face (it is not pattern 9, not an asset-host item, not a preview-form item). [R/GOSIGN2-T45-FIXPREP.md (pattern-7 FIX class); fix executions at FIX3-A1/A2/B, FIX3-S2EN.md section 4, FIX4-LICENSE (KB-04), FIX4-REPOINT (KB-16), FIX4-IWB (skipos); current canonical file (assembly-verified)]
29. **[B] theme:skiesmadestrange-jp** — Duplicate bare [[module Rate]] standing next to the preview credit module, which embeds its own rating module: the page renders two rating widgets. This is a defined FIX class (delete the bare module) that was executed for the Stage-1 and EN1-EN12 row sets but never for this row; the bare module is still in the current canonical file (assembly-verified, check_source.py double-rate info + file context). LOCALIZE-S2-C cross-cutting observation 3: bare [[module Rate]] in the credit flow, current L23. [R/GOSIGN2-T45-FIXPREP.md (FIX class: duplicate bare [[module Rate]]); fix executions at R/REPORT-GOSIGN2-FIX3-A1.md section 1, FIX3-A2, FIX3-S2EN.md section 3 (other row sets only); current file + ledger-assembly checker run]
30. **[B] theme:spidersfalling-jp** — Duplicate bare [[module Rate]] standing next to the preview credit module, which embeds its own rating module: the page renders two rating widgets. This is a defined FIX class (delete the bare module) that was executed for the Stage-1 and EN1-EN12 row sets but never for this row; the bare module is still in the current canonical file (assembly-verified, check_source.py double-rate info + file context). LOCALIZE-S2-C cross-cutting observation 3: bare [[module Rate]] in the credit flow, current L19. [R/GOSIGN2-T45-FIXPREP.md (FIX class: duplicate bare [[module Rate]]); fix executions at R/REPORT-GOSIGN2-FIX3-A1.md section 1, FIX3-A2, FIX3-S2EN.md section 3 (other row sets only); current file + ledger-assembly checker run]
31. **[D] theme:sunside-jp** — LOCALIZE-S2-C checklist item 8: stacks named, none loaded (JP glyphs fall back to OS default). Current file: Noto JP mentioned but no JP stack reference and no JP load. Pattern 7 is a defined FIX class; the fix waves executed it for the Stage-1 rows, EN1-EN12 rows and the themes named in FIX4-LICENSE/REPOINT/IWB only. No disposition ground in the sources covers a missing JP face (it is not pattern 9, not an asset-host item, not a preview-form item). [R/GOSIGN2-T45-FIXPREP.md (pattern-7 FIX class); fix executions at FIX3-A1/A2/B, FIX3-S2EN.md section 4, FIX4-LICENSE (KB-04), FIX4-REPOINT (KB-16), FIX4-IWB (skipos); current canonical file (assembly-verified)]
32. **[D] theme:tales-of-the-mosaic-jp** — LOCALIZE-S2-C checklist item 8: JP font named, never loaded. Current file: JP stack references exist but no JP font import loads the face. Pattern 7 is a defined FIX class; the fix waves executed it for the Stage-1 rows, EN1-EN12 rows and the themes named in FIX4-LICENSE/REPOINT/IWB only. No disposition ground in the sources covers a missing JP face (it is not pattern 9, not an asset-host item, not a preview-form item). [R/GOSIGN2-T45-FIXPREP.md (pattern-7 FIX class); fix executions at FIX3-A1/A2/B, FIX3-S2EN.md section 4, FIX4-LICENSE (KB-04), FIX4-REPOINT (KB-16), FIX4-IWB (skipos); current canonical file (assembly-verified)]
33. **[H] theme:the-foundation-sigma-jp** — Usage example points at nonexistent `theme:the-foundation-sigma` (current L30) while the candidate is theme:the-foundation-sigma-jp: copy-paste 404, charged display-affecting. Still in the current file. (This theme’s local--code /1 delivery item is separately dispositioned as a posting-procedure item in c3.) [R/REPORT-GOSIGN2-LOCALIZE-S2-C.md (the-foundation-sigma row); current canonical file L30 (assembly-verified)]
34. **[D] theme:twin-files-jp** — LOCALIZE-S2-C checklist item 8: JP font named, never loaded. Current file: Noto JP mentioned, no JP load. (This theme’s local--code /1 item is separately dispositioned in the register; the font item is not covered by that disposition.) Pattern 7 is a defined FIX class; the fix waves executed it for the Stage-1 rows, EN1-EN12 rows and the themes named in FIX4-LICENSE/REPOINT/IWB only. No disposition ground in the sources covers a missing JP face (it is not pattern 9, not an asset-host item, not a preview-form item). [R/GOSIGN2-T45-FIXPREP.md (pattern-7 FIX class); fix executions at FIX3-A1/A2/B, FIX3-S2EN.md section 4, FIX4-LICENSE (KB-04), FIX4-REPOINT (KB-16), FIX4-IWB (skipos); current canonical file (assembly-verified)]
35. **[D] theme:ui-jp** — LOCALIZE-S2-C row: pattern 7, no JP font anywhere; Arial-only (display-affecting). Current file: no font imports, no JP font named. Pattern 7 is a defined FIX class; the fix waves executed it for the Stage-1 rows, EN1-EN12 rows and the themes named in FIX4-LICENSE/REPOINT/IWB only. No disposition ground in the sources covers a missing JP face (it is not pattern 9, not an asset-host item, not a preview-form item). [R/GOSIGN2-T45-FIXPREP.md (pattern-7 FIX class); fix executions at FIX3-A1/A2/B, FIX3-S2EN.md section 4, FIX4-LICENSE (KB-04), FIX4-REPOINT (KB-16), FIX4-IWB (skipos); current canonical file (assembly-verified)]
36. **[D] theme:uiu-bhl-theme-jp** — LOCALIZE-S2-C checklist item 8: mono stack is Latin-only. Current file: no JP stack reference, no JP load. Pattern 7 is a defined FIX class; the fix waves executed it for the Stage-1 rows, EN1-EN12 rows and the themes named in FIX4-LICENSE/REPOINT/IWB only. No disposition ground in the sources covers a missing JP face (it is not pattern 9, not an asset-host item, not a preview-form item). [R/GOSIGN2-T45-FIXPREP.md (pattern-7 FIX class); fix executions at FIX3-A1/A2/B, FIX3-S2EN.md section 4, FIX4-LICENSE (KB-04), FIX4-REPOINT (KB-16), FIX4-IWB (skipos); current canonical file (assembly-verified)]
37. **[B] theme:vanguard-jp** — Duplicate bare [[module Rate]] standing next to the preview credit module, which embeds its own rating module: the page renders two rating widgets. This is a defined FIX class (delete the bare module) that was executed for the Stage-1 and EN1-EN12 row sets but never for this row; the bare module is still in the current canonical file (assembly-verified, check_source.py double-rate info + file context). LOCALIZE-S2-C cross-cutting observation 3: bare [[module Rate]] immediately before credit:start-preview, current L22. LOCALIZE-S2-C item 14 leaves this theme’s bare rate as an unmade staff call under the exhibit-exception reading. [R/GOSIGN2-T45-FIXPREP.md (FIX class: duplicate bare [[module Rate]]); fix executions at R/REPORT-GOSIGN2-FIX3-A1.md section 1, FIX3-A2, FIX3-S2EN.md section 3 (other row sets only); current file + ledger-assembly checker run]
38. **[B] theme:vanguard-supplement-jp** — Duplicate bare [[module Rate]] standing next to the preview credit module, which embeds its own rating module: the page renders two rating widgets. This is a defined FIX class (delete the bare module) that was executed for the Stage-1 and EN1-EN12 row sets but never for this row; the bare module is still in the current canonical file (assembly-verified, check_source.py double-rate info + file context). LOCALIZE-S2-C row + item 14: live [[module rate]] duplicating the credit-embedded Rate (pattern 3). The rate carries a **評価:** label (current L20-21) but the lane itself left it as an unmade staff call, and it is not the Classic-class labelled pair (no クレジットモジュール仙き評価 counterpart label). [R/GOSIGN2-T45-FIXPREP.md (FIX class: duplicate bare [[module Rate]]); fix executions at R/REPORT-GOSIGN2-FIX3-A1.md section 1, FIX3-A2, FIX3-S2EN.md section 3 (other row sets only); current file + ledger-assembly checker run]
39. **[B] theme:wilderness-jp** — Duplicate bare [[module Rate]] standing next to the preview credit module, which embeds its own rating module: the page renders two rating widgets. This is a defined FIX class (delete the bare module) that was executed for the Stage-1 and EN1-EN12 row sets but never for this row; the bare module is still in the current canonical file (assembly-verified, check_source.py double-rate info + file context). LOCALIZE-S2-C cross-cutting observation 3: bare [[module Rate]] in the credit flow, current L18. [R/GOSIGN2-T45-FIXPREP.md (FIX class: duplicate bare [[module Rate]]); fix executions at R/REPORT-GOSIGN2-FIX3-A1.md section 1, FIX3-A2, FIX3-S2EN.md section 3 (other row sets only); current file + ledger-assembly checker run]
40. **[B] theme:wondertainment-jp** — Duplicate bare [[module Rate]] standing next to the preview credit module, which embeds its own rating module: the page renders two rating widgets. This is a defined FIX class (delete the bare module) that was executed for the Stage-1 and EN1-EN12 row sets but never for this row; the bare module is still in the current canonical file (assembly-verified, check_source.py double-rate info + file context). LOCALIZE-S2-C cross-cutting observation 3: bare [[module Rate]] in the credit flow, current L12. [R/GOSIGN2-T45-FIXPREP.md (FIX class: duplicate bare [[module Rate]]); fix executions at R/REPORT-GOSIGN2-FIX3-A1.md section 1, FIX3-A2, FIX3-S2EN.md section 3 (other row sets only); current file + ledger-assembly checker run]
41. **[B] theme:words-of-wisdom-jp** — Duplicate bare [[module Rate]] standing next to the preview credit module, which embeds its own rating module: the page renders two rating widgets. This is a defined FIX class (delete the bare module) that was executed for the Stage-1 and EN1-EN12 row sets but never for this row; the bare module is still in the current canonical file (assembly-verified, check_source.py double-rate info + file context). LOCALIZE-S2-C row + item 14: live duplicate [[module Rate]] (pattern 3, display-affecting), current L9, immediately before credit:start-preview; left as an unmade staff call by the lane. [R/GOSIGN2-T45-FIXPREP.md (FIX class: duplicate bare [[module Rate]]); fix executions at R/REPORT-GOSIGN2-FIX3-A1.md section 1, FIX3-A2, FIX3-S2EN.md section 3 (other row sets only); current file + ledger-assembly checker run]
42. **[H] theme:writing-anomalies-jp** — Usage example targets a page name that will never exist on scp-jp: L33 reads `[[include :scp-jp:theme:writing-anomalies]]` (probed 404) while the candidate itself is theme:writing-anomalies-jp. Charged display-affecting once posted (copy-paste 404). Still in the current file. [R/REPORT-GOSIGN2-LOCALIZE-S2-C.md (writing-anomalies row); current canonical file L33 (assembly-verified)]
43. **[H] theme:andesite-jp** — Reader-visible UI labels stand in Chinese in the candidate’s CSS content: strings (current file: 特殊收容措施 / 描述 / 标签 / 页面信息 — the containment-procedures, description, tags and page-info chrome labels). Charged as the row’s main display-affecting item (a). These are chrome UI text, not header/title text, so ruling 2 does not cover them. (The same row’s pattern-9 header variables and pattern-5 hosts are dispositioned in c3.) [R/REPORT-GOSIGN2-LOCALIZE-S2-D.md (andesite row + pattern table); current canonical file (assembly-verified)]
44. **[H] theme:andesite-jp** — Prose links still lead to the CN site / a personal wiki where JP counterparts exist (current L50 theme:basalt, L52 component:sigma-plus, L56 component:betterbetterfootnote on scp-wiki-cn / fendsfox). Charged MISSED under pattern 11; the JP candidates theme:basalt-jp, component:sigma-plus-jp and component:betterbetterfootnote-jp all exist. No wave repointed them. [R/REPORT-GOSIGN2-LOCALIZE-S2-D.md (andesite pattern table, #11); current canonical file L50–L56 (assembly-verified)]
45. **[F] theme:betwixt-jp** — WebKit-specific REAL FINDING on both pages: the mobile sidebar-open hamburger renders in Chromium but is entirely absent in WebKit at 375x812 and 320x640, leaving no visible way to open the sidebar (screenshot-confirmed; machine sidebar-unreachable on all four mobile combos). No fix, no disposition in the sources. [R/ledger-parts/RENDER-ROWS-RERUN16.md / RENDER-ROWS-1.md / RENDER-ROWS-2.md (per-theme rows)]
46. **[I] theme:brokedown-database-jp** — Documented feature blocks missing: the original’s implementation blocks for the `no-animation` and `my-logo` arguments (original L1623–1698) were not ported; the candidate’s guide (L44–60) documents both options but they have no effect (assembly-verified: each name occurs once in the current file, in the documentation only). The same row charges the deletion of the photosensitivity warning block. No wave restored either. [R/REPORT-GOSIGN2-LOCALIZE-S2-D.md (brokedown-database row); current canonical file (assembly-verified)]
47. **[F] theme:cobalt-aero-glass-jp** — Candidate page sidebar-unreachable at <=375 in both engines (machine finding on every mobile combo); no T3 clearance recorded and no fix wave addressed it. [R/ledger-parts/RENDER-ROWS-RERUN16.md / RENDER-ROWS-1.md / RENDER-ROWS-2.md (per-theme rows)]
48. **[B] theme:copper-jp** — Duplicate bare [[module Rate]] standing next to the preview credit module, which embeds its own rating module: the page renders two rating widgets. This is a defined FIX class (delete the bare module) that was executed for the Stage-1 and EN1-EN12 row sets but never for this row; the bare module is still in the current canonical file (assembly-verified, check_source.py double-rate info + file context). LOCALIZE-S2-D row: 評価 UI 二重化 (L52-54, display-affecting). Current L59, bare, after the credit block. [R/GOSIGN2-T45-FIXPREP.md (FIX class: duplicate bare [[module Rate]]); fix executions at R/REPORT-GOSIGN2-FIX3-A1.md section 1, FIX3-A2, FIX3-S2EN.md section 3 (other row sets only); current file + ledger-assembly checker run]
49. **[B] theme:crt-jp** — Duplicate bare [[module Rate]] standing next to the preview credit module, which embeds its own rating module: the page renders two rating widgets. This is a defined FIX class (delete the bare module) that was executed for the Stage-1 and EN1-EN12 row sets but never for this row; the bare module is still in the current canonical file (assembly-verified, check_source.py double-rate info + file context). LOCALIZE-S2-D row: 評価 UI 二重化 (L2343 area); the lane’s own closing line requires Rate-duplicate removal before posting. Current L2354. [R/GOSIGN2-T45-FIXPREP.md (FIX class: duplicate bare [[module Rate]]); fix executions at R/REPORT-GOSIGN2-FIX3-A1.md section 1, FIX3-A2, FIX3-S2EN.md section 3 (other row sets only); current file + ledger-assembly checker run]
50. **[B] theme:darkblue-jp** — Duplicate bare [[module Rate]] standing next to the preview credit module, which embeds its own rating module: the page renders two rating widgets. This is a defined FIX class (delete the bare module) that was executed for the Stage-1 and EN1-EN12 row sets but never for this row; the bare module is still in the current canonical file (assembly-verified, check_source.py double-rate info + file context). LOCALIZE-S2-D row: Rate 二重化 (型 3). Current L29. [R/GOSIGN2-T45-FIXPREP.md (FIX class: duplicate bare [[module Rate]]); fix executions at R/REPORT-GOSIGN2-FIX3-A1.md section 1, FIX3-A2, FIX3-S2EN.md section 3 (other row sets only); current file + ledger-assembly checker run]
51. **[D] theme:darkblue-jp** — LOCALIZE-S2-D row: pattern 7, JP font completely absent (表示影響あり). Current file: no JP font stack reference, no JP load. Pattern 7 is a defined FIX class; the fix waves executed it for the Stage-1 rows, EN1-EN12 rows and the themes named in FIX4-LICENSE/REPOINT/IWB only. No disposition ground in the sources covers a missing JP face (it is not pattern 9, not an asset-host item, not a preview-form item). [R/GOSIGN2-T45-FIXPREP.md (pattern-7 FIX class); fix executions at FIX3-A1/A2/B, FIX3-S2EN.md section 4, FIX4-LICENSE (KB-04), FIX4-REPOINT (KB-16), FIX4-IWB (skipos); current canonical file (assembly-verified)]
52. **[F] theme:darkblue-jp** — Sample sidebar-unreachable at <=375 in both engines (machine finding on every mobile combo); no T3 clearance recorded and no fix wave addressed it. [R/ledger-parts/RENDER-ROWS-RERUN16.md / RENDER-ROWS-1.md / RENDER-ROWS-2.md (per-theme rows)]
53. **[B] theme:decay-jp** — Duplicate bare [[module Rate]] standing next to the preview credit module, which embeds its own rating module: the page renders two rating widgets. This is a defined FIX class (delete the bare module) that was executed for the Stage-1 and EN1-EN12 row sets but never for this row; the bare module is still in the current canonical file (assembly-verified, check_source.py double-rate info + file context). LOCALIZE-S2-D row: Rate 二重化 (型 3). Current L23. [R/GOSIGN2-T45-FIXPREP.md (FIX class: duplicate bare [[module Rate]]); fix executions at R/REPORT-GOSIGN2-FIX3-A1.md section 1, FIX3-A2, FIX3-S2EN.md section 3 (other row sets only); current file + ledger-assembly checker run]
54. **[B] theme:deepspace-jp** — Duplicate bare [[module Rate]] standing next to the preview credit module, which embeds its own rating module: the page renders two rating widgets. This is a defined FIX class (delete the bare module) that was executed for the Stage-1 and EN1-EN12 row sets but never for this row; the bare module is still in the current canonical file (assembly-verified, check_source.py double-rate info + file context). LOCALIZE-S2-D row: Rate 二重化 (型 3). Current L286. [R/GOSIGN2-T45-FIXPREP.md (FIX class: duplicate bare [[module Rate]]); fix executions at R/REPORT-GOSIGN2-FIX3-A1.md section 1, FIX3-A2, FIX3-S2EN.md section 3 (other row sets only); current file + ledger-assembly checker run]
55. **[I] theme:drunken-alley-jp** — The golden-wind base prerequisite was deleted from the usage procedure (original L22) and is supplied nowhere: the current file contains no golden-wind reference at all, so a user following the candidate’s instructions applies the add-on without its required base. Charged as the row’s headline item; FIX4-IWA’s edits to this file (interwiki frame, dead url() removal) did not restore it. [R/REPORT-GOSIGN2-LOCALIZE-S2-D.md (drunken-alley row); current canonical file (assembly-verified)]
56. **[D] theme:fmd-bhl-theme-jp** — LOCALIZE-S2-D row: pattern 7, JP font not loaded, listed in the row’s display-affecting set. No fix wave loaded a JP face for this candidate. Pattern 7 is a defined FIX class; the fix waves executed it for the Stage-1 rows, EN1-EN12 rows and the themes named in FIX4-LICENSE/REPOINT/IWB only. No disposition ground in the sources covers a missing JP face (it is not pattern 9, not an asset-host item, not a preview-form item). [R/GOSIGN2-T45-FIXPREP.md (pattern-7 FIX class); fix executions at FIX3-A1/A2/B, FIX3-S2EN.md section 4, FIX4-LICENSE (KB-04), FIX4-REPOINT (KB-16), FIX4-IWB (skipos); current canonical file (assembly-verified)]
57. **[D] theme:frutiger-aero-jp** — LOCALIZE-S2-D row: pattern 7 in the display-affecting set (JP font not provided). Current file: no font imports, no JP font named. Pattern 7 is a defined FIX class; the fix waves executed it for the Stage-1 rows, EN1-EN12 rows and the themes named in FIX4-LICENSE/REPOINT/IWB only. No disposition ground in the sources covers a missing JP face (it is not pattern 9, not an asset-host item, not a preview-form item). [R/GOSIGN2-T45-FIXPREP.md (pattern-7 FIX class); fix executions at FIX3-A1/A2/B, FIX3-S2EN.md section 4, FIX4-LICENSE (KB-04), FIX4-REPOINT (KB-16), FIX4-IWB (skipos); current canonical file (assembly-verified)]
58. **[D] theme:golden-wind-jp** — LOCALIZE-S2-D row: pattern 7, JP fonts declared but unused, JP text falls back to OS fonts (display-affecting set). Current state: Noto Sans JP / Noto Serif JP are now loaded via Google Fonts imports, but no font-family stack references them; the display stacks name CN OS faces (华文新魏 / 华文楷体, current L121/L138/L148), which JP readers’ machines do not carry. Pattern 7 is a defined FIX class; the fix waves executed it for the Stage-1 rows, EN1-EN12 rows and the themes named in FIX4-LICENSE/REPOINT/IWB only. No disposition ground in the sources covers a missing JP face (it is not pattern 9, not an asset-host item, not a preview-form item). [R/GOSIGN2-T45-FIXPREP.md (pattern-7 FIX class); fix executions at FIX3-A1/A2/B, FIX3-S2EN.md section 4, FIX4-LICENSE (KB-04), FIX4-REPOINT (KB-16), FIX4-IWB (skipos); current canonical file (assembly-verified)]
59. **[H] theme:gp-refresh-jp** — T5: the original’s usage examples and specimens (heading-generation button, tab view, tables, colour demos, font credits, about 190 lines) were deleted wholesale instead of translated; the charging lane records this as directly conflicting with the display-test requirement that themes ship their specimens. No wave restored the section. [R/REPORT-GOSIGN2-LOCALIZE-S2-E.md (gp-refresh row, T5 finding 1)]
60. **[D] theme:greyday-jp** — Broken body font reference (pattern 7, MISSED in substance): the body stack names ‘NotoSansSC-Light’ (current L378), a family that is loaded nowhere — the file’s own comment records that its load was deleted and replaced by ‘Noto Sans SC’, which the body stack does not name. Body JP text therefore matches no loaded face and falls back to the browser default (lane-graded display impact: medium). [R/REPORT-GOSIGN2-LOCALIZE-S2-D.md (greyday pattern table, #7); current canonical file L378 (assembly-verified)]
61. **[H] theme:greyday-jp** — Untranslated Chinese edit-lock text stands in the candidate’s CSS (div#lock-info::before/::after content:, current L1355/L1367/L1372 — the exclusive-lock and saving-page messages shown to editors). This is the KB-18 surface class; the one charged instance the campaign repaired (petrifaction) was repaired by translation. No wave translated greyday’s. [R/REPORT-GOSIGN2-LOCALIZE-S2-D.md (greyday pattern table, #9); patterns/KB-18.md; current canonical file (assembly-verified)]
62. **[B] theme:ink-jp** — Duplicate bare [[module Rate]] standing next to the preview credit module, which embeds its own rating module: the page renders two rating widgets. This is a defined FIX class (delete the bare module) that was executed for the Stage-1 and EN1-EN12 row sets but never for this row; the bare module is still in the current canonical file (assembly-verified, check_source.py double-rate info + file context). LOCALIZE-S2-D row: two live bare Rates (L1701/L1944) duplicating the credit-embedded Rate (pattern 3, display-affecting). Both still present. [R/GOSIGN2-T45-FIXPREP.md (FIX class: duplicate bare [[module Rate]]); fix executions at R/REPORT-GOSIGN2-FIX3-A1.md section 1, FIX3-A2, FIX3-S2EN.md section 3 (other row sets only); current file + ledger-assembly checker run]
63. **[B] theme:kitchen-jp** — Duplicate bare [[module Rate]] standing next to the preview credit module, which embeds its own rating module: the page renders two rating widgets. This is a defined FIX class (delete the bare module) that was executed for the Stage-1 and EN1-EN12 row sets but never for this row; the bare module is still in the current canonical file (assembly-verified, check_source.py double-rate info + file context). LOCALIZE-S2-D row: pattern 3, bare Rate at L39 immediately before the credit block (current L39). [R/GOSIGN2-T45-FIXPREP.md (FIX class: duplicate bare [[module Rate]]); fix executions at R/REPORT-GOSIGN2-FIX3-A1.md section 1, FIX3-A2, FIX3-S2EN.md section 3 (other row sets only); current file + ledger-assembly checker run]
64. **[E] theme:kitchen-jp** — Body text on BOTH pages: near-white rgb(254,254,254) on the pale-pink --BG (244,240,240), contrast 1.06. RERUN16 T3 REAL FINDING; the row records the canonical source has no white body-text rule, so this is the port’s variable binding, not an intended aesthetic. KB-28 confirmed instance. No fix wave corrected a KB-28 binding and no original-faithful ground is recorded for these surfaces. [patterns/KB-28.md (class B theme defect; fix = correct the variable binding in the candidate); R/ledger-parts/RENDER-ROWS-RERUN16.md / RENDER-ROWS-1.md / RENDER-ROWS-2.md / RENDER-ROWS-G.md (per-theme rows)]
65. **[H] theme:magazine-jp** — T5: reader-visible untranslated residue at three places (L7158, L7268/L7272, L7121, pattern 10). The lane records them as mechanically fixable before posting, but no wave fixed them and T5’s pass bar is that no untranslated reader-visible text stands. [R/REPORT-GOSIGN2-LOCALIZE-S2-F.md (magazine row); R/GOSIGN-TESTS.md (T5 definition)]
66. **[E] theme:magicity-jp** — Sample panels: near-black text on dark navy, effectively unreadable. RERUN16 T3 REAL FINDING. KB-28 confirmed instance. No fix wave corrected a KB-28 binding and no original-faithful ground is recorded for these surfaces. [patterns/KB-28.md (class B theme defect; fix = correct the variable binding in the candidate); R/ledger-parts/RENDER-ROWS-RERUN16.md / RENDER-ROWS-1.md / RENDER-ROWS-2.md / RENDER-ROWS-G.md (per-theme rows)]
67. **[F] theme:marchen-jp** — WebKit at 1366x768: the hamburger is present but inert on both pages (Chromium opens; mobile widths open in both engines). RERUN16 T3 REAL FINDING. No fix, no disposition in the sources. [R/ledger-parts/RENDER-ROWS-RERUN16.md / RENDER-ROWS-1.md / RENDER-ROWS-2.md (per-theme rows)]
68. **[D] theme:paradigm-inapplicable-jp** — LOCALIZE-S2-E row: pattern 7, JP font named but never loaded, in the FINDINGS (display/delivery-affecting) set. Current file: 0 Google Fonts imports. Pattern 7 is a defined FIX class; the fix waves executed it for the Stage-1 rows, EN1-EN12 rows and the themes named in FIX4-LICENSE/REPOINT/IWB only. No disposition ground in the sources covers a missing JP face (it is not pattern 9, not an asset-host item, not a preview-form item). [R/GOSIGN2-T45-FIXPREP.md (pattern-7 FIX class); fix executions at FIX3-A1/A2/B, FIX3-S2EN.md section 4, FIX4-LICENSE (KB-04), FIX4-REPOINT (KB-16), FIX4-IWB (skipos); current canonical file (assembly-verified)]
69. **[D] theme:paradigm-inapplicable-sigma-jp** — LOCALIZE-S2-E row: pattern 7, JP font never loaded, in the FINDINGS (publication-affecting) set. Current file: 0 Google Fonts imports. Pattern 7 is a defined FIX class; the fix waves executed it for the Stage-1 rows, EN1-EN12 rows and the themes named in FIX4-LICENSE/REPOINT/IWB only. No disposition ground in the sources covers a missing JP face (it is not pattern 9, not an asset-host item, not a preview-form item). [R/GOSIGN2-T45-FIXPREP.md (pattern-7 FIX class); fix executions at FIX3-A1/A2/B, FIX3-S2EN.md section 4, FIX4-LICENSE (KB-04), FIX4-REPOINT (KB-16), FIX4-IWB (skipos); current canonical file (assembly-verified)]
70. **[D] theme:paradigm-reconstruction-jp** — LOCALIZE-S2-E row: pattern 7, JP font never loaded, in the FINDINGS set. Current file: 0 Google Fonts imports. Pattern 7 is a defined FIX class; the fix waves executed it for the Stage-1 rows, EN1-EN12 rows and the themes named in FIX4-LICENSE/REPOINT/IWB only. No disposition ground in the sources covers a missing JP face (it is not pattern 9, not an asset-host item, not a preview-form item). [R/GOSIGN2-T45-FIXPREP.md (pattern-7 FIX class); fix executions at FIX3-A1/A2/B, FIX3-S2EN.md section 4, FIX4-LICENSE (KB-04), FIX4-REPOINT (KB-16), FIX4-IWB (skipos); current canonical file (assembly-verified)]
71. **[B] theme:peroxide-jp** — Duplicate bare [[module Rate]] standing next to the preview credit module, which embeds its own rating module: the page renders two rating widgets. This is a defined FIX class (delete the bare module) that was executed for the Stage-1 and EN1-EN12 row sets but never for this row; the bare module is still in the current canonical file (assembly-verified, check_source.py double-rate info + file context). LOCALIZE-S2-E row: Rate duplication (L140 x credit) charged as a minor spec violation (軽微だが仕様違反). Current L140, bare, immediately before credit:start-preview. [R/GOSIGN2-T45-FIXPREP.md (FIX class: duplicate bare [[module Rate]]); fix executions at R/REPORT-GOSIGN2-FIX3-A1.md section 1, FIX3-A2, FIX3-S2EN.md section 3 (other row sets only); current file + ledger-assembly checker run]
72. **[B] theme:progress-institute-jp** — Duplicate bare [[module Rate]] standing next to the preview credit module, which embeds its own rating module: the page renders two rating widgets. This is a defined FIX class (delete the bare module) that was executed for the Stage-1 and EN1-EN12 row sets but never for this row; the bare module is still in the current canonical file (assembly-verified, check_source.py double-rate info + file context). LOCALIZE-S2-E row: pattern 3 Rate duplication (L130 x credit Rate L133-145). Current L130, bare, immediately before the credit block. [R/GOSIGN2-T45-FIXPREP.md (FIX class: duplicate bare [[module Rate]]); fix executions at R/REPORT-GOSIGN2-FIX3-A1.md section 1, FIX3-A2, FIX3-S2EN.md section 3 (other row sets only); current file + ledger-assembly checker run]
73. **[A] theme:rima-jp** — Live foreign includes `:semimonth:component:excerpts-tool` x3 (L311/L317/L322). The component has no JP counterpart (NOTFOUND-probed) and the theme page will show three error boxes once posted. FIX2-INCLUDE section 5 states verbatim that this is 'a live posting blocker' and that 'Staff/coordinator adjudication required before go-sign'; no later report or adjudication names rima, and KB-54's named-exception set does not include it. [R/REPORT-GOSIGN2-FIX2-INCLUDE.md section 5; patterns/KB-54.md (named set, rima absent); current checker run: foreign-include x3 on this file]
74. **[F] theme:rima-jp** — Machine finding `sidebar-unreachable` on all 4 mobile combos (chromium/webkit x 375/320) on the candidate page; no T3 clearance recorded and no fix wave addressed it. [R/ledger-parts/RENDER-ROWS-2.md (rima row)]
75. **[H] theme:sci-fi-jp** — Dead prose link to the `sci-fi-hub` page (current L204), which does not exist on scp-jp. Charged under P11. (This theme’s interwiki duplicate-priority defect was fixed by FIX4-IWB; the `[href*=scp-wiki-cn]` selector note in the same row is dispositioned in c3 — the render walk records both pages clean and the selector is inert for JP-internal links.) [R/REPORT-GOSIGN2-LOCALIZE-S2-E.md (CN13-1 sci-fi row); current canonical file L204 (assembly-verified)]
76. **[H] theme:scpdeclassified-jp** — Dead prose link to the `scpdeclassified` hub (current L28), which does not exist on scp-jp. Charged under P11 and in the lane’s cross-cutting dead-target list (item 7). [R/REPORT-GOSIGN2-LOCALIZE-S2-E.md (CN13-2 row + cross-cutting item 7); current canonical file L28 (assembly-verified)]
77. **[D] theme:scpdeclassified-jp** — Pattern 7 in substance: the stacks set JP text in Noto Sans SC / Noto Serif SC (current L160–L169, mainland forms), and the JP faces the documentation claims appear only inside the [[code]] exhibit, which does not deliver them. Charged under P7 with a false font claim at L131. No wave rewired the stacks. [R/REPORT-GOSIGN2-LOCALIZE-S2-E.md (CN13-2 scpdeclassified row); current canonical file (assembly-verified)]
78. **[H] theme:scplive-jp** — Dead prose link to `scplive-foundation-idol-project` (current L22), which does not exist on scp-jp. Charged under P11 and in the lane’s cross-cutting dead-target list (item 7). [R/REPORT-GOSIGN2-LOCALIZE-S2-E.md (CN13-3 row + cross-cutting item 7); current canonical file L22 (assembly-verified)]
79. **[D] theme:scplive-jp** — Pattern 7 in substance: the body font-family names “等线” (DengXian, a Chinese system font, current L189), which is loaded nowhere and which JP readers’ machines do not carry, so body text falls back unstyled by the theme. Charged under P7. No wave rewired it. [R/REPORT-GOSIGN2-LOCALIZE-S2-E.md (CN13-3 scplive row); current canonical file L189 (assembly-verified)]
80. **[H] theme:shancheng-jp** — A Chinese chrome label stands in the candidate’s CSS (current L1270: content: “标签” — the tags label). Charged under pattern 9 in the row’s summary; as chrome UI text rather than header/title text it is not covered by ruling 2 (compare the andesite item). FIX4-SIGMA repointed this theme’s sigma-plus includes; the content: string was not touched. [R/REPORT-GOSIGN2-LOCALIZE-S2-E.md (CN13-4 shancheng row); current canonical file L1270 (assembly-verified)]
81. **[I] theme:share-future-community-jp** — Live delivery from the author’s personal domain stands as the theme’s first CSS import (current L3: hoah.backroomswiki.cn). Charged as a blocking pattern-4 item. FIX4-CREDIT repaired this theme’s credit block and repointed its sigma-plus include, but the personal-domain import was not repointed or rehosted. (Not in the FIX-P4 set or the KB-14 verbatim-import set.) [R/REPORT-GOSIGN2-LOCALIZE-S2-E.md (CN13-5 share-future-community row); current canonical file L3 (assembly-verified)]
82. **[H] theme:shivering-night-jp** — Dead prose links at L86: `theme:basalt`, `theme:parallel`, `theme:aero-glass` and `k-s-g-hub`, none of which exist on scp-jp under those names (the candidates are theme:basalt-jp, theme:parallel-jp, theme:aero-glass-jp). Charged in the row (dead bare links, 404). Its credit-field items were fixed by the credit waves; the links were not. [R/REPORT-GOSIGN2-LOCALIZE-S2-E.md (CN14-1 shivering-night row); current canonical file L86 (assembly-verified)]
83. **[E] theme:sodium-jp** — Rating clear-vote control: near-white on white, effectively invisible (render T3, both pages). KB-28 confirmed instance. No fix wave corrected a KB-28 binding and no original-faithful ground is recorded for these surfaces. [patterns/KB-28.md (class B theme defect; fix = correct the variable binding in the candidate); R/ledger-parts/RENDER-ROWS-RERUN16.md / RENDER-ROWS-1.md / RENDER-ROWS-2.md / RENDER-ROWS-G.md (per-theme rows)]
84. **[E] theme:sound-jp** — Sample section 15/16 panels: near-white text on light ground, effectively unreadable (render T3). KB-28 confirmed instance. No fix wave corrected a KB-28 binding and no original-faithful ground is recorded for these surfaces. [patterns/KB-28.md (class B theme defect; fix = correct the variable binding in the candidate); R/ledger-parts/RENDER-ROWS-RERUN16.md / RENDER-ROWS-1.md / RENDER-ROWS-2.md / RENDER-ROWS-G.md (per-theme rows)]
85. **[F] theme:sound-jp** — Sidebar-unreachable at 375/320 in both engines on page and sample; render T3 confirms the mobile sidebar toggle is missing. No fix, no disposition in the sources. [R/ledger-parts/RENDER-ROWS-RERUN16.md / RENDER-ROWS-1.md / RENDER-ROWS-2.md (per-theme rows)]
86. **[I] theme:starbasalt-jp** — Sample section-15 content panels render as unstyled plain text on black (render T3). No fix wave restored the panel styling and no design ground is recorded in the row. [R/ledger-parts/RENDER-ROWS-G.md (starbasalt row)]
87. **[I] theme:starbasalt-jp** — Unterminated CSS comment in the delivered code block: the header comment opened at L352 of the [[code]] exhibit (served as the theme’s local--code /1, imported by the candidate itself) does not close until L454, commenting out 102 lines — all five font @imports, the :root variable groups (header strings, colours, logo) and the body rules. LOCALIZE-S2-E graded the theme display-fatal for this; assembly re-verified the span in the current file (comment L352–L454). This also explains the unstyled section-15 panels in the render row. [R/REPORT-GOSIGN2-LOCALIZE-S2-E.md (CN14-5 starbasalt row); current canonical file L351–L454 (assembly-verified)]
88. **[H] theme:starry-jp** — Dead prose links at L32: `theme:mox` and `theme:shivering-night`, neither of which exists on scp-jp under those names (the candidates are theme:mox-jp and theme:shivering-night-jp; the candidate’s own base import at L343 correctly uses theme:mox-jp/8). Charged under P11 and in the lane’s cross-cutting dead-target list (item 7). [R/REPORT-GOSIGN2-LOCALIZE-S2-E.md (CN15-1 starry row + cross-cutting item 7); current canonical file L32 (assembly-verified)]
89. **[I] theme:steam-guide-jp** — The opening ListPages wrapper was deleted and its machinery left fused in the page body: raw `%%content{0}%%` literals stand in the current file (L15/L17/L23/L25), interleaved with unrewritten CN credit includes (:scp-wiki-cn:credit:more, :scp-wiki-cn:credit:start-standalone, :scp-wiki-cn:credit:more-standalone). Charged under P1/P3. FIX4-REPOINT’s edit to this file was the avatar scheme only. [R/REPORT-GOSIGN2-LOCALIZE-S2-E.md (CN15-2 steam-guide row); current canonical file L15–L25 (assembly-verified)]
90. **[I] theme:supply-n-demand-jp** — The theme’s entire showcase section was deleted in porting (the row’s headline structural finding). No FIX report records a restoration. (Its pattern-4 imports were separately repointed by FIX-P4.) [R/REPORT-GOSIGN2-LOCALIZE-S2-E.md (CN15-3 supply-n-demand row)]
91. **[H] theme:suprematism-jp** — Credit block: the タイトル field still carries the untranslated CN title while the page body itself renders the theme’s name in Japanese (至上主義, L16), and the credit 著作権者 field names only Liurd although the body names both authors (LemonCat233 and Liurd). Charged as P1/P3 (co-author attribution lost; untranslated credit title); the license-box includes were fixed by FIX2-INCLUDE but the credit fields were not. [R/REPORT-GOSIGN2-LOCALIZE-S2-E.md (suprematism row); current canonical file L3-16 (assembly-verified)]
92. **[I] theme:suprematism-jp** — All 11 `#ifexpr` preset blocks were emptied in porting: the current file carries the eleven iftags/#ifexpr shells (from L382) with empty bodies, so the theme’s documented presets do nothing. Charged as structural mangling (cross-cutting class 5). FIX2-INCLUDE repaired this file’s license-box includes; no wave restored the presets. (Assembly-verified: first three shells at L382/L386/L390 are empty.) [R/REPORT-GOSIGN2-LOCALIZE-S2-E.md (CN15-4 suprematism row + cross-cutting class 5); current canonical file (assembly-verified)]
93. **[H] theme:the-track-changers-jp** — Untranslated Chinese edit-lock text stands in the candidate’s CSS (current L1567/L1588 — the same Basalt-derived lock messages as greyday’s). KB-18 surface class; no wave translated them. (Its jsdelivr imports are separately dispositioned under KB-14.) [R/REPORT-GOSIGN2-LOCALIZE-S2-E.md (CN16-2 the-track-changers row); current canonical file (assembly-verified)]
94. **[H] theme:the-track-changers-jp** — Dead prose links: the text links to `belief` and `theme:old-money-theme` (current L42), neither of which exists on scp-jp (the candidate is theme:old-money-theme-jp). Charged under P11 and in the lane’s cross-cutting dead-target list (item 7). [R/REPORT-GOSIGN2-LOCALIZE-S2-E.md (CN16-2 row + cross-cutting item 7); current canonical file L42 (assembly-verified)]
95. **[H] theme:trauma-jp** — Dead prose link to `theme:suprematism` (standing in the current file), which does not exist on scp-jp (the candidate is theme:suprematism-jp). Charged under P11 and in the lane’s cross-cutting dead-target list (item 7). (This theme’s interwiki defects were fixed by FIX4-IWB; the link was not.) [R/REPORT-GOSIGN2-LOCALIZE-S2-E.md (CN16-3 row + cross-cutting item 7); current canonical file (assembly-verified)]
96. **[H] theme:travellers-book-jp** — Dead prose link to `wanderers:travellers-book-hub` (current L26), a hub page that does not exist on scp-jp. Charged under P11 and in the lane’s cross-cutting dead-target list (item 7). (This theme’s credit items were fixed by FIX4-CREDIT; the link was not.) [R/REPORT-GOSIGN2-LOCALIZE-S2-E.md (CN16-4 row + cross-cutting item 7); current canonical file L26 (assembly-verified)]
97. **[I] theme:voyager-jp** — The Sigma+ base dependency was silently dropped: the original’s sigma-plus include was deleted outright, the candidate’s shipped CSS still references Sigma+ variables (--sp_side-bar-width, --sp_final-header-height) that are defined nowhere in it, and the prose names the unported `component:sigma-plus` (a dead link). Owner ruling 4 ports a needed component with its theme, and component:sigma-plus-jp now exists (FIX3-SP), but this candidate was never rewired to it. The render walk recorded no breakage from the fallback sizing; the source-level defect stands as charged. [R/REPORT-GOSIGN2-LOCALIZE-S2-E.md (voyager pattern table, #1); current canonical file (assembly-verified: no sigma-plus include)]
98. **[H] theme:winddew-in-hand-jp** — Dead prose links: `theme:basalt` (current L32) and `theme:admo` (current L42), neither of which exists on scp-jp under those names (the candidates are theme:basalt-jp and theme:admo-jp); the same row charges the dropped Basalt base reference. (Its usage-example item is separate, class H.) [R/REPORT-GOSIGN2-LOCALIZE-S2-E.md (CN17-4 winddew-in-hand row); current canonical file L32/L42 (assembly-verified)]
99. **[C] theme:07k-jp** — LOCALIZE-S2-F row: 型 3, the EN-style info module (info:start/info:end) is left in place alongside the JP credit module, so two rating areas render. Both includes still stand (current L14 credit, L33/L37 info). FIX-CREDIT-D rewrote this file’s translator credit only. Two credit/info furniture sets render on one page. [R/REPORT-GOSIGN2-LOCALIZE-S2-F.md; R/GOSIGN2-T45-FIXPREP.md (pattern-3 exception covers labelled pairs only); current canonical file (assembly-verified)]
100. **[E] theme:a-midnight-invitation-jp** — Stock-header wordmark and nav in very light gray on near-white at all 8 viewports, nearly illegible; the render lane records it as theme-specific (checklist section 1 contrast). Same mechanism as KB-28. No fix wave corrected a KB-28 binding and no original-faithful ground is recorded for these surfaces. [patterns/KB-28.md (class B theme defect; fix = correct the variable binding in the candidate); R/ledger-parts/RENDER-ROWS-RERUN16.md / RENDER-ROWS-1.md / RENDER-ROWS-2.md / RENDER-ROWS-G.md (per-theme rows)]
101. **[C] theme:animal-instead-of-beast-jp** — LOCALIZE-S2-F row: 型 3, bare info:start/info:end left alongside the credit module (current L33/L34), rendering a second rating area. No wave removed the residue. Two credit/info furniture sets render on one page. [R/REPORT-GOSIGN2-LOCALIZE-S2-F.md; R/GOSIGN2-T45-FIXPREP.md (pattern-3 exception covers labelled pairs only); current canonical file (assembly-verified)]
102. **[E] theme:animal-instead-of-beast-jp** — Header wordmark faint gray-on-white (machine contrast 1.03, T3-recorded). Same mechanism as KB-28. No fix wave corrected a KB-28 binding and no original-faithful ground is recorded for these surfaces. [patterns/KB-28.md (class B theme defect; fix = correct the variable binding in the candidate); R/ledger-parts/RENDER-ROWS-RERUN16.md / RENDER-ROWS-1.md / RENDER-ROWS-2.md / RENDER-ROWS-G.md (per-theme rows)]
103. **[H] theme:back-jan-fire-jp** — Credit block: the タイトル field still carries the untranslated KO title while the page body carries a Japanese title (灯火CSSテーマ, L14). Charged as 型 3 (title untranslated) in the row’s findings set; no wave corrected it. (The parallel item on bulgunae was marked minor by its own lane and is dispositioned there; this row carries no such severity call.) [R/REPORT-GOSIGN2-LOCALIZE-S2-F.md (back-jan-fire row); current canonical file L3-14 (assembly-verified)]
104. **[F] theme:creature-jp** — Oversized circular SCP PARK header art is wider than the mobile viewport and its lettering is cut at the edges at 375/320 in both engines (render T3). No design ground is recorded in the row and no fix wave adjusted the art’s mobile presentation. [R/ledger-parts/RENDER-ROWS-2.md (creature row)]
105. **[C] theme:king-s-palace-jp** — LOCALIZE-S2-F row: 型 3 double credit. The file carries two live credit:start-preview blocks (current L16, a 【サンプル】-titled specimen, and L27, the theme’s own credit). The bare Rate at L10 is a labelled exhibit (評価モジュール:) and is excepted; the second live credit block is not covered by the paired-exhibit exception and no wave removed it. Two credit/info furniture sets render on one page. [R/REPORT-GOSIGN2-LOCALIZE-S2-F.md; R/GOSIGN2-T45-FIXPREP.md (pattern-3 exception covers labelled pairs only); current canonical file (assembly-verified)]
106. **[F] theme:pacom1943-jp** — Long headings run past the content column and are clipped at PC/tablet widths, and wrap/cut at mobile (render T3). No disposition ground is recorded in the row and no fix wave addressed the heading overflow. [R/ledger-parts/RENDER-ROWS-2.md (pacom1943 row)]
107. **[C] theme:plugsoft-jp** — LOCALIZE-S2-F row: 型 3, info:start/info:end left alongside the credit module (current L22/L45), rendering a second rating area. No wave removed the residue. Two credit/info furniture sets render on one page. [R/REPORT-GOSIGN2-LOCALIZE-S2-F.md; R/GOSIGN2-T45-FIXPREP.md (pattern-3 exception covers labelled pairs only); current canonical file (assembly-verified)]

GOSIGN2-LEDGER: COMPLETE
