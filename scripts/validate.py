"""Checks the published Ocean Data Initiative export in data/processed/qem/.

- manifest.json lists every file with its SHA-256 and size, and they match;
- every file the export holds is in the manifest;
- data.json is a version 1 export with places, countries, sources and totals;
- every GeoJSON layer parses, is a FeatureCollection, has the feature count
  layers.json claims, and has no empty geometry or coordinate out of range;
- data/sources.json, if present, parses and has unique ids.

Standard library only. Exit code 1 on any problem.

    python3 scripts/validate.py
"""
import hashlib
import json
import math
import pathlib
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
QEM = ROOT / "data/processed/qem"
problems = []


def problem(msg: str) -> None:
    problems.append(msg)
    print("FAIL", msg)


def coords(geom):
    """Yields every (lon, lat) pair in a GeoJSON geometry."""
    def walk(c):
        if c and isinstance(c[0], (int, float)):
            yield c
        else:
            for x in c:
                yield from walk(x)
    if geom.get("type") == "GeometryCollection":
        for g in geom.get("geometries", []):
            yield from coords(g)
    else:
        yield from walk(geom.get("coordinates") or [])


manifest = json.loads((QEM / "manifest.json").read_text())
if manifest.get("format") != 1:
    problem("manifest.json: format is not 1")
listed = set(manifest.get("files", {}))
on_disk = {str(p.relative_to(QEM)) for p in QEM.rglob("*") if p.is_file() and p.name != "manifest.json"}
for name in sorted(on_disk - listed):
    problem(f"{name}: in the export but not in manifest.json")
for name, want in sorted(manifest.get("files", {}).items()):
    path = QEM / name
    if not path.exists():
        problem(f"{name}: in manifest.json but missing")
        continue
    body = path.read_bytes()
    if hashlib.sha256(body).hexdigest() != want["sha256"] or len(body) != want["bytes"]:
        problem(f"{name}: SHA-256 or size differs from manifest.json")

data = json.loads((QEM / "data.json").read_text())
if data.get("version") != 1:
    problem("data.json: not a version 1 export")
for key in ("places", "countries", "sources", "totals"):
    if not data.get(key):
        problem(f"data.json: no {key}")
for p in data.get("places", []):
    if not (-90 <= p["lat"] <= 90 and -180 <= p["lon"] <= 180):
        problem(f"data.json: place {p['name']} has an impossible position")

layers = json.loads((QEM / "layers/layers.json").read_text())
for layer in layers.get("layers", []):
    path = QEM / "layers" / layer["file"]
    g = json.loads(path.read_text())
    if g.get("type") != "FeatureCollection":
        problem(f"{layer['file']}: not a FeatureCollection")
        continue
    feats = g.get("features", [])
    if len(feats) != layer.get("features"):
        problem(f"{layer['file']}: {len(feats)} features, layers.json says {layer.get('features')}")
    for i, f in enumerate(feats):
        geom = f.get("geometry")
        if not geom or not (geom.get("coordinates") or geom.get("geometries")):
            problem(f"{layer['file']} feature {i}: empty geometry")
            continue
        for c in coords(geom):
            lon, lat = c[0], c[1]
            if not (math.isfinite(lon) and math.isfinite(lat) and -180 <= lon <= 180 and -90 <= lat <= 90):
                problem(f"{layer['file']} feature {i}: coordinate {c} out of range")
                break

sources = ROOT / "data/sources.json"
if sources.exists():
    rows = json.loads(sources.read_text())["sources"]
    ids = [r["id"] for r in rows]
    if len(ids) != len(set(ids)):
        problem("data/sources.json: duplicate ids")

print(f"export of {manifest.get('latest_day')}: {len(listed)} files, "
      f"{len(data.get('places', []))} places, {len(layers.get('layers', []))} layers")
print("ok" if not problems else f"{len(problems)} problem(s)")
sys.exit(1 if problems else 0)
