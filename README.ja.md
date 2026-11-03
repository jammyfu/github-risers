[English](README.md) | [简体中文](README.zh-Hans.md) | [繁體中文](README.zh-Hant.md) | **日本語** | [한국어](README.ko.md)

# GitHub スター急上昇ランキング / GitHub Risers

<img src=".github/social-preview.png" alt="GitHub スター急上昇ランキング / GitHub Risers" width="640">

[![MIT](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE) [![CI](https://github.com/jammyfu/github-risers/actions/workflows/ci.yml/badge.svg)](https://github.com/jammyfu/github-risers/actions/workflows/ci.yml) [![updated](https://img.shields.io/badge/dynamic/json?url=https%3A%2F%2Fraw.githubusercontent.com%2Fjammyfu%2Fgithub-risers%2Fmain%2Fdata%2Fstats.json&query=%24.today_utc&label=updated&color=brightgreen)](latest/rankings.ja.md)

総スター数ではなく、1 日あたりに増えたスター数で GitHub リポジトリを並べます。AI が先頭で、開発者ツール、セキュリティ、Web / フロントエンド、インフラ、デザイン / クリエイティブ、データが続きます。1 日 2 回更新。

データ取得 2026-11-02 23:18（UTC）。1 日 2 回：北京時間 0 時（UTC+8）、ロサンゼルス時間 0 時（America/Los_Angeles）。

[ウェブサイト](https://jammyfu.github.io/github-risers/) · [仕組み](docs/HOW_IT_WORKS.ja.md) · [ファクト](docs/FACTS.md) · [履歴](rankings/README.ja.md) · [最新](latest/rankings.ja.md)

## 今回のカテゴリ別 1 位

| カテゴリ | 新着 1 位（7 日） | 今週 1 位 | 今月 1 位 | 今年 1 位 | 総スター 1 位 |
|---|---|---|---|---|---|
| **[AI](#ai)** ★ メイン | [wangzan101/Mika](https://github.com/wangzan101/Mika)<br>1,203/日 | [morluto/rea](https://github.com/morluto/rea)<br>4,904/日 | [morluto/rea](https://github.com/morluto/rea)<br>13,987/日 | [deepseek-ai/deepseek-harness](https://github.com/deepseek-ai/deepseek-harness)<br>3,318/日 | [morluto/rea](https://github.com/morluto/rea)<br>422,740 ★ |
| **[開発者ツール](#開発者ツール)** | [Verlintas/NOIR](https://github.com/Verlintas/NOIR)<br>610/日 | [zed-industries/zed](https://github.com/zed-industries/zed)<br>56.6/日 | [zed-industries/zed](https://github.com/zed-industries/zed)<br>52.9/日 | [zed-industries/zed](https://github.com/zed-industries/zed)<br>70.3/日 | [oven-sh/bun](https://github.com/oven-sh/bun)<br>96,519 ★ |
| **[セキュリティ](#セキュリティ)** | なし | [projectdiscovery/nuclei](https://github.com/projectdiscovery/nuclei)<br>32.7/日 | [projectdiscovery/nuclei](https://github.com/projectdiscovery/nuclei)<br>30.6/日 | [aquasecurity/trivy](https://github.com/aquasecurity/trivy)<br>27.7/日 | [aquasecurity/trivy](https://github.com/aquasecurity/trivy)<br>38,917 ★ |
| **[Web / フロントエンド](#web--フロントエンド)** | [shipwords-dev/shipwords](https://github.com/shipwords-dev/shipwords)<br>60.7/日 | [shadcn-ui/ui](https://github.com/shadcn-ui/ui)<br>95.4/日 | [shadcn-ui/ui](https://github.com/shadcn-ui/ui)<br>87.4/日 | [shadcn-ui/ui](https://github.com/shadcn-ui/ui)<br>83.2/日 | [facebook/react](https://github.com/facebook/react)<br>251,874 ★ |
| **[インフラ](#インフラ)** | [davemessew/AgentFlux](https://github.com/davemessew/AgentFlux)<br>38.8/日 | [caddyserver/caddy](https://github.com/caddyserver/caddy)<br>37.9/日 | [caddyserver/caddy](https://github.com/caddyserver/caddy)<br>84.0/日 | [caddyserver/caddy](https://github.com/caddyserver/caddy)<br>32.5/日 | [kubernetes/kubernetes](https://github.com/kubernetes/kubernetes)<br>128,619 ★ |
| **[デザイン / クリエイティブ](#デザイン--クリエイティブ)** | [patch-gg/pixelfx](https://github.com/patch-gg/pixelfx)<br>940/日 | [excalidraw/excalidraw](https://github.com/excalidraw/excalidraw)<br>70.3/日 | [excalidraw/excalidraw](https://github.com/excalidraw/excalidraw)<br>66.0/日 | [excalidraw/excalidraw](https://github.com/excalidraw/excalidraw)<br>74.0/日 | [excalidraw/excalidraw](https://github.com/excalidraw/excalidraw)<br>135,054 ★ |
| **[データ](#データ)** | なし | [duckdb/duckdb](https://github.com/duckdb/duckdb)<br>29.9/日 | [duckdb/duckdb](https://github.com/duckdb/duckdb)<br>30.9/日 | [duckdb/duckdb](https://github.com/duckdb/duckdb)<br>25.6/日 | [apache/superset](https://github.com/apache/superset)<br>75,392 ★ |

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
| 1 | [wangzan101/Mika](https://github.com/wangzan101/Mika)<br>スマホ操作が面倒なら、エージェントにお任せ | 2026-10-29<br><sub>4.4 日</sub> | 5,250 | 1,203.0 | <a href="https://www.star-history.com/#wangzan101/Mika&Date"><img src="https://api.star-history.com/svg?repos=wangzan101/Mika&type=Date" width="260" alt="wangzan101/Mika のスター推移グラフ"></a> |
| 2 | [caru-ini/stack-diagram](https://github.com/caru-ini/stack-diagram)<br>構成図を描くのが面倒？一文で公式ロゴ付き図が完成 | 2026-11-01<br><sub>1.7 日</sub> | 1,156 | 665.0 | <a href="https://www.star-history.com/#caru-ini/stack-diagram&Date"><img src="https://api.star-history.com/svg?repos=caru-ini/stack-diagram&type=Date" width="260" alt="caru-ini/stack-diagram のスター推移グラフ"></a> |
| 3 | [Balanov/uncut](https://github.com/Balanov/uncut)<br>勝手なコード切断を防ぎ、無損失でエージェントを動かす | 2026-11-01<br><sub>1.2 日</sub> | 571 | 457.1 | <a href="https://www.star-history.com/#Balanov/uncut&Date"><img src="https://api.star-history.com/svg?repos=Balanov/uncut&type=Date" width="260" alt="Balanov/uncut のスター推移グラフ"></a> |
| 4 | [haydenschmitty/floorplan](https://github.com/haydenschmitty/floorplan)<br>アプリの組み立てが、この地図で見える | 2026-10-27<br><sub>6.5 日</sub> | 2,227 | 344.3 | <a href="https://www.star-history.com/#haydenschmitty/floorplan&Date"><img src="https://api.star-history.com/svg?repos=haydenschmitty/floorplan&type=Date" width="260" alt="haydenschmitty/floorplan のスター推移グラフ"></a> |
| 5 | [modelflare-ai/AnyModelBot](https://github.com/modelflare-ai/AnyModelBot)<br>単一ボットに縛られず、ローカルで自由なモデルを動かす | 2026-10-27<br><sub>6.6 日</sub> | 1,328 | 201.1 | <a href="https://www.star-history.com/#modelflare-ai/AnyModelBot&Date"><img src="https://api.star-history.com/svg?repos=modelflare-ai/AnyModelBot&type=Date" width="260" alt="modelflare-ai/AnyModelBot のスター推移グラフ"></a> |
| 6 | [NiazMorshed2007/reanimate](https://github.com/NiazMorshed2007/reanimate)<br>アニメ再現が難しい？1コマずつ解析して一致を証明 | 2026-10-29<br><sub>4.7 日</sub> | 944 | 200.6 | <a href="https://www.star-history.com/#NiazMorshed2007/reanimate&Date"><img src="https://api.star-history.com/svg?repos=NiazMorshed2007/reanimate&type=Date" width="260" alt="NiazMorshed2007/reanimate のスター推移グラフ"></a> |
| 7 | [N1nEmAn/sapper-v2](https://github.com/N1nEmAn/sapper-v2)<br>セキュリティ診断の手間を、AI自律テストで解消 | 2026-10-30<br><sub>3.3 日</sub> | 596 | 178.6 | <a href="https://www.star-history.com/#N1nEmAn/sapper-v2&Date"><img src="https://api.star-history.com/svg?repos=N1nEmAn/sapper-v2&type=Date" width="260" alt="N1nEmAn/sapper-v2 のスター推移グラフ"></a> |
| 8 | [zhanghao123vip/ai-manju-skills](https://github.com/zhanghao123vip/ai-manju-skills)<br>アイデア一つから AI 漫画動画の全工程を作成 | 2026-10-31<br><sub>2.8 日</sub> | 458 | 161.8 | <a href="https://www.star-history.com/#zhanghao123vip/ai-manju-skills&Date"><img src="https://api.star-history.com/svg?repos=zhanghao123vip/ai-manju-skills&type=Date" width="260" alt="zhanghao123vip/ai-manju-skills のスター推移グラフ"></a> |
| 9 | [sleepy-zone/ai-ref-library-cn](https://github.com/sleepy-zone/ai-ref-library-cn)<br>AI作画の参考が欲しい？顔・ポーズ・服装の素材集 | 2026-10-29<br><sub>4.3 日</sub> | 667 | 154.2 | <a href="https://www.star-history.com/#sleepy-zone/ai-ref-library-cn&Date"><img src="https://api.star-history.com/svg?repos=sleepy-zone/ai-ref-library-cn&type=Date" width="260" alt="sleepy-zone/ai-ref-library-cn のスター推移グラフ"></a> |
| 10 | [alchaincyf/huashu-bird-sticker](https://github.com/alchaincyf/huashu-bird-sticker)<br>鳥の素材が見つからない？11,064種の鳥を網羅 | 2026-10-30<br><sub>3.8 日</sub> | 572 | 152.6 | <a href="https://www.star-history.com/#alchaincyf/huashu-bird-sticker&Date"><img src="https://api.star-history.com/svg?repos=alchaincyf/huashu-bird-sticker&type=Date" width="260" alt="alchaincyf/huashu-bird-sticker のスター推移グラフ"></a> |

### 今週もっとも伸びた（直近 7 日）

| # | プロジェクト | 増加数 | スター/日 | 総スター数 | スター推移 |
|---|---|---:|---:|---:|---|
| 1 | [morluto/rea](https://github.com/morluto/rea)<br>AI でどんなソフトもクローンできる<br>`AI` | +34,330 | 4,904.3 | 422,740 | <a href="https://www.star-history.com/#morluto/rea&Date"><img src="https://api.star-history.com/svg?repos=morluto/rea&type=Date" width="260" alt="morluto/rea のスター推移グラフ"></a> |
| 2 | [cloudflare/security-audit-skill](https://github.com/cloudflare/security-audit-skill)<br>AI が脆弱性を探し、別の AI が一件ずつ検証<br>`AI` | +9,348 | 1,335.4 | 57,354 | <a href="https://www.star-history.com/#cloudflare/security-audit-skill&Date"><img src="https://api.star-history.com/svg?repos=cloudflare/security-audit-skill&type=Date" width="260" alt="cloudflare/security-audit-skill のスター推移グラフ"></a> |
| 3 | [deepseek-ai/deepseek-harness](https://github.com/deepseek-ai/deepseek-harness)<br>欲しいエージェントは、プラグインで自分で組む<br>`AI` | +7,360 | 1,051.4 | 269,552 | <a href="https://www.star-history.com/#deepseek-ai/deepseek-harness&Date"><img src="https://api.star-history.com/svg?repos=deepseek-ai/deepseek-harness&type=Date" width="260" alt="deepseek-ai/deepseek-harness のスター推移グラフ"></a> |
| 4 | [stablyai/orca](https://github.com/stablyai/orca)<br>複数の AI に書かせて、どれが良いか一目で<br>`AI` | +6,941 | 991.6 | 113,572 | <a href="https://www.star-history.com/#stablyai/orca&Date"><img src="https://api.star-history.com/svg?repos=stablyai/orca&type=Date" width="260" alt="stablyai/orca のスター推移グラフ"></a> |
| 5 | [thedotmack/claude-mem](https://github.com/thedotmack/claude-mem)<br>AI が前回の続きを忘れなくなる<br>`AI` | +6,863 | 980.4 | 110,698 | <a href="https://www.star-history.com/#thedotmack/claude-mem&Date"><img src="https://api.star-history.com/svg?repos=thedotmack/claude-mem&type=Date" width="260" alt="thedotmack/claude-mem のスター推移グラフ"></a> |
| 6 | [yetone/magpie](https://github.com/yetone/magpie)<br>コーディング AI のモデルを替え、枠切れでも続行<br>`AI` | +6,346 | 906.6 | 28,379 | <a href="https://www.star-history.com/#yetone/magpie&Date"><img src="https://api.star-history.com/svg?repos=yetone/magpie&type=Date" width="260" alt="yetone/magpie のスター推移グラフ"></a> |
| 7 | [affaan-m/ECC](https://github.com/affaan-m/ECC)<br>コーディング AI に記憶・スキル・安全チェックを<br>`AI` | +6,249 | 892.7 | 295,627 | <a href="https://www.star-history.com/#affaan-m/ECC&Date"><img src="https://api.star-history.com/svg?repos=affaan-m/ECC&type=Date" width="260" alt="affaan-m/ECC のスター推移グラフ"></a> |
| 8 | [DietrichGebert/ponytail](https://github.com/DietrichGebert/ponytail)<br>AI の無駄なコードを減らし、必要な所は正しく<br>`AI` | +6,192 | 884.6 | 182,863 | <a href="https://www.star-history.com/#DietrichGebert/ponytail&Date"><img src="https://api.star-history.com/svg?repos=DietrichGebert/ponytail&type=Date" width="260" alt="DietrichGebert/ponytail のスター推移グラフ"></a> |
| 9 | [Leonxlnx/taste-skill](https://github.com/Leonxlnx/taste-skill)<br>AI が同じ見た目のページばかり作るのを止める<br>`AI` | +5,591 | 798.7 | 108,684 | <a href="https://www.star-history.com/#Leonxlnx/taste-skill&Date"><img src="https://api.star-history.com/svg?repos=Leonxlnx/taste-skill&type=Date" width="260" alt="Leonxlnx/taste-skill のスター推移グラフ"></a> |
| 10 | [Graphify-Labs/graphify](https://github.com/Graphify-Labs/graphify)<br>大きすぎて読めない時は、まずこの地図から<br>`AI` | +5,381 | 768.7 | 141,159 | <a href="https://www.star-history.com/#Graphify-Labs/graphify&Date"><img src="https://api.star-history.com/svg?repos=Graphify-Labs/graphify&type=Date" width="260" alt="Graphify-Labs/graphify のスター推移グラフ"></a> |

### 今月もっとも伸びた（直近 30 日）

| # | プロジェクト | 増加数 | スター/日 | 総スター数 | スター推移 |
|---|---|---:|---:|---:|---|
| 1 | [morluto/rea](https://github.com/morluto/rea)<br>AI でどんなソフトもクローンできる<br>`AI` | +419,602 | 13,986.7 | 422,740 | <a href="https://www.star-history.com/#morluto/rea&Date"><img src="https://api.star-history.com/svg?repos=morluto/rea&type=Date" width="260" alt="morluto/rea のスター推移グラフ"></a> |
| 2 | [cloudflare/security-audit-skill](https://github.com/cloudflare/security-audit-skill)<br>AI が脆弱性を探し、別の AI が一件ずつ検証<br>`AI` | +33,053 | 1,101.8 | 57,354 | <a href="https://www.star-history.com/#cloudflare/security-audit-skill&Date"><img src="https://api.star-history.com/svg?repos=cloudflare/security-audit-skill&type=Date" width="260" alt="cloudflare/security-audit-skill のスター推移グラフ"></a> |
| 3 | [DietrichGebert/ponytail](https://github.com/DietrichGebert/ponytail)<br>AI の無駄なコードを減らし、必要な所は正しく<br>`AI` | +31,390 | 1,046.3 | 182,863 | <a href="https://www.star-history.com/#DietrichGebert/ponytail&Date"><img src="https://api.star-history.com/svg?repos=DietrichGebert/ponytail&type=Date" width="260" alt="DietrichGebert/ponytail のスター推移グラフ"></a> |
| 4 | [stablyai/orca](https://github.com/stablyai/orca)<br>複数の AI に書かせて、どれが良いか一目で<br>`AI` | +29,569 | 985.6 | 113,572 | <a href="https://www.star-history.com/#stablyai/orca&Date"><img src="https://api.star-history.com/svg?repos=stablyai/orca&type=Date" width="260" alt="stablyai/orca のスター推移グラフ"></a> |
| 5 | [deepseek-ai/deepseek-harness](https://github.com/deepseek-ai/deepseek-harness)<br>欲しいエージェントは、プラグインで自分で組む<br>`AI` | +27,731 | 924.4 | 269,552 | <a href="https://www.star-history.com/#deepseek-ai/deepseek-harness&Date"><img src="https://api.star-history.com/svg?repos=deepseek-ai/deepseek-harness&type=Date" width="260" alt="deepseek-ai/deepseek-harness のスター推移グラフ"></a> |
| 6 | [affaan-m/ECC](https://github.com/affaan-m/ECC)<br>コーディング AI に記憶・スキル・安全チェックを<br>`AI` | +25,054 | 835.1 | 295,627 | <a href="https://www.star-history.com/#affaan-m/ECC&Date"><img src="https://api.star-history.com/svg?repos=affaan-m/ECC&type=Date" width="260" alt="affaan-m/ECC のスター推移グラフ"></a> |
| 7 | [yetone/magpie](https://github.com/yetone/magpie)<br>コーディング AI のモデルを替え、枠切れでも続行<br>`AI` | +23,768 | 792.3 | 28,379 | <a href="https://www.star-history.com/#yetone/magpie&Date"><img src="https://api.star-history.com/svg?repos=yetone/magpie&type=Date" width="260" alt="yetone/magpie のスター推移グラフ"></a> |
| 8 | [heygen-com/hyperframes](https://github.com/heygen-com/hyperframes)<br>編集できなくても、Web ページ感覚で動画に<br>`AI` | +21,653 | 721.8 | 77,709 | <a href="https://www.star-history.com/#heygen-com/hyperframes&Date"><img src="https://api.star-history.com/svg?repos=heygen-com/hyperframes&type=Date" width="260" alt="heygen-com/hyperframes のスター推移グラフ"></a> |
| 9 | [Panniantong/Agent-Reach](https://github.com/Panniantong/Agent-Reach)<br>Twitter・YouTube・小紅書を AI が代わりに検索<br>`AI` | +19,273 | 642.4 | 108,066 | <a href="https://www.star-history.com/#Panniantong/Agent-Reach&Date"><img src="https://api.star-history.com/svg?repos=Panniantong/Agent-Reach&type=Date" width="260" alt="Panniantong/Agent-Reach のスター推移グラフ"></a> |
| 10 | [Graphify-Labs/graphify](https://github.com/Graphify-Labs/graphify)<br>大きすぎて読めない時は、まずこの地図から<br>`AI` | +18,134 | 604.5 | 141,159 | <a href="https://www.star-history.com/#Graphify-Labs/graphify&Date"><img src="https://api.star-history.com/svg?repos=Graphify-Labs/graphify&type=Date" width="260" alt="Graphify-Labs/graphify のスター推移グラフ"></a> |

### 今年もっとも伸びた（直近 365 日）

| # | プロジェクト | 増加数 | スター/日 | 総スター数 | スター推移 |
|---|---|---:|---:|---:|---|
| 1 | [deepseek-ai/deepseek-harness](https://github.com/deepseek-ai/deepseek-harness)<br>欲しいエージェントは、プラグインで自分で組む<br>`AI` | +268,781 | 3,318.3 †<br><sub>÷81日</sub> | 269,552 | <a href="https://www.star-history.com/#deepseek-ai/deepseek-harness&Date"><img src="https://api.star-history.com/svg?repos=deepseek-ai/deepseek-harness&type=Date" width="260" alt="deepseek-ai/deepseek-harness のスター推移グラフ"></a> |
| 2 | [morluto/rea](https://github.com/morluto/rea)<br>AI でどんなソフトもクローンできる<br>`AI` | +420,016 | 2,079.3 †<br><sub>÷202日</sub> | 422,740 | <a href="https://www.star-history.com/#morluto/rea&Date"><img src="https://api.star-history.com/svg?repos=morluto/rea&type=Date" width="260" alt="morluto/rea のスター推移グラフ"></a> |
| 3 | [DietrichGebert/ponytail](https://github.com/DietrichGebert/ponytail)<br>AI の無駄なコードを減らし、必要な所は正しく<br>`AI` | +182,348 | 1,275.2 †<br><sub>÷143日</sub> | 182,863 | <a href="https://www.star-history.com/#DietrichGebert/ponytail&Date"><img src="https://api.star-history.com/svg?repos=DietrichGebert/ponytail&type=Date" width="260" alt="DietrichGebert/ponytail のスター推移グラフ"></a> |
| 4 | [openclaw/openclaw](https://github.com/openclaw/openclaw)<br>仕事を片付ける AI アシスタント、動くのは自分の端末<br>`AI` | +393,647 | 1,147.7 †<br><sub>÷343日</sub> | 393,753 | <a href="https://www.star-history.com/#openclaw/openclaw&Date"><img src="https://api.star-history.com/svg?repos=openclaw/openclaw&type=Date" width="260" alt="openclaw/openclaw のスター推移グラフ"></a> |
| 5 | [affaan-m/ECC](https://github.com/affaan-m/ECC)<br>コーディング AI に記憶・スキル・安全チェックを<br>`AI` | +294,971 | 1,024.2 †<br><sub>÷288日</sub> | 295,627 | <a href="https://www.star-history.com/#affaan-m/ECC&Date"><img src="https://api.star-history.com/svg?repos=affaan-m/ECC&type=Date" width="260" alt="affaan-m/ECC のスター推移グラフ"></a> |
| 6 | [NousResearch/hermes-agent](https://github.com/NousResearch/hermes-agent)<br>使うほど仕事が上手くなる AI アシスタント<br>`AI` | +259,591 | 711.2 | 259,851 | <a href="https://www.star-history.com/#NousResearch/hermes-agent&Date"><img src="https://api.star-history.com/svg?repos=NousResearch/hermes-agent&type=Date" width="260" alt="NousResearch/hermes-agent のスター推移グラフ"></a> |
| 7 | [yetone/magpie](https://github.com/yetone/magpie)<br>コーディング AI のモデルを替え、枠切れでも続行<br>`AI` | +28,009 | 700.2 †<br><sub>÷40日</sub> | 28,379 | <a href="https://www.star-history.com/#yetone/magpie&Date"><img src="https://api.star-history.com/svg?repos=yetone/magpie&type=Date" width="260" alt="yetone/magpie のスター推移グラフ"></a> |
| 8 | [Graphify-Labs/graphify](https://github.com/Graphify-Labs/graphify)<br>大きすぎて読めない時は、まずこの地図から<br>`AI` | +140,701 | 660.6 †<br><sub>÷213日</sub> | 141,159 | <a href="https://www.star-history.com/#Graphify-Labs/graphify&Date"><img src="https://api.star-history.com/svg?repos=Graphify-Labs/graphify&type=Date" width="260" alt="Graphify-Labs/graphify のスター推移グラフ"></a> |
| 9 | [anomalyco/opencode](https://github.com/anomalyco/opencode)<br>ターミナルで、オープンソースの AI がコードを書く<br>`AI` | +195,028 | 534.3 | 224,103 | <a href="https://www.star-history.com/#anomalyco/opencode&Date"><img src="https://api.star-history.com/svg?repos=anomalyco/opencode&type=Date" width="260" alt="anomalyco/opencode のスター推移グラフ"></a> |
| 10 | [stablyai/orca](https://github.com/stablyai/orca)<br>複数の AI に書かせて、どれが良いか一目で<br>`AI` | +112,912 | 490.9 †<br><sub>÷230日</sub> | 113,572 | <a href="https://www.star-history.com/#stablyai/orca&Date"><img src="https://api.star-history.com/svg?repos=stablyai/orca&type=Date" width="260" alt="stablyai/orca のスター推移グラフ"></a> |

† リポジトリの作成が集計期間より新しいため、スター/日は期間全体ではなくリポジトリの経過日数（数値の下に表示）で割っています。

### 総スター数ランキング（累計）

| # | プロジェクト | 総スター数 | スター推移 |
|---|---|---:|---|
| 1 | [morluto/rea](https://github.com/morluto/rea)<br>AI でどんなソフトもクローンできる<br>`AI` | 422,740 | <a href="https://www.star-history.com/#morluto/rea&Date"><img src="https://api.star-history.com/svg?repos=morluto/rea&type=Date" width="260" alt="morluto/rea のスター推移グラフ"></a> |
| 2 | [openclaw/openclaw](https://github.com/openclaw/openclaw)<br>仕事を片付ける AI アシスタント、動くのは自分の端末<br>`AI` | 393,753 | <a href="https://www.star-history.com/#openclaw/openclaw&Date"><img src="https://api.star-history.com/svg?repos=openclaw/openclaw&type=Date" width="260" alt="openclaw/openclaw のスター推移グラフ"></a> |
| 3 | [affaan-m/ECC](https://github.com/affaan-m/ECC)<br>コーディング AI に記憶・スキル・安全チェックを<br>`AI` | 295,627 | <a href="https://www.star-history.com/#affaan-m/ECC&Date"><img src="https://api.star-history.com/svg?repos=affaan-m/ECC&type=Date" width="260" alt="affaan-m/ECC のスター推移グラフ"></a> |
| 4 | [deepseek-ai/deepseek-harness](https://github.com/deepseek-ai/deepseek-harness)<br>欲しいエージェントは、プラグインで自分で組む<br>`AI` | 269,552 | <a href="https://www.star-history.com/#deepseek-ai/deepseek-harness&Date"><img src="https://api.star-history.com/svg?repos=deepseek-ai/deepseek-harness&type=Date" width="260" alt="deepseek-ai/deepseek-harness のスター推移グラフ"></a> |
| 5 | [NousResearch/hermes-agent](https://github.com/NousResearch/hermes-agent)<br>使うほど仕事が上手くなる AI アシスタント<br>`AI` | 259,851 | <a href="https://www.star-history.com/#NousResearch/hermes-agent&Date"><img src="https://api.star-history.com/svg?repos=NousResearch/hermes-agent&type=Date" width="260" alt="NousResearch/hermes-agent のスター推移グラフ"></a> |
| 6 | [anomalyco/opencode](https://github.com/anomalyco/opencode)<br>ターミナルで、オープンソースの AI がコードを書く<br>`AI` | 224,103 | <a href="https://www.star-history.com/#anomalyco/opencode&Date"><img src="https://api.star-history.com/svg?repos=anomalyco/opencode&type=Date" width="260" alt="anomalyco/opencode のスター推移グラフ"></a> |
| 7 | [anthropics/skills](https://github.com/anthropics/skills)<br>Claude スキルの書き方は、公式の例で学ぶ<br>`AI` | 186,760 | <a href="https://www.star-history.com/#anthropics/skills&Date"><img src="https://api.star-history.com/svg?repos=anthropics/skills&type=Date" width="260" alt="anthropics/skills のスター推移グラフ"></a> |
| 8 | [DietrichGebert/ponytail](https://github.com/DietrichGebert/ponytail)<br>AI の無駄なコードを減らし、必要な所は正しく<br>`AI` | 182,863 | <a href="https://www.star-history.com/#DietrichGebert/ponytail&Date"><img src="https://api.star-history.com/svg?repos=DietrichGebert/ponytail&type=Date" width="260" alt="DietrichGebert/ponytail のスター推移グラフ"></a> |
| 9 | [farion1231/cc-switch](https://github.com/farion1231/cc-switch)<br>設定ファイルを触らず、ワンクリックで切替<br>`AI` | 151,211 | <a href="https://www.star-history.com/#farion1231/cc-switch&Date"><img src="https://api.star-history.com/svg?repos=farion1231/cc-switch&type=Date" width="260" alt="farion1231/cc-switch のスター推移グラフ"></a> |
| 10 | [nextlevelbuilder/ui-ux-pro-max-skill](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill)<br>AI が作る画面を、プロのデザインらしく<br>`AI` | 144,268 | <a href="https://www.star-history.com/#nextlevelbuilder/ui-ux-pro-max-skill&Date"><img src="https://api.star-history.com/svg?repos=nextlevelbuilder/ui-ux-pro-max-skill&type=Date" width="260" alt="nextlevelbuilder/ui-ux-pro-max-skill のスター推移グラフ"></a> |

## 開発者ツール

> CLI・エディタ・パッケージマネージャ・リンタ・ビルドツール

### 7 日以内の新着で最も熱いリポジトリ（作成から 7 日以内）

| # | プロジェクト | 作成日（UTC） | 総スター数 | スター/日 | スター推移 |
|---|---|---|---:|---:|---|
| 1 | [Verlintas/NOIR](https://github.com/Verlintas/NOIR)<br>Android アプリの情報漏えいをスキャンして安全に対処 | 2026-10-31<br><sub>2.1 日</sub> | 1,265 | 610.5 | <a href="https://www.star-history.com/#Verlintas/NOIR&Date"><img src="https://api.star-history.com/svg?repos=Verlintas/NOIR&type=Date" width="260" alt="Verlintas/NOIR のスター推移グラフ"></a> |
| 2 | [AssassinCreator/steam-stash-value-report-card](https://github.com/AssassinCreator/steam-stash-value-report-card)<br>在庫価値が不明なら、ターミナルでSteamを査定 | 2026-11-02<br><sub>1.0 日</sub> | 590 | 590.0 | <a href="https://www.star-history.com/#AssassinCreator/steam-stash-value-report-card&Date"><img src="https://api.star-history.com/svg?repos=AssassinCreator/steam-stash-value-report-card&type=Date" width="260" alt="AssassinCreator/steam-stash-value-report-card のスター推移グラフ"></a> |
| 3 | [Straitbrashadow/minecraft-ai-mod-builder](https://github.com/Straitbrashadow/minecraft-ai-mod-builder)<br>作りたい建築を入力しワールドに一発配置 | 2026-10-30<br><sub>3.1 日</sub> | 200 | 64.8 | <a href="https://www.star-history.com/#Straitbrashadow/minecraft-ai-mod-builder&Date"><img src="https://api.star-history.com/svg?repos=Straitbrashadow/minecraft-ai-mod-builder&type=Date" width="260" alt="Straitbrashadow/minecraft-ai-mod-builder のスター推移グラフ"></a> |
| 4 | [DiplomatHearth/roblox-ai-place-diff](https://github.com/DiplomatHearth/roblox-ai-place-diff)<br>エージェントの変更を確認してから適用 | 2026-10-30<br><sub>3.1 日</sub> | 160 | 52.2 | <a href="https://www.star-history.com/#DiplomatHearth/roblox-ai-place-diff&Date"><img src="https://api.star-history.com/svg?repos=DiplomatHearth/roblox-ai-place-diff&type=Date" width="260" alt="DiplomatHearth/roblox-ai-place-diff のスター推移グラフ"></a> |
| 5 | [Xpropel/Pi-Remote](https://github.com/Xpropel/Pi-Remote)<br>ブラウザからpiのコーディングエージェントを遠隔操作 | 2026-10-28<br><sub>5.5 日</sub> | 261 | 47.3 | <a href="https://www.star-history.com/#Xpropel/Pi-Remote&Date"><img src="https://api.star-history.com/svg?repos=Xpropel/Pi-Remote&type=Date" width="260" alt="Xpropel/Pi-Remote のスター推移グラフ"></a> |
| 6 | [muaaz9329/cheap-ag](https://github.com/muaaz9329/cheap-ag)<br>制限を気にせず安価なモデルでコードを書く | 2026-10-28<br><sub>5.0 日</sub> | 227 | 45.1 | <a href="https://www.star-history.com/#muaaz9329/cheap-ag&Date"><img src="https://api.star-history.com/svg?repos=muaaz9329/cheap-ag&type=Date" width="260" alt="muaaz9329/cheap-ag のスター推移グラフ"></a> |
| 7 | [tianfuzhibuyuci/readme-visual-kit](https://github.com/tianfuzhibuyuci/readme-visual-kit)<br>ローカルで説明文から3枚のREADME図を生成 | 2026-10-27<br><sub>6.4 日</sub> | 208 | 32.4 | <a href="https://www.star-history.com/#tianfuzhibuyuci/readme-visual-kit&Date"><img src="https://api.star-history.com/svg?repos=tianfuzhibuyuci/readme-visual-kit&type=Date" width="260" alt="tianfuzhibuyuci/readme-visual-kit のスター推移グラフ"></a> |
| 8 | [khanh020905/my-office](https://github.com/khanh020905/my-office)<br>Claude Code用の3Dオフィス空間 | 2026-10-28<br><sub>5.5 日</sub> | 154 | 28.3 | <a href="https://www.star-history.com/#khanh020905/my-office&Date"><img src="https://api.star-history.com/svg?repos=khanh020905/my-office&type=Date" width="260" alt="khanh020905/my-office のスター推移グラフ"></a> |
| 9 | [kyy-logs/code-review-skill](https://github.com/kyy-logs/code-review-skill)<br>確かな根拠でコード検証を助けるレビュー用スキル | 2026-10-29<br><sub>4.6 日</sub> | 119 | 25.6 | <a href="https://www.star-history.com/#kyy-logs/code-review-skill&Date"><img src="https://api.star-history.com/svg?repos=kyy-logs/code-review-skill&type=Date" width="260" alt="kyy-logs/code-review-skill のスター推移グラフ"></a> |
| 10 | [dufu1991/foldgit](https://github.com/dufu1991/foldgit)<br>差分確認からコミットまで1画面で完結 | 2026-10-28<br><sub>5.8 日</sub> | 128 | 21.9 | <a href="https://www.star-history.com/#dufu1991/foldgit&Date"><img src="https://api.star-history.com/svg?repos=dufu1991/foldgit&type=Date" width="260" alt="dufu1991/foldgit のスター推移グラフ"></a> |

### 今週もっとも伸びた（直近 7 日）

| # | プロジェクト | 増加数 | スター/日 | 総スター数 | スター推移 |
|---|---|---:|---:|---:|---|
| 1 | [zed-industries/zed](https://github.com/zed-industries/zed)<br>すぐ開けて、みんなで一緒にコードを書ける<br>`開発者ツール` | +396 | 56.6 | 92,573 | <a href="https://www.star-history.com/#zed-industries/zed&Date"><img src="https://api.star-history.com/svg?repos=zed-industries/zed&type=Date" width="260" alt="zed-industries/zed のスター推移グラフ"></a> |
| 2 | [astral-sh/uv](https://github.com/astral-sh/uv)<br>Python パッケージの導入で待たされない<br>`開発者ツール` | +315 | 45.0 | 91,480 | <a href="https://www.star-history.com/#astral-sh/uv&Date"><img src="https://api.star-history.com/svg?repos=astral-sh/uv&type=Date" width="260" alt="astral-sh/uv のスター推移グラフ"></a> |
| 3 | [jdx/mise](https://github.com/jdx/mise)<br>開発ツール・環境変数・タスクを 1 つで管理<br>`開発者ツール` | +284 | 40.6 | 35,689 | <a href="https://www.star-history.com/#jdx/mise&Date"><img src="https://api.star-history.com/svg?repos=jdx/mise&type=Date" width="260" alt="jdx/mise のスター推移グラフ"></a> |
| 4 | [BurntSushi/ripgrep](https://github.com/BurntSushi/ripgrep)<br>フォルダ全体の文字検索が grep より速い<br>`開発者ツール` | +227 | 32.4 | 69,660 | <a href="https://www.star-history.com/#BurntSushi/ripgrep&Date"><img src="https://api.star-history.com/svg?repos=BurntSushi/ripgrep&type=Date" width="260" alt="BurntSushi/ripgrep のスター推移グラフ"></a> |
| 5 | [oven-sh/bun](https://github.com/oven-sh/bun)<br>実行・バンドル・テスト・導入を 1 つで<br>`開発者ツール` | +138 | 19.7 | 96,519 | <a href="https://www.star-history.com/#oven-sh/bun&Date"><img src="https://api.star-history.com/svg?repos=oven-sh/bun&type=Date" width="260" alt="oven-sh/bun のスター推移グラフ"></a> |
| 6 | [cli/cli](https://github.com/cli/cli)<br>ブラウザを開かず、コマンドラインで GitHub を操作<br>`開発者ツール` | +110 | 15.7 | 46,845 | <a href="https://www.star-history.com/#cli/cli&Date"><img src="https://api.star-history.com/svg?repos=cli/cli&type=Date" width="260" alt="cli/cli のスター推移グラフ"></a> |
| 7 | [helix-editor/helix](https://github.com/helix-editor/helix)<br>構文ハイライトも言語サーバーも内蔵のテキストエディタ<br>`開発者ツール` | +101 | 14.4 | 46,774 | <a href="https://www.star-history.com/#helix-editor/helix&Date"><img src="https://api.star-history.com/svg?repos=helix-editor/helix&type=Date" width="260" alt="helix-editor/helix のスター推移グラフ"></a> |
| 8 | [biomejs/biome](https://github.com/biomejs/biome)<br>Web コードの整形とチェックを 1 つで<br>`開発者ツール` | +51 | 7.3 | 26,041 | <a href="https://www.star-history.com/#biomejs/biome&Date"><img src="https://api.star-history.com/svg?repos=biomejs/biome&type=Date" width="260" alt="biomejs/biome のスター推移グラフ"></a> |

### 今月もっとも伸びた（直近 30 日）

| # | プロジェクト | 増加数 | スター/日 | 総スター数 | スター推移 |
|---|---|---:|---:|---:|---|
| 1 | [zed-industries/zed](https://github.com/zed-industries/zed)<br>すぐ開けて、みんなで一緒にコードを書ける<br>`開発者ツール` | +1,588 | 52.9 | 92,573 | <a href="https://www.star-history.com/#zed-industries/zed&Date"><img src="https://api.star-history.com/svg?repos=zed-industries/zed&type=Date" width="260" alt="zed-industries/zed のスター推移グラフ"></a> |
| 2 | [astral-sh/uv](https://github.com/astral-sh/uv)<br>Python パッケージの導入で待たされない<br>`開発者ツール` | +1,265 | 42.2 | 91,480 | <a href="https://www.star-history.com/#astral-sh/uv&Date"><img src="https://api.star-history.com/svg?repos=astral-sh/uv&type=Date" width="260" alt="astral-sh/uv のスター推移グラフ"></a> |
| 3 | [jdx/mise](https://github.com/jdx/mise)<br>開発ツール・環境変数・タスクを 1 つで管理<br>`開発者ツール` | +1,193 | 39.8 | 35,689 | <a href="https://www.star-history.com/#jdx/mise&Date"><img src="https://api.star-history.com/svg?repos=jdx/mise&type=Date" width="260" alt="jdx/mise のスター推移グラフ"></a> |
| 4 | [BurntSushi/ripgrep](https://github.com/BurntSushi/ripgrep)<br>フォルダ全体の文字検索が grep より速い<br>`開発者ツール` | +989 | 33.0 | 69,660 | <a href="https://www.star-history.com/#BurntSushi/ripgrep&Date"><img src="https://api.star-history.com/svg?repos=BurntSushi/ripgrep&type=Date" width="260" alt="BurntSushi/ripgrep のスター推移グラフ"></a> |
| 5 | [oven-sh/bun](https://github.com/oven-sh/bun)<br>実行・バンドル・テスト・導入を 1 つで<br>`開発者ツール` | +684 | 22.8 | 96,519 | <a href="https://www.star-history.com/#oven-sh/bun&Date"><img src="https://api.star-history.com/svg?repos=oven-sh/bun&type=Date" width="260" alt="oven-sh/bun のスター推移グラフ"></a> |
| 6 | [helix-editor/helix](https://github.com/helix-editor/helix)<br>構文ハイライトも言語サーバーも内蔵のテキストエディタ<br>`開発者ツール` | +451 | 15.0 | 46,774 | <a href="https://www.star-history.com/#helix-editor/helix&Date"><img src="https://api.star-history.com/svg?repos=helix-editor/helix&type=Date" width="260" alt="helix-editor/helix のスター推移グラフ"></a> |
| 7 | [cli/cli](https://github.com/cli/cli)<br>ブラウザを開かず、コマンドラインで GitHub を操作<br>`開発者ツール` | +422 | 14.1 | 46,845 | <a href="https://www.star-history.com/#cli/cli&Date"><img src="https://api.star-history.com/svg?repos=cli/cli&type=Date" width="260" alt="cli/cli のスター推移グラフ"></a> |
| 8 | [biomejs/biome](https://github.com/biomejs/biome)<br>Web コードの整形とチェックを 1 つで<br>`開発者ツール` | +213 | 7.1 | 26,041 | <a href="https://www.star-history.com/#biomejs/biome&Date"><img src="https://api.star-history.com/svg?repos=biomejs/biome&type=Date" width="260" alt="biomejs/biome のスター推移グラフ"></a> |

### 今年もっとも伸びた（直近 365 日）

| # | プロジェクト | 増加数 | スター/日 | 総スター数 | スター推移 |
|---|---|---:|---:|---:|---|
| 1 | [zed-industries/zed](https://github.com/zed-industries/zed)<br>すぐ開けて、みんなで一緒にコードを書ける<br>`開発者ツール` | +25,673 | 70.3 | 92,573 | <a href="https://www.star-history.com/#zed-industries/zed&Date"><img src="https://api.star-history.com/svg?repos=zed-industries/zed&type=Date" width="260" alt="zed-industries/zed のスター推移グラフ"></a> |
| 2 | [astral-sh/uv](https://github.com/astral-sh/uv)<br>Python パッケージの導入で待たされない<br>`開発者ツール` | +21,302 | 58.4 | 91,480 | <a href="https://www.star-history.com/#astral-sh/uv&Date"><img src="https://api.star-history.com/svg?repos=astral-sh/uv&type=Date" width="260" alt="astral-sh/uv のスター推移グラフ"></a> |
| 3 | [oven-sh/bun](https://github.com/oven-sh/bun)<br>実行・バンドル・テスト・導入を 1 つで<br>`開発者ツール` | +16,560 | 45.4 | 96,519 | <a href="https://www.star-history.com/#oven-sh/bun&Date"><img src="https://api.star-history.com/svg?repos=oven-sh/bun&type=Date" width="260" alt="oven-sh/bun のスター推移グラフ"></a> |
| 4 | [jdx/mise](https://github.com/jdx/mise)<br>開発ツール・環境変数・タスクを 1 つで管理<br>`開発者ツール` | +15,052 | 41.2 | 35,689 | <a href="https://www.star-history.com/#jdx/mise&Date"><img src="https://api.star-history.com/svg?repos=jdx/mise&type=Date" width="260" alt="jdx/mise のスター推移グラフ"></a> |
| 5 | [BurntSushi/ripgrep](https://github.com/BurntSushi/ripgrep)<br>フォルダ全体の文字検索が grep より速い<br>`開発者ツール` | +13,358 | 36.6 | 69,660 | <a href="https://www.star-history.com/#BurntSushi/ripgrep&Date"><img src="https://api.star-history.com/svg?repos=BurntSushi/ripgrep&type=Date" width="260" alt="BurntSushi/ripgrep のスター推移グラフ"></a> |
| 6 | [helix-editor/helix](https://github.com/helix-editor/helix)<br>構文ハイライトも言語サーバーも内蔵のテキストエディタ<br>`開発者ツール` | +6,766 | 18.5 | 46,774 | <a href="https://www.star-history.com/#helix-editor/helix&Date"><img src="https://api.star-history.com/svg?repos=helix-editor/helix&type=Date" width="260" alt="helix-editor/helix のスター推移グラフ"></a> |
| 7 | [cli/cli](https://github.com/cli/cli)<br>ブラウザを開かず、コマンドラインで GitHub を操作<br>`開発者ツール` | +6,262 | 17.2 | 46,845 | <a href="https://www.star-history.com/#cli/cli&Date"><img src="https://api.star-history.com/svg?repos=cli/cli&type=Date" width="260" alt="cli/cli のスター推移グラフ"></a> |
| 8 | [biomejs/biome](https://github.com/biomejs/biome)<br>Web コードの整形とチェックを 1 つで<br>`開発者ツール` | +4,582 | 12.6 | 26,041 | <a href="https://www.star-history.com/#biomejs/biome&Date"><img src="https://api.star-history.com/svg?repos=biomejs/biome&type=Date" width="260" alt="biomejs/biome のスター推移グラフ"></a> |

### 総スター数ランキング（累計）

| # | プロジェクト | 総スター数 | スター推移 |
|---|---|---:|---|
| 1 | [oven-sh/bun](https://github.com/oven-sh/bun)<br>実行・バンドル・テスト・導入を 1 つで<br>`開発者ツール` | 96,519 | <a href="https://www.star-history.com/#oven-sh/bun&Date"><img src="https://api.star-history.com/svg?repos=oven-sh/bun&type=Date" width="260" alt="oven-sh/bun のスター推移グラフ"></a> |
| 2 | [zed-industries/zed](https://github.com/zed-industries/zed)<br>すぐ開けて、みんなで一緒にコードを書ける<br>`開発者ツール` | 92,573 | <a href="https://www.star-history.com/#zed-industries/zed&Date"><img src="https://api.star-history.com/svg?repos=zed-industries/zed&type=Date" width="260" alt="zed-industries/zed のスター推移グラフ"></a> |
| 3 | [astral-sh/uv](https://github.com/astral-sh/uv)<br>Python パッケージの導入で待たされない<br>`開発者ツール` | 91,480 | <a href="https://www.star-history.com/#astral-sh/uv&Date"><img src="https://api.star-history.com/svg?repos=astral-sh/uv&type=Date" width="260" alt="astral-sh/uv のスター推移グラフ"></a> |
| 4 | [BurntSushi/ripgrep](https://github.com/BurntSushi/ripgrep)<br>フォルダ全体の文字検索が grep より速い<br>`開発者ツール` | 69,660 | <a href="https://www.star-history.com/#BurntSushi/ripgrep&Date"><img src="https://api.star-history.com/svg?repos=BurntSushi/ripgrep&type=Date" width="260" alt="BurntSushi/ripgrep のスター推移グラフ"></a> |
| 5 | [cli/cli](https://github.com/cli/cli)<br>ブラウザを開かず、コマンドラインで GitHub を操作<br>`開発者ツール` | 46,845 | <a href="https://www.star-history.com/#cli/cli&Date"><img src="https://api.star-history.com/svg?repos=cli/cli&type=Date" width="260" alt="cli/cli のスター推移グラフ"></a> |
| 6 | [helix-editor/helix](https://github.com/helix-editor/helix)<br>構文ハイライトも言語サーバーも内蔵のテキストエディタ<br>`開発者ツール` | 46,774 | <a href="https://www.star-history.com/#helix-editor/helix&Date"><img src="https://api.star-history.com/svg?repos=helix-editor/helix&type=Date" width="260" alt="helix-editor/helix のスター推移グラフ"></a> |
| 7 | [jdx/mise](https://github.com/jdx/mise)<br>開発ツール・環境変数・タスクを 1 つで管理<br>`開発者ツール` | 35,689 | <a href="https://www.star-history.com/#jdx/mise&Date"><img src="https://api.star-history.com/svg?repos=jdx/mise&type=Date" width="260" alt="jdx/mise のスター推移グラフ"></a> |
| 8 | [biomejs/biome](https://github.com/biomejs/biome)<br>Web コードの整形とチェックを 1 つで<br>`開発者ツール` | 26,041 | <a href="https://www.star-history.com/#biomejs/biome&Date"><img src="https://api.star-history.com/svg?repos=biomejs/biome&type=Date" width="260" alt="biomejs/biome のスター推移グラフ"></a> |

## セキュリティ

> 脆弱性スキャン・SAST・サプライチェーン・ランタイムセキュリティ

### 7 日以内の新着で最も熱いリポジトリ（作成から 7 日以内）

今回の実行で条件を満たす新着リポジトリはありませんでした。

### 今週もっとも伸びた（直近 7 日）

| # | プロジェクト | 増加数 | スター/日 | 総スター数 | スター推移 |
|---|---|---:|---:|---:|---|
| 1 | [projectdiscovery/nuclei](https://github.com/projectdiscovery/nuclei)<br>テンプレート 1 つで、脆弱性を一括スキャン<br>`セキュリティ` | +229 | 32.7 | 32,545 | <a href="https://www.star-history.com/#projectdiscovery/nuclei&Date"><img src="https://api.star-history.com/svg?repos=projectdiscovery/nuclei&type=Date" width="260" alt="projectdiscovery/nuclei のスター推移グラフ"></a> |
| 2 | [aquasecurity/trivy](https://github.com/aquasecurity/trivy)<br>コンテナもコードも、安全チェックは 1 回で<br>`セキュリティ` | +201 | 28.7 | 38,917 | <a href="https://www.star-history.com/#aquasecurity/trivy&Date"><img src="https://api.star-history.com/svg?repos=aquasecurity/trivy&type=Date" width="260" alt="aquasecurity/trivy のスター推移グラフ"></a> |
| 3 | [semgrep/semgrep](https://github.com/semgrep/semgrep)<br>コードの問題は、コミット前に見つけ出す<br>`セキュリティ` | +130 | 18.6 | 17,413 | <a href="https://www.star-history.com/#semgrep/semgrep&Date"><img src="https://api.star-history.com/svg?repos=semgrep/semgrep&type=Date" width="260" alt="semgrep/semgrep のスター推移グラフ"></a> |
| 4 | [OWASP/CheatSheetSeries](https://github.com/OWASP/CheatSheetSeries)<br>アプリのセキュリティは、この簡潔な手引きで<br>`セキュリティ` | +107 | 15.3 | 33,852 | <a href="https://www.star-history.com/#OWASP/CheatSheetSeries&Date"><img src="https://api.star-history.com/svg?repos=OWASP/CheatSheetSeries&type=Date" width="260" alt="OWASP/CheatSheetSeries のスター推移グラフ"></a> |
| 5 | [google/osv-scanner](https://github.com/google/osv-scanner)<br>使っている依存は安全か、スキャンすればわかる<br>`セキュリティ` | +83 | 11.9 | 11,368 | <a href="https://www.star-history.com/#google/osv-scanner&Date"><img src="https://api.star-history.com/svg?repos=google/osv-scanner&type=Date" width="260" alt="google/osv-scanner のスター推移グラフ"></a> |
| 6 | [anchore/grype](https://github.com/anchore/grype)<br>コンテナイメージに脆弱性がないか、スキャンで確認<br>`セキュリティ` | +49 | 7.0 | 13,163 | <a href="https://www.star-history.com/#anchore/grype&Date"><img src="https://api.star-history.com/svg?repos=anchore/grype&type=Date" width="260" alt="anchore/grype のスター推移グラフ"></a> |
| 7 | [falcosecurity/falco](https://github.com/falcosecurity/falco)<br>クラウドの異常に、すぐ気づける<br>`セキュリティ` | +26 | 3.7 | 9,547 | <a href="https://www.star-history.com/#falcosecurity/falco&Date"><img src="https://api.star-history.com/svg?repos=falcosecurity/falco&type=Date" width="260" alt="falcosecurity/falco のスター推移グラフ"></a> |
| 8 | [securego/gosec](https://github.com/securego/gosec)<br>Go コードのセキュリティ問題を、スキャンで見つける<br>`セキュリティ` | +12 | 1.7 | 8,996 | <a href="https://www.star-history.com/#securego/gosec&Date"><img src="https://api.star-history.com/svg?repos=securego/gosec&type=Date" width="260" alt="securego/gosec のスター推移グラフ"></a> |

### 今月もっとも伸びた（直近 30 日）

| # | プロジェクト | 増加数 | スター/日 | 総スター数 | スター推移 |
|---|---|---:|---:|---:|---|
| 1 | [projectdiscovery/nuclei](https://github.com/projectdiscovery/nuclei)<br>テンプレート 1 つで、脆弱性を一括スキャン<br>`セキュリティ` | +917 | 30.6 | 32,545 | <a href="https://www.star-history.com/#projectdiscovery/nuclei&Date"><img src="https://api.star-history.com/svg?repos=projectdiscovery/nuclei&type=Date" width="260" alt="projectdiscovery/nuclei のスター推移グラフ"></a> |
| 2 | [aquasecurity/trivy](https://github.com/aquasecurity/trivy)<br>コンテナもコードも、安全チェックは 1 回で<br>`セキュリティ` | +761 | 25.4 | 38,917 | <a href="https://www.star-history.com/#aquasecurity/trivy&Date"><img src="https://api.star-history.com/svg?repos=aquasecurity/trivy&type=Date" width="260" alt="aquasecurity/trivy のスター推移グラフ"></a> |
| 3 | [semgrep/semgrep](https://github.com/semgrep/semgrep)<br>コードの問題は、コミット前に見つけ出す<br>`セキュリティ` | +580 | 19.3 | 17,413 | <a href="https://www.star-history.com/#semgrep/semgrep&Date"><img src="https://api.star-history.com/svg?repos=semgrep/semgrep&type=Date" width="260" alt="semgrep/semgrep のスター推移グラフ"></a> |
| 4 | [OWASP/CheatSheetSeries](https://github.com/OWASP/CheatSheetSeries)<br>アプリのセキュリティは、この簡潔な手引きで<br>`セキュリティ` | +479 | 16.0 | 33,852 | <a href="https://www.star-history.com/#OWASP/CheatSheetSeries&Date"><img src="https://api.star-history.com/svg?repos=OWASP/CheatSheetSeries&type=Date" width="260" alt="OWASP/CheatSheetSeries のスター推移グラフ"></a> |
| 5 | [google/osv-scanner](https://github.com/google/osv-scanner)<br>使っている依存は安全か、スキャンすればわかる<br>`セキュリティ` | +240 | 8.0 | 11,368 | <a href="https://www.star-history.com/#google/osv-scanner&Date"><img src="https://api.star-history.com/svg?repos=google/osv-scanner&type=Date" width="260" alt="google/osv-scanner のスター推移グラフ"></a> |
| 6 | [anchore/grype](https://github.com/anchore/grype)<br>コンテナイメージに脆弱性がないか、スキャンで確認<br>`セキュリティ` | +202 | 6.7 | 13,163 | <a href="https://www.star-history.com/#anchore/grype&Date"><img src="https://api.star-history.com/svg?repos=anchore/grype&type=Date" width="260" alt="anchore/grype のスター推移グラフ"></a> |
| 7 | [falcosecurity/falco](https://github.com/falcosecurity/falco)<br>クラウドの異常に、すぐ気づける<br>`セキュリティ` | +123 | 4.1 | 9,547 | <a href="https://www.star-history.com/#falcosecurity/falco&Date"><img src="https://api.star-history.com/svg?repos=falcosecurity/falco&type=Date" width="260" alt="falcosecurity/falco のスター推移グラフ"></a> |
| 8 | [securego/gosec](https://github.com/securego/gosec)<br>Go コードのセキュリティ問題を、スキャンで見つける<br>`セキュリティ` | +43 | 1.4 | 8,996 | <a href="https://www.star-history.com/#securego/gosec&Date"><img src="https://api.star-history.com/svg?repos=securego/gosec&type=Date" width="260" alt="securego/gosec のスター推移グラフ"></a> |

### 今年もっとも伸びた（直近 365 日）

| # | プロジェクト | 増加数 | スター/日 | 総スター数 | スター推移 |
|---|---|---:|---:|---:|---|
| 1 | [aquasecurity/trivy](https://github.com/aquasecurity/trivy)<br>コンテナもコードも、安全チェックは 1 回で<br>`セキュリティ` | +10,106 | 27.7 | 38,917 | <a href="https://www.star-history.com/#aquasecurity/trivy&Date"><img src="https://api.star-history.com/svg?repos=aquasecurity/trivy&type=Date" width="260" alt="aquasecurity/trivy のスター推移グラフ"></a> |
| 2 | [projectdiscovery/nuclei](https://github.com/projectdiscovery/nuclei)<br>テンプレート 1 つで、脆弱性を一括スキャン<br>`セキュリティ` | +7,603 | 20.8 | 32,545 | <a href="https://www.star-history.com/#projectdiscovery/nuclei&Date"><img src="https://api.star-history.com/svg?repos=projectdiscovery/nuclei&type=Date" width="260" alt="projectdiscovery/nuclei のスター推移グラフ"></a> |
| 3 | [semgrep/semgrep](https://github.com/semgrep/semgrep)<br>コードの問題は、コミット前に見つけ出す<br>`セキュリティ` | +4,372 | 12.0 | 17,413 | <a href="https://www.star-history.com/#semgrep/semgrep&Date"><img src="https://api.star-history.com/svg?repos=semgrep/semgrep&type=Date" width="260" alt="semgrep/semgrep のスター推移グラフ"></a> |
| 4 | [OWASP/CheatSheetSeries](https://github.com/OWASP/CheatSheetSeries)<br>アプリのセキュリティは、この簡潔な手引きで<br>`セキュリティ` | +3,524 | 9.7 | 33,852 | <a href="https://www.star-history.com/#OWASP/CheatSheetSeries&Date"><img src="https://api.star-history.com/svg?repos=OWASP/CheatSheetSeries&type=Date" width="260" alt="OWASP/CheatSheetSeries のスター推移グラフ"></a> |
| 5 | [google/osv-scanner](https://github.com/google/osv-scanner)<br>使っている依存は安全か、スキャンすればわかる<br>`セキュリティ` | +3,488 | 9.6 | 11,368 | <a href="https://www.star-history.com/#google/osv-scanner&Date"><img src="https://api.star-history.com/svg?repos=google/osv-scanner&type=Date" width="260" alt="google/osv-scanner のスター推移グラフ"></a> |
| 6 | [anchore/grype](https://github.com/anchore/grype)<br>コンテナイメージに脆弱性がないか、スキャンで確認<br>`セキュリティ` | +2,355 | 6.5 | 13,163 | <a href="https://www.star-history.com/#anchore/grype&Date"><img src="https://api.star-history.com/svg?repos=anchore/grype&type=Date" width="260" alt="anchore/grype のスター推移グラフ"></a> |
| 7 | [falcosecurity/falco](https://github.com/falcosecurity/falco)<br>クラウドの異常に、すぐ気づける<br>`セキュリティ` | +1,271 | 3.5 | 9,547 | <a href="https://www.star-history.com/#falcosecurity/falco&Date"><img src="https://api.star-history.com/svg?repos=falcosecurity/falco&type=Date" width="260" alt="falcosecurity/falco のスター推移グラフ"></a> |
| 8 | [securego/gosec](https://github.com/securego/gosec)<br>Go コードのセキュリティ問題を、スキャンで見つける<br>`セキュリティ` | +561 | 1.5 | 8,996 | <a href="https://www.star-history.com/#securego/gosec&Date"><img src="https://api.star-history.com/svg?repos=securego/gosec&type=Date" width="260" alt="securego/gosec のスター推移グラフ"></a> |

### 総スター数ランキング（累計）

| # | プロジェクト | 総スター数 | スター推移 |
|---|---|---:|---|
| 1 | [aquasecurity/trivy](https://github.com/aquasecurity/trivy)<br>コンテナもコードも、安全チェックは 1 回で<br>`セキュリティ` | 38,917 | <a href="https://www.star-history.com/#aquasecurity/trivy&Date"><img src="https://api.star-history.com/svg?repos=aquasecurity/trivy&type=Date" width="260" alt="aquasecurity/trivy のスター推移グラフ"></a> |
| 2 | [OWASP/CheatSheetSeries](https://github.com/OWASP/CheatSheetSeries)<br>アプリのセキュリティは、この簡潔な手引きで<br>`セキュリティ` | 33,852 | <a href="https://www.star-history.com/#OWASP/CheatSheetSeries&Date"><img src="https://api.star-history.com/svg?repos=OWASP/CheatSheetSeries&type=Date" width="260" alt="OWASP/CheatSheetSeries のスター推移グラフ"></a> |
| 3 | [projectdiscovery/nuclei](https://github.com/projectdiscovery/nuclei)<br>テンプレート 1 つで、脆弱性を一括スキャン<br>`セキュリティ` | 32,545 | <a href="https://www.star-history.com/#projectdiscovery/nuclei&Date"><img src="https://api.star-history.com/svg?repos=projectdiscovery/nuclei&type=Date" width="260" alt="projectdiscovery/nuclei のスター推移グラフ"></a> |
| 4 | [semgrep/semgrep](https://github.com/semgrep/semgrep)<br>コードの問題は、コミット前に見つけ出す<br>`セキュリティ` | 17,413 | <a href="https://www.star-history.com/#semgrep/semgrep&Date"><img src="https://api.star-history.com/svg?repos=semgrep/semgrep&type=Date" width="260" alt="semgrep/semgrep のスター推移グラフ"></a> |
| 5 | [anchore/grype](https://github.com/anchore/grype)<br>コンテナイメージに脆弱性がないか、スキャンで確認<br>`セキュリティ` | 13,163 | <a href="https://www.star-history.com/#anchore/grype&Date"><img src="https://api.star-history.com/svg?repos=anchore/grype&type=Date" width="260" alt="anchore/grype のスター推移グラフ"></a> |
| 6 | [google/osv-scanner](https://github.com/google/osv-scanner)<br>使っている依存は安全か、スキャンすればわかる<br>`セキュリティ` | 11,368 | <a href="https://www.star-history.com/#google/osv-scanner&Date"><img src="https://api.star-history.com/svg?repos=google/osv-scanner&type=Date" width="260" alt="google/osv-scanner のスター推移グラフ"></a> |
| 7 | [falcosecurity/falco](https://github.com/falcosecurity/falco)<br>クラウドの異常に、すぐ気づける<br>`セキュリティ` | 9,547 | <a href="https://www.star-history.com/#falcosecurity/falco&Date"><img src="https://api.star-history.com/svg?repos=falcosecurity/falco&type=Date" width="260" alt="falcosecurity/falco のスター推移グラフ"></a> |
| 8 | [securego/gosec](https://github.com/securego/gosec)<br>Go コードのセキュリティ問題を、スキャンで見つける<br>`セキュリティ` | 8,996 | <a href="https://www.star-history.com/#securego/gosec&Date"><img src="https://api.star-history.com/svg?repos=securego/gosec&type=Date" width="260" alt="securego/gosec のスター推移グラフ"></a> |

## Web / フロントエンド

> フロントエンド枠組み・UI キット・CSS・ブラウザツール

### 7 日以内の新着で最も熱いリポジトリ（作成から 7 日以内）

| # | プロジェクト | 作成日（UTC） | 総スター数 | スター/日 | スター推移 |
|---|---|---|---:|---:|---|
| 1 | [shipwords-dev/shipwords](https://github.com/shipwords-dev/shipwords)<br>新ワードを見つけたら、午後には AI サイトを公開 | 2026-10-28<br><sub>5.7 日</sub> | 346 | 60.7 | <a href="https://www.star-history.com/#shipwords-dev/shipwords&Date"><img src="https://api.star-history.com/svg?repos=shipwords-dev/shipwords&type=Date" width="260" alt="shipwords-dev/shipwords のスター推移グラフ"></a> |
| 2 | [mofan6/Moect](https://github.com/mofan6/Moect)<br>WeChatの会話を残したい時に、オフラインで書き出し保存 | 2026-10-31<br><sub>2.5 日</sub> | 144 | 57.1 | <a href="https://www.star-history.com/#mofan6/Moect&Date"><img src="https://api.star-history.com/svg?repos=mofan6/Moect&type=Date" width="260" alt="mofan6/Moect のスター推移グラフ"></a> |
| 3 | [Lavagroabide/aegis-spreadwatch](https://github.com/Lavagroabide/aegis-spreadwatch)<br>CS2の取引利益が曖昧？手数料込みの純利益を確認 | 2026-10-30<br><sub>3.0 日</sub> | 156 | 52.2 | <a href="https://www.star-history.com/#Lavagroabide/aegis-spreadwatch&Date"><img src="https://api.star-history.com/svg?repos=Lavagroabide/aegis-spreadwatch&type=Date" width="260" alt="Lavagroabide/aegis-spreadwatch のスター推移グラフ"></a> |
| 4 | [solderdatabraid29/aegis-vaultgrid](https://github.com/solderdatabraid29/aegis-vaultgrid)<br>CS2の注文手数料が不安？アカウント不要で計画 | 2026-10-30<br><sub>3.0 日</sub> | 139 | 46.5 | <a href="https://www.star-history.com/#solderdatabraid29/aegis-vaultgrid&Date"><img src="https://api.star-history.com/svg?repos=solderdatabraid29/aegis-vaultgrid&type=Date" width="260" alt="solderdatabraid29/aegis-vaultgrid のスター推移グラフ"></a> |
| 5 | [Townlanurture/aegis-skin-terminal](https://github.com/Townlanurture/aegis-skin-terminal)<br>CS2の価格差が見えない？手数料込みでローカル確認 | 2026-10-30<br><sub>3.0 日</sub> | 136 | 45.4 | <a href="https://www.star-history.com/#Townlanurture/aegis-skin-terminal&Date"><img src="https://api.star-history.com/svg?repos=Townlanurture/aegis-skin-terminal&type=Date" width="260" alt="Townlanurture/aegis-skin-terminal のスター推移グラフ"></a> |
| 6 | [zklmiao/prompt-vault](https://github.com/zklmiao/prompt-vault)<br>プロンプトの管理に困ったら、ローカルで保存 | 2026-10-28<br><sub>5.8 日</sub> | 241 | 41.6 | <a href="https://www.star-history.com/#zklmiao/prompt-vault&Date"><img src="https://api.star-history.com/svg?repos=zklmiao/prompt-vault&type=Date" width="260" alt="zklmiao/prompt-vault のスター推移グラフ"></a> |
| 7 | [jianxinss/iching-64-motion](https://github.com/jianxinss/iching-64-motion)<br>易経六十四卦をアニメに、すべてコードで | 2026-10-27<br><sub>6.9 日</sub> | 164 | 23.8 | <a href="https://www.star-history.com/#jianxinss/iching-64-motion&Date"><img src="https://api.star-history.com/svg?repos=jianxinss/iching-64-motion&type=Date" width="260" alt="jianxinss/iching-64-motion のスター推移グラフ"></a> |
| 8 | [floatboatai/OpenMinutes](https://github.com/floatboatai/OpenMinutes)<br>ボイスレコーダーの録音を、検索できる文字に | 2026-10-28<br><sub>5.4 日</sub> | 108 | 19.9 | <a href="https://www.star-history.com/#floatboatai/OpenMinutes&Date"><img src="https://api.star-history.com/svg?repos=floatboatai/OpenMinutes&type=Date" width="260" alt="floatboatai/OpenMinutes のスター推移グラフ"></a> |
| 9 | [fush520/fush-vue-mcp](https://github.com/fush520/fush-vue-mcp)<br>Vueの解析に困ったら、リバースとWebセキュリティテスト | 2026-10-27<br><sub>6.3 日</sub> | 104 | 16.5 | <a href="https://www.star-history.com/#fush520/fush-vue-mcp&Date"><img src="https://api.star-history.com/svg?repos=fush520/fush-vue-mcp&type=Date" width="260" alt="fush520/fush-vue-mcp のスター推移グラフ"></a> |

### 今週もっとも伸びた（直近 7 日）

| # | プロジェクト | 増加数 | スター/日 | 総スター数 | スター推移 |
|---|---|---:|---:|---:|---|
| 1 | [shadcn-ui/ui](https://github.com/shadcn-ui/ui)<br>見栄えの良い部品。コードは自分のもの、自由に改造<br>`Web / フロントエンド` | +668 | 95.4 | 127,202 | <a href="https://www.star-history.com/#shadcn-ui/ui&Date"><img src="https://api.star-history.com/svg?repos=shadcn-ui/ui&type=Date" width="260" alt="shadcn-ui/ui のスター推移グラフ"></a> |
| 2 | [facebook/react](https://github.com/facebook/react)<br>Web もネイティブアプリの画面も、これで作る<br>`Web / フロントエンド` | +346 | 49.4 | 251,874 | <a href="https://www.star-history.com/#facebook/react&Date"><img src="https://api.star-history.com/svg?repos=facebook/react&type=Date" width="260" alt="facebook/react のスター推移グラフ"></a> |
| 3 | [withastro/astro](https://github.com/withastro/astro)<br>コンテンツ中心のサイトを、軽量な出力で作る<br>`Web / フロントエンド` | +204 | 29.1 | 63,677 | <a href="https://www.star-history.com/#withastro/astro&Date"><img src="https://api.star-history.com/svg?repos=withastro/astro&type=Date" width="260" alt="withastro/astro のスター推移グラフ"></a> |
| 4 | [vercel/next.js](https://github.com/vercel/next.js)<br>React でサイトを丸ごと、フロントから裏側まで<br>`Web / フロントエンド` | +155 | 22.1 | 143,234 | <a href="https://www.star-history.com/#vercel/next.js&Date"><img src="https://api.star-history.com/svg?repos=vercel/next.js&type=Date" width="260" alt="vercel/next.js のスター推移グラフ"></a> |
| 5 | [sveltejs/svelte](https://github.com/sveltejs/svelte)<br>書いた部品を、コンパイラが効率的な Web コードに<br>`Web / フロントエンド` | +108 | 15.4 | 88,538 | <a href="https://www.star-history.com/#sveltejs/svelte&Date"><img src="https://api.star-history.com/svg?repos=sveltejs/svelte&type=Date" width="260" alt="sveltejs/svelte のスター推移グラフ"></a> |
| 6 | [tailwindlabs/tailwindcss](https://github.com/tailwindlabs/tailwindcss)<br>CSS を大量に書かなくても、独自デザインに<br>`Web / フロントエンド` | +106 | 15.1 | 98,055 | <a href="https://www.star-history.com/#tailwindlabs/tailwindcss&Date"><img src="https://api.star-history.com/svg?repos=tailwindlabs/tailwindcss&type=Date" width="260" alt="tailwindlabs/tailwindcss のスター推移グラフ"></a> |
| 7 | [vuejs/core](https://github.com/vuejs/core)<br>小さなページから始め、使う分だけ学べる<br>`Web / フロントエンド` | +80 | 11.4 | 54,820 | <a href="https://www.star-history.com/#vuejs/core&Date"><img src="https://api.star-history.com/svg?repos=vuejs/core&type=Date" width="260" alt="vuejs/core のスター推移グラフ"></a> |
| 8 | [tanstack/query](https://github.com/tanstack/query)<br>データ取得とキャッシュは、これに任せる<br>`Web / フロントエンド` | +48 | 6.9 | 50,521 | <a href="https://www.star-history.com/#tanstack/query&Date"><img src="https://api.star-history.com/svg?repos=tanstack/query&type=Date" width="260" alt="tanstack/query のスター推移グラフ"></a> |

### 今月もっとも伸びた（直近 30 日）

| # | プロジェクト | 増加数 | スター/日 | 総スター数 | スター推移 |
|---|---|---:|---:|---:|---|
| 1 | [shadcn-ui/ui](https://github.com/shadcn-ui/ui)<br>見栄えの良い部品。コードは自分のもの、自由に改造<br>`Web / フロントエンド` | +2,623 | 87.4 | 127,202 | <a href="https://www.star-history.com/#shadcn-ui/ui&Date"><img src="https://api.star-history.com/svg?repos=shadcn-ui/ui&type=Date" width="260" alt="shadcn-ui/ui のスター推移グラフ"></a> |
| 2 | [facebook/react](https://github.com/facebook/react)<br>Web もネイティブアプリの画面も、これで作る<br>`Web / フロントエンド` | +1,649 | 55.0 | 251,874 | <a href="https://www.star-history.com/#facebook/react&Date"><img src="https://api.star-history.com/svg?repos=facebook/react&type=Date" width="260" alt="facebook/react のスター推移グラフ"></a> |
| 3 | [withastro/astro](https://github.com/withastro/astro)<br>コンテンツ中心のサイトを、軽量な出力で作る<br>`Web / フロントエンド` | +764 | 25.5 | 63,677 | <a href="https://www.star-history.com/#withastro/astro&Date"><img src="https://api.star-history.com/svg?repos=withastro/astro&type=Date" width="260" alt="withastro/astro のスター推移グラフ"></a> |
| 4 | [vercel/next.js](https://github.com/vercel/next.js)<br>React でサイトを丸ごと、フロントから裏側まで<br>`Web / フロントエンド` | +738 | 24.6 | 143,234 | <a href="https://www.star-history.com/#vercel/next.js&Date"><img src="https://api.star-history.com/svg?repos=vercel/next.js&type=Date" width="260" alt="vercel/next.js のスター推移グラフ"></a> |
| 5 | [tailwindlabs/tailwindcss](https://github.com/tailwindlabs/tailwindcss)<br>CSS を大量に書かなくても、独自デザインに<br>`Web / フロントエンド` | +486 | 16.2 | 98,055 | <a href="https://www.star-history.com/#tailwindlabs/tailwindcss&Date"><img src="https://api.star-history.com/svg?repos=tailwindlabs/tailwindcss&type=Date" width="260" alt="tailwindlabs/tailwindcss のスター推移グラフ"></a> |
| 6 | [sveltejs/svelte](https://github.com/sveltejs/svelte)<br>書いた部品を、コンパイラが効率的な Web コードに<br>`Web / フロントエンド` | +486 | 16.2 | 88,538 | <a href="https://www.star-history.com/#sveltejs/svelte&Date"><img src="https://api.star-history.com/svg?repos=sveltejs/svelte&type=Date" width="260" alt="sveltejs/svelte のスター推移グラフ"></a> |
| 7 | [vuejs/core](https://github.com/vuejs/core)<br>小さなページから始め、使う分だけ学べる<br>`Web / フロントエンド` | +410 | 13.7 | 54,820 | <a href="https://www.star-history.com/#vuejs/core&Date"><img src="https://api.star-history.com/svg?repos=vuejs/core&type=Date" width="260" alt="vuejs/core のスター推移グラフ"></a> |
| 8 | [tanstack/query](https://github.com/tanstack/query)<br>データ取得とキャッシュは、これに任せる<br>`Web / フロントエンド` | +210 | 7.0 | 50,521 | <a href="https://www.star-history.com/#tanstack/query&Date"><img src="https://api.star-history.com/svg?repos=tanstack/query&type=Date" width="260" alt="tanstack/query のスター推移グラフ"></a> |

### 今年もっとも伸びた（直近 365 日）

| # | プロジェクト | 増加数 | スター/日 | 総スター数 | スター推移 |
|---|---|---:|---:|---:|---|
| 1 | [shadcn-ui/ui](https://github.com/shadcn-ui/ui)<br>見栄えの良い部品。コードは自分のもの、自由に改造<br>`Web / フロントエンド` | +30,353 | 83.2 | 127,202 | <a href="https://www.star-history.com/#shadcn-ui/ui&Date"><img src="https://api.star-history.com/svg?repos=shadcn-ui/ui&type=Date" width="260" alt="shadcn-ui/ui のスター推移グラフ"></a> |
| 2 | [facebook/react](https://github.com/facebook/react)<br>Web もネイティブアプリの画面も、これで作る<br>`Web / フロントエンド` | +15,193 | 41.6 | 251,874 | <a href="https://www.star-history.com/#facebook/react&Date"><img src="https://api.star-history.com/svg?repos=facebook/react&type=Date" width="260" alt="facebook/react のスター推移グラフ"></a> |
| 3 | [withastro/astro](https://github.com/withastro/astro)<br>コンテンツ中心のサイトを、軽量な出力で作る<br>`Web / フロントエンド` | +10,497 | 28.8 | 63,677 | <a href="https://www.star-history.com/#withastro/astro&Date"><img src="https://api.star-history.com/svg?repos=withastro/astro&type=Date" width="260" alt="withastro/astro のスター推移グラフ"></a> |
| 4 | [vercel/next.js](https://github.com/vercel/next.js)<br>React でサイトを丸ごと、フロントから裏側まで<br>`Web / フロントエンド` | +10,335 | 28.3 | 143,234 | <a href="https://www.star-history.com/#vercel/next.js&Date"><img src="https://api.star-history.com/svg?repos=vercel/next.js&type=Date" width="260" alt="vercel/next.js のスター推移グラフ"></a> |
| 5 | [tailwindlabs/tailwindcss](https://github.com/tailwindlabs/tailwindcss)<br>CSS を大量に書かなくても、独自デザインに<br>`Web / フロントエンド` | +8,527 | 23.4 | 98,055 | <a href="https://www.star-history.com/#tailwindlabs/tailwindcss&Date"><img src="https://api.star-history.com/svg?repos=tailwindlabs/tailwindcss&type=Date" width="260" alt="tailwindlabs/tailwindcss のスター推移グラフ"></a> |
| 6 | [sveltejs/svelte](https://github.com/sveltejs/svelte)<br>書いた部品を、コンパイラが効率的な Web コードに<br>`Web / フロントエンド` | +5,274 | 14.4 | 88,538 | <a href="https://www.star-history.com/#sveltejs/svelte&Date"><img src="https://api.star-history.com/svg?repos=sveltejs/svelte&type=Date" width="260" alt="sveltejs/svelte のスター推移グラフ"></a> |
| 7 | [tanstack/query](https://github.com/tanstack/query)<br>データ取得とキャッシュは、これに任せる<br>`Web / フロントエンド` | +3,856 | 10.6 | 50,521 | <a href="https://www.star-history.com/#tanstack/query&Date"><img src="https://api.star-history.com/svg?repos=tanstack/query&type=Date" width="260" alt="tanstack/query のスター推移グラフ"></a> |
| 8 | [vuejs/core](https://github.com/vuejs/core)<br>小さなページから始め、使う分だけ学べる<br>`Web / フロントエンド` | +3,622 | 9.9 | 54,820 | <a href="https://www.star-history.com/#vuejs/core&Date"><img src="https://api.star-history.com/svg?repos=vuejs/core&type=Date" width="260" alt="vuejs/core のスター推移グラフ"></a> |

### 総スター数ランキング（累計）

| # | プロジェクト | 総スター数 | スター推移 |
|---|---|---:|---|
| 1 | [facebook/react](https://github.com/facebook/react)<br>Web もネイティブアプリの画面も、これで作る<br>`Web / フロントエンド` | 251,874 | <a href="https://www.star-history.com/#facebook/react&Date"><img src="https://api.star-history.com/svg?repos=facebook/react&type=Date" width="260" alt="facebook/react のスター推移グラフ"></a> |
| 2 | [vercel/next.js](https://github.com/vercel/next.js)<br>React でサイトを丸ごと、フロントから裏側まで<br>`Web / フロントエンド` | 143,234 | <a href="https://www.star-history.com/#vercel/next.js&Date"><img src="https://api.star-history.com/svg?repos=vercel/next.js&type=Date" width="260" alt="vercel/next.js のスター推移グラフ"></a> |
| 3 | [shadcn-ui/ui](https://github.com/shadcn-ui/ui)<br>見栄えの良い部品。コードは自分のもの、自由に改造<br>`Web / フロントエンド` | 127,202 | <a href="https://www.star-history.com/#shadcn-ui/ui&Date"><img src="https://api.star-history.com/svg?repos=shadcn-ui/ui&type=Date" width="260" alt="shadcn-ui/ui のスター推移グラフ"></a> |
| 4 | [tailwindlabs/tailwindcss](https://github.com/tailwindlabs/tailwindcss)<br>CSS を大量に書かなくても、独自デザインに<br>`Web / フロントエンド` | 98,055 | <a href="https://www.star-history.com/#tailwindlabs/tailwindcss&Date"><img src="https://api.star-history.com/svg?repos=tailwindlabs/tailwindcss&type=Date" width="260" alt="tailwindlabs/tailwindcss のスター推移グラフ"></a> |
| 5 | [sveltejs/svelte](https://github.com/sveltejs/svelte)<br>書いた部品を、コンパイラが効率的な Web コードに<br>`Web / フロントエンド` | 88,538 | <a href="https://www.star-history.com/#sveltejs/svelte&Date"><img src="https://api.star-history.com/svg?repos=sveltejs/svelte&type=Date" width="260" alt="sveltejs/svelte のスター推移グラフ"></a> |
| 6 | [withastro/astro](https://github.com/withastro/astro)<br>コンテンツ中心のサイトを、軽量な出力で作る<br>`Web / フロントエンド` | 63,677 | <a href="https://www.star-history.com/#withastro/astro&Date"><img src="https://api.star-history.com/svg?repos=withastro/astro&type=Date" width="260" alt="withastro/astro のスター推移グラフ"></a> |
| 7 | [vuejs/core](https://github.com/vuejs/core)<br>小さなページから始め、使う分だけ学べる<br>`Web / フロントエンド` | 54,820 | <a href="https://www.star-history.com/#vuejs/core&Date"><img src="https://api.star-history.com/svg?repos=vuejs/core&type=Date" width="260" alt="vuejs/core のスター推移グラフ"></a> |
| 8 | [tanstack/query](https://github.com/tanstack/query)<br>データ取得とキャッシュは、これに任せる<br>`Web / フロントエンド` | 50,521 | <a href="https://www.star-history.com/#tanstack/query&Date"><img src="https://api.star-history.com/svg?repos=tanstack/query&type=Date" width="260" alt="tanstack/query のスター推移グラフ"></a> |

## インフラ

> コンテナ・Kubernetes・クラウド・ネットワーク・可観測性

### 7 日以内の新着で最も熱いリポジトリ（作成から 7 日以内）

| # | プロジェクト | 作成日（UTC） | 総スター数 | スター/日 | スター推移 |
|---|---|---|---:|---:|---|
| 1 | [davemessew/AgentFlux](https://github.com/davemessew/AgentFlux)<br>AI のワークフローを描いて、自分の環境で動かす | 2026-10-27<br><sub>6.4 日</sub> | 247 | 38.8 | <a href="https://www.star-history.com/#davemessew/AgentFlux&Date"><img src="https://api.star-history.com/svg?repos=davemessew/AgentFlux&type=Date" width="260" alt="davemessew/AgentFlux のスター推移グラフ"></a> |

### 今週もっとも伸びた（直近 7 日）

| # | プロジェクト | 増加数 | スター/日 | 総スター数 | スター推移 |
|---|---|---:|---:|---:|---|
| 1 | [caddyserver/caddy](https://github.com/caddyserver/caddy)<br>Web サーバー構築、HTTPS は自動で設定<br>`インフラ` | +265 | 37.9 | 78,663 | <a href="https://www.star-history.com/#caddyserver/caddy&Date"><img src="https://api.star-history.com/svg?repos=caddyserver/caddy&type=Date" width="260" alt="caddyserver/caddy のスター推移グラフ"></a> |
| 2 | [kubernetes/kubernetes](https://github.com/kubernetes/kubernetes)<br>コンテナが増えても、配備と拡張は任せる<br>`インフラ` | +203 | 29.0 | 128,619 | <a href="https://www.star-history.com/#kubernetes/kubernetes&Date"><img src="https://api.star-history.com/svg?repos=kubernetes/kubernetes&type=Date" width="260" alt="kubernetes/kubernetes のスター推移グラフ"></a> |
| 3 | [grafana/grafana](https://github.com/grafana/grafana)<br>指標・ログ・トレースを 1 つのパネルに<br>`インフラ` | +173 | 24.7 | 77,645 | <a href="https://www.star-history.com/#grafana/grafana&Date"><img src="https://api.star-history.com/svg?repos=grafana/grafana&type=Date" width="260" alt="grafana/grafana のスター推移グラフ"></a> |
| 4 | [prometheus/prometheus](https://github.com/prometheus/prometheus)<br>システムの不具合は、アラートが先に知らせる<br>`インフラ` | +158 | 22.6 | 66,915 | <a href="https://www.star-history.com/#prometheus/prometheus&Date"><img src="https://api.star-history.com/svg?repos=prometheus/prometheus&type=Date" width="260" alt="prometheus/prometheus のスター推移グラフ"></a> |
| 5 | [docker/compose](https://github.com/docker/compose)<br>複数のコンテナを 1 つのファイルでまとめて動かす<br>`インフラ` | +113 | 16.1 | 38,585 | <a href="https://www.star-history.com/#docker/compose&Date"><img src="https://api.star-history.com/svg?repos=docker/compose&type=Date" width="260" alt="docker/compose のスター推移グラフ"></a> |
| 6 | [hashicorp/terraform](https://github.com/hashicorp/terraform)<br>クラウド資源をコードにして、レビューもバージョン管理も<br>`インフラ` | +92 | 13.1 | 50,118 | <a href="https://www.star-history.com/#hashicorp/terraform&Date"><img src="https://api.star-history.com/svg?repos=hashicorp/terraform&type=Date" width="260" alt="hashicorp/terraform のスター推移グラフ"></a> |
| 7 | [traefik/traefik](https://github.com/traefik/traefik)<br>サービスが増えても、通信は自動で振り分け<br>`インフラ` | +89 | 12.7 | 65,446 | <a href="https://www.star-history.com/#traefik/traefik&Date"><img src="https://api.star-history.com/svg?repos=traefik/traefik&type=Date" width="260" alt="traefik/traefik のスター推移グラフ"></a> |
| 8 | [pulumi/pulumi](https://github.com/pulumi/pulumi)<br>使い慣れた言語で、クラウド資源を管理<br>`インフラ` | +30 | 4.3 | 25,840 | <a href="https://www.star-history.com/#pulumi/pulumi&Date"><img src="https://api.star-history.com/svg?repos=pulumi/pulumi&type=Date" width="260" alt="pulumi/pulumi のスター推移グラフ"></a> |

### 今月もっとも伸びた（直近 30 日）

| # | プロジェクト | 増加数 | スター/日 | 総スター数 | スター推移 |
|---|---|---:|---:|---:|---|
| 1 | [caddyserver/caddy](https://github.com/caddyserver/caddy)<br>Web サーバー構築、HTTPS は自動で設定<br>`インフラ` | +2,521 | 84.0 | 78,663 | <a href="https://www.star-history.com/#caddyserver/caddy&Date"><img src="https://api.star-history.com/svg?repos=caddyserver/caddy&type=Date" width="260" alt="caddyserver/caddy のスター推移グラフ"></a> |
| 2 | [kubernetes/kubernetes](https://github.com/kubernetes/kubernetes)<br>コンテナが増えても、配備と拡張は任せる<br>`インフラ` | +892 | 29.7 | 128,619 | <a href="https://www.star-history.com/#kubernetes/kubernetes&Date"><img src="https://api.star-history.com/svg?repos=kubernetes/kubernetes&type=Date" width="260" alt="kubernetes/kubernetes のスター推移グラフ"></a> |
| 3 | [grafana/grafana](https://github.com/grafana/grafana)<br>指標・ログ・トレースを 1 つのパネルに<br>`インフラ` | +746 | 24.9 | 77,645 | <a href="https://www.star-history.com/#grafana/grafana&Date"><img src="https://api.star-history.com/svg?repos=grafana/grafana&type=Date" width="260" alt="grafana/grafana のスター推移グラフ"></a> |
| 4 | [prometheus/prometheus](https://github.com/prometheus/prometheus)<br>システムの不具合は、アラートが先に知らせる<br>`インフラ` | +698 | 23.3 | 66,915 | <a href="https://www.star-history.com/#prometheus/prometheus&Date"><img src="https://api.star-history.com/svg?repos=prometheus/prometheus&type=Date" width="260" alt="prometheus/prometheus のスター推移グラフ"></a> |
| 5 | [traefik/traefik](https://github.com/traefik/traefik)<br>サービスが増えても、通信は自動で振り分け<br>`インフラ` | +482 | 16.1 | 65,446 | <a href="https://www.star-history.com/#traefik/traefik&Date"><img src="https://api.star-history.com/svg?repos=traefik/traefik&type=Date" width="260" alt="traefik/traefik のスター推移グラフ"></a> |
| 6 | [hashicorp/terraform](https://github.com/hashicorp/terraform)<br>クラウド資源をコードにして、レビューもバージョン管理も<br>`インフラ` | +399 | 13.3 | 50,118 | <a href="https://www.star-history.com/#hashicorp/terraform&Date"><img src="https://api.star-history.com/svg?repos=hashicorp/terraform&type=Date" width="260" alt="hashicorp/terraform のスター推移グラフ"></a> |
| 7 | [docker/compose](https://github.com/docker/compose)<br>複数のコンテナを 1 つのファイルでまとめて動かす<br>`インフラ` | +371 | 12.4 | 38,585 | <a href="https://www.star-history.com/#docker/compose&Date"><img src="https://api.star-history.com/svg?repos=docker/compose&type=Date" width="260" alt="docker/compose のスター推移グラフ"></a> |
| 8 | [pulumi/pulumi](https://github.com/pulumi/pulumi)<br>使い慣れた言語で、クラウド資源を管理<br>`インフラ` | +124 | 4.1 | 25,840 | <a href="https://www.star-history.com/#pulumi/pulumi&Date"><img src="https://api.star-history.com/svg?repos=pulumi/pulumi&type=Date" width="260" alt="pulumi/pulumi のスター推移グラフ"></a> |

### 今年もっとも伸びた（直近 365 日）

| # | プロジェクト | 増加数 | スター/日 | 総スター数 | スター推移 |
|---|---|---:|---:|---:|---|
| 1 | [caddyserver/caddy](https://github.com/caddyserver/caddy)<br>Web サーバー構築、HTTPS は自動で設定<br>`インフラ` | +11,877 | 32.5 | 78,663 | <a href="https://www.star-history.com/#caddyserver/caddy&Date"><img src="https://api.star-history.com/svg?repos=caddyserver/caddy&type=Date" width="260" alt="caddyserver/caddy のスター推移グラフ"></a> |
| 2 | [kubernetes/kubernetes](https://github.com/kubernetes/kubernetes)<br>コンテナが増えても、配備と拡張は任せる<br>`インフラ` | +11,583 | 31.7 | 128,619 | <a href="https://www.star-history.com/#kubernetes/kubernetes&Date"><img src="https://api.star-history.com/svg?repos=kubernetes/kubernetes&type=Date" width="260" alt="kubernetes/kubernetes のスター推移グラフ"></a> |
| 3 | [traefik/traefik](https://github.com/traefik/traefik)<br>サービスが増えても、通信は自動で振り分け<br>`インフラ` | +8,713 | 23.9 | 65,446 | <a href="https://www.star-history.com/#traefik/traefik&Date"><img src="https://api.star-history.com/svg?repos=traefik/traefik&type=Date" width="260" alt="traefik/traefik のスター推移グラフ"></a> |
| 4 | [grafana/grafana](https://github.com/grafana/grafana)<br>指標・ログ・トレースを 1 つのパネルに<br>`インフラ` | +7,869 | 21.6 | 77,645 | <a href="https://www.star-history.com/#grafana/grafana&Date"><img src="https://api.star-history.com/svg?repos=grafana/grafana&type=Date" width="260" alt="grafana/grafana のスター推移グラフ"></a> |
| 5 | [prometheus/prometheus](https://github.com/prometheus/prometheus)<br>システムの不具合は、アラートが先に知らせる<br>`インフラ` | +6,540 | 17.9 | 66,915 | <a href="https://www.star-history.com/#prometheus/prometheus&Date"><img src="https://api.star-history.com/svg?repos=prometheus/prometheus&type=Date" width="260" alt="prometheus/prometheus のスター推移グラフ"></a> |
| 6 | [hashicorp/terraform](https://github.com/hashicorp/terraform)<br>クラウド資源をコードにして、レビューもバージョン管理も<br>`インフラ` | +3,769 | 10.3 | 50,118 | <a href="https://www.star-history.com/#hashicorp/terraform&Date"><img src="https://api.star-history.com/svg?repos=hashicorp/terraform&type=Date" width="260" alt="hashicorp/terraform のスター推移グラフ"></a> |
| 7 | [docker/compose](https://github.com/docker/compose)<br>複数のコンテナを 1 つのファイルでまとめて動かす<br>`インフラ` | +2,619 | 7.2 | 38,585 | <a href="https://www.star-history.com/#docker/compose&Date"><img src="https://api.star-history.com/svg?repos=docker/compose&type=Date" width="260" alt="docker/compose のスター推移グラフ"></a> |
| 8 | [pulumi/pulumi](https://github.com/pulumi/pulumi)<br>使い慣れた言語で、クラウド資源を管理<br>`インフラ` | +2,081 | 5.7 | 25,840 | <a href="https://www.star-history.com/#pulumi/pulumi&Date"><img src="https://api.star-history.com/svg?repos=pulumi/pulumi&type=Date" width="260" alt="pulumi/pulumi のスター推移グラフ"></a> |

### 総スター数ランキング（累計）

| # | プロジェクト | 総スター数 | スター推移 |
|---|---|---:|---|
| 1 | [kubernetes/kubernetes](https://github.com/kubernetes/kubernetes)<br>コンテナが増えても、配備と拡張は任せる<br>`インフラ` | 128,619 | <a href="https://www.star-history.com/#kubernetes/kubernetes&Date"><img src="https://api.star-history.com/svg?repos=kubernetes/kubernetes&type=Date" width="260" alt="kubernetes/kubernetes のスター推移グラフ"></a> |
| 2 | [caddyserver/caddy](https://github.com/caddyserver/caddy)<br>Web サーバー構築、HTTPS は自動で設定<br>`インフラ` | 78,663 | <a href="https://www.star-history.com/#caddyserver/caddy&Date"><img src="https://api.star-history.com/svg?repos=caddyserver/caddy&type=Date" width="260" alt="caddyserver/caddy のスター推移グラフ"></a> |
| 3 | [grafana/grafana](https://github.com/grafana/grafana)<br>指標・ログ・トレースを 1 つのパネルに<br>`インフラ` | 77,645 | <a href="https://www.star-history.com/#grafana/grafana&Date"><img src="https://api.star-history.com/svg?repos=grafana/grafana&type=Date" width="260" alt="grafana/grafana のスター推移グラフ"></a> |
| 4 | [prometheus/prometheus](https://github.com/prometheus/prometheus)<br>システムの不具合は、アラートが先に知らせる<br>`インフラ` | 66,915 | <a href="https://www.star-history.com/#prometheus/prometheus&Date"><img src="https://api.star-history.com/svg?repos=prometheus/prometheus&type=Date" width="260" alt="prometheus/prometheus のスター推移グラフ"></a> |
| 5 | [traefik/traefik](https://github.com/traefik/traefik)<br>サービスが増えても、通信は自動で振り分け<br>`インフラ` | 65,446 | <a href="https://www.star-history.com/#traefik/traefik&Date"><img src="https://api.star-history.com/svg?repos=traefik/traefik&type=Date" width="260" alt="traefik/traefik のスター推移グラフ"></a> |
| 6 | [hashicorp/terraform](https://github.com/hashicorp/terraform)<br>クラウド資源をコードにして、レビューもバージョン管理も<br>`インフラ` | 50,118 | <a href="https://www.star-history.com/#hashicorp/terraform&Date"><img src="https://api.star-history.com/svg?repos=hashicorp/terraform&type=Date" width="260" alt="hashicorp/terraform のスター推移グラフ"></a> |
| 7 | [docker/compose](https://github.com/docker/compose)<br>複数のコンテナを 1 つのファイルでまとめて動かす<br>`インフラ` | 38,585 | <a href="https://www.star-history.com/#docker/compose&Date"><img src="https://api.star-history.com/svg?repos=docker/compose&type=Date" width="260" alt="docker/compose のスター推移グラフ"></a> |
| 8 | [pulumi/pulumi](https://github.com/pulumi/pulumi)<br>使い慣れた言語で、クラウド資源を管理<br>`インフラ` | 25,840 | <a href="https://www.star-history.com/#pulumi/pulumi&Date"><img src="https://api.star-history.com/svg?repos=pulumi/pulumi&type=Date" width="260" alt="pulumi/pulumi のスター推移グラフ"></a> |

## デザイン / クリエイティブ

> デザインシステム・描画・アニメーション・制作ツール

### 7 日以内の新着で最も熱いリポジトリ（作成から 7 日以内）

| # | プロジェクト | 作成日（UTC） | 総スター数 | スター/日 | スター推移 |
|---|---|---|---:|---:|---|
| 1 | [patch-gg/pixelfx](https://github.com/patch-gg/pixelfx)<br>ドット絵演出に悩んだら244本の短いコードを貼るだけ | 2026-10-30<br><sub>3.7 日</sub> | 3,469 | 939.8 | <a href="https://www.star-history.com/#patch-gg/pixelfx&Date"><img src="https://api.star-history.com/svg?repos=patch-gg/pixelfx&type=Date" width="260" alt="patch-gg/pixelfx のスター推移グラフ"></a> |
| 2 | [kevinraymond/florilegium](https://github.com/kevinraymond/florilegium)<br>余白が味気ない？デルフトブルーの花柄を自動で描く | 2026-10-30<br><sub>3.6 日</sub> | 1,363 | 373.9 | <a href="https://www.star-history.com/#kevinraymond/florilegium&Date"><img src="https://api.star-history.com/svg?repos=kevinraymond/florilegium&type=Date" width="260" alt="kevinraymond/florilegium のスター推移グラフ"></a> |
| 3 | [op7418/dsh-guizang-design](https://github.com/op7418/dsh-guizang-design)<br>AI臭さが抜けない？4つのスキルでデザインを整える | 2026-10-30<br><sub>3.4 日</sub> | 253 | 75.4 | <a href="https://www.star-history.com/#op7418/dsh-guizang-design&Date"><img src="https://api.star-history.com/svg?repos=op7418/dsh-guizang-design&type=Date" width="260" alt="op7418/dsh-guizang-design のスター推移グラフ"></a> |
| 4 | [artemnovitckii/claude-animation-skills](https://github.com/artemnovitckii/claude-animation-skills)<br>動画素材がない時に、Claude Codeスキルでアニメ制作 | 2026-11-01<br><sub>1.9 日</sub> | 129 | 69.7 | <a href="https://www.star-history.com/#artemnovitckii/claude-animation-skills&Date"><img src="https://api.star-history.com/svg?repos=artemnovitckii/claude-animation-skills&type=Date" width="260" alt="artemnovitckii/claude-animation-skills のスター推移グラフ"></a> |
| 5 | [GuoZheng-de-BaBa/nursing-research-skills](https://github.com/GuoZheng-de-BaBa/nursing-research-skills)<br>看護研究が進まない時に、AIスキルで設計から執筆まで支援 | 2026-10-30<br><sub>3.4 日</sub> | 170 | 50.3 | <a href="https://www.star-history.com/#GuoZheng-de-BaBa/nursing-research-skills&Date"><img src="https://api.star-history.com/svg?repos=GuoZheng-de-BaBa/nursing-research-skills&type=Date" width="260" alt="GuoZheng-de-BaBa/nursing-research-skills のスター推移グラフ"></a> |
| 6 | [Akillll-DuoHe/fy-code-animation](https://github.com/Akillll-DuoHe/fy-code-animation)<br>企画を動かせない？原稿と音声をコード動画に変える | 2026-10-30<br><sub>3.6 日</sub> | 134 | 37.7 | <a href="https://www.star-history.com/#Akillll-DuoHe/fy-code-animation&Date"><img src="https://api.star-history.com/svg?repos=Akillll-DuoHe/fy-code-animation&type=Date" width="260" alt="Akillll-DuoHe/fy-code-animation のスター推移グラフ"></a> |
| 7 | [enmerasoftware/ai-design-check](https://github.com/enmerasoftware/ai-design-check)<br>エージェントが作った画面、デザイン崩れを点検する | 2026-10-28<br><sub>5.7 日</sub> | 198 | 35.0 | <a href="https://www.star-history.com/#enmerasoftware/ai-design-check&Date"><img src="https://api.star-history.com/svg?repos=enmerasoftware/ai-design-check&type=Date" width="260" alt="enmerasoftware/ai-design-check のスター推移グラフ"></a> |
| 8 | [ersinkoc/AI-Video-Factory](https://github.com/ersinkoc/AI-Video-Factory)<br>ひとつの話題から、Claudeエージェントが動画を完成 | 2026-10-29<br><sub>4.0 日</sub> | 132 | 32.7 | <a href="https://www.star-history.com/#ersinkoc/AI-Video-Factory&Date"><img src="https://api.star-history.com/svg?repos=ersinkoc/AI-Video-Factory&type=Date" width="260" alt="ersinkoc/AI-Video-Factory のスター推移グラフ"></a> |
| 9 | [sirioberati/YouTube-AI-Motion-Graphics](https://github.com/sirioberati/YouTube-AI-Motion-Graphics)<br>解説動画の演出が大変？74種のボードを音声と同期 | 2026-10-27<br><sub>6.2 日</sub> | 134 | 21.5 | <a href="https://www.star-history.com/#sirioberati/YouTube-AI-Motion-Graphics&Date"><img src="https://api.star-history.com/svg?repos=sirioberati/YouTube-AI-Motion-Graphics&type=Date" width="260" alt="sirioberati/YouTube-AI-Motion-Graphics のスター推移グラフ"></a> |

### 今週もっとも伸びた（直近 7 日）

| # | プロジェクト | 増加数 | スター/日 | 総スター数 | スター推移 |
|---|---|---:|---:|---:|---|
| 1 | [excalidraw/excalidraw](https://github.com/excalidraw/excalidraw)<br>開いてすぐ描ける、紙に落書きする感覚で<br>`デザイン / クリエイティブ` | +492 | 70.3 | 135,054 | <a href="https://www.star-history.com/#excalidraw/excalidraw&Date"><img src="https://api.star-history.com/svg?repos=excalidraw/excalidraw&type=Date" width="260" alt="excalidraw/excalidraw のスター推移グラフ"></a> |
| 2 | [penpot/penpot](https://github.com/penpot/penpot)<br>チームで一緒にデザイン、オープンソースの基盤で<br>`デザイン / クリエイティブ` | +338 | 48.3 | 61,998 | <a href="https://www.star-history.com/#penpot/penpot&Date"><img src="https://api.star-history.com/svg?repos=penpot/penpot&type=Date" width="260" alt="penpot/penpot のスター推移グラフ"></a> |
| 3 | [lucide-icons/lucide](https://github.com/lucide-icons/lucide)<br>スタイルが揃ったアイコン一式、すぐ使える<br>`デザイン / クリエイティブ` | +167 | 23.9 | 25,474 | <a href="https://www.star-history.com/#lucide-icons/lucide&Date"><img src="https://api.star-history.com/svg?repos=lucide-icons/lucide&type=Date" width="260" alt="lucide-icons/lucide のスター推移グラフ"></a> |
| 4 | [jgraph/drawio](https://github.com/jgraph/drawio)<br>作図もホワイトボードも、1 つのエディタで<br>`デザイン / クリエイティブ` | +142 | 20.3 | 9,140 | <a href="https://www.star-history.com/#jgraph/drawio&Date"><img src="https://api.star-history.com/svg?repos=jgraph/drawio&type=Date" width="260" alt="jgraph/drawio のスター推移グラフ"></a> |
| 5 | [saadeghi/daisyui](https://github.com/saadeghi/daisyui)<br>Tailwind 用の部品が最初から揃っている<br>`デザイン / クリエイティブ` | +73 | 10.4 | 42,734 | <a href="https://www.star-history.com/#saadeghi/daisyui&Date"><img src="https://api.star-history.com/svg?repos=saadeghi/daisyui&type=Date" width="260" alt="saadeghi/daisyui のスター推移グラフ"></a> |
| 6 | [airbnb/lottie-web](https://github.com/airbnb/lottie-web)<br>After Effects のアニメを、そのまま Web に<br>`デザイン / クリエイティブ` | +64 | 9.1 | 32,332 | <a href="https://www.star-history.com/#airbnb/lottie-web&Date"><img src="https://api.star-history.com/svg?repos=airbnb/lottie-web&type=Date" width="260" alt="airbnb/lottie-web のスター推移グラフ"></a> |
| 7 | [phosphor-icons/homepage](https://github.com/phosphor-icons/homepage)<br>誰でも使える、柔軟なアイコンファミリー<br>`デザイン / クリエイティブ` | +38 | 5.4 | 7,755 | <a href="https://www.star-history.com/#phosphor-icons/homepage&Date"><img src="https://api.star-history.com/svg?repos=phosphor-icons/homepage&type=Date" width="260" alt="phosphor-icons/homepage のスター推移グラフ"></a> |
| 8 | [lottiefiles/lottie-ios](https://github.com/lottiefiles/lottie-ios)<br>After Effects のアニメを、そのまま iOS に<br>`デザイン / クリエイティブ` | +0 | 0.0 | 43 | <a href="https://www.star-history.com/#lottiefiles/lottie-ios&Date"><img src="https://api.star-history.com/svg?repos=lottiefiles/lottie-ios&type=Date" width="260" alt="lottiefiles/lottie-ios のスター推移グラフ"></a> |

### 今月もっとも伸びた（直近 30 日）

| # | プロジェクト | 増加数 | スター/日 | 総スター数 | スター推移 |
|---|---|---:|---:|---:|---|
| 1 | [excalidraw/excalidraw](https://github.com/excalidraw/excalidraw)<br>開いてすぐ描ける、紙に落書きする感覚で<br>`デザイン / クリエイティブ` | +1,981 | 66.0 | 135,054 | <a href="https://www.star-history.com/#excalidraw/excalidraw&Date"><img src="https://api.star-history.com/svg?repos=excalidraw/excalidraw&type=Date" width="260" alt="excalidraw/excalidraw のスター推移グラフ"></a> |
| 2 | [penpot/penpot](https://github.com/penpot/penpot)<br>チームで一緒にデザイン、オープンソースの基盤で<br>`デザイン / クリエイティブ` | +1,499 | 50.0 | 61,998 | <a href="https://www.star-history.com/#penpot/penpot&Date"><img src="https://api.star-history.com/svg?repos=penpot/penpot&type=Date" width="260" alt="penpot/penpot のスター推移グラフ"></a> |
| 3 | [lucide-icons/lucide](https://github.com/lucide-icons/lucide)<br>スタイルが揃ったアイコン一式、すぐ使える<br>`デザイン / クリエイティブ` | +682 | 22.7 | 25,474 | <a href="https://www.star-history.com/#lucide-icons/lucide&Date"><img src="https://api.star-history.com/svg?repos=lucide-icons/lucide&type=Date" width="260" alt="lucide-icons/lucide のスター推移グラフ"></a> |
| 4 | [jgraph/drawio](https://github.com/jgraph/drawio)<br>作図もホワイトボードも、1 つのエディタで<br>`デザイン / クリエイティブ` | +612 | 20.4 | 9,140 | <a href="https://www.star-history.com/#jgraph/drawio&Date"><img src="https://api.star-history.com/svg?repos=jgraph/drawio&type=Date" width="260" alt="jgraph/drawio のスター推移グラフ"></a> |
| 5 | [saadeghi/daisyui](https://github.com/saadeghi/daisyui)<br>Tailwind 用の部品が最初から揃っている<br>`デザイン / クリエイティブ` | +277 | 9.2 | 42,734 | <a href="https://www.star-history.com/#saadeghi/daisyui&Date"><img src="https://api.star-history.com/svg?repos=saadeghi/daisyui&type=Date" width="260" alt="saadeghi/daisyui のスター推移グラフ"></a> |
| 6 | [airbnb/lottie-web](https://github.com/airbnb/lottie-web)<br>After Effects のアニメを、そのまま Web に<br>`デザイン / クリエイティブ` | +223 | 7.4 | 32,332 | <a href="https://www.star-history.com/#airbnb/lottie-web&Date"><img src="https://api.star-history.com/svg?repos=airbnb/lottie-web&type=Date" width="260" alt="airbnb/lottie-web のスター推移グラフ"></a> |
| 7 | [phosphor-icons/homepage](https://github.com/phosphor-icons/homepage)<br>誰でも使える、柔軟なアイコンファミリー<br>`デザイン / クリエイティブ` | +181 | 6.0 | 7,755 | <a href="https://www.star-history.com/#phosphor-icons/homepage&Date"><img src="https://api.star-history.com/svg?repos=phosphor-icons/homepage&type=Date" width="260" alt="phosphor-icons/homepage のスター推移グラフ"></a> |
| 8 | [lottiefiles/lottie-ios](https://github.com/lottiefiles/lottie-ios)<br>After Effects のアニメを、そのまま iOS に<br>`デザイン / クリエイティブ` | +0 | 0.0 | 43 | <a href="https://www.star-history.com/#lottiefiles/lottie-ios&Date"><img src="https://api.star-history.com/svg?repos=lottiefiles/lottie-ios&type=Date" width="260" alt="lottiefiles/lottie-ios のスター推移グラフ"></a> |

### 今年もっとも伸びた（直近 365 日）

| # | プロジェクト | 増加数 | スター/日 | 総スター数 | スター推移 |
|---|---|---:|---:|---:|---|
| 1 | [excalidraw/excalidraw](https://github.com/excalidraw/excalidraw)<br>開いてすぐ描ける、紙に落書きする感覚で<br>`デザイン / クリエイティブ` | +27,021 | 74.0 | 135,054 | <a href="https://www.star-history.com/#excalidraw/excalidraw&Date"><img src="https://api.star-history.com/svg?repos=excalidraw/excalidraw&type=Date" width="260" alt="excalidraw/excalidraw のスター推移グラフ"></a> |
| 2 | [penpot/penpot](https://github.com/penpot/penpot)<br>チームで一緒にデザイン、オープンソースの基盤で<br>`デザイン / クリエイティブ` | +21,718 | 59.5 | 61,998 | <a href="https://www.star-history.com/#penpot/penpot&Date"><img src="https://api.star-history.com/svg?repos=penpot/penpot&type=Date" width="260" alt="penpot/penpot のスター推移グラフ"></a> |
| 3 | [jgraph/drawio](https://github.com/jgraph/drawio)<br>作図もホワイトボードも、1 つのエディタで<br>`デザイン / クリエイティブ` | +6,477 | 17.7 | 9,140 | <a href="https://www.star-history.com/#jgraph/drawio&Date"><img src="https://api.star-history.com/svg?repos=jgraph/drawio&type=Date" width="260" alt="jgraph/drawio のスター推移グラフ"></a> |
| 4 | [lucide-icons/lucide](https://github.com/lucide-icons/lucide)<br>スタイルが揃ったアイコン一式、すぐ使える<br>`デザイン / クリエイティブ` | +6,247 | 17.1 | 25,474 | <a href="https://www.star-history.com/#lucide-icons/lucide&Date"><img src="https://api.star-history.com/svg?repos=lucide-icons/lucide&type=Date" width="260" alt="lucide-icons/lucide のスター推移グラフ"></a> |
| 5 | [saadeghi/daisyui](https://github.com/saadeghi/daisyui)<br>Tailwind 用の部品が最初から揃っている<br>`デザイン / クリエイティブ` | +4,226 | 11.6 | 42,734 | <a href="https://www.star-history.com/#saadeghi/daisyui&Date"><img src="https://api.star-history.com/svg?repos=saadeghi/daisyui&type=Date" width="260" alt="saadeghi/daisyui のスター推移グラフ"></a> |
| 6 | [phosphor-icons/homepage](https://github.com/phosphor-icons/homepage)<br>誰でも使える、柔軟なアイコンファミリー<br>`デザイン / クリエイティブ` | +2,195 | 6.0 | 7,755 | <a href="https://www.star-history.com/#phosphor-icons/homepage&Date"><img src="https://api.star-history.com/svg?repos=phosphor-icons/homepage&type=Date" width="260" alt="phosphor-icons/homepage のスター推移グラフ"></a> |
| 7 | [airbnb/lottie-web](https://github.com/airbnb/lottie-web)<br>After Effects のアニメを、そのまま Web に<br>`デザイン / クリエイティブ` | +1,091 | 3.0 | 32,332 | <a href="https://www.star-history.com/#airbnb/lottie-web&Date"><img src="https://api.star-history.com/svg?repos=airbnb/lottie-web&type=Date" width="260" alt="airbnb/lottie-web のスター推移グラフ"></a> |
| 8 | [lottiefiles/lottie-ios](https://github.com/lottiefiles/lottie-ios)<br>After Effects のアニメを、そのまま iOS に<br>`デザイン / クリエイティブ` | +1 | 0.0 | 43 | <a href="https://www.star-history.com/#lottiefiles/lottie-ios&Date"><img src="https://api.star-history.com/svg?repos=lottiefiles/lottie-ios&type=Date" width="260" alt="lottiefiles/lottie-ios のスター推移グラフ"></a> |

### 総スター数ランキング（累計）

| # | プロジェクト | 総スター数 | スター推移 |
|---|---|---:|---|
| 1 | [excalidraw/excalidraw](https://github.com/excalidraw/excalidraw)<br>開いてすぐ描ける、紙に落書きする感覚で<br>`デザイン / クリエイティブ` | 135,054 | <a href="https://www.star-history.com/#excalidraw/excalidraw&Date"><img src="https://api.star-history.com/svg?repos=excalidraw/excalidraw&type=Date" width="260" alt="excalidraw/excalidraw のスター推移グラフ"></a> |
| 2 | [penpot/penpot](https://github.com/penpot/penpot)<br>チームで一緒にデザイン、オープンソースの基盤で<br>`デザイン / クリエイティブ` | 61,998 | <a href="https://www.star-history.com/#penpot/penpot&Date"><img src="https://api.star-history.com/svg?repos=penpot/penpot&type=Date" width="260" alt="penpot/penpot のスター推移グラフ"></a> |
| 3 | [saadeghi/daisyui](https://github.com/saadeghi/daisyui)<br>Tailwind 用の部品が最初から揃っている<br>`デザイン / クリエイティブ` | 42,734 | <a href="https://www.star-history.com/#saadeghi/daisyui&Date"><img src="https://api.star-history.com/svg?repos=saadeghi/daisyui&type=Date" width="260" alt="saadeghi/daisyui のスター推移グラフ"></a> |
| 4 | [airbnb/lottie-web](https://github.com/airbnb/lottie-web)<br>After Effects のアニメを、そのまま Web に<br>`デザイン / クリエイティブ` | 32,332 | <a href="https://www.star-history.com/#airbnb/lottie-web&Date"><img src="https://api.star-history.com/svg?repos=airbnb/lottie-web&type=Date" width="260" alt="airbnb/lottie-web のスター推移グラフ"></a> |
| 5 | [lucide-icons/lucide](https://github.com/lucide-icons/lucide)<br>スタイルが揃ったアイコン一式、すぐ使える<br>`デザイン / クリエイティブ` | 25,474 | <a href="https://www.star-history.com/#lucide-icons/lucide&Date"><img src="https://api.star-history.com/svg?repos=lucide-icons/lucide&type=Date" width="260" alt="lucide-icons/lucide のスター推移グラフ"></a> |
| 6 | [jgraph/drawio](https://github.com/jgraph/drawio)<br>作図もホワイトボードも、1 つのエディタで<br>`デザイン / クリエイティブ` | 9,140 | <a href="https://www.star-history.com/#jgraph/drawio&Date"><img src="https://api.star-history.com/svg?repos=jgraph/drawio&type=Date" width="260" alt="jgraph/drawio のスター推移グラフ"></a> |
| 7 | [phosphor-icons/homepage](https://github.com/phosphor-icons/homepage)<br>誰でも使える、柔軟なアイコンファミリー<br>`デザイン / クリエイティブ` | 7,755 | <a href="https://www.star-history.com/#phosphor-icons/homepage&Date"><img src="https://api.star-history.com/svg?repos=phosphor-icons/homepage&type=Date" width="260" alt="phosphor-icons/homepage のスター推移グラフ"></a> |
| 8 | [lottiefiles/lottie-ios](https://github.com/lottiefiles/lottie-ios)<br>After Effects のアニメを、そのまま iOS に<br>`デザイン / クリエイティブ` | 43 | <a href="https://www.star-history.com/#lottiefiles/lottie-ios&Date"><img src="https://api.star-history.com/svg?repos=lottiefiles/lottie-ios&type=Date" width="260" alt="lottiefiles/lottie-ios のスター推移グラフ"></a> |

## データ

> データベース・分析・ETL・データエンジニアリング

### 7 日以内の新着で最も熱いリポジトリ（作成から 7 日以内）

今回の実行で条件を満たす新着リポジトリはありませんでした。

### 今週もっとも伸びた（直近 7 日）

| # | プロジェクト | 増加数 | スター/日 | 総スター数 | スター推移 |
|---|---|---:|---:|---:|---|
| 1 | [duckdb/duckdb](https://github.com/duckdb/duckdb)<br>データベースサーバーなしで、SQL 分析ができる<br>`データ` | +209 | 29.9 | 42,754 | <a href="https://www.star-history.com/#duckdb/duckdb&Date"><img src="https://api.star-history.com/svg?repos=duckdb/duckdb&type=Date" width="260" alt="duckdb/duckdb のスター推移グラフ"></a> |
| 2 | [ClickHouse/ClickHouse](https://github.com/ClickHouse/ClickHouse)<br>大量データのリアルタイム分析をオープンソースで<br>`データ` | +127 | 18.1 | 50,721 | <a href="https://www.star-history.com/#ClickHouse/ClickHouse&Date"><img src="https://api.star-history.com/svg?repos=ClickHouse/ClickHouse&type=Date" width="260" alt="ClickHouse/ClickHouse のスター推移グラフ"></a> |
| 3 | [apache/superset](https://github.com/apache/superset)<br>データは、グラフにすれば見えてくる<br>`データ` | +105 | 15.0 | 75,392 | <a href="https://www.star-history.com/#apache/superset&Date"><img src="https://api.star-history.com/svg?repos=apache/superset&type=Date" width="260" alt="apache/superset のスター推移グラフ"></a> |
| 4 | [pola-rs/polars](https://github.com/pola-rs/polars)<br>表データの処理が速く、待たされない<br>`データ` | +65 | 9.3 | 40,254 | <a href="https://www.star-history.com/#pola-rs/polars&Date"><img src="https://api.star-history.com/svg?repos=pola-rs/polars&type=Date" width="260" alt="pola-rs/polars のスター推移グラフ"></a> |
| 5 | [apache/kafka](https://github.com/apache/kafka)<br>システム間のイベントの流れを、分散基盤で運ぶ<br>`データ` | +65 | 9.3 | 34,118 | <a href="https://www.star-history.com/#apache/kafka&Date"><img src="https://api.star-history.com/svg?repos=apache/kafka&type=Date" width="260" alt="apache/kafka のスター推移グラフ"></a> |
| 6 | [apache/arrow](https://github.com/apache/arrow)<br>言語が違っても、データはそのまま通じる<br>`データ` | +49 | 7.0 | 17,272 | <a href="https://www.star-history.com/#apache/arrow&Date"><img src="https://api.star-history.com/svg?repos=apache/arrow&type=Date" width="260" alt="apache/arrow のスター推移グラフ"></a> |
| 7 | [dbt-labs/dbt-core](https://github.com/dbt-labs/dbt-core)<br>データ変換を、ソフトウェア開発のやり方で<br>`データ` | +31 | 4.4 | 14,112 | <a href="https://www.star-history.com/#dbt-labs/dbt-core&Date"><img src="https://api.star-history.com/svg?repos=dbt-labs/dbt-core&type=Date" width="260" alt="dbt-labs/dbt-core のスター推移グラフ"></a> |
| 8 | [jupyter/notebook](https://github.com/jupyter/notebook)<br>ブラウザでコードを書き、結果をその場で確認<br>`データ` | +5 | 0.7 | 13,459 | <a href="https://www.star-history.com/#jupyter/notebook&Date"><img src="https://api.star-history.com/svg?repos=jupyter/notebook&type=Date" width="260" alt="jupyter/notebook のスター推移グラフ"></a> |

### 今月もっとも伸びた（直近 30 日）

| # | プロジェクト | 増加数 | スター/日 | 総スター数 | スター推移 |
|---|---|---:|---:|---:|---|
| 1 | [duckdb/duckdb](https://github.com/duckdb/duckdb)<br>データベースサーバーなしで、SQL 分析ができる<br>`データ` | +928 | 30.9 | 42,754 | <a href="https://www.star-history.com/#duckdb/duckdb&Date"><img src="https://api.star-history.com/svg?repos=duckdb/duckdb&type=Date" width="260" alt="duckdb/duckdb のスター推移グラフ"></a> |
| 2 | [ClickHouse/ClickHouse](https://github.com/ClickHouse/ClickHouse)<br>大量データのリアルタイム分析をオープンソースで<br>`データ` | +589 | 19.6 | 50,721 | <a href="https://www.star-history.com/#ClickHouse/ClickHouse&Date"><img src="https://api.star-history.com/svg?repos=ClickHouse/ClickHouse&type=Date" width="260" alt="ClickHouse/ClickHouse のスター推移グラフ"></a> |
| 3 | [apache/superset](https://github.com/apache/superset)<br>データは、グラフにすれば見えてくる<br>`データ` | +464 | 15.5 | 75,392 | <a href="https://www.star-history.com/#apache/superset&Date"><img src="https://api.star-history.com/svg?repos=apache/superset&type=Date" width="260" alt="apache/superset のスター推移グラフ"></a> |
| 4 | [pola-rs/polars](https://github.com/pola-rs/polars)<br>表データの処理が速く、待たされない<br>`データ` | +383 | 12.8 | 40,254 | <a href="https://www.star-history.com/#pola-rs/polars&Date"><img src="https://api.star-history.com/svg?repos=pola-rs/polars&type=Date" width="260" alt="pola-rs/polars のスター推移グラフ"></a> |
| 5 | [apache/kafka](https://github.com/apache/kafka)<br>システム間のイベントの流れを、分散基盤で運ぶ<br>`データ` | +293 | 9.8 | 34,118 | <a href="https://www.star-history.com/#apache/kafka&Date"><img src="https://api.star-history.com/svg?repos=apache/kafka&type=Date" width="260" alt="apache/kafka のスター推移グラフ"></a> |
| 6 | [dbt-labs/dbt-core](https://github.com/dbt-labs/dbt-core)<br>データ変換を、ソフトウェア開発のやり方で<br>`データ` | +169 | 5.6 | 14,112 | <a href="https://www.star-history.com/#dbt-labs/dbt-core&Date"><img src="https://api.star-history.com/svg?repos=dbt-labs/dbt-core&type=Date" width="260" alt="dbt-labs/dbt-core のスター推移グラフ"></a> |
| 7 | [apache/arrow](https://github.com/apache/arrow)<br>言語が違っても、データはそのまま通じる<br>`データ` | +122 | 4.1 | 17,272 | <a href="https://www.star-history.com/#apache/arrow&Date"><img src="https://api.star-history.com/svg?repos=apache/arrow&type=Date" width="260" alt="apache/arrow のスター推移グラフ"></a> |
| 8 | [jupyter/notebook](https://github.com/jupyter/notebook)<br>ブラウザでコードを書き、結果をその場で確認<br>`データ` | +71 | 2.4 | 13,459 | <a href="https://www.star-history.com/#jupyter/notebook&Date"><img src="https://api.star-history.com/svg?repos=jupyter/notebook&type=Date" width="260" alt="jupyter/notebook のスター推移グラフ"></a> |

### 今年もっとも伸びた（直近 365 日）

| # | プロジェクト | 増加数 | スター/日 | 総スター数 | スター推移 |
|---|---|---:|---:|---:|---|
| 1 | [duckdb/duckdb](https://github.com/duckdb/duckdb)<br>データベースサーバーなしで、SQL 分析ができる<br>`データ` | +9,360 | 25.6 | 42,754 | <a href="https://www.star-history.com/#duckdb/duckdb&Date"><img src="https://api.star-history.com/svg?repos=duckdb/duckdb&type=Date" width="260" alt="duckdb/duckdb のスター推移グラフ"></a> |
| 2 | [ClickHouse/ClickHouse](https://github.com/ClickHouse/ClickHouse)<br>大量データのリアルタイム分析をオープンソースで<br>`データ` | +7,629 | 20.9 | 50,721 | <a href="https://www.star-history.com/#ClickHouse/ClickHouse&Date"><img src="https://api.star-history.com/svg?repos=ClickHouse/ClickHouse&type=Date" width="260" alt="ClickHouse/ClickHouse のスター推移グラフ"></a> |
| 3 | [apache/superset](https://github.com/apache/superset)<br>データは、グラフにすれば見えてくる<br>`データ` | +7,448 | 20.4 | 75,392 | <a href="https://www.star-history.com/#apache/superset&Date"><img src="https://api.star-history.com/svg?repos=apache/superset&type=Date" width="260" alt="apache/superset のスター推移グラフ"></a> |
| 4 | [pola-rs/polars](https://github.com/pola-rs/polars)<br>表データの処理が速く、待たされない<br>`データ` | +4,852 | 13.3 | 40,254 | <a href="https://www.star-history.com/#pola-rs/polars&Date"><img src="https://api.star-history.com/svg?repos=pola-rs/polars&type=Date" width="260" alt="pola-rs/polars のスター推移グラフ"></a> |
| 5 | [apache/kafka](https://github.com/apache/kafka)<br>システム間のイベントの流れを、分散基盤で運ぶ<br>`データ` | +3,295 | 9.0 | 34,118 | <a href="https://www.star-history.com/#apache/kafka&Date"><img src="https://api.star-history.com/svg?repos=apache/kafka&type=Date" width="260" alt="apache/kafka のスター推移グラフ"></a> |
| 6 | [dbt-labs/dbt-core](https://github.com/dbt-labs/dbt-core)<br>データ変換を、ソフトウェア開発のやり方で<br>`データ` | +2,465 | 6.8 | 14,112 | <a href="https://www.star-history.com/#dbt-labs/dbt-core&Date"><img src="https://api.star-history.com/svg?repos=dbt-labs/dbt-core&type=Date" width="260" alt="dbt-labs/dbt-core のスター推移グラフ"></a> |
| 7 | [apache/arrow](https://github.com/apache/arrow)<br>言語が違っても、データはそのまま通じる<br>`データ` | +1,316 | 3.6 | 17,272 | <a href="https://www.star-history.com/#apache/arrow&Date"><img src="https://api.star-history.com/svg?repos=apache/arrow&type=Date" width="260" alt="apache/arrow のスター推移グラフ"></a> |
| 8 | [jupyter/notebook](https://github.com/jupyter/notebook)<br>ブラウザでコードを書き、結果をその場で確認<br>`データ` | +907 | 2.5 | 13,459 | <a href="https://www.star-history.com/#jupyter/notebook&Date"><img src="https://api.star-history.com/svg?repos=jupyter/notebook&type=Date" width="260" alt="jupyter/notebook のスター推移グラフ"></a> |

### 総スター数ランキング（累計）

| # | プロジェクト | 総スター数 | スター推移 |
|---|---|---:|---|
| 1 | [apache/superset](https://github.com/apache/superset)<br>データは、グラフにすれば見えてくる<br>`データ` | 75,392 | <a href="https://www.star-history.com/#apache/superset&Date"><img src="https://api.star-history.com/svg?repos=apache/superset&type=Date" width="260" alt="apache/superset のスター推移グラフ"></a> |
| 2 | [ClickHouse/ClickHouse](https://github.com/ClickHouse/ClickHouse)<br>大量データのリアルタイム分析をオープンソースで<br>`データ` | 50,721 | <a href="https://www.star-history.com/#ClickHouse/ClickHouse&Date"><img src="https://api.star-history.com/svg?repos=ClickHouse/ClickHouse&type=Date" width="260" alt="ClickHouse/ClickHouse のスター推移グラフ"></a> |
| 3 | [duckdb/duckdb](https://github.com/duckdb/duckdb)<br>データベースサーバーなしで、SQL 分析ができる<br>`データ` | 42,754 | <a href="https://www.star-history.com/#duckdb/duckdb&Date"><img src="https://api.star-history.com/svg?repos=duckdb/duckdb&type=Date" width="260" alt="duckdb/duckdb のスター推移グラフ"></a> |
| 4 | [pola-rs/polars](https://github.com/pola-rs/polars)<br>表データの処理が速く、待たされない<br>`データ` | 40,254 | <a href="https://www.star-history.com/#pola-rs/polars&Date"><img src="https://api.star-history.com/svg?repos=pola-rs/polars&type=Date" width="260" alt="pola-rs/polars のスター推移グラフ"></a> |
| 5 | [apache/kafka](https://github.com/apache/kafka)<br>システム間のイベントの流れを、分散基盤で運ぶ<br>`データ` | 34,118 | <a href="https://www.star-history.com/#apache/kafka&Date"><img src="https://api.star-history.com/svg?repos=apache/kafka&type=Date" width="260" alt="apache/kafka のスター推移グラフ"></a> |
| 6 | [apache/arrow](https://github.com/apache/arrow)<br>言語が違っても、データはそのまま通じる<br>`データ` | 17,272 | <a href="https://www.star-history.com/#apache/arrow&Date"><img src="https://api.star-history.com/svg?repos=apache/arrow&type=Date" width="260" alt="apache/arrow のスター推移グラフ"></a> |
| 7 | [dbt-labs/dbt-core](https://github.com/dbt-labs/dbt-core)<br>データ変換を、ソフトウェア開発のやり方で<br>`データ` | 14,112 | <a href="https://www.star-history.com/#dbt-labs/dbt-core&Date"><img src="https://api.star-history.com/svg?repos=dbt-labs/dbt-core&type=Date" width="260" alt="dbt-labs/dbt-core のスター推移グラフ"></a> |
| 8 | [jupyter/notebook](https://github.com/jupyter/notebook)<br>ブラウザでコードを書き、結果をその場で確認<br>`データ` | 13,459 | <a href="https://www.star-history.com/#jupyter/notebook&Date"><img src="https://api.star-history.com/svg?repos=jupyter/notebook&type=Date" width="260" alt="jupyter/notebook のスター推移グラフ"></a> |

---

役に立ったら、ほかの人にも見つけてもらえるようリポジトリにスターを付けてください。

引用の仕方：[CITATION.cff](CITATION.cff) を見てください。

数字の出し方と参加方法：[docs/HOW_IT_WORKS.ja.md](docs/HOW_IT_WORKS.ja.md)。新規リポジトリのルール：[docs/NEW_ARRIVALS.md](docs/NEW_ARRIVALS.md)。カテゴリ：[docs/CATEGORIES.md](docs/CATEGORIES.md)。プルリクエスト：[CONTRIBUTING.md](CONTRIBUTING.md)。
