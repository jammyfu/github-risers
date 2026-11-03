[English](README.md) | [简体中文](README.zh-Hans.md) | [繁體中文](README.zh-Hant.md) | **日本語** | [한국어](README.ko.md)

# GitHub スター急上昇ランキング / GitHub Risers

<img src=".github/social-preview.png" alt="GitHub スター急上昇ランキング / GitHub Risers" width="640">

[![MIT](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE) [![CI](https://github.com/jammyfu/github-risers/actions/workflows/ci.yml/badge.svg)](https://github.com/jammyfu/github-risers/actions/workflows/ci.yml) [![updated](https://img.shields.io/badge/dynamic/json?url=https%3A%2F%2Fraw.githubusercontent.com%2Fjammyfu%2Fgithub-risers%2Fmain%2Fdata%2Fstats.json&query=%24.today_utc&label=updated&color=brightgreen)](latest/rankings.ja.md)

総スター数ではなく、1 日あたりに増えたスター数で GitHub リポジトリを並べます。AI が先頭で、開発者ツール、セキュリティ、Web / フロントエンド、インフラ、デザイン / クリエイティブ、データが続きます。1 日 2 回更新。

データ取得 2026-11-03 21:28（UTC）。1 日 2 回：北京時間 0 時（UTC+8）、ロサンゼルス時間 0 時（America/Los_Angeles）。

[ウェブサイト](https://jammyfu.github.io/github-risers/) · [仕組み](docs/HOW_IT_WORKS.ja.md) · [ファクト](docs/FACTS.md) · [履歴](rankings/README.ja.md) · [最新](latest/rankings.ja.md)

## 今回のカテゴリ別 1 位

| カテゴリ | 新着 1 位（7 日） | 今週 1 位 | 今月 1 位 | 今年 1 位 | 総スター 1 位 |
|---|---|---|---|---|---|
| **[AI](#ai)** ★ メイン | [wangzan101/Mika](https://github.com/wangzan101/Mika)<br>1,139/日 | [morluto/rea](https://github.com/morluto/rea)<br>4,514/日 | [morluto/rea](https://github.com/morluto/rea)<br>14,121/日 | [deepseek-ai/deepseek-harness](https://github.com/deepseek-ai/deepseek-harness)<br>3,295/日 | [morluto/rea](https://github.com/morluto/rea)<br>426,698 ★ |
| **[開発者ツール](#開発者ツール)** | [Verlintas/NOIR](https://github.com/Verlintas/NOIR)<br>584/日 | [zed-industries/zed](https://github.com/zed-industries/zed)<br>59.3/日 | [zed-industries/zed](https://github.com/zed-industries/zed)<br>54.1/日 | [zed-industries/zed](https://github.com/zed-industries/zed)<br>70.3/日 | [oven-sh/bun](https://github.com/oven-sh/bun)<br>96,532 ★ |
| **[セキュリティ](#セキュリティ)** | なし | [projectdiscovery/nuclei](https://github.com/projectdiscovery/nuclei)<br>29.4/日 | [projectdiscovery/nuclei](https://github.com/projectdiscovery/nuclei)<br>30.7/日 | [aquasecurity/trivy](https://github.com/aquasecurity/trivy)<br>27.7/日 | [aquasecurity/trivy](https://github.com/aquasecurity/trivy)<br>38,941 ★ |
| **[Web / フロントエンド](#web--フロントエンド)** | [mofan6/Moect](https://github.com/mofan6/Moect)<br>65.3/日 | [shadcn-ui/ui](https://github.com/shadcn-ui/ui)<br>94.9/日 | [shadcn-ui/ui](https://github.com/shadcn-ui/ui)<br>88.4/日 | [shadcn-ui/ui](https://github.com/shadcn-ui/ui)<br>83.2/日 | [facebook/react](https://github.com/facebook/react)<br>251,900 ★ |
| **[インフラ](#インフラ)** | [narratarr/narratarr](https://github.com/narratarr/narratarr)<br>16.5/日 | [caddyserver/caddy](https://github.com/caddyserver/caddy)<br>36.4/日 | [caddyserver/caddy](https://github.com/caddyserver/caddy)<br>84.4/日 | [caddyserver/caddy](https://github.com/caddyserver/caddy)<br>32.6/日 | [kubernetes/kubernetes](https://github.com/kubernetes/kubernetes)<br>128,638 ★ |
| **[デザイン / クリエイティブ](#デザイン--クリエイティブ)** | [patch-gg/pixelfx](https://github.com/patch-gg/pixelfx)<br>882/日 | [excalidraw/excalidraw](https://github.com/excalidraw/excalidraw)<br>72.0/日 | [excalidraw/excalidraw](https://github.com/excalidraw/excalidraw)<br>66.9/日 | [excalidraw/excalidraw](https://github.com/excalidraw/excalidraw)<br>74.2/日 | [excalidraw/excalidraw](https://github.com/excalidraw/excalidraw)<br>135,112 ★ |
| **[データ](#データ)** | なし | [duckdb/duckdb](https://github.com/duckdb/duckdb)<br>28.0/日 | [duckdb/duckdb](https://github.com/duckdb/duckdb)<br>31.5/日 | [duckdb/duckdb](https://github.com/duckdb/duckdb)<br>25.7/日 | [apache/superset](https://github.com/apache/superset)<br>75,398 ★ |

ここでは各ランキングの上位 10 件だけを載せています。上位 20 件の全体は [latest/rankings.ja.md](latest/rankings.ja.md) にあります。

表では 1 プロジェクトにつき 1 行だけ載せています。ツール名や技術的な詳細を含む完全な説明は [docs/DETAILS.ja.md](docs/DETAILS.ja.md) にあります。

## よくある質問

### GitHub Risers とは？

総スター数ではなく、1 日あたりに増えたスター数で GitHub リポジトリを並べたランキングです。AI がメインで、ほかに 6 つのカテゴリがあります。データは GitHub API からスクリプトで作っています。 [詳しく見る](docs/FAQ.md#what-is-github-risers)

### GitHub Trending とどう違う？

GitHub Trending は GitHub 公式のページです。GitHub Risers は独立したオープンソースのプロジェクトで、ルールを公開し、5 言語に対応し、更新のたびに履歴を残します。GitHub とは無関係です。 [詳しく見る](docs/FAQ.md#is-it-the-same-as-github-trending)

### 更新は何回？

1 日 2 回、北京時間 0 時とロサンゼルス時間 0 時です。実行のたびに保存します。 [詳しく見る](docs/FAQ.md#how-often-is-it-updated)

### 数値はどう出す？

直近 7・30・365 の完了した UTC 日の増加スターを日数で割ります。数値はすべて GitHub API から取得し、手入力や推定はしません。 [詳しく見る](docs/FAQ.md#how-is-the-growth-rate-computed)

### 使い方と参加方法は？

下のランキングを見るか、latest/ の上位 20 件を見てください。収録プロジェクトを足すには data/projects.json（5 言語）を編集して pull request を出します。 [詳しく見る](docs/FAQ.md#how-can-i-suggest-a-project-or-report-a-mistake)

## AI

> LLM・エージェント・MCP・コーディング助手・生成 AI

### 7 日以内の新着で最も熱いリポジトリ（作成から 7 日以内）

| # | プロジェクト | 作成日（UTC） | 総スター数 | スター/日 | スター推移 |
|---|---|---|---:|---:|---|
| 1 | [wangzan101/Mika](https://github.com/wangzan101/Mika)<br>スマホ操作が面倒なら、エージェントにお任せ | 2026-10-29<br><sub>5.3 日</sub> | 6,021 | 1,138.7 | <a href="https://www.star-history.com/#wangzan101/Mika&Date"><img src="https://api.star-history.com/svg?repos=wangzan101/Mika&type=Date" width="260" alt="wangzan101/Mika のスター推移グラフ"></a> |
| 2 | [caru-ini/stack-diagram](https://github.com/caru-ini/stack-diagram)<br>構成図を描くのが面倒？一文で公式ロゴ付き図が完成 | 2026-11-01<br><sub>2.7 日</sub> | 1,499 | 563.1 | <a href="https://www.star-history.com/#caru-ini/stack-diagram&Date"><img src="https://api.star-history.com/svg?repos=caru-ini/stack-diagram&type=Date" width="260" alt="caru-ini/stack-diagram のスター推移グラフ"></a> |
| 3 | [lexifina/global-law](https://github.com/lexifina/global-law)<br>Git for Global Law: the law of 700+ jurisdictions in git, each country's record a submodule where every commit is one change, dated by when it took effect and… | 2026-10-28<br><sub>6.3 日</sub> | 1,736 | 274.3 | <a href="https://www.star-history.com/#lexifina/global-law&Date"><img src="https://api.star-history.com/svg?repos=lexifina/global-law&type=Date" width="260" alt="lexifina/global-law のスター推移グラフ"></a> |
| 4 | [Balanov/uncut](https://github.com/Balanov/uncut)<br>勝手なコード切断を防ぎ、無損失でエージェントを動かす | 2026-11-01<br><sub>2.2 日</sub> | 589 | 271.1 | <a href="https://www.star-history.com/#Balanov/uncut&Date"><img src="https://api.star-history.com/svg?repos=Balanov/uncut&type=Date" width="260" alt="Balanov/uncut のスター推移グラフ"></a> |
| 5 | [Balanov/skein](https://github.com/Balanov/skein)<br>Fail-closed swarm orchestration with epoch-fenced work and late-completion rejection. | 2026-11-02<br><sub>1.0 日</sub> | 259 | 259.0 | <a href="https://www.star-history.com/#Balanov/skein&Date"><img src="https://api.star-history.com/svg?repos=Balanov/skein&type=Date" width="260" alt="Balanov/skein のスター推移グラフ"></a> |
| 6 | [mhfed/vn-law-check](https://github.com/mhfed/vn-law-check)<br>Audit pháp lý website theo luật Việt Nam (BVDLCN 91/2025, TMĐT 122/2025, ANM 116/2025, AI 134/2025) cho Claude Code, Cursor, Copilot, Windsurf, Cline | 2026-11-02<br><sub>1.5 日</sub> | 345 | 229.3 | <a href="https://www.star-history.com/#mhfed/vn-law-check&Date"><img src="https://api.star-history.com/svg?repos=mhfed/vn-law-check&type=Date" width="260" alt="mhfed/vn-law-check のスター推移グラフ"></a> |
| 7 | [NiazMorshed2007/reanimate](https://github.com/NiazMorshed2007/reanimate)<br>アニメ再現が難しい？1コマずつ解析して一致を証明 | 2026-10-29<br><sub>5.6 日</sub> | 1,081 | 192.0 | <a href="https://www.star-history.com/#NiazMorshed2007/reanimate&Date"><img src="https://api.star-history.com/svg?repos=NiazMorshed2007/reanimate&type=Date" width="260" alt="NiazMorshed2007/reanimate のスター推移グラフ"></a> |
| 8 | [N1nEmAn/sapper-v2](https://github.com/N1nEmAn/sapper-v2)<br>セキュリティ診断の手間を、AI自律テストで解消 | 2026-10-30<br><sub>4.3 日</sub> | 660 | 154.9 | <a href="https://www.star-history.com/#N1nEmAn/sapper-v2&Date"><img src="https://api.star-history.com/svg?repos=N1nEmAn/sapper-v2&type=Date" width="260" alt="N1nEmAn/sapper-v2 のスター推移グラフ"></a> |
| 9 | [zhanghao123vip/ai-manju-skills](https://github.com/zhanghao123vip/ai-manju-skills)<br>アイデア一つから AI 漫画動画の全工程を作成 | 2026-10-31<br><sub>3.8 日</sub> | 553 | 147.3 | <a href="https://www.star-history.com/#zhanghao123vip/ai-manju-skills&Date"><img src="https://api.star-history.com/svg?repos=zhanghao123vip/ai-manju-skills&type=Date" width="260" alt="zhanghao123vip/ai-manju-skills のスター推移グラフ"></a> |
| 10 | [sleepy-zone/ai-ref-library-cn](https://github.com/sleepy-zone/ai-ref-library-cn)<br>AI作画の参考が欲しい？顔・ポーズ・服装の素材集 | 2026-10-29<br><sub>5.2 日</sub> | 700 | 133.3 | <a href="https://www.star-history.com/#sleepy-zone/ai-ref-library-cn&Date"><img src="https://api.star-history.com/svg?repos=sleepy-zone/ai-ref-library-cn&type=Date" width="260" alt="sleepy-zone/ai-ref-library-cn のスター推移グラフ"></a> |

### 今週もっとも伸びた（直近 7 日）

| # | プロジェクト | 増加数 | スター/日 | 総スター数 | スター推移 |
|---|---|---:|---:|---:|---|
| 1 | [morluto/rea](https://github.com/morluto/rea)<br>AI でどんなソフトもクローンできる<br>`AI` | +31,598 | 4,514.0 | 426,698 | <a href="https://www.star-history.com/#morluto/rea&Date"><img src="https://api.star-history.com/svg?repos=morluto/rea&type=Date" width="260" alt="morluto/rea のスター推移グラフ"></a> |
| 2 | [cloudflare/security-audit-skill](https://github.com/cloudflare/security-audit-skill)<br>AI が脆弱性を探し、別の AI が一件ずつ検証<br>`AI` | +8,813 | 1,259.0 | 58,110 | <a href="https://www.star-history.com/#cloudflare/security-audit-skill&Date"><img src="https://api.star-history.com/svg?repos=cloudflare/security-audit-skill&type=Date" width="260" alt="cloudflare/security-audit-skill のスター推移グラフ"></a> |
| 3 | [thedotmack/claude-mem](https://github.com/thedotmack/claude-mem)<br>AI が前回の続きを忘れなくなる<br>`AI` | +7,744 | 1,106.3 | 111,761 | <a href="https://www.star-history.com/#thedotmack/claude-mem&Date"><img src="https://api.star-history.com/svg?repos=thedotmack/claude-mem&type=Date" width="260" alt="thedotmack/claude-mem のスター推移グラフ"></a> |
| 4 | [deepseek-ai/deepseek-harness](https://github.com/deepseek-ai/deepseek-harness)<br>欲しいエージェントは、プラグインで自分で組む<br>`AI` | +7,560 | 1,080.0 | 271,007 | <a href="https://www.star-history.com/#deepseek-ai/deepseek-harness&Date"><img src="https://api.star-history.com/svg?repos=deepseek-ai/deepseek-harness&type=Date" width="260" alt="deepseek-ai/deepseek-harness のスター推移グラフ"></a> |
| 5 | [stablyai/orca](https://github.com/stablyai/orca)<br>複数の AI に書かせて、どれが良いか一目で<br>`AI` | +6,769 | 967.0 | 114,427 | <a href="https://www.star-history.com/#stablyai/orca&Date"><img src="https://api.star-history.com/svg?repos=stablyai/orca&type=Date" width="260" alt="stablyai/orca のスター推移グラフ"></a> |
| 6 | [affaan-m/ECC](https://github.com/affaan-m/ECC)<br>コーディング AI に記憶・スキル・安全チェックを<br>`AI` | +6,127 | 875.3 | 296,480 | <a href="https://www.star-history.com/#affaan-m/ECC&Date"><img src="https://api.star-history.com/svg?repos=affaan-m/ECC&type=Date" width="260" alt="affaan-m/ECC のスター推移グラフ"></a> |
| 7 | [Leonxlnx/taste-skill](https://github.com/Leonxlnx/taste-skill)<br>AI が同じ見た目のページばかり作るのを止める<br>`AI` | +5,982 | 854.6 | 109,439 | <a href="https://www.star-history.com/#Leonxlnx/taste-skill&Date"><img src="https://api.star-history.com/svg?repos=Leonxlnx/taste-skill&type=Date" width="260" alt="Leonxlnx/taste-skill のスター推移グラフ"></a> |
| 8 | [DietrichGebert/ponytail](https://github.com/DietrichGebert/ponytail)<br>AI の無駄なコードを減らし、必要な所は正しく<br>`AI` | +5,913 | 844.7 | 183,670 | <a href="https://www.star-history.com/#DietrichGebert/ponytail&Date"><img src="https://api.star-history.com/svg?repos=DietrichGebert/ponytail&type=Date" width="260" alt="DietrichGebert/ponytail のスター推移グラフ"></a> |
| 9 | [yetone/magpie](https://github.com/yetone/magpie)<br>コーディング AI のモデルを替え、枠切れでも続行<br>`AI` | +5,883 | 840.4 | 29,038 | <a href="https://www.star-history.com/#yetone/magpie&Date"><img src="https://api.star-history.com/svg?repos=yetone/magpie&type=Date" width="260" alt="yetone/magpie のスター推移グラフ"></a> |
| 10 | [Graphify-Labs/graphify](https://github.com/Graphify-Labs/graphify)<br>大きすぎて読めない時は、まずこの地図から<br>`AI` | +5,187 | 741.0 | 141,784 | <a href="https://www.star-history.com/#Graphify-Labs/graphify&Date"><img src="https://api.star-history.com/svg?repos=Graphify-Labs/graphify&type=Date" width="260" alt="Graphify-Labs/graphify のスター推移グラフ"></a> |

### 今月もっとも伸びた（直近 30 日）

| # | プロジェクト | 増加数 | スター/日 | 総スター数 | スター推移 |
|---|---|---:|---:|---:|---|
| 1 | [morluto/rea](https://github.com/morluto/rea)<br>AI でどんなソフトもクローンできる<br>`AI` | +423,638 | 14,121.3 | 426,698 | <a href="https://www.star-history.com/#morluto/rea&Date"><img src="https://api.star-history.com/svg?repos=morluto/rea&type=Date" width="260" alt="morluto/rea のスター推移グラフ"></a> |
| 2 | [cloudflare/security-audit-skill](https://github.com/cloudflare/security-audit-skill)<br>AI が脆弱性を探し、別の AI が一件ずつ検証<br>`AI` | +33,901 | 1,130.0 | 58,110 | <a href="https://www.star-history.com/#cloudflare/security-audit-skill&Date"><img src="https://api.star-history.com/svg?repos=cloudflare/security-audit-skill&type=Date" width="260" alt="cloudflare/security-audit-skill のスター推移グラフ"></a> |
| 3 | [DietrichGebert/ponytail](https://github.com/DietrichGebert/ponytail)<br>AI の無駄なコードを減らし、必要な所は正しく<br>`AI` | +30,435 | 1,014.5 | 183,670 | <a href="https://www.star-history.com/#DietrichGebert/ponytail&Date"><img src="https://api.star-history.com/svg?repos=DietrichGebert/ponytail&type=Date" width="260" alt="DietrichGebert/ponytail のスター推移グラフ"></a> |
| 4 | [stablyai/orca](https://github.com/stablyai/orca)<br>複数の AI に書かせて、どれが良いか一目で<br>`AI` | +29,998 | 999.9 | 114,427 | <a href="https://www.star-history.com/#stablyai/orca&Date"><img src="https://api.star-history.com/svg?repos=stablyai/orca&type=Date" width="260" alt="stablyai/orca のスター推移グラフ"></a> |
| 5 | [deepseek-ai/deepseek-harness](https://github.com/deepseek-ai/deepseek-harness)<br>欲しいエージェントは、プラグインで自分で組む<br>`AI` | +28,619 | 954.0 | 271,007 | <a href="https://www.star-history.com/#deepseek-ai/deepseek-harness&Date"><img src="https://api.star-history.com/svg?repos=deepseek-ai/deepseek-harness&type=Date" width="260" alt="deepseek-ai/deepseek-harness のスター推移グラフ"></a> |
| 6 | [affaan-m/ECC](https://github.com/affaan-m/ECC)<br>コーディング AI に記憶・スキル・安全チェックを<br>`AI` | +25,102 | 836.7 | 296,480 | <a href="https://www.star-history.com/#affaan-m/ECC&Date"><img src="https://api.star-history.com/svg?repos=affaan-m/ECC&type=Date" width="260" alt="affaan-m/ECC のスター推移グラフ"></a> |
| 7 | [yetone/magpie](https://github.com/yetone/magpie)<br>コーディング AI のモデルを替え、枠切れでも続行<br>`AI` | +24,303 | 810.1 | 29,038 | <a href="https://www.star-history.com/#yetone/magpie&Date"><img src="https://api.star-history.com/svg?repos=yetone/magpie&type=Date" width="260" alt="yetone/magpie のスター推移グラフ"></a> |
| 8 | [heygen-com/hyperframes](https://github.com/heygen-com/hyperframes)<br>編集できなくても、Web ページ感覚で動画に<br>`AI` | +21,890 | 729.7 | 78,294 | <a href="https://www.star-history.com/#heygen-com/hyperframes&Date"><img src="https://api.star-history.com/svg?repos=heygen-com/hyperframes&type=Date" width="260" alt="heygen-com/hyperframes のスター推移グラフ"></a> |
| 9 | [Panniantong/Agent-Reach](https://github.com/Panniantong/Agent-Reach)<br>Twitter・YouTube・小紅書を AI が代わりに検索<br>`AI` | +18,655 | 621.8 | 108,407 | <a href="https://www.star-history.com/#Panniantong/Agent-Reach&Date"><img src="https://api.star-history.com/svg?repos=Panniantong/Agent-Reach&type=Date" width="260" alt="Panniantong/Agent-Reach のスター推移グラフ"></a> |
| 10 | [Graphify-Labs/graphify](https://github.com/Graphify-Labs/graphify)<br>大きすぎて読めない時は、まずこの地図から<br>`AI` | +18,609 | 620.3 | 141,784 | <a href="https://www.star-history.com/#Graphify-Labs/graphify&Date"><img src="https://api.star-history.com/svg?repos=Graphify-Labs/graphify&type=Date" width="260" alt="Graphify-Labs/graphify のスター推移グラフ"></a> |

### 今年もっとも伸びた（直近 365 日）

| # | プロジェクト | 増加数 | スター/日 | 総スター数 | スター推移 |
|---|---|---:|---:|---:|---|
| 1 | [deepseek-ai/deepseek-harness](https://github.com/deepseek-ai/deepseek-harness)<br>欲しいエージェントは、プラグインで自分で組む<br>`AI` | +270,174 | 3,294.8 †<br><sub>÷82日</sub> | 271,007 | <a href="https://www.star-history.com/#deepseek-ai/deepseek-harness&Date"><img src="https://api.star-history.com/svg?repos=deepseek-ai/deepseek-harness&type=Date" width="260" alt="deepseek-ai/deepseek-harness のスター推移グラフ"></a> |
| 2 | [morluto/rea](https://github.com/morluto/rea)<br>AI でどんなソフトもクローンできる<br>`AI` | +424,178 | 2,089.5 †<br><sub>÷203日</sub> | 426,698 | <a href="https://www.star-history.com/#morluto/rea&Date"><img src="https://api.star-history.com/svg?repos=morluto/rea&type=Date" width="260" alt="morluto/rea のスター推移グラフ"></a> |
| 3 | [DietrichGebert/ponytail](https://github.com/DietrichGebert/ponytail)<br>AI の無駄なコードを減らし、必要な所は正しく<br>`AI` | +183,129 | 1,271.7 †<br><sub>÷144日</sub> | 183,670 | <a href="https://www.star-history.com/#DietrichGebert/ponytail&Date"><img src="https://api.star-history.com/svg?repos=DietrichGebert/ponytail&type=Date" width="260" alt="DietrichGebert/ponytail のスター推移グラフ"></a> |
| 4 | [openclaw/openclaw](https://github.com/openclaw/openclaw)<br>仕事を片付ける AI アシスタント、動くのは自分の端末<br>`AI` | +393,754 | 1,144.6 †<br><sub>÷344日</sub> | 393,853 | <a href="https://www.star-history.com/#openclaw/openclaw&Date"><img src="https://api.star-history.com/svg?repos=openclaw/openclaw&type=Date" width="260" alt="openclaw/openclaw のスター推移グラフ"></a> |
| 5 | [affaan-m/ECC](https://github.com/affaan-m/ECC)<br>コーディング AI に記憶・スキル・安全チェックを<br>`AI` | +295,903 | 1,023.9 †<br><sub>÷289日</sub> | 296,480 | <a href="https://www.star-history.com/#affaan-m/ECC&Date"><img src="https://api.star-history.com/svg?repos=affaan-m/ECC&type=Date" width="260" alt="affaan-m/ECC のスター推移グラフ"></a> |
| 6 | [NousResearch/hermes-agent](https://github.com/NousResearch/hermes-agent)<br>使うほど仕事が上手くなる AI アシスタント<br>`AI` | +259,969 | 712.2 | 260,231 | <a href="https://www.star-history.com/#NousResearch/hermes-agent&Date"><img src="https://api.star-history.com/svg?repos=NousResearch/hermes-agent&type=Date" width="260" alt="NousResearch/hermes-agent のスター推移グラフ"></a> |
| 7 | [yetone/magpie](https://github.com/yetone/magpie)<br>コーディング AI のモデルを替え、枠切れでも続行<br>`AI` | +28,740 | 701.0 †<br><sub>÷41日</sub> | 29,038 | <a href="https://www.star-history.com/#yetone/magpie&Date"><img src="https://api.star-history.com/svg?repos=yetone/magpie&type=Date" width="260" alt="yetone/magpie のスター推移グラフ"></a> |
| 8 | [Graphify-Labs/graphify](https://github.com/Graphify-Labs/graphify)<br>大きすぎて読めない時は、まずこの地図から<br>`AI` | +141,393 | 660.7 †<br><sub>÷214日</sub> | 141,784 | <a href="https://www.star-history.com/#Graphify-Labs/graphify&Date"><img src="https://api.star-history.com/svg?repos=Graphify-Labs/graphify&type=Date" width="260" alt="Graphify-Labs/graphify のスター推移グラフ"></a> |
| 9 | [anomalyco/opencode](https://github.com/anomalyco/opencode)<br>ターミナルで、オープンソースの AI がコードを書く<br>`AI` | +194,814 | 533.7 | 224,332 | <a href="https://www.star-history.com/#anomalyco/opencode&Date"><img src="https://api.star-history.com/svg?repos=anomalyco/opencode&type=Date" width="260" alt="anomalyco/opencode のスター推移グラフ"></a> |
| 10 | [stablyai/orca](https://github.com/stablyai/orca)<br>複数の AI に書かせて、どれが良いか一目で<br>`AI` | +113,876 | 493.0 †<br><sub>÷231日</sub> | 114,427 | <a href="https://www.star-history.com/#stablyai/orca&Date"><img src="https://api.star-history.com/svg?repos=stablyai/orca&type=Date" width="260" alt="stablyai/orca のスター推移グラフ"></a> |

† リポジトリの作成が集計期間より新しいため、スター/日は期間全体ではなくリポジトリの経過日数（数値の下に表示）で割っています。

### 総スター数ランキング（累計）

| # | プロジェクト | 総スター数 | スター推移 |
|---|---|---:|---|
| 1 | [morluto/rea](https://github.com/morluto/rea)<br>AI でどんなソフトもクローンできる<br>`AI` | 426,698 | <a href="https://www.star-history.com/#morluto/rea&Date"><img src="https://api.star-history.com/svg?repos=morluto/rea&type=Date" width="260" alt="morluto/rea のスター推移グラフ"></a> |
| 2 | [openclaw/openclaw](https://github.com/openclaw/openclaw)<br>仕事を片付ける AI アシスタント、動くのは自分の端末<br>`AI` | 393,853 | <a href="https://www.star-history.com/#openclaw/openclaw&Date"><img src="https://api.star-history.com/svg?repos=openclaw/openclaw&type=Date" width="260" alt="openclaw/openclaw のスター推移グラフ"></a> |
| 3 | [affaan-m/ECC](https://github.com/affaan-m/ECC)<br>コーディング AI に記憶・スキル・安全チェックを<br>`AI` | 296,480 | <a href="https://www.star-history.com/#affaan-m/ECC&Date"><img src="https://api.star-history.com/svg?repos=affaan-m/ECC&type=Date" width="260" alt="affaan-m/ECC のスター推移グラフ"></a> |
| 4 | [deepseek-ai/deepseek-harness](https://github.com/deepseek-ai/deepseek-harness)<br>欲しいエージェントは、プラグインで自分で組む<br>`AI` | 271,007 | <a href="https://www.star-history.com/#deepseek-ai/deepseek-harness&Date"><img src="https://api.star-history.com/svg?repos=deepseek-ai/deepseek-harness&type=Date" width="260" alt="deepseek-ai/deepseek-harness のスター推移グラフ"></a> |
| 5 | [NousResearch/hermes-agent](https://github.com/NousResearch/hermes-agent)<br>使うほど仕事が上手くなる AI アシスタント<br>`AI` | 260,231 | <a href="https://www.star-history.com/#NousResearch/hermes-agent&Date"><img src="https://api.star-history.com/svg?repos=NousResearch/hermes-agent&type=Date" width="260" alt="NousResearch/hermes-agent のスター推移グラフ"></a> |
| 6 | [anomalyco/opencode](https://github.com/anomalyco/opencode)<br>ターミナルで、オープンソースの AI がコードを書く<br>`AI` | 224,332 | <a href="https://www.star-history.com/#anomalyco/opencode&Date"><img src="https://api.star-history.com/svg?repos=anomalyco/opencode&type=Date" width="260" alt="anomalyco/opencode のスター推移グラフ"></a> |
| 7 | [anthropics/skills](https://github.com/anthropics/skills)<br>Claude スキルの書き方は、公式の例で学ぶ<br>`AI` | 187,076 | <a href="https://www.star-history.com/#anthropics/skills&Date"><img src="https://api.star-history.com/svg?repos=anthropics/skills&type=Date" width="260" alt="anthropics/skills のスター推移グラフ"></a> |
| 8 | [DietrichGebert/ponytail](https://github.com/DietrichGebert/ponytail)<br>AI の無駄なコードを減らし、必要な所は正しく<br>`AI` | 183,670 | <a href="https://www.star-history.com/#DietrichGebert/ponytail&Date"><img src="https://api.star-history.com/svg?repos=DietrichGebert/ponytail&type=Date" width="260" alt="DietrichGebert/ponytail のスター推移グラフ"></a> |
| 9 | [farion1231/cc-switch](https://github.com/farion1231/cc-switch)<br>設定ファイルを触らず、ワンクリックで切替<br>`AI` | 151,513 | <a href="https://www.star-history.com/#farion1231/cc-switch&Date"><img src="https://api.star-history.com/svg?repos=farion1231/cc-switch&type=Date" width="260" alt="farion1231/cc-switch のスター推移グラフ"></a> |
| 10 | [nextlevelbuilder/ui-ux-pro-max-skill](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill)<br>AI が作る画面を、プロのデザインらしく<br>`AI` | 144,735 | <a href="https://www.star-history.com/#nextlevelbuilder/ui-ux-pro-max-skill&Date"><img src="https://api.star-history.com/svg?repos=nextlevelbuilder/ui-ux-pro-max-skill&type=Date" width="260" alt="nextlevelbuilder/ui-ux-pro-max-skill のスター推移グラフ"></a> |

## 開発者ツール

> CLI・エディタ・パッケージマネージャ・リンタ・ビルドツール

### 7 日以内の新着で最も熱いリポジトリ（作成から 7 日以内）

| # | プロジェクト | 作成日（UTC） | 総スター数 | スター/日 | スター推移 |
|---|---|---|---:|---:|---|
| 1 | [Verlintas/NOIR](https://github.com/Verlintas/NOIR)<br>Android アプリの情報漏えいをスキャンして安全に対処 | 2026-10-31<br><sub>3.0 日</sub> | 1,750 | 584.2 | <a href="https://www.star-history.com/#Verlintas/NOIR&Date"><img src="https://api.star-history.com/svg?repos=Verlintas/NOIR&type=Date" width="260" alt="Verlintas/NOIR のスター推移グラフ"></a> |
| 2 | [AssassinCreator/steam-stash-value-report-card](https://github.com/AssassinCreator/steam-stash-value-report-card)<br>在庫価値が不明なら、ターミナルでSteamを査定 | 2026-11-02<br><sub>1.9 日</sub> | 698 | 374.0 | <a href="https://www.star-history.com/#AssassinCreator/steam-stash-value-report-card&Date"><img src="https://api.star-history.com/svg?repos=AssassinCreator/steam-stash-value-report-card&type=Date" width="260" alt="AssassinCreator/steam-stash-value-report-card のスター推移グラフ"></a> |
| 3 | [MomentumGuideContact/fonetrans](https://github.com/MomentumGuideContact/fonetrans)<br>Complete Fonetrans desktop edition 2026, ready-to-run with all features fully activated. | 2026-11-03<br><sub>1.0 日</sub> | 299 | 299.0 | <a href="https://www.star-history.com/#MomentumGuideContact/fonetrans&Date"><img src="https://api.star-history.com/svg?repos=MomentumGuideContact/fonetrans&type=Date" width="260" alt="MomentumGuideContact/fonetrans のスター推移グラフ"></a> |
| 4 | [exzade/EXZA-Remote](https://github.com/exzade/EXZA-Remote)<br>Secure AI-powered remote computer access for ChatGPT, Claude and compatible MCP clients. | 2026-11-02<br><sub>1.5 日</sub> | 176 | 119.3 | <a href="https://www.star-history.com/#exzade/EXZA-Remote&Date"><img src="https://api.star-history.com/svg?repos=exzade/EXZA-Remote&type=Date" width="260" alt="exzade/EXZA-Remote のスター推移グラフ"></a> |
| 5 | [slateoriolewreck/ios-unlocker](https://github.com/slateoriolewreck/ios-unlocker)<br>Complete standalone iOS Unlocker 2026 installation build, fully functional with no activation needed. | 2026-11-03<br><sub>1.0 日</sub> | 100 | 100.0 | <a href="https://www.star-history.com/#slateoriolewreck/ios-unlocker&Date"><img src="https://api.star-history.com/svg?repos=slateoriolewreck/ios-unlocker&type=Date" width="260" alt="slateoriolewreck/ios-unlocker のスター推移グラフ"></a> |
| 6 | [Straitbrashadow/minecraft-ai-mod-builder](https://github.com/Straitbrashadow/minecraft-ai-mod-builder)<br>Vibe-build in Minecraft. Describe a build in your terminal, see it as a blueprint in your world, place it in one step and undo it in one. Writes datapacks too.… | 2026-10-30<br><sub>4.0 日</sub> | 200 | 49.9 | <a href="https://www.star-history.com/#Straitbrashadow/minecraft-ai-mod-builder&Date"><img src="https://api.star-history.com/svg?repos=Straitbrashadow/minecraft-ai-mod-builder&type=Date" width="260" alt="Straitbrashadow/minecraft-ai-mod-builder のスター推移グラフ"></a> |
| 7 | [UncensoredLabs/uncensored-ai-api](https://github.com/UncensoredLabs/uncensored-ai-api)<br>Uncensored AI API and browser chat: DeepSeek and GLM models, streaming, Python and TypeScript examples, pricing and setup guides. | 2026-11-01<br><sub>2.0 日</sub> | 101 | 49.9 | <a href="https://www.star-history.com/#UncensoredLabs/uncensored-ai-api&Date"><img src="https://api.star-history.com/svg?repos=UncensoredLabs/uncensored-ai-api&type=Date" width="260" alt="UncensoredLabs/uncensored-ai-api のスター推移グラフ"></a> |
| 8 | [Xpropel/Pi-Remote](https://github.com/Xpropel/Pi-Remote)<br>ブラウザからpiのコーディングエージェントを遠隔操作 | 2026-10-28<br><sub>6.5 日</sub> | 291 | 45.1 | <a href="https://www.star-history.com/#Xpropel/Pi-Remote&Date"><img src="https://api.star-history.com/svg?repos=Xpropel/Pi-Remote&type=Date" width="260" alt="Xpropel/Pi-Remote のスター推移グラフ"></a> |
| 9 | [muaaz9329/cheap-ag](https://github.com/muaaz9329/cheap-ag)<br>制限を気にせず安価なモデルでコードを書く | 2026-10-28<br><sub>6.0 日</sub> | 250 | 41.9 | <a href="https://www.star-history.com/#muaaz9329/cheap-ag&Date"><img src="https://api.star-history.com/svg?repos=muaaz9329/cheap-ag&type=Date" width="260" alt="muaaz9329/cheap-ag のスター推移グラフ"></a> |
| 10 | [DiplomatHearth/roblox-ai-place-diff](https://github.com/DiplomatHearth/roblox-ai-place-diff)<br>エージェントの変更を確認してから適用 | 2026-10-30<br><sub>4.0 日</sub> | 163 | 40.9 | <a href="https://www.star-history.com/#DiplomatHearth/roblox-ai-place-diff&Date"><img src="https://api.star-history.com/svg?repos=DiplomatHearth/roblox-ai-place-diff&type=Date" width="260" alt="DiplomatHearth/roblox-ai-place-diff のスター推移グラフ"></a> |

### 今週もっとも伸びた（直近 7 日）

| # | プロジェクト | 増加数 | スター/日 | 総スター数 | スター推移 |
|---|---|---:|---:|---:|---|
| 1 | [zed-industries/zed](https://github.com/zed-industries/zed)<br>すぐ開けて、みんなで一緒にコードを書ける<br>`開発者ツール` | +415 | 59.3 | 92,634 | <a href="https://www.star-history.com/#zed-industries/zed&Date"><img src="https://api.star-history.com/svg?repos=zed-industries/zed&type=Date" width="260" alt="zed-industries/zed のスター推移グラフ"></a> |
| 2 | [astral-sh/uv](https://github.com/astral-sh/uv)<br>Python パッケージの導入で待たされない<br>`開発者ツール` | +310 | 44.3 | 91,509 | <a href="https://www.star-history.com/#astral-sh/uv&Date"><img src="https://api.star-history.com/svg?repos=astral-sh/uv&type=Date" width="260" alt="astral-sh/uv のスター推移グラフ"></a> |
| 3 | [jdx/mise](https://github.com/jdx/mise)<br>開発ツール・環境変数・タスクを 1 つで管理<br>`開発者ツール` | +291 | 41.6 | 35,726 | <a href="https://www.star-history.com/#jdx/mise&Date"><img src="https://api.star-history.com/svg?repos=jdx/mise&type=Date" width="260" alt="jdx/mise のスター推移グラフ"></a> |
| 4 | [BurntSushi/ripgrep](https://github.com/BurntSushi/ripgrep)<br>フォルダ全体の文字検索が grep より速い<br>`開発者ツール` | +227 | 32.4 | 69,672 | <a href="https://www.star-history.com/#BurntSushi/ripgrep&Date"><img src="https://api.star-history.com/svg?repos=BurntSushi/ripgrep&type=Date" width="260" alt="BurntSushi/ripgrep のスター推移グラフ"></a> |
| 5 | [oven-sh/bun](https://github.com/oven-sh/bun)<br>実行・バンドル・テスト・導入を 1 つで<br>`開発者ツール` | +137 | 19.6 | 96,532 | <a href="https://www.star-history.com/#oven-sh/bun&Date"><img src="https://api.star-history.com/svg?repos=oven-sh/bun&type=Date" width="260" alt="oven-sh/bun のスター推移グラフ"></a> |
| 6 | [cli/cli](https://github.com/cli/cli)<br>ブラウザを開かず、コマンドラインで GitHub を操作<br>`開発者ツール` | +107 | 15.3 | 46,857 | <a href="https://www.star-history.com/#cli/cli&Date"><img src="https://api.star-history.com/svg?repos=cli/cli&type=Date" width="260" alt="cli/cli のスター推移グラフ"></a> |
| 7 | [helix-editor/helix](https://github.com/helix-editor/helix)<br>構文ハイライトも言語サーバーも内蔵のテキストエディタ<br>`開発者ツール` | +98 | 14.0 | 46,778 | <a href="https://www.star-history.com/#helix-editor/helix&Date"><img src="https://api.star-history.com/svg?repos=helix-editor/helix&type=Date" width="260" alt="helix-editor/helix のスター推移グラフ"></a> |
| 8 | [biomejs/biome](https://github.com/biomejs/biome)<br>Web コードの整形とチェックを 1 つで<br>`開発者ツール` | +47 | 6.7 | 26,046 | <a href="https://www.star-history.com/#biomejs/biome&Date"><img src="https://api.star-history.com/svg?repos=biomejs/biome&type=Date" width="260" alt="biomejs/biome のスター推移グラフ"></a> |

### 今月もっとも伸びた（直近 30 日）

| # | プロジェクト | 増加数 | スター/日 | 総スター数 | スター推移 |
|---|---|---:|---:|---:|---|
| 1 | [zed-industries/zed](https://github.com/zed-industries/zed)<br>すぐ開けて、みんなで一緒にコードを書ける<br>`開発者ツール` | +1,624 | 54.1 | 92,634 | <a href="https://www.star-history.com/#zed-industries/zed&Date"><img src="https://api.star-history.com/svg?repos=zed-industries/zed&type=Date" width="260" alt="zed-industries/zed のスター推移グラフ"></a> |
| 2 | [astral-sh/uv](https://github.com/astral-sh/uv)<br>Python パッケージの導入で待たされない<br>`開発者ツール` | +1,280 | 42.7 | 91,509 | <a href="https://www.star-history.com/#astral-sh/uv&Date"><img src="https://api.star-history.com/svg?repos=astral-sh/uv&type=Date" width="260" alt="astral-sh/uv のスター推移グラフ"></a> |
| 3 | [jdx/mise](https://github.com/jdx/mise)<br>開発ツール・環境変数・タスクを 1 つで管理<br>`開発者ツール` | +1,229 | 41.0 | 35,726 | <a href="https://www.star-history.com/#jdx/mise&Date"><img src="https://api.star-history.com/svg?repos=jdx/mise&type=Date" width="260" alt="jdx/mise のスター推移グラフ"></a> |
| 4 | [BurntSushi/ripgrep](https://github.com/BurntSushi/ripgrep)<br>フォルダ全体の文字検索が grep より速い<br>`開発者ツール` | +991 | 33.0 | 69,672 | <a href="https://www.star-history.com/#BurntSushi/ripgrep&Date"><img src="https://api.star-history.com/svg?repos=BurntSushi/ripgrep&type=Date" width="260" alt="BurntSushi/ripgrep のスター推移グラフ"></a> |
| 5 | [oven-sh/bun](https://github.com/oven-sh/bun)<br>実行・バンドル・テスト・導入を 1 つで<br>`開発者ツール` | +694 | 23.1 | 96,532 | <a href="https://www.star-history.com/#oven-sh/bun&Date"><img src="https://api.star-history.com/svg?repos=oven-sh/bun&type=Date" width="260" alt="oven-sh/bun のスター推移グラフ"></a> |
| 6 | [helix-editor/helix](https://github.com/helix-editor/helix)<br>構文ハイライトも言語サーバーも内蔵のテキストエディタ<br>`開発者ツール` | +445 | 14.8 | 46,778 | <a href="https://www.star-history.com/#helix-editor/helix&Date"><img src="https://api.star-history.com/svg?repos=helix-editor/helix&type=Date" width="260" alt="helix-editor/helix のスター推移グラフ"></a> |
| 7 | [cli/cli](https://github.com/cli/cli)<br>ブラウザを開かず、コマンドラインで GitHub を操作<br>`開発者ツール` | +424 | 14.1 | 46,857 | <a href="https://www.star-history.com/#cli/cli&Date"><img src="https://api.star-history.com/svg?repos=cli/cli&type=Date" width="260" alt="cli/cli のスター推移グラフ"></a> |
| 8 | [biomejs/biome](https://github.com/biomejs/biome)<br>Web コードの整形とチェックを 1 つで<br>`開発者ツール` | +214 | 7.1 | 26,046 | <a href="https://www.star-history.com/#biomejs/biome&Date"><img src="https://api.star-history.com/svg?repos=biomejs/biome&type=Date" width="260" alt="biomejs/biome のスター推移グラフ"></a> |

### 今年もっとも伸びた（直近 365 日）

| # | プロジェクト | 増加数 | スター/日 | 総スター数 | スター推移 |
|---|---|---:|---:|---:|---|
| 1 | [zed-industries/zed](https://github.com/zed-industries/zed)<br>すぐ開けて、みんなで一緒にコードを書ける<br>`開発者ツール` | +25,676 | 70.3 | 92,634 | <a href="https://www.star-history.com/#zed-industries/zed&Date"><img src="https://api.star-history.com/svg?repos=zed-industries/zed&type=Date" width="260" alt="zed-industries/zed のスター推移グラフ"></a> |
| 2 | [astral-sh/uv](https://github.com/astral-sh/uv)<br>Python パッケージの導入で待たされない<br>`開発者ツール` | +21,265 | 58.3 | 91,509 | <a href="https://www.star-history.com/#astral-sh/uv&Date"><img src="https://api.star-history.com/svg?repos=astral-sh/uv&type=Date" width="260" alt="astral-sh/uv のスター推移グラフ"></a> |
| 3 | [oven-sh/bun](https://github.com/oven-sh/bun)<br>実行・バンドル・テスト・導入を 1 つで<br>`開発者ツール` | +16,559 | 45.4 | 96,532 | <a href="https://www.star-history.com/#oven-sh/bun&Date"><img src="https://api.star-history.com/svg?repos=oven-sh/bun&type=Date" width="260" alt="oven-sh/bun のスター推移グラフ"></a> |
| 4 | [jdx/mise](https://github.com/jdx/mise)<br>開発ツール・環境変数・タスクを 1 つで管理<br>`開発者ツール` | +15,084 | 41.3 | 35,726 | <a href="https://www.star-history.com/#jdx/mise&Date"><img src="https://api.star-history.com/svg?repos=jdx/mise&type=Date" width="260" alt="jdx/mise のスター推移グラフ"></a> |
| 5 | [BurntSushi/ripgrep](https://github.com/BurntSushi/ripgrep)<br>フォルダ全体の文字検索が grep より速い<br>`開発者ツール` | +13,364 | 36.6 | 69,672 | <a href="https://www.star-history.com/#BurntSushi/ripgrep&Date"><img src="https://api.star-history.com/svg?repos=BurntSushi/ripgrep&type=Date" width="260" alt="BurntSushi/ripgrep のスター推移グラフ"></a> |
| 6 | [helix-editor/helix](https://github.com/helix-editor/helix)<br>構文ハイライトも言語サーバーも内蔵のテキストエディタ<br>`開発者ツール` | +6,702 | 18.4 | 46,778 | <a href="https://www.star-history.com/#helix-editor/helix&Date"><img src="https://api.star-history.com/svg?repos=helix-editor/helix&type=Date" width="260" alt="helix-editor/helix のスター推移グラフ"></a> |
| 7 | [cli/cli](https://github.com/cli/cli)<br>ブラウザを開かず、コマンドラインで GitHub を操作<br>`開発者ツール` | +6,262 | 17.2 | 46,857 | <a href="https://www.star-history.com/#cli/cli&Date"><img src="https://api.star-history.com/svg?repos=cli/cli&type=Date" width="260" alt="cli/cli のスター推移グラフ"></a> |
| 8 | [biomejs/biome](https://github.com/biomejs/biome)<br>Web コードの整形とチェックを 1 つで<br>`開発者ツール` | +4,571 | 12.5 | 26,046 | <a href="https://www.star-history.com/#biomejs/biome&Date"><img src="https://api.star-history.com/svg?repos=biomejs/biome&type=Date" width="260" alt="biomejs/biome のスター推移グラフ"></a> |

### 総スター数ランキング（累計）

| # | プロジェクト | 総スター数 | スター推移 |
|---|---|---:|---|
| 1 | [oven-sh/bun](https://github.com/oven-sh/bun)<br>実行・バンドル・テスト・導入を 1 つで<br>`開発者ツール` | 96,532 | <a href="https://www.star-history.com/#oven-sh/bun&Date"><img src="https://api.star-history.com/svg?repos=oven-sh/bun&type=Date" width="260" alt="oven-sh/bun のスター推移グラフ"></a> |
| 2 | [zed-industries/zed](https://github.com/zed-industries/zed)<br>すぐ開けて、みんなで一緒にコードを書ける<br>`開発者ツール` | 92,634 | <a href="https://www.star-history.com/#zed-industries/zed&Date"><img src="https://api.star-history.com/svg?repos=zed-industries/zed&type=Date" width="260" alt="zed-industries/zed のスター推移グラフ"></a> |
| 3 | [astral-sh/uv](https://github.com/astral-sh/uv)<br>Python パッケージの導入で待たされない<br>`開発者ツール` | 91,509 | <a href="https://www.star-history.com/#astral-sh/uv&Date"><img src="https://api.star-history.com/svg?repos=astral-sh/uv&type=Date" width="260" alt="astral-sh/uv のスター推移グラフ"></a> |
| 4 | [BurntSushi/ripgrep](https://github.com/BurntSushi/ripgrep)<br>フォルダ全体の文字検索が grep より速い<br>`開発者ツール` | 69,672 | <a href="https://www.star-history.com/#BurntSushi/ripgrep&Date"><img src="https://api.star-history.com/svg?repos=BurntSushi/ripgrep&type=Date" width="260" alt="BurntSushi/ripgrep のスター推移グラフ"></a> |
| 5 | [cli/cli](https://github.com/cli/cli)<br>ブラウザを開かず、コマンドラインで GitHub を操作<br>`開発者ツール` | 46,857 | <a href="https://www.star-history.com/#cli/cli&Date"><img src="https://api.star-history.com/svg?repos=cli/cli&type=Date" width="260" alt="cli/cli のスター推移グラフ"></a> |
| 6 | [helix-editor/helix](https://github.com/helix-editor/helix)<br>構文ハイライトも言語サーバーも内蔵のテキストエディタ<br>`開発者ツール` | 46,778 | <a href="https://www.star-history.com/#helix-editor/helix&Date"><img src="https://api.star-history.com/svg?repos=helix-editor/helix&type=Date" width="260" alt="helix-editor/helix のスター推移グラフ"></a> |
| 7 | [jdx/mise](https://github.com/jdx/mise)<br>開発ツール・環境変数・タスクを 1 つで管理<br>`開発者ツール` | 35,726 | <a href="https://www.star-history.com/#jdx/mise&Date"><img src="https://api.star-history.com/svg?repos=jdx/mise&type=Date" width="260" alt="jdx/mise のスター推移グラフ"></a> |
| 8 | [biomejs/biome](https://github.com/biomejs/biome)<br>Web コードの整形とチェックを 1 つで<br>`開発者ツール` | 26,046 | <a href="https://www.star-history.com/#biomejs/biome&Date"><img src="https://api.star-history.com/svg?repos=biomejs/biome&type=Date" width="260" alt="biomejs/biome のスター推移グラフ"></a> |

## セキュリティ

> 脆弱性スキャン・SAST・サプライチェーン・ランタイムセキュリティ

### 7 日以内の新着で最も熱いリポジトリ（作成から 7 日以内）

今回の実行で条件を満たす新着リポジトリはありませんでした。

### 今週もっとも伸びた（直近 7 日）

| # | プロジェクト | 増加数 | スター/日 | 総スター数 | スター推移 |
|---|---|---:|---:|---:|---|
| 1 | [projectdiscovery/nuclei](https://github.com/projectdiscovery/nuclei)<br>テンプレート 1 つで、脆弱性を一括スキャン<br>`セキュリティ` | +206 | 29.4 | 32,568 | <a href="https://www.star-history.com/#projectdiscovery/nuclei&Date"><img src="https://api.star-history.com/svg?repos=projectdiscovery/nuclei&type=Date" width="260" alt="projectdiscovery/nuclei のスター推移グラフ"></a> |
| 2 | [aquasecurity/trivy](https://github.com/aquasecurity/trivy)<br>コンテナもコードも、安全チェックは 1 回で<br>`セキュリティ` | +182 | 26.0 | 38,941 | <a href="https://www.star-history.com/#aquasecurity/trivy&Date"><img src="https://api.star-history.com/svg?repos=aquasecurity/trivy&type=Date" width="260" alt="aquasecurity/trivy のスター推移グラフ"></a> |
| 3 | [semgrep/semgrep](https://github.com/semgrep/semgrep)<br>コードの問題は、コミット前に見つけ出す<br>`セキュリティ` | +119 | 17.0 | 17,430 | <a href="https://www.star-history.com/#semgrep/semgrep&Date"><img src="https://api.star-history.com/svg?repos=semgrep/semgrep&type=Date" width="260" alt="semgrep/semgrep のスター推移グラフ"></a> |
| 4 | [OWASP/CheatSheetSeries](https://github.com/OWASP/CheatSheetSeries)<br>アプリのセキュリティは、この簡潔な手引きで<br>`セキュリティ` | +106 | 15.1 | 33,869 | <a href="https://www.star-history.com/#OWASP/CheatSheetSeries&Date"><img src="https://api.star-history.com/svg?repos=OWASP/CheatSheetSeries&type=Date" width="260" alt="OWASP/CheatSheetSeries のスター推移グラフ"></a> |
| 5 | [google/osv-scanner](https://github.com/google/osv-scanner)<br>使っている依存は安全か、スキャンすればわかる<br>`セキュリティ` | +94 | 13.4 | 11,382 | <a href="https://www.star-history.com/#google/osv-scanner&Date"><img src="https://api.star-history.com/svg?repos=google/osv-scanner&type=Date" width="260" alt="google/osv-scanner のスター推移グラフ"></a> |
| 6 | [anchore/grype](https://github.com/anchore/grype)<br>コンテナイメージに脆弱性がないか、スキャンで確認<br>`セキュリティ` | +54 | 7.7 | 13,170 | <a href="https://www.star-history.com/#anchore/grype&Date"><img src="https://api.star-history.com/svg?repos=anchore/grype&type=Date" width="260" alt="anchore/grype のスター推移グラフ"></a> |
| 7 | [falcosecurity/falco](https://github.com/falcosecurity/falco)<br>クラウドの異常に、すぐ気づける<br>`セキュリティ` | +22 | 3.1 | 9,548 | <a href="https://www.star-history.com/#falcosecurity/falco&Date"><img src="https://api.star-history.com/svg?repos=falcosecurity/falco&type=Date" width="260" alt="falcosecurity/falco のスター推移グラフ"></a> |
| 8 | [securego/gosec](https://github.com/securego/gosec)<br>Go コードのセキュリティ問題を、スキャンで見つける<br>`セキュリティ` | +9 | 1.3 | 8,997 | <a href="https://www.star-history.com/#securego/gosec&Date"><img src="https://api.star-history.com/svg?repos=securego/gosec&type=Date" width="260" alt="securego/gosec のスター推移グラフ"></a> |

### 今月もっとも伸びた（直近 30 日）

| # | プロジェクト | 増加数 | スター/日 | 総スター数 | スター推移 |
|---|---|---:|---:|---:|---|
| 1 | [projectdiscovery/nuclei](https://github.com/projectdiscovery/nuclei)<br>テンプレート 1 つで、脆弱性を一括スキャン<br>`セキュリティ` | +922 | 30.7 | 32,568 | <a href="https://www.star-history.com/#projectdiscovery/nuclei&Date"><img src="https://api.star-history.com/svg?repos=projectdiscovery/nuclei&type=Date" width="260" alt="projectdiscovery/nuclei のスター推移グラフ"></a> |
| 2 | [aquasecurity/trivy](https://github.com/aquasecurity/trivy)<br>コンテナもコードも、安全チェックは 1 回で<br>`セキュリティ` | +767 | 25.6 | 38,941 | <a href="https://www.star-history.com/#aquasecurity/trivy&Date"><img src="https://api.star-history.com/svg?repos=aquasecurity/trivy&type=Date" width="260" alt="aquasecurity/trivy のスター推移グラフ"></a> |
| 3 | [semgrep/semgrep](https://github.com/semgrep/semgrep)<br>コードの問題は、コミット前に見つけ出す<br>`セキュリティ` | +581 | 19.4 | 17,430 | <a href="https://www.star-history.com/#semgrep/semgrep&Date"><img src="https://api.star-history.com/svg?repos=semgrep/semgrep&type=Date" width="260" alt="semgrep/semgrep のスター推移グラフ"></a> |
| 4 | [OWASP/CheatSheetSeries](https://github.com/OWASP/CheatSheetSeries)<br>アプリのセキュリティは、この簡潔な手引きで<br>`セキュリティ` | +474 | 15.8 | 33,869 | <a href="https://www.star-history.com/#OWASP/CheatSheetSeries&Date"><img src="https://api.star-history.com/svg?repos=OWASP/CheatSheetSeries&type=Date" width="260" alt="OWASP/CheatSheetSeries のスター推移グラフ"></a> |
| 5 | [google/osv-scanner](https://github.com/google/osv-scanner)<br>使っている依存は安全か、スキャンすればわかる<br>`セキュリティ` | +258 | 8.6 | 11,382 | <a href="https://www.star-history.com/#google/osv-scanner&Date"><img src="https://api.star-history.com/svg?repos=google/osv-scanner&type=Date" width="260" alt="google/osv-scanner のスター推移グラフ"></a> |
| 6 | [anchore/grype](https://github.com/anchore/grype)<br>コンテナイメージに脆弱性がないか、スキャンで確認<br>`セキュリティ` | +206 | 6.9 | 13,170 | <a href="https://www.star-history.com/#anchore/grype&Date"><img src="https://api.star-history.com/svg?repos=anchore/grype&type=Date" width="260" alt="anchore/grype のスター推移グラフ"></a> |
| 7 | [falcosecurity/falco](https://github.com/falcosecurity/falco)<br>クラウドの異常に、すぐ気づける<br>`セキュリティ` | +123 | 4.1 | 9,548 | <a href="https://www.star-history.com/#falcosecurity/falco&Date"><img src="https://api.star-history.com/svg?repos=falcosecurity/falco&type=Date" width="260" alt="falcosecurity/falco のスター推移グラフ"></a> |
| 8 | [securego/gosec](https://github.com/securego/gosec)<br>Go コードのセキュリティ問題を、スキャンで見つける<br>`セキュリティ` | +43 | 1.4 | 8,997 | <a href="https://www.star-history.com/#securego/gosec&Date"><img src="https://api.star-history.com/svg?repos=securego/gosec&type=Date" width="260" alt="securego/gosec のスター推移グラフ"></a> |

### 今年もっとも伸びた（直近 365 日）

| # | プロジェクト | 増加数 | スター/日 | 総スター数 | スター推移 |
|---|---|---:|---:|---:|---|
| 1 | [aquasecurity/trivy](https://github.com/aquasecurity/trivy)<br>コンテナもコードも、安全チェックは 1 回で<br>`セキュリティ` | +10,103 | 27.7 | 38,941 | <a href="https://www.star-history.com/#aquasecurity/trivy&Date"><img src="https://api.star-history.com/svg?repos=aquasecurity/trivy&type=Date" width="260" alt="aquasecurity/trivy のスター推移グラフ"></a> |
| 2 | [projectdiscovery/nuclei](https://github.com/projectdiscovery/nuclei)<br>テンプレート 1 つで、脆弱性を一括スキャン<br>`セキュリティ` | +7,610 | 20.8 | 32,568 | <a href="https://www.star-history.com/#projectdiscovery/nuclei&Date"><img src="https://api.star-history.com/svg?repos=projectdiscovery/nuclei&type=Date" width="260" alt="projectdiscovery/nuclei のスター推移グラフ"></a> |
| 3 | [semgrep/semgrep](https://github.com/semgrep/semgrep)<br>コードの問題は、コミット前に見つけ出す<br>`セキュリティ` | +4,377 | 12.0 | 17,430 | <a href="https://www.star-history.com/#semgrep/semgrep&Date"><img src="https://api.star-history.com/svg?repos=semgrep/semgrep&type=Date" width="260" alt="semgrep/semgrep のスター推移グラフ"></a> |
| 4 | [OWASP/CheatSheetSeries](https://github.com/OWASP/CheatSheetSeries)<br>アプリのセキュリティは、この簡潔な手引きで<br>`セキュリティ` | +3,531 | 9.7 | 33,869 | <a href="https://www.star-history.com/#OWASP/CheatSheetSeries&Date"><img src="https://api.star-history.com/svg?repos=OWASP/CheatSheetSeries&type=Date" width="260" alt="OWASP/CheatSheetSeries のスター推移グラフ"></a> |
| 5 | [google/osv-scanner](https://github.com/google/osv-scanner)<br>使っている依存は安全か、スキャンすればわかる<br>`セキュリティ` | +3,502 | 9.6 | 11,382 | <a href="https://www.star-history.com/#google/osv-scanner&Date"><img src="https://api.star-history.com/svg?repos=google/osv-scanner&type=Date" width="260" alt="google/osv-scanner のスター推移グラフ"></a> |
| 6 | [anchore/grype](https://github.com/anchore/grype)<br>コンテナイメージに脆弱性がないか、スキャンで確認<br>`セキュリティ` | +2,356 | 6.5 | 13,170 | <a href="https://www.star-history.com/#anchore/grype&Date"><img src="https://api.star-history.com/svg?repos=anchore/grype&type=Date" width="260" alt="anchore/grype のスター推移グラフ"></a> |
| 7 | [falcosecurity/falco](https://github.com/falcosecurity/falco)<br>クラウドの異常に、すぐ気づける<br>`セキュリティ` | +1,267 | 3.5 | 9,548 | <a href="https://www.star-history.com/#falcosecurity/falco&Date"><img src="https://api.star-history.com/svg?repos=falcosecurity/falco&type=Date" width="260" alt="falcosecurity/falco のスター推移グラフ"></a> |
| 8 | [securego/gosec](https://github.com/securego/gosec)<br>Go コードのセキュリティ問題を、スキャンで見つける<br>`セキュリティ` | +561 | 1.5 | 8,997 | <a href="https://www.star-history.com/#securego/gosec&Date"><img src="https://api.star-history.com/svg?repos=securego/gosec&type=Date" width="260" alt="securego/gosec のスター推移グラフ"></a> |

### 総スター数ランキング（累計）

| # | プロジェクト | 総スター数 | スター推移 |
|---|---|---:|---|
| 1 | [aquasecurity/trivy](https://github.com/aquasecurity/trivy)<br>コンテナもコードも、安全チェックは 1 回で<br>`セキュリティ` | 38,941 | <a href="https://www.star-history.com/#aquasecurity/trivy&Date"><img src="https://api.star-history.com/svg?repos=aquasecurity/trivy&type=Date" width="260" alt="aquasecurity/trivy のスター推移グラフ"></a> |
| 2 | [OWASP/CheatSheetSeries](https://github.com/OWASP/CheatSheetSeries)<br>アプリのセキュリティは、この簡潔な手引きで<br>`セキュリティ` | 33,869 | <a href="https://www.star-history.com/#OWASP/CheatSheetSeries&Date"><img src="https://api.star-history.com/svg?repos=OWASP/CheatSheetSeries&type=Date" width="260" alt="OWASP/CheatSheetSeries のスター推移グラフ"></a> |
| 3 | [projectdiscovery/nuclei](https://github.com/projectdiscovery/nuclei)<br>テンプレート 1 つで、脆弱性を一括スキャン<br>`セキュリティ` | 32,568 | <a href="https://www.star-history.com/#projectdiscovery/nuclei&Date"><img src="https://api.star-history.com/svg?repos=projectdiscovery/nuclei&type=Date" width="260" alt="projectdiscovery/nuclei のスター推移グラフ"></a> |
| 4 | [semgrep/semgrep](https://github.com/semgrep/semgrep)<br>コードの問題は、コミット前に見つけ出す<br>`セキュリティ` | 17,430 | <a href="https://www.star-history.com/#semgrep/semgrep&Date"><img src="https://api.star-history.com/svg?repos=semgrep/semgrep&type=Date" width="260" alt="semgrep/semgrep のスター推移グラフ"></a> |
| 5 | [anchore/grype](https://github.com/anchore/grype)<br>コンテナイメージに脆弱性がないか、スキャンで確認<br>`セキュリティ` | 13,170 | <a href="https://www.star-history.com/#anchore/grype&Date"><img src="https://api.star-history.com/svg?repos=anchore/grype&type=Date" width="260" alt="anchore/grype のスター推移グラフ"></a> |
| 6 | [google/osv-scanner](https://github.com/google/osv-scanner)<br>使っている依存は安全か、スキャンすればわかる<br>`セキュリティ` | 11,382 | <a href="https://www.star-history.com/#google/osv-scanner&Date"><img src="https://api.star-history.com/svg?repos=google/osv-scanner&type=Date" width="260" alt="google/osv-scanner のスター推移グラフ"></a> |
| 7 | [falcosecurity/falco](https://github.com/falcosecurity/falco)<br>クラウドの異常に、すぐ気づける<br>`セキュリティ` | 9,548 | <a href="https://www.star-history.com/#falcosecurity/falco&Date"><img src="https://api.star-history.com/svg?repos=falcosecurity/falco&type=Date" width="260" alt="falcosecurity/falco のスター推移グラフ"></a> |
| 8 | [securego/gosec](https://github.com/securego/gosec)<br>Go コードのセキュリティ問題を、スキャンで見つける<br>`セキュリティ` | 8,997 | <a href="https://www.star-history.com/#securego/gosec&Date"><img src="https://api.star-history.com/svg?repos=securego/gosec&type=Date" width="260" alt="securego/gosec のスター推移グラフ"></a> |

## Web / フロントエンド

> フロントエンド枠組み・UI キット・CSS・ブラウザツール

### 7 日以内の新着で最も熱いリポジトリ（作成から 7 日以内）

| # | プロジェクト | 作成日（UTC） | 総スター数 | スター/日 | スター推移 |
|---|---|---|---:|---:|---|
| 1 | [mofan6/Moect](https://github.com/mofan6/Moect)<br>WeChatの会話を残したい時に、オフラインで書き出し保存 | 2026-10-31<br><sub>3.5 日</sub> | 225 | 65.3 | <a href="https://www.star-history.com/#mofan6/Moect&Date"><img src="https://api.star-history.com/svg?repos=mofan6/Moect&type=Date" width="260" alt="mofan6/Moect のスター推移グラフ"></a> |
| 2 | [shipwords-dev/shipwords](https://github.com/shipwords-dev/shipwords)<br>新ワードを見つけたら、午後には AI サイトを公開 | 2026-10-28<br><sub>6.6 日</sub> | 351 | 53.0 | <a href="https://www.star-history.com/#shipwords-dev/shipwords&Date"><img src="https://api.star-history.com/svg?repos=shipwords-dev/shipwords&type=Date" width="260" alt="shipwords-dev/shipwords のスター推移グラフ"></a> |
| 3 | [zklmiao/prompt-vault](https://github.com/zklmiao/prompt-vault)<br>プロンプトの管理に困ったら、ローカルで保存 | 2026-10-28<br><sub>6.7 日</sub> | 309 | 46.0 | <a href="https://www.star-history.com/#zklmiao/prompt-vault&Date"><img src="https://api.star-history.com/svg?repos=zklmiao/prompt-vault&type=Date" width="260" alt="zklmiao/prompt-vault のスター推移グラフ"></a> |
| 4 | [Lavagroabide/aegis-spreadwatch](https://github.com/Lavagroabide/aegis-spreadwatch)<br>CS2の取引利益が曖昧？手数料込みの純利益を確認 | 2026-10-30<br><sub>3.9 日</sub> | 156 | 39.9 | <a href="https://www.star-history.com/#Lavagroabide/aegis-spreadwatch&Date"><img src="https://api.star-history.com/svg?repos=Lavagroabide/aegis-spreadwatch&type=Date" width="260" alt="Lavagroabide/aegis-spreadwatch のスター推移グラフ"></a> |
| 5 | [solderdatabraid29/aegis-vaultgrid](https://github.com/solderdatabraid29/aegis-vaultgrid)<br>CS2の注文手数料が不安？アカウント不要で計画 | 2026-10-30<br><sub>3.9 日</sub> | 139 | 35.5 | <a href="https://www.star-history.com/#solderdatabraid29/aegis-vaultgrid&Date"><img src="https://api.star-history.com/svg?repos=solderdatabraid29/aegis-vaultgrid&type=Date" width="260" alt="solderdatabraid29/aegis-vaultgrid のスター推移グラフ"></a> |
| 6 | [Townlanurture/aegis-skin-terminal](https://github.com/Townlanurture/aegis-skin-terminal)<br>CS2の価格差が見えない？手数料込みでローカル確認 | 2026-10-30<br><sub>3.9 日</sub> | 136 | 34.7 | <a href="https://www.star-history.com/#Townlanurture/aegis-skin-terminal&Date"><img src="https://api.star-history.com/svg?repos=Townlanurture/aegis-skin-terminal&type=Date" width="260" alt="Townlanurture/aegis-skin-terminal のスター推移グラフ"></a> |
| 7 | [SalmeronDevZone/azure-lab](https://github.com/SalmeronDevZone/azure-lab)<br>Simulador de Azure para aprender DevOps sin cuenta ni costes: portal, Cloud Shell, Azure DevOps y una academia de 13 niveles con 47 laboratorios que se validan… | 2026-10-30<br><sub>4.5 日</sub> | 102 | 22.5 | <a href="https://www.star-history.com/#SalmeronDevZone/azure-lab&Date"><img src="https://api.star-history.com/svg?repos=SalmeronDevZone/azure-lab&type=Date" width="260" alt="SalmeronDevZone/azure-lab のスター推移グラフ"></a> |
| 8 | [floatboatai/OpenMinutes](https://github.com/floatboatai/OpenMinutes)<br>ボイスレコーダーの録音を、検索できる文字に | 2026-10-28<br><sub>6.4 日</sub> | 108 | 17.0 | <a href="https://www.star-history.com/#floatboatai/OpenMinutes&Date"><img src="https://api.star-history.com/svg?repos=floatboatai/OpenMinutes&type=Date" width="260" alt="floatboatai/OpenMinutes のスター推移グラフ"></a> |

### 今週もっとも伸びた（直近 7 日）

| # | プロジェクト | 増加数 | スター/日 | 総スター数 | スター推移 |
|---|---|---:|---:|---:|---|
| 1 | [shadcn-ui/ui](https://github.com/shadcn-ui/ui)<br>見栄えの良い部品。コードは自分のもの、自由に改造<br>`Web / フロントエンド` | +664 | 94.9 | 127,278 | <a href="https://www.star-history.com/#shadcn-ui/ui&Date"><img src="https://api.star-history.com/svg?repos=shadcn-ui/ui&type=Date" width="260" alt="shadcn-ui/ui のスター推移グラフ"></a> |
| 2 | [facebook/react](https://github.com/facebook/react)<br>Web もネイティブアプリの画面も、これで作る<br>`Web / フロントエンド` | +350 | 50.0 | 251,900 | <a href="https://www.star-history.com/#facebook/react&Date"><img src="https://api.star-history.com/svg?repos=facebook/react&type=Date" width="260" alt="facebook/react のスター推移グラフ"></a> |
| 3 | [withastro/astro](https://github.com/withastro/astro)<br>コンテンツ中心のサイトを、軽量な出力で作る<br>`Web / フロントエンド` | +207 | 29.6 | 63,700 | <a href="https://www.star-history.com/#withastro/astro&Date"><img src="https://api.star-history.com/svg?repos=withastro/astro&type=Date" width="260" alt="withastro/astro のスター推移グラフ"></a> |
| 4 | [vercel/next.js](https://github.com/vercel/next.js)<br>React でサイトを丸ごと、フロントから裏側まで<br>`Web / フロントエンド` | +158 | 22.6 | 143,247 | <a href="https://www.star-history.com/#vercel/next.js&Date"><img src="https://api.star-history.com/svg?repos=vercel/next.js&type=Date" width="260" alt="vercel/next.js のスター推移グラフ"></a> |
| 5 | [tailwindlabs/tailwindcss](https://github.com/tailwindlabs/tailwindcss)<br>CSS を大量に書かなくても、独自デザインに<br>`Web / フロントエンド` | +101 | 14.4 | 98,057 | <a href="https://www.star-history.com/#tailwindlabs/tailwindcss&Date"><img src="https://api.star-history.com/svg?repos=tailwindlabs/tailwindcss&type=Date" width="260" alt="tailwindlabs/tailwindcss のスター推移グラフ"></a> |
| 6 | [sveltejs/svelte](https://github.com/sveltejs/svelte)<br>書いた部品を、コンパイラが効率的な Web コードに<br>`Web / フロントエンド` | +100 | 14.3 | 88,549 | <a href="https://www.star-history.com/#sveltejs/svelte&Date"><img src="https://api.star-history.com/svg?repos=sveltejs/svelte&type=Date" width="260" alt="sveltejs/svelte のスター推移グラフ"></a> |
| 7 | [vuejs/core](https://github.com/vuejs/core)<br>小さなページから始め、使う分だけ学べる<br>`Web / フロントエンド` | +72 | 10.3 | 54,823 | <a href="https://www.star-history.com/#vuejs/core&Date"><img src="https://api.star-history.com/svg?repos=vuejs/core&type=Date" width="260" alt="vuejs/core のスター推移グラフ"></a> |
| 8 | [tanstack/query](https://github.com/tanstack/query)<br>データ取得とキャッシュは、これに任せる<br>`Web / フロントエンド` | +45 | 6.4 | 50,520 | <a href="https://www.star-history.com/#tanstack/query&Date"><img src="https://api.star-history.com/svg?repos=tanstack/query&type=Date" width="260" alt="tanstack/query のスター推移グラフ"></a> |

### 今月もっとも伸びた（直近 30 日）

| # | プロジェクト | 増加数 | スター/日 | 総スター数 | スター推移 |
|---|---|---:|---:|---:|---|
| 1 | [shadcn-ui/ui](https://github.com/shadcn-ui/ui)<br>見栄えの良い部品。コードは自分のもの、自由に改造<br>`Web / フロントエンド` | +2,653 | 88.4 | 127,278 | <a href="https://www.star-history.com/#shadcn-ui/ui&Date"><img src="https://api.star-history.com/svg?repos=shadcn-ui/ui&type=Date" width="260" alt="shadcn-ui/ui のスター推移グラフ"></a> |
| 2 | [facebook/react](https://github.com/facebook/react)<br>Web もネイティブアプリの画面も、これで作る<br>`Web / フロントエンド` | +1,673 | 55.8 | 251,900 | <a href="https://www.star-history.com/#facebook/react&Date"><img src="https://api.star-history.com/svg?repos=facebook/react&type=Date" width="260" alt="facebook/react のスター推移グラフ"></a> |
| 3 | [withastro/astro](https://github.com/withastro/astro)<br>コンテンツ中心のサイトを、軽量な出力で作る<br>`Web / フロントエンド` | +774 | 25.8 | 63,700 | <a href="https://www.star-history.com/#withastro/astro&Date"><img src="https://api.star-history.com/svg?repos=withastro/astro&type=Date" width="260" alt="withastro/astro のスター推移グラフ"></a> |
| 4 | [vercel/next.js](https://github.com/vercel/next.js)<br>React でサイトを丸ごと、フロントから裏側まで<br>`Web / フロントエンド` | +719 | 24.0 | 143,247 | <a href="https://www.star-history.com/#vercel/next.js&Date"><img src="https://api.star-history.com/svg?repos=vercel/next.js&type=Date" width="260" alt="vercel/next.js のスター推移グラフ"></a> |
| 5 | [sveltejs/svelte](https://github.com/sveltejs/svelte)<br>書いた部品を、コンパイラが効率的な Web コードに<br>`Web / フロントエンド` | +496 | 16.5 | 88,549 | <a href="https://www.star-history.com/#sveltejs/svelte&Date"><img src="https://api.star-history.com/svg?repos=sveltejs/svelte&type=Date" width="260" alt="sveltejs/svelte のスター推移グラフ"></a> |
| 6 | [tailwindlabs/tailwindcss](https://github.com/tailwindlabs/tailwindcss)<br>CSS を大量に書かなくても、独自デザインに<br>`Web / フロントエンド` | +489 | 16.3 | 98,057 | <a href="https://www.star-history.com/#tailwindlabs/tailwindcss&Date"><img src="https://api.star-history.com/svg?repos=tailwindlabs/tailwindcss&type=Date" width="260" alt="tailwindlabs/tailwindcss のスター推移グラフ"></a> |
| 7 | [vuejs/core](https://github.com/vuejs/core)<br>小さなページから始め、使う分だけ学べる<br>`Web / フロントエンド` | +414 | 13.8 | 54,823 | <a href="https://www.star-history.com/#vuejs/core&Date"><img src="https://api.star-history.com/svg?repos=vuejs/core&type=Date" width="260" alt="vuejs/core のスター推移グラフ"></a> |
| 8 | [tanstack/query](https://github.com/tanstack/query)<br>データ取得とキャッシュは、これに任せる<br>`Web / フロントエンド` | +208 | 6.9 | 50,520 | <a href="https://www.star-history.com/#tanstack/query&Date"><img src="https://api.star-history.com/svg?repos=tanstack/query&type=Date" width="260" alt="tanstack/query のスター推移グラフ"></a> |

### 今年もっとも伸びた（直近 365 日）

| # | プロジェクト | 増加数 | スター/日 | 総スター数 | スター推移 |
|---|---|---:|---:|---:|---|
| 1 | [shadcn-ui/ui](https://github.com/shadcn-ui/ui)<br>見栄えの良い部品。コードは自分のもの、自由に改造<br>`Web / フロントエンド` | +30,378 | 83.2 | 127,278 | <a href="https://www.star-history.com/#shadcn-ui/ui&Date"><img src="https://api.star-history.com/svg?repos=shadcn-ui/ui&type=Date" width="260" alt="shadcn-ui/ui のスター推移グラフ"></a> |
| 2 | [facebook/react](https://github.com/facebook/react)<br>Web もネイティブアプリの画面も、これで作る<br>`Web / フロントエンド` | +15,211 | 41.7 | 251,900 | <a href="https://www.star-history.com/#facebook/react&Date"><img src="https://api.star-history.com/svg?repos=facebook/react&type=Date" width="260" alt="facebook/react のスター推移グラフ"></a> |
| 3 | [withastro/astro](https://github.com/withastro/astro)<br>コンテンツ中心のサイトを、軽量な出力で作る<br>`Web / フロントエンド` | +10,505 | 28.8 | 63,700 | <a href="https://www.star-history.com/#withastro/astro&Date"><img src="https://api.star-history.com/svg?repos=withastro/astro&type=Date" width="260" alt="withastro/astro のスター推移グラフ"></a> |
| 4 | [vercel/next.js](https://github.com/vercel/next.js)<br>React でサイトを丸ごと、フロントから裏側まで<br>`Web / フロントエンド` | +10,336 | 28.3 | 143,247 | <a href="https://www.star-history.com/#vercel/next.js&Date"><img src="https://api.star-history.com/svg?repos=vercel/next.js&type=Date" width="260" alt="vercel/next.js のスター推移グラフ"></a> |
| 5 | [tailwindlabs/tailwindcss](https://github.com/tailwindlabs/tailwindcss)<br>CSS を大量に書かなくても、独自デザインに<br>`Web / フロントエンド` | +8,528 | 23.4 | 98,057 | <a href="https://www.star-history.com/#tailwindlabs/tailwindcss&Date"><img src="https://api.star-history.com/svg?repos=tailwindlabs/tailwindcss&type=Date" width="260" alt="tailwindlabs/tailwindcss のスター推移グラフ"></a> |
| 6 | [sveltejs/svelte](https://github.com/sveltejs/svelte)<br>書いた部品を、コンパイラが効率的な Web コードに<br>`Web / フロントエンド` | +5,279 | 14.5 | 88,549 | <a href="https://www.star-history.com/#sveltejs/svelte&Date"><img src="https://api.star-history.com/svg?repos=sveltejs/svelte&type=Date" width="260" alt="sveltejs/svelte のスター推移グラフ"></a> |
| 7 | [tanstack/query](https://github.com/tanstack/query)<br>データ取得とキャッシュは、これに任せる<br>`Web / フロントエンド` | +3,843 | 10.5 | 50,520 | <a href="https://www.star-history.com/#tanstack/query&Date"><img src="https://api.star-history.com/svg?repos=tanstack/query&type=Date" width="260" alt="tanstack/query のスター推移グラフ"></a> |
| 8 | [vuejs/core](https://github.com/vuejs/core)<br>小さなページから始め、使う分だけ学べる<br>`Web / フロントエンド` | +3,620 | 9.9 | 54,823 | <a href="https://www.star-history.com/#vuejs/core&Date"><img src="https://api.star-history.com/svg?repos=vuejs/core&type=Date" width="260" alt="vuejs/core のスター推移グラフ"></a> |

### 総スター数ランキング（累計）

| # | プロジェクト | 総スター数 | スター推移 |
|---|---|---:|---|
| 1 | [facebook/react](https://github.com/facebook/react)<br>Web もネイティブアプリの画面も、これで作る<br>`Web / フロントエンド` | 251,900 | <a href="https://www.star-history.com/#facebook/react&Date"><img src="https://api.star-history.com/svg?repos=facebook/react&type=Date" width="260" alt="facebook/react のスター推移グラフ"></a> |
| 2 | [vercel/next.js](https://github.com/vercel/next.js)<br>React でサイトを丸ごと、フロントから裏側まで<br>`Web / フロントエンド` | 143,247 | <a href="https://www.star-history.com/#vercel/next.js&Date"><img src="https://api.star-history.com/svg?repos=vercel/next.js&type=Date" width="260" alt="vercel/next.js のスター推移グラフ"></a> |
| 3 | [shadcn-ui/ui](https://github.com/shadcn-ui/ui)<br>見栄えの良い部品。コードは自分のもの、自由に改造<br>`Web / フロントエンド` | 127,278 | <a href="https://www.star-history.com/#shadcn-ui/ui&Date"><img src="https://api.star-history.com/svg?repos=shadcn-ui/ui&type=Date" width="260" alt="shadcn-ui/ui のスター推移グラフ"></a> |
| 4 | [tailwindlabs/tailwindcss](https://github.com/tailwindlabs/tailwindcss)<br>CSS を大量に書かなくても、独自デザインに<br>`Web / フロントエンド` | 98,057 | <a href="https://www.star-history.com/#tailwindlabs/tailwindcss&Date"><img src="https://api.star-history.com/svg?repos=tailwindlabs/tailwindcss&type=Date" width="260" alt="tailwindlabs/tailwindcss のスター推移グラフ"></a> |
| 5 | [sveltejs/svelte](https://github.com/sveltejs/svelte)<br>書いた部品を、コンパイラが効率的な Web コードに<br>`Web / フロントエンド` | 88,549 | <a href="https://www.star-history.com/#sveltejs/svelte&Date"><img src="https://api.star-history.com/svg?repos=sveltejs/svelte&type=Date" width="260" alt="sveltejs/svelte のスター推移グラフ"></a> |
| 6 | [withastro/astro](https://github.com/withastro/astro)<br>コンテンツ中心のサイトを、軽量な出力で作る<br>`Web / フロントエンド` | 63,700 | <a href="https://www.star-history.com/#withastro/astro&Date"><img src="https://api.star-history.com/svg?repos=withastro/astro&type=Date" width="260" alt="withastro/astro のスター推移グラフ"></a> |
| 7 | [vuejs/core](https://github.com/vuejs/core)<br>小さなページから始め、使う分だけ学べる<br>`Web / フロントエンド` | 54,823 | <a href="https://www.star-history.com/#vuejs/core&Date"><img src="https://api.star-history.com/svg?repos=vuejs/core&type=Date" width="260" alt="vuejs/core のスター推移グラフ"></a> |
| 8 | [tanstack/query](https://github.com/tanstack/query)<br>データ取得とキャッシュは、これに任せる<br>`Web / フロントエンド` | 50,520 | <a href="https://www.star-history.com/#tanstack/query&Date"><img src="https://api.star-history.com/svg?repos=tanstack/query&type=Date" width="260" alt="tanstack/query のスター推移グラフ"></a> |

## インフラ

> コンテナ・Kubernetes・クラウド・ネットワーク・可観測性

### 7 日以内の新着で最も熱いリポジトリ（作成から 7 日以内）

| # | プロジェクト | 作成日（UTC） | 総スター数 | スター/日 | スター推移 |
|---|---|---|---:|---:|---|
| 1 | [narratarr/narratarr](https://github.com/narratarr/narratarr)<br>Your audiobooks: found, fetched, and playing. An *arr-style audiobook manager with a built-in player. | 2026-10-28<br><sub>6.1 日</sub> | 101 | 16.5 | <a href="https://www.star-history.com/#narratarr/narratarr&Date"><img src="https://api.star-history.com/svg?repos=narratarr/narratarr&type=Date" width="260" alt="narratarr/narratarr のスター推移グラフ"></a> |

### 今週もっとも伸びた（直近 7 日）

| # | プロジェクト | 増加数 | スター/日 | 総スター数 | スター推移 |
|---|---|---:|---:|---:|---|
| 1 | [caddyserver/caddy](https://github.com/caddyserver/caddy)<br>Web サーバー構築、HTTPS は自動で設定<br>`インフラ` | +255 | 36.4 | 78,704 | <a href="https://www.star-history.com/#caddyserver/caddy&Date"><img src="https://api.star-history.com/svg?repos=caddyserver/caddy&type=Date" width="260" alt="caddyserver/caddy のスター推移グラフ"></a> |
| 2 | [kubernetes/kubernetes](https://github.com/kubernetes/kubernetes)<br>コンテナが増えても、配備と拡張は任せる<br>`インフラ` | +218 | 31.1 | 128,638 | <a href="https://www.star-history.com/#kubernetes/kubernetes&Date"><img src="https://api.star-history.com/svg?repos=kubernetes/kubernetes&type=Date" width="260" alt="kubernetes/kubernetes のスター推移グラフ"></a> |
| 3 | [grafana/grafana](https://github.com/grafana/grafana)<br>指標・ログ・トレースを 1 つのパネルに<br>`インフラ` | +174 | 24.9 | 77,663 | <a href="https://www.star-history.com/#grafana/grafana&Date"><img src="https://api.star-history.com/svg?repos=grafana/grafana&type=Date" width="260" alt="grafana/grafana のスター推移グラフ"></a> |
| 4 | [prometheus/prometheus](https://github.com/prometheus/prometheus)<br>システムの不具合は、アラートが先に知らせる<br>`インフラ` | +154 | 22.0 | 66,931 | <a href="https://www.star-history.com/#prometheus/prometheus&Date"><img src="https://api.star-history.com/svg?repos=prometheus/prometheus&type=Date" width="260" alt="prometheus/prometheus のスター推移グラフ"></a> |
| 5 | [docker/compose](https://github.com/docker/compose)<br>複数のコンテナを 1 つのファイルでまとめて動かす<br>`インフラ` | +117 | 16.7 | 38,584 | <a href="https://www.star-history.com/#docker/compose&Date"><img src="https://api.star-history.com/svg?repos=docker/compose&type=Date" width="260" alt="docker/compose のスター推移グラフ"></a> |
| 6 | [traefik/traefik](https://github.com/traefik/traefik)<br>サービスが増えても、通信は自動で振り分け<br>`インフラ` | +93 | 13.3 | 65,451 | <a href="https://www.star-history.com/#traefik/traefik&Date"><img src="https://api.star-history.com/svg?repos=traefik/traefik&type=Date" width="260" alt="traefik/traefik のスター推移グラフ"></a> |
| 7 | [hashicorp/terraform](https://github.com/hashicorp/terraform)<br>クラウド資源をコードにして、レビューもバージョン管理も<br>`インフラ` | +86 | 12.3 | 50,120 | <a href="https://www.star-history.com/#hashicorp/terraform&Date"><img src="https://api.star-history.com/svg?repos=hashicorp/terraform&type=Date" width="260" alt="hashicorp/terraform のスター推移グラフ"></a> |
| 8 | [pulumi/pulumi](https://github.com/pulumi/pulumi)<br>使い慣れた言語で、クラウド資源を管理<br>`インフラ` | +25 | 3.6 | 25,843 | <a href="https://www.star-history.com/#pulumi/pulumi&Date"><img src="https://api.star-history.com/svg?repos=pulumi/pulumi&type=Date" width="260" alt="pulumi/pulumi のスター推移グラフ"></a> |

### 今月もっとも伸びた（直近 30 日）

| # | プロジェクト | 増加数 | スター/日 | 総スター数 | スター推移 |
|---|---|---:|---:|---:|---|
| 1 | [caddyserver/caddy](https://github.com/caddyserver/caddy)<br>Web サーバー構築、HTTPS は自動で設定<br>`インフラ` | +2,532 | 84.4 | 78,704 | <a href="https://www.star-history.com/#caddyserver/caddy&Date"><img src="https://api.star-history.com/svg?repos=caddyserver/caddy&type=Date" width="260" alt="caddyserver/caddy のスター推移グラフ"></a> |
| 2 | [kubernetes/kubernetes](https://github.com/kubernetes/kubernetes)<br>コンテナが増えても、配備と拡張は任せる<br>`インフラ` | +919 | 30.6 | 128,638 | <a href="https://www.star-history.com/#kubernetes/kubernetes&Date"><img src="https://api.star-history.com/svg?repos=kubernetes/kubernetes&type=Date" width="260" alt="kubernetes/kubernetes のスター推移グラフ"></a> |
| 3 | [grafana/grafana](https://github.com/grafana/grafana)<br>指標・ログ・トレースを 1 つのパネルに<br>`インフラ` | +760 | 25.3 | 77,663 | <a href="https://www.star-history.com/#grafana/grafana&Date"><img src="https://api.star-history.com/svg?repos=grafana/grafana&type=Date" width="260" alt="grafana/grafana のスター推移グラフ"></a> |
| 4 | [prometheus/prometheus](https://github.com/prometheus/prometheus)<br>システムの不具合は、アラートが先に知らせる<br>`インフラ` | +711 | 23.7 | 66,931 | <a href="https://www.star-history.com/#prometheus/prometheus&Date"><img src="https://api.star-history.com/svg?repos=prometheus/prometheus&type=Date" width="260" alt="prometheus/prometheus のスター推移グラフ"></a> |
| 5 | [traefik/traefik](https://github.com/traefik/traefik)<br>サービスが増えても、通信は自動で振り分け<br>`インフラ` | +487 | 16.2 | 65,451 | <a href="https://www.star-history.com/#traefik/traefik&Date"><img src="https://api.star-history.com/svg?repos=traefik/traefik&type=Date" width="260" alt="traefik/traefik のスター推移グラフ"></a> |
| 6 | [hashicorp/terraform](https://github.com/hashicorp/terraform)<br>クラウド資源をコードにして、レビューもバージョン管理も<br>`インフラ` | +401 | 13.4 | 50,120 | <a href="https://www.star-history.com/#hashicorp/terraform&Date"><img src="https://api.star-history.com/svg?repos=hashicorp/terraform&type=Date" width="260" alt="hashicorp/terraform のスター推移グラフ"></a> |
| 7 | [docker/compose](https://github.com/docker/compose)<br>複数のコンテナを 1 つのファイルでまとめて動かす<br>`インフラ` | +390 | 13.0 | 38,584 | <a href="https://www.star-history.com/#docker/compose&Date"><img src="https://api.star-history.com/svg?repos=docker/compose&type=Date" width="260" alt="docker/compose のスター推移グラフ"></a> |
| 8 | [pulumi/pulumi](https://github.com/pulumi/pulumi)<br>使い慣れた言語で、クラウド資源を管理<br>`インフラ` | +125 | 4.2 | 25,843 | <a href="https://www.star-history.com/#pulumi/pulumi&Date"><img src="https://api.star-history.com/svg?repos=pulumi/pulumi&type=Date" width="260" alt="pulumi/pulumi のスター推移グラフ"></a> |

### 今年もっとも伸びた（直近 365 日）

| # | プロジェクト | 増加数 | スター/日 | 総スター数 | スター推移 |
|---|---|---:|---:|---:|---|
| 1 | [caddyserver/caddy](https://github.com/caddyserver/caddy)<br>Web サーバー構築、HTTPS は自動で設定<br>`インフラ` | +11,884 | 32.6 | 78,704 | <a href="https://www.star-history.com/#caddyserver/caddy&Date"><img src="https://api.star-history.com/svg?repos=caddyserver/caddy&type=Date" width="260" alt="caddyserver/caddy のスター推移グラフ"></a> |
| 2 | [kubernetes/kubernetes](https://github.com/kubernetes/kubernetes)<br>コンテナが増えても、配備と拡張は任せる<br>`インフラ` | +11,593 | 31.8 | 128,638 | <a href="https://www.star-history.com/#kubernetes/kubernetes&Date"><img src="https://api.star-history.com/svg?repos=kubernetes/kubernetes&type=Date" width="260" alt="kubernetes/kubernetes のスター推移グラフ"></a> |
| 3 | [traefik/traefik](https://github.com/traefik/traefik)<br>サービスが増えても、通信は自動で振り分け<br>`インフラ` | +8,707 | 23.9 | 65,451 | <a href="https://www.star-history.com/#traefik/traefik&Date"><img src="https://api.star-history.com/svg?repos=traefik/traefik&type=Date" width="260" alt="traefik/traefik のスター推移グラフ"></a> |
| 4 | [grafana/grafana](https://github.com/grafana/grafana)<br>指標・ログ・トレースを 1 つのパネルに<br>`インフラ` | +7,885 | 21.6 | 77,663 | <a href="https://www.star-history.com/#grafana/grafana&Date"><img src="https://api.star-history.com/svg?repos=grafana/grafana&type=Date" width="260" alt="grafana/grafana のスター推移グラフ"></a> |
| 5 | [prometheus/prometheus](https://github.com/prometheus/prometheus)<br>システムの不具合は、アラートが先に知らせる<br>`インフラ` | +6,537 | 17.9 | 66,931 | <a href="https://www.star-history.com/#prometheus/prometheus&Date"><img src="https://api.star-history.com/svg?repos=prometheus/prometheus&type=Date" width="260" alt="prometheus/prometheus のスター推移グラフ"></a> |
| 6 | [hashicorp/terraform](https://github.com/hashicorp/terraform)<br>クラウド資源をコードにして、レビューもバージョン管理も<br>`インフラ` | +3,770 | 10.3 | 50,120 | <a href="https://www.star-history.com/#hashicorp/terraform&Date"><img src="https://api.star-history.com/svg?repos=hashicorp/terraform&type=Date" width="260" alt="hashicorp/terraform のスター推移グラフ"></a> |
| 7 | [docker/compose](https://github.com/docker/compose)<br>複数のコンテナを 1 つのファイルでまとめて動かす<br>`インフラ` | +2,628 | 7.2 | 38,584 | <a href="https://www.star-history.com/#docker/compose&Date"><img src="https://api.star-history.com/svg?repos=docker/compose&type=Date" width="260" alt="docker/compose のスター推移グラフ"></a> |
| 8 | [pulumi/pulumi](https://github.com/pulumi/pulumi)<br>使い慣れた言語で、クラウド資源を管理<br>`インフラ` | +2,076 | 5.7 | 25,843 | <a href="https://www.star-history.com/#pulumi/pulumi&Date"><img src="https://api.star-history.com/svg?repos=pulumi/pulumi&type=Date" width="260" alt="pulumi/pulumi のスター推移グラフ"></a> |

### 総スター数ランキング（累計）

| # | プロジェクト | 総スター数 | スター推移 |
|---|---|---:|---|
| 1 | [kubernetes/kubernetes](https://github.com/kubernetes/kubernetes)<br>コンテナが増えても、配備と拡張は任せる<br>`インフラ` | 128,638 | <a href="https://www.star-history.com/#kubernetes/kubernetes&Date"><img src="https://api.star-history.com/svg?repos=kubernetes/kubernetes&type=Date" width="260" alt="kubernetes/kubernetes のスター推移グラフ"></a> |
| 2 | [caddyserver/caddy](https://github.com/caddyserver/caddy)<br>Web サーバー構築、HTTPS は自動で設定<br>`インフラ` | 78,704 | <a href="https://www.star-history.com/#caddyserver/caddy&Date"><img src="https://api.star-history.com/svg?repos=caddyserver/caddy&type=Date" width="260" alt="caddyserver/caddy のスター推移グラフ"></a> |
| 3 | [grafana/grafana](https://github.com/grafana/grafana)<br>指標・ログ・トレースを 1 つのパネルに<br>`インフラ` | 77,663 | <a href="https://www.star-history.com/#grafana/grafana&Date"><img src="https://api.star-history.com/svg?repos=grafana/grafana&type=Date" width="260" alt="grafana/grafana のスター推移グラフ"></a> |
| 4 | [prometheus/prometheus](https://github.com/prometheus/prometheus)<br>システムの不具合は、アラートが先に知らせる<br>`インフラ` | 66,931 | <a href="https://www.star-history.com/#prometheus/prometheus&Date"><img src="https://api.star-history.com/svg?repos=prometheus/prometheus&type=Date" width="260" alt="prometheus/prometheus のスター推移グラフ"></a> |
| 5 | [traefik/traefik](https://github.com/traefik/traefik)<br>サービスが増えても、通信は自動で振り分け<br>`インフラ` | 65,451 | <a href="https://www.star-history.com/#traefik/traefik&Date"><img src="https://api.star-history.com/svg?repos=traefik/traefik&type=Date" width="260" alt="traefik/traefik のスター推移グラフ"></a> |
| 6 | [hashicorp/terraform](https://github.com/hashicorp/terraform)<br>クラウド資源をコードにして、レビューもバージョン管理も<br>`インフラ` | 50,120 | <a href="https://www.star-history.com/#hashicorp/terraform&Date"><img src="https://api.star-history.com/svg?repos=hashicorp/terraform&type=Date" width="260" alt="hashicorp/terraform のスター推移グラフ"></a> |
| 7 | [docker/compose](https://github.com/docker/compose)<br>複数のコンテナを 1 つのファイルでまとめて動かす<br>`インフラ` | 38,584 | <a href="https://www.star-history.com/#docker/compose&Date"><img src="https://api.star-history.com/svg?repos=docker/compose&type=Date" width="260" alt="docker/compose のスター推移グラフ"></a> |
| 8 | [pulumi/pulumi](https://github.com/pulumi/pulumi)<br>使い慣れた言語で、クラウド資源を管理<br>`インフラ` | 25,843 | <a href="https://www.star-history.com/#pulumi/pulumi&Date"><img src="https://api.star-history.com/svg?repos=pulumi/pulumi&type=Date" width="260" alt="pulumi/pulumi のスター推移グラフ"></a> |

## デザイン / クリエイティブ

> デザインシステム・描画・アニメーション・制作ツール

### 7 日以内の新着で最も熱いリポジトリ（作成から 7 日以内）

| # | プロジェクト | 作成日（UTC） | 総スター数 | スター/日 | スター推移 |
|---|---|---|---:|---:|---|
| 1 | [patch-gg/pixelfx](https://github.com/patch-gg/pixelfx)<br>ドット絵演出に悩んだら244本の短いコードを貼るだけ | 2026-10-30<br><sub>4.6 日</sub> | 4,069 | 881.8 | <a href="https://www.star-history.com/#patch-gg/pixelfx&Date"><img src="https://api.star-history.com/svg?repos=patch-gg/pixelfx&type=Date" width="260" alt="patch-gg/pixelfx のスター推移グラフ"></a> |
| 2 | [kevinraymond/florilegium](https://github.com/kevinraymond/florilegium)<br>余白が味気ない？デルフトブルーの花柄を自動で描く | 2026-10-30<br><sub>4.6 日</sub> | 1,405 | 307.5 | <a href="https://www.star-history.com/#kevinraymond/florilegium&Date"><img src="https://api.star-history.com/svg?repos=kevinraymond/florilegium&type=Date" width="260" alt="kevinraymond/florilegium のスター推移グラフ"></a> |
| 3 | [DominikScholz/open-bot-avatar](https://github.com/DominikScholz/open-bot-avatar)<br>A JSON spec and renderer for interactive agent avatars | 2026-11-02<br><sub>1.2 日</sub> | 115 | 97.1 | <a href="https://www.star-history.com/#DominikScholz/open-bot-avatar&Date"><img src="https://api.star-history.com/svg?repos=DominikScholz/open-bot-avatar&type=Date" width="260" alt="DominikScholz/open-bot-avatar のスター推移グラフ"></a> |
| 4 | [op7418/dsh-guizang-design](https://github.com/op7418/dsh-guizang-design)<br>AI臭さが抜けない？4つのスキルでデザインを整える | 2026-10-30<br><sub>4.3 日</sub> | 354 | 82.7 | <a href="https://www.star-history.com/#op7418/dsh-guizang-design&Date"><img src="https://api.star-history.com/svg?repos=op7418/dsh-guizang-design&type=Date" width="260" alt="op7418/dsh-guizang-design のスター推移グラフ"></a> |
| 5 | [GuoZheng-de-BaBa/nursing-research-skills](https://github.com/GuoZheng-de-BaBa/nursing-research-skills)<br>看護研究が進まない時に、AIスキルで設計から執筆まで支援 | 2026-10-30<br><sub>4.3 日</sub> | 228 | 53.0 | <a href="https://www.star-history.com/#GuoZheng-de-BaBa/nursing-research-skills&Date"><img src="https://api.star-history.com/svg?repos=GuoZheng-de-BaBa/nursing-research-skills&type=Date" width="260" alt="GuoZheng-de-BaBa/nursing-research-skills のスター推移グラフ"></a> |
| 6 | [Akillll-DuoHe/fy-code-animation](https://github.com/Akillll-DuoHe/fy-code-animation)<br>企画を動かせない？原稿と音声をコード動画に変える | 2026-10-30<br><sub>4.5 日</sub> | 168 | 37.5 | <a href="https://www.star-history.com/#Akillll-DuoHe/fy-code-animation&Date"><img src="https://api.star-history.com/svg?repos=Akillll-DuoHe/fy-code-animation&type=Date" width="260" alt="Akillll-DuoHe/fy-code-animation のスター推移グラフ"></a> |
| 7 | [ersinkoc/AI-Video-Factory](https://github.com/ersinkoc/AI-Video-Factory)<br>ひとつの話題から、Claudeエージェントが動画を完成 | 2026-10-29<br><sub>5.0 日</sub> | 177 | 35.7 | <a href="https://www.star-history.com/#ersinkoc/AI-Video-Factory&Date"><img src="https://api.star-history.com/svg?repos=ersinkoc/AI-Video-Factory&type=Date" width="260" alt="ersinkoc/AI-Video-Factory のスター推移グラフ"></a> |
| 8 | [enmerasoftware/ai-design-check](https://github.com/enmerasoftware/ai-design-check)<br>エージェントが作った画面、デザイン崩れを点検する | 2026-10-28<br><sub>6.6 日</sub> | 212 | 32.2 | <a href="https://www.star-history.com/#enmerasoftware/ai-design-check&Date"><img src="https://api.star-history.com/svg?repos=enmerasoftware/ai-design-check&type=Date" width="260" alt="enmerasoftware/ai-design-check のスター推移グラフ"></a> |

### 今週もっとも伸びた（直近 7 日）

| # | プロジェクト | 増加数 | スター/日 | 総スター数 | スター推移 |
|---|---|---:|---:|---:|---|
| 1 | [excalidraw/excalidraw](https://github.com/excalidraw/excalidraw)<br>開いてすぐ描ける、紙に落書きする感覚で<br>`デザイン / クリエイティブ` | +504 | 72.0 | 135,112 | <a href="https://www.star-history.com/#excalidraw/excalidraw&Date"><img src="https://api.star-history.com/svg?repos=excalidraw/excalidraw&type=Date" width="260" alt="excalidraw/excalidraw のスター推移グラフ"></a> |
| 2 | [penpot/penpot](https://github.com/penpot/penpot)<br>チームで一緒にデザイン、オープンソースの基盤で<br>`デザイン / クリエイティブ` | +313 | 44.7 | 62,027 | <a href="https://www.star-history.com/#penpot/penpot&Date"><img src="https://api.star-history.com/svg?repos=penpot/penpot&type=Date" width="260" alt="penpot/penpot のスター推移グラフ"></a> |
| 3 | [lucide-icons/lucide](https://github.com/lucide-icons/lucide)<br>スタイルが揃ったアイコン一式、すぐ使える<br>`デザイン / クリエイティブ` | +175 | 25.0 | 25,510 | <a href="https://www.star-history.com/#lucide-icons/lucide&Date"><img src="https://api.star-history.com/svg?repos=lucide-icons/lucide&type=Date" width="260" alt="lucide-icons/lucide のスター推移グラフ"></a> |
| 4 | [jgraph/drawio](https://github.com/jgraph/drawio)<br>作図もホワイトボードも、1 つのエディタで<br>`デザイン / クリエイティブ` | +150 | 21.4 | 9,163 | <a href="https://www.star-history.com/#jgraph/drawio&Date"><img src="https://api.star-history.com/svg?repos=jgraph/drawio&type=Date" width="260" alt="jgraph/drawio のスター推移グラフ"></a> |
| 5 | [saadeghi/daisyui](https://github.com/saadeghi/daisyui)<br>Tailwind 用の部品が最初から揃っている<br>`デザイン / クリエイティブ` | +74 | 10.6 | 42,731 | <a href="https://www.star-history.com/#saadeghi/daisyui&Date"><img src="https://api.star-history.com/svg?repos=saadeghi/daisyui&type=Date" width="260" alt="saadeghi/daisyui のスター推移グラフ"></a> |
| 6 | [airbnb/lottie-web](https://github.com/airbnb/lottie-web)<br>After Effects のアニメを、そのまま Web に<br>`デザイン / クリエイティブ` | +60 | 8.6 | 32,340 | <a href="https://www.star-history.com/#airbnb/lottie-web&Date"><img src="https://api.star-history.com/svg?repos=airbnb/lottie-web&type=Date" width="260" alt="airbnb/lottie-web のスター推移グラフ"></a> |
| 7 | [phosphor-icons/homepage](https://github.com/phosphor-icons/homepage)<br>誰でも使える、柔軟なアイコンファミリー<br>`デザイン / クリエイティブ` | +33 | 4.7 | 7,761 | <a href="https://www.star-history.com/#phosphor-icons/homepage&Date"><img src="https://api.star-history.com/svg?repos=phosphor-icons/homepage&type=Date" width="260" alt="phosphor-icons/homepage のスター推移グラフ"></a> |
| 8 | [lottiefiles/lottie-ios](https://github.com/lottiefiles/lottie-ios)<br>After Effects のアニメを、そのまま iOS に<br>`デザイン / クリエイティブ` | +0 | 0.0 | 43 | <a href="https://www.star-history.com/#lottiefiles/lottie-ios&Date"><img src="https://api.star-history.com/svg?repos=lottiefiles/lottie-ios&type=Date" width="260" alt="lottiefiles/lottie-ios のスター推移グラフ"></a> |

### 今月もっとも伸びた（直近 30 日）

| # | プロジェクト | 増加数 | スター/日 | 総スター数 | スター推移 |
|---|---|---:|---:|---:|---|
| 1 | [excalidraw/excalidraw](https://github.com/excalidraw/excalidraw)<br>開いてすぐ描ける、紙に落書きする感覚で<br>`デザイン / クリエイティブ` | +2,007 | 66.9 | 135,112 | <a href="https://www.star-history.com/#excalidraw/excalidraw&Date"><img src="https://api.star-history.com/svg?repos=excalidraw/excalidraw&type=Date" width="260" alt="excalidraw/excalidraw のスター推移グラフ"></a> |
| 2 | [penpot/penpot](https://github.com/penpot/penpot)<br>チームで一緒にデザイン、オープンソースの基盤で<br>`デザイン / クリエイティブ` | +1,488 | 49.6 | 62,027 | <a href="https://www.star-history.com/#penpot/penpot&Date"><img src="https://api.star-history.com/svg?repos=penpot/penpot&type=Date" width="260" alt="penpot/penpot のスター推移グラフ"></a> |
| 3 | [lucide-icons/lucide](https://github.com/lucide-icons/lucide)<br>スタイルが揃ったアイコン一式、すぐ使える<br>`デザイン / クリエイティブ` | +699 | 23.3 | 25,510 | <a href="https://www.star-history.com/#lucide-icons/lucide&Date"><img src="https://api.star-history.com/svg?repos=lucide-icons/lucide&type=Date" width="260" alt="lucide-icons/lucide のスター推移グラフ"></a> |
| 4 | [jgraph/drawio](https://github.com/jgraph/drawio)<br>作図もホワイトボードも、1 つのエディタで<br>`デザイン / クリエイティブ` | +625 | 20.8 | 9,163 | <a href="https://www.star-history.com/#jgraph/drawio&Date"><img src="https://api.star-history.com/svg?repos=jgraph/drawio&type=Date" width="260" alt="jgraph/drawio のスター推移グラフ"></a> |
| 5 | [saadeghi/daisyui](https://github.com/saadeghi/daisyui)<br>Tailwind 用の部品が最初から揃っている<br>`デザイン / クリエイティブ` | +283 | 9.4 | 42,731 | <a href="https://www.star-history.com/#saadeghi/daisyui&Date"><img src="https://api.star-history.com/svg?repos=saadeghi/daisyui&type=Date" width="260" alt="saadeghi/daisyui のスター推移グラフ"></a> |
| 6 | [airbnb/lottie-web](https://github.com/airbnb/lottie-web)<br>After Effects のアニメを、そのまま Web に<br>`デザイン / クリエイティブ` | +227 | 7.6 | 32,340 | <a href="https://www.star-history.com/#airbnb/lottie-web&Date"><img src="https://api.star-history.com/svg?repos=airbnb/lottie-web&type=Date" width="260" alt="airbnb/lottie-web のスター推移グラフ"></a> |
| 7 | [phosphor-icons/homepage](https://github.com/phosphor-icons/homepage)<br>誰でも使える、柔軟なアイコンファミリー<br>`デザイン / クリエイティブ` | +177 | 5.9 | 7,761 | <a href="https://www.star-history.com/#phosphor-icons/homepage&Date"><img src="https://api.star-history.com/svg?repos=phosphor-icons/homepage&type=Date" width="260" alt="phosphor-icons/homepage のスター推移グラフ"></a> |
| 8 | [lottiefiles/lottie-ios](https://github.com/lottiefiles/lottie-ios)<br>After Effects のアニメを、そのまま iOS に<br>`デザイン / クリエイティブ` | +0 | 0.0 | 43 | <a href="https://www.star-history.com/#lottiefiles/lottie-ios&Date"><img src="https://api.star-history.com/svg?repos=lottiefiles/lottie-ios&type=Date" width="260" alt="lottiefiles/lottie-ios のスター推移グラフ"></a> |

### 今年もっとも伸びた（直近 365 日）

| # | プロジェクト | 増加数 | スター/日 | 総スター数 | スター推移 |
|---|---|---:|---:|---:|---|
| 1 | [excalidraw/excalidraw](https://github.com/excalidraw/excalidraw)<br>開いてすぐ描ける、紙に落書きする感覚で<br>`デザイン / クリエイティブ` | +27,065 | 74.2 | 135,112 | <a href="https://www.star-history.com/#excalidraw/excalidraw&Date"><img src="https://api.star-history.com/svg?repos=excalidraw/excalidraw&type=Date" width="260" alt="excalidraw/excalidraw のスター推移グラフ"></a> |
| 2 | [penpot/penpot](https://github.com/penpot/penpot)<br>チームで一緒にデザイン、オープンソースの基盤で<br>`デザイン / クリエイティブ` | +21,740 | 59.6 | 62,027 | <a href="https://www.star-history.com/#penpot/penpot&Date"><img src="https://api.star-history.com/svg?repos=penpot/penpot&type=Date" width="260" alt="penpot/penpot のスター推移グラフ"></a> |
| 3 | [jgraph/drawio](https://github.com/jgraph/drawio)<br>作図もホワイトボードも、1 つのエディタで<br>`デザイン / クリエイティブ` | +6,501 | 17.8 | 9,163 | <a href="https://www.star-history.com/#jgraph/drawio&Date"><img src="https://api.star-history.com/svg?repos=jgraph/drawio&type=Date" width="260" alt="jgraph/drawio のスター推移グラフ"></a> |
| 4 | [lucide-icons/lucide](https://github.com/lucide-icons/lucide)<br>スタイルが揃ったアイコン一式、すぐ使える<br>`デザイン / クリエイティブ` | +6,269 | 17.2 | 25,510 | <a href="https://www.star-history.com/#lucide-icons/lucide&Date"><img src="https://api.star-history.com/svg?repos=lucide-icons/lucide&type=Date" width="260" alt="lucide-icons/lucide のスター推移グラフ"></a> |
| 5 | [saadeghi/daisyui](https://github.com/saadeghi/daisyui)<br>Tailwind 用の部品が最初から揃っている<br>`デザイン / クリエイティブ` | +4,228 | 11.6 | 42,731 | <a href="https://www.star-history.com/#saadeghi/daisyui&Date"><img src="https://api.star-history.com/svg?repos=saadeghi/daisyui&type=Date" width="260" alt="saadeghi/daisyui のスター推移グラフ"></a> |
| 6 | [phosphor-icons/homepage](https://github.com/phosphor-icons/homepage)<br>誰でも使える、柔軟なアイコンファミリー<br>`デザイン / クリエイティブ` | +2,194 | 6.0 | 7,761 | <a href="https://www.star-history.com/#phosphor-icons/homepage&Date"><img src="https://api.star-history.com/svg?repos=phosphor-icons/homepage&type=Date" width="260" alt="phosphor-icons/homepage のスター推移グラフ"></a> |
| 7 | [airbnb/lottie-web](https://github.com/airbnb/lottie-web)<br>After Effects のアニメを、そのまま Web に<br>`デザイン / クリエイティブ` | +1,098 | 3.0 | 32,340 | <a href="https://www.star-history.com/#airbnb/lottie-web&Date"><img src="https://api.star-history.com/svg?repos=airbnb/lottie-web&type=Date" width="260" alt="airbnb/lottie-web のスター推移グラフ"></a> |
| 8 | [lottiefiles/lottie-ios](https://github.com/lottiefiles/lottie-ios)<br>After Effects のアニメを、そのまま iOS に<br>`デザイン / クリエイティブ` | +1 | 0.0 | 43 | <a href="https://www.star-history.com/#lottiefiles/lottie-ios&Date"><img src="https://api.star-history.com/svg?repos=lottiefiles/lottie-ios&type=Date" width="260" alt="lottiefiles/lottie-ios のスター推移グラフ"></a> |

### 総スター数ランキング（累計）

| # | プロジェクト | 総スター数 | スター推移 |
|---|---|---:|---|
| 1 | [excalidraw/excalidraw](https://github.com/excalidraw/excalidraw)<br>開いてすぐ描ける、紙に落書きする感覚で<br>`デザイン / クリエイティブ` | 135,112 | <a href="https://www.star-history.com/#excalidraw/excalidraw&Date"><img src="https://api.star-history.com/svg?repos=excalidraw/excalidraw&type=Date" width="260" alt="excalidraw/excalidraw のスター推移グラフ"></a> |
| 2 | [penpot/penpot](https://github.com/penpot/penpot)<br>チームで一緒にデザイン、オープンソースの基盤で<br>`デザイン / クリエイティブ` | 62,027 | <a href="https://www.star-history.com/#penpot/penpot&Date"><img src="https://api.star-history.com/svg?repos=penpot/penpot&type=Date" width="260" alt="penpot/penpot のスター推移グラフ"></a> |
| 3 | [saadeghi/daisyui](https://github.com/saadeghi/daisyui)<br>Tailwind 用の部品が最初から揃っている<br>`デザイン / クリエイティブ` | 42,731 | <a href="https://www.star-history.com/#saadeghi/daisyui&Date"><img src="https://api.star-history.com/svg?repos=saadeghi/daisyui&type=Date" width="260" alt="saadeghi/daisyui のスター推移グラフ"></a> |
| 4 | [airbnb/lottie-web](https://github.com/airbnb/lottie-web)<br>After Effects のアニメを、そのまま Web に<br>`デザイン / クリエイティブ` | 32,340 | <a href="https://www.star-history.com/#airbnb/lottie-web&Date"><img src="https://api.star-history.com/svg?repos=airbnb/lottie-web&type=Date" width="260" alt="airbnb/lottie-web のスター推移グラフ"></a> |
| 5 | [lucide-icons/lucide](https://github.com/lucide-icons/lucide)<br>スタイルが揃ったアイコン一式、すぐ使える<br>`デザイン / クリエイティブ` | 25,510 | <a href="https://www.star-history.com/#lucide-icons/lucide&Date"><img src="https://api.star-history.com/svg?repos=lucide-icons/lucide&type=Date" width="260" alt="lucide-icons/lucide のスター推移グラフ"></a> |
| 6 | [jgraph/drawio](https://github.com/jgraph/drawio)<br>作図もホワイトボードも、1 つのエディタで<br>`デザイン / クリエイティブ` | 9,163 | <a href="https://www.star-history.com/#jgraph/drawio&Date"><img src="https://api.star-history.com/svg?repos=jgraph/drawio&type=Date" width="260" alt="jgraph/drawio のスター推移グラフ"></a> |
| 7 | [phosphor-icons/homepage](https://github.com/phosphor-icons/homepage)<br>誰でも使える、柔軟なアイコンファミリー<br>`デザイン / クリエイティブ` | 7,761 | <a href="https://www.star-history.com/#phosphor-icons/homepage&Date"><img src="https://api.star-history.com/svg?repos=phosphor-icons/homepage&type=Date" width="260" alt="phosphor-icons/homepage のスター推移グラフ"></a> |
| 8 | [lottiefiles/lottie-ios](https://github.com/lottiefiles/lottie-ios)<br>After Effects のアニメを、そのまま iOS に<br>`デザイン / クリエイティブ` | 43 | <a href="https://www.star-history.com/#lottiefiles/lottie-ios&Date"><img src="https://api.star-history.com/svg?repos=lottiefiles/lottie-ios&type=Date" width="260" alt="lottiefiles/lottie-ios のスター推移グラフ"></a> |

## データ

> データベース・分析・ETL・データエンジニアリング

### 7 日以内の新着で最も熱いリポジトリ（作成から 7 日以内）

今回の実行で条件を満たす新着リポジトリはありませんでした。

### 今週もっとも伸びた（直近 7 日）

| # | プロジェクト | 増加数 | スター/日 | 総スター数 | スター推移 |
|---|---|---:|---:|---:|---|
| 1 | [duckdb/duckdb](https://github.com/duckdb/duckdb)<br>データベースサーバーなしで、SQL 分析ができる<br>`データ` | +196 | 28.0 | 42,785 | <a href="https://www.star-history.com/#duckdb/duckdb&Date"><img src="https://api.star-history.com/svg?repos=duckdb/duckdb&type=Date" width="260" alt="duckdb/duckdb のスター推移グラフ"></a> |
| 2 | [ClickHouse/ClickHouse](https://github.com/ClickHouse/ClickHouse)<br>大量データのリアルタイム分析をオープンソースで<br>`データ` | +121 | 17.3 | 50,736 | <a href="https://www.star-history.com/#ClickHouse/ClickHouse&Date"><img src="https://api.star-history.com/svg?repos=ClickHouse/ClickHouse&type=Date" width="260" alt="ClickHouse/ClickHouse のスター推移グラフ"></a> |
| 3 | [apache/superset](https://github.com/apache/superset)<br>データは、グラフにすれば見えてくる<br>`データ` | +100 | 14.3 | 75,398 | <a href="https://www.star-history.com/#apache/superset&Date"><img src="https://api.star-history.com/svg?repos=apache/superset&type=Date" width="260" alt="apache/superset のスター推移グラフ"></a> |
| 4 | [pola-rs/polars](https://github.com/pola-rs/polars)<br>表データの処理が速く、待たされない<br>`データ` | +59 | 8.4 | 40,257 | <a href="https://www.star-history.com/#pola-rs/polars&Date"><img src="https://api.star-history.com/svg?repos=pola-rs/polars&type=Date" width="260" alt="pola-rs/polars のスター推移グラフ"></a> |
| 5 | [apache/kafka](https://github.com/apache/kafka)<br>システム間のイベントの流れを、分散基盤で運ぶ<br>`データ` | +59 | 8.4 | 34,122 | <a href="https://www.star-history.com/#apache/kafka&Date"><img src="https://api.star-history.com/svg?repos=apache/kafka&type=Date" width="260" alt="apache/kafka のスター推移グラフ"></a> |
| 6 | [apache/arrow](https://github.com/apache/arrow)<br>言語が違っても、データはそのまま通じる<br>`データ` | +43 | 6.1 | 17,274 | <a href="https://www.star-history.com/#apache/arrow&Date"><img src="https://api.star-history.com/svg?repos=apache/arrow&type=Date" width="260" alt="apache/arrow のスター推移グラフ"></a> |
| 7 | [dbt-labs/dbt-core](https://github.com/dbt-labs/dbt-core)<br>データ変換を、ソフトウェア開発のやり方で<br>`データ` | +29 | 4.1 | 14,115 | <a href="https://www.star-history.com/#dbt-labs/dbt-core&Date"><img src="https://api.star-history.com/svg?repos=dbt-labs/dbt-core&type=Date" width="260" alt="dbt-labs/dbt-core のスター推移グラフ"></a> |
| 8 | [jupyter/notebook](https://github.com/jupyter/notebook)<br>ブラウザでコードを書き、結果をその場で確認<br>`データ` | +4 | 0.6 | 13,458 | <a href="https://www.star-history.com/#jupyter/notebook&Date"><img src="https://api.star-history.com/svg?repos=jupyter/notebook&type=Date" width="260" alt="jupyter/notebook のスター推移グラフ"></a> |

### 今月もっとも伸びた（直近 30 日）

| # | プロジェクト | 増加数 | スター/日 | 総スター数 | スター推移 |
|---|---|---:|---:|---:|---|
| 1 | [duckdb/duckdb](https://github.com/duckdb/duckdb)<br>データベースサーバーなしで、SQL 分析ができる<br>`データ` | +945 | 31.5 | 42,785 | <a href="https://www.star-history.com/#duckdb/duckdb&Date"><img src="https://api.star-history.com/svg?repos=duckdb/duckdb&type=Date" width="260" alt="duckdb/duckdb のスター推移グラフ"></a> |
| 2 | [ClickHouse/ClickHouse](https://github.com/ClickHouse/ClickHouse)<br>大量データのリアルタイム分析をオープンソースで<br>`データ` | +588 | 19.6 | 50,736 | <a href="https://www.star-history.com/#ClickHouse/ClickHouse&Date"><img src="https://api.star-history.com/svg?repos=ClickHouse/ClickHouse&type=Date" width="260" alt="ClickHouse/ClickHouse のスター推移グラフ"></a> |
| 3 | [apache/superset](https://github.com/apache/superset)<br>データは、グラフにすれば見えてくる<br>`データ` | +459 | 15.3 | 75,398 | <a href="https://www.star-history.com/#apache/superset&Date"><img src="https://api.star-history.com/svg?repos=apache/superset&type=Date" width="260" alt="apache/superset のスター推移グラフ"></a> |
| 4 | [pola-rs/polars](https://github.com/pola-rs/polars)<br>表データの処理が速く、待たされない<br>`データ` | +387 | 12.9 | 40,257 | <a href="https://www.star-history.com/#pola-rs/polars&Date"><img src="https://api.star-history.com/svg?repos=pola-rs/polars&type=Date" width="260" alt="pola-rs/polars のスター推移グラフ"></a> |
| 5 | [apache/kafka](https://github.com/apache/kafka)<br>システム間のイベントの流れを、分散基盤で運ぶ<br>`データ` | +292 | 9.7 | 34,122 | <a href="https://www.star-history.com/#apache/kafka&Date"><img src="https://api.star-history.com/svg?repos=apache/kafka&type=Date" width="260" alt="apache/kafka のスター推移グラフ"></a> |
| 6 | [dbt-labs/dbt-core](https://github.com/dbt-labs/dbt-core)<br>データ変換を、ソフトウェア開発のやり方で<br>`データ` | +168 | 5.6 | 14,115 | <a href="https://www.star-history.com/#dbt-labs/dbt-core&Date"><img src="https://api.star-history.com/svg?repos=dbt-labs/dbt-core&type=Date" width="260" alt="dbt-labs/dbt-core のスター推移グラフ"></a> |
| 7 | [apache/arrow](https://github.com/apache/arrow)<br>言語が違っても、データはそのまま通じる<br>`データ` | +120 | 4.0 | 17,274 | <a href="https://www.star-history.com/#apache/arrow&Date"><img src="https://api.star-history.com/svg?repos=apache/arrow&type=Date" width="260" alt="apache/arrow のスター推移グラフ"></a> |
| 8 | [jupyter/notebook](https://github.com/jupyter/notebook)<br>ブラウザでコードを書き、結果をその場で確認<br>`データ` | +70 | 2.3 | 13,458 | <a href="https://www.star-history.com/#jupyter/notebook&Date"><img src="https://api.star-history.com/svg?repos=jupyter/notebook&type=Date" width="260" alt="jupyter/notebook のスター推移グラフ"></a> |

### 今年もっとも伸びた（直近 365 日）

| # | プロジェクト | 増加数 | スター/日 | 総スター数 | スター推移 |
|---|---|---:|---:|---:|---|
| 1 | [duckdb/duckdb](https://github.com/duckdb/duckdb)<br>データベースサーバーなしで、SQL 分析ができる<br>`データ` | +9,374 | 25.7 | 42,785 | <a href="https://www.star-history.com/#duckdb/duckdb&Date"><img src="https://api.star-history.com/svg?repos=duckdb/duckdb&type=Date" width="260" alt="duckdb/duckdb のスター推移グラフ"></a> |
| 2 | [ClickHouse/ClickHouse](https://github.com/ClickHouse/ClickHouse)<br>大量データのリアルタイム分析をオープンソースで<br>`データ` | +7,624 | 20.9 | 50,736 | <a href="https://www.star-history.com/#ClickHouse/ClickHouse&Date"><img src="https://api.star-history.com/svg?repos=ClickHouse/ClickHouse&type=Date" width="260" alt="ClickHouse/ClickHouse のスター推移グラフ"></a> |
| 3 | [apache/superset](https://github.com/apache/superset)<br>データは、グラフにすれば見えてくる<br>`データ` | +7,436 | 20.4 | 75,398 | <a href="https://www.star-history.com/#apache/superset&Date"><img src="https://api.star-history.com/svg?repos=apache/superset&type=Date" width="260" alt="apache/superset のスター推移グラフ"></a> |
| 4 | [pola-rs/polars](https://github.com/pola-rs/polars)<br>表データの処理が速く、待たされない<br>`データ` | +4,853 | 13.3 | 40,257 | <a href="https://www.star-history.com/#pola-rs/polars&Date"><img src="https://api.star-history.com/svg?repos=pola-rs/polars&type=Date" width="260" alt="pola-rs/polars のスター推移グラフ"></a> |
| 5 | [apache/kafka](https://github.com/apache/kafka)<br>システム間のイベントの流れを、分散基盤で運ぶ<br>`データ` | +3,295 | 9.0 | 34,122 | <a href="https://www.star-history.com/#apache/kafka&Date"><img src="https://api.star-history.com/svg?repos=apache/kafka&type=Date" width="260" alt="apache/kafka のスター推移グラフ"></a> |
| 6 | [dbt-labs/dbt-core](https://github.com/dbt-labs/dbt-core)<br>データ変換を、ソフトウェア開発のやり方で<br>`データ` | +2,465 | 6.8 | 14,115 | <a href="https://www.star-history.com/#dbt-labs/dbt-core&Date"><img src="https://api.star-history.com/svg?repos=dbt-labs/dbt-core&type=Date" width="260" alt="dbt-labs/dbt-core のスター推移グラフ"></a> |
| 7 | [apache/arrow](https://github.com/apache/arrow)<br>言語が違っても、データはそのまま通じる<br>`データ` | +1,318 | 3.6 | 17,274 | <a href="https://www.star-history.com/#apache/arrow&Date"><img src="https://api.star-history.com/svg?repos=apache/arrow&type=Date" width="260" alt="apache/arrow のスター推移グラフ"></a> |
| 8 | [jupyter/notebook](https://github.com/jupyter/notebook)<br>ブラウザでコードを書き、結果をその場で確認<br>`データ` | +904 | 2.5 | 13,458 | <a href="https://www.star-history.com/#jupyter/notebook&Date"><img src="https://api.star-history.com/svg?repos=jupyter/notebook&type=Date" width="260" alt="jupyter/notebook のスター推移グラフ"></a> |

### 総スター数ランキング（累計）

| # | プロジェクト | 総スター数 | スター推移 |
|---|---|---:|---|
| 1 | [apache/superset](https://github.com/apache/superset)<br>データは、グラフにすれば見えてくる<br>`データ` | 75,398 | <a href="https://www.star-history.com/#apache/superset&Date"><img src="https://api.star-history.com/svg?repos=apache/superset&type=Date" width="260" alt="apache/superset のスター推移グラフ"></a> |
| 2 | [ClickHouse/ClickHouse](https://github.com/ClickHouse/ClickHouse)<br>大量データのリアルタイム分析をオープンソースで<br>`データ` | 50,736 | <a href="https://www.star-history.com/#ClickHouse/ClickHouse&Date"><img src="https://api.star-history.com/svg?repos=ClickHouse/ClickHouse&type=Date" width="260" alt="ClickHouse/ClickHouse のスター推移グラフ"></a> |
| 3 | [duckdb/duckdb](https://github.com/duckdb/duckdb)<br>データベースサーバーなしで、SQL 分析ができる<br>`データ` | 42,785 | <a href="https://www.star-history.com/#duckdb/duckdb&Date"><img src="https://api.star-history.com/svg?repos=duckdb/duckdb&type=Date" width="260" alt="duckdb/duckdb のスター推移グラフ"></a> |
| 4 | [pola-rs/polars](https://github.com/pola-rs/polars)<br>表データの処理が速く、待たされない<br>`データ` | 40,257 | <a href="https://www.star-history.com/#pola-rs/polars&Date"><img src="https://api.star-history.com/svg?repos=pola-rs/polars&type=Date" width="260" alt="pola-rs/polars のスター推移グラフ"></a> |
| 5 | [apache/kafka](https://github.com/apache/kafka)<br>システム間のイベントの流れを、分散基盤で運ぶ<br>`データ` | 34,122 | <a href="https://www.star-history.com/#apache/kafka&Date"><img src="https://api.star-history.com/svg?repos=apache/kafka&type=Date" width="260" alt="apache/kafka のスター推移グラフ"></a> |
| 6 | [apache/arrow](https://github.com/apache/arrow)<br>言語が違っても、データはそのまま通じる<br>`データ` | 17,274 | <a href="https://www.star-history.com/#apache/arrow&Date"><img src="https://api.star-history.com/svg?repos=apache/arrow&type=Date" width="260" alt="apache/arrow のスター推移グラフ"></a> |
| 7 | [dbt-labs/dbt-core](https://github.com/dbt-labs/dbt-core)<br>データ変換を、ソフトウェア開発のやり方で<br>`データ` | 14,115 | <a href="https://www.star-history.com/#dbt-labs/dbt-core&Date"><img src="https://api.star-history.com/svg?repos=dbt-labs/dbt-core&type=Date" width="260" alt="dbt-labs/dbt-core のスター推移グラフ"></a> |
| 8 | [jupyter/notebook](https://github.com/jupyter/notebook)<br>ブラウザでコードを書き、結果をその場で確認<br>`データ` | 13,458 | <a href="https://www.star-history.com/#jupyter/notebook&Date"><img src="https://api.star-history.com/svg?repos=jupyter/notebook&type=Date" width="260" alt="jupyter/notebook のスター推移グラフ"></a> |

---

役に立ったら、ほかの人にも見つけてもらえるようリポジトリにスターを付けてください。

引用の仕方：[CITATION.cff](CITATION.cff) を見てください。

数字の出し方と参加方法：[docs/HOW_IT_WORKS.ja.md](docs/HOW_IT_WORKS.ja.md)。新規リポジトリのルール：[docs/NEW_ARRIVALS.md](docs/NEW_ARRIVALS.md)。カテゴリ：[docs/CATEGORIES.md](docs/CATEGORIES.md)。プルリクエスト：[CONTRIBUTING.md](CONTRIBUTING.md)。
