[English](README.md) | **简体中文** | [繁體中文](README.zh-Hant.md) | [日本語](README.ja.md) | [한국어](README.ko.md)

# GitHub 涨星榜 / GitHub Risers

<img src=".github/social-preview.png" alt="GitHub 涨星榜 / GitHub Risers" width="640">

[![MIT](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE) [![CI](https://github.com/jammyfu/github-risers/actions/workflows/ci.yml/badge.svg)](https://github.com/jammyfu/github-risers/actions/workflows/ci.yml) [![updated](https://img.shields.io/badge/dynamic/json?url=https%3A%2F%2Fraw.githubusercontent.com%2Fjammyfu%2Fgithub-risers%2Fmain%2Fdata%2Fstats.json&query=%24.today_utc&label=updated&color=brightgreen)](latest/rankings.zh-Hans.md)

按每天新增星标（而不是总星标）给 GitHub 仓库排名：AI 在前，其后是开发者工具、安全、Web / 前端、基础设施、设计 / 创意和数据；每天更新两次。

数据取自 2026-11-03 21:28（UTC）。每天两次：北京时间 0 点（UTC+8）、洛杉矶时间 0 点（America/Los_Angeles）。

[网站](https://jammyfu.github.io/github-risers/) · [运作方式](docs/HOW_IT_WORKS.zh-Hans.md) · [事实速查](docs/FACTS.md) · [历史榜单](rankings/README.zh-Hans.md) · [最新快照](latest/rankings.zh-Hans.md)

## 本期各类榜首

| 分类 | 新仓库第 1 名（7 天） | 本周第 1 名 | 本月第 1 名 | 今年第 1 名 | 总星标第 1 名 |
|---|---|---|---|---|---|
| **[人工智能](#人工智能)** ★ 主榜 | [wangzan101/Mika](https://github.com/wangzan101/Mika)<br>1,139/天 | [morluto/rea](https://github.com/morluto/rea)<br>4,514/天 | [morluto/rea](https://github.com/morluto/rea)<br>14,121/天 | [deepseek-ai/deepseek-harness](https://github.com/deepseek-ai/deepseek-harness)<br>3,295/天 | [morluto/rea](https://github.com/morluto/rea)<br>426,698 ★ |
| **[开发者工具](#开发者工具)** | [Verlintas/NOIR](https://github.com/Verlintas/NOIR)<br>584/天 | [zed-industries/zed](https://github.com/zed-industries/zed)<br>59.3/天 | [zed-industries/zed](https://github.com/zed-industries/zed)<br>54.1/天 | [zed-industries/zed](https://github.com/zed-industries/zed)<br>70.3/天 | [oven-sh/bun](https://github.com/oven-sh/bun)<br>96,532 ★ |
| **[安全](#安全)** | 无 | [projectdiscovery/nuclei](https://github.com/projectdiscovery/nuclei)<br>29.4/天 | [projectdiscovery/nuclei](https://github.com/projectdiscovery/nuclei)<br>30.7/天 | [aquasecurity/trivy](https://github.com/aquasecurity/trivy)<br>27.7/天 | [aquasecurity/trivy](https://github.com/aquasecurity/trivy)<br>38,941 ★ |
| **[Web / 前端](#web--前端)** | [mofan6/Moect](https://github.com/mofan6/Moect)<br>65.3/天 | [shadcn-ui/ui](https://github.com/shadcn-ui/ui)<br>94.9/天 | [shadcn-ui/ui](https://github.com/shadcn-ui/ui)<br>88.4/天 | [shadcn-ui/ui](https://github.com/shadcn-ui/ui)<br>83.2/天 | [facebook/react](https://github.com/facebook/react)<br>251,900 ★ |
| **[基础设施](#基础设施)** | [narratarr/narratarr](https://github.com/narratarr/narratarr)<br>16.5/天 | [caddyserver/caddy](https://github.com/caddyserver/caddy)<br>36.4/天 | [caddyserver/caddy](https://github.com/caddyserver/caddy)<br>84.4/天 | [caddyserver/caddy](https://github.com/caddyserver/caddy)<br>32.6/天 | [kubernetes/kubernetes](https://github.com/kubernetes/kubernetes)<br>128,638 ★ |
| **[设计 / 创意](#设计--创意)** | [patch-gg/pixelfx](https://github.com/patch-gg/pixelfx)<br>882/天 | [excalidraw/excalidraw](https://github.com/excalidraw/excalidraw)<br>72.0/天 | [excalidraw/excalidraw](https://github.com/excalidraw/excalidraw)<br>66.9/天 | [excalidraw/excalidraw](https://github.com/excalidraw/excalidraw)<br>74.2/天 | [excalidraw/excalidraw](https://github.com/excalidraw/excalidraw)<br>135,112 ★ |
| **[数据](#数据)** | 无 | [duckdb/duckdb](https://github.com/duckdb/duckdb)<br>28.0/天 | [duckdb/duckdb](https://github.com/duckdb/duckdb)<br>31.5/天 | [duckdb/duckdb](https://github.com/duckdb/duckdb)<br>25.7/天 | [apache/superset](https://github.com/apache/superset)<br>75,398 ★ |

这里每张榜只列前 10 名，完整的前 20 名见 [latest/rankings.zh-Hans.md](latest/rankings.zh-Hans.md)。

表里每个项目只留一句话；完整介绍（含工具名、技术细节）见 [docs/DETAILS.zh-Hans.md](docs/DETAILS.zh-Hans.md)。

## 常见问题

### GitHub 涨星榜是什么？

按每天新增星标、而不是总星标给 GitHub 仓库排名的榜单。AI 是主榜，后面还有六个分类；数据由脚本从 GitHub API 生成。 [了解更多](docs/FAQ.md#what-is-github-risers)

### 和 GitHub Trending 有什么不同？

GitHub Trending 是 GitHub 官方页面；GitHub 涨星榜是独立的开源项目，规则公开，有五种语言，并保存每次更新的历史。它与 GitHub 官方没有关联。 [了解更多](docs/FAQ.md#is-it-the-same-as-github-trending)

### 多久更新一次？

每天两次，北京时间 0 点和洛杉矶时间 0 点；每次运行都会存档。 [了解更多](docs/FAQ.md#how-often-is-it-updated)

### 数据怎么算？

取最近 7、30 或 365 个完整 UTC 日的新增星标，再除以天数。数字全部来自 GitHub API，没有手填或估算。 [了解更多](docs/FAQ.md#how-is-the-growth-rate-computed)

### 怎么看、怎么参与？

看下面的榜，完整前 20 名在 latest/。要收录项目，改 data/projects.json（五种语言）并发 pull request。 [了解更多](docs/FAQ.md#how-can-i-suggest-a-project-or-report-a-mistake)

## 人工智能

> 大模型、智能体、MCP、编程助手与生成式 AI

### 最热新仓库（近 7 天内创建）

| # | 项目 | 创建时间（UTC） | 总星标 | 星标/天 | 星标历史 |
|---|---|---|---:|---:|---|
| 1 | [wangzan101/Mika](https://github.com/wangzan101/Mika)<br>手机琐事太多？让智能体替你操作应用 | 2026-10-29<br><sub>5.3 天</sub> | 6,021 | 1,138.7 | <a href="https://www.star-history.com/#wangzan101/Mika&Date"><img src="https://api.star-history.com/svg?repos=wangzan101/Mika&type=Date" width="260" alt="wangzan101/Mika 的星标历史曲线"></a> |
| 2 | [caru-ini/stack-diagram](https://github.com/caru-ini/stack-diagram)<br>一句话描述技术栈，自动生成架构图 | 2026-11-01<br><sub>2.7 天</sub> | 1,499 | 563.1 | <a href="https://www.star-history.com/#caru-ini/stack-diagram&Date"><img src="https://api.star-history.com/svg?repos=caru-ini/stack-diagram&type=Date" width="260" alt="caru-ini/stack-diagram 的星标历史曲线"></a> |
| 3 | [lexifina/global-law](https://github.com/lexifina/global-law)<br>Git for Global Law: the law of 700+ jurisdictions in git, each country's record a submodule where every commit is one change, dated by when it took effect and… | 2026-10-28<br><sub>6.3 天</sub> | 1,736 | 274.3 | <a href="https://www.star-history.com/#lexifina/global-law&Date"><img src="https://api.star-history.com/svg?repos=lexifina/global-law&type=Date" width="260" alt="lexifina/global-law 的星标历史曲线"></a> |
| 4 | [Balanov/uncut](https://github.com/Balanov/uncut)<br>告别静默截断，无损运行代码智能体 | 2026-11-01<br><sub>2.2 天</sub> | 589 | 271.1 | <a href="https://www.star-history.com/#Balanov/uncut&Date"><img src="https://api.star-history.com/svg?repos=Balanov/uncut&type=Date" width="260" alt="Balanov/uncut 的星标历史曲线"></a> |
| 5 | [Balanov/skein](https://github.com/Balanov/skein)<br>Fail-closed swarm orchestration with epoch-fenced work and late-completion rejection. | 2026-11-02<br><sub>1.0 天</sub> | 259 | 259.0 | <a href="https://www.star-history.com/#Balanov/skein&Date"><img src="https://api.star-history.com/svg?repos=Balanov/skein&type=Date" width="260" alt="Balanov/skein 的星标历史曲线"></a> |
| 6 | [mhfed/vn-law-check](https://github.com/mhfed/vn-law-check)<br>Audit pháp lý website theo luật Việt Nam (BVDLCN 91/2025, TMĐT 122/2025, ANM 116/2025, AI 134/2025) cho Claude Code, Cursor, Copilot, Windsurf, Cline | 2026-11-02<br><sub>1.5 天</sub> | 345 | 229.3 | <a href="https://www.star-history.com/#mhfed/vn-law-check&Date"><img src="https://api.star-history.com/svg?repos=mhfed/vn-law-check&type=Date" width="260" alt="mhfed/vn-law-check 的星标历史曲线"></a> |
| 7 | [NiazMorshed2007/reanimate](https://github.com/NiazMorshed2007/reanimate)<br>动效抄不像？逐帧还原并验证完全一致 | 2026-10-29<br><sub>5.6 天</sub> | 1,081 | 192.0 | <a href="https://www.star-history.com/#NiazMorshed2007/reanimate&Date"><img src="https://api.star-history.com/svg?repos=NiazMorshed2007/reanimate&type=Date" width="260" alt="NiazMorshed2007/reanimate 的星标历史曲线"></a> |
| 8 | [N1nEmAn/sapper-v2](https://github.com/N1nEmAn/sapper-v2)<br>安全测试太费劲？让 AI 军团自主排查 | 2026-10-30<br><sub>4.3 天</sub> | 660 | 154.9 | <a href="https://www.star-history.com/#N1nEmAn/sapper-v2&Date"><img src="https://api.star-history.com/svg?repos=N1nEmAn/sapper-v2&type=Date" width="260" alt="N1nEmAn/sapper-v2 的星标历史曲线"></a> |
| 9 | [zhanghao123vip/ai-manju-skills](https://github.com/zhanghao123vip/ai-manju-skills)<br>只有一个点子，也能生成全流程 AI 漫剧 | 2026-10-31<br><sub>3.8 天</sub> | 553 | 147.3 | <a href="https://www.star-history.com/#zhanghao123vip/ai-manju-skills&Date"><img src="https://api.star-history.com/svg?repos=zhanghao123vip/ai-manju-skills&type=Date" width="260" alt="zhanghao123vip/ai-manju-skills 的星标历史曲线"></a> |
| 10 | [sleepy-zone/ai-ref-library-cn](https://github.com/sleepy-zone/ai-ref-library-cn)<br>AI作图缺参考？备齐脸型姿势与服装 | 2026-10-29<br><sub>5.2 天</sub> | 700 | 133.3 | <a href="https://www.star-history.com/#sleepy-zone/ai-ref-library-cn&Date"><img src="https://api.star-history.com/svg?repos=sleepy-zone/ai-ref-library-cn&type=Date" width="260" alt="sleepy-zone/ai-ref-library-cn 的星标历史曲线"></a> |

### 本周增长最快（近 7 天）

| # | 项目 | 新增星标 | 星标/天 | 总星标 | 星标历史 |
|---|---|---:|---:|---:|---|
| 1 | [morluto/rea](https://github.com/morluto/rea)<br>让 AI 帮你克隆任何软件<br>`人工智能` | +31,598 | 4,514.0 | 426,698 | <a href="https://www.star-history.com/#morluto/rea&Date"><img src="https://api.star-history.com/svg?repos=morluto/rea&type=Date" width="260" alt="morluto/rea 的星标历史曲线"></a> |
| 2 | [cloudflare/security-audit-skill](https://github.com/cloudflare/security-audit-skill)<br>AI 查代码漏洞，另一个 AI 逐条复核<br>`人工智能` | +8,813 | 1,259.0 | 58,110 | <a href="https://www.star-history.com/#cloudflare/security-audit-skill&Date"><img src="https://api.star-history.com/svg?repos=cloudflare/security-audit-skill&type=Date" width="260" alt="cloudflare/security-audit-skill 的星标历史曲线"></a> |
| 3 | [thedotmack/claude-mem](https://github.com/thedotmack/claude-mem)<br>AI 不再忘记上次做到哪<br>`人工智能` | +7,744 | 1,106.3 | 111,761 | <a href="https://www.star-history.com/#thedotmack/claude-mem&Date"><img src="https://api.star-history.com/svg?repos=thedotmack/claude-mem&type=Date" width="260" alt="thedotmack/claude-mem 的星标历史曲线"></a> |
| 4 | [deepseek-ai/deepseek-harness](https://github.com/deepseek-ai/deepseek-harness)<br>想要什么智能体，用插件自己拼<br>`人工智能` | +7,560 | 1,080.0 | 271,007 | <a href="https://www.star-history.com/#deepseek-ai/deepseek-harness&Date"><img src="https://api.star-history.com/svg?repos=deepseek-ai/deepseek-harness&type=Date" width="260" alt="deepseek-ai/deepseek-harness 的星标历史曲线"></a> |
| 5 | [stablyai/orca](https://github.com/stablyai/orca)<br>几个 AI 一起写，谁好用一眼看出<br>`人工智能` | +6,769 | 967.0 | 114,427 | <a href="https://www.star-history.com/#stablyai/orca&Date"><img src="https://api.star-history.com/svg?repos=stablyai/orca&type=Date" width="260" alt="stablyai/orca 的星标历史曲线"></a> |
| 6 | [affaan-m/ECC](https://github.com/affaan-m/ECC)<br>给编程 AI 加记忆、技能和安全检查<br>`人工智能` | +6,127 | 875.3 | 296,480 | <a href="https://www.star-history.com/#affaan-m/ECC&Date"><img src="https://api.star-history.com/svg?repos=affaan-m/ECC&type=Date" width="260" alt="affaan-m/ECC 的星标历史曲线"></a> |
| 7 | [Leonxlnx/taste-skill](https://github.com/Leonxlnx/taste-skill)<br>别再让 AI 做出千篇一律的页面<br>`人工智能` | +5,982 | 854.6 | 109,439 | <a href="https://www.star-history.com/#Leonxlnx/taste-skill&Date"><img src="https://api.star-history.com/svg?repos=Leonxlnx/taste-skill&type=Date" width="260" alt="Leonxlnx/taste-skill 的星标历史曲线"></a> |
| 8 | [DietrichGebert/ponytail](https://github.com/DietrichGebert/ponytail)<br>让 AI 少写废代码，该写的写对<br>`人工智能` | +5,913 | 844.7 | 183,670 | <a href="https://www.star-history.com/#DietrichGebert/ponytail&Date"><img src="https://api.star-history.com/svg?repos=DietrichGebert/ponytail&type=Date" width="260" alt="DietrichGebert/ponytail 的星标历史曲线"></a> |
| 9 | [yetone/magpie](https://github.com/yetone/magpie)<br>编程 AI 换模型，额度用完自动续<br>`人工智能` | +5,883 | 840.4 | 29,038 | <a href="https://www.star-history.com/#yetone/magpie&Date"><img src="https://api.star-history.com/svg?repos=yetone/magpie&type=Date" width="260" alt="yetone/magpie 的星标历史曲线"></a> |
| 10 | [Graphify-Labs/graphify](https://github.com/Graphify-Labs/graphify)<br>大项目看不过来，先看这张地图<br>`人工智能` | +5,187 | 741.0 | 141,784 | <a href="https://www.star-history.com/#Graphify-Labs/graphify&Date"><img src="https://api.star-history.com/svg?repos=Graphify-Labs/graphify&type=Date" width="260" alt="Graphify-Labs/graphify 的星标历史曲线"></a> |

### 本月增长最快（近 30 天）

| # | 项目 | 新增星标 | 星标/天 | 总星标 | 星标历史 |
|---|---|---:|---:|---:|---|
| 1 | [morluto/rea](https://github.com/morluto/rea)<br>让 AI 帮你克隆任何软件<br>`人工智能` | +423,638 | 14,121.3 | 426,698 | <a href="https://www.star-history.com/#morluto/rea&Date"><img src="https://api.star-history.com/svg?repos=morluto/rea&type=Date" width="260" alt="morluto/rea 的星标历史曲线"></a> |
| 2 | [cloudflare/security-audit-skill](https://github.com/cloudflare/security-audit-skill)<br>AI 查代码漏洞，另一个 AI 逐条复核<br>`人工智能` | +33,901 | 1,130.0 | 58,110 | <a href="https://www.star-history.com/#cloudflare/security-audit-skill&Date"><img src="https://api.star-history.com/svg?repos=cloudflare/security-audit-skill&type=Date" width="260" alt="cloudflare/security-audit-skill 的星标历史曲线"></a> |
| 3 | [DietrichGebert/ponytail](https://github.com/DietrichGebert/ponytail)<br>让 AI 少写废代码，该写的写对<br>`人工智能` | +30,435 | 1,014.5 | 183,670 | <a href="https://www.star-history.com/#DietrichGebert/ponytail&Date"><img src="https://api.star-history.com/svg?repos=DietrichGebert/ponytail&type=Date" width="260" alt="DietrichGebert/ponytail 的星标历史曲线"></a> |
| 4 | [stablyai/orca](https://github.com/stablyai/orca)<br>几个 AI 一起写，谁好用一眼看出<br>`人工智能` | +29,998 | 999.9 | 114,427 | <a href="https://www.star-history.com/#stablyai/orca&Date"><img src="https://api.star-history.com/svg?repos=stablyai/orca&type=Date" width="260" alt="stablyai/orca 的星标历史曲线"></a> |
| 5 | [deepseek-ai/deepseek-harness](https://github.com/deepseek-ai/deepseek-harness)<br>想要什么智能体，用插件自己拼<br>`人工智能` | +28,619 | 954.0 | 271,007 | <a href="https://www.star-history.com/#deepseek-ai/deepseek-harness&Date"><img src="https://api.star-history.com/svg?repos=deepseek-ai/deepseek-harness&type=Date" width="260" alt="deepseek-ai/deepseek-harness 的星标历史曲线"></a> |
| 6 | [affaan-m/ECC](https://github.com/affaan-m/ECC)<br>给编程 AI 加记忆、技能和安全检查<br>`人工智能` | +25,102 | 836.7 | 296,480 | <a href="https://www.star-history.com/#affaan-m/ECC&Date"><img src="https://api.star-history.com/svg?repos=affaan-m/ECC&type=Date" width="260" alt="affaan-m/ECC 的星标历史曲线"></a> |
| 7 | [yetone/magpie](https://github.com/yetone/magpie)<br>编程 AI 换模型，额度用完自动续<br>`人工智能` | +24,303 | 810.1 | 29,038 | <a href="https://www.star-history.com/#yetone/magpie&Date"><img src="https://api.star-history.com/svg?repos=yetone/magpie&type=Date" width="260" alt="yetone/magpie 的星标历史曲线"></a> |
| 8 | [heygen-com/hyperframes](https://github.com/heygen-com/hyperframes)<br>不会剪辑，写网页一样就能出片<br>`人工智能` | +21,890 | 729.7 | 78,294 | <a href="https://www.star-history.com/#heygen-com/hyperframes&Date"><img src="https://api.star-history.com/svg?repos=heygen-com/hyperframes&type=Date" width="260" alt="heygen-com/hyperframes 的星标历史曲线"></a> |
| 9 | [Panniantong/Agent-Reach](https://github.com/Panniantong/Agent-Reach)<br>推特油管小红书，AI 都能帮你搜<br>`人工智能` | +18,655 | 621.8 | 108,407 | <a href="https://www.star-history.com/#Panniantong/Agent-Reach&Date"><img src="https://api.star-history.com/svg?repos=Panniantong/Agent-Reach&type=Date" width="260" alt="Panniantong/Agent-Reach 的星标历史曲线"></a> |
| 10 | [Graphify-Labs/graphify](https://github.com/Graphify-Labs/graphify)<br>大项目看不过来，先看这张地图<br>`人工智能` | +18,609 | 620.3 | 141,784 | <a href="https://www.star-history.com/#Graphify-Labs/graphify&Date"><img src="https://api.star-history.com/svg?repos=Graphify-Labs/graphify&type=Date" width="260" alt="Graphify-Labs/graphify 的星标历史曲线"></a> |

### 今年增长最快（近 365 天）

| # | 项目 | 新增星标 | 星标/天 | 总星标 | 星标历史 |
|---|---|---:|---:|---:|---|
| 1 | [deepseek-ai/deepseek-harness](https://github.com/deepseek-ai/deepseek-harness)<br>想要什么智能体，用插件自己拼<br>`人工智能` | +270,174 | 3,294.8 †<br><sub>÷82 天</sub> | 271,007 | <a href="https://www.star-history.com/#deepseek-ai/deepseek-harness&Date"><img src="https://api.star-history.com/svg?repos=deepseek-ai/deepseek-harness&type=Date" width="260" alt="deepseek-ai/deepseek-harness 的星标历史曲线"></a> |
| 2 | [morluto/rea](https://github.com/morluto/rea)<br>让 AI 帮你克隆任何软件<br>`人工智能` | +424,178 | 2,089.5 †<br><sub>÷203 天</sub> | 426,698 | <a href="https://www.star-history.com/#morluto/rea&Date"><img src="https://api.star-history.com/svg?repos=morluto/rea&type=Date" width="260" alt="morluto/rea 的星标历史曲线"></a> |
| 3 | [DietrichGebert/ponytail](https://github.com/DietrichGebert/ponytail)<br>让 AI 少写废代码，该写的写对<br>`人工智能` | +183,129 | 1,271.7 †<br><sub>÷144 天</sub> | 183,670 | <a href="https://www.star-history.com/#DietrichGebert/ponytail&Date"><img src="https://api.star-history.com/svg?repos=DietrichGebert/ponytail&type=Date" width="260" alt="DietrichGebert/ponytail 的星标历史曲线"></a> |
| 4 | [openclaw/openclaw](https://github.com/openclaw/openclaw)<br>能把事做完的 AI 助手，跑在自己设备上<br>`人工智能` | +393,754 | 1,144.6 †<br><sub>÷344 天</sub> | 393,853 | <a href="https://www.star-history.com/#openclaw/openclaw&Date"><img src="https://api.star-history.com/svg?repos=openclaw/openclaw&type=Date" width="260" alt="openclaw/openclaw 的星标历史曲线"></a> |
| 5 | [affaan-m/ECC](https://github.com/affaan-m/ECC)<br>给编程 AI 加记忆、技能和安全检查<br>`人工智能` | +295,903 | 1,023.9 †<br><sub>÷289 天</sub> | 296,480 | <a href="https://www.star-history.com/#affaan-m/ECC&Date"><img src="https://api.star-history.com/svg?repos=affaan-m/ECC&type=Date" width="260" alt="affaan-m/ECC 的星标历史曲线"></a> |
| 6 | [NousResearch/hermes-agent](https://github.com/NousResearch/hermes-agent)<br>越用越会干活的 AI 助手<br>`人工智能` | +259,969 | 712.2 | 260,231 | <a href="https://www.star-history.com/#NousResearch/hermes-agent&Date"><img src="https://api.star-history.com/svg?repos=NousResearch/hermes-agent&type=Date" width="260" alt="NousResearch/hermes-agent 的星标历史曲线"></a> |
| 7 | [yetone/magpie](https://github.com/yetone/magpie)<br>编程 AI 换模型，额度用完自动续<br>`人工智能` | +28,740 | 701.0 †<br><sub>÷41 天</sub> | 29,038 | <a href="https://www.star-history.com/#yetone/magpie&Date"><img src="https://api.star-history.com/svg?repos=yetone/magpie&type=Date" width="260" alt="yetone/magpie 的星标历史曲线"></a> |
| 8 | [Graphify-Labs/graphify](https://github.com/Graphify-Labs/graphify)<br>大项目看不过来，先看这张地图<br>`人工智能` | +141,393 | 660.7 †<br><sub>÷214 天</sub> | 141,784 | <a href="https://www.star-history.com/#Graphify-Labs/graphify&Date"><img src="https://api.star-history.com/svg?repos=Graphify-Labs/graphify&type=Date" width="260" alt="Graphify-Labs/graphify 的星标历史曲线"></a> |
| 9 | [anomalyco/opencode](https://github.com/anomalyco/opencode)<br>终端里，有个开源 AI 帮你写代码<br>`人工智能` | +194,814 | 533.7 | 224,332 | <a href="https://www.star-history.com/#anomalyco/opencode&Date"><img src="https://api.star-history.com/svg?repos=anomalyco/opencode&type=Date" width="260" alt="anomalyco/opencode 的星标历史曲线"></a> |
| 10 | [stablyai/orca](https://github.com/stablyai/orca)<br>几个 AI 一起写，谁好用一眼看出<br>`人工智能` | +113,876 | 493.0 †<br><sub>÷231 天</sub> | 114,427 | <a href="https://www.star-history.com/#stablyai/orca&Date"><img src="https://api.star-history.com/svg?repos=stablyai/orca&type=Date" width="260" alt="stablyai/orca 的星标历史曲线"></a> |

† 该仓库创建时间短于统计窗口，因此“星标/天”按仓库存在的天数（显示在数字下方）计算，而不是按完整窗口。

### 总星标数（历史累计）

| # | 项目 | 总星标 | 星标历史 |
|---|---|---:|---|
| 1 | [morluto/rea](https://github.com/morluto/rea)<br>让 AI 帮你克隆任何软件<br>`人工智能` | 426,698 | <a href="https://www.star-history.com/#morluto/rea&Date"><img src="https://api.star-history.com/svg?repos=morluto/rea&type=Date" width="260" alt="morluto/rea 的星标历史曲线"></a> |
| 2 | [openclaw/openclaw](https://github.com/openclaw/openclaw)<br>能把事做完的 AI 助手，跑在自己设备上<br>`人工智能` | 393,853 | <a href="https://www.star-history.com/#openclaw/openclaw&Date"><img src="https://api.star-history.com/svg?repos=openclaw/openclaw&type=Date" width="260" alt="openclaw/openclaw 的星标历史曲线"></a> |
| 3 | [affaan-m/ECC](https://github.com/affaan-m/ECC)<br>给编程 AI 加记忆、技能和安全检查<br>`人工智能` | 296,480 | <a href="https://www.star-history.com/#affaan-m/ECC&Date"><img src="https://api.star-history.com/svg?repos=affaan-m/ECC&type=Date" width="260" alt="affaan-m/ECC 的星标历史曲线"></a> |
| 4 | [deepseek-ai/deepseek-harness](https://github.com/deepseek-ai/deepseek-harness)<br>想要什么智能体，用插件自己拼<br>`人工智能` | 271,007 | <a href="https://www.star-history.com/#deepseek-ai/deepseek-harness&Date"><img src="https://api.star-history.com/svg?repos=deepseek-ai/deepseek-harness&type=Date" width="260" alt="deepseek-ai/deepseek-harness 的星标历史曲线"></a> |
| 5 | [NousResearch/hermes-agent](https://github.com/NousResearch/hermes-agent)<br>越用越会干活的 AI 助手<br>`人工智能` | 260,231 | <a href="https://www.star-history.com/#NousResearch/hermes-agent&Date"><img src="https://api.star-history.com/svg?repos=NousResearch/hermes-agent&type=Date" width="260" alt="NousResearch/hermes-agent 的星标历史曲线"></a> |
| 6 | [anomalyco/opencode](https://github.com/anomalyco/opencode)<br>终端里，有个开源 AI 帮你写代码<br>`人工智能` | 224,332 | <a href="https://www.star-history.com/#anomalyco/opencode&Date"><img src="https://api.star-history.com/svg?repos=anomalyco/opencode&type=Date" width="260" alt="anomalyco/opencode 的星标历史曲线"></a> |
| 7 | [anthropics/skills](https://github.com/anthropics/skills)<br>Claude 技能怎么写，照着官方学<br>`人工智能` | 187,076 | <a href="https://www.star-history.com/#anthropics/skills&Date"><img src="https://api.star-history.com/svg?repos=anthropics/skills&type=Date" width="260" alt="anthropics/skills 的星标历史曲线"></a> |
| 8 | [DietrichGebert/ponytail](https://github.com/DietrichGebert/ponytail)<br>让 AI 少写废代码，该写的写对<br>`人工智能` | 183,670 | <a href="https://www.star-history.com/#DietrichGebert/ponytail&Date"><img src="https://api.star-history.com/svg?repos=DietrichGebert/ponytail&type=Date" width="260" alt="DietrichGebert/ponytail 的星标历史曲线"></a> |
| 9 | [farion1231/cc-switch](https://github.com/farion1231/cc-switch)<br>换接口不用改配置，一键切<br>`人工智能` | 151,513 | <a href="https://www.star-history.com/#farion1231/cc-switch&Date"><img src="https://api.star-history.com/svg?repos=farion1231/cc-switch&type=Date" width="260" alt="farion1231/cc-switch 的星标历史曲线"></a> |
| 10 | [nextlevelbuilder/ui-ux-pro-max-skill](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill)<br>AI 做的界面，看着像专业设计<br>`人工智能` | 144,735 | <a href="https://www.star-history.com/#nextlevelbuilder/ui-ux-pro-max-skill&Date"><img src="https://api.star-history.com/svg?repos=nextlevelbuilder/ui-ux-pro-max-skill&type=Date" width="260" alt="nextlevelbuilder/ui-ux-pro-max-skill 的星标历史曲线"></a> |

## 开发者工具

> 命令行、编辑器、包管理、代码检查与构建工具

### 最热新仓库（近 7 天内创建）

| # | 项目 | 创建时间（UTC） | 总星标 | 星标/天 | 星标历史 |
|---|---|---|---:|---:|---|
| 1 | [Verlintas/NOIR](https://github.com/Verlintas/NOIR)<br>扫出安卓应用隐私泄露，并支持安全回滚 | 2026-10-31<br><sub>3.0 天</sub> | 1,750 | 584.2 | <a href="https://www.star-history.com/#Verlintas/NOIR&Date"><img src="https://api.star-history.com/svg?repos=Verlintas/NOIR&type=Date" width="260" alt="Verlintas/NOIR 的星标历史曲线"></a> |
| 2 | [AssassinCreator/steam-stash-value-report-card](https://github.com/AssassinCreator/steam-stash-value-report-card)<br>不知库存价值，在终端盘点并生成分享卡 | 2026-11-02<br><sub>1.9 天</sub> | 698 | 374.0 | <a href="https://www.star-history.com/#AssassinCreator/steam-stash-value-report-card&Date"><img src="https://api.star-history.com/svg?repos=AssassinCreator/steam-stash-value-report-card&type=Date" width="260" alt="AssassinCreator/steam-stash-value-report-card 的星标历史曲线"></a> |
| 3 | [MomentumGuideContact/fonetrans](https://github.com/MomentumGuideContact/fonetrans)<br>Complete Fonetrans desktop edition 2026, ready-to-run with all features fully activated. | 2026-11-03<br><sub>1.0 天</sub> | 299 | 299.0 | <a href="https://www.star-history.com/#MomentumGuideContact/fonetrans&Date"><img src="https://api.star-history.com/svg?repos=MomentumGuideContact/fonetrans&type=Date" width="260" alt="MomentumGuideContact/fonetrans 的星标历史曲线"></a> |
| 4 | [exzade/EXZA-Remote](https://github.com/exzade/EXZA-Remote)<br>Secure AI-powered remote computer access for ChatGPT, Claude and compatible MCP clients. | 2026-11-02<br><sub>1.5 天</sub> | 176 | 119.3 | <a href="https://www.star-history.com/#exzade/EXZA-Remote&Date"><img src="https://api.star-history.com/svg?repos=exzade/EXZA-Remote&type=Date" width="260" alt="exzade/EXZA-Remote 的星标历史曲线"></a> |
| 5 | [slateoriolewreck/ios-unlocker](https://github.com/slateoriolewreck/ios-unlocker)<br>Complete standalone iOS Unlocker 2026 installation build, fully functional with no activation needed. | 2026-11-03<br><sub>1.0 天</sub> | 100 | 100.0 | <a href="https://www.star-history.com/#slateoriolewreck/ios-unlocker&Date"><img src="https://api.star-history.com/svg?repos=slateoriolewreck/ios-unlocker&type=Date" width="260" alt="slateoriolewreck/ios-unlocker 的星标历史曲线"></a> |
| 6 | [Straitbrashadow/minecraft-ai-mod-builder](https://github.com/Straitbrashadow/minecraft-ai-mod-builder)<br>Vibe-build in Minecraft. Describe a build in your terminal, see it as a blueprint in your world, place it in one step and undo it in one. Writes datapacks too.… | 2026-10-30<br><sub>4.0 天</sub> | 200 | 49.9 | <a href="https://www.star-history.com/#Straitbrashadow/minecraft-ai-mod-builder&Date"><img src="https://api.star-history.com/svg?repos=Straitbrashadow/minecraft-ai-mod-builder&type=Date" width="260" alt="Straitbrashadow/minecraft-ai-mod-builder 的星标历史曲线"></a> |
| 7 | [UncensoredLabs/uncensored-ai-api](https://github.com/UncensoredLabs/uncensored-ai-api)<br>Uncensored AI API and browser chat: DeepSeek and GLM models, streaming, Python and TypeScript examples, pricing and setup guides. | 2026-11-01<br><sub>2.0 天</sub> | 101 | 49.9 | <a href="https://www.star-history.com/#UncensoredLabs/uncensored-ai-api&Date"><img src="https://api.star-history.com/svg?repos=UncensoredLabs/uncensored-ai-api&type=Date" width="260" alt="UncensoredLabs/uncensored-ai-api 的星标历史曲线"></a> |
| 8 | [Xpropel/Pi-Remote](https://github.com/Xpropel/Pi-Remote)<br>在任意浏览器中远程控制 pi 智能体 | 2026-10-28<br><sub>6.5 天</sub> | 291 | 45.1 | <a href="https://www.star-history.com/#Xpropel/Pi-Remote&Date"><img src="https://api.star-history.com/svg?repos=Xpropel/Pi-Remote&type=Date" width="260" alt="Xpropel/Pi-Remote 的星标历史曲线"></a> |
| 9 | [muaaz9329/cheap-ag](https://github.com/muaaz9329/cheap-ag)<br>套餐总碰上限？让便宜模型写代码 | 2026-10-28<br><sub>6.0 天</sub> | 250 | 41.9 | <a href="https://www.star-history.com/#muaaz9329/cheap-ag&Date"><img src="https://api.star-history.com/svg?repos=muaaz9329/cheap-ag&type=Date" width="260" alt="muaaz9329/cheap-ag 的星标历史曲线"></a> |
| 10 | [DiplomatHearth/roblox-ai-place-diff](https://github.com/DiplomatHearth/roblox-ai-place-diff)<br>怕改坏场景，智能体修改先由你确认 | 2026-10-30<br><sub>4.0 天</sub> | 163 | 40.9 | <a href="https://www.star-history.com/#DiplomatHearth/roblox-ai-place-diff&Date"><img src="https://api.star-history.com/svg?repos=DiplomatHearth/roblox-ai-place-diff&type=Date" width="260" alt="DiplomatHearth/roblox-ai-place-diff 的星标历史曲线"></a> |

### 本周增长最快（近 7 天）

| # | 项目 | 新增星标 | 星标/天 | 总星标 | 星标历史 |
|---|---|---:|---:|---:|---|
| 1 | [zed-industries/zed](https://github.com/zed-industries/zed)<br>打开就快，还能多人一起写代码<br>`开发者工具` | +415 | 59.3 | 92,634 | <a href="https://www.star-history.com/#zed-industries/zed&Date"><img src="https://api.star-history.com/svg?repos=zed-industries/zed&type=Date" width="260" alt="zed-industries/zed 的星标历史曲线"></a> |
| 2 | [astral-sh/uv](https://github.com/astral-sh/uv)<br>装 Python 包，不用再干等<br>`开发者工具` | +310 | 44.3 | 91,509 | <a href="https://www.star-history.com/#astral-sh/uv&Date"><img src="https://api.star-history.com/svg?repos=astral-sh/uv&type=Date" width="260" alt="astral-sh/uv 的星标历史曲线"></a> |
| 3 | [jdx/mise](https://github.com/jdx/mise)<br>开发工具、环境变量、任务，一个工具管<br>`开发者工具` | +291 | 41.6 | 35,726 | <a href="https://www.star-history.com/#jdx/mise&Date"><img src="https://api.star-history.com/svg?repos=jdx/mise&type=Date" width="260" alt="jdx/mise 的星标历史曲线"></a> |
| 4 | [BurntSushi/ripgrep](https://github.com/BurntSushi/ripgrep)<br>翻遍整个目录找文字，比 grep 快<br>`开发者工具` | +227 | 32.4 | 69,672 | <a href="https://www.star-history.com/#BurntSushi/ripgrep&Date"><img src="https://api.star-history.com/svg?repos=BurntSushi/ripgrep&type=Date" width="260" alt="BurntSushi/ripgrep 的星标历史曲线"></a> |
| 5 | [oven-sh/bun](https://github.com/oven-sh/bun)<br>运行打包测试装包，一个工具全包<br>`开发者工具` | +137 | 19.6 | 96,532 | <a href="https://www.star-history.com/#oven-sh/bun&Date"><img src="https://api.star-history.com/svg?repos=oven-sh/bun&type=Date" width="260" alt="oven-sh/bun 的星标历史曲线"></a> |
| 6 | [cli/cli](https://github.com/cli/cli)<br>不开网页，命令行里处理 GitHub<br>`开发者工具` | +107 | 15.3 | 46,857 | <a href="https://www.star-history.com/#cli/cli&Date"><img src="https://api.star-history.com/svg?repos=cli/cli&type=Date" width="260" alt="cli/cli 的星标历史曲线"></a> |
| 7 | [helix-editor/helix](https://github.com/helix-editor/helix)<br>语法高亮、语言服务都内置的文本编辑器<br>`开发者工具` | +98 | 14.0 | 46,778 | <a href="https://www.star-history.com/#helix-editor/helix&Date"><img src="https://api.star-history.com/svg?repos=helix-editor/helix&type=Date" width="260" alt="helix-editor/helix 的星标历史曲线"></a> |
| 8 | [biomejs/biome](https://github.com/biomejs/biome)<br>网页代码格式和检查，一个工具搞定<br>`开发者工具` | +47 | 6.7 | 26,046 | <a href="https://www.star-history.com/#biomejs/biome&Date"><img src="https://api.star-history.com/svg?repos=biomejs/biome&type=Date" width="260" alt="biomejs/biome 的星标历史曲线"></a> |

### 本月增长最快（近 30 天）

| # | 项目 | 新增星标 | 星标/天 | 总星标 | 星标历史 |
|---|---|---:|---:|---:|---|
| 1 | [zed-industries/zed](https://github.com/zed-industries/zed)<br>打开就快，还能多人一起写代码<br>`开发者工具` | +1,624 | 54.1 | 92,634 | <a href="https://www.star-history.com/#zed-industries/zed&Date"><img src="https://api.star-history.com/svg?repos=zed-industries/zed&type=Date" width="260" alt="zed-industries/zed 的星标历史曲线"></a> |
| 2 | [astral-sh/uv](https://github.com/astral-sh/uv)<br>装 Python 包，不用再干等<br>`开发者工具` | +1,280 | 42.7 | 91,509 | <a href="https://www.star-history.com/#astral-sh/uv&Date"><img src="https://api.star-history.com/svg?repos=astral-sh/uv&type=Date" width="260" alt="astral-sh/uv 的星标历史曲线"></a> |
| 3 | [jdx/mise](https://github.com/jdx/mise)<br>开发工具、环境变量、任务，一个工具管<br>`开发者工具` | +1,229 | 41.0 | 35,726 | <a href="https://www.star-history.com/#jdx/mise&Date"><img src="https://api.star-history.com/svg?repos=jdx/mise&type=Date" width="260" alt="jdx/mise 的星标历史曲线"></a> |
| 4 | [BurntSushi/ripgrep](https://github.com/BurntSushi/ripgrep)<br>翻遍整个目录找文字，比 grep 快<br>`开发者工具` | +991 | 33.0 | 69,672 | <a href="https://www.star-history.com/#BurntSushi/ripgrep&Date"><img src="https://api.star-history.com/svg?repos=BurntSushi/ripgrep&type=Date" width="260" alt="BurntSushi/ripgrep 的星标历史曲线"></a> |
| 5 | [oven-sh/bun](https://github.com/oven-sh/bun)<br>运行打包测试装包，一个工具全包<br>`开发者工具` | +694 | 23.1 | 96,532 | <a href="https://www.star-history.com/#oven-sh/bun&Date"><img src="https://api.star-history.com/svg?repos=oven-sh/bun&type=Date" width="260" alt="oven-sh/bun 的星标历史曲线"></a> |
| 6 | [helix-editor/helix](https://github.com/helix-editor/helix)<br>语法高亮、语言服务都内置的文本编辑器<br>`开发者工具` | +445 | 14.8 | 46,778 | <a href="https://www.star-history.com/#helix-editor/helix&Date"><img src="https://api.star-history.com/svg?repos=helix-editor/helix&type=Date" width="260" alt="helix-editor/helix 的星标历史曲线"></a> |
| 7 | [cli/cli](https://github.com/cli/cli)<br>不开网页，命令行里处理 GitHub<br>`开发者工具` | +424 | 14.1 | 46,857 | <a href="https://www.star-history.com/#cli/cli&Date"><img src="https://api.star-history.com/svg?repos=cli/cli&type=Date" width="260" alt="cli/cli 的星标历史曲线"></a> |
| 8 | [biomejs/biome](https://github.com/biomejs/biome)<br>网页代码格式和检查，一个工具搞定<br>`开发者工具` | +214 | 7.1 | 26,046 | <a href="https://www.star-history.com/#biomejs/biome&Date"><img src="https://api.star-history.com/svg?repos=biomejs/biome&type=Date" width="260" alt="biomejs/biome 的星标历史曲线"></a> |

### 今年增长最快（近 365 天）

| # | 项目 | 新增星标 | 星标/天 | 总星标 | 星标历史 |
|---|---|---:|---:|---:|---|
| 1 | [zed-industries/zed](https://github.com/zed-industries/zed)<br>打开就快，还能多人一起写代码<br>`开发者工具` | +25,676 | 70.3 | 92,634 | <a href="https://www.star-history.com/#zed-industries/zed&Date"><img src="https://api.star-history.com/svg?repos=zed-industries/zed&type=Date" width="260" alt="zed-industries/zed 的星标历史曲线"></a> |
| 2 | [astral-sh/uv](https://github.com/astral-sh/uv)<br>装 Python 包，不用再干等<br>`开发者工具` | +21,265 | 58.3 | 91,509 | <a href="https://www.star-history.com/#astral-sh/uv&Date"><img src="https://api.star-history.com/svg?repos=astral-sh/uv&type=Date" width="260" alt="astral-sh/uv 的星标历史曲线"></a> |
| 3 | [oven-sh/bun](https://github.com/oven-sh/bun)<br>运行打包测试装包，一个工具全包<br>`开发者工具` | +16,559 | 45.4 | 96,532 | <a href="https://www.star-history.com/#oven-sh/bun&Date"><img src="https://api.star-history.com/svg?repos=oven-sh/bun&type=Date" width="260" alt="oven-sh/bun 的星标历史曲线"></a> |
| 4 | [jdx/mise](https://github.com/jdx/mise)<br>开发工具、环境变量、任务，一个工具管<br>`开发者工具` | +15,084 | 41.3 | 35,726 | <a href="https://www.star-history.com/#jdx/mise&Date"><img src="https://api.star-history.com/svg?repos=jdx/mise&type=Date" width="260" alt="jdx/mise 的星标历史曲线"></a> |
| 5 | [BurntSushi/ripgrep](https://github.com/BurntSushi/ripgrep)<br>翻遍整个目录找文字，比 grep 快<br>`开发者工具` | +13,364 | 36.6 | 69,672 | <a href="https://www.star-history.com/#BurntSushi/ripgrep&Date"><img src="https://api.star-history.com/svg?repos=BurntSushi/ripgrep&type=Date" width="260" alt="BurntSushi/ripgrep 的星标历史曲线"></a> |
| 6 | [helix-editor/helix](https://github.com/helix-editor/helix)<br>语法高亮、语言服务都内置的文本编辑器<br>`开发者工具` | +6,702 | 18.4 | 46,778 | <a href="https://www.star-history.com/#helix-editor/helix&Date"><img src="https://api.star-history.com/svg?repos=helix-editor/helix&type=Date" width="260" alt="helix-editor/helix 的星标历史曲线"></a> |
| 7 | [cli/cli](https://github.com/cli/cli)<br>不开网页，命令行里处理 GitHub<br>`开发者工具` | +6,262 | 17.2 | 46,857 | <a href="https://www.star-history.com/#cli/cli&Date"><img src="https://api.star-history.com/svg?repos=cli/cli&type=Date" width="260" alt="cli/cli 的星标历史曲线"></a> |
| 8 | [biomejs/biome](https://github.com/biomejs/biome)<br>网页代码格式和检查，一个工具搞定<br>`开发者工具` | +4,571 | 12.5 | 26,046 | <a href="https://www.star-history.com/#biomejs/biome&Date"><img src="https://api.star-history.com/svg?repos=biomejs/biome&type=Date" width="260" alt="biomejs/biome 的星标历史曲线"></a> |

### 总星标数（历史累计）

| # | 项目 | 总星标 | 星标历史 |
|---|---|---:|---|
| 1 | [oven-sh/bun](https://github.com/oven-sh/bun)<br>运行打包测试装包，一个工具全包<br>`开发者工具` | 96,532 | <a href="https://www.star-history.com/#oven-sh/bun&Date"><img src="https://api.star-history.com/svg?repos=oven-sh/bun&type=Date" width="260" alt="oven-sh/bun 的星标历史曲线"></a> |
| 2 | [zed-industries/zed](https://github.com/zed-industries/zed)<br>打开就快，还能多人一起写代码<br>`开发者工具` | 92,634 | <a href="https://www.star-history.com/#zed-industries/zed&Date"><img src="https://api.star-history.com/svg?repos=zed-industries/zed&type=Date" width="260" alt="zed-industries/zed 的星标历史曲线"></a> |
| 3 | [astral-sh/uv](https://github.com/astral-sh/uv)<br>装 Python 包，不用再干等<br>`开发者工具` | 91,509 | <a href="https://www.star-history.com/#astral-sh/uv&Date"><img src="https://api.star-history.com/svg?repos=astral-sh/uv&type=Date" width="260" alt="astral-sh/uv 的星标历史曲线"></a> |
| 4 | [BurntSushi/ripgrep](https://github.com/BurntSushi/ripgrep)<br>翻遍整个目录找文字，比 grep 快<br>`开发者工具` | 69,672 | <a href="https://www.star-history.com/#BurntSushi/ripgrep&Date"><img src="https://api.star-history.com/svg?repos=BurntSushi/ripgrep&type=Date" width="260" alt="BurntSushi/ripgrep 的星标历史曲线"></a> |
| 5 | [cli/cli](https://github.com/cli/cli)<br>不开网页，命令行里处理 GitHub<br>`开发者工具` | 46,857 | <a href="https://www.star-history.com/#cli/cli&Date"><img src="https://api.star-history.com/svg?repos=cli/cli&type=Date" width="260" alt="cli/cli 的星标历史曲线"></a> |
| 6 | [helix-editor/helix](https://github.com/helix-editor/helix)<br>语法高亮、语言服务都内置的文本编辑器<br>`开发者工具` | 46,778 | <a href="https://www.star-history.com/#helix-editor/helix&Date"><img src="https://api.star-history.com/svg?repos=helix-editor/helix&type=Date" width="260" alt="helix-editor/helix 的星标历史曲线"></a> |
| 7 | [jdx/mise](https://github.com/jdx/mise)<br>开发工具、环境变量、任务，一个工具管<br>`开发者工具` | 35,726 | <a href="https://www.star-history.com/#jdx/mise&Date"><img src="https://api.star-history.com/svg?repos=jdx/mise&type=Date" width="260" alt="jdx/mise 的星标历史曲线"></a> |
| 8 | [biomejs/biome](https://github.com/biomejs/biome)<br>网页代码格式和检查，一个工具搞定<br>`开发者工具` | 26,046 | <a href="https://www.star-history.com/#biomejs/biome&Date"><img src="https://api.star-history.com/svg?repos=biomejs/biome&type=Date" width="260" alt="biomejs/biome 的星标历史曲线"></a> |

## 安全

> 漏洞扫描、静态分析、供应链与运行时安全

### 最热新仓库（近 7 天内创建）

本次运行中没有符合条件的新仓库。

### 本周增长最快（近 7 天）

| # | 项目 | 新增星标 | 星标/天 | 总星标 | 星标历史 |
|---|---|---:|---:|---:|---|
| 1 | [projectdiscovery/nuclei](https://github.com/projectdiscovery/nuclei)<br>写个模板，就能批量扫漏洞<br>`安全` | +206 | 29.4 | 32,568 | <a href="https://www.star-history.com/#projectdiscovery/nuclei&Date"><img src="https://api.star-history.com/svg?repos=projectdiscovery/nuclei&type=Date" width="260" alt="projectdiscovery/nuclei 的星标历史曲线"></a> |
| 2 | [aquasecurity/trivy](https://github.com/aquasecurity/trivy)<br>容器和代码仓，一次扫完安全问题<br>`安全` | +182 | 26.0 | 38,941 | <a href="https://www.star-history.com/#aquasecurity/trivy&Date"><img src="https://api.star-history.com/svg?repos=aquasecurity/trivy&type=Date" width="260" alt="aquasecurity/trivy 的星标历史曲线"></a> |
| 3 | [semgrep/semgrep](https://github.com/semgrep/semgrep)<br>代码里的问题，提交前先揪出来<br>`安全` | +119 | 17.0 | 17,430 | <a href="https://www.star-history.com/#semgrep/semgrep&Date"><img src="https://api.star-history.com/svg?repos=semgrep/semgrep&type=Date" width="260" alt="semgrep/semgrep 的星标历史曲线"></a> |
| 4 | [OWASP/CheatSheetSeries](https://github.com/OWASP/CheatSheetSeries)<br>应用安全怎么做，看这套速查表<br>`安全` | +106 | 15.1 | 33,869 | <a href="https://www.star-history.com/#OWASP/CheatSheetSeries&Date"><img src="https://api.star-history.com/svg?repos=OWASP/CheatSheetSeries&type=Date" width="260" alt="OWASP/CheatSheetSeries 的星标历史曲线"></a> |
| 5 | [google/osv-scanner](https://github.com/google/osv-scanner)<br>用的依赖安不安全，扫一下就知道<br>`安全` | +94 | 13.4 | 11,382 | <a href="https://www.star-history.com/#google/osv-scanner&Date"><img src="https://api.star-history.com/svg?repos=google/osv-scanner&type=Date" width="260" alt="google/osv-scanner 的星标历史曲线"></a> |
| 6 | [anchore/grype](https://github.com/anchore/grype)<br>容器镜像有没有漏洞，扫一下就知道<br>`安全` | +54 | 7.7 | 13,170 | <a href="https://www.star-history.com/#anchore/grype&Date"><img src="https://api.star-history.com/svg?repos=anchore/grype&type=Date" width="260" alt="anchore/grype 的星标历史曲线"></a> |
| 7 | [falcosecurity/falco](https://github.com/falcosecurity/falco)<br>云上有异常，第一时间知道<br>`安全` | +22 | 3.1 | 9,548 | <a href="https://www.star-history.com/#falcosecurity/falco&Date"><img src="https://api.star-history.com/svg?repos=falcosecurity/falco&type=Date" width="260" alt="falcosecurity/falco 的星标历史曲线"></a> |
| 8 | [securego/gosec](https://github.com/securego/gosec)<br>Go 代码的安全隐患，扫一遍就知道<br>`安全` | +9 | 1.3 | 8,997 | <a href="https://www.star-history.com/#securego/gosec&Date"><img src="https://api.star-history.com/svg?repos=securego/gosec&type=Date" width="260" alt="securego/gosec 的星标历史曲线"></a> |

### 本月增长最快（近 30 天）

| # | 项目 | 新增星标 | 星标/天 | 总星标 | 星标历史 |
|---|---|---:|---:|---:|---|
| 1 | [projectdiscovery/nuclei](https://github.com/projectdiscovery/nuclei)<br>写个模板，就能批量扫漏洞<br>`安全` | +922 | 30.7 | 32,568 | <a href="https://www.star-history.com/#projectdiscovery/nuclei&Date"><img src="https://api.star-history.com/svg?repos=projectdiscovery/nuclei&type=Date" width="260" alt="projectdiscovery/nuclei 的星标历史曲线"></a> |
| 2 | [aquasecurity/trivy](https://github.com/aquasecurity/trivy)<br>容器和代码仓，一次扫完安全问题<br>`安全` | +767 | 25.6 | 38,941 | <a href="https://www.star-history.com/#aquasecurity/trivy&Date"><img src="https://api.star-history.com/svg?repos=aquasecurity/trivy&type=Date" width="260" alt="aquasecurity/trivy 的星标历史曲线"></a> |
| 3 | [semgrep/semgrep](https://github.com/semgrep/semgrep)<br>代码里的问题，提交前先揪出来<br>`安全` | +581 | 19.4 | 17,430 | <a href="https://www.star-history.com/#semgrep/semgrep&Date"><img src="https://api.star-history.com/svg?repos=semgrep/semgrep&type=Date" width="260" alt="semgrep/semgrep 的星标历史曲线"></a> |
| 4 | [OWASP/CheatSheetSeries](https://github.com/OWASP/CheatSheetSeries)<br>应用安全怎么做，看这套速查表<br>`安全` | +474 | 15.8 | 33,869 | <a href="https://www.star-history.com/#OWASP/CheatSheetSeries&Date"><img src="https://api.star-history.com/svg?repos=OWASP/CheatSheetSeries&type=Date" width="260" alt="OWASP/CheatSheetSeries 的星标历史曲线"></a> |
| 5 | [google/osv-scanner](https://github.com/google/osv-scanner)<br>用的依赖安不安全，扫一下就知道<br>`安全` | +258 | 8.6 | 11,382 | <a href="https://www.star-history.com/#google/osv-scanner&Date"><img src="https://api.star-history.com/svg?repos=google/osv-scanner&type=Date" width="260" alt="google/osv-scanner 的星标历史曲线"></a> |
| 6 | [anchore/grype](https://github.com/anchore/grype)<br>容器镜像有没有漏洞，扫一下就知道<br>`安全` | +206 | 6.9 | 13,170 | <a href="https://www.star-history.com/#anchore/grype&Date"><img src="https://api.star-history.com/svg?repos=anchore/grype&type=Date" width="260" alt="anchore/grype 的星标历史曲线"></a> |
| 7 | [falcosecurity/falco](https://github.com/falcosecurity/falco)<br>云上有异常，第一时间知道<br>`安全` | +123 | 4.1 | 9,548 | <a href="https://www.star-history.com/#falcosecurity/falco&Date"><img src="https://api.star-history.com/svg?repos=falcosecurity/falco&type=Date" width="260" alt="falcosecurity/falco 的星标历史曲线"></a> |
| 8 | [securego/gosec](https://github.com/securego/gosec)<br>Go 代码的安全隐患，扫一遍就知道<br>`安全` | +43 | 1.4 | 8,997 | <a href="https://www.star-history.com/#securego/gosec&Date"><img src="https://api.star-history.com/svg?repos=securego/gosec&type=Date" width="260" alt="securego/gosec 的星标历史曲线"></a> |

### 今年增长最快（近 365 天）

| # | 项目 | 新增星标 | 星标/天 | 总星标 | 星标历史 |
|---|---|---:|---:|---:|---|
| 1 | [aquasecurity/trivy](https://github.com/aquasecurity/trivy)<br>容器和代码仓，一次扫完安全问题<br>`安全` | +10,103 | 27.7 | 38,941 | <a href="https://www.star-history.com/#aquasecurity/trivy&Date"><img src="https://api.star-history.com/svg?repos=aquasecurity/trivy&type=Date" width="260" alt="aquasecurity/trivy 的星标历史曲线"></a> |
| 2 | [projectdiscovery/nuclei](https://github.com/projectdiscovery/nuclei)<br>写个模板，就能批量扫漏洞<br>`安全` | +7,610 | 20.8 | 32,568 | <a href="https://www.star-history.com/#projectdiscovery/nuclei&Date"><img src="https://api.star-history.com/svg?repos=projectdiscovery/nuclei&type=Date" width="260" alt="projectdiscovery/nuclei 的星标历史曲线"></a> |
| 3 | [semgrep/semgrep](https://github.com/semgrep/semgrep)<br>代码里的问题，提交前先揪出来<br>`安全` | +4,377 | 12.0 | 17,430 | <a href="https://www.star-history.com/#semgrep/semgrep&Date"><img src="https://api.star-history.com/svg?repos=semgrep/semgrep&type=Date" width="260" alt="semgrep/semgrep 的星标历史曲线"></a> |
| 4 | [OWASP/CheatSheetSeries](https://github.com/OWASP/CheatSheetSeries)<br>应用安全怎么做，看这套速查表<br>`安全` | +3,531 | 9.7 | 33,869 | <a href="https://www.star-history.com/#OWASP/CheatSheetSeries&Date"><img src="https://api.star-history.com/svg?repos=OWASP/CheatSheetSeries&type=Date" width="260" alt="OWASP/CheatSheetSeries 的星标历史曲线"></a> |
| 5 | [google/osv-scanner](https://github.com/google/osv-scanner)<br>用的依赖安不安全，扫一下就知道<br>`安全` | +3,502 | 9.6 | 11,382 | <a href="https://www.star-history.com/#google/osv-scanner&Date"><img src="https://api.star-history.com/svg?repos=google/osv-scanner&type=Date" width="260" alt="google/osv-scanner 的星标历史曲线"></a> |
| 6 | [anchore/grype](https://github.com/anchore/grype)<br>容器镜像有没有漏洞，扫一下就知道<br>`安全` | +2,356 | 6.5 | 13,170 | <a href="https://www.star-history.com/#anchore/grype&Date"><img src="https://api.star-history.com/svg?repos=anchore/grype&type=Date" width="260" alt="anchore/grype 的星标历史曲线"></a> |
| 7 | [falcosecurity/falco](https://github.com/falcosecurity/falco)<br>云上有异常，第一时间知道<br>`安全` | +1,267 | 3.5 | 9,548 | <a href="https://www.star-history.com/#falcosecurity/falco&Date"><img src="https://api.star-history.com/svg?repos=falcosecurity/falco&type=Date" width="260" alt="falcosecurity/falco 的星标历史曲线"></a> |
| 8 | [securego/gosec](https://github.com/securego/gosec)<br>Go 代码的安全隐患，扫一遍就知道<br>`安全` | +561 | 1.5 | 8,997 | <a href="https://www.star-history.com/#securego/gosec&Date"><img src="https://api.star-history.com/svg?repos=securego/gosec&type=Date" width="260" alt="securego/gosec 的星标历史曲线"></a> |

### 总星标数（历史累计）

| # | 项目 | 总星标 | 星标历史 |
|---|---|---:|---|
| 1 | [aquasecurity/trivy](https://github.com/aquasecurity/trivy)<br>容器和代码仓，一次扫完安全问题<br>`安全` | 38,941 | <a href="https://www.star-history.com/#aquasecurity/trivy&Date"><img src="https://api.star-history.com/svg?repos=aquasecurity/trivy&type=Date" width="260" alt="aquasecurity/trivy 的星标历史曲线"></a> |
| 2 | [OWASP/CheatSheetSeries](https://github.com/OWASP/CheatSheetSeries)<br>应用安全怎么做，看这套速查表<br>`安全` | 33,869 | <a href="https://www.star-history.com/#OWASP/CheatSheetSeries&Date"><img src="https://api.star-history.com/svg?repos=OWASP/CheatSheetSeries&type=Date" width="260" alt="OWASP/CheatSheetSeries 的星标历史曲线"></a> |
| 3 | [projectdiscovery/nuclei](https://github.com/projectdiscovery/nuclei)<br>写个模板，就能批量扫漏洞<br>`安全` | 32,568 | <a href="https://www.star-history.com/#projectdiscovery/nuclei&Date"><img src="https://api.star-history.com/svg?repos=projectdiscovery/nuclei&type=Date" width="260" alt="projectdiscovery/nuclei 的星标历史曲线"></a> |
| 4 | [semgrep/semgrep](https://github.com/semgrep/semgrep)<br>代码里的问题，提交前先揪出来<br>`安全` | 17,430 | <a href="https://www.star-history.com/#semgrep/semgrep&Date"><img src="https://api.star-history.com/svg?repos=semgrep/semgrep&type=Date" width="260" alt="semgrep/semgrep 的星标历史曲线"></a> |
| 5 | [anchore/grype](https://github.com/anchore/grype)<br>容器镜像有没有漏洞，扫一下就知道<br>`安全` | 13,170 | <a href="https://www.star-history.com/#anchore/grype&Date"><img src="https://api.star-history.com/svg?repos=anchore/grype&type=Date" width="260" alt="anchore/grype 的星标历史曲线"></a> |
| 6 | [google/osv-scanner](https://github.com/google/osv-scanner)<br>用的依赖安不安全，扫一下就知道<br>`安全` | 11,382 | <a href="https://www.star-history.com/#google/osv-scanner&Date"><img src="https://api.star-history.com/svg?repos=google/osv-scanner&type=Date" width="260" alt="google/osv-scanner 的星标历史曲线"></a> |
| 7 | [falcosecurity/falco](https://github.com/falcosecurity/falco)<br>云上有异常，第一时间知道<br>`安全` | 9,548 | <a href="https://www.star-history.com/#falcosecurity/falco&Date"><img src="https://api.star-history.com/svg?repos=falcosecurity/falco&type=Date" width="260" alt="falcosecurity/falco 的星标历史曲线"></a> |
| 8 | [securego/gosec](https://github.com/securego/gosec)<br>Go 代码的安全隐患，扫一遍就知道<br>`安全` | 8,997 | <a href="https://www.star-history.com/#securego/gosec&Date"><img src="https://api.star-history.com/svg?repos=securego/gosec&type=Date" width="260" alt="securego/gosec 的星标历史曲线"></a> |

## Web / 前端

> 前端框架、UI 组件库、CSS 与浏览器工具

### 最热新仓库（近 7 天内创建）

| # | 项目 | 创建时间（UTC） | 总星标 | 星标/天 | 星标历史 |
|---|---|---|---:|---:|---|
| 1 | [mofan6/Moect](https://github.com/mofan6/Moect)<br>微信聊天记录想留存，离线导出与备份 | 2026-10-31<br><sub>3.5 天</sub> | 225 | 65.3 | <a href="https://www.star-history.com/#mofan6/Moect&Date"><img src="https://api.star-history.com/svg?repos=mofan6/Moect&type=Date" width="260" alt="mofan6/Moect 的星标历史曲线"></a> |
| 2 | [shipwords-dev/shipwords](https://github.com/shipwords-dev/shipwords)<br>追到新词，一下午上线一个 AI 站 | 2026-10-28<br><sub>6.6 天</sub> | 351 | 53.0 | <a href="https://www.star-history.com/#shipwords-dev/shipwords&Date"><img src="https://api.star-history.com/svg?repos=shipwords-dev/shipwords&type=Date" width="260" alt="shipwords-dev/shipwords 的星标历史曲线"></a> |
| 3 | [zklmiao/prompt-vault](https://github.com/zklmiao/prompt-vault)<br>提示词到处乱放？在桌面本地统一收藏 | 2026-10-28<br><sub>6.7 天</sub> | 309 | 46.0 | <a href="https://www.star-history.com/#zklmiao/prompt-vault&Date"><img src="https://api.star-history.com/svg?repos=zklmiao/prompt-vault&type=Date" width="260" alt="zklmiao/prompt-vault 的星标历史曲线"></a> |
| 4 | [Lavagroabide/aegis-spreadwatch](https://github.com/Lavagroabide/aegis-spreadwatch)<br>CS2 买卖看不清，在设备上直接看净利润 | 2026-10-30<br><sub>3.9 天</sub> | 156 | 39.9 | <a href="https://www.star-history.com/#Lavagroabide/aegis-spreadwatch&Date"><img src="https://api.star-history.com/svg?repos=Lavagroabide/aegis-spreadwatch&type=Date" width="260" alt="Lavagroabide/aegis-spreadwatch 的星标历史曲线"></a> |
| 5 | [solderdatabraid29/aegis-vaultgrid](https://github.com/solderdatabraid29/aegis-vaultgrid)<br>不想登录看库存？在本地规划 CS2 订单 | 2026-10-30<br><sub>3.9 天</sub> | 139 | 35.5 | <a href="https://www.star-history.com/#solderdatabraid29/aegis-vaultgrid&Date"><img src="https://api.star-history.com/svg?repos=solderdatabraid29/aegis-vaultgrid&type=Date" width="260" alt="solderdatabraid29/aegis-vaultgrid 的星标历史曲线"></a> |
| 6 | [Townlanurture/aegis-skin-terminal](https://github.com/Townlanurture/aegis-skin-terminal)<br>CS2 交易怕算漏手续费，本地直接扫差价 | 2026-10-30<br><sub>3.9 天</sub> | 136 | 34.7 | <a href="https://www.star-history.com/#Townlanurture/aegis-skin-terminal&Date"><img src="https://api.star-history.com/svg?repos=Townlanurture/aegis-skin-terminal&type=Date" width="260" alt="Townlanurture/aegis-skin-terminal 的星标历史曲线"></a> |
| 7 | [SalmeronDevZone/azure-lab](https://github.com/SalmeronDevZone/azure-lab)<br>Simulador de Azure para aprender DevOps sin cuenta ni costes: portal, Cloud Shell, Azure DevOps y una academia de 13 niveles con 47 laboratorios que se validan… | 2026-10-30<br><sub>4.5 天</sub> | 102 | 22.5 | <a href="https://www.star-history.com/#SalmeronDevZone/azure-lab&Date"><img src="https://api.star-history.com/svg?repos=SalmeronDevZone/azure-lab&type=Date" width="260" alt="SalmeronDevZone/azure-lab 的星标历史曲线"></a> |
| 8 | [floatboatai/OpenMinutes](https://github.com/floatboatai/OpenMinutes)<br>录音笔的录音，转成能搜的文字 | 2026-10-28<br><sub>6.4 天</sub> | 108 | 17.0 | <a href="https://www.star-history.com/#floatboatai/OpenMinutes&Date"><img src="https://api.star-history.com/svg?repos=floatboatai/OpenMinutes&type=Date" width="260" alt="floatboatai/OpenMinutes 的星标历史曲线"></a> |

### 本周增长最快（近 7 天）

| # | 项目 | 新增星标 | 星标/天 | 总星标 | 星标历史 |
|---|---|---:|---:|---:|---|
| 1 | [shadcn-ui/ui](https://github.com/shadcn-ui/ui)<br>好看的组件，代码归你，随便改<br>`Web / 前端` | +664 | 94.9 | 127,278 | <a href="https://www.star-history.com/#shadcn-ui/ui&Date"><img src="https://api.star-history.com/svg?repos=shadcn-ui/ui&type=Date" width="260" alt="shadcn-ui/ui 的星标历史曲线"></a> |
| 2 | [facebook/react](https://github.com/facebook/react)<br>网页和 App 界面，都能用它来搭<br>`Web / 前端` | +350 | 50.0 | 251,900 | <a href="https://www.star-history.com/#facebook/react&Date"><img src="https://api.star-history.com/svg?repos=facebook/react&type=Date" width="260" alt="facebook/react 的星标历史曲线"></a> |
| 3 | [withastro/astro](https://github.com/withastro/astro)<br>做内容型网站，页面输出更轻量<br>`Web / 前端` | +207 | 29.6 | 63,700 | <a href="https://www.star-history.com/#withastro/astro&Date"><img src="https://api.star-history.com/svg?repos=withastro/astro&type=Date" width="260" alt="withastro/astro 的星标历史曲线"></a> |
| 4 | [vercel/next.js](https://github.com/vercel/next.js)<br>用 React 做完整网站，从前到后<br>`Web / 前端` | +158 | 22.6 | 143,247 | <a href="https://www.star-history.com/#vercel/next.js&Date"><img src="https://api.star-history.com/svg?repos=vercel/next.js&type=Date" width="260" alt="vercel/next.js 的星标历史曲线"></a> |
| 5 | [tailwindlabs/tailwindcss](https://github.com/tailwindlabs/tailwindcss)<br>不写一大堆 CSS，也能做定制界面<br>`Web / 前端` | +101 | 14.4 | 98,057 | <a href="https://www.star-history.com/#tailwindlabs/tailwindcss&Date"><img src="https://api.star-history.com/svg?repos=tailwindlabs/tailwindcss&type=Date" width="260" alt="tailwindlabs/tailwindcss 的星标历史曲线"></a> |
| 6 | [sveltejs/svelte](https://github.com/sveltejs/svelte)<br>你写组件，编译器变出高效的网页代码<br>`Web / 前端` | +100 | 14.3 | 88,549 | <a href="https://www.star-history.com/#sveltejs/svelte&Date"><img src="https://api.star-history.com/svg?repos=sveltejs/svelte&type=Date" width="260" alt="sveltejs/svelte 的星标历史曲线"></a> |
| 7 | [vuejs/core](https://github.com/vuejs/core)<br>从一个小页面开始，用多少学多少<br>`Web / 前端` | +72 | 10.3 | 54,823 | <a href="https://www.star-history.com/#vuejs/core&Date"><img src="https://api.star-history.com/svg?repos=vuejs/core&type=Date" width="260" alt="vuejs/core 的星标历史曲线"></a> |
| 8 | [tanstack/query](https://github.com/tanstack/query)<br>请求数据和缓存，交给它管<br>`Web / 前端` | +45 | 6.4 | 50,520 | <a href="https://www.star-history.com/#tanstack/query&Date"><img src="https://api.star-history.com/svg?repos=tanstack/query&type=Date" width="260" alt="tanstack/query 的星标历史曲线"></a> |

### 本月增长最快（近 30 天）

| # | 项目 | 新增星标 | 星标/天 | 总星标 | 星标历史 |
|---|---|---:|---:|---:|---|
| 1 | [shadcn-ui/ui](https://github.com/shadcn-ui/ui)<br>好看的组件，代码归你，随便改<br>`Web / 前端` | +2,653 | 88.4 | 127,278 | <a href="https://www.star-history.com/#shadcn-ui/ui&Date"><img src="https://api.star-history.com/svg?repos=shadcn-ui/ui&type=Date" width="260" alt="shadcn-ui/ui 的星标历史曲线"></a> |
| 2 | [facebook/react](https://github.com/facebook/react)<br>网页和 App 界面，都能用它来搭<br>`Web / 前端` | +1,673 | 55.8 | 251,900 | <a href="https://www.star-history.com/#facebook/react&Date"><img src="https://api.star-history.com/svg?repos=facebook/react&type=Date" width="260" alt="facebook/react 的星标历史曲线"></a> |
| 3 | [withastro/astro](https://github.com/withastro/astro)<br>做内容型网站，页面输出更轻量<br>`Web / 前端` | +774 | 25.8 | 63,700 | <a href="https://www.star-history.com/#withastro/astro&Date"><img src="https://api.star-history.com/svg?repos=withastro/astro&type=Date" width="260" alt="withastro/astro 的星标历史曲线"></a> |
| 4 | [vercel/next.js](https://github.com/vercel/next.js)<br>用 React 做完整网站，从前到后<br>`Web / 前端` | +719 | 24.0 | 143,247 | <a href="https://www.star-history.com/#vercel/next.js&Date"><img src="https://api.star-history.com/svg?repos=vercel/next.js&type=Date" width="260" alt="vercel/next.js 的星标历史曲线"></a> |
| 5 | [sveltejs/svelte](https://github.com/sveltejs/svelte)<br>你写组件，编译器变出高效的网页代码<br>`Web / 前端` | +496 | 16.5 | 88,549 | <a href="https://www.star-history.com/#sveltejs/svelte&Date"><img src="https://api.star-history.com/svg?repos=sveltejs/svelte&type=Date" width="260" alt="sveltejs/svelte 的星标历史曲线"></a> |
| 6 | [tailwindlabs/tailwindcss](https://github.com/tailwindlabs/tailwindcss)<br>不写一大堆 CSS，也能做定制界面<br>`Web / 前端` | +489 | 16.3 | 98,057 | <a href="https://www.star-history.com/#tailwindlabs/tailwindcss&Date"><img src="https://api.star-history.com/svg?repos=tailwindlabs/tailwindcss&type=Date" width="260" alt="tailwindlabs/tailwindcss 的星标历史曲线"></a> |
| 7 | [vuejs/core](https://github.com/vuejs/core)<br>从一个小页面开始，用多少学多少<br>`Web / 前端` | +414 | 13.8 | 54,823 | <a href="https://www.star-history.com/#vuejs/core&Date"><img src="https://api.star-history.com/svg?repos=vuejs/core&type=Date" width="260" alt="vuejs/core 的星标历史曲线"></a> |
| 8 | [tanstack/query](https://github.com/tanstack/query)<br>请求数据和缓存，交给它管<br>`Web / 前端` | +208 | 6.9 | 50,520 | <a href="https://www.star-history.com/#tanstack/query&Date"><img src="https://api.star-history.com/svg?repos=tanstack/query&type=Date" width="260" alt="tanstack/query 的星标历史曲线"></a> |

### 今年增长最快（近 365 天）

| # | 项目 | 新增星标 | 星标/天 | 总星标 | 星标历史 |
|---|---|---:|---:|---:|---|
| 1 | [shadcn-ui/ui](https://github.com/shadcn-ui/ui)<br>好看的组件，代码归你，随便改<br>`Web / 前端` | +30,378 | 83.2 | 127,278 | <a href="https://www.star-history.com/#shadcn-ui/ui&Date"><img src="https://api.star-history.com/svg?repos=shadcn-ui/ui&type=Date" width="260" alt="shadcn-ui/ui 的星标历史曲线"></a> |
| 2 | [facebook/react](https://github.com/facebook/react)<br>网页和 App 界面，都能用它来搭<br>`Web / 前端` | +15,211 | 41.7 | 251,900 | <a href="https://www.star-history.com/#facebook/react&Date"><img src="https://api.star-history.com/svg?repos=facebook/react&type=Date" width="260" alt="facebook/react 的星标历史曲线"></a> |
| 3 | [withastro/astro](https://github.com/withastro/astro)<br>做内容型网站，页面输出更轻量<br>`Web / 前端` | +10,505 | 28.8 | 63,700 | <a href="https://www.star-history.com/#withastro/astro&Date"><img src="https://api.star-history.com/svg?repos=withastro/astro&type=Date" width="260" alt="withastro/astro 的星标历史曲线"></a> |
| 4 | [vercel/next.js](https://github.com/vercel/next.js)<br>用 React 做完整网站，从前到后<br>`Web / 前端` | +10,336 | 28.3 | 143,247 | <a href="https://www.star-history.com/#vercel/next.js&Date"><img src="https://api.star-history.com/svg?repos=vercel/next.js&type=Date" width="260" alt="vercel/next.js 的星标历史曲线"></a> |
| 5 | [tailwindlabs/tailwindcss](https://github.com/tailwindlabs/tailwindcss)<br>不写一大堆 CSS，也能做定制界面<br>`Web / 前端` | +8,528 | 23.4 | 98,057 | <a href="https://www.star-history.com/#tailwindlabs/tailwindcss&Date"><img src="https://api.star-history.com/svg?repos=tailwindlabs/tailwindcss&type=Date" width="260" alt="tailwindlabs/tailwindcss 的星标历史曲线"></a> |
| 6 | [sveltejs/svelte](https://github.com/sveltejs/svelte)<br>你写组件，编译器变出高效的网页代码<br>`Web / 前端` | +5,279 | 14.5 | 88,549 | <a href="https://www.star-history.com/#sveltejs/svelte&Date"><img src="https://api.star-history.com/svg?repos=sveltejs/svelte&type=Date" width="260" alt="sveltejs/svelte 的星标历史曲线"></a> |
| 7 | [tanstack/query](https://github.com/tanstack/query)<br>请求数据和缓存，交给它管<br>`Web / 前端` | +3,843 | 10.5 | 50,520 | <a href="https://www.star-history.com/#tanstack/query&Date"><img src="https://api.star-history.com/svg?repos=tanstack/query&type=Date" width="260" alt="tanstack/query 的星标历史曲线"></a> |
| 8 | [vuejs/core](https://github.com/vuejs/core)<br>从一个小页面开始，用多少学多少<br>`Web / 前端` | +3,620 | 9.9 | 54,823 | <a href="https://www.star-history.com/#vuejs/core&Date"><img src="https://api.star-history.com/svg?repos=vuejs/core&type=Date" width="260" alt="vuejs/core 的星标历史曲线"></a> |

### 总星标数（历史累计）

| # | 项目 | 总星标 | 星标历史 |
|---|---|---:|---|
| 1 | [facebook/react](https://github.com/facebook/react)<br>网页和 App 界面，都能用它来搭<br>`Web / 前端` | 251,900 | <a href="https://www.star-history.com/#facebook/react&Date"><img src="https://api.star-history.com/svg?repos=facebook/react&type=Date" width="260" alt="facebook/react 的星标历史曲线"></a> |
| 2 | [vercel/next.js](https://github.com/vercel/next.js)<br>用 React 做完整网站，从前到后<br>`Web / 前端` | 143,247 | <a href="https://www.star-history.com/#vercel/next.js&Date"><img src="https://api.star-history.com/svg?repos=vercel/next.js&type=Date" width="260" alt="vercel/next.js 的星标历史曲线"></a> |
| 3 | [shadcn-ui/ui](https://github.com/shadcn-ui/ui)<br>好看的组件，代码归你，随便改<br>`Web / 前端` | 127,278 | <a href="https://www.star-history.com/#shadcn-ui/ui&Date"><img src="https://api.star-history.com/svg?repos=shadcn-ui/ui&type=Date" width="260" alt="shadcn-ui/ui 的星标历史曲线"></a> |
| 4 | [tailwindlabs/tailwindcss](https://github.com/tailwindlabs/tailwindcss)<br>不写一大堆 CSS，也能做定制界面<br>`Web / 前端` | 98,057 | <a href="https://www.star-history.com/#tailwindlabs/tailwindcss&Date"><img src="https://api.star-history.com/svg?repos=tailwindlabs/tailwindcss&type=Date" width="260" alt="tailwindlabs/tailwindcss 的星标历史曲线"></a> |
| 5 | [sveltejs/svelte](https://github.com/sveltejs/svelte)<br>你写组件，编译器变出高效的网页代码<br>`Web / 前端` | 88,549 | <a href="https://www.star-history.com/#sveltejs/svelte&Date"><img src="https://api.star-history.com/svg?repos=sveltejs/svelte&type=Date" width="260" alt="sveltejs/svelte 的星标历史曲线"></a> |
| 6 | [withastro/astro](https://github.com/withastro/astro)<br>做内容型网站，页面输出更轻量<br>`Web / 前端` | 63,700 | <a href="https://www.star-history.com/#withastro/astro&Date"><img src="https://api.star-history.com/svg?repos=withastro/astro&type=Date" width="260" alt="withastro/astro 的星标历史曲线"></a> |
| 7 | [vuejs/core](https://github.com/vuejs/core)<br>从一个小页面开始，用多少学多少<br>`Web / 前端` | 54,823 | <a href="https://www.star-history.com/#vuejs/core&Date"><img src="https://api.star-history.com/svg?repos=vuejs/core&type=Date" width="260" alt="vuejs/core 的星标历史曲线"></a> |
| 8 | [tanstack/query](https://github.com/tanstack/query)<br>请求数据和缓存，交给它管<br>`Web / 前端` | 50,520 | <a href="https://www.star-history.com/#tanstack/query&Date"><img src="https://api.star-history.com/svg?repos=tanstack/query&type=Date" width="260" alt="tanstack/query 的星标历史曲线"></a> |

## 基础设施

> 容器、Kubernetes、云、网络与可观测性

### 最热新仓库（近 7 天内创建）

| # | 项目 | 创建时间（UTC） | 总星标 | 星标/天 | 星标历史 |
|---|---|---|---:|---:|---|
| 1 | [narratarr/narratarr](https://github.com/narratarr/narratarr)<br>Your audiobooks: found, fetched, and playing. An *arr-style audiobook manager with a built-in player. | 2026-10-28<br><sub>6.1 天</sub> | 101 | 16.5 | <a href="https://www.star-history.com/#narratarr/narratarr&Date"><img src="https://api.star-history.com/svg?repos=narratarr/narratarr&type=Date" width="260" alt="narratarr/narratarr 的星标历史曲线"></a> |

### 本周增长最快（近 7 天）

| # | 项目 | 新增星标 | 星标/天 | 总星标 | 星标历史 |
|---|---|---:|---:|---:|---|
| 1 | [caddyserver/caddy](https://github.com/caddyserver/caddy)<br>搭网站服务器，HTTPS 自动配好<br>`基础设施` | +255 | 36.4 | 78,704 | <a href="https://www.star-history.com/#caddyserver/caddy&Date"><img src="https://api.star-history.com/svg?repos=caddyserver/caddy&type=Date" width="260" alt="caddyserver/caddy 的星标历史曲线"></a> |
| 2 | [kubernetes/kubernetes](https://github.com/kubernetes/kubernetes)<br>容器多了，部署扩容交给它<br>`基础设施` | +218 | 31.1 | 128,638 | <a href="https://www.star-history.com/#kubernetes/kubernetes&Date"><img src="https://api.star-history.com/svg?repos=kubernetes/kubernetes&type=Date" width="260" alt="kubernetes/kubernetes 的星标历史曲线"></a> |
| 3 | [grafana/grafana](https://github.com/grafana/grafana)<br>指标日志链路，放进一个面板<br>`基础设施` | +174 | 24.9 | 77,663 | <a href="https://www.star-history.com/#grafana/grafana&Date"><img src="https://api.star-history.com/svg?repos=grafana/grafana&type=Date" width="260" alt="grafana/grafana 的星标历史曲线"></a> |
| 4 | [prometheus/prometheus](https://github.com/prometheus/prometheus)<br>系统出问题，告警先找到你<br>`基础设施` | +154 | 22.0 | 66,931 | <a href="https://www.star-history.com/#prometheus/prometheus&Date"><img src="https://api.star-history.com/svg?repos=prometheus/prometheus&type=Date" width="260" alt="prometheus/prometheus 的星标历史曲线"></a> |
| 5 | [docker/compose](https://github.com/docker/compose)<br>多个容器写进一个文件，一起跑<br>`基础设施` | +117 | 16.7 | 38,584 | <a href="https://www.star-history.com/#docker/compose&Date"><img src="https://api.star-history.com/svg?repos=docker/compose&type=Date" width="260" alt="docker/compose 的星标历史曲线"></a> |
| 6 | [traefik/traefik](https://github.com/traefik/traefik)<br>服务多了，流量自动分好<br>`基础设施` | +93 | 13.3 | 65,451 | <a href="https://www.star-history.com/#traefik/traefik&Date"><img src="https://api.star-history.com/svg?repos=traefik/traefik&type=Date" width="260" alt="traefik/traefik 的星标历史曲线"></a> |
| 7 | [hashicorp/terraform](https://github.com/hashicorp/terraform)<br>云资源写成代码，可审阅、可版本管理<br>`基础设施` | +86 | 12.3 | 50,120 | <a href="https://www.star-history.com/#hashicorp/terraform&Date"><img src="https://api.star-history.com/svg?repos=hashicorp/terraform&type=Date" width="260" alt="hashicorp/terraform 的星标历史曲线"></a> |
| 8 | [pulumi/pulumi](https://github.com/pulumi/pulumi)<br>用熟悉的编程语言管云资源<br>`基础设施` | +25 | 3.6 | 25,843 | <a href="https://www.star-history.com/#pulumi/pulumi&Date"><img src="https://api.star-history.com/svg?repos=pulumi/pulumi&type=Date" width="260" alt="pulumi/pulumi 的星标历史曲线"></a> |

### 本月增长最快（近 30 天）

| # | 项目 | 新增星标 | 星标/天 | 总星标 | 星标历史 |
|---|---|---:|---:|---:|---|
| 1 | [caddyserver/caddy](https://github.com/caddyserver/caddy)<br>搭网站服务器，HTTPS 自动配好<br>`基础设施` | +2,532 | 84.4 | 78,704 | <a href="https://www.star-history.com/#caddyserver/caddy&Date"><img src="https://api.star-history.com/svg?repos=caddyserver/caddy&type=Date" width="260" alt="caddyserver/caddy 的星标历史曲线"></a> |
| 2 | [kubernetes/kubernetes](https://github.com/kubernetes/kubernetes)<br>容器多了，部署扩容交给它<br>`基础设施` | +919 | 30.6 | 128,638 | <a href="https://www.star-history.com/#kubernetes/kubernetes&Date"><img src="https://api.star-history.com/svg?repos=kubernetes/kubernetes&type=Date" width="260" alt="kubernetes/kubernetes 的星标历史曲线"></a> |
| 3 | [grafana/grafana](https://github.com/grafana/grafana)<br>指标日志链路，放进一个面板<br>`基础设施` | +760 | 25.3 | 77,663 | <a href="https://www.star-history.com/#grafana/grafana&Date"><img src="https://api.star-history.com/svg?repos=grafana/grafana&type=Date" width="260" alt="grafana/grafana 的星标历史曲线"></a> |
| 4 | [prometheus/prometheus](https://github.com/prometheus/prometheus)<br>系统出问题，告警先找到你<br>`基础设施` | +711 | 23.7 | 66,931 | <a href="https://www.star-history.com/#prometheus/prometheus&Date"><img src="https://api.star-history.com/svg?repos=prometheus/prometheus&type=Date" width="260" alt="prometheus/prometheus 的星标历史曲线"></a> |
| 5 | [traefik/traefik](https://github.com/traefik/traefik)<br>服务多了，流量自动分好<br>`基础设施` | +487 | 16.2 | 65,451 | <a href="https://www.star-history.com/#traefik/traefik&Date"><img src="https://api.star-history.com/svg?repos=traefik/traefik&type=Date" width="260" alt="traefik/traefik 的星标历史曲线"></a> |
| 6 | [hashicorp/terraform](https://github.com/hashicorp/terraform)<br>云资源写成代码，可审阅、可版本管理<br>`基础设施` | +401 | 13.4 | 50,120 | <a href="https://www.star-history.com/#hashicorp/terraform&Date"><img src="https://api.star-history.com/svg?repos=hashicorp/terraform&type=Date" width="260" alt="hashicorp/terraform 的星标历史曲线"></a> |
| 7 | [docker/compose](https://github.com/docker/compose)<br>多个容器写进一个文件，一起跑<br>`基础设施` | +390 | 13.0 | 38,584 | <a href="https://www.star-history.com/#docker/compose&Date"><img src="https://api.star-history.com/svg?repos=docker/compose&type=Date" width="260" alt="docker/compose 的星标历史曲线"></a> |
| 8 | [pulumi/pulumi](https://github.com/pulumi/pulumi)<br>用熟悉的编程语言管云资源<br>`基础设施` | +125 | 4.2 | 25,843 | <a href="https://www.star-history.com/#pulumi/pulumi&Date"><img src="https://api.star-history.com/svg?repos=pulumi/pulumi&type=Date" width="260" alt="pulumi/pulumi 的星标历史曲线"></a> |

### 今年增长最快（近 365 天）

| # | 项目 | 新增星标 | 星标/天 | 总星标 | 星标历史 |
|---|---|---:|---:|---:|---|
| 1 | [caddyserver/caddy](https://github.com/caddyserver/caddy)<br>搭网站服务器，HTTPS 自动配好<br>`基础设施` | +11,884 | 32.6 | 78,704 | <a href="https://www.star-history.com/#caddyserver/caddy&Date"><img src="https://api.star-history.com/svg?repos=caddyserver/caddy&type=Date" width="260" alt="caddyserver/caddy 的星标历史曲线"></a> |
| 2 | [kubernetes/kubernetes](https://github.com/kubernetes/kubernetes)<br>容器多了，部署扩容交给它<br>`基础设施` | +11,593 | 31.8 | 128,638 | <a href="https://www.star-history.com/#kubernetes/kubernetes&Date"><img src="https://api.star-history.com/svg?repos=kubernetes/kubernetes&type=Date" width="260" alt="kubernetes/kubernetes 的星标历史曲线"></a> |
| 3 | [traefik/traefik](https://github.com/traefik/traefik)<br>服务多了，流量自动分好<br>`基础设施` | +8,707 | 23.9 | 65,451 | <a href="https://www.star-history.com/#traefik/traefik&Date"><img src="https://api.star-history.com/svg?repos=traefik/traefik&type=Date" width="260" alt="traefik/traefik 的星标历史曲线"></a> |
| 4 | [grafana/grafana](https://github.com/grafana/grafana)<br>指标日志链路，放进一个面板<br>`基础设施` | +7,885 | 21.6 | 77,663 | <a href="https://www.star-history.com/#grafana/grafana&Date"><img src="https://api.star-history.com/svg?repos=grafana/grafana&type=Date" width="260" alt="grafana/grafana 的星标历史曲线"></a> |
| 5 | [prometheus/prometheus](https://github.com/prometheus/prometheus)<br>系统出问题，告警先找到你<br>`基础设施` | +6,537 | 17.9 | 66,931 | <a href="https://www.star-history.com/#prometheus/prometheus&Date"><img src="https://api.star-history.com/svg?repos=prometheus/prometheus&type=Date" width="260" alt="prometheus/prometheus 的星标历史曲线"></a> |
| 6 | [hashicorp/terraform](https://github.com/hashicorp/terraform)<br>云资源写成代码，可审阅、可版本管理<br>`基础设施` | +3,770 | 10.3 | 50,120 | <a href="https://www.star-history.com/#hashicorp/terraform&Date"><img src="https://api.star-history.com/svg?repos=hashicorp/terraform&type=Date" width="260" alt="hashicorp/terraform 的星标历史曲线"></a> |
| 7 | [docker/compose](https://github.com/docker/compose)<br>多个容器写进一个文件，一起跑<br>`基础设施` | +2,628 | 7.2 | 38,584 | <a href="https://www.star-history.com/#docker/compose&Date"><img src="https://api.star-history.com/svg?repos=docker/compose&type=Date" width="260" alt="docker/compose 的星标历史曲线"></a> |
| 8 | [pulumi/pulumi](https://github.com/pulumi/pulumi)<br>用熟悉的编程语言管云资源<br>`基础设施` | +2,076 | 5.7 | 25,843 | <a href="https://www.star-history.com/#pulumi/pulumi&Date"><img src="https://api.star-history.com/svg?repos=pulumi/pulumi&type=Date" width="260" alt="pulumi/pulumi 的星标历史曲线"></a> |

### 总星标数（历史累计）

| # | 项目 | 总星标 | 星标历史 |
|---|---|---:|---|
| 1 | [kubernetes/kubernetes](https://github.com/kubernetes/kubernetes)<br>容器多了，部署扩容交给它<br>`基础设施` | 128,638 | <a href="https://www.star-history.com/#kubernetes/kubernetes&Date"><img src="https://api.star-history.com/svg?repos=kubernetes/kubernetes&type=Date" width="260" alt="kubernetes/kubernetes 的星标历史曲线"></a> |
| 2 | [caddyserver/caddy](https://github.com/caddyserver/caddy)<br>搭网站服务器，HTTPS 自动配好<br>`基础设施` | 78,704 | <a href="https://www.star-history.com/#caddyserver/caddy&Date"><img src="https://api.star-history.com/svg?repos=caddyserver/caddy&type=Date" width="260" alt="caddyserver/caddy 的星标历史曲线"></a> |
| 3 | [grafana/grafana](https://github.com/grafana/grafana)<br>指标日志链路，放进一个面板<br>`基础设施` | 77,663 | <a href="https://www.star-history.com/#grafana/grafana&Date"><img src="https://api.star-history.com/svg?repos=grafana/grafana&type=Date" width="260" alt="grafana/grafana 的星标历史曲线"></a> |
| 4 | [prometheus/prometheus](https://github.com/prometheus/prometheus)<br>系统出问题，告警先找到你<br>`基础设施` | 66,931 | <a href="https://www.star-history.com/#prometheus/prometheus&Date"><img src="https://api.star-history.com/svg?repos=prometheus/prometheus&type=Date" width="260" alt="prometheus/prometheus 的星标历史曲线"></a> |
| 5 | [traefik/traefik](https://github.com/traefik/traefik)<br>服务多了，流量自动分好<br>`基础设施` | 65,451 | <a href="https://www.star-history.com/#traefik/traefik&Date"><img src="https://api.star-history.com/svg?repos=traefik/traefik&type=Date" width="260" alt="traefik/traefik 的星标历史曲线"></a> |
| 6 | [hashicorp/terraform](https://github.com/hashicorp/terraform)<br>云资源写成代码，可审阅、可版本管理<br>`基础设施` | 50,120 | <a href="https://www.star-history.com/#hashicorp/terraform&Date"><img src="https://api.star-history.com/svg?repos=hashicorp/terraform&type=Date" width="260" alt="hashicorp/terraform 的星标历史曲线"></a> |
| 7 | [docker/compose](https://github.com/docker/compose)<br>多个容器写进一个文件，一起跑<br>`基础设施` | 38,584 | <a href="https://www.star-history.com/#docker/compose&Date"><img src="https://api.star-history.com/svg?repos=docker/compose&type=Date" width="260" alt="docker/compose 的星标历史曲线"></a> |
| 8 | [pulumi/pulumi](https://github.com/pulumi/pulumi)<br>用熟悉的编程语言管云资源<br>`基础设施` | 25,843 | <a href="https://www.star-history.com/#pulumi/pulumi&Date"><img src="https://api.star-history.com/svg?repos=pulumi/pulumi&type=Date" width="260" alt="pulumi/pulumi 的星标历史曲线"></a> |

## 设计 / 创意

> 设计系统、绘图、动画与创意工具

### 最热新仓库（近 7 天内创建）

| # | 项目 | 创建时间（UTC） | 总星标 | 星标/天 | 星标历史 |
|---|---|---|---:|---:|---|
| 1 | [patch-gg/pixelfx](https://github.com/patch-gg/pixelfx)<br>缺像素特效？244段简短代码直接套用 | 2026-10-30<br><sub>4.6 天</sub> | 4,069 | 881.8 | <a href="https://www.star-history.com/#patch-gg/pixelfx&Date"><img src="https://api.star-history.com/svg?repos=patch-gg/pixelfx&type=Date" width="260" alt="patch-gg/pixelfx 的星标历史曲线"></a> |
| 2 | [kevinraymond/florilegium](https://github.com/kevinraymond/florilegium)<br>页面太单调？画上代尔夫特蓝花卉页边 | 2026-10-30<br><sub>4.6 天</sub> | 1,405 | 307.5 | <a href="https://www.star-history.com/#kevinraymond/florilegium&Date"><img src="https://api.star-history.com/svg?repos=kevinraymond/florilegium&type=Date" width="260" alt="kevinraymond/florilegium 的星标历史曲线"></a> |
| 3 | [DominikScholz/open-bot-avatar](https://github.com/DominikScholz/open-bot-avatar)<br>A JSON spec and renderer for interactive agent avatars | 2026-11-02<br><sub>1.2 天</sub> | 115 | 97.1 | <a href="https://www.star-history.com/#DominikScholz/open-bot-avatar&Date"><img src="https://api.star-history.com/svg?repos=DominikScholz/open-bot-avatar&type=Date" width="260" alt="DominikScholz/open-bot-avatar 的星标历史曲线"></a> |
| 4 | [op7418/dsh-guizang-design](https://github.com/op7418/dsh-guizang-design)<br>排版全是 AI 味？用一套设计系统去掉 | 2026-10-30<br><sub>4.3 天</sub> | 354 | 82.7 | <a href="https://www.star-history.com/#op7418/dsh-guizang-design&Date"><img src="https://api.star-history.com/svg?repos=op7418/dsh-guizang-design&type=Date" width="260" alt="op7418/dsh-guizang-design 的星标历史曲线"></a> |
| 5 | [GuoZheng-de-BaBa/nursing-research-skills](https://github.com/GuoZheng-de-BaBa/nursing-research-skills)<br>护理科研太繁琐，AI 技能帮你做 | 2026-10-30<br><sub>4.3 天</sub> | 228 | 53.0 | <a href="https://www.star-history.com/#GuoZheng-de-BaBa/nursing-research-skills&Date"><img src="https://api.star-history.com/svg?repos=GuoZheng-de-BaBa/nursing-research-skills&type=Date" width="260" alt="GuoZheng-de-BaBa/nursing-research-skills 的星标历史曲线"></a> |
| 6 | [Akillll-DuoHe/fy-code-animation](https://github.com/Akillll-DuoHe/fy-code-animation)<br>代码动画难做？文案与声音直接生成 | 2026-10-30<br><sub>4.5 天</sub> | 168 | 37.5 | <a href="https://www.star-history.com/#Akillll-DuoHe/fy-code-animation&Date"><img src="https://api.star-history.com/svg?repos=Akillll-DuoHe/fy-code-animation&type=Date" width="260" alt="Akillll-DuoHe/fy-code-animation 的星标历史曲线"></a> |
| 7 | [ersinkoc/AI-Video-Factory](https://github.com/ersinkoc/AI-Video-Factory)<br>给一个主题，智能体做成多语言视频 | 2026-10-29<br><sub>5.0 天</sub> | 177 | 35.7 | <a href="https://www.star-history.com/#ersinkoc/AI-Video-Factory&Date"><img src="https://api.star-history.com/svg?repos=ersinkoc/AI-Video-Factory&type=Date" width="260" alt="ersinkoc/AI-Video-Factory 的星标历史曲线"></a> |
| 8 | [enmerasoftware/ai-design-check](https://github.com/enmerasoftware/ai-design-check)<br>AI 智能体写的界面，帮你检查设计规范 | 2026-10-28<br><sub>6.6 天</sub> | 212 | 32.2 | <a href="https://www.star-history.com/#enmerasoftware/ai-design-check&Date"><img src="https://api.star-history.com/svg?repos=enmerasoftware/ai-design-check&type=Date" width="260" alt="enmerasoftware/ai-design-check 的星标历史曲线"></a> |

### 本周增长最快（近 7 天）

| # | 项目 | 新增星标 | 星标/天 | 总星标 | 星标历史 |
|---|---|---:|---:|---:|---|
| 1 | [excalidraw/excalidraw](https://github.com/excalidraw/excalidraw)<br>打开就画，像在纸上随手画图<br>`设计 / 创意` | +504 | 72.0 | 135,112 | <a href="https://www.star-history.com/#excalidraw/excalidraw&Date"><img src="https://api.star-history.com/svg?repos=excalidraw/excalidraw&type=Date" width="260" alt="excalidraw/excalidraw 的星标历史曲线"></a> |
| 2 | [penpot/penpot](https://github.com/penpot/penpot)<br>团队一起做设计，用开源平台<br>`设计 / 创意` | +313 | 44.7 | 62,027 | <a href="https://www.star-history.com/#penpot/penpot&Date"><img src="https://api.star-history.com/svg?repos=penpot/penpot&type=Date" width="260" alt="penpot/penpot 的星标历史曲线"></a> |
| 3 | [lucide-icons/lucide](https://github.com/lucide-icons/lucide)<br>一套图标风格统一，拿来就用<br>`设计 / 创意` | +175 | 25.0 | 25,510 | <a href="https://www.star-history.com/#lucide-icons/lucide&Date"><img src="https://api.star-history.com/svg?repos=lucide-icons/lucide&type=Date" width="260" alt="lucide-icons/lucide 的星标历史曲线"></a> |
| 4 | [jgraph/drawio](https://github.com/jgraph/drawio)<br>画图和白板，一个编辑器搞定<br>`设计 / 创意` | +150 | 21.4 | 9,163 | <a href="https://www.star-history.com/#jgraph/drawio&Date"><img src="https://api.star-history.com/svg?repos=jgraph/drawio&type=Date" width="260" alt="jgraph/drawio 的星标历史曲线"></a> |
| 5 | [saadeghi/daisyui](https://github.com/saadeghi/daisyui)<br>Tailwind 也有现成组件可挑<br>`设计 / 创意` | +74 | 10.6 | 42,731 | <a href="https://www.star-history.com/#saadeghi/daisyui&Date"><img src="https://api.star-history.com/svg?repos=saadeghi/daisyui&type=Date" width="260" alt="saadeghi/daisyui 的星标历史曲线"></a> |
| 6 | [airbnb/lottie-web](https://github.com/airbnb/lottie-web)<br>AE 做的动画，直接放进网页<br>`设计 / 创意` | +60 | 8.6 | 32,340 | <a href="https://www.star-history.com/#airbnb/lottie-web&Date"><img src="https://api.star-history.com/svg?repos=airbnb/lottie-web&type=Date" width="260" alt="airbnb/lottie-web 的星标历史曲线"></a> |
| 7 | [phosphor-icons/homepage](https://github.com/phosphor-icons/homepage)<br>一整套灵活的图标，人人可用<br>`设计 / 创意` | +33 | 4.7 | 7,761 | <a href="https://www.star-history.com/#phosphor-icons/homepage&Date"><img src="https://api.star-history.com/svg?repos=phosphor-icons/homepage&type=Date" width="260" alt="phosphor-icons/homepage 的星标历史曲线"></a> |
| 8 | [lottiefiles/lottie-ios](https://github.com/lottiefiles/lottie-ios)<br>AE 做的动画，直接放进 iOS<br>`设计 / 创意` | +0 | 0.0 | 43 | <a href="https://www.star-history.com/#lottiefiles/lottie-ios&Date"><img src="https://api.star-history.com/svg?repos=lottiefiles/lottie-ios&type=Date" width="260" alt="lottiefiles/lottie-ios 的星标历史曲线"></a> |

### 本月增长最快（近 30 天）

| # | 项目 | 新增星标 | 星标/天 | 总星标 | 星标历史 |
|---|---|---:|---:|---:|---|
| 1 | [excalidraw/excalidraw](https://github.com/excalidraw/excalidraw)<br>打开就画，像在纸上随手画图<br>`设计 / 创意` | +2,007 | 66.9 | 135,112 | <a href="https://www.star-history.com/#excalidraw/excalidraw&Date"><img src="https://api.star-history.com/svg?repos=excalidraw/excalidraw&type=Date" width="260" alt="excalidraw/excalidraw 的星标历史曲线"></a> |
| 2 | [penpot/penpot](https://github.com/penpot/penpot)<br>团队一起做设计，用开源平台<br>`设计 / 创意` | +1,488 | 49.6 | 62,027 | <a href="https://www.star-history.com/#penpot/penpot&Date"><img src="https://api.star-history.com/svg?repos=penpot/penpot&type=Date" width="260" alt="penpot/penpot 的星标历史曲线"></a> |
| 3 | [lucide-icons/lucide](https://github.com/lucide-icons/lucide)<br>一套图标风格统一，拿来就用<br>`设计 / 创意` | +699 | 23.3 | 25,510 | <a href="https://www.star-history.com/#lucide-icons/lucide&Date"><img src="https://api.star-history.com/svg?repos=lucide-icons/lucide&type=Date" width="260" alt="lucide-icons/lucide 的星标历史曲线"></a> |
| 4 | [jgraph/drawio](https://github.com/jgraph/drawio)<br>画图和白板，一个编辑器搞定<br>`设计 / 创意` | +625 | 20.8 | 9,163 | <a href="https://www.star-history.com/#jgraph/drawio&Date"><img src="https://api.star-history.com/svg?repos=jgraph/drawio&type=Date" width="260" alt="jgraph/drawio 的星标历史曲线"></a> |
| 5 | [saadeghi/daisyui](https://github.com/saadeghi/daisyui)<br>Tailwind 也有现成组件可挑<br>`设计 / 创意` | +283 | 9.4 | 42,731 | <a href="https://www.star-history.com/#saadeghi/daisyui&Date"><img src="https://api.star-history.com/svg?repos=saadeghi/daisyui&type=Date" width="260" alt="saadeghi/daisyui 的星标历史曲线"></a> |
| 6 | [airbnb/lottie-web](https://github.com/airbnb/lottie-web)<br>AE 做的动画，直接放进网页<br>`设计 / 创意` | +227 | 7.6 | 32,340 | <a href="https://www.star-history.com/#airbnb/lottie-web&Date"><img src="https://api.star-history.com/svg?repos=airbnb/lottie-web&type=Date" width="260" alt="airbnb/lottie-web 的星标历史曲线"></a> |
| 7 | [phosphor-icons/homepage](https://github.com/phosphor-icons/homepage)<br>一整套灵活的图标，人人可用<br>`设计 / 创意` | +177 | 5.9 | 7,761 | <a href="https://www.star-history.com/#phosphor-icons/homepage&Date"><img src="https://api.star-history.com/svg?repos=phosphor-icons/homepage&type=Date" width="260" alt="phosphor-icons/homepage 的星标历史曲线"></a> |
| 8 | [lottiefiles/lottie-ios](https://github.com/lottiefiles/lottie-ios)<br>AE 做的动画，直接放进 iOS<br>`设计 / 创意` | +0 | 0.0 | 43 | <a href="https://www.star-history.com/#lottiefiles/lottie-ios&Date"><img src="https://api.star-history.com/svg?repos=lottiefiles/lottie-ios&type=Date" width="260" alt="lottiefiles/lottie-ios 的星标历史曲线"></a> |

### 今年增长最快（近 365 天）

| # | 项目 | 新增星标 | 星标/天 | 总星标 | 星标历史 |
|---|---|---:|---:|---:|---|
| 1 | [excalidraw/excalidraw](https://github.com/excalidraw/excalidraw)<br>打开就画，像在纸上随手画图<br>`设计 / 创意` | +27,065 | 74.2 | 135,112 | <a href="https://www.star-history.com/#excalidraw/excalidraw&Date"><img src="https://api.star-history.com/svg?repos=excalidraw/excalidraw&type=Date" width="260" alt="excalidraw/excalidraw 的星标历史曲线"></a> |
| 2 | [penpot/penpot](https://github.com/penpot/penpot)<br>团队一起做设计，用开源平台<br>`设计 / 创意` | +21,740 | 59.6 | 62,027 | <a href="https://www.star-history.com/#penpot/penpot&Date"><img src="https://api.star-history.com/svg?repos=penpot/penpot&type=Date" width="260" alt="penpot/penpot 的星标历史曲线"></a> |
| 3 | [jgraph/drawio](https://github.com/jgraph/drawio)<br>画图和白板，一个编辑器搞定<br>`设计 / 创意` | +6,501 | 17.8 | 9,163 | <a href="https://www.star-history.com/#jgraph/drawio&Date"><img src="https://api.star-history.com/svg?repos=jgraph/drawio&type=Date" width="260" alt="jgraph/drawio 的星标历史曲线"></a> |
| 4 | [lucide-icons/lucide](https://github.com/lucide-icons/lucide)<br>一套图标风格统一，拿来就用<br>`设计 / 创意` | +6,269 | 17.2 | 25,510 | <a href="https://www.star-history.com/#lucide-icons/lucide&Date"><img src="https://api.star-history.com/svg?repos=lucide-icons/lucide&type=Date" width="260" alt="lucide-icons/lucide 的星标历史曲线"></a> |
| 5 | [saadeghi/daisyui](https://github.com/saadeghi/daisyui)<br>Tailwind 也有现成组件可挑<br>`设计 / 创意` | +4,228 | 11.6 | 42,731 | <a href="https://www.star-history.com/#saadeghi/daisyui&Date"><img src="https://api.star-history.com/svg?repos=saadeghi/daisyui&type=Date" width="260" alt="saadeghi/daisyui 的星标历史曲线"></a> |
| 6 | [phosphor-icons/homepage](https://github.com/phosphor-icons/homepage)<br>一整套灵活的图标，人人可用<br>`设计 / 创意` | +2,194 | 6.0 | 7,761 | <a href="https://www.star-history.com/#phosphor-icons/homepage&Date"><img src="https://api.star-history.com/svg?repos=phosphor-icons/homepage&type=Date" width="260" alt="phosphor-icons/homepage 的星标历史曲线"></a> |
| 7 | [airbnb/lottie-web](https://github.com/airbnb/lottie-web)<br>AE 做的动画，直接放进网页<br>`设计 / 创意` | +1,098 | 3.0 | 32,340 | <a href="https://www.star-history.com/#airbnb/lottie-web&Date"><img src="https://api.star-history.com/svg?repos=airbnb/lottie-web&type=Date" width="260" alt="airbnb/lottie-web 的星标历史曲线"></a> |
| 8 | [lottiefiles/lottie-ios](https://github.com/lottiefiles/lottie-ios)<br>AE 做的动画，直接放进 iOS<br>`设计 / 创意` | +1 | 0.0 | 43 | <a href="https://www.star-history.com/#lottiefiles/lottie-ios&Date"><img src="https://api.star-history.com/svg?repos=lottiefiles/lottie-ios&type=Date" width="260" alt="lottiefiles/lottie-ios 的星标历史曲线"></a> |

### 总星标数（历史累计）

| # | 项目 | 总星标 | 星标历史 |
|---|---|---:|---|
| 1 | [excalidraw/excalidraw](https://github.com/excalidraw/excalidraw)<br>打开就画，像在纸上随手画图<br>`设计 / 创意` | 135,112 | <a href="https://www.star-history.com/#excalidraw/excalidraw&Date"><img src="https://api.star-history.com/svg?repos=excalidraw/excalidraw&type=Date" width="260" alt="excalidraw/excalidraw 的星标历史曲线"></a> |
| 2 | [penpot/penpot](https://github.com/penpot/penpot)<br>团队一起做设计，用开源平台<br>`设计 / 创意` | 62,027 | <a href="https://www.star-history.com/#penpot/penpot&Date"><img src="https://api.star-history.com/svg?repos=penpot/penpot&type=Date" width="260" alt="penpot/penpot 的星标历史曲线"></a> |
| 3 | [saadeghi/daisyui](https://github.com/saadeghi/daisyui)<br>Tailwind 也有现成组件可挑<br>`设计 / 创意` | 42,731 | <a href="https://www.star-history.com/#saadeghi/daisyui&Date"><img src="https://api.star-history.com/svg?repos=saadeghi/daisyui&type=Date" width="260" alt="saadeghi/daisyui 的星标历史曲线"></a> |
| 4 | [airbnb/lottie-web](https://github.com/airbnb/lottie-web)<br>AE 做的动画，直接放进网页<br>`设计 / 创意` | 32,340 | <a href="https://www.star-history.com/#airbnb/lottie-web&Date"><img src="https://api.star-history.com/svg?repos=airbnb/lottie-web&type=Date" width="260" alt="airbnb/lottie-web 的星标历史曲线"></a> |
| 5 | [lucide-icons/lucide](https://github.com/lucide-icons/lucide)<br>一套图标风格统一，拿来就用<br>`设计 / 创意` | 25,510 | <a href="https://www.star-history.com/#lucide-icons/lucide&Date"><img src="https://api.star-history.com/svg?repos=lucide-icons/lucide&type=Date" width="260" alt="lucide-icons/lucide 的星标历史曲线"></a> |
| 6 | [jgraph/drawio](https://github.com/jgraph/drawio)<br>画图和白板，一个编辑器搞定<br>`设计 / 创意` | 9,163 | <a href="https://www.star-history.com/#jgraph/drawio&Date"><img src="https://api.star-history.com/svg?repos=jgraph/drawio&type=Date" width="260" alt="jgraph/drawio 的星标历史曲线"></a> |
| 7 | [phosphor-icons/homepage](https://github.com/phosphor-icons/homepage)<br>一整套灵活的图标，人人可用<br>`设计 / 创意` | 7,761 | <a href="https://www.star-history.com/#phosphor-icons/homepage&Date"><img src="https://api.star-history.com/svg?repos=phosphor-icons/homepage&type=Date" width="260" alt="phosphor-icons/homepage 的星标历史曲线"></a> |
| 8 | [lottiefiles/lottie-ios](https://github.com/lottiefiles/lottie-ios)<br>AE 做的动画，直接放进 iOS<br>`设计 / 创意` | 43 | <a href="https://www.star-history.com/#lottiefiles/lottie-ios&Date"><img src="https://api.star-history.com/svg?repos=lottiefiles/lottie-ios&type=Date" width="260" alt="lottiefiles/lottie-ios 的星标历史曲线"></a> |

## 数据

> 数据库、分析、ETL 与数据工程

### 最热新仓库（近 7 天内创建）

本次运行中没有符合条件的新仓库。

### 本周增长最快（近 7 天）

| # | 项目 | 新增星标 | 星标/天 | 总星标 | 星标历史 |
|---|---|---:|---:|---:|---|
| 1 | [duckdb/duckdb](https://github.com/duckdb/duckdb)<br>不搭数据库服务，也能跑 SQL 分析<br>`数据` | +196 | 28.0 | 42,785 | <a href="https://www.star-history.com/#duckdb/duckdb&Date"><img src="https://api.star-history.com/svg?repos=duckdb/duckdb&type=Date" width="260" alt="duckdb/duckdb 的星标历史曲线"></a> |
| 2 | [ClickHouse/ClickHouse](https://github.com/ClickHouse/ClickHouse)<br>大量数据实时分析，用开源的<br>`数据` | +121 | 17.3 | 50,736 | <a href="https://www.star-history.com/#ClickHouse/ClickHouse&Date"><img src="https://api.star-history.com/svg?repos=ClickHouse/ClickHouse&type=Date" width="260" alt="ClickHouse/ClickHouse 的星标历史曲线"></a> |
| 3 | [apache/superset](https://github.com/apache/superset)<br>数据看不懂，做成图就明白<br>`数据` | +100 | 14.3 | 75,398 | <a href="https://www.star-history.com/#apache/superset&Date"><img src="https://api.star-history.com/svg?repos=apache/superset&type=Date" width="260" alt="apache/superset 的星标历史曲线"></a> |
| 4 | [pola-rs/polars](https://github.com/pola-rs/polars)<br>表格数据处理快，不用干等<br>`数据` | +59 | 8.4 | 40,257 | <a href="https://www.star-history.com/#pola-rs/polars&Date"><img src="https://api.star-history.com/svg?repos=pola-rs/polars&type=Date" width="260" alt="pola-rs/polars 的星标历史曲线"></a> |
| 5 | [apache/kafka](https://github.com/apache/kafka)<br>系统之间的事件流，交给它来传<br>`数据` | +59 | 8.4 | 34,122 | <a href="https://www.star-history.com/#apache/kafka&Date"><img src="https://api.star-history.com/svg?repos=apache/kafka&type=Date" width="260" alt="apache/kafka 的星标历史曲线"></a> |
| 6 | [apache/arrow](https://github.com/apache/arrow)<br>不同语言之间，数据直接通用<br>`数据` | +43 | 6.1 | 17,274 | <a href="https://www.star-history.com/#apache/arrow&Date"><img src="https://api.star-history.com/svg?repos=apache/arrow&type=Date" width="260" alt="apache/arrow 的星标历史曲线"></a> |
| 7 | [dbt-labs/dbt-core](https://github.com/dbt-labs/dbt-core)<br>数据转换，照软件工程的做法来<br>`数据` | +29 | 4.1 | 14,115 | <a href="https://www.star-history.com/#dbt-labs/dbt-core&Date"><img src="https://api.star-history.com/svg?repos=dbt-labs/dbt-core&type=Date" width="260" alt="dbt-labs/dbt-core 的星标历史曲线"></a> |
| 8 | [jupyter/notebook](https://github.com/jupyter/notebook)<br>在网页里写代码，边写边看结果<br>`数据` | +4 | 0.6 | 13,458 | <a href="https://www.star-history.com/#jupyter/notebook&Date"><img src="https://api.star-history.com/svg?repos=jupyter/notebook&type=Date" width="260" alt="jupyter/notebook 的星标历史曲线"></a> |

### 本月增长最快（近 30 天）

| # | 项目 | 新增星标 | 星标/天 | 总星标 | 星标历史 |
|---|---|---:|---:|---:|---|
| 1 | [duckdb/duckdb](https://github.com/duckdb/duckdb)<br>不搭数据库服务，也能跑 SQL 分析<br>`数据` | +945 | 31.5 | 42,785 | <a href="https://www.star-history.com/#duckdb/duckdb&Date"><img src="https://api.star-history.com/svg?repos=duckdb/duckdb&type=Date" width="260" alt="duckdb/duckdb 的星标历史曲线"></a> |
| 2 | [ClickHouse/ClickHouse](https://github.com/ClickHouse/ClickHouse)<br>大量数据实时分析，用开源的<br>`数据` | +588 | 19.6 | 50,736 | <a href="https://www.star-history.com/#ClickHouse/ClickHouse&Date"><img src="https://api.star-history.com/svg?repos=ClickHouse/ClickHouse&type=Date" width="260" alt="ClickHouse/ClickHouse 的星标历史曲线"></a> |
| 3 | [apache/superset](https://github.com/apache/superset)<br>数据看不懂，做成图就明白<br>`数据` | +459 | 15.3 | 75,398 | <a href="https://www.star-history.com/#apache/superset&Date"><img src="https://api.star-history.com/svg?repos=apache/superset&type=Date" width="260" alt="apache/superset 的星标历史曲线"></a> |
| 4 | [pola-rs/polars](https://github.com/pola-rs/polars)<br>表格数据处理快，不用干等<br>`数据` | +387 | 12.9 | 40,257 | <a href="https://www.star-history.com/#pola-rs/polars&Date"><img src="https://api.star-history.com/svg?repos=pola-rs/polars&type=Date" width="260" alt="pola-rs/polars 的星标历史曲线"></a> |
| 5 | [apache/kafka](https://github.com/apache/kafka)<br>系统之间的事件流，交给它来传<br>`数据` | +292 | 9.7 | 34,122 | <a href="https://www.star-history.com/#apache/kafka&Date"><img src="https://api.star-history.com/svg?repos=apache/kafka&type=Date" width="260" alt="apache/kafka 的星标历史曲线"></a> |
| 6 | [dbt-labs/dbt-core](https://github.com/dbt-labs/dbt-core)<br>数据转换，照软件工程的做法来<br>`数据` | +168 | 5.6 | 14,115 | <a href="https://www.star-history.com/#dbt-labs/dbt-core&Date"><img src="https://api.star-history.com/svg?repos=dbt-labs/dbt-core&type=Date" width="260" alt="dbt-labs/dbt-core 的星标历史曲线"></a> |
| 7 | [apache/arrow](https://github.com/apache/arrow)<br>不同语言之间，数据直接通用<br>`数据` | +120 | 4.0 | 17,274 | <a href="https://www.star-history.com/#apache/arrow&Date"><img src="https://api.star-history.com/svg?repos=apache/arrow&type=Date" width="260" alt="apache/arrow 的星标历史曲线"></a> |
| 8 | [jupyter/notebook](https://github.com/jupyter/notebook)<br>在网页里写代码，边写边看结果<br>`数据` | +70 | 2.3 | 13,458 | <a href="https://www.star-history.com/#jupyter/notebook&Date"><img src="https://api.star-history.com/svg?repos=jupyter/notebook&type=Date" width="260" alt="jupyter/notebook 的星标历史曲线"></a> |

### 今年增长最快（近 365 天）

| # | 项目 | 新增星标 | 星标/天 | 总星标 | 星标历史 |
|---|---|---:|---:|---:|---|
| 1 | [duckdb/duckdb](https://github.com/duckdb/duckdb)<br>不搭数据库服务，也能跑 SQL 分析<br>`数据` | +9,374 | 25.7 | 42,785 | <a href="https://www.star-history.com/#duckdb/duckdb&Date"><img src="https://api.star-history.com/svg?repos=duckdb/duckdb&type=Date" width="260" alt="duckdb/duckdb 的星标历史曲线"></a> |
| 2 | [ClickHouse/ClickHouse](https://github.com/ClickHouse/ClickHouse)<br>大量数据实时分析，用开源的<br>`数据` | +7,624 | 20.9 | 50,736 | <a href="https://www.star-history.com/#ClickHouse/ClickHouse&Date"><img src="https://api.star-history.com/svg?repos=ClickHouse/ClickHouse&type=Date" width="260" alt="ClickHouse/ClickHouse 的星标历史曲线"></a> |
| 3 | [apache/superset](https://github.com/apache/superset)<br>数据看不懂，做成图就明白<br>`数据` | +7,436 | 20.4 | 75,398 | <a href="https://www.star-history.com/#apache/superset&Date"><img src="https://api.star-history.com/svg?repos=apache/superset&type=Date" width="260" alt="apache/superset 的星标历史曲线"></a> |
| 4 | [pola-rs/polars](https://github.com/pola-rs/polars)<br>表格数据处理快，不用干等<br>`数据` | +4,853 | 13.3 | 40,257 | <a href="https://www.star-history.com/#pola-rs/polars&Date"><img src="https://api.star-history.com/svg?repos=pola-rs/polars&type=Date" width="260" alt="pola-rs/polars 的星标历史曲线"></a> |
| 5 | [apache/kafka](https://github.com/apache/kafka)<br>系统之间的事件流，交给它来传<br>`数据` | +3,295 | 9.0 | 34,122 | <a href="https://www.star-history.com/#apache/kafka&Date"><img src="https://api.star-history.com/svg?repos=apache/kafka&type=Date" width="260" alt="apache/kafka 的星标历史曲线"></a> |
| 6 | [dbt-labs/dbt-core](https://github.com/dbt-labs/dbt-core)<br>数据转换，照软件工程的做法来<br>`数据` | +2,465 | 6.8 | 14,115 | <a href="https://www.star-history.com/#dbt-labs/dbt-core&Date"><img src="https://api.star-history.com/svg?repos=dbt-labs/dbt-core&type=Date" width="260" alt="dbt-labs/dbt-core 的星标历史曲线"></a> |
| 7 | [apache/arrow](https://github.com/apache/arrow)<br>不同语言之间，数据直接通用<br>`数据` | +1,318 | 3.6 | 17,274 | <a href="https://www.star-history.com/#apache/arrow&Date"><img src="https://api.star-history.com/svg?repos=apache/arrow&type=Date" width="260" alt="apache/arrow 的星标历史曲线"></a> |
| 8 | [jupyter/notebook](https://github.com/jupyter/notebook)<br>在网页里写代码，边写边看结果<br>`数据` | +904 | 2.5 | 13,458 | <a href="https://www.star-history.com/#jupyter/notebook&Date"><img src="https://api.star-history.com/svg?repos=jupyter/notebook&type=Date" width="260" alt="jupyter/notebook 的星标历史曲线"></a> |

### 总星标数（历史累计）

| # | 项目 | 总星标 | 星标历史 |
|---|---|---:|---|
| 1 | [apache/superset](https://github.com/apache/superset)<br>数据看不懂，做成图就明白<br>`数据` | 75,398 | <a href="https://www.star-history.com/#apache/superset&Date"><img src="https://api.star-history.com/svg?repos=apache/superset&type=Date" width="260" alt="apache/superset 的星标历史曲线"></a> |
| 2 | [ClickHouse/ClickHouse](https://github.com/ClickHouse/ClickHouse)<br>大量数据实时分析，用开源的<br>`数据` | 50,736 | <a href="https://www.star-history.com/#ClickHouse/ClickHouse&Date"><img src="https://api.star-history.com/svg?repos=ClickHouse/ClickHouse&type=Date" width="260" alt="ClickHouse/ClickHouse 的星标历史曲线"></a> |
| 3 | [duckdb/duckdb](https://github.com/duckdb/duckdb)<br>不搭数据库服务，也能跑 SQL 分析<br>`数据` | 42,785 | <a href="https://www.star-history.com/#duckdb/duckdb&Date"><img src="https://api.star-history.com/svg?repos=duckdb/duckdb&type=Date" width="260" alt="duckdb/duckdb 的星标历史曲线"></a> |
| 4 | [pola-rs/polars](https://github.com/pola-rs/polars)<br>表格数据处理快，不用干等<br>`数据` | 40,257 | <a href="https://www.star-history.com/#pola-rs/polars&Date"><img src="https://api.star-history.com/svg?repos=pola-rs/polars&type=Date" width="260" alt="pola-rs/polars 的星标历史曲线"></a> |
| 5 | [apache/kafka](https://github.com/apache/kafka)<br>系统之间的事件流，交给它来传<br>`数据` | 34,122 | <a href="https://www.star-history.com/#apache/kafka&Date"><img src="https://api.star-history.com/svg?repos=apache/kafka&type=Date" width="260" alt="apache/kafka 的星标历史曲线"></a> |
| 6 | [apache/arrow](https://github.com/apache/arrow)<br>不同语言之间，数据直接通用<br>`数据` | 17,274 | <a href="https://www.star-history.com/#apache/arrow&Date"><img src="https://api.star-history.com/svg?repos=apache/arrow&type=Date" width="260" alt="apache/arrow 的星标历史曲线"></a> |
| 7 | [dbt-labs/dbt-core](https://github.com/dbt-labs/dbt-core)<br>数据转换，照软件工程的做法来<br>`数据` | 14,115 | <a href="https://www.star-history.com/#dbt-labs/dbt-core&Date"><img src="https://api.star-history.com/svg?repos=dbt-labs/dbt-core&type=Date" width="260" alt="dbt-labs/dbt-core 的星标历史曲线"></a> |
| 8 | [jupyter/notebook](https://github.com/jupyter/notebook)<br>在网页里写代码，边写边看结果<br>`数据` | 13,458 | <a href="https://www.star-history.com/#jupyter/notebook&Date"><img src="https://api.star-history.com/svg?repos=jupyter/notebook&type=Date" width="260" alt="jupyter/notebook 的星标历史曲线"></a> |

---

如果它帮你省了时间，请给仓库点个星标，让更多人找得到。

如何引用：见 [CITATION.cff](CITATION.cff)。

数据怎么算和如何参与：[docs/HOW_IT_WORKS.zh-Hans.md](docs/HOW_IT_WORKS.zh-Hans.md)。新仓库规则：[docs/NEW_ARRIVALS.md](docs/NEW_ARRIVALS.md)。分类说明：[docs/CATEGORIES.md](docs/CATEGORIES.md)。提交改动：[CONTRIBUTING.md](CONTRIBUTING.md)。
