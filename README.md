**English** | [简体中文](README.zh-Hans.md) | [繁體中文](README.zh-Hant.md) | [日本語](README.ja.md) | [한국어](README.ko.md)

# GitHub Risers: Ranked by Stars Gained per Day

<img src=".github/social-preview.png" alt="GitHub Risers: Ranked by Stars Gained per Day" width="640">

[![MIT](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE) [![CI](https://github.com/jammyfu/github-risers/actions/workflows/ci.yml/badge.svg)](https://github.com/jammyfu/github-risers/actions/workflows/ci.yml) [![updated](https://img.shields.io/badge/dynamic/json?url=https%3A%2F%2Fraw.githubusercontent.com%2Fjammyfu%2Fgithub-risers%2Fmain%2Fdata%2Fstats.json&query=%24.today_utc&label=updated&color=brightgreen)](latest/rankings.md)

Trending GitHub repos ranked by star growth (stars gained per day), not total stars: AI first, then developer tools, security, web, infrastructure, design and data.

Data from 2026-11-14 13:50 UTC. Updated daily.

**Live boards:** [Website](https://jammyfu.github.io/github-risers/) · [Latest snapshot](latest/rankings.md)

## Use it now

1. Open the [live boards](https://jammyfu.github.io/github-risers/) — no install.
2. Or read this round's category leaders below, then the boards.
3. Each board here shows the top 10; the full top 20 is in [latest/rankings.md](latest/rankings.md).

[Website](https://jammyfu.github.io/github-risers/) · [How it works](docs/HOW_IT_WORKS.md) · [Facts](docs/FACTS.md) · [History](rankings/README.md) · [Latest](latest/rankings.md)

## Category leaders this round

| Category | #1 new (7 days) | #1 this week | #1 this month | #1 this year | #1 total stars |
|---|---|---|---|---|---|
| **[AI](#ai)** ★ primary | [FrigadeHQ/yogurt](https://github.com/FrigadeHQ/yogurt)<br>366/day | [morluto/rea](https://github.com/morluto/rea)<br>2,870/day | [morluto/rea](https://github.com/morluto/rea)<br>6,977/day | [deepseek-ai/deepseek-harness](https://github.com/deepseek-ai/deepseek-harness)<br>3,018/day | [morluto/rea](https://github.com/morluto/rea)<br>458,892 ★ |
| **[Developer Tools](#developer-tools)** | [alexeyw/lot-map](https://github.com/alexeyw/lot-map)<br>163/day | [zed-industries/zed](https://github.com/zed-industries/zed)<br>183/day | [zed-industries/zed](https://github.com/zed-industries/zed)<br>118/day | [zed-industries/zed](https://github.com/zed-industries/zed)<br>75.0/day | [oven-sh/bun](https://github.com/oven-sh/bun)<br>96,693 ★ |
| **[Security](#security)** | n/a | [projectdiscovery/nuclei](https://github.com/projectdiscovery/nuclei)<br>36.7/day | [aquasecurity/trivy](https://github.com/aquasecurity/trivy)<br>31.8/day | [aquasecurity/trivy](https://github.com/aquasecurity/trivy)<br>28.4/day | [aquasecurity/trivy](https://github.com/aquasecurity/trivy)<br>39,337 ★ |
| **[Web / Frontend](#web--frontend)** | [opencoredev/islandcn](https://github.com/opencoredev/islandcn)<br>542/day | [shadcn-ui/ui](https://github.com/shadcn-ui/ui)<br>96.6/day | [shadcn-ui/ui](https://github.com/shadcn-ui/ui)<br>93.2/day | [shadcn-ui/ui](https://github.com/shadcn-ui/ui)<br>83.6/day | [facebook/react](https://github.com/facebook/react)<br>252,602 ★ |
| **[Infrastructure](#infrastructure)** | [HolyArrs/HolyArrs](https://github.com/HolyArrs/HolyArrs)<br>249/day | [prometheus/prometheus](https://github.com/prometheus/prometheus)<br>64.1/day | [caddyserver/caddy](https://github.com/caddyserver/caddy)<br>39.8/day | [caddyserver/caddy](https://github.com/caddyserver/caddy)<br>33.1/day | [kubernetes/kubernetes](https://github.com/kubernetes/kubernetes)<br>129,056 ★ |
| **[Design / Creative](#design--creative)** | [lobehub/lobe-mygo](https://github.com/lobehub/lobe-mygo)<br>40.4/day | [excalidraw/excalidraw](https://github.com/excalidraw/excalidraw)<br>64.4/day | [excalidraw/excalidraw](https://github.com/excalidraw/excalidraw)<br>66.2/day | [excalidraw/excalidraw](https://github.com/excalidraw/excalidraw)<br>73.8/day | [excalidraw/excalidraw](https://github.com/excalidraw/excalidraw)<br>135,672 ★ |
| **[Data](#data)** | n/a | [duckdb/duckdb](https://github.com/duckdb/duckdb)<br>28.1/day | [duckdb/duckdb](https://github.com/duckdb/duckdb)<br>32.0/day | [duckdb/duckdb](https://github.com/duckdb/duckdb)<br>25.9/day | [apache/superset](https://github.com/apache/superset)<br>75,523 ★ |

Each board shows the top 10 here. The full top-20 lists are in [latest/rankings.md](latest/rankings.md).

Each row is one line on purpose. The full description of every project, with tool names and technical details, is in [docs/DETAILS.md](docs/DETAILS.md).

## Quick answers

### What is GitHub Risers?

A leaderboard of GitHub repos ranked by stars gained per day, not total stars. AI is the main board; six more categories follow. Built by script from the GitHub API. [Read more](docs/FAQ.md#what-is-github-risers)

### How is it different from GitHub Trending?

GitHub Trending is GitHub's own page. GitHub Risers is an independent open-source project with published rules, five languages and a saved history of every update. It is not affiliated with GitHub. [Read more](docs/FAQ.md#is-it-the-same-as-github-trending)

### How often is it updated?

Updated daily. Every run is archived. [Read more](docs/FAQ.md#how-often-is-it-updated)

### How is the data computed?

Stars gained in the last 7, 30 or 365 complete UTC days, divided by those days. All numbers come from the GitHub API; nothing is typed or estimated. [Read more](docs/FAQ.md#how-is-the-growth-rate-computed)

### How do I use or contribute?

Read the boards below, or the full top 20 in latest/. To add a tracked project, edit data/projects.json (five languages) and open a pull request. [Read more](docs/FAQ.md#how-can-i-suggest-a-project-or-report-a-mistake)

## AI

> LLMs, agents, MCP, coding copilots and generative AI

### Hottest new repos (created in the last 7 days)

| # | Project | Created (UTC) | Total stars | Stars/day |
|---|---|---|---:|---:|
| 1 | [FrigadeHQ/yogurt](https://github.com/FrigadeHQ/yogurt)<br>Keep your AI meeting notes private on your own computer | 2026-11-10<br><sub>3.7 d</sub> | 1,368 | 365.5 |
| 2 | [AdmiralEmporium/ai--manus](https://github.com/AdmiralEmporium/ai--manus)<br>Run various agent tools and operations in a sandbox | 2026-11-13<br><sub>1.0 d</sub> | 266 | 266.0 |
| 3 | [ApothecaryDesign/ai--manus](https://github.com/ApothecaryDesign/ai--manus)<br>Run various agent tools and operations in a sandbox | 2026-11-13<br><sub>1.0 d</sub> | 266 | 266.0 |
| 4 | [ArcherAmplify/ai--manus](https://github.com/ArcherAmplify/ai--manus)<br>Run various agent tools and operations in a sandbox | 2026-11-13<br><sub>1.0 d</sub> | 266 | 266.0 |
| 5 | [Archiveeutrough/ai--manus](https://github.com/Archiveeutrough/ai--manus)<br>Run various agent tools and operations in a sandbox | 2026-11-13<br><sub>1.0 d</sub> | 266 | 266.0 |
| 6 | [ArcticPrawnEmporium/ai--manus](https://github.com/ArcticPrawnEmporium/ai--manus)<br>Run various agent tools and operations in a sandbox | 2026-11-13<br><sub>1.0 d</sub> | 266 | 266.0 |
| 7 | [armsworminterface/ai--manus](https://github.com/armsworminterface/ai--manus)<br>Run various agent tools and operations in a sandbox | 2026-11-13<br><sub>1.0 d</sub> | 266 | 266.0 |
| 8 | [armysystemsun/ai--manus](https://github.com/armysystemsun/ai--manus)<br>Run various agent tools and operations in a sandbox | 2026-11-13<br><sub>1.0 d</sub> | 266 | 266.0 |
| 9 | [Aspectnisafeguard/ai--manus](https://github.com/Aspectnisafeguard/ai--manus)<br>Need AI to run tools? Let an agent work in a sandbox | 2026-11-13<br><sub>1.0 d</sub> | 266 | 266.0 |
| 10 | [BarrierCenter/ai--manus](https://github.com/BarrierCenter/ai--manus)<br>Need AI to run tools? Let an agent work in a sandbox | 2026-11-13<br><sub>1.0 d</sub> | 266 | 266.0 |

<details>
<summary>Star history charts for this board</summary>

<a href="https://www.star-history.com/#FrigadeHQ/yogurt&Date"><img src="https://api.star-history.com/svg?repos=FrigadeHQ/yogurt&type=Date" width="260" alt="star history FrigadeHQ/yogurt"></a>

<a href="https://www.star-history.com/#AdmiralEmporium/ai--manus&Date"><img src="https://api.star-history.com/svg?repos=AdmiralEmporium/ai--manus&type=Date" width="260" alt="star history AdmiralEmporium/ai--manus"></a>

<a href="https://www.star-history.com/#ApothecaryDesign/ai--manus&Date"><img src="https://api.star-history.com/svg?repos=ApothecaryDesign/ai--manus&type=Date" width="260" alt="star history ApothecaryDesign/ai--manus"></a>

<a href="https://www.star-history.com/#ArcherAmplify/ai--manus&Date"><img src="https://api.star-history.com/svg?repos=ArcherAmplify/ai--manus&type=Date" width="260" alt="star history ArcherAmplify/ai--manus"></a>

<a href="https://www.star-history.com/#Archiveeutrough/ai--manus&Date"><img src="https://api.star-history.com/svg?repos=Archiveeutrough/ai--manus&type=Date" width="260" alt="star history Archiveeutrough/ai--manus"></a>

<a href="https://www.star-history.com/#ArcticPrawnEmporium/ai--manus&Date"><img src="https://api.star-history.com/svg?repos=ArcticPrawnEmporium/ai--manus&type=Date" width="260" alt="star history ArcticPrawnEmporium/ai--manus"></a>

<a href="https://www.star-history.com/#armsworminterface/ai--manus&Date"><img src="https://api.star-history.com/svg?repos=armsworminterface/ai--manus&type=Date" width="260" alt="star history armsworminterface/ai--manus"></a>

<a href="https://www.star-history.com/#armysystemsun/ai--manus&Date"><img src="https://api.star-history.com/svg?repos=armysystemsun/ai--manus&type=Date" width="260" alt="star history armysystemsun/ai--manus"></a>

<a href="https://www.star-history.com/#Aspectnisafeguard/ai--manus&Date"><img src="https://api.star-history.com/svg?repos=Aspectnisafeguard/ai--manus&type=Date" width="260" alt="star history Aspectnisafeguard/ai--manus"></a>

<a href="https://www.star-history.com/#BarrierCenter/ai--manus&Date"><img src="https://api.star-history.com/svg?repos=BarrierCenter/ai--manus&type=Date" width="260" alt="star history BarrierCenter/ai--manus"></a>

</details>

### Fastest rising this week (last 7 days)

| # | Project | Stars gained | Stars/day | Total stars |
|---|---|---:|---:|---:|
| 1 | [morluto/rea](https://github.com/morluto/rea)<br>Let AI clone any software for you<br>`AI` | +20,088 | 2,869.7 | 458,892 |
| 2 | [cloudflare/security-audit-skill](https://github.com/cloudflare/security-audit-skill)<br>One AI hunts security holes, a fresh AI verifies each<br>`AI` | +7,696 | 1,099.4 | 72,290 |
| 3 | [stablyai/orca](https://github.com/stablyai/orca)<br>Several AIs write at once, see which one works best<br>`AI` | +6,731 | 961.6 | 124,716 |
| 4 | [anthropics/skills](https://github.com/anthropics/skills)<br>Learn to write Claude skills from the official examples<br>`AI` | +6,162 | 880.3 | 194,398 |
| 5 | [deepseek-ai/deepseek-harness](https://github.com/deepseek-ai/deepseek-harness)<br>Pick plugins and build the agent you want<br>`AI` | +5,941 | 848.7 | 280,918 |
| 6 | [yetone/magpie](https://github.com/yetone/magpie)<br>Swap models in your coding AI; quota runs out, it carries on<br>`AI` | +4,960 | 708.6 | 36,411 |
| 7 | [DietrichGebert/ponytail](https://github.com/DietrichGebert/ponytail)<br>Less filler code from AI, the needed code done right<br>`AI` | +4,715 | 673.6 | 190,646 |
| 8 | [affaan-m/ECC](https://github.com/affaan-m/ECC)<br>Give your coding AI memory, skills and safety checks<br>`AI` | +4,119 | 588.4 | 302,675 |
| 9 | [Leonxlnx/taste-skill](https://github.com/Leonxlnx/taste-skill)<br>Stop AI from making every page look the same<br>`AI` | +4,000 | 571.4 | 115,365 |
| 10 | [heygen-com/hyperframes](https://github.com/heygen-com/hyperframes)<br>Can't edit video? Write it like a web page<br>`AI` | +3,941 | 563.0 | 84,175 |

<details>
<summary>Star history charts for this board</summary>

<a href="https://www.star-history.com/#morluto/rea&Date"><img src="https://api.star-history.com/svg?repos=morluto/rea&type=Date" width="260" alt="star history morluto/rea"></a>

<a href="https://www.star-history.com/#cloudflare/security-audit-skill&Date"><img src="https://api.star-history.com/svg?repos=cloudflare/security-audit-skill&type=Date" width="260" alt="star history cloudflare/security-audit-skill"></a>

<a href="https://www.star-history.com/#stablyai/orca&Date"><img src="https://api.star-history.com/svg?repos=stablyai/orca&type=Date" width="260" alt="star history stablyai/orca"></a>

<a href="https://www.star-history.com/#anthropics/skills&Date"><img src="https://api.star-history.com/svg?repos=anthropics/skills&type=Date" width="260" alt="star history anthropics/skills"></a>

<a href="https://www.star-history.com/#deepseek-ai/deepseek-harness&Date"><img src="https://api.star-history.com/svg?repos=deepseek-ai/deepseek-harness&type=Date" width="260" alt="star history deepseek-ai/deepseek-harness"></a>

<a href="https://www.star-history.com/#yetone/magpie&Date"><img src="https://api.star-history.com/svg?repos=yetone/magpie&type=Date" width="260" alt="star history yetone/magpie"></a>

<a href="https://www.star-history.com/#DietrichGebert/ponytail&Date"><img src="https://api.star-history.com/svg?repos=DietrichGebert/ponytail&type=Date" width="260" alt="star history DietrichGebert/ponytail"></a>

<a href="https://www.star-history.com/#affaan-m/ECC&Date"><img src="https://api.star-history.com/svg?repos=affaan-m/ECC&type=Date" width="260" alt="star history affaan-m/ECC"></a>

<a href="https://www.star-history.com/#Leonxlnx/taste-skill&Date"><img src="https://api.star-history.com/svg?repos=Leonxlnx/taste-skill&type=Date" width="260" alt="star history Leonxlnx/taste-skill"></a>

<a href="https://www.star-history.com/#heygen-com/hyperframes&Date"><img src="https://api.star-history.com/svg?repos=heygen-com/hyperframes&type=Date" width="260" alt="star history heygen-com/hyperframes"></a>

</details>

### Fastest rising this month (last 30 days)

| # | Project | Stars gained | Stars/day | Total stars |
|---|---|---:|---:|---:|
| 1 | [morluto/rea](https://github.com/morluto/rea)<br>Let AI clone any software for you<br>`AI` | +209,304 | 6,976.8 | 458,892 |
| 2 | [cloudflare/security-audit-skill](https://github.com/cloudflare/security-audit-skill)<br>One AI hunts security holes, a fresh AI verifies each<br>`AI` | +42,686 | 1,422.9 | 72,290 |
| 3 | [stablyai/orca](https://github.com/stablyai/orca)<br>Several AIs write at once, see which one works best<br>`AI` | +32,487 | 1,082.9 | 124,716 |
| 4 | [deepseek-ai/deepseek-harness](https://github.com/deepseek-ai/deepseek-harness)<br>Pick plugins and build the agent you want<br>`AI` | +32,052 | 1,068.4 | 280,918 |
| 5 | [DietrichGebert/ponytail](https://github.com/DietrichGebert/ponytail)<br>Less filler code from AI, the needed code done right<br>`AI` | +27,560 | 918.7 | 190,646 |
| 6 | [affaan-m/ECC](https://github.com/affaan-m/ECC)<br>Give your coding AI memory, skills and safety checks<br>`AI` | +24,207 | 806.9 | 302,675 |
| 7 | [yetone/magpie](https://github.com/yetone/magpie)<br>Swap models in your coding AI; quota runs out, it carries on<br>`AI` | +23,503 | 783.4 | 36,411 |
| 8 | [Graphify-Labs/graphify](https://github.com/Graphify-Labs/graphify)<br>Too big to read? Start with this map of the code<br>`AI` | +21,351 | 711.7 | 147,514 |
| 9 | [heygen-com/hyperframes](https://github.com/heygen-com/hyperframes)<br>Can't edit video? Write it like a web page<br>`AI` | +20,496 | 683.2 | 84,175 |
| 10 | [Leonxlnx/taste-skill](https://github.com/Leonxlnx/taste-skill)<br>Stop AI from making every page look the same<br>`AI` | +18,975 | 632.5 | 115,365 |

<details>
<summary>Star history charts for this board</summary>

<a href="https://www.star-history.com/#morluto/rea&Date"><img src="https://api.star-history.com/svg?repos=morluto/rea&type=Date" width="260" alt="star history morluto/rea"></a>

<a href="https://www.star-history.com/#cloudflare/security-audit-skill&Date"><img src="https://api.star-history.com/svg?repos=cloudflare/security-audit-skill&type=Date" width="260" alt="star history cloudflare/security-audit-skill"></a>

<a href="https://www.star-history.com/#stablyai/orca&Date"><img src="https://api.star-history.com/svg?repos=stablyai/orca&type=Date" width="260" alt="star history stablyai/orca"></a>

<a href="https://www.star-history.com/#deepseek-ai/deepseek-harness&Date"><img src="https://api.star-history.com/svg?repos=deepseek-ai/deepseek-harness&type=Date" width="260" alt="star history deepseek-ai/deepseek-harness"></a>

<a href="https://www.star-history.com/#DietrichGebert/ponytail&Date"><img src="https://api.star-history.com/svg?repos=DietrichGebert/ponytail&type=Date" width="260" alt="star history DietrichGebert/ponytail"></a>

<a href="https://www.star-history.com/#affaan-m/ECC&Date"><img src="https://api.star-history.com/svg?repos=affaan-m/ECC&type=Date" width="260" alt="star history affaan-m/ECC"></a>

<a href="https://www.star-history.com/#yetone/magpie&Date"><img src="https://api.star-history.com/svg?repos=yetone/magpie&type=Date" width="260" alt="star history yetone/magpie"></a>

<a href="https://www.star-history.com/#Graphify-Labs/graphify&Date"><img src="https://api.star-history.com/svg?repos=Graphify-Labs/graphify&type=Date" width="260" alt="star history Graphify-Labs/graphify"></a>

<a href="https://www.star-history.com/#heygen-com/hyperframes&Date"><img src="https://api.star-history.com/svg?repos=heygen-com/hyperframes&type=Date" width="260" alt="star history heygen-com/hyperframes"></a>

<a href="https://www.star-history.com/#Leonxlnx/taste-skill&Date"><img src="https://api.star-history.com/svg?repos=Leonxlnx/taste-skill&type=Date" width="260" alt="star history Leonxlnx/taste-skill"></a>

</details>

### Fastest rising this year (last 365 days)

| # | Project | Stars gained | Stars/day | Total stars |
|---|---|---:|---:|---:|
| 1 | [deepseek-ai/deepseek-harness](https://github.com/deepseek-ai/deepseek-harness)<br>Pick plugins and build the agent you want<br>`AI` | +280,719 | 3,018.5 †<br><sub>÷93d</sub> | 280,918 |
| 2 | [morluto/rea](https://github.com/morluto/rea)<br>Let AI clone any software for you<br>`AI` | +458,250 | 2,141.4 †<br><sub>÷214d</sub> | 458,892 |
| 3 | [DietrichGebert/ponytail](https://github.com/DietrichGebert/ponytail)<br>Less filler code from AI, the needed code done right<br>`AI` | +190,493 | 1,229.0 †<br><sub>÷155d</sub> | 190,646 |
| 4 | [openclaw/openclaw](https://github.com/openclaw/openclaw)<br>An AI assistant that gets things done, on your own devices<br>`AI` | +394,402 | 1,111.0 †<br><sub>÷355d</sub> | 394,433 |
| 5 | [affaan-m/ECC](https://github.com/affaan-m/ECC)<br>Give your coding AI memory, skills and safety checks<br>`AI` | +302,558 | 1,008.5 †<br><sub>÷300d</sub> | 302,675 |
| 6 | [NousResearch/hermes-agent](https://github.com/NousResearch/hermes-agent)<br>An AI helper that gets better the more you use it<br>`AI` | +263,247 | 721.2 | 263,296 |
| 7 | [yetone/magpie](https://github.com/yetone/magpie)<br>Swap models in your coding AI; quota runs out, it carries on<br>`AI` | +36,273 | 697.6 †<br><sub>÷52d</sub> | 36,411 |
| 8 | [Graphify-Labs/graphify](https://github.com/Graphify-Labs/graphify)<br>Too big to read? Start with this map of the code<br>`AI` | +147,400 | 655.1 †<br><sub>÷225d</sub> | 147,514 |
| 9 | [anomalyco/opencode](https://github.com/anomalyco/opencode)<br>An open-source AI that writes code in your terminal<br>`AI` | +195,380 | 535.3 | 226,785 |
| 10 | [stablyai/orca](https://github.com/stablyai/orca)<br>Several AIs write at once, see which one works best<br>`AI` | +124,530 | 514.6 †<br><sub>÷242d</sub> | 124,716 |

<details>
<summary>Star history charts for this board</summary>

<a href="https://www.star-history.com/#deepseek-ai/deepseek-harness&Date"><img src="https://api.star-history.com/svg?repos=deepseek-ai/deepseek-harness&type=Date" width="260" alt="star history deepseek-ai/deepseek-harness"></a>

<a href="https://www.star-history.com/#morluto/rea&Date"><img src="https://api.star-history.com/svg?repos=morluto/rea&type=Date" width="260" alt="star history morluto/rea"></a>

<a href="https://www.star-history.com/#DietrichGebert/ponytail&Date"><img src="https://api.star-history.com/svg?repos=DietrichGebert/ponytail&type=Date" width="260" alt="star history DietrichGebert/ponytail"></a>

<a href="https://www.star-history.com/#openclaw/openclaw&Date"><img src="https://api.star-history.com/svg?repos=openclaw/openclaw&type=Date" width="260" alt="star history openclaw/openclaw"></a>

<a href="https://www.star-history.com/#affaan-m/ECC&Date"><img src="https://api.star-history.com/svg?repos=affaan-m/ECC&type=Date" width="260" alt="star history affaan-m/ECC"></a>

<a href="https://www.star-history.com/#NousResearch/hermes-agent&Date"><img src="https://api.star-history.com/svg?repos=NousResearch/hermes-agent&type=Date" width="260" alt="star history NousResearch/hermes-agent"></a>

<a href="https://www.star-history.com/#yetone/magpie&Date"><img src="https://api.star-history.com/svg?repos=yetone/magpie&type=Date" width="260" alt="star history yetone/magpie"></a>

<a href="https://www.star-history.com/#Graphify-Labs/graphify&Date"><img src="https://api.star-history.com/svg?repos=Graphify-Labs/graphify&type=Date" width="260" alt="star history Graphify-Labs/graphify"></a>

<a href="https://www.star-history.com/#anomalyco/opencode&Date"><img src="https://api.star-history.com/svg?repos=anomalyco/opencode&type=Date" width="260" alt="star history anomalyco/opencode"></a>

<a href="https://www.star-history.com/#stablyai/orca&Date"><img src="https://api.star-history.com/svg?repos=stablyai/orca&type=Date" width="260" alt="star history stablyai/orca"></a>

</details>

† The repo is younger than the window, so stars/day is divided by the repo age in days (shown under the figure) instead of the full window.

### Total stars (all time)

| # | Project | Total stars |
|---|---|---:|
| 1 | [morluto/rea](https://github.com/morluto/rea)<br>Let AI clone any software for you<br>`AI` | 458,892 |
| 2 | [openclaw/openclaw](https://github.com/openclaw/openclaw)<br>An AI assistant that gets things done, on your own devices<br>`AI` | 394,433 |
| 3 | [affaan-m/ECC](https://github.com/affaan-m/ECC)<br>Give your coding AI memory, skills and safety checks<br>`AI` | 302,675 |
| 4 | [deepseek-ai/deepseek-harness](https://github.com/deepseek-ai/deepseek-harness)<br>Pick plugins and build the agent you want<br>`AI` | 280,918 |
| 5 | [NousResearch/hermes-agent](https://github.com/NousResearch/hermes-agent)<br>An AI helper that gets better the more you use it<br>`AI` | 263,296 |
| 6 | [anomalyco/opencode](https://github.com/anomalyco/opencode)<br>An open-source AI that writes code in your terminal<br>`AI` | 226,785 |
| 7 | [anthropics/skills](https://github.com/anthropics/skills)<br>Learn to write Claude skills from the official examples<br>`AI` | 194,398 |
| 8 | [DietrichGebert/ponytail](https://github.com/DietrichGebert/ponytail)<br>Less filler code from AI, the needed code done right<br>`AI` | 190,646 |
| 9 | [farion1231/cc-switch](https://github.com/farion1231/cc-switch)<br>Switch providers in one click, no config editing<br>`AI` | 154,380 |
| 10 | [nextlevelbuilder/ui-ux-pro-max-skill](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill)<br>UIs built by AI that look professionally designed<br>`AI` | 149,327 |

<details>
<summary>Star history charts for this board</summary>

<a href="https://www.star-history.com/#morluto/rea&Date"><img src="https://api.star-history.com/svg?repos=morluto/rea&type=Date" width="260" alt="star history morluto/rea"></a>

<a href="https://www.star-history.com/#openclaw/openclaw&Date"><img src="https://api.star-history.com/svg?repos=openclaw/openclaw&type=Date" width="260" alt="star history openclaw/openclaw"></a>

<a href="https://www.star-history.com/#affaan-m/ECC&Date"><img src="https://api.star-history.com/svg?repos=affaan-m/ECC&type=Date" width="260" alt="star history affaan-m/ECC"></a>

<a href="https://www.star-history.com/#deepseek-ai/deepseek-harness&Date"><img src="https://api.star-history.com/svg?repos=deepseek-ai/deepseek-harness&type=Date" width="260" alt="star history deepseek-ai/deepseek-harness"></a>

<a href="https://www.star-history.com/#NousResearch/hermes-agent&Date"><img src="https://api.star-history.com/svg?repos=NousResearch/hermes-agent&type=Date" width="260" alt="star history NousResearch/hermes-agent"></a>

<a href="https://www.star-history.com/#anomalyco/opencode&Date"><img src="https://api.star-history.com/svg?repos=anomalyco/opencode&type=Date" width="260" alt="star history anomalyco/opencode"></a>

<a href="https://www.star-history.com/#anthropics/skills&Date"><img src="https://api.star-history.com/svg?repos=anthropics/skills&type=Date" width="260" alt="star history anthropics/skills"></a>

<a href="https://www.star-history.com/#DietrichGebert/ponytail&Date"><img src="https://api.star-history.com/svg?repos=DietrichGebert/ponytail&type=Date" width="260" alt="star history DietrichGebert/ponytail"></a>

<a href="https://www.star-history.com/#farion1231/cc-switch&Date"><img src="https://api.star-history.com/svg?repos=farion1231/cc-switch&type=Date" width="260" alt="star history farion1231/cc-switch"></a>

<a href="https://www.star-history.com/#nextlevelbuilder/ui-ux-pro-max-skill&Date"><img src="https://api.star-history.com/svg?repos=nextlevelbuilder/ui-ux-pro-max-skill&type=Date" width="260" alt="star history nextlevelbuilder/ui-ux-pro-max-skill"></a>

</details>

## Developer Tools

> CLIs, editors, package managers, linters and build tooling

### Hottest new repos (created in the last 7 days)

| # | Project | Created (UTC) | Total stars | Stars/day |
|---|---|---|---:|---:|
| 1 | [alexeyw/lot-map](https://github.com/alexeyw/lot-map)<br>See what Claude Code is doing in real time beside your chat | 2026-11-09<br><sub>4.8 d</sub> | 780 | 163.3 |
| 2 | [RouteInferno/shamus-osint-ai-agent](https://github.com/RouteInferno/shamus-osint-ai-agent)<br>Command-line AI agent for OSINT: one command, it picks the tools, runs them and writes the case file. | 2026-11-13<br><sub>1.0 d</sub> | 157 | 157.0 |
| 3 | [brunnojob/cifuse](https://github.com/brunnojob/cifuse)<br>Turn noisy CI logs into grouped failures, exact evidence and investigation steps. Offline CLI, reusable GitHub Action and bilingual browser workbench. No API k… | 2026-11-07<br><sub>6.8 d</sub> | 111 | 16.4 |
| 4 | [azuresail195/wondershare-recoverit-desktop](https://github.com/azuresail195/wondershare-recoverit-desktop)<br>Wondershare Recoverit 2026 desktop setup for recovering deleted files from disks, SD cards and USB drives, repairing corrupted video and photo files, and crash… | 2026-11-13<br><sub>1.0 d</sub> | 285 | 285.0 |
| 5 | [ben-miller-23/dxo-photolab-10-desktop](https://github.com/ben-miller-23/dxo-photolab-10-desktop)<br>DxO PhotoLab 10 2026 desktop setup with DeepPRIME XD denoising for clean high-ISO shots, optical corrections from measured lens profiles, and non-destructive R… | 2026-11-13<br><sub>1.0 d</sub> | 285 | 285.0 |
| 6 | [ariamitchell54/cubase-studio-desktop](https://github.com/ariamitchell54/cubase-studio-desktop)<br>Cubase Studio 2026 desktop setup with plugin suite | 2026-11-13<br><sub>1.0 d</sub> | 284 | 284.0 |
| 7 | [azure-teal-slope/windows-optimizer-desktop](https://github.com/azure-teal-slope/windows-optimizer-desktop)<br>Windows Optimizer 2026 desktop setup and file cleaner | 2026-11-13<br><sub>1.0 d</sub> | 284 | 284.0 |
| 8 | [azuremaple1997/coreldraw-desktop](https://github.com/azuremaple1997/coreldraw-desktop)<br>CorelDraw Desktop 2026 setup with color grading and HDR | 2026-11-13<br><sub>1.0 d</sub> | 284 | 284.0 |
| 9 | [ben-cook-42/kontakt-8-desktop](https://github.com/ben-cook-42/kontakt-8-desktop)<br>Kontakt 8 2026 desktop setup with instrument sampler | 2026-11-13<br><sub>1.0 d</sub> | 283 | 283.0 |
| 10 | [briskember13/adobe-acrobat-pdf-desktop](https://github.com/briskember13/adobe-acrobat-pdf-desktop)<br>Adobe Acrobat PDF 2026 desktop setup for PDF editing | 2026-11-14<br><sub>1.0 d</sub> | 283 | 283.0 |

<details>
<summary>Star history charts for this board</summary>

<a href="https://www.star-history.com/#alexeyw/lot-map&Date"><img src="https://api.star-history.com/svg?repos=alexeyw/lot-map&type=Date" width="260" alt="star history alexeyw/lot-map"></a>

<a href="https://www.star-history.com/#RouteInferno/shamus-osint-ai-agent&Date"><img src="https://api.star-history.com/svg?repos=RouteInferno/shamus-osint-ai-agent&type=Date" width="260" alt="star history RouteInferno/shamus-osint-ai-agent"></a>

<a href="https://www.star-history.com/#brunnojob/cifuse&Date"><img src="https://api.star-history.com/svg?repos=brunnojob/cifuse&type=Date" width="260" alt="star history brunnojob/cifuse"></a>

<a href="https://www.star-history.com/#azuresail195/wondershare-recoverit-desktop&Date"><img src="https://api.star-history.com/svg?repos=azuresail195/wondershare-recoverit-desktop&type=Date" width="260" alt="star history azuresail195/wondershare-recoverit-desktop"></a>

<a href="https://www.star-history.com/#ben-miller-23/dxo-photolab-10-desktop&Date"><img src="https://api.star-history.com/svg?repos=ben-miller-23/dxo-photolab-10-desktop&type=Date" width="260" alt="star history ben-miller-23/dxo-photolab-10-desktop"></a>

<a href="https://www.star-history.com/#ariamitchell54/cubase-studio-desktop&Date"><img src="https://api.star-history.com/svg?repos=ariamitchell54/cubase-studio-desktop&type=Date" width="260" alt="star history ariamitchell54/cubase-studio-desktop"></a>

<a href="https://www.star-history.com/#azure-teal-slope/windows-optimizer-desktop&Date"><img src="https://api.star-history.com/svg?repos=azure-teal-slope/windows-optimizer-desktop&type=Date" width="260" alt="star history azure-teal-slope/windows-optimizer-desktop"></a>

<a href="https://www.star-history.com/#azuremaple1997/coreldraw-desktop&Date"><img src="https://api.star-history.com/svg?repos=azuremaple1997/coreldraw-desktop&type=Date" width="260" alt="star history azuremaple1997/coreldraw-desktop"></a>

<a href="https://www.star-history.com/#ben-cook-42/kontakt-8-desktop&Date"><img src="https://api.star-history.com/svg?repos=ben-cook-42/kontakt-8-desktop&type=Date" width="260" alt="star history ben-cook-42/kontakt-8-desktop"></a>

<a href="https://www.star-history.com/#briskember13/adobe-acrobat-pdf-desktop&Date"><img src="https://api.star-history.com/svg?repos=briskember13/adobe-acrobat-pdf-desktop&type=Date" width="260" alt="star history briskember13/adobe-acrobat-pdf-desktop"></a>

</details>

### Fastest rising this week (last 7 days)

| # | Project | Stars gained | Stars/day | Total stars |
|---|---|---:|---:|---:|
| 1 | [zed-industries/zed](https://github.com/zed-industries/zed)<br>Opens fast, and you can code together with others<br>`Developer Tools` | +1,280 | 182.9 | 95,021 |
| 2 | [astral-sh/uv](https://github.com/astral-sh/uv)<br>Install Python packages without the wait<br>`Developer Tools` | +408 | 58.3 | 91,989 |
| 3 | [jdx/mise](https://github.com/jdx/mise)<br>Dev tools, env variables and tasks, in one tool<br>`Developer Tools` | +256 | 36.6 | 36,130 |
| 4 | [BurntSushi/ripgrep](https://github.com/BurntSushi/ripgrep)<br>Search a whole folder for text, faster than grep<br>`Developer Tools` | +223 | 31.9 | 69,944 |
| 5 | [oven-sh/bun](https://github.com/oven-sh/bun)<br>Run, bundle, test, install: one tool does it all<br>`Developer Tools` | +159 | 22.7 | 96,693 |
| 6 | [cli/cli](https://github.com/cli/cli)<br>Handle GitHub from the command line, no browser<br>`Developer Tools` | +117 | 16.7 | 47,015 |
| 7 | [helix-editor/helix](https://github.com/helix-editor/helix)<br>A text editor with language server and highlighting built in<br>`Developer Tools` | +99 | 14.1 | 46,892 |
| 8 | [biomejs/biome](https://github.com/biomejs/biome)<br>Format and check web code with one tool<br>`Developer Tools` | +55 | 7.9 | 26,102 |

<details>
<summary>Star history charts for this board</summary>

<a href="https://www.star-history.com/#zed-industries/zed&Date"><img src="https://api.star-history.com/svg?repos=zed-industries/zed&type=Date" width="260" alt="star history zed-industries/zed"></a>

<a href="https://www.star-history.com/#astral-sh/uv&Date"><img src="https://api.star-history.com/svg?repos=astral-sh/uv&type=Date" width="260" alt="star history astral-sh/uv"></a>

<a href="https://www.star-history.com/#jdx/mise&Date"><img src="https://api.star-history.com/svg?repos=jdx/mise&type=Date" width="260" alt="star history jdx/mise"></a>

<a href="https://www.star-history.com/#BurntSushi/ripgrep&Date"><img src="https://api.star-history.com/svg?repos=BurntSushi/ripgrep&type=Date" width="260" alt="star history BurntSushi/ripgrep"></a>

<a href="https://www.star-history.com/#oven-sh/bun&Date"><img src="https://api.star-history.com/svg?repos=oven-sh/bun&type=Date" width="260" alt="star history oven-sh/bun"></a>

<a href="https://www.star-history.com/#cli/cli&Date"><img src="https://api.star-history.com/svg?repos=cli/cli&type=Date" width="260" alt="star history cli/cli"></a>

<a href="https://www.star-history.com/#helix-editor/helix&Date"><img src="https://api.star-history.com/svg?repos=helix-editor/helix&type=Date" width="260" alt="star history helix-editor/helix"></a>

<a href="https://www.star-history.com/#biomejs/biome&Date"><img src="https://api.star-history.com/svg?repos=biomejs/biome&type=Date" width="260" alt="star history biomejs/biome"></a>

</details>

### Fastest rising this month (last 30 days)

| # | Project | Stars gained | Stars/day | Total stars |
|---|---|---:|---:|---:|
| 1 | [zed-industries/zed](https://github.com/zed-industries/zed)<br>Opens fast, and you can code together with others<br>`Developer Tools` | +3,552 | 118.4 | 95,021 |
| 2 | [astral-sh/uv](https://github.com/astral-sh/uv)<br>Install Python packages without the wait<br>`Developer Tools` | +1,386 | 46.2 | 91,989 |
| 3 | [jdx/mise](https://github.com/jdx/mise)<br>Dev tools, env variables and tasks, in one tool<br>`Developer Tools` | +1,182 | 39.4 | 36,130 |
| 4 | [BurntSushi/ripgrep](https://github.com/BurntSushi/ripgrep)<br>Search a whole folder for text, faster than grep<br>`Developer Tools` | +959 | 32.0 | 69,944 |
| 5 | [oven-sh/bun](https://github.com/oven-sh/bun)<br>Run, bundle, test, install: one tool does it all<br>`Developer Tools` | +685 | 22.8 | 96,693 |
| 6 | [cli/cli](https://github.com/cli/cli)<br>Handle GitHub from the command line, no browser<br>`Developer Tools` | +448 | 14.9 | 47,015 |
| 7 | [helix-editor/helix](https://github.com/helix-editor/helix)<br>A text editor with language server and highlighting built in<br>`Developer Tools` | +415 | 13.8 | 46,892 |
| 8 | [biomejs/biome](https://github.com/biomejs/biome)<br>Format and check web code with one tool<br>`Developer Tools` | +216 | 7.2 | 26,102 |

<details>
<summary>Star history charts for this board</summary>

<a href="https://www.star-history.com/#zed-industries/zed&Date"><img src="https://api.star-history.com/svg?repos=zed-industries/zed&type=Date" width="260" alt="star history zed-industries/zed"></a>

<a href="https://www.star-history.com/#astral-sh/uv&Date"><img src="https://api.star-history.com/svg?repos=astral-sh/uv&type=Date" width="260" alt="star history astral-sh/uv"></a>

<a href="https://www.star-history.com/#jdx/mise&Date"><img src="https://api.star-history.com/svg?repos=jdx/mise&type=Date" width="260" alt="star history jdx/mise"></a>

<a href="https://www.star-history.com/#BurntSushi/ripgrep&Date"><img src="https://api.star-history.com/svg?repos=BurntSushi/ripgrep&type=Date" width="260" alt="star history BurntSushi/ripgrep"></a>

<a href="https://www.star-history.com/#oven-sh/bun&Date"><img src="https://api.star-history.com/svg?repos=oven-sh/bun&type=Date" width="260" alt="star history oven-sh/bun"></a>

<a href="https://www.star-history.com/#cli/cli&Date"><img src="https://api.star-history.com/svg?repos=cli/cli&type=Date" width="260" alt="star history cli/cli"></a>

<a href="https://www.star-history.com/#helix-editor/helix&Date"><img src="https://api.star-history.com/svg?repos=helix-editor/helix&type=Date" width="260" alt="star history helix-editor/helix"></a>

<a href="https://www.star-history.com/#biomejs/biome&Date"><img src="https://api.star-history.com/svg?repos=biomejs/biome&type=Date" width="260" alt="star history biomejs/biome"></a>

</details>

### Fastest rising this year (last 365 days)

| # | Project | Stars gained | Stars/day | Total stars |
|---|---|---:|---:|---:|
| 1 | [zed-industries/zed](https://github.com/zed-industries/zed)<br>Opens fast, and you can code together with others<br>`Developer Tools` | +27,392 | 75.0 | 95,021 |
| 2 | [astral-sh/uv](https://github.com/astral-sh/uv)<br>Install Python packages without the wait<br>`Developer Tools` | +20,758 | 56.9 | 91,989 |
| 3 | [oven-sh/bun](https://github.com/oven-sh/bun)<br>Run, bundle, test, install: one tool does it all<br>`Developer Tools` | +16,517 | 45.3 | 96,693 |
| 4 | [jdx/mise](https://github.com/jdx/mise)<br>Dev tools, env variables and tasks, in one tool<br>`Developer Tools` | +15,228 | 41.7 | 36,130 |
| 5 | [BurntSushi/ripgrep](https://github.com/BurntSushi/ripgrep)<br>Search a whole folder for text, faster than grep<br>`Developer Tools` | +13,374 | 36.6 | 69,944 |
| 6 | [helix-editor/helix](https://github.com/helix-editor/helix)<br>A text editor with language server and highlighting built in<br>`Developer Tools` | +6,514 | 17.8 | 46,892 |
| 7 | [cli/cli](https://github.com/cli/cli)<br>Handle GitHub from the command line, no browser<br>`Developer Tools` | +6,313 | 17.3 | 47,015 |
| 8 | [biomejs/biome](https://github.com/biomejs/biome)<br>Format and check web code with one tool<br>`Developer Tools` | +4,426 | 12.1 | 26,102 |

<details>
<summary>Star history charts for this board</summary>

<a href="https://www.star-history.com/#zed-industries/zed&Date"><img src="https://api.star-history.com/svg?repos=zed-industries/zed&type=Date" width="260" alt="star history zed-industries/zed"></a>

<a href="https://www.star-history.com/#astral-sh/uv&Date"><img src="https://api.star-history.com/svg?repos=astral-sh/uv&type=Date" width="260" alt="star history astral-sh/uv"></a>

<a href="https://www.star-history.com/#oven-sh/bun&Date"><img src="https://api.star-history.com/svg?repos=oven-sh/bun&type=Date" width="260" alt="star history oven-sh/bun"></a>

<a href="https://www.star-history.com/#jdx/mise&Date"><img src="https://api.star-history.com/svg?repos=jdx/mise&type=Date" width="260" alt="star history jdx/mise"></a>

<a href="https://www.star-history.com/#BurntSushi/ripgrep&Date"><img src="https://api.star-history.com/svg?repos=BurntSushi/ripgrep&type=Date" width="260" alt="star history BurntSushi/ripgrep"></a>

<a href="https://www.star-history.com/#helix-editor/helix&Date"><img src="https://api.star-history.com/svg?repos=helix-editor/helix&type=Date" width="260" alt="star history helix-editor/helix"></a>

<a href="https://www.star-history.com/#cli/cli&Date"><img src="https://api.star-history.com/svg?repos=cli/cli&type=Date" width="260" alt="star history cli/cli"></a>

<a href="https://www.star-history.com/#biomejs/biome&Date"><img src="https://api.star-history.com/svg?repos=biomejs/biome&type=Date" width="260" alt="star history biomejs/biome"></a>

</details>

### Total stars (all time)

| # | Project | Total stars |
|---|---|---:|
| 1 | [oven-sh/bun](https://github.com/oven-sh/bun)<br>Run, bundle, test, install: one tool does it all<br>`Developer Tools` | 96,693 |
| 2 | [zed-industries/zed](https://github.com/zed-industries/zed)<br>Opens fast, and you can code together with others<br>`Developer Tools` | 95,021 |
| 3 | [astral-sh/uv](https://github.com/astral-sh/uv)<br>Install Python packages without the wait<br>`Developer Tools` | 91,989 |
| 4 | [BurntSushi/ripgrep](https://github.com/BurntSushi/ripgrep)<br>Search a whole folder for text, faster than grep<br>`Developer Tools` | 69,944 |
| 5 | [cli/cli](https://github.com/cli/cli)<br>Handle GitHub from the command line, no browser<br>`Developer Tools` | 47,015 |
| 6 | [helix-editor/helix](https://github.com/helix-editor/helix)<br>A text editor with language server and highlighting built in<br>`Developer Tools` | 46,892 |
| 7 | [jdx/mise](https://github.com/jdx/mise)<br>Dev tools, env variables and tasks, in one tool<br>`Developer Tools` | 36,130 |
| 8 | [biomejs/biome](https://github.com/biomejs/biome)<br>Format and check web code with one tool<br>`Developer Tools` | 26,102 |

<details>
<summary>Star history charts for this board</summary>

<a href="https://www.star-history.com/#oven-sh/bun&Date"><img src="https://api.star-history.com/svg?repos=oven-sh/bun&type=Date" width="260" alt="star history oven-sh/bun"></a>

<a href="https://www.star-history.com/#zed-industries/zed&Date"><img src="https://api.star-history.com/svg?repos=zed-industries/zed&type=Date" width="260" alt="star history zed-industries/zed"></a>

<a href="https://www.star-history.com/#astral-sh/uv&Date"><img src="https://api.star-history.com/svg?repos=astral-sh/uv&type=Date" width="260" alt="star history astral-sh/uv"></a>

<a href="https://www.star-history.com/#BurntSushi/ripgrep&Date"><img src="https://api.star-history.com/svg?repos=BurntSushi/ripgrep&type=Date" width="260" alt="star history BurntSushi/ripgrep"></a>

<a href="https://www.star-history.com/#cli/cli&Date"><img src="https://api.star-history.com/svg?repos=cli/cli&type=Date" width="260" alt="star history cli/cli"></a>

<a href="https://www.star-history.com/#helix-editor/helix&Date"><img src="https://api.star-history.com/svg?repos=helix-editor/helix&type=Date" width="260" alt="star history helix-editor/helix"></a>

<a href="https://www.star-history.com/#jdx/mise&Date"><img src="https://api.star-history.com/svg?repos=jdx/mise&type=Date" width="260" alt="star history jdx/mise"></a>

<a href="https://www.star-history.com/#biomejs/biome&Date"><img src="https://api.star-history.com/svg?repos=biomejs/biome&type=Date" width="260" alt="star history biomejs/biome"></a>

</details>

## Security

> Vulnerability scanners, SAST, supply-chain and runtime security

### Hottest new repos (created in the last 7 days)

No new repo met the criteria in this run.

### Fastest rising this week (last 7 days)

| # | Project | Stars gained | Stars/day | Total stars |
|---|---|---:|---:|---:|
| 1 | [projectdiscovery/nuclei](https://github.com/projectdiscovery/nuclei)<br>Write one template, scan for vulnerabilities in bulk<br>`Security` | +257 | 36.7 | 32,904 |
| 2 | [aquasecurity/trivy](https://github.com/aquasecurity/trivy)<br>Scan containers and code repos for security issues at once<br>`Security` | +252 | 36.0 | 39,337 |
| 3 | [semgrep/semgrep](https://github.com/semgrep/semgrep)<br>Catch the problems in your code before you commit<br>`Security` | +139 | 19.9 | 17,670 |
| 4 | [OWASP/CheatSheetSeries](https://github.com/OWASP/CheatSheetSeries)<br>Concise cheat sheets on application security<br>`Security` | +138 | 19.7 | 34,056 |
| 5 | [google/osv-scanner](https://github.com/google/osv-scanner)<br>Are your dependencies safe? One scan tells you<br>`Security` | +78 | 11.1 | 11,516 |
| 6 | [anchore/grype](https://github.com/anchore/grype)<br>Does your container image have vulnerabilities? Scan it<br>`Security` | +63 | 9.0 | 13,265 |
| 7 | [falcosecurity/falco](https://github.com/falcosecurity/falco)<br>Know the moment something odd happens in the cloud<br>`Security` | +20 | 2.9 | 9,579 |
| 8 | [securego/gosec](https://github.com/securego/gosec)<br>Scan your Go code for security problems<br>`Security` | +6 | 0.9 | 9,005 |

<details>
<summary>Star history charts for this board</summary>

<a href="https://www.star-history.com/#projectdiscovery/nuclei&Date"><img src="https://api.star-history.com/svg?repos=projectdiscovery/nuclei&type=Date" width="260" alt="star history projectdiscovery/nuclei"></a>

<a href="https://www.star-history.com/#aquasecurity/trivy&Date"><img src="https://api.star-history.com/svg?repos=aquasecurity/trivy&type=Date" width="260" alt="star history aquasecurity/trivy"></a>

<a href="https://www.star-history.com/#semgrep/semgrep&Date"><img src="https://api.star-history.com/svg?repos=semgrep/semgrep&type=Date" width="260" alt="star history semgrep/semgrep"></a>

<a href="https://www.star-history.com/#OWASP/CheatSheetSeries&Date"><img src="https://api.star-history.com/svg?repos=OWASP/CheatSheetSeries&type=Date" width="260" alt="star history OWASP/CheatSheetSeries"></a>

<a href="https://www.star-history.com/#google/osv-scanner&Date"><img src="https://api.star-history.com/svg?repos=google/osv-scanner&type=Date" width="260" alt="star history google/osv-scanner"></a>

<a href="https://www.star-history.com/#anchore/grype&Date"><img src="https://api.star-history.com/svg?repos=anchore/grype&type=Date" width="260" alt="star history anchore/grype"></a>

<a href="https://www.star-history.com/#falcosecurity/falco&Date"><img src="https://api.star-history.com/svg?repos=falcosecurity/falco&type=Date" width="260" alt="star history falcosecurity/falco"></a>

<a href="https://www.star-history.com/#securego/gosec&Date"><img src="https://api.star-history.com/svg?repos=securego/gosec&type=Date" width="260" alt="star history securego/gosec"></a>

</details>

### Fastest rising this month (last 30 days)

| # | Project | Stars gained | Stars/day | Total stars |
|---|---|---:|---:|---:|
| 1 | [aquasecurity/trivy](https://github.com/aquasecurity/trivy)<br>Scan containers and code repos for security issues at once<br>`Security` | +955 | 31.8 | 39,337 |
| 2 | [projectdiscovery/nuclei](https://github.com/projectdiscovery/nuclei)<br>Write one template, scan for vulnerabilities in bulk<br>`Security` | +933 | 31.1 | 32,904 |
| 3 | [semgrep/semgrep](https://github.com/semgrep/semgrep)<br>Catch the problems in your code before you commit<br>`Security` | +627 | 20.9 | 17,670 |
| 4 | [OWASP/CheatSheetSeries](https://github.com/OWASP/CheatSheetSeries)<br>Concise cheat sheets on application security<br>`Security` | +449 | 15.0 | 34,056 |
| 5 | [google/osv-scanner](https://github.com/google/osv-scanner)<br>Are your dependencies safe? One scan tells you<br>`Security` | +347 | 11.6 | 11,516 |
| 6 | [anchore/grype](https://github.com/anchore/grype)<br>Does your container image have vulnerabilities? Scan it<br>`Security` | +246 | 8.2 | 13,265 |
| 7 | [falcosecurity/falco](https://github.com/falcosecurity/falco)<br>Know the moment something odd happens in the cloud<br>`Security` | +117 | 3.9 | 9,579 |
| 8 | [securego/gosec](https://github.com/securego/gosec)<br>Scan your Go code for security problems<br>`Security` | +38 | 1.3 | 9,005 |

<details>
<summary>Star history charts for this board</summary>

<a href="https://www.star-history.com/#aquasecurity/trivy&Date"><img src="https://api.star-history.com/svg?repos=aquasecurity/trivy&type=Date" width="260" alt="star history aquasecurity/trivy"></a>

<a href="https://www.star-history.com/#projectdiscovery/nuclei&Date"><img src="https://api.star-history.com/svg?repos=projectdiscovery/nuclei&type=Date" width="260" alt="star history projectdiscovery/nuclei"></a>

<a href="https://www.star-history.com/#semgrep/semgrep&Date"><img src="https://api.star-history.com/svg?repos=semgrep/semgrep&type=Date" width="260" alt="star history semgrep/semgrep"></a>

<a href="https://www.star-history.com/#OWASP/CheatSheetSeries&Date"><img src="https://api.star-history.com/svg?repos=OWASP/CheatSheetSeries&type=Date" width="260" alt="star history OWASP/CheatSheetSeries"></a>

<a href="https://www.star-history.com/#google/osv-scanner&Date"><img src="https://api.star-history.com/svg?repos=google/osv-scanner&type=Date" width="260" alt="star history google/osv-scanner"></a>

<a href="https://www.star-history.com/#anchore/grype&Date"><img src="https://api.star-history.com/svg?repos=anchore/grype&type=Date" width="260" alt="star history anchore/grype"></a>

<a href="https://www.star-history.com/#falcosecurity/falco&Date"><img src="https://api.star-history.com/svg?repos=falcosecurity/falco&type=Date" width="260" alt="star history falcosecurity/falco"></a>

<a href="https://www.star-history.com/#securego/gosec&Date"><img src="https://api.star-history.com/svg?repos=securego/gosec&type=Date" width="260" alt="star history securego/gosec"></a>

</details>

### Fastest rising this year (last 365 days)

| # | Project | Stars gained | Stars/day | Total stars |
|---|---|---:|---:|---:|
| 1 | [aquasecurity/trivy](https://github.com/aquasecurity/trivy)<br>Scan containers and code repos for security issues at once<br>`Security` | +10,380 | 28.4 | 39,337 |
| 2 | [projectdiscovery/nuclei](https://github.com/projectdiscovery/nuclei)<br>Write one template, scan for vulnerabilities in bulk<br>`Security` | +7,854 | 21.5 | 32,904 |
| 3 | [semgrep/semgrep](https://github.com/semgrep/semgrep)<br>Catch the problems in your code before you commit<br>`Security` | +4,538 | 12.4 | 17,670 |
| 4 | [OWASP/CheatSheetSeries](https://github.com/OWASP/CheatSheetSeries)<br>Concise cheat sheets on application security<br>`Security` | +3,641 | 10.0 | 34,056 |
| 5 | [google/osv-scanner](https://github.com/google/osv-scanner)<br>Are your dependencies safe? One scan tells you<br>`Security` | +3,599 | 9.9 | 11,516 |
| 6 | [anchore/grype](https://github.com/anchore/grype)<br>Does your container image have vulnerabilities? Scan it<br>`Security` | +2,386 | 6.5 | 13,265 |
| 7 | [falcosecurity/falco](https://github.com/falcosecurity/falco)<br>Know the moment something odd happens in the cloud<br>`Security` | +1,272 | 3.5 | 9,579 |
| 8 | [securego/gosec](https://github.com/securego/gosec)<br>Scan your Go code for security problems<br>`Security` | +553 | 1.5 | 9,005 |

<details>
<summary>Star history charts for this board</summary>

<a href="https://www.star-history.com/#aquasecurity/trivy&Date"><img src="https://api.star-history.com/svg?repos=aquasecurity/trivy&type=Date" width="260" alt="star history aquasecurity/trivy"></a>

<a href="https://www.star-history.com/#projectdiscovery/nuclei&Date"><img src="https://api.star-history.com/svg?repos=projectdiscovery/nuclei&type=Date" width="260" alt="star history projectdiscovery/nuclei"></a>

<a href="https://www.star-history.com/#semgrep/semgrep&Date"><img src="https://api.star-history.com/svg?repos=semgrep/semgrep&type=Date" width="260" alt="star history semgrep/semgrep"></a>

<a href="https://www.star-history.com/#OWASP/CheatSheetSeries&Date"><img src="https://api.star-history.com/svg?repos=OWASP/CheatSheetSeries&type=Date" width="260" alt="star history OWASP/CheatSheetSeries"></a>

<a href="https://www.star-history.com/#google/osv-scanner&Date"><img src="https://api.star-history.com/svg?repos=google/osv-scanner&type=Date" width="260" alt="star history google/osv-scanner"></a>

<a href="https://www.star-history.com/#anchore/grype&Date"><img src="https://api.star-history.com/svg?repos=anchore/grype&type=Date" width="260" alt="star history anchore/grype"></a>

<a href="https://www.star-history.com/#falcosecurity/falco&Date"><img src="https://api.star-history.com/svg?repos=falcosecurity/falco&type=Date" width="260" alt="star history falcosecurity/falco"></a>

<a href="https://www.star-history.com/#securego/gosec&Date"><img src="https://api.star-history.com/svg?repos=securego/gosec&type=Date" width="260" alt="star history securego/gosec"></a>

</details>

### Total stars (all time)

| # | Project | Total stars |
|---|---|---:|
| 1 | [aquasecurity/trivy](https://github.com/aquasecurity/trivy)<br>Scan containers and code repos for security issues at once<br>`Security` | 39,337 |
| 2 | [OWASP/CheatSheetSeries](https://github.com/OWASP/CheatSheetSeries)<br>Concise cheat sheets on application security<br>`Security` | 34,056 |
| 3 | [projectdiscovery/nuclei](https://github.com/projectdiscovery/nuclei)<br>Write one template, scan for vulnerabilities in bulk<br>`Security` | 32,904 |
| 4 | [semgrep/semgrep](https://github.com/semgrep/semgrep)<br>Catch the problems in your code before you commit<br>`Security` | 17,670 |
| 5 | [anchore/grype](https://github.com/anchore/grype)<br>Does your container image have vulnerabilities? Scan it<br>`Security` | 13,265 |
| 6 | [google/osv-scanner](https://github.com/google/osv-scanner)<br>Are your dependencies safe? One scan tells you<br>`Security` | 11,516 |
| 7 | [falcosecurity/falco](https://github.com/falcosecurity/falco)<br>Know the moment something odd happens in the cloud<br>`Security` | 9,579 |
| 8 | [securego/gosec](https://github.com/securego/gosec)<br>Scan your Go code for security problems<br>`Security` | 9,005 |

<details>
<summary>Star history charts for this board</summary>

<a href="https://www.star-history.com/#aquasecurity/trivy&Date"><img src="https://api.star-history.com/svg?repos=aquasecurity/trivy&type=Date" width="260" alt="star history aquasecurity/trivy"></a>

<a href="https://www.star-history.com/#OWASP/CheatSheetSeries&Date"><img src="https://api.star-history.com/svg?repos=OWASP/CheatSheetSeries&type=Date" width="260" alt="star history OWASP/CheatSheetSeries"></a>

<a href="https://www.star-history.com/#projectdiscovery/nuclei&Date"><img src="https://api.star-history.com/svg?repos=projectdiscovery/nuclei&type=Date" width="260" alt="star history projectdiscovery/nuclei"></a>

<a href="https://www.star-history.com/#semgrep/semgrep&Date"><img src="https://api.star-history.com/svg?repos=semgrep/semgrep&type=Date" width="260" alt="star history semgrep/semgrep"></a>

<a href="https://www.star-history.com/#anchore/grype&Date"><img src="https://api.star-history.com/svg?repos=anchore/grype&type=Date" width="260" alt="star history anchore/grype"></a>

<a href="https://www.star-history.com/#google/osv-scanner&Date"><img src="https://api.star-history.com/svg?repos=google/osv-scanner&type=Date" width="260" alt="star history google/osv-scanner"></a>

<a href="https://www.star-history.com/#falcosecurity/falco&Date"><img src="https://api.star-history.com/svg?repos=falcosecurity/falco&type=Date" width="260" alt="star history falcosecurity/falco"></a>

<a href="https://www.star-history.com/#securego/gosec&Date"><img src="https://api.star-history.com/svg?repos=securego/gosec&type=Date" width="260" alt="star history securego/gosec"></a>

</details>

## Web / Frontend

> Frontend frameworks, UI kits, CSS and browser tooling

### Hottest new repos (created in the last 7 days)

| # | Project | Created (UTC) | Total stars | Stars/day |
|---|---|---|---:|---:|
| 1 | [opencoredev/islandcn](https://github.com/opencoredev/islandcn)<br>Add an open-source Dynamic Island to React with shadcn | 2026-11-13<br><sub>1.1 d</sub> | 587 | 542.1 |
| 2 | [AdvisorShake/ai--manus](https://github.com/AdvisorShake/ai--manus)<br>Let an AI Agent run tools and operations in a sandbox | 2026-11-13<br><sub>1.0 d</sub> | 266 | 266.0 |
| 3 | [AgentLobster/ai--manus](https://github.com/AgentLobster/ai--manus)<br>Need an AI agent to run tools? Run them in a sandbox | 2026-11-13<br><sub>1.0 d</sub> | 266 | 266.0 |
| 4 | [AmplitudeBoss/ai--manus](https://github.com/AmplitudeBoss/ai--manus)<br>Need an AI agent to run tools? Run them in a sandbox | 2026-11-13<br><sub>1.0 d</sub> | 266 | 266.0 |
| 5 | [AtomEmissary/ai--manus](https://github.com/AtomEmissary/ai--manus)<br>Need an AI agent to run tools? Run them in a sandbox | 2026-11-13<br><sub>1.0 d</sub> | 266 | 266.0 |
| 6 | [avenuemistravage47/ai--manus](https://github.com/avenuemistravage47/ai--manus)<br>Need an AI agent to run tools? Run them in a sandbox | 2026-11-13<br><sub>1.0 d</sub> | 266 | 266.0 |
| 7 | [bandbeetleruminate/ai--manus](https://github.com/bandbeetleruminate/ai--manus)<br>Need an AI agent to run tools? Run them in a sandbox | 2026-11-13<br><sub>1.0 d</sub> | 266 | 266.0 |
| 8 | [BannerCatbird/ai--manus](https://github.com/BannerCatbird/ai--manus)<br>Need an AI agent to run tools? Run them in a sandbox | 2026-11-13<br><sub>1.0 d</sub> | 266 | 266.0 |
| 9 | [Beachnuconceal/ai--manus](https://github.com/Beachnuconceal/ai--manus)<br>Need an AI agent to run tools? Run them in a sandbox | 2026-11-13<br><sub>1.0 d</sub> | 266 | 266.0 |
| 10 | [BeastBlazeAttract/ai--manus](https://github.com/BeastBlazeAttract/ai--manus)<br>Need an AI agent to run tools? Run them in a sandbox | 2026-11-13<br><sub>1.0 d</sub> | 266 | 266.0 |

<details>
<summary>Star history charts for this board</summary>

<a href="https://www.star-history.com/#opencoredev/islandcn&Date"><img src="https://api.star-history.com/svg?repos=opencoredev/islandcn&type=Date" width="260" alt="star history opencoredev/islandcn"></a>

<a href="https://www.star-history.com/#AdvisorShake/ai--manus&Date"><img src="https://api.star-history.com/svg?repos=AdvisorShake/ai--manus&type=Date" width="260" alt="star history AdvisorShake/ai--manus"></a>

<a href="https://www.star-history.com/#AgentLobster/ai--manus&Date"><img src="https://api.star-history.com/svg?repos=AgentLobster/ai--manus&type=Date" width="260" alt="star history AgentLobster/ai--manus"></a>

<a href="https://www.star-history.com/#AmplitudeBoss/ai--manus&Date"><img src="https://api.star-history.com/svg?repos=AmplitudeBoss/ai--manus&type=Date" width="260" alt="star history AmplitudeBoss/ai--manus"></a>

<a href="https://www.star-history.com/#AtomEmissary/ai--manus&Date"><img src="https://api.star-history.com/svg?repos=AtomEmissary/ai--manus&type=Date" width="260" alt="star history AtomEmissary/ai--manus"></a>

<a href="https://www.star-history.com/#avenuemistravage47/ai--manus&Date"><img src="https://api.star-history.com/svg?repos=avenuemistravage47/ai--manus&type=Date" width="260" alt="star history avenuemistravage47/ai--manus"></a>

<a href="https://www.star-history.com/#bandbeetleruminate/ai--manus&Date"><img src="https://api.star-history.com/svg?repos=bandbeetleruminate/ai--manus&type=Date" width="260" alt="star history bandbeetleruminate/ai--manus"></a>

<a href="https://www.star-history.com/#BannerCatbird/ai--manus&Date"><img src="https://api.star-history.com/svg?repos=BannerCatbird/ai--manus&type=Date" width="260" alt="star history BannerCatbird/ai--manus"></a>

<a href="https://www.star-history.com/#Beachnuconceal/ai--manus&Date"><img src="https://api.star-history.com/svg?repos=Beachnuconceal/ai--manus&type=Date" width="260" alt="star history Beachnuconceal/ai--manus"></a>

<a href="https://www.star-history.com/#BeastBlazeAttract/ai--manus&Date"><img src="https://api.star-history.com/svg?repos=BeastBlazeAttract/ai--manus&type=Date" width="260" alt="star history BeastBlazeAttract/ai--manus"></a>

</details>

### Fastest rising this week (last 7 days)

| # | Project | Stars gained | Stars/day | Total stars |
|---|---|---:|---:|---:|
| 1 | [shadcn-ui/ui](https://github.com/shadcn-ui/ui)<br>Good-looking components, and the code is yours to change<br>`Web / Frontend` | +676 | 96.6 | 128,166 |
| 2 | [tailwindlabs/tailwindcss](https://github.com/tailwindlabs/tailwindcss)<br>Custom designs without writing a pile of CSS<br>`Web / Frontend` | +568 | 81.1 | 98,601 |
| 3 | [facebook/react](https://github.com/facebook/react)<br>Build web and native app interfaces with one library<br>`Web / Frontend` | +452 | 64.6 | 252,602 |
| 4 | [vuejs/core](https://github.com/vuejs/core)<br>Start with one small page, learn only what you use<br>`Web / Frontend` | +200 | 28.6 | 55,016 |
| 5 | [sveltejs/svelte](https://github.com/sveltejs/svelte)<br>A compiler turns your components into efficient web code<br>`Web / Frontend` | +199 | 28.4 | 88,733 |
| 6 | [vercel/next.js](https://github.com/vercel/next.js)<br>Build a whole site with React, front to back<br>`Web / Frontend` | +188 | 26.9 | 143,510 |
| 7 | [withastro/astro](https://github.com/withastro/astro)<br>For content-driven websites, with lightweight output<br>`Web / Frontend` | +175 | 25.0 | 63,940 |
| 8 | [tanstack/query](https://github.com/tanstack/query)<br>Fetching data and caching it? Leave it to this<br>`Web / Frontend` | +40 | 5.7 | 50,564 |

<details>
<summary>Star history charts for this board</summary>

<a href="https://www.star-history.com/#shadcn-ui/ui&Date"><img src="https://api.star-history.com/svg?repos=shadcn-ui/ui&type=Date" width="260" alt="star history shadcn-ui/ui"></a>

<a href="https://www.star-history.com/#tailwindlabs/tailwindcss&Date"><img src="https://api.star-history.com/svg?repos=tailwindlabs/tailwindcss&type=Date" width="260" alt="star history tailwindlabs/tailwindcss"></a>

<a href="https://www.star-history.com/#facebook/react&Date"><img src="https://api.star-history.com/svg?repos=facebook/react&type=Date" width="260" alt="star history facebook/react"></a>

<a href="https://www.star-history.com/#vuejs/core&Date"><img src="https://api.star-history.com/svg?repos=vuejs/core&type=Date" width="260" alt="star history vuejs/core"></a>

<a href="https://www.star-history.com/#sveltejs/svelte&Date"><img src="https://api.star-history.com/svg?repos=sveltejs/svelte&type=Date" width="260" alt="star history sveltejs/svelte"></a>

<a href="https://www.star-history.com/#vercel/next.js&Date"><img src="https://api.star-history.com/svg?repos=vercel/next.js&type=Date" width="260" alt="star history vercel/next.js"></a>

<a href="https://www.star-history.com/#withastro/astro&Date"><img src="https://api.star-history.com/svg?repos=withastro/astro&type=Date" width="260" alt="star history withastro/astro"></a>

<a href="https://www.star-history.com/#tanstack/query&Date"><img src="https://api.star-history.com/svg?repos=tanstack/query&type=Date" width="260" alt="star history tanstack/query"></a>

</details>

### Fastest rising this month (last 30 days)

| # | Project | Stars gained | Stars/day | Total stars |
|---|---|---:|---:|---:|
| 1 | [shadcn-ui/ui](https://github.com/shadcn-ui/ui)<br>Good-looking components, and the code is yours to change<br>`Web / Frontend` | +2,797 | 93.2 | 128,166 |
| 2 | [facebook/react](https://github.com/facebook/react)<br>Build web and native app interfaces with one library<br>`Web / Frontend` | +2,006 | 66.9 | 252,602 |
| 3 | [tailwindlabs/tailwindcss](https://github.com/tailwindlabs/tailwindcss)<br>Custom designs without writing a pile of CSS<br>`Web / Frontend` | +933 | 31.1 | 98,601 |
| 4 | [withastro/astro](https://github.com/withastro/astro)<br>For content-driven websites, with lightweight output<br>`Web / Frontend` | +807 | 26.9 | 63,940 |
| 5 | [vercel/next.js](https://github.com/vercel/next.js)<br>Build a whole site with React, front to back<br>`Web / Frontend` | +786 | 26.2 | 143,510 |
| 6 | [sveltejs/svelte](https://github.com/sveltejs/svelte)<br>A compiler turns your components into efficient web code<br>`Web / Frontend` | +531 | 17.7 | 88,733 |
| 7 | [vuejs/core](https://github.com/vuejs/core)<br>Start with one small page, learn only what you use<br>`Web / Frontend` | +464 | 15.5 | 55,016 |
| 8 | [tanstack/query](https://github.com/tanstack/query)<br>Fetching data and caching it? Leave it to this<br>`Web / Frontend` | +203 | 6.8 | 50,564 |

<details>
<summary>Star history charts for this board</summary>

<a href="https://www.star-history.com/#shadcn-ui/ui&Date"><img src="https://api.star-history.com/svg?repos=shadcn-ui/ui&type=Date" width="260" alt="star history shadcn-ui/ui"></a>

<a href="https://www.star-history.com/#facebook/react&Date"><img src="https://api.star-history.com/svg?repos=facebook/react&type=Date" width="260" alt="star history facebook/react"></a>

<a href="https://www.star-history.com/#tailwindlabs/tailwindcss&Date"><img src="https://api.star-history.com/svg?repos=tailwindlabs/tailwindcss&type=Date" width="260" alt="star history tailwindlabs/tailwindcss"></a>

<a href="https://www.star-history.com/#withastro/astro&Date"><img src="https://api.star-history.com/svg?repos=withastro/astro&type=Date" width="260" alt="star history withastro/astro"></a>

<a href="https://www.star-history.com/#vercel/next.js&Date"><img src="https://api.star-history.com/svg?repos=vercel/next.js&type=Date" width="260" alt="star history vercel/next.js"></a>

<a href="https://www.star-history.com/#sveltejs/svelte&Date"><img src="https://api.star-history.com/svg?repos=sveltejs/svelte&type=Date" width="260" alt="star history sveltejs/svelte"></a>

<a href="https://www.star-history.com/#vuejs/core&Date"><img src="https://api.star-history.com/svg?repos=vuejs/core&type=Date" width="260" alt="star history vuejs/core"></a>

<a href="https://www.star-history.com/#tanstack/query&Date"><img src="https://api.star-history.com/svg?repos=tanstack/query&type=Date" width="260" alt="star history tanstack/query"></a>

</details>

### Fastest rising this year (last 365 days)

| # | Project | Stars gained | Stars/day | Total stars |
|---|---|---:|---:|---:|
| 1 | [shadcn-ui/ui](https://github.com/shadcn-ui/ui)<br>Good-looking components, and the code is yours to change<br>`Web / Frontend` | +30,497 | 83.6 | 128,166 |
| 2 | [facebook/react](https://github.com/facebook/react)<br>Build web and native app interfaces with one library<br>`Web / Frontend` | +15,680 | 43.0 | 252,602 |
| 3 | [withastro/astro](https://github.com/withastro/astro)<br>For content-driven websites, with lightweight output<br>`Web / Frontend` | +10,564 | 28.9 | 63,940 |
| 4 | [vercel/next.js](https://github.com/vercel/next.js)<br>Build a whole site with React, front to back<br>`Web / Frontend` | +10,407 | 28.5 | 143,510 |
| 5 | [tailwindlabs/tailwindcss](https://github.com/tailwindlabs/tailwindcss)<br>Custom designs without writing a pile of CSS<br>`Web / Frontend` | +8,913 | 24.4 | 98,601 |
| 6 | [sveltejs/svelte](https://github.com/sveltejs/svelte)<br>A compiler turns your components into efficient web code<br>`Web / Frontend` | +5,203 | 14.3 | 88,733 |
| 7 | [tanstack/query](https://github.com/tanstack/query)<br>Fetching data and caching it? Leave it to this<br>`Web / Frontend` | +3,749 | 10.3 | 50,564 |
| 8 | [vuejs/core](https://github.com/vuejs/core)<br>Start with one small page, learn only what you use<br>`Web / Frontend` | +3,719 | 10.2 | 55,016 |

<details>
<summary>Star history charts for this board</summary>

<a href="https://www.star-history.com/#shadcn-ui/ui&Date"><img src="https://api.star-history.com/svg?repos=shadcn-ui/ui&type=Date" width="260" alt="star history shadcn-ui/ui"></a>

<a href="https://www.star-history.com/#facebook/react&Date"><img src="https://api.star-history.com/svg?repos=facebook/react&type=Date" width="260" alt="star history facebook/react"></a>

<a href="https://www.star-history.com/#withastro/astro&Date"><img src="https://api.star-history.com/svg?repos=withastro/astro&type=Date" width="260" alt="star history withastro/astro"></a>

<a href="https://www.star-history.com/#vercel/next.js&Date"><img src="https://api.star-history.com/svg?repos=vercel/next.js&type=Date" width="260" alt="star history vercel/next.js"></a>

<a href="https://www.star-history.com/#tailwindlabs/tailwindcss&Date"><img src="https://api.star-history.com/svg?repos=tailwindlabs/tailwindcss&type=Date" width="260" alt="star history tailwindlabs/tailwindcss"></a>

<a href="https://www.star-history.com/#sveltejs/svelte&Date"><img src="https://api.star-history.com/svg?repos=sveltejs/svelte&type=Date" width="260" alt="star history sveltejs/svelte"></a>

<a href="https://www.star-history.com/#tanstack/query&Date"><img src="https://api.star-history.com/svg?repos=tanstack/query&type=Date" width="260" alt="star history tanstack/query"></a>

<a href="https://www.star-history.com/#vuejs/core&Date"><img src="https://api.star-history.com/svg?repos=vuejs/core&type=Date" width="260" alt="star history vuejs/core"></a>

</details>

### Total stars (all time)

| # | Project | Total stars |
|---|---|---:|
| 1 | [facebook/react](https://github.com/facebook/react)<br>Build web and native app interfaces with one library<br>`Web / Frontend` | 252,602 |
| 2 | [vercel/next.js](https://github.com/vercel/next.js)<br>Build a whole site with React, front to back<br>`Web / Frontend` | 143,510 |
| 3 | [shadcn-ui/ui](https://github.com/shadcn-ui/ui)<br>Good-looking components, and the code is yours to change<br>`Web / Frontend` | 128,166 |
| 4 | [tailwindlabs/tailwindcss](https://github.com/tailwindlabs/tailwindcss)<br>Custom designs without writing a pile of CSS<br>`Web / Frontend` | 98,601 |
| 5 | [sveltejs/svelte](https://github.com/sveltejs/svelte)<br>A compiler turns your components into efficient web code<br>`Web / Frontend` | 88,733 |
| 6 | [withastro/astro](https://github.com/withastro/astro)<br>For content-driven websites, with lightweight output<br>`Web / Frontend` | 63,940 |
| 7 | [vuejs/core](https://github.com/vuejs/core)<br>Start with one small page, learn only what you use<br>`Web / Frontend` | 55,016 |
| 8 | [tanstack/query](https://github.com/tanstack/query)<br>Fetching data and caching it? Leave it to this<br>`Web / Frontend` | 50,564 |

<details>
<summary>Star history charts for this board</summary>

<a href="https://www.star-history.com/#facebook/react&Date"><img src="https://api.star-history.com/svg?repos=facebook/react&type=Date" width="260" alt="star history facebook/react"></a>

<a href="https://www.star-history.com/#vercel/next.js&Date"><img src="https://api.star-history.com/svg?repos=vercel/next.js&type=Date" width="260" alt="star history vercel/next.js"></a>

<a href="https://www.star-history.com/#shadcn-ui/ui&Date"><img src="https://api.star-history.com/svg?repos=shadcn-ui/ui&type=Date" width="260" alt="star history shadcn-ui/ui"></a>

<a href="https://www.star-history.com/#tailwindlabs/tailwindcss&Date"><img src="https://api.star-history.com/svg?repos=tailwindlabs/tailwindcss&type=Date" width="260" alt="star history tailwindlabs/tailwindcss"></a>

<a href="https://www.star-history.com/#sveltejs/svelte&Date"><img src="https://api.star-history.com/svg?repos=sveltejs/svelte&type=Date" width="260" alt="star history sveltejs/svelte"></a>

<a href="https://www.star-history.com/#withastro/astro&Date"><img src="https://api.star-history.com/svg?repos=withastro/astro&type=Date" width="260" alt="star history withastro/astro"></a>

<a href="https://www.star-history.com/#vuejs/core&Date"><img src="https://api.star-history.com/svg?repos=vuejs/core&type=Date" width="260" alt="star history vuejs/core"></a>

<a href="https://www.star-history.com/#tanstack/query&Date"><img src="https://api.star-history.com/svg?repos=tanstack/query&type=Date" width="260" alt="star history tanstack/query"></a>

</details>

## Infrastructure

> Containers, Kubernetes, cloud, networking and observability

### Hottest new repos (created in the last 7 days)

| # | Project | Created (UTC) | Total stars | Stars/day |
|---|---|---|---:|---:|
| 1 | [HolyArrs/HolyArrs](https://github.com/HolyArrs/HolyArrs)<br>Too many apps? Keep shows and music in one self-hosted app | 2026-11-09<br><sub>4.6 d</sub> | 1,141 | 249.1 |
| 2 | [serveroshq/panel](https://github.com/serveroshq/panel)<br>Run the Linux servers you already own in one place | 2026-11-09<br><sub>5.5 d</sub> | 771 | 139.1 |
| 3 | [ValidatorStack/solana-vigil](https://github.com/ValidatorStack/solana-vigil)<br>Check Solana validator health in 60 seconds safely | 2026-11-10<br><sub>3.9 d</sub> | 230 | 58.7 |
| 4 | [MuseumCassowaryCarve/twitch-drops-miner](https://github.com/MuseumCassowaryCarve/twitch-drops-miner)<br>Claim Twitch drops in the background with no video download | 2026-11-08<br><sub>6.3 d</sub> | 119 | 18.9 |

<details>
<summary>Star history charts for this board</summary>

<a href="https://www.star-history.com/#HolyArrs/HolyArrs&Date"><img src="https://api.star-history.com/svg?repos=HolyArrs/HolyArrs&type=Date" width="260" alt="star history HolyArrs/HolyArrs"></a>

<a href="https://www.star-history.com/#serveroshq/panel&Date"><img src="https://api.star-history.com/svg?repos=serveroshq/panel&type=Date" width="260" alt="star history serveroshq/panel"></a>

<a href="https://www.star-history.com/#ValidatorStack/solana-vigil&Date"><img src="https://api.star-history.com/svg?repos=ValidatorStack/solana-vigil&type=Date" width="260" alt="star history ValidatorStack/solana-vigil"></a>

<a href="https://www.star-history.com/#MuseumCassowaryCarve/twitch-drops-miner&Date"><img src="https://api.star-history.com/svg?repos=MuseumCassowaryCarve/twitch-drops-miner&type=Date" width="260" alt="star history MuseumCassowaryCarve/twitch-drops-miner"></a>

</details>

### Fastest rising this week (last 7 days)

| # | Project | Stars gained | Stars/day | Total stars |
|---|---|---:|---:|---:|
| 1 | [prometheus/prometheus](https://github.com/prometheus/prometheus)<br>When the system breaks, the alert finds you first<br>`Infrastructure` | +449 | 64.1 | 67,599 |
| 2 | [kubernetes/kubernetes](https://github.com/kubernetes/kubernetes)<br>Lots of containers? Leave deploying and scaling to it<br>`Infrastructure` | +301 | 43.0 | 129,056 |
| 3 | [docker/compose](https://github.com/docker/compose)<br>Put many containers in one file and run them together<br>`Infrastructure` | +219 | 31.3 | 38,833 |
| 4 | [caddyserver/caddy](https://github.com/caddyserver/caddy)<br>Set up a web server with HTTPS configured for you<br>`Infrastructure` | +198 | 28.3 | 79,038 |
| 5 | [grafana/grafana](https://github.com/grafana/grafana)<br>Metrics, logs and traces on one dashboard<br>`Infrastructure` | +187 | 26.7 | 77,898 |
| 6 | [hashicorp/terraform](https://github.com/hashicorp/terraform)<br>Write cloud resources as code you can review and version<br>`Infrastructure` | +88 | 12.6 | 50,227 |
| 7 | [traefik/traefik](https://github.com/traefik/traefik)<br>With many services, traffic gets sorted automatically<br>`Infrastructure` | +80 | 11.4 | 65,543 |
| 8 | [pulumi/pulumi](https://github.com/pulumi/pulumi)<br>Manage cloud resources in a language you already know<br>`Infrastructure` | +67 | 9.6 | 25,903 |

<details>
<summary>Star history charts for this board</summary>

<a href="https://www.star-history.com/#prometheus/prometheus&Date"><img src="https://api.star-history.com/svg?repos=prometheus/prometheus&type=Date" width="260" alt="star history prometheus/prometheus"></a>

<a href="https://www.star-history.com/#kubernetes/kubernetes&Date"><img src="https://api.star-history.com/svg?repos=kubernetes/kubernetes&type=Date" width="260" alt="star history kubernetes/kubernetes"></a>

<a href="https://www.star-history.com/#docker/compose&Date"><img src="https://api.star-history.com/svg?repos=docker/compose&type=Date" width="260" alt="star history docker/compose"></a>

<a href="https://www.star-history.com/#caddyserver/caddy&Date"><img src="https://api.star-history.com/svg?repos=caddyserver/caddy&type=Date" width="260" alt="star history caddyserver/caddy"></a>

<a href="https://www.star-history.com/#grafana/grafana&Date"><img src="https://api.star-history.com/svg?repos=grafana/grafana&type=Date" width="260" alt="star history grafana/grafana"></a>

<a href="https://www.star-history.com/#hashicorp/terraform&Date"><img src="https://api.star-history.com/svg?repos=hashicorp/terraform&type=Date" width="260" alt="star history hashicorp/terraform"></a>

<a href="https://www.star-history.com/#traefik/traefik&Date"><img src="https://api.star-history.com/svg?repos=traefik/traefik&type=Date" width="260" alt="star history traefik/traefik"></a>

<a href="https://www.star-history.com/#pulumi/pulumi&Date"><img src="https://api.star-history.com/svg?repos=pulumi/pulumi&type=Date" width="260" alt="star history pulumi/pulumi"></a>

</details>

### Fastest rising this month (last 30 days)

| # | Project | Stars gained | Stars/day | Total stars |
|---|---|---:|---:|---:|
| 1 | [caddyserver/caddy](https://github.com/caddyserver/caddy)<br>Set up a web server with HTTPS configured for you<br>`Infrastructure` | +1,193 | 39.8 | 79,038 |
| 2 | [prometheus/prometheus](https://github.com/prometheus/prometheus)<br>When the system breaks, the alert finds you first<br>`Infrastructure` | +1,154 | 38.5 | 67,599 |
| 3 | [kubernetes/kubernetes](https://github.com/kubernetes/kubernetes)<br>Lots of containers? Leave deploying and scaling to it<br>`Infrastructure` | +1,098 | 36.6 | 129,056 |
| 4 | [grafana/grafana](https://github.com/grafana/grafana)<br>Metrics, logs and traces on one dashboard<br>`Infrastructure` | +763 | 25.4 | 77,898 |
| 5 | [docker/compose](https://github.com/docker/compose)<br>Put many containers in one file and run them together<br>`Infrastructure` | +537 | 17.9 | 38,833 |
| 6 | [traefik/traefik](https://github.com/traefik/traefik)<br>With many services, traffic gets sorted automatically<br>`Infrastructure` | +424 | 14.1 | 65,543 |
| 7 | [hashicorp/terraform](https://github.com/hashicorp/terraform)<br>Write cloud resources as code you can review and version<br>`Infrastructure` | +401 | 13.4 | 50,227 |
| 8 | [pulumi/pulumi](https://github.com/pulumi/pulumi)<br>Manage cloud resources in a language you already know<br>`Infrastructure` | +158 | 5.3 | 25,903 |

<details>
<summary>Star history charts for this board</summary>

<a href="https://www.star-history.com/#caddyserver/caddy&Date"><img src="https://api.star-history.com/svg?repos=caddyserver/caddy&type=Date" width="260" alt="star history caddyserver/caddy"></a>

<a href="https://www.star-history.com/#prometheus/prometheus&Date"><img src="https://api.star-history.com/svg?repos=prometheus/prometheus&type=Date" width="260" alt="star history prometheus/prometheus"></a>

<a href="https://www.star-history.com/#kubernetes/kubernetes&Date"><img src="https://api.star-history.com/svg?repos=kubernetes/kubernetes&type=Date" width="260" alt="star history kubernetes/kubernetes"></a>

<a href="https://www.star-history.com/#grafana/grafana&Date"><img src="https://api.star-history.com/svg?repos=grafana/grafana&type=Date" width="260" alt="star history grafana/grafana"></a>

<a href="https://www.star-history.com/#docker/compose&Date"><img src="https://api.star-history.com/svg?repos=docker/compose&type=Date" width="260" alt="star history docker/compose"></a>

<a href="https://www.star-history.com/#traefik/traefik&Date"><img src="https://api.star-history.com/svg?repos=traefik/traefik&type=Date" width="260" alt="star history traefik/traefik"></a>

<a href="https://www.star-history.com/#hashicorp/terraform&Date"><img src="https://api.star-history.com/svg?repos=hashicorp/terraform&type=Date" width="260" alt="star history hashicorp/terraform"></a>

<a href="https://www.star-history.com/#pulumi/pulumi&Date"><img src="https://api.star-history.com/svg?repos=pulumi/pulumi&type=Date" width="260" alt="star history pulumi/pulumi"></a>

</details>

### Fastest rising this year (last 365 days)

| # | Project | Stars gained | Stars/day | Total stars |
|---|---|---:|---:|---:|
| 1 | [caddyserver/caddy](https://github.com/caddyserver/caddy)<br>Set up a web server with HTTPS configured for you<br>`Infrastructure` | +12,076 | 33.1 | 79,038 |
| 2 | [kubernetes/kubernetes](https://github.com/kubernetes/kubernetes)<br>Lots of containers? Leave deploying and scaling to it<br>`Infrastructure` | +11,804 | 32.3 | 129,056 |
| 3 | [traefik/traefik](https://github.com/traefik/traefik)<br>With many services, traffic gets sorted automatically<br>`Infrastructure` | +8,300 | 22.7 | 65,543 |
| 4 | [grafana/grafana](https://github.com/grafana/grafana)<br>Metrics, logs and traces on one dashboard<br>`Infrastructure` | +7,969 | 21.8 | 77,898 |
| 5 | [prometheus/prometheus](https://github.com/prometheus/prometheus)<br>When the system breaks, the alert finds you first<br>`Infrastructure` | +7,031 | 19.3 | 67,599 |
| 6 | [hashicorp/terraform](https://github.com/hashicorp/terraform)<br>Write cloud resources as code you can review and version<br>`Infrastructure` | +3,808 | 10.4 | 50,227 |
| 7 | [docker/compose](https://github.com/docker/compose)<br>Put many containers in one file and run them together<br>`Infrastructure` | +2,822 | 7.7 | 38,833 |
| 8 | [pulumi/pulumi](https://github.com/pulumi/pulumi)<br>Manage cloud resources in a language you already know<br>`Infrastructure` | +2,110 | 5.8 | 25,903 |

<details>
<summary>Star history charts for this board</summary>

<a href="https://www.star-history.com/#caddyserver/caddy&Date"><img src="https://api.star-history.com/svg?repos=caddyserver/caddy&type=Date" width="260" alt="star history caddyserver/caddy"></a>

<a href="https://www.star-history.com/#kubernetes/kubernetes&Date"><img src="https://api.star-history.com/svg?repos=kubernetes/kubernetes&type=Date" width="260" alt="star history kubernetes/kubernetes"></a>

<a href="https://www.star-history.com/#traefik/traefik&Date"><img src="https://api.star-history.com/svg?repos=traefik/traefik&type=Date" width="260" alt="star history traefik/traefik"></a>

<a href="https://www.star-history.com/#grafana/grafana&Date"><img src="https://api.star-history.com/svg?repos=grafana/grafana&type=Date" width="260" alt="star history grafana/grafana"></a>

<a href="https://www.star-history.com/#prometheus/prometheus&Date"><img src="https://api.star-history.com/svg?repos=prometheus/prometheus&type=Date" width="260" alt="star history prometheus/prometheus"></a>

<a href="https://www.star-history.com/#hashicorp/terraform&Date"><img src="https://api.star-history.com/svg?repos=hashicorp/terraform&type=Date" width="260" alt="star history hashicorp/terraform"></a>

<a href="https://www.star-history.com/#docker/compose&Date"><img src="https://api.star-history.com/svg?repos=docker/compose&type=Date" width="260" alt="star history docker/compose"></a>

<a href="https://www.star-history.com/#pulumi/pulumi&Date"><img src="https://api.star-history.com/svg?repos=pulumi/pulumi&type=Date" width="260" alt="star history pulumi/pulumi"></a>

</details>

### Total stars (all time)

| # | Project | Total stars |
|---|---|---:|
| 1 | [kubernetes/kubernetes](https://github.com/kubernetes/kubernetes)<br>Lots of containers? Leave deploying and scaling to it<br>`Infrastructure` | 129,056 |
| 2 | [caddyserver/caddy](https://github.com/caddyserver/caddy)<br>Set up a web server with HTTPS configured for you<br>`Infrastructure` | 79,038 |
| 3 | [grafana/grafana](https://github.com/grafana/grafana)<br>Metrics, logs and traces on one dashboard<br>`Infrastructure` | 77,898 |
| 4 | [prometheus/prometheus](https://github.com/prometheus/prometheus)<br>When the system breaks, the alert finds you first<br>`Infrastructure` | 67,599 |
| 5 | [traefik/traefik](https://github.com/traefik/traefik)<br>With many services, traffic gets sorted automatically<br>`Infrastructure` | 65,543 |
| 6 | [hashicorp/terraform](https://github.com/hashicorp/terraform)<br>Write cloud resources as code you can review and version<br>`Infrastructure` | 50,227 |
| 7 | [docker/compose](https://github.com/docker/compose)<br>Put many containers in one file and run them together<br>`Infrastructure` | 38,833 |
| 8 | [pulumi/pulumi](https://github.com/pulumi/pulumi)<br>Manage cloud resources in a language you already know<br>`Infrastructure` | 25,903 |

<details>
<summary>Star history charts for this board</summary>

<a href="https://www.star-history.com/#kubernetes/kubernetes&Date"><img src="https://api.star-history.com/svg?repos=kubernetes/kubernetes&type=Date" width="260" alt="star history kubernetes/kubernetes"></a>

<a href="https://www.star-history.com/#caddyserver/caddy&Date"><img src="https://api.star-history.com/svg?repos=caddyserver/caddy&type=Date" width="260" alt="star history caddyserver/caddy"></a>

<a href="https://www.star-history.com/#grafana/grafana&Date"><img src="https://api.star-history.com/svg?repos=grafana/grafana&type=Date" width="260" alt="star history grafana/grafana"></a>

<a href="https://www.star-history.com/#prometheus/prometheus&Date"><img src="https://api.star-history.com/svg?repos=prometheus/prometheus&type=Date" width="260" alt="star history prometheus/prometheus"></a>

<a href="https://www.star-history.com/#traefik/traefik&Date"><img src="https://api.star-history.com/svg?repos=traefik/traefik&type=Date" width="260" alt="star history traefik/traefik"></a>

<a href="https://www.star-history.com/#hashicorp/terraform&Date"><img src="https://api.star-history.com/svg?repos=hashicorp/terraform&type=Date" width="260" alt="star history hashicorp/terraform"></a>

<a href="https://www.star-history.com/#docker/compose&Date"><img src="https://api.star-history.com/svg?repos=docker/compose&type=Date" width="260" alt="star history docker/compose"></a>

<a href="https://www.star-history.com/#pulumi/pulumi&Date"><img src="https://api.star-history.com/svg?repos=pulumi/pulumi&type=Date" width="260" alt="star history pulumi/pulumi"></a>

</details>

## Design / Creative

> Design systems, drawing, animation and creative tooling

### Hottest new repos (created in the last 7 days)

| # | Project | Created (UTC) | Total stars | Stars/day |
|---|---|---|---:|---:|
| 1 | [lobehub/lobe-mygo](https://github.com/lobehub/lobe-mygo)<br>Build native Go UIs drawn on the GPU in pure Go | 2026-11-08<br><sub>6.1 d</sub> | 245 | 40.4 |

<details>
<summary>Star history charts for this board</summary>

<a href="https://www.star-history.com/#lobehub/lobe-mygo&Date"><img src="https://api.star-history.com/svg?repos=lobehub/lobe-mygo&type=Date" width="260" alt="star history lobehub/lobe-mygo"></a>

</details>

### Fastest rising this week (last 7 days)

| # | Project | Stars gained | Stars/day | Total stars |
|---|---|---:|---:|---:|
| 1 | [excalidraw/excalidraw](https://github.com/excalidraw/excalidraw)<br>Open it and draw, like sketching on paper<br>`Design / Creative` | +451 | 64.4 | 135,672 |
| 2 | [penpot/penpot](https://github.com/penpot/penpot)<br>Design together as a team, on an open-source platform<br>`Design / Creative` | +230 | 32.9 | 62,345 |
| 3 | [lucide-icons/lucide](https://github.com/lucide-icons/lucide)<br>One icon set in one style, ready to use<br>`Design / Creative` | +154 | 22.0 | 25,755 |
| 4 | [jgraph/drawio](https://github.com/jgraph/drawio)<br>Diagrams and a whiteboard in one editor<br>`Design / Creative` | +134 | 19.1 | 9,362 |
| 5 | [saadeghi/daisyui](https://github.com/saadeghi/daisyui)<br>Pick ready-made components for Tailwind CSS<br>`Design / Creative` | +90 | 12.9 | 42,837 |
| 6 | [airbnb/lottie-web](https://github.com/airbnb/lottie-web)<br>Drop After Effects animations straight into web pages<br>`Design / Creative` | +45 | 6.4 | 32,411 |
| 7 | [phosphor-icons/homepage](https://github.com/phosphor-icons/homepage)<br>A flexible icon family for everyone<br>`Design / Creative` | +36 | 5.1 | 7,809 |
| 8 | [lottiefiles/lottie-ios](https://github.com/lottiefiles/lottie-ios)<br>Drop After Effects animations straight into iOS<br>`Design / Creative` | +0 | 0.0 | 43 |

<details>
<summary>Star history charts for this board</summary>

<a href="https://www.star-history.com/#excalidraw/excalidraw&Date"><img src="https://api.star-history.com/svg?repos=excalidraw/excalidraw&type=Date" width="260" alt="star history excalidraw/excalidraw"></a>

<a href="https://www.star-history.com/#penpot/penpot&Date"><img src="https://api.star-history.com/svg?repos=penpot/penpot&type=Date" width="260" alt="star history penpot/penpot"></a>

<a href="https://www.star-history.com/#lucide-icons/lucide&Date"><img src="https://api.star-history.com/svg?repos=lucide-icons/lucide&type=Date" width="260" alt="star history lucide-icons/lucide"></a>

<a href="https://www.star-history.com/#jgraph/drawio&Date"><img src="https://api.star-history.com/svg?repos=jgraph/drawio&type=Date" width="260" alt="star history jgraph/drawio"></a>

<a href="https://www.star-history.com/#saadeghi/daisyui&Date"><img src="https://api.star-history.com/svg?repos=saadeghi/daisyui&type=Date" width="260" alt="star history saadeghi/daisyui"></a>

<a href="https://www.star-history.com/#airbnb/lottie-web&Date"><img src="https://api.star-history.com/svg?repos=airbnb/lottie-web&type=Date" width="260" alt="star history airbnb/lottie-web"></a>

<a href="https://www.star-history.com/#phosphor-icons/homepage&Date"><img src="https://api.star-history.com/svg?repos=phosphor-icons/homepage&type=Date" width="260" alt="star history phosphor-icons/homepage"></a>

<a href="https://www.star-history.com/#lottiefiles/lottie-ios&Date"><img src="https://api.star-history.com/svg?repos=lottiefiles/lottie-ios&type=Date" width="260" alt="star history lottiefiles/lottie-ios"></a>

</details>

### Fastest rising this month (last 30 days)

| # | Project | Stars gained | Stars/day | Total stars |
|---|---|---:|---:|---:|
| 1 | [excalidraw/excalidraw](https://github.com/excalidraw/excalidraw)<br>Open it and draw, like sketching on paper<br>`Design / Creative` | +1,987 | 66.2 | 135,672 |
| 2 | [penpot/penpot](https://github.com/penpot/penpot)<br>Design together as a team, on an open-source platform<br>`Design / Creative` | +1,401 | 46.7 | 62,345 |
| 3 | [lucide-icons/lucide](https://github.com/lucide-icons/lucide)<br>One icon set in one style, ready to use<br>`Design / Creative` | +777 | 25.9 | 25,755 |
| 4 | [jgraph/drawio](https://github.com/jgraph/drawio)<br>Diagrams and a whiteboard in one editor<br>`Design / Creative` | +609 | 20.3 | 9,362 |
| 5 | [saadeghi/daisyui](https://github.com/saadeghi/daisyui)<br>Pick ready-made components for Tailwind CSS<br>`Design / Creative` | +316 | 10.5 | 42,837 |
| 6 | [airbnb/lottie-web](https://github.com/airbnb/lottie-web)<br>Drop After Effects animations straight into web pages<br>`Design / Creative` | +209 | 7.0 | 32,411 |
| 7 | [phosphor-icons/homepage](https://github.com/phosphor-icons/homepage)<br>A flexible icon family for everyone<br>`Design / Creative` | +166 | 5.5 | 7,809 |
| 8 | [lottiefiles/lottie-ios](https://github.com/lottiefiles/lottie-ios)<br>Drop After Effects animations straight into iOS<br>`Design / Creative` | +0 | 0.0 | 43 |

<details>
<summary>Star history charts for this board</summary>

<a href="https://www.star-history.com/#excalidraw/excalidraw&Date"><img src="https://api.star-history.com/svg?repos=excalidraw/excalidraw&type=Date" width="260" alt="star history excalidraw/excalidraw"></a>

<a href="https://www.star-history.com/#penpot/penpot&Date"><img src="https://api.star-history.com/svg?repos=penpot/penpot&type=Date" width="260" alt="star history penpot/penpot"></a>

<a href="https://www.star-history.com/#lucide-icons/lucide&Date"><img src="https://api.star-history.com/svg?repos=lucide-icons/lucide&type=Date" width="260" alt="star history lucide-icons/lucide"></a>

<a href="https://www.star-history.com/#jgraph/drawio&Date"><img src="https://api.star-history.com/svg?repos=jgraph/drawio&type=Date" width="260" alt="star history jgraph/drawio"></a>

<a href="https://www.star-history.com/#saadeghi/daisyui&Date"><img src="https://api.star-history.com/svg?repos=saadeghi/daisyui&type=Date" width="260" alt="star history saadeghi/daisyui"></a>

<a href="https://www.star-history.com/#airbnb/lottie-web&Date"><img src="https://api.star-history.com/svg?repos=airbnb/lottie-web&type=Date" width="260" alt="star history airbnb/lottie-web"></a>

<a href="https://www.star-history.com/#phosphor-icons/homepage&Date"><img src="https://api.star-history.com/svg?repos=phosphor-icons/homepage&type=Date" width="260" alt="star history phosphor-icons/homepage"></a>

<a href="https://www.star-history.com/#lottiefiles/lottie-ios&Date"><img src="https://api.star-history.com/svg?repos=lottiefiles/lottie-ios&type=Date" width="260" alt="star history lottiefiles/lottie-ios"></a>

</details>

### Fastest rising this year (last 365 days)

| # | Project | Stars gained | Stars/day | Total stars |
|---|---|---:|---:|---:|
| 1 | [excalidraw/excalidraw](https://github.com/excalidraw/excalidraw)<br>Open it and draw, like sketching on paper<br>`Design / Creative` | +26,949 | 73.8 | 135,672 |
| 2 | [penpot/penpot](https://github.com/penpot/penpot)<br>Design together as a team, on an open-source platform<br>`Design / Creative` | +21,621 | 59.2 | 62,345 |
| 3 | [jgraph/drawio](https://github.com/jgraph/drawio)<br>Diagrams and a whiteboard in one editor<br>`Design / Creative` | +6,624 | 18.1 | 9,362 |
| 4 | [lucide-icons/lucide](https://github.com/lucide-icons/lucide)<br>One icon set in one style, ready to use<br>`Design / Creative` | +6,382 | 17.5 | 25,755 |
| 5 | [saadeghi/daisyui](https://github.com/saadeghi/daisyui)<br>Pick ready-made components for Tailwind CSS<br>`Design / Creative` | +4,226 | 11.6 | 42,837 |
| 6 | [phosphor-icons/homepage](https://github.com/phosphor-icons/homepage)<br>A flexible icon family for everyone<br>`Design / Creative` | +2,209 | 6.1 | 7,809 |
| 7 | [airbnb/lottie-web](https://github.com/airbnb/lottie-web)<br>Drop After Effects animations straight into web pages<br>`Design / Creative` | +1,152 | 3.2 | 32,411 |
| 8 | [lottiefiles/lottie-ios](https://github.com/lottiefiles/lottie-ios)<br>Drop After Effects animations straight into iOS<br>`Design / Creative` | +1 | 0.0 | 43 |

<details>
<summary>Star history charts for this board</summary>

<a href="https://www.star-history.com/#excalidraw/excalidraw&Date"><img src="https://api.star-history.com/svg?repos=excalidraw/excalidraw&type=Date" width="260" alt="star history excalidraw/excalidraw"></a>

<a href="https://www.star-history.com/#penpot/penpot&Date"><img src="https://api.star-history.com/svg?repos=penpot/penpot&type=Date" width="260" alt="star history penpot/penpot"></a>

<a href="https://www.star-history.com/#jgraph/drawio&Date"><img src="https://api.star-history.com/svg?repos=jgraph/drawio&type=Date" width="260" alt="star history jgraph/drawio"></a>

<a href="https://www.star-history.com/#lucide-icons/lucide&Date"><img src="https://api.star-history.com/svg?repos=lucide-icons/lucide&type=Date" width="260" alt="star history lucide-icons/lucide"></a>

<a href="https://www.star-history.com/#saadeghi/daisyui&Date"><img src="https://api.star-history.com/svg?repos=saadeghi/daisyui&type=Date" width="260" alt="star history saadeghi/daisyui"></a>

<a href="https://www.star-history.com/#phosphor-icons/homepage&Date"><img src="https://api.star-history.com/svg?repos=phosphor-icons/homepage&type=Date" width="260" alt="star history phosphor-icons/homepage"></a>

<a href="https://www.star-history.com/#airbnb/lottie-web&Date"><img src="https://api.star-history.com/svg?repos=airbnb/lottie-web&type=Date" width="260" alt="star history airbnb/lottie-web"></a>

<a href="https://www.star-history.com/#lottiefiles/lottie-ios&Date"><img src="https://api.star-history.com/svg?repos=lottiefiles/lottie-ios&type=Date" width="260" alt="star history lottiefiles/lottie-ios"></a>

</details>

### Total stars (all time)

| # | Project | Total stars |
|---|---|---:|
| 1 | [excalidraw/excalidraw](https://github.com/excalidraw/excalidraw)<br>Open it and draw, like sketching on paper<br>`Design / Creative` | 135,672 |
| 2 | [penpot/penpot](https://github.com/penpot/penpot)<br>Design together as a team, on an open-source platform<br>`Design / Creative` | 62,345 |
| 3 | [saadeghi/daisyui](https://github.com/saadeghi/daisyui)<br>Pick ready-made components for Tailwind CSS<br>`Design / Creative` | 42,837 |
| 4 | [airbnb/lottie-web](https://github.com/airbnb/lottie-web)<br>Drop After Effects animations straight into web pages<br>`Design / Creative` | 32,411 |
| 5 | [lucide-icons/lucide](https://github.com/lucide-icons/lucide)<br>One icon set in one style, ready to use<br>`Design / Creative` | 25,755 |
| 6 | [jgraph/drawio](https://github.com/jgraph/drawio)<br>Diagrams and a whiteboard in one editor<br>`Design / Creative` | 9,362 |
| 7 | [phosphor-icons/homepage](https://github.com/phosphor-icons/homepage)<br>A flexible icon family for everyone<br>`Design / Creative` | 7,809 |
| 8 | [lottiefiles/lottie-ios](https://github.com/lottiefiles/lottie-ios)<br>Drop After Effects animations straight into iOS<br>`Design / Creative` | 43 |

<details>
<summary>Star history charts for this board</summary>

<a href="https://www.star-history.com/#excalidraw/excalidraw&Date"><img src="https://api.star-history.com/svg?repos=excalidraw/excalidraw&type=Date" width="260" alt="star history excalidraw/excalidraw"></a>

<a href="https://www.star-history.com/#penpot/penpot&Date"><img src="https://api.star-history.com/svg?repos=penpot/penpot&type=Date" width="260" alt="star history penpot/penpot"></a>

<a href="https://www.star-history.com/#saadeghi/daisyui&Date"><img src="https://api.star-history.com/svg?repos=saadeghi/daisyui&type=Date" width="260" alt="star history saadeghi/daisyui"></a>

<a href="https://www.star-history.com/#airbnb/lottie-web&Date"><img src="https://api.star-history.com/svg?repos=airbnb/lottie-web&type=Date" width="260" alt="star history airbnb/lottie-web"></a>

<a href="https://www.star-history.com/#lucide-icons/lucide&Date"><img src="https://api.star-history.com/svg?repos=lucide-icons/lucide&type=Date" width="260" alt="star history lucide-icons/lucide"></a>

<a href="https://www.star-history.com/#jgraph/drawio&Date"><img src="https://api.star-history.com/svg?repos=jgraph/drawio&type=Date" width="260" alt="star history jgraph/drawio"></a>

<a href="https://www.star-history.com/#phosphor-icons/homepage&Date"><img src="https://api.star-history.com/svg?repos=phosphor-icons/homepage&type=Date" width="260" alt="star history phosphor-icons/homepage"></a>

<a href="https://www.star-history.com/#lottiefiles/lottie-ios&Date"><img src="https://api.star-history.com/svg?repos=lottiefiles/lottie-ios&type=Date" width="260" alt="star history lottiefiles/lottie-ios"></a>

</details>

## Data

> Databases, analytics, ETL and data engineering

### Hottest new repos (created in the last 7 days)

No new repo met the criteria in this run.

### Fastest rising this week (last 7 days)

| # | Project | Stars gained | Stars/day | Total stars |
|---|---|---:|---:|---:|
| 1 | [duckdb/duckdb](https://github.com/duckdb/duckdb)<br>Run SQL analysis without setting up a database server<br>`Data` | +197 | 28.1 | 43,059 |
| 2 | [ClickHouse/ClickHouse](https://github.com/ClickHouse/ClickHouse)<br>Real-time analysis of huge data, with open source<br>`Data` | +138 | 19.7 | 50,923 |
| 3 | [apache/superset](https://github.com/apache/superset)<br>Can't make sense of the data? Turn it into charts<br>`Data` | +99 | 14.1 | 75,523 |
| 4 | [pola-rs/polars](https://github.com/pola-rs/polars)<br>Table data handled fast, no more waiting<br>`Data` | +76 | 10.9 | 40,339 |
| 5 | [apache/kafka](https://github.com/apache/kafka)<br>Stream events between systems on one distributed platform<br>`Data` | +42 | 6.0 | 34,219 |
| 6 | [dbt-labs/dbt-core](https://github.com/dbt-labs/dbt-core)<br>Transform data the way software engineers build apps<br>`Data` | +42 | 6.0 | 14,171 |
| 7 | [apache/arrow](https://github.com/apache/arrow)<br>Across languages, the data works as it is<br>`Data` | +17 | 2.4 | 17,294 |
| 8 | [jupyter/notebook](https://github.com/jupyter/notebook)<br>Write code in the browser and see results as you go<br>`Data` | +7 | 1.0 | 13,468 |

<details>
<summary>Star history charts for this board</summary>

<a href="https://www.star-history.com/#duckdb/duckdb&Date"><img src="https://api.star-history.com/svg?repos=duckdb/duckdb&type=Date" width="260" alt="star history duckdb/duckdb"></a>

<a href="https://www.star-history.com/#ClickHouse/ClickHouse&Date"><img src="https://api.star-history.com/svg?repos=ClickHouse/ClickHouse&type=Date" width="260" alt="star history ClickHouse/ClickHouse"></a>

<a href="https://www.star-history.com/#apache/superset&Date"><img src="https://api.star-history.com/svg?repos=apache/superset&type=Date" width="260" alt="star history apache/superset"></a>

<a href="https://www.star-history.com/#pola-rs/polars&Date"><img src="https://api.star-history.com/svg?repos=pola-rs/polars&type=Date" width="260" alt="star history pola-rs/polars"></a>

<a href="https://www.star-history.com/#apache/kafka&Date"><img src="https://api.star-history.com/svg?repos=apache/kafka&type=Date" width="260" alt="star history apache/kafka"></a>

<a href="https://www.star-history.com/#dbt-labs/dbt-core&Date"><img src="https://api.star-history.com/svg?repos=dbt-labs/dbt-core&type=Date" width="260" alt="star history dbt-labs/dbt-core"></a>

<a href="https://www.star-history.com/#apache/arrow&Date"><img src="https://api.star-history.com/svg?repos=apache/arrow&type=Date" width="260" alt="star history apache/arrow"></a>

<a href="https://www.star-history.com/#jupyter/notebook&Date"><img src="https://api.star-history.com/svg?repos=jupyter/notebook&type=Date" width="260" alt="star history jupyter/notebook"></a>

</details>

### Fastest rising this month (last 30 days)

| # | Project | Stars gained | Stars/day | Total stars |
|---|---|---:|---:|---:|
| 1 | [duckdb/duckdb](https://github.com/duckdb/duckdb)<br>Run SQL analysis without setting up a database server<br>`Data` | +959 | 32.0 | 43,059 |
| 2 | [ClickHouse/ClickHouse](https://github.com/ClickHouse/ClickHouse)<br>Real-time analysis of huge data, with open source<br>`Data` | +576 | 19.2 | 50,923 |
| 3 | [apache/superset](https://github.com/apache/superset)<br>Can't make sense of the data? Turn it into charts<br>`Data` | +471 | 15.7 | 75,523 |
| 4 | [apache/kafka](https://github.com/apache/kafka)<br>Stream events between systems on one distributed platform<br>`Data` | +321 | 10.7 | 34,219 |
| 5 | [pola-rs/polars](https://github.com/pola-rs/polars)<br>Table data handled fast, no more waiting<br>`Data` | +301 | 10.0 | 40,339 |
| 6 | [dbt-labs/dbt-core](https://github.com/dbt-labs/dbt-core)<br>Transform data the way software engineers build apps<br>`Data` | +169 | 5.6 | 14,171 |
| 7 | [apache/arrow](https://github.com/apache/arrow)<br>Across languages, the data works as it is<br>`Data` | +101 | 3.4 | 17,294 |
| 8 | [jupyter/notebook](https://github.com/jupyter/notebook)<br>Write code in the browser and see results as you go<br>`Data` | +49 | 1.6 | 13,468 |

<details>
<summary>Star history charts for this board</summary>

<a href="https://www.star-history.com/#duckdb/duckdb&Date"><img src="https://api.star-history.com/svg?repos=duckdb/duckdb&type=Date" width="260" alt="star history duckdb/duckdb"></a>

<a href="https://www.star-history.com/#ClickHouse/ClickHouse&Date"><img src="https://api.star-history.com/svg?repos=ClickHouse/ClickHouse&type=Date" width="260" alt="star history ClickHouse/ClickHouse"></a>

<a href="https://www.star-history.com/#apache/superset&Date"><img src="https://api.star-history.com/svg?repos=apache/superset&type=Date" width="260" alt="star history apache/superset"></a>

<a href="https://www.star-history.com/#apache/kafka&Date"><img src="https://api.star-history.com/svg?repos=apache/kafka&type=Date" width="260" alt="star history apache/kafka"></a>

<a href="https://www.star-history.com/#pola-rs/polars&Date"><img src="https://api.star-history.com/svg?repos=pola-rs/polars&type=Date" width="260" alt="star history pola-rs/polars"></a>

<a href="https://www.star-history.com/#dbt-labs/dbt-core&Date"><img src="https://api.star-history.com/svg?repos=dbt-labs/dbt-core&type=Date" width="260" alt="star history dbt-labs/dbt-core"></a>

<a href="https://www.star-history.com/#apache/arrow&Date"><img src="https://api.star-history.com/svg?repos=apache/arrow&type=Date" width="260" alt="star history apache/arrow"></a>

<a href="https://www.star-history.com/#jupyter/notebook&Date"><img src="https://api.star-history.com/svg?repos=jupyter/notebook&type=Date" width="260" alt="star history jupyter/notebook"></a>

</details>

### Fastest rising this year (last 365 days)

| # | Project | Stars gained | Stars/day | Total stars |
|---|---|---:|---:|---:|
| 1 | [duckdb/duckdb](https://github.com/duckdb/duckdb)<br>Run SQL analysis without setting up a database server<br>`Data` | +9,438 | 25.9 | 43,059 |
| 2 | [ClickHouse/ClickHouse](https://github.com/ClickHouse/ClickHouse)<br>Real-time analysis of huge data, with open source<br>`Data` | +7,576 | 20.8 | 50,923 |
| 3 | [apache/superset](https://github.com/apache/superset)<br>Can't make sense of the data? Turn it into charts<br>`Data` | +7,380 | 20.2 | 75,523 |
| 4 | [pola-rs/polars](https://github.com/pola-rs/polars)<br>Table data handled fast, no more waiting<br>`Data` | +4,800 | 13.2 | 40,339 |
| 5 | [apache/kafka](https://github.com/apache/kafka)<br>Stream events between systems on one distributed platform<br>`Data` | +3,320 | 9.1 | 34,219 |
| 6 | [dbt-labs/dbt-core](https://github.com/dbt-labs/dbt-core)<br>Transform data the way software engineers build apps<br>`Data` | +2,473 | 6.8 | 14,171 |
| 7 | [apache/arrow](https://github.com/apache/arrow)<br>Across languages, the data works as it is<br>`Data` | +1,301 | 3.6 | 17,294 |
| 8 | [jupyter/notebook](https://github.com/jupyter/notebook)<br>Write code in the browser and see results as you go<br>`Data` | +878 | 2.4 | 13,468 |

<details>
<summary>Star history charts for this board</summary>

<a href="https://www.star-history.com/#duckdb/duckdb&Date"><img src="https://api.star-history.com/svg?repos=duckdb/duckdb&type=Date" width="260" alt="star history duckdb/duckdb"></a>

<a href="https://www.star-history.com/#ClickHouse/ClickHouse&Date"><img src="https://api.star-history.com/svg?repos=ClickHouse/ClickHouse&type=Date" width="260" alt="star history ClickHouse/ClickHouse"></a>

<a href="https://www.star-history.com/#apache/superset&Date"><img src="https://api.star-history.com/svg?repos=apache/superset&type=Date" width="260" alt="star history apache/superset"></a>

<a href="https://www.star-history.com/#pola-rs/polars&Date"><img src="https://api.star-history.com/svg?repos=pola-rs/polars&type=Date" width="260" alt="star history pola-rs/polars"></a>

<a href="https://www.star-history.com/#apache/kafka&Date"><img src="https://api.star-history.com/svg?repos=apache/kafka&type=Date" width="260" alt="star history apache/kafka"></a>

<a href="https://www.star-history.com/#dbt-labs/dbt-core&Date"><img src="https://api.star-history.com/svg?repos=dbt-labs/dbt-core&type=Date" width="260" alt="star history dbt-labs/dbt-core"></a>

<a href="https://www.star-history.com/#apache/arrow&Date"><img src="https://api.star-history.com/svg?repos=apache/arrow&type=Date" width="260" alt="star history apache/arrow"></a>

<a href="https://www.star-history.com/#jupyter/notebook&Date"><img src="https://api.star-history.com/svg?repos=jupyter/notebook&type=Date" width="260" alt="star history jupyter/notebook"></a>

</details>

### Total stars (all time)

| # | Project | Total stars |
|---|---|---:|
| 1 | [apache/superset](https://github.com/apache/superset)<br>Can't make sense of the data? Turn it into charts<br>`Data` | 75,523 |
| 2 | [ClickHouse/ClickHouse](https://github.com/ClickHouse/ClickHouse)<br>Real-time analysis of huge data, with open source<br>`Data` | 50,923 |
| 3 | [duckdb/duckdb](https://github.com/duckdb/duckdb)<br>Run SQL analysis without setting up a database server<br>`Data` | 43,059 |
| 4 | [pola-rs/polars](https://github.com/pola-rs/polars)<br>Table data handled fast, no more waiting<br>`Data` | 40,339 |
| 5 | [apache/kafka](https://github.com/apache/kafka)<br>Stream events between systems on one distributed platform<br>`Data` | 34,219 |
| 6 | [apache/arrow](https://github.com/apache/arrow)<br>Across languages, the data works as it is<br>`Data` | 17,294 |
| 7 | [dbt-labs/dbt-core](https://github.com/dbt-labs/dbt-core)<br>Transform data the way software engineers build apps<br>`Data` | 14,171 |
| 8 | [jupyter/notebook](https://github.com/jupyter/notebook)<br>Write code in the browser and see results as you go<br>`Data` | 13,468 |

<details>
<summary>Star history charts for this board</summary>

<a href="https://www.star-history.com/#apache/superset&Date"><img src="https://api.star-history.com/svg?repos=apache/superset&type=Date" width="260" alt="star history apache/superset"></a>

<a href="https://www.star-history.com/#ClickHouse/ClickHouse&Date"><img src="https://api.star-history.com/svg?repos=ClickHouse/ClickHouse&type=Date" width="260" alt="star history ClickHouse/ClickHouse"></a>

<a href="https://www.star-history.com/#duckdb/duckdb&Date"><img src="https://api.star-history.com/svg?repos=duckdb/duckdb&type=Date" width="260" alt="star history duckdb/duckdb"></a>

<a href="https://www.star-history.com/#pola-rs/polars&Date"><img src="https://api.star-history.com/svg?repos=pola-rs/polars&type=Date" width="260" alt="star history pola-rs/polars"></a>

<a href="https://www.star-history.com/#apache/kafka&Date"><img src="https://api.star-history.com/svg?repos=apache/kafka&type=Date" width="260" alt="star history apache/kafka"></a>

<a href="https://www.star-history.com/#apache/arrow&Date"><img src="https://api.star-history.com/svg?repos=apache/arrow&type=Date" width="260" alt="star history apache/arrow"></a>

<a href="https://www.star-history.com/#dbt-labs/dbt-core&Date"><img src="https://api.star-history.com/svg?repos=dbt-labs/dbt-core&type=Date" width="260" alt="star history dbt-labs/dbt-core"></a>

<a href="https://www.star-history.com/#jupyter/notebook&Date"><img src="https://api.star-history.com/svg?repos=jupyter/notebook&type=Date" width="260" alt="star history jupyter/notebook"></a>

</details>

---

If this saved you time, give the repo a star so others can find it.

How to cite: see [CITATION.cff](CITATION.cff).

How the numbers are produced and how to contribute: [docs/HOW_IT_WORKS.md](docs/HOW_IT_WORKS.md). New-repo rules: [docs/NEW_ARRIVALS.md](docs/NEW_ARRIVALS.md). Categories: [docs/CATEGORIES.md](docs/CATEGORIES.md). Pull requests: [CONTRIBUTING.md](CONTRIBUTING.md).
