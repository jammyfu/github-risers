# Maintaining the five-language introduction

The ranking READMEs were already available in five languages. This website now offers the same five entry languages without duplicating ranking snapshots.

| Entry | Language | Ranking destination |
| --- | --- | --- |
| `/` | English | `README.md` |
| `/zh-Hans/` | 简体中文 | `README.zh-Hans.md` |
| `/zh-Hant/` | 繁體中文（台灣用語） | `README.zh-Hant.md` |
| `/ja/` | 日本語 | `README.ja.md` |
| `/ko/` | 한국어 | `README.ko.md` |

Edit `tools/site_locales.json`, then run:

```bash
python3 tools/render_site.py
python3 tools/render_site.py --check
python3 tools/verify.py
```

The generator shares layout, language links, canonical URLs, sitemap and FAQ schema. Every FAQ schema answer comes from the same localized text shown on screen. Root `llms.txt` is copied to the published site; edit the root file only.

## Presentation and evidence

- Reuse `.github/social-preview.png` as project identity, not a fake screenshot of the current rankings.
- Keep the primary action pointed at the current language's live README; numeric data and ranking logic remain in the existing pipeline.
- The facts table remains a table; flexible navigation, wrapping text and a fluid title image support narrow screens without removing content.
- No client-side executable scripts or telemetry are added. JSON-LD is inert structured data.
- Discovery improvements are clearer localized titles, descriptions, links and exact answer text, not keyword stuffing or a ranking guarantee. `llms.txt` cannot guarantee AI citations.
- Supporting methodology documents linked from these pages may still be English or Simplified Chinese; this change does not claim that every repository document has five translations.
- Translations are AI-reviewed and remain open to corrections from native speakers.
