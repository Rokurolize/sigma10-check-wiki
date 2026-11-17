# Sigma-10 テーマキャンペーン 統合完了報告書

作成日: 2026-11-16 / 草案: lane-oc-final-draft / 最終化: コーディネーター（2026-11-16、最終確認ラウンドの裁定と最終検証結果を反映）

本書は、Sigma-10 テーマキャンペーンの記録（レコードディレクトリ `theme-port-readiness-20261114/`）に基づく統合完了報告書である。数値はすべて記録から転記したものであり、記録にない数値は創作していない。

## 1. Stage 1 ゴーサイン

出典: `GOSIGN.md`、`REPORT-GOSIGN.md`

- テーマ行: **44**（READY 19 / NOT READY 25）。各行は判定状態・理由（保存済みフル基準スイープ `grades_final3.json` 由来）・記録された参照リビジョン・diff ページ（あれば）を記す。READY は保存済み基準状態であり、Check 5 は別途掃引されていないため、READY 行は CRITERIA.md の Check 5 注記の下で暫定的である。
- 既存ページ: **153**（一致 139 / 不一致 14）。うち 4 行（blankstyle・placestyle・af2026・ny21）は `grades_existing_p23.json`（ビルド `f7e6cd103`）由来、残り 149 行は `grades_existing_p13.json` 由来。
- 検証結果（`REPORT-GOSIGN.md` §4、及びコーディネーター確認 2026-11-15 ~22:49 JST 追記分として引用）:

  `verify.py`: exited **0**: `OK: 317 pages match on both wikis`（当時の 315 ページ + 新規 diff ページ 2 件。コーディネーターが canonical `ab71620` に対して ~22:44 JST に再実行し、exit 0 を確認）

- 個別列挙された例外（issue 番号付き）:
  - リテラルマークアップ **#3738**: `theme:nebulae`、`theme:monotypical`、`theme:darkcode`、`theme:ijamea-bhl`（いずれも不一致・`PENDING-REMEASURE.md` の literal-markup 行で保留中）、`theme:cyberpunk`（既存ページ側は一致だが #3738 再測定は未了）。
  - 構造: `old:theme:basalt`（collapsibles 3 vs 4; tabs 2 vs 3）、`theme:shushuin`（tabs 1 vs 2）。
  - カスケード: `component:af2024theme`、`theme:foxtrot`、`theme:neo-linkage`、`theme:teito-keizai`、`component:ny21`（一致だがカスケードの style 部は保留中）。
  - Info モジュール **#3722**（SCP-JP/sigma 側）: **open**。既存ページの判定行ではなく 153 件には含まれない。後段の Wikijump フェーズ向けのプラットフォーム側項目。
