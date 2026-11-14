#!/usr/bin/env python3
"""Verify the two check wikis match this repository's canonical sources.

Canonical text = the Wikidot-side text in pages/<fullname>.txt.
The Wikijump side must equal the canonical text after the ALLOWLIST A1/A2
transforms (which apply only inside theme-decoration-sample), modulo a
trailing-newline difference, which is exempt.

Run with the wikidot.py venv python from the wikidot.py checkout:
  cd /home/roku/src/Rokurolize/wikidot.py && .venv/bin/python \
      /home/roku/src/Rokurolize/sigma10-check-wiki/verify.py
Exit code 0 = no drift; 1 = drift (pages listed).
"""
import json
import os
import subprocess
import sys

sys.path.insert(0, "/home/roku/.local/state/wikijump/muse-bhl/sigma10-unify-20261114")
REPO = os.path.dirname(os.path.abspath(__file__))


# Pages that exist on the Wikidot check wiki only, by design:
# theme:sigma-10-jp is delivered to the JP environment by CDN (GitHub Pages),
# not by a local theme page on the Wikijump side (declared in the brief).
WIKIDOT_ONLY = {"theme:sigma-10-jp"}


def to_wikijump_form(fn, text):
    if fn == "theme-decoration-sample":
        text = text.replace(
            "sigma10-jp-test.wdfiles.com", "scp-jp-sigma10.wjfiles.localhost:28443"
        )
        text = text.replace("[[*user voted-fated-smuggler]]", "[[*user daveyoufool]]")
    return text


def norm(t):
    return "\n".join(line.rstrip() for line in t.rstrip("\n").split("\n"))


def wikijump_source(fn):
    q = (
        "SELECT t.contents FROM page p "
        "JOIN page_revision pr ON pr.revision_id = p.latest_revision_id "
        "JOIN text t ON t.hash = pr.wikitext_hash "
        f"WHERE p.site_id = 6000303 AND p.slug = '{fn}'"
    )
    out = subprocess.run(
        ["docker", "exec", "-u", "wikijump", "wikijump-stafflab-database-1",
         "psql", "-U", "wikijump", "-d", "wikijump", "-Atc", q],
        capture_output=True, text=True, check=True,
    ).stdout
    if out == "":
        return None
    return out[:-1] if out.endswith("\n") else out



def existing_files():
    d = os.path.join(REPO, "pages-existing")
    if not os.path.isdir(d):
        return []
    return sorted(f[:-4] for f in os.listdir(d) if f.endswith(".txt"))

def main():
    from wd_common import get_client

    files = sorted(
        f[:-4] for f in os.listdir(os.path.join(REPO, "pages")) if f.endswith(".txt")
    )
    client = get_client()
    site = client.site.get("sigma10-jp-test")
    drift = []
    for fn in files + existing_files():
        canonical = open(os.path.join(REPO, "pages", fn + ".txt"), encoding="utf-8").read()
        try:
            wd = site.page.get(fn).source.wiki_text
        except Exception as e:
            drift.append((fn, "wikidot fetch failed: " + str(e)[:80]))
            continue
        if norm(wd) != norm(canonical):
            drift.append((fn, "wikidot differs from canonical"))
        if fn in WIKIDOT_ONLY:
            continue
        got = wikijump_source(fn)
        if got is None:
            drift.append((fn, "missing on wikijump"))
        elif norm(got) != norm(to_wikijump_form(fn, canonical)):
            drift.append((fn, "wikijump differs from canonical (after A1/A2)"))
    if drift:
        print("DRIFT on", len(drift), "page(s):")
        for fn, why in drift:
            print(" -", fn, ":", why)
        return 1
    print("OK:", len(files), "pages match on both wikis")
    return 0


if __name__ == "__main__":
    sys.exit(main())
