# Ocean 🌊

The open data repository of the **Ocean Data Initiative**, led by the [Ocean Climate Fund](https://oceanclimatefund.com) with Hub Culture. Launched at COP31, Antalya, November 2026. Free and open source.

## 📈 Live data

[`data/processed/qem/`](data/processed/qem/) holds the Initiative's latest export, refreshed every Monday by Hub Culture's QEM. It's the data behind [oceanclimatefund.com/data/OceanDataInitiative](https://oceanclimatefund.com/data/OceanDataInitiative).

- `data.json`: tide gauges, buoys and Argo floats checked against ocean models (Copernicus Marine, NOAA OISST, MUR), coral reef heat stress (NOAA Coral Reef Watch), and marine protection, ocean finance and aid for every Atlantic Rim country (Protected Planet via the World Bank, UN SDG, World Bank projects, IATI).
- `layers/`: the same as GeoJSON map layers tagged with H3 cells, for any GIS tool and for the Gaia map. `layers/layers.json` lists each layer's sources, licences and H3 resolutions.
- `manifest.json`: every file's size and SHA-256, and the last day the export covers.

Earlier weeks are in this repo's history.

## How the data is checked

Every reading is a *speck* in the QEM: content-addressed, signed, and carrying its source's licence. A reading starts unlit and is marked **certain** only when an independent source agrees with it (a tide gauge and an ocean model within 1 °C, say), a **guess** when no independent source agrees yet, and **refuted** when independent sources outvote it. Copies of one source count once. See [docs/data-structures.md](docs/data-structures.md) for every field.

## What's here

| Path | What it is |
| --- | --- |
| [`data/processed/qem/`](data/processed/qem/) | The weekly export (published automatically; don't edit by hand) |
| [`data/sources.json`](data/sources.json) | Every source the Initiative reads or is preparing to read, with access, licence and whether it is live |
| [`docs/data-structures.md`](docs/data-structures.md) | The export's files and fields |
| [`docs/resources.md`](docs/resources.md) | Ocean data resources: the OCF's list of 25 providers, and what has been added since, including blue carbon, ocean carbon and MPA sources |
| [`scripts/validate.py`](scripts/validate.py) | Checks the export against its manifest and every map layer for valid geometry; runs on every push |
| [`scripts/build_sources.py`](scripts/build_sources.py) | Rebuilds `data/sources.json` from the QEM's source registry |

## Use it

```bash
git clone https://github.com/hub-culture/Ocean.git
cd Ocean
python3 scripts/validate.py      # check the files against the manifest
```

```python
import json
d = json.load(open("data/processed/qem/data.json"))
for place in d["places"]:
    print(place["name"], place["certain"], "certain hours of", len(place["hours"]))
```

The GeoJSON layers open directly in QGIS, kepler.gl, Mapbox or geojson.io.

## Related

- [hub-culture/Commons](https://github.com/hub-culture/Commons): the Global Commons Initiative, where the ocean is the first test case and the **Open Blue Carbon Registry** is being built ([design](https://github.com/hub-culture/Commons/blob/main/docs/blue-carbon-registry.md)).
- The Bermuda Standard: the QEM's climate engine (CO₂, methane, global temperature, sea ice, Bermuda's air), run alongside this Initiative.

## Contributing

Data partners, scientists and developers are welcome. Read [CONTRIBUTING.md](CONTRIBUTING.md), then open an issue or a pull request.

## Licence

Code and documentation in this repository are under the [MIT License](LICENSE). **The data keeps each source's own licence and terms**, listed per layer in `layers/layers.json` and per source in `data/sources.json`. Most sources are public domain or CC BY 4.0; a few (OBIS datasets marked CC BY-NC, Open-Meteo's free tier) are for non-commercial use only. Credit the sources when you use the data.