- スコープ境界（重要）: 証明の単位は **153 のテーマタグ付き既存ページ + 44 の候補行** に限られる。テーマを単に使用しているだけの一般記事は、このキャンペーンでは列挙も採点もされていない。
- 補足（`REPORT-GOSIGN.md` のコーディネーター追記より）: §2 の要約文は cyberpunk を #3738 リテラルマークアップのページに列挙しているが、cyberpunk は現在の 14 ページ不一致セットには含まれない（#3738 issue のページセットと現在の不一致セットは異なる）。GOSIGN.md のページ毎データは正しい。
- 備考: Theme rows READY の暫定性（Check 5 未掃引）、Min Theme・Shushuin は JP オリジナル（参照 rev なし）、Generic Space 28→32・Turbo Vision 53→54 は no-follow（bulk-only：画像 URL / フォント配信元のみ）として処理済み（`REPORT-GOSIGN.md` §1・§3、commit `ab71620`）。
- **コーディネーター裁定（2026-11-16、最終確認ラウンド）**: 保存済みスイープの「19 READY / 25 NOT READY」は、そのままではゴーサインの根拠にならない。理由は2つある。(1) NOT READY の理由のうち「移植候補がない」とされた8件（BLANKSTYLE、Flopstyle、Halloween、Just Girly Things、Min Theme、SCP Human Resources、Shushuin、Simple Yonder）は、正本リポジトリに候補ファイル（`theme:<slug>-jp.txt`）が全件実在し、理由として誤りである（最終確認ラウンドで全件を実物確認）。(2) 残りの Check 3 不合格理由（折りたたみの差・タブの差・raw wikitext leak・画像の差）は、プラットフォーム側の描画欠陥を修正する前の測定であり、その種類はいずれも `PENDING-REMEASURE.md` に issue 番号つきで記録されたクラスである。うち Basalt と Flopstyle DARK は、修正を載せたビルドでの再測定で一致が確認され閉じている。Check 5 の暫定性については、2026-11-15 の相互作用スイープで根本原因（サンプル側の hovertip 展示の誤用）が特定され Phase 20 でサンプルを修正済みであり、影響クラスは解消している。したがって本報告書のゴーサインは、オーナーが定めた物差し（Wikidot 側の材料がそろい、Wikijump 側の描画の差が記録されていれば、その行の Wikidot 側作業は完了）に基づいて出す。保存済みスイープの数字と上記の食い違いは、隠さずここに明記する。再測定待ちの項目は Wikijump フェーズ（現在凍結中）が PENDING-REMEASURE を消費する時点で再判定される。**訂正（2026-11-16 18:1x）**: この裁定は /start の完了像の範囲では正しいが、ゴーサインの根拠にはならない。ゴーサインの条件はスタッフ査読スキルによる全テーマの点検であり、本裁定をもってゴーサインを出した §9 初版は取り下げた（§9 参照）。

## 2. Stage 2 本番制作と統合

出典: `stage2-lanes/LEDGER.json`、`REPORT-INT-*.md` セット（EN1–EN3 は `REPORT-S2E1.md` 経由）、`REPORT-INT-CN1.md`

- バッチ数: **50**（EN 24 / CN 18 / KO 8）。対象テーマ数: **243**（EN 117 / CN 87 / KO 39、AUDIT-INLINE.md の列挙による）。LEDGER.json の全バッチの status は `integrated` であり、統合は **50/50** 完了している。
- 個別レポートは `REPORT-INT-<BATCH>.md` が 47 件存在し、EN1–EN3（Stage 2 最初のバッチ）は `REPORT-S2E1.md` で本セッションが本番制作・統合を行い、2026-11-16 に status が `integrated` に整合された旨が LEDGER.json に記録されている。
- 各統合は PLAYBOOK 形式（canonical コピー → /start スプライス → 単一 canonical コミット → 両チェック wiki への reflection → スコープ付き検証 `verify_scoped.py` → レポート）で実行され、検証は原則スコープ付きチェックのみで行われた（full `verify.py` はバッチ内では禁止 — §5 参照）。
- **amethyst-v2 例外とその処置**（`REPORT-INT-CN1.md`、`stage2-lanes/LEDGER.json` CN1 行）: CN1 バッチ（canonical commit `4a2f4a5`、12 ページ追加、`SCOPED-OK: 13 pages match on both wikis`）では、`amethyst-v2` は **g2lighter コンポーネントファミリーのテーマであり、単独の候補ページを作成できない**ため本番制作がブロックされた（lane の証拠は `lane-dsh-cn1/MANIFEST.md` に記録）。他の 4 テーマ（andesite・another-night・ared・asagao）は完成・統合済みで、CN1 の統合自体は完了として記録されている。なお最終確認ラウンド（§8）で、amethyst-v2 が /start に一切記載されていないことが判明したため、候補を作れなかった理由を明記した行を /start に追加した（commit `d1877e4`）。
- 備考: CN2・CN8・CN9・CN12 の各バッチは、oversize 再作業（§3）によって 2026-11-16 にクローズされた旨が LEDGER.json に記録されている。

## 3. oversize 根本原因と再作業

出典: `REPORT-REWORK-OVERSIZE.md`（関連: `REPORT-INT-CN2.md`、`REPORT-INT-CN8.md`、`REPORT-INT-CN12.md`、`FIX-BLOCKED-4-PROMPT.md`）

