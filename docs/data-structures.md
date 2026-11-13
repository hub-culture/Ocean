# Data structures

The export in `data/processed/qem/` is written by the QEM's `qem export ocean` and `qem export layers` and published every Monday. This page describes it as of the export of 9 November 2026 (format 1). Fields may be added; existing fields keep their meaning.

Times are UTC. Temperatures are °C. Positions are WGS 84 decimal degrees.

## `manifest.json`

| Field | Meaning |
| --- | --- |
| `format` | Always `1` for now |
| `latest_day` | The last UTC day the export covers |
| `published` | When it was published |
| `files` | For every other file: `sha256` and `bytes`. `scripts/validate.py` checks them |

## `data.json`

| Field | Meaning |
| --- | --- |
| `version` | Export version (`1`) |
| `tolerance_c` | How close two sea temperatures must be to agree (1.0 °C) |
| `totals` | Counts: `specks`, hourly `triangles` and their `certain` / `guesses` / `refuted`; `daily_*` for the daily three-way check (gauge, satellite analysis, model); `three_*` for the hourly three-source check; `from` and `to` |
| `sources` | One row per source: `id`, `name`, `role`, `access`, `enabled`, `lineage`, `home`, `licence`, `specks` (how many it contributed) |
| `places` | Fixed stations (tide gauges, weather buoys, moored buoys) |
| `argo` | Argo float profiles, each its own place |
| `reefs` | Coral reef sites with daily heat stress |
| `countries` | Atlantic Rim countries with protection, finance and aid |

### `places[]`

| Field | Meaning |
| --- | --- |
| `name`, `lat`, `lon` | The station |
| `gauge` | The source id of its sensor (`noaa-coops`, `marine-ie`, `pirata`) |
| `country`, `eez`, `ecoregion` | Where it is (EEZ from Marine Regions; ecoregion from the Marine Ecoregions of the World, both with Marine Regions `mrgid`s in the QEM) |
| `certain`, `guesses`, `refuted` | Hourly verdicts over the export's window |
| `hours[]` | `t`, `gauge` (the sensor's reading), `model` (Open-Meteo's model at the nearest sea cell), `state` (the verdict of gauge vs model), `copernicus` (Copernicus Marine's reading, when fetched), `state3` (the three-source verdict, when a model of another lineage exists) |
| `days[]` | The daily check: `date`, `gauge_mean`, `analysis` (NASA/JPL MUR satellite analysis), `model_mean`, `state` (two of three within the tolerance) |
| `oisst[]` | NOAA OISST daily analysis, `t` and `value`. Kept on the line, not used to triangulate: it shares NOAA's lineage with the NOAA gauges. Empty where OISST counts the cell as land |
| `occurrences`, `species[]` | OBIS species records within 0.25° (a year behind, as OBIS is): total, and `name` / `records` per species. Names of people are never kept |

PIRATA buoys report one daily mean, shown at midday in `hours` and weighed in `days`.

### `argo[]`

`place` (float and profile), `lat`, `lon` (rounded to 4 decimals from the next export), `t`, `gauge` (near-surface temperature, top 10 dbar), `model`, `state`, `copernicus`, `state3`.

### `reefs[]`

`name`, `lat`, `lon`, `country`, `ecoregion`, and `days[]` from NOAA Coral Reef Watch's 5 km product:

| Field | Meaning |
| --- | --- |
| `date` | The day CRW's grid is for (CRW is two days behind) |
| `alert`, `alert_name` | Bleaching Alert Area: 0 No Stress, 1 Watch, 2 Warning, 3 Alert Level 1, 4 Alert Level 2 |
| `dhw` | Degree Heating Weeks: heat stress accumulated over 12 weeks |
| `hotspot` | Today's temperature above the warmest-month mean (negative means cooler) |
| `sst_anomaly` | Today's temperature against the long-term mean for the day |

A reef can show high `dhw` with `alert` 0 after a heatwave passes: `alert` follows today's `hotspot`, while `dhw` carries the 12 weeks behind it. A missing day means CRW had no grid for it; the QEM asks again on later runs.

### `countries[]`

| Field | Meaning |
| --- | --- |
| `name`, `iso3` | The country |
| `mpa_share` | `year`, `value`: marine protected areas as % of territorial waters (World Bank ER.MRN.PTMR.ZS, from Protected Planet) |
| `kba_protected` | `year`, `value`: % of marine Key Biodiversity Areas covered by protected areas (UN SDG 14.5.1) |
| `owid[]` | From the next export: Our World in Data fisheries, seafood and emissions series, latest value of each, credited to the producer behind it (FAO, Global Carbon Project) |
| `projects[]` | World Bank projects tagged with ocean themes: `id`, `name`, `country`, `iso2`, `commitment_usd` (whole project, not its ocean share), `status`, `approved`, `theme`, `url` |
| `aid[]` | IATI aid activities: `id`, `title`, `donor`, `status` (IATI activity status: 1 pipeline, 2 implementation, 3 finalisation, 4 closed), `start`, `end`, `share` (this country's reported %, if any), `url` (d-portal), and from the next export `related_ids`: other IATI records of the same activity folded into this row. Amounts are not stored |

## `layers/`

`layers.json` lists each layer: `id`, `name`, `description`, `geometry`, `h3_resolutions`, `attribution` (every source with its licence), `features`, `file`. Addressing follows the Gaia spec: `MIP1|GAIA|CELL|{h3index}`.

| Layer | Geometry | Properties |
| --- | --- | --- |
| `ocf-ocean-observations` | Point | `kind`, `name`, `gauge`, `country`, `ecoregion`, `hours_certain`, `hours_guesses`, `days_checked`, `species_records`, `h3_r6`, `h3_r9` |
| `ocf-reef-heat-stress` | Point | `kind`, `name`, `country`, `ecoregion`, `date`, `alert`, `alert_name`, `dhw`, `h3_r6`, `h3_r9` (latest day) |
| `ocf-eez-protection-finance` | MultiPolygon | `kind`, `name`, `mrgid` (Marine Regions id), `sovereign`, `country_iso3`, `area_km2`, `mpa_share_territorial`, `kba_protected`, `ocean_projects_active`, `ocean_commitment_active_usd`, `aid_activities_live`, `h3_r4` |
| `ocf-microplastics` | Point | NOAA NCEI marine microplastics: `kind`, `date`, `ocean`, `region`, `country`, `medium`, `sample`, `method`, `mesh_mm`, `value`, `unit`, `class`, `reference`, `doi`, `h3_r6`, `h3_r9` |
| `ocf-sargassum` | Point (box centres) | NOAA AOML AFAI sargassum index over boxes: `kind`, `name`, `time`, `afai_mean`, `afai_max`, `clear_cells`, `cells_at_cap`, `share_at_cap`, `composites`, `box_half_deg`, `h3_r6`, `h3_r9` |

## Changes

- **Next export (16 November 2026):** Argo positions rounded to 4 decimals and CRW anomalies and aid shares to 2 (they carried float32 noise such as `0.7000000000000001`); IATI records of one activity folded into one `aid` row with `related_ids`; `owid[]` added to each country.
