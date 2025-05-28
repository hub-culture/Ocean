Ocean/
├── README.md
├── LICENSE
├── CONTRIBUTING.md
├── CODE_OF_CONDUCT.md
├── data/
│   ├── raw/
│   ├── processed/
│   ├── metadata/
│   └── sources.json
├── scripts/
│   ├── ingestion/
│   ├── processing/
│   └── visualization/
├── notebooks/
│   └── examples.ipynb
├── docs/
│   ├── architecture.md
│   └── partners.md
└── .github/
    ├── ISSUE_TEMPLATE/
    ├── PULL_REQUEST_TEMPLATE.md
    └── workflows/
        └── data_pipeline.yml

---

# README.md

```markdown
# Ocean Sprint Open Data Repository 🌊

Welcome to the **Ocean Sprint** GitHub repository — an open data initiative led by the Ocean Climate Fund in collaboration with Hub Culture. This project aims to secure **open data architectures and resources** in support of a sustainable future for the world ocean.

## 🌐 Mission

We are building tools, data standards, and resources to:

- Promote transparency and data accessibility across ocean regions
- Support scientific research, policy development, and public engagement
- Foster collaboration through open contributions from global partners

## 📁 Repository Structure

- `data/` — Raw and processed datasets with metadata and [sources.json](data/sources.json)
- `scripts/` — Ingestion, processing, and visualization tools
- `notebooks/` — Jupyter notebooks demonstrating usage
- `docs/` — Technical documentation and architecture
- `.github/` — Workflow automation and contribution templates

## 📊 Getting Started

```bash
# Clone the repository
git clone https://github.com/hub-culture/Ocean.git
cd Ocean
```

Explore sample notebooks in `notebooks/` or start working with data in `data/`.

## 🤝 Contributing

We welcome your contributions! Please review our [CONTRIBUTING.md](CONTRIBUTING.md) and [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md) to get started.

## 📄 License

This project is licensed under the [MIT License](LICENSE).

## 🔗 Learn More

- [Ocean Climate Fund](https://oceanclimatefund.com)
- [Hub Culture Partnerships](https://hubculture.com/partnerships/)
- [World Ocean Summit Activity](https://hubculture.com/hubs/518/events/630/index)
```

---

# LICENSE

```text
MIT License

Copyright (c) 2025 Hub Culture and contributors

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```

---

# data/sources.json

```json
[
  {
    "name": "Example Ocean Temperature Dataset",
    "description": "Sea surface temperature data collected via satellite.",
    "source_url": "https://example.com/ocean-temperature",
    "license": "CC-BY-4.0",
    "last_updated": "2025-05-01",
    "tags": ["temperature", "climate", "satellite"]
  },
  {
    "name": "Marine Protected Areas (MPA) Boundaries",
    "description": "Geospatial data of global MPAs.",
    "source_url": "https://example.com/mpa-boundaries",
    "license": "ODC-By 1.0",
    "last_updated": "2025-04-20",
    "tags": ["biodiversity", "conservation", "geospatial"]
  }
]
```
Ocean/
├── README.md
├── LICENSE
├── CONTRIBUTING.md
├── CODE_OF_CONDUCT.md
├── data/
│   ├── raw/
│   ├── processed/
│   ├── metadata/
│   └── sources.json
├── scripts/
│   ├── ingestion/
│   │   └── fetch_example_dataset.py
│   ├── processing/
│   └── visualization/
├── notebooks/
│   └── examples.ipynb
├── docs/
│   ├── architecture.md
│   └── partners.md
└── .github/
    ├── ISSUE_TEMPLATE/
    ├── PULL_REQUEST_TEMPLATE.md
    └── workflows/
        └── data_pipeline.yml

---

# scripts/ingestion/fetch_example_dataset.py

```python
import os
import requests

DATA_URL = "https://example.com/data/ocean-temperature.csv"
OUTPUT_PATH = os.path.join("data", "raw", "ocean-temperature.csv")

def fetch_data():
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    print(f"Downloading data from {DATA_URL}...")
    response = requests.get(DATA_URL)
    response.raise_for_status()

    with open(OUTPUT_PATH, "wb") as f:
        f.write(response.content)

    print(f"Data saved to {OUTPUT_PATH}")

if __name__ == "__main__":
    fetch_data()
```