- **根本原因**: Stage 2 の 4 つの候補が Wikidot の 200,000 文字ページソース上限を超過したのは、**base material（Parallel フレームワーク等の基盤）が候補ページ自身にインライン展開されていたため**である。具体的には:
  - `theme:betwixt-jp` 251,093 文字（normalize-parallel-min.css 全体 + parallel-min.css 残余 ~194,050 文字 + normalize v8.0.1 prefix のインライン）
  - `theme:kitchen-jp` 240,392 文字（`#normalize` div + `#parallel` div に base を verbatim インライン）
  - `theme:peroxide-jp` 233,113 文字（peroxide.css 全体 218,493 文字を 5 セクションにわたり `[[code type="css"]]` にインライン）
  - `theme:magazine-jp` 206,282 文字（collapsible-sidebar コンポーネントの外部 CSS のバイト同一コピー ~20,550 バイトをインライン）
- **以前の lock/captcha 診断は誤りだった**: 保存失敗は `TargetErrorException: Page theme:kitchen-jp is locked or other locks exist`、`"AMC is respond error status: 'error'"`、`need_captcha` 仮説として報告されていたが、実際は Wikidot が over-limit ソースに対して `status: "error"` を返すことが 200,000 文字超過という同一原因を別のツール層から見たものであり、**captcha は無関係**（`SAVE-BODY ... ページソースが長すぎます(最大200000文字)`）。観測されたロックは自ツール用アカウントが probe で作成したロック（自己失効するもの）であり、他ウィキへの投稿経路のブロックではなかった。
- **再作業の方針**: 原本（オリジナル）のファイル分離をミラーした。base は候補ページの外（`theme:parallel-jp` の include、`fragment:peroxide-jp-base-css` / `fragment:peroxide-jp-elements-css`、collapsible-sidebar の外部 `@import`）へ移し、候補ページは自身の CSS のみを持つ構成とした。`theme:parallel-jp` は include ターゲットとして機能させるため、2 行の `@import` をコードバンドルの先頭へ移動した（25,045 → 25,046 文字の支持編集）。
- **最終サイズ**（`REPORT-REWORK-OVERSIZE.md`）:

  | theme | before | after | Δ |
  |---|---|---|---|
  | `theme:betwixt-jp` | 251,093 | 48,034 | −203,059 (−80.9%) |
  | `theme:kitchen-jp` | 240,392 | 37,463 | −202,929 (−84.4%) |
  | `theme:peroxide-jp` | 233,113 | 14,903 | −218,210 (−93.6%) |
  | `theme:magazine-jp` | 206,282 | 185,842 | −20,440 (−9.9%) |
  | `theme:parallel-jp`（支持編集） | 25,045 | 25,046 | +1 |

- **スコープ付き検証（verbatim）**: `SCOPED-OK: 8 pages match on both wikis`（`theme:parallel-jp theme:betwixt-jp theme:kitchen-jp fragment:peroxide-jp-base-css fragment:peroxide-jp-elements-css theme:peroxide-jp theme:magazine-jp start` に対して）。4 つの候補ページとも保存済み・anon-visible・両 wiki で HTTP 200。headless Chromium によるレンダー確認でも 8/8 が include-error マーカーなし、期待どおりの CSS リクエストが発火することを確認済み。
- この再作業は 2026-11-16 に実施され、commit `3000981`（betwixt）→ `7cbe280`（parallel-jp）→ `eb1e7ae`（kitchen）→ `ff96155`（peroxide, +fragment pages）→ `c839ec3`（magazine）の順で canonical にコミットされ、両チェック wiki に投入された。

## 4. インライン監査と REWORK2

出典: `AUDIT-INLINE.md`、`REPORT-REWORK2-P1.md` 〜 `REPORT-REWORK2-P5.md`、`REPORT-REWORK2-INT.md`

### 4.1 監査（`AUDIT-INLINE.md`、2026-11-16）

