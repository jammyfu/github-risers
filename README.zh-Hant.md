[English](README.md) | [简体中文](README.zh-Hans.md) | **繁體中文** | [日本語](README.ja.md) | [한국어](README.ko.md)

# GitHub 漲星榜 / GitHub Risers

<img src=".github/social-preview.png" alt="GitHub 漲星榜 / GitHub Risers" width="640">

[![MIT](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE) [![CI](https://github.com/jammyfu/github-risers/actions/workflows/ci.yml/badge.svg)](https://github.com/jammyfu/github-risers/actions/workflows/ci.yml) [![updated](https://img.shields.io/badge/dynamic/json?url=https%3A%2F%2Fraw.githubusercontent.com%2Fjammyfu%2Fgithub-risers%2Fmain%2Fdata%2Fstats.json&query=%24.today_utc&label=updated&color=brightgreen)](latest/rankings.zh-Hant.md)

依每天新增星號（而不是總星號）替 GitHub 儲存庫排名：AI 在前，接著是開發者工具、資安、Web / 前端、基礎建設、設計 / 創意與資料；每天更新兩次。

資料取自 2026-11-01 20:08（UTC）。每天兩次：北京時間 0 點（UTC+8）、洛杉磯時間 0 點（America/Los_Angeles）。

[網站](https://jammyfu.github.io/github-risers/) · [運作方式](docs/HOW_IT_WORKS.zh-Hant.md) · [事實速查](docs/FACTS.md) · [歷史榜單](rankings/README.zh-Hant.md) · [最新快照](latest/rankings.zh-Hant.md)

## 本期各類榜首

| 分類 | 新儲存庫第 1 名（7 天） | 本週第 1 名 | 本月第 1 名 | 今年第 1 名 | 總星號第 1 名 |
|---|---|---|---|---|---|
| **[人工智慧](#人工智慧)** ★ 主榜 | [wangzan101/Mika](https://github.com/wangzan101/Mika)<br>1,156/天 | [morluto/rea](https://github.com/morluto/rea)<br>5,273/天 | [morluto/rea](https://github.com/morluto/rea)<br>13,859/天 | [deepseek-ai/deepseek-harness](https://github.com/deepseek-ai/deepseek-harness)<br>3,346/天 | [morluto/rea](https://github.com/morluto/rea)<br>418,258 ★ |
| **[開發者工具](#開發者工具)** | [Verlintas/NOIR](https://github.com/Verlintas/NOIR)<br>220/天 | [zed-industries/zed](https://github.com/zed-industries/zed)<br>55.3/天 | [zed-industries/zed](https://github.com/zed-industries/zed)<br>52.4/天 | [zed-industries/zed](https://github.com/zed-industries/zed)<br>70.4/天 | [oven-sh/bun](https://github.com/oven-sh/bun)<br>96,498 ★ |
| **[資安](#資安)** | [vaishantsah/watson-AI-osint-all-in-one](https://github.com/vaishantsah/watson-AI-osint-all-in-one)<br>74.1/天 | [projectdiscovery/nuclei](https://github.com/projectdiscovery/nuclei)<br>32.3/天 | [projectdiscovery/nuclei](https://github.com/projectdiscovery/nuclei)<br>30.5/天 | [aquasecurity/trivy](https://github.com/aquasecurity/trivy)<br>27.7/天 | [aquasecurity/trivy](https://github.com/aquasecurity/trivy)<br>38,895 ★ |
| **[Web / 前端](#web--前端)** | [D3voz/openjutsu](https://github.com/D3voz/openjutsu)<br>164/天 | [shadcn-ui/ui](https://github.com/shadcn-ui/ui)<br>96.4/天 | [shadcn-ui/ui](https://github.com/shadcn-ui/ui)<br>86.5/天 | [shadcn-ui/ui](https://github.com/shadcn-ui/ui)<br>83.1/天 | [facebook/react](https://github.com/facebook/react)<br>252,066 ★ |
| **[基礎建設](#基礎建設)** | [davemessew/AgentFlux](https://github.com/davemessew/AgentFlux)<br>45.2/天 | [kubernetes/kubernetes](https://github.com/kubernetes/kubernetes)<br>63.4/天 | [caddyserver/caddy](https://github.com/caddyserver/caddy)<br>83.7/天 | [caddyserver/caddy](https://github.com/caddyserver/caddy)<br>32.5/天 | [kubernetes/kubernetes](https://github.com/kubernetes/kubernetes)<br>128,809 ★ |
| **[設計 / 創意](#設計--創意)** | [patch-gg/pixelfx](https://github.com/patch-gg/pixelfx)<br>958/天 | [excalidraw/excalidraw](https://github.com/excalidraw/excalidraw)<br>68.3/天 | [excalidraw/excalidraw](https://github.com/excalidraw/excalidraw)<br>65.5/天 | [excalidraw/excalidraw](https://github.com/excalidraw/excalidraw)<br>74.0/天 | [excalidraw/excalidraw](https://github.com/excalidraw/excalidraw)<br>134,976 ★ |
| **[資料](#資料)** | 無 | [duckdb/duckdb](https://github.com/duckdb/duckdb)<br>35.3/天 | [duckdb/duckdb](https://github.com/duckdb/duckdb)<br>31.0/天 | [duckdb/duckdb](https://github.com/duckdb/duckdb)<br>25.6/天 | [apache/superset](https://github.com/apache/superset)<br>75,386 ★ |

這裡每張榜只列前 10 名，完整的前 20 名見 [latest/rankings.zh-Hant.md](latest/rankings.zh-Hant.md)。

表裡每個專案只留一句話；完整介紹（含工具名稱、技術細節）見 [docs/DETAILS.zh-Hant.md](docs/DETAILS.zh-Hant.md)。

## 常見問題

### GitHub 漲星榜是什麼？

依每天新增星號、而不是總星號替 GitHub 儲存庫排名的榜單。AI 是主榜，後面還有六個分類；資料由腳本從 GitHub API 產生。 [了解更多](docs/FAQ.md#what-is-github-risers)

### 和 GitHub Trending 有什麼不同？

GitHub Trending 是 GitHub 官方頁面；GitHub 漲星榜是獨立的開源專案，規則公開，有五種語言，並保存每次更新的歷史。它與 GitHub 官方沒有關聯。 [了解更多](docs/FAQ.md#is-it-the-same-as-github-trending)

### 多久更新一次？

每天兩次，北京時間 0 點和洛杉磯時間 0 點；每次執行都會存檔。 [了解更多](docs/FAQ.md#how-often-is-it-updated)

### 資料怎麼算？

取最近 7、30 或 365 個完整 UTC 日的新增星號，再除以天數。數字全部來自 GitHub API，沒有手填或估算。 [了解更多](docs/FAQ.md#how-is-the-growth-rate-computed)

### 怎麼看、怎麼參與？

看下面的榜，完整前 20 名在 latest/。要收錄專案，改 data/projects.json（五種語言）並發 pull request。 [了解更多](docs/FAQ.md#how-can-i-suggest-a-project-or-report-a-mistake)

## 人工智慧

> 大型語言模型、代理、MCP、程式設計助手與生成式 AI

### 最熱新儲存庫（近 7 天內建立）

| # | 專案 | 建立時間（UTC） | 總星號 | 星號/天 | 星號歷史 |
|---|---|---|---:|---:|---|
| 1 | [wangzan101/Mika](https://github.com/wangzan101/Mika)<br>手機瑣事太多？讓代理替你操作應用 | 2026-10-29<br><sub>3.2 天</sub> | 3,737 | 1,156.3 | <a href="https://www.star-history.com/#wangzan101/Mika&Date"><img src="https://api.star-history.com/svg?repos=wangzan101/Mika&type=Date" width="260" alt="wangzan101/Mika 的星號歷史曲線"></a> |
| 2 | [caru-ini/stack-diagram](https://github.com/caru-ini/stack-diagram)<br>Agent skill: describe your stack in a sentence, get an architecture diagram with official logos | 2026-11-01<br><sub>1.0 天</sub> | 296 | 296.0 | <a href="https://www.star-history.com/#caru-ini/stack-diagram&Date"><img src="https://api.star-history.com/svg?repos=caru-ini/stack-diagram&type=Date" width="260" alt="caru-ini/stack-diagram 的星號歷史曲線"></a> |
| 3 | [haydenschmitty/floorplan](https://github.com/haydenschmitty/floorplan)<br>程式碼庫怎麼拼起來的，看這張圖 | 2026-10-27<br><sub>5.3 天</sub> | 1,498 | 280.7 | <a href="https://www.star-history.com/#haydenschmitty/floorplan&Date"><img src="https://api.star-history.com/svg?repos=haydenschmitty/floorplan&type=Date" width="260" alt="haydenschmitty/floorplan 的星號歷史曲線"></a> |
| 4 | [NiazMorshed2007/reanimate](https://github.com/NiazMorshed2007/reanimate)<br>動效抄不像？逐幀還原並驗證完全一致 | 2026-10-29<br><sub>3.6 天</sub> | 708 | 198.1 | <a href="https://www.star-history.com/#NiazMorshed2007/reanimate&Date"><img src="https://api.star-history.com/svg?repos=NiazMorshed2007/reanimate&type=Date" width="260" alt="NiazMorshed2007/reanimate 的星號歷史曲線"></a> |
| 5 | [N1nEmAn/sapper-v2](https://github.com/N1nEmAn/sapper-v2)<br>安全測試太費勁？讓 AI 軍團自主排查 | 2026-10-30<br><sub>2.2 天</sub> | 432 | 195.9 | <a href="https://www.star-history.com/#N1nEmAn/sapper-v2&Date"><img src="https://api.star-history.com/svg?repos=N1nEmAn/sapper-v2&type=Date" width="260" alt="N1nEmAn/sapper-v2 的星號歷史曲線"></a> |
| 6 | [alchaincyf/huashu-bird-sticker](https://github.com/alchaincyf/huashu-bird-sticker)<br>找鳥類貼紙太難？集齊 11,064 種鳥 | 2026-10-30<br><sub>2.6 天</sub> | 485 | 185.3 | <a href="https://www.star-history.com/#alchaincyf/huashu-bird-sticker&Date"><img src="https://api.star-history.com/svg?repos=alchaincyf/huashu-bird-sticker&type=Date" width="260" alt="alchaincyf/huashu-bird-sticker 的星號歷史曲線"></a> |
| 7 | [sleepy-zone/ai-ref-library-cn](https://github.com/sleepy-zone/ai-ref-library-cn)<br>AI作圖缺參考？備齊臉型姿勢與服裝 | 2026-10-29<br><sub>3.2 天</sub> | 551 | 172.5 | <a href="https://www.star-history.com/#sleepy-zone/ai-ref-library-cn&Date"><img src="https://api.star-history.com/svg?repos=sleepy-zone/ai-ref-library-cn&type=Date" width="260" alt="sleepy-zone/ai-ref-library-cn 的星號歷史曲線"></a> |
| 8 | [Pluviobyte/douyin-comments](https://github.com/Pluviobyte/douyin-comments)<br>抖音評論抓不全？完整抓取所有樓中樓 | 2026-10-30<br><sub>2.2 天</sub> | 366 | 167.8 | <a href="https://www.star-history.com/#Pluviobyte/douyin-comments&Date"><img src="https://api.star-history.com/svg?repos=Pluviobyte/douyin-comments&type=Date" width="260" alt="Pluviobyte/douyin-comments 的星號歷史曲線"></a> |
| 9 | [tavern-labs-ai/persona-ai-sdk](https://github.com/tavern-labs-ai/persona-ai-sdk)<br>AI總記不住聊天？為角色添上持久記憶 | 2026-10-31<br><sub>1.2 天</sub> | 192 | 155.4 | <a href="https://www.star-history.com/#tavern-labs-ai/persona-ai-sdk&Date"><img src="https://api.star-history.com/svg?repos=tavern-labs-ai/persona-ai-sdk&type=Date" width="260" alt="tavern-labs-ai/persona-ai-sdk 的星號歷史曲線"></a> |
| 10 | [jackwener/DSH-Android](https://github.com/jackwener/DSH-Android)<br>免 ROOT 免 Termux，一個 APK 在安卓手機上跑 DeepSeek Harness。引擎內嵌 App 行程 · 讀屏操作 App · 改系統設定 · 定時/條件自動化 · 可選 Shizuku | 2026-10-27<br><sub>5.0 天</sub> | 691 | 137.4 | <a href="https://www.star-history.com/#jackwener/DSH-Android&Date"><img src="https://api.star-history.com/svg?repos=jackwener/DSH-Android&type=Date" width="260" alt="jackwener/DSH-Android 的星號歷史曲線"></a> |

### 本週成長最快（近 7 天）

| # | 專案 | 新增星號 | 星號/天 | 總星號 | 星號歷史 |
|---|---|---:|---:|---:|---|
| 1 | [morluto/rea](https://github.com/morluto/rea)<br>讓 AI 幫你克隆任何軟體<br>`人工智慧` | +36,911 | 5,273.0 | 418,258 | <a href="https://www.star-history.com/#morluto/rea&Date"><img src="https://api.star-history.com/svg?repos=morluto/rea&type=Date" width="260" alt="morluto/rea 的星號歷史曲線"></a> |
| 2 | [cloudflare/security-audit-skill](https://github.com/cloudflare/security-audit-skill)<br>AI 查程式碼漏洞，另一個 AI 逐條複核<br>`人工智慧` | +10,474 | 1,496.3 | 56,224 | <a href="https://www.star-history.com/#cloudflare/security-audit-skill&Date"><img src="https://api.star-history.com/svg?repos=cloudflare/security-audit-skill&type=Date" width="260" alt="cloudflare/security-audit-skill 的星號歷史曲線"></a> |
| 3 | [deepseek-ai/deepseek-harness](https://github.com/deepseek-ai/deepseek-harness)<br>想要什麼代理，用外掛自己拼<br>`人工智慧` | +7,321 | 1,045.9 | 268,255 | <a href="https://www.star-history.com/#deepseek-ai/deepseek-harness&Date"><img src="https://api.star-history.com/svg?repos=deepseek-ai/deepseek-harness&type=Date" width="260" alt="deepseek-ai/deepseek-harness 的星號歷史曲線"></a> |
| 4 | [stablyai/orca](https://github.com/stablyai/orca)<br>幾個 AI 一起寫，誰好用一眼看出<br>`人工智慧` | +6,963 | 994.7 | 112,366 | <a href="https://www.star-history.com/#stablyai/orca&Date"><img src="https://api.star-history.com/svg?repos=stablyai/orca&type=Date" width="260" alt="stablyai/orca 的星號歷史曲線"></a> |
| 5 | [yetone/magpie](https://github.com/yetone/magpie)<br>程式設計 AI 換模型，額度用完自動續<br>`人工智慧` | +6,278 | 896.9 | 27,536 | <a href="https://www.star-history.com/#yetone/magpie&Date"><img src="https://api.star-history.com/svg?repos=yetone/magpie&type=Date" width="260" alt="yetone/magpie 的星號歷史曲線"></a> |
| 6 | [affaan-m/ECC](https://github.com/affaan-m/ECC)<br>給程式設計 AI 加記憶、技能和安全檢查<br>`人工智慧` | +6,269 | 895.6 | 294,677 | <a href="https://www.star-history.com/#affaan-m/ECC&Date"><img src="https://api.star-history.com/svg?repos=affaan-m/ECC&type=Date" width="260" alt="affaan-m/ECC 的星號歷史曲線"></a> |
| 7 | [DietrichGebert/ponytail](https://github.com/DietrichGebert/ponytail)<br>讓 AI 少寫廢程式碼，該寫的寫對<br>`人工智慧` | +6,206 | 886.6 | 182,039 | <a href="https://www.star-history.com/#DietrichGebert/ponytail&Date"><img src="https://api.star-history.com/svg?repos=DietrichGebert/ponytail&type=Date" width="260" alt="DietrichGebert/ponytail 的星號歷史曲線"></a> |
| 8 | [Graphify-Labs/graphify](https://github.com/Graphify-Labs/graphify)<br>大專案看不過來，先看這張地圖<br>`人工智慧` | +5,723 | 817.6 | 140,462 | <a href="https://www.star-history.com/#Graphify-Labs/graphify&Date"><img src="https://api.star-history.com/svg?repos=Graphify-Labs/graphify&type=Date" width="260" alt="Graphify-Labs/graphify 的星號歷史曲線"></a> |
| 9 | [Panniantong/Agent-Reach](https://github.com/Panniantong/Agent-Reach)<br>推特油管小紅書，AI 都能幫你搜<br>`人工智慧` | +5,490 | 784.3 | 107,557 | <a href="https://www.star-history.com/#Panniantong/Agent-Reach&Date"><img src="https://api.star-history.com/svg?repos=Panniantong/Agent-Reach&type=Date" width="260" alt="Panniantong/Agent-Reach 的星號歷史曲線"></a> |
| 10 | [thedotmack/claude-mem](https://github.com/thedotmack/claude-mem)<br>AI 不再忘記上次做到哪<br>`人工智慧` | +5,436 | 776.6 | 109,008 | <a href="https://www.star-history.com/#thedotmack/claude-mem&Date"><img src="https://api.star-history.com/svg?repos=thedotmack/claude-mem&type=Date" width="260" alt="thedotmack/claude-mem 的星號歷史曲線"></a> |

### 本月成長最快（近 30 天）

| # | 專案 | 新增星號 | 星號/天 | 總星號 | 星號歷史 |
|---|---|---:|---:|---:|---|
| 1 | [morluto/rea](https://github.com/morluto/rea)<br>讓 AI 幫你克隆任何軟體<br>`人工智慧` | +415,781 | 13,859.4 | 418,258 | <a href="https://www.star-history.com/#morluto/rea&Date"><img src="https://api.star-history.com/svg?repos=morluto/rea&type=Date" width="260" alt="morluto/rea 的星號歷史曲線"></a> |
| 2 | [cloudflare/security-audit-skill](https://github.com/cloudflare/security-audit-skill)<br>AI 查程式碼漏洞，另一個 AI 逐條複核<br>`人工智慧` | +32,125 | 1,070.8 | 56,224 | <a href="https://www.star-history.com/#cloudflare/security-audit-skill&Date"><img src="https://api.star-history.com/svg?repos=cloudflare/security-audit-skill&type=Date" width="260" alt="cloudflare/security-audit-skill 的星號歷史曲線"></a> |
| 3 | [DietrichGebert/ponytail](https://github.com/DietrichGebert/ponytail)<br>讓 AI 少寫廢程式碼，該寫的寫對<br>`人工智慧` | +31,929 | 1,064.3 | 182,039 | <a href="https://www.star-history.com/#DietrichGebert/ponytail&Date"><img src="https://api.star-history.com/svg?repos=DietrichGebert/ponytail&type=Date" width="260" alt="DietrichGebert/ponytail 的星號歷史曲線"></a> |
| 4 | [stablyai/orca](https://github.com/stablyai/orca)<br>幾個 AI 一起寫，誰好用一眼看出<br>`人工智慧` | +29,183 | 972.8 | 112,366 | <a href="https://www.star-history.com/#stablyai/orca&Date"><img src="https://api.star-history.com/svg?repos=stablyai/orca&type=Date" width="260" alt="stablyai/orca 的星號歷史曲線"></a> |
| 5 | [deepseek-ai/deepseek-harness](https://github.com/deepseek-ai/deepseek-harness)<br>想要什麼代理，用外掛自己拼<br>`人工智慧` | +27,225 | 907.5 | 268,255 | <a href="https://www.star-history.com/#deepseek-ai/deepseek-harness&Date"><img src="https://api.star-history.com/svg?repos=deepseek-ai/deepseek-harness&type=Date" width="260" alt="deepseek-ai/deepseek-harness 的星號歷史曲線"></a> |
| 6 | [affaan-m/ECC](https://github.com/affaan-m/ECC)<br>給程式設計 AI 加記憶、技能和安全檢查<br>`人工智慧` | +25,033 | 834.4 | 294,677 | <a href="https://www.star-history.com/#affaan-m/ECC&Date"><img src="https://api.star-history.com/svg?repos=affaan-m/ECC&type=Date" width="260" alt="affaan-m/ECC 的星號歷史曲線"></a> |
| 7 | [yetone/magpie](https://github.com/yetone/magpie)<br>程式設計 AI 換模型，額度用完自動續<br>`人工智慧` | +23,074 | 769.1 | 27,536 | <a href="https://www.star-history.com/#yetone/magpie&Date"><img src="https://api.star-history.com/svg?repos=yetone/magpie&type=Date" width="260" alt="yetone/magpie 的星號歷史曲線"></a> |
| 8 | [heygen-com/hyperframes](https://github.com/heygen-com/hyperframes)<br>不會剪輯，寫網頁一樣就能出片<br>`人工智慧` | +21,555 | 718.5 | 77,028 | <a href="https://www.star-history.com/#heygen-com/hyperframes&Date"><img src="https://api.star-history.com/svg?repos=heygen-com/hyperframes&type=Date" width="260" alt="heygen-com/hyperframes 的星號歷史曲線"></a> |
| 9 | [Panniantong/Agent-Reach](https://github.com/Panniantong/Agent-Reach)<br>推特油管小紅書，AI 都能幫你搜<br>`人工智慧` | +20,265 | 675.5 | 107,557 | <a href="https://www.star-history.com/#Panniantong/Agent-Reach&Date"><img src="https://api.star-history.com/svg?repos=Panniantong/Agent-Reach&type=Date" width="260" alt="Panniantong/Agent-Reach 的星號歷史曲線"></a> |
| 10 | [Graphify-Labs/graphify](https://github.com/Graphify-Labs/graphify)<br>大專案看不過來，先看這張地圖<br>`人工智慧` | +17,813 | 593.8 | 140,462 | <a href="https://www.star-history.com/#Graphify-Labs/graphify&Date"><img src="https://api.star-history.com/svg?repos=Graphify-Labs/graphify&type=Date" width="260" alt="Graphify-Labs/graphify 的星號歷史曲線"></a> |

### 今年成長最快（近 365 天）

| # | 專案 | 新增星號 | 星號/天 | 總星號 | 星號歷史 |
|---|---|---:|---:|---:|---|
| 1 | [deepseek-ai/deepseek-harness](https://github.com/deepseek-ai/deepseek-harness)<br>想要什麼代理，用外掛自己拼<br>`人工智慧` | +267,656 | 3,345.7 †<br><sub>÷80 天</sub> | 268,255 | <a href="https://www.star-history.com/#deepseek-ai/deepseek-harness&Date"><img src="https://api.star-history.com/svg?repos=deepseek-ai/deepseek-harness&type=Date" width="260" alt="deepseek-ai/deepseek-harness 的星號歷史曲線"></a> |
| 2 | [morluto/rea](https://github.com/morluto/rea)<br>讓 AI 幫你克隆任何軟體<br>`人工智慧` | +416,184 | 2,070.6 †<br><sub>÷201 天</sub> | 418,258 | <a href="https://www.star-history.com/#morluto/rea&Date"><img src="https://api.star-history.com/svg?repos=morluto/rea&type=Date" width="260" alt="morluto/rea 的星號歷史曲線"></a> |
| 3 | [DietrichGebert/ponytail](https://github.com/DietrichGebert/ponytail)<br>讓 AI 少寫廢程式碼，該寫的寫對<br>`人工智慧` | +181,642 | 1,279.2 †<br><sub>÷142 天</sub> | 182,039 | <a href="https://www.star-history.com/#DietrichGebert/ponytail&Date"><img src="https://api.star-history.com/svg?repos=DietrichGebert/ponytail&type=Date" width="260" alt="DietrichGebert/ponytail 的星號歷史曲線"></a> |
| 4 | [openclaw/openclaw](https://github.com/openclaw/openclaw)<br>能把事做完的 AI 助理，跑在自己裝置上<br>`人工智慧` | +393,546 | 1,150.7 †<br><sub>÷342 天</sub> | 393,635 | <a href="https://www.star-history.com/#openclaw/openclaw&Date"><img src="https://api.star-history.com/svg?repos=openclaw/openclaw&type=Date" width="260" alt="openclaw/openclaw 的星號歷史曲線"></a> |
| 5 | [affaan-m/ECC](https://github.com/affaan-m/ECC)<br>給程式設計 AI 加記憶、技能和安全檢查<br>`人工智慧` | +294,202 | 1,025.1 †<br><sub>÷287 天</sub> | 294,677 | <a href="https://www.star-history.com/#affaan-m/ECC&Date"><img src="https://api.star-history.com/svg?repos=affaan-m/ECC&type=Date" width="260" alt="affaan-m/ECC 的星號歷史曲線"></a> |
| 6 | [NousResearch/hermes-agent](https://github.com/NousResearch/hermes-agent)<br>越用越會幹活的 AI 助手<br>`人工智慧` | +259,250 | 710.3 | 259,458 | <a href="https://www.star-history.com/#NousResearch/hermes-agent&Date"><img src="https://api.star-history.com/svg?repos=NousResearch/hermes-agent&type=Date" width="260" alt="NousResearch/hermes-agent 的星號歷史曲線"></a> |
| 7 | [yetone/magpie](https://github.com/yetone/magpie)<br>程式設計 AI 換模型，額度用完自動續<br>`人工智慧` | +27,144 | 696.0 †<br><sub>÷39 天</sub> | 27,536 | <a href="https://www.star-history.com/#yetone/magpie&Date"><img src="https://api.star-history.com/svg?repos=yetone/magpie&type=Date" width="260" alt="yetone/magpie 的星號歷史曲線"></a> |
| 8 | [Graphify-Labs/graphify](https://github.com/Graphify-Labs/graphify)<br>大專案看不過來，先看這張地圖<br>`人工智慧` | +140,130 | 661.0 †<br><sub>÷212 天</sub> | 140,462 | <a href="https://www.star-history.com/#Graphify-Labs/graphify&Date"><img src="https://api.star-history.com/svg?repos=Graphify-Labs/graphify&type=Date" width="260" alt="Graphify-Labs/graphify 的星號歷史曲線"></a> |
| 9 | [anomalyco/opencode](https://github.com/anomalyco/opencode)<br>終端機裡，有個開源 AI 幫你寫程式碼<br>`人工智慧` | +194,966 | 534.2 | 223,805 | <a href="https://www.star-history.com/#anomalyco/opencode&Date"><img src="https://api.star-history.com/svg?repos=anomalyco/opencode&type=Date" width="260" alt="anomalyco/opencode 的星號歷史曲線"></a> |
| 10 | [stablyai/orca](https://github.com/stablyai/orca)<br>幾個 AI 一起寫，誰好用一眼看出<br>`人工智慧` | +111,873 | 488.5 †<br><sub>÷229 天</sub> | 112,366 | <a href="https://www.star-history.com/#stablyai/orca&Date"><img src="https://api.star-history.com/svg?repos=stablyai/orca&type=Date" width="260" alt="stablyai/orca 的星號歷史曲線"></a> |

† 該儲存庫建立時間短於統計區間，因此「星號/天」是以儲存庫存在的天數（顯示在數字下方）計算，而不是以完整區間計算。

### 總星號數（歷史累計）

| # | 專案 | 總星號 | 星號歷史 |
|---|---|---:|---|
| 1 | [morluto/rea](https://github.com/morluto/rea)<br>讓 AI 幫你克隆任何軟體<br>`人工智慧` | 418,258 | <a href="https://www.star-history.com/#morluto/rea&Date"><img src="https://api.star-history.com/svg?repos=morluto/rea&type=Date" width="260" alt="morluto/rea 的星號歷史曲線"></a> |
| 2 | [openclaw/openclaw](https://github.com/openclaw/openclaw)<br>能把事做完的 AI 助理，跑在自己裝置上<br>`人工智慧` | 393,635 | <a href="https://www.star-history.com/#openclaw/openclaw&Date"><img src="https://api.star-history.com/svg?repos=openclaw/openclaw&type=Date" width="260" alt="openclaw/openclaw 的星號歷史曲線"></a> |
| 3 | [affaan-m/ECC](https://github.com/affaan-m/ECC)<br>給程式設計 AI 加記憶、技能和安全檢查<br>`人工智慧` | 294,677 | <a href="https://www.star-history.com/#affaan-m/ECC&Date"><img src="https://api.star-history.com/svg?repos=affaan-m/ECC&type=Date" width="260" alt="affaan-m/ECC 的星號歷史曲線"></a> |
| 4 | [deepseek-ai/deepseek-harness](https://github.com/deepseek-ai/deepseek-harness)<br>想要什麼代理，用外掛自己拼<br>`人工智慧` | 268,255 | <a href="https://www.star-history.com/#deepseek-ai/deepseek-harness&Date"><img src="https://api.star-history.com/svg?repos=deepseek-ai/deepseek-harness&type=Date" width="260" alt="deepseek-ai/deepseek-harness 的星號歷史曲線"></a> |
| 5 | [NousResearch/hermes-agent](https://github.com/NousResearch/hermes-agent)<br>越用越會幹活的 AI 助手<br>`人工智慧` | 259,458 | <a href="https://www.star-history.com/#NousResearch/hermes-agent&Date"><img src="https://api.star-history.com/svg?repos=NousResearch/hermes-agent&type=Date" width="260" alt="NousResearch/hermes-agent 的星號歷史曲線"></a> |
| 6 | [anomalyco/opencode](https://github.com/anomalyco/opencode)<br>終端機裡，有個開源 AI 幫你寫程式碼<br>`人工智慧` | 223,805 | <a href="https://www.star-history.com/#anomalyco/opencode&Date"><img src="https://api.star-history.com/svg?repos=anomalyco/opencode&type=Date" width="260" alt="anomalyco/opencode 的星號歷史曲線"></a> |
| 7 | [anthropics/skills](https://github.com/anthropics/skills)<br>Claude 技能怎麼寫，照著官方學<br>`人工智慧` | 186,287 | <a href="https://www.star-history.com/#anthropics/skills&Date"><img src="https://api.star-history.com/svg?repos=anthropics/skills&type=Date" width="260" alt="anthropics/skills 的星號歷史曲線"></a> |
| 8 | [DietrichGebert/ponytail](https://github.com/DietrichGebert/ponytail)<br>讓 AI 少寫廢程式碼，該寫的寫對<br>`人工智慧` | 182,039 | <a href="https://www.star-history.com/#DietrichGebert/ponytail&Date"><img src="https://api.star-history.com/svg?repos=DietrichGebert/ponytail&type=Date" width="260" alt="DietrichGebert/ponytail 的星號歷史曲線"></a> |
| 9 | [farion1231/cc-switch](https://github.com/farion1231/cc-switch)<br>換介面不用改配置，一鍵切<br>`人工智慧` | 150,858 | <a href="https://www.star-history.com/#farion1231/cc-switch&Date"><img src="https://api.star-history.com/svg?repos=farion1231/cc-switch&type=Date" width="260" alt="farion1231/cc-switch 的星號歷史曲線"></a> |
| 10 | [nextlevelbuilder/ui-ux-pro-max-skill](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill)<br>AI 做的介面，看著像專業設計<br>`人工智慧` | 143,768 | <a href="https://www.star-history.com/#nextlevelbuilder/ui-ux-pro-max-skill&Date"><img src="https://api.star-history.com/svg?repos=nextlevelbuilder/ui-ux-pro-max-skill&type=Date" width="260" alt="nextlevelbuilder/ui-ux-pro-max-skill 的星號歷史曲線"></a> |

## 開發者工具

> 命令列、編輯器、套件管理、程式碼檢查與建置工具

### 最熱新儲存庫（近 7 天內建立）

| # | 專案 | 建立時間（UTC） | 總星號 | 星號/天 | 星號歷史 |
|---|---|---|---:|---:|---|
| 1 | [Verlintas/NOIR](https://github.com/Verlintas/NOIR)<br>手機隱私審計：用 adb 掃出 Android 應用的權限、回報端點與數據流向，並給出可復原的處置。桌面 Android 洩漏審計：權限、端點、數據流向、可復原的修復。 | 2026-10-31<br><sub>1.0 天</sub> | 220 | 220.0 | <a href="https://www.star-history.com/#Verlintas/NOIR&Date"><img src="https://api.star-history.com/svg?repos=Verlintas/NOIR&type=Date" width="260" alt="Verlintas/NOIR 的星號歷史曲線"></a> |
| 2 | [Balanov/uncut](https://github.com/Balanov/uncut)<br>A 7 MB lossless coding-agent harness for shell, CI, and local models. No TUI. No silent context cuts. | 2026-11-01<br><sub>1.0 天</sub> | 131 | 131.0 | <a href="https://www.star-history.com/#Balanov/uncut&Date"><img src="https://api.star-history.com/svg?repos=Balanov/uncut&type=Date" width="260" alt="Balanov/uncut 的星號歷史曲線"></a> |
| 3 | [Straitbrashadow/minecraft-ai-mod-builder](https://github.com/Straitbrashadow/minecraft-ai-mod-builder)<br>輸入建築想法，在遊戲中一鍵放置或復原 | 2026-10-30<br><sub>2.0 天</sub> | 189 | 96.6 | <a href="https://www.star-history.com/#Straitbrashadow/minecraft-ai-mod-builder&Date"><img src="https://api.star-history.com/svg?repos=Straitbrashadow/minecraft-ai-mod-builder&type=Date" width="260" alt="Straitbrashadow/minecraft-ai-mod-builder 的星號歷史曲線"></a> |
| 4 | [DiplomatHearth/roblox-ai-place-diff](https://github.com/DiplomatHearth/roblox-ai-place-diff)<br>這款 Roblox Studio 代理所做的每一項變更都是由你先批准的 place diff。只需一次 Ctrl+Z 即可回退任何輪次，測試遊玩在複本上執行，因此實際資料絕不會移動… | 2026-10-30<br><sub>1.9 天</sub> | 151 | 78.2 | <a href="https://www.star-history.com/#DiplomatHearth/roblox-ai-place-diff&Date"><img src="https://api.star-history.com/svg?repos=DiplomatHearth/roblox-ai-place-diff&type=Date" width="260" alt="DiplomatHearth/roblox-ai-place-diff 的星號歷史曲線"></a> |
| 5 | [muaaz9329/cheap-ag](https://github.com/muaaz9329/cheap-ag)<br>避免用盡 Claude 配額，低成本寫程式 | 2026-10-28<br><sub>3.9 天</sub> | 192 | 49.2 | <a href="https://www.star-history.com/#muaaz9329/cheap-ag&Date"><img src="https://api.star-history.com/svg?repos=muaaz9329/cheap-ag&type=Date" width="260" alt="muaaz9329/cheap-ag 的星號歷史曲線"></a> |
| 6 | [OriginShaper/Microsoft-365](https://github.com/OriginShaper/Microsoft-365)<br>Microsoft 365 桌面公用程式設定 - 完整的獨立安裝設定，已啟用所有功能，開箱即用。 | 2026-10-30<br><sub>2.1 天</sub> | 102 | 48.3 | <a href="https://www.star-history.com/#OriginShaper/Microsoft-365&Date"><img src="https://api.star-history.com/svg?repos=OriginShaper/Microsoft-365&type=Date" width="260" alt="OriginShaper/Microsoft-365 的星號歷史曲線"></a> |
| 7 | [GravityHazeWay13/DxO-PhotoLab-10](https://github.com/GravityHazeWay13/DxO-PhotoLab-10)<br>開箱即用的 Dxo Photolab 10 桌面安裝組建版本，已完全啟用，隨時可用於專業相片處理。 | 2026-10-30<br><sub>2.1 天</sub> | 100 | 47.3 | <a href="https://www.star-history.com/#GravityHazeWay13/DxO-PhotoLab-10&Date"><img src="https://api.star-history.com/svg?repos=GravityHazeWay13/DxO-PhotoLab-10&type=Date" width="260" alt="GravityHazeWay13/DxO-PhotoLab-10 的星號歷史曲線"></a> |
| 8 | [Xpropel/Pi-Remote](https://github.com/Xpropel/Pi-Remote)<br>在任意瀏覽器中遠端控制 pi 代理 | 2026-10-28<br><sub>4.4 天</sub> | 200 | 45.6 | <a href="https://www.star-history.com/#Xpropel/Pi-Remote&Date"><img src="https://api.star-history.com/svg?repos=Xpropel/Pi-Remote&type=Date" width="260" alt="Xpropel/Pi-Remote 的星號歷史曲線"></a> |
| 9 | [tianfuzhibuyuci/readme-visual-kit](https://github.com/tianfuzhibuyuci/readme-visual-kit)<br>本機將專案說明生成三張 README 架構圖 | 2026-10-27<br><sub>5.3 天</sub> | 186 | 35.2 | <a href="https://www.star-history.com/#tianfuzhibuyuci/readme-visual-kit&Date"><img src="https://api.star-history.com/svg?repos=tianfuzhibuyuci/readme-visual-kit&type=Date" width="260" alt="tianfuzhibuyuci/readme-visual-kit 的星號歷史曲線"></a> |
| 10 | [khanh020905/my-office](https://github.com/khanh020905/my-office)<br>為 Claude Code 打造 3D 辦公空間 | 2026-10-28<br><sub>4.3 天</sub> | 128 | 29.6 | <a href="https://www.star-history.com/#khanh020905/my-office&Date"><img src="https://api.star-history.com/svg?repos=khanh020905/my-office&type=Date" width="260" alt="khanh020905/my-office 的星號歷史曲線"></a> |

### 本週成長最快（近 7 天）

| # | 專案 | 新增星號 | 星號/天 | 總星號 | 星號歷史 |
|---|---|---:|---:|---:|---|
| 1 | [zed-industries/zed](https://github.com/zed-industries/zed)<br>開啟就快，還能多人一起寫程式碼<br>`開發者工具` | +387 | 55.3 | 92,496 | <a href="https://www.star-history.com/#zed-industries/zed&Date"><img src="https://api.star-history.com/svg?repos=zed-industries/zed&type=Date" width="260" alt="zed-industries/zed 的星號歷史曲線"></a> |
| 2 | [astral-sh/uv](https://github.com/astral-sh/uv)<br>裝 Python 套件，不用再乾等<br>`開發者工具` | +329 | 47.0 | 91,429 | <a href="https://www.star-history.com/#astral-sh/uv&Date"><img src="https://api.star-history.com/svg?repos=astral-sh/uv&type=Date" width="260" alt="astral-sh/uv 的星號歷史曲線"></a> |
| 3 | [jdx/mise](https://github.com/jdx/mise)<br>開發工具、環境變數、任務，一個工具管<br>`開發者工具` | +275 | 39.3 | 35,620 | <a href="https://www.star-history.com/#jdx/mise&Date"><img src="https://api.star-history.com/svg?repos=jdx/mise&type=Date" width="260" alt="jdx/mise 的星號歷史曲線"></a> |
| 4 | [BurntSushi/ripgrep](https://github.com/BurntSushi/ripgrep)<br>翻遍整個目錄找文字，比 grep 快<br>`開發者工具` | +225 | 32.1 | 69,618 | <a href="https://www.star-history.com/#BurntSushi/ripgrep&Date"><img src="https://api.star-history.com/svg?repos=BurntSushi/ripgrep&type=Date" width="260" alt="BurntSushi/ripgrep 的星號歷史曲線"></a> |
| 5 | [oven-sh/bun](https://github.com/oven-sh/bun)<br>執行打包測試裝套件，一個工具全包<br>`開發者工具` | +148 | 21.1 | 96,498 | <a href="https://www.star-history.com/#oven-sh/bun&Date"><img src="https://api.star-history.com/svg?repos=oven-sh/bun&type=Date" width="260" alt="oven-sh/bun 的星號歷史曲線"></a> |
| 6 | [cli/cli](https://github.com/cli/cli)<br>不開網頁，命令列裡處理 GitHub<br>`開發者工具` | +112 | 16.0 | 46,837 | <a href="https://www.star-history.com/#cli/cli&Date"><img src="https://api.star-history.com/svg?repos=cli/cli&type=Date" width="260" alt="cli/cli 的星號歷史曲線"></a> |
| 7 | [helix-editor/helix](https://github.com/helix-editor/helix)<br>語法上色、語言服務都內建的文字編輯器<br>`開發者工具` | +106 | 15.1 | 46,761 | <a href="https://www.star-history.com/#helix-editor/helix&Date"><img src="https://api.star-history.com/svg?repos=helix-editor/helix&type=Date" width="260" alt="helix-editor/helix 的星號歷史曲線"></a> |
| 8 | [biomejs/biome](https://github.com/biomejs/biome)<br>網頁程式碼格式和檢查，一個工具搞定<br>`開發者工具` | +51 | 7.3 | 26,033 | <a href="https://www.star-history.com/#biomejs/biome&Date"><img src="https://api.star-history.com/svg?repos=biomejs/biome&type=Date" width="260" alt="biomejs/biome 的星號歷史曲線"></a> |

### 本月成長最快（近 30 天）

| # | 專案 | 新增星號 | 星號/天 | 總星號 | 星號歷史 |
|---|---|---:|---:|---:|---|
| 1 | [zed-industries/zed](https://github.com/zed-industries/zed)<br>開啟就快，還能多人一起寫程式碼<br>`開發者工具` | +1,571 | 52.4 | 92,496 | <a href="https://www.star-history.com/#zed-industries/zed&Date"><img src="https://api.star-history.com/svg?repos=zed-industries/zed&type=Date" width="260" alt="zed-industries/zed 的星號歷史曲線"></a> |
| 2 | [astral-sh/uv](https://github.com/astral-sh/uv)<br>裝 Python 套件，不用再乾等<br>`開發者工具` | +1,255 | 41.8 | 91,429 | <a href="https://www.star-history.com/#astral-sh/uv&Date"><img src="https://api.star-history.com/svg?repos=astral-sh/uv&type=Date" width="260" alt="astral-sh/uv 的星號歷史曲線"></a> |
| 3 | [jdx/mise](https://github.com/jdx/mise)<br>開發工具、環境變數、任務，一個工具管<br>`開發者工具` | +1,191 | 39.7 | 35,620 | <a href="https://www.star-history.com/#jdx/mise&Date"><img src="https://api.star-history.com/svg?repos=jdx/mise&type=Date" width="260" alt="jdx/mise 的星號歷史曲線"></a> |
| 4 | [BurntSushi/ripgrep](https://github.com/BurntSushi/ripgrep)<br>翻遍整個目錄找文字，比 grep 快<br>`開發者工具` | +974 | 32.5 | 69,618 | <a href="https://www.star-history.com/#BurntSushi/ripgrep&Date"><img src="https://api.star-history.com/svg?repos=BurntSushi/ripgrep&type=Date" width="260" alt="BurntSushi/ripgrep 的星號歷史曲線"></a> |
| 5 | [oven-sh/bun](https://github.com/oven-sh/bun)<br>執行打包測試裝套件，一個工具全包<br>`開發者工具` | +680 | 22.7 | 96,498 | <a href="https://www.star-history.com/#oven-sh/bun&Date"><img src="https://api.star-history.com/svg?repos=oven-sh/bun&type=Date" width="260" alt="oven-sh/bun 的星號歷史曲線"></a> |
| 6 | [helix-editor/helix](https://github.com/helix-editor/helix)<br>語法上色、語言服務都內建的文字編輯器<br>`開發者工具` | +451 | 15.0 | 46,761 | <a href="https://www.star-history.com/#helix-editor/helix&Date"><img src="https://api.star-history.com/svg?repos=helix-editor/helix&type=Date" width="260" alt="helix-editor/helix 的星號歷史曲線"></a> |
| 7 | [cli/cli](https://github.com/cli/cli)<br>不開網頁，命令列裡處理 GitHub<br>`開發者工具` | +427 | 14.2 | 46,837 | <a href="https://www.star-history.com/#cli/cli&Date"><img src="https://api.star-history.com/svg?repos=cli/cli&type=Date" width="260" alt="cli/cli 的星號歷史曲線"></a> |
| 8 | [biomejs/biome](https://github.com/biomejs/biome)<br>網頁程式碼格式和檢查，一個工具搞定<br>`開發者工具` | +210 | 7.0 | 26,033 | <a href="https://www.star-history.com/#biomejs/biome&Date"><img src="https://api.star-history.com/svg?repos=biomejs/biome&type=Date" width="260" alt="biomejs/biome 的星號歷史曲線"></a> |

### 今年成長最快（近 365 天）

| # | 專案 | 新增星號 | 星號/天 | 總星號 | 星號歷史 |
|---|---|---:|---:|---:|---|
| 1 | [zed-industries/zed](https://github.com/zed-industries/zed)<br>開啟就快，還能多人一起寫程式碼<br>`開發者工具` | +25,688 | 70.4 | 92,496 | <a href="https://www.star-history.com/#zed-industries/zed&Date"><img src="https://api.star-history.com/svg?repos=zed-industries/zed&type=Date" width="260" alt="zed-industries/zed 的星號歷史曲線"></a> |
| 2 | [astral-sh/uv](https://github.com/astral-sh/uv)<br>裝 Python 套件，不用再乾等<br>`開發者工具` | +21,322 | 58.4 | 91,429 | <a href="https://www.star-history.com/#astral-sh/uv&Date"><img src="https://api.star-history.com/svg?repos=astral-sh/uv&type=Date" width="260" alt="astral-sh/uv 的星號歷史曲線"></a> |
| 3 | [oven-sh/bun](https://github.com/oven-sh/bun)<br>執行打包測試裝套件，一個工具全包<br>`開發者工具` | +16,557 | 45.4 | 96,498 | <a href="https://www.star-history.com/#oven-sh/bun&Date"><img src="https://api.star-history.com/svg?repos=oven-sh/bun&type=Date" width="260" alt="oven-sh/bun 的星號歷史曲線"></a> |
| 4 | [jdx/mise](https://github.com/jdx/mise)<br>開發工具、環境變數、任務，一個工具管<br>`開發者工具` | +15,030 | 41.2 | 35,620 | <a href="https://www.star-history.com/#jdx/mise&Date"><img src="https://api.star-history.com/svg?repos=jdx/mise&type=Date" width="260" alt="jdx/mise 的星號歷史曲線"></a> |
| 5 | [BurntSushi/ripgrep](https://github.com/BurntSushi/ripgrep)<br>翻遍整個目錄找文字，比 grep 快<br>`開發者工具` | +13,341 | 36.6 | 69,618 | <a href="https://www.star-history.com/#BurntSushi/ripgrep&Date"><img src="https://api.star-history.com/svg?repos=BurntSushi/ripgrep&type=Date" width="260" alt="BurntSushi/ripgrep 的星號歷史曲線"></a> |
| 6 | [helix-editor/helix](https://github.com/helix-editor/helix)<br>語法上色、語言服務都內建的文字編輯器<br>`開發者工具` | +6,788 | 18.6 | 46,761 | <a href="https://www.star-history.com/#helix-editor/helix&Date"><img src="https://api.star-history.com/svg?repos=helix-editor/helix&type=Date" width="260" alt="helix-editor/helix 的星號歷史曲線"></a> |
| 7 | [cli/cli](https://github.com/cli/cli)<br>不開網頁，命令列裡處理 GitHub<br>`開發者工具` | +6,259 | 17.1 | 46,837 | <a href="https://www.star-history.com/#cli/cli&Date"><img src="https://api.star-history.com/svg?repos=cli/cli&type=Date" width="260" alt="cli/cli 的星號歷史曲線"></a> |
| 8 | [biomejs/biome](https://github.com/biomejs/biome)<br>網頁程式碼格式和檢查，一個工具搞定<br>`開發者工具` | +4,583 | 12.6 | 26,033 | <a href="https://www.star-history.com/#biomejs/biome&Date"><img src="https://api.star-history.com/svg?repos=biomejs/biome&type=Date" width="260" alt="biomejs/biome 的星號歷史曲線"></a> |

### 總星號數（歷史累計）

| # | 專案 | 總星號 | 星號歷史 |
|---|---|---:|---|
| 1 | [oven-sh/bun](https://github.com/oven-sh/bun)<br>執行打包測試裝套件，一個工具全包<br>`開發者工具` | 96,498 | <a href="https://www.star-history.com/#oven-sh/bun&Date"><img src="https://api.star-history.com/svg?repos=oven-sh/bun&type=Date" width="260" alt="oven-sh/bun 的星號歷史曲線"></a> |
| 2 | [zed-industries/zed](https://github.com/zed-industries/zed)<br>開啟就快，還能多人一起寫程式碼<br>`開發者工具` | 92,496 | <a href="https://www.star-history.com/#zed-industries/zed&Date"><img src="https://api.star-history.com/svg?repos=zed-industries/zed&type=Date" width="260" alt="zed-industries/zed 的星號歷史曲線"></a> |
| 3 | [astral-sh/uv](https://github.com/astral-sh/uv)<br>裝 Python 套件，不用再乾等<br>`開發者工具` | 91,429 | <a href="https://www.star-history.com/#astral-sh/uv&Date"><img src="https://api.star-history.com/svg?repos=astral-sh/uv&type=Date" width="260" alt="astral-sh/uv 的星號歷史曲線"></a> |
| 4 | [BurntSushi/ripgrep](https://github.com/BurntSushi/ripgrep)<br>翻遍整個目錄找文字，比 grep 快<br>`開發者工具` | 69,618 | <a href="https://www.star-history.com/#BurntSushi/ripgrep&Date"><img src="https://api.star-history.com/svg?repos=BurntSushi/ripgrep&type=Date" width="260" alt="BurntSushi/ripgrep 的星號歷史曲線"></a> |
| 5 | [cli/cli](https://github.com/cli/cli)<br>不開網頁，命令列裡處理 GitHub<br>`開發者工具` | 46,837 | <a href="https://www.star-history.com/#cli/cli&Date"><img src="https://api.star-history.com/svg?repos=cli/cli&type=Date" width="260" alt="cli/cli 的星號歷史曲線"></a> |
| 6 | [helix-editor/helix](https://github.com/helix-editor/helix)<br>語法上色、語言服務都內建的文字編輯器<br>`開發者工具` | 46,761 | <a href="https://www.star-history.com/#helix-editor/helix&Date"><img src="https://api.star-history.com/svg?repos=helix-editor/helix&type=Date" width="260" alt="helix-editor/helix 的星號歷史曲線"></a> |
| 7 | [jdx/mise](https://github.com/jdx/mise)<br>開發工具、環境變數、任務，一個工具管<br>`開發者工具` | 35,620 | <a href="https://www.star-history.com/#jdx/mise&Date"><img src="https://api.star-history.com/svg?repos=jdx/mise&type=Date" width="260" alt="jdx/mise 的星號歷史曲線"></a> |
| 8 | [biomejs/biome](https://github.com/biomejs/biome)<br>網頁程式碼格式和檢查，一個工具搞定<br>`開發者工具` | 26,033 | <a href="https://www.star-history.com/#biomejs/biome&Date"><img src="https://api.star-history.com/svg?repos=biomejs/biome&type=Date" width="260" alt="biomejs/biome 的星號歷史曲線"></a> |

## 資安

> 弱點掃描、靜態分析、供應鏈與執行時資安

### 最熱新儲存庫（近 7 天內建立）

| # | 專案 | 建立時間（UTC） | 總星號 | 星號/天 | 星號歷史 |
|---|---|---|---:|---:|---|
| 1 | [vaishantsah/watson-AI-osint-all-in-one](https://github.com/vaishantsah/watson-AI-osint-all-in-one)<br>暱稱郵箱電話，查遍 3,100 多個站點 | 2026-10-28<br><sub>4.8 天</sub> | 358 | 74.1 | <a href="https://www.star-history.com/#vaishantsah/watson-AI-osint-all-in-one&Date"><img src="https://api.star-history.com/svg?repos=vaishantsah/watson-AI-osint-all-in-one&type=Date" width="260" alt="vaishantsah/watson-AI-osint-all-in-one 的星號歷史曲線"></a> |

### 本週成長最快（近 7 天）

| # | 專案 | 新增星號 | 星號/天 | 總星號 | 星號歷史 |
|---|---|---:|---:|---:|---|
| 1 | [projectdiscovery/nuclei](https://github.com/projectdiscovery/nuclei)<br>寫個模板，就能批次掃漏洞<br>`資安` | +226 | 32.3 | 32,523 | <a href="https://www.star-history.com/#projectdiscovery/nuclei&Date"><img src="https://api.star-history.com/svg?repos=projectdiscovery/nuclei&type=Date" width="260" alt="projectdiscovery/nuclei 的星號歷史曲線"></a> |
| 2 | [aquasecurity/trivy](https://github.com/aquasecurity/trivy)<br>容器和程式碼倉，一次掃完安全問題<br>`資安` | +200 | 28.6 | 38,895 | <a href="https://www.star-history.com/#aquasecurity/trivy&Date"><img src="https://api.star-history.com/svg?repos=aquasecurity/trivy&type=Date" width="260" alt="aquasecurity/trivy 的星號歷史曲線"></a> |
| 3 | [semgrep/semgrep](https://github.com/semgrep/semgrep)<br>程式碼裡的問題，提交前先揪出來<br>`資安` | +131 | 18.7 | 17,398 | <a href="https://www.star-history.com/#semgrep/semgrep&Date"><img src="https://api.star-history.com/svg?repos=semgrep/semgrep&type=Date" width="260" alt="semgrep/semgrep 的星號歷史曲線"></a> |
| 4 | [OWASP/CheatSheetSeries](https://github.com/OWASP/CheatSheetSeries)<br>應用程式資安怎麼做，看這套速查表<br>`資安` | +99 | 14.1 | 33,834 | <a href="https://www.star-history.com/#OWASP/CheatSheetSeries&Date"><img src="https://api.star-history.com/svg?repos=OWASP/CheatSheetSeries&type=Date" width="260" alt="OWASP/CheatSheetSeries 的星號歷史曲線"></a> |
| 5 | [google/osv-scanner](https://github.com/google/osv-scanner)<br>用的依賴安不安全，掃一下就知道<br>`資安` | +81 | 11.6 | 11,346 | <a href="https://www.star-history.com/#google/osv-scanner&Date"><img src="https://api.star-history.com/svg?repos=google/osv-scanner&type=Date" width="260" alt="google/osv-scanner 的星號歷史曲線"></a> |
| 6 | [anchore/grype](https://github.com/anchore/grype)<br>容器映像檔有沒有漏洞，掃一下就知道<br>`資安` | +52 | 7.4 | 13,154 | <a href="https://www.star-history.com/#anchore/grype&Date"><img src="https://api.star-history.com/svg?repos=anchore/grype&type=Date" width="260" alt="anchore/grype 的星號歷史曲線"></a> |
| 7 | [falcosecurity/falco](https://github.com/falcosecurity/falco)<br>雲上有異常，第一時間知道<br>`資安` | +29 | 4.1 | 9,544 | <a href="https://www.star-history.com/#falcosecurity/falco&Date"><img src="https://api.star-history.com/svg?repos=falcosecurity/falco&type=Date" width="260" alt="falcosecurity/falco 的星號歷史曲線"></a> |
| 8 | [securego/gosec](https://github.com/securego/gosec)<br>Go 程式碼的資安隱患，掃一遍就知道<br>`資安` | +11 | 1.6 | 8,995 | <a href="https://www.star-history.com/#securego/gosec&Date"><img src="https://api.star-history.com/svg?repos=securego/gosec&type=Date" width="260" alt="securego/gosec 的星號歷史曲線"></a> |

### 本月成長最快（近 30 天）

| # | 專案 | 新增星號 | 星號/天 | 總星號 | 星號歷史 |
|---|---|---:|---:|---:|---|
| 1 | [projectdiscovery/nuclei](https://github.com/projectdiscovery/nuclei)<br>寫個模板，就能批次掃漏洞<br>`資安` | +914 | 30.5 | 32,523 | <a href="https://www.star-history.com/#projectdiscovery/nuclei&Date"><img src="https://api.star-history.com/svg?repos=projectdiscovery/nuclei&type=Date" width="260" alt="projectdiscovery/nuclei 的星號歷史曲線"></a> |
| 2 | [aquasecurity/trivy](https://github.com/aquasecurity/trivy)<br>容器和程式碼倉，一次掃完安全問題<br>`資安` | +769 | 25.6 | 38,895 | <a href="https://www.star-history.com/#aquasecurity/trivy&Date"><img src="https://api.star-history.com/svg?repos=aquasecurity/trivy&type=Date" width="260" alt="aquasecurity/trivy 的星號歷史曲線"></a> |
| 3 | [semgrep/semgrep](https://github.com/semgrep/semgrep)<br>程式碼裡的問題，提交前先揪出來<br>`資安` | +578 | 19.3 | 17,398 | <a href="https://www.star-history.com/#semgrep/semgrep&Date"><img src="https://api.star-history.com/svg?repos=semgrep/semgrep&type=Date" width="260" alt="semgrep/semgrep 的星號歷史曲線"></a> |
| 4 | [OWASP/CheatSheetSeries](https://github.com/OWASP/CheatSheetSeries)<br>應用程式資安怎麼做，看這套速查表<br>`資安` | +480 | 16.0 | 33,834 | <a href="https://www.star-history.com/#OWASP/CheatSheetSeries&Date"><img src="https://api.star-history.com/svg?repos=OWASP/CheatSheetSeries&type=Date" width="260" alt="OWASP/CheatSheetSeries 的星號歷史曲線"></a> |
| 5 | [google/osv-scanner](https://github.com/google/osv-scanner)<br>用的依賴安不安全，掃一下就知道<br>`資安` | +233 | 7.8 | 11,346 | <a href="https://www.star-history.com/#google/osv-scanner&Date"><img src="https://api.star-history.com/svg?repos=google/osv-scanner&type=Date" width="260" alt="google/osv-scanner 的星號歷史曲線"></a> |
| 6 | [anchore/grype](https://github.com/anchore/grype)<br>容器映像檔有沒有漏洞，掃一下就知道<br>`資安` | +201 | 6.7 | 13,154 | <a href="https://www.star-history.com/#anchore/grype&Date"><img src="https://api.star-history.com/svg?repos=anchore/grype&type=Date" width="260" alt="anchore/grype 的星號歷史曲線"></a> |
| 7 | [falcosecurity/falco](https://github.com/falcosecurity/falco)<br>雲上有異常，第一時間知道<br>`資安` | +123 | 4.1 | 9,544 | <a href="https://www.star-history.com/#falcosecurity/falco&Date"><img src="https://api.star-history.com/svg?repos=falcosecurity/falco&type=Date" width="260" alt="falcosecurity/falco 的星號歷史曲線"></a> |
| 8 | [securego/gosec](https://github.com/securego/gosec)<br>Go 程式碼的資安隱患，掃一遍就知道<br>`資安` | +42 | 1.4 | 8,995 | <a href="https://www.star-history.com/#securego/gosec&Date"><img src="https://api.star-history.com/svg?repos=securego/gosec&type=Date" width="260" alt="securego/gosec 的星號歷史曲線"></a> |

### 今年成長最快（近 365 天）

| # | 專案 | 新增星號 | 星號/天 | 總星號 | 星號歷史 |
|---|---|---:|---:|---:|---|
| 1 | [aquasecurity/trivy](https://github.com/aquasecurity/trivy)<br>容器和程式碼倉，一次掃完安全問題<br>`資安` | +10,097 | 27.7 | 38,895 | <a href="https://www.star-history.com/#aquasecurity/trivy&Date"><img src="https://api.star-history.com/svg?repos=aquasecurity/trivy&type=Date" width="260" alt="aquasecurity/trivy 的星號歷史曲線"></a> |
| 2 | [projectdiscovery/nuclei](https://github.com/projectdiscovery/nuclei)<br>寫個模板，就能批次掃漏洞<br>`資安` | +7,601 | 20.8 | 32,523 | <a href="https://www.star-history.com/#projectdiscovery/nuclei&Date"><img src="https://api.star-history.com/svg?repos=projectdiscovery/nuclei&type=Date" width="260" alt="projectdiscovery/nuclei 的星號歷史曲線"></a> |
| 3 | [semgrep/semgrep](https://github.com/semgrep/semgrep)<br>程式碼裡的問題，提交前先揪出來<br>`資安` | +4,364 | 12.0 | 17,398 | <a href="https://www.star-history.com/#semgrep/semgrep&Date"><img src="https://api.star-history.com/svg?repos=semgrep/semgrep&type=Date" width="260" alt="semgrep/semgrep 的星號歷史曲線"></a> |
| 4 | [OWASP/CheatSheetSeries](https://github.com/OWASP/CheatSheetSeries)<br>應用程式資安怎麼做，看這套速查表<br>`資安` | +3,512 | 9.6 | 33,834 | <a href="https://www.star-history.com/#OWASP/CheatSheetSeries&Date"><img src="https://api.star-history.com/svg?repos=OWASP/CheatSheetSeries&type=Date" width="260" alt="OWASP/CheatSheetSeries 的星號歷史曲線"></a> |
| 5 | [google/osv-scanner](https://github.com/google/osv-scanner)<br>用的依賴安不安全，掃一下就知道<br>`資安` | +3,480 | 9.5 | 11,346 | <a href="https://www.star-history.com/#google/osv-scanner&Date"><img src="https://api.star-history.com/svg?repos=google/osv-scanner&type=Date" width="260" alt="google/osv-scanner 的星號歷史曲線"></a> |
| 6 | [anchore/grype](https://github.com/anchore/grype)<br>容器映像檔有沒有漏洞，掃一下就知道<br>`資安` | +2,359 | 6.5 | 13,154 | <a href="https://www.star-history.com/#anchore/grype&Date"><img src="https://api.star-history.com/svg?repos=anchore/grype&type=Date" width="260" alt="anchore/grype 的星號歷史曲線"></a> |
| 7 | [falcosecurity/falco](https://github.com/falcosecurity/falco)<br>雲上有異常，第一時間知道<br>`資安` | +1,270 | 3.5 | 9,544 | <a href="https://www.star-history.com/#falcosecurity/falco&Date"><img src="https://api.star-history.com/svg?repos=falcosecurity/falco&type=Date" width="260" alt="falcosecurity/falco 的星號歷史曲線"></a> |
| 8 | [securego/gosec](https://github.com/securego/gosec)<br>Go 程式碼的資安隱患，掃一遍就知道<br>`資安` | +560 | 1.5 | 8,995 | <a href="https://www.star-history.com/#securego/gosec&Date"><img src="https://api.star-history.com/svg?repos=securego/gosec&type=Date" width="260" alt="securego/gosec 的星號歷史曲線"></a> |

### 總星號數（歷史累計）

| # | 專案 | 總星號 | 星號歷史 |
|---|---|---:|---|
| 1 | [aquasecurity/trivy](https://github.com/aquasecurity/trivy)<br>容器和程式碼倉，一次掃完安全問題<br>`資安` | 38,895 | <a href="https://www.star-history.com/#aquasecurity/trivy&Date"><img src="https://api.star-history.com/svg?repos=aquasecurity/trivy&type=Date" width="260" alt="aquasecurity/trivy 的星號歷史曲線"></a> |
| 2 | [OWASP/CheatSheetSeries](https://github.com/OWASP/CheatSheetSeries)<br>應用程式資安怎麼做，看這套速查表<br>`資安` | 33,834 | <a href="https://www.star-history.com/#OWASP/CheatSheetSeries&Date"><img src="https://api.star-history.com/svg?repos=OWASP/CheatSheetSeries&type=Date" width="260" alt="OWASP/CheatSheetSeries 的星號歷史曲線"></a> |
| 3 | [projectdiscovery/nuclei](https://github.com/projectdiscovery/nuclei)<br>寫個模板，就能批次掃漏洞<br>`資安` | 32,523 | <a href="https://www.star-history.com/#projectdiscovery/nuclei&Date"><img src="https://api.star-history.com/svg?repos=projectdiscovery/nuclei&type=Date" width="260" alt="projectdiscovery/nuclei 的星號歷史曲線"></a> |
| 4 | [semgrep/semgrep](https://github.com/semgrep/semgrep)<br>程式碼裡的問題，提交前先揪出來<br>`資安` | 17,398 | <a href="https://www.star-history.com/#semgrep/semgrep&Date"><img src="https://api.star-history.com/svg?repos=semgrep/semgrep&type=Date" width="260" alt="semgrep/semgrep 的星號歷史曲線"></a> |
| 5 | [anchore/grype](https://github.com/anchore/grype)<br>容器映像檔有沒有漏洞，掃一下就知道<br>`資安` | 13,154 | <a href="https://www.star-history.com/#anchore/grype&Date"><img src="https://api.star-history.com/svg?repos=anchore/grype&type=Date" width="260" alt="anchore/grype 的星號歷史曲線"></a> |
| 6 | [google/osv-scanner](https://github.com/google/osv-scanner)<br>用的依賴安不安全，掃一下就知道<br>`資安` | 11,346 | <a href="https://www.star-history.com/#google/osv-scanner&Date"><img src="https://api.star-history.com/svg?repos=google/osv-scanner&type=Date" width="260" alt="google/osv-scanner 的星號歷史曲線"></a> |
| 7 | [falcosecurity/falco](https://github.com/falcosecurity/falco)<br>雲上有異常，第一時間知道<br>`資安` | 9,544 | <a href="https://www.star-history.com/#falcosecurity/falco&Date"><img src="https://api.star-history.com/svg?repos=falcosecurity/falco&type=Date" width="260" alt="falcosecurity/falco 的星號歷史曲線"></a> |
| 8 | [securego/gosec](https://github.com/securego/gosec)<br>Go 程式碼的資安隱患，掃一遍就知道<br>`資安` | 8,995 | <a href="https://www.star-history.com/#securego/gosec&Date"><img src="https://api.star-history.com/svg?repos=securego/gosec&type=Date" width="260" alt="securego/gosec 的星號歷史曲線"></a> |

## Web / 前端

> 前端框架、UI 元件庫、CSS 與瀏覽器工具

### 最熱新儲存庫（近 7 天內建立）

| # | 專案 | 建立時間（UTC） | 總星號 | 星號/天 | 星號歷史 |
|---|---|---|---:|---:|---|
| 1 | [D3voz/openjutsu](https://github.com/D3voz/openjutsu)<br>影片換角色，一鍵在本機完成 | 2026-10-26<br><sub>6.3 天</sub> | 1,024 | 163.5 | <a href="https://www.star-history.com/#D3voz/openjutsu&Date"><img src="https://api.star-history.com/svg?repos=D3voz/openjutsu&type=Date" width="260" alt="D3voz/openjutsu 的星號歷史曲線"></a> |
| 2 | [Lavagroabide/aegis-spreadwatch](https://github.com/Lavagroabide/aegis-spreadwatch)<br>Aegis SpreadWatch: 讓 CS2 買賣機會清晰可見——每個交易場所的淨利潤、ROI 和費用假設，均在裝置端計算。 | 2026-10-30<br><sub>1.9 天</sub> | 138 | 74.3 | <a href="https://www.star-history.com/#Lavagroabide/aegis-spreadwatch&Date"><img src="https://api.star-history.com/svg?repos=Lavagroabide/aegis-spreadwatch&type=Date" width="260" alt="Lavagroabide/aegis-spreadwatch 的星號歷史曲線"></a> |
| 3 | [Moh4696/open-3d-skills](https://github.com/Moh4696/open-3d-skills)<br>Eight agent skills for 3D and animated websites: three.js scenes from code, scroll films, transparent video, cursor rigs, exploded views, AI motion assets, bro… | 2026-10-31<br><sub>1.5 天</sub> | 107 | 72.6 | <a href="https://www.star-history.com/#Moh4696/open-3d-skills&Date"><img src="https://api.star-history.com/svg?repos=Moh4696/open-3d-skills&type=Date" width="260" alt="Moh4696/open-3d-skills 的星號歷史曲線"></a> |
| 4 | [solderdatabraid29/aegis-vaultgrid](https://github.com/solderdatabraid29/aegis-vaultgrid)<br>Aegis VaultGrid: 將 CS2 庫存保險庫與感知費用的訂單規劃器相結合。本機 JSON 狀態，無需帳戶即可瀏覽。 | 2026-10-30<br><sub>1.9 天</sub> | 131 | 70.6 | <a href="https://www.star-history.com/#solderdatabraid29/aegis-vaultgrid&Date"><img src="https://api.star-history.com/svg?repos=solderdatabraid29/aegis-vaultgrid&type=Date" width="260" alt="solderdatabraid29/aegis-vaultgrid 的星號歷史曲線"></a> |
| 5 | [Townlanurture/aegis-skin-terminal](https://github.com/Townlanurture/aegis-skin-terminal)<br>Aegis Skin Terminal: 本機優先的 CS2 交易工作區，配備感知費用的價差掃描器、保險庫工作區和離線 Steam Guard 代碼。 | 2026-10-30<br><sub>1.9 天</sub> | 117 | 62.8 | <a href="https://www.star-history.com/#Townlanurture/aegis-skin-terminal&Date"><img src="https://api.star-history.com/svg?repos=Townlanurture/aegis-skin-terminal&type=Date" width="260" alt="Townlanurture/aegis-skin-terminal 的星號歷史曲線"></a> |
| 6 | [Forward-Future/folio](https://github.com/Forward-Future/folio)<br>Folio — 一款適用於 Windows 的簡單、簡潔的開源 PDF 閱讀器 | 2026-10-26<br><sub>6.0 天</sub> | 253 | 42.4 | <a href="https://www.star-history.com/#Forward-Future/folio&Date"><img src="https://api.star-history.com/svg?repos=Forward-Future/folio&type=Date" width="260" alt="Forward-Future/folio 的星號歷史曲線"></a> |
| 7 | [zklmiao/prompt-vault](https://github.com/zklmiao/prompt-vault)<br>提示詞到處亂放？在桌面本機統一收藏 | 2026-10-28<br><sub>4.7 天</sub> | 187 | 40.1 | <a href="https://www.star-history.com/#zklmiao/prompt-vault&Date"><img src="https://api.star-history.com/svg?repos=zklmiao/prompt-vault&type=Date" width="260" alt="zklmiao/prompt-vault 的星號歷史曲線"></a> |
| 8 | [jianxinss/iching-64-motion](https://github.com/jianxinss/iching-64-motion)<br>六十四卦做成動畫，全靠程式碼 | 2026-10-27<br><sub>5.8 天</sub> | 161 | 27.9 | <a href="https://www.star-history.com/#jianxinss/iching-64-motion&Date"><img src="https://api.star-history.com/svg?repos=jianxinss/iching-64-motion&type=Date" width="260" alt="jianxinss/iching-64-motion 的星號歷史曲線"></a> |
| 9 | [floatboatai/OpenMinutes](https://github.com/floatboatai/OpenMinutes)<br>錄音筆的錄音，轉成能搜的文字 | 2026-10-28<br><sub>4.3 天</sub> | 108 | 25.1 | <a href="https://www.star-history.com/#floatboatai/OpenMinutes&Date"><img src="https://api.star-history.com/svg?repos=floatboatai/OpenMinutes&type=Date" width="260" alt="floatboatai/OpenMinutes 的星號歷史曲線"></a> |

### 本週成長最快（近 7 天）

| # | 專案 | 新增星號 | 星號/天 | 總星號 | 星號歷史 |
|---|---|---:|---:|---:|---|
| 1 | [shadcn-ui/ui](https://github.com/shadcn-ui/ui)<br>好看的元件，程式碼歸你，隨便改<br>`Web / 前端` | +675 | 96.4 | 127,115 | <a href="https://www.star-history.com/#shadcn-ui/ui&Date"><img src="https://api.star-history.com/svg?repos=shadcn-ui/ui&type=Date" width="260" alt="shadcn-ui/ui 的星號歷史曲線"></a> |
| 2 | [facebook/react](https://github.com/facebook/react)<br>網頁和 App 介面，都能用它來搭<br>`Web / 前端` | +580 | 82.9 | 252,066 | <a href="https://www.star-history.com/#facebook/react&Date"><img src="https://api.star-history.com/svg?repos=facebook/react&type=Date" width="260" alt="facebook/react 的星號歷史曲線"></a> |
| 3 | [vercel/next.js](https://github.com/vercel/next.js)<br>用 React 做完整網站，從前到後<br>`Web / 前端` | +402 | 57.4 | 143,460 | <a href="https://www.star-history.com/#vercel/next.js&Date"><img src="https://api.star-history.com/svg?repos=vercel/next.js&type=Date" width="260" alt="vercel/next.js 的星號歷史曲線"></a> |
| 4 | [tailwindlabs/tailwindcss](https://github.com/tailwindlabs/tailwindcss)<br>不寫一大堆 CSS，也能做定製介面<br>`Web / 前端` | +344 | 49.1 | 98,277 | <a href="https://www.star-history.com/#tailwindlabs/tailwindcss&Date"><img src="https://api.star-history.com/svg?repos=tailwindlabs/tailwindcss&type=Date" width="260" alt="tailwindlabs/tailwindcss 的星號歷史曲線"></a> |
| 5 | [vuejs/core](https://github.com/vuejs/core)<br>從一個小頁面開始，用多少學多少<br>`Web / 前端` | +297 | 42.4 | 55,022 | <a href="https://www.star-history.com/#vuejs/core&Date"><img src="https://api.star-history.com/svg?repos=vuejs/core&type=Date" width="260" alt="vuejs/core 的星號歷史曲線"></a> |
| 6 | [withastro/astro](https://github.com/withastro/astro)<br>做內容型網站，頁面輸出更輕量<br>`Web / 前端` | +199 | 28.4 | 63,649 | <a href="https://www.star-history.com/#withastro/astro&Date"><img src="https://api.star-history.com/svg?repos=withastro/astro&type=Date" width="260" alt="withastro/astro 的星號歷史曲線"></a> |
| 7 | [sveltejs/svelte](https://github.com/sveltejs/svelte)<br>你寫元件，編譯器變出高效的網頁程式碼<br>`Web / 前端` | +115 | 16.4 | 88,520 | <a href="https://www.star-history.com/#sveltejs/svelte&Date"><img src="https://api.star-history.com/svg?repos=sveltejs/svelte&type=Date" width="260" alt="sveltejs/svelte 的星號歷史曲線"></a> |
| 8 | [tanstack/query](https://github.com/tanstack/query)<br>請求資料和快取，交給它管<br>`Web / 前端` | +44 | 6.3 | 50,515 | <a href="https://www.star-history.com/#tanstack/query&Date"><img src="https://api.star-history.com/svg?repos=tanstack/query&type=Date" width="260" alt="tanstack/query 的星號歷史曲線"></a> |

### 本月成長最快（近 30 天）

| # | 專案 | 新增星號 | 星號/天 | 總星號 | 星號歷史 |
|---|---|---:|---:|---:|---|
| 1 | [shadcn-ui/ui](https://github.com/shadcn-ui/ui)<br>好看的元件，程式碼歸你，隨便改<br>`Web / 前端` | +2,595 | 86.5 | 127,115 | <a href="https://www.star-history.com/#shadcn-ui/ui&Date"><img src="https://api.star-history.com/svg?repos=shadcn-ui/ui&type=Date" width="260" alt="shadcn-ui/ui 的星號歷史曲線"></a> |
| 2 | [facebook/react](https://github.com/facebook/react)<br>網頁和 App 介面，都能用它來搭<br>`Web / 前端` | +1,852 | 61.7 | 252,066 | <a href="https://www.star-history.com/#facebook/react&Date"><img src="https://api.star-history.com/svg?repos=facebook/react&type=Date" width="260" alt="facebook/react 的星號歷史曲線"></a> |
| 3 | [vercel/next.js](https://github.com/vercel/next.js)<br>用 React 做完整網站，從前到後<br>`Web / 前端` | +1,018 | 33.9 | 143,460 | <a href="https://www.star-history.com/#vercel/next.js&Date"><img src="https://api.star-history.com/svg?repos=vercel/next.js&type=Date" width="260" alt="vercel/next.js 的星號歷史曲線"></a> |
| 4 | [withastro/astro](https://github.com/withastro/astro)<br>做內容型網站，頁面輸出更輕量<br>`Web / 前端` | +767 | 25.6 | 63,649 | <a href="https://www.star-history.com/#withastro/astro&Date"><img src="https://api.star-history.com/svg?repos=withastro/astro&type=Date" width="260" alt="withastro/astro 的星號歷史曲線"></a> |
| 5 | [tailwindlabs/tailwindcss](https://github.com/tailwindlabs/tailwindcss)<br>不寫一大堆 CSS，也能做定製介面<br>`Web / 前端` | +720 | 24.0 | 98,277 | <a href="https://www.star-history.com/#tailwindlabs/tailwindcss&Date"><img src="https://api.star-history.com/svg?repos=tailwindlabs/tailwindcss&type=Date" width="260" alt="tailwindlabs/tailwindcss 的星號歷史曲線"></a> |
| 6 | [vuejs/core](https://github.com/vuejs/core)<br>從一個小頁面開始，用多少學多少<br>`Web / 前端` | +622 | 20.7 | 55,022 | <a href="https://www.star-history.com/#vuejs/core&Date"><img src="https://api.star-history.com/svg?repos=vuejs/core&type=Date" width="260" alt="vuejs/core 的星號歷史曲線"></a> |
| 7 | [sveltejs/svelte](https://github.com/sveltejs/svelte)<br>你寫元件，編譯器變出高效的網頁程式碼<br>`Web / 前端` | +482 | 16.1 | 88,520 | <a href="https://www.star-history.com/#sveltejs/svelte&Date"><img src="https://api.star-history.com/svg?repos=sveltejs/svelte&type=Date" width="260" alt="sveltejs/svelte 的星號歷史曲線"></a> |
| 8 | [tanstack/query](https://github.com/tanstack/query)<br>請求資料和快取，交給它管<br>`Web / 前端` | +206 | 6.9 | 50,515 | <a href="https://www.star-history.com/#tanstack/query&Date"><img src="https://api.star-history.com/svg?repos=tanstack/query&type=Date" width="260" alt="tanstack/query 的星號歷史曲線"></a> |

### 今年成長最快（近 365 天）

| # | 專案 | 新增星號 | 星號/天 | 總星號 | 星號歷史 |
|---|---|---:|---:|---:|---|
| 1 | [shadcn-ui/ui](https://github.com/shadcn-ui/ui)<br>好看的元件，程式碼歸你，隨便改<br>`Web / 前端` | +30,316 | 83.1 | 127,115 | <a href="https://www.star-history.com/#shadcn-ui/ui&Date"><img src="https://api.star-history.com/svg?repos=shadcn-ui/ui&type=Date" width="260" alt="shadcn-ui/ui 的星號歷史曲線"></a> |
| 2 | [facebook/react](https://github.com/facebook/react)<br>網頁和 App 介面，都能用它來搭<br>`Web / 前端` | +15,415 | 42.2 | 252,066 | <a href="https://www.star-history.com/#facebook/react&Date"><img src="https://api.star-history.com/svg?repos=facebook/react&type=Date" width="260" alt="facebook/react 的星號歷史曲線"></a> |
| 3 | [vercel/next.js](https://github.com/vercel/next.js)<br>用 React 做完整網站，從前到後<br>`Web / 前端` | +10,573 | 29.0 | 143,460 | <a href="https://www.star-history.com/#vercel/next.js&Date"><img src="https://api.star-history.com/svg?repos=vercel/next.js&type=Date" width="260" alt="vercel/next.js 的星號歷史曲線"></a> |
| 4 | [withastro/astro](https://github.com/withastro/astro)<br>做內容型網站，頁面輸出更輕量<br>`Web / 前端` | +10,482 | 28.7 | 63,649 | <a href="https://www.star-history.com/#withastro/astro&Date"><img src="https://api.star-history.com/svg?repos=withastro/astro&type=Date" width="260" alt="withastro/astro 的星號歷史曲線"></a> |
| 5 | [tailwindlabs/tailwindcss](https://github.com/tailwindlabs/tailwindcss)<br>不寫一大堆 CSS，也能做定製介面<br>`Web / 前端` | +8,764 | 24.0 | 98,277 | <a href="https://www.star-history.com/#tailwindlabs/tailwindcss&Date"><img src="https://api.star-history.com/svg?repos=tailwindlabs/tailwindcss&type=Date" width="260" alt="tailwindlabs/tailwindcss 的星號歷史曲線"></a> |
| 6 | [sveltejs/svelte](https://github.com/sveltejs/svelte)<br>你寫元件，編譯器變出高效的網頁程式碼<br>`Web / 前端` | +5,265 | 14.4 | 88,520 | <a href="https://www.star-history.com/#sveltejs/svelte&Date"><img src="https://api.star-history.com/svg?repos=sveltejs/svelte&type=Date" width="260" alt="sveltejs/svelte 的星號歷史曲線"></a> |
| 7 | [tanstack/query](https://github.com/tanstack/query)<br>請求資料和快取，交給它管<br>`Web / 前端` | +3,856 | 10.6 | 50,515 | <a href="https://www.star-history.com/#tanstack/query&Date"><img src="https://api.star-history.com/svg?repos=tanstack/query&type=Date" width="260" alt="tanstack/query 的星號歷史曲線"></a> |
| 8 | [vuejs/core](https://github.com/vuejs/core)<br>從一個小頁面開始，用多少學多少<br>`Web / 前端` | +3,834 | 10.5 | 55,022 | <a href="https://www.star-history.com/#vuejs/core&Date"><img src="https://api.star-history.com/svg?repos=vuejs/core&type=Date" width="260" alt="vuejs/core 的星號歷史曲線"></a> |

### 總星號數（歷史累計）

| # | 專案 | 總星號 | 星號歷史 |
|---|---|---:|---|
| 1 | [facebook/react](https://github.com/facebook/react)<br>網頁和 App 介面，都能用它來搭<br>`Web / 前端` | 252,066 | <a href="https://www.star-history.com/#facebook/react&Date"><img src="https://api.star-history.com/svg?repos=facebook/react&type=Date" width="260" alt="facebook/react 的星號歷史曲線"></a> |
| 2 | [vercel/next.js](https://github.com/vercel/next.js)<br>用 React 做完整網站，從前到後<br>`Web / 前端` | 143,460 | <a href="https://www.star-history.com/#vercel/next.js&Date"><img src="https://api.star-history.com/svg?repos=vercel/next.js&type=Date" width="260" alt="vercel/next.js 的星號歷史曲線"></a> |
| 3 | [shadcn-ui/ui](https://github.com/shadcn-ui/ui)<br>好看的元件，程式碼歸你，隨便改<br>`Web / 前端` | 127,115 | <a href="https://www.star-history.com/#shadcn-ui/ui&Date"><img src="https://api.star-history.com/svg?repos=shadcn-ui/ui&type=Date" width="260" alt="shadcn-ui/ui 的星號歷史曲線"></a> |
| 4 | [tailwindlabs/tailwindcss](https://github.com/tailwindlabs/tailwindcss)<br>不寫一大堆 CSS，也能做定製介面<br>`Web / 前端` | 98,277 | <a href="https://www.star-history.com/#tailwindlabs/tailwindcss&Date"><img src="https://api.star-history.com/svg?repos=tailwindlabs/tailwindcss&type=Date" width="260" alt="tailwindlabs/tailwindcss 的星號歷史曲線"></a> |
| 5 | [sveltejs/svelte](https://github.com/sveltejs/svelte)<br>你寫元件，編譯器變出高效的網頁程式碼<br>`Web / 前端` | 88,520 | <a href="https://www.star-history.com/#sveltejs/svelte&Date"><img src="https://api.star-history.com/svg?repos=sveltejs/svelte&type=Date" width="260" alt="sveltejs/svelte 的星號歷史曲線"></a> |
| 6 | [withastro/astro](https://github.com/withastro/astro)<br>做內容型網站，頁面輸出更輕量<br>`Web / 前端` | 63,649 | <a href="https://www.star-history.com/#withastro/astro&Date"><img src="https://api.star-history.com/svg?repos=withastro/astro&type=Date" width="260" alt="withastro/astro 的星號歷史曲線"></a> |
| 7 | [vuejs/core](https://github.com/vuejs/core)<br>從一個小頁面開始，用多少學多少<br>`Web / 前端` | 55,022 | <a href="https://www.star-history.com/#vuejs/core&Date"><img src="https://api.star-history.com/svg?repos=vuejs/core&type=Date" width="260" alt="vuejs/core 的星號歷史曲線"></a> |
| 8 | [tanstack/query](https://github.com/tanstack/query)<br>請求資料和快取，交給它管<br>`Web / 前端` | 50,515 | <a href="https://www.star-history.com/#tanstack/query&Date"><img src="https://api.star-history.com/svg?repos=tanstack/query&type=Date" width="260" alt="tanstack/query 的星號歷史曲線"></a> |

## 基礎建設

> 容器、Kubernetes、雲端、網路與可觀測性

### 最熱新儲存庫（近 7 天內建立）

| # | 專案 | 建立時間（UTC） | 總星號 | 星號/天 | 星號歷史 |
|---|---|---|---:|---:|---|
| 1 | [davemessew/AgentFlux](https://github.com/davemessew/AgentFlux)<br>畫出 AI 工作流程，在自己電腦上跑 | 2026-10-27<br><sub>5.2 天</sub> | 236 | 45.2 | <a href="https://www.star-history.com/#davemessew/AgentFlux&Date"><img src="https://api.star-history.com/svg?repos=davemessew/AgentFlux&type=Date" width="260" alt="davemessew/AgentFlux 的星號歷史曲線"></a> |

### 本週成長最快（近 7 天）

| # | 專案 | 新增星號 | 星號/天 | 總星號 | 星號歷史 |
|---|---|---:|---:|---:|---|
| 1 | [kubernetes/kubernetes](https://github.com/kubernetes/kubernetes)<br>容器多了，部署擴容交給它<br>`基礎建設` | +444 | 63.4 | 128,809 | <a href="https://www.star-history.com/#kubernetes/kubernetes&Date"><img src="https://api.star-history.com/svg?repos=kubernetes/kubernetes&type=Date" width="260" alt="kubernetes/kubernetes 的星號歷史曲線"></a> |
| 2 | [hashicorp/terraform](https://github.com/hashicorp/terraform)<br>雲資源寫成程式碼，可審閱、可版本管理<br>`基礎建設` | +339 | 48.4 | 50,340 | <a href="https://www.star-history.com/#hashicorp/terraform&Date"><img src="https://api.star-history.com/svg?repos=hashicorp/terraform&type=Date" width="260" alt="hashicorp/terraform 的星號歷史曲線"></a> |
| 3 | [caddyserver/caddy](https://github.com/caddyserver/caddy)<br>搭網站伺服器，HTTPS 自動配好<br>`基礎建設` | +277 | 39.6 | 78,623 | <a href="https://www.star-history.com/#caddyserver/caddy&Date"><img src="https://api.star-history.com/svg?repos=caddyserver/caddy&type=Date" width="260" alt="caddyserver/caddy 的星號歷史曲線"></a> |
| 4 | [grafana/grafana](https://github.com/grafana/grafana)<br>指標日誌追蹤，放進一個面板<br>`基礎建設` | +174 | 24.9 | 77,615 | <a href="https://www.star-history.com/#grafana/grafana&Date"><img src="https://api.star-history.com/svg?repos=grafana/grafana&type=Date" width="260" alt="grafana/grafana 的星號歷史曲線"></a> |
| 5 | [prometheus/prometheus](https://github.com/prometheus/prometheus)<br>系統出問題，告警先找到你<br>`基礎建設` | +172 | 24.6 | 66,893 | <a href="https://www.star-history.com/#prometheus/prometheus&Date"><img src="https://api.star-history.com/svg?repos=prometheus/prometheus&type=Date" width="260" alt="prometheus/prometheus 的星號歷史曲線"></a> |
| 6 | [docker/compose](https://github.com/docker/compose)<br>多個容器寫進一個檔案，一起跑<br>`基礎建設` | +116 | 16.6 | 38,558 | <a href="https://www.star-history.com/#docker/compose&Date"><img src="https://api.star-history.com/svg?repos=docker/compose&type=Date" width="260" alt="docker/compose 的星號歷史曲線"></a> |
| 7 | [traefik/traefik](https://github.com/traefik/traefik)<br>服務多了，流量自動分好<br>`基礎建設` | +95 | 13.6 | 65,428 | <a href="https://www.star-history.com/#traefik/traefik&Date"><img src="https://api.star-history.com/svg?repos=traefik/traefik&type=Date" width="260" alt="traefik/traefik 的星號歷史曲線"></a> |
| 8 | [pulumi/pulumi](https://github.com/pulumi/pulumi)<br>用熟悉的程式語言管雲資源<br>`基礎建設` | +29 | 4.1 | 25,838 | <a href="https://www.star-history.com/#pulumi/pulumi&Date"><img src="https://api.star-history.com/svg?repos=pulumi/pulumi&type=Date" width="260" alt="pulumi/pulumi 的星號歷史曲線"></a> |

### 本月成長最快（近 30 天）

| # | 專案 | 新增星號 | 星號/天 | 總星號 | 星號歷史 |
|---|---|---:|---:|---:|---|
| 1 | [caddyserver/caddy](https://github.com/caddyserver/caddy)<br>搭網站伺服器，HTTPS 自動配好<br>`基礎建設` | +2,510 | 83.7 | 78,623 | <a href="https://www.star-history.com/#caddyserver/caddy&Date"><img src="https://api.star-history.com/svg?repos=caddyserver/caddy&type=Date" width="260" alt="caddyserver/caddy 的星號歷史曲線"></a> |
| 2 | [kubernetes/kubernetes](https://github.com/kubernetes/kubernetes)<br>容器多了，部署擴容交給它<br>`基礎建設` | +1,119 | 37.3 | 128,809 | <a href="https://www.star-history.com/#kubernetes/kubernetes&Date"><img src="https://api.star-history.com/svg?repos=kubernetes/kubernetes&type=Date" width="260" alt="kubernetes/kubernetes 的星號歷史曲線"></a> |
| 3 | [grafana/grafana](https://github.com/grafana/grafana)<br>指標日誌追蹤，放進一個面板<br>`基礎建設` | +746 | 24.9 | 77,615 | <a href="https://www.star-history.com/#grafana/grafana&Date"><img src="https://api.star-history.com/svg?repos=grafana/grafana&type=Date" width="260" alt="grafana/grafana 的星號歷史曲線"></a> |
| 4 | [prometheus/prometheus](https://github.com/prometheus/prometheus)<br>系統出問題，告警先找到你<br>`基礎建設` | +697 | 23.2 | 66,893 | <a href="https://www.star-history.com/#prometheus/prometheus&Date"><img src="https://api.star-history.com/svg?repos=prometheus/prometheus&type=Date" width="260" alt="prometheus/prometheus 的星號歷史曲線"></a> |
| 5 | [hashicorp/terraform](https://github.com/hashicorp/terraform)<br>雲資源寫成程式碼，可審閱、可版本管理<br>`基礎建設` | +637 | 21.2 | 50,340 | <a href="https://www.star-history.com/#hashicorp/terraform&Date"><img src="https://api.star-history.com/svg?repos=hashicorp/terraform&type=Date" width="260" alt="hashicorp/terraform 的星號歷史曲線"></a> |
| 6 | [traefik/traefik](https://github.com/traefik/traefik)<br>服務多了，流量自動分好<br>`基礎建設` | +484 | 16.1 | 65,428 | <a href="https://www.star-history.com/#traefik/traefik&Date"><img src="https://api.star-history.com/svg?repos=traefik/traefik&type=Date" width="260" alt="traefik/traefik 的星號歷史曲線"></a> |
| 7 | [docker/compose](https://github.com/docker/compose)<br>多個容器寫進一個檔案，一起跑<br>`基礎建設` | +362 | 12.1 | 38,558 | <a href="https://www.star-history.com/#docker/compose&Date"><img src="https://api.star-history.com/svg?repos=docker/compose&type=Date" width="260" alt="docker/compose 的星號歷史曲線"></a> |
| 8 | [pulumi/pulumi](https://github.com/pulumi/pulumi)<br>用熟悉的程式語言管雲資源<br>`基礎建設` | +132 | 4.4 | 25,838 | <a href="https://www.star-history.com/#pulumi/pulumi&Date"><img src="https://api.star-history.com/svg?repos=pulumi/pulumi&type=Date" width="260" alt="pulumi/pulumi 的星號歷史曲線"></a> |

### 今年成長最快（近 365 天）

| # | 專案 | 新增星號 | 星號/天 | 總星號 | 星號歷史 |
|---|---|---:|---:|---:|---|
| 1 | [caddyserver/caddy](https://github.com/caddyserver/caddy)<br>搭網站伺服器，HTTPS 自動配好<br>`基礎建設` | +11,869 | 32.5 | 78,623 | <a href="https://www.star-history.com/#caddyserver/caddy&Date"><img src="https://api.star-history.com/svg?repos=caddyserver/caddy&type=Date" width="260" alt="caddyserver/caddy 的星號歷史曲線"></a> |
| 2 | [kubernetes/kubernetes](https://github.com/kubernetes/kubernetes)<br>容器多了，部署擴容交給它<br>`基礎建設` | +11,804 | 32.3 | 128,809 | <a href="https://www.star-history.com/#kubernetes/kubernetes&Date"><img src="https://api.star-history.com/svg?repos=kubernetes/kubernetes&type=Date" width="260" alt="kubernetes/kubernetes 的星號歷史曲線"></a> |
| 3 | [traefik/traefik](https://github.com/traefik/traefik)<br>服務多了，流量自動分好<br>`基礎建設` | +8,720 | 23.9 | 65,428 | <a href="https://www.star-history.com/#traefik/traefik&Date"><img src="https://api.star-history.com/svg?repos=traefik/traefik&type=Date" width="260" alt="traefik/traefik 的星號歷史曲線"></a> |
| 4 | [grafana/grafana](https://github.com/grafana/grafana)<br>指標日誌追蹤，放進一個面板<br>`基礎建設` | +7,861 | 21.5 | 77,615 | <a href="https://www.star-history.com/#grafana/grafana&Date"><img src="https://api.star-history.com/svg?repos=grafana/grafana&type=Date" width="260" alt="grafana/grafana 的星號歷史曲線"></a> |
| 5 | [prometheus/prometheus](https://github.com/prometheus/prometheus)<br>系統出問題，告警先找到你<br>`基礎建設` | +6,534 | 17.9 | 66,893 | <a href="https://www.star-history.com/#prometheus/prometheus&Date"><img src="https://api.star-history.com/svg?repos=prometheus/prometheus&type=Date" width="260" alt="prometheus/prometheus 的星號歷史曲線"></a> |
| 6 | [hashicorp/terraform](https://github.com/hashicorp/terraform)<br>雲資源寫成程式碼，可審閱、可版本管理<br>`基礎建設` | +3,996 | 10.9 | 50,340 | <a href="https://www.star-history.com/#hashicorp/terraform&Date"><img src="https://api.star-history.com/svg?repos=hashicorp/terraform&type=Date" width="260" alt="hashicorp/terraform 的星號歷史曲線"></a> |
| 7 | [docker/compose](https://github.com/docker/compose)<br>多個容器寫進一個檔案，一起跑<br>`基礎建設` | +2,610 | 7.2 | 38,558 | <a href="https://www.star-history.com/#docker/compose&Date"><img src="https://api.star-history.com/svg?repos=docker/compose&type=Date" width="260" alt="docker/compose 的星號歷史曲線"></a> |
| 8 | [pulumi/pulumi](https://github.com/pulumi/pulumi)<br>用熟悉的程式語言管雲資源<br>`基礎建設` | +2,084 | 5.7 | 25,838 | <a href="https://www.star-history.com/#pulumi/pulumi&Date"><img src="https://api.star-history.com/svg?repos=pulumi/pulumi&type=Date" width="260" alt="pulumi/pulumi 的星號歷史曲線"></a> |

### 總星號數（歷史累計）

| # | 專案 | 總星號 | 星號歷史 |
|---|---|---:|---|
| 1 | [kubernetes/kubernetes](https://github.com/kubernetes/kubernetes)<br>容器多了，部署擴容交給它<br>`基礎建設` | 128,809 | <a href="https://www.star-history.com/#kubernetes/kubernetes&Date"><img src="https://api.star-history.com/svg?repos=kubernetes/kubernetes&type=Date" width="260" alt="kubernetes/kubernetes 的星號歷史曲線"></a> |
| 2 | [caddyserver/caddy](https://github.com/caddyserver/caddy)<br>搭網站伺服器，HTTPS 自動配好<br>`基礎建設` | 78,623 | <a href="https://www.star-history.com/#caddyserver/caddy&Date"><img src="https://api.star-history.com/svg?repos=caddyserver/caddy&type=Date" width="260" alt="caddyserver/caddy 的星號歷史曲線"></a> |
| 3 | [grafana/grafana](https://github.com/grafana/grafana)<br>指標日誌追蹤，放進一個面板<br>`基礎建設` | 77,615 | <a href="https://www.star-history.com/#grafana/grafana&Date"><img src="https://api.star-history.com/svg?repos=grafana/grafana&type=Date" width="260" alt="grafana/grafana 的星號歷史曲線"></a> |
| 4 | [prometheus/prometheus](https://github.com/prometheus/prometheus)<br>系統出問題，告警先找到你<br>`基礎建設` | 66,893 | <a href="https://www.star-history.com/#prometheus/prometheus&Date"><img src="https://api.star-history.com/svg?repos=prometheus/prometheus&type=Date" width="260" alt="prometheus/prometheus 的星號歷史曲線"></a> |
| 5 | [traefik/traefik](https://github.com/traefik/traefik)<br>服務多了，流量自動分好<br>`基礎建設` | 65,428 | <a href="https://www.star-history.com/#traefik/traefik&Date"><img src="https://api.star-history.com/svg?repos=traefik/traefik&type=Date" width="260" alt="traefik/traefik 的星號歷史曲線"></a> |
| 6 | [hashicorp/terraform](https://github.com/hashicorp/terraform)<br>雲資源寫成程式碼，可審閱、可版本管理<br>`基礎建設` | 50,340 | <a href="https://www.star-history.com/#hashicorp/terraform&Date"><img src="https://api.star-history.com/svg?repos=hashicorp/terraform&type=Date" width="260" alt="hashicorp/terraform 的星號歷史曲線"></a> |
| 7 | [docker/compose](https://github.com/docker/compose)<br>多個容器寫進一個檔案，一起跑<br>`基礎建設` | 38,558 | <a href="https://www.star-history.com/#docker/compose&Date"><img src="https://api.star-history.com/svg?repos=docker/compose&type=Date" width="260" alt="docker/compose 的星號歷史曲線"></a> |
| 8 | [pulumi/pulumi](https://github.com/pulumi/pulumi)<br>用熟悉的程式語言管雲資源<br>`基礎建設` | 25,838 | <a href="https://www.star-history.com/#pulumi/pulumi&Date"><img src="https://api.star-history.com/svg?repos=pulumi/pulumi&type=Date" width="260" alt="pulumi/pulumi 的星號歷史曲線"></a> |

## 設計 / 創意

> 設計系統、繪圖、動畫與創意工具

### 最熱新儲存庫（近 7 天內建立）

| # | 專案 | 建立時間（UTC） | 總星號 | 星號/天 | 星號歷史 |
|---|---|---|---:|---:|---|
| 1 | [patch-gg/pixelfx](https://github.com/patch-gg/pixelfx)<br>缺像素特效？244段簡短程式碼直接套用 | 2026-10-30<br><sub>2.6 天</sub> | 2,452 | 958.3 | <a href="https://www.star-history.com/#patch-gg/pixelfx&Date"><img src="https://api.star-history.com/svg?repos=patch-gg/pixelfx&type=Date" width="260" alt="patch-gg/pixelfx 的星號歷史曲線"></a> |
| 2 | [kevinraymond/florilegium](https://github.com/kevinraymond/florilegium)<br>頁面太單調？畫上代爾夫特藍花卉頁邊 | 2026-10-30<br><sub>2.5 天</sub> | 1,271 | 505.7 | <a href="https://www.star-history.com/#kevinraymond/florilegium&Date"><img src="https://api.star-history.com/svg?repos=kevinraymond/florilegium&type=Date" width="260" alt="kevinraymond/florilegium 的星號歷史曲線"></a> |
| 3 | [op7418/dsh-guizang-design](https://github.com/op7418/dsh-guizang-design)<br>歸藏设计 · DeepSeek Harness 插件：網頁 PPT、圖文卡片、網頁排版、去 AI 味四個技能，一套設計系統；作品庫、內容生產工作流、語氣檔案 | 2026-10-30<br><sub>2.2 天</sub> | 224 | 100.7 | <a href="https://www.star-history.com/#op7418/dsh-guizang-design&Date"><img src="https://api.star-history.com/svg?repos=op7418/dsh-guizang-design&type=Date" width="260" alt="op7418/dsh-guizang-design 的星號歷史曲線"></a> |
| 4 | [Akillll-DuoHe/fy-code-animation](https://github.com/Akillll-DuoHe/fy-code-animation)<br>代碼動畫難做？文案與聲音直接生成 | 2026-10-30<br><sub>2.4 天</sub> | 100 | 41.2 | <a href="https://www.star-history.com/#Akillll-DuoHe/fy-code-animation&Date"><img src="https://api.star-history.com/svg?repos=Akillll-DuoHe/fy-code-animation&type=Date" width="260" alt="Akillll-DuoHe/fy-code-animation 的星號歷史曲線"></a> |
| 5 | [enmerasoftware/ai-design-check](https://github.com/enmerasoftware/ai-design-check)<br>代理寫的介面不規範？一鍵檢查設計規則 | 2026-10-28<br><sub>4.5 天</sub> | 135 | 29.8 | <a href="https://www.star-history.com/#enmerasoftware/ai-design-check&Date"><img src="https://api.star-history.com/svg?repos=enmerasoftware/ai-design-check&type=Date" width="260" alt="enmerasoftware/ai-design-check 的星號歷史曲線"></a> |
| 6 | [sirioberati/YouTube-AI-Motion-Graphics](https://github.com/sirioberati/YouTube-AI-Motion-Graphics)<br>解說動效難做？74個看板隨語音同步 | 2026-10-27<br><sub>5.1 天</sub> | 119 | 23.3 | <a href="https://www.star-history.com/#sirioberati/YouTube-AI-Motion-Graphics&Date"><img src="https://api.star-history.com/svg?repos=sirioberati/YouTube-AI-Motion-Graphics&type=Date" width="260" alt="sirioberati/YouTube-AI-Motion-Graphics 的星號歷史曲線"></a> |

### 本週成長最快（近 7 天）

| # | 專案 | 新增星號 | 星號/天 | 總星號 | 星號歷史 |
|---|---|---:|---:|---:|---|
| 1 | [excalidraw/excalidraw](https://github.com/excalidraw/excalidraw)<br>開啟就畫，像在紙上隨手畫圖<br>`設計 / 創意` | +478 | 68.3 | 134,976 | <a href="https://www.star-history.com/#excalidraw/excalidraw&Date"><img src="https://api.star-history.com/svg?repos=excalidraw/excalidraw&type=Date" width="260" alt="excalidraw/excalidraw 的星號歷史曲線"></a> |
| 2 | [penpot/penpot](https://github.com/penpot/penpot)<br>團隊一起做設計，用開源平台<br>`設計 / 創意` | +346 | 49.4 | 61,963 | <a href="https://www.star-history.com/#penpot/penpot&Date"><img src="https://api.star-history.com/svg?repos=penpot/penpot&type=Date" width="260" alt="penpot/penpot 的星號歷史曲線"></a> |
| 3 | [lucide-icons/lucide](https://github.com/lucide-icons/lucide)<br>一套圖示風格統一，拿來就用<br>`設計 / 創意` | +182 | 26.0 | 25,444 | <a href="https://www.star-history.com/#lucide-icons/lucide&Date"><img src="https://api.star-history.com/svg?repos=lucide-icons/lucide&type=Date" width="260" alt="lucide-icons/lucide 的星號歷史曲線"></a> |
| 4 | [jgraph/drawio](https://github.com/jgraph/drawio)<br>畫圖和白板，一個編輯器搞定<br>`設計 / 創意` | +142 | 20.3 | 9,115 | <a href="https://www.star-history.com/#jgraph/drawio&Date"><img src="https://api.star-history.com/svg?repos=jgraph/drawio&type=Date" width="260" alt="jgraph/drawio 的星號歷史曲線"></a> |
| 5 | [saadeghi/daisyui](https://github.com/saadeghi/daisyui)<br>Tailwind 也有現成元件可挑<br>`設計 / 創意` | +72 | 10.3 | 42,723 | <a href="https://www.star-history.com/#saadeghi/daisyui&Date"><img src="https://api.star-history.com/svg?repos=saadeghi/daisyui&type=Date" width="260" alt="saadeghi/daisyui 的星號歷史曲線"></a> |
| 6 | [airbnb/lottie-web](https://github.com/airbnb/lottie-web)<br>AE 做的動畫，直接放進網頁<br>`設計 / 創意` | +56 | 8.0 | 32,327 | <a href="https://www.star-history.com/#airbnb/lottie-web&Date"><img src="https://api.star-history.com/svg?repos=airbnb/lottie-web&type=Date" width="260" alt="airbnb/lottie-web 的星號歷史曲線"></a> |
| 7 | [phosphor-icons/homepage](https://github.com/phosphor-icons/homepage)<br>一整套靈活的圖示，人人可用<br>`設計 / 創意` | +36 | 5.1 | 7,750 | <a href="https://www.star-history.com/#phosphor-icons/homepage&Date"><img src="https://api.star-history.com/svg?repos=phosphor-icons/homepage&type=Date" width="260" alt="phosphor-icons/homepage 的星號歷史曲線"></a> |
| 8 | [lottiefiles/lottie-ios](https://github.com/lottiefiles/lottie-ios)<br>AE 做的動畫，直接放進 iOS<br>`設計 / 創意` | +0 | 0.0 | 43 | <a href="https://www.star-history.com/#lottiefiles/lottie-ios&Date"><img src="https://api.star-history.com/svg?repos=lottiefiles/lottie-ios&type=Date" width="260" alt="lottiefiles/lottie-ios 的星號歷史曲線"></a> |

### 本月成長最快（近 30 天）

| # | 專案 | 新增星號 | 星號/天 | 總星號 | 星號歷史 |
|---|---|---:|---:|---:|---|
| 1 | [excalidraw/excalidraw](https://github.com/excalidraw/excalidraw)<br>開啟就畫，像在紙上隨手畫圖<br>`設計 / 創意` | +1,964 | 65.5 | 134,976 | <a href="https://www.star-history.com/#excalidraw/excalidraw&Date"><img src="https://api.star-history.com/svg?repos=excalidraw/excalidraw&type=Date" width="260" alt="excalidraw/excalidraw 的星號歷史曲線"></a> |
| 2 | [penpot/penpot](https://github.com/penpot/penpot)<br>團隊一起做設計，用開源平台<br>`設計 / 創意` | +1,495 | 49.8 | 61,963 | <a href="https://www.star-history.com/#penpot/penpot&Date"><img src="https://api.star-history.com/svg?repos=penpot/penpot&type=Date" width="260" alt="penpot/penpot 的星號歷史曲線"></a> |
| 3 | [lucide-icons/lucide](https://github.com/lucide-icons/lucide)<br>一套圖示風格統一，拿來就用<br>`設計 / 創意` | +673 | 22.4 | 25,444 | <a href="https://www.star-history.com/#lucide-icons/lucide&Date"><img src="https://api.star-history.com/svg?repos=lucide-icons/lucide&type=Date" width="260" alt="lucide-icons/lucide 的星號歷史曲線"></a> |
| 4 | [jgraph/drawio](https://github.com/jgraph/drawio)<br>畫圖和白板，一個編輯器搞定<br>`設計 / 創意` | +607 | 20.2 | 9,115 | <a href="https://www.star-history.com/#jgraph/drawio&Date"><img src="https://api.star-history.com/svg?repos=jgraph/drawio&type=Date" width="260" alt="jgraph/drawio 的星號歷史曲線"></a> |
| 5 | [saadeghi/daisyui](https://github.com/saadeghi/daisyui)<br>Tailwind 也有現成元件可挑<br>`設計 / 創意` | +274 | 9.1 | 42,723 | <a href="https://www.star-history.com/#saadeghi/daisyui&Date"><img src="https://api.star-history.com/svg?repos=saadeghi/daisyui&type=Date" width="260" alt="saadeghi/daisyui 的星號歷史曲線"></a> |
| 6 | [airbnb/lottie-web](https://github.com/airbnb/lottie-web)<br>AE 做的動畫，直接放進網頁<br>`設計 / 創意` | +213 | 7.1 | 32,327 | <a href="https://www.star-history.com/#airbnb/lottie-web&Date"><img src="https://api.star-history.com/svg?repos=airbnb/lottie-web&type=Date" width="260" alt="airbnb/lottie-web 的星號歷史曲線"></a> |
| 7 | [phosphor-icons/homepage](https://github.com/phosphor-icons/homepage)<br>一整套靈活的圖示，人人可用<br>`設計 / 創意` | +176 | 5.9 | 7,750 | <a href="https://www.star-history.com/#phosphor-icons/homepage&Date"><img src="https://api.star-history.com/svg?repos=phosphor-icons/homepage&type=Date" width="260" alt="phosphor-icons/homepage 的星號歷史曲線"></a> |
| 8 | [lottiefiles/lottie-ios](https://github.com/lottiefiles/lottie-ios)<br>AE 做的動畫，直接放進 iOS<br>`設計 / 創意` | +0 | 0.0 | 43 | <a href="https://www.star-history.com/#lottiefiles/lottie-ios&Date"><img src="https://api.star-history.com/svg?repos=lottiefiles/lottie-ios&type=Date" width="260" alt="lottiefiles/lottie-ios 的星號歷史曲線"></a> |

### 今年成長最快（近 365 天）

| # | 專案 | 新增星號 | 星號/天 | 總星號 | 星號歷史 |
|---|---|---:|---:|---:|---|
| 1 | [excalidraw/excalidraw](https://github.com/excalidraw/excalidraw)<br>開啟就畫，像在紙上隨手畫圖<br>`設計 / 創意` | +26,994 | 74.0 | 134,976 | <a href="https://www.star-history.com/#excalidraw/excalidraw&Date"><img src="https://api.star-history.com/svg?repos=excalidraw/excalidraw&type=Date" width="260" alt="excalidraw/excalidraw 的星號歷史曲線"></a> |
| 2 | [penpot/penpot](https://github.com/penpot/penpot)<br>團隊一起做設計，用開源平台<br>`設計 / 創意` | +21,692 | 59.4 | 61,963 | <a href="https://www.star-history.com/#penpot/penpot&Date"><img src="https://api.star-history.com/svg?repos=penpot/penpot&type=Date" width="260" alt="penpot/penpot 的星號歷史曲線"></a> |
| 3 | [jgraph/drawio](https://github.com/jgraph/drawio)<br>畫圖和白板，一個編輯器搞定<br>`設計 / 創意` | +6,467 | 17.7 | 9,115 | <a href="https://www.star-history.com/#jgraph/drawio&Date"><img src="https://api.star-history.com/svg?repos=jgraph/drawio&type=Date" width="260" alt="jgraph/drawio 的星號歷史曲線"></a> |
| 4 | [lucide-icons/lucide](https://github.com/lucide-icons/lucide)<br>一套圖示風格統一，拿來就用<br>`設計 / 創意` | +6,232 | 17.1 | 25,444 | <a href="https://www.star-history.com/#lucide-icons/lucide&Date"><img src="https://api.star-history.com/svg?repos=lucide-icons/lucide&type=Date" width="260" alt="lucide-icons/lucide 的星號歷史曲線"></a> |
| 5 | [saadeghi/daisyui](https://github.com/saadeghi/daisyui)<br>Tailwind 也有現成元件可挑<br>`設計 / 創意` | +4,226 | 11.6 | 42,723 | <a href="https://www.star-history.com/#saadeghi/daisyui&Date"><img src="https://api.star-history.com/svg?repos=saadeghi/daisyui&type=Date" width="260" alt="saadeghi/daisyui 的星號歷史曲線"></a> |
| 6 | [phosphor-icons/homepage](https://github.com/phosphor-icons/homepage)<br>一整套靈活的圖示，人人可用<br>`設計 / 創意` | +2,192 | 6.0 | 7,750 | <a href="https://www.star-history.com/#phosphor-icons/homepage&Date"><img src="https://api.star-history.com/svg?repos=phosphor-icons/homepage&type=Date" width="260" alt="phosphor-icons/homepage 的星號歷史曲線"></a> |
| 7 | [airbnb/lottie-web](https://github.com/airbnb/lottie-web)<br>AE 做的動畫，直接放進網頁<br>`設計 / 創意` | +1,080 | 3.0 | 32,327 | <a href="https://www.star-history.com/#airbnb/lottie-web&Date"><img src="https://api.star-history.com/svg?repos=airbnb/lottie-web&type=Date" width="260" alt="airbnb/lottie-web 的星號歷史曲線"></a> |
| 8 | [lottiefiles/lottie-ios](https://github.com/lottiefiles/lottie-ios)<br>AE 做的動畫，直接放進 iOS<br>`設計 / 創意` | +1 | 0.0 | 43 | <a href="https://www.star-history.com/#lottiefiles/lottie-ios&Date"><img src="https://api.star-history.com/svg?repos=lottiefiles/lottie-ios&type=Date" width="260" alt="lottiefiles/lottie-ios 的星號歷史曲線"></a> |

### 總星號數（歷史累計）

| # | 專案 | 總星號 | 星號歷史 |
|---|---|---:|---|
| 1 | [excalidraw/excalidraw](https://github.com/excalidraw/excalidraw)<br>開啟就畫，像在紙上隨手畫圖<br>`設計 / 創意` | 134,976 | <a href="https://www.star-history.com/#excalidraw/excalidraw&Date"><img src="https://api.star-history.com/svg?repos=excalidraw/excalidraw&type=Date" width="260" alt="excalidraw/excalidraw 的星號歷史曲線"></a> |
| 2 | [penpot/penpot](https://github.com/penpot/penpot)<br>團隊一起做設計，用開源平台<br>`設計 / 創意` | 61,963 | <a href="https://www.star-history.com/#penpot/penpot&Date"><img src="https://api.star-history.com/svg?repos=penpot/penpot&type=Date" width="260" alt="penpot/penpot 的星號歷史曲線"></a> |
| 3 | [saadeghi/daisyui](https://github.com/saadeghi/daisyui)<br>Tailwind 也有現成元件可挑<br>`設計 / 創意` | 42,723 | <a href="https://www.star-history.com/#saadeghi/daisyui&Date"><img src="https://api.star-history.com/svg?repos=saadeghi/daisyui&type=Date" width="260" alt="saadeghi/daisyui 的星號歷史曲線"></a> |
| 4 | [airbnb/lottie-web](https://github.com/airbnb/lottie-web)<br>AE 做的動畫，直接放進網頁<br>`設計 / 創意` | 32,327 | <a href="https://www.star-history.com/#airbnb/lottie-web&Date"><img src="https://api.star-history.com/svg?repos=airbnb/lottie-web&type=Date" width="260" alt="airbnb/lottie-web 的星號歷史曲線"></a> |
| 5 | [lucide-icons/lucide](https://github.com/lucide-icons/lucide)<br>一套圖示風格統一，拿來就用<br>`設計 / 創意` | 25,444 | <a href="https://www.star-history.com/#lucide-icons/lucide&Date"><img src="https://api.star-history.com/svg?repos=lucide-icons/lucide&type=Date" width="260" alt="lucide-icons/lucide 的星號歷史曲線"></a> |
| 6 | [jgraph/drawio](https://github.com/jgraph/drawio)<br>畫圖和白板，一個編輯器搞定<br>`設計 / 創意` | 9,115 | <a href="https://www.star-history.com/#jgraph/drawio&Date"><img src="https://api.star-history.com/svg?repos=jgraph/drawio&type=Date" width="260" alt="jgraph/drawio 的星號歷史曲線"></a> |
| 7 | [phosphor-icons/homepage](https://github.com/phosphor-icons/homepage)<br>一整套靈活的圖示，人人可用<br>`設計 / 創意` | 7,750 | <a href="https://www.star-history.com/#phosphor-icons/homepage&Date"><img src="https://api.star-history.com/svg?repos=phosphor-icons/homepage&type=Date" width="260" alt="phosphor-icons/homepage 的星號歷史曲線"></a> |
| 8 | [lottiefiles/lottie-ios](https://github.com/lottiefiles/lottie-ios)<br>AE 做的動畫，直接放進 iOS<br>`設計 / 創意` | 43 | <a href="https://www.star-history.com/#lottiefiles/lottie-ios&Date"><img src="https://api.star-history.com/svg?repos=lottiefiles/lottie-ios&type=Date" width="260" alt="lottiefiles/lottie-ios 的星號歷史曲線"></a> |

## 資料

> 資料庫、分析、ETL 與資料工程

### 最熱新儲存庫（近 7 天內建立）

本次執行中沒有符合條件的新儲存庫。

### 本週成長最快（近 7 天）

| # | 專案 | 新增星號 | 星號/天 | 總星號 | 星號歷史 |
|---|---|---:|---:|---:|---|
| 1 | [duckdb/duckdb](https://github.com/duckdb/duckdb)<br>不搭資料庫服務，也能跑 SQL 分析<br>`資料` | +247 | 35.3 | 42,732 | <a href="https://www.star-history.com/#duckdb/duckdb&Date"><img src="https://api.star-history.com/svg?repos=duckdb/duckdb&type=Date" width="260" alt="duckdb/duckdb 的星號歷史曲線"></a> |
| 2 | [ClickHouse/ClickHouse](https://github.com/ClickHouse/ClickHouse)<br>大量資料即時分析，用開源的<br>`資料` | +127 | 18.1 | 50,705 | <a href="https://www.star-history.com/#ClickHouse/ClickHouse&Date"><img src="https://api.star-history.com/svg?repos=ClickHouse/ClickHouse&type=Date" width="260" alt="ClickHouse/ClickHouse 的星號歷史曲線"></a> |
| 3 | [apache/superset](https://github.com/apache/superset)<br>資料看不懂，做成圖就明白<br>`資料` | +110 | 15.7 | 75,386 | <a href="https://www.star-history.com/#apache/superset&Date"><img src="https://api.star-history.com/svg?repos=apache/superset&type=Date" width="260" alt="apache/superset 的星號歷史曲線"></a> |
| 4 | [pola-rs/polars](https://github.com/pola-rs/polars)<br>表格資料處理快，不用乾等<br>`資料` | +70 | 10.0 | 40,247 | <a href="https://www.star-history.com/#pola-rs/polars&Date"><img src="https://api.star-history.com/svg?repos=pola-rs/polars&type=Date" width="260" alt="pola-rs/polars 的星號歷史曲線"></a> |
| 5 | [apache/kafka](https://github.com/apache/kafka)<br>系統之間的事件流，交給它來傳<br>`資料` | +63 | 9.0 | 34,109 | <a href="https://www.star-history.com/#apache/kafka&Date"><img src="https://api.star-history.com/svg?repos=apache/kafka&type=Date" width="260" alt="apache/kafka 的星號歷史曲線"></a> |
| 6 | [apache/arrow](https://github.com/apache/arrow)<br>不同語言之間，資料直接通用<br>`資料` | +49 | 7.0 | 17,268 | <a href="https://www.star-history.com/#apache/arrow&Date"><img src="https://api.star-history.com/svg?repos=apache/arrow&type=Date" width="260" alt="apache/arrow 的星號歷史曲線"></a> |
| 7 | [dbt-labs/dbt-core](https://github.com/dbt-labs/dbt-core)<br>資料轉換，照軟體工程的做法來<br>`資料` | +34 | 4.9 | 14,106 | <a href="https://www.star-history.com/#dbt-labs/dbt-core&Date"><img src="https://api.star-history.com/svg?repos=dbt-labs/dbt-core&type=Date" width="260" alt="dbt-labs/dbt-core 的星號歷史曲線"></a> |
| 8 | [jupyter/notebook](https://github.com/jupyter/notebook)<br>在網頁裡寫程式碼，邊寫邊看結果<br>`資料` | +5 | 0.7 | 13,458 | <a href="https://www.star-history.com/#jupyter/notebook&Date"><img src="https://api.star-history.com/svg?repos=jupyter/notebook&type=Date" width="260" alt="jupyter/notebook 的星號歷史曲線"></a> |

### 本月成長最快（近 30 天）

| # | 專案 | 新增星號 | 星號/天 | 總星號 | 星號歷史 |
|---|---|---:|---:|---:|---|
| 1 | [duckdb/duckdb](https://github.com/duckdb/duckdb)<br>不搭資料庫服務，也能跑 SQL 分析<br>`資料` | +930 | 31.0 | 42,732 | <a href="https://www.star-history.com/#duckdb/duckdb&Date"><img src="https://api.star-history.com/svg?repos=duckdb/duckdb&type=Date" width="260" alt="duckdb/duckdb 的星號歷史曲線"></a> |
| 2 | [ClickHouse/ClickHouse](https://github.com/ClickHouse/ClickHouse)<br>大量資料即時分析，用開源的<br>`資料` | +602 | 20.1 | 50,705 | <a href="https://www.star-history.com/#ClickHouse/ClickHouse&Date"><img src="https://api.star-history.com/svg?repos=ClickHouse/ClickHouse&type=Date" width="260" alt="ClickHouse/ClickHouse 的星號歷史曲線"></a> |
| 3 | [apache/superset](https://github.com/apache/superset)<br>資料看不懂，做成圖就明白<br>`資料` | +474 | 15.8 | 75,386 | <a href="https://www.star-history.com/#apache/superset&Date"><img src="https://api.star-history.com/svg?repos=apache/superset&type=Date" width="260" alt="apache/superset 的星號歷史曲線"></a> |
| 4 | [pola-rs/polars](https://github.com/pola-rs/polars)<br>表格資料處理快，不用乾等<br>`資料` | +385 | 12.8 | 40,247 | <a href="https://www.star-history.com/#pola-rs/polars&Date"><img src="https://api.star-history.com/svg?repos=pola-rs/polars&type=Date" width="260" alt="pola-rs/polars 的星號歷史曲線"></a> |
| 5 | [apache/kafka](https://github.com/apache/kafka)<br>系統之間的事件流，交給它來傳<br>`資料` | +294 | 9.8 | 34,109 | <a href="https://www.star-history.com/#apache/kafka&Date"><img src="https://api.star-history.com/svg?repos=apache/kafka&type=Date" width="260" alt="apache/kafka 的星號歷史曲線"></a> |
| 6 | [dbt-labs/dbt-core](https://github.com/dbt-labs/dbt-core)<br>資料轉換，照軟體工程的做法來<br>`資料` | +169 | 5.6 | 14,106 | <a href="https://www.star-history.com/#dbt-labs/dbt-core&Date"><img src="https://api.star-history.com/svg?repos=dbt-labs/dbt-core&type=Date" width="260" alt="dbt-labs/dbt-core 的星號歷史曲線"></a> |
| 7 | [apache/arrow](https://github.com/apache/arrow)<br>不同語言之間，資料直接通用<br>`資料` | +121 | 4.0 | 17,268 | <a href="https://www.star-history.com/#apache/arrow&Date"><img src="https://api.star-history.com/svg?repos=apache/arrow&type=Date" width="260" alt="apache/arrow 的星號歷史曲線"></a> |
| 8 | [jupyter/notebook](https://github.com/jupyter/notebook)<br>在網頁裡寫程式碼，邊寫邊看結果<br>`資料` | +73 | 2.4 | 13,458 | <a href="https://www.star-history.com/#jupyter/notebook&Date"><img src="https://api.star-history.com/svg?repos=jupyter/notebook&type=Date" width="260" alt="jupyter/notebook 的星號歷史曲線"></a> |

### 今年成長最快（近 365 天）

| # | 專案 | 新增星號 | 星號/天 | 總星號 | 星號歷史 |
|---|---|---:|---:|---:|---|
| 1 | [duckdb/duckdb](https://github.com/duckdb/duckdb)<br>不搭資料庫服務，也能跑 SQL 分析<br>`資料` | +9,360 | 25.6 | 42,732 | <a href="https://www.star-history.com/#duckdb/duckdb&Date"><img src="https://api.star-history.com/svg?repos=duckdb/duckdb&type=Date" width="260" alt="duckdb/duckdb 的星號歷史曲線"></a> |
| 2 | [ClickHouse/ClickHouse](https://github.com/ClickHouse/ClickHouse)<br>大量資料即時分析，用開源的<br>`資料` | +7,631 | 20.9 | 50,705 | <a href="https://www.star-history.com/#ClickHouse/ClickHouse&Date"><img src="https://api.star-history.com/svg?repos=ClickHouse/ClickHouse&type=Date" width="260" alt="ClickHouse/ClickHouse 的星號歷史曲線"></a> |
| 3 | [apache/superset](https://github.com/apache/superset)<br>資料看不懂，做成圖就明白<br>`資料` | +7,453 | 20.4 | 75,386 | <a href="https://www.star-history.com/#apache/superset&Date"><img src="https://api.star-history.com/svg?repos=apache/superset&type=Date" width="260" alt="apache/superset 的星號歷史曲線"></a> |
| 4 | [pola-rs/polars](https://github.com/pola-rs/polars)<br>表格資料處理快，不用乾等<br>`資料` | +4,861 | 13.3 | 40,247 | <a href="https://www.star-history.com/#pola-rs/polars&Date"><img src="https://api.star-history.com/svg?repos=pola-rs/polars&type=Date" width="260" alt="pola-rs/polars 的星號歷史曲線"></a> |
| 5 | [apache/kafka](https://github.com/apache/kafka)<br>系統之間的事件流，交給它來傳<br>`資料` | +3,298 | 9.0 | 34,109 | <a href="https://www.star-history.com/#apache/kafka&Date"><img src="https://api.star-history.com/svg?repos=apache/kafka&type=Date" width="260" alt="apache/kafka 的星號歷史曲線"></a> |
| 6 | [dbt-labs/dbt-core](https://github.com/dbt-labs/dbt-core)<br>資料轉換，照軟體工程的做法來<br>`資料` | +2,461 | 6.7 | 14,106 | <a href="https://www.star-history.com/#dbt-labs/dbt-core&Date"><img src="https://api.star-history.com/svg?repos=dbt-labs/dbt-core&type=Date" width="260" alt="dbt-labs/dbt-core 的星號歷史曲線"></a> |
| 7 | [apache/arrow](https://github.com/apache/arrow)<br>不同語言之間，資料直接通用<br>`資料` | +1,315 | 3.6 | 17,268 | <a href="https://www.star-history.com/#apache/arrow&Date"><img src="https://api.star-history.com/svg?repos=apache/arrow&type=Date" width="260" alt="apache/arrow 的星號歷史曲線"></a> |
| 8 | [jupyter/notebook](https://github.com/jupyter/notebook)<br>在網頁裡寫程式碼，邊寫邊看結果<br>`資料` | +912 | 2.5 | 13,458 | <a href="https://www.star-history.com/#jupyter/notebook&Date"><img src="https://api.star-history.com/svg?repos=jupyter/notebook&type=Date" width="260" alt="jupyter/notebook 的星號歷史曲線"></a> |

### 總星號數（歷史累計）

| # | 專案 | 總星號 | 星號歷史 |
|---|---|---:|---|
| 1 | [apache/superset](https://github.com/apache/superset)<br>資料看不懂，做成圖就明白<br>`資料` | 75,386 | <a href="https://www.star-history.com/#apache/superset&Date"><img src="https://api.star-history.com/svg?repos=apache/superset&type=Date" width="260" alt="apache/superset 的星號歷史曲線"></a> |
| 2 | [ClickHouse/ClickHouse](https://github.com/ClickHouse/ClickHouse)<br>大量資料即時分析，用開源的<br>`資料` | 50,705 | <a href="https://www.star-history.com/#ClickHouse/ClickHouse&Date"><img src="https://api.star-history.com/svg?repos=ClickHouse/ClickHouse&type=Date" width="260" alt="ClickHouse/ClickHouse 的星號歷史曲線"></a> |
| 3 | [duckdb/duckdb](https://github.com/duckdb/duckdb)<br>不搭資料庫服務，也能跑 SQL 分析<br>`資料` | 42,732 | <a href="https://www.star-history.com/#duckdb/duckdb&Date"><img src="https://api.star-history.com/svg?repos=duckdb/duckdb&type=Date" width="260" alt="duckdb/duckdb 的星號歷史曲線"></a> |
| 4 | [pola-rs/polars](https://github.com/pola-rs/polars)<br>表格資料處理快，不用乾等<br>`資料` | 40,247 | <a href="https://www.star-history.com/#pola-rs/polars&Date"><img src="https://api.star-history.com/svg?repos=pola-rs/polars&type=Date" width="260" alt="pola-rs/polars 的星號歷史曲線"></a> |
| 5 | [apache/kafka](https://github.com/apache/kafka)<br>系統之間的事件流，交給它來傳<br>`資料` | 34,109 | <a href="https://www.star-history.com/#apache/kafka&Date"><img src="https://api.star-history.com/svg?repos=apache/kafka&type=Date" width="260" alt="apache/kafka 的星號歷史曲線"></a> |
| 6 | [apache/arrow](https://github.com/apache/arrow)<br>不同語言之間，資料直接通用<br>`資料` | 17,268 | <a href="https://www.star-history.com/#apache/arrow&Date"><img src="https://api.star-history.com/svg?repos=apache/arrow&type=Date" width="260" alt="apache/arrow 的星號歷史曲線"></a> |
| 7 | [dbt-labs/dbt-core](https://github.com/dbt-labs/dbt-core)<br>資料轉換，照軟體工程的做法來<br>`資料` | 14,106 | <a href="https://www.star-history.com/#dbt-labs/dbt-core&Date"><img src="https://api.star-history.com/svg?repos=dbt-labs/dbt-core&type=Date" width="260" alt="dbt-labs/dbt-core 的星號歷史曲線"></a> |
| 8 | [jupyter/notebook](https://github.com/jupyter/notebook)<br>在網頁裡寫程式碼，邊寫邊看結果<br>`資料` | 13,458 | <a href="https://www.star-history.com/#jupyter/notebook&Date"><img src="https://api.star-history.com/svg?repos=jupyter/notebook&type=Date" width="260" alt="jupyter/notebook 的星號歷史曲線"></a> |

---

如果它幫你省了時間，請給儲存庫按個星號，讓更多人找得到。

如何引用：見 [CITATION.cff](CITATION.cff)。

資料怎麼算與如何參與：[docs/HOW_IT_WORKS.zh-Hant.md](docs/HOW_IT_WORKS.zh-Hant.md)。新儲存庫規則：[docs/NEW_ARRIVALS.md](docs/NEW_ARRIVALS.md)。分類說明：[docs/CATEGORIES.md](docs/CATEGORIES.md)。提交改動：[CONTRIBUTING.md](CONTRIBUTING.md)。
