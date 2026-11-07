[English](README.md) | **简体中文** | [繁體中文](README.zh-Hant.md) | [日本語](README.ja.md) | [한국어](README.ko.md)

# GitHub 涨星榜 / GitHub Risers

<img src=".github/social-preview.png" alt="GitHub 涨星榜 / GitHub Risers" width="640">

[![MIT](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE) [![CI](https://github.com/jammyfu/github-risers/actions/workflows/ci.yml/badge.svg)](https://github.com/jammyfu/github-risers/actions/workflows/ci.yml) [![updated](https://img.shields.io/badge/dynamic/json?url=https%3A%2F%2Fraw.githubusercontent.com%2Fjammyfu%2Fgithub-risers%2Fmain%2Fdata%2Fstats.json&query=%24.today_utc&label=updated&color=brightgreen)](latest/rankings.zh-Hans.md)

按每天新增星标（而不是总星标）给 GitHub 仓库排名：AI 在前，其后是开发者工具、安全、Web / 前端、基础设施、设计 / 创意和数据；每天更新。

数据取自 2026-11-07 12:46（UTC）。每天更新。

[网站](https://jammyfu.github.io/github-risers/) · [运作方式](docs/HOW_IT_WORKS.zh-Hans.md) · [事实速查](docs/FACTS.md) · [历史榜单](rankings/README.zh-Hans.md) · [最新快照](latest/rankings.zh-Hans.md)

## 本期各类榜首

| 分类 | 新仓库第 1 名（7 天） | 本周第 1 名 | 本月第 1 名 | 今年第 1 名 | 总星标第 1 名 |
|---|---|---|---|---|---|
| **[人工智能](#人工智能)** ★ 主榜 | [KKKKhazix/agent-autoloop](https://github.com/KKKKhazix/agent-autoloop)<br>923/天 | [morluto/rea](https://github.com/morluto/rea)<br>3,785/天 | [morluto/rea](https://github.com/morluto/rea)<br>14,058/天 | [deepseek-ai/deepseek-harness](https://github.com/deepseek-ai/deepseek-harness)<br>3,200/天 | [morluto/rea](https://github.com/morluto/rea)<br>439,541 ★ |
| **[开发者工具](#开发者工具)** | [govijr/terminal-mac](https://github.com/govijr/terminal-mac)<br>502/天 | [zed-industries/zed](https://github.com/zed-industries/zed)<br>217/天 | [zed-industries/zed](https://github.com/zed-industries/zed)<br>92.2/天 | [zed-industries/zed](https://github.com/zed-industries/zed)<br>73.2/天 | [oven-sh/bun](https://github.com/oven-sh/bun)<br>96,677 ★ |
| **[安全](#安全)** | [yorkeccak/globalhackmap](https://github.com/yorkeccak/globalhackmap)<br>23.5/天 | [aquasecurity/trivy](https://github.com/aquasecurity/trivy)<br>33.1/天 | [projectdiscovery/nuclei](https://github.com/projectdiscovery/nuclei)<br>30.6/天 | [aquasecurity/trivy](https://github.com/aquasecurity/trivy)<br>28.0/天 | [aquasecurity/trivy](https://github.com/aquasecurity/trivy)<br>39,090 ★ |
| **[Web / 前端](#web--前端)** | [AtomIllusionistDwell/watson-username-footprint-finder](https://github.com/AtomIllusionistDwell/watson-username-footprint-finder)<br>178/天 | [facebook/react](https://github.com/facebook/react)<br>91.1/天 | [shadcn-ui/ui](https://github.com/shadcn-ui/ui)<br>91.9/天 | [shadcn-ui/ui](https://github.com/shadcn-ui/ui)<br>83.2/天 | [facebook/react](https://github.com/facebook/react)<br>252,347 ★ |
| **[基础设施](#基础设施)** | [sksarvesh007/antiglaude](https://github.com/sksarvesh007/antiglaude)<br>34.5/天 | [prometheus/prometheus](https://github.com/prometheus/prometheus)<br>60.0/天 | [caddyserver/caddy](https://github.com/caddyserver/caddy)<br>50.3/天 | [caddyserver/caddy](https://github.com/caddyserver/caddy)<br>32.9/天 | [kubernetes/kubernetes](https://github.com/kubernetes/kubernetes)<br>128,884 ★ |
| **[设计 / 创意](#设计--创意)** | [kubai087/kubai-icons](https://github.com/kubai087/kubai-icons)<br>61.2/天 | [excalidraw/excalidraw](https://github.com/excalidraw/excalidraw)<br>64.9/天 | [excalidraw/excalidraw](https://github.com/excalidraw/excalidraw)<br>67.0/天 | [excalidraw/excalidraw](https://github.com/excalidraw/excalidraw)<br>74.0/天 | [excalidraw/excalidraw](https://github.com/excalidraw/excalidraw)<br>135,275 ★ |
| **[数据](#数据)** | 无 | [duckdb/duckdb](https://github.com/duckdb/duckdb)<br>29.6/天 | [duckdb/duckdb](https://github.com/duckdb/duckdb)<br>32.4/天 | [duckdb/duckdb](https://github.com/duckdb/duckdb)<br>25.7/天 | [apache/superset](https://github.com/apache/superset)<br>75,449 ★ |

这里每张榜只列前 10 名，完整的前 20 名见 [latest/rankings.zh-Hans.md](latest/rankings.zh-Hans.md)。

表里每个项目只留一句话；完整介绍（含工具名、技术细节）见 [docs/DETAILS.zh-Hans.md](docs/DETAILS.zh-Hans.md)。

## 常见问题

### GitHub 涨星榜是什么？

按每天新增星标、而不是总星标给 GitHub 仓库排名的榜单。AI 是主榜，后面还有六个分类；数据由脚本从 GitHub API 生成。 [了解更多](docs/FAQ.md#what-is-github-risers)

### 和 GitHub Trending 有什么不同？

GitHub Trending 是 GitHub 官方页面；GitHub 涨星榜是独立的开源项目，规则公开，有五种语言，并保存每次更新的历史。它与 GitHub 官方没有关联。 [了解更多](docs/FAQ.md#is-it-the-same-as-github-trending)

### 多久更新一次？

每天更新；每次运行都会存档。 [了解更多](docs/FAQ.md#how-often-is-it-updated)

### 数据怎么算？

取最近 7、30 或 365 个完整 UTC 日的新增星标，再除以天数。数字全部来自 GitHub API，没有手填或估算。 [了解更多](docs/FAQ.md#how-is-the-growth-rate-computed)

### 怎么看、怎么参与？

看下面的榜，完整前 20 名在 latest/。要收录项目，改 data/projects.json（五种语言）并发 pull request。 [了解更多](docs/FAQ.md#how-can-i-suggest-a-project-or-report-a-mistake)

## 人工智能

> 大模型、智能体、MCP、编程助手与生成式 AI

### 最热新仓库（近 7 天内创建）

| # | 项目 | 创建时间（UTC） | 总星标 | 星标/天 | 星标历史 |
|---|---|---|---:|---:|---|
| 1 | [KKKKhazix/agent-autoloop](https://github.com/KKKKhazix/agent-autoloop)<br>不用一直盯梢，智能体拿不准时才找你 | 2026-11-03<br><sub>4.2 天</sub> | 3,873 | 922.7 | <a href="https://www.star-history.com/#KKKKhazix/agent-autoloop&Date"><img src="https://api.star-history.com/svg?repos=KKKKhazix/agent-autoloop&type=Date" width="260" alt="KKKKhazix/agent-autoloop 的星标历史曲线"></a> |
| 2 | [voyager-so/vork](https://github.com/voyager-so/vork)<br>让智能体处理三维与视觉特效 | 2026-11-05<br><sub>1.6 天</sub> | 638 | 401.3 | <a href="https://www.star-history.com/#voyager-so/vork&Date"><img src="https://api.star-history.com/svg?repos=voyager-so/vork&type=Date" width="260" alt="voyager-so/vork 的星标历史曲线"></a> |
| 3 | [HerdBuilderEstimate/roblox-studio-mcp](https://github.com/HerdBuilderEstimate/roblox-studio-mcp)<br>让 AI 帮你编辑游戏脚本 | 2026-11-06<br><sub>1.3 天</sub> | 427 | 336.0 | <a href="https://www.star-history.com/#HerdBuilderEstimate/roblox-studio-mcp&Date"><img src="https://api.star-history.com/svg?repos=HerdBuilderEstimate/roblox-studio-mcp&type=Date" width="260" alt="HerdBuilderEstimate/roblox-studio-mcp 的星标历史曲线"></a> |
| 4 | [caru-ini/stack-diagram](https://github.com/caru-ini/stack-diagram)<br>一句话描述技术栈，自动生成架构图 | 2026-11-01<br><sub>6.3 天</sub> | 2,024 | 321.3 | <a href="https://www.star-history.com/#caru-ini/stack-diagram&Date"><img src="https://api.star-history.com/svg?repos=caru-ini/stack-diagram&type=Date" width="260" alt="caru-ini/stack-diagram 的星标历史曲线"></a> |
| 5 | [JosssphZhou/poki](https://github.com/JosssphZhou/poki)<br>让 AI 操作真实的 iPhone | 2026-11-05<br><sub>1.9 天</sub> | 453 | 237.9 | <a href="https://www.star-history.com/#JosssphZhou/poki&Date"><img src="https://api.star-history.com/svg?repos=JosssphZhou/poki&type=Date" width="260" alt="JosssphZhou/poki 的星标历史曲线"></a> |
| 6 | [Sandflow-ai/sand3d](https://github.com/Sandflow-ai/sand3d)<br>让大模型用 Python 做三维建模 | 2026-11-03<br><sub>4.2 天</sub> | 934 | 223.3 | <a href="https://www.star-history.com/#Sandflow-ai/sand3d&Date"><img src="https://api.star-history.com/svg?repos=Sandflow-ai/sand3d&type=Date" width="260" alt="Sandflow-ai/sand3d 的星标历史曲线"></a> |
| 7 | [yucezerey/turkish-anti-ai-skill](https://github.com/yucezerey/turkish-anti-ai-skill)<br>去掉土耳其语文章里的 AI 痕迹 | 2026-11-05<br><sub>1.7 天</sub> | 249 | 147.1 | <a href="https://www.star-history.com/#yucezerey/turkish-anti-ai-skill&Date"><img src="https://api.star-history.com/svg?repos=yucezerey/turkish-anti-ai-skill&type=Date" width="260" alt="yucezerey/turkish-anti-ai-skill 的星标历史曲线"></a> |
| 8 | [shanselman/sandbox-mcp](https://github.com/shanselman/sandbox-mcp)<br>用一次性 Windows 环境测试应用 | 2026-11-06<br><sub>1.0 天</sub> | 137 | 137.0 | <a href="https://www.star-history.com/#shanselman/sandbox-mcp&Date"><img src="https://api.star-history.com/svg?repos=shanselman/sandbox-mcp&type=Date" width="260" alt="shanselman/sandbox-mcp 的星标历史曲线"></a> |
| 9 | [dabingfy-dot/solo-to-team-skills](https://github.com/dabingfy-dot/solo-to-team-skills)<br>把任务分派给你的 AI 团队 | 2026-11-07<br><sub>1.0 天</sub> | 107 | 107.0 | <a href="https://www.star-history.com/#dabingfy-dot/solo-to-team-skills&Date"><img src="https://api.star-history.com/svg?repos=dabingfy-dot/solo-to-team-skills&type=Date" width="260" alt="dabingfy-dot/solo-to-team-skills 的星标历史曲线"></a> |
| 10 | [mhfed/vn-law-check](https://github.com/mhfed/vn-law-check)<br>检查网站是否符合越南法规要求 | 2026-11-02<br><sub>5.1 天</sub> | 466 | 90.6 | <a href="https://www.star-history.com/#mhfed/vn-law-check&Date"><img src="https://api.star-history.com/svg?repos=mhfed/vn-law-check&type=Date" width="260" alt="mhfed/vn-law-check 的星标历史曲线"></a> |

### 本周增长最快（近 7 天）

| # | 项目 | 新增星标 | 星标/天 | 总星标 | 星标历史 |
|---|---|---:|---:|---:|---|
| 1 | [morluto/rea](https://github.com/morluto/rea)<br>让 AI 帮你克隆任何软件<br>`人工智能` | +26,494 | 3,784.9 | 439,541 | <a href="https://www.star-history.com/#morluto/rea&Date"><img src="https://api.star-history.com/svg?repos=morluto/rea&type=Date" width="260" alt="morluto/rea 的星标历史曲线"></a> |
| 2 | [cloudflare/security-audit-skill](https://github.com/cloudflare/security-audit-skill)<br>AI 查代码漏洞，另一个 AI 逐条复核<br>`人工智能` | +10,230 | 1,461.4 | 64,844 | <a href="https://www.star-history.com/#cloudflare/security-audit-skill&Date"><img src="https://api.star-history.com/svg?repos=cloudflare/security-audit-skill&type=Date" width="260" alt="cloudflare/security-audit-skill 的星标历史曲线"></a> |
| 3 | [deepseek-ai/deepseek-harness](https://github.com/deepseek-ai/deepseek-harness)<br>想要什么智能体，用插件自己拼<br>`人工智能` | +8,653 | 1,236.1 | 275,423 | <a href="https://www.star-history.com/#deepseek-ai/deepseek-harness&Date"><img src="https://api.star-history.com/svg?repos=deepseek-ai/deepseek-harness&type=Date" width="260" alt="deepseek-ai/deepseek-harness 的星标历史曲线"></a> |
| 4 | [thedotmack/claude-mem](https://github.com/thedotmack/claude-mem)<br>AI 不再忘记上次做到哪<br>`人工智能` | +7,647 | 1,092.4 | 114,234 | <a href="https://www.star-history.com/#thedotmack/claude-mem&Date"><img src="https://api.star-history.com/svg?repos=thedotmack/claude-mem&type=Date" width="260" alt="thedotmack/claude-mem 的星标历史曲线"></a> |
| 5 | [stablyai/orca](https://github.com/stablyai/orca)<br>几个 AI 一起写，谁好用一眼看出<br>`人工智能` | +6,959 | 994.1 | 118,209 | <a href="https://www.star-history.com/#stablyai/orca&Date"><img src="https://api.star-history.com/svg?repos=stablyai/orca&type=Date" width="260" alt="stablyai/orca 的星标历史曲线"></a> |
| 6 | [affaan-m/ECC](https://github.com/affaan-m/ECC)<br>给编程 AI 加记忆、技能和安全检查<br>`人工智能` | +5,510 | 787.1 | 298,872 | <a href="https://www.star-history.com/#affaan-m/ECC&Date"><img src="https://api.star-history.com/svg?repos=affaan-m/ECC&type=Date" width="260" alt="affaan-m/ECC 的星标历史曲线"></a> |
| 7 | [DietrichGebert/ponytail](https://github.com/DietrichGebert/ponytail)<br>让 AI 少写废代码，该写的写对<br>`人工智能` | +5,125 | 732.1 | 186,120 | <a href="https://www.star-history.com/#DietrichGebert/ponytail&Date"><img src="https://api.star-history.com/svg?repos=DietrichGebert/ponytail&type=Date" width="260" alt="DietrichGebert/ponytail 的星标历史曲线"></a> |
| 8 | [yetone/magpie](https://github.com/yetone/magpie)<br>编程 AI 换模型，额度用完自动续<br>`人工智能` | +5,087 | 726.7 | 31,597 | <a href="https://www.star-history.com/#yetone/magpie&Date"><img src="https://api.star-history.com/svg?repos=yetone/magpie&type=Date" width="260" alt="yetone/magpie 的星标历史曲线"></a> |
| 9 | [Leonxlnx/taste-skill](https://github.com/Leonxlnx/taste-skill)<br>别再让 AI 做出千篇一律的页面<br>`人工智能` | +4,969 | 709.9 | 111,422 | <a href="https://www.star-history.com/#Leonxlnx/taste-skill&Date"><img src="https://api.star-history.com/svg?repos=Leonxlnx/taste-skill&type=Date" width="260" alt="Leonxlnx/taste-skill 的星标历史曲线"></a> |
| 10 | [Graphify-Labs/graphify](https://github.com/Graphify-Labs/graphify)<br>大项目看不过来，先看这张地图<br>`人工智能` | +4,212 | 601.7 | 143,765 | <a href="https://www.star-history.com/#Graphify-Labs/graphify&Date"><img src="https://api.star-history.com/svg?repos=Graphify-Labs/graphify&type=Date" width="260" alt="Graphify-Labs/graphify 的星标历史曲线"></a> |

### 本月增长最快（近 30 天）

| # | 项目 | 新增星标 | 星标/天 | 总星标 | 星标历史 |
|---|---|---:|---:|---:|---|
| 1 | [morluto/rea](https://github.com/morluto/rea)<br>让 AI 帮你克隆任何软件<br>`人工智能` | +421,747 | 14,058.2 | 439,541 | <a href="https://www.star-history.com/#morluto/rea&Date"><img src="https://api.star-history.com/svg?repos=morluto/rea&type=Date" width="260" alt="morluto/rea 的星标历史曲线"></a> |
| 2 | [cloudflare/security-audit-skill](https://github.com/cloudflare/security-audit-skill)<br>AI 查代码漏洞，另一个 AI 逐条复核<br>`人工智能` | +38,501 | 1,283.4 | 64,844 | <a href="https://www.star-history.com/#cloudflare/security-audit-skill&Date"><img src="https://api.star-history.com/svg?repos=cloudflare/security-audit-skill&type=Date" width="260" alt="cloudflare/security-audit-skill 的星标历史曲线"></a> |
| 3 | [stablyai/orca](https://github.com/stablyai/orca)<br>几个 AI 一起写，谁好用一眼看出<br>`人工智能` | +31,348 | 1,044.9 | 118,209 | <a href="https://www.star-history.com/#stablyai/orca&Date"><img src="https://api.star-history.com/svg?repos=stablyai/orca&type=Date" width="260" alt="stablyai/orca 的星标历史曲线"></a> |
| 4 | [deepseek-ai/deepseek-harness](https://github.com/deepseek-ai/deepseek-harness)<br>想要什么智能体，用插件自己拼<br>`人工智能` | +31,273 | 1,042.4 | 275,423 | <a href="https://www.star-history.com/#deepseek-ai/deepseek-harness&Date"><img src="https://api.star-history.com/svg?repos=deepseek-ai/deepseek-harness&type=Date" width="260" alt="deepseek-ai/deepseek-harness 的星标历史曲线"></a> |
| 5 | [DietrichGebert/ponytail](https://github.com/DietrichGebert/ponytail)<br>让 AI 少写废代码，该写的写对<br>`人工智能` | +29,248 | 974.9 | 186,120 | <a href="https://www.star-history.com/#DietrichGebert/ponytail&Date"><img src="https://api.star-history.com/svg?repos=DietrichGebert/ponytail&type=Date" width="260" alt="DietrichGebert/ponytail 的星标历史曲线"></a> |
| 6 | [yetone/magpie](https://github.com/yetone/magpie)<br>编程 AI 换模型，额度用完自动续<br>`人工智能` | +25,289 | 843.0 | 31,597 | <a href="https://www.star-history.com/#yetone/magpie&Date"><img src="https://api.star-history.com/svg?repos=yetone/magpie&type=Date" width="260" alt="yetone/magpie 的星标历史曲线"></a> |
| 7 | [affaan-m/ECC](https://github.com/affaan-m/ECC)<br>给编程 AI 加记忆、技能和安全检查<br>`人工智能` | +25,236 | 841.2 | 298,872 | <a href="https://www.star-history.com/#affaan-m/ECC&Date"><img src="https://api.star-history.com/svg?repos=affaan-m/ECC&type=Date" width="260" alt="affaan-m/ECC 的星标历史曲线"></a> |
| 8 | [heygen-com/hyperframes](https://github.com/heygen-com/hyperframes)<br>不会剪辑，写网页一样就能出片<br>`人工智能` | +21,836 | 727.9 | 80,322 | <a href="https://www.star-history.com/#heygen-com/hyperframes&Date"><img src="https://api.star-history.com/svg?repos=heygen-com/hyperframes&type=Date" width="260" alt="heygen-com/hyperframes 的星标历史曲线"></a> |
| 9 | [Graphify-Labs/graphify](https://github.com/Graphify-Labs/graphify)<br>大项目看不过来，先看这张地图<br>`人工智能` | +19,728 | 657.6 | 143,765 | <a href="https://www.star-history.com/#Graphify-Labs/graphify&Date"><img src="https://api.star-history.com/svg?repos=Graphify-Labs/graphify&type=Date" width="260" alt="Graphify-Labs/graphify 的星标历史曲线"></a> |
| 10 | [Leonxlnx/taste-skill](https://github.com/Leonxlnx/taste-skill)<br>别再让 AI 做出千篇一律的页面<br>`人工智能` | +18,258 | 608.6 | 111,422 | <a href="https://www.star-history.com/#Leonxlnx/taste-skill&Date"><img src="https://api.star-history.com/svg?repos=Leonxlnx/taste-skill&type=Date" width="260" alt="Leonxlnx/taste-skill 的星标历史曲线"></a> |

### 今年增长最快（近 365 天）

| # | 项目 | 新增星标 | 星标/天 | 总星标 | 星标历史 |
|---|---|---:|---:|---:|---|
| 1 | [deepseek-ai/deepseek-harness](https://github.com/deepseek-ai/deepseek-harness)<br>想要什么智能体，用插件自己拼<br>`人工智能` | +275,200 | 3,200.0 †<br><sub>÷86 天</sub> | 275,423 | <a href="https://www.star-history.com/#deepseek-ai/deepseek-harness&Date"><img src="https://api.star-history.com/svg?repos=deepseek-ai/deepseek-harness&type=Date" width="260" alt="deepseek-ai/deepseek-harness 的星标历史曲线"></a> |
| 2 | [morluto/rea](https://github.com/morluto/rea)<br>让 AI 帮你克隆任何软件<br>`人工智能` | +438,859 | 2,120.1 †<br><sub>÷207 天</sub> | 439,541 | <a href="https://www.star-history.com/#morluto/rea&Date"><img src="https://api.star-history.com/svg?repos=morluto/rea&type=Date" width="260" alt="morluto/rea 的星标历史曲线"></a> |
| 3 | [DietrichGebert/ponytail](https://github.com/DietrichGebert/ponytail)<br>让 AI 少写废代码，该写的写对<br>`人工智能` | +185,998 | 1,256.7 †<br><sub>÷148 天</sub> | 186,120 | <a href="https://www.star-history.com/#DietrichGebert/ponytail&Date"><img src="https://api.star-history.com/svg?repos=DietrichGebert/ponytail&type=Date" width="260" alt="DietrichGebert/ponytail 的星标历史曲线"></a> |
| 4 | [openclaw/openclaw](https://github.com/openclaw/openclaw)<br>能把事做完的 AI 助手，跑在自己设备上<br>`人工智能` | +394,082 | 1,132.4 †<br><sub>÷348 天</sub> | 394,104 | <a href="https://www.star-history.com/#openclaw/openclaw&Date"><img src="https://api.star-history.com/svg?repos=openclaw/openclaw&type=Date" width="260" alt="openclaw/openclaw 的星标历史曲线"></a> |
| 5 | [affaan-m/ECC](https://github.com/affaan-m/ECC)<br>给编程 AI 加记忆、技能和安全检查<br>`人工智能` | +298,729 | 1,019.6 †<br><sub>÷293 天</sub> | 298,872 | <a href="https://www.star-history.com/#affaan-m/ECC&Date"><img src="https://api.star-history.com/svg?repos=affaan-m/ECC&type=Date" width="260" alt="affaan-m/ECC 的星标历史曲线"></a> |
| 6 | [NousResearch/hermes-agent](https://github.com/NousResearch/hermes-agent)<br>越用越会干活的 AI 助手<br>`人工智能` | +261,277 | 715.8 | 261,362 | <a href="https://www.star-history.com/#NousResearch/hermes-agent&Date"><img src="https://api.star-history.com/svg?repos=NousResearch/hermes-agent&type=Date" width="260" alt="NousResearch/hermes-agent 的星标历史曲线"></a> |
| 7 | [yetone/magpie](https://github.com/yetone/magpie)<br>编程 AI 换模型，额度用完自动续<br>`人工智能` | +31,451 | 698.9 †<br><sub>÷45 天</sub> | 31,597 | <a href="https://www.star-history.com/#yetone/magpie&Date"><img src="https://api.star-history.com/svg?repos=yetone/magpie&type=Date" width="260" alt="yetone/magpie 的星标历史曲线"></a> |
| 8 | [Graphify-Labs/graphify](https://github.com/Graphify-Labs/graphify)<br>大项目看不过来，先看这张地图<br>`人工智能` | +143,665 | 659.0 †<br><sub>÷218 天</sub> | 143,765 | <a href="https://www.star-history.com/#Graphify-Labs/graphify&Date"><img src="https://api.star-history.com/svg?repos=Graphify-Labs/graphify&type=Date" width="260" alt="Graphify-Labs/graphify 的星标历史曲线"></a> |
| 9 | [anomalyco/opencode](https://github.com/anomalyco/opencode)<br>终端里，有个开源 AI 帮你写代码<br>`人工智能` | +194,589 | 533.1 | 225,176 | <a href="https://www.star-history.com/#anomalyco/opencode&Date"><img src="https://api.star-history.com/svg?repos=anomalyco/opencode&type=Date" width="260" alt="anomalyco/opencode 的星标历史曲线"></a> |
| 10 | [stablyai/orca](https://github.com/stablyai/orca)<br>几个 AI 一起写，谁好用一眼看出<br>`人工智能` | +118,020 | 502.2 †<br><sub>÷235 天</sub> | 118,209 | <a href="https://www.star-history.com/#stablyai/orca&Date"><img src="https://api.star-history.com/svg?repos=stablyai/orca&type=Date" width="260" alt="stablyai/orca 的星标历史曲线"></a> |

† 该仓库创建时间短于统计窗口，因此“星标/天”按仓库存在的天数（显示在数字下方）计算，而不是按完整窗口。

### 总星标数（历史累计）

| # | 项目 | 总星标 | 星标历史 |
|---|---|---:|---|
| 1 | [morluto/rea](https://github.com/morluto/rea)<br>让 AI 帮你克隆任何软件<br>`人工智能` | 439,541 | <a href="https://www.star-history.com/#morluto/rea&Date"><img src="https://api.star-history.com/svg?repos=morluto/rea&type=Date" width="260" alt="morluto/rea 的星标历史曲线"></a> |
| 2 | [openclaw/openclaw](https://github.com/openclaw/openclaw)<br>能把事做完的 AI 助手，跑在自己设备上<br>`人工智能` | 394,104 | <a href="https://www.star-history.com/#openclaw/openclaw&Date"><img src="https://api.star-history.com/svg?repos=openclaw/openclaw&type=Date" width="260" alt="openclaw/openclaw 的星标历史曲线"></a> |
| 3 | [affaan-m/ECC](https://github.com/affaan-m/ECC)<br>给编程 AI 加记忆、技能和安全检查<br>`人工智能` | 298,872 | <a href="https://www.star-history.com/#affaan-m/ECC&Date"><img src="https://api.star-history.com/svg?repos=affaan-m/ECC&type=Date" width="260" alt="affaan-m/ECC 的星标历史曲线"></a> |
| 4 | [deepseek-ai/deepseek-harness](https://github.com/deepseek-ai/deepseek-harness)<br>想要什么智能体，用插件自己拼<br>`人工智能` | 275,423 | <a href="https://www.star-history.com/#deepseek-ai/deepseek-harness&Date"><img src="https://api.star-history.com/svg?repos=deepseek-ai/deepseek-harness&type=Date" width="260" alt="deepseek-ai/deepseek-harness 的星标历史曲线"></a> |
| 5 | [NousResearch/hermes-agent](https://github.com/NousResearch/hermes-agent)<br>越用越会干活的 AI 助手<br>`人工智能` | 261,362 | <a href="https://www.star-history.com/#NousResearch/hermes-agent&Date"><img src="https://api.star-history.com/svg?repos=NousResearch/hermes-agent&type=Date" width="260" alt="NousResearch/hermes-agent 的星标历史曲线"></a> |
| 6 | [anomalyco/opencode](https://github.com/anomalyco/opencode)<br>终端里，有个开源 AI 帮你写代码<br>`人工智能` | 225,176 | <a href="https://www.star-history.com/#anomalyco/opencode&Date"><img src="https://api.star-history.com/svg?repos=anomalyco/opencode&type=Date" width="260" alt="anomalyco/opencode 的星标历史曲线"></a> |
| 7 | [anthropics/skills](https://github.com/anthropics/skills)<br>Claude 技能怎么写，照着官方学<br>`人工智能` | 188,365 | <a href="https://www.star-history.com/#anthropics/skills&Date"><img src="https://api.star-history.com/svg?repos=anthropics/skills&type=Date" width="260" alt="anthropics/skills 的星标历史曲线"></a> |
| 8 | [DietrichGebert/ponytail](https://github.com/DietrichGebert/ponytail)<br>让 AI 少写废代码，该写的写对<br>`人工智能` | 186,120 | <a href="https://www.star-history.com/#DietrichGebert/ponytail&Date"><img src="https://api.star-history.com/svg?repos=DietrichGebert/ponytail&type=Date" width="260" alt="DietrichGebert/ponytail 的星标历史曲线"></a> |
| 9 | [farion1231/cc-switch](https://github.com/farion1231/cc-switch)<br>换接口不用改配置，一键切<br>`人工智能` | 152,528 | <a href="https://www.star-history.com/#farion1231/cc-switch&Date"><img src="https://api.star-history.com/svg?repos=farion1231/cc-switch&type=Date" width="260" alt="farion1231/cc-switch 的星标历史曲线"></a> |
| 10 | [nextlevelbuilder/ui-ux-pro-max-skill](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill)<br>AI 做的界面，看着像专业设计<br>`人工智能` | 146,367 | <a href="https://www.star-history.com/#nextlevelbuilder/ui-ux-pro-max-skill&Date"><img src="https://api.star-history.com/svg?repos=nextlevelbuilder/ui-ux-pro-max-skill&type=Date" width="260" alt="nextlevelbuilder/ui-ux-pro-max-skill 的星标历史曲线"></a> |

## 开发者工具

> 命令行、编辑器、包管理、代码检查与构建工具

### 最热新仓库（近 7 天内创建）

| # | 项目 | 创建时间（UTC） | 总星标 | 星标/天 | 星标历史 |
|---|---|---|---:|---:|---|
| 1 | [govijr/terminal-mac](https://github.com/govijr/terminal-mac)<br>不想离开终端，在里面运行完整 macOS | 2026-11-03<br><sub>4.4 天</sub> | 2,206 | 502.4 | <a href="https://www.star-history.com/#govijr/terminal-mac&Date"><img src="https://api.star-history.com/svg?repos=govijr/terminal-mac&type=Date" width="260" alt="govijr/terminal-mac 的星标历史曲线"></a> |
| 2 | [Verlintas/NOIR](https://github.com/Verlintas/NOIR)<br>扫出安卓应用隐私泄露，并支持安全回滚 | 2026-10-31<br><sub>6.6 天</sub> | 2,842 | 428.5 | <a href="https://www.star-history.com/#Verlintas/NOIR&Date"><img src="https://api.star-history.com/svg?repos=Verlintas/NOIR&type=Date" width="260" alt="Verlintas/NOIR 的星标历史曲线"></a> |
| 3 | [devvmhq/devvm](https://github.com/devvmhq/devvm)<br>每个项目都有独立编程沙箱 | 2026-11-06<br><sub>1.2 天</sub> | 296 | 238.9 | <a href="https://www.star-history.com/#devvmhq/devvm&Date"><img src="https://api.star-history.com/svg?repos=devvmhq/devvm&type=Date" width="260" alt="devvmhq/devvm 的星标历史曲线"></a> |
| 4 | [MetalHairdresser/slideshow-video-maker](https://github.com/MetalHairdresser/slideshow-video-maker)<br>视频编辑软件自动部署流程 | 2026-11-06<br><sub>1.0 天</sub> | 221 | 221.0 | <a href="https://www.star-history.com/#MetalHairdresser/slideshow-video-maker&Date"><img src="https://api.star-history.com/svg?repos=MetalHairdresser/slideshow-video-maker&type=Date" width="260" alt="MetalHairdresser/slideshow-video-maker 的星标历史曲线"></a> |
| 5 | [MinisterRoute/sp-flash-tool](https://github.com/MinisterRoute/sp-flash-tool)<br>桌面软件部署预配置环境 | 2026-11-06<br><sub>1.0 天</sub> | 221 | 221.0 | <a href="https://www.star-history.com/#MinisterRoute/sp-flash-tool&Date"><img src="https://api.star-history.com/svg?repos=MinisterRoute/sp-flash-tool&type=Date" width="260" alt="MinisterRoute/sp-flash-tool 的星标历史曲线"></a> |
| 6 | [Flintfaconceal/ads-blocker](https://github.com/Flintfaconceal/ads-blocker)<br>隔离环境中的桌面软件部署 | 2026-11-06<br><sub>1.0 天</sub> | 220 | 220.0 | <a href="https://www.star-history.com/#Flintfaconceal/ads-blocker&Date"><img src="https://api.star-history.com/svg?repos=Flintfaconceal/ads-blocker&type=Date" width="260" alt="Flintfaconceal/ads-blocker 的星标历史曲线"></a> |
| 7 | [Flockcleplank/aion-2-trainer-tool](https://github.com/Flockcleplank/aion-2-trainer-tool)<br>提示词工程任务的软件包部署 | 2026-11-06<br><sub>1.0 天</sub> | 220 | 220.0 | <a href="https://www.star-history.com/#Flockcleplank/aion-2-trainer-tool&Date"><img src="https://api.star-history.com/svg?repos=Flockcleplank/aion-2-trainer-tool&type=Date" width="260" alt="Flockcleplank/aion-2-trainer-tool 的星标历史曲线"></a> |
| 8 | [FloorFlameDone/androidunlocker](https://github.com/FloorFlameDone/androidunlocker)<br>本地工作站部署预配置环境 | 2026-11-06<br><sub>1.0 天</sub> | 220 | 220.0 | <a href="https://www.star-history.com/#FloorFlameDone/androidunlocker&Date"><img src="https://api.star-history.com/svg?repos=FloorFlameDone/androidunlocker&type=Date" width="260" alt="FloorFlameDone/androidunlocker 的星标历史曲线"></a> |
| 9 | [gravitygovernorhinge/clion](https://github.com/gravitygovernorhinge/clion)<br>本地工作站部署预配置环境 | 2026-11-06<br><sub>1.0 天</sub> | 220 | 220.0 | <a href="https://www.star-history.com/#gravitygovernorhinge/clion&Date"><img src="https://api.star-history.com/svg?repos=gravitygovernorhinge/clion&type=Date" width="260" alt="gravitygovernorhinge/clion 的星标历史曲线"></a> |
| 10 | [Hairanfollow/discord-quest-completer](https://github.com/Hairanfollow/discord-quest-completer)<br>本地工作站部署预配置环境 | 2026-11-06<br><sub>1.0 天</sub> | 220 | 220.0 | <a href="https://www.star-history.com/#Hairanfollow/discord-quest-completer&Date"><img src="https://api.star-history.com/svg?repos=Hairanfollow/discord-quest-completer&type=Date" width="260" alt="Hairanfollow/discord-quest-completer 的星标历史曲线"></a> |

### 本周增长最快（近 7 天）

| # | 项目 | 新增星标 | 星标/天 | 总星标 | 星标历史 |
|---|---|---:|---:|---:|---|
| 1 | [zed-industries/zed](https://github.com/zed-industries/zed)<br>打开就快，还能多人一起写代码<br>`开发者工具` | +1,521 | 217.3 | 94,047 | <a href="https://www.star-history.com/#zed-industries/zed&Date"><img src="https://api.star-history.com/svg?repos=zed-industries/zed&type=Date" width="260" alt="zed-industries/zed 的星标历史曲线"></a> |
| 2 | [astral-sh/uv](https://github.com/astral-sh/uv)<br>装 Python 包，不用再干等<br>`开发者工具` | +396 | 56.6 | 91,720 | <a href="https://www.star-history.com/#astral-sh/uv&Date"><img src="https://api.star-history.com/svg?repos=astral-sh/uv&type=Date" width="260" alt="astral-sh/uv 的星标历史曲线"></a> |
| 3 | [jdx/mise](https://github.com/jdx/mise)<br>开发工具、环境变量、任务，一个工具管<br>`开发者工具` | +331 | 47.3 | 35,889 | <a href="https://www.star-history.com/#jdx/mise&Date"><img src="https://api.star-history.com/svg?repos=jdx/mise&type=Date" width="260" alt="jdx/mise 的星标历史曲线"></a> |
| 4 | [BurntSushi/ripgrep](https://github.com/BurntSushi/ripgrep)<br>翻遍整个目录找文字，比 grep 快<br>`开发者工具` | +305 | 43.6 | 69,857 | <a href="https://www.star-history.com/#BurntSushi/ripgrep&Date"><img src="https://api.star-history.com/svg?repos=BurntSushi/ripgrep&type=Date" width="260" alt="BurntSushi/ripgrep 的星标历史曲线"></a> |
| 5 | [oven-sh/bun](https://github.com/oven-sh/bun)<br>运行打包测试装包，一个工具全包<br>`开发者工具` | +247 | 35.3 | 96,677 | <a href="https://www.star-history.com/#oven-sh/bun&Date"><img src="https://api.star-history.com/svg?repos=oven-sh/bun&type=Date" width="260" alt="oven-sh/bun 的星标历史曲线"></a> |
| 6 | [helix-editor/helix](https://github.com/helix-editor/helix)<br>语法高亮、语言服务都内置的文本编辑器<br>`开发者工具` | +176 | 25.1 | 46,905 | <a href="https://www.star-history.com/#helix-editor/helix&Date"><img src="https://api.star-history.com/svg?repos=helix-editor/helix&type=Date" width="260" alt="helix-editor/helix 的星标历史曲线"></a> |
| 7 | [cli/cli](https://github.com/cli/cli)<br>不开网页，命令行里处理 GitHub<br>`开发者工具` | +107 | 15.3 | 46,901 | <a href="https://www.star-history.com/#cli/cli&Date"><img src="https://api.star-history.com/svg?repos=cli/cli&type=Date" width="260" alt="cli/cli 的星标历史曲线"></a> |
| 8 | [biomejs/biome](https://github.com/biomejs/biome)<br>网页代码格式和检查，一个工具搞定<br>`开发者工具` | +42 | 6.0 | 26,055 | <a href="https://www.star-history.com/#biomejs/biome&Date"><img src="https://api.star-history.com/svg?repos=biomejs/biome&type=Date" width="260" alt="biomejs/biome 的星标历史曲线"></a> |

### 本月增长最快（近 30 天）

| # | 项目 | 新增星标 | 星标/天 | 总星标 | 星标历史 |
|---|---|---:|---:|---:|---|
| 1 | [zed-industries/zed](https://github.com/zed-industries/zed)<br>打开就快，还能多人一起写代码<br>`开发者工具` | +2,766 | 92.2 | 94,047 | <a href="https://www.star-history.com/#zed-industries/zed&Date"><img src="https://api.star-history.com/svg?repos=zed-industries/zed&type=Date" width="260" alt="zed-industries/zed 的星标历史曲线"></a> |
| 2 | [astral-sh/uv](https://github.com/astral-sh/uv)<br>装 Python 包，不用再干等<br>`开发者工具` | +1,417 | 47.2 | 91,720 | <a href="https://www.star-history.com/#astral-sh/uv&Date"><img src="https://api.star-history.com/svg?repos=astral-sh/uv&type=Date" width="260" alt="astral-sh/uv 的星标历史曲线"></a> |
| 3 | [jdx/mise](https://github.com/jdx/mise)<br>开发工具、环境变量、任务，一个工具管<br>`开发者工具` | +1,223 | 40.8 | 35,889 | <a href="https://www.star-history.com/#jdx/mise&Date"><img src="https://api.star-history.com/svg?repos=jdx/mise&type=Date" width="260" alt="jdx/mise 的星标历史曲线"></a> |
| 4 | [BurntSushi/ripgrep](https://github.com/BurntSushi/ripgrep)<br>翻遍整个目录找文字，比 grep 快<br>`开发者工具` | +1,083 | 36.1 | 69,857 | <a href="https://www.star-history.com/#BurntSushi/ripgrep&Date"><img src="https://api.star-history.com/svg?repos=BurntSushi/ripgrep&type=Date" width="260" alt="BurntSushi/ripgrep 的星标历史曲线"></a> |
| 5 | [oven-sh/bun](https://github.com/oven-sh/bun)<br>运行打包测试装包，一个工具全包<br>`开发者工具` | +813 | 27.1 | 96,677 | <a href="https://www.star-history.com/#oven-sh/bun&Date"><img src="https://api.star-history.com/svg?repos=oven-sh/bun&type=Date" width="260" alt="oven-sh/bun 的星标历史曲线"></a> |
| 6 | [helix-editor/helix](https://github.com/helix-editor/helix)<br>语法高亮、语言服务都内置的文本编辑器<br>`开发者工具` | +516 | 17.2 | 46,905 | <a href="https://www.star-history.com/#helix-editor/helix&Date"><img src="https://api.star-history.com/svg?repos=helix-editor/helix&type=Date" width="260" alt="helix-editor/helix 的星标历史曲线"></a> |
| 7 | [cli/cli](https://github.com/cli/cli)<br>不开网页，命令行里处理 GitHub<br>`开发者工具` | +440 | 14.7 | 46,901 | <a href="https://www.star-history.com/#cli/cli&Date"><img src="https://api.star-history.com/svg?repos=cli/cli&type=Date" width="260" alt="cli/cli 的星标历史曲线"></a> |
| 8 | [biomejs/biome](https://github.com/biomejs/biome)<br>网页代码格式和检查，一个工具搞定<br>`开发者工具` | +216 | 7.2 | 26,055 | <a href="https://www.star-history.com/#biomejs/biome&Date"><img src="https://api.star-history.com/svg?repos=biomejs/biome&type=Date" width="260" alt="biomejs/biome 的星标历史曲线"></a> |

### 今年增长最快（近 365 天）

| # | 项目 | 新增星标 | 星标/天 | 总星标 | 星标历史 |
|---|---|---:|---:|---:|---|
| 1 | [zed-industries/zed](https://github.com/zed-industries/zed)<br>打开就快，还能多人一起写代码<br>`开发者工具` | +26,702 | 73.2 | 94,047 | <a href="https://www.star-history.com/#zed-industries/zed&Date"><img src="https://api.star-history.com/svg?repos=zed-industries/zed&type=Date" width="260" alt="zed-industries/zed 的星标历史曲线"></a> |
| 2 | [astral-sh/uv](https://github.com/astral-sh/uv)<br>装 Python 包，不用再干等<br>`开发者工具` | +21,102 | 57.8 | 91,720 | <a href="https://www.star-history.com/#astral-sh/uv&Date"><img src="https://api.star-history.com/svg?repos=astral-sh/uv&type=Date" width="260" alt="astral-sh/uv 的星标历史曲线"></a> |
| 3 | [oven-sh/bun](https://github.com/oven-sh/bun)<br>运行打包测试装包，一个工具全包<br>`开发者工具` | +16,646 | 45.6 | 96,677 | <a href="https://www.star-history.com/#oven-sh/bun&Date"><img src="https://api.star-history.com/svg?repos=oven-sh/bun&type=Date" width="260" alt="oven-sh/bun 的星标历史曲线"></a> |
| 4 | [jdx/mise](https://github.com/jdx/mise)<br>开发工具、环境变量、任务，一个工具管<br>`开发者工具` | +15,141 | 41.5 | 35,889 | <a href="https://www.star-history.com/#jdx/mise&Date"><img src="https://api.star-history.com/svg?repos=jdx/mise&type=Date" width="260" alt="jdx/mise 的星标历史曲线"></a> |
| 5 | [BurntSushi/ripgrep](https://github.com/BurntSushi/ripgrep)<br>翻遍整个目录找文字，比 grep 快<br>`开发者工具` | +13,453 | 36.9 | 69,857 | <a href="https://www.star-history.com/#BurntSushi/ripgrep&Date"><img src="https://api.star-history.com/svg?repos=BurntSushi/ripgrep&type=Date" width="260" alt="BurntSushi/ripgrep 的星标历史曲线"></a> |
| 6 | [helix-editor/helix](https://github.com/helix-editor/helix)<br>语法高亮、语言服务都内置的文本编辑器<br>`开发者工具` | +6,685 | 18.3 | 46,905 | <a href="https://www.star-history.com/#helix-editor/helix&Date"><img src="https://api.star-history.com/svg?repos=helix-editor/helix&type=Date" width="260" alt="helix-editor/helix 的星标历史曲线"></a> |
| 7 | [cli/cli](https://github.com/cli/cli)<br>不开网页，命令行里处理 GitHub<br>`开发者工具` | +6,275 | 17.2 | 46,901 | <a href="https://www.star-history.com/#cli/cli&Date"><img src="https://api.star-history.com/svg?repos=cli/cli&type=Date" width="260" alt="cli/cli 的星标历史曲线"></a> |
| 8 | [biomejs/biome](https://github.com/biomejs/biome)<br>网页代码格式和检查，一个工具搞定<br>`开发者工具` | +4,503 | 12.3 | 26,055 | <a href="https://www.star-history.com/#biomejs/biome&Date"><img src="https://api.star-history.com/svg?repos=biomejs/biome&type=Date" width="260" alt="biomejs/biome 的星标历史曲线"></a> |

### 总星标数（历史累计）

| # | 项目 | 总星标 | 星标历史 |
|---|---|---:|---|
| 1 | [oven-sh/bun](https://github.com/oven-sh/bun)<br>运行打包测试装包，一个工具全包<br>`开发者工具` | 96,677 | <a href="https://www.star-history.com/#oven-sh/bun&Date"><img src="https://api.star-history.com/svg?repos=oven-sh/bun&type=Date" width="260" alt="oven-sh/bun 的星标历史曲线"></a> |
| 2 | [zed-industries/zed](https://github.com/zed-industries/zed)<br>打开就快，还能多人一起写代码<br>`开发者工具` | 94,047 | <a href="https://www.star-history.com/#zed-industries/zed&Date"><img src="https://api.star-history.com/svg?repos=zed-industries/zed&type=Date" width="260" alt="zed-industries/zed 的星标历史曲线"></a> |
| 3 | [astral-sh/uv](https://github.com/astral-sh/uv)<br>装 Python 包，不用再干等<br>`开发者工具` | 91,720 | <a href="https://www.star-history.com/#astral-sh/uv&Date"><img src="https://api.star-history.com/svg?repos=astral-sh/uv&type=Date" width="260" alt="astral-sh/uv 的星标历史曲线"></a> |
| 4 | [BurntSushi/ripgrep](https://github.com/BurntSushi/ripgrep)<br>翻遍整个目录找文字，比 grep 快<br>`开发者工具` | 69,857 | <a href="https://www.star-history.com/#BurntSushi/ripgrep&Date"><img src="https://api.star-history.com/svg?repos=BurntSushi/ripgrep&type=Date" width="260" alt="BurntSushi/ripgrep 的星标历史曲线"></a> |
| 5 | [helix-editor/helix](https://github.com/helix-editor/helix)<br>语法高亮、语言服务都内置的文本编辑器<br>`开发者工具` | 46,905 | <a href="https://www.star-history.com/#helix-editor/helix&Date"><img src="https://api.star-history.com/svg?repos=helix-editor/helix&type=Date" width="260" alt="helix-editor/helix 的星标历史曲线"></a> |
| 6 | [cli/cli](https://github.com/cli/cli)<br>不开网页，命令行里处理 GitHub<br>`开发者工具` | 46,901 | <a href="https://www.star-history.com/#cli/cli&Date"><img src="https://api.star-history.com/svg?repos=cli/cli&type=Date" width="260" alt="cli/cli 的星标历史曲线"></a> |
| 7 | [jdx/mise](https://github.com/jdx/mise)<br>开发工具、环境变量、任务，一个工具管<br>`开发者工具` | 35,889 | <a href="https://www.star-history.com/#jdx/mise&Date"><img src="https://api.star-history.com/svg?repos=jdx/mise&type=Date" width="260" alt="jdx/mise 的星标历史曲线"></a> |
| 8 | [biomejs/biome](https://github.com/biomejs/biome)<br>网页代码格式和检查，一个工具搞定<br>`开发者工具` | 26,055 | <a href="https://www.star-history.com/#biomejs/biome&Date"><img src="https://api.star-history.com/svg?repos=biomejs/biome&type=Date" width="260" alt="biomejs/biome 的星标历史曲线"></a> |

## 安全

> 漏洞扫描、静态分析、供应链与运行时安全

### 最热新仓库（近 7 天内创建）

| # | 项目 | 创建时间（UTC） | 总星标 | 星标/天 | 星标历史 |
|---|---|---|---:|---:|---|
| 1 | [yorkeccak/globalhackmap](https://github.com/yorkeccak/globalhackmap)<br>在地球仪上实时查看安全事件 | 2026-11-02<br><sub>4.8 天</sub> | 113 | 23.5 | <a href="https://www.star-history.com/#yorkeccak/globalhackmap&Date"><img src="https://api.star-history.com/svg?repos=yorkeccak/globalhackmap&type=Date" width="260" alt="yorkeccak/globalhackmap 的星标历史曲线"></a> |

### 本周增长最快（近 7 天）

| # | 项目 | 新增星标 | 星标/天 | 总星标 | 星标历史 |
|---|---|---:|---:|---:|---|
| 1 | [aquasecurity/trivy](https://github.com/aquasecurity/trivy)<br>容器和代码仓，一次扫完安全问题<br>`安全` | +232 | 33.1 | 39,090 | <a href="https://www.star-history.com/#aquasecurity/trivy&Date"><img src="https://api.star-history.com/svg?repos=aquasecurity/trivy&type=Date" width="260" alt="aquasecurity/trivy 的星标历史曲线"></a> |
| 2 | [projectdiscovery/nuclei](https://github.com/projectdiscovery/nuclei)<br>写个模板，就能批量扫漏洞<br>`安全` | +193 | 27.6 | 32,656 | <a href="https://www.star-history.com/#projectdiscovery/nuclei&Date"><img src="https://api.star-history.com/svg?repos=projectdiscovery/nuclei&type=Date" width="260" alt="projectdiscovery/nuclei 的星标历史曲线"></a> |
| 3 | [semgrep/semgrep](https://github.com/semgrep/semgrep)<br>代码里的问题，提交前先揪出来<br>`安全` | +174 | 24.9 | 17,535 | <a href="https://www.star-history.com/#semgrep/semgrep&Date"><img src="https://api.star-history.com/svg?repos=semgrep/semgrep&type=Date" width="260" alt="semgrep/semgrep 的星标历史曲线"></a> |
| 4 | [OWASP/CheatSheetSeries](https://github.com/OWASP/CheatSheetSeries)<br>应用安全怎么做，看这套速查表<br>`安全` | +118 | 16.9 | 33,928 | <a href="https://www.star-history.com/#OWASP/CheatSheetSeries&Date"><img src="https://api.star-history.com/svg?repos=OWASP/CheatSheetSeries&type=Date" width="260" alt="OWASP/CheatSheetSeries 的星标历史曲线"></a> |
| 5 | [google/osv-scanner](https://github.com/google/osv-scanner)<br>用的依赖安不安全，扫一下就知道<br>`安全` | +113 | 16.1 | 11,447 | <a href="https://www.star-history.com/#google/osv-scanner&Date"><img src="https://api.star-history.com/svg?repos=google/osv-scanner&type=Date" width="260" alt="google/osv-scanner 的星标历史曲线"></a> |
| 6 | [anchore/grype](https://github.com/anchore/grype)<br>容器镜像有没有漏洞，扫一下就知道<br>`安全` | +57 | 8.1 | 13,203 | <a href="https://www.star-history.com/#anchore/grype&Date"><img src="https://api.star-history.com/svg?repos=anchore/grype&type=Date" width="260" alt="anchore/grype 的星标历史曲线"></a> |
| 7 | [falcosecurity/falco](https://github.com/falcosecurity/falco)<br>云上有异常，第一时间知道<br>`安全` | +21 | 3.0 | 9,560 | <a href="https://www.star-history.com/#falcosecurity/falco&Date"><img src="https://api.star-history.com/svg?repos=falcosecurity/falco&type=Date" width="260" alt="falcosecurity/falco 的星标历史曲线"></a> |
| 8 | [securego/gosec](https://github.com/securego/gosec)<br>Go 代码的安全隐患，扫一遍就知道<br>`安全` | +7 | 1.0 | 9,000 | <a href="https://www.star-history.com/#securego/gosec&Date"><img src="https://api.star-history.com/svg?repos=securego/gosec&type=Date" width="260" alt="securego/gosec 的星标历史曲线"></a> |

### 本月增长最快（近 30 天）

| # | 项目 | 新增星标 | 星标/天 | 总星标 | 星标历史 |
|---|---|---:|---:|---:|---|
| 1 | [projectdiscovery/nuclei](https://github.com/projectdiscovery/nuclei)<br>写个模板，就能批量扫漏洞<br>`安全` | +919 | 30.6 | 32,656 | <a href="https://www.star-history.com/#projectdiscovery/nuclei&Date"><img src="https://api.star-history.com/svg?repos=projectdiscovery/nuclei&type=Date" width="260" alt="projectdiscovery/nuclei 的星标历史曲线"></a> |
| 2 | [aquasecurity/trivy](https://github.com/aquasecurity/trivy)<br>容器和代码仓，一次扫完安全问题<br>`安全` | +853 | 28.4 | 39,090 | <a href="https://www.star-history.com/#aquasecurity/trivy&Date"><img src="https://api.star-history.com/svg?repos=aquasecurity/trivy&type=Date" width="260" alt="aquasecurity/trivy 的星标历史曲线"></a> |
| 3 | [semgrep/semgrep](https://github.com/semgrep/semgrep)<br>代码里的问题，提交前先揪出来<br>`安全` | +638 | 21.3 | 17,535 | <a href="https://www.star-history.com/#semgrep/semgrep&Date"><img src="https://api.star-history.com/svg?repos=semgrep/semgrep&type=Date" width="260" alt="semgrep/semgrep 的星标历史曲线"></a> |
| 4 | [OWASP/CheatSheetSeries](https://github.com/OWASP/CheatSheetSeries)<br>应用安全怎么做，看这套速查表<br>`安全` | +415 | 13.8 | 33,928 | <a href="https://www.star-history.com/#OWASP/CheatSheetSeries&Date"><img src="https://api.star-history.com/svg?repos=OWASP/CheatSheetSeries&type=Date" width="260" alt="OWASP/CheatSheetSeries 的星标历史曲线"></a> |
| 5 | [google/osv-scanner](https://github.com/google/osv-scanner)<br>用的依赖安不安全，扫一下就知道<br>`安全` | +310 | 10.3 | 11,447 | <a href="https://www.star-history.com/#google/osv-scanner&Date"><img src="https://api.star-history.com/svg?repos=google/osv-scanner&type=Date" width="260" alt="google/osv-scanner 的星标历史曲线"></a> |
| 6 | [anchore/grype](https://github.com/anchore/grype)<br>容器镜像有没有漏洞，扫一下就知道<br>`安全` | +225 | 7.5 | 13,203 | <a href="https://www.star-history.com/#anchore/grype&Date"><img src="https://api.star-history.com/svg?repos=anchore/grype&type=Date" width="260" alt="anchore/grype 的星标历史曲线"></a> |
| 7 | [falcosecurity/falco](https://github.com/falcosecurity/falco)<br>云上有异常，第一时间知道<br>`安全` | +116 | 3.9 | 9,560 | <a href="https://www.star-history.com/#falcosecurity/falco&Date"><img src="https://api.star-history.com/svg?repos=falcosecurity/falco&type=Date" width="260" alt="falcosecurity/falco 的星标历史曲线"></a> |
| 8 | [securego/gosec](https://github.com/securego/gosec)<br>Go 代码的安全隐患，扫一遍就知道<br>`安全` | +43 | 1.4 | 9,000 | <a href="https://www.star-history.com/#securego/gosec&Date"><img src="https://api.star-history.com/svg?repos=securego/gosec&type=Date" width="260" alt="securego/gosec 的星标历史曲线"></a> |

### 今年增长最快（近 365 天）

| # | 项目 | 新增星标 | 星标/天 | 总星标 | 星标历史 |
|---|---|---:|---:|---:|---|
| 1 | [aquasecurity/trivy](https://github.com/aquasecurity/trivy)<br>容器和代码仓，一次扫完安全问题<br>`安全` | +10,221 | 28.0 | 39,090 | <a href="https://www.star-history.com/#aquasecurity/trivy&Date"><img src="https://api.star-history.com/svg?repos=aquasecurity/trivy&type=Date" width="260" alt="aquasecurity/trivy 的星标历史曲线"></a> |
| 2 | [projectdiscovery/nuclei](https://github.com/projectdiscovery/nuclei)<br>写个模板，就能批量扫漏洞<br>`安全` | +7,668 | 21.0 | 32,656 | <a href="https://www.star-history.com/#projectdiscovery/nuclei&Date"><img src="https://api.star-history.com/svg?repos=projectdiscovery/nuclei&type=Date" width="260" alt="projectdiscovery/nuclei 的星标历史曲线"></a> |
| 3 | [semgrep/semgrep](https://github.com/semgrep/semgrep)<br>代码里的问题，提交前先揪出来<br>`安全` | +4,463 | 12.2 | 17,535 | <a href="https://www.star-history.com/#semgrep/semgrep&Date"><img src="https://api.star-history.com/svg?repos=semgrep/semgrep&type=Date" width="260" alt="semgrep/semgrep 的星标历史曲线"></a> |
| 4 | [OWASP/CheatSheetSeries](https://github.com/OWASP/CheatSheetSeries)<br>应用安全怎么做，看这套速查表<br>`安全` | +3,571 | 9.8 | 33,928 | <a href="https://www.star-history.com/#OWASP/CheatSheetSeries&Date"><img src="https://api.star-history.com/svg?repos=OWASP/CheatSheetSeries&type=Date" width="260" alt="OWASP/CheatSheetSeries 的星标历史曲线"></a> |
| 5 | [google/osv-scanner](https://github.com/google/osv-scanner)<br>用的依赖安不安全，扫一下就知道<br>`安全` | +3,553 | 9.7 | 11,447 | <a href="https://www.star-history.com/#google/osv-scanner&Date"><img src="https://api.star-history.com/svg?repos=google/osv-scanner&type=Date" width="260" alt="google/osv-scanner 的星标历史曲线"></a> |
| 6 | [anchore/grype](https://github.com/anchore/grype)<br>容器镜像有没有漏洞，扫一下就知道<br>`安全` | +2,367 | 6.5 | 13,203 | <a href="https://www.star-history.com/#anchore/grype&Date"><img src="https://api.star-history.com/svg?repos=anchore/grype&type=Date" width="260" alt="anchore/grype 的星标历史曲线"></a> |
| 7 | [falcosecurity/falco](https://github.com/falcosecurity/falco)<br>云上有异常，第一时间知道<br>`安全` | +1,269 | 3.5 | 9,560 | <a href="https://www.star-history.com/#falcosecurity/falco&Date"><img src="https://api.star-history.com/svg?repos=falcosecurity/falco&type=Date" width="260" alt="falcosecurity/falco 的星标历史曲线"></a> |
| 8 | [securego/gosec](https://github.com/securego/gosec)<br>Go 代码的安全隐患，扫一遍就知道<br>`安全` | +560 | 1.5 | 9,000 | <a href="https://www.star-history.com/#securego/gosec&Date"><img src="https://api.star-history.com/svg?repos=securego/gosec&type=Date" width="260" alt="securego/gosec 的星标历史曲线"></a> |

### 总星标数（历史累计）

| # | 项目 | 总星标 | 星标历史 |
|---|---|---:|---|
| 1 | [aquasecurity/trivy](https://github.com/aquasecurity/trivy)<br>容器和代码仓，一次扫完安全问题<br>`安全` | 39,090 | <a href="https://www.star-history.com/#aquasecurity/trivy&Date"><img src="https://api.star-history.com/svg?repos=aquasecurity/trivy&type=Date" width="260" alt="aquasecurity/trivy 的星标历史曲线"></a> |
| 2 | [OWASP/CheatSheetSeries](https://github.com/OWASP/CheatSheetSeries)<br>应用安全怎么做，看这套速查表<br>`安全` | 33,928 | <a href="https://www.star-history.com/#OWASP/CheatSheetSeries&Date"><img src="https://api.star-history.com/svg?repos=OWASP/CheatSheetSeries&type=Date" width="260" alt="OWASP/CheatSheetSeries 的星标历史曲线"></a> |
| 3 | [projectdiscovery/nuclei](https://github.com/projectdiscovery/nuclei)<br>写个模板，就能批量扫漏洞<br>`安全` | 32,656 | <a href="https://www.star-history.com/#projectdiscovery/nuclei&Date"><img src="https://api.star-history.com/svg?repos=projectdiscovery/nuclei&type=Date" width="260" alt="projectdiscovery/nuclei 的星标历史曲线"></a> |
| 4 | [semgrep/semgrep](https://github.com/semgrep/semgrep)<br>代码里的问题，提交前先揪出来<br>`安全` | 17,535 | <a href="https://www.star-history.com/#semgrep/semgrep&Date"><img src="https://api.star-history.com/svg?repos=semgrep/semgrep&type=Date" width="260" alt="semgrep/semgrep 的星标历史曲线"></a> |
| 5 | [anchore/grype](https://github.com/anchore/grype)<br>容器镜像有没有漏洞，扫一下就知道<br>`安全` | 13,203 | <a href="https://www.star-history.com/#anchore/grype&Date"><img src="https://api.star-history.com/svg?repos=anchore/grype&type=Date" width="260" alt="anchore/grype 的星标历史曲线"></a> |
| 6 | [google/osv-scanner](https://github.com/google/osv-scanner)<br>用的依赖安不安全，扫一下就知道<br>`安全` | 11,447 | <a href="https://www.star-history.com/#google/osv-scanner&Date"><img src="https://api.star-history.com/svg?repos=google/osv-scanner&type=Date" width="260" alt="google/osv-scanner 的星标历史曲线"></a> |
| 7 | [falcosecurity/falco](https://github.com/falcosecurity/falco)<br>云上有异常，第一时间知道<br>`安全` | 9,560 | <a href="https://www.star-history.com/#falcosecurity/falco&Date"><img src="https://api.star-history.com/svg?repos=falcosecurity/falco&type=Date" width="260" alt="falcosecurity/falco 的星标历史曲线"></a> |
| 8 | [securego/gosec](https://github.com/securego/gosec)<br>Go 代码的安全隐患，扫一遍就知道<br>`安全` | 9,000 | <a href="https://www.star-history.com/#securego/gosec&Date"><img src="https://api.star-history.com/svg?repos=securego/gosec&type=Date" width="260" alt="securego/gosec 的星标历史曲线"></a> |

## Web / 前端

> 前端框架、UI 组件库、CSS 与浏览器工具

### 最热新仓库（近 7 天内创建）

| # | 项目 | 创建时间（UTC） | 总星标 | 星标/天 | 星标历史 |
|---|---|---|---:|---:|---|
| 1 | [AtomIllusionistDwell/watson-username-footprint-finder](https://github.com/AtomIllusionistDwell/watson-username-footprint-finder)<br>把公开页面的人物搜索汇成报告 | 2026-11-05<br><sub>2.3 天</sub> | 412 | 178.4 | <a href="https://www.star-history.com/#AtomIllusionistDwell/watson-username-footprint-finder&Date"><img src="https://api.star-history.com/svg?repos=AtomIllusionistDwell/watson-username-footprint-finder&type=Date" width="260" alt="AtomIllusionistDwell/watson-username-footprint-finder 的星标历史曲线"></a> |
| 2 | [zeemscript/block-roll](https://github.com/zeemscript/block-roll)<br>加密存储和分享文件 | 2026-11-05<br><sub>2.5 天</sub> | 164 | 65.0 | <a href="https://www.star-history.com/#zeemscript/block-roll&Date"><img src="https://api.star-history.com/svg?repos=zeemscript/block-roll&type=Date" width="260" alt="zeemscript/block-roll 的星标历史曲线"></a> |
| 3 | [lijiaqi-AI-Product-Manager/dsh-agent-compare](https://github.com/lijiaqi-AI-Product-Manager/dsh-agent-compare)<br>先体验两个版本，再审查选用 | 2026-11-02<br><sub>5.5 天</sub> | 180 | 32.6 | <a href="https://www.star-history.com/#lijiaqi-AI-Product-Manager/dsh-agent-compare&Date"><img src="https://api.star-history.com/svg?repos=lijiaqi-AI-Product-Manager/dsh-agent-compare&type=Date" width="260" alt="lijiaqi-AI-Product-Manager/dsh-agent-compare 的星标历史曲线"></a> |

### 本周增长最快（近 7 天）

| # | 项目 | 新增星标 | 星标/天 | 总星标 | 星标历史 |
|---|---|---:|---:|---:|---|
| 1 | [facebook/react](https://github.com/facebook/react)<br>网页和 App 界面，都能用它来搭<br>`Web / 前端` | +638 | 91.1 | 252,347 | <a href="https://www.star-history.com/#facebook/react&Date"><img src="https://api.star-history.com/svg?repos=facebook/react&type=Date" width="260" alt="facebook/react 的星标历史曲线"></a> |
| 2 | [shadcn-ui/ui](https://github.com/shadcn-ui/ui)<br>好看的组件，代码归你，随便改<br>`Web / 前端` | +605 | 86.4 | 127,562 | <a href="https://www.star-history.com/#shadcn-ui/ui&Date"><img src="https://api.star-history.com/svg?repos=shadcn-ui/ui&type=Date" width="260" alt="shadcn-ui/ui 的星标历史曲线"></a> |
| 3 | [vercel/next.js](https://github.com/vercel/next.js)<br>用 React 做完整网站，从前到后<br>`Web / 前端` | +223 | 31.9 | 143,379 | <a href="https://www.star-history.com/#vercel/next.js&Date"><img src="https://api.star-history.com/svg?repos=vercel/next.js&type=Date" width="260" alt="vercel/next.js 的星标历史曲线"></a> |
| 4 | [tailwindlabs/tailwindcss](https://github.com/tailwindlabs/tailwindcss)<br>不写一大堆 CSS，也能做定制界面<br>`Web / 前端` | +203 | 29.0 | 98,214 | <a href="https://www.star-history.com/#tailwindlabs/tailwindcss&Date"><img src="https://api.star-history.com/svg?repos=tailwindlabs/tailwindcss&type=Date" width="260" alt="tailwindlabs/tailwindcss 的星标历史曲线"></a> |
| 5 | [withastro/astro](https://github.com/withastro/astro)<br>做内容型网站，页面输出更轻量<br>`Web / 前端` | +203 | 29.0 | 63,799 | <a href="https://www.star-history.com/#withastro/astro&Date"><img src="https://api.star-history.com/svg?repos=withastro/astro&type=Date" width="260" alt="withastro/astro 的星标历史曲线"></a> |
| 6 | [sveltejs/svelte](https://github.com/sveltejs/svelte)<br>你写组件，编译器变出高效的网页代码<br>`Web / 前端` | +197 | 28.1 | 88,657 | <a href="https://www.star-history.com/#sveltejs/svelte&Date"><img src="https://api.star-history.com/svg?repos=sveltejs/svelte&type=Date" width="260" alt="sveltejs/svelte 的星标历史曲线"></a> |
| 7 | [vuejs/core](https://github.com/vuejs/core)<br>从一个小页面开始，用多少学多少<br>`Web / 前端` | +72 | 10.3 | 54,841 | <a href="https://www.star-history.com/#vuejs/core&Date"><img src="https://api.star-history.com/svg?repos=vuejs/core&type=Date" width="260" alt="vuejs/core 的星标历史曲线"></a> |
| 8 | [tanstack/query](https://github.com/tanstack/query)<br>请求数据和缓存，交给它管<br>`Web / 前端` | +48 | 6.9 | 50,535 | <a href="https://www.star-history.com/#tanstack/query&Date"><img src="https://api.star-history.com/svg?repos=tanstack/query&type=Date" width="260" alt="tanstack/query 的星标历史曲线"></a> |

### 本月增长最快（近 30 天）

| # | 项目 | 新增星标 | 星标/天 | 总星标 | 星标历史 |
|---|---|---:|---:|---:|---|
| 1 | [shadcn-ui/ui](https://github.com/shadcn-ui/ui)<br>好看的组件，代码归你，随便改<br>`Web / 前端` | +2,756 | 91.9 | 127,562 | <a href="https://www.star-history.com/#shadcn-ui/ui&Date"><img src="https://api.star-history.com/svg?repos=shadcn-ui/ui&type=Date" width="260" alt="shadcn-ui/ui 的星标历史曲线"></a> |
| 2 | [facebook/react](https://github.com/facebook/react)<br>网页和 App 界面，都能用它来搭<br>`Web / 前端` | +2,044 | 68.1 | 252,347 | <a href="https://www.star-history.com/#facebook/react&Date"><img src="https://api.star-history.com/svg?repos=facebook/react&type=Date" width="260" alt="facebook/react 的星标历史曲线"></a> |
| 3 | [withastro/astro](https://github.com/withastro/astro)<br>做内容型网站，页面输出更轻量<br>`Web / 前端` | +804 | 26.8 | 63,799 | <a href="https://www.star-history.com/#withastro/astro&Date"><img src="https://api.star-history.com/svg?repos=withastro/astro&type=Date" width="260" alt="withastro/astro 的星标历史曲线"></a> |
| 4 | [vercel/next.js](https://github.com/vercel/next.js)<br>用 React 做完整网站，从前到后<br>`Web / 前端` | +768 | 25.6 | 143,379 | <a href="https://www.star-history.com/#vercel/next.js&Date"><img src="https://api.star-history.com/svg?repos=vercel/next.js&type=Date" width="260" alt="vercel/next.js 的星标历史曲线"></a> |
| 5 | [sveltejs/svelte](https://github.com/sveltejs/svelte)<br>你写组件，编译器变出高效的网页代码<br>`Web / 前端` | +580 | 19.3 | 88,657 | <a href="https://www.star-history.com/#sveltejs/svelte&Date"><img src="https://api.star-history.com/svg?repos=sveltejs/svelte&type=Date" width="260" alt="sveltejs/svelte 的星标历史曲线"></a> |
| 6 | [tailwindlabs/tailwindcss](https://github.com/tailwindlabs/tailwindcss)<br>不写一大堆 CSS，也能做定制界面<br>`Web / 前端` | +572 | 19.1 | 98,214 | <a href="https://www.star-history.com/#tailwindlabs/tailwindcss&Date"><img src="https://api.star-history.com/svg?repos=tailwindlabs/tailwindcss&type=Date" width="260" alt="tailwindlabs/tailwindcss 的星标历史曲线"></a> |
| 7 | [vuejs/core](https://github.com/vuejs/core)<br>从一个小页面开始，用多少学多少<br>`Web / 前端` | +415 | 13.8 | 54,841 | <a href="https://www.star-history.com/#vuejs/core&Date"><img src="https://api.star-history.com/svg?repos=vuejs/core&type=Date" width="260" alt="vuejs/core 的星标历史曲线"></a> |
| 8 | [tanstack/query](https://github.com/tanstack/query)<br>请求数据和缓存，交给它管<br>`Web / 前端` | +208 | 6.9 | 50,535 | <a href="https://www.star-history.com/#tanstack/query&Date"><img src="https://api.star-history.com/svg?repos=tanstack/query&type=Date" width="260" alt="tanstack/query 的星标历史曲线"></a> |

### 今年增长最快（近 365 天）

| # | 项目 | 新增星标 | 星标/天 | 总星标 | 星标历史 |
|---|---|---:|---:|---:|---|
| 1 | [shadcn-ui/ui](https://github.com/shadcn-ui/ui)<br>好看的组件，代码归你，随便改<br>`Web / 前端` | +30,382 | 83.2 | 127,562 | <a href="https://www.star-history.com/#shadcn-ui/ui&Date"><img src="https://api.star-history.com/svg?repos=shadcn-ui/ui&type=Date" width="260" alt="shadcn-ui/ui 的星标历史曲线"></a> |
| 2 | [facebook/react](https://github.com/facebook/react)<br>网页和 App 界面，都能用它来搭<br>`Web / 前端` | +15,557 | 42.6 | 252,347 | <a href="https://www.star-history.com/#facebook/react&Date"><img src="https://api.star-history.com/svg?repos=facebook/react&type=Date" width="260" alt="facebook/react 的星标历史曲线"></a> |
| 3 | [withastro/astro](https://github.com/withastro/astro)<br>做内容型网站，页面输出更轻量<br>`Web / 前端` | +10,542 | 28.9 | 63,799 | <a href="https://www.star-history.com/#withastro/astro&Date"><img src="https://api.star-history.com/svg?repos=withastro/astro&type=Date" width="260" alt="withastro/astro 的星标历史曲线"></a> |
| 4 | [vercel/next.js](https://github.com/vercel/next.js)<br>用 React 做完整网站，从前到后<br>`Web / 前端` | +10,393 | 28.5 | 143,379 | <a href="https://www.star-history.com/#vercel/next.js&Date"><img src="https://api.star-history.com/svg?repos=vercel/next.js&type=Date" width="260" alt="vercel/next.js 的星标历史曲线"></a> |
| 5 | [tailwindlabs/tailwindcss](https://github.com/tailwindlabs/tailwindcss)<br>不写一大堆 CSS，也能做定制界面<br>`Web / 前端` | +8,592 | 23.5 | 98,214 | <a href="https://www.star-history.com/#tailwindlabs/tailwindcss&Date"><img src="https://api.star-history.com/svg?repos=tailwindlabs/tailwindcss&type=Date" width="260" alt="tailwindlabs/tailwindcss 的星标历史曲线"></a> |
| 6 | [sveltejs/svelte](https://github.com/sveltejs/svelte)<br>你写组件，编译器变出高效的网页代码<br>`Web / 前端` | +5,251 | 14.4 | 88,657 | <a href="https://www.star-history.com/#sveltejs/svelte&Date"><img src="https://api.star-history.com/svg?repos=sveltejs/svelte&type=Date" width="260" alt="sveltejs/svelte 的星标历史曲线"></a> |
| 7 | [tanstack/query](https://github.com/tanstack/query)<br>请求数据和缓存，交给它管<br>`Web / 前端` | +3,803 | 10.4 | 50,535 | <a href="https://www.star-history.com/#tanstack/query&Date"><img src="https://api.star-history.com/svg?repos=tanstack/query&type=Date" width="260" alt="tanstack/query 的星标历史曲线"></a> |
| 8 | [vuejs/core](https://github.com/vuejs/core)<br>从一个小页面开始，用多少学多少<br>`Web / 前端` | +3,603 | 9.9 | 54,841 | <a href="https://www.star-history.com/#vuejs/core&Date"><img src="https://api.star-history.com/svg?repos=vuejs/core&type=Date" width="260" alt="vuejs/core 的星标历史曲线"></a> |

### 总星标数（历史累计）

| # | 项目 | 总星标 | 星标历史 |
|---|---|---:|---|
| 1 | [facebook/react](https://github.com/facebook/react)<br>网页和 App 界面，都能用它来搭<br>`Web / 前端` | 252,347 | <a href="https://www.star-history.com/#facebook/react&Date"><img src="https://api.star-history.com/svg?repos=facebook/react&type=Date" width="260" alt="facebook/react 的星标历史曲线"></a> |
| 2 | [vercel/next.js](https://github.com/vercel/next.js)<br>用 React 做完整网站，从前到后<br>`Web / 前端` | 143,379 | <a href="https://www.star-history.com/#vercel/next.js&Date"><img src="https://api.star-history.com/svg?repos=vercel/next.js&type=Date" width="260" alt="vercel/next.js 的星标历史曲线"></a> |
| 3 | [shadcn-ui/ui](https://github.com/shadcn-ui/ui)<br>好看的组件，代码归你，随便改<br>`Web / 前端` | 127,562 | <a href="https://www.star-history.com/#shadcn-ui/ui&Date"><img src="https://api.star-history.com/svg?repos=shadcn-ui/ui&type=Date" width="260" alt="shadcn-ui/ui 的星标历史曲线"></a> |
| 4 | [tailwindlabs/tailwindcss](https://github.com/tailwindlabs/tailwindcss)<br>不写一大堆 CSS，也能做定制界面<br>`Web / 前端` | 98,214 | <a href="https://www.star-history.com/#tailwindlabs/tailwindcss&Date"><img src="https://api.star-history.com/svg?repos=tailwindlabs/tailwindcss&type=Date" width="260" alt="tailwindlabs/tailwindcss 的星标历史曲线"></a> |
| 5 | [sveltejs/svelte](https://github.com/sveltejs/svelte)<br>你写组件，编译器变出高效的网页代码<br>`Web / 前端` | 88,657 | <a href="https://www.star-history.com/#sveltejs/svelte&Date"><img src="https://api.star-history.com/svg?repos=sveltejs/svelte&type=Date" width="260" alt="sveltejs/svelte 的星标历史曲线"></a> |
| 6 | [withastro/astro](https://github.com/withastro/astro)<br>做内容型网站，页面输出更轻量<br>`Web / 前端` | 63,799 | <a href="https://www.star-history.com/#withastro/astro&Date"><img src="https://api.star-history.com/svg?repos=withastro/astro&type=Date" width="260" alt="withastro/astro 的星标历史曲线"></a> |
| 7 | [vuejs/core](https://github.com/vuejs/core)<br>从一个小页面开始，用多少学多少<br>`Web / 前端` | 54,841 | <a href="https://www.star-history.com/#vuejs/core&Date"><img src="https://api.star-history.com/svg?repos=vuejs/core&type=Date" width="260" alt="vuejs/core 的星标历史曲线"></a> |
| 8 | [tanstack/query](https://github.com/tanstack/query)<br>请求数据和缓存，交给它管<br>`Web / 前端` | 50,535 | <a href="https://www.star-history.com/#tanstack/query&Date"><img src="https://api.star-history.com/svg?repos=tanstack/query&type=Date" width="260" alt="tanstack/query 的星标历史曲线"></a> |

## 基础设施

> 容器、Kubernetes、云、网络与可观测性

### 最热新仓库（近 7 天内创建）

| # | 项目 | 创建时间（UTC） | 总星标 | 星标/天 | 星标历史 |
|---|---|---|---:|---:|---|
| 1 | [sksarvesh007/antiglaude](https://github.com/sksarvesh007/antiglaude)<br>把 Claude Code 接上 Gemini | 2026-11-03<br><sub>3.7 天</sub> | 128 | 34.5 | <a href="https://www.star-history.com/#sksarvesh007/antiglaude&Date"><img src="https://api.star-history.com/svg?repos=sksarvesh007/antiglaude&type=Date" width="260" alt="sksarvesh007/antiglaude 的星标历史曲线"></a> |

### 本周增长最快（近 7 天）

| # | 项目 | 新增星标 | 星标/天 | 总星标 | 星标历史 |
|---|---|---:|---:|---:|---|
| 1 | [prometheus/prometheus](https://github.com/prometheus/prometheus)<br>系统出问题，告警先找到你<br>`基础设施` | +420 | 60.0 | 67,293 | <a href="https://www.star-history.com/#prometheus/prometheus&Date"><img src="https://api.star-history.com/svg?repos=prometheus/prometheus&type=Date" width="260" alt="prometheus/prometheus 的星标历史曲线"></a> |
| 2 | [kubernetes/kubernetes](https://github.com/kubernetes/kubernetes)<br>容器多了，部署扩容交给它<br>`基础设施` | +402 | 57.4 | 128,884 | <a href="https://www.star-history.com/#kubernetes/kubernetes&Date"><img src="https://api.star-history.com/svg?repos=kubernetes/kubernetes&type=Date" width="260" alt="kubernetes/kubernetes 的星标历史曲线"></a> |
| 3 | [caddyserver/caddy](https://github.com/caddyserver/caddy)<br>搭网站服务器，HTTPS 自动配好<br>`基础设施` | +321 | 45.9 | 78,866 | <a href="https://www.star-history.com/#caddyserver/caddy&Date"><img src="https://api.star-history.com/svg?repos=caddyserver/caddy&type=Date" width="260" alt="caddyserver/caddy 的星标历史曲线"></a> |
| 4 | [grafana/grafana](https://github.com/grafana/grafana)<br>指标日志链路，放进一个面板<br>`基础设施` | +192 | 27.4 | 77,743 | <a href="https://www.star-history.com/#grafana/grafana&Date"><img src="https://api.star-history.com/svg?repos=grafana/grafana&type=Date" width="260" alt="grafana/grafana 的星标历史曲线"></a> |
| 5 | [docker/compose](https://github.com/docker/compose)<br>多个容器写进一个文件，一起跑<br>`基础设施` | +127 | 18.1 | 38,631 | <a href="https://www.star-history.com/#docker/compose&Date"><img src="https://api.star-history.com/svg?repos=docker/compose&type=Date" width="260" alt="docker/compose 的星标历史曲线"></a> |
| 6 | [traefik/traefik](https://github.com/traefik/traefik)<br>服务多了，流量自动分好<br>`基础设施` | +93 | 13.3 | 65,487 | <a href="https://www.star-history.com/#traefik/traefik&Date"><img src="https://api.star-history.com/svg?repos=traefik/traefik&type=Date" width="260" alt="traefik/traefik 的星标历史曲线"></a> |
| 7 | [hashicorp/terraform](https://github.com/hashicorp/terraform)<br>云资源写成代码，可审阅、可版本管理<br>`基础设施` | +85 | 12.1 | 50,155 | <a href="https://www.star-history.com/#hashicorp/terraform&Date"><img src="https://api.star-history.com/svg?repos=hashicorp/terraform&type=Date" width="260" alt="hashicorp/terraform 的星标历史曲线"></a> |
| 8 | [pulumi/pulumi](https://github.com/pulumi/pulumi)<br>用熟悉的编程语言管云资源<br>`基础设施` | +24 | 3.4 | 25,848 | <a href="https://www.star-history.com/#pulumi/pulumi&Date"><img src="https://api.star-history.com/svg?repos=pulumi/pulumi&type=Date" width="260" alt="pulumi/pulumi 的星标历史曲线"></a> |

### 本月增长最快（近 30 天）

| # | 项目 | 新增星标 | 星标/天 | 总星标 | 星标历史 |
|---|---|---:|---:|---:|---|
| 1 | [caddyserver/caddy](https://github.com/caddyserver/caddy)<br>搭网站服务器，HTTPS 自动配好<br>`基础设施` | +1,508 | 50.3 | 78,866 | <a href="https://www.star-history.com/#caddyserver/caddy&Date"><img src="https://api.star-history.com/svg?repos=caddyserver/caddy&type=Date" width="260" alt="caddyserver/caddy 的星标历史曲线"></a> |
| 2 | [kubernetes/kubernetes](https://github.com/kubernetes/kubernetes)<br>容器多了，部署扩容交给它<br>`基础设施` | +1,099 | 36.6 | 128,884 | <a href="https://www.star-history.com/#kubernetes/kubernetes&Date"><img src="https://api.star-history.com/svg?repos=kubernetes/kubernetes&type=Date" width="260" alt="kubernetes/kubernetes 的星标历史曲线"></a> |
| 3 | [prometheus/prometheus](https://github.com/prometheus/prometheus)<br>系统出问题，告警先找到你<br>`基础设施` | +987 | 32.9 | 67,293 | <a href="https://www.star-history.com/#prometheus/prometheus&Date"><img src="https://api.star-history.com/svg?repos=prometheus/prometheus&type=Date" width="260" alt="prometheus/prometheus 的星标历史曲线"></a> |
| 4 | [grafana/grafana](https://github.com/grafana/grafana)<br>指标日志链路，放进一个面板<br>`基础设施` | +777 | 25.9 | 77,743 | <a href="https://www.star-history.com/#grafana/grafana&Date"><img src="https://api.star-history.com/svg?repos=grafana/grafana&type=Date" width="260" alt="grafana/grafana 的星标历史曲线"></a> |
| 5 | [traefik/traefik](https://github.com/traefik/traefik)<br>服务多了，流量自动分好<br>`基础设施` | +485 | 16.2 | 65,487 | <a href="https://www.star-history.com/#traefik/traefik&Date"><img src="https://api.star-history.com/svg?repos=traefik/traefik&type=Date" width="260" alt="traefik/traefik 的星标历史曲线"></a> |
| 6 | [docker/compose](https://github.com/docker/compose)<br>多个容器写进一个文件，一起跑<br>`基础设施` | +429 | 14.3 | 38,631 | <a href="https://www.star-history.com/#docker/compose&Date"><img src="https://api.star-history.com/svg?repos=docker/compose&type=Date" width="260" alt="docker/compose 的星标历史曲线"></a> |
| 7 | [hashicorp/terraform](https://github.com/hashicorp/terraform)<br>云资源写成代码，可审阅、可版本管理<br>`基础设施` | +415 | 13.8 | 50,155 | <a href="https://www.star-history.com/#hashicorp/terraform&Date"><img src="https://api.star-history.com/svg?repos=hashicorp/terraform&type=Date" width="260" alt="hashicorp/terraform 的星标历史曲线"></a> |
| 8 | [pulumi/pulumi](https://github.com/pulumi/pulumi)<br>用熟悉的编程语言管云资源<br>`基础设施` | +127 | 4.2 | 25,848 | <a href="https://www.star-history.com/#pulumi/pulumi&Date"><img src="https://api.star-history.com/svg?repos=pulumi/pulumi&type=Date" width="260" alt="pulumi/pulumi 的星标历史曲线"></a> |

### 今年增长最快（近 365 天）

| # | 项目 | 新增星标 | 星标/天 | 总星标 | 星标历史 |
|---|---|---:|---:|---:|---|
| 1 | [caddyserver/caddy](https://github.com/caddyserver/caddy)<br>搭网站服务器，HTTPS 自动配好<br>`基础设施` | +12,019 | 32.9 | 78,866 | <a href="https://www.star-history.com/#caddyserver/caddy&Date"><img src="https://api.star-history.com/svg?repos=caddyserver/caddy&type=Date" width="260" alt="caddyserver/caddy 的星标历史曲线"></a> |
| 2 | [kubernetes/kubernetes](https://github.com/kubernetes/kubernetes)<br>容器多了，部署扩容交给它<br>`基础设施` | +11,767 | 32.2 | 128,884 | <a href="https://www.star-history.com/#kubernetes/kubernetes&Date"><img src="https://api.star-history.com/svg?repos=kubernetes/kubernetes&type=Date" width="260" alt="kubernetes/kubernetes 的星标历史曲线"></a> |
| 3 | [traefik/traefik](https://github.com/traefik/traefik)<br>服务多了，流量自动分好<br>`基础设施` | +8,676 | 23.8 | 65,487 | <a href="https://www.star-history.com/#traefik/traefik&Date"><img src="https://api.star-history.com/svg?repos=traefik/traefik&type=Date" width="260" alt="traefik/traefik 的星标历史曲线"></a> |
| 4 | [grafana/grafana](https://github.com/grafana/grafana)<br>指标日志链路，放进一个面板<br>`基础设施` | +7,906 | 21.7 | 77,743 | <a href="https://www.star-history.com/#grafana/grafana&Date"><img src="https://api.star-history.com/svg?repos=grafana/grafana&type=Date" width="260" alt="grafana/grafana 的星标历史曲线"></a> |
| 5 | [prometheus/prometheus](https://github.com/prometheus/prometheus)<br>系统出问题，告警先找到你<br>`基础设施` | +6,812 | 18.7 | 67,293 | <a href="https://www.star-history.com/#prometheus/prometheus&Date"><img src="https://api.star-history.com/svg?repos=prometheus/prometheus&type=Date" width="260" alt="prometheus/prometheus 的星标历史曲线"></a> |
| 6 | [hashicorp/terraform](https://github.com/hashicorp/terraform)<br>云资源写成代码，可审阅、可版本管理<br>`基础设施` | +3,785 | 10.4 | 50,155 | <a href="https://www.star-history.com/#hashicorp/terraform&Date"><img src="https://api.star-history.com/svg?repos=hashicorp/terraform&type=Date" width="260" alt="hashicorp/terraform 的星标历史曲线"></a> |
| 7 | [docker/compose](https://github.com/docker/compose)<br>多个容器写进一个文件，一起跑<br>`基础设施` | +2,655 | 7.3 | 38,631 | <a href="https://www.star-history.com/#docker/compose&Date"><img src="https://api.star-history.com/svg?repos=docker/compose&type=Date" width="260" alt="docker/compose 的星标历史曲线"></a> |
| 8 | [pulumi/pulumi](https://github.com/pulumi/pulumi)<br>用熟悉的编程语言管云资源<br>`基础设施` | +2,075 | 5.7 | 25,848 | <a href="https://www.star-history.com/#pulumi/pulumi&Date"><img src="https://api.star-history.com/svg?repos=pulumi/pulumi&type=Date" width="260" alt="pulumi/pulumi 的星标历史曲线"></a> |

### 总星标数（历史累计）

| # | 项目 | 总星标 | 星标历史 |
|---|---|---:|---|
| 1 | [kubernetes/kubernetes](https://github.com/kubernetes/kubernetes)<br>容器多了，部署扩容交给它<br>`基础设施` | 128,884 | <a href="https://www.star-history.com/#kubernetes/kubernetes&Date"><img src="https://api.star-history.com/svg?repos=kubernetes/kubernetes&type=Date" width="260" alt="kubernetes/kubernetes 的星标历史曲线"></a> |
| 2 | [caddyserver/caddy](https://github.com/caddyserver/caddy)<br>搭网站服务器，HTTPS 自动配好<br>`基础设施` | 78,866 | <a href="https://www.star-history.com/#caddyserver/caddy&Date"><img src="https://api.star-history.com/svg?repos=caddyserver/caddy&type=Date" width="260" alt="caddyserver/caddy 的星标历史曲线"></a> |
| 3 | [grafana/grafana](https://github.com/grafana/grafana)<br>指标日志链路，放进一个面板<br>`基础设施` | 77,743 | <a href="https://www.star-history.com/#grafana/grafana&Date"><img src="https://api.star-history.com/svg?repos=grafana/grafana&type=Date" width="260" alt="grafana/grafana 的星标历史曲线"></a> |
| 4 | [prometheus/prometheus](https://github.com/prometheus/prometheus)<br>系统出问题，告警先找到你<br>`基础设施` | 67,293 | <a href="https://www.star-history.com/#prometheus/prometheus&Date"><img src="https://api.star-history.com/svg?repos=prometheus/prometheus&type=Date" width="260" alt="prometheus/prometheus 的星标历史曲线"></a> |
| 5 | [traefik/traefik](https://github.com/traefik/traefik)<br>服务多了，流量自动分好<br>`基础设施` | 65,487 | <a href="https://www.star-history.com/#traefik/traefik&Date"><img src="https://api.star-history.com/svg?repos=traefik/traefik&type=Date" width="260" alt="traefik/traefik 的星标历史曲线"></a> |
| 6 | [hashicorp/terraform](https://github.com/hashicorp/terraform)<br>云资源写成代码，可审阅、可版本管理<br>`基础设施` | 50,155 | <a href="https://www.star-history.com/#hashicorp/terraform&Date"><img src="https://api.star-history.com/svg?repos=hashicorp/terraform&type=Date" width="260" alt="hashicorp/terraform 的星标历史曲线"></a> |
| 7 | [docker/compose](https://github.com/docker/compose)<br>多个容器写进一个文件，一起跑<br>`基础设施` | 38,631 | <a href="https://www.star-history.com/#docker/compose&Date"><img src="https://api.star-history.com/svg?repos=docker/compose&type=Date" width="260" alt="docker/compose 的星标历史曲线"></a> |
| 8 | [pulumi/pulumi](https://github.com/pulumi/pulumi)<br>用熟悉的编程语言管云资源<br>`基础设施` | 25,848 | <a href="https://www.star-history.com/#pulumi/pulumi&Date"><img src="https://api.star-history.com/svg?repos=pulumi/pulumi&type=Date" width="260" alt="pulumi/pulumi 的星标历史曲线"></a> |

## 设计 / 创意

> 设计系统、绘图、动画与创意工具

### 最热新仓库（近 7 天内创建）

| # | 项目 | 创建时间（UTC） | 总星标 | 星标/天 | 星标历史 |
|---|---|---|---:|---:|---|
| 1 | [kubai087/kubai-icons](https://github.com/kubai087/kubai-icons)<br>用 Claude 技能统一图标风格 | 2026-11-03<br><sub>4.1 天</sub> | 252 | 61.2 | <a href="https://www.star-history.com/#kubai087/kubai-icons&Date"><img src="https://api.star-history.com/svg?repos=kubai087/kubai-icons&type=Date" width="260" alt="kubai087/kubai-icons 的星标历史曲线"></a> |
| 2 | [DominikScholz/open-bot-avatar](https://github.com/DominikScholz/open-bot-avatar)<br>给互动智能体轻松渲染虚拟形象 | 2026-11-02<br><sub>4.8 天</sub> | 276 | 57.2 | <a href="https://www.star-history.com/#DominikScholz/open-bot-avatar&Date"><img src="https://api.star-history.com/svg?repos=DominikScholz/open-bot-avatar&type=Date" width="260" alt="DominikScholz/open-bot-avatar 的星标历史曲线"></a> |
| 3 | [leodavincs/kalem](https://github.com/leodavincs/kalem)<br>给视频每个场景选合适的引擎 | 2026-11-01<br><sub>5.9 天</sub> | 107 | 18.1 | <a href="https://www.star-history.com/#leodavincs/kalem&Date"><img src="https://api.star-history.com/svg?repos=leodavincs/kalem&type=Date" width="260" alt="leodavincs/kalem 的星标历史曲线"></a> |

### 本周增长最快（近 7 天）

| # | 项目 | 新增星标 | 星标/天 | 总星标 | 星标历史 |
|---|---|---:|---:|---:|---|
| 1 | [excalidraw/excalidraw](https://github.com/excalidraw/excalidraw)<br>打开就画，像在纸上随手画图<br>`设计 / 创意` | +454 | 64.9 | 135,275 | <a href="https://www.star-history.com/#excalidraw/excalidraw&Date"><img src="https://api.star-history.com/svg?repos=excalidraw/excalidraw&type=Date" width="260" alt="excalidraw/excalidraw 的星标历史曲线"></a> |
| 2 | [penpot/penpot](https://github.com/penpot/penpot)<br>团队一起做设计，用开源平台<br>`设计 / 创意` | +281 | 40.1 | 62,153 | <a href="https://www.star-history.com/#penpot/penpot&Date"><img src="https://api.star-history.com/svg?repos=penpot/penpot&type=Date" width="260" alt="penpot/penpot 的星标历史曲线"></a> |
| 3 | [lucide-icons/lucide](https://github.com/lucide-icons/lucide)<br>一套图标风格统一，拿来就用<br>`设计 / 创意` | +219 | 31.3 | 25,619 | <a href="https://www.star-history.com/#lucide-icons/lucide&Date"><img src="https://api.star-history.com/svg?repos=lucide-icons/lucide&type=Date" width="260" alt="lucide-icons/lucide 的星标历史曲线"></a> |
| 4 | [jgraph/drawio](https://github.com/jgraph/drawio)<br>画图和白板，一个编辑器搞定<br>`设计 / 创意` | +145 | 20.7 | 9,234 | <a href="https://www.star-history.com/#jgraph/drawio&Date"><img src="https://api.star-history.com/svg?repos=jgraph/drawio&type=Date" width="260" alt="jgraph/drawio 的星标历史曲线"></a> |
| 5 | [airbnb/lottie-web](https://github.com/airbnb/lottie-web)<br>AE 做的动画，直接放进网页<br>`设计 / 创意` | +85 | 12.1 | 32,373 | <a href="https://www.star-history.com/#airbnb/lottie-web&Date"><img src="https://api.star-history.com/svg?repos=airbnb/lottie-web&type=Date" width="260" alt="airbnb/lottie-web 的星标历史曲线"></a> |
| 6 | [saadeghi/daisyui](https://github.com/saadeghi/daisyui)<br>Tailwind 也有现成组件可挑<br>`设计 / 创意` | +78 | 11.1 | 42,764 | <a href="https://www.star-history.com/#saadeghi/daisyui&Date"><img src="https://api.star-history.com/svg?repos=saadeghi/daisyui&type=Date" width="260" alt="saadeghi/daisyui 的星标历史曲线"></a> |
| 7 | [phosphor-icons/homepage](https://github.com/phosphor-icons/homepage)<br>一整套灵活的图标，人人可用<br>`设计 / 创意` | +32 | 4.6 | 7,775 | <a href="https://www.star-history.com/#phosphor-icons/homepage&Date"><img src="https://api.star-history.com/svg?repos=phosphor-icons/homepage&type=Date" width="260" alt="phosphor-icons/homepage 的星标历史曲线"></a> |
| 8 | [lottiefiles/lottie-ios](https://github.com/lottiefiles/lottie-ios)<br>AE 做的动画，直接放进 iOS<br>`设计 / 创意` | +0 | 0.0 | 43 | <a href="https://www.star-history.com/#lottiefiles/lottie-ios&Date"><img src="https://api.star-history.com/svg?repos=lottiefiles/lottie-ios&type=Date" width="260" alt="lottiefiles/lottie-ios 的星标历史曲线"></a> |

### 本月增长最快（近 30 天）

| # | 项目 | 新增星标 | 星标/天 | 总星标 | 星标历史 |
|---|---|---:|---:|---:|---|
| 1 | [excalidraw/excalidraw](https://github.com/excalidraw/excalidraw)<br>打开就画，像在纸上随手画图<br>`设计 / 创意` | +2,011 | 67.0 | 135,275 | <a href="https://www.star-history.com/#excalidraw/excalidraw&Date"><img src="https://api.star-history.com/svg?repos=excalidraw/excalidraw&type=Date" width="260" alt="excalidraw/excalidraw 的星标历史曲线"></a> |
| 2 | [penpot/penpot](https://github.com/penpot/penpot)<br>团队一起做设计，用开源平台<br>`设计 / 创意` | +1,497 | 49.9 | 62,153 | <a href="https://www.star-history.com/#penpot/penpot&Date"><img src="https://api.star-history.com/svg?repos=penpot/penpot&type=Date" width="260" alt="penpot/penpot 的星标历史曲线"></a> |
| 3 | [lucide-icons/lucide](https://github.com/lucide-icons/lucide)<br>一套图标风格统一，拿来就用<br>`设计 / 创意` | +769 | 25.6 | 25,619 | <a href="https://www.star-history.com/#lucide-icons/lucide&Date"><img src="https://api.star-history.com/svg?repos=lucide-icons/lucide&type=Date" width="260" alt="lucide-icons/lucide 的星标历史曲线"></a> |
| 4 | [jgraph/drawio](https://github.com/jgraph/drawio)<br>画图和白板，一个编辑器搞定<br>`设计 / 创意` | +639 | 21.3 | 9,234 | <a href="https://www.star-history.com/#jgraph/drawio&Date"><img src="https://api.star-history.com/svg?repos=jgraph/drawio&type=Date" width="260" alt="jgraph/drawio 的星标历史曲线"></a> |
| 5 | [saadeghi/daisyui](https://github.com/saadeghi/daisyui)<br>Tailwind 也有现成组件可挑<br>`设计 / 创意` | +295 | 9.8 | 42,764 | <a href="https://www.star-history.com/#saadeghi/daisyui&Date"><img src="https://api.star-history.com/svg?repos=saadeghi/daisyui&type=Date" width="260" alt="saadeghi/daisyui 的星标历史曲线"></a> |
| 6 | [airbnb/lottie-web](https://github.com/airbnb/lottie-web)<br>AE 做的动画，直接放进网页<br>`设计 / 创意` | +263 | 8.8 | 32,373 | <a href="https://www.star-history.com/#airbnb/lottie-web&Date"><img src="https://api.star-history.com/svg?repos=airbnb/lottie-web&type=Date" width="260" alt="airbnb/lottie-web 的星标历史曲线"></a> |
| 7 | [phosphor-icons/homepage](https://github.com/phosphor-icons/homepage)<br>一整套灵活的图标，人人可用<br>`设计 / 创意` | +169 | 5.6 | 7,775 | <a href="https://www.star-history.com/#phosphor-icons/homepage&Date"><img src="https://api.star-history.com/svg?repos=phosphor-icons/homepage&type=Date" width="260" alt="phosphor-icons/homepage 的星标历史曲线"></a> |
| 8 | [lottiefiles/lottie-ios](https://github.com/lottiefiles/lottie-ios)<br>AE 做的动画，直接放进 iOS<br>`设计 / 创意` | +0 | 0.0 | 43 | <a href="https://www.star-history.com/#lottiefiles/lottie-ios&Date"><img src="https://api.star-history.com/svg?repos=lottiefiles/lottie-ios&type=Date" width="260" alt="lottiefiles/lottie-ios 的星标历史曲线"></a> |

### 今年增长最快（近 365 天）

| # | 项目 | 新增星标 | 星标/天 | 总星标 | 星标历史 |
|---|---|---:|---:|---:|---|
| 1 | [excalidraw/excalidraw](https://github.com/excalidraw/excalidraw)<br>打开就画，像在纸上随手画图<br>`设计 / 创意` | +27,023 | 74.0 | 135,275 | <a href="https://www.star-history.com/#excalidraw/excalidraw&Date"><img src="https://api.star-history.com/svg?repos=excalidraw/excalidraw&type=Date" width="260" alt="excalidraw/excalidraw 的星标历史曲线"></a> |
| 2 | [penpot/penpot](https://github.com/penpot/penpot)<br>团队一起做设计，用开源平台<br>`设计 / 创意` | +21,833 | 59.8 | 62,153 | <a href="https://www.star-history.com/#penpot/penpot&Date"><img src="https://api.star-history.com/svg?repos=penpot/penpot&type=Date" width="260" alt="penpot/penpot 的星标历史曲线"></a> |
| 3 | [jgraph/drawio](https://github.com/jgraph/drawio)<br>画图和白板，一个编辑器搞定<br>`设计 / 创意` | +6,555 | 18.0 | 9,234 | <a href="https://www.star-history.com/#jgraph/drawio&Date"><img src="https://api.star-history.com/svg?repos=jgraph/drawio&type=Date" width="260" alt="jgraph/drawio 的星标历史曲线"></a> |
| 4 | [lucide-icons/lucide](https://github.com/lucide-icons/lucide)<br>一套图标风格统一，拿来就用<br>`设计 / 创意` | +6,332 | 17.3 | 25,619 | <a href="https://www.star-history.com/#lucide-icons/lucide&Date"><img src="https://api.star-history.com/svg?repos=lucide-icons/lucide&type=Date" width="260" alt="lucide-icons/lucide 的星标历史曲线"></a> |
| 5 | [saadeghi/daisyui](https://github.com/saadeghi/daisyui)<br>Tailwind 也有现成组件可挑<br>`设计 / 创意` | +4,229 | 11.6 | 42,764 | <a href="https://www.star-history.com/#saadeghi/daisyui&Date"><img src="https://api.star-history.com/svg?repos=saadeghi/daisyui&type=Date" width="260" alt="saadeghi/daisyui 的星标历史曲线"></a> |
| 6 | [phosphor-icons/homepage](https://github.com/phosphor-icons/homepage)<br>一整套灵活的图标，人人可用<br>`设计 / 创意` | +2,199 | 6.0 | 7,775 | <a href="https://www.star-history.com/#phosphor-icons/homepage&Date"><img src="https://api.star-history.com/svg?repos=phosphor-icons/homepage&type=Date" width="260" alt="phosphor-icons/homepage 的星标历史曲线"></a> |
| 7 | [airbnb/lottie-web](https://github.com/airbnb/lottie-web)<br>AE 做的动画，直接放进网页<br>`设计 / 创意` | +1,124 | 3.1 | 32,373 | <a href="https://www.star-history.com/#airbnb/lottie-web&Date"><img src="https://api.star-history.com/svg?repos=airbnb/lottie-web&type=Date" width="260" alt="airbnb/lottie-web 的星标历史曲线"></a> |
| 8 | [lottiefiles/lottie-ios](https://github.com/lottiefiles/lottie-ios)<br>AE 做的动画，直接放进 iOS<br>`设计 / 创意` | +1 | 0.0 | 43 | <a href="https://www.star-history.com/#lottiefiles/lottie-ios&Date"><img src="https://api.star-history.com/svg?repos=lottiefiles/lottie-ios&type=Date" width="260" alt="lottiefiles/lottie-ios 的星标历史曲线"></a> |

### 总星标数（历史累计）

| # | 项目 | 总星标 | 星标历史 |
|---|---|---:|---|
| 1 | [excalidraw/excalidraw](https://github.com/excalidraw/excalidraw)<br>打开就画，像在纸上随手画图<br>`设计 / 创意` | 135,275 | <a href="https://www.star-history.com/#excalidraw/excalidraw&Date"><img src="https://api.star-history.com/svg?repos=excalidraw/excalidraw&type=Date" width="260" alt="excalidraw/excalidraw 的星标历史曲线"></a> |
| 2 | [penpot/penpot](https://github.com/penpot/penpot)<br>团队一起做设计，用开源平台<br>`设计 / 创意` | 62,153 | <a href="https://www.star-history.com/#penpot/penpot&Date"><img src="https://api.star-history.com/svg?repos=penpot/penpot&type=Date" width="260" alt="penpot/penpot 的星标历史曲线"></a> |
| 3 | [saadeghi/daisyui](https://github.com/saadeghi/daisyui)<br>Tailwind 也有现成组件可挑<br>`设计 / 创意` | 42,764 | <a href="https://www.star-history.com/#saadeghi/daisyui&Date"><img src="https://api.star-history.com/svg?repos=saadeghi/daisyui&type=Date" width="260" alt="saadeghi/daisyui 的星标历史曲线"></a> |
| 4 | [airbnb/lottie-web](https://github.com/airbnb/lottie-web)<br>AE 做的动画，直接放进网页<br>`设计 / 创意` | 32,373 | <a href="https://www.star-history.com/#airbnb/lottie-web&Date"><img src="https://api.star-history.com/svg?repos=airbnb/lottie-web&type=Date" width="260" alt="airbnb/lottie-web 的星标历史曲线"></a> |
| 5 | [lucide-icons/lucide](https://github.com/lucide-icons/lucide)<br>一套图标风格统一，拿来就用<br>`设计 / 创意` | 25,619 | <a href="https://www.star-history.com/#lucide-icons/lucide&Date"><img src="https://api.star-history.com/svg?repos=lucide-icons/lucide&type=Date" width="260" alt="lucide-icons/lucide 的星标历史曲线"></a> |
| 6 | [jgraph/drawio](https://github.com/jgraph/drawio)<br>画图和白板，一个编辑器搞定<br>`设计 / 创意` | 9,234 | <a href="https://www.star-history.com/#jgraph/drawio&Date"><img src="https://api.star-history.com/svg?repos=jgraph/drawio&type=Date" width="260" alt="jgraph/drawio 的星标历史曲线"></a> |
| 7 | [phosphor-icons/homepage](https://github.com/phosphor-icons/homepage)<br>一整套灵活的图标，人人可用<br>`设计 / 创意` | 7,775 | <a href="https://www.star-history.com/#phosphor-icons/homepage&Date"><img src="https://api.star-history.com/svg?repos=phosphor-icons/homepage&type=Date" width="260" alt="phosphor-icons/homepage 的星标历史曲线"></a> |
| 8 | [lottiefiles/lottie-ios](https://github.com/lottiefiles/lottie-ios)<br>AE 做的动画，直接放进 iOS<br>`设计 / 创意` | 43 | <a href="https://www.star-history.com/#lottiefiles/lottie-ios&Date"><img src="https://api.star-history.com/svg?repos=lottiefiles/lottie-ios&type=Date" width="260" alt="lottiefiles/lottie-ios 的星标历史曲线"></a> |

## 数据

> 数据库、分析、ETL 与数据工程

### 最热新仓库（近 7 天内创建）

本次运行中没有符合条件的新仓库。

### 本周增长最快（近 7 天）

| # | 项目 | 新增星标 | 星标/天 | 总星标 | 星标历史 |
|---|---|---:|---:|---:|---|
| 1 | [duckdb/duckdb](https://github.com/duckdb/duckdb)<br>不搭数据库服务，也能跑 SQL 分析<br>`数据` | +207 | 29.6 | 42,882 | <a href="https://www.star-history.com/#duckdb/duckdb&Date"><img src="https://api.star-history.com/svg?repos=duckdb/duckdb&type=Date" width="260" alt="duckdb/duckdb 的星标历史曲线"></a> |
| 2 | [ClickHouse/ClickHouse](https://github.com/ClickHouse/ClickHouse)<br>大量数据实时分析，用开源的<br>`数据` | +134 | 19.1 | 50,800 | <a href="https://www.star-history.com/#ClickHouse/ClickHouse&Date"><img src="https://api.star-history.com/svg?repos=ClickHouse/ClickHouse&type=Date" width="260" alt="ClickHouse/ClickHouse 的星标历史曲线"></a> |
| 3 | [apache/kafka](https://github.com/apache/kafka)<br>系统之间的事件流，交给它来传<br>`数据` | +99 | 14.1 | 34,191 | <a href="https://www.star-history.com/#apache/kafka&Date"><img src="https://api.star-history.com/svg?repos=apache/kafka&type=Date" width="260" alt="apache/kafka 的星标历史曲线"></a> |
| 4 | [apache/superset](https://github.com/apache/superset)<br>数据看不懂，做成图就明白<br>`数据` | +95 | 13.6 | 75,449 | <a href="https://www.star-history.com/#apache/superset&Date"><img src="https://api.star-history.com/svg?repos=apache/superset&type=Date" width="260" alt="apache/superset 的星标历史曲线"></a> |
| 5 | [pola-rs/polars](https://github.com/pola-rs/polars)<br>表格数据处理快，不用干等<br>`数据` | +60 | 8.6 | 40,277 | <a href="https://www.star-history.com/#pola-rs/polars&Date"><img src="https://api.star-history.com/svg?repos=pola-rs/polars&type=Date" width="260" alt="pola-rs/polars 的星标历史曲线"></a> |
| 6 | [dbt-labs/dbt-core](https://github.com/dbt-labs/dbt-core)<br>数据转换，照软件工程的做法来<br>`数据` | +32 | 4.6 | 14,130 | <a href="https://www.star-history.com/#dbt-labs/dbt-core&Date"><img src="https://api.star-history.com/svg?repos=dbt-labs/dbt-core&type=Date" width="260" alt="dbt-labs/dbt-core 的星标历史曲线"></a> |
| 7 | [apache/arrow](https://github.com/apache/arrow)<br>不同语言之间，数据直接通用<br>`数据` | +21 | 3.0 | 17,277 | <a href="https://www.star-history.com/#apache/arrow&Date"><img src="https://api.star-history.com/svg?repos=apache/arrow&type=Date" width="260" alt="apache/arrow 的星标历史曲线"></a> |
| 8 | [jupyter/notebook](https://github.com/jupyter/notebook)<br>在网页里写代码，边写边看结果<br>`数据` | +6 | 0.9 | 13,461 | <a href="https://www.star-history.com/#jupyter/notebook&Date"><img src="https://api.star-history.com/svg?repos=jupyter/notebook&type=Date" width="260" alt="jupyter/notebook 的星标历史曲线"></a> |

### 本月增长最快（近 30 天）

| # | 项目 | 新增星标 | 星标/天 | 总星标 | 星标历史 |
|---|---|---:|---:|---:|---|
| 1 | [duckdb/duckdb](https://github.com/duckdb/duckdb)<br>不搭数据库服务，也能跑 SQL 分析<br>`数据` | +973 | 32.4 | 42,882 | <a href="https://www.star-history.com/#duckdb/duckdb&Date"><img src="https://api.star-history.com/svg?repos=duckdb/duckdb&type=Date" width="260" alt="duckdb/duckdb 的星标历史曲线"></a> |
| 2 | [ClickHouse/ClickHouse](https://github.com/ClickHouse/ClickHouse)<br>大量数据实时分析，用开源的<br>`数据` | +601 | 20.0 | 50,800 | <a href="https://www.star-history.com/#ClickHouse/ClickHouse&Date"><img src="https://api.star-history.com/svg?repos=ClickHouse/ClickHouse&type=Date" width="260" alt="ClickHouse/ClickHouse 的星标历史曲线"></a> |
| 3 | [apache/superset](https://github.com/apache/superset)<br>数据看不懂，做成图就明白<br>`数据` | +477 | 15.9 | 75,449 | <a href="https://www.star-history.com/#apache/superset&Date"><img src="https://api.star-history.com/svg?repos=apache/superset&type=Date" width="260" alt="apache/superset 的星标历史曲线"></a> |
| 4 | [apache/kafka](https://github.com/apache/kafka)<br>系统之间的事件流，交给它来传<br>`数据` | +343 | 11.4 | 34,191 | <a href="https://www.star-history.com/#apache/kafka&Date"><img src="https://api.star-history.com/svg?repos=apache/kafka&type=Date" width="260" alt="apache/kafka 的星标历史曲线"></a> |
| 5 | [pola-rs/polars](https://github.com/pola-rs/polars)<br>表格数据处理快，不用干等<br>`数据` | +327 | 10.9 | 40,277 | <a href="https://www.star-history.com/#pola-rs/polars&Date"><img src="https://api.star-history.com/svg?repos=pola-rs/polars&type=Date" width="260" alt="pola-rs/polars 的星标历史曲线"></a> |
| 6 | [dbt-labs/dbt-core](https://github.com/dbt-labs/dbt-core)<br>数据转换，照软件工程的做法来<br>`数据` | +174 | 5.8 | 14,130 | <a href="https://www.star-history.com/#dbt-labs/dbt-core&Date"><img src="https://api.star-history.com/svg?repos=dbt-labs/dbt-core&type=Date" width="260" alt="dbt-labs/dbt-core 的星标历史曲线"></a> |
| 7 | [apache/arrow](https://github.com/apache/arrow)<br>不同语言之间，数据直接通用<br>`数据` | +113 | 3.8 | 17,277 | <a href="https://www.star-history.com/#apache/arrow&Date"><img src="https://api.star-history.com/svg?repos=apache/arrow&type=Date" width="260" alt="apache/arrow 的星标历史曲线"></a> |
| 8 | [jupyter/notebook](https://github.com/jupyter/notebook)<br>在网页里写代码，边写边看结果<br>`数据` | +62 | 2.1 | 13,461 | <a href="https://www.star-history.com/#jupyter/notebook&Date"><img src="https://api.star-history.com/svg?repos=jupyter/notebook&type=Date" width="260" alt="jupyter/notebook 的星标历史曲线"></a> |

### 今年增长最快（近 365 天）

| # | 项目 | 新增星标 | 星标/天 | 总星标 | 星标历史 |
|---|---|---:|---:|---:|---|
| 1 | [duckdb/duckdb](https://github.com/duckdb/duckdb)<br>不搭数据库服务，也能跑 SQL 分析<br>`数据` | +9,386 | 25.7 | 42,882 | <a href="https://www.star-history.com/#duckdb/duckdb&Date"><img src="https://api.star-history.com/svg?repos=duckdb/duckdb&type=Date" width="260" alt="duckdb/duckdb 的星标历史曲线"></a> |
| 2 | [ClickHouse/ClickHouse](https://github.com/ClickHouse/ClickHouse)<br>大量数据实时分析，用开源的<br>`数据` | +7,587 | 20.8 | 50,800 | <a href="https://www.star-history.com/#ClickHouse/ClickHouse&Date"><img src="https://api.star-history.com/svg?repos=ClickHouse/ClickHouse&type=Date" width="260" alt="ClickHouse/ClickHouse 的星标历史曲线"></a> |
| 3 | [apache/superset](https://github.com/apache/superset)<br>数据看不懂，做成图就明白<br>`数据` | +7,404 | 20.3 | 75,449 | <a href="https://www.star-history.com/#apache/superset&Date"><img src="https://api.star-history.com/svg?repos=apache/superset&type=Date" width="260" alt="apache/superset 的星标历史曲线"></a> |
| 4 | [pola-rs/polars](https://github.com/pola-rs/polars)<br>表格数据处理快，不用干等<br>`数据` | +4,827 | 13.2 | 40,277 | <a href="https://www.star-history.com/#pola-rs/polars&Date"><img src="https://api.star-history.com/svg?repos=pola-rs/polars&type=Date" width="260" alt="pola-rs/polars 的星标历史曲线"></a> |
| 5 | [apache/kafka](https://github.com/apache/kafka)<br>系统之间的事件流，交给它来传<br>`数据` | +3,337 | 9.1 | 34,191 | <a href="https://www.star-history.com/#apache/kafka&Date"><img src="https://api.star-history.com/svg?repos=apache/kafka&type=Date" width="260" alt="apache/kafka 的星标历史曲线"></a> |
| 6 | [dbt-labs/dbt-core](https://github.com/dbt-labs/dbt-core)<br>数据转换，照软件工程的做法来<br>`数据` | +2,463 | 6.7 | 14,130 | <a href="https://www.star-history.com/#dbt-labs/dbt-core&Date"><img src="https://api.star-history.com/svg?repos=dbt-labs/dbt-core&type=Date" width="260" alt="dbt-labs/dbt-core 的星标历史曲线"></a> |
| 7 | [apache/arrow](https://github.com/apache/arrow)<br>不同语言之间，数据直接通用<br>`数据` | +1,312 | 3.6 | 17,277 | <a href="https://www.star-history.com/#apache/arrow&Date"><img src="https://api.star-history.com/svg?repos=apache/arrow&type=Date" width="260" alt="apache/arrow 的星标历史曲线"></a> |
| 8 | [jupyter/notebook](https://github.com/jupyter/notebook)<br>在网页里写代码，边写边看结果<br>`数据` | +892 | 2.4 | 13,461 | <a href="https://www.star-history.com/#jupyter/notebook&Date"><img src="https://api.star-history.com/svg?repos=jupyter/notebook&type=Date" width="260" alt="jupyter/notebook 的星标历史曲线"></a> |

### 总星标数（历史累计）

| # | 项目 | 总星标 | 星标历史 |
|---|---|---:|---|
| 1 | [apache/superset](https://github.com/apache/superset)<br>数据看不懂，做成图就明白<br>`数据` | 75,449 | <a href="https://www.star-history.com/#apache/superset&Date"><img src="https://api.star-history.com/svg?repos=apache/superset&type=Date" width="260" alt="apache/superset 的星标历史曲线"></a> |
| 2 | [ClickHouse/ClickHouse](https://github.com/ClickHouse/ClickHouse)<br>大量数据实时分析，用开源的<br>`数据` | 50,800 | <a href="https://www.star-history.com/#ClickHouse/ClickHouse&Date"><img src="https://api.star-history.com/svg?repos=ClickHouse/ClickHouse&type=Date" width="260" alt="ClickHouse/ClickHouse 的星标历史曲线"></a> |
| 3 | [duckdb/duckdb](https://github.com/duckdb/duckdb)<br>不搭数据库服务，也能跑 SQL 分析<br>`数据` | 42,882 | <a href="https://www.star-history.com/#duckdb/duckdb&Date"><img src="https://api.star-history.com/svg?repos=duckdb/duckdb&type=Date" width="260" alt="duckdb/duckdb 的星标历史曲线"></a> |
| 4 | [pola-rs/polars](https://github.com/pola-rs/polars)<br>表格数据处理快，不用干等<br>`数据` | 40,277 | <a href="https://www.star-history.com/#pola-rs/polars&Date"><img src="https://api.star-history.com/svg?repos=pola-rs/polars&type=Date" width="260" alt="pola-rs/polars 的星标历史曲线"></a> |
| 5 | [apache/kafka](https://github.com/apache/kafka)<br>系统之间的事件流，交给它来传<br>`数据` | 34,191 | <a href="https://www.star-history.com/#apache/kafka&Date"><img src="https://api.star-history.com/svg?repos=apache/kafka&type=Date" width="260" alt="apache/kafka 的星标历史曲线"></a> |
| 6 | [apache/arrow](https://github.com/apache/arrow)<br>不同语言之间，数据直接通用<br>`数据` | 17,277 | <a href="https://www.star-history.com/#apache/arrow&Date"><img src="https://api.star-history.com/svg?repos=apache/arrow&type=Date" width="260" alt="apache/arrow 的星标历史曲线"></a> |
| 7 | [dbt-labs/dbt-core](https://github.com/dbt-labs/dbt-core)<br>数据转换，照软件工程的做法来<br>`数据` | 14,130 | <a href="https://www.star-history.com/#dbt-labs/dbt-core&Date"><img src="https://api.star-history.com/svg?repos=dbt-labs/dbt-core&type=Date" width="260" alt="dbt-labs/dbt-core 的星标历史曲线"></a> |
| 8 | [jupyter/notebook](https://github.com/jupyter/notebook)<br>在网页里写代码，边写边看结果<br>`数据` | 13,461 | <a href="https://www.star-history.com/#jupyter/notebook&Date"><img src="https://api.star-history.com/svg?repos=jupyter/notebook&type=Date" width="260" alt="jupyter/notebook 的星标历史曲线"></a> |

---

如果它帮你省了时间，请给仓库点个星标，让更多人找得到。

如何引用：见 [CITATION.cff](CITATION.cff)。

数据怎么算和如何参与：[docs/HOW_IT_WORKS.zh-Hans.md](docs/HOW_IT_WORKS.zh-Hans.md)。新仓库规则：[docs/NEW_ARRIVALS.md](docs/NEW_ARRIVALS.md)。分类说明：[docs/CATEGORIES.md](docs/CATEGORIES.md)。提交改动：[CONTRIBUTING.md](CONTRIBUTING.md)。