- 監査対象: **243 ペア**（EN 117 / CN 87 / KO 39。`stage2-lanes/LEDGER.json` 列挙 + lane manifest・canonical repo と突合）。オリジナルは branch wiki から 1 度ずつ fetch（EN → scp-wiki.wikidot.com、CN → scp-wiki-cn.wikidot.com、KO → **scpko.wikidot.com**（brief 記載の `scp-wiki-ko.wikidot.com` は存在せず））。fetch 結果: **243/243 OK、0 失敗**。
- 分類（ペア毎にちょうど 1 つ）:

  | 分類 | 件数 | EN | CN | KO |
  |---|---|---|---|---|
  | FAITHFUL | **186** | 108 | 51 | 27 |
  | SELF-CONTAINED | **11** | 2 | 5 | 4 |
  | INLINED-FITS | **35** | 5 | 24 | 6 |
  | INLINED-BLOCKING | **0** | — | — | — |
  | UNRESOLVED | **11** | 2 | 7 | 2 |

- UNRESOLVED の内訳は、**amethyst-v2**（候補ページ自体が非存在、§2）と、**10 件の drop**（base の届け物が候補に一切存在しないもの: `5k-jp`、`admo-jp`、`paradigm-inapplicable-sigma-jp`、`waxed-oxidized-cut-copper-slab-jp`、`foundom-jp`、`tfnac-jp`、`food-jp`、`voyager-jp`、`bulgunae-jp`、`garak-the-magazine-jp`）。インラインは 0 件ではないが、上限超過は 1 件もなかった（最大は `dustframe-jp` 194,747 文字、INLINED-FITS）。
- なお、監査は以前 oversize だった 4 ペアが再作業後にすべて FAITHFUL と分類されることを検証した（§3 の効果確認）。
- INLINED-FITS 35 件のうち、大型 third-party base の直埋めは P4/P5 で処理され、小規模なもの・既存形式に一致するものは個別に措置された（以下）。

### 4.2 REWORK2 各パケットの結果（`REPORT-REWORK2-P1..P5.md`）

- **P1 — DROP 9 ペアの base 届け物を復元**（`REPORT-REWORK2-P1.md`）: 9 候補へ不足している base deliveries を復元（`5k-jp`→basalt-jp、`admo-jp`→EN-CDN @import、`paradigm-inapplicable-sigma-jp`→dustframe-jp、`waxed-oxidized-cut-copper-slab-jp`・`foundom-jp`→parallel-jp、`food-jp`・`voyager-jp`・`bulgunae-jp`・`garak-the-magazine-jp`→`:scp-jp:` コンポーネント / `:scp-jp:nav:side` 等）。garak-the-magazine-jp 用に新規受け皿 `fragment:u-navstyle-jp-base-css` を作成（KO コンポーネント rev 4 の CSS を verbatim 収録）。件数: 225,042 → 226,339 文字（+1,297）。
- **P2 — INLINED 9 ペアを参照方式へ交換**（`REPORT-REWORK2-P2.md`）: `creature-jp`、`doap-nvl-jp`、`navla-style-jp`、`dia-de-muertos-jp`、`vanguard-supplement-jp`、`words-of-wisdom-jp`、`anon-jp`、`pacom1943-jp`、`gsk-jp`。新規受け皿 3 件（`component:navla-jp`、`theme:creepypasta-jp`、`theme:pacom-jp`）。合計 268,455 → 149,862 文字（−118,593）。
- **P3 — Sigma-Plus 共有受け皿**（`REPORT-REWORK2-P3.md`）: `sunside-jp`、`andesite-jp`、`ink-jp`、`magicity-jp`、`tfnac-jp` の 5 ペア。`component:sigma-plus-jp` を作成（EN rev.38 を verbatim 同梱）。同時に **andesite-jp で非 savingpage の追加修正が見つかった**: インラインされていた「Saving Pageなし」無効化ブロック（lines 878–932）を除去し、CN 原本の verbatim `@import url("https://evernight-aquarium.wikidot.com/component:non-savingpage/code/1");` を同じ届けポイントに復元した（sigma-plus → non-savingpage → fonts → font-awesome → betterbetterfootnote の CN 原本順）。補注: 「46 番目の事例」という序数は記録からは裏付けられない（P3 レーンが andesite で発見した追加修正として記録されている）。
- **P4 — 大型 third-party base**（`REPORT-REWORK2-P4.md`）: 11 ペアのうち 10 件を再構成（`suprematism-jp`・`trauma-jp`→共有受け皿 `fragment:suprematism-jp-base-css`、`sound-jp`・`starry-jp`→既存 `theme:mox-jp/8`、`paradigm-inapplicable-jp`・`paradigm-reconstruction-jp`・`dream-of-the-stars-jp`→pinned jsDelivr dustjacket @import 復元、`share-future-community-jp`・`the-track-changers-jp`→verbatim @import 復元、`sodium-jp`→受け皿 `fragment:sodium-jp-base-css`）。**`theme:sci-fi-jp` は測定の結果「テーマ自身の適応済み CSS（own CSS, adapted）」であり、分離すべき外部 base が存在しないため再構成なし（no restructure）の処置**。件数: 891,039 → 224,049 文字（−666,990）。
- **P5 — Sigma-9 base 系列・小型埋め込み・画像 1 件**（`REPORT-REWORK2-P5.md`）: 11 ペアのうち 8 件を再構成（`asagao-jp`、`travellers-book-jp`、`parablue-jp`、`brokedown-database-jp`、`winxp-jp`、`rok-gov-theme-jp`、`the-buck-stops-here-jp`、`rima-jp`（base64 画像 → 原本の cdn.mer.run URL へ差し戻し）。新規受け皿 4 件（`fragment:collapsible-sidebar-jp-base-css`、`fragment:centered-header-bhl-jp-base-css`、`component:rok-gov-base-jp`、`component:the-buck-stops-here-base-1-jp`）。
- **監査の誤検知 4 件は変更なし（no-change disposition）として確定**: `normal-jp`、`mox-jp`、`dustframe-jp`（P5）、`sci-fi-jp`（P4）。いずれも原本側がその形式で届けるものをミラーしているだけであり、埋め込みではなかった。
- **andesite non-savingpage の位置づけ**: 上記 P3 の追加修正が、REWORK2 パケット中で唯一、監査の分類外で発見された追加の base 除去である。

