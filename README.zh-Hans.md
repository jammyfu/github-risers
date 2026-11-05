[English](README.md) | **简体中文** | [繁體中文](README.zh-Hant.md) | [日本語](README.ja.md) | [한국어](README.ko.md)

# GitHub 涨星榜 / GitHub Risers

<img src=".github/social-preview.png" alt="GitHub 涨星榜 / GitHub Risers" width="640">

[![MIT](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE) [![CI](https://github.com/jammyfu/github-risers/actions/workflows/ci.yml/badge.svg)](https://github.com/jammyfu/github-risers/actions/workflows/ci.yml) [![updated](https://img.shields.io/badge/dynamic/json?url=https%3A%2F%2Fraw.githubusercontent.com%2Fjammyfu%2Fgithub-risers%2Fmain%2Fdata%2Fstats.json&query=%24.today_utc&label=updated&color=brightgreen)](latest/rankings.zh-Hans.md)

按每天新增星标（而不是总星标）给 GitHub 仓库排名：AI 在前，其后是开发者工具、安全、Web / 前端、基础设施、设计 / 创意和数据；每天更新。

数据取自 2026-11-04 21:42（UTC）。每天更新。

[网站](https://jammyfu.github.io/github-risers/) · [运作方式](docs/HOW_IT_WORKS.zh-Hans.md) · [事实速查](docs/FACTS.md) · [历史榜单](rankings/README.zh-Hans.md) · [最新快照](latest/rankings.zh-Hans.md)

## 本期各类榜首

| 分类 | 新仓库第 1 名（7 天） | 本周第 1 名 | 本月第 1 名 | 今年第 1 名 | 总星标第 1 名 |
|---|---|---|---|---|---|
| **[人工智能](#人工智能)** ★ 主榜 | [KKKKhazix/agent-autoloop](https://github.com/KKKKhazix/agent-autoloop)<br>1,528/天 | [morluto/rea](https://github.com/morluto/rea)<br>4,321/天 | [morluto/rea](https://github.com/morluto/rea)<br>14,176/天 | [deepseek-ai/deepseek-harness](https://github.com/deepseek-ai/deepseek-harness)<br>3,273/天 | [morluto/rea](https://github.com/morluto/rea)<br>430,567 ★ |
| **[开发者工具](#开发者工具)** | [govijr/terminal-mac](https://github.com/govijr/terminal-mac)<br>815/天 | [zed-industries/zed](https://github.com/zed-industries/zed)<br>57.7/天 | [zed-industries/zed](https://github.com/zed-industries/zed)<br>54.5/天 | [zed-industries/zed](https://github.com/zed-industries/zed)<br>70.2/天 | [oven-sh/bun](https://github.com/oven-sh/bun)<br>96,546 ★ |
| **[安全](#安全)** | 无 | [projectdiscovery/nuclei](https://github.com/projectdiscovery/nuclei)<br>30.1/天 | [projectdiscovery/nuclei](https://github.com/projectdiscovery/nuclei)<br>30.7/天 | [aquasecurity/trivy](https://github.com/aquasecurity/trivy)<br>27.8/天 | [aquasecurity/trivy](https://github.com/aquasecurity/trivy)<br>38,984 ★ |
| **[Web / 前端](#web--前端)** | [mofan6/Moect](https://github.com/mofan6/Moect)<br>64.0/天 | [shadcn-ui/ui](https://github.com/shadcn-ui/ui)<br>89.1/天 | [shadcn-ui/ui](https://github.com/shadcn-ui/ui)<br>89.2/天 | [shadcn-ui/ui](https://github.com/shadcn-ui/ui)<br>83.2/天 | [facebook/react](https://github.com/facebook/react)<br>251,958 ★ |
| **[基础设施](#基础设施)** | 无 | [caddyserver/caddy](https://github.com/caddyserver/caddy)<br>40.0/天 | [caddyserver/caddy](https://github.com/caddyserver/caddy)<br>72.6/天 | [caddyserver/caddy](https://github.com/caddyserver/caddy)<br>32.7/天 | [kubernetes/kubernetes](https://github.com/kubernetes/kubernetes)<br>128,665 ★ |
| **[设计 / 创意](#设计--创意)** | [patch-gg/pixelfx](https://github.com/patch-gg/pixelfx)<br>830/天 | [excalidraw/excalidraw](https://github.com/excalidraw/excalidraw)<br>74.6/天 | [excalidraw/excalidraw](https://github.com/excalidraw/excalidraw)<br>67.9/天 | [excalidraw/excalidraw](https://github.com/excalidraw/excalidraw)<br>74.2/天 | [excalidraw/excalidraw](https://github.com/excalidraw/excalidraw)<br>135,169 ★ |
| **[数据](#数据)** | 无 | [duckdb/duckdb](https://github.com/duckdb/duckdb)<br>27.6/天 | [duckdb/duckdb](https://github.com/duckdb/duckdb)<br>32.1/天 | [duckdb/duckdb](https://github.com/duckdb/duckdb)<br>25.7/天 | [apache/superset](https://github.com/apache/superset)<br>75,409 ★ |

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
| 1 | [KKKKhazix/agent-autoloop](https://github.com/KKKKhazix/agent-autoloop)<br>不用一直盯梢，智能体拿不准时才找你 | 2026-11-03<br><sub>1.6 天</sub> | 2,398 | 1,527.7 | <a href="https://www.star-history.com/#KKKKhazix/agent-autoloop&Date"><img src="https://api.star-history.com/svg?repos=KKKKhazix/agent-autoloop&type=Date" width="260" alt="KKKKhazix/agent-autoloop 的星标历史曲线"></a> |
| 2 | [wangzan101/Mika](https://github.com/wangzan101/Mika)<br>手机琐事太多？让智能体替你操作应用 | 2026-10-29<br><sub>6.3 天</sub> | 6,596 | 1,047.4 | <a href="https://www.star-history.com/#wangzan101/Mika&Date"><img src="https://api.star-history.com/svg?repos=wangzan101/Mika&type=Date" width="260" alt="wangzan101/Mika 的星标历史曲线"></a> |
| 3 | [caru-ini/stack-diagram](https://github.com/caru-ini/stack-diagram)<br>一句话描述技术栈，自动生成架构图 | 2026-11-01<br><sub>3.7 天</sub> | 1,738 | 473.3 | <a href="https://www.star-history.com/#caru-ini/stack-diagram&Date"><img src="https://api.star-history.com/svg?repos=caru-ini/stack-diagram&type=Date" width="260" alt="caru-ini/stack-diagram 的星标历史曲线"></a> |
| 4 | [Balanov/uncut](https://github.com/Balanov/uncut)<br>告别静默截断，无损运行代码智能体 | 2026-11-01<br><sub>3.2 天</sub> | 600 | 188.5 | <a href="https://www.star-history.com/#Balanov/uncut&Date"><img src="https://api.star-history.com/svg?repos=Balanov/uncut&type=Date" width="260" alt="Balanov/uncut 的星标历史曲线"></a> |
| 5 | [NiazMorshed2007/reanimate](https://github.com/NiazMorshed2007/reanimate)<br>动效抄不像？逐帧还原并验证完全一致 | 2026-10-29<br><sub>6.6 天</sub> | 1,170 | 176.2 | <a href="https://www.star-history.com/#NiazMorshed2007/reanimate&Date"><img src="https://api.star-history.com/svg?repos=NiazMorshed2007/reanimate&type=Date" width="260" alt="NiazMorshed2007/reanimate 的星标历史曲线"></a> |
| 6 | [mhfed/vn-law-check](https://github.com/mhfed/vn-law-check)<br>检查网站是否符合越南法规要求 | 2026-11-02<br><sub>2.5 天</sub> | 408 | 162.3 | <a href="https://www.star-history.com/#mhfed/vn-law-check&Date"><img src="https://api.star-history.com/svg?repos=mhfed/vn-law-check&type=Date" width="260" alt="mhfed/vn-law-check 的星标历史曲线"></a> |
| 7 | [N1nEmAn/sapper-v2](https://github.com/N1nEmAn/sapper-v2)<br>安全测试太费劲？让 AI 军团自主排查 | 2026-10-30<br><sub>5.3 天</sub> | 798 | 151.4 | <a href="https://www.star-history.com/#N1nEmAn/sapper-v2&Date"><img src="https://api.star-history.com/svg?repos=N1nEmAn/sapper-v2&type=Date" width="260" alt="N1nEmAn/sapper-v2 的星标历史曲线"></a> |
| 8 | [JuneYaooo/rea-video](https://github.com/JuneYaooo/rea-video)<br>看不懂视频怎么做，逐镜拆解画面与剪辑 | 2026-10-29<br><sub>6.2 天</sub> | 860 | 138.1 | <a href="https://www.star-history.com/#JuneYaooo/rea-video&Date"><img src="https://api.star-history.com/svg?repos=JuneYaooo/rea-video&type=Date" width="260" alt="JuneYaooo/rea-video 的星标历史曲线"></a> |
| 9 | [Balanov/skein](https://github.com/Balanov/skein)<br>拦截超时过期任务，防止搞乱协同作业 | 2026-11-02<br><sub>1.9 天</sub> | 263 | 137.9 | <a href="https://www.star-history.com/#Balanov/skein&Date"><img src="https://api.star-history.com/svg?repos=Balanov/skein&type=Date" width="260" alt="Balanov/skein 的星标历史曲线"></a> |
| 10 | [zhanghao123vip/ai-manju-skills](https://github.com/zhanghao123vip/ai-manju-skills)<br>只有一个点子，也能生成全流程 AI 漫剧 | 2026-10-31<br><sub>4.8 天</sub> | 571 | 119.9 | <a href="https://www.star-history.com/#zhanghao123vip/ai-manju-skills&Date"><img src="https://api.star-history.com/svg?repos=zhanghao123vip/ai-manju-skills&type=Date" width="260" alt="zhanghao123vip/ai-manju-skills 的星标历史曲线"></a> |

### 本周增长最快（近 7 天）

| # | 项目 | 新增星标 | 星标/天 | 总星标 | 星标历史 |
|---|---|---:|---:|---:|---|
| 1 | [morluto/rea](https://github.com/morluto/rea)<br>让 AI 帮你克隆任何软件<br>`人工智能` | +30,249 | 4,321.3 | 430,567 | <a href="https://www.star-history.com/#morluto/rea&Date"><img src="https://api.star-history.com/svg?repos=morluto/rea&type=Date" width="260" alt="morluto/rea 的星标历史曲线"></a> |
| 2 | [thedotmack/claude-mem](https://github.com/thedotmack/claude-mem)<br>AI 不再忘记上次做到哪<br>`人工智能` | +8,615 | 1,230.7 | 112,745 | <a href="https://www.star-history.com/#thedotmack/claude-mem&Date"><img src="https://api.star-history.com/svg?repos=thedotmack/claude-mem&type=Date" width="260" alt="thedotmack/claude-mem 的星标历史曲线"></a> |
| 3 | [cloudflare/security-audit-skill](https://github.com/cloudflare/security-audit-skill)<br>AI 查代码漏洞，另一个 AI 逐条复核<br>`人工智能` | +7,917 | 1,131.0 | 59,126 | <a href="https://www.star-history.com/#cloudflare/security-audit-skill&Date"><img src="https://api.star-history.com/svg?repos=cloudflare/security-audit-skill&type=Date" width="260" alt="cloudflare/security-audit-skill 的星标历史曲线"></a> |
| 4 | [deepseek-ai/deepseek-harness](https://github.com/deepseek-ai/deepseek-harness)<br>想要什么智能体，用插件自己拼<br>`人工智能` | +7,911 | 1,130.1 | 272,453 | <a href="https://www.star-history.com/#deepseek-ai/deepseek-harness&Date"><img src="https://api.star-history.com/svg?repos=deepseek-ai/deepseek-harness&type=Date" width="260" alt="deepseek-ai/deepseek-harness 的星标历史曲线"></a> |
| 5 | [stablyai/orca](https://github.com/stablyai/orca)<br>几个 AI 一起写，谁好用一眼看出<br>`人工智能` | +6,729 | 961.3 | 115,377 | <a href="https://www.star-history.com/#stablyai/orca&Date"><img src="https://api.star-history.com/svg?repos=stablyai/orca&type=Date" width="260" alt="stablyai/orca 的星标历史曲线"></a> |
| 6 | [Leonxlnx/taste-skill](https://github.com/Leonxlnx/taste-skill)<br>别再让 AI 做出千篇一律的页面<br>`人工智能` | +5,952 | 850.3 | 109,992 | <a href="https://www.star-history.com/#Leonxlnx/taste-skill&Date"><img src="https://api.star-history.com/svg?repos=Leonxlnx/taste-skill&type=Date" width="260" alt="Leonxlnx/taste-skill 的星标历史曲线"></a> |
| 7 | [affaan-m/ECC](https://github.com/affaan-m/ECC)<br>给编程 AI 加记忆、技能和安全检查<br>`人工智能` | +5,896 | 842.3 | 297,183 | <a href="https://www.star-history.com/#affaan-m/ECC&Date"><img src="https://api.star-history.com/svg?repos=affaan-m/ECC&type=Date" width="260" alt="affaan-m/ECC 的星标历史曲线"></a> |
| 8 | [DietrichGebert/ponytail](https://github.com/DietrichGebert/ponytail)<br>让 AI 少写废代码，该写的写对<br>`人工智能` | +5,768 | 824.0 | 184,476 | <a href="https://www.star-history.com/#DietrichGebert/ponytail&Date"><img src="https://api.star-history.com/svg?repos=DietrichGebert/ponytail&type=Date" width="260" alt="DietrichGebert/ponytail 的星标历史曲线"></a> |
| 9 | [yetone/magpie](https://github.com/yetone/magpie)<br>编程 AI 换模型，额度用完自动续<br>`人工智能` | +5,420 | 774.3 | 29,713 | <a href="https://www.star-history.com/#yetone/magpie&Date"><img src="https://api.star-history.com/svg?repos=yetone/magpie&type=Date" width="260" alt="yetone/magpie 的星标历史曲线"></a> |
| 10 | [Graphify-Labs/graphify](https://github.com/Graphify-Labs/graphify)<br>大项目看不过来，先看这张地图<br>`人工智能` | +4,990 | 712.9 | 142,377 | <a href="https://www.star-history.com/#Graphify-Labs/graphify&Date"><img src="https://api.star-history.com/svg?repos=Graphify-Labs/graphify&type=Date" width="260" alt="Graphify-Labs/graphify 的星标历史曲线"></a> |

### 本月增长最快（近 30 天）

| # | 项目 | 新增星标 | 星标/天 | 总星标 | 星标历史 |
|---|---|---:|---:|---:|---|
| 1 | [morluto/rea](https://github.com/morluto/rea)<br>让 AI 帮你克隆任何软件<br>`人工智能` | +425,294 | 14,176.5 | 430,567 | <a href="https://www.star-history.com/#morluto/rea&Date"><img src="https://api.star-history.com/svg?repos=morluto/rea&type=Date" width="260" alt="morluto/rea 的星标历史曲线"></a> |
| 2 | [cloudflare/security-audit-skill](https://github.com/cloudflare/security-audit-skill)<br>AI 查代码漏洞，另一个 AI 逐条复核<br>`人工智能` | +34,178 | 1,139.3 | 59,126 | <a href="https://www.star-history.com/#cloudflare/security-audit-skill&Date"><img src="https://api.star-history.com/svg?repos=cloudflare/security-audit-skill&type=Date" width="260" alt="cloudflare/security-audit-skill 的星标历史曲线"></a> |
| 3 | [stablyai/orca](https://github.com/stablyai/orca)<br>几个 AI 一起写，谁好用一眼看出<br>`人工智能` | +30,287 | 1,009.6 | 115,377 | <a href="https://www.star-history.com/#stablyai/orca&Date"><img src="https://api.star-history.com/svg?repos=stablyai/orca&type=Date" width="260" alt="stablyai/orca 的星标历史曲线"></a> |
| 4 | [DietrichGebert/ponytail](https://github.com/DietrichGebert/ponytail)<br>让 AI 少写废代码，该写的写对<br>`人工智能` | +29,866 | 995.5 | 184,476 | <a href="https://www.star-history.com/#DietrichGebert/ponytail&Date"><img src="https://api.star-history.com/svg?repos=DietrichGebert/ponytail&type=Date" width="260" alt="DietrichGebert/ponytail 的星标历史曲线"></a> |
| 5 | [deepseek-ai/deepseek-harness](https://github.com/deepseek-ai/deepseek-harness)<br>想要什么智能体，用插件自己拼<br>`人工智能` | +29,609 | 987.0 | 272,453 | <a href="https://www.star-history.com/#deepseek-ai/deepseek-harness&Date"><img src="https://api.star-history.com/svg?repos=deepseek-ai/deepseek-harness&type=Date" width="260" alt="deepseek-ai/deepseek-harness 的星标历史曲线"></a> |
| 6 | [affaan-m/ECC](https://github.com/affaan-m/ECC)<br>给编程 AI 加记忆、技能和安全检查<br>`人工智能` | +25,205 | 840.2 | 297,183 | <a href="https://www.star-history.com/#affaan-m/ECC&Date"><img src="https://api.star-history.com/svg?repos=affaan-m/ECC&type=Date" width="260" alt="affaan-m/ECC 的星标历史曲线"></a> |
| 7 | [yetone/magpie](https://github.com/yetone/magpie)<br>编程 AI 换模型，额度用完自动续<br>`人工智能` | +24,512 | 817.1 | 29,713 | <a href="https://www.star-history.com/#yetone/magpie&Date"><img src="https://api.star-history.com/svg?repos=yetone/magpie&type=Date" width="260" alt="yetone/magpie 的星标历史曲线"></a> |
| 8 | [heygen-com/hyperframes](https://github.com/heygen-com/hyperframes)<br>不会剪辑，写网页一样就能出片<br>`人工智能` | +21,988 | 732.9 | 78,874 | <a href="https://www.star-history.com/#heygen-com/hyperframes&Date"><img src="https://api.star-history.com/svg?repos=heygen-com/hyperframes&type=Date" width="260" alt="heygen-com/hyperframes 的星标历史曲线"></a> |
| 9 | [Graphify-Labs/graphify](https://github.com/Graphify-Labs/graphify)<br>大项目看不过来，先看这张地图<br>`人工智能` | +18,964 | 632.1 | 142,377 | <a href="https://www.star-history.com/#Graphify-Labs/graphify&Date"><img src="https://api.star-history.com/svg?repos=Graphify-Labs/graphify&type=Date" width="260" alt="Graphify-Labs/graphify 的星标历史曲线"></a> |
| 10 | [Panniantong/Agent-Reach](https://github.com/Panniantong/Agent-Reach)<br>推特油管小红书，AI 都能帮你搜<br>`人工智能` | +17,879 | 596.0 | 108,780 | <a href="https://www.star-history.com/#Panniantong/Agent-Reach&Date"><img src="https://api.star-history.com/svg?repos=Panniantong/Agent-Reach&type=Date" width="260" alt="Panniantong/Agent-Reach 的星标历史曲线"></a> |

### 今年增长最快（近 365 天）

| # | 项目 | 新增星标 | 星标/天 | 总星标 | 星标历史 |
|---|---|---:|---:|---:|---|
| 1 | [deepseek-ai/deepseek-harness](https://github.com/deepseek-ai/deepseek-harness)<br>想要什么智能体，用插件自己拼<br>`人工智能` | +271,643 | 3,272.8 †<br><sub>÷83 天</sub> | 272,453 | <a href="https://www.star-history.com/#deepseek-ai/deepseek-harness&Date"><img src="https://api.star-history.com/svg?repos=deepseek-ai/deepseek-harness&type=Date" width="260" alt="deepseek-ai/deepseek-harness 的星标历史曲线"></a> |
| 2 | [morluto/rea](https://github.com/morluto/rea)<br>让 AI 帮你克隆任何软件<br>`人工智能` | +428,259 | 2,099.3 †<br><sub>÷204 天</sub> | 430,567 | <a href="https://www.star-history.com/#morluto/rea&Date"><img src="https://api.star-history.com/svg?repos=morluto/rea&type=Date" width="260" alt="morluto/rea 的星标历史曲线"></a> |
| 3 | [DietrichGebert/ponytail](https://github.com/DietrichGebert/ponytail)<br>让 AI 少写废代码，该写的写对<br>`人工智能` | +183,956 | 1,268.7 †<br><sub>÷145 天</sub> | 184,476 | <a href="https://www.star-history.com/#DietrichGebert/ponytail&Date"><img src="https://api.star-history.com/svg?repos=DietrichGebert/ponytail&type=Date" width="260" alt="DietrichGebert/ponytail 的星标历史曲线"></a> |
| 4 | [openclaw/openclaw](https://github.com/openclaw/openclaw)<br>能把事做完的 AI 助手，跑在自己设备上<br>`人工智能` | +393,830 | 1,141.5 †<br><sub>÷345 天</sub> | 393,916 | <a href="https://www.star-history.com/#openclaw/openclaw&Date"><img src="https://api.star-history.com/svg?repos=openclaw/openclaw&type=Date" width="260" alt="openclaw/openclaw 的星标历史曲线"></a> |
| 5 | [affaan-m/ECC](https://github.com/affaan-m/ECC)<br>给编程 AI 加记忆、技能和安全检查<br>`人工智能` | +296,703 | 1,023.1 †<br><sub>÷290 天</sub> | 297,183 | <a href="https://www.star-history.com/#affaan-m/ECC&Date"><img src="https://api.star-history.com/svg?repos=affaan-m/ECC&type=Date" width="260" alt="affaan-m/ECC 的星标历史曲线"></a> |
| 6 | [NousResearch/hermes-agent](https://github.com/NousResearch/hermes-agent)<br>越用越会干活的 AI 助手<br>`人工智能` | +260,301 | 713.2 | 260,536 | <a href="https://www.star-history.com/#NousResearch/hermes-agent&Date"><img src="https://api.star-history.com/svg?repos=NousResearch/hermes-agent&type=Date" width="260" alt="NousResearch/hermes-agent 的星标历史曲线"></a> |
| 7 | [yetone/magpie](https://github.com/yetone/magpie)<br>编程 AI 换模型，额度用完自动续<br>`人工智能` | +29,358 | 699.0 †<br><sub>÷42 天</sub> | 29,713 | <a href="https://www.star-history.com/#yetone/magpie&Date"><img src="https://api.star-history.com/svg?repos=yetone/magpie&type=Date" width="260" alt="yetone/magpie 的星标历史曲线"></a> |
| 8 | [Graphify-Labs/graphify](https://github.com/Graphify-Labs/graphify)<br>大项目看不过来，先看这张地图<br>`人工智能` | +141,989 | 660.4 †<br><sub>÷215 天</sub> | 142,377 | <a href="https://www.star-history.com/#Graphify-Labs/graphify&Date"><img src="https://api.star-history.com/svg?repos=Graphify-Labs/graphify&type=Date" width="260" alt="Graphify-Labs/graphify 的星标历史曲线"></a> |
| 9 | [anomalyco/opencode](https://github.com/anomalyco/opencode)<br>终端里，有个开源 AI 帮你写代码<br>`人工智能` | +194,584 | 533.1 | 224,582 | <a href="https://www.star-history.com/#anomalyco/opencode&Date"><img src="https://api.star-history.com/svg?repos=anomalyco/opencode&type=Date" width="260" alt="anomalyco/opencode 的星标历史曲线"></a> |
| 10 | [stablyai/orca](https://github.com/stablyai/orca)<br>几个 AI 一起写，谁好用一眼看出<br>`人工智能` | +114,808 | 494.9 †<br><sub>÷232 天</sub> | 115,377 | <a href="https://www.star-history.com/#stablyai/orca&Date"><img src="https://api.star-history.com/svg?repos=stablyai/orca&type=Date" width="260" alt="stablyai/orca 的星标历史曲线"></a> |

† 该仓库创建时间短于统计窗口，因此“星标/天”按仓库存在的天数（显示在数字下方）计算，而不是按完整窗口。

### 总星标数（历史累计）

| # | 项目 | 总星标 | 星标历史 |
|---|---|---:|---|
| 1 | [morluto/rea](https://github.com/morluto/rea)<br>让 AI 帮你克隆任何软件<br>`人工智能` | 430,567 | <a href="https://www.star-history.com/#morluto/rea&Date"><img src="https://api.star-history.com/svg?repos=morluto/rea&type=Date" width="260" alt="morluto/rea 的星标历史曲线"></a> |
| 2 | [openclaw/openclaw](https://github.com/openclaw/openclaw)<br>能把事做完的 AI 助手，跑在自己设备上<br>`人工智能` | 393,916 | <a href="https://www.star-history.com/#openclaw/openclaw&Date"><img src="https://api.star-history.com/svg?repos=openclaw/openclaw&type=Date" width="260" alt="openclaw/openclaw 的星标历史曲线"></a> |
| 3 | [affaan-m/ECC](https://github.com/affaan-m/ECC)<br>给编程 AI 加记忆、技能和安全检查<br>`人工智能` | 297,183 | <a href="https://www.star-history.com/#affaan-m/ECC&Date"><img src="https://api.star-history.com/svg?repos=affaan-m/ECC&type=Date" width="260" alt="affaan-m/ECC 的星标历史曲线"></a> |
| 4 | [deepseek-ai/deepseek-harness](https://github.com/deepseek-ai/deepseek-harness)<br>想要什么智能体，用插件自己拼<br>`人工智能` | 272,453 | <a href="https://www.star-history.com/#deepseek-ai/deepseek-harness&Date"><img src="https://api.star-history.com/svg?repos=deepseek-ai/deepseek-harness&type=Date" width="260" alt="deepseek-ai/deepseek-harness 的星标历史曲线"></a> |
| 5 | [NousResearch/hermes-agent](https://github.com/NousResearch/hermes-agent)<br>越用越会干活的 AI 助手<br>`人工智能` | 260,536 | <a href="https://www.star-history.com/#NousResearch/hermes-agent&Date"><img src="https://api.star-history.com/svg?repos=NousResearch/hermes-agent&type=Date" width="260" alt="NousResearch/hermes-agent 的星标历史曲线"></a> |
| 6 | [anomalyco/opencode](https://github.com/anomalyco/opencode)<br>终端里，有个开源 AI 帮你写代码<br>`人工智能` | 224,582 | <a href="https://www.star-history.com/#anomalyco/opencode&Date"><img src="https://api.star-history.com/svg?repos=anomalyco/opencode&type=Date" width="260" alt="anomalyco/opencode 的星标历史曲线"></a> |
| 7 | [anthropics/skills](https://github.com/anthropics/skills)<br>Claude 技能怎么写，照着官方学<br>`人工智能` | 187,391 | <a href="https://www.star-history.com/#anthropics/skills&Date"><img src="https://api.star-history.com/svg?repos=anthropics/skills&type=Date" width="260" alt="anthropics/skills 的星标历史曲线"></a> |
| 8 | [DietrichGebert/ponytail](https://github.com/DietrichGebert/ponytail)<br>让 AI 少写废代码，该写的写对<br>`人工智能` | 184,476 | <a href="https://www.star-history.com/#DietrichGebert/ponytail&Date"><img src="https://api.star-history.com/svg?repos=DietrichGebert/ponytail&type=Date" width="260" alt="DietrichGebert/ponytail 的星标历史曲线"></a> |
| 9 | [farion1231/cc-switch](https://github.com/farion1231/cc-switch)<br>换接口不用改配置，一键切<br>`人工智能` | 151,819 | <a href="https://www.star-history.com/#farion1231/cc-switch&Date"><img src="https://api.star-history.com/svg?repos=farion1231/cc-switch&type=Date" width="260" alt="farion1231/cc-switch 的星标历史曲线"></a> |
| 10 | [nextlevelbuilder/ui-ux-pro-max-skill](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill)<br>AI 做的界面，看着像专业设计<br>`人工智能` | 145,185 | <a href="https://www.star-history.com/#nextlevelbuilder/ui-ux-pro-max-skill&Date"><img src="https://api.star-history.com/svg?repos=nextlevelbuilder/ui-ux-pro-max-skill&type=Date" width="260" alt="nextlevelbuilder/ui-ux-pro-max-skill 的星标历史曲线"></a> |

## 开发者工具

> 命令行、编辑器、包管理、代码检查与构建工具

### 最热新仓库（近 7 天内创建）

| # | 项目 | 创建时间（UTC） | 总星标 | 星标/天 | 星标历史 |
|---|---|---|---:|---:|---|
| 1 | [govijr/terminal-mac](https://github.com/govijr/terminal-mac)<br>不想离开终端，在里面运行完整 macOS | 2026-11-03<br><sub>1.8 天</sub> | 1,437 | 814.8 | <a href="https://www.star-history.com/#govijr/terminal-mac&Date"><img src="https://api.star-history.com/svg?repos=govijr/terminal-mac&type=Date" width="260" alt="govijr/terminal-mac 的星标历史曲线"></a> |
| 2 | [Verlintas/NOIR](https://github.com/Verlintas/NOIR)<br>扫出安卓应用隐私泄露，并支持安全回滚 | 2026-10-31<br><sub>4.0 天</sub> | 2,003 | 500.1 | <a href="https://www.star-history.com/#Verlintas/NOIR&Date"><img src="https://api.star-history.com/svg?repos=Verlintas/NOIR&type=Date" width="260" alt="Verlintas/NOIR 的星标历史曲线"></a> |
| 3 | [AssassinCreator/steam-stash-value-report-card](https://github.com/AssassinCreator/steam-stash-value-report-card)<br>不知库存价值，在终端盘点并生成分享卡 | 2026-11-02<br><sub>2.9 天</sub> | 744 | 258.7 | <a href="https://www.star-history.com/#AssassinCreator/steam-stash-value-report-card&Date"><img src="https://api.star-history.com/svg?repos=AssassinCreator/steam-stash-value-report-card&type=Date" width="260" alt="AssassinCreator/steam-stash-value-report-card 的星标历史曲线"></a> |
| 4 | [UncensoredLabs/uncensored-ai-api](https://github.com/UncensoredLabs/uncensored-ai-api)<br>想接入模型？提供 API 与浏览器对话 | 2026-11-01<br><sub>3.0 天</sub> | 672 | 221.5 | <a href="https://www.star-history.com/#UncensoredLabs/uncensored-ai-api&Date"><img src="https://api.star-history.com/svg?repos=UncensoredLabs/uncensored-ai-api&type=Date" width="260" alt="UncensoredLabs/uncensored-ai-api 的星标历史曲线"></a> |
| 5 | [ChannelDivinerCast/VSCode-Extension-Helper](https://github.com/ChannelDivinerCast/VSCode-Extension-Helper)<br>扩展杂乱难管理，智能整理并优化性能 | 2026-11-04<br><sub>1.0 天</sub> | 163 | 163.0 | <a href="https://www.star-history.com/#ChannelDivinerCast/VSCode-Extension-Helper&Date"><img src="https://api.star-history.com/svg?repos=ChannelDivinerCast/VSCode-Extension-Helper&type=Date" width="260" alt="ChannelDivinerCast/VSCode-Extension-Helper 的星标历史曲线"></a> |
| 6 | [Straitbrashadow/minecraft-ai-mod-builder](https://github.com/Straitbrashadow/minecraft-ai-mod-builder)<br>不想手动搭建，在终端描述即可一步放置 | 2026-10-30<br><sub>5.0 天</sub> | 200 | 39.8 | <a href="https://www.star-history.com/#Straitbrashadow/minecraft-ai-mod-builder&Date"><img src="https://api.star-history.com/svg?repos=Straitbrashadow/minecraft-ai-mod-builder&type=Date" width="260" alt="Straitbrashadow/minecraft-ai-mod-builder 的星标历史曲线"></a> |
| 7 | [muaaz9329/cheap-ag](https://github.com/muaaz9329/cheap-ag)<br>套餐总碰上限？让便宜模型写代码 | 2026-10-28<br><sub>7.0 天</sub> | 270 | 38.7 | <a href="https://www.star-history.com/#muaaz9329/cheap-ag&Date"><img src="https://api.star-history.com/svg?repos=muaaz9329/cheap-ag&type=Date" width="260" alt="muaaz9329/cheap-ag 的星标历史曲线"></a> |
| 8 | [kyy-logs/code-review-skill](https://github.com/kyy-logs/code-review-skill)<br>代码审查有据可依，合并更有把握 | 2026-10-29<br><sub>6.6 天</sub> | 240 | 36.5 | <a href="https://www.star-history.com/#kyy-logs/code-review-skill&Date"><img src="https://api.star-history.com/svg?repos=kyy-logs/code-review-skill&type=Date" width="260" alt="kyy-logs/code-review-skill 的星标历史曲线"></a> |
| 9 | [DiplomatHearth/roblox-ai-place-diff](https://github.com/DiplomatHearth/roblox-ai-place-diff)<br>怕改坏场景，智能体修改先由你确认 | 2026-10-30<br><sub>5.0 天</sub> | 163 | 32.6 | <a href="https://www.star-history.com/#DiplomatHearth/roblox-ai-place-diff&Date"><img src="https://api.star-history.com/svg?repos=DiplomatHearth/roblox-ai-place-diff&type=Date" width="260" alt="DiplomatHearth/roblox-ai-place-diff 的星标历史曲线"></a> |
| 10 | [4yk5/Ghostman](https://github.com/4yk5/Ghostman)<br>厌倦笨重工具，纯键盘操控且完全本地 | 2026-10-30<br><sub>5.6 天</sub> | 110 | 19.7 | <a href="https://www.star-history.com/#4yk5/Ghostman&Date"><img src="https://api.star-history.com/svg?repos=4yk5/Ghostman&type=Date" width="260" alt="4yk5/Ghostman 的星标历史曲线"></a> |

### 本周增长最快（近 7 天）

| # | 项目 | 新增星标 | 星标/天 | 总星标 | 星标历史 |
|---|---|---:|---:|---:|---|
| 1 | [zed-industries/zed](https://github.com/zed-industries/zed)<br>打开就快，还能多人一起写代码<br>`开发者工具` | +404 | 57.7 | 92,690 | <a href="https://www.star-history.com/#zed-industries/zed&Date"><img src="https://api.star-history.com/svg?repos=zed-industries/zed&type=Date" width="260" alt="zed-industries/zed 的星标历史曲线"></a> |
| 2 | [astral-sh/uv](https://github.com/astral-sh/uv)<br>装 Python 包，不用再干等<br>`开发者工具` | +321 | 45.9 | 91,543 | <a href="https://www.star-history.com/#astral-sh/uv&Date"><img src="https://api.star-history.com/svg?repos=astral-sh/uv&type=Date" width="260" alt="astral-sh/uv 的星标历史曲线"></a> |
| 3 | [jdx/mise](https://github.com/jdx/mise)<br>开发工具、环境变量、任务，一个工具管<br>`开发者工具` | +283 | 40.4 | 35,772 | <a href="https://www.star-history.com/#jdx/mise&Date"><img src="https://api.star-history.com/svg?repos=jdx/mise&type=Date" width="260" alt="jdx/mise 的星标历史曲线"></a> |
| 4 | [BurntSushi/ripgrep](https://github.com/BurntSushi/ripgrep)<br>翻遍整个目录找文字，比 grep 快<br>`开发者工具` | +217 | 31.0 | 69,699 | <a href="https://www.star-history.com/#BurntSushi/ripgrep&Date"><img src="https://api.star-history.com/svg?repos=BurntSushi/ripgrep&type=Date" width="260" alt="BurntSushi/ripgrep 的星标历史曲线"></a> |
| 5 | [oven-sh/bun](https://github.com/oven-sh/bun)<br>运行打包测试装包，一个工具全包<br>`开发者工具` | +133 | 19.0 | 96,546 | <a href="https://www.star-history.com/#oven-sh/bun&Date"><img src="https://api.star-history.com/svg?repos=oven-sh/bun&type=Date" width="260" alt="oven-sh/bun 的星标历史曲线"></a> |
| 6 | [cli/cli](https://github.com/cli/cli)<br>不开网页，命令行里处理 GitHub<br>`开发者工具` | +99 | 14.1 | 46,873 | <a href="https://www.star-history.com/#cli/cli&Date"><img src="https://api.star-history.com/svg?repos=cli/cli&type=Date" width="260" alt="cli/cli 的星标历史曲线"></a> |
| 7 | [helix-editor/helix](https://github.com/helix-editor/helix)<br>语法高亮、语言服务都内置的文本编辑器<br>`开发者工具` | +96 | 13.7 | 46,784 | <a href="https://www.star-history.com/#helix-editor/helix&Date"><img src="https://api.star-history.com/svg?repos=helix-editor/helix&type=Date" width="260" alt="helix-editor/helix 的星标历史曲线"></a> |
| 8 | [biomejs/biome](https://github.com/biomejs/biome)<br>网页代码格式和检查，一个工具搞定<br>`开发者工具` | +42 | 6.0 | 26,049 | <a href="https://www.star-history.com/#biomejs/biome&Date"><img src="https://api.star-history.com/svg?repos=biomejs/biome&type=Date" width="260" alt="biomejs/biome 的星标历史曲线"></a> |

### 本月增长最快（近 30 天）

| # | 项目 | 新增星标 | 星标/天 | 总星标 | 星标历史 |
|---|---|---:|---:|---:|---|
| 1 | [zed-industries/zed](https://github.com/zed-industries/zed)<br>打开就快，还能多人一起写代码<br>`开发者工具` | +1,635 | 54.5 | 92,690 | <a href="https://www.star-history.com/#zed-industries/zed&Date"><img src="https://api.star-history.com/svg?repos=zed-industries/zed&type=Date" width="260" alt="zed-industries/zed 的星标历史曲线"></a> |
| 2 | [astral-sh/uv](https://github.com/astral-sh/uv)<br>装 Python 包，不用再干等<br>`开发者工具` | +1,319 | 44.0 | 91,543 | <a href="https://www.star-history.com/#astral-sh/uv&Date"><img src="https://api.star-history.com/svg?repos=astral-sh/uv&type=Date" width="260" alt="astral-sh/uv 的星标历史曲线"></a> |
| 3 | [jdx/mise](https://github.com/jdx/mise)<br>开发工具、环境变量、任务，一个工具管<br>`开发者工具` | +1,240 | 41.3 | 35,772 | <a href="https://www.star-history.com/#jdx/mise&Date"><img src="https://api.star-history.com/svg?repos=jdx/mise&type=Date" width="260" alt="jdx/mise 的星标历史曲线"></a> |
| 4 | [BurntSushi/ripgrep](https://github.com/BurntSushi/ripgrep)<br>翻遍整个目录找文字，比 grep 快<br>`开发者工具` | +993 | 33.1 | 69,699 | <a href="https://www.star-history.com/#BurntSushi/ripgrep&Date"><img src="https://api.star-history.com/svg?repos=BurntSushi/ripgrep&type=Date" width="260" alt="BurntSushi/ripgrep 的星标历史曲线"></a> |
| 5 | [oven-sh/bun](https://github.com/oven-sh/bun)<br>运行打包测试装包，一个工具全包<br>`开发者工具` | +701 | 23.4 | 96,546 | <a href="https://www.star-history.com/#oven-sh/bun&Date"><img src="https://api.star-history.com/svg?repos=oven-sh/bun&type=Date" width="260" alt="oven-sh/bun 的星标历史曲线"></a> |
| 6 | [helix-editor/helix](https://github.com/helix-editor/helix)<br>语法高亮、语言服务都内置的文本编辑器<br>`开发者工具` | +442 | 14.7 | 46,784 | <a href="https://www.star-history.com/#helix-editor/helix&Date"><img src="https://api.star-history.com/svg?repos=helix-editor/helix&type=Date" width="260" alt="helix-editor/helix 的星标历史曲线"></a> |
| 7 | [cli/cli](https://github.com/cli/cli)<br>不开网页，命令行里处理 GitHub<br>`开发者工具` | +425 | 14.2 | 46,873 | <a href="https://www.star-history.com/#cli/cli&Date"><img src="https://api.star-history.com/svg?repos=cli/cli&type=Date" width="260" alt="cli/cli 的星标历史曲线"></a> |
| 8 | [biomejs/biome](https://github.com/biomejs/biome)<br>网页代码格式和检查，一个工具搞定<br>`开发者工具` | +214 | 7.1 | 26,049 | <a href="https://www.star-history.com/#biomejs/biome&Date"><img src="https://api.star-history.com/svg?repos=biomejs/biome&type=Date" width="260" alt="biomejs/biome 的星标历史曲线"></a> |

### 今年增长最快（近 365 天）

| # | 项目 | 新增星标 | 星标/天 | 总星标 | 星标历史 |
|---|---|---:|---:|---:|---|
| 1 | [zed-industries/zed](https://github.com/zed-industries/zed)<br>打开就快，还能多人一起写代码<br>`开发者工具` | +25,641 | 70.2 | 92,690 | <a href="https://www.star-history.com/#zed-industries/zed&Date"><img src="https://api.star-history.com/svg?repos=zed-industries/zed&type=Date" width="260" alt="zed-industries/zed 的星标历史曲线"></a> |
| 2 | [astral-sh/uv](https://github.com/astral-sh/uv)<br>装 Python 包，不用再干等<br>`开发者工具` | +21,199 | 58.1 | 91,543 | <a href="https://www.star-history.com/#astral-sh/uv&Date"><img src="https://api.star-history.com/svg?repos=astral-sh/uv&type=Date" width="260" alt="astral-sh/uv 的星标历史曲线"></a> |
| 3 | [oven-sh/bun](https://github.com/oven-sh/bun)<br>运行打包测试装包，一个工具全包<br>`开发者工具` | +16,555 | 45.4 | 96,546 | <a href="https://www.star-history.com/#oven-sh/bun&Date"><img src="https://api.star-history.com/svg?repos=oven-sh/bun&type=Date" width="260" alt="oven-sh/bun 的星标历史曲线"></a> |
| 4 | [jdx/mise](https://github.com/jdx/mise)<br>开发工具、环境变量、任务，一个工具管<br>`开发者工具` | +15,085 | 41.3 | 35,772 | <a href="https://www.star-history.com/#jdx/mise&Date"><img src="https://api.star-history.com/svg?repos=jdx/mise&type=Date" width="260" alt="jdx/mise 的星标历史曲线"></a> |
| 5 | [BurntSushi/ripgrep](https://github.com/BurntSushi/ripgrep)<br>翻遍整个目录找文字，比 grep 快<br>`开发者工具` | +13,357 | 36.6 | 69,699 | <a href="https://www.star-history.com/#BurntSushi/ripgrep&Date"><img src="https://api.star-history.com/svg?repos=BurntSushi/ripgrep&type=Date" width="260" alt="BurntSushi/ripgrep 的星标历史曲线"></a> |
| 6 | [helix-editor/helix](https://github.com/helix-editor/helix)<br>语法高亮、语言服务都内置的文本编辑器<br>`开发者工具` | +6,650 | 18.2 | 46,784 | <a href="https://www.star-history.com/#helix-editor/helix&Date"><img src="https://api.star-history.com/svg?repos=helix-editor/helix&type=Date" width="260" alt="helix-editor/helix 的星标历史曲线"></a> |
| 7 | [cli/cli](https://github.com/cli/cli)<br>不开网页，命令行里处理 GitHub<br>`开发者工具` | +6,263 | 17.2 | 46,873 | <a href="https://www.star-history.com/#cli/cli&Date"><img src="https://api.star-history.com/svg?repos=cli/cli&type=Date" width="260" alt="cli/cli 的星标历史曲线"></a> |
| 8 | [biomejs/biome](https://github.com/biomejs/biome)<br>网页代码格式和检查，一个工具搞定<br>`开发者工具` | +4,556 | 12.5 | 26,049 | <a href="https://www.star-history.com/#biomejs/biome&Date"><img src="https://api.star-history.com/svg?repos=biomejs/biome&type=Date" width="260" alt="biomejs/biome 的星标历史曲线"></a> |

### 总星标数（历史累计）

| # | 项目 | 总星标 | 星标历史 |
|---|---|---:|---|
| 1 | [oven-sh/bun](https://github.com/oven-sh/bun)<br>运行打包测试装包，一个工具全包<br>`开发者工具` | 96,546 | <a href="https://www.star-history.com/#oven-sh/bun&Date"><img src="https://api.star-history.com/svg?repos=oven-sh/bun&type=Date" width="260" alt="oven-sh/bun 的星标历史曲线"></a> |
| 2 | [zed-industries/zed](https://github.com/zed-industries/zed)<br>打开就快，还能多人一起写代码<br>`开发者工具` | 92,690 | <a href="https://www.star-history.com/#zed-industries/zed&Date"><img src="https://api.star-history.com/svg?repos=zed-industries/zed&type=Date" width="260" alt="zed-industries/zed 的星标历史曲线"></a> |
| 3 | [astral-sh/uv](https://github.com/astral-sh/uv)<br>装 Python 包，不用再干等<br>`开发者工具` | 91,543 | <a href="https://www.star-history.com/#astral-sh/uv&Date"><img src="https://api.star-history.com/svg?repos=astral-sh/uv&type=Date" width="260" alt="astral-sh/uv 的星标历史曲线"></a> |
| 4 | [BurntSushi/ripgrep](https://github.com/BurntSushi/ripgrep)<br>翻遍整个目录找文字，比 grep 快<br>`开发者工具` | 69,699 | <a href="https://www.star-history.com/#BurntSushi/ripgrep&Date"><img src="https://api.star-history.com/svg?repos=BurntSushi/ripgrep&type=Date" width="260" alt="BurntSushi/ripgrep 的星标历史曲线"></a> |
| 5 | [cli/cli](https://github.com/cli/cli)<br>不开网页，命令行里处理 GitHub<br>`开发者工具` | 46,873 | <a href="https://www.star-history.com/#cli/cli&Date"><img src="https://api.star-history.com/svg?repos=cli/cli&type=Date" width="260" alt="cli/cli 的星标历史曲线"></a> |
| 6 | [helix-editor/helix](https://github.com/helix-editor/helix)<br>语法高亮、语言服务都内置的文本编辑器<br>`开发者工具` | 46,784 | <a href="https://www.star-history.com/#helix-editor/helix&Date"><img src="https://api.star-history.com/svg?repos=helix-editor/helix&type=Date" width="260" alt="helix-editor/helix 的星标历史曲线"></a> |
| 7 | [jdx/mise](https://github.com/jdx/mise)<br>开发工具、环境变量、任务，一个工具管<br>`开发者工具` | 35,772 | <a href="https://www.star-history.com/#jdx/mise&Date"><img src="https://api.star-history.com/svg?repos=jdx/mise&type=Date" width="260" alt="jdx/mise 的星标历史曲线"></a> |
| 8 | [biomejs/biome](https://github.com/biomejs/biome)<br>网页代码格式和检查，一个工具搞定<br>`开发者工具` | 26,049 | <a href="https://www.star-history.com/#biomejs/biome&Date"><img src="https://api.star-history.com/svg?repos=biomejs/biome&type=Date" width="260" alt="biomejs/biome 的星标历史曲线"></a> |

## 安全

> 漏洞扫描、静态分析、供应链与运行时安全

### 最热新仓库（近 7 天内创建）

本次运行中没有符合条件的新仓库。

### 本周增长最快（近 7 天）

| # | 项目 | 新增星标 | 星标/天 | 总星标 | 星标历史 |
|---|---|---:|---:|---:|---|
| 1 | [projectdiscovery/nuclei](https://github.com/projectdiscovery/nuclei)<br>写个模板，就能批量扫漏洞<br>`安全` | +211 | 30.1 | 32,588 | <a href="https://www.star-history.com/#projectdiscovery/nuclei&Date"><img src="https://api.star-history.com/svg?repos=projectdiscovery/nuclei&type=Date" width="260" alt="projectdiscovery/nuclei 的星标历史曲线"></a> |
| 2 | [aquasecurity/trivy](https://github.com/aquasecurity/trivy)<br>容器和代码仓，一次扫完安全问题<br>`安全` | +183 | 26.1 | 38,984 | <a href="https://www.star-history.com/#aquasecurity/trivy&Date"><img src="https://api.star-history.com/svg?repos=aquasecurity/trivy&type=Date" width="260" alt="aquasecurity/trivy 的星标历史曲线"></a> |
| 3 | [semgrep/semgrep](https://github.com/semgrep/semgrep)<br>代码里的问题，提交前先揪出来<br>`安全` | +131 | 18.7 | 17,457 | <a href="https://www.star-history.com/#semgrep/semgrep&Date"><img src="https://api.star-history.com/svg?repos=semgrep/semgrep&type=Date" width="260" alt="semgrep/semgrep 的星标历史曲线"></a> |
| 4 | [OWASP/CheatSheetSeries](https://github.com/OWASP/CheatSheetSeries)<br>应用安全怎么做，看这套速查表<br>`安全` | +115 | 16.4 | 33,885 | <a href="https://www.star-history.com/#OWASP/CheatSheetSeries&Date"><img src="https://api.star-history.com/svg?repos=OWASP/CheatSheetSeries&type=Date" width="260" alt="OWASP/CheatSheetSeries 的星标历史曲线"></a> |
| 5 | [google/osv-scanner](https://github.com/google/osv-scanner)<br>用的依赖安不安全，扫一下就知道<br>`安全` | +92 | 13.1 | 11,396 | <a href="https://www.star-history.com/#google/osv-scanner&Date"><img src="https://api.star-history.com/svg?repos=google/osv-scanner&type=Date" width="260" alt="google/osv-scanner 的星标历史曲线"></a> |
| 6 | [anchore/grype](https://github.com/anchore/grype)<br>容器镜像有没有漏洞，扫一下就知道<br>`安全` | +50 | 7.1 | 13,176 | <a href="https://www.star-history.com/#anchore/grype&Date"><img src="https://api.star-history.com/svg?repos=anchore/grype&type=Date" width="260" alt="anchore/grype 的星标历史曲线"></a> |
| 7 | [falcosecurity/falco](https://github.com/falcosecurity/falco)<br>云上有异常，第一时间知道<br>`安全` | +20 | 2.9 | 9,551 | <a href="https://www.star-history.com/#falcosecurity/falco&Date"><img src="https://api.star-history.com/svg?repos=falcosecurity/falco&type=Date" width="260" alt="falcosecurity/falco 的星标历史曲线"></a> |
| 8 | [securego/gosec](https://github.com/securego/gosec)<br>Go 代码的安全隐患，扫一遍就知道<br>`安全` | +9 | 1.3 | 8,999 | <a href="https://www.star-history.com/#securego/gosec&Date"><img src="https://api.star-history.com/svg?repos=securego/gosec&type=Date" width="260" alt="securego/gosec 的星标历史曲线"></a> |

### 本月增长最快（近 30 天）

| # | 项目 | 新增星标 | 星标/天 | 总星标 | 星标历史 |
|---|---|---:|---:|---:|---|
| 1 | [projectdiscovery/nuclei](https://github.com/projectdiscovery/nuclei)<br>写个模板，就能批量扫漏洞<br>`安全` | +922 | 30.7 | 32,588 | <a href="https://www.star-history.com/#projectdiscovery/nuclei&Date"><img src="https://api.star-history.com/svg?repos=projectdiscovery/nuclei&type=Date" width="260" alt="projectdiscovery/nuclei 的星标历史曲线"></a> |
| 2 | [aquasecurity/trivy](https://github.com/aquasecurity/trivy)<br>容器和代码仓，一次扫完安全问题<br>`安全` | +790 | 26.3 | 38,984 | <a href="https://www.star-history.com/#aquasecurity/trivy&Date"><img src="https://api.star-history.com/svg?repos=aquasecurity/trivy&type=Date" width="260" alt="aquasecurity/trivy 的星标历史曲线"></a> |
| 3 | [semgrep/semgrep](https://github.com/semgrep/semgrep)<br>代码里的问题，提交前先揪出来<br>`安全` | +590 | 19.7 | 17,457 | <a href="https://www.star-history.com/#semgrep/semgrep&Date"><img src="https://api.star-history.com/svg?repos=semgrep/semgrep&type=Date" width="260" alt="semgrep/semgrep 的星标历史曲线"></a> |
| 4 | [OWASP/CheatSheetSeries](https://github.com/OWASP/CheatSheetSeries)<br>应用安全怎么做，看这套速查表<br>`安全` | +487 | 16.2 | 33,885 | <a href="https://www.star-history.com/#OWASP/CheatSheetSeries&Date"><img src="https://api.star-history.com/svg?repos=OWASP/CheatSheetSeries&type=Date" width="260" alt="OWASP/CheatSheetSeries 的星标历史曲线"></a> |
| 5 | [google/osv-scanner](https://github.com/google/osv-scanner)<br>用的依赖安不安全，扫一下就知道<br>`安全` | +269 | 9.0 | 11,396 | <a href="https://www.star-history.com/#google/osv-scanner&Date"><img src="https://api.star-history.com/svg?repos=google/osv-scanner&type=Date" width="260" alt="google/osv-scanner 的星标历史曲线"></a> |
| 6 | [anchore/grype](https://github.com/anchore/grype)<br>容器镜像有没有漏洞，扫一下就知道<br>`安全` | +213 | 7.1 | 13,176 | <a href="https://www.star-history.com/#anchore/grype&Date"><img src="https://api.star-history.com/svg?repos=anchore/grype&type=Date" width="260" alt="anchore/grype 的星标历史曲线"></a> |
| 7 | [falcosecurity/falco](https://github.com/falcosecurity/falco)<br>云上有异常，第一时间知道<br>`安全` | +116 | 3.9 | 9,551 | <a href="https://www.star-history.com/#falcosecurity/falco&Date"><img src="https://api.star-history.com/svg?repos=falcosecurity/falco&type=Date" width="260" alt="falcosecurity/falco 的星标历史曲线"></a> |
| 8 | [securego/gosec](https://github.com/securego/gosec)<br>Go 代码的安全隐患，扫一遍就知道<br>`安全` | +43 | 1.4 | 8,999 | <a href="https://www.star-history.com/#securego/gosec&Date"><img src="https://api.star-history.com/svg?repos=securego/gosec&type=Date" width="260" alt="securego/gosec 的星标历史曲线"></a> |

### 今年增长最快（近 365 天）

| # | 项目 | 新增星标 | 星标/天 | 总星标 | 星标历史 |
|---|---|---:|---:|---:|---|
| 1 | [aquasecurity/trivy](https://github.com/aquasecurity/trivy)<br>容器和代码仓，一次扫完安全问题<br>`安全` | +10,129 | 27.8 | 38,984 | <a href="https://www.star-history.com/#aquasecurity/trivy&Date"><img src="https://api.star-history.com/svg?repos=aquasecurity/trivy&type=Date" width="260" alt="aquasecurity/trivy 的星标历史曲线"></a> |
| 2 | [projectdiscovery/nuclei](https://github.com/projectdiscovery/nuclei)<br>写个模板，就能批量扫漏洞<br>`安全` | +7,621 | 20.9 | 32,588 | <a href="https://www.star-history.com/#projectdiscovery/nuclei&Date"><img src="https://api.star-history.com/svg?repos=projectdiscovery/nuclei&type=Date" width="260" alt="projectdiscovery/nuclei 的星标历史曲线"></a> |
| 3 | [semgrep/semgrep](https://github.com/semgrep/semgrep)<br>代码里的问题，提交前先揪出来<br>`安全` | +4,398 | 12.0 | 17,457 | <a href="https://www.star-history.com/#semgrep/semgrep&Date"><img src="https://api.star-history.com/svg?repos=semgrep/semgrep&type=Date" width="260" alt="semgrep/semgrep 的星标历史曲线"></a> |
| 4 | [OWASP/CheatSheetSeries](https://github.com/OWASP/CheatSheetSeries)<br>应用安全怎么做，看这套速查表<br>`安全` | +3,541 | 9.7 | 33,885 | <a href="https://www.star-history.com/#OWASP/CheatSheetSeries&Date"><img src="https://api.star-history.com/svg?repos=OWASP/CheatSheetSeries&type=Date" width="260" alt="OWASP/CheatSheetSeries 的星标历史曲线"></a> |
| 5 | [google/osv-scanner](https://github.com/google/osv-scanner)<br>用的依赖安不安全，扫一下就知道<br>`安全` | +3,510 | 9.6 | 11,396 | <a href="https://www.star-history.com/#google/osv-scanner&Date"><img src="https://api.star-history.com/svg?repos=google/osv-scanner&type=Date" width="260" alt="google/osv-scanner 的星标历史曲线"></a> |
| 6 | [anchore/grype](https://github.com/anchore/grype)<br>容器镜像有没有漏洞，扫一下就知道<br>`安全` | +2,357 | 6.5 | 13,176 | <a href="https://www.star-history.com/#anchore/grype&Date"><img src="https://api.star-history.com/svg?repos=anchore/grype&type=Date" width="260" alt="anchore/grype 的星标历史曲线"></a> |
| 7 | [falcosecurity/falco](https://github.com/falcosecurity/falco)<br>云上有异常，第一时间知道<br>`安全` | +1,268 | 3.5 | 9,551 | <a href="https://www.star-history.com/#falcosecurity/falco&Date"><img src="https://api.star-history.com/svg?repos=falcosecurity/falco&type=Date" width="260" alt="falcosecurity/falco 的星标历史曲线"></a> |
| 8 | [securego/gosec](https://github.com/securego/gosec)<br>Go 代码的安全隐患，扫一遍就知道<br>`安全` | +562 | 1.5 | 8,999 | <a href="https://www.star-history.com/#securego/gosec&Date"><img src="https://api.star-history.com/svg?repos=securego/gosec&type=Date" width="260" alt="securego/gosec 的星标历史曲线"></a> |

### 总星标数（历史累计）

| # | 项目 | 总星标 | 星标历史 |
|---|---|---:|---|
| 1 | [aquasecurity/trivy](https://github.com/aquasecurity/trivy)<br>容器和代码仓，一次扫完安全问题<br>`安全` | 38,984 | <a href="https://www.star-history.com/#aquasecurity/trivy&Date"><img src="https://api.star-history.com/svg?repos=aquasecurity/trivy&type=Date" width="260" alt="aquasecurity/trivy 的星标历史曲线"></a> |
| 2 | [OWASP/CheatSheetSeries](https://github.com/OWASP/CheatSheetSeries)<br>应用安全怎么做，看这套速查表<br>`安全` | 33,885 | <a href="https://www.star-history.com/#OWASP/CheatSheetSeries&Date"><img src="https://api.star-history.com/svg?repos=OWASP/CheatSheetSeries&type=Date" width="260" alt="OWASP/CheatSheetSeries 的星标历史曲线"></a> |
| 3 | [projectdiscovery/nuclei](https://github.com/projectdiscovery/nuclei)<br>写个模板，就能批量扫漏洞<br>`安全` | 32,588 | <a href="https://www.star-history.com/#projectdiscovery/nuclei&Date"><img src="https://api.star-history.com/svg?repos=projectdiscovery/nuclei&type=Date" width="260" alt="projectdiscovery/nuclei 的星标历史曲线"></a> |
| 4 | [semgrep/semgrep](https://github.com/semgrep/semgrep)<br>代码里的问题，提交前先揪出来<br>`安全` | 17,457 | <a href="https://www.star-history.com/#semgrep/semgrep&Date"><img src="https://api.star-history.com/svg?repos=semgrep/semgrep&type=Date" width="260" alt="semgrep/semgrep 的星标历史曲线"></a> |
| 5 | [anchore/grype](https://github.com/anchore/grype)<br>容器镜像有没有漏洞，扫一下就知道<br>`安全` | 13,176 | <a href="https://www.star-history.com/#anchore/grype&Date"><img src="https://api.star-history.com/svg?repos=anchore/grype&type=Date" width="260" alt="anchore/grype 的星标历史曲线"></a> |
| 6 | [google/osv-scanner](https://github.com/google/osv-scanner)<br>用的依赖安不安全，扫一下就知道<br>`安全` | 11,396 | <a href="https://www.star-history.com/#google/osv-scanner&Date"><img src="https://api.star-history.com/svg?repos=google/osv-scanner&type=Date" width="260" alt="google/osv-scanner 的星标历史曲线"></a> |
| 7 | [falcosecurity/falco](https://github.com/falcosecurity/falco)<br>云上有异常，第一时间知道<br>`安全` | 9,551 | <a href="https://www.star-history.com/#falcosecurity/falco&Date"><img src="https://api.star-history.com/svg?repos=falcosecurity/falco&type=Date" width="260" alt="falcosecurity/falco 的星标历史曲线"></a> |
| 8 | [securego/gosec](https://github.com/securego/gosec)<br>Go 代码的安全隐患，扫一遍就知道<br>`安全` | 8,999 | <a href="https://www.star-history.com/#securego/gosec&Date"><img src="https://api.star-history.com/svg?repos=securego/gosec&type=Date" width="260" alt="securego/gosec 的星标历史曲线"></a> |

## Web / 前端

> 前端框架、UI 组件库、CSS 与浏览器工具

### 最热新仓库（近 7 天内创建）

| # | 项目 | 创建时间（UTC） | 总星标 | 星标/天 | 星标历史 |
|---|---|---|---:|---:|---|
| 1 | [mofan6/Moect](https://github.com/mofan6/Moect)<br>微信聊天记录想留存，离线导出与备份 | 2026-10-31<br><sub>4.5 天</sub> | 285 | 64.0 | <a href="https://www.star-history.com/#mofan6/Moect&Date"><img src="https://api.star-history.com/svg?repos=mofan6/Moect&type=Date" width="260" alt="mofan6/Moect 的星标历史曲线"></a> |
| 2 | [Lavagroabide/aegis-spreadwatch](https://github.com/Lavagroabide/aegis-spreadwatch)<br>CS2 买卖看不清，在设备上直接看净利润 | 2026-10-30<br><sub>4.9 天</sub> | 156 | 31.7 | <a href="https://www.star-history.com/#Lavagroabide/aegis-spreadwatch&Date"><img src="https://api.star-history.com/svg?repos=Lavagroabide/aegis-spreadwatch&type=Date" width="260" alt="Lavagroabide/aegis-spreadwatch 的星标历史曲线"></a> |
| 3 | [solderdatabraid29/aegis-vaultgrid](https://github.com/solderdatabraid29/aegis-vaultgrid)<br>不想登录看库存？在本地规划 CS2 订单 | 2026-10-30<br><sub>4.9 天</sub> | 139 | 28.3 | <a href="https://www.star-history.com/#solderdatabraid29/aegis-vaultgrid&Date"><img src="https://api.star-history.com/svg?repos=solderdatabraid29/aegis-vaultgrid&type=Date" width="260" alt="solderdatabraid29/aegis-vaultgrid 的星标历史曲线"></a> |
| 4 | [Townlanurture/aegis-skin-terminal](https://github.com/Townlanurture/aegis-skin-terminal)<br>CS2 交易怕算漏手续费，本地直接扫差价 | 2026-10-30<br><sub>4.9 天</sub> | 136 | 27.6 | <a href="https://www.star-history.com/#Townlanurture/aegis-skin-terminal&Date"><img src="https://api.star-history.com/svg?repos=Townlanurture/aegis-skin-terminal&type=Date" width="260" alt="Townlanurture/aegis-skin-terminal 的星标历史曲线"></a> |
| 5 | [SalmeronDevZone/azure-lab](https://github.com/SalmeronDevZone/azure-lab)<br>不用账号也不花钱，直接上手练习 Azure | 2026-10-30<br><sub>5.5 天</sub> | 117 | 21.1 | <a href="https://www.star-history.com/#SalmeronDevZone/azure-lab&Date"><img src="https://api.star-history.com/svg?repos=SalmeronDevZone/azure-lab&type=Date" width="260" alt="SalmeronDevZone/azure-lab 的星标历史曲线"></a> |
| 6 | [declarative-dragging/dragology](https://github.com/declarative-dragging/dragology)<br>网页 SVG 不好拖，声明一下就能拖动 | 2026-10-29<br><sub>6.8 天</sub> | 106 | 15.5 | <a href="https://www.star-history.com/#declarative-dragging/dragology&Date"><img src="https://api.star-history.com/svg?repos=declarative-dragging/dragology&type=Date" width="260" alt="declarative-dragging/dragology 的星标历史曲线"></a> |

### 本周增长最快（近 7 天）

| # | 项目 | 新增星标 | 星标/天 | 总星标 | 星标历史 |
|---|---|---:|---:|---:|---|
| 1 | [shadcn-ui/ui](https://github.com/shadcn-ui/ui)<br>好看的组件，代码归你，随便改<br>`Web / 前端` | +624 | 89.1 | 127,358 | <a href="https://www.star-history.com/#shadcn-ui/ui&Date"><img src="https://api.star-history.com/svg?repos=shadcn-ui/ui&type=Date" width="260" alt="shadcn-ui/ui 的星标历史曲线"></a> |
| 2 | [facebook/react](https://github.com/facebook/react)<br>网页和 App 界面，都能用它来搭<br>`Web / 前端` | +333 | 47.6 | 251,958 | <a href="https://www.star-history.com/#facebook/react&Date"><img src="https://api.star-history.com/svg?repos=facebook/react&type=Date" width="260" alt="facebook/react 的星标历史曲线"></a> |
| 3 | [withastro/astro](https://github.com/withastro/astro)<br>做内容型网站，页面输出更轻量<br>`Web / 前端` | +199 | 28.4 | 63,726 | <a href="https://www.star-history.com/#withastro/astro&Date"><img src="https://api.star-history.com/svg?repos=withastro/astro&type=Date" width="260" alt="withastro/astro 的星标历史曲线"></a> |
| 4 | [vercel/next.js](https://github.com/vercel/next.js)<br>用 React 做完整网站，从前到后<br>`Web / 前端` | +163 | 23.3 | 143,322 | <a href="https://www.star-history.com/#vercel/next.js&Date"><img src="https://api.star-history.com/svg?repos=vercel/next.js&type=Date" width="260" alt="vercel/next.js 的星标历史曲线"></a> |
| 5 | [tailwindlabs/tailwindcss](https://github.com/tailwindlabs/tailwindcss)<br>不写一大堆 CSS，也能做定制界面<br>`Web / 前端` | +102 | 14.6 | 98,065 | <a href="https://www.star-history.com/#tailwindlabs/tailwindcss&Date"><img src="https://api.star-history.com/svg?repos=tailwindlabs/tailwindcss&type=Date" width="260" alt="tailwindlabs/tailwindcss 的星标历史曲线"></a> |
| 6 | [sveltejs/svelte](https://github.com/sveltejs/svelte)<br>你写组件，编译器变出高效的网页代码<br>`Web / 前端` | +102 | 14.6 | 88,556 | <a href="https://www.star-history.com/#sveltejs/svelte&Date"><img src="https://api.star-history.com/svg?repos=sveltejs/svelte&type=Date" width="260" alt="sveltejs/svelte 的星标历史曲线"></a> |
| 7 | [vuejs/core](https://github.com/vuejs/core)<br>从一个小页面开始，用多少学多少<br>`Web / 前端` | +66 | 9.4 | 54,833 | <a href="https://www.star-history.com/#vuejs/core&Date"><img src="https://api.star-history.com/svg?repos=vuejs/core&type=Date" width="260" alt="vuejs/core 的星标历史曲线"></a> |
| 8 | [tanstack/query](https://github.com/tanstack/query)<br>请求数据和缓存，交给它管<br>`Web / 前端` | +49 | 7.0 | 50,525 | <a href="https://www.star-history.com/#tanstack/query&Date"><img src="https://api.star-history.com/svg?repos=tanstack/query&type=Date" width="260" alt="tanstack/query 的星标历史曲线"></a> |

### 本月增长最快（近 30 天）

| # | 项目 | 新增星标 | 星标/天 | 总星标 | 星标历史 |
|---|---|---:|---:|---:|---|
| 1 | [shadcn-ui/ui](https://github.com/shadcn-ui/ui)<br>好看的组件，代码归你，随便改<br>`Web / 前端` | +2,676 | 89.2 | 127,358 | <a href="https://www.star-history.com/#shadcn-ui/ui&Date"><img src="https://api.star-history.com/svg?repos=shadcn-ui/ui&type=Date" width="260" alt="shadcn-ui/ui 的星标历史曲线"></a> |
| 2 | [facebook/react](https://github.com/facebook/react)<br>网页和 App 界面，都能用它来搭<br>`Web / 前端` | +1,684 | 56.1 | 251,958 | <a href="https://www.star-history.com/#facebook/react&Date"><img src="https://api.star-history.com/svg?repos=facebook/react&type=Date" width="260" alt="facebook/react 的星标历史曲线"></a> |
| 3 | [withastro/astro](https://github.com/withastro/astro)<br>做内容型网站，页面输出更轻量<br>`Web / 前端` | +775 | 25.8 | 63,726 | <a href="https://www.star-history.com/#withastro/astro&Date"><img src="https://api.star-history.com/svg?repos=withastro/astro&type=Date" width="260" alt="withastro/astro 的星标历史曲线"></a> |
| 4 | [vercel/next.js](https://github.com/vercel/next.js)<br>用 React 做完整网站，从前到后<br>`Web / 前端` | +698 | 23.3 | 143,322 | <a href="https://www.star-history.com/#vercel/next.js&Date"><img src="https://api.star-history.com/svg?repos=vercel/next.js&type=Date" width="260" alt="vercel/next.js 的星标历史曲线"></a> |
| 5 | [sveltejs/svelte](https://github.com/sveltejs/svelte)<br>你写组件，编译器变出高效的网页代码<br>`Web / 前端` | +499 | 16.6 | 88,556 | <a href="https://www.star-history.com/#sveltejs/svelte&Date"><img src="https://api.star-history.com/svg?repos=sveltejs/svelte&type=Date" width="260" alt="sveltejs/svelte 的星标历史曲线"></a> |
| 6 | [tailwindlabs/tailwindcss](https://github.com/tailwindlabs/tailwindcss)<br>不写一大堆 CSS，也能做定制界面<br>`Web / 前端` | +486 | 16.2 | 98,065 | <a href="https://www.star-history.com/#tailwindlabs/tailwindcss&Date"><img src="https://api.star-history.com/svg?repos=tailwindlabs/tailwindcss&type=Date" width="260" alt="tailwindlabs/tailwindcss 的星标历史曲线"></a> |
| 7 | [vuejs/core](https://github.com/vuejs/core)<br>从一个小页面开始，用多少学多少<br>`Web / 前端` | +417 | 13.9 | 54,833 | <a href="https://www.star-history.com/#vuejs/core&Date"><img src="https://api.star-history.com/svg?repos=vuejs/core&type=Date" width="260" alt="vuejs/core 的星标历史曲线"></a> |
| 8 | [tanstack/query](https://github.com/tanstack/query)<br>请求数据和缓存，交给它管<br>`Web / 前端` | +215 | 7.2 | 50,525 | <a href="https://www.star-history.com/#tanstack/query&Date"><img src="https://api.star-history.com/svg?repos=tanstack/query&type=Date" width="260" alt="tanstack/query 的星标历史曲线"></a> |

### 今年增长最快（近 365 天）

| # | 项目 | 新增星标 | 星标/天 | 总星标 | 星标历史 |
|---|---|---:|---:|---:|---|
| 1 | [shadcn-ui/ui](https://github.com/shadcn-ui/ui)<br>好看的组件，代码归你，随便改<br>`Web / 前端` | +30,378 | 83.2 | 127,358 | <a href="https://www.star-history.com/#shadcn-ui/ui&Date"><img src="https://api.star-history.com/svg?repos=shadcn-ui/ui&type=Date" width="260" alt="shadcn-ui/ui 的星标历史曲线"></a> |
| 2 | [facebook/react](https://github.com/facebook/react)<br>网页和 App 界面，都能用它来搭<br>`Web / 前端` | +15,216 | 41.7 | 251,958 | <a href="https://www.star-history.com/#facebook/react&Date"><img src="https://api.star-history.com/svg?repos=facebook/react&type=Date" width="260" alt="facebook/react 的星标历史曲线"></a> |
| 3 | [withastro/astro](https://github.com/withastro/astro)<br>做内容型网站，页面输出更轻量<br>`Web / 前端` | +10,513 | 28.8 | 63,726 | <a href="https://www.star-history.com/#withastro/astro&Date"><img src="https://api.star-history.com/svg?repos=withastro/astro&type=Date" width="260" alt="withastro/astro 的星标历史曲线"></a> |
| 4 | [vercel/next.js](https://github.com/vercel/next.js)<br>用 React 做完整网站，从前到后<br>`Web / 前端` | +10,334 | 28.3 | 143,322 | <a href="https://www.star-history.com/#vercel/next.js&Date"><img src="https://api.star-history.com/svg?repos=vercel/next.js&type=Date" width="260" alt="vercel/next.js 的星标历史曲线"></a> |
| 5 | [tailwindlabs/tailwindcss](https://github.com/tailwindlabs/tailwindcss)<br>不写一大堆 CSS，也能做定制界面<br>`Web / 前端` | +8,520 | 23.3 | 98,065 | <a href="https://www.star-history.com/#tailwindlabs/tailwindcss&Date"><img src="https://api.star-history.com/svg?repos=tailwindlabs/tailwindcss&type=Date" width="260" alt="tailwindlabs/tailwindcss 的星标历史曲线"></a> |
| 6 | [sveltejs/svelte](https://github.com/sveltejs/svelte)<br>你写组件，编译器变出高效的网页代码<br>`Web / 前端` | +5,272 | 14.4 | 88,556 | <a href="https://www.star-history.com/#sveltejs/svelte&Date"><img src="https://api.star-history.com/svg?repos=sveltejs/svelte&type=Date" width="260" alt="sveltejs/svelte 的星标历史曲线"></a> |
| 7 | [tanstack/query](https://github.com/tanstack/query)<br>请求数据和缓存，交给它管<br>`Web / 前端` | +3,834 | 10.5 | 50,525 | <a href="https://www.star-history.com/#tanstack/query&Date"><img src="https://api.star-history.com/svg?repos=tanstack/query&type=Date" width="260" alt="tanstack/query 的星标历史曲线"></a> |
| 8 | [vuejs/core](https://github.com/vuejs/core)<br>从一个小页面开始，用多少学多少<br>`Web / 前端` | +3,616 | 9.9 | 54,833 | <a href="https://www.star-history.com/#vuejs/core&Date"><img src="https://api.star-history.com/svg?repos=vuejs/core&type=Date" width="260" alt="vuejs/core 的星标历史曲线"></a> |

### 总星标数（历史累计）

| # | 项目 | 总星标 | 星标历史 |
|---|---|---:|---|
| 1 | [facebook/react](https://github.com/facebook/react)<br>网页和 App 界面，都能用它来搭<br>`Web / 前端` | 251,958 | <a href="https://www.star-history.com/#facebook/react&Date"><img src="https://api.star-history.com/svg?repos=facebook/react&type=Date" width="260" alt="facebook/react 的星标历史曲线"></a> |
| 2 | [vercel/next.js](https://github.com/vercel/next.js)<br>用 React 做完整网站，从前到后<br>`Web / 前端` | 143,322 | <a href="https://www.star-history.com/#vercel/next.js&Date"><img src="https://api.star-history.com/svg?repos=vercel/next.js&type=Date" width="260" alt="vercel/next.js 的星标历史曲线"></a> |
| 3 | [shadcn-ui/ui](https://github.com/shadcn-ui/ui)<br>好看的组件，代码归你，随便改<br>`Web / 前端` | 127,358 | <a href="https://www.star-history.com/#shadcn-ui/ui&Date"><img src="https://api.star-history.com/svg?repos=shadcn-ui/ui&type=Date" width="260" alt="shadcn-ui/ui 的星标历史曲线"></a> |
| 4 | [tailwindlabs/tailwindcss](https://github.com/tailwindlabs/tailwindcss)<br>不写一大堆 CSS，也能做定制界面<br>`Web / 前端` | 98,065 | <a href="https://www.star-history.com/#tailwindlabs/tailwindcss&Date"><img src="https://api.star-history.com/svg?repos=tailwindlabs/tailwindcss&type=Date" width="260" alt="tailwindlabs/tailwindcss 的星标历史曲线"></a> |
| 5 | [sveltejs/svelte](https://github.com/sveltejs/svelte)<br>你写组件，编译器变出高效的网页代码<br>`Web / 前端` | 88,556 | <a href="https://www.star-history.com/#sveltejs/svelte&Date"><img src="https://api.star-history.com/svg?repos=sveltejs/svelte&type=Date" width="260" alt="sveltejs/svelte 的星标历史曲线"></a> |
| 6 | [withastro/astro](https://github.com/withastro/astro)<br>做内容型网站，页面输出更轻量<br>`Web / 前端` | 63,726 | <a href="https://www.star-history.com/#withastro/astro&Date"><img src="https://api.star-history.com/svg?repos=withastro/astro&type=Date" width="260" alt="withastro/astro 的星标历史曲线"></a> |
| 7 | [vuejs/core](https://github.com/vuejs/core)<br>从一个小页面开始，用多少学多少<br>`Web / 前端` | 54,833 | <a href="https://www.star-history.com/#vuejs/core&Date"><img src="https://api.star-history.com/svg?repos=vuejs/core&type=Date" width="260" alt="vuejs/core 的星标历史曲线"></a> |
| 8 | [tanstack/query](https://github.com/tanstack/query)<br>请求数据和缓存，交给它管<br>`Web / 前端` | 50,525 | <a href="https://www.star-history.com/#tanstack/query&Date"><img src="https://api.star-history.com/svg?repos=tanstack/query&type=Date" width="260" alt="tanstack/query 的星标历史曲线"></a> |

## 基础设施

> 容器、Kubernetes、云、网络与可观测性

### 最热新仓库（近 7 天内创建）

本次运行中没有符合条件的新仓库。

### 本周增长最快（近 7 天）

| # | 项目 | 新增星标 | 星标/天 | 总星标 | 星标历史 |
|---|---|---:|---:|---:|---|
| 1 | [caddyserver/caddy](https://github.com/caddyserver/caddy)<br>搭网站服务器，HTTPS 自动配好<br>`基础设施` | +280 | 40.0 | 78,766 | <a href="https://www.star-history.com/#caddyserver/caddy&Date"><img src="https://api.star-history.com/svg?repos=caddyserver/caddy&type=Date" width="260" alt="caddyserver/caddy 的星标历史曲线"></a> |
| 2 | [kubernetes/kubernetes](https://github.com/kubernetes/kubernetes)<br>容器多了，部署扩容交给它<br>`基础设施` | +207 | 29.6 | 128,665 | <a href="https://www.star-history.com/#kubernetes/kubernetes&Date"><img src="https://api.star-history.com/svg?repos=kubernetes/kubernetes&type=Date" width="260" alt="kubernetes/kubernetes 的星标历史曲线"></a> |
| 3 | [grafana/grafana](https://github.com/grafana/grafana)<br>指标日志链路，放进一个面板<br>`基础设施` | +169 | 24.1 | 77,690 | <a href="https://www.star-history.com/#grafana/grafana&Date"><img src="https://api.star-history.com/svg?repos=grafana/grafana&type=Date" width="260" alt="grafana/grafana 的星标历史曲线"></a> |
| 4 | [prometheus/prometheus](https://github.com/prometheus/prometheus)<br>系统出问题，告警先找到你<br>`基础设施` | +148 | 21.1 | 66,947 | <a href="https://www.star-history.com/#prometheus/prometheus&Date"><img src="https://api.star-history.com/svg?repos=prometheus/prometheus&type=Date" width="260" alt="prometheus/prometheus 的星标历史曲线"></a> |
| 5 | [docker/compose](https://github.com/docker/compose)<br>多个容器写进一个文件，一起跑<br>`基础设施` | +126 | 18.0 | 38,600 | <a href="https://www.star-history.com/#docker/compose&Date"><img src="https://api.star-history.com/svg?repos=docker/compose&type=Date" width="260" alt="docker/compose 的星标历史曲线"></a> |
| 6 | [traefik/traefik](https://github.com/traefik/traefik)<br>服务多了，流量自动分好<br>`基础设施` | +89 | 12.7 | 65,466 | <a href="https://www.star-history.com/#traefik/traefik&Date"><img src="https://api.star-history.com/svg?repos=traefik/traefik&type=Date" width="260" alt="traefik/traefik 的星标历史曲线"></a> |
| 7 | [hashicorp/terraform](https://github.com/hashicorp/terraform)<br>云资源写成代码，可审阅、可版本管理<br>`基础设施` | +85 | 12.1 | 50,137 | <a href="https://www.star-history.com/#hashicorp/terraform&Date"><img src="https://api.star-history.com/svg?repos=hashicorp/terraform&type=Date" width="260" alt="hashicorp/terraform 的星标历史曲线"></a> |
| 8 | [pulumi/pulumi](https://github.com/pulumi/pulumi)<br>用熟悉的编程语言管云资源<br>`基础设施` | +30 | 4.3 | 25,846 | <a href="https://www.star-history.com/#pulumi/pulumi&Date"><img src="https://api.star-history.com/svg?repos=pulumi/pulumi&type=Date" width="260" alt="pulumi/pulumi 的星标历史曲线"></a> |

### 本月增长最快（近 30 天）

| # | 项目 | 新增星标 | 星标/天 | 总星标 | 星标历史 |
|---|---|---:|---:|---:|---|
| 1 | [caddyserver/caddy](https://github.com/caddyserver/caddy)<br>搭网站服务器，HTTPS 自动配好<br>`基础设施` | +2,179 | 72.6 | 78,766 | <a href="https://www.star-history.com/#caddyserver/caddy&Date"><img src="https://api.star-history.com/svg?repos=caddyserver/caddy&type=Date" width="260" alt="caddyserver/caddy 的星标历史曲线"></a> |
| 2 | [kubernetes/kubernetes](https://github.com/kubernetes/kubernetes)<br>容器多了，部署扩容交给它<br>`基础设施` | +916 | 30.5 | 128,665 | <a href="https://www.star-history.com/#kubernetes/kubernetes&Date"><img src="https://api.star-history.com/svg?repos=kubernetes/kubernetes&type=Date" width="260" alt="kubernetes/kubernetes 的星标历史曲线"></a> |
| 3 | [grafana/grafana](https://github.com/grafana/grafana)<br>指标日志链路，放进一个面板<br>`基础设施` | +762 | 25.4 | 77,690 | <a href="https://www.star-history.com/#grafana/grafana&Date"><img src="https://api.star-history.com/svg?repos=grafana/grafana&type=Date" width="260" alt="grafana/grafana 的星标历史曲线"></a> |
| 4 | [prometheus/prometheus](https://github.com/prometheus/prometheus)<br>系统出问题，告警先找到你<br>`基础设施` | +713 | 23.8 | 66,947 | <a href="https://www.star-history.com/#prometheus/prometheus&Date"><img src="https://api.star-history.com/svg?repos=prometheus/prometheus&type=Date" width="260" alt="prometheus/prometheus 的星标历史曲线"></a> |
| 5 | [traefik/traefik](https://github.com/traefik/traefik)<br>服务多了，流量自动分好<br>`基础设施` | +489 | 16.3 | 65,466 | <a href="https://www.star-history.com/#traefik/traefik&Date"><img src="https://api.star-history.com/svg?repos=traefik/traefik&type=Date" width="260" alt="traefik/traefik 的星标历史曲线"></a> |
| 6 | [hashicorp/terraform](https://github.com/hashicorp/terraform)<br>云资源写成代码，可审阅、可版本管理<br>`基础设施` | +404 | 13.5 | 50,137 | <a href="https://www.star-history.com/#hashicorp/terraform&Date"><img src="https://api.star-history.com/svg?repos=hashicorp/terraform&type=Date" width="260" alt="hashicorp/terraform 的星标历史曲线"></a> |
| 7 | [docker/compose](https://github.com/docker/compose)<br>多个容器写进一个文件，一起跑<br>`基础设施` | +403 | 13.4 | 38,600 | <a href="https://www.star-history.com/#docker/compose&Date"><img src="https://api.star-history.com/svg?repos=docker/compose&type=Date" width="260" alt="docker/compose 的星标历史曲线"></a> |
| 8 | [pulumi/pulumi](https://github.com/pulumi/pulumi)<br>用熟悉的编程语言管云资源<br>`基础设施` | +131 | 4.4 | 25,846 | <a href="https://www.star-history.com/#pulumi/pulumi&Date"><img src="https://api.star-history.com/svg?repos=pulumi/pulumi&type=Date" width="260" alt="pulumi/pulumi 的星标历史曲线"></a> |

### 今年增长最快（近 365 天）

| # | 项目 | 新增星标 | 星标/天 | 总星标 | 星标历史 |
|---|---|---:|---:|---:|---|
| 1 | [caddyserver/caddy](https://github.com/caddyserver/caddy)<br>搭网站服务器，HTTPS 自动配好<br>`基础设施` | +11,942 | 32.7 | 78,766 | <a href="https://www.star-history.com/#caddyserver/caddy&Date"><img src="https://api.star-history.com/svg?repos=caddyserver/caddy&type=Date" width="260" alt="caddyserver/caddy 的星标历史曲线"></a> |
| 2 | [kubernetes/kubernetes](https://github.com/kubernetes/kubernetes)<br>容器多了，部署扩容交给它<br>`基础设施` | +11,599 | 31.8 | 128,665 | <a href="https://www.star-history.com/#kubernetes/kubernetes&Date"><img src="https://api.star-history.com/svg?repos=kubernetes/kubernetes&type=Date" width="260" alt="kubernetes/kubernetes 的星标历史曲线"></a> |
| 3 | [traefik/traefik](https://github.com/traefik/traefik)<br>服务多了，流量自动分好<br>`基础设施` | +8,699 | 23.8 | 65,466 | <a href="https://www.star-history.com/#traefik/traefik&Date"><img src="https://api.star-history.com/svg?repos=traefik/traefik&type=Date" width="260" alt="traefik/traefik 的星标历史曲线"></a> |
| 4 | [grafana/grafana](https://github.com/grafana/grafana)<br>指标日志链路，放进一个面板<br>`基础设施` | +7,891 | 21.6 | 77,690 | <a href="https://www.star-history.com/#grafana/grafana&Date"><img src="https://api.star-history.com/svg?repos=grafana/grafana&type=Date" width="260" alt="grafana/grafana 的星标历史曲线"></a> |
| 5 | [prometheus/prometheus](https://github.com/prometheus/prometheus)<br>系统出问题，告警先找到你<br>`基础设施` | +6,535 | 17.9 | 66,947 | <a href="https://www.star-history.com/#prometheus/prometheus&Date"><img src="https://api.star-history.com/svg?repos=prometheus/prometheus&type=Date" width="260" alt="prometheus/prometheus 的星标历史曲线"></a> |
| 6 | [hashicorp/terraform](https://github.com/hashicorp/terraform)<br>云资源写成代码，可审阅、可版本管理<br>`基础设施` | +3,771 | 10.3 | 50,137 | <a href="https://www.star-history.com/#hashicorp/terraform&Date"><img src="https://api.star-history.com/svg?repos=hashicorp/terraform&type=Date" width="260" alt="hashicorp/terraform 的星标历史曲线"></a> |
| 7 | [docker/compose](https://github.com/docker/compose)<br>多个容器写进一个文件，一起跑<br>`基础设施` | +2,639 | 7.2 | 38,600 | <a href="https://www.star-history.com/#docker/compose&Date"><img src="https://api.star-history.com/svg?repos=docker/compose&type=Date" width="260" alt="docker/compose 的星标历史曲线"></a> |
| 8 | [pulumi/pulumi](https://github.com/pulumi/pulumi)<br>用熟悉的编程语言管云资源<br>`基础设施` | +2,076 | 5.7 | 25,846 | <a href="https://www.star-history.com/#pulumi/pulumi&Date"><img src="https://api.star-history.com/svg?repos=pulumi/pulumi&type=Date" width="260" alt="pulumi/pulumi 的星标历史曲线"></a> |

### 总星标数（历史累计）

| # | 项目 | 总星标 | 星标历史 |
|---|---|---:|---|
| 1 | [kubernetes/kubernetes](https://github.com/kubernetes/kubernetes)<br>容器多了，部署扩容交给它<br>`基础设施` | 128,665 | <a href="https://www.star-history.com/#kubernetes/kubernetes&Date"><img src="https://api.star-history.com/svg?repos=kubernetes/kubernetes&type=Date" width="260" alt="kubernetes/kubernetes 的星标历史曲线"></a> |
| 2 | [caddyserver/caddy](https://github.com/caddyserver/caddy)<br>搭网站服务器，HTTPS 自动配好<br>`基础设施` | 78,766 | <a href="https://www.star-history.com/#caddyserver/caddy&Date"><img src="https://api.star-history.com/svg?repos=caddyserver/caddy&type=Date" width="260" alt="caddyserver/caddy 的星标历史曲线"></a> |
| 3 | [grafana/grafana](https://github.com/grafana/grafana)<br>指标日志链路，放进一个面板<br>`基础设施` | 77,690 | <a href="https://www.star-history.com/#grafana/grafana&Date"><img src="https://api.star-history.com/svg?repos=grafana/grafana&type=Date" width="260" alt="grafana/grafana 的星标历史曲线"></a> |
| 4 | [prometheus/prometheus](https://github.com/prometheus/prometheus)<br>系统出问题，告警先找到你<br>`基础设施` | 66,947 | <a href="https://www.star-history.com/#prometheus/prometheus&Date"><img src="https://api.star-history.com/svg?repos=prometheus/prometheus&type=Date" width="260" alt="prometheus/prometheus 的星标历史曲线"></a> |
| 5 | [traefik/traefik](https://github.com/traefik/traefik)<br>服务多了，流量自动分好<br>`基础设施` | 65,466 | <a href="https://www.star-history.com/#traefik/traefik&Date"><img src="https://api.star-history.com/svg?repos=traefik/traefik&type=Date" width="260" alt="traefik/traefik 的星标历史曲线"></a> |
| 6 | [hashicorp/terraform](https://github.com/hashicorp/terraform)<br>云资源写成代码，可审阅、可版本管理<br>`基础设施` | 50,137 | <a href="https://www.star-history.com/#hashicorp/terraform&Date"><img src="https://api.star-history.com/svg?repos=hashicorp/terraform&type=Date" width="260" alt="hashicorp/terraform 的星标历史曲线"></a> |
| 7 | [docker/compose](https://github.com/docker/compose)<br>多个容器写进一个文件，一起跑<br>`基础设施` | 38,600 | <a href="https://www.star-history.com/#docker/compose&Date"><img src="https://api.star-history.com/svg?repos=docker/compose&type=Date" width="260" alt="docker/compose 的星标历史曲线"></a> |
| 8 | [pulumi/pulumi](https://github.com/pulumi/pulumi)<br>用熟悉的编程语言管云资源<br>`基础设施` | 25,846 | <a href="https://www.star-history.com/#pulumi/pulumi&Date"><img src="https://api.star-history.com/svg?repos=pulumi/pulumi&type=Date" width="260" alt="pulumi/pulumi 的星标历史曲线"></a> |

## 设计 / 创意

> 设计系统、绘图、动画与创意工具

### 最热新仓库（近 7 天内创建）

| # | 项目 | 创建时间（UTC） | 总星标 | 星标/天 | 星标历史 |
|---|---|---|---:|---:|---|
| 1 | [patch-gg/pixelfx](https://github.com/patch-gg/pixelfx)<br>缺像素特效？244段简短代码直接套用 | 2026-10-30<br><sub>5.6 天</sub> | 4,668 | 830.0 | <a href="https://www.star-history.com/#patch-gg/pixelfx&Date"><img src="https://api.star-history.com/svg?repos=patch-gg/pixelfx&type=Date" width="260" alt="patch-gg/pixelfx 的星标历史曲线"></a> |
| 2 | [kevinraymond/florilegium](https://github.com/kevinraymond/florilegium)<br>页面太单调？画上代尔夫特蓝花卉页边 | 2026-10-30<br><sub>5.6 天</sub> | 1,426 | 255.6 | <a href="https://www.star-history.com/#kevinraymond/florilegium&Date"><img src="https://api.star-history.com/svg?repos=kevinraymond/florilegium&type=Date" width="260" alt="kevinraymond/florilegium 的星标历史曲线"></a> |
| 3 | [kubai087/kubai-icons](https://github.com/kubai087/kubai-icons)<br>以一致风格绘制动态图标的 Claude 技能，带有悬停动效或作为静态 SVG。 | 2026-11-03<br><sub>1.5 天</sub> | 161 | 107.8 | <a href="https://www.star-history.com/#kubai087/kubai-icons&Date"><img src="https://api.star-history.com/svg?repos=kubai087/kubai-icons&type=Date" width="260" alt="kubai087/kubai-icons 的星标历史曲线"></a> |
| 4 | [op7418/dsh-guizang-design](https://github.com/op7418/dsh-guizang-design)<br>排版全是 AI 味？用一套设计系统去掉 | 2026-10-30<br><sub>5.3 天</sub> | 432 | 81.7 | <a href="https://www.star-history.com/#op7418/dsh-guizang-design&Date"><img src="https://api.star-history.com/svg?repos=op7418/dsh-guizang-design&type=Date" width="260" alt="op7418/dsh-guizang-design 的星标历史曲线"></a> |
| 5 | [DominikScholz/open-bot-avatar](https://github.com/DominikScholz/open-bot-avatar)<br>给互动智能体轻松渲染虚拟形象 | 2026-11-02<br><sub>2.2 天</sub> | 156 | 71.1 | <a href="https://www.star-history.com/#DominikScholz/open-bot-avatar&Date"><img src="https://api.star-history.com/svg?repos=DominikScholz/open-bot-avatar&type=Date" width="260" alt="DominikScholz/open-bot-avatar 的星标历史曲线"></a> |
| 6 | [GuoZheng-de-BaBa/nursing-research-skills](https://github.com/GuoZheng-de-BaBa/nursing-research-skills)<br>护理科研太繁琐，AI 技能帮你做 | 2026-10-30<br><sub>5.3 天</sub> | 257 | 48.4 | <a href="https://www.star-history.com/#GuoZheng-de-BaBa/nursing-research-skills&Date"><img src="https://api.star-history.com/svg?repos=GuoZheng-de-BaBa/nursing-research-skills&type=Date" width="260" alt="GuoZheng-de-BaBa/nursing-research-skills 的星标历史曲线"></a> |
| 7 | [Akillll-DuoHe/fy-code-animation](https://github.com/Akillll-DuoHe/fy-code-animation)<br>代码动画难做？文案与声音直接生成 | 2026-10-30<br><sub>5.5 天</sub> | 195 | 35.5 | <a href="https://www.star-history.com/#Akillll-DuoHe/fy-code-animation&Date"><img src="https://api.star-history.com/svg?repos=Akillll-DuoHe/fy-code-animation&type=Date" width="260" alt="Akillll-DuoHe/fy-code-animation 的星标历史曲线"></a> |
| 8 | [ersinkoc/AI-Video-Factory](https://github.com/ersinkoc/AI-Video-Factory)<br>给一个主题，智能体做成多语言视频 | 2026-10-29<br><sub>6.0 天</sub> | 185 | 31.0 | <a href="https://www.star-history.com/#ersinkoc/AI-Video-Factory&Date"><img src="https://api.star-history.com/svg?repos=ersinkoc/AI-Video-Factory&type=Date" width="260" alt="ersinkoc/AI-Video-Factory 的星标历史曲线"></a> |

### 本周增长最快（近 7 天）

| # | 项目 | 新增星标 | 星标/天 | 总星标 | 星标历史 |
|---|---|---:|---:|---:|---|
| 1 | [excalidraw/excalidraw](https://github.com/excalidraw/excalidraw)<br>打开就画，像在纸上随手画图<br>`设计 / 创意` | +522 | 74.6 | 135,169 | <a href="https://www.star-history.com/#excalidraw/excalidraw&Date"><img src="https://api.star-history.com/svg?repos=excalidraw/excalidraw&type=Date" width="260" alt="excalidraw/excalidraw 的星标历史曲线"></a> |
| 2 | [penpot/penpot](https://github.com/penpot/penpot)<br>团队一起做设计，用开源平台<br>`设计 / 创意` | +316 | 45.1 | 62,070 | <a href="https://www.star-history.com/#penpot/penpot&Date"><img src="https://api.star-history.com/svg?repos=penpot/penpot&type=Date" width="260" alt="penpot/penpot 的星标历史曲线"></a> |
| 3 | [lucide-icons/lucide](https://github.com/lucide-icons/lucide)<br>一套图标风格统一，拿来就用<br>`设计 / 创意` | +204 | 29.1 | 25,570 | <a href="https://www.star-history.com/#lucide-icons/lucide&Date"><img src="https://api.star-history.com/svg?repos=lucide-icons/lucide&type=Date" width="260" alt="lucide-icons/lucide 的星标历史曲线"></a> |
| 4 | [jgraph/drawio](https://github.com/jgraph/drawio)<br>画图和白板，一个编辑器搞定<br>`设计 / 创意` | +148 | 21.1 | 9,182 | <a href="https://www.star-history.com/#jgraph/drawio&Date"><img src="https://api.star-history.com/svg?repos=jgraph/drawio&type=Date" width="260" alt="jgraph/drawio 的星标历史曲线"></a> |
| 5 | [saadeghi/daisyui](https://github.com/saadeghi/daisyui)<br>Tailwind 也有现成组件可挑<br>`设计 / 创意` | +68 | 9.7 | 42,737 | <a href="https://www.star-history.com/#saadeghi/daisyui&Date"><img src="https://api.star-history.com/svg?repos=saadeghi/daisyui&type=Date" width="260" alt="saadeghi/daisyui 的星标历史曲线"></a> |
| 6 | [airbnb/lottie-web](https://github.com/airbnb/lottie-web)<br>AE 做的动画，直接放进网页<br>`设计 / 创意` | +66 | 9.4 | 32,357 | <a href="https://www.star-history.com/#airbnb/lottie-web&Date"><img src="https://api.star-history.com/svg?repos=airbnb/lottie-web&type=Date" width="260" alt="airbnb/lottie-web 的星标历史曲线"></a> |
| 7 | [phosphor-icons/homepage](https://github.com/phosphor-icons/homepage)<br>一整套灵活的图标，人人可用<br>`设计 / 创意` | +37 | 5.3 | 7,765 | <a href="https://www.star-history.com/#phosphor-icons/homepage&Date"><img src="https://api.star-history.com/svg?repos=phosphor-icons/homepage&type=Date" width="260" alt="phosphor-icons/homepage 的星标历史曲线"></a> |
| 8 | [lottiefiles/lottie-ios](https://github.com/lottiefiles/lottie-ios)<br>AE 做的动画，直接放进 iOS<br>`设计 / 创意` | +0 | 0.0 | 43 | <a href="https://www.star-history.com/#lottiefiles/lottie-ios&Date"><img src="https://api.star-history.com/svg?repos=lottiefiles/lottie-ios&type=Date" width="260" alt="lottiefiles/lottie-ios 的星标历史曲线"></a> |

### 本月增长最快（近 30 天）

| # | 项目 | 新增星标 | 星标/天 | 总星标 | 星标历史 |
|---|---|---:|---:|---:|---|
| 1 | [excalidraw/excalidraw](https://github.com/excalidraw/excalidraw)<br>打开就画，像在纸上随手画图<br>`设计 / 创意` | +2,036 | 67.9 | 135,169 | <a href="https://www.star-history.com/#excalidraw/excalidraw&Date"><img src="https://api.star-history.com/svg?repos=excalidraw/excalidraw&type=Date" width="260" alt="excalidraw/excalidraw 的星标历史曲线"></a> |
| 2 | [penpot/penpot](https://github.com/penpot/penpot)<br>团队一起做设计，用开源平台<br>`设计 / 创意` | +1,497 | 49.9 | 62,070 | <a href="https://www.star-history.com/#penpot/penpot&Date"><img src="https://api.star-history.com/svg?repos=penpot/penpot&type=Date" width="260" alt="penpot/penpot 的星标历史曲线"></a> |
| 3 | [lucide-icons/lucide](https://github.com/lucide-icons/lucide)<br>一套图标风格统一，拿来就用<br>`设计 / 创意` | +737 | 24.6 | 25,570 | <a href="https://www.star-history.com/#lucide-icons/lucide&Date"><img src="https://api.star-history.com/svg?repos=lucide-icons/lucide&type=Date" width="260" alt="lucide-icons/lucide 的星标历史曲线"></a> |
| 4 | [jgraph/drawio](https://github.com/jgraph/drawio)<br>画图和白板，一个编辑器搞定<br>`设计 / 创意` | +627 | 20.9 | 9,182 | <a href="https://www.star-history.com/#jgraph/drawio&Date"><img src="https://api.star-history.com/svg?repos=jgraph/drawio&type=Date" width="260" alt="jgraph/drawio 的星标历史曲线"></a> |
| 5 | [saadeghi/daisyui](https://github.com/saadeghi/daisyui)<br>Tailwind 也有现成组件可挑<br>`设计 / 创意` | +279 | 9.3 | 42,737 | <a href="https://www.star-history.com/#saadeghi/daisyui&Date"><img src="https://api.star-history.com/svg?repos=saadeghi/daisyui&type=Date" width="260" alt="saadeghi/daisyui 的星标历史曲线"></a> |
| 6 | [airbnb/lottie-web](https://github.com/airbnb/lottie-web)<br>AE 做的动画，直接放进网页<br>`设计 / 创意` | +234 | 7.8 | 32,357 | <a href="https://www.star-history.com/#airbnb/lottie-web&Date"><img src="https://api.star-history.com/svg?repos=airbnb/lottie-web&type=Date" width="260" alt="airbnb/lottie-web 的星标历史曲线"></a> |
| 7 | [phosphor-icons/homepage](https://github.com/phosphor-icons/homepage)<br>一整套灵活的图标，人人可用<br>`设计 / 创意` | +181 | 6.0 | 7,765 | <a href="https://www.star-history.com/#phosphor-icons/homepage&Date"><img src="https://api.star-history.com/svg?repos=phosphor-icons/homepage&type=Date" width="260" alt="phosphor-icons/homepage 的星标历史曲线"></a> |
| 8 | [lottiefiles/lottie-ios](https://github.com/lottiefiles/lottie-ios)<br>AE 做的动画，直接放进 iOS<br>`设计 / 创意` | +0 | 0.0 | 43 | <a href="https://www.star-history.com/#lottiefiles/lottie-ios&Date"><img src="https://api.star-history.com/svg?repos=lottiefiles/lottie-ios&type=Date" width="260" alt="lottiefiles/lottie-ios 的星标历史曲线"></a> |

### 今年增长最快（近 365 天）

| # | 项目 | 新增星标 | 星标/天 | 总星标 | 星标历史 |
|---|---|---:|---:|---:|---|
| 1 | [excalidraw/excalidraw](https://github.com/excalidraw/excalidraw)<br>打开就画，像在纸上随手画图<br>`设计 / 创意` | +27,077 | 74.2 | 135,169 | <a href="https://www.star-history.com/#excalidraw/excalidraw&Date"><img src="https://api.star-history.com/svg?repos=excalidraw/excalidraw&type=Date" width="260" alt="excalidraw/excalidraw 的星标历史曲线"></a> |
| 2 | [penpot/penpot](https://github.com/penpot/penpot)<br>团队一起做设计，用开源平台<br>`设计 / 创意` | +21,778 | 59.7 | 62,070 | <a href="https://www.star-history.com/#penpot/penpot&Date"><img src="https://api.star-history.com/svg?repos=penpot/penpot&type=Date" width="260" alt="penpot/penpot 的星标历史曲线"></a> |
| 3 | [jgraph/drawio](https://github.com/jgraph/drawio)<br>画图和白板，一个编辑器搞定<br>`设计 / 创意` | +6,511 | 17.8 | 9,182 | <a href="https://www.star-history.com/#jgraph/drawio&Date"><img src="https://api.star-history.com/svg?repos=jgraph/drawio&type=Date" width="260" alt="jgraph/drawio 的星标历史曲线"></a> |
| 4 | [lucide-icons/lucide](https://github.com/lucide-icons/lucide)<br>一套图标风格统一，拿来就用<br>`设计 / 创意` | +6,312 | 17.3 | 25,570 | <a href="https://www.star-history.com/#lucide-icons/lucide&Date"><img src="https://api.star-history.com/svg?repos=lucide-icons/lucide&type=Date" width="260" alt="lucide-icons/lucide 的星标历史曲线"></a> |
| 5 | [saadeghi/daisyui](https://github.com/saadeghi/daisyui)<br>Tailwind 也有现成组件可挑<br>`设计 / 创意` | +4,223 | 11.6 | 42,737 | <a href="https://www.star-history.com/#saadeghi/daisyui&Date"><img src="https://api.star-history.com/svg?repos=saadeghi/daisyui&type=Date" width="260" alt="saadeghi/daisyui 的星标历史曲线"></a> |
| 6 | [phosphor-icons/homepage](https://github.com/phosphor-icons/homepage)<br>一整套灵活的图标，人人可用<br>`设计 / 创意` | +2,199 | 6.0 | 7,765 | <a href="https://www.star-history.com/#phosphor-icons/homepage&Date"><img src="https://api.star-history.com/svg?repos=phosphor-icons/homepage&type=Date" width="260" alt="phosphor-icons/homepage 的星标历史曲线"></a> |
| 7 | [airbnb/lottie-web](https://github.com/airbnb/lottie-web)<br>AE 做的动画，直接放进网页<br>`设计 / 创意` | +1,105 | 3.0 | 32,357 | <a href="https://www.star-history.com/#airbnb/lottie-web&Date"><img src="https://api.star-history.com/svg?repos=airbnb/lottie-web&type=Date" width="260" alt="airbnb/lottie-web 的星标历史曲线"></a> |
| 8 | [lottiefiles/lottie-ios](https://github.com/lottiefiles/lottie-ios)<br>AE 做的动画，直接放进 iOS<br>`设计 / 创意` | +1 | 0.0 | 43 | <a href="https://www.star-history.com/#lottiefiles/lottie-ios&Date"><img src="https://api.star-history.com/svg?repos=lottiefiles/lottie-ios&type=Date" width="260" alt="lottiefiles/lottie-ios 的星标历史曲线"></a> |

### 总星标数（历史累计）

| # | 项目 | 总星标 | 星标历史 |
|---|---|---:|---|
| 1 | [excalidraw/excalidraw](https://github.com/excalidraw/excalidraw)<br>打开就画，像在纸上随手画图<br>`设计 / 创意` | 135,169 | <a href="https://www.star-history.com/#excalidraw/excalidraw&Date"><img src="https://api.star-history.com/svg?repos=excalidraw/excalidraw&type=Date" width="260" alt="excalidraw/excalidraw 的星标历史曲线"></a> |
| 2 | [penpot/penpot](https://github.com/penpot/penpot)<br>团队一起做设计，用开源平台<br>`设计 / 创意` | 62,070 | <a href="https://www.star-history.com/#penpot/penpot&Date"><img src="https://api.star-history.com/svg?repos=penpot/penpot&type=Date" width="260" alt="penpot/penpot 的星标历史曲线"></a> |
| 3 | [saadeghi/daisyui](https://github.com/saadeghi/daisyui)<br>Tailwind 也有现成组件可挑<br>`设计 / 创意` | 42,737 | <a href="https://www.star-history.com/#saadeghi/daisyui&Date"><img src="https://api.star-history.com/svg?repos=saadeghi/daisyui&type=Date" width="260" alt="saadeghi/daisyui 的星标历史曲线"></a> |
| 4 | [airbnb/lottie-web](https://github.com/airbnb/lottie-web)<br>AE 做的动画，直接放进网页<br>`设计 / 创意` | 32,357 | <a href="https://www.star-history.com/#airbnb/lottie-web&Date"><img src="https://api.star-history.com/svg?repos=airbnb/lottie-web&type=Date" width="260" alt="airbnb/lottie-web 的星标历史曲线"></a> |
| 5 | [lucide-icons/lucide](https://github.com/lucide-icons/lucide)<br>一套图标风格统一，拿来就用<br>`设计 / 创意` | 25,570 | <a href="https://www.star-history.com/#lucide-icons/lucide&Date"><img src="https://api.star-history.com/svg?repos=lucide-icons/lucide&type=Date" width="260" alt="lucide-icons/lucide 的星标历史曲线"></a> |
| 6 | [jgraph/drawio](https://github.com/jgraph/drawio)<br>画图和白板，一个编辑器搞定<br>`设计 / 创意` | 9,182 | <a href="https://www.star-history.com/#jgraph/drawio&Date"><img src="https://api.star-history.com/svg?repos=jgraph/drawio&type=Date" width="260" alt="jgraph/drawio 的星标历史曲线"></a> |
| 7 | [phosphor-icons/homepage](https://github.com/phosphor-icons/homepage)<br>一整套灵活的图标，人人可用<br>`设计 / 创意` | 7,765 | <a href="https://www.star-history.com/#phosphor-icons/homepage&Date"><img src="https://api.star-history.com/svg?repos=phosphor-icons/homepage&type=Date" width="260" alt="phosphor-icons/homepage 的星标历史曲线"></a> |
| 8 | [lottiefiles/lottie-ios](https://github.com/lottiefiles/lottie-ios)<br>AE 做的动画，直接放进 iOS<br>`设计 / 创意` | 43 | <a href="https://www.star-history.com/#lottiefiles/lottie-ios&Date"><img src="https://api.star-history.com/svg?repos=lottiefiles/lottie-ios&type=Date" width="260" alt="lottiefiles/lottie-ios 的星标历史曲线"></a> |

## 数据

> 数据库、分析、ETL 与数据工程

### 最热新仓库（近 7 天内创建）

本次运行中没有符合条件的新仓库。

### 本周增长最快（近 7 天）

| # | 项目 | 新增星标 | 星标/天 | 总星标 | 星标历史 |
|---|---|---:|---:|---:|---|
| 1 | [duckdb/duckdb](https://github.com/duckdb/duckdb)<br>不搭数据库服务，也能跑 SQL 分析<br>`数据` | +193 | 27.6 | 42,820 | <a href="https://www.star-history.com/#duckdb/duckdb&Date"><img src="https://api.star-history.com/svg?repos=duckdb/duckdb&type=Date" width="260" alt="duckdb/duckdb 的星标历史曲线"></a> |
| 2 | [ClickHouse/ClickHouse](https://github.com/ClickHouse/ClickHouse)<br>大量数据实时分析，用开源的<br>`数据` | +121 | 17.3 | 50,747 | <a href="https://www.star-history.com/#ClickHouse/ClickHouse&Date"><img src="https://api.star-history.com/svg?repos=ClickHouse/ClickHouse&type=Date" width="260" alt="ClickHouse/ClickHouse 的星标历史曲线"></a> |
| 3 | [apache/superset](https://github.com/apache/superset)<br>数据看不懂，做成图就明白<br>`数据` | +94 | 13.4 | 75,409 | <a href="https://www.star-history.com/#apache/superset&Date"><img src="https://api.star-history.com/svg?repos=apache/superset&type=Date" width="260" alt="apache/superset 的星标历史曲线"></a> |
| 4 | [pola-rs/polars](https://github.com/pola-rs/polars)<br>表格数据处理快，不用干等<br>`数据` | +58 | 8.3 | 40,258 | <a href="https://www.star-history.com/#pola-rs/polars&Date"><img src="https://api.star-history.com/svg?repos=pola-rs/polars&type=Date" width="260" alt="pola-rs/polars 的星标历史曲线"></a> |
| 5 | [apache/kafka](https://github.com/apache/kafka)<br>系统之间的事件流，交给它来传<br>`数据` | +53 | 7.6 | 34,128 | <a href="https://www.star-history.com/#apache/kafka&Date"><img src="https://api.star-history.com/svg?repos=apache/kafka&type=Date" width="260" alt="apache/kafka 的星标历史曲线"></a> |
| 6 | [apache/arrow](https://github.com/apache/arrow)<br>不同语言之间，数据直接通用<br>`数据` | +40 | 5.7 | 17,276 | <a href="https://www.star-history.com/#apache/arrow&Date"><img src="https://api.star-history.com/svg?repos=apache/arrow&type=Date" width="260" alt="apache/arrow 的星标历史曲线"></a> |
| 7 | [dbt-labs/dbt-core](https://github.com/dbt-labs/dbt-core)<br>数据转换，照软件工程的做法来<br>`数据` | +34 | 4.9 | 14,119 | <a href="https://www.star-history.com/#dbt-labs/dbt-core&Date"><img src="https://api.star-history.com/svg?repos=dbt-labs/dbt-core&type=Date" width="260" alt="dbt-labs/dbt-core 的星标历史曲线"></a> |
| 8 | [jupyter/notebook](https://github.com/jupyter/notebook)<br>在网页里写代码，边写边看结果<br>`数据` | +3 | 0.4 | 13,459 | <a href="https://www.star-history.com/#jupyter/notebook&Date"><img src="https://api.star-history.com/svg?repos=jupyter/notebook&type=Date" width="260" alt="jupyter/notebook 的星标历史曲线"></a> |

### 本月增长最快（近 30 天）

| # | 项目 | 新增星标 | 星标/天 | 总星标 | 星标历史 |
|---|---|---:|---:|---:|---|
| 1 | [duckdb/duckdb](https://github.com/duckdb/duckdb)<br>不搭数据库服务，也能跑 SQL 分析<br>`数据` | +962 | 32.1 | 42,820 | <a href="https://www.star-history.com/#duckdb/duckdb&Date"><img src="https://api.star-history.com/svg?repos=duckdb/duckdb&type=Date" width="260" alt="duckdb/duckdb 的星标历史曲线"></a> |
| 2 | [ClickHouse/ClickHouse](https://github.com/ClickHouse/ClickHouse)<br>大量数据实时分析，用开源的<br>`数据` | +583 | 19.4 | 50,747 | <a href="https://www.star-history.com/#ClickHouse/ClickHouse&Date"><img src="https://api.star-history.com/svg?repos=ClickHouse/ClickHouse&type=Date" width="260" alt="ClickHouse/ClickHouse 的星标历史曲线"></a> |
| 3 | [apache/superset](https://github.com/apache/superset)<br>数据看不懂，做成图就明白<br>`数据` | +463 | 15.4 | 75,409 | <a href="https://www.star-history.com/#apache/superset&Date"><img src="https://api.star-history.com/svg?repos=apache/superset&type=Date" width="260" alt="apache/superset 的星标历史曲线"></a> |
| 4 | [pola-rs/polars](https://github.com/pola-rs/polars)<br>表格数据处理快，不用干等<br>`数据` | +389 | 13.0 | 40,258 | <a href="https://www.star-history.com/#pola-rs/polars&Date"><img src="https://api.star-history.com/svg?repos=pola-rs/polars&type=Date" width="260" alt="pola-rs/polars 的星标历史曲线"></a> |
| 5 | [apache/kafka](https://github.com/apache/kafka)<br>系统之间的事件流，交给它来传<br>`数据` | +292 | 9.7 | 34,128 | <a href="https://www.star-history.com/#apache/kafka&Date"><img src="https://api.star-history.com/svg?repos=apache/kafka&type=Date" width="260" alt="apache/kafka 的星标历史曲线"></a> |
| 6 | [dbt-labs/dbt-core](https://github.com/dbt-labs/dbt-core)<br>数据转换，照软件工程的做法来<br>`数据` | +173 | 5.8 | 14,119 | <a href="https://www.star-history.com/#dbt-labs/dbt-core&Date"><img src="https://api.star-history.com/svg?repos=dbt-labs/dbt-core&type=Date" width="260" alt="dbt-labs/dbt-core 的星标历史曲线"></a> |
| 7 | [apache/arrow](https://github.com/apache/arrow)<br>不同语言之间，数据直接通用<br>`数据` | +119 | 4.0 | 17,276 | <a href="https://www.star-history.com/#apache/arrow&Date"><img src="https://api.star-history.com/svg?repos=apache/arrow&type=Date" width="260" alt="apache/arrow 的星标历史曲线"></a> |
| 8 | [jupyter/notebook](https://github.com/jupyter/notebook)<br>在网页里写代码，边写边看结果<br>`数据` | +67 | 2.2 | 13,459 | <a href="https://www.star-history.com/#jupyter/notebook&Date"><img src="https://api.star-history.com/svg?repos=jupyter/notebook&type=Date" width="260" alt="jupyter/notebook 的星标历史曲线"></a> |

### 今年增长最快（近 365 天）

| # | 项目 | 新增星标 | 星标/天 | 总星标 | 星标历史 |
|---|---|---:|---:|---:|---|
| 1 | [duckdb/duckdb](https://github.com/duckdb/duckdb)<br>不搭数据库服务，也能跑 SQL 分析<br>`数据` | +9,388 | 25.7 | 42,820 | <a href="https://www.star-history.com/#duckdb/duckdb&Date"><img src="https://api.star-history.com/svg?repos=duckdb/duckdb&type=Date" width="260" alt="duckdb/duckdb 的星标历史曲线"></a> |
| 2 | [ClickHouse/ClickHouse](https://github.com/ClickHouse/ClickHouse)<br>大量数据实时分析，用开源的<br>`数据` | +7,622 | 20.9 | 50,747 | <a href="https://www.star-history.com/#ClickHouse/ClickHouse&Date"><img src="https://api.star-history.com/svg?repos=ClickHouse/ClickHouse&type=Date" width="260" alt="ClickHouse/ClickHouse 的星标历史曲线"></a> |
| 3 | [apache/superset](https://github.com/apache/superset)<br>数据看不懂，做成图就明白<br>`数据` | +7,431 | 20.4 | 75,409 | <a href="https://www.star-history.com/#apache/superset&Date"><img src="https://api.star-history.com/svg?repos=apache/superset&type=Date" width="260" alt="apache/superset 的星标历史曲线"></a> |
| 4 | [pola-rs/polars](https://github.com/pola-rs/polars)<br>表格数据处理快，不用干等<br>`数据` | +4,847 | 13.3 | 40,258 | <a href="https://www.star-history.com/#pola-rs/polars&Date"><img src="https://api.star-history.com/svg?repos=pola-rs/polars&type=Date" width="260" alt="pola-rs/polars 的星标历史曲线"></a> |
| 5 | [apache/kafka](https://github.com/apache/kafka)<br>系统之间的事件流，交给它来传<br>`数据` | +3,293 | 9.0 | 34,128 | <a href="https://www.star-history.com/#apache/kafka&Date"><img src="https://api.star-history.com/svg?repos=apache/kafka&type=Date" width="260" alt="apache/kafka 的星标历史曲线"></a> |
| 6 | [dbt-labs/dbt-core](https://github.com/dbt-labs/dbt-core)<br>数据转换，照软件工程的做法来<br>`数据` | +2,470 | 6.8 | 14,119 | <a href="https://www.star-history.com/#dbt-labs/dbt-core&Date"><img src="https://api.star-history.com/svg?repos=dbt-labs/dbt-core&type=Date" width="260" alt="dbt-labs/dbt-core 的星标历史曲线"></a> |
| 7 | [apache/arrow](https://github.com/apache/arrow)<br>不同语言之间，数据直接通用<br>`数据` | +1,318 | 3.6 | 17,276 | <a href="https://www.star-history.com/#apache/arrow&Date"><img src="https://api.star-history.com/svg?repos=apache/arrow&type=Date" width="260" alt="apache/arrow 的星标历史曲线"></a> |
| 8 | [jupyter/notebook](https://github.com/jupyter/notebook)<br>在网页里写代码，边写边看结果<br>`数据` | +899 | 2.5 | 13,459 | <a href="https://www.star-history.com/#jupyter/notebook&Date"><img src="https://api.star-history.com/svg?repos=jupyter/notebook&type=Date" width="260" alt="jupyter/notebook 的星标历史曲线"></a> |

### 总星标数（历史累计）

| # | 项目 | 总星标 | 星标历史 |
|---|---|---:|---|
| 1 | [apache/superset](https://github.com/apache/superset)<br>数据看不懂，做成图就明白<br>`数据` | 75,409 | <a href="https://www.star-history.com/#apache/superset&Date"><img src="https://api.star-history.com/svg?repos=apache/superset&type=Date" width="260" alt="apache/superset 的星标历史曲线"></a> |
| 2 | [ClickHouse/ClickHouse](https://github.com/ClickHouse/ClickHouse)<br>大量数据实时分析，用开源的<br>`数据` | 50,747 | <a href="https://www.star-history.com/#ClickHouse/ClickHouse&Date"><img src="https://api.star-history.com/svg?repos=ClickHouse/ClickHouse&type=Date" width="260" alt="ClickHouse/ClickHouse 的星标历史曲线"></a> |
| 3 | [duckdb/duckdb](https://github.com/duckdb/duckdb)<br>不搭数据库服务，也能跑 SQL 分析<br>`数据` | 42,820 | <a href="https://www.star-history.com/#duckdb/duckdb&Date"><img src="https://api.star-history.com/svg?repos=duckdb/duckdb&type=Date" width="260" alt="duckdb/duckdb 的星标历史曲线"></a> |
| 4 | [pola-rs/polars](https://github.com/pola-rs/polars)<br>表格数据处理快，不用干等<br>`数据` | 40,258 | <a href="https://www.star-history.com/#pola-rs/polars&Date"><img src="https://api.star-history.com/svg?repos=pola-rs/polars&type=Date" width="260" alt="pola-rs/polars 的星标历史曲线"></a> |
| 5 | [apache/kafka](https://github.com/apache/kafka)<br>系统之间的事件流，交给它来传<br>`数据` | 34,128 | <a href="https://www.star-history.com/#apache/kafka&Date"><img src="https://api.star-history.com/svg?repos=apache/kafka&type=Date" width="260" alt="apache/kafka 的星标历史曲线"></a> |
| 6 | [apache/arrow](https://github.com/apache/arrow)<br>不同语言之间，数据直接通用<br>`数据` | 17,276 | <a href="https://www.star-history.com/#apache/arrow&Date"><img src="https://api.star-history.com/svg?repos=apache/arrow&type=Date" width="260" alt="apache/arrow 的星标历史曲线"></a> |
| 7 | [dbt-labs/dbt-core](https://github.com/dbt-labs/dbt-core)<br>数据转换，照软件工程的做法来<br>`数据` | 14,119 | <a href="https://www.star-history.com/#dbt-labs/dbt-core&Date"><img src="https://api.star-history.com/svg?repos=dbt-labs/dbt-core&type=Date" width="260" alt="dbt-labs/dbt-core 的星标历史曲线"></a> |
| 8 | [jupyter/notebook](https://github.com/jupyter/notebook)<br>在网页里写代码，边写边看结果<br>`数据` | 13,459 | <a href="https://www.star-history.com/#jupyter/notebook&Date"><img src="https://api.star-history.com/svg?repos=jupyter/notebook&type=Date" width="260" alt="jupyter/notebook 的星标历史曲线"></a> |

---

如果它帮你省了时间，请给仓库点个星标，让更多人找得到。

如何引用：见 [CITATION.cff](CITATION.cff)。

数据怎么算和如何参与：[docs/HOW_IT_WORKS.zh-Hans.md](docs/HOW_IT_WORKS.zh-Hans.md)。新仓库规则：[docs/NEW_ARRIVALS.md](docs/NEW_ARRIVALS.md)。分类说明：[docs/CATEGORIES.md](docs/CATEGORIES.md)。提交改动：[CONTRIBUTING.md](CONTRIBUTING.md)。
