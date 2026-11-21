[English](README.md) | **简体中文** | [繁體中文](README.zh-Hant.md) | [日本語](README.ja.md) | [한국어](README.ko.md)

# GitHub 涨星榜 / GitHub Risers

<img src=".github/social-preview.png" alt="GitHub 涨星榜 / GitHub Risers" width="640">

[![MIT](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE) [![CI](https://github.com/jammyfu/github-risers/actions/workflows/ci.yml/badge.svg)](https://github.com/jammyfu/github-risers/actions/workflows/ci.yml) [![updated](https://img.shields.io/badge/dynamic/json?url=https%3A%2F%2Fraw.githubusercontent.com%2Fjammyfu%2Fgithub-risers%2Fmain%2Fdata%2Fstats.json&query=%24.today_utc&label=updated&color=brightgreen)](latest/rankings.zh-Hans.md)

按每天新增星标（而不是总星标）给 GitHub 仓库排名：AI 在前，其后是开发者工具、安全、Web / 前端、基础设施、设计 / 创意和数据；每天更新。

数据取自 2026-11-21 14:58（UTC）。每天更新。

**在线榜单：** [网站](https://jammyfu.github.io/github-risers/) · [最新快照](latest/rankings.zh-Hans.md)

## 马上使用

1. 打开[在线榜单](https://jammyfu.github.io/github-risers/)，不用安装。
2. 或者先看下面本期各类榜首，再翻分类榜。
3. 这里每张榜只列前 10 名；完整前 20 名在 [latest/rankings.zh-Hans.md](latest/rankings.zh-Hans.md)。

[网站](https://jammyfu.github.io/github-risers/) · [运作方式](docs/HOW_IT_WORKS.zh-Hans.md) · [事实速查](docs/FACTS.md) · [历史榜单](rankings/README.zh-Hans.md) · [最新快照](latest/rankings.zh-Hans.md)

## 本期各类榜首

| 分类 | 新仓库第 1 名（7 天） | 本周第 1 名 | 本月第 1 名 | 今年第 1 名 | 总星标第 1 名 |
|---|---|---|---|---|---|
| **[人工智能](#人工智能)** ★ 主榜 | [erkamyaman/rust-anything](https://github.com/erkamyaman/rust-anything)<br>1,395/天 | [morluto/rea](https://github.com/morluto/rea)<br>2,021/天 | [morluto/rea](https://github.com/morluto/rea)<br>3,804/天 | [deepseek-ai/deepseek-harness](https://github.com/deepseek-ai/deepseek-harness)<br>2,848/天 | [morluto/rea](https://github.com/morluto/rea)<br>472,297 ★ |
| **[开发者工具](#开发者工具)** | [mariaquinonesm-dot/wezterm-cerroora](https://github.com/mariaquinonesm-dot/wezterm-cerroora)<br>92.4/天 | [astral-sh/uv](https://github.com/astral-sh/uv)<br>86.1/天 | [zed-industries/zed](https://github.com/zed-industries/zed)<br>124/天 | [zed-industries/zed](https://github.com/zed-industries/zed)<br>75.2/天 | [oven-sh/bun](https://github.com/oven-sh/bun)<br>96,816 ★ |
| **[安全](#安全)** | 无 | [projectdiscovery/nuclei](https://github.com/projectdiscovery/nuclei)<br>40.6/天 | [aquasecurity/trivy](https://github.com/aquasecurity/trivy)<br>35.2/天 | [aquasecurity/trivy](https://github.com/aquasecurity/trivy)<br>28.9/天 | [aquasecurity/trivy](https://github.com/aquasecurity/trivy)<br>39,592 ★ |
| **[Web / 前端](#web--前端)** | [carlperry-88/devlabs](https://github.com/carlperry-88/devlabs)<br>106/天 | [sveltejs/svelte](https://github.com/sveltejs/svelte)<br>172/天 | [shadcn-ui/ui](https://github.com/shadcn-ui/ui)<br>92.0/天 | [shadcn-ui/ui](https://github.com/shadcn-ui/ui)<br>82.9/天 | [facebook/react](https://github.com/facebook/react)<br>252,843 ★ |
| **[基础设施](#基础设施)** | [replit/datacat](https://github.com/replit/datacat)<br>108/天 | [kubernetes/kubernetes](https://github.com/kubernetes/kubernetes)<br>50.1/天 | [caddyserver/caddy](https://github.com/caddyserver/caddy)<br>41.5/天 | [caddyserver/caddy](https://github.com/caddyserver/caddy)<br>33.6/天 | [kubernetes/kubernetes](https://github.com/kubernetes/kubernetes)<br>129,308 ★ |
| **[设计 / 创意](#设计--创意)** | 无 | [excalidraw/excalidraw](https://github.com/excalidraw/excalidraw)<br>60.6/天 | [excalidraw/excalidraw](https://github.com/excalidraw/excalidraw)<br>63.6/天 | [excalidraw/excalidraw](https://github.com/excalidraw/excalidraw)<br>73.3/天 | [excalidraw/excalidraw](https://github.com/excalidraw/excalidraw)<br>136,056 ★ |
| **[数据](#数据)** | 无 | [duckdb/duckdb](https://github.com/duckdb/duckdb)<br>25.0/天 | [duckdb/duckdb](https://github.com/duckdb/duckdb)<br>30.8/天 | [duckdb/duckdb](https://github.com/duckdb/duckdb)<br>25.8/天 | [apache/superset](https://github.com/apache/superset)<br>75,604 ★ |

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

| # | 项目 | 创建时间（UTC） | 总星标 | 星标/天 |
|---|---|---|---:|---:|
| 1 | [erkamyaman/rust-anything](https://github.com/erkamyaman/rust-anything)<br>想换成 Rust？对照原行为一步步迁移 | 2026-11-16<br><sub>5.1 天</sub> | 7,137 | 1,394.9 |
| 2 | [danielwh2/sprite-stacking](https://github.com/danielwh2/sprite-stacking)<br>Agent skill: turn four pixel art views into fake-3D sprites you can spin. Works with Claude Code, Codex, Cursor, OpenCode, Gemini CLI, Pi. | 2026-11-20<br><sub>1.0 天</sub> | 306 | 300.6 |
| 3 | [sybil-solutions/inference-optimisation-skill](https://github.com/sybil-solutions/inference-optimisation-skill)<br>本地LLM太慢？让智能体技能帮你加速 | 2026-11-16<br><sub>4.8 天</sub> | 1,426 | 294.3 |
| 4 | [boringmarketer/boring-marketing-skills](https://github.com/boringmarketer/boring-marketing-skills)<br>让 AI 智能体掌握 32 项免费营销技能 | 2026-11-16<br><sub>5.0 天</sub> | 763 | 152.8 |
| 5 | [INK-Q/agy-fast](https://github.com/INK-Q/agy-fast)<br>对话太耗Token？帮你减少额度消耗 | 2026-11-19<br><sub>2.4 天</sub> | 238 | 98.5 |
| 6 | [staryone/motlab](https://github.com/staryone/motlab)<br>给参考资料，让智能体写代码做视频 | 2026-11-16<br><sub>5.0 天</sub> | 331 | 65.5 |
| 7 | [diego3g/craft](https://github.com/diego3g/craft)<br>界面设计太繁琐？让智能体画全状态页面 | 2026-11-15<br><sub>5.8 天</sub> | 341 | 58.9 |
| 8 | [jackson-cmd/claude-multi-desktop](https://github.com/jackson-cmd/claude-multi-desktop)<br>在 Mac 同时登录多个 Claude 桌面账号 | 2026-11-16<br><sub>5.4 天</sub> | 247 | 45.4 |
| 9 | [kobimusic/dettato](https://github.com/kobimusic/dettato)<br>KobiMusic's multi-instrument audio-to-MIDI transcriber: notes, instrument tracks and drums from any recording | 2026-11-16<br><sub>5.2 天</sub> | 211 | 40.2 |
| 10 | [google-deepmind/robotics-antigravity-plugin](https://github.com/google-deepmind/robotics-antigravity-plugin)<br>打不通仿真与真机？运行智能体式工作流 | 2026-11-16<br><sub>4.8 天</sub> | 191 | 39.5 |

<details>
<summary>本榜星标历史曲线</summary>

<a href="https://www.star-history.com/#erkamyaman/rust-anything&Date"><img src="https://api.star-history.com/svg?repos=erkamyaman/rust-anything&type=Date" width="260" alt="erkamyaman/rust-anything 的星标历史曲线"></a>

<a href="https://www.star-history.com/#danielwh2/sprite-stacking&Date"><img src="https://api.star-history.com/svg?repos=danielwh2/sprite-stacking&type=Date" width="260" alt="danielwh2/sprite-stacking 的星标历史曲线"></a>

<a href="https://www.star-history.com/#sybil-solutions/inference-optimisation-skill&Date"><img src="https://api.star-history.com/svg?repos=sybil-solutions/inference-optimisation-skill&type=Date" width="260" alt="sybil-solutions/inference-optimisation-skill 的星标历史曲线"></a>

<a href="https://www.star-history.com/#boringmarketer/boring-marketing-skills&Date"><img src="https://api.star-history.com/svg?repos=boringmarketer/boring-marketing-skills&type=Date" width="260" alt="boringmarketer/boring-marketing-skills 的星标历史曲线"></a>

<a href="https://www.star-history.com/#INK-Q/agy-fast&Date"><img src="https://api.star-history.com/svg?repos=INK-Q/agy-fast&type=Date" width="260" alt="INK-Q/agy-fast 的星标历史曲线"></a>

<a href="https://www.star-history.com/#staryone/motlab&Date"><img src="https://api.star-history.com/svg?repos=staryone/motlab&type=Date" width="260" alt="staryone/motlab 的星标历史曲线"></a>

<a href="https://www.star-history.com/#diego3g/craft&Date"><img src="https://api.star-history.com/svg?repos=diego3g/craft&type=Date" width="260" alt="diego3g/craft 的星标历史曲线"></a>

<a href="https://www.star-history.com/#jackson-cmd/claude-multi-desktop&Date"><img src="https://api.star-history.com/svg?repos=jackson-cmd/claude-multi-desktop&type=Date" width="260" alt="jackson-cmd/claude-multi-desktop 的星标历史曲线"></a>

<a href="https://www.star-history.com/#kobimusic/dettato&Date"><img src="https://api.star-history.com/svg?repos=kobimusic/dettato&type=Date" width="260" alt="kobimusic/dettato 的星标历史曲线"></a>

<a href="https://www.star-history.com/#google-deepmind/robotics-antigravity-plugin&Date"><img src="https://api.star-history.com/svg?repos=google-deepmind/robotics-antigravity-plugin&type=Date" width="260" alt="google-deepmind/robotics-antigravity-plugin 的星标历史曲线"></a>

</details>

### 本周增长最快（近 7 天）

| # | 项目 | 新增星标 | 星标/天 | 总星标 |
|---|---|---:|---:|---:|
| 1 | [morluto/rea](https://github.com/morluto/rea)<br>让 AI 帮你克隆任何软件<br>`人工智能` | +14,144 | 2,020.6 | 472,297 |
| 2 | [stablyai/orca](https://github.com/stablyai/orca)<br>几个 AI 一起写，谁好用一眼看出<br>`人工智能` | +7,004 | 1,000.6 | 131,641 |
| 3 | [affaan-m/ECC](https://github.com/affaan-m/ECC)<br>给编程 AI 加记忆、技能和安全检查<br>`人工智能` | +5,736 | 819.4 | 308,158 |
| 4 | [DietrichGebert/ponytail](https://github.com/DietrichGebert/ponytail)<br>让 AI 少写废代码，该写的写对<br>`人工智能` | +5,538 | 791.1 | 196,088 |
| 5 | [cloudflare/security-audit-skill](https://github.com/cloudflare/security-audit-skill)<br>AI 查代码漏洞，另一个 AI 逐条复核<br>`人工智能` | +4,412 | 630.3 | 76,530 |
| 6 | [deepseek-ai/deepseek-harness](https://github.com/deepseek-ai/deepseek-harness)<br>想要什么智能体，用插件自己拼<br>`人工智能` | +4,384 | 626.3 | 284,963 |
| 7 | [Leonxlnx/taste-skill](https://github.com/Leonxlnx/taste-skill)<br>别再让 AI 做出千篇一律的页面<br>`人工智能` | +4,372 | 624.6 | 119,591 |
| 8 | [anthropics/skills](https://github.com/anthropics/skills)<br>Claude 技能怎么写，照着官方学<br>`人工智能` | +4,067 | 581.0 | 198,324 |
| 9 | [Graphify-Labs/graphify](https://github.com/Graphify-Labs/graphify)<br>大项目看不过来，先看这张地图<br>`人工智能` | +4,062 | 580.3 | 151,459 |
| 10 | [heygen-com/hyperframes](https://github.com/heygen-com/hyperframes)<br>不会剪辑，写网页一样就能出片<br>`人工智能` | +3,615 | 516.4 | 87,707 |

<details>
<summary>本榜星标历史曲线</summary>

<a href="https://www.star-history.com/#morluto/rea&Date"><img src="https://api.star-history.com/svg?repos=morluto/rea&type=Date" width="260" alt="morluto/rea 的星标历史曲线"></a>

<a href="https://www.star-history.com/#stablyai/orca&Date"><img src="https://api.star-history.com/svg?repos=stablyai/orca&type=Date" width="260" alt="stablyai/orca 的星标历史曲线"></a>

<a href="https://www.star-history.com/#affaan-m/ECC&Date"><img src="https://api.star-history.com/svg?repos=affaan-m/ECC&type=Date" width="260" alt="affaan-m/ECC 的星标历史曲线"></a>

<a href="https://www.star-history.com/#DietrichGebert/ponytail&Date"><img src="https://api.star-history.com/svg?repos=DietrichGebert/ponytail&type=Date" width="260" alt="DietrichGebert/ponytail 的星标历史曲线"></a>

<a href="https://www.star-history.com/#cloudflare/security-audit-skill&Date"><img src="https://api.star-history.com/svg?repos=cloudflare/security-audit-skill&type=Date" width="260" alt="cloudflare/security-audit-skill 的星标历史曲线"></a>

<a href="https://www.star-history.com/#deepseek-ai/deepseek-harness&Date"><img src="https://api.star-history.com/svg?repos=deepseek-ai/deepseek-harness&type=Date" width="260" alt="deepseek-ai/deepseek-harness 的星标历史曲线"></a>

<a href="https://www.star-history.com/#Leonxlnx/taste-skill&Date"><img src="https://api.star-history.com/svg?repos=Leonxlnx/taste-skill&type=Date" width="260" alt="Leonxlnx/taste-skill 的星标历史曲线"></a>

<a href="https://www.star-history.com/#anthropics/skills&Date"><img src="https://api.star-history.com/svg?repos=anthropics/skills&type=Date" width="260" alt="anthropics/skills 的星标历史曲线"></a>

<a href="https://www.star-history.com/#Graphify-Labs/graphify&Date"><img src="https://api.star-history.com/svg?repos=Graphify-Labs/graphify&type=Date" width="260" alt="Graphify-Labs/graphify 的星标历史曲线"></a>

<a href="https://www.star-history.com/#heygen-com/hyperframes&Date"><img src="https://api.star-history.com/svg?repos=heygen-com/hyperframes&type=Date" width="260" alt="heygen-com/hyperframes 的星标历史曲线"></a>

</details>

### 本月增长最快（近 30 天）

| # | 项目 | 新增星标 | 星标/天 | 总星标 |
|---|---|---:|---:|---:|
| 1 | [morluto/rea](https://github.com/morluto/rea)<br>让 AI 帮你克隆任何软件<br>`人工智能` | +114,114 | 3,803.8 | 472,297 |
| 2 | [cloudflare/security-audit-skill](https://github.com/cloudflare/security-audit-skill)<br>AI 查代码漏洞，另一个 AI 逐条复核<br>`人工智能` | +39,317 | 1,310.6 | 76,530 |
| 3 | [stablyai/orca](https://github.com/stablyai/orca)<br>几个 AI 一起写，谁好用一眼看出<br>`人工智能` | +30,281 | 1,009.4 | 131,641 |
| 4 | [deepseek-ai/deepseek-harness](https://github.com/deepseek-ai/deepseek-harness)<br>想要什么智能体，用插件自己拼<br>`人工智能` | +28,723 | 957.4 | 284,963 |
| 5 | [DietrichGebert/ponytail](https://github.com/DietrichGebert/ponytail)<br>让 AI 少写废代码，该写的写对<br>`人工智能` | +24,510 | 817.0 | 196,088 |
| 6 | [affaan-m/ECC](https://github.com/affaan-m/ECC)<br>给编程 AI 加记忆、技能和安全检查<br>`人工智能` | +23,305 | 776.8 | 308,158 |
| 7 | [yetone/magpie](https://github.com/yetone/magpie)<br>编程 AI 换模型，额度用完自动续<br>`人工智能` | +20,905 | 696.8 | 39,723 |
| 8 | [Graphify-Labs/graphify](https://github.com/Graphify-Labs/graphify)<br>大项目看不过来，先看这张地图<br>`人工智能` | +19,907 | 663.6 | 151,459 |
| 9 | [Leonxlnx/taste-skill](https://github.com/Leonxlnx/taste-skill)<br>别再让 AI 做出千篇一律的页面<br>`人工智能` | +19,169 | 639.0 | 119,591 |
| 10 | [heygen-com/hyperframes](https://github.com/heygen-com/hyperframes)<br>不会剪辑，写网页一样就能出片<br>`人工智能` | +18,514 | 617.1 | 87,707 |

<details>
<summary>本榜星标历史曲线</summary>

<a href="https://www.star-history.com/#morluto/rea&Date"><img src="https://api.star-history.com/svg?repos=morluto/rea&type=Date" width="260" alt="morluto/rea 的星标历史曲线"></a>

<a href="https://www.star-history.com/#cloudflare/security-audit-skill&Date"><img src="https://api.star-history.com/svg?repos=cloudflare/security-audit-skill&type=Date" width="260" alt="cloudflare/security-audit-skill 的星标历史曲线"></a>

<a href="https://www.star-history.com/#stablyai/orca&Date"><img src="https://api.star-history.com/svg?repos=stablyai/orca&type=Date" width="260" alt="stablyai/orca 的星标历史曲线"></a>

<a href="https://www.star-history.com/#deepseek-ai/deepseek-harness&Date"><img src="https://api.star-history.com/svg?repos=deepseek-ai/deepseek-harness&type=Date" width="260" alt="deepseek-ai/deepseek-harness 的星标历史曲线"></a>

<a href="https://www.star-history.com/#DietrichGebert/ponytail&Date"><img src="https://api.star-history.com/svg?repos=DietrichGebert/ponytail&type=Date" width="260" alt="DietrichGebert/ponytail 的星标历史曲线"></a>

<a href="https://www.star-history.com/#affaan-m/ECC&Date"><img src="https://api.star-history.com/svg?repos=affaan-m/ECC&type=Date" width="260" alt="affaan-m/ECC 的星标历史曲线"></a>

<a href="https://www.star-history.com/#yetone/magpie&Date"><img src="https://api.star-history.com/svg?repos=yetone/magpie&type=Date" width="260" alt="yetone/magpie 的星标历史曲线"></a>

<a href="https://www.star-history.com/#Graphify-Labs/graphify&Date"><img src="https://api.star-history.com/svg?repos=Graphify-Labs/graphify&type=Date" width="260" alt="Graphify-Labs/graphify 的星标历史曲线"></a>

<a href="https://www.star-history.com/#Leonxlnx/taste-skill&Date"><img src="https://api.star-history.com/svg?repos=Leonxlnx/taste-skill&type=Date" width="260" alt="Leonxlnx/taste-skill 的星标历史曲线"></a>

<a href="https://www.star-history.com/#heygen-com/hyperframes&Date"><img src="https://api.star-history.com/svg?repos=heygen-com/hyperframes&type=Date" width="260" alt="heygen-com/hyperframes 的星标历史曲线"></a>

</details>

### 今年增长最快（近 365 天）

| # | 项目 | 新增星标 | 星标/天 | 总星标 |
|---|---|---:|---:|---:|
| 1 | [deepseek-ai/deepseek-harness](https://github.com/deepseek-ai/deepseek-harness)<br>想要什么智能体，用插件自己拼<br>`人工智能` | +284,810 | 2,848.1 †<br><sub>÷100 天</sub> | 284,963 |
| 2 | [morluto/rea](https://github.com/morluto/rea)<br>让 AI 帮你克隆任何软件<br>`人工智能` | +471,838 | 2,135.0 †<br><sub>÷221 天</sub> | 472,297 |
| 3 | [DietrichGebert/ponytail](https://github.com/DietrichGebert/ponytail)<br>让 AI 少写废代码，该写的写对<br>`人工智能` | +195,826 | 1,208.8 †<br><sub>÷162 天</sub> | 196,088 |
| 4 | [openclaw/openclaw](https://github.com/openclaw/openclaw)<br>能把事做完的 AI 助手，跑在自己设备上<br>`人工智能` | +394,925 | 1,091.0 †<br><sub>÷362 天</sub> | 394,959 |
| 5 | [affaan-m/ECC](https://github.com/affaan-m/ECC)<br>给编程 AI 加记忆、技能和安全检查<br>`人工智能` | +307,980 | 1,003.2 †<br><sub>÷307 天</sub> | 308,158 |
| 6 | [NousResearch/hermes-agent](https://github.com/NousResearch/hermes-agent)<br>越用越会干活的 AI 助手<br>`人工智能` | +265,034 | 726.1 | 265,129 |
| 7 | [yetone/magpie](https://github.com/yetone/magpie)<br>编程 AI 换模型，额度用完自动续<br>`人工智能` | +39,614 | 671.4 †<br><sub>÷59 天</sub> | 39,723 |
| 8 | [Graphify-Labs/graphify](https://github.com/Graphify-Labs/graphify)<br>大项目看不过来，先看这张地图<br>`人工智能` | +151,308 | 652.2 †<br><sub>÷232 天</sub> | 151,459 |
| 9 | [anomalyco/opencode](https://github.com/anomalyco/opencode)<br>终端里，有个开源 AI 帮你写代码<br>`人工智能` | +196,227 | 537.6 | 228,360 |
| 10 | [stablyai/orca](https://github.com/stablyai/orca)<br>几个 AI 一起写，谁好用一眼看出<br>`人工智能` | +131,308 | 527.3 †<br><sub>÷249 天</sub> | 131,641 |

<details>
<summary>本榜星标历史曲线</summary>

<a href="https://www.star-history.com/#deepseek-ai/deepseek-harness&Date"><img src="https://api.star-history.com/svg?repos=deepseek-ai/deepseek-harness&type=Date" width="260" alt="deepseek-ai/deepseek-harness 的星标历史曲线"></a>

<a href="https://www.star-history.com/#morluto/rea&Date"><img src="https://api.star-history.com/svg?repos=morluto/rea&type=Date" width="260" alt="morluto/rea 的星标历史曲线"></a>

<a href="https://www.star-history.com/#DietrichGebert/ponytail&Date"><img src="https://api.star-history.com/svg?repos=DietrichGebert/ponytail&type=Date" width="260" alt="DietrichGebert/ponytail 的星标历史曲线"></a>

<a href="https://www.star-history.com/#openclaw/openclaw&Date"><img src="https://api.star-history.com/svg?repos=openclaw/openclaw&type=Date" width="260" alt="openclaw/openclaw 的星标历史曲线"></a>

<a href="https://www.star-history.com/#affaan-m/ECC&Date"><img src="https://api.star-history.com/svg?repos=affaan-m/ECC&type=Date" width="260" alt="affaan-m/ECC 的星标历史曲线"></a>

<a href="https://www.star-history.com/#NousResearch/hermes-agent&Date"><img src="https://api.star-history.com/svg?repos=NousResearch/hermes-agent&type=Date" width="260" alt="NousResearch/hermes-agent 的星标历史曲线"></a>

<a href="https://www.star-history.com/#yetone/magpie&Date"><img src="https://api.star-history.com/svg?repos=yetone/magpie&type=Date" width="260" alt="yetone/magpie 的星标历史曲线"></a>

<a href="https://www.star-history.com/#Graphify-Labs/graphify&Date"><img src="https://api.star-history.com/svg?repos=Graphify-Labs/graphify&type=Date" width="260" alt="Graphify-Labs/graphify 的星标历史曲线"></a>

<a href="https://www.star-history.com/#anomalyco/opencode&Date"><img src="https://api.star-history.com/svg?repos=anomalyco/opencode&type=Date" width="260" alt="anomalyco/opencode 的星标历史曲线"></a>

<a href="https://www.star-history.com/#stablyai/orca&Date"><img src="https://api.star-history.com/svg?repos=stablyai/orca&type=Date" width="260" alt="stablyai/orca 的星标历史曲线"></a>

</details>

† 该仓库创建时间短于统计窗口，因此“星标/天”按仓库存在的天数（显示在数字下方）计算，而不是按完整窗口。

### 总星标数（历史累计）

| # | 项目 | 总星标 |
|---|---|---:|
| 1 | [morluto/rea](https://github.com/morluto/rea)<br>让 AI 帮你克隆任何软件<br>`人工智能` | 472,297 |
| 2 | [openclaw/openclaw](https://github.com/openclaw/openclaw)<br>能把事做完的 AI 助手，跑在自己设备上<br>`人工智能` | 394,959 |
| 3 | [affaan-m/ECC](https://github.com/affaan-m/ECC)<br>给编程 AI 加记忆、技能和安全检查<br>`人工智能` | 308,158 |
| 4 | [deepseek-ai/deepseek-harness](https://github.com/deepseek-ai/deepseek-harness)<br>想要什么智能体，用插件自己拼<br>`人工智能` | 284,963 |
| 5 | [NousResearch/hermes-agent](https://github.com/NousResearch/hermes-agent)<br>越用越会干活的 AI 助手<br>`人工智能` | 265,129 |
| 6 | [anomalyco/opencode](https://github.com/anomalyco/opencode)<br>终端里，有个开源 AI 帮你写代码<br>`人工智能` | 228,360 |
| 7 | [anthropics/skills](https://github.com/anthropics/skills)<br>Claude 技能怎么写，照着官方学<br>`人工智能` | 198,324 |
| 8 | [DietrichGebert/ponytail](https://github.com/DietrichGebert/ponytail)<br>让 AI 少写废代码，该写的写对<br>`人工智能` | 196,088 |
| 9 | [farion1231/cc-switch](https://github.com/farion1231/cc-switch)<br>换接口不用改配置，一键切<br>`人工智能` | 156,169 |
| 10 | [nextlevelbuilder/ui-ux-pro-max-skill](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill)<br>AI 做的界面，看着像专业设计<br>`人工智能` | 152,383 |

<details>
<summary>本榜星标历史曲线</summary>

<a href="https://www.star-history.com/#morluto/rea&Date"><img src="https://api.star-history.com/svg?repos=morluto/rea&type=Date" width="260" alt="morluto/rea 的星标历史曲线"></a>

<a href="https://www.star-history.com/#openclaw/openclaw&Date"><img src="https://api.star-history.com/svg?repos=openclaw/openclaw&type=Date" width="260" alt="openclaw/openclaw 的星标历史曲线"></a>

<a href="https://www.star-history.com/#affaan-m/ECC&Date"><img src="https://api.star-history.com/svg?repos=affaan-m/ECC&type=Date" width="260" alt="affaan-m/ECC 的星标历史曲线"></a>

<a href="https://www.star-history.com/#deepseek-ai/deepseek-harness&Date"><img src="https://api.star-history.com/svg?repos=deepseek-ai/deepseek-harness&type=Date" width="260" alt="deepseek-ai/deepseek-harness 的星标历史曲线"></a>

<a href="https://www.star-history.com/#NousResearch/hermes-agent&Date"><img src="https://api.star-history.com/svg?repos=NousResearch/hermes-agent&type=Date" width="260" alt="NousResearch/hermes-agent 的星标历史曲线"></a>

<a href="https://www.star-history.com/#anomalyco/opencode&Date"><img src="https://api.star-history.com/svg?repos=anomalyco/opencode&type=Date" width="260" alt="anomalyco/opencode 的星标历史曲线"></a>

<a href="https://www.star-history.com/#anthropics/skills&Date"><img src="https://api.star-history.com/svg?repos=anthropics/skills&type=Date" width="260" alt="anthropics/skills 的星标历史曲线"></a>

<a href="https://www.star-history.com/#DietrichGebert/ponytail&Date"><img src="https://api.star-history.com/svg?repos=DietrichGebert/ponytail&type=Date" width="260" alt="DietrichGebert/ponytail 的星标历史曲线"></a>

<a href="https://www.star-history.com/#farion1231/cc-switch&Date"><img src="https://api.star-history.com/svg?repos=farion1231/cc-switch&type=Date" width="260" alt="farion1231/cc-switch 的星标历史曲线"></a>

<a href="https://www.star-history.com/#nextlevelbuilder/ui-ux-pro-max-skill&Date"><img src="https://api.star-history.com/svg?repos=nextlevelbuilder/ui-ux-pro-max-skill&type=Date" width="260" alt="nextlevelbuilder/ui-ux-pro-max-skill 的星标历史曲线"></a>

</details>

## 开发者工具

> 命令行、编辑器、包管理、代码检查与构建工具

### 最热新仓库（近 7 天内创建）

| # | 项目 | 创建时间（UTC） | 总星标 | 星标/天 |
|---|---|---|---:|---:|
| 1 | [mariaquinonesm-dot/wezterm-cerroora](https://github.com/mariaquinonesm-dot/wezterm-cerroora)<br>Terminal emulator configuration with customizable themes and keybindings. | 2026-11-20<br><sub>1.6 天</sub> | 149 | 92.4 |
| 2 | [govijr/fix-storage](https://github.com/govijr/fix-storage)<br>存储空间出问题？一条命令直接修复 | 2026-11-14<br><sub>6.9 天</sub> | 209 | 30.2 |
| 3 | [Orderchodrag/smelt-minecraft-mods-to-rust-converter](https://github.com/Orderchodrag/smelt-minecraft-mods-to-rust-converter)<br>Java模组难移植？转出Rust代码 | 2026-11-16<br><sub>5.0 天</sub> | 142 | 28.6 |
| 4 | [vulnix0x4/a-better-antivirus](https://github.com/vulnix0x4/a-better-antivirus)<br>Catches infostealers in the act on Windows: plants fake passwords, wallets and app data that only malware would read, and freezes whatever touches them. | 2026-11-17<br><sub>4.5 天</sub> | 111 | 24.7 |
| 5 | [ineedfoundmyway/planrelay](https://github.com/ineedfoundmyway/planrelay)<br>在方案与代码评审中快速批注并解决卡点 | 2026-11-15<br><sub>6.3 天</sub> | 123 | 19.6 |
| 6 | [luisgonzaleznf/renfe-cli](https://github.com/luisgonzaleznf/renfe-cli)<br>JSON-first CLI for Renfe train timetables and fares. No account needed. | 2026-11-15<br><sub>5.9 天</sub> | 105 | 17.9 |
| 7 | [takidd767-ship-it/rust-external-trainer-sanolan](https://github.com/takidd767-ship-it/rust-external-trainer-sanolan)<br>A focused Rust external trainer delivering practical in-game aid and readable data panels. | 2026-11-21<br><sub>1.0 天</sub> | 189 | 189.0 |
| 8 | [2411500034-indra/delta-force-trainer-velmora](https://github.com/2411500034-indra/delta-force-trainer-velmora)<br>Play Delta Force with Velmora's trainer for live tactical readouts. | 2026-11-20<br><sub>1.0 天</sub> | 151 | 151.0 |
| 9 | [luciskynet-cloud/sonyvegas](https://github.com/luciskynet-cloud/sonyvegas)<br>Sonyvegas delivers core functionality — built with direct, technical precision. | 2026-11-20<br><sub>1.1 天</sub> | 151 | 142.7 |
| 10 | [MinosoaRafalimanana/adobe-dreamweaver-varvera](https://github.com/MinosoaRafalimanana/adobe-dreamweaver-varvera)<br>Varvera edition of Adobe Dreamweaver, a web development environment for coding and design. | 2026-11-18<br><sub>2.8 天</sub> | 152 | 53.7 |

<details>
<summary>本榜星标历史曲线</summary>

<a href="https://www.star-history.com/#mariaquinonesm-dot/wezterm-cerroora&Date"><img src="https://api.star-history.com/svg?repos=mariaquinonesm-dot/wezterm-cerroora&type=Date" width="260" alt="mariaquinonesm-dot/wezterm-cerroora 的星标历史曲线"></a>

<a href="https://www.star-history.com/#govijr/fix-storage&Date"><img src="https://api.star-history.com/svg?repos=govijr/fix-storage&type=Date" width="260" alt="govijr/fix-storage 的星标历史曲线"></a>

<a href="https://www.star-history.com/#Orderchodrag/smelt-minecraft-mods-to-rust-converter&Date"><img src="https://api.star-history.com/svg?repos=Orderchodrag/smelt-minecraft-mods-to-rust-converter&type=Date" width="260" alt="Orderchodrag/smelt-minecraft-mods-to-rust-converter 的星标历史曲线"></a>

<a href="https://www.star-history.com/#vulnix0x4/a-better-antivirus&Date"><img src="https://api.star-history.com/svg?repos=vulnix0x4/a-better-antivirus&type=Date" width="260" alt="vulnix0x4/a-better-antivirus 的星标历史曲线"></a>

<a href="https://www.star-history.com/#ineedfoundmyway/planrelay&Date"><img src="https://api.star-history.com/svg?repos=ineedfoundmyway/planrelay&type=Date" width="260" alt="ineedfoundmyway/planrelay 的星标历史曲线"></a>

<a href="https://www.star-history.com/#luisgonzaleznf/renfe-cli&Date"><img src="https://api.star-history.com/svg?repos=luisgonzaleznf/renfe-cli&type=Date" width="260" alt="luisgonzaleznf/renfe-cli 的星标历史曲线"></a>

<a href="https://www.star-history.com/#takidd767-ship-it/rust-external-trainer-sanolan&Date"><img src="https://api.star-history.com/svg?repos=takidd767-ship-it/rust-external-trainer-sanolan&type=Date" width="260" alt="takidd767-ship-it/rust-external-trainer-sanolan 的星标历史曲线"></a>

<a href="https://www.star-history.com/#2411500034-indra/delta-force-trainer-velmora&Date"><img src="https://api.star-history.com/svg?repos=2411500034-indra/delta-force-trainer-velmora&type=Date" width="260" alt="2411500034-indra/delta-force-trainer-velmora 的星标历史曲线"></a>

<a href="https://www.star-history.com/#luciskynet-cloud/sonyvegas&Date"><img src="https://api.star-history.com/svg?repos=luciskynet-cloud/sonyvegas&type=Date" width="260" alt="luciskynet-cloud/sonyvegas 的星标历史曲线"></a>

<a href="https://www.star-history.com/#MinosoaRafalimanana/adobe-dreamweaver-varvera&Date"><img src="https://api.star-history.com/svg?repos=MinosoaRafalimanana/adobe-dreamweaver-varvera&type=Date" width="260" alt="MinosoaRafalimanana/adobe-dreamweaver-varvera 的星标历史曲线"></a>

</details>

### 本周增长最快（近 7 天）

| # | 项目 | 新增星标 | 星标/天 | 总星标 |
|---|---|---:|---:|---:|
| 1 | [astral-sh/uv](https://github.com/astral-sh/uv)<br>装 Python 包，不用再干等<br>`开发者工具` | +603 | 86.1 | 92,481 |
| 2 | [zed-industries/zed](https://github.com/zed-industries/zed)<br>打开就快，还能多人一起写代码<br>`开发者工具` | +527 | 75.3 | 95,464 |
| 3 | [jdx/mise](https://github.com/jdx/mise)<br>开发工具、环境变量、任务，一个工具管<br>`开发者工具` | +251 | 35.9 | 36,366 |
| 4 | [BurntSushi/ripgrep](https://github.com/BurntSushi/ripgrep)<br>翻遍整个目录找文字，比 grep 快<br>`开发者工具` | +203 | 29.0 | 70,118 |
| 5 | [oven-sh/bun](https://github.com/oven-sh/bun)<br>运行打包测试装包，一个工具全包<br>`开发者工具` | +167 | 23.9 | 96,816 |
| 6 | [cli/cli](https://github.com/cli/cli)<br>不开网页，命令行里处理 GitHub<br>`开发者工具` | +127 | 18.1 | 47,124 |
| 7 | [helix-editor/helix](https://github.com/helix-editor/helix)<br>语法高亮、语言服务都内置的文本编辑器<br>`开发者工具` | +95 | 13.6 | 46,951 |
| 8 | [biomejs/biome](https://github.com/biomejs/biome)<br>网页代码格式和检查，一个工具搞定<br>`开发者工具` | +73 | 10.4 | 26,168 |

<details>
<summary>本榜星标历史曲线</summary>

<a href="https://www.star-history.com/#astral-sh/uv&Date"><img src="https://api.star-history.com/svg?repos=astral-sh/uv&type=Date" width="260" alt="astral-sh/uv 的星标历史曲线"></a>

<a href="https://www.star-history.com/#zed-industries/zed&Date"><img src="https://api.star-history.com/svg?repos=zed-industries/zed&type=Date" width="260" alt="zed-industries/zed 的星标历史曲线"></a>

<a href="https://www.star-history.com/#jdx/mise&Date"><img src="https://api.star-history.com/svg?repos=jdx/mise&type=Date" width="260" alt="jdx/mise 的星标历史曲线"></a>

<a href="https://www.star-history.com/#BurntSushi/ripgrep&Date"><img src="https://api.star-history.com/svg?repos=BurntSushi/ripgrep&type=Date" width="260" alt="BurntSushi/ripgrep 的星标历史曲线"></a>

<a href="https://www.star-history.com/#oven-sh/bun&Date"><img src="https://api.star-history.com/svg?repos=oven-sh/bun&type=Date" width="260" alt="oven-sh/bun 的星标历史曲线"></a>

<a href="https://www.star-history.com/#cli/cli&Date"><img src="https://api.star-history.com/svg?repos=cli/cli&type=Date" width="260" alt="cli/cli 的星标历史曲线"></a>

<a href="https://www.star-history.com/#helix-editor/helix&Date"><img src="https://api.star-history.com/svg?repos=helix-editor/helix&type=Date" width="260" alt="helix-editor/helix 的星标历史曲线"></a>

<a href="https://www.star-history.com/#biomejs/biome&Date"><img src="https://api.star-history.com/svg?repos=biomejs/biome&type=Date" width="260" alt="biomejs/biome 的星标历史曲线"></a>

</details>

### 本月增长最快（近 30 天）

| # | 项目 | 新增星标 | 星标/天 | 总星标 |
|---|---|---:|---:|---:|
| 1 | [zed-industries/zed](https://github.com/zed-industries/zed)<br>打开就快，还能多人一起写代码<br>`开发者工具` | +3,708 | 123.6 | 95,464 |
| 2 | [astral-sh/uv](https://github.com/astral-sh/uv)<br>装 Python 包，不用再干等<br>`开发者工具` | +1,660 | 55.3 | 92,481 |
| 3 | [jdx/mise](https://github.com/jdx/mise)<br>开发工具、环境变量、任务，一个工具管<br>`开发者工具` | +1,184 | 39.5 | 36,366 |
| 4 | [BurntSushi/ripgrep](https://github.com/BurntSushi/ripgrep)<br>翻遍整个目录找文字，比 grep 快<br>`开发者工具` | +936 | 31.2 | 70,118 |
| 5 | [oven-sh/bun](https://github.com/oven-sh/bun)<br>运行打包测试装包，一个工具全包<br>`开发者工具` | +677 | 22.6 | 96,816 |
| 6 | [cli/cli](https://github.com/cli/cli)<br>不开网页，命令行里处理 GitHub<br>`开发者工具` | +476 | 15.9 | 47,124 |
| 7 | [helix-editor/helix](https://github.com/helix-editor/helix)<br>语法高亮、语言服务都内置的文本编辑器<br>`开发者工具` | +401 | 13.4 | 46,951 |
| 8 | [biomejs/biome](https://github.com/biomejs/biome)<br>网页代码格式和检查，一个工具搞定<br>`开发者工具` | +241 | 8.0 | 26,168 |

<details>
<summary>本榜星标历史曲线</summary>

<a href="https://www.star-history.com/#zed-industries/zed&Date"><img src="https://api.star-history.com/svg?repos=zed-industries/zed&type=Date" width="260" alt="zed-industries/zed 的星标历史曲线"></a>

<a href="https://www.star-history.com/#astral-sh/uv&Date"><img src="https://api.star-history.com/svg?repos=astral-sh/uv&type=Date" width="260" alt="astral-sh/uv 的星标历史曲线"></a>

<a href="https://www.star-history.com/#jdx/mise&Date"><img src="https://api.star-history.com/svg?repos=jdx/mise&type=Date" width="260" alt="jdx/mise 的星标历史曲线"></a>

<a href="https://www.star-history.com/#BurntSushi/ripgrep&Date"><img src="https://api.star-history.com/svg?repos=BurntSushi/ripgrep&type=Date" width="260" alt="BurntSushi/ripgrep 的星标历史曲线"></a>

<a href="https://www.star-history.com/#oven-sh/bun&Date"><img src="https://api.star-history.com/svg?repos=oven-sh/bun&type=Date" width="260" alt="oven-sh/bun 的星标历史曲线"></a>

<a href="https://www.star-history.com/#cli/cli&Date"><img src="https://api.star-history.com/svg?repos=cli/cli&type=Date" width="260" alt="cli/cli 的星标历史曲线"></a>

<a href="https://www.star-history.com/#helix-editor/helix&Date"><img src="https://api.star-history.com/svg?repos=helix-editor/helix&type=Date" width="260" alt="helix-editor/helix 的星标历史曲线"></a>

<a href="https://www.star-history.com/#biomejs/biome&Date"><img src="https://api.star-history.com/svg?repos=biomejs/biome&type=Date" width="260" alt="biomejs/biome 的星标历史曲线"></a>

</details>

### 今年增长最快（近 365 天）

| # | 项目 | 新增星标 | 星标/天 | 总星标 |
|---|---|---:|---:|---:|
| 1 | [zed-industries/zed](https://github.com/zed-industries/zed)<br>打开就快，还能多人一起写代码<br>`开发者工具` | +27,435 | 75.2 | 95,464 |
| 2 | [astral-sh/uv](https://github.com/astral-sh/uv)<br>装 Python 包，不用再干等<br>`开发者工具` | +20,738 | 56.8 | 92,481 |
| 3 | [oven-sh/bun](https://github.com/oven-sh/bun)<br>运行打包测试装包，一个工具全包<br>`开发者工具` | +16,533 | 45.3 | 96,816 |
| 4 | [jdx/mise](https://github.com/jdx/mise)<br>开发工具、环境变量、任务，一个工具管<br>`开发者工具` | +15,306 | 41.9 | 36,366 |
| 5 | [BurntSushi/ripgrep](https://github.com/BurntSushi/ripgrep)<br>翻遍整个目录找文字，比 grep 快<br>`开发者工具` | +13,350 | 36.6 | 70,118 |
| 6 | [helix-editor/helix](https://github.com/helix-editor/helix)<br>语法高亮、语言服务都内置的文本编辑器<br>`开发者工具` | +6,444 | 17.7 | 46,951 |
| 7 | [cli/cli](https://github.com/cli/cli)<br>不开网页，命令行里处理 GitHub<br>`开发者工具` | +6,346 | 17.4 | 47,124 |
| 8 | [biomejs/biome](https://github.com/biomejs/biome)<br>网页代码格式和检查，一个工具搞定<br>`开发者工具` | +4,393 | 12.0 | 26,168 |

<details>
<summary>本榜星标历史曲线</summary>

<a href="https://www.star-history.com/#zed-industries/zed&Date"><img src="https://api.star-history.com/svg?repos=zed-industries/zed&type=Date" width="260" alt="zed-industries/zed 的星标历史曲线"></a>

<a href="https://www.star-history.com/#astral-sh/uv&Date"><img src="https://api.star-history.com/svg?repos=astral-sh/uv&type=Date" width="260" alt="astral-sh/uv 的星标历史曲线"></a>

<a href="https://www.star-history.com/#oven-sh/bun&Date"><img src="https://api.star-history.com/svg?repos=oven-sh/bun&type=Date" width="260" alt="oven-sh/bun 的星标历史曲线"></a>

<a href="https://www.star-history.com/#jdx/mise&Date"><img src="https://api.star-history.com/svg?repos=jdx/mise&type=Date" width="260" alt="jdx/mise 的星标历史曲线"></a>

<a href="https://www.star-history.com/#BurntSushi/ripgrep&Date"><img src="https://api.star-history.com/svg?repos=BurntSushi/ripgrep&type=Date" width="260" alt="BurntSushi/ripgrep 的星标历史曲线"></a>

<a href="https://www.star-history.com/#helix-editor/helix&Date"><img src="https://api.star-history.com/svg?repos=helix-editor/helix&type=Date" width="260" alt="helix-editor/helix 的星标历史曲线"></a>

<a href="https://www.star-history.com/#cli/cli&Date"><img src="https://api.star-history.com/svg?repos=cli/cli&type=Date" width="260" alt="cli/cli 的星标历史曲线"></a>

<a href="https://www.star-history.com/#biomejs/biome&Date"><img src="https://api.star-history.com/svg?repos=biomejs/biome&type=Date" width="260" alt="biomejs/biome 的星标历史曲线"></a>

</details>

### 总星标数（历史累计）

| # | 项目 | 总星标 |
|---|---|---:|
| 1 | [oven-sh/bun](https://github.com/oven-sh/bun)<br>运行打包测试装包，一个工具全包<br>`开发者工具` | 96,816 |
| 2 | [zed-industries/zed](https://github.com/zed-industries/zed)<br>打开就快，还能多人一起写代码<br>`开发者工具` | 95,464 |
| 3 | [astral-sh/uv](https://github.com/astral-sh/uv)<br>装 Python 包，不用再干等<br>`开发者工具` | 92,481 |
| 4 | [BurntSushi/ripgrep](https://github.com/BurntSushi/ripgrep)<br>翻遍整个目录找文字，比 grep 快<br>`开发者工具` | 70,118 |
| 5 | [cli/cli](https://github.com/cli/cli)<br>不开网页，命令行里处理 GitHub<br>`开发者工具` | 47,124 |
| 6 | [helix-editor/helix](https://github.com/helix-editor/helix)<br>语法高亮、语言服务都内置的文本编辑器<br>`开发者工具` | 46,951 |
| 7 | [jdx/mise](https://github.com/jdx/mise)<br>开发工具、环境变量、任务，一个工具管<br>`开发者工具` | 36,366 |
| 8 | [biomejs/biome](https://github.com/biomejs/biome)<br>网页代码格式和检查，一个工具搞定<br>`开发者工具` | 26,168 |

<details>
<summary>本榜星标历史曲线</summary>

<a href="https://www.star-history.com/#oven-sh/bun&Date"><img src="https://api.star-history.com/svg?repos=oven-sh/bun&type=Date" width="260" alt="oven-sh/bun 的星标历史曲线"></a>

<a href="https://www.star-history.com/#zed-industries/zed&Date"><img src="https://api.star-history.com/svg?repos=zed-industries/zed&type=Date" width="260" alt="zed-industries/zed 的星标历史曲线"></a>

<a href="https://www.star-history.com/#astral-sh/uv&Date"><img src="https://api.star-history.com/svg?repos=astral-sh/uv&type=Date" width="260" alt="astral-sh/uv 的星标历史曲线"></a>

<a href="https://www.star-history.com/#BurntSushi/ripgrep&Date"><img src="https://api.star-history.com/svg?repos=BurntSushi/ripgrep&type=Date" width="260" alt="BurntSushi/ripgrep 的星标历史曲线"></a>

<a href="https://www.star-history.com/#cli/cli&Date"><img src="https://api.star-history.com/svg?repos=cli/cli&type=Date" width="260" alt="cli/cli 的星标历史曲线"></a>

<a href="https://www.star-history.com/#helix-editor/helix&Date"><img src="https://api.star-history.com/svg?repos=helix-editor/helix&type=Date" width="260" alt="helix-editor/helix 的星标历史曲线"></a>

<a href="https://www.star-history.com/#jdx/mise&Date"><img src="https://api.star-history.com/svg?repos=jdx/mise&type=Date" width="260" alt="jdx/mise 的星标历史曲线"></a>

<a href="https://www.star-history.com/#biomejs/biome&Date"><img src="https://api.star-history.com/svg?repos=biomejs/biome&type=Date" width="260" alt="biomejs/biome 的星标历史曲线"></a>

</details>

## 安全

> 漏洞扫描、静态分析、供应链与运行时安全

### 最热新仓库（近 7 天内创建）

本次运行中没有符合条件的新仓库。

### 本周增长最快（近 7 天）

| # | 项目 | 新增星标 | 星标/天 | 总星标 |
|---|---|---:|---:|---:|
| 1 | [projectdiscovery/nuclei](https://github.com/projectdiscovery/nuclei)<br>写个模板，就能批量扫漏洞<br>`安全` | +284 | 40.6 | 33,169 |
| 2 | [aquasecurity/trivy](https://github.com/aquasecurity/trivy)<br>容器和代码仓，一次扫完安全问题<br>`安全` | +277 | 39.6 | 39,592 |
| 3 | [semgrep/semgrep](https://github.com/semgrep/semgrep)<br>代码里的问题，提交前先揪出来<br>`安全` | +205 | 29.3 | 17,874 |
| 4 | [OWASP/CheatSheetSeries](https://github.com/OWASP/CheatSheetSeries)<br>应用安全怎么做，看这套速查表<br>`安全` | +108 | 15.4 | 34,152 |
| 5 | [google/osv-scanner](https://github.com/google/osv-scanner)<br>用的依赖安不安全，扫一下就知道<br>`安全` | +68 | 9.7 | 11,582 |
| 6 | [anchore/grype](https://github.com/anchore/grype)<br>容器镜像有没有漏洞，扫一下就知道<br>`安全` | +53 | 7.6 | 13,311 |
| 7 | [falcosecurity/falco](https://github.com/falcosecurity/falco)<br>云上有异常，第一时间知道<br>`安全` | +16 | 2.3 | 9,594 |
| 8 | [securego/gosec](https://github.com/securego/gosec)<br>Go 代码的安全隐患，扫一遍就知道<br>`安全` | +10 | 1.4 | 9,012 |

<details>
<summary>本榜星标历史曲线</summary>

<a href="https://www.star-history.com/#projectdiscovery/nuclei&Date"><img src="https://api.star-history.com/svg?repos=projectdiscovery/nuclei&type=Date" width="260" alt="projectdiscovery/nuclei 的星标历史曲线"></a>

<a href="https://www.star-history.com/#aquasecurity/trivy&Date"><img src="https://api.star-history.com/svg?repos=aquasecurity/trivy&type=Date" width="260" alt="aquasecurity/trivy 的星标历史曲线"></a>

<a href="https://www.star-history.com/#semgrep/semgrep&Date"><img src="https://api.star-history.com/svg?repos=semgrep/semgrep&type=Date" width="260" alt="semgrep/semgrep 的星标历史曲线"></a>

<a href="https://www.star-history.com/#OWASP/CheatSheetSeries&Date"><img src="https://api.star-history.com/svg?repos=OWASP/CheatSheetSeries&type=Date" width="260" alt="OWASP/CheatSheetSeries 的星标历史曲线"></a>

<a href="https://www.star-history.com/#google/osv-scanner&Date"><img src="https://api.star-history.com/svg?repos=google/osv-scanner&type=Date" width="260" alt="google/osv-scanner 的星标历史曲线"></a>

<a href="https://www.star-history.com/#anchore/grype&Date"><img src="https://api.star-history.com/svg?repos=anchore/grype&type=Date" width="260" alt="anchore/grype 的星标历史曲线"></a>

<a href="https://www.star-history.com/#falcosecurity/falco&Date"><img src="https://api.star-history.com/svg?repos=falcosecurity/falco&type=Date" width="260" alt="falcosecurity/falco 的星标历史曲线"></a>

<a href="https://www.star-history.com/#securego/gosec&Date"><img src="https://api.star-history.com/svg?repos=securego/gosec&type=Date" width="260" alt="securego/gosec 的星标历史曲线"></a>

</details>

### 本月增长最快（近 30 天）

| # | 项目 | 新增星标 | 星标/天 | 总星标 |
|---|---|---:|---:|---:|
| 1 | [aquasecurity/trivy](https://github.com/aquasecurity/trivy)<br>容器和代码仓，一次扫完安全问题<br>`安全` | +1,055 | 35.2 | 39,592 |
| 2 | [projectdiscovery/nuclei](https://github.com/projectdiscovery/nuclei)<br>写个模板，就能批量扫漏洞<br>`安全` | +1,024 | 34.1 | 33,169 |
| 3 | [semgrep/semgrep](https://github.com/semgrep/semgrep)<br>代码里的问题，提交前先揪出来<br>`安全` | +715 | 23.8 | 17,874 |
| 4 | [OWASP/CheatSheetSeries](https://github.com/OWASP/CheatSheetSeries)<br>应用安全怎么做，看这套速查表<br>`安全` | +489 | 16.3 | 34,152 |
| 5 | [google/osv-scanner](https://github.com/google/osv-scanner)<br>用的依赖安不安全，扫一下就知道<br>`安全` | +367 | 12.2 | 11,582 |
| 6 | [anchore/grype](https://github.com/anchore/grype)<br>容器镜像有没有漏洞，扫一下就知道<br>`安全` | +254 | 8.5 | 13,311 |
| 7 | [falcosecurity/falco](https://github.com/falcosecurity/falco)<br>云上有异常，第一时间知道<br>`安全` | +98 | 3.3 | 9,594 |
| 8 | [securego/gosec](https://github.com/securego/gosec)<br>Go 代码的安全隐患，扫一遍就知道<br>`安全` | +39 | 1.3 | 9,012 |

<details>
<summary>本榜星标历史曲线</summary>

<a href="https://www.star-history.com/#aquasecurity/trivy&Date"><img src="https://api.star-history.com/svg?repos=aquasecurity/trivy&type=Date" width="260" alt="aquasecurity/trivy 的星标历史曲线"></a>

<a href="https://www.star-history.com/#projectdiscovery/nuclei&Date"><img src="https://api.star-history.com/svg?repos=projectdiscovery/nuclei&type=Date" width="260" alt="projectdiscovery/nuclei 的星标历史曲线"></a>

<a href="https://www.star-history.com/#semgrep/semgrep&Date"><img src="https://api.star-history.com/svg?repos=semgrep/semgrep&type=Date" width="260" alt="semgrep/semgrep 的星标历史曲线"></a>

<a href="https://www.star-history.com/#OWASP/CheatSheetSeries&Date"><img src="https://api.star-history.com/svg?repos=OWASP/CheatSheetSeries&type=Date" width="260" alt="OWASP/CheatSheetSeries 的星标历史曲线"></a>

<a href="https://www.star-history.com/#google/osv-scanner&Date"><img src="https://api.star-history.com/svg?repos=google/osv-scanner&type=Date" width="260" alt="google/osv-scanner 的星标历史曲线"></a>

<a href="https://www.star-history.com/#anchore/grype&Date"><img src="https://api.star-history.com/svg?repos=anchore/grype&type=Date" width="260" alt="anchore/grype 的星标历史曲线"></a>

<a href="https://www.star-history.com/#falcosecurity/falco&Date"><img src="https://api.star-history.com/svg?repos=falcosecurity/falco&type=Date" width="260" alt="falcosecurity/falco 的星标历史曲线"></a>

<a href="https://www.star-history.com/#securego/gosec&Date"><img src="https://api.star-history.com/svg?repos=securego/gosec&type=Date" width="260" alt="securego/gosec 的星标历史曲线"></a>

</details>

### 今年增长最快（近 365 天）

| # | 项目 | 新增星标 | 星标/天 | 总星标 |
|---|---|---:|---:|---:|
| 1 | [aquasecurity/trivy](https://github.com/aquasecurity/trivy)<br>容器和代码仓，一次扫完安全问题<br>`安全` | +10,548 | 28.9 | 39,592 |
| 2 | [projectdiscovery/nuclei](https://github.com/projectdiscovery/nuclei)<br>写个模板，就能批量扫漏洞<br>`安全` | +7,936 | 21.7 | 33,169 |
| 3 | [semgrep/semgrep](https://github.com/semgrep/semgrep)<br>代码里的问题，提交前先揪出来<br>`安全` | +4,656 | 12.8 | 17,874 |
| 4 | [OWASP/CheatSheetSeries](https://github.com/OWASP/CheatSheetSeries)<br>应用安全怎么做，看这套速查表<br>`安全` | +3,690 | 10.1 | 34,152 |
| 5 | [google/osv-scanner](https://github.com/google/osv-scanner)<br>用的依赖安不安全，扫一下就知道<br>`安全` | +3,616 | 9.9 | 11,582 |
| 6 | [anchore/grype](https://github.com/anchore/grype)<br>容器镜像有没有漏洞，扫一下就知道<br>`安全` | +2,410 | 6.6 | 13,311 |
| 7 | [falcosecurity/falco](https://github.com/falcosecurity/falco)<br>云上有异常，第一时间知道<br>`安全` | +1,267 | 3.5 | 9,594 |
| 8 | [securego/gosec](https://github.com/securego/gosec)<br>Go 代码的安全隐患，扫一遍就知道<br>`安全` | +557 | 1.5 | 9,012 |

<details>
<summary>本榜星标历史曲线</summary>

<a href="https://www.star-history.com/#aquasecurity/trivy&Date"><img src="https://api.star-history.com/svg?repos=aquasecurity/trivy&type=Date" width="260" alt="aquasecurity/trivy 的星标历史曲线"></a>

<a href="https://www.star-history.com/#projectdiscovery/nuclei&Date"><img src="https://api.star-history.com/svg?repos=projectdiscovery/nuclei&type=Date" width="260" alt="projectdiscovery/nuclei 的星标历史曲线"></a>

<a href="https://www.star-history.com/#semgrep/semgrep&Date"><img src="https://api.star-history.com/svg?repos=semgrep/semgrep&type=Date" width="260" alt="semgrep/semgrep 的星标历史曲线"></a>

<a href="https://www.star-history.com/#OWASP/CheatSheetSeries&Date"><img src="https://api.star-history.com/svg?repos=OWASP/CheatSheetSeries&type=Date" width="260" alt="OWASP/CheatSheetSeries 的星标历史曲线"></a>

<a href="https://www.star-history.com/#google/osv-scanner&Date"><img src="https://api.star-history.com/svg?repos=google/osv-scanner&type=Date" width="260" alt="google/osv-scanner 的星标历史曲线"></a>

<a href="https://www.star-history.com/#anchore/grype&Date"><img src="https://api.star-history.com/svg?repos=anchore/grype&type=Date" width="260" alt="anchore/grype 的星标历史曲线"></a>

<a href="https://www.star-history.com/#falcosecurity/falco&Date"><img src="https://api.star-history.com/svg?repos=falcosecurity/falco&type=Date" width="260" alt="falcosecurity/falco 的星标历史曲线"></a>

<a href="https://www.star-history.com/#securego/gosec&Date"><img src="https://api.star-history.com/svg?repos=securego/gosec&type=Date" width="260" alt="securego/gosec 的星标历史曲线"></a>

</details>

### 总星标数（历史累计）

| # | 项目 | 总星标 |
|---|---|---:|
| 1 | [aquasecurity/trivy](https://github.com/aquasecurity/trivy)<br>容器和代码仓，一次扫完安全问题<br>`安全` | 39,592 |
| 2 | [OWASP/CheatSheetSeries](https://github.com/OWASP/CheatSheetSeries)<br>应用安全怎么做，看这套速查表<br>`安全` | 34,152 |
| 3 | [projectdiscovery/nuclei](https://github.com/projectdiscovery/nuclei)<br>写个模板，就能批量扫漏洞<br>`安全` | 33,169 |
| 4 | [semgrep/semgrep](https://github.com/semgrep/semgrep)<br>代码里的问题，提交前先揪出来<br>`安全` | 17,874 |
| 5 | [anchore/grype](https://github.com/anchore/grype)<br>容器镜像有没有漏洞，扫一下就知道<br>`安全` | 13,311 |
| 6 | [google/osv-scanner](https://github.com/google/osv-scanner)<br>用的依赖安不安全，扫一下就知道<br>`安全` | 11,582 |
| 7 | [falcosecurity/falco](https://github.com/falcosecurity/falco)<br>云上有异常，第一时间知道<br>`安全` | 9,594 |
| 8 | [securego/gosec](https://github.com/securego/gosec)<br>Go 代码的安全隐患，扫一遍就知道<br>`安全` | 9,012 |

<details>
<summary>本榜星标历史曲线</summary>

<a href="https://www.star-history.com/#aquasecurity/trivy&Date"><img src="https://api.star-history.com/svg?repos=aquasecurity/trivy&type=Date" width="260" alt="aquasecurity/trivy 的星标历史曲线"></a>

<a href="https://www.star-history.com/#OWASP/CheatSheetSeries&Date"><img src="https://api.star-history.com/svg?repos=OWASP/CheatSheetSeries&type=Date" width="260" alt="OWASP/CheatSheetSeries 的星标历史曲线"></a>

<a href="https://www.star-history.com/#projectdiscovery/nuclei&Date"><img src="https://api.star-history.com/svg?repos=projectdiscovery/nuclei&type=Date" width="260" alt="projectdiscovery/nuclei 的星标历史曲线"></a>

<a href="https://www.star-history.com/#semgrep/semgrep&Date"><img src="https://api.star-history.com/svg?repos=semgrep/semgrep&type=Date" width="260" alt="semgrep/semgrep 的星标历史曲线"></a>

<a href="https://www.star-history.com/#anchore/grype&Date"><img src="https://api.star-history.com/svg?repos=anchore/grype&type=Date" width="260" alt="anchore/grype 的星标历史曲线"></a>

<a href="https://www.star-history.com/#google/osv-scanner&Date"><img src="https://api.star-history.com/svg?repos=google/osv-scanner&type=Date" width="260" alt="google/osv-scanner 的星标历史曲线"></a>

<a href="https://www.star-history.com/#falcosecurity/falco&Date"><img src="https://api.star-history.com/svg?repos=falcosecurity/falco&type=Date" width="260" alt="falcosecurity/falco 的星标历史曲线"></a>

<a href="https://www.star-history.com/#securego/gosec&Date"><img src="https://api.star-history.com/svg?repos=securego/gosec&type=Date" width="260" alt="securego/gosec 的星标历史曲线"></a>

</details>

## Web / 前端

> 前端框架、UI 组件库、CSS 与浏览器工具

### 最热新仓库（近 7 天内创建）

| # | 项目 | 创建时间（UTC） | 总星标 | 星标/天 |
|---|---|---|---:|---:|
| 1 | [carlperry-88/devlabs](https://github.com/carlperry-88/devlabs) | 2026-11-20<br><sub>1.0 天</sub> | 106 | 106.0 |
| 2 | [chuxuan861119/zhichan-xiaozhan-work](https://github.com/chuxuan861119/zhichan-xiaozhan-work)<br>面向中国专利撰写的专业编辑器，支持发明、实用新型五书编辑和外观设计专利材料整理，提供专利库管理、二维 CAD、文档检查、AI 辅助及 Word/PDF 导出。GPL-3.0 开源。 | 2026-11-17<br><sub>4.1 天</sub> | 130 | 31.7 |
| 3 | [rohit3a/t3-clawd](https://github.com/rohit3a/t3-clawd)<br>不用 fork，单文件就能换主题 | 2026-11-14<br><sub>6.7 天</sub> | 139 | 20.7 |
| 4 | [manuelgscom/inside-llm](https://github.com/manuelgscom/inside-llm)<br>浏览器内GGUF量化与采样检查工具 | 2026-11-15<br><sub>5.8 天</sub> | 115 | 19.7 |
| 5 | [johnnablea29-art/stratgies-indicator](https://github.com/johnnablea29-art/stratgies-indicator)<br>用于重复执行机器人任务的自动化脚本 | 2026-11-15<br><sub>5.8 天</sub> | 153 | 26.6 |
| 6 | [ELEL182/bunny-hopping-mod](https://github.com/ELEL182/bunny-hopping-mod)<br>掌握连跳技巧，靠惯性高速移动 | 2026-11-15<br><sub>5.8 天</sub> | 153 | 26.3 |

<details>
<summary>本榜星标历史曲线</summary>

<a href="https://www.star-history.com/#carlperry-88/devlabs&Date"><img src="https://api.star-history.com/svg?repos=carlperry-88/devlabs&type=Date" width="260" alt="carlperry-88/devlabs 的星标历史曲线"></a>

<a href="https://www.star-history.com/#chuxuan861119/zhichan-xiaozhan-work&Date"><img src="https://api.star-history.com/svg?repos=chuxuan861119/zhichan-xiaozhan-work&type=Date" width="260" alt="chuxuan861119/zhichan-xiaozhan-work 的星标历史曲线"></a>

<a href="https://www.star-history.com/#rohit3a/t3-clawd&Date"><img src="https://api.star-history.com/svg?repos=rohit3a/t3-clawd&type=Date" width="260" alt="rohit3a/t3-clawd 的星标历史曲线"></a>

<a href="https://www.star-history.com/#manuelgscom/inside-llm&Date"><img src="https://api.star-history.com/svg?repos=manuelgscom/inside-llm&type=Date" width="260" alt="manuelgscom/inside-llm 的星标历史曲线"></a>

<a href="https://www.star-history.com/#johnnablea29-art/stratgies-indicator&Date"><img src="https://api.star-history.com/svg?repos=johnnablea29-art/stratgies-indicator&type=Date" width="260" alt="johnnablea29-art/stratgies-indicator 的星标历史曲线"></a>

<a href="https://www.star-history.com/#ELEL182/bunny-hopping-mod&Date"><img src="https://api.star-history.com/svg?repos=ELEL182/bunny-hopping-mod&type=Date" width="260" alt="ELEL182/bunny-hopping-mod 的星标历史曲线"></a>

</details>

### 本周增长最快（近 7 天）

| # | 项目 | 新增星标 | 星标/天 | 总星标 |
|---|---|---:|---:|---:|
| 1 | [sveltejs/svelte](https://github.com/sveltejs/svelte)<br>你写组件，编译器变出高效的网页代码<br>`Web / 前端` | +1,201 | 171.6 | 89,844 |
| 2 | [shadcn-ui/ui](https://github.com/shadcn-ui/ui)<br>好看的组件，代码归你，随便改<br>`Web / 前端` | +568 | 81.1 | 128,684 |
| 3 | [facebook/react](https://github.com/facebook/react)<br>网页和 App 界面，都能用它来搭<br>`Web / 前端` | +383 | 54.7 | 252,843 |
| 4 | [vercel/next.js](https://github.com/vercel/next.js)<br>用 React 做完整网站，从前到后<br>`Web / 前端` | +191 | 27.3 | 143,631 |
| 5 | [withastro/astro](https://github.com/withastro/astro)<br>做内容型网站，页面输出更轻量<br>`Web / 前端` | +179 | 25.6 | 64,103 |
| 6 | [tailwindlabs/tailwindcss](https://github.com/tailwindlabs/tailwindcss)<br>不写一大堆 CSS，也能做定制界面<br>`Web / 前端` | +164 | 23.4 | 98,719 |
| 7 | [vuejs/core](https://github.com/vuejs/core)<br>从一个小页面开始，用多少学多少<br>`Web / 前端` | +119 | 17.0 | 55,060 |
| 8 | [tanstack/query](https://github.com/tanstack/query)<br>请求数据和缓存，交给它管<br>`Web / 前端` | +55 | 7.9 | 50,605 |

<details>
<summary>本榜星标历史曲线</summary>

<a href="https://www.star-history.com/#sveltejs/svelte&Date"><img src="https://api.star-history.com/svg?repos=sveltejs/svelte&type=Date" width="260" alt="sveltejs/svelte 的星标历史曲线"></a>

<a href="https://www.star-history.com/#shadcn-ui/ui&Date"><img src="https://api.star-history.com/svg?repos=shadcn-ui/ui&type=Date" width="260" alt="shadcn-ui/ui 的星标历史曲线"></a>

<a href="https://www.star-history.com/#facebook/react&Date"><img src="https://api.star-history.com/svg?repos=facebook/react&type=Date" width="260" alt="facebook/react 的星标历史曲线"></a>

<a href="https://www.star-history.com/#vercel/next.js&Date"><img src="https://api.star-history.com/svg?repos=vercel/next.js&type=Date" width="260" alt="vercel/next.js 的星标历史曲线"></a>

<a href="https://www.star-history.com/#withastro/astro&Date"><img src="https://api.star-history.com/svg?repos=withastro/astro&type=Date" width="260" alt="withastro/astro 的星标历史曲线"></a>

<a href="https://www.star-history.com/#tailwindlabs/tailwindcss&Date"><img src="https://api.star-history.com/svg?repos=tailwindlabs/tailwindcss&type=Date" width="260" alt="tailwindlabs/tailwindcss 的星标历史曲线"></a>

<a href="https://www.star-history.com/#vuejs/core&Date"><img src="https://api.star-history.com/svg?repos=vuejs/core&type=Date" width="260" alt="vuejs/core 的星标历史曲线"></a>

<a href="https://www.star-history.com/#tanstack/query&Date"><img src="https://api.star-history.com/svg?repos=tanstack/query&type=Date" width="260" alt="tanstack/query 的星标历史曲线"></a>

</details>

### 本月增长最快（近 30 天）

| # | 项目 | 新增星标 | 星标/天 | 总星标 |
|---|---|---:|---:|---:|
| 1 | [shadcn-ui/ui](https://github.com/shadcn-ui/ui)<br>好看的组件，代码归你，随便改<br>`Web / 前端` | +2,760 | 92.0 | 128,684 |
| 2 | [facebook/react](https://github.com/facebook/react)<br>网页和 App 界面，都能用它来搭<br>`Web / 前端` | +1,741 | 58.0 | 252,843 |
| 3 | [sveltejs/svelte](https://github.com/sveltejs/svelte)<br>你写组件，编译器变出高效的网页代码<br>`Web / 前端` | +1,592 | 53.1 | 89,844 |
| 4 | [tailwindlabs/tailwindcss](https://github.com/tailwindlabs/tailwindcss)<br>不写一大堆 CSS，也能做定制界面<br>`Web / 前端` | +973 | 32.4 | 98,719 |
| 5 | [withastro/astro](https://github.com/withastro/astro)<br>做内容型网站，页面输出更轻量<br>`Web / 前端` | +816 | 27.2 | 64,103 |
| 6 | [vercel/next.js](https://github.com/vercel/next.js)<br>用 React 做完整网站，从前到后<br>`Web / 前端` | +785 | 26.2 | 143,631 |
| 7 | [vuejs/core](https://github.com/vuejs/core)<br>从一个小页面开始，用多少学多少<br>`Web / 前端` | +452 | 15.1 | 55,060 |
| 8 | [tanstack/query](https://github.com/tanstack/query)<br>请求数据和缓存，交给它管<br>`Web / 前端` | +199 | 6.6 | 50,605 |

<details>
<summary>本榜星标历史曲线</summary>

<a href="https://www.star-history.com/#shadcn-ui/ui&Date"><img src="https://api.star-history.com/svg?repos=shadcn-ui/ui&type=Date" width="260" alt="shadcn-ui/ui 的星标历史曲线"></a>

<a href="https://www.star-history.com/#facebook/react&Date"><img src="https://api.star-history.com/svg?repos=facebook/react&type=Date" width="260" alt="facebook/react 的星标历史曲线"></a>

<a href="https://www.star-history.com/#sveltejs/svelte&Date"><img src="https://api.star-history.com/svg?repos=sveltejs/svelte&type=Date" width="260" alt="sveltejs/svelte 的星标历史曲线"></a>

<a href="https://www.star-history.com/#tailwindlabs/tailwindcss&Date"><img src="https://api.star-history.com/svg?repos=tailwindlabs/tailwindcss&type=Date" width="260" alt="tailwindlabs/tailwindcss 的星标历史曲线"></a>

<a href="https://www.star-history.com/#withastro/astro&Date"><img src="https://api.star-history.com/svg?repos=withastro/astro&type=Date" width="260" alt="withastro/astro 的星标历史曲线"></a>

<a href="https://www.star-history.com/#vercel/next.js&Date"><img src="https://api.star-history.com/svg?repos=vercel/next.js&type=Date" width="260" alt="vercel/next.js 的星标历史曲线"></a>

<a href="https://www.star-history.com/#vuejs/core&Date"><img src="https://api.star-history.com/svg?repos=vuejs/core&type=Date" width="260" alt="vuejs/core 的星标历史曲线"></a>

<a href="https://www.star-history.com/#tanstack/query&Date"><img src="https://api.star-history.com/svg?repos=tanstack/query&type=Date" width="260" alt="tanstack/query 的星标历史曲线"></a>

</details>

### 今年增长最快（近 365 天）

| # | 项目 | 新增星标 | 星标/天 | 总星标 |
|---|---|---:|---:|---:|
| 1 | [shadcn-ui/ui](https://github.com/shadcn-ui/ui)<br>好看的组件，代码归你，随便改<br>`Web / 前端` | +30,258 | 82.9 | 128,684 |
| 2 | [facebook/react](https://github.com/facebook/react)<br>网页和 App 界面，都能用它来搭<br>`Web / 前端` | +15,757 | 43.2 | 252,843 |
| 3 | [withastro/astro](https://github.com/withastro/astro)<br>做内容型网站，页面输出更轻量<br>`Web / 前端` | +10,601 | 29.0 | 64,103 |
| 4 | [vercel/next.js](https://github.com/vercel/next.js)<br>用 React 做完整网站，从前到后<br>`Web / 前端` | +10,382 | 28.4 | 143,631 |
| 5 | [tailwindlabs/tailwindcss](https://github.com/tailwindlabs/tailwindcss)<br>不写一大堆 CSS，也能做定制界面<br>`Web / 前端` | +8,918 | 24.4 | 98,719 |
| 6 | [sveltejs/svelte](https://github.com/sveltejs/svelte)<br>你写组件，编译器变出高效的网页代码<br>`Web / 前端` | +6,227 | 17.1 | 89,844 |
| 7 | [tanstack/query](https://github.com/tanstack/query)<br>请求数据和缓存，交给它管<br>`Web / 前端` | +3,712 | 10.2 | 50,605 |
| 8 | [vuejs/core](https://github.com/vuejs/core)<br>从一个小页面开始，用多少学多少<br>`Web / 前端` | +3,701 | 10.1 | 55,060 |

<details>
<summary>本榜星标历史曲线</summary>

<a href="https://www.star-history.com/#shadcn-ui/ui&Date"><img src="https://api.star-history.com/svg?repos=shadcn-ui/ui&type=Date" width="260" alt="shadcn-ui/ui 的星标历史曲线"></a>

<a href="https://www.star-history.com/#facebook/react&Date"><img src="https://api.star-history.com/svg?repos=facebook/react&type=Date" width="260" alt="facebook/react 的星标历史曲线"></a>

<a href="https://www.star-history.com/#withastro/astro&Date"><img src="https://api.star-history.com/svg?repos=withastro/astro&type=Date" width="260" alt="withastro/astro 的星标历史曲线"></a>

<a href="https://www.star-history.com/#vercel/next.js&Date"><img src="https://api.star-history.com/svg?repos=vercel/next.js&type=Date" width="260" alt="vercel/next.js 的星标历史曲线"></a>

<a href="https://www.star-history.com/#tailwindlabs/tailwindcss&Date"><img src="https://api.star-history.com/svg?repos=tailwindlabs/tailwindcss&type=Date" width="260" alt="tailwindlabs/tailwindcss 的星标历史曲线"></a>

<a href="https://www.star-history.com/#sveltejs/svelte&Date"><img src="https://api.star-history.com/svg?repos=sveltejs/svelte&type=Date" width="260" alt="sveltejs/svelte 的星标历史曲线"></a>

<a href="https://www.star-history.com/#tanstack/query&Date"><img src="https://api.star-history.com/svg?repos=tanstack/query&type=Date" width="260" alt="tanstack/query 的星标历史曲线"></a>

<a href="https://www.star-history.com/#vuejs/core&Date"><img src="https://api.star-history.com/svg?repos=vuejs/core&type=Date" width="260" alt="vuejs/core 的星标历史曲线"></a>

</details>

### 总星标数（历史累计）

| # | 项目 | 总星标 |
|---|---|---:|
| 1 | [facebook/react](https://github.com/facebook/react)<br>网页和 App 界面，都能用它来搭<br>`Web / 前端` | 252,843 |
| 2 | [vercel/next.js](https://github.com/vercel/next.js)<br>用 React 做完整网站，从前到后<br>`Web / 前端` | 143,631 |
| 3 | [shadcn-ui/ui](https://github.com/shadcn-ui/ui)<br>好看的组件，代码归你，随便改<br>`Web / 前端` | 128,684 |
| 4 | [tailwindlabs/tailwindcss](https://github.com/tailwindlabs/tailwindcss)<br>不写一大堆 CSS，也能做定制界面<br>`Web / 前端` | 98,719 |
| 5 | [sveltejs/svelte](https://github.com/sveltejs/svelte)<br>你写组件，编译器变出高效的网页代码<br>`Web / 前端` | 89,844 |
| 6 | [withastro/astro](https://github.com/withastro/astro)<br>做内容型网站，页面输出更轻量<br>`Web / 前端` | 64,103 |
| 7 | [vuejs/core](https://github.com/vuejs/core)<br>从一个小页面开始，用多少学多少<br>`Web / 前端` | 55,060 |
| 8 | [tanstack/query](https://github.com/tanstack/query)<br>请求数据和缓存，交给它管<br>`Web / 前端` | 50,605 |

<details>
<summary>本榜星标历史曲线</summary>

<a href="https://www.star-history.com/#facebook/react&Date"><img src="https://api.star-history.com/svg?repos=facebook/react&type=Date" width="260" alt="facebook/react 的星标历史曲线"></a>

<a href="https://www.star-history.com/#vercel/next.js&Date"><img src="https://api.star-history.com/svg?repos=vercel/next.js&type=Date" width="260" alt="vercel/next.js 的星标历史曲线"></a>

<a href="https://www.star-history.com/#shadcn-ui/ui&Date"><img src="https://api.star-history.com/svg?repos=shadcn-ui/ui&type=Date" width="260" alt="shadcn-ui/ui 的星标历史曲线"></a>

<a href="https://www.star-history.com/#tailwindlabs/tailwindcss&Date"><img src="https://api.star-history.com/svg?repos=tailwindlabs/tailwindcss&type=Date" width="260" alt="tailwindlabs/tailwindcss 的星标历史曲线"></a>

<a href="https://www.star-history.com/#sveltejs/svelte&Date"><img src="https://api.star-history.com/svg?repos=sveltejs/svelte&type=Date" width="260" alt="sveltejs/svelte 的星标历史曲线"></a>

<a href="https://www.star-history.com/#withastro/astro&Date"><img src="https://api.star-history.com/svg?repos=withastro/astro&type=Date" width="260" alt="withastro/astro 的星标历史曲线"></a>

<a href="https://www.star-history.com/#vuejs/core&Date"><img src="https://api.star-history.com/svg?repos=vuejs/core&type=Date" width="260" alt="vuejs/core 的星标历史曲线"></a>

<a href="https://www.star-history.com/#tanstack/query&Date"><img src="https://api.star-history.com/svg?repos=tanstack/query&type=Date" width="260" alt="tanstack/query 的星标历史曲线"></a>

</details>

## 基础设施

> 容器、Kubernetes、云、网络与可观测性

### 最热新仓库（近 7 天内创建）

| # | 项目 | 创建时间（UTC） | 总星标 | 星标/天 |
|---|---|---|---:|---:|
| 1 | [replit/datacat](https://github.com/replit/datacat)<br>想自己做监控？自托管仪表盘与告警 | 2026-11-17<br><sub>4.5 天</sub> | 488 | 108.3 |
| 2 | [piomin/ai-software-factory](https://github.com/piomin/ai-software-factory)<br>AI Software Factory running on Kubernetes / OpenShift with Tekton and vLLM | 2026-11-18<br><sub>2.7 天</sub> | 114 | 42.6 |
| 3 | [hackclub/orchard](https://github.com/hackclub/orchard)<br>部署太烦？一条命令从Git发到服务器 | 2026-11-17<br><sub>4.5 天</sub> | 115 | 25.6 |
| 4 | [Realmeshowroom/jet-reports-skill](https://github.com/Realmeshowroom/jet-reports-skill)<br>直观理清并呈现工作簿工作流 | 2026-11-15<br><sub>5.8 天</sub> | 153 | 26.5 |
| 5 | [mmclucknorrismm/cmangos-helm](https://github.com/mmclucknorrismm/cmangos-helm)<br>用Helm掌控并管理你的CMaNGOS领域 | 2026-11-15<br><sub>5.8 天</sub> | 153 | 26.4 |

<details>
<summary>本榜星标历史曲线</summary>

<a href="https://www.star-history.com/#replit/datacat&Date"><img src="https://api.star-history.com/svg?repos=replit/datacat&type=Date" width="260" alt="replit/datacat 的星标历史曲线"></a>

<a href="https://www.star-history.com/#piomin/ai-software-factory&Date"><img src="https://api.star-history.com/svg?repos=piomin/ai-software-factory&type=Date" width="260" alt="piomin/ai-software-factory 的星标历史曲线"></a>

<a href="https://www.star-history.com/#hackclub/orchard&Date"><img src="https://api.star-history.com/svg?repos=hackclub/orchard&type=Date" width="260" alt="hackclub/orchard 的星标历史曲线"></a>

<a href="https://www.star-history.com/#Realmeshowroom/jet-reports-skill&Date"><img src="https://api.star-history.com/svg?repos=Realmeshowroom/jet-reports-skill&type=Date" width="260" alt="Realmeshowroom/jet-reports-skill 的星标历史曲线"></a>

<a href="https://www.star-history.com/#mmclucknorrismm/cmangos-helm&Date"><img src="https://api.star-history.com/svg?repos=mmclucknorrismm/cmangos-helm&type=Date" width="260" alt="mmclucknorrismm/cmangos-helm 的星标历史曲线"></a>

</details>

### 本周增长最快（近 7 天）

| # | 项目 | 新增星标 | 星标/天 | 总星标 |
|---|---|---:|---:|---:|
| 1 | [kubernetes/kubernetes](https://github.com/kubernetes/kubernetes)<br>容器多了，部署扩容交给它<br>`基础设施` | +351 | 50.1 | 129,308 |
| 2 | [caddyserver/caddy](https://github.com/caddyserver/caddy)<br>搭网站服务器，HTTPS 自动配好<br>`基础设施` | +341 | 48.7 | 79,357 |
| 3 | [docker/compose](https://github.com/docker/compose)<br>多个容器写进一个文件，一起跑<br>`基础设施` | +305 | 43.6 | 39,067 |
| 4 | [prometheus/prometheus](https://github.com/prometheus/prometheus)<br>系统出问题，告警先找到你<br>`基础设施` | +169 | 24.1 | 67,744 |
| 5 | [grafana/grafana](https://github.com/grafana/grafana)<br>指标日志链路，放进一个面板<br>`基础设施` | +161 | 23.0 | 78,024 |
| 6 | [traefik/traefik](https://github.com/traefik/traefik)<br>服务多了，流量自动分好<br>`基础设施` | +113 | 16.1 | 65,644 |
| 7 | [hashicorp/terraform](https://github.com/hashicorp/terraform)<br>云资源写成代码，可审阅、可版本管理<br>`基础设施` | +85 | 12.1 | 50,302 |
| 8 | [pulumi/pulumi](https://github.com/pulumi/pulumi)<br>用熟悉的编程语言管云资源<br>`基础设施` | +31 | 4.4 | 25,929 |

<details>
<summary>本榜星标历史曲线</summary>

<a href="https://www.star-history.com/#kubernetes/kubernetes&Date"><img src="https://api.star-history.com/svg?repos=kubernetes/kubernetes&type=Date" width="260" alt="kubernetes/kubernetes 的星标历史曲线"></a>

<a href="https://www.star-history.com/#caddyserver/caddy&Date"><img src="https://api.star-history.com/svg?repos=caddyserver/caddy&type=Date" width="260" alt="caddyserver/caddy 的星标历史曲线"></a>

<a href="https://www.star-history.com/#docker/compose&Date"><img src="https://api.star-history.com/svg?repos=docker/compose&type=Date" width="260" alt="docker/compose 的星标历史曲线"></a>

<a href="https://www.star-history.com/#prometheus/prometheus&Date"><img src="https://api.star-history.com/svg?repos=prometheus/prometheus&type=Date" width="260" alt="prometheus/prometheus 的星标历史曲线"></a>

<a href="https://www.star-history.com/#grafana/grafana&Date"><img src="https://api.star-history.com/svg?repos=grafana/grafana&type=Date" width="260" alt="grafana/grafana 的星标历史曲线"></a>

<a href="https://www.star-history.com/#traefik/traefik&Date"><img src="https://api.star-history.com/svg?repos=traefik/traefik&type=Date" width="260" alt="traefik/traefik 的星标历史曲线"></a>

<a href="https://www.star-history.com/#hashicorp/terraform&Date"><img src="https://api.star-history.com/svg?repos=hashicorp/terraform&type=Date" width="260" alt="hashicorp/terraform 的星标历史曲线"></a>

<a href="https://www.star-history.com/#pulumi/pulumi&Date"><img src="https://api.star-history.com/svg?repos=pulumi/pulumi&type=Date" width="260" alt="pulumi/pulumi 的星标历史曲线"></a>

</details>

### 本月增长最快（近 30 天）

| # | 项目 | 新增星标 | 星标/天 | 总星标 |
|---|---|---:|---:|---:|
| 1 | [caddyserver/caddy](https://github.com/caddyserver/caddy)<br>搭网站服务器，HTTPS 自动配好<br>`基础设施` | +1,244 | 41.5 | 79,357 |
| 2 | [prometheus/prometheus](https://github.com/prometheus/prometheus)<br>系统出问题，告警先找到你<br>`基础设施` | +1,164 | 38.8 | 67,744 |
| 3 | [kubernetes/kubernetes](https://github.com/kubernetes/kubernetes)<br>容器多了，部署扩容交给它<br>`基础设施` | +1,153 | 38.4 | 129,308 |
| 4 | [grafana/grafana](https://github.com/grafana/grafana)<br>指标日志链路，放进一个面板<br>`基础设施` | +759 | 25.3 | 78,024 |
| 5 | [docker/compose](https://github.com/docker/compose)<br>多个容器写进一个文件，一起跑<br>`基础设施` | +722 | 24.1 | 39,067 |
| 6 | [traefik/traefik](https://github.com/traefik/traefik)<br>服务多了，流量自动分好<br>`基础设施` | +424 | 14.1 | 65,644 |
| 7 | [hashicorp/terraform](https://github.com/hashicorp/terraform)<br>云资源写成代码，可审阅、可版本管理<br>`基础设施` | +391 | 13.0 | 50,302 |
| 8 | [pulumi/pulumi](https://github.com/pulumi/pulumi)<br>用熟悉的编程语言管云资源<br>`基础设施` | +166 | 5.5 | 25,929 |

<details>
<summary>本榜星标历史曲线</summary>

<a href="https://www.star-history.com/#caddyserver/caddy&Date"><img src="https://api.star-history.com/svg?repos=caddyserver/caddy&type=Date" width="260" alt="caddyserver/caddy 的星标历史曲线"></a>

<a href="https://www.star-history.com/#prometheus/prometheus&Date"><img src="https://api.star-history.com/svg?repos=prometheus/prometheus&type=Date" width="260" alt="prometheus/prometheus 的星标历史曲线"></a>

<a href="https://www.star-history.com/#kubernetes/kubernetes&Date"><img src="https://api.star-history.com/svg?repos=kubernetes/kubernetes&type=Date" width="260" alt="kubernetes/kubernetes 的星标历史曲线"></a>

<a href="https://www.star-history.com/#grafana/grafana&Date"><img src="https://api.star-history.com/svg?repos=grafana/grafana&type=Date" width="260" alt="grafana/grafana 的星标历史曲线"></a>

<a href="https://www.star-history.com/#docker/compose&Date"><img src="https://api.star-history.com/svg?repos=docker/compose&type=Date" width="260" alt="docker/compose 的星标历史曲线"></a>

<a href="https://www.star-history.com/#traefik/traefik&Date"><img src="https://api.star-history.com/svg?repos=traefik/traefik&type=Date" width="260" alt="traefik/traefik 的星标历史曲线"></a>

<a href="https://www.star-history.com/#hashicorp/terraform&Date"><img src="https://api.star-history.com/svg?repos=hashicorp/terraform&type=Date" width="260" alt="hashicorp/terraform 的星标历史曲线"></a>

<a href="https://www.star-history.com/#pulumi/pulumi&Date"><img src="https://api.star-history.com/svg?repos=pulumi/pulumi&type=Date" width="260" alt="pulumi/pulumi 的星标历史曲线"></a>

</details>

### 今年增长最快（近 365 天）

| # | 项目 | 新增星标 | 星标/天 | 总星标 |
|---|---|---:|---:|---:|
| 1 | [caddyserver/caddy](https://github.com/caddyserver/caddy)<br>搭网站服务器，HTTPS 自动配好<br>`基础设施` | +12,248 | 33.6 | 79,357 |
| 2 | [kubernetes/kubernetes](https://github.com/kubernetes/kubernetes)<br>容器多了，部署扩容交给它<br>`基础设施` | +11,910 | 32.6 | 129,308 |
| 3 | [grafana/grafana](https://github.com/grafana/grafana)<br>指标日志链路，放进一个面板<br>`基础设施` | +7,972 | 21.8 | 78,024 |
| 4 | [traefik/traefik](https://github.com/traefik/traefik)<br>服务多了，流量自动分好<br>`基础设施` | +7,553 | 20.7 | 65,644 |
| 5 | [prometheus/prometheus](https://github.com/prometheus/prometheus)<br>系统出问题，告警先找到你<br>`基础设施` | +7,062 | 19.3 | 67,744 |
| 6 | [hashicorp/terraform](https://github.com/hashicorp/terraform)<br>云资源写成代码，可审阅、可版本管理<br>`基础设施` | +3,839 | 10.5 | 50,302 |
| 7 | [docker/compose](https://github.com/docker/compose)<br>多个容器写进一个文件，一起跑<br>`基础设施` | +3,023 | 8.3 | 39,067 |
| 8 | [pulumi/pulumi](https://github.com/pulumi/pulumi)<br>用熟悉的编程语言管云资源<br>`基础设施` | +2,101 | 5.8 | 25,929 |

<details>
<summary>本榜星标历史曲线</summary>

<a href="https://www.star-history.com/#caddyserver/caddy&Date"><img src="https://api.star-history.com/svg?repos=caddyserver/caddy&type=Date" width="260" alt="caddyserver/caddy 的星标历史曲线"></a>

<a href="https://www.star-history.com/#kubernetes/kubernetes&Date"><img src="https://api.star-history.com/svg?repos=kubernetes/kubernetes&type=Date" width="260" alt="kubernetes/kubernetes 的星标历史曲线"></a>

<a href="https://www.star-history.com/#grafana/grafana&Date"><img src="https://api.star-history.com/svg?repos=grafana/grafana&type=Date" width="260" alt="grafana/grafana 的星标历史曲线"></a>

<a href="https://www.star-history.com/#traefik/traefik&Date"><img src="https://api.star-history.com/svg?repos=traefik/traefik&type=Date" width="260" alt="traefik/traefik 的星标历史曲线"></a>

<a href="https://www.star-history.com/#prometheus/prometheus&Date"><img src="https://api.star-history.com/svg?repos=prometheus/prometheus&type=Date" width="260" alt="prometheus/prometheus 的星标历史曲线"></a>

<a href="https://www.star-history.com/#hashicorp/terraform&Date"><img src="https://api.star-history.com/svg?repos=hashicorp/terraform&type=Date" width="260" alt="hashicorp/terraform 的星标历史曲线"></a>

<a href="https://www.star-history.com/#docker/compose&Date"><img src="https://api.star-history.com/svg?repos=docker/compose&type=Date" width="260" alt="docker/compose 的星标历史曲线"></a>

<a href="https://www.star-history.com/#pulumi/pulumi&Date"><img src="https://api.star-history.com/svg?repos=pulumi/pulumi&type=Date" width="260" alt="pulumi/pulumi 的星标历史曲线"></a>

</details>

### 总星标数（历史累计）

| # | 项目 | 总星标 |
|---|---|---:|
| 1 | [kubernetes/kubernetes](https://github.com/kubernetes/kubernetes)<br>容器多了，部署扩容交给它<br>`基础设施` | 129,308 |
| 2 | [caddyserver/caddy](https://github.com/caddyserver/caddy)<br>搭网站服务器，HTTPS 自动配好<br>`基础设施` | 79,357 |
| 3 | [grafana/grafana](https://github.com/grafana/grafana)<br>指标日志链路，放进一个面板<br>`基础设施` | 78,024 |
| 4 | [prometheus/prometheus](https://github.com/prometheus/prometheus)<br>系统出问题，告警先找到你<br>`基础设施` | 67,744 |
| 5 | [traefik/traefik](https://github.com/traefik/traefik)<br>服务多了，流量自动分好<br>`基础设施` | 65,644 |
| 6 | [hashicorp/terraform](https://github.com/hashicorp/terraform)<br>云资源写成代码，可审阅、可版本管理<br>`基础设施` | 50,302 |
| 7 | [docker/compose](https://github.com/docker/compose)<br>多个容器写进一个文件，一起跑<br>`基础设施` | 39,067 |
| 8 | [pulumi/pulumi](https://github.com/pulumi/pulumi)<br>用熟悉的编程语言管云资源<br>`基础设施` | 25,929 |

<details>
<summary>本榜星标历史曲线</summary>

<a href="https://www.star-history.com/#kubernetes/kubernetes&Date"><img src="https://api.star-history.com/svg?repos=kubernetes/kubernetes&type=Date" width="260" alt="kubernetes/kubernetes 的星标历史曲线"></a>

<a href="https://www.star-history.com/#caddyserver/caddy&Date"><img src="https://api.star-history.com/svg?repos=caddyserver/caddy&type=Date" width="260" alt="caddyserver/caddy 的星标历史曲线"></a>

<a href="https://www.star-history.com/#grafana/grafana&Date"><img src="https://api.star-history.com/svg?repos=grafana/grafana&type=Date" width="260" alt="grafana/grafana 的星标历史曲线"></a>

<a href="https://www.star-history.com/#prometheus/prometheus&Date"><img src="https://api.star-history.com/svg?repos=prometheus/prometheus&type=Date" width="260" alt="prometheus/prometheus 的星标历史曲线"></a>

<a href="https://www.star-history.com/#traefik/traefik&Date"><img src="https://api.star-history.com/svg?repos=traefik/traefik&type=Date" width="260" alt="traefik/traefik 的星标历史曲线"></a>

<a href="https://www.star-history.com/#hashicorp/terraform&Date"><img src="https://api.star-history.com/svg?repos=hashicorp/terraform&type=Date" width="260" alt="hashicorp/terraform 的星标历史曲线"></a>

<a href="https://www.star-history.com/#docker/compose&Date"><img src="https://api.star-history.com/svg?repos=docker/compose&type=Date" width="260" alt="docker/compose 的星标历史曲线"></a>

<a href="https://www.star-history.com/#pulumi/pulumi&Date"><img src="https://api.star-history.com/svg?repos=pulumi/pulumi&type=Date" width="260" alt="pulumi/pulumi 的星标历史曲线"></a>

</details>

## 设计 / 创意

> 设计系统、绘图、动画与创意工具

### 最热新仓库（近 7 天内创建）

| # | 项目 | 创建时间（UTC） | 总星标 | 星标/天 |
|---|---|---|---:|---:|
| 1 | [randrianiaina1/illustrator-datalin-vector-design](https://github.com/randrianiaina1/illustrator-datalin-vector-design)<br>Illustrator Datalin Vector Design delivers precise vector design workflows for structured artwork. | 2026-11-20<br><sub>1.0 天</sub> | 206 | 206.0 |
| 2 | [bgleeson180-afk/cinema-4d-sacerin-motion-studio](https://github.com/bgleeson180-afk/cinema-4d-sacerin-motion-studio)<br>Builds Cinema 4D Sacerin motion scenes through a structured studio workflow. | 2026-11-21<br><sub>1.0 天</sub> | 203 | 203.0 |
| 3 | [himeshsuthar91-eng/after-effects-ceramar-motion-design](https://github.com/himeshsuthar91-eng/after-effects-ceramar-motion-design)<br>After Effects Ceramar Motion Design: a motion design project built around Ceramar techniques. | 2026-11-21<br><sub>1.0 天</sub> | 196 | 196.0 |
| 4 | [124113009-art/adobe-fresco-elrina](https://github.com/124113009-art/adobe-fresco-elrina)<br>Explore brushes and tools in Adobe Fresco Elrina with screenshot-heavy visual guides. | 2026-11-19<br><sub>1.6 天</sub> | 152 | 92.9 |
| 5 | [SPAPharma/adobe-animate-velvona](https://github.com/SPAPharma/adobe-animate-velvona)<br>Create and refine animations with Adobe Animate Velvona tools. | 2026-11-19<br><sub>1.6 天</sub> | 150 | 91.3 |
| 6 | [Anais27-pharma/adobe-character-animator-calrara](https://github.com/Anais27-pharma/adobe-character-animator-calrara)<br>Real-time puppet animation driven by webcam and audio input—Calrara integrates expression mapping | 2026-11-19<br><sub>1.6 天</sub> | 149 | 90.9 |
| 7 | [charaf24/substance-3d-designer-norlora](https://github.com/charaf24/substance-3d-designer-norlora)<br>Node-based texturing workflow for procedural material authoring and 3D asset design. | 2026-11-18<br><sub>2.7 天</sub> | 152 | 55.8 |
| 8 | [tarouquelaprogramacao-max/krita-elvona-art-studio](https://github.com/tarouquelaprogramacao-max/krita-elvona-art-studio)<br>Krita plugin that builds a structured art studio workspace for digital painters. | 2026-11-18<br><sub>3.0 天</sub> | 152 | 50.1 |

<details>
<summary>本榜星标历史曲线</summary>

<a href="https://www.star-history.com/#randrianiaina1/illustrator-datalin-vector-design&Date"><img src="https://api.star-history.com/svg?repos=randrianiaina1/illustrator-datalin-vector-design&type=Date" width="260" alt="randrianiaina1/illustrator-datalin-vector-design 的星标历史曲线"></a>

<a href="https://www.star-history.com/#bgleeson180-afk/cinema-4d-sacerin-motion-studio&Date"><img src="https://api.star-history.com/svg?repos=bgleeson180-afk/cinema-4d-sacerin-motion-studio&type=Date" width="260" alt="bgleeson180-afk/cinema-4d-sacerin-motion-studio 的星标历史曲线"></a>

<a href="https://www.star-history.com/#himeshsuthar91-eng/after-effects-ceramar-motion-design&Date"><img src="https://api.star-history.com/svg?repos=himeshsuthar91-eng/after-effects-ceramar-motion-design&type=Date" width="260" alt="himeshsuthar91-eng/after-effects-ceramar-motion-design 的星标历史曲线"></a>

<a href="https://www.star-history.com/#124113009-art/adobe-fresco-elrina&Date"><img src="https://api.star-history.com/svg?repos=124113009-art/adobe-fresco-elrina&type=Date" width="260" alt="124113009-art/adobe-fresco-elrina 的星标历史曲线"></a>

<a href="https://www.star-history.com/#SPAPharma/adobe-animate-velvona&Date"><img src="https://api.star-history.com/svg?repos=SPAPharma/adobe-animate-velvona&type=Date" width="260" alt="SPAPharma/adobe-animate-velvona 的星标历史曲线"></a>

<a href="https://www.star-history.com/#Anais27-pharma/adobe-character-animator-calrara&Date"><img src="https://api.star-history.com/svg?repos=Anais27-pharma/adobe-character-animator-calrara&type=Date" width="260" alt="Anais27-pharma/adobe-character-animator-calrara 的星标历史曲线"></a>

<a href="https://www.star-history.com/#charaf24/substance-3d-designer-norlora&Date"><img src="https://api.star-history.com/svg?repos=charaf24/substance-3d-designer-norlora&type=Date" width="260" alt="charaf24/substance-3d-designer-norlora 的星标历史曲线"></a>

<a href="https://www.star-history.com/#tarouquelaprogramacao-max/krita-elvona-art-studio&Date"><img src="https://api.star-history.com/svg?repos=tarouquelaprogramacao-max/krita-elvona-art-studio&type=Date" width="260" alt="tarouquelaprogramacao-max/krita-elvona-art-studio 的星标历史曲线"></a>

</details>

### 本周增长最快（近 7 天）

| # | 项目 | 新增星标 | 星标/天 | 总星标 |
|---|---|---:|---:|---:|
| 1 | [excalidraw/excalidraw](https://github.com/excalidraw/excalidraw)<br>打开就画，像在纸上随手画图<br>`设计 / 创意` | +424 | 60.6 | 136,056 |
| 2 | [penpot/penpot](https://github.com/penpot/penpot)<br>团队一起做设计，用开源平台<br>`设计 / 创意` | +283 | 40.4 | 62,607 |
| 3 | [lucide-icons/lucide](https://github.com/lucide-icons/lucide)<br>一套图标风格统一，拿来就用<br>`设计 / 创意` | +159 | 22.7 | 25,906 |
| 4 | [jgraph/drawio](https://github.com/jgraph/drawio)<br>画图和白板，一个编辑器搞定<br>`设计 / 创意` | +145 | 20.7 | 9,505 |
| 5 | [airbnb/lottie-web](https://github.com/airbnb/lottie-web)<br>AE 做的动画，直接放进网页<br>`设计 / 创意` | +135 | 19.3 | 32,538 |
| 6 | [saadeghi/daisyui](https://github.com/saadeghi/daisyui)<br>Tailwind 也有现成组件可挑<br>`设计 / 创意` | +109 | 15.6 | 42,924 |
| 7 | [phosphor-icons/homepage](https://github.com/phosphor-icons/homepage)<br>一整套灵活的图标，人人可用<br>`设计 / 创意` | +34 | 4.9 | 7,837 |
| 8 | [lottiefiles/lottie-ios](https://github.com/lottiefiles/lottie-ios)<br>AE 做的动画，直接放进 iOS<br>`设计 / 创意` | +0 | 0.0 | 43 |

<details>
<summary>本榜星标历史曲线</summary>

<a href="https://www.star-history.com/#excalidraw/excalidraw&Date"><img src="https://api.star-history.com/svg?repos=excalidraw/excalidraw&type=Date" width="260" alt="excalidraw/excalidraw 的星标历史曲线"></a>

<a href="https://www.star-history.com/#penpot/penpot&Date"><img src="https://api.star-history.com/svg?repos=penpot/penpot&type=Date" width="260" alt="penpot/penpot 的星标历史曲线"></a>

<a href="https://www.star-history.com/#lucide-icons/lucide&Date"><img src="https://api.star-history.com/svg?repos=lucide-icons/lucide&type=Date" width="260" alt="lucide-icons/lucide 的星标历史曲线"></a>

<a href="https://www.star-history.com/#jgraph/drawio&Date"><img src="https://api.star-history.com/svg?repos=jgraph/drawio&type=Date" width="260" alt="jgraph/drawio 的星标历史曲线"></a>

<a href="https://www.star-history.com/#airbnb/lottie-web&Date"><img src="https://api.star-history.com/svg?repos=airbnb/lottie-web&type=Date" width="260" alt="airbnb/lottie-web 的星标历史曲线"></a>

<a href="https://www.star-history.com/#saadeghi/daisyui&Date"><img src="https://api.star-history.com/svg?repos=saadeghi/daisyui&type=Date" width="260" alt="saadeghi/daisyui 的星标历史曲线"></a>

<a href="https://www.star-history.com/#phosphor-icons/homepage&Date"><img src="https://api.star-history.com/svg?repos=phosphor-icons/homepage&type=Date" width="260" alt="phosphor-icons/homepage 的星标历史曲线"></a>

<a href="https://www.star-history.com/#lottiefiles/lottie-ios&Date"><img src="https://api.star-history.com/svg?repos=lottiefiles/lottie-ios&type=Date" width="260" alt="lottiefiles/lottie-ios 的星标历史曲线"></a>

</details>

### 本月增长最快（近 30 天）

| # | 项目 | 新增星标 | 星标/天 | 总星标 |
|---|---|---:|---:|---:|
| 1 | [excalidraw/excalidraw](https://github.com/excalidraw/excalidraw)<br>打开就画，像在纸上随手画图<br>`设计 / 创意` | +1,908 | 63.6 | 136,056 |
| 2 | [penpot/penpot](https://github.com/penpot/penpot)<br>团队一起做设计，用开源平台<br>`设计 / 创意` | +1,262 | 42.1 | 62,607 |
| 3 | [lucide-icons/lucide](https://github.com/lucide-icons/lucide)<br>一套图标风格统一，拿来就用<br>`设计 / 创意` | +753 | 25.1 | 25,906 |
| 4 | [jgraph/drawio](https://github.com/jgraph/drawio)<br>画图和白板，一个编辑器搞定<br>`设计 / 创意` | +602 | 20.1 | 9,505 |
| 5 | [saadeghi/daisyui](https://github.com/saadeghi/daisyui)<br>Tailwind 也有现成组件可挑<br>`设计 / 创意` | +362 | 12.1 | 42,924 |
| 6 | [airbnb/lottie-web](https://github.com/airbnb/lottie-web)<br>AE 做的动画，直接放进网页<br>`设计 / 创意` | +309 | 10.3 | 32,538 |
| 7 | [phosphor-icons/homepage](https://github.com/phosphor-icons/homepage)<br>一整套灵活的图标，人人可用<br>`设计 / 创意` | +157 | 5.2 | 7,837 |
| 8 | [lottiefiles/lottie-ios](https://github.com/lottiefiles/lottie-ios)<br>AE 做的动画，直接放进 iOS<br>`设计 / 创意` | +0 | 0.0 | 43 |

<details>
<summary>本榜星标历史曲线</summary>

<a href="https://www.star-history.com/#excalidraw/excalidraw&Date"><img src="https://api.star-history.com/svg?repos=excalidraw/excalidraw&type=Date" width="260" alt="excalidraw/excalidraw 的星标历史曲线"></a>

<a href="https://www.star-history.com/#penpot/penpot&Date"><img src="https://api.star-history.com/svg?repos=penpot/penpot&type=Date" width="260" alt="penpot/penpot 的星标历史曲线"></a>

<a href="https://www.star-history.com/#lucide-icons/lucide&Date"><img src="https://api.star-history.com/svg?repos=lucide-icons/lucide&type=Date" width="260" alt="lucide-icons/lucide 的星标历史曲线"></a>

<a href="https://www.star-history.com/#jgraph/drawio&Date"><img src="https://api.star-history.com/svg?repos=jgraph/drawio&type=Date" width="260" alt="jgraph/drawio 的星标历史曲线"></a>

<a href="https://www.star-history.com/#saadeghi/daisyui&Date"><img src="https://api.star-history.com/svg?repos=saadeghi/daisyui&type=Date" width="260" alt="saadeghi/daisyui 的星标历史曲线"></a>

<a href="https://www.star-history.com/#airbnb/lottie-web&Date"><img src="https://api.star-history.com/svg?repos=airbnb/lottie-web&type=Date" width="260" alt="airbnb/lottie-web 的星标历史曲线"></a>

<a href="https://www.star-history.com/#phosphor-icons/homepage&Date"><img src="https://api.star-history.com/svg?repos=phosphor-icons/homepage&type=Date" width="260" alt="phosphor-icons/homepage 的星标历史曲线"></a>

<a href="https://www.star-history.com/#lottiefiles/lottie-ios&Date"><img src="https://api.star-history.com/svg?repos=lottiefiles/lottie-ios&type=Date" width="260" alt="lottiefiles/lottie-ios 的星标历史曲线"></a>

</details>

### 今年增长最快（近 365 天）

| # | 项目 | 新增星标 | 星标/天 | 总星标 |
|---|---|---:|---:|---:|
| 1 | [excalidraw/excalidraw](https://github.com/excalidraw/excalidraw)<br>打开就画，像在纸上随手画图<br>`设计 / 创意` | +26,764 | 73.3 | 136,056 |
| 2 | [penpot/penpot](https://github.com/penpot/penpot)<br>团队一起做设计，用开源平台<br>`设计 / 创意` | +21,772 | 59.6 | 62,607 |
| 3 | [jgraph/drawio](https://github.com/jgraph/drawio)<br>画图和白板，一个编辑器搞定<br>`设计 / 创意` | +6,705 | 18.4 | 9,505 |
| 4 | [lucide-icons/lucide](https://github.com/lucide-icons/lucide)<br>一套图标风格统一，拿来就用<br>`设计 / 创意` | +6,443 | 17.7 | 25,906 |
| 5 | [saadeghi/daisyui](https://github.com/saadeghi/daisyui)<br>Tailwind 也有现成组件可挑<br>`设计 / 创意` | +4,255 | 11.7 | 42,924 |
| 6 | [phosphor-icons/homepage](https://github.com/phosphor-icons/homepage)<br>一整套灵活的图标，人人可用<br>`设计 / 创意` | +2,214 | 6.1 | 7,837 |
| 7 | [airbnb/lottie-web](https://github.com/airbnb/lottie-web)<br>AE 做的动画，直接放进网页<br>`设计 / 创意` | +1,267 | 3.5 | 32,538 |
| 8 | [lottiefiles/lottie-ios](https://github.com/lottiefiles/lottie-ios)<br>AE 做的动画，直接放进 iOS<br>`设计 / 创意` | +1 | 0.0 | 43 |

<details>
<summary>本榜星标历史曲线</summary>

<a href="https://www.star-history.com/#excalidraw/excalidraw&Date"><img src="https://api.star-history.com/svg?repos=excalidraw/excalidraw&type=Date" width="260" alt="excalidraw/excalidraw 的星标历史曲线"></a>

<a href="https://www.star-history.com/#penpot/penpot&Date"><img src="https://api.star-history.com/svg?repos=penpot/penpot&type=Date" width="260" alt="penpot/penpot 的星标历史曲线"></a>

<a href="https://www.star-history.com/#jgraph/drawio&Date"><img src="https://api.star-history.com/svg?repos=jgraph/drawio&type=Date" width="260" alt="jgraph/drawio 的星标历史曲线"></a>

<a href="https://www.star-history.com/#lucide-icons/lucide&Date"><img src="https://api.star-history.com/svg?repos=lucide-icons/lucide&type=Date" width="260" alt="lucide-icons/lucide 的星标历史曲线"></a>

<a href="https://www.star-history.com/#saadeghi/daisyui&Date"><img src="https://api.star-history.com/svg?repos=saadeghi/daisyui&type=Date" width="260" alt="saadeghi/daisyui 的星标历史曲线"></a>

<a href="https://www.star-history.com/#phosphor-icons/homepage&Date"><img src="https://api.star-history.com/svg?repos=phosphor-icons/homepage&type=Date" width="260" alt="phosphor-icons/homepage 的星标历史曲线"></a>

<a href="https://www.star-history.com/#airbnb/lottie-web&Date"><img src="https://api.star-history.com/svg?repos=airbnb/lottie-web&type=Date" width="260" alt="airbnb/lottie-web 的星标历史曲线"></a>

<a href="https://www.star-history.com/#lottiefiles/lottie-ios&Date"><img src="https://api.star-history.com/svg?repos=lottiefiles/lottie-ios&type=Date" width="260" alt="lottiefiles/lottie-ios 的星标历史曲线"></a>

</details>

### 总星标数（历史累计）

| # | 项目 | 总星标 |
|---|---|---:|
| 1 | [excalidraw/excalidraw](https://github.com/excalidraw/excalidraw)<br>打开就画，像在纸上随手画图<br>`设计 / 创意` | 136,056 |
| 2 | [penpot/penpot](https://github.com/penpot/penpot)<br>团队一起做设计，用开源平台<br>`设计 / 创意` | 62,607 |
| 3 | [saadeghi/daisyui](https://github.com/saadeghi/daisyui)<br>Tailwind 也有现成组件可挑<br>`设计 / 创意` | 42,924 |
| 4 | [airbnb/lottie-web](https://github.com/airbnb/lottie-web)<br>AE 做的动画，直接放进网页<br>`设计 / 创意` | 32,538 |
| 5 | [lucide-icons/lucide](https://github.com/lucide-icons/lucide)<br>一套图标风格统一，拿来就用<br>`设计 / 创意` | 25,906 |
| 6 | [jgraph/drawio](https://github.com/jgraph/drawio)<br>画图和白板，一个编辑器搞定<br>`设计 / 创意` | 9,505 |
| 7 | [phosphor-icons/homepage](https://github.com/phosphor-icons/homepage)<br>一整套灵活的图标，人人可用<br>`设计 / 创意` | 7,837 |
| 8 | [lottiefiles/lottie-ios](https://github.com/lottiefiles/lottie-ios)<br>AE 做的动画，直接放进 iOS<br>`设计 / 创意` | 43 |

<details>
<summary>本榜星标历史曲线</summary>

<a href="https://www.star-history.com/#excalidraw/excalidraw&Date"><img src="https://api.star-history.com/svg?repos=excalidraw/excalidraw&type=Date" width="260" alt="excalidraw/excalidraw 的星标历史曲线"></a>

<a href="https://www.star-history.com/#penpot/penpot&Date"><img src="https://api.star-history.com/svg?repos=penpot/penpot&type=Date" width="260" alt="penpot/penpot 的星标历史曲线"></a>

<a href="https://www.star-history.com/#saadeghi/daisyui&Date"><img src="https://api.star-history.com/svg?repos=saadeghi/daisyui&type=Date" width="260" alt="saadeghi/daisyui 的星标历史曲线"></a>

<a href="https://www.star-history.com/#airbnb/lottie-web&Date"><img src="https://api.star-history.com/svg?repos=airbnb/lottie-web&type=Date" width="260" alt="airbnb/lottie-web 的星标历史曲线"></a>

<a href="https://www.star-history.com/#lucide-icons/lucide&Date"><img src="https://api.star-history.com/svg?repos=lucide-icons/lucide&type=Date" width="260" alt="lucide-icons/lucide 的星标历史曲线"></a>

<a href="https://www.star-history.com/#jgraph/drawio&Date"><img src="https://api.star-history.com/svg?repos=jgraph/drawio&type=Date" width="260" alt="jgraph/drawio 的星标历史曲线"></a>

<a href="https://www.star-history.com/#phosphor-icons/homepage&Date"><img src="https://api.star-history.com/svg?repos=phosphor-icons/homepage&type=Date" width="260" alt="phosphor-icons/homepage 的星标历史曲线"></a>

<a href="https://www.star-history.com/#lottiefiles/lottie-ios&Date"><img src="https://api.star-history.com/svg?repos=lottiefiles/lottie-ios&type=Date" width="260" alt="lottiefiles/lottie-ios 的星标历史曲线"></a>

</details>

## 数据

> 数据库、分析、ETL 与数据工程

### 最热新仓库（近 7 天内创建）

| # | 项目 | 创建时间（UTC） | 总星标 | 星标/天 |
|---|---|---|---:|---:|
| 1 | [aurahamzzz-cyber/microsoft-excel-alvaora](https://github.com/aurahamzzz-cyber/microsoft-excel-alvaora)<br>Automates structured data workflows and spreadsheet task orchestration in Excel. | 2026-11-18<br><sub>2.8 天</sub> | 152 | 54.6 |

<details>
<summary>本榜星标历史曲线</summary>

<a href="https://www.star-history.com/#aurahamzzz-cyber/microsoft-excel-alvaora&Date"><img src="https://api.star-history.com/svg?repos=aurahamzzz-cyber/microsoft-excel-alvaora&type=Date" width="260" alt="aurahamzzz-cyber/microsoft-excel-alvaora 的星标历史曲线"></a>

</details>

### 本周增长最快（近 7 天）

| # | 项目 | 新增星标 | 星标/天 | 总星标 |
|---|---|---:|---:|---:|
| 1 | [duckdb/duckdb](https://github.com/duckdb/duckdb)<br>不搭数据库服务，也能跑 SQL 分析<br>`数据` | +175 | 25.0 | 43,216 |
| 2 | [ClickHouse/ClickHouse](https://github.com/ClickHouse/ClickHouse)<br>大量数据实时分析，用开源的<br>`数据` | +148 | 21.1 | 51,051 |
| 3 | [apache/superset](https://github.com/apache/superset)<br>数据看不懂，做成图就明白<br>`数据` | +104 | 14.9 | 75,604 |
| 4 | [pola-rs/polars](https://github.com/pola-rs/polars)<br>表格数据处理快，不用干等<br>`数据` | +83 | 11.9 | 40,416 |
| 5 | [apache/kafka](https://github.com/apache/kafka)<br>系统之间的事件流，交给它来传<br>`数据` | +43 | 6.1 | 34,247 |
| 6 | [apache/arrow](https://github.com/apache/arrow)<br>不同语言之间，数据直接通用<br>`数据` | +36 | 5.1 | 17,326 |
| 7 | [dbt-labs/dbt-core](https://github.com/dbt-labs/dbt-core)<br>数据转换，照软件工程的做法来<br>`数据` | +30 | 4.3 | 14,196 |
| 8 | [jupyter/notebook](https://github.com/jupyter/notebook)<br>在网页里写代码，边写边看结果<br>`数据` | +10 | 1.4 | 13,477 |

<details>
<summary>本榜星标历史曲线</summary>

<a href="https://www.star-history.com/#duckdb/duckdb&Date"><img src="https://api.star-history.com/svg?repos=duckdb/duckdb&type=Date" width="260" alt="duckdb/duckdb 的星标历史曲线"></a>

<a href="https://www.star-history.com/#ClickHouse/ClickHouse&Date"><img src="https://api.star-history.com/svg?repos=ClickHouse/ClickHouse&type=Date" width="260" alt="ClickHouse/ClickHouse 的星标历史曲线"></a>

<a href="https://www.star-history.com/#apache/superset&Date"><img src="https://api.star-history.com/svg?repos=apache/superset&type=Date" width="260" alt="apache/superset 的星标历史曲线"></a>

<a href="https://www.star-history.com/#pola-rs/polars&Date"><img src="https://api.star-history.com/svg?repos=pola-rs/polars&type=Date" width="260" alt="pola-rs/polars 的星标历史曲线"></a>

<a href="https://www.star-history.com/#apache/kafka&Date"><img src="https://api.star-history.com/svg?repos=apache/kafka&type=Date" width="260" alt="apache/kafka 的星标历史曲线"></a>

<a href="https://www.star-history.com/#apache/arrow&Date"><img src="https://api.star-history.com/svg?repos=apache/arrow&type=Date" width="260" alt="apache/arrow 的星标历史曲线"></a>

<a href="https://www.star-history.com/#dbt-labs/dbt-core&Date"><img src="https://api.star-history.com/svg?repos=dbt-labs/dbt-core&type=Date" width="260" alt="dbt-labs/dbt-core 的星标历史曲线"></a>

<a href="https://www.star-history.com/#jupyter/notebook&Date"><img src="https://api.star-history.com/svg?repos=jupyter/notebook&type=Date" width="260" alt="jupyter/notebook 的星标历史曲线"></a>

</details>

### 本月增长最快（近 30 天）

| # | 项目 | 新增星标 | 星标/天 | 总星标 |
|---|---|---:|---:|---:|
| 1 | [duckdb/duckdb](https://github.com/duckdb/duckdb)<br>不搭数据库服务，也能跑 SQL 分析<br>`数据` | +925 | 30.8 | 43,216 |
| 2 | [ClickHouse/ClickHouse](https://github.com/ClickHouse/ClickHouse)<br>大量数据实时分析，用开源的<br>`数据` | +591 | 19.7 | 51,051 |
| 3 | [apache/superset](https://github.com/apache/superset)<br>数据看不懂，做成图就明白<br>`数据` | +454 | 15.1 | 75,604 |
| 4 | [pola-rs/polars](https://github.com/pola-rs/polars)<br>表格数据处理快，不用干等<br>`数据` | +313 | 10.4 | 40,416 |
| 5 | [apache/kafka](https://github.com/apache/kafka)<br>系统之间的事件流，交给它来传<br>`数据` | +265 | 8.8 | 34,247 |
| 6 | [dbt-labs/dbt-core](https://github.com/dbt-labs/dbt-core)<br>数据转换，照软件工程的做法来<br>`数据` | +155 | 5.2 | 14,196 |
| 7 | [apache/arrow](https://github.com/apache/arrow)<br>不同语言之间，数据直接通用<br>`数据` | +124 | 4.1 | 17,326 |
| 8 | [jupyter/notebook](https://github.com/jupyter/notebook)<br>在网页里写代码，边写边看结果<br>`数据` | +30 | 1.0 | 13,477 |

<details>
<summary>本榜星标历史曲线</summary>

<a href="https://www.star-history.com/#duckdb/duckdb&Date"><img src="https://api.star-history.com/svg?repos=duckdb/duckdb&type=Date" width="260" alt="duckdb/duckdb 的星标历史曲线"></a>

<a href="https://www.star-history.com/#ClickHouse/ClickHouse&Date"><img src="https://api.star-history.com/svg?repos=ClickHouse/ClickHouse&type=Date" width="260" alt="ClickHouse/ClickHouse 的星标历史曲线"></a>

<a href="https://www.star-history.com/#apache/superset&Date"><img src="https://api.star-history.com/svg?repos=apache/superset&type=Date" width="260" alt="apache/superset 的星标历史曲线"></a>

<a href="https://www.star-history.com/#pola-rs/polars&Date"><img src="https://api.star-history.com/svg?repos=pola-rs/polars&type=Date" width="260" alt="pola-rs/polars 的星标历史曲线"></a>

<a href="https://www.star-history.com/#apache/kafka&Date"><img src="https://api.star-history.com/svg?repos=apache/kafka&type=Date" width="260" alt="apache/kafka 的星标历史曲线"></a>

<a href="https://www.star-history.com/#dbt-labs/dbt-core&Date"><img src="https://api.star-history.com/svg?repos=dbt-labs/dbt-core&type=Date" width="260" alt="dbt-labs/dbt-core 的星标历史曲线"></a>

<a href="https://www.star-history.com/#apache/arrow&Date"><img src="https://api.star-history.com/svg?repos=apache/arrow&type=Date" width="260" alt="apache/arrow 的星标历史曲线"></a>

<a href="https://www.star-history.com/#jupyter/notebook&Date"><img src="https://api.star-history.com/svg?repos=jupyter/notebook&type=Date" width="260" alt="jupyter/notebook 的星标历史曲线"></a>

</details>

### 今年增长最快（近 365 天）

| # | 项目 | 新增星标 | 星标/天 | 总星标 |
|---|---|---:|---:|---:|
| 1 | [duckdb/duckdb](https://github.com/duckdb/duckdb)<br>不搭数据库服务，也能跑 SQL 分析<br>`数据` | +9,399 | 25.8 | 43,216 |
| 2 | [ClickHouse/ClickHouse](https://github.com/ClickHouse/ClickHouse)<br>大量数据实时分析，用开源的<br>`数据` | +7,541 | 20.7 | 51,051 |
| 3 | [apache/superset](https://github.com/apache/superset)<br>数据看不懂，做成图就明白<br>`数据` | +7,366 | 20.2 | 75,604 |
| 4 | [pola-rs/polars](https://github.com/pola-rs/polars)<br>表格数据处理快，不用干等<br>`数据` | +4,759 | 13.0 | 40,416 |
| 5 | [apache/kafka](https://github.com/apache/kafka)<br>系统之间的事件流，交给它来传<br>`数据` | +3,296 | 9.0 | 34,247 |
| 6 | [dbt-labs/dbt-core](https://github.com/dbt-labs/dbt-core)<br>数据转换，照软件工程的做法来<br>`数据` | +2,464 | 6.8 | 14,196 |
| 7 | [apache/arrow](https://github.com/apache/arrow)<br>不同语言之间，数据直接通用<br>`数据` | +1,308 | 3.6 | 17,326 |
| 8 | [jupyter/notebook](https://github.com/jupyter/notebook)<br>在网页里写代码，边写边看结果<br>`数据` | +861 | 2.4 | 13,477 |

<details>
<summary>本榜星标历史曲线</summary>

<a href="https://www.star-history.com/#duckdb/duckdb&Date"><img src="https://api.star-history.com/svg?repos=duckdb/duckdb&type=Date" width="260" alt="duckdb/duckdb 的星标历史曲线"></a>

<a href="https://www.star-history.com/#ClickHouse/ClickHouse&Date"><img src="https://api.star-history.com/svg?repos=ClickHouse/ClickHouse&type=Date" width="260" alt="ClickHouse/ClickHouse 的星标历史曲线"></a>

<a href="https://www.star-history.com/#apache/superset&Date"><img src="https://api.star-history.com/svg?repos=apache/superset&type=Date" width="260" alt="apache/superset 的星标历史曲线"></a>

<a href="https://www.star-history.com/#pola-rs/polars&Date"><img src="https://api.star-history.com/svg?repos=pola-rs/polars&type=Date" width="260" alt="pola-rs/polars 的星标历史曲线"></a>

<a href="https://www.star-history.com/#apache/kafka&Date"><img src="https://api.star-history.com/svg?repos=apache/kafka&type=Date" width="260" alt="apache/kafka 的星标历史曲线"></a>

<a href="https://www.star-history.com/#dbt-labs/dbt-core&Date"><img src="https://api.star-history.com/svg?repos=dbt-labs/dbt-core&type=Date" width="260" alt="dbt-labs/dbt-core 的星标历史曲线"></a>

<a href="https://www.star-history.com/#apache/arrow&Date"><img src="https://api.star-history.com/svg?repos=apache/arrow&type=Date" width="260" alt="apache/arrow 的星标历史曲线"></a>

<a href="https://www.star-history.com/#jupyter/notebook&Date"><img src="https://api.star-history.com/svg?repos=jupyter/notebook&type=Date" width="260" alt="jupyter/notebook 的星标历史曲线"></a>

</details>

### 总星标数（历史累计）

| # | 项目 | 总星标 |
|---|---|---:|
| 1 | [apache/superset](https://github.com/apache/superset)<br>数据看不懂，做成图就明白<br>`数据` | 75,604 |
| 2 | [ClickHouse/ClickHouse](https://github.com/ClickHouse/ClickHouse)<br>大量数据实时分析，用开源的<br>`数据` | 51,051 |
| 3 | [duckdb/duckdb](https://github.com/duckdb/duckdb)<br>不搭数据库服务，也能跑 SQL 分析<br>`数据` | 43,216 |
| 4 | [pola-rs/polars](https://github.com/pola-rs/polars)<br>表格数据处理快，不用干等<br>`数据` | 40,416 |
| 5 | [apache/kafka](https://github.com/apache/kafka)<br>系统之间的事件流，交给它来传<br>`数据` | 34,247 |
| 6 | [apache/arrow](https://github.com/apache/arrow)<br>不同语言之间，数据直接通用<br>`数据` | 17,326 |
| 7 | [dbt-labs/dbt-core](https://github.com/dbt-labs/dbt-core)<br>数据转换，照软件工程的做法来<br>`数据` | 14,196 |
| 8 | [jupyter/notebook](https://github.com/jupyter/notebook)<br>在网页里写代码，边写边看结果<br>`数据` | 13,477 |

<details>
<summary>本榜星标历史曲线</summary>

<a href="https://www.star-history.com/#apache/superset&Date"><img src="https://api.star-history.com/svg?repos=apache/superset&type=Date" width="260" alt="apache/superset 的星标历史曲线"></a>

<a href="https://www.star-history.com/#ClickHouse/ClickHouse&Date"><img src="https://api.star-history.com/svg?repos=ClickHouse/ClickHouse&type=Date" width="260" alt="ClickHouse/ClickHouse 的星标历史曲线"></a>

<a href="https://www.star-history.com/#duckdb/duckdb&Date"><img src="https://api.star-history.com/svg?repos=duckdb/duckdb&type=Date" width="260" alt="duckdb/duckdb 的星标历史曲线"></a>

<a href="https://www.star-history.com/#pola-rs/polars&Date"><img src="https://api.star-history.com/svg?repos=pola-rs/polars&type=Date" width="260" alt="pola-rs/polars 的星标历史曲线"></a>

<a href="https://www.star-history.com/#apache/kafka&Date"><img src="https://api.star-history.com/svg?repos=apache/kafka&type=Date" width="260" alt="apache/kafka 的星标历史曲线"></a>

<a href="https://www.star-history.com/#apache/arrow&Date"><img src="https://api.star-history.com/svg?repos=apache/arrow&type=Date" width="260" alt="apache/arrow 的星标历史曲线"></a>

<a href="https://www.star-history.com/#dbt-labs/dbt-core&Date"><img src="https://api.star-history.com/svg?repos=dbt-labs/dbt-core&type=Date" width="260" alt="dbt-labs/dbt-core 的星标历史曲线"></a>

<a href="https://www.star-history.com/#jupyter/notebook&Date"><img src="https://api.star-history.com/svg?repos=jupyter/notebook&type=Date" width="260" alt="jupyter/notebook 的星标历史曲线"></a>

</details>

---

如果它帮你省了时间，请给仓库点个星标，让更多人找得到。

如何引用：见 [CITATION.cff](CITATION.cff)。

数据怎么算和如何参与：[docs/HOW_IT_WORKS.zh-Hans.md](docs/HOW_IT_WORKS.zh-Hans.md)。新仓库规则：[docs/NEW_ARRIVALS.md](docs/NEW_ARRIVALS.md)。分类说明：[docs/CATEGORIES.md](docs/CATEGORIES.md)。提交改动：[CONTRIBUTING.md](CONTRIBUTING.md)。