### 4.3 REWORK2 の統合（`REPORT-REWORK2-INT.md`）

- 5 パケットを P1→P2→P3→P4→P5 の順で直列統合。canonical への初回コミット系列: `95fd1d1`（P1）→ `a393736`（コーディネーター LF 修正）→ `c65ec92`（P2）→ `2d69b1c`（P3）→ `3607153`（コーディネーター tab 修正）→ `7d9877c`（P4）→ `b89741d`（P5）→ `d4d0afe`（/start 更新）。最終 canonical HEAD は **`d4d0afe`**（`git status --porcelain` はクリーン）。
- 各パケットのスコープ付き検証（verbatim）:
  - P1: `SCOPED-OK: 10 pages match on both wikis`（初回は `fragment:u-navstyle-jp-base-css` で `SCOPED-DRIFT`（Wikidot が先頭の LF を除去するサーバ挙動）→ コーディネーターが canonical と lane コピー双方の先頭 LF を除去（commit `a393736`）後、再反映して SCOPED-OK）
  - P2: `SCOPED-OK: 12 pages match on both wikis`
  - P3: `SCOPED-OK: 7 pages match on both wikis`（初回は `component:sigma-plus-jp` line 674 `\tmargin: 0;` で `SCOPED-DRIFT`（Wikidot が行頭 tab を 4 スペースに変換するサーバ挙動）→ コーディネーターが canonical と lane コピー双方を tab→4 スペースに正規化（commit `3607153`）後、再反映して SCOPED-OK）
  - P4: `SCOPED-OK: 12 pages match on both wikis`
  - P5: `SCOPED-OK: 12 pages match on both wikis`
  - /start 更新（`d4d0afe`）: `SCOPED-OK: 9 pages match on both wikis`（`start` + 参照される 8 受け皿ページ）
- **コーディネーターによる 2 件の空白文字修正**（いずれも Wikidot のサーバ側正規化が原因で、canonical 側を修めて両側を byte-identical にしたもの）:
  1. **先頭 LF**（`fragment:u-navstyle-jp-base-css.txt`、commit `a393736`）: Wikidot が先頭の空白行を保存時に除去するため、canonical と lane コピー双方から先頭の `\n` を除去。
  2. **先頭 tab**（`component:sigma-plus-jp.txt` line 674、commit `3607153`）: Wikidot が行頭の tab を 4 スペースに書き換えるため、canonical と lane コピー双方を 4 スペースに正規化。