---

This script fetches a remote ocean temperature dataset and stores it under `data/raw/`. You can run it with:

```bash
python scripts/ingestion/fetch_example_dataset.py
```

To fully automate this ingestion pipeline later, we can also trigger it using GitHub Actions inside `.github/workflows/data_pipeline.yml`. Let me know when you're ready to scaffold that too.



Here is a curated list of 25 open and publicly accessible APIs and data platforms that provide valuable ocean-related data. These resources are instrumental for researchers, developers, and policymakers working on marine and climate initiatives.
marinedatascience.co

🌊 Top 25 Open Ocean Data APIs & Platforms
Global Fishing Watch API
Access real-time and historical data on global fishing activity to promote transparency in fisheries.
🔗 globalfishingwatch.org/our-apis

NOAA CO-OPS API
Retrieve observations and predictions from NOAA's Center for Operational Oceanographic Products and Services.
🔗 api.tidesandcurrents.noaa.gov

Open-Meteo Marine Weather API
Provides ocean wave forecasts and marine weather data with free access for non-commercial use.
🔗 open-meteo.com

Ocean Networks Canada OpenAPI
Programmatically access Ocean Networks Canada's vast data archive via user-defined code.
🔗 data.oceannetworks.ca/OpenAPI

Sinay Maritime APIs
Offers APIs for ETA predictions, CO₂ monitoring, noise emissions, and port congestion analytics.
🔗 sinay.ai

World Ocean Database (WOD)
The world's largest collection of uniformly formatted, quality-controlled ocean profile data.
🔗 ncei.noaa.gov/products/world-ocean-database

Ocean Biodiversity Information System (OBIS)
A global open-access data and information clearing-house on marine biodiversity.
🔗 obis.org

AquaMaps
Provides modelled distribution maps for marine species based on environmental data.
🔗 aquamaps.org

SeaBASS (SeaWiFS Bio-optical Archive and Storage System)
Archive of in situ oceanographic data supporting satellite remote sensing research.
🔗 seabass.gsfc.nasa.gov

OpenSeaMap
A free nautical chart project collecting and providing open-access marine geospatial data.
🔗 openseamap.org

MarineTraffic API
Provides real-time information on ship movements and ports worldwide.
🔗 marinetraffic.com

Argo Data System
Offers real-time data from a global array of profiling floats measuring temperature and salinity.
🔗 argo.ucsd.edu

EMODnet (European Marine Observation and Data Network)
Provides access to European marine data across various themes like bathymetry and biology.
🔗 emodnet.eu

SeaDataNet
Pan-European infrastructure for managing and providing access to marine data.
🔗 seadatanet.org

ICES Oceanographic Database
Access to oceanographic data collected by the International Council for the Exploration of the Sea.
🔗 ices.dk

Marine Copernicus
Provides free access to operational marine data and services for the global ocean and European seas.
🔗 marine.copernicus.eu

NOAA National Centers for Environmental Information (NCEI) Ocean Archive
Comprehensive archive of oceanographic data collected by NOAA.
🔗 ncei.noaa.gov

Marine Data Exchange (UK)
Platform for sharing UK offshore survey data collected by the marine industry.
🔗 marinedataexchange.co.uk

Australian Ocean Data Network (AODN)
Provides access to a wide range of Australian marine and climate data.
🔗 aodn.org.au

NOAA Fisheries Data Portal
Access to data on fisheries, protected species, and ecosystems managed by NOAA Fisheries.
🔗 fisheries.noaa.gov

Integrated Marine Observing System (IMOS) Australia
Collects and provides free access to marine data from around Australia.
🔗 imos.org.au

SeaDataCloud
Enhances the SeaDataNet infrastructure with cloud services for marine data management.
🔗 seadatanet.org

Marine Institute Data Portal (Ireland)
Provides access to a range of marine data collected by the Marine Institute of Ireland.
🔗 marine.ie

British Oceanographic Data Centre (BODC)
National facility for storing and distributing marine data in the UK.
🔗 bodc.ac.uk

Ocean Data Portal (UNESCO IOC)
Facilitates the discovery and exchange of oceanographic data and services.
🔗 oceandataportal.org


