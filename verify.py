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

Incremental behaviour (added 2026-11-16 — a full re-fetch of every page on
every run wasted ~35 minutes and 1,157 HTTPS fetches even when nothing had
changed):

* Wikijump side: ALL page texts are fetched in ONE psql query (the pattern
  proven by verify_scoped.py), never one subprocess per page.
* Wikidot side: a paginated ListPages sweep first collects every page's
  updated_at in a handful of calls. A page's source text is fetched only
  when the cache cannot prove it unchanged: the cache entry must match
  BOTH the canonical file's sha256 AND the sweep's current updated_at.
  If either differs (or there is no entry, or the sweep has no probe for
  the page), the page is fetched fresh and the cache entry is replaced.
  Re-running with nothing changed therefore re-fetches ~nothing and
  finishes in about a minute.

The cache lives outside the repo (~/.cache/wikijump-verify/<repo-key>.json)
and is only ever a shortcut to the same comparison: every page is still
compared, from text the probe proved current. `--no-cache` ignores the
cache for reading and rebuilds it. `--cache-file PATH` overrides the
cache location. Run statistics go to stderr; stdout keeps the original
contract (drift list, or the final "OK: N pages match on both wikis").

Known limit: updated_at is second-resolution. Two edits to the same page
within one second, the second restoring identical text, could in theory
keep a stale probe — use `--no-cache` when that class of doubt matters.
"""
import hashlib
import json
import os
import subprocess
import sys
import time

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


def wikijump_sources(fns):
    """Fetch every requested Wikijump-side page in ONE psql subprocess.

    Returns {slug: contents}. Missing pages are simply absent from the dict.
    Contents are carried as JSON so multi-line text survives a single
    -Atc query intact. (Pattern from verify_scoped.py.)
    """
    if not fns:
        return {}

    def esc(s):
        return s.replace("'", "''")

    in_list = ", ".join("'" + esc(fn) + "'" for fn in fns)
    q = (
        "SELECT COALESCE(json_agg(json_build_object('slug', p.slug, 'contents', t.contents)), '[]'::json) "
        "FROM page p "
        "JOIN page_revision pr ON pr.revision_id = p.latest_revision_id "
        "JOIN text t ON t.hash = pr.wikitext_hash "
        f"WHERE p.site_id = 6000303 AND p.slug IN ({in_list})"
    )
    out = subprocess.run(
        ["docker", "exec", "-u", "wikijump", "wikijump-stafflab-database-1",
         "psql", "-U", "wikijump", "-d", "wikijump", "-Atc", q],
        capture_output=True, text=True, check=True,
    ).stdout.strip()
    rows = json.loads(out) if out else []
    return {row["slug"]: row["contents"] for row in rows}


def existing_files():
    d = os.path.join(REPO, "pages-existing")
    if not os.path.isdir(d):
        return []
    return sorted(f[:-4] for f in os.listdir(d) if f.endswith(".txt"))


def default_cache_path():
    base = os.environ.get("XDG_CACHE_HOME") or os.path.expanduser("~/.cache")
    d = os.path.join(base, "wikijump-verify")
    os.makedirs(d, exist_ok=True)
    key = hashlib.sha256(os.path.realpath(REPO).encode()).hexdigest()[:16]
    return os.path.join(d, key + ".json")


def load_cache(path):
    try:
        with open(path, encoding="utf-8") as f:
            data = json.load(f)
        if data.get("version") == 1 and isinstance(data.get("pages"), dict):
            return data["pages"]
    except Exception:
        pass
    return {}


def save_cache(path, pages):
    tmp = path + ".tmp"
    with open(tmp, "w", encoding="utf-8") as f:
        json.dump({"version": 1, "pages": pages}, f)
    os.replace(tmp, path)


def wikidot_probe(site):
    """{fullname: updated_at} for every page on the Wikidot check wiki,
    collected with paginated ListPages searches (a few calls total)."""
    probe = {}
    offset, per = 0, 250
    while True:
        items = list(site.pages.search(offset=offset, limit=per, perPage=per))
        for pg in items:
            fn = getattr(pg, "fullname", None)
            if fn:
                ua = getattr(pg, "updated_at", None)
                # updated_at arrives as a datetime; only equality matters,
                # and the cache is JSON, so keep its string form.
                probe[fn] = None if ua is None else str(ua)
        if len(items) < per:
            return probe
        offset += per


def main():
    from wd_common import get_client

    argv = sys.argv[1:]
    use_cache = "--no-cache" not in argv
    cache_file = default_cache_path()
    if "--cache-file" in argv:
        cache_file = argv[argv.index("--cache-file") + 1]
    started = time.time()

    files = sorted(
        f[:-4] for f in os.listdir(os.path.join(REPO, "pages")) if f.endswith(".txt")
    )
    pairs = [("pages", fn) for fn in files] + [("pages-existing", fn) for fn in existing_files()]
    canonical = {}
    canon_sha = {}
    for subdir, fn in pairs:
        text = open(os.path.join(REPO, subdir, fn + ".txt"), encoding="utf-8").read()
        canonical[fn] = text
        canon_sha[fn] = hashlib.sha256(text.encode("utf-8")).hexdigest()

    client = get_client()
    site = client.site.get("sigma10-jp-test")

    # Wikijump side: one query for everything.
    wj = wikijump_sources([fn for _, fn in pairs if fn not in WIKIDOT_ONLY])

    # Wikidot side: probe sweep, then fetch only what the cache cannot
    # prove unchanged.
    probe = wikidot_probe(site)
    cache = load_cache(cache_file) if use_cache else {}
    new_cache = {}
    wd_text = {}
    fetched = reused = 0
    for _, fn in pairs:
        entry = cache.get(fn)
        ua = probe.get(fn)
        if (
            entry
            and ua is not None
            and entry.get("ua") == ua
            and entry.get("canon") == canon_sha[fn]
        ):
            wd_text[fn] = entry["text"]
            new_cache[fn] = entry
            reused += 1
            continue
        try:
            text = site.page.get(fn).source.wiki_text
        except Exception as e:
            wd_text[fn] = e  # remember the failure for the drift report
            fetched += 1
            continue
        wd_text[fn] = text
        new_cache[fn] = {"canon": canon_sha[fn], "ua": ua, "text": text}
        fetched += 1
    save_cache(cache_file, new_cache)

    drift = []
    for _, fn in pairs:
        wd = wd_text[fn]
        if isinstance(wd, Exception):
            drift.append((fn, "wikidot fetch failed: " + str(wd)[:80]))
            continue
        if norm(wd) != norm(canonical[fn]):
            drift.append((fn, "wikidot differs from canonical"))
        if fn in WIKIDOT_ONLY:
            continue
        got = wj.get(fn)
        if got is None:
            drift.append((fn, "missing on wikijump"))
        elif norm(got) != norm(to_wikijump_form(fn, canonical[fn])):
            drift.append((fn, "wikijump differs from canonical (after A1/A2)"))

    print(
        f"verify: {len(pairs)} pages; wikidot fetched {fetched}, cache-reused {reused}; "
        f"elapsed {time.time() - started:.1f}s",
        file=sys.stderr,
    )
    if drift:
        print("DRIFT on", len(drift), "page(s):")
        for fn, why in drift:
            print(" -", fn, ":", why)
        return 1
    print("OK:", len(pairs), "pages match on both wikis")
    return 0


if __name__ == "__main__":
    sys.exit(main())