- `/start` への反映は各パケットレポートが「必要」と判定した行のみに限られ（P1 9 行、P2 9 行、P3 5 行、P4 10 行、P5 0 行）、合計 33 行が `d4d0afe` でコミットされ、両 wiki に反映された。1 件も余分な変更は加えていない。
- 全パケット完了マーカー: `REWORK2-P1..P5: COMPLETE`、`REWORK2-INT: COMPLETE`。

## 5. 記録すべきプロセス変更

出典: `stage2-lanes/lane-analysis2/ANALYSIS2.md`、`STEER-FANOUT.md`、`STEER-PARALLEL-ALL.md`、`STEER-PLAYBOOK.md`、`STEER-NO-FULL-VERIFY.md`、`STEER-SCOPED-VERIFY.md`、`STEER-NO-UPLOADS.md`、`STEER-NO-CHECK5.md`、`STEER-PRIOR-ART-INDEX.md`、`PRIOR-ART-INDEX.md`、`PATTERNS.md`

- **ファンアウトとバルクステア（残キュー 41 → 0）**: Stage 2 統合は当初バッチ逐次で実行されていたが、STEER-FANOUT.md（バッチ内の per-theme 並列化: reflection を 1 テーマ 1 サブエージェント）、STEER-PLAYBOOK.md（PLAYBOOK マイクロタスク形式）、STEER-PARALLEL-ALL.md（残りの全統合キュー — brief 記載では 41 件、同ファイルには "~40 integration briefs"、ANALYSIS2.md では 42 バッチ残 — を 1 つの並列 assignment として一括ステア）によって処理速度が大きく変わった。キューは全件処理され（LEDGER.json: 50/50 integrated）、引き継ぎは当初の予定どおり 2026-11-16 10:00 JST に OpenCode リードレーンへ移行した。
- **verify.py のコスト計測とスコープ付き検証への移行**: ANALYSIS2.md は 5 統合ターン（EN6・EN4・EN5・EN7・EN10）を計測し、verify.py の実行が壁時計の 65%（合計 ~8,051 秒 ≈ 134 分、9 ラン、ターンあたり計測シェア 33.0–80.2%）を占め、しかも `start` drift による再実行が EN7/EN10/EN4 で発生したことを示した。これに基づき STEER-NO-FULL-VERIFY.md（バッチ内の full verify.py 禁止、キャンペーン最終検証のみ）と STEER-SCOPED-VERIFY.md（スコープ付き検証 `verify_scoped.py` によるバッチ毎のクロージング、`SCOPED-OK: <n> pages` を報告行とする）が発出・定着した。
- **no-asset-uploads ルール**: owner の指示（2026-11-16、ANALYSIS2.md 記録では 02:11 JST の owner order）により、Stage 2 統合におけるアセットのアップロードは一切禁止された。画像参照は原ホストへの直接リンクのまま維持し、ホスティングは投稿フェーズへ延期（「asset hosting deferred — owner decision 2026-11-16」）。STEER-NO-UPLOADS.md に明文化されている。
- **Check 5 の Stage 2 退役**: STEER-NO-CHECK5.md（2026-11-16）により、Stage 2 統合の per-sample Check 5 計測は一切禁止された。理由: Check 5 が作成されるきっかけとなった Interaction 欠陥クラスは、共有サンプル本体の手書き in-flow hovertip exhibit に根本原因があったことが判明し（Phase 20 で除去済み）、再測定は「settled cause at full price」に過ぎないため。EN4（10 steps / 188.8 s）・EN6（16 steps / 518.5 s）が計測に払ったコストも計測記録に残っている。
- **prior-art 活用**: `PRIOR-ART-INDEX.md`（coordinator 生成、2026-11-16）は Stage 2 全 243 テーマについて scp-wiki-translation リポジトリの日本語ファイルの正確なパスを列挙し、日本語訳が存在したのは **220 テーマ**、ABSENT は 23 テーマ。`PATTERNS.md` は、prior translation をキャンペーン形に適用するための **8 つの機械的パターン**（credit:start-preview 不在、参照リビジョン未記録、bare `[[module Rate]]`、fonts.bunny.net imports、残存 `:scp-wiki:` include、nu-scptheme.github.io 等の EN BHL ホスト、EN タグ語 in iftags、EN-host assets）と、**3 項目の判断残件**（live EN との鮮度 diff、日本語 prose の品質、header/design 判断）を定義する。STEER-PRIOR-ART-INDEX.md はこれらを rework の出発点とするよう指示する。

