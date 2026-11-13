"""Builds data/sources.json, the catalogue of every source the Ocean Data
Initiative reads or is preparing to read, from the QEM's source registry
(hub-culture/qem, sources/registry.json).

    python3 scripts/build_sources.py path/to/qem/sources/registry.json
"""
import json
import sys

reg = json.load(open(sys.argv[1]))
rows = []
for s in reg["sources"]:
    rows.append({
        "id": s["id"],
        "name": s["name"],
        "home": s.get("home", ""),
        "programme": "bermuda-standard" if s.get("role") == "climate" or s.get("bcde") else "ocean",
        "role": s.get("role", ""),
        "access": s.get("access", ""),
        "live": bool(s.get("enabled")),
        "on_ocf_list": bool(s.get("ocf")),
        "licence": s.get("licence", ""),
        "about": s.get("what", ""),
    })
out = {
    "about": "Every source the Ocean Data Initiative (and the Bermuda Standard's climate engine) reads, "
             "or is preparing to read. live=true: fetched every week by the QEM. live=false: listed, "
             "with a reader still to build or access still to arrange. Being listed is not trust: every "
             "reading starts unlit and brightens only when independent sources agree. Built from "
             "hub-culture/qem sources/registry.json by scripts/build_sources.py.",
    "sources": rows,
}
open("data/sources.json", "w").write(json.dumps(out, indent=2, ensure_ascii=False) + "\n")
print(f"{len(rows)} sources, {sum(r['live'] for r in rows)} live")
