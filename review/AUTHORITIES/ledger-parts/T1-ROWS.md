# T1-ROWS — go-sign ledger, T1 baseline verdict rows

Data extraction only. All values (baseline exit, errors, warns, infos, error CODE multiset) are taken verbatim from `R/REPORT-GOSIGN2-T1-BASELINE.md` (single uniform post-fix baseline, 2026-11-16). No checker was re-run; the canonical repo was not edited and nothing was reflected. The final column is left blank for the coordinator.

'theme fullname (candidate)' is the candidate page fullname. Row 144 (Amethyst V2 版式) is the documented EXCEPTION — no candidate exists — carried through as-is. Errors/warns/infos/code multiset describe the error level findings; `—` means none. Error-code multiset format: `CODE×count`.

| # | theme fullname (candidate) | baseline exit | errors | warns | infos | error CODE multiset | residual classes after FIX3 |
|---|---|---|---|---|---|---|---|
| 1 | `theme:aesthetic-theme-jp` | 1 | 3 | 1 | 3 | pseudo-ref×3 |  |
| 2 | `theme:al-slop-jp` | 1 | 20 | 1 | 2 | pseudo-ref×18, hotlink×2 |  |
| 3 | `theme:basalt-jp` | 1 | 33 | 2 | 2 | pseudo-ref×23, hotlink×10 |  |
| 4 | `theme:bedrock-jp` | 1 | 4 | 0 | 2 | hotlink×2, pseudo-ref×2 |  |
| 5 | `theme:black-highlighter-theme-jp` | 1 | 1 | 3 | 1 | pseudo-ref×1 |  |
| 6 | `theme:blankstyle-jp` | 0 | 0 | 1 | 1 | — |  |
| 7 | `theme:classic-jp` | 1 | 2 | 0 | 2 | pseudo-ref×2 |  |
| 8 | `theme:cosmonaut-jp` | 1 | 2 | 0 | 1 | pseudo-ref×2 |  |
| 9 | `theme:dear-dictator-jp` | 1 | 6 | 1 | 1 | pseudo-ref×6 |  |
| 10 | `theme:extra-black-highlighter-theme-jp` | 1 | 2 | 0 | 2 | pseudo-ref×2 |  |
| 11 | `theme:flopstyle-jp` | 1 | 2 | 1 | 2 | hotlink×2 |  |
| 12 | `theme:flopstyle-dark-jp` | 1 | 74 | 13 | 2 | pseudo-ref×67, foreign-include×4, hotlink×3 |  |
| 13 | `theme:foxtrot-jp` | 1 | 33 | 6 | 3 | http×30, foreign-include×2, hotlink×1 |  |
| 14 | `theme:halloween-jp` | 1 | 1 | 1 | 1 | hotlink×1 |  |
| 15 | `theme:hansarp-jp` | 1 | 2 | 2 | 5 | pseudo-ref×2 |  |
| 16 | `theme:inkblot-jp` | 1 | 8 | 3 | 2 | pseudo-ref×5, hotlink×3 |  |
| 17 | `theme:isolated-terminal-jp` | 1 | 2 | 1 | 2 | pseudo-ref×2 |  |
| 18 | `theme:jakstyle-jp` | 1 | 1 | 8 | 1 | pseudo-ref×1 |  |
| 19 | `theme:just-girly-things-jp` | 1 | 3 | 1 | 1 | hotlink×3 |  |
| 20 | `theme:min-theme-jp` | 0 | 0 | 3 | 2 | — |  |
| 21 | `theme:minimalist-bhl-jp` | 1 | 3 | 1 | 3 | http×2, pseudo-ref×1 |  |
| 22 | `theme:monotypical-jp` | 1 | 6 | 3 | 2 | pseudo-ref×4, hotlink×2 |  |
| 23 | `theme:much-cool-jp` | 1 | 1 | 1 | 2 | pseudo-ref×1 |  |
| 24 | `theme:night-rush-theme-jp` | 1 | 2 | 1 | 4 | http×2 |  |
| 25 | `theme:ouroborous-theme-jp` | 1 | 3 | 2 | 6 | pseudo-ref×3 |  |
| 26 | `theme:paperstack-jp` | 1 | 5 | 1 | 5 | http×3, pseudo-ref×2 |  |
| 27 | `theme:pataphysics-jp` | 0 | 0 | 1 | 2 | — |  |
| 28 | `theme:penumbra-jp` | 1 | 2 | 2 | 2 | http×2 |  |
| 29 | `theme:quand-le-soleil-se-couche` | 1 | 2 | 3 | 1 | pseudo-ref×2 |  |
| 30 | `theme:redtape-jp` | 1 | 4 | 1 | 1 | pseudo-ref×4 |  |
| 31 | `theme:scheme-jp` | 1 | 16 | 1 | 7 | pseudo-ref×14, hotlink×2 |  |
| 32 | `theme:scp-human-resources-jp` | 0 | 0 | 1 | 0 | — |  |
| 33 | `theme:scp-offices-theme-jp` | 1 | 4 | 1 | 2 | pseudo-ref×4 |  |
| 34 | `theme:scpedia-jp` | 1 | 5 | 2 | 2 | hotlink×3, pseudo-ref×2 |  |
| 35 | `theme:shushuin-jp` | 0 | 0 | 5 | 2 | — |  |
| 36 | `theme:sigma-jp` | 1 | 1 | 4 | 1 | hotlink×1 |  |
| 37 | `theme:sigma-10-jp` | 1 | 2 | 1 | 0 | no-credit×1, no-rate×1 |  |
| 38 | `theme:simple-yonder-jp` | 1 | 6 | 1 | 1 | hotlink×6 |  |
| 39 | `theme:skipos-jp` | 1 | 8 | 1 | 1 | pseudo-ref×6, hotlink×2 |  |
| 40 | `theme:space-jp` | 1 | 1 | 2 | 1 | pseudo-ref×1 |  |
| 41 | `theme:turbo-vision-jp` | 1 | 2 | 0 | 1 | pseudo-ref×2 |  |
| 42 | `theme:wikifot-jp` | 1 | 1 | 0 | 2 | pseudo-ref×1 |  |
| 43 | `theme:y2k-jp` | 1 | 2 | 0 | 3 | http×1, pseudo-ref×1 |  |
| 44 | `theme:yossistyle-jp` | 0 | 0 | 3 | 2 | — |  |
| 45 | `theme:3law-pride-jp` | 1 | 4 | 1 | 0 | hotlink×4 |  |
| 46 | `theme:3lawcracked-jp` | 1 | 5 | 1 | 0 | hotlink×5 |  |
| 47 | `theme:512-onwards-jp` | 1 | 25 | 1 | 1 | hotlink×23, pseudo-ref×2 |  |
| 48 | `theme:5k-jp` | 1 | 4 | 1 | 1 | hotlink×3, unencoded-colon×1 |  |
| 49 | `theme:a-problematic-theme-jp` | 1 | 1 | 1 | 0 | hotlink×1 |  |
| 50 | `theme:aces-and-eights-jp` | 1 | 3 | 1 | 1 | hotlink×3 |  |
| 51 | `theme:ad-abyssum-penumbra-jp` | 1 | 1 | 1 | 1 | hotlink×1 |  |
| 52 | `theme:admo-jp` | 1 | 12 | 1 | 1 | hotlink×9, pseudo-ref×2, http×1 |  |
| 53 | `theme:alcur-theme-jp` | 1 | 12 | 1 | 1 | hotlink×10, pseudo-ref×2 |  |
| 54 | `theme:alexylva-university-jp` | 1 | 5 | 1 | 0 | hotlink×5 |  |
| 55 | `theme:ambrose-chapter-two-jp` | 1 | 2 | 1 | 1 | hotlink×2 |  |
| 56 | `theme:angel-jp` | 1 | 3 | 1 | 1 | hotlink×3 |  |
| 57 | `theme:anon-jp` | 1 | 4 | 2 | 1 | hotlink×3, pseudo-ref×1 |  |
| 58 | `theme:art-deco-jp` | 0 | 0 | 1 | 1 | — |  |
| 59 | `theme:ashes-to-ashes-jp` | 1 | 3 | 1 | 0 | hotlink×3 |  |
| 60 | `theme:chaos-jp` | 1 | 2 | 2 | 2 | pseudo-ref×2 |  |
| 61 | `theme:cleaning-services-jp` | 1 | 4 | 2 | 2 | pseudo-ref×4 |  |
| 62 | `theme:clock-tower-jp` | 1 | 5 | 1 | 2 | pseudo-ref×5 |  |
| 63 | `theme:cosmos-jp` | 1 | 6 | 1 | 2 | pseudo-ref×6 |  |
| 64 | `theme:crayon-jp` | 1 | 2 | 1 | 1 | pseudo-ref×2 |  |
| 65 | `theme:bedbugs-theme-jp` | 1 | 3 | 2 | 0 | pseudo-ref×3 |  |
| 66 | `theme:black-diamond-jp` | 1 | 4 | 0 | 1 | pseudo-ref×4 |  |
| 67 | `theme:black-market-jp` | 1 | 4 | 1 | 0 | pseudo-ref×4 |  |
| 68 | `theme:black-serpent-jp` | 1 | 3 | 2 | 0 | pseudo-ref×3 |  |
| 69 | `theme:blood-jp` | 1 | 5 | 1 | 0 | pseudo-ref×5 |  |
| 70 | `theme:bloodraven-jp` | 1 | 43 | 1 | 1 | hotlink×42, pseudo-ref×1 |  |
| 71 | `theme:borealis-constant-theme-jp` | 1 | 10 | 1 | 1 | hotlink×8, pseudo-ref×2 |  |
| 72 | `theme:caretaker-sigma-jp` | 1 | 4 | 1 | 0 | hotlink×3, pseudo-ref×1 |  |
| 73 | `theme:caretaker-theme-jp` | 1 | 3 | 1 | 0 | hotlink×2, pseudo-ref×1 |  |
| 74 | `theme:ch-scp-theme-jp` | 1 | 9 | 2 | 3 | hotlink×8, pseudo-ref×1 |  |
| 75 | `theme:dark-jp` | 1 | 4 | 2 | 1 | pseudo-ref×4 |  |
| 76 | `theme:dark-dealings-jp` | 1 | 20 | 2 | 1 | pseudo-ref×18, foreign-include×2 |  |
| 77 | `theme:darkqueer-jp` | 1 | 3 | 2 | 1 | pseudo-ref×3 |  |
| 78 | `theme:decom-dept-jp` | 1 | 7 | 0 | 1 | pseudo-ref×5, foreign-include×2 |  |
| 79 | `theme:derby-jp` | 1 | 14 | 1 | 1 | pseudo-ref×14 |  |
| 80 | `theme:fossil-jp` | 1 | 6 | 1 | 0 | hotlink×5, pseudo-ref×1 |  |
| 81 | `theme:frownstyle-jp` | 1 | 6 | 3 | 1 | pseudo-ref×4, hotlink×2 |  |
| 82 | `theme:fuladh-theme-jp` | 1 | 6 | 1 | 1 | hotlink×5, pseudo-ref×1 |  |
| 83 | `theme:galactic-theme-jp` | 1 | 5 | 1 | 7 | hotlink×4, pseudo-ref×1 |  |
| 84 | `theme:golden-feast-jp` | 1 | 4 | 1 | 1 | hotlink×3, pseudo-ref×1 |  |
| 85 | `theme:enlightened-eyes-jp` | 1 | 6 | 0 | 1 | pseudo-ref×6 |  |
| 86 | `theme:eventyr-jp` | 1 | 49 | 1 | 1 | pseudo-ref×49 |  |
| 87 | `theme:fandom-jp` | 1 | 2 | 0 | 1 | pseudo-ref×2 |  |
| 88 | `theme:febris-pharmaceuticals-theme-jp` | 1 | 2 | 2 | 0 | pseudo-ref×2 |  |
| 89 | `theme:fish-jp` | 1 | 4 | 0 | 0 | pseudo-ref×4 |  |
| 90 | `theme:i57-theme-jp` | 1 | 8 | 0 | 1 | hotlink×7, pseudo-ref×1 |  |
| 91 | `theme:immrama-jp` | 1 | 8 | 1 | 0 | hotlink×7, pseudo-ref×1 |  |
| 92 | `theme:internal-affairs-jp` | 1 | 3 | 0 | 1 | hotlink×2, pseudo-ref×1 |  |
| 93 | `theme:janitor-closet-jp` | 1 | 4 | 1 | 1 | hotlink×3, pseudo-ref×1 |  |
| 94 | `theme:kiryu-labs-theme-jp` | 1 | 3 | 0 | 1 | hotlink×2, pseudo-ref×1 |  |
| 95 | `theme:lampeter-warm-jp` | 1 | 6 | 1 | 1 | pseudo-ref×6 |  |
| 96 | `theme:laruetheme-jp` | 1 | 7 | 1 | 1 | pseudo-ref×7 |  |
| 97 | `theme:last-frontier-jp` | 1 | 7 | 0 | 1 | pseudo-ref×7 |  |
| 98 | `theme:laughter-and-knives-theme-jp` | 1 | 2 | 1 | 3 | pseudo-ref×2 |  |
| 99 | `theme:linear-black-jp` | 1 | 4 | 0 | 1 | pseudo-ref×4 |  |
| 100 | `theme:dia-de-muertos-jp` | 1 | 8 | 1 | 0 | pseudo-ref×8 |  |
| 101 | `theme:diamond-highlighter-jp` | 1 | 3 | 1 | 0 | pseudo-ref×3 |  |
| 102 | `theme:dynamikron-jp` | 1 | 8 | 1 | 2 | pseudo-ref×8 |  |
| 103 | `theme:eigenmachine-jp` | 1 | 35 | 2 | 1 | pseudo-ref×34, hotlink×1 |  |
| 104 | `theme:eigenvector-jp` | 1 | 8 | 0 | 0 | pseudo-ref×8 |  |
| 105 | `theme:greystyle-jp` | 1 | 21 | 3 | 3 | hotlink×21 |  |
| 106 | `theme:helix-jp` | 1 | 11 | 1 | 0 | hotlink×11 |  |
| 107 | `theme:highroller-jp` | 1 | 11 | 1 | 1 | hotlink×11 |  |
| 108 | `theme:hytoth-two-jp` | 1 | 15 | 0 | 1 | hotlink×13, pseudo-ref×2 |  |
| 109 | `theme:i57-jp` | 1 | 13 | 1 | 1 | hotlink×13 |  |
| 110 | `theme:lumina-jp` | 1 | 6 | 1 | 1 | hotlink×3, pseudo-ref×3 |  |
| 111 | `theme:magpie-swoops-jp` | 1 | 2 | 0 | 0 | hotlink×1, pseudo-ref×1 |  |
| 112 | `theme:maxwell-s-silver-hammer-jp` | 1 | 4 | 1 | 1 | hotlink×3, pseudo-ref×1 |  |
| 113 | `theme:mcf-jp` | 1 | 5 | 1 | 0 | hotlink×4, pseudo-ref×1 |  |
| 114 | `theme:oceanbound-jp` | 1 | 6 | 0 | 1 | hotlink×4, pseudo-ref×2 |  |
| 115 | `theme:old-money-theme-jp` | 1 | 10 | 1 | 1 | pseudo-ref×10 |  |
| 116 | `theme:onko-sinulla-nalka-theme-jp` | 1 | 7 | 1 | 0 | pseudo-ref×7 |  |
| 117 | `theme:ordopharm-jp` | 1 | 6 | 1 | 1 | pseudo-ref×6 |  |
| 118 | `theme:our-open-veins-jp` | 1 | 7 | 0 | 1 | pseudo-ref×7 |  |
| 119 | `theme:pack-of-peanuts-jp` | 1 | 5 | 0 | 1 | pseudo-ref×5 |  |
| 120 | `theme:shark-punching-centre-bhl-jp` | 1 | 5 | 2 | 2 | pseudo-ref×5 |  |
| 121 | `theme:shattered-thoughts-jp` | 1 | 5 | 0 | 2 | pseudo-ref×5 |  |
| 122 | `theme:shoebill-jp` | 1 | 6 | 3 | 2 | pseudo-ref×6 |  |
| 123 | `theme:skiesmadestrange-jp` | 1 | 2 | 1 | 1 | pseudo-ref×2 |  |
| 124 | `theme:spidersfalling-jp` | 1 | 11 | 1 | 1 | pseudo-ref×11 |  |
| 125 | `theme:retro-aiad-theme-jp` | 1 | 5 | 0 | 0 | pseudo-ref×5 |  |
| 126 | `theme:retrofutura-jp` | 1 | 2 | 1 | 1 | pseudo-ref×2 |  |
| 127 | `theme:saphir-jp` | 1 | 5 | 0 | 2 | pseudo-ref×5 |  |
| 128 | `theme:scp-human-resources-sigma-jp` | 1 | 1 | 0 | 2 | pseudo-ref×1 |  |
| 129 | `theme:scp-offices-sigma-jp` | 1 | 1 | 1 | 2 | pseudo-ref×1 |  |
| 130 | `theme:thalassophobia-jp` | 1 | 4 | 3 | 1 | pseudo-ref×4 |  |
| 131 | `theme:thalassophobia-sigma-jp` | 1 | 7 | 3 | 1 | pseudo-ref×7 |  |
| 132 | `theme:the-coalition-theme-jp` | 1 | 4 | 1 | 1 | pseudo-ref×4 |  |
| 133 | `theme:the-foundation-sigma-jp` | 1 | 1 | 1 | 1 | pseudo-ref×1 |  |
| 134 | `theme:the-smell-of-smoke-jp` | 1 | 3 | 1 | 1 | pseudo-ref×3 |  |
| 135 | `theme:turbo-vision-dark-jp` | 1 | 7 | 2 | 1 | pseudo-ref×7 |  |
| 136 | `theme:twin-files-jp` | 1 | 12 | 1 | 1 | pseudo-ref×12 |  |
| 137 | `theme:ui-jp` | 1 | 2 | 2 | 0 | pseudo-ref×2 |  |
| 138 | `theme:uiu-bhl-theme-jp` | 1 | 2 | 2 | 1 | pseudo-ref×2 |  |
| 139 | `theme:unusual-cargo-jp` | 1 | 16 | 0 | 1 | pseudo-ref×16 |  |
| 140 | `theme:andesite-jp` | 1 | 8 | 1 | 1 | hotlink×5, pseudo-ref×3 |  |
| 141 | `theme:another-night-jp` | 1 | 15 | 3 | 1 | hotlink×10, pseudo-ref×5 |  |
| 142 | `theme:ared-jp` | 1 | 3 | 1 | 1 | hotlink×2, pseudo-ref×1 |  |
| 143 | `theme:asagao-jp` | 1 | 13 | 0 | 1 | hotlink×12, pseudo-ref×1 |  |
| 144 | — (EXCEPTION — no candidate) | — | — | — | — | — |  |
| 145 | `theme:betwixt-jp` | 1 | 8 | 0 | 1 | pseudo-ref×8 |  |
| 146 | `theme:black-rain-jp` | 1 | 2 | 1 | 1 | pseudo-ref×2 |  |
| 147 | `theme:blackinblack-jp` | 1 | 2 | 1 | 1 | pseudo-ref×2 |  |
| 148 | `theme:brokedown-database-jp` | 1 | 5 | 2 | 1 | pseudo-ref×5 |  |
| 149 | `theme:broken-light-jp` | 1 | 13 | 1 | 1 | pseudo-ref×10, hotlink×3 |  |
| 150 | `theme:queen-s-gambit-jp` | 1 | 4 | 1 | 1 | hotlink×3, pseudo-ref×1 |  |
| 151 | `theme:queerstyle-jp` | 1 | 2 | 1 | 0 | pseudo-ref×2 |  |
| 152 | `theme:ragnarok-theme-jp` | 1 | 4 | 2 | 1 | hotlink×4 |  |
| 153 | `theme:raisa-jp` | 1 | 2 | 0 | 2 | hotlink×1, pseudo-ref×1 |  |
| 154 | `theme:raisa-sigma-jp` | 1 | 3 | 0 | 1 | hotlink×2, pseudo-ref×1 |  |
| 155 | `theme:paramycota-jp` | 1 | 15 | 3 | 1 | pseudo-ref×15 |  |
| 156 | `theme:parawatch-pumpkin-jp` | 1 | 2 | 2 | 0 | pseudo-ref×2 |  |
| 157 | `theme:pastel-skies-jp` | 1 | 11 | 1 | 1 | pseudo-ref×11 |  |
| 158 | `theme:plant-jp` | 1 | 6 | 2 | 0 | pseudo-ref×6 |  |
| 159 | `theme:prom-labs-jp` | 1 | 3 | 1 | 1 | pseudo-ref×3 |  |
| 160 | `theme:stargazer-jp` | 1 | 12 | 1 | 1 | hotlink×10, pseudo-ref×2 |  |
| 161 | `theme:stellar-jp` | 1 | 8 | 1 | 0 | hotlink×6, pseudo-ref×2 |  |
| 162 | `theme:sunside-jp` | 1 | 3 | 2 | 0 | hotlink×3 |  |
| 163 | `theme:tales-of-the-mosaic-jp` | 1 | 21 | 1 | 1 | hotlink×20, foreign-include×1 |  |
| 164 | `theme:telecommunications-monitoring-office-theme-jp` | 0 | 0 | 0 | 1 | — |  |
| 165 | `theme:ethic-committee-jp` | 1 | 2 | 2 | 1 | hotlink×1, pseudo-ref×1 |  |
| 166 | `theme:fmd-bhl-theme-jp` | 1 | 5 | 1 | 1 | hotlink×4, pseudo-ref×1 |  |
| 167 | `theme:food-jp` | 1 | 5 | 1 | 0 | hotlink×4, pseudo-ref×1 |  |
| 168 | `theme:foundom-jp` | 1 | 5 | 3 | 0 | hotlink×4, pseudo-ref×1 |  |
| 169 | `theme:frutiger-aero-jp` | 1 | 4 | 1 | 1 | hotlink×3, pseudo-ref×1 |  |
| 170 | `theme:vanguard-jp` | 1 | 3 | 4 | 1 | pseudo-ref×3 |  |
| 171 | `theme:vanguard-supplement-jp` | 1 | 1 | 2 | 2 | pseudo-ref×1 |  |
| 172 | `theme:wilderness-jp` | 1 | 3 | 2 | 2 | pseudo-ref×3 |  |
| 173 | `theme:wondertainment-jp` | 1 | 6 | 0 | 2 | pseudo-ref×6 |  |
| 174 | `theme:words-of-wisdom-jp` | 1 | 3 | 1 | 2 | pseudo-ref×3 |  |
| 175 | `theme:golden-wind-jp` | 1 | 12 | 0 | 2 | pseudo-ref×11, hotlink×1 |  |
| 176 | `theme:gp-refresh-jp` | 1 | 21 | 3 | 1 | pseudo-ref×21 |  |
| 177 | `theme:greyday-jp` | 1 | 7 | 1 | 2 | pseudo-ref×7 |  |
| 178 | `theme:gsk-jp` | 1 | 11 | 4 | 1 | pseudo-ref×11 |  |
| 179 | `theme:highlighter-bhl-jp` | 1 | 4 | 7 | 1 | pseudo-ref×3, hotlink×1 |  |
| 180 | `theme:writing-anomalies-jp` | 1 | 5 | 0 | 1 | pseudo-ref×5 |  |
| 181 | `theme:xmas-jp` | 1 | 20 | 0 | 0 | pseudo-ref×20 |  |
| 182 | `theme:parablue-jp` | 1 | 16 | 7 | 3 | hotlink×12, http×2, foreign-include×1, pseudo-ref×1 |  |
| 183 | `theme:paradigm-inapplicable-jp` | 1 | 6 | 1 | 1 | hotlink×5, pseudo-ref×1 |  |
| 184 | `theme:paradigm-inapplicable-sigma-jp` | 1 | 3 | 2 | 0 | hotlink×2, pseudo-ref×1 |  |
| 185 | `theme:paradigm-reconstruction-jp` | 1 | 6 | 1 | 0 | hotlink×5, pseudo-ref×1 |  |
| 186 | `theme:parallel-jp` | 1 | 11 | 9 | 0 | hotlink×9, foreign-include×1, pseudo-ref×1 |  |
| 187 | `theme:sci-fi-jp` | 1 | 3 | 6 | 1 | pseudo-ref×3 |  |
| 188 | `theme:scpdeclassified-jp` | 1 | 6 | 1 | 1 | pseudo-ref×6 |  |
| 189 | `theme:scplive-jp` | 1 | 2 | 2 | 1 | pseudo-ref×2 |  |
| 190 | `theme:shancheng-jp` | 1 | 8 | 1 | 1 | pseudo-ref×8 |  |
| 191 | `theme:share-future-community-jp` | 1 | 3 | 3 | 0 | pseudo-ref×2, hotlink×1 |  |
| 192 | `theme:starry-jp` | 1 | 57 | 3 | 2 | hotlink×54, pseudo-ref×2, http×1 |  |
| 193 | `theme:steam-guide-jp` | 1 | 7 | 2 | 7 | hotlink×5, http×1, pseudo-ref×1 |  |
| 194 | `theme:supply-n-demand-jp` | 1 | 6 | 2 | 1 | hotlink×5, pseudo-ref×1 |  |
| 195 | `theme:suprematism-jp` | 1 | 14 | 0 | 0 | hotlink×11, pseudo-ref×2, old-bhl×1 |  |
| 196 | `theme:tfnac-jp` | 1 | 4 | 2 | 0 | old-bhl×2, hotlink×1, pseudo-ref×1 |  |
| 197 | `theme:broken-world-jp` | 1 | 14 | 4 | 2 | pseudo-ref×13, hotlink×1 |  |
| 198 | `theme:candela-jp` | 1 | 12 | 0 | 1 | pseudo-ref×10, hotlink×2 |  |
| 199 | `theme:cmst-jp` | 1 | 5 | 0 | 1 | pseudo-ref×5 |  |
| 200 | `theme:cobalt-aero-glass-jp` | 1 | 10 | 1 | 1 | pseudo-ref×10 |  |
| 201 | `theme:construct-jp` | 1 | 1 | 2 | 1 | pseudo-ref×1 |  |
| 202 | `theme:the-other-side-jp` | 1 | 4 | 0 | 1 | pseudo-ref×4 |  |
| 203 | `theme:the-track-changers-jp` | 1 | 7 | 2 | 1 | pseudo-ref×5, hotlink×2 |  |
| 204 | `theme:trauma-jp` | 1 | 13 | 1 | 0 | pseudo-ref×12, hotlink×1 |  |
| 205 | `theme:travellers-book-jp` | 1 | 6 | 2 | 1 | pseudo-ref×6 |  |
| 206 | `theme:ultimate-reader-jp` | 1 | 3 | 1 | 1 | pseudo-ref×3 |  |
| 207 | `theme:voyager-jp` | 1 | 4 | 1 | 1 | hotlink×3, pseudo-ref×1 |  |
| 208 | `theme:walk-in-the-dark-jp` | 1 | 4 | 2 | 1 | hotlink×3, pseudo-ref×1 |  |
| 209 | `theme:waxed-oxidized-cut-copper-slab-jp` | 1 | 9 | 3 | 1 | hotlink×8, pseudo-ref×1 |  |
| 210 | `theme:winddew-in-hand-jp` | 1 | 5 | 2 | 1 | hotlink×4, pseudo-ref×1 |  |
| 211 | `theme:winxp-jp` | 1 | 9 | 2 | 1 | hotlink×8, pseudo-ref×1 |  |
| 212 | `theme:copper-jp` | 1 | 7 | 0 | 2 | pseudo-ref×7 |  |
| 213 | `theme:crt-jp` | 1 | 3 | 1 | 2 | pseudo-ref×3 |  |
| 214 | `theme:darkblue-jp` | 1 | 5 | 1 | 2 | pseudo-ref×5 |  |
| 215 | `theme:decay-jp` | 1 | 11 | 2 | 2 | pseudo-ref×11 |  |
| 216 | `theme:deepspace-jp` | 1 | 2 | 1 | 2 | pseudo-ref×2 |  |
| 217 | `theme:deserted-years-theme-jp` | 1 | 7 | 1 | 1 | hotlink×7 |  |
| 218 | `theme:dream-of-the-stars-jp` | 1 | 3 | 1 | 1 | hotlink×2, pseudo-ref×1 |  |
| 219 | `theme:drunken-alley-jp` | 1 | 2 | 1 | 2 | hotlink×1, pseudo-ref×1 |  |
| 220 | `theme:dustframe-jp` | 0 | 0 | 1 | 1 | — |  |
| 221 | `theme:emotion-division-jp` | 1 | 3 | 1 | 1 | hotlink×2, pseudo-ref×1 |  |
| 222 | `theme:nameless-jp` | 1 | 10 | 1 | 1 | hotlink×10 |  |
| 223 | `theme:normal-jp` | 1 | 37 | 1 | 0 | hotlink×35, pseudo-ref×2 |  |
| 224 | `theme:obflow-jp` | 1 | 6 | 1 | 1 | hotlink×6 |  |
| 225 | `theme:oneiroi-west-jp` | 1 | 6 | 2 | 1 | hotlink×6 |  |
| 226 | `theme:opinions-broadcaster-jp` | 1 | 34 | 4 | 2 | hotlink×29, foreign-include×3, pseudo-ref×2 |  |
| 227 | `theme:horn-jp` | 1 | 5 | 1 | 2 | hotlink×4, pseudo-ref×1 |  |
| 228 | `theme:ink-jp` | 1 | 20 | 5 | 4 | hotlink×16, pseudo-ref×4 |  |
| 229 | `theme:inland-empire-jp` | 1 | 6 | 3 | 2 | hotlink×5, pseudo-ref×1 |  |
| 230 | `theme:kitchen-jp` | 1 | 126 | 1 | 2 | hotlink×125, pseudo-ref×1 |  |
| 231 | `theme:lead-by-example-jp` | 1 | 16 | 0 | 2 | hotlink×16 |  |
| 232 | `theme:07k-jp` | 1 | 3 | 0 | 1 | pseudo-ref×2, hotlink×1 |  |
| 233 | `theme:a-midnight-invitation-jp` | 1 | 4 | 2 | 1 | pseudo-ref×4 |  |
| 234 | `theme:animal-instead-of-beast-jp` | 1 | 4 | 1 | 1 | pseudo-ref×4 |  |
| 235 | `theme:anniversary-jp` | 1 | 3 | 0 | 1 | pseudo-ref×3 |  |
| 236 | `theme:atlas-maniacus-jp` | 1 | 3 | 2 | 0 | pseudo-ref×3 |  |
| 237 | `theme:back-jan-fire-jp` | 1 | 2 | 0 | 0 | hotlink×1, pseudo-ref×1 |  |
| 238 | `theme:bulgunae-jp` | 1 | 10 | 0 | 7 | hotlink×6, old-bhl×2, http×1, pseudo-ref×1 |  |
| 239 | `theme:chatscp-jp` | 1 | 1 | 3 | 1 | pseudo-ref×1 |  |
| 240 | `theme:creature-jp` | 1 | 4 | 3 | 1 | hotlink×2, pseudo-ref×2 |  |
| 241 | `theme:cyber-specter-jp` | 1 | 4 | 2 | 1 | hotlink×3, pseudo-ref×1 |  |
| 242 | `theme:peroxide-jp` | 1 | 37 | 0 | 2 | hotlink×18, foreign-include×17, pseudo-ref×2 |  |
| 243 | `theme:petrifaction-jp` | 1 | 9 | 0 | 2 | hotlink×8, pseudo-ref×1 |  |
| 244 | `theme:progress-institute-jp` | 1 | 4 | 0 | 2 | hotlink×3, pseudo-ref×1 |  |
| 245 | `theme:redsquare-jp` | 1 | 4 | 2 | 1 | hotlink×3, pseudo-ref×1 |  |
| 246 | `theme:rima-jp` | 1 | 19 | 3 | 2 | hotlink×15, foreign-include×3, pseudo-ref×1 |  |
| 247 | `theme:wish-for-miracle-jp` | 1 | 9 | 0 | 1 | hotlink×6, pseudo-ref×3 |  |
| 248 | `theme:yore-jp` | 1 | 12 | 0 | 1 | hotlink×9, pseudo-ref×3 |  |
| 249 | `theme:pacom1943-jp` | 1 | 8 | 1 | 1 | pseudo-ref×8 |  |
| 250 | `theme:past-oriented-jp` | 1 | 3 | 0 | 1 | pseudo-ref×3 |  |
| 251 | `theme:path-of-jinin-jp` | 1 | 6 | 1 | 1 | pseudo-ref×6 |  |
| 252 | `theme:plugsoft-jp` | 1 | 3 | 1 | 1 | pseudo-ref×2, hotlink×1 |  |
| 253 | `theme:rok-gov-theme-jp` | 1 | 1 | 2 | 0 | pseudo-ref×1 |  |
| 254 | `theme:rpma-jp` | 1 | 7 | 0 | 1 | hotlink×6, pseudo-ref×1 |  |
| 255 | `theme:some-guider-jp` | 1 | 12 | 1 | 1 | hotlink×11, pseudo-ref×1 |  |
| 256 | `theme:the-buck-stops-here-jp` | 0 | 0 | 1 | 0 | — |  |
| 257 | `theme:the-greatest-education-jp` | 1 | 4 | 2 | 1 | hotlink×3, pseudo-ref×1 |  |
| 258 | `theme:shivering-night-jp` | 1 | 22 | 4 | 1 | pseudo-ref×22 |  |
| 259 | `theme:sodium-jp` | 1 | 9 | 3 | 0 | pseudo-ref×9 |  |
| 260 | `theme:sodium-pentasulfide-jp` | 1 | 11 | 4 | 1 | pseudo-ref×11 |  |
| 261 | `theme:sound-jp` | 1 | 31 | 0 | 1 | pseudo-ref×31 |  |
| 262 | `theme:starbasalt-jp` | 1 | 1 | 1 | 1 | pseudo-ref×1 |  |
| 263 | `theme:doap-bhl-jp` | 1 | 9 | 1 | 1 | pseudo-ref×9 |  |
| 264 | `theme:doap-nvl-jp` | 1 | 8 | 1 | 0 | pseudo-ref×8 |  |
| 265 | `theme:flowergarden-jp` | 1 | 8 | 0 | 1 | pseudo-ref×8 |  |
| 266 | `theme:fmaf-theme-jp` | 1 | 4 | 0 | 0 | pseudo-ref×4 |  |
| 267 | `theme:fogwalker-jp` | 1 | 6 | 0 | 1 | pseudo-ref×6 |  |
| 268 | `theme:madoka-jp` | 1 | 95 | 2 | 1 | pseudo-ref×95 |  |
| 269 | `theme:magazine-jp` | 1 | 31 | 1 | 3 | pseudo-ref×30, hotlink×1 |  |
| 270 | `theme:magicity-jp` | 1 | 15 | 2 | 1 | pseudo-ref×15 |  |
| 271 | `theme:marchen-jp` | 1 | 19 | 1 | 1 | pseudo-ref×15, hotlink×4 |  |
| 272 | `theme:mox-jp` | 1 | 59 | 3 | 4 | pseudo-ref×59 |  |
| 273 | `theme:jiha-jp` | 1 | 7 | 3 | 1 | pseudo-ref×7 |  |
| 274 | `theme:kcia10-jp` | 1 | 2 | 4 | 1 | pseudo-ref×2 |  |
| 275 | `theme:king-s-palace-jp` | 1 | 4 | 3 | 2 | pseudo-ref×4 |  |
| 276 | `theme:legend-of-blue-jp` | 1 | 6 | 0 | 1 | pseudo-ref×6 |  |
| 277 | `theme:minimal-scp-foundation-by-cocoonist-jp` | 1 | 1 | 1 | 1 | pseudo-ref×1 |  |
| 278 | `theme:mole-cricket-jp` | 1 | 4 | 1 | 1 | pseudo-ref×4 |  |
| 279 | `theme:mr-reprisal-jp` | 1 | 4 | 1 | 1 | pseudo-ref×4 |  |
| 280 | `theme:navla-style-jp` | 1 | 3 | 2 | 1 | pseudo-ref×3 |  |
| 281 | `theme:note-theme-jp` | 1 | 6 | 0 | 1 | pseudo-ref×6 |  |
| 282 | `theme:ontology-department-jp` | 1 | 2 | 0 | 0 | pseudo-ref×2 |  |
| 283 | `theme:foundation-paper-jp` | 1 | 1 | 2 | 0 | pseudo-ref×1 |  |
| 284 | `theme:garak-the-magazine-jp` | 1 | 3 | 2 | 1 | pseudo-ref×3 |  |
| 285 | `theme:golden-samdaecheon-jp` | 1 | 4 | 3 | 1 | pseudo-ref×4 |  |
| 286 | `theme:halloween-koreana-jp` | 1 | 3 | 1 | 0 | pseudo-ref×3 |  |
| 287 | `theme:it-pillar-of-industry-jp` | 1 | 6 | 1 | 1 | pseudo-ref×6 |  |

## Totals

- Rows: **287** (286 checks + 1 EXCEPTION: no candidate, amethyst-v2).
- Themes at baseline exit 0: **10**.
- Themes at baseline exit 1: **276**.
- Errors / warns / infos (sum over checks): **2357 / 413 / 353**.
- Total errors by code across the population:
  - `pseudo-ref`: **1355**
  - `hotlink`: **912**
  - `http`: **46**
  - `foreign-include`: **36**
  - `old-bhl`: **5**
  - `no-credit`: **1**
  - `no-rate`: **1**
  - `unencoded-colon`: **1**

LEDGER-T1: COMPLETE