## 6. 最終検証

- キャンペーン最終の全件照合（`verify.py`、2026-11-16 16:36 JST 開始、正本 HEAD `d1877e4` の構成に対して）: **exit 0 — `OK: 1157 pages match on both wikis`**。
- 補足: この実行の途中で、最終確認ラウンドの指摘に基づく /start の修正2件（commit `64f196e`、`d1877e4`）が入った。start の最終状態については、各コミットの反映後に範囲チェック（`verify_scoped.py start` → `SCOPED-OK: 1 pages match on both wikis`）で個別に確認済みであり、全件照合自体も exit 0 で返っている。したがって最終構成の全ページが照合済みである。

## 8. 最終確認ラウンド（2026-11-16、ゴーサインからの逆算による検証）

材料のそろい方（Stage 1: 実在テーマの候補と既存ページの材料 / Stage 2: 未掲載の原典テーマは全部、移植候補が /start に載ってマージまで完了）が嘘になる経路を列挙し、それぞれを独立レーンで検証した（`REPORT-REWORK2-FIN-*.md`）。注記（2026-11-16 18:1x 追記）: これは材料完全性の検証であり、ゴーサインの主張（スタッフ査読スキルで表示トラブルが無いことの確認）に対する検証ではない。§9 の取り下げを参照。

- **独立再確認（範囲チェック）**: REWORK2 の全ページを3分割して再照合 — P1+P2 22件、P3+P4 19件、P5+/start 13件、すべて `SCOPED-OK`（両 Wiki 一致）。
- **無変更判定の再裁き（FIN-DISPO）**: 監査の誤検知として無変更にした4件（normal、mox、dustframe、sci-fi）は、第三者レーンが原典キャッシュと突き合わせて **4件とも CONFIRM**（判定は正しい）。
- **母集団の再確認（FIN-LIVESET）**: 本物の scp-jp を当日再取得し、テーマタグ付きページの集合がキャンペーンの153件と完全一致（増減なし・改名なし）。
- **在席チェック（FIN-STARTSET）**: Stage 2 候補243件・Stage 1 の44行・既存153件が /start と正本に在ることを機械的に確認。欠けは名前のある例外だけだった（amethyst-v2 の候補ファイルなし＝処置済みの例外、telecommunications-monitoring-office-theme は EN20 の改名により短縮名で掲載）。
- **整合性チェック（FIN-CONSIST）とその処置**: 既存153件の等級は台帳と /start で完全一致（139/14）。cyberpunk と ny21 は台帳側でも等級は一致で、残るのは Wikijump 側の再測定注記のみと裁定し /start は変更なし。一方、実質的な古さ2件を修正した — (a) EN1–EN3 の15行が素材再ホスト必須時代の「候補完成（Check 4 未達）」のままだった（2026-11-16 の素材アップロード禁止の決定で未達理由は消滅）ため、統合済みの形に更新。(b) amethyst-v2 が /start に一切載っていなかったため、候補を作れなかった理由を明記した行を追加。いずれも正本先行で commit（`d1877e4`。先行する基盤セル修正は `64f196e`）、両 Wiki へ反映し範囲チェックで一致を確認した。なお EN1–EN3 の古さの根本原因は、P5 レーンが正本でない旧作業ファイルを見て「行がない」と誤判定した REWORK2 側の件と同じ型（見るべきファイルの取り違え）である。
- **棚卸し（FIN-HYGIENE）**: 正本ツリー clean（HEAD `d4d0afe` 時点）、200,000字を超えるページなし（最大は dustframe-jp の 194,747字）、新設の受けページ12件はすべて利用側から参照されている。
- **スキルへの反映（FIN-SKILL）**: theme-campaign-procedure スキルへの改善案を裁定し、適用可の5件（パケットの事前生成、経路の明記、領収書による判定、台帳の同時更新、副次効果の撤回可能性の明記）をスキル本体へ適用した。「バッチごとに全件照合」を含む3件は、オーナーの禁止命令と衝突するため却下した。あわせて、スキル内の分離モデルの記述を現在の運用（Wikidot 側を先に完了させる逐次分離）に修正した。

