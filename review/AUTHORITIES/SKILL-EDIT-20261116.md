# Staff skill local edit — sigma10-jp-test as a draft wiki (2026-11-16, owner order)

The theme-component-review skill's draft model names only pseudo-scp-jp as the draft wiki.
The Sigma-10 migration display-check wiki (sigma10-jp-test) did not exist in that model, so
check_source.py flagged every sigma10-jp-test reference as `hotlink` (prohibited direct link)
and render_check.py flagged its runtime hosts as `runtime-hotlink` errors. The coordinator's
T1 classification had treated those references as draft-sanctioned by analogy to localize
pattern 4 instead of against the skill's literal draft-host definition; the owner corrected
this (2026-11-16 18:55) and ordered the skill edited to allow sigma10-jp-test explicitly.

Edits (local working tree of /home/roku/src/SCP-JP/claude-plugins-staff — the SCP-JP org
clone; UNCOMMITTED and not pushed; upstreaming is a staff-review matter):
- scripts/check_source.py: DRAFT_HOSTS = ("pseudo-scp-jp.", "sigma10-jp-test."); draft-host
  resource references and includes now yield `pseudo-ref` naming the actual host; hotlink
  hint text mentions sigma10-jp-test for the Sigma-10 check.
- scripts/render_check.py: sigma10-jp-test.* hosts count as draft hosts (info `draft-host`),
  excluded from `runtime-hotlink`.
- SKILL.md: definitional bullet — for the Sigma-10 migration check, sigma10-jp-test plays
  the draft-wiki role, same treatment as pseudo-scp-jp.
- references/structure.md, references/localize.md (pattern 4): sigma10-jp-test local--code
  named as the draft form in that environment.
- references/operations.md, references/checklist.md: sigma10-jp-test added to the
  must-not-remain-at-posting reference lists.

Verification: check_source.py on theme:basalt-jp after the edit — still error 34 / warn 2 /
info 2, but every sigma10-jp-test reference is now `pseudo-ref`; remaining `hotlink` lines
are genuinely outside hosts (fonts.bunny.net, scp-wiki.wdfiles.com).

Consequence for GOSIGN2: host-class codes in REPORT-GOSIGN2-SOURCE.md (and any lane output
produced before ~18:57 JST) use the old codes; the (i)/(ii)/(iii) substance is unchanged
(pseudo-ref = rewrite at posting). The GOSIGN2-LEDGER baseline will be a fresh mechanical
re-run of the edited checker over all 287 candidates.
