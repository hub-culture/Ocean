# Ocean data resources

Updated 13 November 2026. The machine-readable version, with licences and access for each, is [`data/sources.json`](../data/sources.json). **Live** means the QEM reads it every week and its readings are in the export.

## The Ocean Climate Fund's list

The 25 open ocean data providers listed at [oceanclimatefund.com/data](https://oceanclimatefund.com/data) when the Initiative began, and where each stands.

| Provider | Status | Access |
| --- | --- | --- |
| [NOAA CO-OPS (Tides and Currents)](https://tidesandcurrents.noaa.gov) | Live: tide-gauge water temperature | Open |
| [Open-Meteo Marine](https://open-meteo.com/en/docs/marine-weather-api) | Live: modelled sea surface temperature | Open (non-commercial free tier) |
| [Marine Institute Ireland](https://erddap.marine.ie/erddap/tabledap/IWBNetwork.html) | Live: M-series weather buoys | Open |
| [Argo](https://argo.ucsd.edu) | Live: floats in the western North Atlantic and off Africa | Open |
| [Copernicus Marine](https://marine.copernicus.eu) | Live: Mercator global ocean model | Free account |
| [OBIS](https://obis.org) | Live: species occurrences near each station | Open |
| [Our World in Data](https://ourworldindata.org) | Live: fisheries, seafood and emissions series | Open |
| [Global Fishing Watch](https://globalfishingwatch.org/our-apis) | Listed: needs a token | Token |
| [Ocean Networks Canada](https://data.oceannetworks.ca/OpenAPI) | Listed: needs a token | Token |
| [EMODnet](https://emodnet.eu) | Listed: reader to build | Open |
| [AODN / IMOS](https://aodn.org.au) | Listed: outside the Atlantic Rim focus | Open |
| [NOAA World Ocean Database](https://www.ncei.noaa.gov/products/world-ocean-database) | Listed: portal | Portal |
| [NOAA Fisheries](https://www.fisheries.noaa.gov) | Listed: reader to build | Open |
| [ICES](https://www.ices.dk) | Listed: reader to build | Open |
| [SeaDataNet](https://www.seadatanet.org) | Listed: account | Account |
| [BODC](https://www.bodc.ac.uk) | Listed: account | Account |
| [Marine Data Exchange (UK)](https://www.marinedataexchange.co.uk) | Listed: account | Account |
| [NASA SeaBASS](https://seabass.gsfc.nasa.gov) | Listed: portal | Portal |
| [AquaMaps](https://www.aquamaps.org) | Listed: portal | Portal |
| [OpenSeaMap](https://www.openseamap.org) | Listed | Open |
| [IODE Ocean Data Portal / ODIS](https://www.oceandataportal.org) | Listed | Open |
| [MarineTraffic](https://www.marinetraffic.com) | Listed: commercial | Commercial |
| [Sinay](https://sinay.ai) | Listed: commercial | Commercial |
| Ocean Sprint / OCF repository | This repository | Open |

## Added since: checks and context

These are live and were added to give each reading an independent second or third voice, or the context around it.

| Resource | What it adds |
| --- | --- |
| [PIRATA moored buoys (NOAA PMEL)](https://www.pmel.noaa.gov/gtmba/pmel-theme/atlantic-ocean-pirata) | Daily sea temperature in the tropical Atlantic, including the African side |
| [NOAA OISST v2.1](https://www.ncei.noaa.gov/products/optimum-interpolation-sst) | Daily blended satellite/ship/buoy analysis |
| [NASA/JPL MUR SST](https://podaac.jpl.nasa.gov/MEaSUREs-MUR) | Daily 1 km satellite analysis: the third voice in the daily check |
| [NOAA Coral Reef Watch](https://coralreefwatch.noaa.gov/product/5km/index.php) | Bleaching alerts and Degree Heating Weeks at Atlantic Rim reefs |
| [NOAA AOML sargassum (AFAI)](https://cwcgom.aoml.noaa.gov/erddap/griddap/noaa_aoml_atlantic_oceanwatch_AFAI_7D.html) | Weekly sargassum index |
| [NOAA NCEI Marine Microplastics](https://www.ncei.noaa.gov/products/microplastics) | Microplastics samples |
| [Marine Regions EEZ boundaries](https://www.marineregions.org/eez.php) | Exclusive Economic Zones for the map |
| [World Bank indicators](https://data.worldbank.org/indicator/ER.MRN.PTMR.ZS) and [UN SDG 14.5.1](https://unstats.un.org/sdgs/dataportal) | Marine protection per country |
| [World Bank projects](https://projects.worldbank.org) and [IATI](https://iatistandard.org) | Ocean finance and aid per country |

## New candidates (13 November 2026): ocean carbon, blue carbon and verification

Added to the QEM's registry as candidates (readers to build). They serve two things: stronger verification for the Bermuda Standard, and the evidence base for the [Open Blue Carbon Registry](https://github.com/hub-culture/Commons/blob/main/docs/blue-carbon-registry.md).

| Resource | What it adds | Licence |
| --- | --- | --- |
| [Global Mangrove Watch v4.1](https://www.globalmangrovewatch.org) | Mangrove extent and change, 30 m, every year 1985-2025: the baseline for blue carbon area claims | CC BY 4.0 |
| [Coastal Carbon Network Data Library](https://serc.si.edu/coastalcarbon) ([GitHub](https://github.com/smithsonian/ccn-data-library)) | ≈15,000 open soil cores from marshes, mangroves and seagrass: the check on soil carbon stocks | Per dataset, mostly CC BY 4.0 |
| [SOCAT v2026](https://socat.info) | 50M+ quality-controlled surface-ocean CO₂ observations: ocean carbon uptake and acidification | CC BY 4.0 |
| [BIOS BATS and Hydrostation S](https://www.bios.asu.edu/research/projects/bats) | Bermuda's monthly ocean-carbon and hydrography record since 1954/1988 | Open, with citation |
| [AGAGE](https://agage.mit.edu) | Independent in-situ methane, including Ragged Point (Barbados) and Mace Head (Ireland) | Open, AGAGE data policy |
| [Carbon Mapper](https://data.carbonmapper.org) | Facility-scale methane and CO₂ plumes from satellite | Non-commercial |

## Marine protected areas and the high seas (BBNJ)

To cross-collate MPA and BBNJ data, as the Initiative's MPA strategy work needs:

| Resource | What it adds |
| --- | --- |
| [Protected Planet (WDPA)](https://www.protectedplanet.net) | The world database of protected areas, UNEP-WCMC and IUCN. Already reaches the export through the World Bank's MPA indicator; boundaries are the next step. Check its terms for commercial use |
| [MPAtlas](https://mpatlas.org) | MPAs classified by stage and level of protection, using the MPA Guide |
| [The MPA Guide](https://doi.org/10.1126/science.abf0861) | The framework for describing how protected an MPA really is (a practice in [Commons](https://github.com/hub-culture/Commons/tree/main/data/practices)) |
| [Marine Regions](https://www.marineregions.org) | Maritime boundaries, including the high seas beyond national jurisdiction, where the BBNJ Agreement applies |

## Standards and tools

| Resource | Why it's here |
| --- | --- |
| [Verra VM0033](https://verra.org/methodologies/vm0033-methodology-for-tidal-wetland-and-seagrass-restoration-v2-1/) | The leading methodology for tidal wetland and seagrass restoration (v2.1; v3.0 consulted on in 2026) |
| [Hedera Guardian](https://guardian.hedera.com) | Open-source platform where VM0033 runs as a digital policy; the QEM is linked to it |
| [ERDDAP](https://erddap.github.io) | The data server most of the live sources use |
| [H3](https://h3geo.org) | The hexagonal grid the layers are tagged with, as Gaia uses |

Know a resource that should be here? Open an issue with its link, licence and what it would add.