## 9. ゴーサイン — 取り下げ（2026-11-16 18:1x JST、コーディネーター）

本節は当初、オーナーの物差しとして「Wikidot 側の材料がそろい、Wikijump 側の描画の差が記録されていれば完了」と解釈してゴーサインを出していたが、これは誤りであり、**ゴーサインは取り下げる**。その物差しは /start の完了像（/start に残作業として何を載せるか）の話であって、ゴーサインの条件ではない。オーナーが 2026-11-16 16:44 に示した条件は「ゴーサインを出せるかから逆算せよ」であり、その後に明確化されたゴーサインの主張は次の通りである： **SCP-JP スタッフのテーマ査読スキル（theme-component-review）を全テーマに適用し、Sigma-10 へ移行しても表示トラブルが出ないことを確認できたら、ゴーサインが出せる。**

本キャンペーンがこれまでに行った検証（CRITERIA の Check 1〜4、最終確認ラウンド §8）は、材料のそろい方と正本・両 Wiki の一致を確認したもので、スタッフ査読スキルの点検（check_source.py の機械チェック、render_check.py の多幅・両エンジン点検、checklist.md の目視項目、localize.md 型 1〜11 の判定、参照 rev 以後の原語版更新の追従確認）は行っていない。したがって本報告書の確定事項は「Wikidot 側の材料はそろった」までであり、ゴーサインは未発行である。逆算したテスト一式と実施状況は `GOSIGN-TESTS.md` に置く。

## 10. ゴーサイン — 発行（2026-11-17、コーディネーター）

§9 の取り下げは本節により置き換える。ゴーサインの条件（SCP-JP スタッフの theme-component-review スキルを全テーマに適用し、Sigma-10 へ移行しても表示トラブルが出ないことを確認する）は、次の証拠連鎖により満たされた。

- 検証一式（`GOSIGN-TESTS.md` の T1〜T5）は全 287 テーマ（EN 157 / CN 87 / KO 40 / JP 2 / FR 1）に対して実施済みである（T1 ソースチェック全数、T4/T5 ローカライズ判定全数、T2/T3 描画チェック全数。測定内訳は 269 件実測 + 17 件再測定 + 1 件 NOT-RUN）。
- 台帳 `GOSIGN2-LEDGER.md` が全所見を登録し、ブロッキング OPEN 107 件（88 テーマ）を列挙した。FIX5 波（12 レーン）がこれら全件に対応し、補遺 `GOSIGN2-LEDGER-SUPPLEMENT.md` が再判定した：FIXED 81 件、根拠付き DISPOSITIONED 26 件、STILL OPEN 0 件。構造修正は正本ファイルに対するスポット検証でも確認済みである。
- 対象 287 件のうち合格判定の対象は 286 件であり、全件が「全所見が修正済み、または根拠付きで処分済み」の基準を満たす。残る 1 件 theme:amethyst-v2 は候補を制作できなかった指名例外であり、台帳にその旨記録されている。
- 修正はすべて正本（Rokurolize/sigma10-check-wiki、HEAD 435a6bb）にコミットされ、両チェック Wiki への反映は verify_scoped で一致を確認済みである。

よって、Sigma-10 移行の Wikidot 側材料について**ゴーサインを発行する**。なお本節の主張は Wikidot 側の材料と査読に限る。Wikijump 側フェーズは凍結されたままであり、本ゴーサインの対象に含まない。
