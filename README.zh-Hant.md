[English](README.md) | [简体中文](README.zh-Hans.md) | **繁體中文** | [日本語](README.ja.md) | [한국어](README.ko.md)

# GitHub 漲星榜 / GitHub Risers

<img src=".github/social-preview.png" alt="GitHub 漲星榜 / GitHub Risers" width="640">

[![MIT](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE) [![CI](https://github.com/jammyfu/github-risers/actions/workflows/ci.yml/badge.svg)](https://github.com/jammyfu/github-risers/actions/workflows/ci.yml) [![updated](https://img.shields.io/badge/dynamic/json?url=https%3A%2F%2Fraw.githubusercontent.com%2Fjammyfu%2Fgithub-risers%2Fmain%2Fdata%2Fstats.json&query=%24.today_utc&label=updated&color=brightgreen)](latest/rankings.zh-Hant.md)

依每天新增星號（而不是總星號）替 GitHub 儲存庫排名：AI 在前，接著是開發者工具、資安、Web / 前端、基礎建設、設計 / 創意與資料；每天更新。

資料取自 2026-11-25 17:40（UTC）。每天更新。

**線上榜單：** [網站](https://jammyfu.github.io/github-risers/) · [最新快照](latest/rankings.zh-Hant.md)

## 立刻使用

1. 打開[線上榜單](https://jammyfu.github.io/github-risers/)，不用安裝。
2. 或者先看下面本期各類榜首，再翻分類榜。
3. 這裡每張榜只列前 10 名；完整前 20 名在 [latest/rankings.zh-Hant.md](latest/rankings.zh-Hant.md)。

[網站](https://jammyfu.github.io/github-risers/) · [運作方式](docs/HOW_IT_WORKS.zh-Hant.md) · [事實速查](docs/FACTS.md) · [歷史榜單](rankings/README.zh-Hant.md) · [最新快照](latest/rankings.zh-Hant.md)

## 本期各類榜首

| 分類 | 新儲存庫第 1 名（7 天） | 本週第 1 名 | 本月第 1 名 | 今年第 1 名 | 總星號第 1 名 |
|---|---|---|---|---|---|
| **[人工智慧](#人工智慧)** ★ 主榜 | [EL4CTEO/fast-anything](https://github.com/EL4CTEO/fast-anything)<br>943/天 | [morluto/rea](https://github.com/morluto/rea)<br>1,586/天 | [morluto/rea](https://github.com/morluto/rea)<br>3,116/天 | [deepseek-ai/deepseek-harness](https://github.com/deepseek-ai/deepseek-harness)<br>2,757/天 | [morluto/rea](https://github.com/morluto/rea)<br>478,153 ★ |
| **[開發者工具](#開發者工具)** | 無 | [astral-sh/uv](https://github.com/astral-sh/uv)<br>88.1/天 | [zed-industries/zed](https://github.com/zed-industries/zed)<br>126/天 | [zed-industries/zed](https://github.com/zed-industries/zed)<br>75.2/天 | [oven-sh/bun](https://github.com/oven-sh/bun)<br>96,966 ★ |
| **[資安](#資安)** | 無 | [aquasecurity/trivy](https://github.com/aquasecurity/trivy)<br>33.0/天 | [aquasecurity/trivy](https://github.com/aquasecurity/trivy)<br>35.0/天 | [aquasecurity/trivy](https://github.com/aquasecurity/trivy)<br>29.1/天 | [aquasecurity/trivy](https://github.com/aquasecurity/trivy)<br>39,733 ★ |
| **[Web / 前端](#web--前端)** | [SilverFeit/StikSound](https://github.com/SilverFeit/StikSound)<br>160/天 | [shadcn-ui/ui](https://github.com/shadcn-ui/ui)<br>92.3/天 | [shadcn-ui/ui](https://github.com/shadcn-ui/ui)<br>91.4/天 | [shadcn-ui/ui](https://github.com/shadcn-ui/ui)<br>83.4/天 | [facebook/react](https://github.com/facebook/react)<br>252,939 ★ |
| **[基礎建設](#基礎建設)** | 無 | [caddyserver/caddy](https://github.com/caddyserver/caddy)<br>56.1/天 | [caddyserver/caddy](https://github.com/caddyserver/caddy)<br>41.5/天 | [caddyserver/caddy](https://github.com/caddyserver/caddy)<br>33.8/天 | [kubernetes/kubernetes](https://github.com/kubernetes/kubernetes)<br>129,337 ★ |
| **[設計 / 創意](#設計--創意)** | 無 | [excalidraw/excalidraw](https://github.com/excalidraw/excalidraw)<br>61.3/天 | [excalidraw/excalidraw](https://github.com/excalidraw/excalidraw)<br>64.7/天 | [excalidraw/excalidraw](https://github.com/excalidraw/excalidraw)<br>73.2/天 | [excalidraw/excalidraw](https://github.com/excalidraw/excalidraw)<br>136,294 ★ |
| **[資料](#資料)** | 無 | [duckdb/duckdb](https://github.com/duckdb/duckdb)<br>26.3/天 | [duckdb/duckdb](https://github.com/duckdb/duckdb)<br>28.3/天 | [duckdb/duckdb](https://github.com/duckdb/duckdb)<br>25.9/天 | [apache/superset](https://github.com/apache/superset)<br>75,678 ★ |

這裡每張榜只列前 10 名，完整的前 20 名見 [latest/rankings.zh-Hant.md](latest/rankings.zh-Hant.md)。

表裡每個專案只留一句話；完整介紹（含工具名稱、技術細節）見 [docs/DETAILS.zh-Hant.md](docs/DETAILS.zh-Hant.md)。

## 常見問題

### GitHub 漲星榜是什麼？

依每天新增星號、而不是總星號替 GitHub 儲存庫排名的榜單。AI 是主榜，後面還有六個分類；資料由腳本從 GitHub API 產生。 [了解更多](docs/FAQ.md#what-is-github-risers)

### 和 GitHub Trending 有什麼不同？

GitHub Trending 是 GitHub 官方頁面；GitHub 漲星榜是獨立的開源專案，規則公開，有五種語言，並保存每次更新的歷史。它與 GitHub 官方沒有關聯。 [了解更多](docs/FAQ.md#is-it-the-same-as-github-trending)

### 多久更新一次？

每天更新；每次執行都會存檔。 [了解更多](docs/FAQ.md#how-often-is-it-updated)

### 資料怎麼算？

取最近 7、30 或 365 個完整 UTC 日的新增星號，再除以天數。數字全部來自 GitHub API，沒有手填或估算。 [了解更多](docs/FAQ.md#how-is-the-growth-rate-computed)

### 怎麼看、怎麼參與？

看下面的榜，完整前 20 名在 latest/。要收錄專案，改 data/projects.json（五種語言）並發 pull request。 [了解更多](docs/FAQ.md#how-can-i-suggest-a-project-or-report-a-mistake)

## 人工智慧

> 大型語言模型、代理、MCP、程式設計助手與生成式 AI

### 最熱新儲存庫（近 7 天內建立）

| # | 專案 | 建立時間（UTC） | 總星號 | 星號/天 |
|---|---|---|---:|---:|
| 1 | [EL4CTEO/fast-anything](https://github.com/EL4CTEO/fast-anything)<br>程式太慢？讓代理只重寫最慢的5% | 2026-11-21<br><sub>4.1 天</sub> | 3,889 | 942.8 |
| 2 | [qianyiai/kurocat](https://github.com/qianyiai/kurocat)<br>開源免費的置頂桌面打字小貓伴侶 | 2026-11-21<br><sub>4.1 天</sub> | 938 | 230.1 |
| 3 | [INK-Q/agy-fast](https://github.com/INK-Q/agy-fast)<br>對話太耗Token？幫你減少額度消耗 | 2026-11-19<br><sub>6.5 天</sub> | 1,482 | 227.0 |
| 4 | [erkamyaman/safe-anything](https://github.com/erkamyaman/safe-anything)<br>趕在別人發現前，快速找出系統漏洞 | 2026-11-22<br><sub>3.0 天</sub> | 687 | 226.1 |
| 5 | [chanke17/KuroCat](https://github.com/chanke17/KuroCat)<br>在桌面養一隻隨時互動的小萌貓 | 2026-11-23<br><sub>2.7 天</sub> | 514 | 191.1 |
| 6 | [danielwh2/sprite-stacking](https://github.com/danielwh2/sprite-stacking)<br>四張像素畫直接變能旋轉的偽3D | 2026-11-20<br><sub>5.1 天</sub> | 884 | 172.3 |
| 7 | [sous-labs/songe](https://github.com/sous-labs/songe)<br>閒置算力浪費了？用來訓練你的本機模型 | 2026-11-20<br><sub>5.3 天</sub> | 832 | 157.7 |
| 8 | [matheusmongarde/garimpo](https://github.com/matheusmongarde/garimpo)<br>找不到客戶？開源從地圖搜店到談單收款 | 2026-11-24<br><sub>1.0 天</sub> | 154 | 154.0 |
| 9 | [Developing-Gamer/agent-sim](https://github.com/Developing-Gamer/agent-sim)<br>在 Linux 上為 AI 代理運行 iOS 模擬器 | 2026-11-21<br><sub>3.9 天</sub> | 590 | 151.9 |
| 10 | [w01fb0ss/PiBot](https://github.com/w01fb0ss/PiBot)<br>在桌面運行開源的本機AI代理團隊 | 2026-11-21<br><sub>4.5 天</sub> | 587 | 132.0 |

<details>
<summary>本榜星號歷史曲線</summary>

<a href="https://www.star-history.com/#EL4CTEO/fast-anything&Date"><img src="https://api.star-history.com/svg?repos=EL4CTEO/fast-anything&type=Date" width="260" alt="EL4CTEO/fast-anything 的星號歷史曲線"></a>

<a href="https://www.star-history.com/#qianyiai/kurocat&Date"><img src="https://api.star-history.com/svg?repos=qianyiai/kurocat&type=Date" width="260" alt="qianyiai/kurocat 的星號歷史曲線"></a>

<a href="https://www.star-history.com/#INK-Q/agy-fast&Date"><img src="https://api.star-history.com/svg?repos=INK-Q/agy-fast&type=Date" width="260" alt="INK-Q/agy-fast 的星號歷史曲線"></a>

<a href="https://www.star-history.com/#erkamyaman/safe-anything&Date"><img src="https://api.star-history.com/svg?repos=erkamyaman/safe-anything&type=Date" width="260" alt="erkamyaman/safe-anything 的星號歷史曲線"></a>

<a href="https://www.star-history.com/#chanke17/KuroCat&Date"><img src="https://api.star-history.com/svg?repos=chanke17/KuroCat&type=Date" width="260" alt="chanke17/KuroCat 的星號歷史曲線"></a>

<a href="https://www.star-history.com/#danielwh2/sprite-stacking&Date"><img src="https://api.star-history.com/svg?repos=danielwh2/sprite-stacking&type=Date" width="260" alt="danielwh2/sprite-stacking 的星號歷史曲線"></a>

<a href="https://www.star-history.com/#sous-labs/songe&Date"><img src="https://api.star-history.com/svg?repos=sous-labs/songe&type=Date" width="260" alt="sous-labs/songe 的星號歷史曲線"></a>

<a href="https://www.star-history.com/#matheusmongarde/garimpo&Date"><img src="https://api.star-history.com/svg?repos=matheusmongarde/garimpo&type=Date" width="260" alt="matheusmongarde/garimpo 的星號歷史曲線"></a>

<a href="https://www.star-history.com/#Developing-Gamer/agent-sim&Date"><img src="https://api.star-history.com/svg?repos=Developing-Gamer/agent-sim&type=Date" width="260" alt="Developing-Gamer/agent-sim 的星號歷史曲線"></a>

<a href="https://www.star-history.com/#w01fb0ss/PiBot&Date"><img src="https://api.star-history.com/svg?repos=w01fb0ss/PiBot&type=Date" width="260" alt="w01fb0ss/PiBot 的星號歷史曲線"></a>

</details>

### 本週成長最快（近 7 天）

| # | 專案 | 新增星號 | 星號/天 | 總星號 |
|---|---|---:|---:|---:|
| 1 | [morluto/rea](https://github.com/morluto/rea)<br>讓 AI 幫你克隆任何軟體<br>`人工智慧` | +11,103 | 1,586.1 | 478,153 |
| 2 | [stablyai/orca](https://github.com/stablyai/orca)<br>幾個 AI 一起寫，誰好用一眼看出<br>`人工智慧` | +8,805 | 1,257.9 | 137,655 |
| 3 | [DietrichGebert/ponytail](https://github.com/DietrichGebert/ponytail)<br>讓 AI 少寫廢程式碼，該寫的寫對<br>`人工智慧` | +5,019 | 717.0 | 198,590 |
| 4 | [affaan-m/ECC](https://github.com/affaan-m/ECC)<br>給程式設計 AI 加記憶、技能和安全檢查<br>`人工智慧` | +4,780 | 682.9 | 310,582 |
| 5 | [deepseek-ai/deepseek-harness](https://github.com/deepseek-ai/deepseek-harness)<br>想要什麼代理，用外掛自己拼<br>`人工智慧` | +3,788 | 541.1 | 286,961 |
| 6 | [heygen-com/hyperframes](https://github.com/heygen-com/hyperframes)<br>不會剪輯，寫網頁一樣就能出片<br>`人工智慧` | +3,674 | 524.9 | 90,021 |
| 7 | [Graphify-Labs/graphify](https://github.com/Graphify-Labs/graphify)<br>大專案看不過來，先看這張地圖<br>`人工智慧` | +3,425 | 489.3 | 153,258 |
| 8 | [Leonxlnx/taste-skill](https://github.com/Leonxlnx/taste-skill)<br>別再讓 AI 做出千篇一律的頁面<br>`人工智慧` | +3,395 | 485.0 | 121,455 |
| 9 | [anthropics/skills](https://github.com/anthropics/skills)<br>Claude 技能怎麼寫，照著官方學<br>`人工智慧` | +3,371 | 481.6 | 200,377 |
| 10 | [cloudflare/security-audit-skill](https://github.com/cloudflare/security-audit-skill)<br>AI 查程式碼漏洞，另一個 AI 逐條複核<br>`人工智慧` | +3,183 | 454.7 | 78,258 |

<details>
<summary>本榜星號歷史曲線</summary>

<a href="https://www.star-history.com/#morluto/rea&Date"><img src="https://api.star-history.com/svg?repos=morluto/rea&type=Date" width="260" alt="morluto/rea 的星號歷史曲線"></a>

<a href="https://www.star-history.com/#stablyai/orca&Date"><img src="https://api.star-history.com/svg?repos=stablyai/orca&type=Date" width="260" alt="stablyai/orca 的星號歷史曲線"></a>

<a href="https://www.star-history.com/#DietrichGebert/ponytail&Date"><img src="https://api.star-history.com/svg?repos=DietrichGebert/ponytail&type=Date" width="260" alt="DietrichGebert/ponytail 的星號歷史曲線"></a>

<a href="https://www.star-history.com/#affaan-m/ECC&Date"><img src="https://api.star-history.com/svg?repos=affaan-m/ECC&type=Date" width="260" alt="affaan-m/ECC 的星號歷史曲線"></a>

<a href="https://www.star-history.com/#deepseek-ai/deepseek-harness&Date"><img src="https://api.star-history.com/svg?repos=deepseek-ai/deepseek-harness&type=Date" width="260" alt="deepseek-ai/deepseek-harness 的星號歷史曲線"></a>

<a href="https://www.star-history.com/#heygen-com/hyperframes&Date"><img src="https://api.star-history.com/svg?repos=heygen-com/hyperframes&type=Date" width="260" alt="heygen-com/hyperframes 的星號歷史曲線"></a>

<a href="https://www.star-history.com/#Graphify-Labs/graphify&Date"><img src="https://api.star-history.com/svg?repos=Graphify-Labs/graphify&type=Date" width="260" alt="Graphify-Labs/graphify 的星號歷史曲線"></a>

<a href="https://www.star-history.com/#Leonxlnx/taste-skill&Date"><img src="https://api.star-history.com/svg?repos=Leonxlnx/taste-skill&type=Date" width="260" alt="Leonxlnx/taste-skill 的星號歷史曲線"></a>

<a href="https://www.star-history.com/#anthropics/skills&Date"><img src="https://api.star-history.com/svg?repos=anthropics/skills&type=Date" width="260" alt="anthropics/skills 的星號歷史曲線"></a>

<a href="https://www.star-history.com/#cloudflare/security-audit-skill&Date"><img src="https://api.star-history.com/svg?repos=cloudflare/security-audit-skill&type=Date" width="260" alt="cloudflare/security-audit-skill 的星號歷史曲線"></a>

</details>

### 本月成長最快（近 30 天）

| # | 專案 | 新增星號 | 星號/天 | 總星號 |
|---|---|---:|---:|---:|
| 1 | [morluto/rea](https://github.com/morluto/rea)<br>讓 AI 幫你克隆任何軟體<br>`人工智慧` | +93,477 | 3,115.9 | 478,153 |
| 2 | [stablyai/orca](https://github.com/stablyai/orca)<br>幾個 AI 一起寫，誰好用一眼看出<br>`人工智慧` | +31,335 | 1,044.5 | 137,655 |
| 3 | [cloudflare/security-audit-skill](https://github.com/cloudflare/security-audit-skill)<br>AI 查程式碼漏洞，另一個 AI 逐條複核<br>`人工智慧` | +31,005 | 1,033.5 | 78,258 |
| 4 | [deepseek-ai/deepseek-harness](https://github.com/deepseek-ai/deepseek-harness)<br>想要什麼代理，用外掛自己拼<br>`人工智慧` | +26,289 | 876.3 | 286,961 |
| 5 | [DietrichGebert/ponytail](https://github.com/DietrichGebert/ponytail)<br>讓 AI 少寫廢程式碼，該寫的寫對<br>`人工智慧` | +22,691 | 756.4 | 198,590 |
| 6 | [affaan-m/ECC](https://github.com/affaan-m/ECC)<br>給程式設計 AI 加記憶、技能和安全檢查<br>`人工智慧` | +22,482 | 749.4 | 310,582 |
| 7 | [yetone/magpie](https://github.com/yetone/magpie)<br>程式設計 AI 換模型，額度用完自動續<br>`人工智慧` | +19,798 | 659.9 | 41,432 |
| 8 | [Leonxlnx/taste-skill](https://github.com/Leonxlnx/taste-skill)<br>別再讓 AI 做出千篇一律的頁面<br>`人工智慧` | +19,073 | 635.8 | 121,455 |
| 9 | [Graphify-Labs/graphify](https://github.com/Graphify-Labs/graphify)<br>大專案看不過來，先看這張地圖<br>`人工智慧` | +18,173 | 605.8 | 153,258 |
| 10 | [heygen-com/hyperframes](https://github.com/heygen-com/hyperframes)<br>不會剪輯，寫網頁一樣就能出片<br>`人工智慧` | +17,691 | 589.7 | 90,021 |

<details>
<summary>本榜星號歷史曲線</summary>

<a href="https://www.star-history.com/#morluto/rea&Date"><img src="https://api.star-history.com/svg?repos=morluto/rea&type=Date" width="260" alt="morluto/rea 的星號歷史曲線"></a>

<a href="https://www.star-history.com/#stablyai/orca&Date"><img src="https://api.star-history.com/svg?repos=stablyai/orca&type=Date" width="260" alt="stablyai/orca 的星號歷史曲線"></a>

<a href="https://www.star-history.com/#cloudflare/security-audit-skill&Date"><img src="https://api.star-history.com/svg?repos=cloudflare/security-audit-skill&type=Date" width="260" alt="cloudflare/security-audit-skill 的星號歷史曲線"></a>

<a href="https://www.star-history.com/#deepseek-ai/deepseek-harness&Date"><img src="https://api.star-history.com/svg?repos=deepseek-ai/deepseek-harness&type=Date" width="260" alt="deepseek-ai/deepseek-harness 的星號歷史曲線"></a>

<a href="https://www.star-history.com/#DietrichGebert/ponytail&Date"><img src="https://api.star-history.com/svg?repos=DietrichGebert/ponytail&type=Date" width="260" alt="DietrichGebert/ponytail 的星號歷史曲線"></a>

<a href="https://www.star-history.com/#affaan-m/ECC&Date"><img src="https://api.star-history.com/svg?repos=affaan-m/ECC&type=Date" width="260" alt="affaan-m/ECC 的星號歷史曲線"></a>

<a href="https://www.star-history.com/#yetone/magpie&Date"><img src="https://api.star-history.com/svg?repos=yetone/magpie&type=Date" width="260" alt="yetone/magpie 的星號歷史曲線"></a>

<a href="https://www.star-history.com/#Leonxlnx/taste-skill&Date"><img src="https://api.star-history.com/svg?repos=Leonxlnx/taste-skill&type=Date" width="260" alt="Leonxlnx/taste-skill 的星號歷史曲線"></a>

<a href="https://www.star-history.com/#Graphify-Labs/graphify&Date"><img src="https://api.star-history.com/svg?repos=Graphify-Labs/graphify&type=Date" width="260" alt="Graphify-Labs/graphify 的星號歷史曲線"></a>

<a href="https://www.star-history.com/#heygen-com/hyperframes&Date"><img src="https://api.star-history.com/svg?repos=heygen-com/hyperframes&type=Date" width="260" alt="heygen-com/hyperframes 的星號歷史曲線"></a>

</details>

### 今年成長最快（近 365 天）

| # | 專案 | 新增星號 | 星號/天 | 總星號 |
|---|---|---:|---:|---:|
| 1 | [deepseek-ai/deepseek-harness](https://github.com/deepseek-ai/deepseek-harness)<br>想要什麼代理，用外掛自己拼<br>`人工智慧` | +286,724 | 2,757.0 †<br><sub>÷104 天</sub> | 286,961 |
| 2 | [morluto/rea](https://github.com/morluto/rea)<br>讓 AI 幫你克隆任何軟體<br>`人工智慧` | +477,552 | 2,122.5 †<br><sub>÷225 天</sub> | 478,153 |
| 3 | [DietrichGebert/ponytail](https://github.com/DietrichGebert/ponytail)<br>讓 AI 少寫廢程式碼，該寫的寫對<br>`人工智慧` | +198,279 | 1,194.5 †<br><sub>÷166 天</sub> | 198,590 |
| 4 | [openclaw/openclaw](https://github.com/openclaw/openclaw)<br>能把事做完的 AI 助理，跑在自己裝置上<br>`人工智慧` | +395,126 | 1,082.5 | 395,194 |
| 5 | [affaan-m/ECC](https://github.com/affaan-m/ECC)<br>給程式設計 AI 加記憶、技能和安全檢查<br>`人工智慧` | +310,345 | 997.9 †<br><sub>÷311 天</sub> | 310,582 |
| 6 | [NousResearch/hermes-agent](https://github.com/NousResearch/hermes-agent)<br>越用越會幹活的 AI 助手<br>`人工智慧` | +265,952 | 728.6 | 266,056 |
| 7 | [yetone/magpie](https://github.com/yetone/magpie)<br>程式設計 AI 換模型，額度用完自動續<br>`人工智慧` | +41,211 | 654.1 †<br><sub>÷63 天</sub> | 41,432 |
| 8 | [Graphify-Labs/graphify](https://github.com/Graphify-Labs/graphify)<br>大專案看不過來，先看這張地圖<br>`人工智慧` | +153,088 | 648.7 †<br><sub>÷236 天</sub> | 153,258 |
| 9 | [stablyai/orca](https://github.com/stablyai/orca)<br>幾個 AI 一起寫，誰好用一眼看出<br>`人工智慧` | +136,754 | 540.5 †<br><sub>÷253 天</sub> | 137,655 |
| 10 | [anomalyco/opencode](https://github.com/anomalyco/opencode)<br>終端機裡，有個開源 AI 幫你寫程式碼<br>`人工智慧` | +196,591 | 538.6 | 229,133 |

<details>
<summary>本榜星號歷史曲線</summary>

<a href="https://www.star-history.com/#deepseek-ai/deepseek-harness&Date"><img src="https://api.star-history.com/svg?repos=deepseek-ai/deepseek-harness&type=Date" width="260" alt="deepseek-ai/deepseek-harness 的星號歷史曲線"></a>

<a href="https://www.star-history.com/#morluto/rea&Date"><img src="https://api.star-history.com/svg?repos=morluto/rea&type=Date" width="260" alt="morluto/rea 的星號歷史曲線"></a>

<a href="https://www.star-history.com/#DietrichGebert/ponytail&Date"><img src="https://api.star-history.com/svg?repos=DietrichGebert/ponytail&type=Date" width="260" alt="DietrichGebert/ponytail 的星號歷史曲線"></a>

<a href="https://www.star-history.com/#openclaw/openclaw&Date"><img src="https://api.star-history.com/svg?repos=openclaw/openclaw&type=Date" width="260" alt="openclaw/openclaw 的星號歷史曲線"></a>

<a href="https://www.star-history.com/#affaan-m/ECC&Date"><img src="https://api.star-history.com/svg?repos=affaan-m/ECC&type=Date" width="260" alt="affaan-m/ECC 的星號歷史曲線"></a>

<a href="https://www.star-history.com/#NousResearch/hermes-agent&Date"><img src="https://api.star-history.com/svg?repos=NousResearch/hermes-agent&type=Date" width="260" alt="NousResearch/hermes-agent 的星號歷史曲線"></a>

<a href="https://www.star-history.com/#yetone/magpie&Date"><img src="https://api.star-history.com/svg?repos=yetone/magpie&type=Date" width="260" alt="yetone/magpie 的星號歷史曲線"></a>

<a href="https://www.star-history.com/#Graphify-Labs/graphify&Date"><img src="https://api.star-history.com/svg?repos=Graphify-Labs/graphify&type=Date" width="260" alt="Graphify-Labs/graphify 的星號歷史曲線"></a>

<a href="https://www.star-history.com/#stablyai/orca&Date"><img src="https://api.star-history.com/svg?repos=stablyai/orca&type=Date" width="260" alt="stablyai/orca 的星號歷史曲線"></a>

<a href="https://www.star-history.com/#anomalyco/opencode&Date"><img src="https://api.star-history.com/svg?repos=anomalyco/opencode&type=Date" width="260" alt="anomalyco/opencode 的星號歷史曲線"></a>

</details>

† 該儲存庫建立時間短於統計區間，因此「星號/天」是以儲存庫存在的天數（顯示在數字下方）計算，而不是以完整區間計算。

### 總星號數（歷史累計）

| # | 專案 | 總星號 |
|---|---|---:|
| 1 | [morluto/rea](https://github.com/morluto/rea)<br>讓 AI 幫你克隆任何軟體<br>`人工智慧` | 478,153 |
| 2 | [openclaw/openclaw](https://github.com/openclaw/openclaw)<br>能把事做完的 AI 助理，跑在自己裝置上<br>`人工智慧` | 395,194 |
| 3 | [affaan-m/ECC](https://github.com/affaan-m/ECC)<br>給程式設計 AI 加記憶、技能和安全檢查<br>`人工智慧` | 310,582 |
| 4 | [deepseek-ai/deepseek-harness](https://github.com/deepseek-ai/deepseek-harness)<br>想要什麼代理，用外掛自己拼<br>`人工智慧` | 286,961 |
| 5 | [NousResearch/hermes-agent](https://github.com/NousResearch/hermes-agent)<br>越用越會幹活的 AI 助手<br>`人工智慧` | 266,056 |
| 6 | [anomalyco/opencode](https://github.com/anomalyco/opencode)<br>終端機裡，有個開源 AI 幫你寫程式碼<br>`人工智慧` | 229,133 |
| 7 | [anthropics/skills](https://github.com/anthropics/skills)<br>Claude 技能怎麼寫，照著官方學<br>`人工智慧` | 200,377 |
| 8 | [DietrichGebert/ponytail](https://github.com/DietrichGebert/ponytail)<br>讓 AI 少寫廢程式碼，該寫的寫對<br>`人工智慧` | 198,590 |
| 9 | [farion1231/cc-switch](https://github.com/farion1231/cc-switch)<br>換介面不用改配置，一鍵切<br>`人工智慧` | 157,134 |
| 10 | [nextlevelbuilder/ui-ux-pro-max-skill](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill)<br>AI 做的介面，看著像專業設計<br>`人工智慧` | 154,095 |

<details>
<summary>本榜星號歷史曲線</summary>

<a href="https://www.star-history.com/#morluto/rea&Date"><img src="https://api.star-history.com/svg?repos=morluto/rea&type=Date" width="260" alt="morluto/rea 的星號歷史曲線"></a>

<a href="https://www.star-history.com/#openclaw/openclaw&Date"><img src="https://api.star-history.com/svg?repos=openclaw/openclaw&type=Date" width="260" alt="openclaw/openclaw 的星號歷史曲線"></a>

<a href="https://www.star-history.com/#affaan-m/ECC&Date"><img src="https://api.star-history.com/svg?repos=affaan-m/ECC&type=Date" width="260" alt="affaan-m/ECC 的星號歷史曲線"></a>

<a href="https://www.star-history.com/#deepseek-ai/deepseek-harness&Date"><img src="https://api.star-history.com/svg?repos=deepseek-ai/deepseek-harness&type=Date" width="260" alt="deepseek-ai/deepseek-harness 的星號歷史曲線"></a>

<a href="https://www.star-history.com/#NousResearch/hermes-agent&Date"><img src="https://api.star-history.com/svg?repos=NousResearch/hermes-agent&type=Date" width="260" alt="NousResearch/hermes-agent 的星號歷史曲線"></a>

<a href="https://www.star-history.com/#anomalyco/opencode&Date"><img src="https://api.star-history.com/svg?repos=anomalyco/opencode&type=Date" width="260" alt="anomalyco/opencode 的星號歷史曲線"></a>

<a href="https://www.star-history.com/#anthropics/skills&Date"><img src="https://api.star-history.com/svg?repos=anthropics/skills&type=Date" width="260" alt="anthropics/skills 的星號歷史曲線"></a>

<a href="https://www.star-history.com/#DietrichGebert/ponytail&Date"><img src="https://api.star-history.com/svg?repos=DietrichGebert/ponytail&type=Date" width="260" alt="DietrichGebert/ponytail 的星號歷史曲線"></a>

<a href="https://www.star-history.com/#farion1231/cc-switch&Date"><img src="https://api.star-history.com/svg?repos=farion1231/cc-switch&type=Date" width="260" alt="farion1231/cc-switch 的星號歷史曲線"></a>

<a href="https://www.star-history.com/#nextlevelbuilder/ui-ux-pro-max-skill&Date"><img src="https://api.star-history.com/svg?repos=nextlevelbuilder/ui-ux-pro-max-skill&type=Date" width="260" alt="nextlevelbuilder/ui-ux-pro-max-skill 的星號歷史曲線"></a>

</details>

## 開發者工具

> 命令列、編輯器、套件管理、程式碼檢查與建置工具

### 最熱新儲存庫（近 7 天內建立）

| # | 專案 | 建立時間（UTC） | 總星號 | 星號/天 |
|---|---|---|---:|---:|
| 1 | [Adabi0304/studioonepro7-release](https://github.com/Adabi0304/studioonepro7-release)<br>Studioonepro7發布，含全功能桌面套件 | 2026-11-21<br><sub>4.0 天</sub> | 340 | 84.6 |
| 2 | [cr4zyp4ul/quicken-deluxe](https://github.com/cr4zyp4ul/quicken-deluxe)<br>Quicken Deluxe桌面財務管理發布版 | 2026-11-21<br><sub>4.0 天</sub> | 338 | 84.0 |
| 3 | [Daax116/startall-back-utility](https://github.com/Daax116/startall-back-utility)<br>Startall Back 介面自訂桌面工具 | 2026-11-21<br><sub>4.0 天</sub> | 337 | 83.9 |
| 4 | [hariachayan5-dotcom/sp-flash-tool](https://github.com/hariachayan5-dotcom/sp-flash-tool)<br>MediaTek 裝置命令列設定工具 | 2026-11-21<br><sub>4.0 天</sub> | 337 | 83.9 |
| 5 | [official00shivansh-eng/ultra-iso](https://github.com/official00shivansh-eng/ultra-iso)<br>Ultra ISO 桌面光碟映像製作與轉換工具 | 2026-11-21<br><sub>4.0 天</sub> | 336 | 83.7 |
| 6 | [jomicat1989-dotcom/rust-external-trainer-tool](https://github.com/jomicat1989-dotcom/rust-external-trainer-tool)<br>Rust 外部修改工具，標為遊戲增強 | 2026-11-21<br><sub>4.0 天</sub> | 336 | 83.6 |
| 7 | [jshami391-bit/scrcpy-screen-mirroring](https://github.com/jshami391-bit/scrcpy-screen-mirroring)<br>Android 低延遲投螢與輸入控制 | 2026-11-21<br><sub>4.0 天</sub> | 336 | 83.6 |
| 8 | [dongarenikhilit047-star/portfolio-rebalancer](https://github.com/dongarenikhilit047-star/portfolio-rebalancer)<br>桌面投資組合配置與分配管理工具 | 2026-11-21<br><sub>4.1 天</sub> | 338 | 83.1 |
| 9 | [ayux777/metatrader-5-bot](https://github.com/ayux777/metatrader-5-bot)<br>MetaTrader 5 桌面機器人 | 2026-11-21<br><sub>4.1 天</sub> | 337 | 82.0 |
| 10 | [njoniktu5/microstation-utility](https://github.com/njoniktu5/microstation-utility)<br>MicroStation 桌面工程工具 | 2026-11-21<br><sub>4.1 天</sub> | 336 | 82.0 |

<details>
<summary>本榜星號歷史曲線</summary>

<a href="https://www.star-history.com/#Adabi0304/studioonepro7-release&Date"><img src="https://api.star-history.com/svg?repos=Adabi0304/studioonepro7-release&type=Date" width="260" alt="Adabi0304/studioonepro7-release 的星號歷史曲線"></a>

<a href="https://www.star-history.com/#cr4zyp4ul/quicken-deluxe&Date"><img src="https://api.star-history.com/svg?repos=cr4zyp4ul/quicken-deluxe&type=Date" width="260" alt="cr4zyp4ul/quicken-deluxe 的星號歷史曲線"></a>

<a href="https://www.star-history.com/#Daax116/startall-back-utility&Date"><img src="https://api.star-history.com/svg?repos=Daax116/startall-back-utility&type=Date" width="260" alt="Daax116/startall-back-utility 的星號歷史曲線"></a>

<a href="https://www.star-history.com/#hariachayan5-dotcom/sp-flash-tool&Date"><img src="https://api.star-history.com/svg?repos=hariachayan5-dotcom/sp-flash-tool&type=Date" width="260" alt="hariachayan5-dotcom/sp-flash-tool 的星號歷史曲線"></a>

<a href="https://www.star-history.com/#official00shivansh-eng/ultra-iso&Date"><img src="https://api.star-history.com/svg?repos=official00shivansh-eng/ultra-iso&type=Date" width="260" alt="official00shivansh-eng/ultra-iso 的星號歷史曲線"></a>

<a href="https://www.star-history.com/#jomicat1989-dotcom/rust-external-trainer-tool&Date"><img src="https://api.star-history.com/svg?repos=jomicat1989-dotcom/rust-external-trainer-tool&type=Date" width="260" alt="jomicat1989-dotcom/rust-external-trainer-tool 的星號歷史曲線"></a>

<a href="https://www.star-history.com/#jshami391-bit/scrcpy-screen-mirroring&Date"><img src="https://api.star-history.com/svg?repos=jshami391-bit/scrcpy-screen-mirroring&type=Date" width="260" alt="jshami391-bit/scrcpy-screen-mirroring 的星號歷史曲線"></a>

<a href="https://www.star-history.com/#dongarenikhilit047-star/portfolio-rebalancer&Date"><img src="https://api.star-history.com/svg?repos=dongarenikhilit047-star/portfolio-rebalancer&type=Date" width="260" alt="dongarenikhilit047-star/portfolio-rebalancer 的星號歷史曲線"></a>

<a href="https://www.star-history.com/#ayux777/metatrader-5-bot&Date"><img src="https://api.star-history.com/svg?repos=ayux777/metatrader-5-bot&type=Date" width="260" alt="ayux777/metatrader-5-bot 的星號歷史曲線"></a>

<a href="https://www.star-history.com/#njoniktu5/microstation-utility&Date"><img src="https://api.star-history.com/svg?repos=njoniktu5/microstation-utility&type=Date" width="260" alt="njoniktu5/microstation-utility 的星號歷史曲線"></a>

</details>

### 本週成長最快（近 7 天）

| # | 專案 | 新增星號 | 星號/天 | 總星號 |
|---|---|---:|---:|---:|
| 1 | [astral-sh/uv](https://github.com/astral-sh/uv)<br>裝 Python 套件，不用再乾等<br>`開發者工具` | +617 | 88.1 | 92,645 |
| 2 | [zed-industries/zed](https://github.com/zed-industries/zed)<br>開啟就快，還能多人一起寫程式碼<br>`開發者工具` | +499 | 71.3 | 95,728 |
| 3 | [BurntSushi/ripgrep](https://github.com/BurntSushi/ripgrep)<br>翻遍整個目錄找文字，比 grep 快<br>`開發者工具` | +294 | 42.0 | 70,331 |
| 4 | [jdx/mise](https://github.com/jdx/mise)<br>開發工具、環境變數、任務，一個工具管<br>`開發者工具` | +249 | 35.6 | 36,517 |
| 5 | [oven-sh/bun](https://github.com/oven-sh/bun)<br>執行打包測試裝套件，一個工具全包<br>`開發者工具` | +229 | 32.7 | 96,966 |
| 6 | [cli/cli](https://github.com/cli/cli)<br>不開網頁，命令列裡處理 GitHub<br>`開發者工具` | +148 | 21.1 | 47,204 |
| 7 | [helix-editor/helix](https://github.com/helix-editor/helix)<br>語法上色、語言服務都內建的文字編輯器<br>`開發者工具` | +123 | 17.6 | 47,019 |
| 8 | [biomejs/biome](https://github.com/biomejs/biome)<br>網頁程式碼格式和檢查，一個工具搞定<br>`開發者工具` | +90 | 12.9 | 26,210 |

<details>
<summary>本榜星號歷史曲線</summary>

<a href="https://www.star-history.com/#astral-sh/uv&Date"><img src="https://api.star-history.com/svg?repos=astral-sh/uv&type=Date" width="260" alt="astral-sh/uv 的星號歷史曲線"></a>

<a href="https://www.star-history.com/#zed-industries/zed&Date"><img src="https://api.star-history.com/svg?repos=zed-industries/zed&type=Date" width="260" alt="zed-industries/zed 的星號歷史曲線"></a>

<a href="https://www.star-history.com/#BurntSushi/ripgrep&Date"><img src="https://api.star-history.com/svg?repos=BurntSushi/ripgrep&type=Date" width="260" alt="BurntSushi/ripgrep 的星號歷史曲線"></a>

<a href="https://www.star-history.com/#jdx/mise&Date"><img src="https://api.star-history.com/svg?repos=jdx/mise&type=Date" width="260" alt="jdx/mise 的星號歷史曲線"></a>

<a href="https://www.star-history.com/#oven-sh/bun&Date"><img src="https://api.star-history.com/svg?repos=oven-sh/bun&type=Date" width="260" alt="oven-sh/bun 的星號歷史曲線"></a>

<a href="https://www.star-history.com/#cli/cli&Date"><img src="https://api.star-history.com/svg?repos=cli/cli&type=Date" width="260" alt="cli/cli 的星號歷史曲線"></a>

<a href="https://www.star-history.com/#helix-editor/helix&Date"><img src="https://api.star-history.com/svg?repos=helix-editor/helix&type=Date" width="260" alt="helix-editor/helix 的星號歷史曲線"></a>

<a href="https://www.star-history.com/#biomejs/biome&Date"><img src="https://api.star-history.com/svg?repos=biomejs/biome&type=Date" width="260" alt="biomejs/biome 的星號歷史曲線"></a>

</details>

### 本月成長最快（近 30 天）

| # | 專案 | 新增星號 | 星號/天 | 總星號 |
|---|---|---:|---:|---:|
| 1 | [zed-industries/zed](https://github.com/zed-industries/zed)<br>開啟就快，還能多人一起寫程式碼<br>`開發者工具` | +3,771 | 125.7 | 95,728 |
| 2 | [astral-sh/uv](https://github.com/astral-sh/uv)<br>裝 Python 套件，不用再乾等<br>`開發者工具` | +1,651 | 55.0 | 92,645 |
| 3 | [jdx/mise](https://github.com/jdx/mise)<br>開發工具、環境變數、任務，一個工具管<br>`開發者工具` | +1,201 | 40.0 | 36,517 |
| 4 | [BurntSushi/ripgrep](https://github.com/BurntSushi/ripgrep)<br>翻遍整個目錄找文字，比 grep 快<br>`開發者工具` | +998 | 33.3 | 70,331 |
| 5 | [oven-sh/bun](https://github.com/oven-sh/bun)<br>執行打包測試裝套件，一個工具全包<br>`開發者工具` | +707 | 23.6 | 96,966 |
| 6 | [cli/cli](https://github.com/cli/cli)<br>不開網頁，命令列裡處理 GitHub<br>`開發者工具` | +509 | 17.0 | 47,204 |
| 7 | [helix-editor/helix](https://github.com/helix-editor/helix)<br>語法上色、語言服務都內建的文字編輯器<br>`開發者工具` | +434 | 14.5 | 47,019 |
| 8 | [biomejs/biome](https://github.com/biomejs/biome)<br>網頁程式碼格式和檢查，一個工具搞定<br>`開發者工具` | +260 | 8.7 | 26,210 |

<details>
<summary>本榜星號歷史曲線</summary>

<a href="https://www.star-history.com/#zed-industries/zed&Date"><img src="https://api.star-history.com/svg?repos=zed-industries/zed&type=Date" width="260" alt="zed-industries/zed 的星號歷史曲線"></a>

<a href="https://www.star-history.com/#astral-sh/uv&Date"><img src="https://api.star-history.com/svg?repos=astral-sh/uv&type=Date" width="260" alt="astral-sh/uv 的星號歷史曲線"></a>

<a href="https://www.star-history.com/#jdx/mise&Date"><img src="https://api.star-history.com/svg?repos=jdx/mise&type=Date" width="260" alt="jdx/mise 的星號歷史曲線"></a>

<a href="https://www.star-history.com/#BurntSushi/ripgrep&Date"><img src="https://api.star-history.com/svg?repos=BurntSushi/ripgrep&type=Date" width="260" alt="BurntSushi/ripgrep 的星號歷史曲線"></a>

<a href="https://www.star-history.com/#oven-sh/bun&Date"><img src="https://api.star-history.com/svg?repos=oven-sh/bun&type=Date" width="260" alt="oven-sh/bun 的星號歷史曲線"></a>

<a href="https://www.star-history.com/#cli/cli&Date"><img src="https://api.star-history.com/svg?repos=cli/cli&type=Date" width="260" alt="cli/cli 的星號歷史曲線"></a>

<a href="https://www.star-history.com/#helix-editor/helix&Date"><img src="https://api.star-history.com/svg?repos=helix-editor/helix&type=Date" width="260" alt="helix-editor/helix 的星號歷史曲線"></a>

<a href="https://www.star-history.com/#biomejs/biome&Date"><img src="https://api.star-history.com/svg?repos=biomejs/biome&type=Date" width="260" alt="biomejs/biome 的星號歷史曲線"></a>

</details>

### 今年成長最快（近 365 天）

| # | 專案 | 新增星號 | 星號/天 | 總星號 |
|---|---|---:|---:|---:|
| 1 | [zed-industries/zed](https://github.com/zed-industries/zed)<br>開啟就快，還能多人一起寫程式碼<br>`開發者工具` | +27,446 | 75.2 | 95,728 |
| 2 | [astral-sh/uv](https://github.com/astral-sh/uv)<br>裝 Python 套件，不用再乾等<br>`開發者工具` | +20,609 | 56.5 | 92,645 |
| 3 | [oven-sh/bun](https://github.com/oven-sh/bun)<br>執行打包測試裝套件，一個工具全包<br>`開發者工具` | +16,577 | 45.4 | 96,966 |
| 4 | [jdx/mise](https://github.com/jdx/mise)<br>開發工具、環境變數、任務，一個工具管<br>`開發者工具` | +15,349 | 42.1 | 36,517 |
| 5 | [BurntSushi/ripgrep](https://github.com/BurntSushi/ripgrep)<br>翻遍整個目錄找文字，比 grep 快<br>`開發者工具` | +13,440 | 36.8 | 70,331 |
| 6 | [helix-editor/helix](https://github.com/helix-editor/helix)<br>語法上色、語言服務都內建的文字編輯器<br>`開發者工具` | +6,439 | 17.6 | 47,019 |
| 7 | [cli/cli](https://github.com/cli/cli)<br>不開網頁，命令列裡處理 GitHub<br>`開發者工具` | +6,387 | 17.5 | 47,204 |
| 8 | [biomejs/biome](https://github.com/biomejs/biome)<br>網頁程式碼格式和檢查，一個工具搞定<br>`開發者工具` | +4,361 | 11.9 | 26,210 |

<details>
<summary>本榜星號歷史曲線</summary>

<a href="https://www.star-history.com/#zed-industries/zed&Date"><img src="https://api.star-history.com/svg?repos=zed-industries/zed&type=Date" width="260" alt="zed-industries/zed 的星號歷史曲線"></a>

<a href="https://www.star-history.com/#astral-sh/uv&Date"><img src="https://api.star-history.com/svg?repos=astral-sh/uv&type=Date" width="260" alt="astral-sh/uv 的星號歷史曲線"></a>

<a href="https://www.star-history.com/#oven-sh/bun&Date"><img src="https://api.star-history.com/svg?repos=oven-sh/bun&type=Date" width="260" alt="oven-sh/bun 的星號歷史曲線"></a>

<a href="https://www.star-history.com/#jdx/mise&Date"><img src="https://api.star-history.com/svg?repos=jdx/mise&type=Date" width="260" alt="jdx/mise 的星號歷史曲線"></a>

<a href="https://www.star-history.com/#BurntSushi/ripgrep&Date"><img src="https://api.star-history.com/svg?repos=BurntSushi/ripgrep&type=Date" width="260" alt="BurntSushi/ripgrep 的星號歷史曲線"></a>

<a href="https://www.star-history.com/#helix-editor/helix&Date"><img src="https://api.star-history.com/svg?repos=helix-editor/helix&type=Date" width="260" alt="helix-editor/helix 的星號歷史曲線"></a>

<a href="https://www.star-history.com/#cli/cli&Date"><img src="https://api.star-history.com/svg?repos=cli/cli&type=Date" width="260" alt="cli/cli 的星號歷史曲線"></a>

<a href="https://www.star-history.com/#biomejs/biome&Date"><img src="https://api.star-history.com/svg?repos=biomejs/biome&type=Date" width="260" alt="biomejs/biome 的星號歷史曲線"></a>

</details>

### 總星號數（歷史累計）

| # | 專案 | 總星號 |
|---|---|---:|
| 1 | [oven-sh/bun](https://github.com/oven-sh/bun)<br>執行打包測試裝套件，一個工具全包<br>`開發者工具` | 96,966 |
| 2 | [zed-industries/zed](https://github.com/zed-industries/zed)<br>開啟就快，還能多人一起寫程式碼<br>`開發者工具` | 95,728 |
| 3 | [astral-sh/uv](https://github.com/astral-sh/uv)<br>裝 Python 套件，不用再乾等<br>`開發者工具` | 92,645 |
| 4 | [BurntSushi/ripgrep](https://github.com/BurntSushi/ripgrep)<br>翻遍整個目錄找文字，比 grep 快<br>`開發者工具` | 70,331 |
| 5 | [cli/cli](https://github.com/cli/cli)<br>不開網頁，命令列裡處理 GitHub<br>`開發者工具` | 47,204 |
| 6 | [helix-editor/helix](https://github.com/helix-editor/helix)<br>語法上色、語言服務都內建的文字編輯器<br>`開發者工具` | 47,019 |
| 7 | [jdx/mise](https://github.com/jdx/mise)<br>開發工具、環境變數、任務，一個工具管<br>`開發者工具` | 36,517 |
| 8 | [biomejs/biome](https://github.com/biomejs/biome)<br>網頁程式碼格式和檢查，一個工具搞定<br>`開發者工具` | 26,210 |

<details>
<summary>本榜星號歷史曲線</summary>

<a href="https://www.star-history.com/#oven-sh/bun&Date"><img src="https://api.star-history.com/svg?repos=oven-sh/bun&type=Date" width="260" alt="oven-sh/bun 的星號歷史曲線"></a>

<a href="https://www.star-history.com/#zed-industries/zed&Date"><img src="https://api.star-history.com/svg?repos=zed-industries/zed&type=Date" width="260" alt="zed-industries/zed 的星號歷史曲線"></a>

<a href="https://www.star-history.com/#astral-sh/uv&Date"><img src="https://api.star-history.com/svg?repos=astral-sh/uv&type=Date" width="260" alt="astral-sh/uv 的星號歷史曲線"></a>

<a href="https://www.star-history.com/#BurntSushi/ripgrep&Date"><img src="https://api.star-history.com/svg?repos=BurntSushi/ripgrep&type=Date" width="260" alt="BurntSushi/ripgrep 的星號歷史曲線"></a>

<a href="https://www.star-history.com/#cli/cli&Date"><img src="https://api.star-history.com/svg?repos=cli/cli&type=Date" width="260" alt="cli/cli 的星號歷史曲線"></a>

<a href="https://www.star-history.com/#helix-editor/helix&Date"><img src="https://api.star-history.com/svg?repos=helix-editor/helix&type=Date" width="260" alt="helix-editor/helix 的星號歷史曲線"></a>

<a href="https://www.star-history.com/#jdx/mise&Date"><img src="https://api.star-history.com/svg?repos=jdx/mise&type=Date" width="260" alt="jdx/mise 的星號歷史曲線"></a>

<a href="https://www.star-history.com/#biomejs/biome&Date"><img src="https://api.star-history.com/svg?repos=biomejs/biome&type=Date" width="260" alt="biomejs/biome 的星號歷史曲線"></a>

</details>

## 資安

> 弱點掃描、靜態分析、供應鏈與執行時資安

### 最熱新儲存庫（近 7 天內建立）

本次執行中沒有符合條件的新儲存庫。

### 本週成長最快（近 7 天）

| # | 專案 | 新增星號 | 星號/天 | 總星號 |
|---|---|---:|---:|---:|
| 1 | [aquasecurity/trivy](https://github.com/aquasecurity/trivy)<br>容器和程式碼倉，一次掃完安全問題<br>`資安` | +231 | 33.0 | 39,733 |
| 2 | [projectdiscovery/nuclei](https://github.com/projectdiscovery/nuclei)<br>寫個模板，就能批次掃漏洞<br>`資安` | +221 | 31.6 | 33,279 |
| 3 | [semgrep/semgrep](https://github.com/semgrep/semgrep)<br>程式碼裡的問題，提交前先揪出來<br>`資安` | +148 | 21.1 | 17,940 |
| 4 | [OWASP/CheatSheetSeries](https://github.com/OWASP/CheatSheetSeries)<br>應用程式資安怎麼做，看這套速查表<br>`資安` | +97 | 13.9 | 34,199 |
| 5 | [google/osv-scanner](https://github.com/google/osv-scanner)<br>用的依賴安不安全，掃一下就知道<br>`資安` | +76 | 10.9 | 11,626 |
| 6 | [anchore/grype](https://github.com/anchore/grype)<br>容器映像檔有沒有漏洞，掃一下就知道<br>`資安` | +63 | 9.0 | 13,345 |
| 7 | [falcosecurity/falco](https://github.com/falcosecurity/falco)<br>雲上有異常，第一時間知道<br>`資安` | +27 | 3.9 | 9,613 |
| 8 | [securego/gosec](https://github.com/securego/gosec)<br>Go 程式碼的資安隱患，掃一遍就知道<br>`資安` | +11 | 1.6 | 9,024 |

<details>
<summary>本榜星號歷史曲線</summary>

<a href="https://www.star-history.com/#aquasecurity/trivy&Date"><img src="https://api.star-history.com/svg?repos=aquasecurity/trivy&type=Date" width="260" alt="aquasecurity/trivy 的星號歷史曲線"></a>

<a href="https://www.star-history.com/#projectdiscovery/nuclei&Date"><img src="https://api.star-history.com/svg?repos=projectdiscovery/nuclei&type=Date" width="260" alt="projectdiscovery/nuclei 的星號歷史曲線"></a>

<a href="https://www.star-history.com/#semgrep/semgrep&Date"><img src="https://api.star-history.com/svg?repos=semgrep/semgrep&type=Date" width="260" alt="semgrep/semgrep 的星號歷史曲線"></a>

<a href="https://www.star-history.com/#OWASP/CheatSheetSeries&Date"><img src="https://api.star-history.com/svg?repos=OWASP/CheatSheetSeries&type=Date" width="260" alt="OWASP/CheatSheetSeries 的星號歷史曲線"></a>

<a href="https://www.star-history.com/#google/osv-scanner&Date"><img src="https://api.star-history.com/svg?repos=google/osv-scanner&type=Date" width="260" alt="google/osv-scanner 的星號歷史曲線"></a>

<a href="https://www.star-history.com/#anchore/grype&Date"><img src="https://api.star-history.com/svg?repos=anchore/grype&type=Date" width="260" alt="anchore/grype 的星號歷史曲線"></a>

<a href="https://www.star-history.com/#falcosecurity/falco&Date"><img src="https://api.star-history.com/svg?repos=falcosecurity/falco&type=Date" width="260" alt="falcosecurity/falco 的星號歷史曲線"></a>

<a href="https://www.star-history.com/#securego/gosec&Date"><img src="https://api.star-history.com/svg?repos=securego/gosec&type=Date" width="260" alt="securego/gosec 的星號歷史曲線"></a>

</details>

### 本月成長最快（近 30 天）

| # | 專案 | 新增星號 | 星號/天 | 總星號 |
|---|---|---:|---:|---:|
| 1 | [aquasecurity/trivy](https://github.com/aquasecurity/trivy)<br>容器和程式碼倉，一次掃完安全問題<br>`資安` | +1,050 | 35.0 | 39,733 |
| 2 | [projectdiscovery/nuclei](https://github.com/projectdiscovery/nuclei)<br>寫個模板，就能批次掃漏洞<br>`資安` | +1,021 | 34.0 | 33,279 |
| 3 | [semgrep/semgrep](https://github.com/semgrep/semgrep)<br>程式碼裡的問題，提交前先揪出來<br>`資安` | +682 | 22.7 | 17,940 |
| 4 | [OWASP/CheatSheetSeries](https://github.com/OWASP/CheatSheetSeries)<br>應用程式資安怎麼做，看這套速查表<br>`資安` | +486 | 16.2 | 34,199 |
| 5 | [google/osv-scanner](https://github.com/google/osv-scanner)<br>用的依賴安不安全，掃一下就知道<br>`資安` | +367 | 12.2 | 11,626 |
| 6 | [anchore/grype](https://github.com/anchore/grype)<br>容器映像檔有沒有漏洞，掃一下就知道<br>`資安` | +246 | 8.2 | 13,345 |
| 7 | [falcosecurity/falco](https://github.com/falcosecurity/falco)<br>雲上有異常，第一時間知道<br>`資安` | +100 | 3.3 | 9,613 |
| 8 | [securego/gosec](https://github.com/securego/gosec)<br>Go 程式碼的資安隱患，掃一遍就知道<br>`資安` | +41 | 1.4 | 9,024 |

<details>
<summary>本榜星號歷史曲線</summary>

<a href="https://www.star-history.com/#aquasecurity/trivy&Date"><img src="https://api.star-history.com/svg?repos=aquasecurity/trivy&type=Date" width="260" alt="aquasecurity/trivy 的星號歷史曲線"></a>

<a href="https://www.star-history.com/#projectdiscovery/nuclei&Date"><img src="https://api.star-history.com/svg?repos=projectdiscovery/nuclei&type=Date" width="260" alt="projectdiscovery/nuclei 的星號歷史曲線"></a>

<a href="https://www.star-history.com/#semgrep/semgrep&Date"><img src="https://api.star-history.com/svg?repos=semgrep/semgrep&type=Date" width="260" alt="semgrep/semgrep 的星號歷史曲線"></a>

<a href="https://www.star-history.com/#OWASP/CheatSheetSeries&Date"><img src="https://api.star-history.com/svg?repos=OWASP/CheatSheetSeries&type=Date" width="260" alt="OWASP/CheatSheetSeries 的星號歷史曲線"></a>

<a href="https://www.star-history.com/#google/osv-scanner&Date"><img src="https://api.star-history.com/svg?repos=google/osv-scanner&type=Date" width="260" alt="google/osv-scanner 的星號歷史曲線"></a>

<a href="https://www.star-history.com/#anchore/grype&Date"><img src="https://api.star-history.com/svg?repos=anchore/grype&type=Date" width="260" alt="anchore/grype 的星號歷史曲線"></a>

<a href="https://www.star-history.com/#falcosecurity/falco&Date"><img src="https://api.star-history.com/svg?repos=falcosecurity/falco&type=Date" width="260" alt="falcosecurity/falco 的星號歷史曲線"></a>

<a href="https://www.star-history.com/#securego/gosec&Date"><img src="https://api.star-history.com/svg?repos=securego/gosec&type=Date" width="260" alt="securego/gosec 的星號歷史曲線"></a>

</details>

### 今年成長最快（近 365 天）

| # | 專案 | 新增星號 | 星號/天 | 總星號 |
|---|---|---:|---:|---:|
| 1 | [aquasecurity/trivy](https://github.com/aquasecurity/trivy)<br>容器和程式碼倉，一次掃完安全問題<br>`資安` | +10,636 | 29.1 | 39,733 |
| 2 | [projectdiscovery/nuclei](https://github.com/projectdiscovery/nuclei)<br>寫個模板，就能批次掃漏洞<br>`資安` | +8,004 | 21.9 | 33,279 |
| 3 | [semgrep/semgrep](https://github.com/semgrep/semgrep)<br>程式碼裡的問題，提交前先揪出來<br>`資安` | +4,696 | 12.9 | 17,940 |
| 4 | [OWASP/CheatSheetSeries](https://github.com/OWASP/CheatSheetSeries)<br>應用程式資安怎麼做，看這套速查表<br>`資安` | +3,720 | 10.2 | 34,199 |
| 5 | [google/osv-scanner](https://github.com/google/osv-scanner)<br>用的依賴安不安全，掃一下就知道<br>`資安` | +3,650 | 10.0 | 11,626 |
| 6 | [anchore/grype](https://github.com/anchore/grype)<br>容器映像檔有沒有漏洞，掃一下就知道<br>`資安` | +2,427 | 6.6 | 13,345 |
| 7 | [falcosecurity/falco](https://github.com/falcosecurity/falco)<br>雲上有異常，第一時間知道<br>`資安` | +1,279 | 3.5 | 9,613 |
| 8 | [securego/gosec](https://github.com/securego/gosec)<br>Go 程式碼的資安隱患，掃一遍就知道<br>`資安` | +561 | 1.5 | 9,024 |

<details>
<summary>本榜星號歷史曲線</summary>

<a href="https://www.star-history.com/#aquasecurity/trivy&Date"><img src="https://api.star-history.com/svg?repos=aquasecurity/trivy&type=Date" width="260" alt="aquasecurity/trivy 的星號歷史曲線"></a>

<a href="https://www.star-history.com/#projectdiscovery/nuclei&Date"><img src="https://api.star-history.com/svg?repos=projectdiscovery/nuclei&type=Date" width="260" alt="projectdiscovery/nuclei 的星號歷史曲線"></a>

<a href="https://www.star-history.com/#semgrep/semgrep&Date"><img src="https://api.star-history.com/svg?repos=semgrep/semgrep&type=Date" width="260" alt="semgrep/semgrep 的星號歷史曲線"></a>

<a href="https://www.star-history.com/#OWASP/CheatSheetSeries&Date"><img src="https://api.star-history.com/svg?repos=OWASP/CheatSheetSeries&type=Date" width="260" alt="OWASP/CheatSheetSeries 的星號歷史曲線"></a>

<a href="https://www.star-history.com/#google/osv-scanner&Date"><img src="https://api.star-history.com/svg?repos=google/osv-scanner&type=Date" width="260" alt="google/osv-scanner 的星號歷史曲線"></a>

<a href="https://www.star-history.com/#anchore/grype&Date"><img src="https://api.star-history.com/svg?repos=anchore/grype&type=Date" width="260" alt="anchore/grype 的星號歷史曲線"></a>

<a href="https://www.star-history.com/#falcosecurity/falco&Date"><img src="https://api.star-history.com/svg?repos=falcosecurity/falco&type=Date" width="260" alt="falcosecurity/falco 的星號歷史曲線"></a>

<a href="https://www.star-history.com/#securego/gosec&Date"><img src="https://api.star-history.com/svg?repos=securego/gosec&type=Date" width="260" alt="securego/gosec 的星號歷史曲線"></a>

</details>

### 總星號數（歷史累計）

| # | 專案 | 總星號 |
|---|---|---:|
| 1 | [aquasecurity/trivy](https://github.com/aquasecurity/trivy)<br>容器和程式碼倉，一次掃完安全問題<br>`資安` | 39,733 |
| 2 | [OWASP/CheatSheetSeries](https://github.com/OWASP/CheatSheetSeries)<br>應用程式資安怎麼做，看這套速查表<br>`資安` | 34,199 |
| 3 | [projectdiscovery/nuclei](https://github.com/projectdiscovery/nuclei)<br>寫個模板，就能批次掃漏洞<br>`資安` | 33,279 |
| 4 | [semgrep/semgrep](https://github.com/semgrep/semgrep)<br>程式碼裡的問題，提交前先揪出來<br>`資安` | 17,940 |
| 5 | [anchore/grype](https://github.com/anchore/grype)<br>容器映像檔有沒有漏洞，掃一下就知道<br>`資安` | 13,345 |
| 6 | [google/osv-scanner](https://github.com/google/osv-scanner)<br>用的依賴安不安全，掃一下就知道<br>`資安` | 11,626 |
| 7 | [falcosecurity/falco](https://github.com/falcosecurity/falco)<br>雲上有異常，第一時間知道<br>`資安` | 9,613 |
| 8 | [securego/gosec](https://github.com/securego/gosec)<br>Go 程式碼的資安隱患，掃一遍就知道<br>`資安` | 9,024 |

<details>
<summary>本榜星號歷史曲線</summary>

<a href="https://www.star-history.com/#aquasecurity/trivy&Date"><img src="https://api.star-history.com/svg?repos=aquasecurity/trivy&type=Date" width="260" alt="aquasecurity/trivy 的星號歷史曲線"></a>

<a href="https://www.star-history.com/#OWASP/CheatSheetSeries&Date"><img src="https://api.star-history.com/svg?repos=OWASP/CheatSheetSeries&type=Date" width="260" alt="OWASP/CheatSheetSeries 的星號歷史曲線"></a>

<a href="https://www.star-history.com/#projectdiscovery/nuclei&Date"><img src="https://api.star-history.com/svg?repos=projectdiscovery/nuclei&type=Date" width="260" alt="projectdiscovery/nuclei 的星號歷史曲線"></a>

<a href="https://www.star-history.com/#semgrep/semgrep&Date"><img src="https://api.star-history.com/svg?repos=semgrep/semgrep&type=Date" width="260" alt="semgrep/semgrep 的星號歷史曲線"></a>

<a href="https://www.star-history.com/#anchore/grype&Date"><img src="https://api.star-history.com/svg?repos=anchore/grype&type=Date" width="260" alt="anchore/grype 的星號歷史曲線"></a>

<a href="https://www.star-history.com/#google/osv-scanner&Date"><img src="https://api.star-history.com/svg?repos=google/osv-scanner&type=Date" width="260" alt="google/osv-scanner 的星號歷史曲線"></a>

<a href="https://www.star-history.com/#falcosecurity/falco&Date"><img src="https://api.star-history.com/svg?repos=falcosecurity/falco&type=Date" width="260" alt="falcosecurity/falco 的星號歷史曲線"></a>

<a href="https://www.star-history.com/#securego/gosec&Date"><img src="https://api.star-history.com/svg?repos=securego/gosec&type=Date" width="260" alt="securego/gosec 的星號歷史曲線"></a>

</details>

## Web / 前端

> 前端框架、UI 元件庫、CSS 與瀏覽器工具

### 最熱新儲存庫（近 7 天內建立）

| # | 專案 | 建立時間（UTC） | 總星號 | 星號/天 |
|---|---|---|---:|---:|
| 1 | [SilverFeit/StikSound](https://github.com/SilverFeit/StikSound)<br>給貼圖加上最多5秒的專屬聲音 | 2026-11-24<br><sub>1.0 天</sub> | 160 | 160.0 |
| 2 | [terry-holmes71/devlabs](https://github.com/terry-holmes71/devlabs) | 2026-11-23<br><sub>1.8 天</sub> | 128 | 69.8 |
| 3 | [Johnson-Durui/ApexCluster](https://github.com/Johnson-Durui/ApexCluster)<br>需求架構難寫，讓代理集群直出原型 | 2026-11-19<br><sub>6.7 天</sub> | 210 | 31.5 |
| 4 | [jianghao-jianghao-jianghao/newHoldem](https://github.com/jianghao-jianghao-jianghao/newHoldem)<br>自行架設 3D 德州撲克室，支援 AI 複盤 | 2026-11-20<br><sub>5.1 天</sub> | 149 | 29.0 |
| 5 | [AdityaKodez/trazo](https://github.com/AdityaKodez/trazo)<br>頁面太單調？為網頁貼上手繪蠟筆貼紙 | 2026-11-19<br><sub>6.5 天</sub> | 111 | 17.0 |

<details>
<summary>本榜星號歷史曲線</summary>

<a href="https://www.star-history.com/#SilverFeit/StikSound&Date"><img src="https://api.star-history.com/svg?repos=SilverFeit/StikSound&type=Date" width="260" alt="SilverFeit/StikSound 的星號歷史曲線"></a>

<a href="https://www.star-history.com/#terry-holmes71/devlabs&Date"><img src="https://api.star-history.com/svg?repos=terry-holmes71/devlabs&type=Date" width="260" alt="terry-holmes71/devlabs 的星號歷史曲線"></a>

<a href="https://www.star-history.com/#Johnson-Durui/ApexCluster&Date"><img src="https://api.star-history.com/svg?repos=Johnson-Durui/ApexCluster&type=Date" width="260" alt="Johnson-Durui/ApexCluster 的星號歷史曲線"></a>

<a href="https://www.star-history.com/#jianghao-jianghao-jianghao/newHoldem&Date"><img src="https://api.star-history.com/svg?repos=jianghao-jianghao-jianghao/newHoldem&type=Date" width="260" alt="jianghao-jianghao-jianghao/newHoldem 的星號歷史曲線"></a>

<a href="https://www.star-history.com/#AdityaKodez/trazo&Date"><img src="https://api.star-history.com/svg?repos=AdityaKodez/trazo&type=Date" width="260" alt="AdityaKodez/trazo 的星號歷史曲線"></a>

</details>

### 本週成長最快（近 7 天）

| # | 專案 | 新增星號 | 星號/天 | 總星號 |
|---|---|---:|---:|---:|
| 1 | [shadcn-ui/ui](https://github.com/shadcn-ui/ui)<br>好看的元件，程式碼歸你，隨便改<br>`Web / 前端` | +646 | 92.3 | 129,068 |
| 2 | [sveltejs/svelte](https://github.com/sveltejs/svelte)<br>你寫元件，編譯器變出高效的網頁程式碼<br>`Web / 前端` | +548 | 78.3 | 89,906 |
| 3 | [facebook/react](https://github.com/facebook/react)<br>網頁和 App 介面，都能用它來搭<br>`Web / 前端` | +338 | 48.3 | 252,939 |
| 4 | [tailwindlabs/tailwindcss](https://github.com/tailwindlabs/tailwindcss)<br>不寫一大堆 CSS，也能做定製介面<br>`Web / 前端` | +204 | 29.1 | 98,826 |
| 5 | [vercel/next.js](https://github.com/vercel/next.js)<br>用 React 做完整網站，從前到後<br>`Web / 前端` | +190 | 27.1 | 143,719 |
| 6 | [withastro/astro](https://github.com/withastro/astro)<br>做內容型網站，頁面輸出更輕量<br>`Web / 前端` | +188 | 26.9 | 64,202 |
| 7 | [vuejs/core](https://github.com/vuejs/core)<br>從一個小頁面開始，用多少學多少<br>`Web / 前端` | +120 | 17.1 | 55,115 |
| 8 | [tanstack/query](https://github.com/tanstack/query)<br>請求資料和快取，交給它管<br>`Web / 前端` | +74 | 10.6 | 50,638 |

<details>
<summary>本榜星號歷史曲線</summary>

<a href="https://www.star-history.com/#shadcn-ui/ui&Date"><img src="https://api.star-history.com/svg?repos=shadcn-ui/ui&type=Date" width="260" alt="shadcn-ui/ui 的星號歷史曲線"></a>

<a href="https://www.star-history.com/#sveltejs/svelte&Date"><img src="https://api.star-history.com/svg?repos=sveltejs/svelte&type=Date" width="260" alt="sveltejs/svelte 的星號歷史曲線"></a>

<a href="https://www.star-history.com/#facebook/react&Date"><img src="https://api.star-history.com/svg?repos=facebook/react&type=Date" width="260" alt="facebook/react 的星號歷史曲線"></a>

<a href="https://www.star-history.com/#tailwindlabs/tailwindcss&Date"><img src="https://api.star-history.com/svg?repos=tailwindlabs/tailwindcss&type=Date" width="260" alt="tailwindlabs/tailwindcss 的星號歷史曲線"></a>

<a href="https://www.star-history.com/#vercel/next.js&Date"><img src="https://api.star-history.com/svg?repos=vercel/next.js&type=Date" width="260" alt="vercel/next.js 的星號歷史曲線"></a>

<a href="https://www.star-history.com/#withastro/astro&Date"><img src="https://api.star-history.com/svg?repos=withastro/astro&type=Date" width="260" alt="withastro/astro 的星號歷史曲線"></a>

<a href="https://www.star-history.com/#vuejs/core&Date"><img src="https://api.star-history.com/svg?repos=vuejs/core&type=Date" width="260" alt="vuejs/core 的星號歷史曲線"></a>

<a href="https://www.star-history.com/#tanstack/query&Date"><img src="https://api.star-history.com/svg?repos=tanstack/query&type=Date" width="260" alt="tanstack/query 的星號歷史曲線"></a>

</details>

### 本月成長最快（近 30 天）

| # | 專案 | 新增星號 | 星號/天 | 總星號 |
|---|---|---:|---:|---:|
| 1 | [shadcn-ui/ui](https://github.com/shadcn-ui/ui)<br>好看的元件，程式碼歸你，隨便改<br>`Web / 前端` | +2,741 | 91.4 | 129,068 |
| 2 | [facebook/react](https://github.com/facebook/react)<br>網頁和 App 介面，都能用它來搭<br>`Web / 前端` | +1,662 | 55.4 | 252,939 |
| 3 | [sveltejs/svelte](https://github.com/sveltejs/svelte)<br>你寫元件，編譯器變出高效的網頁程式碼<br>`Web / 前端` | +1,566 | 52.2 | 89,906 |
| 4 | [tailwindlabs/tailwindcss](https://github.com/tailwindlabs/tailwindcss)<br>不寫一大堆 CSS，也能做定製介面<br>`Web / 前端` | +1,006 | 33.5 | 98,826 |
| 5 | [withastro/astro](https://github.com/withastro/astro)<br>做內容型網站，頁面輸出更輕量<br>`Web / 前端` | +816 | 27.2 | 64,202 |
| 6 | [vercel/next.js](https://github.com/vercel/next.js)<br>用 React 做完整網站，從前到後<br>`Web / 前端` | +774 | 25.8 | 143,719 |
| 7 | [vuejs/core](https://github.com/vuejs/core)<br>從一個小頁面開始，用多少學多少<br>`Web / 前端` | +452 | 15.1 | 55,115 |
| 8 | [tanstack/query](https://github.com/tanstack/query)<br>請求資料和快取，交給它管<br>`Web / 前端` | +208 | 6.9 | 50,638 |

<details>
<summary>本榜星號歷史曲線</summary>

<a href="https://www.star-history.com/#shadcn-ui/ui&Date"><img src="https://api.star-history.com/svg?repos=shadcn-ui/ui&type=Date" width="260" alt="shadcn-ui/ui 的星號歷史曲線"></a>

<a href="https://www.star-history.com/#facebook/react&Date"><img src="https://api.star-history.com/svg?repos=facebook/react&type=Date" width="260" alt="facebook/react 的星號歷史曲線"></a>

<a href="https://www.star-history.com/#sveltejs/svelte&Date"><img src="https://api.star-history.com/svg?repos=sveltejs/svelte&type=Date" width="260" alt="sveltejs/svelte 的星號歷史曲線"></a>

<a href="https://www.star-history.com/#tailwindlabs/tailwindcss&Date"><img src="https://api.star-history.com/svg?repos=tailwindlabs/tailwindcss&type=Date" width="260" alt="tailwindlabs/tailwindcss 的星號歷史曲線"></a>

<a href="https://www.star-history.com/#withastro/astro&Date"><img src="https://api.star-history.com/svg?repos=withastro/astro&type=Date" width="260" alt="withastro/astro 的星號歷史曲線"></a>

<a href="https://www.star-history.com/#vercel/next.js&Date"><img src="https://api.star-history.com/svg?repos=vercel/next.js&type=Date" width="260" alt="vercel/next.js 的星號歷史曲線"></a>

<a href="https://www.star-history.com/#vuejs/core&Date"><img src="https://api.star-history.com/svg?repos=vuejs/core&type=Date" width="260" alt="vuejs/core 的星號歷史曲線"></a>

<a href="https://www.star-history.com/#tanstack/query&Date"><img src="https://api.star-history.com/svg?repos=tanstack/query&type=Date" width="260" alt="tanstack/query 的星號歷史曲線"></a>

</details>

### 今年成長最快（近 365 天）

| # | 專案 | 新增星號 | 星號/天 | 總星號 |
|---|---|---:|---:|---:|
| 1 | [shadcn-ui/ui](https://github.com/shadcn-ui/ui)<br>好看的元件，程式碼歸你，隨便改<br>`Web / 前端` | +30,428 | 83.4 | 129,068 |
| 2 | [facebook/react](https://github.com/facebook/react)<br>網頁和 App 介面，都能用它來搭<br>`Web / 前端` | +15,724 | 43.1 | 252,939 |
| 3 | [withastro/astro](https://github.com/withastro/astro)<br>做內容型網站，頁面輸出更輕量<br>`Web / 前端` | +10,637 | 29.1 | 64,202 |
| 4 | [vercel/next.js](https://github.com/vercel/next.js)<br>用 React 做完整網站，從前到後<br>`Web / 前端` | +10,394 | 28.5 | 143,719 |
| 5 | [tailwindlabs/tailwindcss](https://github.com/tailwindlabs/tailwindcss)<br>不寫一大堆 CSS，也能做定製介面<br>`Web / 前端` | +8,955 | 24.5 | 98,826 |
| 6 | [sveltejs/svelte](https://github.com/sveltejs/svelte)<br>你寫元件，編譯器變出高效的網頁程式碼<br>`Web / 前端` | +6,197 | 17.0 | 89,906 |
| 7 | [vuejs/core](https://github.com/vuejs/core)<br>從一個小頁面開始，用多少學多少<br>`Web / 前端` | +3,721 | 10.2 | 55,115 |
| 8 | [tanstack/query](https://github.com/tanstack/query)<br>請求資料和快取，交給它管<br>`Web / 前端` | +3,705 | 10.2 | 50,638 |

<details>
<summary>本榜星號歷史曲線</summary>

<a href="https://www.star-history.com/#shadcn-ui/ui&Date"><img src="https://api.star-history.com/svg?repos=shadcn-ui/ui&type=Date" width="260" alt="shadcn-ui/ui 的星號歷史曲線"></a>

<a href="https://www.star-history.com/#facebook/react&Date"><img src="https://api.star-history.com/svg?repos=facebook/react&type=Date" width="260" alt="facebook/react 的星號歷史曲線"></a>

<a href="https://www.star-history.com/#withastro/astro&Date"><img src="https://api.star-history.com/svg?repos=withastro/astro&type=Date" width="260" alt="withastro/astro 的星號歷史曲線"></a>

<a href="https://www.star-history.com/#vercel/next.js&Date"><img src="https://api.star-history.com/svg?repos=vercel/next.js&type=Date" width="260" alt="vercel/next.js 的星號歷史曲線"></a>

<a href="https://www.star-history.com/#tailwindlabs/tailwindcss&Date"><img src="https://api.star-history.com/svg?repos=tailwindlabs/tailwindcss&type=Date" width="260" alt="tailwindlabs/tailwindcss 的星號歷史曲線"></a>

<a href="https://www.star-history.com/#sveltejs/svelte&Date"><img src="https://api.star-history.com/svg?repos=sveltejs/svelte&type=Date" width="260" alt="sveltejs/svelte 的星號歷史曲線"></a>

<a href="https://www.star-history.com/#vuejs/core&Date"><img src="https://api.star-history.com/svg?repos=vuejs/core&type=Date" width="260" alt="vuejs/core 的星號歷史曲線"></a>

<a href="https://www.star-history.com/#tanstack/query&Date"><img src="https://api.star-history.com/svg?repos=tanstack/query&type=Date" width="260" alt="tanstack/query 的星號歷史曲線"></a>

</details>

### 總星號數（歷史累計）

| # | 專案 | 總星號 |
|---|---|---:|
| 1 | [facebook/react](https://github.com/facebook/react)<br>網頁和 App 介面，都能用它來搭<br>`Web / 前端` | 252,939 |
| 2 | [vercel/next.js](https://github.com/vercel/next.js)<br>用 React 做完整網站，從前到後<br>`Web / 前端` | 143,719 |
| 3 | [shadcn-ui/ui](https://github.com/shadcn-ui/ui)<br>好看的元件，程式碼歸你，隨便改<br>`Web / 前端` | 129,068 |
| 4 | [tailwindlabs/tailwindcss](https://github.com/tailwindlabs/tailwindcss)<br>不寫一大堆 CSS，也能做定製介面<br>`Web / 前端` | 98,826 |
| 5 | [sveltejs/svelte](https://github.com/sveltejs/svelte)<br>你寫元件，編譯器變出高效的網頁程式碼<br>`Web / 前端` | 89,906 |
| 6 | [withastro/astro](https://github.com/withastro/astro)<br>做內容型網站，頁面輸出更輕量<br>`Web / 前端` | 64,202 |
| 7 | [vuejs/core](https://github.com/vuejs/core)<br>從一個小頁面開始，用多少學多少<br>`Web / 前端` | 55,115 |
| 8 | [tanstack/query](https://github.com/tanstack/query)<br>請求資料和快取，交給它管<br>`Web / 前端` | 50,638 |

<details>
<summary>本榜星號歷史曲線</summary>

<a href="https://www.star-history.com/#facebook/react&Date"><img src="https://api.star-history.com/svg?repos=facebook/react&type=Date" width="260" alt="facebook/react 的星號歷史曲線"></a>

<a href="https://www.star-history.com/#vercel/next.js&Date"><img src="https://api.star-history.com/svg?repos=vercel/next.js&type=Date" width="260" alt="vercel/next.js 的星號歷史曲線"></a>

<a href="https://www.star-history.com/#shadcn-ui/ui&Date"><img src="https://api.star-history.com/svg?repos=shadcn-ui/ui&type=Date" width="260" alt="shadcn-ui/ui 的星號歷史曲線"></a>

<a href="https://www.star-history.com/#tailwindlabs/tailwindcss&Date"><img src="https://api.star-history.com/svg?repos=tailwindlabs/tailwindcss&type=Date" width="260" alt="tailwindlabs/tailwindcss 的星號歷史曲線"></a>

<a href="https://www.star-history.com/#sveltejs/svelte&Date"><img src="https://api.star-history.com/svg?repos=sveltejs/svelte&type=Date" width="260" alt="sveltejs/svelte 的星號歷史曲線"></a>

<a href="https://www.star-history.com/#withastro/astro&Date"><img src="https://api.star-history.com/svg?repos=withastro/astro&type=Date" width="260" alt="withastro/astro 的星號歷史曲線"></a>

<a href="https://www.star-history.com/#vuejs/core&Date"><img src="https://api.star-history.com/svg?repos=vuejs/core&type=Date" width="260" alt="vuejs/core 的星號歷史曲線"></a>

<a href="https://www.star-history.com/#tanstack/query&Date"><img src="https://api.star-history.com/svg?repos=tanstack/query&type=Date" width="260" alt="tanstack/query 的星號歷史曲線"></a>

</details>

## 基礎建設

> 容器、Kubernetes、雲端、網路與可觀測性

### 最熱新儲存庫（近 7 天內建立）

本次執行中沒有符合條件的新儲存庫。

### 本週成長最快（近 7 天）

| # | 專案 | 新增星號 | 星號/天 | 總星號 |
|---|---|---:|---:|---:|
| 1 | [caddyserver/caddy](https://github.com/caddyserver/caddy)<br>搭網站伺服器，HTTPS 自動配好<br>`基礎建設` | +393 | 56.1 | 79,534 |
| 2 | [kubernetes/kubernetes](https://github.com/kubernetes/kubernetes)<br>容器多了，部署擴容交給它<br>`基礎建設` | +258 | 36.9 | 129,337 |
| 3 | [docker/compose](https://github.com/docker/compose)<br>多個容器寫進一個檔案，一起跑<br>`基礎建設` | +208 | 29.7 | 39,088 |
| 4 | [grafana/grafana](https://github.com/grafana/grafana)<br>指標日誌追蹤，放進一個面板<br>`基礎建設` | +198 | 28.3 | 78,176 |
| 5 | [prometheus/prometheus](https://github.com/prometheus/prometheus)<br>系統出問題，告警先找到你<br>`基礎建設` | +198 | 28.3 | 67,880 |
| 6 | [traefik/traefik](https://github.com/traefik/traefik)<br>服務多了，流量自動分好<br>`基礎建設` | +121 | 17.3 | 65,699 |
| 7 | [hashicorp/terraform](https://github.com/hashicorp/terraform)<br>雲資源寫成程式碼，可審閱、可版本管理<br>`基礎建設` | +69 | 9.9 | 50,323 |
| 8 | [pulumi/pulumi](https://github.com/pulumi/pulumi)<br>用熟悉的程式語言管雲資源<br>`基礎建設` | +35 | 5.0 | 25,939 |

<details>
<summary>本榜星號歷史曲線</summary>

<a href="https://www.star-history.com/#caddyserver/caddy&Date"><img src="https://api.star-history.com/svg?repos=caddyserver/caddy&type=Date" width="260" alt="caddyserver/caddy 的星號歷史曲線"></a>

<a href="https://www.star-history.com/#kubernetes/kubernetes&Date"><img src="https://api.star-history.com/svg?repos=kubernetes/kubernetes&type=Date" width="260" alt="kubernetes/kubernetes 的星號歷史曲線"></a>

<a href="https://www.star-history.com/#docker/compose&Date"><img src="https://api.star-history.com/svg?repos=docker/compose&type=Date" width="260" alt="docker/compose 的星號歷史曲線"></a>

<a href="https://www.star-history.com/#grafana/grafana&Date"><img src="https://api.star-history.com/svg?repos=grafana/grafana&type=Date" width="260" alt="grafana/grafana 的星號歷史曲線"></a>

<a href="https://www.star-history.com/#prometheus/prometheus&Date"><img src="https://api.star-history.com/svg?repos=prometheus/prometheus&type=Date" width="260" alt="prometheus/prometheus 的星號歷史曲線"></a>

<a href="https://www.star-history.com/#traefik/traefik&Date"><img src="https://api.star-history.com/svg?repos=traefik/traefik&type=Date" width="260" alt="traefik/traefik 的星號歷史曲線"></a>

<a href="https://www.star-history.com/#hashicorp/terraform&Date"><img src="https://api.star-history.com/svg?repos=hashicorp/terraform&type=Date" width="260" alt="hashicorp/terraform 的星號歷史曲線"></a>

<a href="https://www.star-history.com/#pulumi/pulumi&Date"><img src="https://api.star-history.com/svg?repos=pulumi/pulumi&type=Date" width="260" alt="pulumi/pulumi 的星號歷史曲線"></a>

</details>

### 本月成長最快（近 30 天）

| # | 專案 | 新增星號 | 星號/天 | 總星號 |
|---|---|---:|---:|---:|
| 1 | [caddyserver/caddy](https://github.com/caddyserver/caddy)<br>搭網站伺服器，HTTPS 自動配好<br>`基礎建設` | +1,246 | 41.5 | 79,534 |
| 2 | [prometheus/prometheus](https://github.com/prometheus/prometheus)<br>系統出問題，告警先找到你<br>`基礎建設` | +1,189 | 39.6 | 67,880 |
| 3 | [kubernetes/kubernetes](https://github.com/kubernetes/kubernetes)<br>容器多了，部署擴容交給它<br>`基礎建設` | +1,050 | 35.0 | 129,337 |
| 4 | [grafana/grafana](https://github.com/grafana/grafana)<br>指標日誌追蹤，放進一個面板<br>`基礎建設` | +790 | 26.3 | 78,176 |
| 5 | [docker/compose](https://github.com/docker/compose)<br>多個容器寫進一個檔案，一起跑<br>`基礎建設` | +654 | 21.8 | 39,088 |
| 6 | [traefik/traefik](https://github.com/traefik/traefik)<br>服務多了，流量自動分好<br>`基礎建設` | +409 | 13.6 | 65,699 |
| 7 | [hashicorp/terraform](https://github.com/hashicorp/terraform)<br>雲資源寫成程式碼，可審閱、可版本管理<br>`基礎建設` | +351 | 11.7 | 50,323 |
| 8 | [pulumi/pulumi](https://github.com/pulumi/pulumi)<br>用熟悉的程式語言管雲資源<br>`基礎建設` | +161 | 5.4 | 25,939 |

<details>
<summary>本榜星號歷史曲線</summary>

<a href="https://www.star-history.com/#caddyserver/caddy&Date"><img src="https://api.star-history.com/svg?repos=caddyserver/caddy&type=Date" width="260" alt="caddyserver/caddy 的星號歷史曲線"></a>

<a href="https://www.star-history.com/#prometheus/prometheus&Date"><img src="https://api.star-history.com/svg?repos=prometheus/prometheus&type=Date" width="260" alt="prometheus/prometheus 的星號歷史曲線"></a>

<a href="https://www.star-history.com/#kubernetes/kubernetes&Date"><img src="https://api.star-history.com/svg?repos=kubernetes/kubernetes&type=Date" width="260" alt="kubernetes/kubernetes 的星號歷史曲線"></a>

<a href="https://www.star-history.com/#grafana/grafana&Date"><img src="https://api.star-history.com/svg?repos=grafana/grafana&type=Date" width="260" alt="grafana/grafana 的星號歷史曲線"></a>

<a href="https://www.star-history.com/#docker/compose&Date"><img src="https://api.star-history.com/svg?repos=docker/compose&type=Date" width="260" alt="docker/compose 的星號歷史曲線"></a>

<a href="https://www.star-history.com/#traefik/traefik&Date"><img src="https://api.star-history.com/svg?repos=traefik/traefik&type=Date" width="260" alt="traefik/traefik 的星號歷史曲線"></a>

<a href="https://www.star-history.com/#hashicorp/terraform&Date"><img src="https://api.star-history.com/svg?repos=hashicorp/terraform&type=Date" width="260" alt="hashicorp/terraform 的星號歷史曲線"></a>

<a href="https://www.star-history.com/#pulumi/pulumi&Date"><img src="https://api.star-history.com/svg?repos=pulumi/pulumi&type=Date" width="260" alt="pulumi/pulumi 的星號歷史曲線"></a>

</details>

### 今年成長最快（近 365 天）

| # | 專案 | 新增星號 | 星號/天 | 總星號 |
|---|---|---:|---:|---:|
| 1 | [caddyserver/caddy](https://github.com/caddyserver/caddy)<br>搭網站伺服器，HTTPS 自動配好<br>`基礎建設` | +12,342 | 33.8 | 79,534 |
| 2 | [kubernetes/kubernetes](https://github.com/kubernetes/kubernetes)<br>容器多了，部署擴容交給它<br>`基礎建設` | +11,849 | 32.5 | 129,337 |
| 3 | [grafana/grafana](https://github.com/grafana/grafana)<br>指標日誌追蹤，放進一個面板<br>`基礎建設` | +8,042 | 22.0 | 78,176 |
| 4 | [traefik/traefik](https://github.com/traefik/traefik)<br>服務多了，流量自動分好<br>`基礎建設` | +7,233 | 19.8 | 65,699 |
| 5 | [prometheus/prometheus](https://github.com/prometheus/prometheus)<br>系統出問題，告警先找到你<br>`基礎建設` | +7,119 | 19.5 | 67,880 |
| 6 | [hashicorp/terraform](https://github.com/hashicorp/terraform)<br>雲資源寫成程式碼，可審閱、可版本管理<br>`基礎建設` | +3,840 | 10.5 | 50,323 |
| 7 | [docker/compose](https://github.com/docker/compose)<br>多個容器寫進一個檔案，一起跑<br>`基礎建設` | +2,989 | 8.2 | 39,088 |
| 8 | [pulumi/pulumi](https://github.com/pulumi/pulumi)<br>用熟悉的程式語言管雲資源<br>`基礎建設` | +2,085 | 5.7 | 25,939 |

<details>
<summary>本榜星號歷史曲線</summary>

<a href="https://www.star-history.com/#caddyserver/caddy&Date"><img src="https://api.star-history.com/svg?repos=caddyserver/caddy&type=Date" width="260" alt="caddyserver/caddy 的星號歷史曲線"></a>

<a href="https://www.star-history.com/#kubernetes/kubernetes&Date"><img src="https://api.star-history.com/svg?repos=kubernetes/kubernetes&type=Date" width="260" alt="kubernetes/kubernetes 的星號歷史曲線"></a>

<a href="https://www.star-history.com/#grafana/grafana&Date"><img src="https://api.star-history.com/svg?repos=grafana/grafana&type=Date" width="260" alt="grafana/grafana 的星號歷史曲線"></a>

<a href="https://www.star-history.com/#traefik/traefik&Date"><img src="https://api.star-history.com/svg?repos=traefik/traefik&type=Date" width="260" alt="traefik/traefik 的星號歷史曲線"></a>

<a href="https://www.star-history.com/#prometheus/prometheus&Date"><img src="https://api.star-history.com/svg?repos=prometheus/prometheus&type=Date" width="260" alt="prometheus/prometheus 的星號歷史曲線"></a>

<a href="https://www.star-history.com/#hashicorp/terraform&Date"><img src="https://api.star-history.com/svg?repos=hashicorp/terraform&type=Date" width="260" alt="hashicorp/terraform 的星號歷史曲線"></a>

<a href="https://www.star-history.com/#docker/compose&Date"><img src="https://api.star-history.com/svg?repos=docker/compose&type=Date" width="260" alt="docker/compose 的星號歷史曲線"></a>

<a href="https://www.star-history.com/#pulumi/pulumi&Date"><img src="https://api.star-history.com/svg?repos=pulumi/pulumi&type=Date" width="260" alt="pulumi/pulumi 的星號歷史曲線"></a>

</details>

### 總星號數（歷史累計）

| # | 專案 | 總星號 |
|---|---|---:|
| 1 | [kubernetes/kubernetes](https://github.com/kubernetes/kubernetes)<br>容器多了，部署擴容交給它<br>`基礎建設` | 129,337 |
| 2 | [caddyserver/caddy](https://github.com/caddyserver/caddy)<br>搭網站伺服器，HTTPS 自動配好<br>`基礎建設` | 79,534 |
| 3 | [grafana/grafana](https://github.com/grafana/grafana)<br>指標日誌追蹤，放進一個面板<br>`基礎建設` | 78,176 |
| 4 | [prometheus/prometheus](https://github.com/prometheus/prometheus)<br>系統出問題，告警先找到你<br>`基礎建設` | 67,880 |
| 5 | [traefik/traefik](https://github.com/traefik/traefik)<br>服務多了，流量自動分好<br>`基礎建設` | 65,699 |
| 6 | [hashicorp/terraform](https://github.com/hashicorp/terraform)<br>雲資源寫成程式碼，可審閱、可版本管理<br>`基礎建設` | 50,323 |
| 7 | [docker/compose](https://github.com/docker/compose)<br>多個容器寫進一個檔案，一起跑<br>`基礎建設` | 39,088 |
| 8 | [pulumi/pulumi](https://github.com/pulumi/pulumi)<br>用熟悉的程式語言管雲資源<br>`基礎建設` | 25,939 |

<details>
<summary>本榜星號歷史曲線</summary>

<a href="https://www.star-history.com/#kubernetes/kubernetes&Date"><img src="https://api.star-history.com/svg?repos=kubernetes/kubernetes&type=Date" width="260" alt="kubernetes/kubernetes 的星號歷史曲線"></a>

<a href="https://www.star-history.com/#caddyserver/caddy&Date"><img src="https://api.star-history.com/svg?repos=caddyserver/caddy&type=Date" width="260" alt="caddyserver/caddy 的星號歷史曲線"></a>

<a href="https://www.star-history.com/#grafana/grafana&Date"><img src="https://api.star-history.com/svg?repos=grafana/grafana&type=Date" width="260" alt="grafana/grafana 的星號歷史曲線"></a>

<a href="https://www.star-history.com/#prometheus/prometheus&Date"><img src="https://api.star-history.com/svg?repos=prometheus/prometheus&type=Date" width="260" alt="prometheus/prometheus 的星號歷史曲線"></a>

<a href="https://www.star-history.com/#traefik/traefik&Date"><img src="https://api.star-history.com/svg?repos=traefik/traefik&type=Date" width="260" alt="traefik/traefik 的星號歷史曲線"></a>

<a href="https://www.star-history.com/#hashicorp/terraform&Date"><img src="https://api.star-history.com/svg?repos=hashicorp/terraform&type=Date" width="260" alt="hashicorp/terraform 的星號歷史曲線"></a>

<a href="https://www.star-history.com/#docker/compose&Date"><img src="https://api.star-history.com/svg?repos=docker/compose&type=Date" width="260" alt="docker/compose 的星號歷史曲線"></a>

<a href="https://www.star-history.com/#pulumi/pulumi&Date"><img src="https://api.star-history.com/svg?repos=pulumi/pulumi&type=Date" width="260" alt="pulumi/pulumi 的星號歷史曲線"></a>

</details>

## 設計 / 創意

> 設計系統、繪圖、動畫與創意工具

### 最熱新儲存庫（近 7 天內建立）

| # | 專案 | 建立時間（UTC） | 總星號 | 星號/天 |
|---|---|---|---:|---:|
| 1 | [kennethkumar05/figma-figjam](https://github.com/kennethkumar05/figma-figjam)<br>適用於 Windows 10/11 的 Figma Figjam。建立包含便簽、形狀、連接線和即時游標的協作白板，讓團隊繪製流程圖、進行腦力激… | 2026-11-24<br><sub>1.3 天</sub> | 122 | 96.8 |
| 2 | [praseesh369/youtube-ai-video-editing-system](https://github.com/praseesh369/youtube-ai-video-editing-system)<br>YouTube的AI影片剪輯工作流程 | 2026-11-21<br><sub>4.0 天</sub> | 338 | 84.2 |

<details>
<summary>本榜星號歷史曲線</summary>

<a href="https://www.star-history.com/#kennethkumar05/figma-figjam&Date"><img src="https://api.star-history.com/svg?repos=kennethkumar05/figma-figjam&type=Date" width="260" alt="kennethkumar05/figma-figjam 的星號歷史曲線"></a>

<a href="https://www.star-history.com/#praseesh369/youtube-ai-video-editing-system&Date"><img src="https://api.star-history.com/svg?repos=praseesh369/youtube-ai-video-editing-system&type=Date" width="260" alt="praseesh369/youtube-ai-video-editing-system 的星號歷史曲線"></a>

</details>

### 本週成長最快（近 7 天）

| # | 專案 | 新增星號 | 星號/天 | 總星號 |
|---|---|---:|---:|---:|
| 1 | [excalidraw/excalidraw](https://github.com/excalidraw/excalidraw)<br>開啟就畫，像在紙上隨手畫圖<br>`設計 / 創意` | +429 | 61.3 | 136,294 |
| 2 | [penpot/penpot](https://github.com/penpot/penpot)<br>團隊一起做設計，用開源平台<br>`設計 / 創意` | +260 | 37.1 | 62,735 |
| 3 | [lucide-icons/lucide](https://github.com/lucide-icons/lucide)<br>一套圖示風格統一，拿來就用<br>`設計 / 創意` | +171 | 24.4 | 25,999 |
| 4 | [saadeghi/daisyui](https://github.com/saadeghi/daisyui)<br>Tailwind 也有現成元件可挑<br>`設計 / 創意` | +123 | 17.6 | 42,997 |
| 5 | [jgraph/drawio](https://github.com/jgraph/drawio)<br>畫圖和白板，一個編輯器搞定<br>`設計 / 創意` | +122 | 17.4 | 9,575 |
| 6 | [airbnb/lottie-web](https://github.com/airbnb/lottie-web)<br>AE 做的動畫，直接放進網頁<br>`設計 / 創意` | +89 | 12.7 | 32,584 |
| 7 | [phosphor-icons/homepage](https://github.com/phosphor-icons/homepage)<br>一整套靈活的圖示，人人可用<br>`設計 / 創意` | +33 | 4.7 | 7,855 |
| 8 | [lottiefiles/lottie-ios](https://github.com/lottiefiles/lottie-ios)<br>AE 做的動畫，直接放進 iOS<br>`設計 / 創意` | +0 | 0.0 | 43 |

<details>
<summary>本榜星號歷史曲線</summary>

<a href="https://www.star-history.com/#excalidraw/excalidraw&Date"><img src="https://api.star-history.com/svg?repos=excalidraw/excalidraw&type=Date" width="260" alt="excalidraw/excalidraw 的星號歷史曲線"></a>

<a href="https://www.star-history.com/#penpot/penpot&Date"><img src="https://api.star-history.com/svg?repos=penpot/penpot&type=Date" width="260" alt="penpot/penpot 的星號歷史曲線"></a>

<a href="https://www.star-history.com/#lucide-icons/lucide&Date"><img src="https://api.star-history.com/svg?repos=lucide-icons/lucide&type=Date" width="260" alt="lucide-icons/lucide 的星號歷史曲線"></a>

<a href="https://www.star-history.com/#saadeghi/daisyui&Date"><img src="https://api.star-history.com/svg?repos=saadeghi/daisyui&type=Date" width="260" alt="saadeghi/daisyui 的星號歷史曲線"></a>

<a href="https://www.star-history.com/#jgraph/drawio&Date"><img src="https://api.star-history.com/svg?repos=jgraph/drawio&type=Date" width="260" alt="jgraph/drawio 的星號歷史曲線"></a>

<a href="https://www.star-history.com/#airbnb/lottie-web&Date"><img src="https://api.star-history.com/svg?repos=airbnb/lottie-web&type=Date" width="260" alt="airbnb/lottie-web 的星號歷史曲線"></a>

<a href="https://www.star-history.com/#phosphor-icons/homepage&Date"><img src="https://api.star-history.com/svg?repos=phosphor-icons/homepage&type=Date" width="260" alt="phosphor-icons/homepage 的星號歷史曲線"></a>

<a href="https://www.star-history.com/#lottiefiles/lottie-ios&Date"><img src="https://api.star-history.com/svg?repos=lottiefiles/lottie-ios&type=Date" width="260" alt="lottiefiles/lottie-ios 的星號歷史曲線"></a>

</details>

### 本月成長最快（近 30 天）

| # | 專案 | 新增星號 | 星號/天 | 總星號 |
|---|---|---:|---:|---:|
| 1 | [excalidraw/excalidraw](https://github.com/excalidraw/excalidraw)<br>開啟就畫，像在紙上隨手畫圖<br>`設計 / 創意` | +1,941 | 64.7 | 136,294 |
| 2 | [penpot/penpot](https://github.com/penpot/penpot)<br>團隊一起做設計，用開源平台<br>`設計 / 創意` | +1,189 | 39.6 | 62,735 |
| 3 | [lucide-icons/lucide](https://github.com/lucide-icons/lucide)<br>一套圖示風格統一，拿來就用<br>`設計 / 創意` | +746 | 24.9 | 25,999 |
| 4 | [jgraph/drawio](https://github.com/jgraph/drawio)<br>畫圖和白板，一個編輯器搞定<br>`設計 / 創意` | +597 | 19.9 | 9,575 |
| 5 | [saadeghi/daisyui](https://github.com/saadeghi/daisyui)<br>Tailwind 也有現成元件可挑<br>`設計 / 創意` | +408 | 13.6 | 42,997 |
| 6 | [airbnb/lottie-web](https://github.com/airbnb/lottie-web)<br>AE 做的動畫，直接放進網頁<br>`設計 / 創意` | +342 | 11.4 | 32,584 |
| 7 | [phosphor-icons/homepage](https://github.com/phosphor-icons/homepage)<br>一整套靈活的圖示，人人可用<br>`設計 / 創意` | +150 | 5.0 | 7,855 |
| 8 | [lottiefiles/lottie-ios](https://github.com/lottiefiles/lottie-ios)<br>AE 做的動畫，直接放進 iOS<br>`設計 / 創意` | +0 | 0.0 | 43 |

<details>
<summary>本榜星號歷史曲線</summary>

<a href="https://www.star-history.com/#excalidraw/excalidraw&Date"><img src="https://api.star-history.com/svg?repos=excalidraw/excalidraw&type=Date" width="260" alt="excalidraw/excalidraw 的星號歷史曲線"></a>

<a href="https://www.star-history.com/#penpot/penpot&Date"><img src="https://api.star-history.com/svg?repos=penpot/penpot&type=Date" width="260" alt="penpot/penpot 的星號歷史曲線"></a>

<a href="https://www.star-history.com/#lucide-icons/lucide&Date"><img src="https://api.star-history.com/svg?repos=lucide-icons/lucide&type=Date" width="260" alt="lucide-icons/lucide 的星號歷史曲線"></a>

<a href="https://www.star-history.com/#jgraph/drawio&Date"><img src="https://api.star-history.com/svg?repos=jgraph/drawio&type=Date" width="260" alt="jgraph/drawio 的星號歷史曲線"></a>

<a href="https://www.star-history.com/#saadeghi/daisyui&Date"><img src="https://api.star-history.com/svg?repos=saadeghi/daisyui&type=Date" width="260" alt="saadeghi/daisyui 的星號歷史曲線"></a>

<a href="https://www.star-history.com/#airbnb/lottie-web&Date"><img src="https://api.star-history.com/svg?repos=airbnb/lottie-web&type=Date" width="260" alt="airbnb/lottie-web 的星號歷史曲線"></a>

<a href="https://www.star-history.com/#phosphor-icons/homepage&Date"><img src="https://api.star-history.com/svg?repos=phosphor-icons/homepage&type=Date" width="260" alt="phosphor-icons/homepage 的星號歷史曲線"></a>

<a href="https://www.star-history.com/#lottiefiles/lottie-ios&Date"><img src="https://api.star-history.com/svg?repos=lottiefiles/lottie-ios&type=Date" width="260" alt="lottiefiles/lottie-ios 的星號歷史曲線"></a>

</details>

### 今年成長最快（近 365 天）

| # | 專案 | 新增星號 | 星號/天 | 總星號 |
|---|---|---:|---:|---:|
| 1 | [excalidraw/excalidraw](https://github.com/excalidraw/excalidraw)<br>開啟就畫，像在紙上隨手畫圖<br>`設計 / 創意` | +26,722 | 73.2 | 136,294 |
| 2 | [penpot/penpot](https://github.com/penpot/penpot)<br>團隊一起做設計，用開源平台<br>`設計 / 創意` | +21,853 | 59.9 | 62,735 |
| 3 | [jgraph/drawio](https://github.com/jgraph/drawio)<br>畫圖和白板，一個編輯器搞定<br>`設計 / 創意` | +6,750 | 18.5 | 9,575 |
| 4 | [lucide-icons/lucide](https://github.com/lucide-icons/lucide)<br>一套圖示風格統一，拿來就用<br>`設計 / 創意` | +6,500 | 17.8 | 25,999 |
| 5 | [saadeghi/daisyui](https://github.com/saadeghi/daisyui)<br>Tailwind 也有現成元件可挑<br>`設計 / 創意` | +4,300 | 11.8 | 42,997 |
| 6 | [phosphor-icons/homepage](https://github.com/phosphor-icons/homepage)<br>一整套靈活的圖示，人人可用<br>`設計 / 創意` | +2,214 | 6.1 | 7,855 |
| 7 | [airbnb/lottie-web](https://github.com/airbnb/lottie-web)<br>AE 做的動畫，直接放進網頁<br>`設計 / 創意` | +1,309 | 3.6 | 32,584 |
| 8 | [lottiefiles/lottie-ios](https://github.com/lottiefiles/lottie-ios)<br>AE 做的動畫，直接放進 iOS<br>`設計 / 創意` | +1 | 0.0 | 43 |

<details>
<summary>本榜星號歷史曲線</summary>

<a href="https://www.star-history.com/#excalidraw/excalidraw&Date"><img src="https://api.star-history.com/svg?repos=excalidraw/excalidraw&type=Date" width="260" alt="excalidraw/excalidraw 的星號歷史曲線"></a>

<a href="https://www.star-history.com/#penpot/penpot&Date"><img src="https://api.star-history.com/svg?repos=penpot/penpot&type=Date" width="260" alt="penpot/penpot 的星號歷史曲線"></a>

<a href="https://www.star-history.com/#jgraph/drawio&Date"><img src="https://api.star-history.com/svg?repos=jgraph/drawio&type=Date" width="260" alt="jgraph/drawio 的星號歷史曲線"></a>

<a href="https://www.star-history.com/#lucide-icons/lucide&Date"><img src="https://api.star-history.com/svg?repos=lucide-icons/lucide&type=Date" width="260" alt="lucide-icons/lucide 的星號歷史曲線"></a>

<a href="https://www.star-history.com/#saadeghi/daisyui&Date"><img src="https://api.star-history.com/svg?repos=saadeghi/daisyui&type=Date" width="260" alt="saadeghi/daisyui 的星號歷史曲線"></a>

<a href="https://www.star-history.com/#phosphor-icons/homepage&Date"><img src="https://api.star-history.com/svg?repos=phosphor-icons/homepage&type=Date" width="260" alt="phosphor-icons/homepage 的星號歷史曲線"></a>

<a href="https://www.star-history.com/#airbnb/lottie-web&Date"><img src="https://api.star-history.com/svg?repos=airbnb/lottie-web&type=Date" width="260" alt="airbnb/lottie-web 的星號歷史曲線"></a>

<a href="https://www.star-history.com/#lottiefiles/lottie-ios&Date"><img src="https://api.star-history.com/svg?repos=lottiefiles/lottie-ios&type=Date" width="260" alt="lottiefiles/lottie-ios 的星號歷史曲線"></a>

</details>

### 總星號數（歷史累計）

| # | 專案 | 總星號 |
|---|---|---:|
| 1 | [excalidraw/excalidraw](https://github.com/excalidraw/excalidraw)<br>開啟就畫，像在紙上隨手畫圖<br>`設計 / 創意` | 136,294 |
| 2 | [penpot/penpot](https://github.com/penpot/penpot)<br>團隊一起做設計，用開源平台<br>`設計 / 創意` | 62,735 |
| 3 | [saadeghi/daisyui](https://github.com/saadeghi/daisyui)<br>Tailwind 也有現成元件可挑<br>`設計 / 創意` | 42,997 |
| 4 | [airbnb/lottie-web](https://github.com/airbnb/lottie-web)<br>AE 做的動畫，直接放進網頁<br>`設計 / 創意` | 32,584 |
| 5 | [lucide-icons/lucide](https://github.com/lucide-icons/lucide)<br>一套圖示風格統一，拿來就用<br>`設計 / 創意` | 25,999 |
| 6 | [jgraph/drawio](https://github.com/jgraph/drawio)<br>畫圖和白板，一個編輯器搞定<br>`設計 / 創意` | 9,575 |
| 7 | [phosphor-icons/homepage](https://github.com/phosphor-icons/homepage)<br>一整套靈活的圖示，人人可用<br>`設計 / 創意` | 7,855 |
| 8 | [lottiefiles/lottie-ios](https://github.com/lottiefiles/lottie-ios)<br>AE 做的動畫，直接放進 iOS<br>`設計 / 創意` | 43 |

<details>
<summary>本榜星號歷史曲線</summary>

<a href="https://www.star-history.com/#excalidraw/excalidraw&Date"><img src="https://api.star-history.com/svg?repos=excalidraw/excalidraw&type=Date" width="260" alt="excalidraw/excalidraw 的星號歷史曲線"></a>

<a href="https://www.star-history.com/#penpot/penpot&Date"><img src="https://api.star-history.com/svg?repos=penpot/penpot&type=Date" width="260" alt="penpot/penpot 的星號歷史曲線"></a>

<a href="https://www.star-history.com/#saadeghi/daisyui&Date"><img src="https://api.star-history.com/svg?repos=saadeghi/daisyui&type=Date" width="260" alt="saadeghi/daisyui 的星號歷史曲線"></a>

<a href="https://www.star-history.com/#airbnb/lottie-web&Date"><img src="https://api.star-history.com/svg?repos=airbnb/lottie-web&type=Date" width="260" alt="airbnb/lottie-web 的星號歷史曲線"></a>

<a href="https://www.star-history.com/#lucide-icons/lucide&Date"><img src="https://api.star-history.com/svg?repos=lucide-icons/lucide&type=Date" width="260" alt="lucide-icons/lucide 的星號歷史曲線"></a>

<a href="https://www.star-history.com/#jgraph/drawio&Date"><img src="https://api.star-history.com/svg?repos=jgraph/drawio&type=Date" width="260" alt="jgraph/drawio 的星號歷史曲線"></a>

<a href="https://www.star-history.com/#phosphor-icons/homepage&Date"><img src="https://api.star-history.com/svg?repos=phosphor-icons/homepage&type=Date" width="260" alt="phosphor-icons/homepage 的星號歷史曲線"></a>

<a href="https://www.star-history.com/#lottiefiles/lottie-ios&Date"><img src="https://api.star-history.com/svg?repos=lottiefiles/lottie-ios&type=Date" width="260" alt="lottiefiles/lottie-ios 的星號歷史曲線"></a>

</details>

## 資料

> 資料庫、分析、ETL 與資料工程

### 最熱新儲存庫（近 7 天內建立）

| # | 專案 | 建立時間（UTC） | 總星號 | 星號/天 |
|---|---|---|---:|---:|
| 1 | [Liangsystems/microsoft-teams-rooms](https://github.com/Liangsystems/microsoft-teams-rooms)<br>適用於 Windows 10/11 的 Microsoft Teams Rooms。加入排定的會議、共用內容並在會議硬體上執行會議室音訊與視訊，讓 IT 管理員管… | 2026-11-24<br><sub>1.2 天</sub> | 121 | 99.4 |

<details>
<summary>本榜星號歷史曲線</summary>

<a href="https://www.star-history.com/#Liangsystems/microsoft-teams-rooms&Date"><img src="https://api.star-history.com/svg?repos=Liangsystems/microsoft-teams-rooms&type=Date" width="260" alt="Liangsystems/microsoft-teams-rooms 的星號歷史曲線"></a>

</details>

### 本週成長最快（近 7 天）

| # | 專案 | 新增星號 | 星號/天 | 總星號 |
|---|---|---:|---:|---:|
| 1 | [duckdb/duckdb](https://github.com/duckdb/duckdb)<br>不搭資料庫服務，也能跑 SQL 分析<br>`資料` | +184 | 26.3 | 43,347 |
| 2 | [ClickHouse/ClickHouse](https://github.com/ClickHouse/ClickHouse)<br>大量資料即時分析，用開源的<br>`資料` | +153 | 21.9 | 51,134 |
| 3 | [apache/superset](https://github.com/apache/superset)<br>資料看不懂，做成圖就明白<br>`資料` | +141 | 20.1 | 75,678 |
| 4 | [pola-rs/polars](https://github.com/pola-rs/polars)<br>表格資料處理快，不用乾等<br>`資料` | +137 | 19.6 | 40,503 |
| 5 | [apache/kafka](https://github.com/apache/kafka)<br>系統之間的事件流，交給它來傳<br>`資料` | +102 | 14.6 | 34,351 |
| 6 | [apache/arrow](https://github.com/apache/arrow)<br>不同語言之間，資料直接通用<br>`資料` | +34 | 4.9 | 17,345 |
| 7 | [dbt-labs/dbt-core](https://github.com/dbt-labs/dbt-core)<br>資料轉換，照軟體工程的做法來<br>`資料` | +28 | 4.0 | 14,213 |
| 8 | [jupyter/notebook](https://github.com/jupyter/notebook)<br>在網頁裡寫程式碼，邊寫邊看結果<br>`資料` | +10 | 1.4 | 13,482 |

<details>
<summary>本榜星號歷史曲線</summary>

<a href="https://www.star-history.com/#duckdb/duckdb&Date"><img src="https://api.star-history.com/svg?repos=duckdb/duckdb&type=Date" width="260" alt="duckdb/duckdb 的星號歷史曲線"></a>

<a href="https://www.star-history.com/#ClickHouse/ClickHouse&Date"><img src="https://api.star-history.com/svg?repos=ClickHouse/ClickHouse&type=Date" width="260" alt="ClickHouse/ClickHouse 的星號歷史曲線"></a>

<a href="https://www.star-history.com/#apache/superset&Date"><img src="https://api.star-history.com/svg?repos=apache/superset&type=Date" width="260" alt="apache/superset 的星號歷史曲線"></a>

<a href="https://www.star-history.com/#pola-rs/polars&Date"><img src="https://api.star-history.com/svg?repos=pola-rs/polars&type=Date" width="260" alt="pola-rs/polars 的星號歷史曲線"></a>

<a href="https://www.star-history.com/#apache/kafka&Date"><img src="https://api.star-history.com/svg?repos=apache/kafka&type=Date" width="260" alt="apache/kafka 的星號歷史曲線"></a>

<a href="https://www.star-history.com/#apache/arrow&Date"><img src="https://api.star-history.com/svg?repos=apache/arrow&type=Date" width="260" alt="apache/arrow 的星號歷史曲線"></a>

<a href="https://www.star-history.com/#dbt-labs/dbt-core&Date"><img src="https://api.star-history.com/svg?repos=dbt-labs/dbt-core&type=Date" width="260" alt="dbt-labs/dbt-core 的星號歷史曲線"></a>

<a href="https://www.star-history.com/#jupyter/notebook&Date"><img src="https://api.star-history.com/svg?repos=jupyter/notebook&type=Date" width="260" alt="jupyter/notebook 的星號歷史曲線"></a>

</details>

### 本月成長最快（近 30 天）

| # | 專案 | 新增星號 | 星號/天 | 總星號 |
|---|---|---:|---:|---:|
| 1 | [duckdb/duckdb](https://github.com/duckdb/duckdb)<br>不搭資料庫服務，也能跑 SQL 分析<br>`資料` | +849 | 28.3 | 43,347 |
| 2 | [ClickHouse/ClickHouse](https://github.com/ClickHouse/ClickHouse)<br>大量資料即時分析，用開源的<br>`資料` | +592 | 19.7 | 51,134 |
| 3 | [apache/superset](https://github.com/apache/superset)<br>資料看不懂，做成圖就明白<br>`資料` | +463 | 15.4 | 75,678 |
| 4 | [pola-rs/polars](https://github.com/pola-rs/polars)<br>表格資料處理快，不用乾等<br>`資料` | +356 | 11.9 | 40,503 |
| 5 | [apache/kafka](https://github.com/apache/kafka)<br>系統之間的事件流，交給它來傳<br>`資料` | +316 | 10.5 | 34,351 |
| 6 | [dbt-labs/dbt-core](https://github.com/dbt-labs/dbt-core)<br>資料轉換，照軟體工程的做法來<br>`資料` | +147 | 4.9 | 14,213 |
| 7 | [apache/arrow](https://github.com/apache/arrow)<br>不同語言之間，資料直接通用<br>`資料` | +132 | 4.4 | 17,345 |
| 8 | [jupyter/notebook](https://github.com/jupyter/notebook)<br>在網頁裡寫程式碼，邊寫邊看結果<br>`資料` | +34 | 1.1 | 13,482 |

<details>
<summary>本榜星號歷史曲線</summary>

<a href="https://www.star-history.com/#duckdb/duckdb&Date"><img src="https://api.star-history.com/svg?repos=duckdb/duckdb&type=Date" width="260" alt="duckdb/duckdb 的星號歷史曲線"></a>

<a href="https://www.star-history.com/#ClickHouse/ClickHouse&Date"><img src="https://api.star-history.com/svg?repos=ClickHouse/ClickHouse&type=Date" width="260" alt="ClickHouse/ClickHouse 的星號歷史曲線"></a>

<a href="https://www.star-history.com/#apache/superset&Date"><img src="https://api.star-history.com/svg?repos=apache/superset&type=Date" width="260" alt="apache/superset 的星號歷史曲線"></a>

<a href="https://www.star-history.com/#pola-rs/polars&Date"><img src="https://api.star-history.com/svg?repos=pola-rs/polars&type=Date" width="260" alt="pola-rs/polars 的星號歷史曲線"></a>

<a href="https://www.star-history.com/#apache/kafka&Date"><img src="https://api.star-history.com/svg?repos=apache/kafka&type=Date" width="260" alt="apache/kafka 的星號歷史曲線"></a>

<a href="https://www.star-history.com/#dbt-labs/dbt-core&Date"><img src="https://api.star-history.com/svg?repos=dbt-labs/dbt-core&type=Date" width="260" alt="dbt-labs/dbt-core 的星號歷史曲線"></a>

<a href="https://www.star-history.com/#apache/arrow&Date"><img src="https://api.star-history.com/svg?repos=apache/arrow&type=Date" width="260" alt="apache/arrow 的星號歷史曲線"></a>

<a href="https://www.star-history.com/#jupyter/notebook&Date"><img src="https://api.star-history.com/svg?repos=jupyter/notebook&type=Date" width="260" alt="jupyter/notebook 的星號歷史曲線"></a>

</details>

### 今年成長最快（近 365 天）

| # | 專案 | 新增星號 | 星號/天 | 總星號 |
|---|---|---:|---:|---:|
| 1 | [duckdb/duckdb](https://github.com/duckdb/duckdb)<br>不搭資料庫服務，也能跑 SQL 分析<br>`資料` | +9,440 | 25.9 | 43,347 |
| 2 | [ClickHouse/ClickHouse](https://github.com/ClickHouse/ClickHouse)<br>大量資料即時分析，用開源的<br>`資料` | +7,526 | 20.6 | 51,134 |
| 3 | [apache/superset](https://github.com/apache/superset)<br>資料看不懂，做成圖就明白<br>`資料` | +7,405 | 20.3 | 75,678 |
| 4 | [pola-rs/polars](https://github.com/pola-rs/polars)<br>表格資料處理快，不用乾等<br>`資料` | +4,782 | 13.1 | 40,503 |
| 5 | [apache/kafka](https://github.com/apache/kafka)<br>系統之間的事件流，交給它來傳<br>`資料` | +3,340 | 9.2 | 34,351 |
| 6 | [dbt-labs/dbt-core](https://github.com/dbt-labs/dbt-core)<br>資料轉換，照軟體工程的做法來<br>`資料` | +2,466 | 6.8 | 14,213 |
| 7 | [apache/arrow](https://github.com/apache/arrow)<br>不同語言之間，資料直接通用<br>`資料` | +1,317 | 3.6 | 17,345 |
| 8 | [jupyter/notebook](https://github.com/jupyter/notebook)<br>在網頁裡寫程式碼，邊寫邊看結果<br>`資料` | +854 | 2.3 | 13,482 |

<details>
<summary>本榜星號歷史曲線</summary>

<a href="https://www.star-history.com/#duckdb/duckdb&Date"><img src="https://api.star-history.com/svg?repos=duckdb/duckdb&type=Date" width="260" alt="duckdb/duckdb 的星號歷史曲線"></a>

<a href="https://www.star-history.com/#ClickHouse/ClickHouse&Date"><img src="https://api.star-history.com/svg?repos=ClickHouse/ClickHouse&type=Date" width="260" alt="ClickHouse/ClickHouse 的星號歷史曲線"></a>

<a href="https://www.star-history.com/#apache/superset&Date"><img src="https://api.star-history.com/svg?repos=apache/superset&type=Date" width="260" alt="apache/superset 的星號歷史曲線"></a>

<a href="https://www.star-history.com/#pola-rs/polars&Date"><img src="https://api.star-history.com/svg?repos=pola-rs/polars&type=Date" width="260" alt="pola-rs/polars 的星號歷史曲線"></a>

<a href="https://www.star-history.com/#apache/kafka&Date"><img src="https://api.star-history.com/svg?repos=apache/kafka&type=Date" width="260" alt="apache/kafka 的星號歷史曲線"></a>

<a href="https://www.star-history.com/#dbt-labs/dbt-core&Date"><img src="https://api.star-history.com/svg?repos=dbt-labs/dbt-core&type=Date" width="260" alt="dbt-labs/dbt-core 的星號歷史曲線"></a>

<a href="https://www.star-history.com/#apache/arrow&Date"><img src="https://api.star-history.com/svg?repos=apache/arrow&type=Date" width="260" alt="apache/arrow 的星號歷史曲線"></a>

<a href="https://www.star-history.com/#jupyter/notebook&Date"><img src="https://api.star-history.com/svg?repos=jupyter/notebook&type=Date" width="260" alt="jupyter/notebook 的星號歷史曲線"></a>

</details>

### 總星號數（歷史累計）

| # | 專案 | 總星號 |
|---|---|---:|
| 1 | [apache/superset](https://github.com/apache/superset)<br>資料看不懂，做成圖就明白<br>`資料` | 75,678 |
| 2 | [ClickHouse/ClickHouse](https://github.com/ClickHouse/ClickHouse)<br>大量資料即時分析，用開源的<br>`資料` | 51,134 |
| 3 | [duckdb/duckdb](https://github.com/duckdb/duckdb)<br>不搭資料庫服務，也能跑 SQL 分析<br>`資料` | 43,347 |
| 4 | [pola-rs/polars](https://github.com/pola-rs/polars)<br>表格資料處理快，不用乾等<br>`資料` | 40,503 |
| 5 | [apache/kafka](https://github.com/apache/kafka)<br>系統之間的事件流，交給它來傳<br>`資料` | 34,351 |
| 6 | [apache/arrow](https://github.com/apache/arrow)<br>不同語言之間，資料直接通用<br>`資料` | 17,345 |
| 7 | [dbt-labs/dbt-core](https://github.com/dbt-labs/dbt-core)<br>資料轉換，照軟體工程的做法來<br>`資料` | 14,213 |
| 8 | [jupyter/notebook](https://github.com/jupyter/notebook)<br>在網頁裡寫程式碼，邊寫邊看結果<br>`資料` | 13,482 |

<details>
<summary>本榜星號歷史曲線</summary>

<a href="https://www.star-history.com/#apache/superset&Date"><img src="https://api.star-history.com/svg?repos=apache/superset&type=Date" width="260" alt="apache/superset 的星號歷史曲線"></a>

<a href="https://www.star-history.com/#ClickHouse/ClickHouse&Date"><img src="https://api.star-history.com/svg?repos=ClickHouse/ClickHouse&type=Date" width="260" alt="ClickHouse/ClickHouse 的星號歷史曲線"></a>

<a href="https://www.star-history.com/#duckdb/duckdb&Date"><img src="https://api.star-history.com/svg?repos=duckdb/duckdb&type=Date" width="260" alt="duckdb/duckdb 的星號歷史曲線"></a>

<a href="https://www.star-history.com/#pola-rs/polars&Date"><img src="https://api.star-history.com/svg?repos=pola-rs/polars&type=Date" width="260" alt="pola-rs/polars 的星號歷史曲線"></a>

<a href="https://www.star-history.com/#apache/kafka&Date"><img src="https://api.star-history.com/svg?repos=apache/kafka&type=Date" width="260" alt="apache/kafka 的星號歷史曲線"></a>

<a href="https://www.star-history.com/#apache/arrow&Date"><img src="https://api.star-history.com/svg?repos=apache/arrow&type=Date" width="260" alt="apache/arrow 的星號歷史曲線"></a>

<a href="https://www.star-history.com/#dbt-labs/dbt-core&Date"><img src="https://api.star-history.com/svg?repos=dbt-labs/dbt-core&type=Date" width="260" alt="dbt-labs/dbt-core 的星號歷史曲線"></a>

<a href="https://www.star-history.com/#jupyter/notebook&Date"><img src="https://api.star-history.com/svg?repos=jupyter/notebook&type=Date" width="260" alt="jupyter/notebook 的星號歷史曲線"></a>

</details>

---

如果它幫你省了時間，請給儲存庫按個星號，讓更多人找得到。

如何引用：見 [CITATION.cff](CITATION.cff)。

資料怎麼算與如何參與：[docs/HOW_IT_WORKS.zh-Hant.md](docs/HOW_IT_WORKS.zh-Hant.md)。新儲存庫規則：[docs/NEW_ARRIVALS.md](docs/NEW_ARRIVALS.md)。分類說明：[docs/CATEGORIES.md](docs/CATEGORIES.md)。提交改動：[CONTRIBUTING.md](CONTRIBUTING.md)。
