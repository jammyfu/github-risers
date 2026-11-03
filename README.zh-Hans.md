[English](README.md) | **简体中文** | [繁體中文](README.zh-Hant.md) | [日本語](README.ja.md) | [한국어](README.ko.md)

# GitHub 涨星榜 / GitHub Risers

<img src=".github/social-preview.png" alt="GitHub 涨星榜 / GitHub Risers" width="640">

[![MIT](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE) [![CI](https://github.com/jammyfu/github-risers/actions/workflows/ci.yml/badge.svg)](https://github.com/jammyfu/github-risers/actions/workflows/ci.yml) [![updated](https://img.shields.io/badge/dynamic/json?url=https%3A%2F%2Fraw.githubusercontent.com%2Fjammyfu%2Fgithub-risers%2Fmain%2Fdata%2Fstats.json&query=%24.today_utc&label=updated&color=brightgreen)](latest/rankings.zh-Hans.md)

按每天新增星标（而不是总星标）给 GitHub 仓库排名：AI 在前，其后是开发者工具、安全、Web / 前端、基础设施、设计 / 创意和数据；每天更新两次。

数据取自 2026-11-02 23:18（UTC）。每天两次：北京时间 0 点（UTC+8）、洛杉矶时间 0 点（America/Los_Angeles）。

[网站](https://jammyfu.github.io/github-risers/) · [运作方式](docs/HOW_IT_WORKS.zh-Hans.md) · [事实速查](docs/FACTS.md) · [历史榜单](rankings/README.zh-Hans.md) · [最新快照](latest/rankings.zh-Hans.md)

## 本期各类榜首

| 分类 | 新仓库第 1 名（7 天） | 本周第 1 名 | 本月第 1 名 | 今年第 1 名 | 总星标第 1 名 |
|---|---|---|---|---|---|
| **[人工智能](#人工智能)** ★ 主榜 | [wangzan101/Mika](https://github.com/wangzan101/Mika)<br>1,203/天 | [morluto/rea](https://github.com/morluto/rea)<br>4,904/天 | [morluto/rea](https://github.com/morluto/rea)<br>13,987/天 | [deepseek-ai/deepseek-harness](https://github.com/deepseek-ai/deepseek-harness)<br>3,318/天 | [morluto/rea](https://github.com/morluto/rea)<br>422,740 ★ |
| **[开发者工具](#开发者工具)** | [Verlintas/NOIR](https://github.com/Verlintas/NOIR)<br>610/天 | [zed-industries/zed](https://github.com/zed-industries/zed)<br>56.6/天 | [zed-industries/zed](https://github.com/zed-industries/zed)<br>52.9/天 | [zed-industries/zed](https://github.com/zed-industries/zed)<br>70.3/天 | [oven-sh/bun](https://github.com/oven-sh/bun)<br>96,519 ★ |
| **[安全](#安全)** | 无 | [projectdiscovery/nuclei](https://github.com/projectdiscovery/nuclei)<br>32.7/天 | [projectdiscovery/nuclei](https://github.com/projectdiscovery/nuclei)<br>30.6/天 | [aquasecurity/trivy](https://github.com/aquasecurity/trivy)<br>27.7/天 | [aquasecurity/trivy](https://github.com/aquasecurity/trivy)<br>38,917 ★ |
| **[Web / 前端](#web--前端)** | [shipwords-dev/shipwords](https://github.com/shipwords-dev/shipwords)<br>60.7/天 | [shadcn-ui/ui](https://github.com/shadcn-ui/ui)<br>95.4/天 | [shadcn-ui/ui](https://github.com/shadcn-ui/ui)<br>87.4/天 | [shadcn-ui/ui](https://github.com/shadcn-ui/ui)<br>83.2/天 | [facebook/react](https://github.com/facebook/react)<br>251,874 ★ |
| **[基础设施](#基础设施)** | [davemessew/AgentFlux](https://github.com/davemessew/AgentFlux)<br>38.8/天 | [caddyserver/caddy](https://github.com/caddyserver/caddy)<br>37.9/天 | [caddyserver/caddy](https://github.com/caddyserver/caddy)<br>84.0/天 | [caddyserver/caddy](https://github.com/caddyserver/caddy)<br>32.5/天 | [kubernetes/kubernetes](https://github.com/kubernetes/kubernetes)<br>128,619 ★ |
| **[设计 / 创意](#设计--创意)** | [patch-gg/pixelfx](https://github.com/patch-gg/pixelfx)<br>940/天 | [excalidraw/excalidraw](https://github.com/excalidraw/excalidraw)<br>70.3/天 | [excalidraw/excalidraw](https://github.com/excalidraw/excalidraw)<br>66.0/天 | [excalidraw/excalidraw](https://github.com/excalidraw/excalidraw)<br>74.0/天 | [excalidraw/excalidraw](https://github.com/excalidraw/excalidraw)<br>135,054 ★ |
| **[数据](#数据)** | 无 | [duckdb/duckdb](https://github.com/duckdb/duckdb)<br>29.9/天 | [duckdb/duckdb](https://github.com/duckdb/duckdb)<br>30.9/天 | [duckdb/duckdb](https://github.com/duckdb/duckdb)<br>25.6/天 | [apache/superset](https://github.com/apache/superset)<br>75,392 ★ |

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
| 1 | [wangzan101/Mika](https://github.com/wangzan101/Mika)<br>手机琐事太多？让智能体替你操作应用 | 2026-10-29<br><sub>4.4 天</sub> | 5,250 | 1,203.0 | <a href="https://www.star-history.com/#wangzan101/Mika&Date"><img src="https://api.star-history.com/svg?repos=wangzan101/Mika&type=Date" width="260" alt="wangzan101/Mika 的星标历史曲线"></a> |
| 2 | [caru-ini/stack-diagram](https://github.com/caru-ini/stack-diagram)<br>一句话描述技术栈，自动生成架构图 | 2026-11-01<br><sub>1.7 天</sub> | 1,156 | 665.0 | <a href="https://www.star-history.com/#caru-ini/stack-diagram&Date"><img src="https://api.star-history.com/svg?repos=caru-ini/stack-diagram&type=Date" width="260" alt="caru-ini/stack-diagram 的星标历史曲线"></a> |
| 3 | [Balanov/uncut](https://github.com/Balanov/uncut)<br>告别静默截断，无损运行代码智能体 | 2026-11-01<br><sub>1.2 天</sub> | 571 | 457.1 | <a href="https://www.star-history.com/#Balanov/uncut&Date"><img src="https://api.star-history.com/svg?repos=Balanov/uncut&type=Date" width="260" alt="Balanov/uncut 的星标历史曲线"></a> |
| 4 | [haydenschmitty/floorplan](https://github.com/haydenschmitty/floorplan)<br>代码库怎么拼起来的，看这张图 | 2026-10-27<br><sub>6.5 天</sub> | 2,227 | 344.3 | <a href="https://www.star-history.com/#haydenschmitty/floorplan&Date"><img src="https://api.star-history.com/svg?repos=haydenschmitty/floorplan&type=Date" width="260" alt="haydenschmitty/floorplan 的星标历史曲线"></a> |
| 5 | [modelflare-ai/AnyModelBot](https://github.com/modelflare-ai/AnyModelBot)<br>🤖 Grok Bot、OpenAI dots 和 Claude Duet 的开源、本地优先替代品。在任何模型上拥有你自己的 AI 机器人：GPT、Claude、Gemini、Grok、DeepSeek、Kimi、GLM… | 2026-10-27<br><sub>6.6 天</sub> | 1,328 | 201.1 | <a href="https://www.star-history.com/#modelflare-ai/AnyModelBot&Date"><img src="https://api.star-history.com/svg?repos=modelflare-ai/AnyModelBot&type=Date" width="260" alt="modelflare-ai/AnyModelBot 的星标历史曲线"></a> |
| 6 | [NiazMorshed2007/reanimate](https://github.com/NiazMorshed2007/reanimate)<br>动效抄不像？逐帧还原并验证完全一致 | 2026-10-29<br><sub>4.7 天</sub> | 944 | 200.6 | <a href="https://www.star-history.com/#NiazMorshed2007/reanimate&Date"><img src="https://api.star-history.com/svg?repos=NiazMorshed2007/reanimate&type=Date" width="260" alt="NiazMorshed2007/reanimate 的星标历史曲线"></a> |
| 7 | [N1nEmAn/sapper-v2](https://github.com/N1nEmAn/sapper-v2)<br>安全测试太费劲？让 AI 军团自主排查 | 2026-10-30<br><sub>3.3 天</sub> | 596 | 178.6 | <a href="https://www.star-history.com/#N1nEmAn/sapper-v2&Date"><img src="https://api.star-history.com/svg?repos=N1nEmAn/sapper-v2&type=Date" width="260" alt="N1nEmAn/sapper-v2 的星标历史曲线"></a> |
| 8 | [zhanghao123vip/ai-manju-skills](https://github.com/zhanghao123vip/ai-manju-skills)<br>只有一个点子，也能生成全流程 AI 漫剧 | 2026-10-31<br><sub>2.8 天</sub> | 458 | 161.8 | <a href="https://www.star-history.com/#zhanghao123vip/ai-manju-skills&Date"><img src="https://api.star-history.com/svg?repos=zhanghao123vip/ai-manju-skills&type=Date" width="260" alt="zhanghao123vip/ai-manju-skills 的星标历史曲线"></a> |
| 9 | [sleepy-zone/ai-ref-library-cn](https://github.com/sleepy-zone/ai-ref-library-cn)<br>AI作图缺参考？备齐脸型姿势与服装 | 2026-10-29<br><sub>4.3 天</sub> | 667 | 154.2 | <a href="https://www.star-history.com/#sleepy-zone/ai-ref-library-cn&Date"><img src="https://api.star-history.com/svg?repos=sleepy-zone/ai-ref-library-cn&type=Date" width="260" alt="sleepy-zone/ai-ref-library-cn 的星标历史曲线"></a> |
| 10 | [alchaincyf/huashu-bird-sticker](https://github.com/alchaincyf/huashu-bird-sticker)<br>找鸟类贴纸太难？集齐 11,064 种鸟 | 2026-10-30<br><sub>3.8 天</sub> | 572 | 152.6 | <a href="https://www.star-history.com/#alchaincyf/huashu-bird-sticker&Date"><img src="https://api.star-history.com/svg?repos=alchaincyf/huashu-bird-sticker&type=Date" width="260" alt="alchaincyf/huashu-bird-sticker 的星标历史曲线"></a> |

### 本周增长最快（近 7 天）

| # | 项目 | 新增星标 | 星标/天 | 总星标 | 星标历史 |
|---|---|---:|---:|---:|---|
| 1 | [morluto/rea](https://github.com/morluto/rea)<br>让 AI 帮你克隆任何软件<br>`人工智能` | +34,330 | 4,904.3 | 422,740 | <a href="https://www.star-history.com/#morluto/rea&Date"><img src="https://api.star-history.com/svg?repos=morluto/rea&type=Date" width="260" alt="morluto/rea 的星标历史曲线"></a> |
| 2 | [cloudflare/security-audit-skill](https://github.com/cloudflare/security-audit-skill)<br>AI 查代码漏洞，另一个 AI 逐条复核<br>`人工智能` | +9,348 | 1,335.4 | 57,354 | <a href="https://www.star-history.com/#cloudflare/security-audit-skill&Date"><img src="https://api.star-history.com/svg?repos=cloudflare/security-audit-skill&type=Date" width="260" alt="cloudflare/security-audit-skill 的星标历史曲线"></a> |
| 3 | [deepseek-ai/deepseek-harness](https://github.com/deepseek-ai/deepseek-harness)<br>想要什么智能体，用插件自己拼<br>`人工智能` | +7,360 | 1,051.4 | 269,552 | <a href="https://www.star-history.com/#deepseek-ai/deepseek-harness&Date"><img src="https://api.star-history.com/svg?repos=deepseek-ai/deepseek-harness&type=Date" width="260" alt="deepseek-ai/deepseek-harness 的星标历史曲线"></a> |
| 4 | [stablyai/orca](https://github.com/stablyai/orca)<br>几个 AI 一起写，谁好用一眼看出<br>`人工智能` | +6,941 | 991.6 | 113,572 | <a href="https://www.star-history.com/#stablyai/orca&Date"><img src="https://api.star-history.com/svg?repos=stablyai/orca&type=Date" width="260" alt="stablyai/orca 的星标历史曲线"></a> |
| 5 | [thedotmack/claude-mem](https://github.com/thedotmack/claude-mem)<br>AI 不再忘记上次做到哪<br>`人工智能` | +6,863 | 980.4 | 110,698 | <a href="https://www.star-history.com/#thedotmack/claude-mem&Date"><img src="https://api.star-history.com/svg?repos=thedotmack/claude-mem&type=Date" width="260" alt="thedotmack/claude-mem 的星标历史曲线"></a> |
| 6 | [yetone/magpie](https://github.com/yetone/magpie)<br>编程 AI 换模型，额度用完自动续<br>`人工智能` | +6,346 | 906.6 | 28,379 | <a href="https://www.star-history.com/#yetone/magpie&Date"><img src="https://api.star-history.com/svg?repos=yetone/magpie&type=Date" width="260" alt="yetone/magpie 的星标历史曲线"></a> |
| 7 | [affaan-m/ECC](https://github.com/affaan-m/ECC)<br>给编程 AI 加记忆、技能和安全检查<br>`人工智能` | +6,249 | 892.7 | 295,627 | <a href="https://www.star-history.com/#affaan-m/ECC&Date"><img src="https://api.star-history.com/svg?repos=affaan-m/ECC&type=Date" width="260" alt="affaan-m/ECC 的星标历史曲线"></a> |
| 8 | [DietrichGebert/ponytail](https://github.com/DietrichGebert/ponytail)<br>让 AI 少写废代码，该写的写对<br>`人工智能` | +6,192 | 884.6 | 182,863 | <a href="https://www.star-history.com/#DietrichGebert/ponytail&Date"><img src="https://api.star-history.com/svg?repos=DietrichGebert/ponytail&type=Date" width="260" alt="DietrichGebert/ponytail 的星标历史曲线"></a> |
| 9 | [Leonxlnx/taste-skill](https://github.com/Leonxlnx/taste-skill)<br>别再让 AI 做出千篇一律的页面<br>`人工智能` | +5,591 | 798.7 | 108,684 | <a href="https://www.star-history.com/#Leonxlnx/taste-skill&Date"><img src="https://api.star-history.com/svg?repos=Leonxlnx/taste-skill&type=Date" width="260" alt="Leonxlnx/taste-skill 的星标历史曲线"></a> |
| 10 | [Graphify-Labs/graphify](https://github.com/Graphify-Labs/graphify)<br>大项目看不过来，先看这张地图<br>`人工智能` | +5,381 | 768.7 | 141,159 | <a href="https://www.star-history.com/#Graphify-Labs/graphify&Date"><img src="https://api.star-history.com/svg?repos=Graphify-Labs/graphify&type=Date" width="260" alt="Graphify-Labs/graphify 的星标历史曲线"></a> |

### 本月增长最快（近 30 天）

| # | 项目 | 新增星标 | 星标/天 | 总星标 | 星标历史 |
|---|---|---:|---:|---:|---|
| 1 | [morluto/rea](https://github.com/morluto/rea)<br>让 AI 帮你克隆任何软件<br>`人工智能` | +419,602 | 13,986.7 | 422,740 | <a href="https://www.star-history.com/#morluto/rea&Date"><img src="https://api.star-history.com/svg?repos=morluto/rea&type=Date" width="260" alt="morluto/rea 的星标历史曲线"></a> |
| 2 | [cloudflare/security-audit-skill](https://github.com/cloudflare/security-audit-skill)<br>AI 查代码漏洞，另一个 AI 逐条复核<br>`人工智能` | +33,053 | 1,101.8 | 57,354 | <a href="https://www.star-history.com/#cloudflare/security-audit-skill&Date"><img src="https://api.star-history.com/svg?repos=cloudflare/security-audit-skill&type=Date" width="260" alt="cloudflare/security-audit-skill 的星标历史曲线"></a> |
| 3 | [DietrichGebert/ponytail](https://github.com/DietrichGebert/ponytail)<br>让 AI 少写废代码，该写的写对<br>`人工智能` | +31,390 | 1,046.3 | 182,863 | <a href="https://www.star-history.com/#DietrichGebert/ponytail&Date"><img src="https://api.star-history.com/svg?repos=DietrichGebert/ponytail&type=Date" width="260" alt="DietrichGebert/ponytail 的星标历史曲线"></a> |
| 4 | [stablyai/orca](https://github.com/stablyai/orca)<br>几个 AI 一起写，谁好用一眼看出<br>`人工智能` | +29,569 | 985.6 | 113,572 | <a href="https://www.star-history.com/#stablyai/orca&Date"><img src="https://api.star-history.com/svg?repos=stablyai/orca&type=Date" width="260" alt="stablyai/orca 的星标历史曲线"></a> |
| 5 | [deepseek-ai/deepseek-harness](https://github.com/deepseek-ai/deepseek-harness)<br>想要什么智能体，用插件自己拼<br>`人工智能` | +27,731 | 924.4 | 269,552 | <a href="https://www.star-history.com/#deepseek-ai/deepseek-harness&Date"><img src="https://api.star-history.com/svg?repos=deepseek-ai/deepseek-harness&type=Date" width="260" alt="deepseek-ai/deepseek-harness 的星标历史曲线"></a> |
| 6 | [affaan-m/ECC](https://github.com/affaan-m/ECC)<br>给编程 AI 加记忆、技能和安全检查<br>`人工智能` | +25,054 | 835.1 | 295,627 | <a href="https://www.star-history.com/#affaan-m/ECC&Date"><img src="https://api.star-history.com/svg?repos=affaan-m/ECC&type=Date" width="260" alt="affaan-m/ECC 的星标历史曲线"></a> |
| 7 | [yetone/magpie](https://github.com/yetone/magpie)<br>编程 AI 换模型，额度用完自动续<br>`人工智能` | +23,768 | 792.3 | 28,379 | <a href="https://www.star-history.com/#yetone/magpie&Date"><img src="https://api.star-history.com/svg?repos=yetone/magpie&type=Date" width="260" alt="yetone/magpie 的星标历史曲线"></a> |
| 8 | [heygen-com/hyperframes](https://github.com/heygen-com/hyperframes)<br>不会剪辑，写网页一样就能出片<br>`人工智能` | +21,653 | 721.8 | 77,709 | <a href="https://www.star-history.com/#heygen-com/hyperframes&Date"><img src="https://api.star-history.com/svg?repos=heygen-com/hyperframes&type=Date" width="260" alt="heygen-com/hyperframes 的星标历史曲线"></a> |
| 9 | [Panniantong/Agent-Reach](https://github.com/Panniantong/Agent-Reach)<br>推特油管小红书，AI 都能帮你搜<br>`人工智能` | +19,273 | 642.4 | 108,066 | <a href="https://www.star-history.com/#Panniantong/Agent-Reach&Date"><img src="https://api.star-history.com/svg?repos=Panniantong/Agent-Reach&type=Date" width="260" alt="Panniantong/Agent-Reach 的星标历史曲线"></a> |
| 10 | [Graphify-Labs/graphify](https://github.com/Graphify-Labs/graphify)<br>大项目看不过来，先看这张地图<br>`人工智能` | +18,134 | 604.5 | 141,159 | <a href="https://www.star-history.com/#Graphify-Labs/graphify&Date"><img src="https://api.star-history.com/svg?repos=Graphify-Labs/graphify&type=Date" width="260" alt="Graphify-Labs/graphify 的星标历史曲线"></a> |

### 今年增长最快（近 365 天）

| # | 项目 | 新增星标 | 星标/天 | 总星标 | 星标历史 |
|---|---|---:|---:|---:|---|
| 1 | [deepseek-ai/deepseek-harness](https://github.com/deepseek-ai/deepseek-harness)<br>想要什么智能体，用插件自己拼<br>`人工智能` | +268,781 | 3,318.3 †<br><sub>÷81 天</sub> | 269,552 | <a href="https://www.star-history.com/#deepseek-ai/deepseek-harness&Date"><img src="https://api.star-history.com/svg?repos=deepseek-ai/deepseek-harness&type=Date" width="260" alt="deepseek-ai/deepseek-harness 的星标历史曲线"></a> |
| 2 | [morluto/rea](https://github.com/morluto/rea)<br>让 AI 帮你克隆任何软件<br>`人工智能` | +420,016 | 2,079.3 †<br><sub>÷202 天</sub> | 422,740 | <a href="https://www.star-history.com/#morluto/rea&Date"><img src="https://api.star-history.com/svg?repos=morluto/rea&type=Date" width="260" alt="morluto/rea 的星标历史曲线"></a> |
| 3 | [DietrichGebert/ponytail](https://github.com/DietrichGebert/ponytail)<br>让 AI 少写废代码，该写的写对<br>`人工智能` | +182,348 | 1,275.2 †<br><sub>÷143 天</sub> | 182,863 | <a href="https://www.star-history.com/#DietrichGebert/ponytail&Date"><img src="https://api.star-history.com/svg?repos=DietrichGebert/ponytail&type=Date" width="260" alt="DietrichGebert/ponytail 的星标历史曲线"></a> |
| 4 | [openclaw/openclaw](https://github.com/openclaw/openclaw)<br>能把事做完的 AI 助手，跑在自己设备上<br>`人工智能` | +393,647 | 1,147.7 †<br><sub>÷343 天</sub> | 393,753 | <a href="https://www.star-history.com/#openclaw/openclaw&Date"><img src="https://api.star-history.com/svg?repos=openclaw/openclaw&type=Date" width="260" alt="openclaw/openclaw 的星标历史曲线"></a> |
| 5 | [affaan-m/ECC](https://github.com/affaan-m/ECC)<br>给编程 AI 加记忆、技能和安全检查<br>`人工智能` | +294,971 | 1,024.2 †<br><sub>÷288 天</sub> | 295,627 | <a href="https://www.star-history.com/#affaan-m/ECC&Date"><img src="https://api.star-history.com/svg?repos=affaan-m/ECC&type=Date" width="260" alt="affaan-m/ECC 的星标历史曲线"></a> |
| 6 | [NousResearch/hermes-agent](https://github.com/NousResearch/hermes-agent)<br>越用越会干活的 AI 助手<br>`人工智能` | +259,591 | 711.2 | 259,851 | <a href="https://www.star-history.com/#NousResearch/hermes-agent&Date"><img src="https://api.star-history.com/svg?repos=NousResearch/hermes-agent&type=Date" width="260" alt="NousResearch/hermes-agent 的星标历史曲线"></a> |
| 7 | [yetone/magpie](https://github.com/yetone/magpie)<br>编程 AI 换模型，额度用完自动续<br>`人工智能` | +28,009 | 700.2 †<br><sub>÷40 天</sub> | 28,379 | <a href="https://www.star-history.com/#yetone/magpie&Date"><img src="https://api.star-history.com/svg?repos=yetone/magpie&type=Date" width="260" alt="yetone/magpie 的星标历史曲线"></a> |
| 8 | [Graphify-Labs/graphify](https://github.com/Graphify-Labs/graphify)<br>大项目看不过来，先看这张地图<br>`人工智能` | +140,701 | 660.6 †<br><sub>÷213 天</sub> | 141,159 | <a href="https://www.star-history.com/#Graphify-Labs/graphify&Date"><img src="https://api.star-history.com/svg?repos=Graphify-Labs/graphify&type=Date" width="260" alt="Graphify-Labs/graphify 的星标历史曲线"></a> |
| 9 | [anomalyco/opencode](https://github.com/anomalyco/opencode)<br>终端里，有个开源 AI 帮你写代码<br>`人工智能` | +195,028 | 534.3 | 224,103 | <a href="https://www.star-history.com/#anomalyco/opencode&Date"><img src="https://api.star-history.com/svg?repos=anomalyco/opencode&type=Date" width="260" alt="anomalyco/opencode 的星标历史曲线"></a> |
| 10 | [stablyai/orca](https://github.com/stablyai/orca)<br>几个 AI 一起写，谁好用一眼看出<br>`人工智能` | +112,912 | 490.9 †<br><sub>÷230 天</sub> | 113,572 | <a href="https://www.star-history.com/#stablyai/orca&Date"><img src="https://api.star-history.com/svg?repos=stablyai/orca&type=Date" width="260" alt="stablyai/orca 的星标历史曲线"></a> |

† 该仓库创建时间短于统计窗口，因此“星标/天”按仓库存在的天数（显示在数字下方）计算，而不是按完整窗口。

### 总星标数（历史累计）

| # | 项目 | 总星标 | 星标历史 |
|---|---|---:|---|
| 1 | [morluto/rea](https://github.com/morluto/rea)<br>让 AI 帮你克隆任何软件<br>`人工智能` | 422,740 | <a href="https://www.star-history.com/#morluto/rea&Date"><img src="https://api.star-history.com/svg?repos=morluto/rea&type=Date" width="260" alt="morluto/rea 的星标历史曲线"></a> |
| 2 | [openclaw/openclaw](https://github.com/openclaw/openclaw)<br>能把事做完的 AI 助手，跑在自己设备上<br>`人工智能` | 393,753 | <a href="https://www.star-history.com/#openclaw/openclaw&Date"><img src="https://api.star-history.com/svg?repos=openclaw/openclaw&type=Date" width="260" alt="openclaw/openclaw 的星标历史曲线"></a> |
| 3 | [affaan-m/ECC](https://github.com/affaan-m/ECC)<br>给编程 AI 加记忆、技能和安全检查<br>`人工智能` | 295,627 | <a href="https://www.star-history.com/#affaan-m/ECC&Date"><img src="https://api.star-history.com/svg?repos=affaan-m/ECC&type=Date" width="260" alt="affaan-m/ECC 的星标历史曲线"></a> |
| 4 | [deepseek-ai/deepseek-harness](https://github.com/deepseek-ai/deepseek-harness)<br>想要什么智能体，用插件自己拼<br>`人工智能` | 269,552 | <a href="https://www.star-history.com/#deepseek-ai/deepseek-harness&Date"><img src="https://api.star-history.com/svg?repos=deepseek-ai/deepseek-harness&type=Date" width="260" alt="deepseek-ai/deepseek-harness 的星标历史曲线"></a> |
| 5 | [NousResearch/hermes-agent](https://github.com/NousResearch/hermes-agent)<br>越用越会干活的 AI 助手<br>`人工智能` | 259,851 | <a href="https://www.star-history.com/#NousResearch/hermes-agent&Date"><img src="https://api.star-history.com/svg?repos=NousResearch/hermes-agent&type=Date" width="260" alt="NousResearch/hermes-agent 的星标历史曲线"></a> |
| 6 | [anomalyco/opencode](https://github.com/anomalyco/opencode)<br>终端里，有个开源 AI 帮你写代码<br>`人工智能` | 224,103 | <a href="https://www.star-history.com/#anomalyco/opencode&Date"><img src="https://api.star-history.com/svg?repos=anomalyco/opencode&type=Date" width="260" alt="anomalyco/opencode 的星标历史曲线"></a> |
| 7 | [anthropics/skills](https://github.com/anthropics/skills)<br>Claude 技能怎么写，照着官方学<br>`人工智能` | 186,760 | <a href="https://www.star-history.com/#anthropics/skills&Date"><img src="https://api.star-history.com/svg?repos=anthropics/skills&type=Date" width="260" alt="anthropics/skills 的星标历史曲线"></a> |
| 8 | [DietrichGebert/ponytail](https://github.com/DietrichGebert/ponytail)<br>让 AI 少写废代码，该写的写对<br>`人工智能` | 182,863 | <a href="https://www.star-history.com/#DietrichGebert/ponytail&Date"><img src="https://api.star-history.com/svg?repos=DietrichGebert/ponytail&type=Date" width="260" alt="DietrichGebert/ponytail 的星标历史曲线"></a> |
| 9 | [farion1231/cc-switch](https://github.com/farion1231/cc-switch)<br>换接口不用改配置，一键切<br>`人工智能` | 151,211 | <a href="https://www.star-history.com/#farion1231/cc-switch&Date"><img src="https://api.star-history.com/svg?repos=farion1231/cc-switch&type=Date" width="260" alt="farion1231/cc-switch 的星标历史曲线"></a> |
| 10 | [nextlevelbuilder/ui-ux-pro-max-skill](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill)<br>AI 做的界面，看着像专业设计<br>`人工智能` | 144,268 | <a href="https://www.star-history.com/#nextlevelbuilder/ui-ux-pro-max-skill&Date"><img src="https://api.star-history.com/svg?repos=nextlevelbuilder/ui-ux-pro-max-skill&type=Date" width="260" alt="nextlevelbuilder/ui-ux-pro-max-skill 的星标历史曲线"></a> |

## 开发者工具

> 命令行、编辑器、包管理、代码检查与构建工具

### 最热新仓库（近 7 天内创建）

| # | 项目 | 创建时间（UTC） | 总星标 | 星标/天 | 星标历史 |
|---|---|---|---:|---:|---|
| 1 | [Verlintas/NOIR](https://github.com/Verlintas/NOIR)<br>扫出安卓应用隐私泄露，并支持安全回滚 | 2026-10-31<br><sub>2.1 天</sub> | 1,265 | 610.5 | <a href="https://www.star-history.com/#Verlintas/NOIR&Date"><img src="https://api.star-history.com/svg?repos=Verlintas/NOIR&type=Date" width="260" alt="Verlintas/NOIR 的星标历史曲线"></a> |
| 2 | [AssassinCreator/steam-stash-value-report-card](https://github.com/AssassinCreator/steam-stash-value-report-card)<br>不知库存价值，在终端盘点并生成分享卡 | 2026-11-02<br><sub>1.0 天</sub> | 590 | 590.0 | <a href="https://www.star-history.com/#AssassinCreator/steam-stash-value-report-card&Date"><img src="https://api.star-history.com/svg?repos=AssassinCreator/steam-stash-value-report-card&type=Date" width="260" alt="AssassinCreator/steam-stash-value-report-card 的星标历史曲线"></a> |
| 3 | [Straitbrashadow/minecraft-ai-mod-builder](https://github.com/Straitbrashadow/minecraft-ai-mod-builder)<br>输入建筑想法，在游戏中一键放置或撤销 | 2026-10-30<br><sub>3.1 天</sub> | 200 | 64.8 | <a href="https://www.star-history.com/#Straitbrashadow/minecraft-ai-mod-builder&Date"><img src="https://api.star-history.com/svg?repos=Straitbrashadow/minecraft-ai-mod-builder&type=Date" width="260" alt="Straitbrashadow/minecraft-ai-mod-builder 的星标历史曲线"></a> |
| 4 | [DiplomatHearth/roblox-ai-place-diff](https://github.com/DiplomatHearth/roblox-ai-place-diff)<br>怕改坏场景，智能体修改先由你确认 | 2026-10-30<br><sub>3.1 天</sub> | 160 | 52.2 | <a href="https://www.star-history.com/#DiplomatHearth/roblox-ai-place-diff&Date"><img src="https://api.star-history.com/svg?repos=DiplomatHearth/roblox-ai-place-diff&type=Date" width="260" alt="DiplomatHearth/roblox-ai-place-diff 的星标历史曲线"></a> |
| 5 | [Xpropel/Pi-Remote](https://github.com/Xpropel/Pi-Remote)<br>在任意浏览器中远程控制 pi 智能体 | 2026-10-28<br><sub>5.5 天</sub> | 261 | 47.3 | <a href="https://www.star-history.com/#Xpropel/Pi-Remote&Date"><img src="https://api.star-history.com/svg?repos=Xpropel/Pi-Remote&type=Date" width="260" alt="Xpropel/Pi-Remote 的星标历史曲线"></a> |
| 6 | [muaaz9329/cheap-ag](https://github.com/muaaz9329/cheap-ag)<br>使用 cheap-ag 将你的使用量提升 50 倍。Opus/Astra 计划，极便宜的模型编写每一行代码，测试决定交付内容。你的 $20 计划不再触碰限制。一个 MCP… | 2026-10-28<br><sub>5.0 天</sub> | 227 | 45.1 | <a href="https://www.star-history.com/#muaaz9329/cheap-ag&Date"><img src="https://api.star-history.com/svg?repos=muaaz9329/cheap-ag&type=Date" width="260" alt="muaaz9329/cheap-ag 的星标历史曲线"></a> |
| 7 | [tianfuzhibuyuci/readme-visual-kit](https://github.com/tianfuzhibuyuci/readme-visual-kit)<br>本地将项目说明生成三张 README 架构图 | 2026-10-27<br><sub>6.4 天</sub> | 208 | 32.4 | <a href="https://www.star-history.com/#tianfuzhibuyuci/readme-visual-kit&Date"><img src="https://api.star-history.com/svg?repos=tianfuzhibuyuci/readme-visual-kit&type=Date" width="260" alt="tianfuzhibuyuci/readme-visual-kit 的星标历史曲线"></a> |
| 8 | [khanh020905/my-office](https://github.com/khanh020905/my-office)<br>为 Claude Code 打造 3D 办公空间 | 2026-10-28<br><sub>5.5 天</sub> | 154 | 28.3 | <a href="https://www.star-history.com/#khanh020905/my-office&Date"><img src="https://api.star-history.com/svg?repos=khanh020905/my-office&type=Date" width="260" alt="khanh020905/my-office 的星标历史曲线"></a> |
| 9 | [kyy-logs/code-review-skill](https://github.com/kyy-logs/code-review-skill)<br>代码审查有据可依，合并更有把握 | 2026-10-29<br><sub>4.6 天</sub> | 119 | 25.6 | <a href="https://www.star-history.com/#kyy-logs/code-review-skill&Date"><img src="https://api.star-history.com/svg?repos=kyy-logs/code-review-skill&type=Date" width="260" alt="kyy-logs/code-review-skill 的星标历史曲线"></a> |
| 10 | [dufu1991/foldgit](https://github.com/dufu1991/foldgit)<br>单窗口搞定仓库管理、差异比对与提交 | 2026-10-28<br><sub>5.8 天</sub> | 128 | 21.9 | <a href="https://www.star-history.com/#dufu1991/foldgit&Date"><img src="https://api.star-history.com/svg?repos=dufu1991/foldgit&type=Date" width="260" alt="dufu1991/foldgit 的星标历史曲线"></a> |

### 本周增长最快（近 7 天）

| # | 项目 | 新增星标 | 星标/天 | 总星标 | 星标历史 |
|---|---|---:|---:|---:|---|
| 1 | [zed-industries/zed](https://github.com/zed-industries/zed)<br>打开就快，还能多人一起写代码<br>`开发者工具` | +396 | 56.6 | 92,573 | <a href="https://www.star-history.com/#zed-industries/zed&Date"><img src="https://api.star-history.com/svg?repos=zed-industries/zed&type=Date" width="260" alt="zed-industries/zed 的星标历史曲线"></a> |
| 2 | [astral-sh/uv](https://github.com/astral-sh/uv)<br>装 Python 包，不用再干等<br>`开发者工具` | +315 | 45.0 | 91,480 | <a href="https://www.star-history.com/#astral-sh/uv&Date"><img src="https://api.star-history.com/svg?repos=astral-sh/uv&type=Date" width="260" alt="astral-sh/uv 的星标历史曲线"></a> |
| 3 | [jdx/mise](https://github.com/jdx/mise)<br>开发工具、环境变量、任务，一个工具管<br>`开发者工具` | +284 | 40.6 | 35,689 | <a href="https://www.star-history.com/#jdx/mise&Date"><img src="https://api.star-history.com/svg?repos=jdx/mise&type=Date" width="260" alt="jdx/mise 的星标历史曲线"></a> |
| 4 | [BurntSushi/ripgrep](https://github.com/BurntSushi/ripgrep)<br>翻遍整个目录找文字，比 grep 快<br>`开发者工具` | +227 | 32.4 | 69,660 | <a href="https://www.star-history.com/#BurntSushi/ripgrep&Date"><img src="https://api.star-history.com/svg?repos=BurntSushi/ripgrep&type=Date" width="260" alt="BurntSushi/ripgrep 的星标历史曲线"></a> |
| 5 | [oven-sh/bun](https://github.com/oven-sh/bun)<br>运行打包测试装包，一个工具全包<br>`开发者工具` | +138 | 19.7 | 96,519 | <a href="https://www.star-history.com/#oven-sh/bun&Date"><img src="https://api.star-history.com/svg?repos=oven-sh/bun&type=Date" width="260" alt="oven-sh/bun 的星标历史曲线"></a> |
| 6 | [cli/cli](https://github.com/cli/cli)<br>不开网页，命令行里处理 GitHub<br>`开发者工具` | +110 | 15.7 | 46,845 | <a href="https://www.star-history.com/#cli/cli&Date"><img src="https://api.star-history.com/svg?repos=cli/cli&type=Date" width="260" alt="cli/cli 的星标历史曲线"></a> |
| 7 | [helix-editor/helix](https://github.com/helix-editor/helix)<br>语法高亮、语言服务都内置的文本编辑器<br>`开发者工具` | +101 | 14.4 | 46,774 | <a href="https://www.star-history.com/#helix-editor/helix&Date"><img src="https://api.star-history.com/svg?repos=helix-editor/helix&type=Date" width="260" alt="helix-editor/helix 的星标历史曲线"></a> |
| 8 | [biomejs/biome](https://github.com/biomejs/biome)<br>网页代码格式和检查，一个工具搞定<br>`开发者工具` | +51 | 7.3 | 26,041 | <a href="https://www.star-history.com/#biomejs/biome&Date"><img src="https://api.star-history.com/svg?repos=biomejs/biome&type=Date" width="260" alt="biomejs/biome 的星标历史曲线"></a> |

### 本月增长最快（近 30 天）

| # | 项目 | 新增星标 | 星标/天 | 总星标 | 星标历史 |
|---|---|---:|---:|---:|---|
| 1 | [zed-industries/zed](https://github.com/zed-industries/zed)<br>打开就快，还能多人一起写代码<br>`开发者工具` | +1,588 | 52.9 | 92,573 | <a href="https://www.star-history.com/#zed-industries/zed&Date"><img src="https://api.star-history.com/svg?repos=zed-industries/zed&type=Date" width="260" alt="zed-industries/zed 的星标历史曲线"></a> |
| 2 | [astral-sh/uv](https://github.com/astral-sh/uv)<br>装 Python 包，不用再干等<br>`开发者工具` | +1,265 | 42.2 | 91,480 | <a href="https://www.star-history.com/#astral-sh/uv&Date"><img src="https://api.star-history.com/svg?repos=astral-sh/uv&type=Date" width="260" alt="astral-sh/uv 的星标历史曲线"></a> |
| 3 | [jdx/mise](https://github.com/jdx/mise)<br>开发工具、环境变量、任务，一个工具管<br>`开发者工具` | +1,193 | 39.8 | 35,689 | <a href="https://www.star-history.com/#jdx/mise&Date"><img src="https://api.star-history.com/svg?repos=jdx/mise&type=Date" width="260" alt="jdx/mise 的星标历史曲线"></a> |
| 4 | [BurntSushi/ripgrep](https://github.com/BurntSushi/ripgrep)<br>翻遍整个目录找文字，比 grep 快<br>`开发者工具` | +989 | 33.0 | 69,660 | <a href="https://www.star-history.com/#BurntSushi/ripgrep&Date"><img src="https://api.star-history.com/svg?repos=BurntSushi/ripgrep&type=Date" width="260" alt="BurntSushi/ripgrep 的星标历史曲线"></a> |
| 5 | [oven-sh/bun](https://github.com/oven-sh/bun)<br>运行打包测试装包，一个工具全包<br>`开发者工具` | +684 | 22.8 | 96,519 | <a href="https://www.star-history.com/#oven-sh/bun&Date"><img src="https://api.star-history.com/svg?repos=oven-sh/bun&type=Date" width="260" alt="oven-sh/bun 的星标历史曲线"></a> |
| 6 | [helix-editor/helix](https://github.com/helix-editor/helix)<br>语法高亮、语言服务都内置的文本编辑器<br>`开发者工具` | +451 | 15.0 | 46,774 | <a href="https://www.star-history.com/#helix-editor/helix&Date"><img src="https://api.star-history.com/svg?repos=helix-editor/helix&type=Date" width="260" alt="helix-editor/helix 的星标历史曲线"></a> |
| 7 | [cli/cli](https://github.com/cli/cli)<br>不开网页，命令行里处理 GitHub<br>`开发者工具` | +422 | 14.1 | 46,845 | <a href="https://www.star-history.com/#cli/cli&Date"><img src="https://api.star-history.com/svg?repos=cli/cli&type=Date" width="260" alt="cli/cli 的星标历史曲线"></a> |
| 8 | [biomejs/biome](https://github.com/biomejs/biome)<br>网页代码格式和检查，一个工具搞定<br>`开发者工具` | +213 | 7.1 | 26,041 | <a href="https://www.star-history.com/#biomejs/biome&Date"><img src="https://api.star-history.com/svg?repos=biomejs/biome&type=Date" width="260" alt="biomejs/biome 的星标历史曲线"></a> |

### 今年增长最快（近 365 天）

| # | 项目 | 新增星标 | 星标/天 | 总星标 | 星标历史 |
|---|---|---:|---:|---:|---|
| 1 | [zed-industries/zed](https://github.com/zed-industries/zed)<br>打开就快，还能多人一起写代码<br>`开发者工具` | +25,673 | 70.3 | 92,573 | <a href="https://www.star-history.com/#zed-industries/zed&Date"><img src="https://api.star-history.com/svg?repos=zed-industries/zed&type=Date" width="260" alt="zed-industries/zed 的星标历史曲线"></a> |
| 2 | [astral-sh/uv](https://github.com/astral-sh/uv)<br>装 Python 包，不用再干等<br>`开发者工具` | +21,302 | 58.4 | 91,480 | <a href="https://www.star-history.com/#astral-sh/uv&Date"><img src="https://api.star-history.com/svg?repos=astral-sh/uv&type=Date" width="260" alt="astral-sh/uv 的星标历史曲线"></a> |
| 3 | [oven-sh/bun](https://github.com/oven-sh/bun)<br>运行打包测试装包，一个工具全包<br>`开发者工具` | +16,560 | 45.4 | 96,519 | <a href="https://www.star-history.com/#oven-sh/bun&Date"><img src="https://api.star-history.com/svg?repos=oven-sh/bun&type=Date" width="260" alt="oven-sh/bun 的星标历史曲线"></a> |
| 4 | [jdx/mise](https://github.com/jdx/mise)<br>开发工具、环境变量、任务，一个工具管<br>`开发者工具` | +15,052 | 41.2 | 35,689 | <a href="https://www.star-history.com/#jdx/mise&Date"><img src="https://api.star-history.com/svg?repos=jdx/mise&type=Date" width="260" alt="jdx/mise 的星标历史曲线"></a> |
| 5 | [BurntSushi/ripgrep](https://github.com/BurntSushi/ripgrep)<br>翻遍整个目录找文字，比 grep 快<br>`开发者工具` | +13,358 | 36.6 | 69,660 | <a href="https://www.star-history.com/#BurntSushi/ripgrep&Date"><img src="https://api.star-history.com/svg?repos=BurntSushi/ripgrep&type=Date" width="260" alt="BurntSushi/ripgrep 的星标历史曲线"></a> |
| 6 | [helix-editor/helix](https://github.com/helix-editor/helix)<br>语法高亮、语言服务都内置的文本编辑器<br>`开发者工具` | +6,766 | 18.5 | 46,774 | <a href="https://www.star-history.com/#helix-editor/helix&Date"><img src="https://api.star-history.com/svg?repos=helix-editor/helix&type=Date" width="260" alt="helix-editor/helix 的星标历史曲线"></a> |
| 7 | [cli/cli](https://github.com/cli/cli)<br>不开网页，命令行里处理 GitHub<br>`开发者工具` | +6,262 | 17.2 | 46,845 | <a href="https://www.star-history.com/#cli/cli&Date"><img src="https://api.star-history.com/svg?repos=cli/cli&type=Date" width="260" alt="cli/cli 的星标历史曲线"></a> |
| 8 | [biomejs/biome](https://github.com/biomejs/biome)<br>网页代码格式和检查，一个工具搞定<br>`开发者工具` | +4,582 | 12.6 | 26,041 | <a href="https://www.star-history.com/#biomejs/biome&Date"><img src="https://api.star-history.com/svg?repos=biomejs/biome&type=Date" width="260" alt="biomejs/biome 的星标历史曲线"></a> |

### 总星标数（历史累计）

| # | 项目 | 总星标 | 星标历史 |
|---|---|---:|---|
| 1 | [oven-sh/bun](https://github.com/oven-sh/bun)<br>运行打包测试装包，一个工具全包<br>`开发者工具` | 96,519 | <a href="https://www.star-history.com/#oven-sh/bun&Date"><img src="https://api.star-history.com/svg?repos=oven-sh/bun&type=Date" width="260" alt="oven-sh/bun 的星标历史曲线"></a> |
| 2 | [zed-industries/zed](https://github.com/zed-industries/zed)<br>打开就快，还能多人一起写代码<br>`开发者工具` | 92,573 | <a href="https://www.star-history.com/#zed-industries/zed&Date"><img src="https://api.star-history.com/svg?repos=zed-industries/zed&type=Date" width="260" alt="zed-industries/zed 的星标历史曲线"></a> |
| 3 | [astral-sh/uv](https://github.com/astral-sh/uv)<br>装 Python 包，不用再干等<br>`开发者工具` | 91,480 | <a href="https://www.star-history.com/#astral-sh/uv&Date"><img src="https://api.star-history.com/svg?repos=astral-sh/uv&type=Date" width="260" alt="astral-sh/uv 的星标历史曲线"></a> |
| 4 | [BurntSushi/ripgrep](https://github.com/BurntSushi/ripgrep)<br>翻遍整个目录找文字，比 grep 快<br>`开发者工具` | 69,660 | <a href="https://www.star-history.com/#BurntSushi/ripgrep&Date"><img src="https://api.star-history.com/svg?repos=BurntSushi/ripgrep&type=Date" width="260" alt="BurntSushi/ripgrep 的星标历史曲线"></a> |
| 5 | [cli/cli](https://github.com/cli/cli)<br>不开网页，命令行里处理 GitHub<br>`开发者工具` | 46,845 | <a href="https://www.star-history.com/#cli/cli&Date"><img src="https://api.star-history.com/svg?repos=cli/cli&type=Date" width="260" alt="cli/cli 的星标历史曲线"></a> |
| 6 | [helix-editor/helix](https://github.com/helix-editor/helix)<br>语法高亮、语言服务都内置的文本编辑器<br>`开发者工具` | 46,774 | <a href="https://www.star-history.com/#helix-editor/helix&Date"><img src="https://api.star-history.com/svg?repos=helix-editor/helix&type=Date" width="260" alt="helix-editor/helix 的星标历史曲线"></a> |
| 7 | [jdx/mise](https://github.com/jdx/mise)<br>开发工具、环境变量、任务，一个工具管<br>`开发者工具` | 35,689 | <a href="https://www.star-history.com/#jdx/mise&Date"><img src="https://api.star-history.com/svg?repos=jdx/mise&type=Date" width="260" alt="jdx/mise 的星标历史曲线"></a> |
| 8 | [biomejs/biome](https://github.com/biomejs/biome)<br>网页代码格式和检查，一个工具搞定<br>`开发者工具` | 26,041 | <a href="https://www.star-history.com/#biomejs/biome&Date"><img src="https://api.star-history.com/svg?repos=biomejs/biome&type=Date" width="260" alt="biomejs/biome 的星标历史曲线"></a> |

## 安全

> 漏洞扫描、静态分析、供应链与运行时安全

### 最热新仓库（近 7 天内创建）

本次运行中没有符合条件的新仓库。

### 本周增长最快（近 7 天）

| # | 项目 | 新增星标 | 星标/天 | 总星标 | 星标历史 |
|---|---|---:|---:|---:|---|
| 1 | [projectdiscovery/nuclei](https://github.com/projectdiscovery/nuclei)<br>写个模板，就能批量扫漏洞<br>`安全` | +229 | 32.7 | 32,545 | <a href="https://www.star-history.com/#projectdiscovery/nuclei&Date"><img src="https://api.star-history.com/svg?repos=projectdiscovery/nuclei&type=Date" width="260" alt="projectdiscovery/nuclei 的星标历史曲线"></a> |
| 2 | [aquasecurity/trivy](https://github.com/aquasecurity/trivy)<br>容器和代码仓，一次扫完安全问题<br>`安全` | +201 | 28.7 | 38,917 | <a href="https://www.star-history.com/#aquasecurity/trivy&Date"><img src="https://api.star-history.com/svg?repos=aquasecurity/trivy&type=Date" width="260" alt="aquasecurity/trivy 的星标历史曲线"></a> |
| 3 | [semgrep/semgrep](https://github.com/semgrep/semgrep)<br>代码里的问题，提交前先揪出来<br>`安全` | +130 | 18.6 | 17,413 | <a href="https://www.star-history.com/#semgrep/semgrep&Date"><img src="https://api.star-history.com/svg?repos=semgrep/semgrep&type=Date" width="260" alt="semgrep/semgrep 的星标历史曲线"></a> |
| 4 | [OWASP/CheatSheetSeries](https://github.com/OWASP/CheatSheetSeries)<br>应用安全怎么做，看这套速查表<br>`安全` | +107 | 15.3 | 33,852 | <a href="https://www.star-history.com/#OWASP/CheatSheetSeries&Date"><img src="https://api.star-history.com/svg?repos=OWASP/CheatSheetSeries&type=Date" width="260" alt="OWASP/CheatSheetSeries 的星标历史曲线"></a> |
| 5 | [google/osv-scanner](https://github.com/google/osv-scanner)<br>用的依赖安不安全，扫一下就知道<br>`安全` | +83 | 11.9 | 11,368 | <a href="https://www.star-history.com/#google/osv-scanner&Date"><img src="https://api.star-history.com/svg?repos=google/osv-scanner&type=Date" width="260" alt="google/osv-scanner 的星标历史曲线"></a> |
| 6 | [anchore/grype](https://github.com/anchore/grype)<br>容器镜像有没有漏洞，扫一下就知道<br>`安全` | +49 | 7.0 | 13,163 | <a href="https://www.star-history.com/#anchore/grype&Date"><img src="https://api.star-history.com/svg?repos=anchore/grype&type=Date" width="260" alt="anchore/grype 的星标历史曲线"></a> |
| 7 | [falcosecurity/falco](https://github.com/falcosecurity/falco)<br>云上有异常，第一时间知道<br>`安全` | +26 | 3.7 | 9,547 | <a href="https://www.star-history.com/#falcosecurity/falco&Date"><img src="https://api.star-history.com/svg?repos=falcosecurity/falco&type=Date" width="260" alt="falcosecurity/falco 的星标历史曲线"></a> |
| 8 | [securego/gosec](https://github.com/securego/gosec)<br>Go 代码的安全隐患，扫一遍就知道<br>`安全` | +12 | 1.7 | 8,996 | <a href="https://www.star-history.com/#securego/gosec&Date"><img src="https://api.star-history.com/svg?repos=securego/gosec&type=Date" width="260" alt="securego/gosec 的星标历史曲线"></a> |

### 本月增长最快（近 30 天）

| # | 项目 | 新增星标 | 星标/天 | 总星标 | 星标历史 |
|---|---|---:|---:|---:|---|
| 1 | [projectdiscovery/nuclei](https://github.com/projectdiscovery/nuclei)<br>写个模板，就能批量扫漏洞<br>`安全` | +917 | 30.6 | 32,545 | <a href="https://www.star-history.com/#projectdiscovery/nuclei&Date"><img src="https://api.star-history.com/svg?repos=projectdiscovery/nuclei&type=Date" width="260" alt="projectdiscovery/nuclei 的星标历史曲线"></a> |
| 2 | [aquasecurity/trivy](https://github.com/aquasecurity/trivy)<br>容器和代码仓，一次扫完安全问题<br>`安全` | +761 | 25.4 | 38,917 | <a href="https://www.star-history.com/#aquasecurity/trivy&Date"><img src="https://api.star-history.com/svg?repos=aquasecurity/trivy&type=Date" width="260" alt="aquasecurity/trivy 的星标历史曲线"></a> |
| 3 | [semgrep/semgrep](https://github.com/semgrep/semgrep)<br>代码里的问题，提交前先揪出来<br>`安全` | +580 | 19.3 | 17,413 | <a href="https://www.star-history.com/#semgrep/semgrep&Date"><img src="https://api.star-history.com/svg?repos=semgrep/semgrep&type=Date" width="260" alt="semgrep/semgrep 的星标历史曲线"></a> |
| 4 | [OWASP/CheatSheetSeries](https://github.com/OWASP/CheatSheetSeries)<br>应用安全怎么做，看这套速查表<br>`安全` | +479 | 16.0 | 33,852 | <a href="https://www.star-history.com/#OWASP/CheatSheetSeries&Date"><img src="https://api.star-history.com/svg?repos=OWASP/CheatSheetSeries&type=Date" width="260" alt="OWASP/CheatSheetSeries 的星标历史曲线"></a> |
| 5 | [google/osv-scanner](https://github.com/google/osv-scanner)<br>用的依赖安不安全，扫一下就知道<br>`安全` | +240 | 8.0 | 11,368 | <a href="https://www.star-history.com/#google/osv-scanner&Date"><img src="https://api.star-history.com/svg?repos=google/osv-scanner&type=Date" width="260" alt="google/osv-scanner 的星标历史曲线"></a> |
| 6 | [anchore/grype](https://github.com/anchore/grype)<br>容器镜像有没有漏洞，扫一下就知道<br>`安全` | +202 | 6.7 | 13,163 | <a href="https://www.star-history.com/#anchore/grype&Date"><img src="https://api.star-history.com/svg?repos=anchore/grype&type=Date" width="260" alt="anchore/grype 的星标历史曲线"></a> |
| 7 | [falcosecurity/falco](https://github.com/falcosecurity/falco)<br>云上有异常，第一时间知道<br>`安全` | +123 | 4.1 | 9,547 | <a href="https://www.star-history.com/#falcosecurity/falco&Date"><img src="https://api.star-history.com/svg?repos=falcosecurity/falco&type=Date" width="260" alt="falcosecurity/falco 的星标历史曲线"></a> |
| 8 | [securego/gosec](https://github.com/securego/gosec)<br>Go 代码的安全隐患，扫一遍就知道<br>`安全` | +43 | 1.4 | 8,996 | <a href="https://www.star-history.com/#securego/gosec&Date"><img src="https://api.star-history.com/svg?repos=securego/gosec&type=Date" width="260" alt="securego/gosec 的星标历史曲线"></a> |

### 今年增长最快（近 365 天）

| # | 项目 | 新增星标 | 星标/天 | 总星标 | 星标历史 |
|---|---|---:|---:|---:|---|
| 1 | [aquasecurity/trivy](https://github.com/aquasecurity/trivy)<br>容器和代码仓，一次扫完安全问题<br>`安全` | +10,106 | 27.7 | 38,917 | <a href="https://www.star-history.com/#aquasecurity/trivy&Date"><img src="https://api.star-history.com/svg?repos=aquasecurity/trivy&type=Date" width="260" alt="aquasecurity/trivy 的星标历史曲线"></a> |
| 2 | [projectdiscovery/nuclei](https://github.com/projectdiscovery/nuclei)<br>写个模板，就能批量扫漏洞<br>`安全` | +7,603 | 20.8 | 32,545 | <a href="https://www.star-history.com/#projectdiscovery/nuclei&Date"><img src="https://api.star-history.com/svg?repos=projectdiscovery/nuclei&type=Date" width="260" alt="projectdiscovery/nuclei 的星标历史曲线"></a> |
| 3 | [semgrep/semgrep](https://github.com/semgrep/semgrep)<br>代码里的问题，提交前先揪出来<br>`安全` | +4,372 | 12.0 | 17,413 | <a href="https://www.star-history.com/#semgrep/semgrep&Date"><img src="https://api.star-history.com/svg?repos=semgrep/semgrep&type=Date" width="260" alt="semgrep/semgrep 的星标历史曲线"></a> |
| 4 | [OWASP/CheatSheetSeries](https://github.com/OWASP/CheatSheetSeries)<br>应用安全怎么做，看这套速查表<br>`安全` | +3,524 | 9.7 | 33,852 | <a href="https://www.star-history.com/#OWASP/CheatSheetSeries&Date"><img src="https://api.star-history.com/svg?repos=OWASP/CheatSheetSeries&type=Date" width="260" alt="OWASP/CheatSheetSeries 的星标历史曲线"></a> |
| 5 | [google/osv-scanner](https://github.com/google/osv-scanner)<br>用的依赖安不安全，扫一下就知道<br>`安全` | +3,488 | 9.6 | 11,368 | <a href="https://www.star-history.com/#google/osv-scanner&Date"><img src="https://api.star-history.com/svg?repos=google/osv-scanner&type=Date" width="260" alt="google/osv-scanner 的星标历史曲线"></a> |
| 6 | [anchore/grype](https://github.com/anchore/grype)<br>容器镜像有没有漏洞，扫一下就知道<br>`安全` | +2,355 | 6.5 | 13,163 | <a href="https://www.star-history.com/#anchore/grype&Date"><img src="https://api.star-history.com/svg?repos=anchore/grype&type=Date" width="260" alt="anchore/grype 的星标历史曲线"></a> |
| 7 | [falcosecurity/falco](https://github.com/falcosecurity/falco)<br>云上有异常，第一时间知道<br>`安全` | +1,271 | 3.5 | 9,547 | <a href="https://www.star-history.com/#falcosecurity/falco&Date"><img src="https://api.star-history.com/svg?repos=falcosecurity/falco&type=Date" width="260" alt="falcosecurity/falco 的星标历史曲线"></a> |
| 8 | [securego/gosec](https://github.com/securego/gosec)<br>Go 代码的安全隐患，扫一遍就知道<br>`安全` | +561 | 1.5 | 8,996 | <a href="https://www.star-history.com/#securego/gosec&Date"><img src="https://api.star-history.com/svg?repos=securego/gosec&type=Date" width="260" alt="securego/gosec 的星标历史曲线"></a> |

### 总星标数（历史累计）

| # | 项目 | 总星标 | 星标历史 |
|---|---|---:|---|
| 1 | [aquasecurity/trivy](https://github.com/aquasecurity/trivy)<br>容器和代码仓，一次扫完安全问题<br>`安全` | 38,917 | <a href="https://www.star-history.com/#aquasecurity/trivy&Date"><img src="https://api.star-history.com/svg?repos=aquasecurity/trivy&type=Date" width="260" alt="aquasecurity/trivy 的星标历史曲线"></a> |
| 2 | [OWASP/CheatSheetSeries](https://github.com/OWASP/CheatSheetSeries)<br>应用安全怎么做，看这套速查表<br>`安全` | 33,852 | <a href="https://www.star-history.com/#OWASP/CheatSheetSeries&Date"><img src="https://api.star-history.com/svg?repos=OWASP/CheatSheetSeries&type=Date" width="260" alt="OWASP/CheatSheetSeries 的星标历史曲线"></a> |
| 3 | [projectdiscovery/nuclei](https://github.com/projectdiscovery/nuclei)<br>写个模板，就能批量扫漏洞<br>`安全` | 32,545 | <a href="https://www.star-history.com/#projectdiscovery/nuclei&Date"><img src="https://api.star-history.com/svg?repos=projectdiscovery/nuclei&type=Date" width="260" alt="projectdiscovery/nuclei 的星标历史曲线"></a> |
| 4 | [semgrep/semgrep](https://github.com/semgrep/semgrep)<br>代码里的问题，提交前先揪出来<br>`安全` | 17,413 | <a href="https://www.star-history.com/#semgrep/semgrep&Date"><img src="https://api.star-history.com/svg?repos=semgrep/semgrep&type=Date" width="260" alt="semgrep/semgrep 的星标历史曲线"></a> |
| 5 | [anchore/grype](https://github.com/anchore/grype)<br>容器镜像有没有漏洞，扫一下就知道<br>`安全` | 13,163 | <a href="https://www.star-history.com/#anchore/grype&Date"><img src="https://api.star-history.com/svg?repos=anchore/grype&type=Date" width="260" alt="anchore/grype 的星标历史曲线"></a> |
| 6 | [google/osv-scanner](https://github.com/google/osv-scanner)<br>用的依赖安不安全，扫一下就知道<br>`安全` | 11,368 | <a href="https://www.star-history.com/#google/osv-scanner&Date"><img src="https://api.star-history.com/svg?repos=google/osv-scanner&type=Date" width="260" alt="google/osv-scanner 的星标历史曲线"></a> |
| 7 | [falcosecurity/falco](https://github.com/falcosecurity/falco)<br>云上有异常，第一时间知道<br>`安全` | 9,547 | <a href="https://www.star-history.com/#falcosecurity/falco&Date"><img src="https://api.star-history.com/svg?repos=falcosecurity/falco&type=Date" width="260" alt="falcosecurity/falco 的星标历史曲线"></a> |
| 8 | [securego/gosec](https://github.com/securego/gosec)<br>Go 代码的安全隐患，扫一遍就知道<br>`安全` | 8,996 | <a href="https://www.star-history.com/#securego/gosec&Date"><img src="https://api.star-history.com/svg?repos=securego/gosec&type=Date" width="260" alt="securego/gosec 的星标历史曲线"></a> |

## Web / 前端

> 前端框架、UI 组件库、CSS 与浏览器工具

### 最热新仓库（近 7 天内创建）

| # | 项目 | 创建时间（UTC） | 总星标 | 星标/天 | 星标历史 |
|---|---|---|---:|---:|---|
| 1 | [shipwords-dev/shipwords](https://github.com/shipwords-dev/shipwords)<br>追到新词，一下午上线一个 AI 站 | 2026-10-28<br><sub>5.7 天</sub> | 346 | 60.7 | <a href="https://www.star-history.com/#shipwords-dev/shipwords&Date"><img src="https://api.star-history.com/svg?repos=shipwords-dev/shipwords&type=Date" width="260" alt="shipwords-dev/shipwords 的星标历史曲线"></a> |
| 2 | [mofan6/Moect](https://github.com/mofan6/Moect)<br>微信聊天记录想留存，离线导出与备份 | 2026-10-31<br><sub>2.5 天</sub> | 144 | 57.1 | <a href="https://www.star-history.com/#mofan6/Moect&Date"><img src="https://api.star-history.com/svg?repos=mofan6/Moect&type=Date" width="260" alt="mofan6/Moect 的星标历史曲线"></a> |
| 3 | [Lavagroabide/aegis-spreadwatch](https://github.com/Lavagroabide/aegis-spreadwatch)<br>CS2 买卖看不清，在设备上直接看净利润 | 2026-10-30<br><sub>3.0 天</sub> | 156 | 52.2 | <a href="https://www.star-history.com/#Lavagroabide/aegis-spreadwatch&Date"><img src="https://api.star-history.com/svg?repos=Lavagroabide/aegis-spreadwatch&type=Date" width="260" alt="Lavagroabide/aegis-spreadwatch 的星标历史曲线"></a> |
| 4 | [solderdatabraid29/aegis-vaultgrid](https://github.com/solderdatabraid29/aegis-vaultgrid)<br>不想登录看库存？在本地规划 CS2 订单 | 2026-10-30<br><sub>3.0 天</sub> | 139 | 46.5 | <a href="https://www.star-history.com/#solderdatabraid29/aegis-vaultgrid&Date"><img src="https://api.star-history.com/svg?repos=solderdatabraid29/aegis-vaultgrid&type=Date" width="260" alt="solderdatabraid29/aegis-vaultgrid 的星标历史曲线"></a> |
| 5 | [Townlanurture/aegis-skin-terminal](https://github.com/Townlanurture/aegis-skin-terminal)<br>CS2 交易怕算漏手续费，本地直接扫差价 | 2026-10-30<br><sub>3.0 天</sub> | 136 | 45.4 | <a href="https://www.star-history.com/#Townlanurture/aegis-skin-terminal&Date"><img src="https://api.star-history.com/svg?repos=Townlanurture/aegis-skin-terminal&type=Date" width="260" alt="Townlanurture/aegis-skin-terminal 的星标历史曲线"></a> |
| 6 | [zklmiao/prompt-vault](https://github.com/zklmiao/prompt-vault)<br>提示词到处乱放？在桌面本地统一收藏 | 2026-10-28<br><sub>5.8 天</sub> | 241 | 41.6 | <a href="https://www.star-history.com/#zklmiao/prompt-vault&Date"><img src="https://api.star-history.com/svg?repos=zklmiao/prompt-vault&type=Date" width="260" alt="zklmiao/prompt-vault 的星标历史曲线"></a> |
| 7 | [jianxinss/iching-64-motion](https://github.com/jianxinss/iching-64-motion)<br>六十四卦做成动画，全靠代码 | 2026-10-27<br><sub>6.9 天</sub> | 164 | 23.8 | <a href="https://www.star-history.com/#jianxinss/iching-64-motion&Date"><img src="https://api.star-history.com/svg?repos=jianxinss/iching-64-motion&type=Date" width="260" alt="jianxinss/iching-64-motion 的星标历史曲线"></a> |
| 8 | [floatboatai/OpenMinutes](https://github.com/floatboatai/OpenMinutes)<br>录音笔的录音，转成能搜的文字 | 2026-10-28<br><sub>5.4 天</sub> | 108 | 19.9 | <a href="https://www.star-history.com/#floatboatai/OpenMinutes&Date"><img src="https://api.star-history.com/svg?repos=floatboatai/OpenMinutes&type=Date" width="260" alt="floatboatai/OpenMinutes 的星标历史曲线"></a> |
| 9 | [fush520/fush-vue-mcp](https://github.com/fush520/fush-vue-mcp)<br>Fush Vue MCP —— Vue 前端逆向 + Web 安全测试工具（Chrome 扩展 + MCP 服务端，91 个工具） | 2026-10-27<br><sub>6.3 天</sub> | 104 | 16.5 | <a href="https://www.star-history.com/#fush520/fush-vue-mcp&Date"><img src="https://api.star-history.com/svg?repos=fush520/fush-vue-mcp&type=Date" width="260" alt="fush520/fush-vue-mcp 的星标历史曲线"></a> |

### 本周增长最快（近 7 天）

| # | 项目 | 新增星标 | 星标/天 | 总星标 | 星标历史 |
|---|---|---:|---:|---:|---|
| 1 | [shadcn-ui/ui](https://github.com/shadcn-ui/ui)<br>好看的组件，代码归你，随便改<br>`Web / 前端` | +668 | 95.4 | 127,202 | <a href="https://www.star-history.com/#shadcn-ui/ui&Date"><img src="https://api.star-history.com/svg?repos=shadcn-ui/ui&type=Date" width="260" alt="shadcn-ui/ui 的星标历史曲线"></a> |
| 2 | [facebook/react](https://github.com/facebook/react)<br>网页和 App 界面，都能用它来搭<br>`Web / 前端` | +346 | 49.4 | 251,874 | <a href="https://www.star-history.com/#facebook/react&Date"><img src="https://api.star-history.com/svg?repos=facebook/react&type=Date" width="260" alt="facebook/react 的星标历史曲线"></a> |
| 3 | [withastro/astro](https://github.com/withastro/astro)<br>做内容型网站，页面输出更轻量<br>`Web / 前端` | +204 | 29.1 | 63,677 | <a href="https://www.star-history.com/#withastro/astro&Date"><img src="https://api.star-history.com/svg?repos=withastro/astro&type=Date" width="260" alt="withastro/astro 的星标历史曲线"></a> |
| 4 | [vercel/next.js](https://github.com/vercel/next.js)<br>用 React 做完整网站，从前到后<br>`Web / 前端` | +155 | 22.1 | 143,234 | <a href="https://www.star-history.com/#vercel/next.js&Date"><img src="https://api.star-history.com/svg?repos=vercel/next.js&type=Date" width="260" alt="vercel/next.js 的星标历史曲线"></a> |
| 5 | [sveltejs/svelte](https://github.com/sveltejs/svelte)<br>你写组件，编译器变出高效的网页代码<br>`Web / 前端` | +108 | 15.4 | 88,538 | <a href="https://www.star-history.com/#sveltejs/svelte&Date"><img src="https://api.star-history.com/svg?repos=sveltejs/svelte&type=Date" width="260" alt="sveltejs/svelte 的星标历史曲线"></a> |
| 6 | [tailwindlabs/tailwindcss](https://github.com/tailwindlabs/tailwindcss)<br>不写一大堆 CSS，也能做定制界面<br>`Web / 前端` | +106 | 15.1 | 98,055 | <a href="https://www.star-history.com/#tailwindlabs/tailwindcss&Date"><img src="https://api.star-history.com/svg?repos=tailwindlabs/tailwindcss&type=Date" width="260" alt="tailwindlabs/tailwindcss 的星标历史曲线"></a> |
| 7 | [vuejs/core](https://github.com/vuejs/core)<br>从一个小页面开始，用多少学多少<br>`Web / 前端` | +80 | 11.4 | 54,820 | <a href="https://www.star-history.com/#vuejs/core&Date"><img src="https://api.star-history.com/svg?repos=vuejs/core&type=Date" width="260" alt="vuejs/core 的星标历史曲线"></a> |
| 8 | [tanstack/query](https://github.com/tanstack/query)<br>请求数据和缓存，交给它管<br>`Web / 前端` | +48 | 6.9 | 50,521 | <a href="https://www.star-history.com/#tanstack/query&Date"><img src="https://api.star-history.com/svg?repos=tanstack/query&type=Date" width="260" alt="tanstack/query 的星标历史曲线"></a> |

### 本月增长最快（近 30 天）

| # | 项目 | 新增星标 | 星标/天 | 总星标 | 星标历史 |
|---|---|---:|---:|---:|---|
| 1 | [shadcn-ui/ui](https://github.com/shadcn-ui/ui)<br>好看的组件，代码归你，随便改<br>`Web / 前端` | +2,623 | 87.4 | 127,202 | <a href="https://www.star-history.com/#shadcn-ui/ui&Date"><img src="https://api.star-history.com/svg?repos=shadcn-ui/ui&type=Date" width="260" alt="shadcn-ui/ui 的星标历史曲线"></a> |
| 2 | [facebook/react](https://github.com/facebook/react)<br>网页和 App 界面，都能用它来搭<br>`Web / 前端` | +1,649 | 55.0 | 251,874 | <a href="https://www.star-history.com/#facebook/react&Date"><img src="https://api.star-history.com/svg?repos=facebook/react&type=Date" width="260" alt="facebook/react 的星标历史曲线"></a> |
| 3 | [withastro/astro](https://github.com/withastro/astro)<br>做内容型网站，页面输出更轻量<br>`Web / 前端` | +764 | 25.5 | 63,677 | <a href="https://www.star-history.com/#withastro/astro&Date"><img src="https://api.star-history.com/svg?repos=withastro/astro&type=Date" width="260" alt="withastro/astro 的星标历史曲线"></a> |
| 4 | [vercel/next.js](https://github.com/vercel/next.js)<br>用 React 做完整网站，从前到后<br>`Web / 前端` | +738 | 24.6 | 143,234 | <a href="https://www.star-history.com/#vercel/next.js&Date"><img src="https://api.star-history.com/svg?repos=vercel/next.js&type=Date" width="260" alt="vercel/next.js 的星标历史曲线"></a> |
| 5 | [tailwindlabs/tailwindcss](https://github.com/tailwindlabs/tailwindcss)<br>不写一大堆 CSS，也能做定制界面<br>`Web / 前端` | +486 | 16.2 | 98,055 | <a href="https://www.star-history.com/#tailwindlabs/tailwindcss&Date"><img src="https://api.star-history.com/svg?repos=tailwindlabs/tailwindcss&type=Date" width="260" alt="tailwindlabs/tailwindcss 的星标历史曲线"></a> |
| 6 | [sveltejs/svelte](https://github.com/sveltejs/svelte)<br>你写组件，编译器变出高效的网页代码<br>`Web / 前端` | +486 | 16.2 | 88,538 | <a href="https://www.star-history.com/#sveltejs/svelte&Date"><img src="https://api.star-history.com/svg?repos=sveltejs/svelte&type=Date" width="260" alt="sveltejs/svelte 的星标历史曲线"></a> |
| 7 | [vuejs/core](https://github.com/vuejs/core)<br>从一个小页面开始，用多少学多少<br>`Web / 前端` | +410 | 13.7 | 54,820 | <a href="https://www.star-history.com/#vuejs/core&Date"><img src="https://api.star-history.com/svg?repos=vuejs/core&type=Date" width="260" alt="vuejs/core 的星标历史曲线"></a> |
| 8 | [tanstack/query](https://github.com/tanstack/query)<br>请求数据和缓存，交给它管<br>`Web / 前端` | +210 | 7.0 | 50,521 | <a href="https://www.star-history.com/#tanstack/query&Date"><img src="https://api.star-history.com/svg?repos=tanstack/query&type=Date" width="260" alt="tanstack/query 的星标历史曲线"></a> |

### 今年增长最快（近 365 天）

| # | 项目 | 新增星标 | 星标/天 | 总星标 | 星标历史 |
|---|---|---:|---:|---:|---|
| 1 | [shadcn-ui/ui](https://github.com/shadcn-ui/ui)<br>好看的组件，代码归你，随便改<br>`Web / 前端` | +30,353 | 83.2 | 127,202 | <a href="https://www.star-history.com/#shadcn-ui/ui&Date"><img src="https://api.star-history.com/svg?repos=shadcn-ui/ui&type=Date" width="260" alt="shadcn-ui/ui 的星标历史曲线"></a> |
| 2 | [facebook/react](https://github.com/facebook/react)<br>网页和 App 界面，都能用它来搭<br>`Web / 前端` | +15,193 | 41.6 | 251,874 | <a href="https://www.star-history.com/#facebook/react&Date"><img src="https://api.star-history.com/svg?repos=facebook/react&type=Date" width="260" alt="facebook/react 的星标历史曲线"></a> |
| 3 | [withastro/astro](https://github.com/withastro/astro)<br>做内容型网站，页面输出更轻量<br>`Web / 前端` | +10,497 | 28.8 | 63,677 | <a href="https://www.star-history.com/#withastro/astro&Date"><img src="https://api.star-history.com/svg?repos=withastro/astro&type=Date" width="260" alt="withastro/astro 的星标历史曲线"></a> |
| 4 | [vercel/next.js](https://github.com/vercel/next.js)<br>用 React 做完整网站，从前到后<br>`Web / 前端` | +10,335 | 28.3 | 143,234 | <a href="https://www.star-history.com/#vercel/next.js&Date"><img src="https://api.star-history.com/svg?repos=vercel/next.js&type=Date" width="260" alt="vercel/next.js 的星标历史曲线"></a> |
| 5 | [tailwindlabs/tailwindcss](https://github.com/tailwindlabs/tailwindcss)<br>不写一大堆 CSS，也能做定制界面<br>`Web / 前端` | +8,527 | 23.4 | 98,055 | <a href="https://www.star-history.com/#tailwindlabs/tailwindcss&Date"><img src="https://api.star-history.com/svg?repos=tailwindlabs/tailwindcss&type=Date" width="260" alt="tailwindlabs/tailwindcss 的星标历史曲线"></a> |
| 6 | [sveltejs/svelte](https://github.com/sveltejs/svelte)<br>你写组件，编译器变出高效的网页代码<br>`Web / 前端` | +5,274 | 14.4 | 88,538 | <a href="https://www.star-history.com/#sveltejs/svelte&Date"><img src="https://api.star-history.com/svg?repos=sveltejs/svelte&type=Date" width="260" alt="sveltejs/svelte 的星标历史曲线"></a> |
| 7 | [tanstack/query](https://github.com/tanstack/query)<br>请求数据和缓存，交给它管<br>`Web / 前端` | +3,856 | 10.6 | 50,521 | <a href="https://www.star-history.com/#tanstack/query&Date"><img src="https://api.star-history.com/svg?repos=tanstack/query&type=Date" width="260" alt="tanstack/query 的星标历史曲线"></a> |
| 8 | [vuejs/core](https://github.com/vuejs/core)<br>从一个小页面开始，用多少学多少<br>`Web / 前端` | +3,622 | 9.9 | 54,820 | <a href="https://www.star-history.com/#vuejs/core&Date"><img src="https://api.star-history.com/svg?repos=vuejs/core&type=Date" width="260" alt="vuejs/core 的星标历史曲线"></a> |

### 总星标数（历史累计）

| # | 项目 | 总星标 | 星标历史 |
|---|---|---:|---|
| 1 | [facebook/react](https://github.com/facebook/react)<br>网页和 App 界面，都能用它来搭<br>`Web / 前端` | 251,874 | <a href="https://www.star-history.com/#facebook/react&Date"><img src="https://api.star-history.com/svg?repos=facebook/react&type=Date" width="260" alt="facebook/react 的星标历史曲线"></a> |
| 2 | [vercel/next.js](https://github.com/vercel/next.js)<br>用 React 做完整网站，从前到后<br>`Web / 前端` | 143,234 | <a href="https://www.star-history.com/#vercel/next.js&Date"><img src="https://api.star-history.com/svg?repos=vercel/next.js&type=Date" width="260" alt="vercel/next.js 的星标历史曲线"></a> |
| 3 | [shadcn-ui/ui](https://github.com/shadcn-ui/ui)<br>好看的组件，代码归你，随便改<br>`Web / 前端` | 127,202 | <a href="https://www.star-history.com/#shadcn-ui/ui&Date"><img src="https://api.star-history.com/svg?repos=shadcn-ui/ui&type=Date" width="260" alt="shadcn-ui/ui 的星标历史曲线"></a> |
| 4 | [tailwindlabs/tailwindcss](https://github.com/tailwindlabs/tailwindcss)<br>不写一大堆 CSS，也能做定制界面<br>`Web / 前端` | 98,055 | <a href="https://www.star-history.com/#tailwindlabs/tailwindcss&Date"><img src="https://api.star-history.com/svg?repos=tailwindlabs/tailwindcss&type=Date" width="260" alt="tailwindlabs/tailwindcss 的星标历史曲线"></a> |
| 5 | [sveltejs/svelte](https://github.com/sveltejs/svelte)<br>你写组件，编译器变出高效的网页代码<br>`Web / 前端` | 88,538 | <a href="https://www.star-history.com/#sveltejs/svelte&Date"><img src="https://api.star-history.com/svg?repos=sveltejs/svelte&type=Date" width="260" alt="sveltejs/svelte 的星标历史曲线"></a> |
| 6 | [withastro/astro](https://github.com/withastro/astro)<br>做内容型网站，页面输出更轻量<br>`Web / 前端` | 63,677 | <a href="https://www.star-history.com/#withastro/astro&Date"><img src="https://api.star-history.com/svg?repos=withastro/astro&type=Date" width="260" alt="withastro/astro 的星标历史曲线"></a> |
| 7 | [vuejs/core](https://github.com/vuejs/core)<br>从一个小页面开始，用多少学多少<br>`Web / 前端` | 54,820 | <a href="https://www.star-history.com/#vuejs/core&Date"><img src="https://api.star-history.com/svg?repos=vuejs/core&type=Date" width="260" alt="vuejs/core 的星标历史曲线"></a> |
| 8 | [tanstack/query](https://github.com/tanstack/query)<br>请求数据和缓存，交给它管<br>`Web / 前端` | 50,521 | <a href="https://www.star-history.com/#tanstack/query&Date"><img src="https://api.star-history.com/svg?repos=tanstack/query&type=Date" width="260" alt="tanstack/query 的星标历史曲线"></a> |

## 基础设施

> 容器、Kubernetes、云、网络与可观测性

### 最热新仓库（近 7 天内创建）

| # | 项目 | 创建时间（UTC） | 总星标 | 星标/天 | 星标历史 |
|---|---|---|---:|---:|---|
| 1 | [davemessew/AgentFlux](https://github.com/davemessew/AgentFlux)<br>画出 AI 工作流，在自己电脑上跑 | 2026-10-27<br><sub>6.4 天</sub> | 247 | 38.8 | <a href="https://www.star-history.com/#davemessew/AgentFlux&Date"><img src="https://api.star-history.com/svg?repos=davemessew/AgentFlux&type=Date" width="260" alt="davemessew/AgentFlux 的星标历史曲线"></a> |

### 本周增长最快（近 7 天）

| # | 项目 | 新增星标 | 星标/天 | 总星标 | 星标历史 |
|---|---|---:|---:|---:|---|
| 1 | [caddyserver/caddy](https://github.com/caddyserver/caddy)<br>搭网站服务器，HTTPS 自动配好<br>`基础设施` | +265 | 37.9 | 78,663 | <a href="https://www.star-history.com/#caddyserver/caddy&Date"><img src="https://api.star-history.com/svg?repos=caddyserver/caddy&type=Date" width="260" alt="caddyserver/caddy 的星标历史曲线"></a> |
| 2 | [kubernetes/kubernetes](https://github.com/kubernetes/kubernetes)<br>容器多了，部署扩容交给它<br>`基础设施` | +203 | 29.0 | 128,619 | <a href="https://www.star-history.com/#kubernetes/kubernetes&Date"><img src="https://api.star-history.com/svg?repos=kubernetes/kubernetes&type=Date" width="260" alt="kubernetes/kubernetes 的星标历史曲线"></a> |
| 3 | [grafana/grafana](https://github.com/grafana/grafana)<br>指标日志链路，放进一个面板<br>`基础设施` | +173 | 24.7 | 77,645 | <a href="https://www.star-history.com/#grafana/grafana&Date"><img src="https://api.star-history.com/svg?repos=grafana/grafana&type=Date" width="260" alt="grafana/grafana 的星标历史曲线"></a> |
| 4 | [prometheus/prometheus](https://github.com/prometheus/prometheus)<br>系统出问题，告警先找到你<br>`基础设施` | +158 | 22.6 | 66,915 | <a href="https://www.star-history.com/#prometheus/prometheus&Date"><img src="https://api.star-history.com/svg?repos=prometheus/prometheus&type=Date" width="260" alt="prometheus/prometheus 的星标历史曲线"></a> |
| 5 | [docker/compose](https://github.com/docker/compose)<br>多个容器写进一个文件，一起跑<br>`基础设施` | +113 | 16.1 | 38,585 | <a href="https://www.star-history.com/#docker/compose&Date"><img src="https://api.star-history.com/svg?repos=docker/compose&type=Date" width="260" alt="docker/compose 的星标历史曲线"></a> |
| 6 | [hashicorp/terraform](https://github.com/hashicorp/terraform)<br>云资源写成代码，可审阅、可版本管理<br>`基础设施` | +92 | 13.1 | 50,118 | <a href="https://www.star-history.com/#hashicorp/terraform&Date"><img src="https://api.star-history.com/svg?repos=hashicorp/terraform&type=Date" width="260" alt="hashicorp/terraform 的星标历史曲线"></a> |
| 7 | [traefik/traefik](https://github.com/traefik/traefik)<br>服务多了，流量自动分好<br>`基础设施` | +89 | 12.7 | 65,446 | <a href="https://www.star-history.com/#traefik/traefik&Date"><img src="https://api.star-history.com/svg?repos=traefik/traefik&type=Date" width="260" alt="traefik/traefik 的星标历史曲线"></a> |
| 8 | [pulumi/pulumi](https://github.com/pulumi/pulumi)<br>用熟悉的编程语言管云资源<br>`基础设施` | +30 | 4.3 | 25,840 | <a href="https://www.star-history.com/#pulumi/pulumi&Date"><img src="https://api.star-history.com/svg?repos=pulumi/pulumi&type=Date" width="260" alt="pulumi/pulumi 的星标历史曲线"></a> |

### 本月增长最快（近 30 天）

| # | 项目 | 新增星标 | 星标/天 | 总星标 | 星标历史 |
|---|---|---:|---:|---:|---|
| 1 | [caddyserver/caddy](https://github.com/caddyserver/caddy)<br>搭网站服务器，HTTPS 自动配好<br>`基础设施` | +2,521 | 84.0 | 78,663 | <a href="https://www.star-history.com/#caddyserver/caddy&Date"><img src="https://api.star-history.com/svg?repos=caddyserver/caddy&type=Date" width="260" alt="caddyserver/caddy 的星标历史曲线"></a> |
| 2 | [kubernetes/kubernetes](https://github.com/kubernetes/kubernetes)<br>容器多了，部署扩容交给它<br>`基础设施` | +892 | 29.7 | 128,619 | <a href="https://www.star-history.com/#kubernetes/kubernetes&Date"><img src="https://api.star-history.com/svg?repos=kubernetes/kubernetes&type=Date" width="260" alt="kubernetes/kubernetes 的星标历史曲线"></a> |
| 3 | [grafana/grafana](https://github.com/grafana/grafana)<br>指标日志链路，放进一个面板<br>`基础设施` | +746 | 24.9 | 77,645 | <a href="https://www.star-history.com/#grafana/grafana&Date"><img src="https://api.star-history.com/svg?repos=grafana/grafana&type=Date" width="260" alt="grafana/grafana 的星标历史曲线"></a> |
| 4 | [prometheus/prometheus](https://github.com/prometheus/prometheus)<br>系统出问题，告警先找到你<br>`基础设施` | +698 | 23.3 | 66,915 | <a href="https://www.star-history.com/#prometheus/prometheus&Date"><img src="https://api.star-history.com/svg?repos=prometheus/prometheus&type=Date" width="260" alt="prometheus/prometheus 的星标历史曲线"></a> |
| 5 | [traefik/traefik](https://github.com/traefik/traefik)<br>服务多了，流量自动分好<br>`基础设施` | +482 | 16.1 | 65,446 | <a href="https://www.star-history.com/#traefik/traefik&Date"><img src="https://api.star-history.com/svg?repos=traefik/traefik&type=Date" width="260" alt="traefik/traefik 的星标历史曲线"></a> |
| 6 | [hashicorp/terraform](https://github.com/hashicorp/terraform)<br>云资源写成代码，可审阅、可版本管理<br>`基础设施` | +399 | 13.3 | 50,118 | <a href="https://www.star-history.com/#hashicorp/terraform&Date"><img src="https://api.star-history.com/svg?repos=hashicorp/terraform&type=Date" width="260" alt="hashicorp/terraform 的星标历史曲线"></a> |
| 7 | [docker/compose](https://github.com/docker/compose)<br>多个容器写进一个文件，一起跑<br>`基础设施` | +371 | 12.4 | 38,585 | <a href="https://www.star-history.com/#docker/compose&Date"><img src="https://api.star-history.com/svg?repos=docker/compose&type=Date" width="260" alt="docker/compose 的星标历史曲线"></a> |
| 8 | [pulumi/pulumi](https://github.com/pulumi/pulumi)<br>用熟悉的编程语言管云资源<br>`基础设施` | +124 | 4.1 | 25,840 | <a href="https://www.star-history.com/#pulumi/pulumi&Date"><img src="https://api.star-history.com/svg?repos=pulumi/pulumi&type=Date" width="260" alt="pulumi/pulumi 的星标历史曲线"></a> |

### 今年增长最快（近 365 天）

| # | 项目 | 新增星标 | 星标/天 | 总星标 | 星标历史 |
|---|---|---:|---:|---:|---|
| 1 | [caddyserver/caddy](https://github.com/caddyserver/caddy)<br>搭网站服务器，HTTPS 自动配好<br>`基础设施` | +11,877 | 32.5 | 78,663 | <a href="https://www.star-history.com/#caddyserver/caddy&Date"><img src="https://api.star-history.com/svg?repos=caddyserver/caddy&type=Date" width="260" alt="caddyserver/caddy 的星标历史曲线"></a> |
| 2 | [kubernetes/kubernetes](https://github.com/kubernetes/kubernetes)<br>容器多了，部署扩容交给它<br>`基础设施` | +11,583 | 31.7 | 128,619 | <a href="https://www.star-history.com/#kubernetes/kubernetes&Date"><img src="https://api.star-history.com/svg?repos=kubernetes/kubernetes&type=Date" width="260" alt="kubernetes/kubernetes 的星标历史曲线"></a> |
| 3 | [traefik/traefik](https://github.com/traefik/traefik)<br>服务多了，流量自动分好<br>`基础设施` | +8,713 | 23.9 | 65,446 | <a href="https://www.star-history.com/#traefik/traefik&Date"><img src="https://api.star-history.com/svg?repos=traefik/traefik&type=Date" width="260" alt="traefik/traefik 的星标历史曲线"></a> |
| 4 | [grafana/grafana](https://github.com/grafana/grafana)<br>指标日志链路，放进一个面板<br>`基础设施` | +7,869 | 21.6 | 77,645 | <a href="https://www.star-history.com/#grafana/grafana&Date"><img src="https://api.star-history.com/svg?repos=grafana/grafana&type=Date" width="260" alt="grafana/grafana 的星标历史曲线"></a> |
| 5 | [prometheus/prometheus](https://github.com/prometheus/prometheus)<br>系统出问题，告警先找到你<br>`基础设施` | +6,540 | 17.9 | 66,915 | <a href="https://www.star-history.com/#prometheus/prometheus&Date"><img src="https://api.star-history.com/svg?repos=prometheus/prometheus&type=Date" width="260" alt="prometheus/prometheus 的星标历史曲线"></a> |
| 6 | [hashicorp/terraform](https://github.com/hashicorp/terraform)<br>云资源写成代码，可审阅、可版本管理<br>`基础设施` | +3,769 | 10.3 | 50,118 | <a href="https://www.star-history.com/#hashicorp/terraform&Date"><img src="https://api.star-history.com/svg?repos=hashicorp/terraform&type=Date" width="260" alt="hashicorp/terraform 的星标历史曲线"></a> |
| 7 | [docker/compose](https://github.com/docker/compose)<br>多个容器写进一个文件，一起跑<br>`基础设施` | +2,619 | 7.2 | 38,585 | <a href="https://www.star-history.com/#docker/compose&Date"><img src="https://api.star-history.com/svg?repos=docker/compose&type=Date" width="260" alt="docker/compose 的星标历史曲线"></a> |
| 8 | [pulumi/pulumi](https://github.com/pulumi/pulumi)<br>用熟悉的编程语言管云资源<br>`基础设施` | +2,081 | 5.7 | 25,840 | <a href="https://www.star-history.com/#pulumi/pulumi&Date"><img src="https://api.star-history.com/svg?repos=pulumi/pulumi&type=Date" width="260" alt="pulumi/pulumi 的星标历史曲线"></a> |

### 总星标数（历史累计）

| # | 项目 | 总星标 | 星标历史 |
|---|---|---:|---|
| 1 | [kubernetes/kubernetes](https://github.com/kubernetes/kubernetes)<br>容器多了，部署扩容交给它<br>`基础设施` | 128,619 | <a href="https://www.star-history.com/#kubernetes/kubernetes&Date"><img src="https://api.star-history.com/svg?repos=kubernetes/kubernetes&type=Date" width="260" alt="kubernetes/kubernetes 的星标历史曲线"></a> |
| 2 | [caddyserver/caddy](https://github.com/caddyserver/caddy)<br>搭网站服务器，HTTPS 自动配好<br>`基础设施` | 78,663 | <a href="https://www.star-history.com/#caddyserver/caddy&Date"><img src="https://api.star-history.com/svg?repos=caddyserver/caddy&type=Date" width="260" alt="caddyserver/caddy 的星标历史曲线"></a> |
| 3 | [grafana/grafana](https://github.com/grafana/grafana)<br>指标日志链路，放进一个面板<br>`基础设施` | 77,645 | <a href="https://www.star-history.com/#grafana/grafana&Date"><img src="https://api.star-history.com/svg?repos=grafana/grafana&type=Date" width="260" alt="grafana/grafana 的星标历史曲线"></a> |
| 4 | [prometheus/prometheus](https://github.com/prometheus/prometheus)<br>系统出问题，告警先找到你<br>`基础设施` | 66,915 | <a href="https://www.star-history.com/#prometheus/prometheus&Date"><img src="https://api.star-history.com/svg?repos=prometheus/prometheus&type=Date" width="260" alt="prometheus/prometheus 的星标历史曲线"></a> |
| 5 | [traefik/traefik](https://github.com/traefik/traefik)<br>服务多了，流量自动分好<br>`基础设施` | 65,446 | <a href="https://www.star-history.com/#traefik/traefik&Date"><img src="https://api.star-history.com/svg?repos=traefik/traefik&type=Date" width="260" alt="traefik/traefik 的星标历史曲线"></a> |
| 6 | [hashicorp/terraform](https://github.com/hashicorp/terraform)<br>云资源写成代码，可审阅、可版本管理<br>`基础设施` | 50,118 | <a href="https://www.star-history.com/#hashicorp/terraform&Date"><img src="https://api.star-history.com/svg?repos=hashicorp/terraform&type=Date" width="260" alt="hashicorp/terraform 的星标历史曲线"></a> |
| 7 | [docker/compose](https://github.com/docker/compose)<br>多个容器写进一个文件，一起跑<br>`基础设施` | 38,585 | <a href="https://www.star-history.com/#docker/compose&Date"><img src="https://api.star-history.com/svg?repos=docker/compose&type=Date" width="260" alt="docker/compose 的星标历史曲线"></a> |
| 8 | [pulumi/pulumi](https://github.com/pulumi/pulumi)<br>用熟悉的编程语言管云资源<br>`基础设施` | 25,840 | <a href="https://www.star-history.com/#pulumi/pulumi&Date"><img src="https://api.star-history.com/svg?repos=pulumi/pulumi&type=Date" width="260" alt="pulumi/pulumi 的星标历史曲线"></a> |

## 设计 / 创意

> 设计系统、绘图、动画与创意工具

### 最热新仓库（近 7 天内创建）

| # | 项目 | 创建时间（UTC） | 总星标 | 星标/天 | 星标历史 |
|---|---|---|---:|---:|---|
| 1 | [patch-gg/pixelfx](https://github.com/patch-gg/pixelfx)<br>缺像素特效？244段简短代码直接套用 | 2026-10-30<br><sub>3.7 天</sub> | 3,469 | 939.8 | <a href="https://www.star-history.com/#patch-gg/pixelfx&Date"><img src="https://api.star-history.com/svg?repos=patch-gg/pixelfx&type=Date" width="260" alt="patch-gg/pixelfx 的星标历史曲线"></a> |
| 2 | [kevinraymond/florilegium](https://github.com/kevinraymond/florilegium)<br>页面太单调？画上代尔夫特蓝花卉页边 | 2026-10-30<br><sub>3.6 天</sub> | 1,363 | 373.9 | <a href="https://www.star-history.com/#kevinraymond/florilegium&Date"><img src="https://api.star-history.com/svg?repos=kevinraymond/florilegium&type=Date" width="260" alt="kevinraymond/florilegium 的星标历史曲线"></a> |
| 3 | [op7418/dsh-guizang-design](https://github.com/op7418/dsh-guizang-design)<br>排版全是 AI 味？用一套设计系统去掉 | 2026-10-30<br><sub>3.4 天</sub> | 253 | 75.4 | <a href="https://www.star-history.com/#op7418/dsh-guizang-design&Date"><img src="https://api.star-history.com/svg?repos=op7418/dsh-guizang-design&type=Date" width="260" alt="op7418/dsh-guizang-design 的星标历史曲线"></a> |
| 4 | [artemnovitckii/claude-animation-skills](https://github.com/artemnovitckii/claude-animation-skills)<br>六个无需素材即可为 reels 制作动画的 Claude Code 技能：3D 卡通解说、火柴人、极简线条艺术、3D 地图路线、分解视图、li… | 2026-11-01<br><sub>1.9 天</sub> | 129 | 69.7 | <a href="https://www.star-history.com/#artemnovitckii/claude-animation-skills&Date"><img src="https://api.star-history.com/svg?repos=artemnovitckii/claude-animation-skills&type=Date" width="260" alt="artemnovitckii/claude-animation-skills 的星标历史曲线"></a> |
| 5 | [GuoZheng-de-BaBa/nursing-research-skills](https://github.com/GuoZheng-de-BaBa/nursing-research-skills)<br>护研搭子｜18个开源护理科研AI技能，覆盖检索、设计、数据、统计、写作与图表；新增队列研究和RCT流程、模板及合成示例。 | 2026-10-30<br><sub>3.4 天</sub> | 170 | 50.3 | <a href="https://www.star-history.com/#GuoZheng-de-BaBa/nursing-research-skills&Date"><img src="https://api.star-history.com/svg?repos=GuoZheng-de-BaBa/nursing-research-skills&type=Date" width="260" alt="GuoZheng-de-BaBa/nursing-research-skills 的星标历史曲线"></a> |
| 6 | [Akillll-DuoHe/fy-code-animation](https://github.com/Akillll-DuoHe/fy-code-animation)<br>代码动画难做？文案与声音直接生成 | 2026-10-30<br><sub>3.6 天</sub> | 134 | 37.7 | <a href="https://www.star-history.com/#Akillll-DuoHe/fy-code-animation&Date"><img src="https://api.star-history.com/svg?repos=Akillll-DuoHe/fy-code-animation&type=Date" width="260" alt="Akillll-DuoHe/fy-code-animation 的星标历史曲线"></a> |
| 7 | [enmerasoftware/ai-design-check](https://github.com/enmerasoftware/ai-design-check)<br>AI 智能体写的界面，帮你检查设计规范 | 2026-10-28<br><sub>5.7 天</sub> | 198 | 35.0 | <a href="https://www.star-history.com/#enmerasoftware/ai-design-check&Date"><img src="https://api.star-history.com/svg?repos=enmerasoftware/ai-design-check&type=Date" width="260" alt="enmerasoftware/ai-design-check 的星标历史曲线"></a> |
| 8 | [ersinkoc/AI-Video-Factory](https://github.com/ersinkoc/AI-Video-Factory)<br>AI 视频工厂：从一个主题到成品的跨语言 YouTube 视频。Claude 智能体负责编写、规划、绘制与审核；Studio 让用户始终掌控全局。 | 2026-10-29<br><sub>4.0 天</sub> | 132 | 32.7 | <a href="https://www.star-history.com/#ersinkoc/AI-Video-Factory&Date"><img src="https://api.star-history.com/svg?repos=ersinkoc/AI-Video-Factory&type=Date" width="260" alt="ersinkoc/AI-Video-Factory 的星标历史曲线"></a> |
| 9 | [sirioberati/YouTube-AI-Motion-Graphics](https://github.com/sirioberati/YouTube-AI-Motion-Graphics)<br>解说动效难做？74个看板随语音同步 | 2026-10-27<br><sub>6.2 天</sub> | 134 | 21.5 | <a href="https://www.star-history.com/#sirioberati/YouTube-AI-Motion-Graphics&Date"><img src="https://api.star-history.com/svg?repos=sirioberati/YouTube-AI-Motion-Graphics&type=Date" width="260" alt="sirioberati/YouTube-AI-Motion-Graphics 的星标历史曲线"></a> |

### 本周增长最快（近 7 天）

| # | 项目 | 新增星标 | 星标/天 | 总星标 | 星标历史 |
|---|---|---:|---:|---:|---|
| 1 | [excalidraw/excalidraw](https://github.com/excalidraw/excalidraw)<br>打开就画，像在纸上随手画图<br>`设计 / 创意` | +492 | 70.3 | 135,054 | <a href="https://www.star-history.com/#excalidraw/excalidraw&Date"><img src="https://api.star-history.com/svg?repos=excalidraw/excalidraw&type=Date" width="260" alt="excalidraw/excalidraw 的星标历史曲线"></a> |
| 2 | [penpot/penpot](https://github.com/penpot/penpot)<br>团队一起做设计，用开源平台<br>`设计 / 创意` | +338 | 48.3 | 61,998 | <a href="https://www.star-history.com/#penpot/penpot&Date"><img src="https://api.star-history.com/svg?repos=penpot/penpot&type=Date" width="260" alt="penpot/penpot 的星标历史曲线"></a> |
| 3 | [lucide-icons/lucide](https://github.com/lucide-icons/lucide)<br>一套图标风格统一，拿来就用<br>`设计 / 创意` | +167 | 23.9 | 25,474 | <a href="https://www.star-history.com/#lucide-icons/lucide&Date"><img src="https://api.star-history.com/svg?repos=lucide-icons/lucide&type=Date" width="260" alt="lucide-icons/lucide 的星标历史曲线"></a> |
| 4 | [jgraph/drawio](https://github.com/jgraph/drawio)<br>画图和白板，一个编辑器搞定<br>`设计 / 创意` | +142 | 20.3 | 9,140 | <a href="https://www.star-history.com/#jgraph/drawio&Date"><img src="https://api.star-history.com/svg?repos=jgraph/drawio&type=Date" width="260" alt="jgraph/drawio 的星标历史曲线"></a> |
| 5 | [saadeghi/daisyui](https://github.com/saadeghi/daisyui)<br>Tailwind 也有现成组件可挑<br>`设计 / 创意` | +73 | 10.4 | 42,734 | <a href="https://www.star-history.com/#saadeghi/daisyui&Date"><img src="https://api.star-history.com/svg?repos=saadeghi/daisyui&type=Date" width="260" alt="saadeghi/daisyui 的星标历史曲线"></a> |
| 6 | [airbnb/lottie-web](https://github.com/airbnb/lottie-web)<br>AE 做的动画，直接放进网页<br>`设计 / 创意` | +64 | 9.1 | 32,332 | <a href="https://www.star-history.com/#airbnb/lottie-web&Date"><img src="https://api.star-history.com/svg?repos=airbnb/lottie-web&type=Date" width="260" alt="airbnb/lottie-web 的星标历史曲线"></a> |
| 7 | [phosphor-icons/homepage](https://github.com/phosphor-icons/homepage)<br>一整套灵活的图标，人人可用<br>`设计 / 创意` | +38 | 5.4 | 7,755 | <a href="https://www.star-history.com/#phosphor-icons/homepage&Date"><img src="https://api.star-history.com/svg?repos=phosphor-icons/homepage&type=Date" width="260" alt="phosphor-icons/homepage 的星标历史曲线"></a> |
| 8 | [lottiefiles/lottie-ios](https://github.com/lottiefiles/lottie-ios)<br>AE 做的动画，直接放进 iOS<br>`设计 / 创意` | +0 | 0.0 | 43 | <a href="https://www.star-history.com/#lottiefiles/lottie-ios&Date"><img src="https://api.star-history.com/svg?repos=lottiefiles/lottie-ios&type=Date" width="260" alt="lottiefiles/lottie-ios 的星标历史曲线"></a> |

### 本月增长最快（近 30 天）

| # | 项目 | 新增星标 | 星标/天 | 总星标 | 星标历史 |
|---|---|---:|---:|---:|---|
| 1 | [excalidraw/excalidraw](https://github.com/excalidraw/excalidraw)<br>打开就画，像在纸上随手画图<br>`设计 / 创意` | +1,981 | 66.0 | 135,054 | <a href="https://www.star-history.com/#excalidraw/excalidraw&Date"><img src="https://api.star-history.com/svg?repos=excalidraw/excalidraw&type=Date" width="260" alt="excalidraw/excalidraw 的星标历史曲线"></a> |
| 2 | [penpot/penpot](https://github.com/penpot/penpot)<br>团队一起做设计，用开源平台<br>`设计 / 创意` | +1,499 | 50.0 | 61,998 | <a href="https://www.star-history.com/#penpot/penpot&Date"><img src="https://api.star-history.com/svg?repos=penpot/penpot&type=Date" width="260" alt="penpot/penpot 的星标历史曲线"></a> |
| 3 | [lucide-icons/lucide](https://github.com/lucide-icons/lucide)<br>一套图标风格统一，拿来就用<br>`设计 / 创意` | +682 | 22.7 | 25,474 | <a href="https://www.star-history.com/#lucide-icons/lucide&Date"><img src="https://api.star-history.com/svg?repos=lucide-icons/lucide&type=Date" width="260" alt="lucide-icons/lucide 的星标历史曲线"></a> |
| 4 | [jgraph/drawio](https://github.com/jgraph/drawio)<br>画图和白板，一个编辑器搞定<br>`设计 / 创意` | +612 | 20.4 | 9,140 | <a href="https://www.star-history.com/#jgraph/drawio&Date"><img src="https://api.star-history.com/svg?repos=jgraph/drawio&type=Date" width="260" alt="jgraph/drawio 的星标历史曲线"></a> |
| 5 | [saadeghi/daisyui](https://github.com/saadeghi/daisyui)<br>Tailwind 也有现成组件可挑<br>`设计 / 创意` | +277 | 9.2 | 42,734 | <a href="https://www.star-history.com/#saadeghi/daisyui&Date"><img src="https://api.star-history.com/svg?repos=saadeghi/daisyui&type=Date" width="260" alt="saadeghi/daisyui 的星标历史曲线"></a> |
| 6 | [airbnb/lottie-web](https://github.com/airbnb/lottie-web)<br>AE 做的动画，直接放进网页<br>`设计 / 创意` | +223 | 7.4 | 32,332 | <a href="https://www.star-history.com/#airbnb/lottie-web&Date"><img src="https://api.star-history.com/svg?repos=airbnb/lottie-web&type=Date" width="260" alt="airbnb/lottie-web 的星标历史曲线"></a> |
| 7 | [phosphor-icons/homepage](https://github.com/phosphor-icons/homepage)<br>一整套灵活的图标，人人可用<br>`设计 / 创意` | +181 | 6.0 | 7,755 | <a href="https://www.star-history.com/#phosphor-icons/homepage&Date"><img src="https://api.star-history.com/svg?repos=phosphor-icons/homepage&type=Date" width="260" alt="phosphor-icons/homepage 的星标历史曲线"></a> |
| 8 | [lottiefiles/lottie-ios](https://github.com/lottiefiles/lottie-ios)<br>AE 做的动画，直接放进 iOS<br>`设计 / 创意` | +0 | 0.0 | 43 | <a href="https://www.star-history.com/#lottiefiles/lottie-ios&Date"><img src="https://api.star-history.com/svg?repos=lottiefiles/lottie-ios&type=Date" width="260" alt="lottiefiles/lottie-ios 的星标历史曲线"></a> |

### 今年增长最快（近 365 天）

| # | 项目 | 新增星标 | 星标/天 | 总星标 | 星标历史 |
|---|---|---:|---:|---:|---|
| 1 | [excalidraw/excalidraw](https://github.com/excalidraw/excalidraw)<br>打开就画，像在纸上随手画图<br>`设计 / 创意` | +27,021 | 74.0 | 135,054 | <a href="https://www.star-history.com/#excalidraw/excalidraw&Date"><img src="https://api.star-history.com/svg?repos=excalidraw/excalidraw&type=Date" width="260" alt="excalidraw/excalidraw 的星标历史曲线"></a> |
| 2 | [penpot/penpot](https://github.com/penpot/penpot)<br>团队一起做设计，用开源平台<br>`设计 / 创意` | +21,718 | 59.5 | 61,998 | <a href="https://www.star-history.com/#penpot/penpot&Date"><img src="https://api.star-history.com/svg?repos=penpot/penpot&type=Date" width="260" alt="penpot/penpot 的星标历史曲线"></a> |
| 3 | [jgraph/drawio](https://github.com/jgraph/drawio)<br>画图和白板，一个编辑器搞定<br>`设计 / 创意` | +6,477 | 17.7 | 9,140 | <a href="https://www.star-history.com/#jgraph/drawio&Date"><img src="https://api.star-history.com/svg?repos=jgraph/drawio&type=Date" width="260" alt="jgraph/drawio 的星标历史曲线"></a> |
| 4 | [lucide-icons/lucide](https://github.com/lucide-icons/lucide)<br>一套图标风格统一，拿来就用<br>`设计 / 创意` | +6,247 | 17.1 | 25,474 | <a href="https://www.star-history.com/#lucide-icons/lucide&Date"><img src="https://api.star-history.com/svg?repos=lucide-icons/lucide&type=Date" width="260" alt="lucide-icons/lucide 的星标历史曲线"></a> |
| 5 | [saadeghi/daisyui](https://github.com/saadeghi/daisyui)<br>Tailwind 也有现成组件可挑<br>`设计 / 创意` | +4,226 | 11.6 | 42,734 | <a href="https://www.star-history.com/#saadeghi/daisyui&Date"><img src="https://api.star-history.com/svg?repos=saadeghi/daisyui&type=Date" width="260" alt="saadeghi/daisyui 的星标历史曲线"></a> |
| 6 | [phosphor-icons/homepage](https://github.com/phosphor-icons/homepage)<br>一整套灵活的图标，人人可用<br>`设计 / 创意` | +2,195 | 6.0 | 7,755 | <a href="https://www.star-history.com/#phosphor-icons/homepage&Date"><img src="https://api.star-history.com/svg?repos=phosphor-icons/homepage&type=Date" width="260" alt="phosphor-icons/homepage 的星标历史曲线"></a> |
| 7 | [airbnb/lottie-web](https://github.com/airbnb/lottie-web)<br>AE 做的动画，直接放进网页<br>`设计 / 创意` | +1,091 | 3.0 | 32,332 | <a href="https://www.star-history.com/#airbnb/lottie-web&Date"><img src="https://api.star-history.com/svg?repos=airbnb/lottie-web&type=Date" width="260" alt="airbnb/lottie-web 的星标历史曲线"></a> |
| 8 | [lottiefiles/lottie-ios](https://github.com/lottiefiles/lottie-ios)<br>AE 做的动画，直接放进 iOS<br>`设计 / 创意` | +1 | 0.0 | 43 | <a href="https://www.star-history.com/#lottiefiles/lottie-ios&Date"><img src="https://api.star-history.com/svg?repos=lottiefiles/lottie-ios&type=Date" width="260" alt="lottiefiles/lottie-ios 的星标历史曲线"></a> |

### 总星标数（历史累计）

| # | 项目 | 总星标 | 星标历史 |
|---|---|---:|---|
| 1 | [excalidraw/excalidraw](https://github.com/excalidraw/excalidraw)<br>打开就画，像在纸上随手画图<br>`设计 / 创意` | 135,054 | <a href="https://www.star-history.com/#excalidraw/excalidraw&Date"><img src="https://api.star-history.com/svg?repos=excalidraw/excalidraw&type=Date" width="260" alt="excalidraw/excalidraw 的星标历史曲线"></a> |
| 2 | [penpot/penpot](https://github.com/penpot/penpot)<br>团队一起做设计，用开源平台<br>`设计 / 创意` | 61,998 | <a href="https://www.star-history.com/#penpot/penpot&Date"><img src="https://api.star-history.com/svg?repos=penpot/penpot&type=Date" width="260" alt="penpot/penpot 的星标历史曲线"></a> |
| 3 | [saadeghi/daisyui](https://github.com/saadeghi/daisyui)<br>Tailwind 也有现成组件可挑<br>`设计 / 创意` | 42,734 | <a href="https://www.star-history.com/#saadeghi/daisyui&Date"><img src="https://api.star-history.com/svg?repos=saadeghi/daisyui&type=Date" width="260" alt="saadeghi/daisyui 的星标历史曲线"></a> |
| 4 | [airbnb/lottie-web](https://github.com/airbnb/lottie-web)<br>AE 做的动画，直接放进网页<br>`设计 / 创意` | 32,332 | <a href="https://www.star-history.com/#airbnb/lottie-web&Date"><img src="https://api.star-history.com/svg?repos=airbnb/lottie-web&type=Date" width="260" alt="airbnb/lottie-web 的星标历史曲线"></a> |
| 5 | [lucide-icons/lucide](https://github.com/lucide-icons/lucide)<br>一套图标风格统一，拿来就用<br>`设计 / 创意` | 25,474 | <a href="https://www.star-history.com/#lucide-icons/lucide&Date"><img src="https://api.star-history.com/svg?repos=lucide-icons/lucide&type=Date" width="260" alt="lucide-icons/lucide 的星标历史曲线"></a> |
| 6 | [jgraph/drawio](https://github.com/jgraph/drawio)<br>画图和白板，一个编辑器搞定<br>`设计 / 创意` | 9,140 | <a href="https://www.star-history.com/#jgraph/drawio&Date"><img src="https://api.star-history.com/svg?repos=jgraph/drawio&type=Date" width="260" alt="jgraph/drawio 的星标历史曲线"></a> |
| 7 | [phosphor-icons/homepage](https://github.com/phosphor-icons/homepage)<br>一整套灵活的图标，人人可用<br>`设计 / 创意` | 7,755 | <a href="https://www.star-history.com/#phosphor-icons/homepage&Date"><img src="https://api.star-history.com/svg?repos=phosphor-icons/homepage&type=Date" width="260" alt="phosphor-icons/homepage 的星标历史曲线"></a> |
| 8 | [lottiefiles/lottie-ios](https://github.com/lottiefiles/lottie-ios)<br>AE 做的动画，直接放进 iOS<br>`设计 / 创意` | 43 | <a href="https://www.star-history.com/#lottiefiles/lottie-ios&Date"><img src="https://api.star-history.com/svg?repos=lottiefiles/lottie-ios&type=Date" width="260" alt="lottiefiles/lottie-ios 的星标历史曲线"></a> |

## 数据

> 数据库、分析、ETL 与数据工程

### 最热新仓库（近 7 天内创建）

本次运行中没有符合条件的新仓库。

### 本周增长最快（近 7 天）

| # | 项目 | 新增星标 | 星标/天 | 总星标 | 星标历史 |
|---|---|---:|---:|---:|---|
| 1 | [duckdb/duckdb](https://github.com/duckdb/duckdb)<br>不搭数据库服务，也能跑 SQL 分析<br>`数据` | +209 | 29.9 | 42,754 | <a href="https://www.star-history.com/#duckdb/duckdb&Date"><img src="https://api.star-history.com/svg?repos=duckdb/duckdb&type=Date" width="260" alt="duckdb/duckdb 的星标历史曲线"></a> |
| 2 | [ClickHouse/ClickHouse](https://github.com/ClickHouse/ClickHouse)<br>大量数据实时分析，用开源的<br>`数据` | +127 | 18.1 | 50,721 | <a href="https://www.star-history.com/#ClickHouse/ClickHouse&Date"><img src="https://api.star-history.com/svg?repos=ClickHouse/ClickHouse&type=Date" width="260" alt="ClickHouse/ClickHouse 的星标历史曲线"></a> |
| 3 | [apache/superset](https://github.com/apache/superset)<br>数据看不懂，做成图就明白<br>`数据` | +105 | 15.0 | 75,392 | <a href="https://www.star-history.com/#apache/superset&Date"><img src="https://api.star-history.com/svg?repos=apache/superset&type=Date" width="260" alt="apache/superset 的星标历史曲线"></a> |
| 4 | [pola-rs/polars](https://github.com/pola-rs/polars)<br>表格数据处理快，不用干等<br>`数据` | +65 | 9.3 | 40,254 | <a href="https://www.star-history.com/#pola-rs/polars&Date"><img src="https://api.star-history.com/svg?repos=pola-rs/polars&type=Date" width="260" alt="pola-rs/polars 的星标历史曲线"></a> |
| 5 | [apache/kafka](https://github.com/apache/kafka)<br>系统之间的事件流，交给它来传<br>`数据` | +65 | 9.3 | 34,118 | <a href="https://www.star-history.com/#apache/kafka&Date"><img src="https://api.star-history.com/svg?repos=apache/kafka&type=Date" width="260" alt="apache/kafka 的星标历史曲线"></a> |
| 6 | [apache/arrow](https://github.com/apache/arrow)<br>不同语言之间，数据直接通用<br>`数据` | +49 | 7.0 | 17,272 | <a href="https://www.star-history.com/#apache/arrow&Date"><img src="https://api.star-history.com/svg?repos=apache/arrow&type=Date" width="260" alt="apache/arrow 的星标历史曲线"></a> |
| 7 | [dbt-labs/dbt-core](https://github.com/dbt-labs/dbt-core)<br>数据转换，照软件工程的做法来<br>`数据` | +31 | 4.4 | 14,112 | <a href="https://www.star-history.com/#dbt-labs/dbt-core&Date"><img src="https://api.star-history.com/svg?repos=dbt-labs/dbt-core&type=Date" width="260" alt="dbt-labs/dbt-core 的星标历史曲线"></a> |
| 8 | [jupyter/notebook](https://github.com/jupyter/notebook)<br>在网页里写代码，边写边看结果<br>`数据` | +5 | 0.7 | 13,459 | <a href="https://www.star-history.com/#jupyter/notebook&Date"><img src="https://api.star-history.com/svg?repos=jupyter/notebook&type=Date" width="260" alt="jupyter/notebook 的星标历史曲线"></a> |

### 本月增长最快（近 30 天）

| # | 项目 | 新增星标 | 星标/天 | 总星标 | 星标历史 |
|---|---|---:|---:|---:|---|
| 1 | [duckdb/duckdb](https://github.com/duckdb/duckdb)<br>不搭数据库服务，也能跑 SQL 分析<br>`数据` | +928 | 30.9 | 42,754 | <a href="https://www.star-history.com/#duckdb/duckdb&Date"><img src="https://api.star-history.com/svg?repos=duckdb/duckdb&type=Date" width="260" alt="duckdb/duckdb 的星标历史曲线"></a> |
| 2 | [ClickHouse/ClickHouse](https://github.com/ClickHouse/ClickHouse)<br>大量数据实时分析，用开源的<br>`数据` | +589 | 19.6 | 50,721 | <a href="https://www.star-history.com/#ClickHouse/ClickHouse&Date"><img src="https://api.star-history.com/svg?repos=ClickHouse/ClickHouse&type=Date" width="260" alt="ClickHouse/ClickHouse 的星标历史曲线"></a> |
| 3 | [apache/superset](https://github.com/apache/superset)<br>数据看不懂，做成图就明白<br>`数据` | +464 | 15.5 | 75,392 | <a href="https://www.star-history.com/#apache/superset&Date"><img src="https://api.star-history.com/svg?repos=apache/superset&type=Date" width="260" alt="apache/superset 的星标历史曲线"></a> |
| 4 | [pola-rs/polars](https://github.com/pola-rs/polars)<br>表格数据处理快，不用干等<br>`数据` | +383 | 12.8 | 40,254 | <a href="https://www.star-history.com/#pola-rs/polars&Date"><img src="https://api.star-history.com/svg?repos=pola-rs/polars&type=Date" width="260" alt="pola-rs/polars 的星标历史曲线"></a> |
| 5 | [apache/kafka](https://github.com/apache/kafka)<br>系统之间的事件流，交给它来传<br>`数据` | +293 | 9.8 | 34,118 | <a href="https://www.star-history.com/#apache/kafka&Date"><img src="https://api.star-history.com/svg?repos=apache/kafka&type=Date" width="260" alt="apache/kafka 的星标历史曲线"></a> |
| 6 | [dbt-labs/dbt-core](https://github.com/dbt-labs/dbt-core)<br>数据转换，照软件工程的做法来<br>`数据` | +169 | 5.6 | 14,112 | <a href="https://www.star-history.com/#dbt-labs/dbt-core&Date"><img src="https://api.star-history.com/svg?repos=dbt-labs/dbt-core&type=Date" width="260" alt="dbt-labs/dbt-core 的星标历史曲线"></a> |
| 7 | [apache/arrow](https://github.com/apache/arrow)<br>不同语言之间，数据直接通用<br>`数据` | +122 | 4.1 | 17,272 | <a href="https://www.star-history.com/#apache/arrow&Date"><img src="https://api.star-history.com/svg?repos=apache/arrow&type=Date" width="260" alt="apache/arrow 的星标历史曲线"></a> |
| 8 | [jupyter/notebook](https://github.com/jupyter/notebook)<br>在网页里写代码，边写边看结果<br>`数据` | +71 | 2.4 | 13,459 | <a href="https://www.star-history.com/#jupyter/notebook&Date"><img src="https://api.star-history.com/svg?repos=jupyter/notebook&type=Date" width="260" alt="jupyter/notebook 的星标历史曲线"></a> |

### 今年增长最快（近 365 天）

| # | 项目 | 新增星标 | 星标/天 | 总星标 | 星标历史 |
|---|---|---:|---:|---:|---|
| 1 | [duckdb/duckdb](https://github.com/duckdb/duckdb)<br>不搭数据库服务，也能跑 SQL 分析<br>`数据` | +9,360 | 25.6 | 42,754 | <a href="https://www.star-history.com/#duckdb/duckdb&Date"><img src="https://api.star-history.com/svg?repos=duckdb/duckdb&type=Date" width="260" alt="duckdb/duckdb 的星标历史曲线"></a> |
| 2 | [ClickHouse/ClickHouse](https://github.com/ClickHouse/ClickHouse)<br>大量数据实时分析，用开源的<br>`数据` | +7,629 | 20.9 | 50,721 | <a href="https://www.star-history.com/#ClickHouse/ClickHouse&Date"><img src="https://api.star-history.com/svg?repos=ClickHouse/ClickHouse&type=Date" width="260" alt="ClickHouse/ClickHouse 的星标历史曲线"></a> |
| 3 | [apache/superset](https://github.com/apache/superset)<br>数据看不懂，做成图就明白<br>`数据` | +7,448 | 20.4 | 75,392 | <a href="https://www.star-history.com/#apache/superset&Date"><img src="https://api.star-history.com/svg?repos=apache/superset&type=Date" width="260" alt="apache/superset 的星标历史曲线"></a> |
| 4 | [pola-rs/polars](https://github.com/pola-rs/polars)<br>表格数据处理快，不用干等<br>`数据` | +4,852 | 13.3 | 40,254 | <a href="https://www.star-history.com/#pola-rs/polars&Date"><img src="https://api.star-history.com/svg?repos=pola-rs/polars&type=Date" width="260" alt="pola-rs/polars 的星标历史曲线"></a> |
| 5 | [apache/kafka](https://github.com/apache/kafka)<br>系统之间的事件流，交给它来传<br>`数据` | +3,295 | 9.0 | 34,118 | <a href="https://www.star-history.com/#apache/kafka&Date"><img src="https://api.star-history.com/svg?repos=apache/kafka&type=Date" width="260" alt="apache/kafka 的星标历史曲线"></a> |
| 6 | [dbt-labs/dbt-core](https://github.com/dbt-labs/dbt-core)<br>数据转换，照软件工程的做法来<br>`数据` | +2,465 | 6.8 | 14,112 | <a href="https://www.star-history.com/#dbt-labs/dbt-core&Date"><img src="https://api.star-history.com/svg?repos=dbt-labs/dbt-core&type=Date" width="260" alt="dbt-labs/dbt-core 的星标历史曲线"></a> |
| 7 | [apache/arrow](https://github.com/apache/arrow)<br>不同语言之间，数据直接通用<br>`数据` | +1,316 | 3.6 | 17,272 | <a href="https://www.star-history.com/#apache/arrow&Date"><img src="https://api.star-history.com/svg?repos=apache/arrow&type=Date" width="260" alt="apache/arrow 的星标历史曲线"></a> |
| 8 | [jupyter/notebook](https://github.com/jupyter/notebook)<br>在网页里写代码，边写边看结果<br>`数据` | +907 | 2.5 | 13,459 | <a href="https://www.star-history.com/#jupyter/notebook&Date"><img src="https://api.star-history.com/svg?repos=jupyter/notebook&type=Date" width="260" alt="jupyter/notebook 的星标历史曲线"></a> |

### 总星标数（历史累计）

| # | 项目 | 总星标 | 星标历史 |
|---|---|---:|---|
| 1 | [apache/superset](https://github.com/apache/superset)<br>数据看不懂，做成图就明白<br>`数据` | 75,392 | <a href="https://www.star-history.com/#apache/superset&Date"><img src="https://api.star-history.com/svg?repos=apache/superset&type=Date" width="260" alt="apache/superset 的星标历史曲线"></a> |
| 2 | [ClickHouse/ClickHouse](https://github.com/ClickHouse/ClickHouse)<br>大量数据实时分析，用开源的<br>`数据` | 50,721 | <a href="https://www.star-history.com/#ClickHouse/ClickHouse&Date"><img src="https://api.star-history.com/svg?repos=ClickHouse/ClickHouse&type=Date" width="260" alt="ClickHouse/ClickHouse 的星标历史曲线"></a> |
| 3 | [duckdb/duckdb](https://github.com/duckdb/duckdb)<br>不搭数据库服务，也能跑 SQL 分析<br>`数据` | 42,754 | <a href="https://www.star-history.com/#duckdb/duckdb&Date"><img src="https://api.star-history.com/svg?repos=duckdb/duckdb&type=Date" width="260" alt="duckdb/duckdb 的星标历史曲线"></a> |
| 4 | [pola-rs/polars](https://github.com/pola-rs/polars)<br>表格数据处理快，不用干等<br>`数据` | 40,254 | <a href="https://www.star-history.com/#pola-rs/polars&Date"><img src="https://api.star-history.com/svg?repos=pola-rs/polars&type=Date" width="260" alt="pola-rs/polars 的星标历史曲线"></a> |
| 5 | [apache/kafka](https://github.com/apache/kafka)<br>系统之间的事件流，交给它来传<br>`数据` | 34,118 | <a href="https://www.star-history.com/#apache/kafka&Date"><img src="https://api.star-history.com/svg?repos=apache/kafka&type=Date" width="260" alt="apache/kafka 的星标历史曲线"></a> |
| 6 | [apache/arrow](https://github.com/apache/arrow)<br>不同语言之间，数据直接通用<br>`数据` | 17,272 | <a href="https://www.star-history.com/#apache/arrow&Date"><img src="https://api.star-history.com/svg?repos=apache/arrow&type=Date" width="260" alt="apache/arrow 的星标历史曲线"></a> |
| 7 | [dbt-labs/dbt-core](https://github.com/dbt-labs/dbt-core)<br>数据转换，照软件工程的做法来<br>`数据` | 14,112 | <a href="https://www.star-history.com/#dbt-labs/dbt-core&Date"><img src="https://api.star-history.com/svg?repos=dbt-labs/dbt-core&type=Date" width="260" alt="dbt-labs/dbt-core 的星标历史曲线"></a> |
| 8 | [jupyter/notebook](https://github.com/jupyter/notebook)<br>在网页里写代码，边写边看结果<br>`数据` | 13,459 | <a href="https://www.star-history.com/#jupyter/notebook&Date"><img src="https://api.star-history.com/svg?repos=jupyter/notebook&type=Date" width="260" alt="jupyter/notebook 的星标历史曲线"></a> |

---

如果它帮你省了时间，请给仓库点个星标，让更多人找得到。

如何引用：见 [CITATION.cff](CITATION.cff)。

数据怎么算和如何参与：[docs/HOW_IT_WORKS.zh-Hans.md](docs/HOW_IT_WORKS.zh-Hans.md)。新仓库规则：[docs/NEW_ARRIVALS.md](docs/NEW_ARRIVALS.md)。分类说明：[docs/CATEGORIES.md](docs/CATEGORIES.md)。提交改动：[CONTRIBUTING.md](CONTRIBUTING.md)。
