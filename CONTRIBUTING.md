# Contributing

Thank you for helping open up ocean data.

## Ways to help

- **Suggest a data source.** Open an issue with its link, licence, how it's reached (open API, token, portal) and what it would add: a new place, an independent check on a reading, or context (protection, finance, biodiversity, carbon).
- **Report a problem in the data.** Name the file, the place or feature, and the time. If a reading looks wrong, say what you compared it with.
- **Build.** Readers for the candidate sources in `data/sources.json` (`live: false`), map tools on the GeoJSON layers, notebooks that use the export.

## Ground rules

- `data/processed/qem/` is published automatically every Monday; don't edit it by hand. Fixes to the data go into the QEM, which produces it.
- Keep every source's licence with its data, and credit sources.
- No personal data: names of people are dropped from every source.
- Run `python3 scripts/validate.py` before opening a pull request.

## Code of conduct

Be kind, be precise, assume good faith. Disagree about the data, not the person.
