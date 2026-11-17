# Review package — scp-jp-storage (FS) site theme: Sigma-9 → Sigma-10

## Status

| Field | Value |
|---|---|
| Package status | Pilot — 本パッケージはテーマ別レビューパッケージの最初の1件であり、残り全体の形式を決めるための試行である。 |
| Candidate status | Authored, not deployed — 2026-11-17 に本パッケージのために作成した。どこにもデプロイしておらず、本番の FS は現在も original を配信している。 |
| Verification status | Source-level only — 添付ファイルページでの確認（要件が求める描画確認）は未実施であり、本パッケージのどこでも実施済みとは主張しない。 |
| Governing requirement | `/start` の「サイト運用Wiki」表の FS 行（正本リポジトリ `pages/start.txt`）。以下に原文のまま引用する。 |

Requirement（FS 行、要件セル）:

> Sigma-10をベースにします。ヘッダー背景、グラデーション、オーバーレイは、Sigma-10のヘッダーとトップバーと競合するため再表現します。固定「SCP財団」の疑似要素は「SCP-JP ストレージ」に置き換え、モバイルのspan非表示も新しい構造に合わせます。top-bar非表示の調整とprivileged.cssは維持します。添付ファイルページで確認します。

Current composition（FS 行、現在の構成セル）:

> Sigma-9（/files/theme/sigma-9/sigma-9.css）＋storage上書き（header-bg.png、黒→#002bbd、topbar #535353→#3c3c3c、top140/23pxオーバーレイ、h1 150%、モバイル「SCP-JP ストレージ」）＋privileged.css

本パッケージの判断根拠は、キャンペーンルート（`/home/roku/.local/state/wikijump/muse-bhl/theme-port-readiness-20261114/`）にある `REPORT24.md` の §3（FS 調整インベントリ F1–F8）と §4 である。

## Provenance

FS は Wikidot のテーマページではなく、SCP-JP の GitHub Pages ツリーから配信される静的 CSS ファイルがテーマであり、各ページへはサイトの internal-style 層が読み込む。したがって本パッケージにおける「参照リビジョンにおける原典」とは、ページレビジョンではなく、2026-11-15（Asia/Tokyo）に取得した配信ファイルのキャプチャである。以下のミラーはいずれもキャプチャとバイト単位で同一であり、ハッシュによって誰でも再検証できる。

| File | Source | Role | Captured | SHA-256 |
|---|---|---|---|---|
| `original.css` | https://scp-jp.github.io/files/util/storage/styles/theme.css | FS の上書き層そのもの。Sigma-9 ベースと privileged.css を import し、ストレージ固有のルールをすべてここで設定する。candidate が置き換える対象はこのファイルである。 | 2026-11-15、証拠キャプチャ `evidence/p24/fs-theme.css`（キャンペーンルート） | `2c6a67f37b8e0293f03f94b153a75611f3e56aba43a17cf7fcd20427cbc82e81` |
| `original-privileged.css` | https://manage.scp-jp.com/api/public/privileged.css?sid=4548695&required_level=moderator | original が import する管理用スタイルシート（モデレータ権限スコープ、指名されたスタッフアカウントに対する user-target 非表示）。記録のためのミラーであり、candidate は存在しない（「Deliberately unchanged」参照）。 | 2026-11-15、証拠キャプチャ `evidence/p24/privileged-fs.css`（キャンペーンルート） | `ac5488624888359e72d405cb45c447bb377682d7b22d58efb9fccafd9931ab23` |
| `candidate.css` | — (authored here) | 移植後の上書き層。`original.css` と同じ役割を Sigma-10 ベースで担う。デプロイとは、上記 `original.css` の Source URL にあるファイルをこれで置き換えることである。 | Authored 2026-11-17 | — |
| `diff.md` | — (generated) | `original.css` → `candidate.css` の unified diff。`review/build_review.py` が生成する。手で編集しないこと。 | Generated 2026-11-17 | — |

構造比較に使った参照キャプチャ（本パッケージにはミラーしない。同じ証拠セット `evidence/p24/`）:

- 素の Sigma-9 ベース `sigma-9.css`（30,638 B）、SHA-256 `69d856fed1eb75998b4be68024ff20441d672066660a8c83eaef70db143087b8`。original の最初の `@import` が読み込むファイル。
- 取得時点の Sigma-10 JP ベース `sigma10-jp.css`（20,312 B）、SHA-256 `2057dd4383be635bd239716615f3eafa9af036fd6197017efd7ee476c3ab6ab8`。表示確認 Wiki の `theme:sigma-10-jp` の背後にある CSS で、その配信先は https://scp-jp.github.io/sigma/css/sigma.min.css（SCP-JP/sigma、基盤カスケードは KanekoLiku/sigma）。

## Summary

FS（scp-jp-storage.wikidot.com）は SCP-JP の添付ファイル保管用 Wiki である。その視覚的アイデンティティは、素のベースに対する46行の CSS ファイル1件に尽きる。青いヘッダーグラデーションとストレージバナー画像、ヘッダー下の暗いグラデーションバンド、拡大されたサイトタイトル、モバイル用タイトル文字列である。移行ではこのファイルの下敷きが Sigma-9 から Sigma-10 に変わり、ルールのうち3件が新しいベースと衝突する。ファイルが定義するカスタムプロパティは Sigma-10 には存在しないインターフェースであり、さらに Sigma-10 はヘッダータイトルを自前で印字する（「SCP」+「財団」の疑似要素、実サイト名の span は非表示）ため、ストレージのタイトルが壊れる。そこで candidate は、ベースの import を差し替え、2つのグラデーションを利用箇所に直接書き下し、タイトルの疑似要素を両方とも置き換えて、ヘッダーがちょうど「SCP-JP ストレージ」と読めるようにする。それ以外、管理用 privileged.css の import もタイトルサイズも含め、すべて据え置く。diff 全体は3ハンク、+14 / −16 行。そのうち追加6行は出荷されないレビュー段階のコメントである（各 change class の「Delivery-stage forms」参照。移植そのものの変更は +8 / −16）。

## Change classes

### 1. Base import: Sigma-9 → Sigma-10 (diff hunk 1)

**What changed.** 最初の `@import` が、FS Wiki にアップロードされた Sigma-9 のコピー `/files/theme/sigma-9/sigma-9.css` ではなく、Sigma-10 JP の配信先 `https://scp-jp.github.io/sigma/css/sigma.min.css` を読み込むようになる。変更は1行で、直下の privileged.css の import には触れないため、カスケード順序（ベース → privileged → 本ファイル自身のルール）は保たれる。

**Why.** 要件の最初の一文「Sigma-10をベースにします」による。本ファイルの後続ルールはすべて Sigma-9 のヘッダージオメトリとタイトル構造を前提に書かれており、Sigma-9 の import を残せばサイト全体が旧ベースに留まる。選んだ URL は本番の Sigma-10 JP 成果物であり、Sigma-10 表示確認 Wiki が `theme:sigma-10-jp`（正本リポジトリ `pages/theme:sigma-10-jp.txt`）経由で使う配信先と同一である。

**Verify.** `diff.md` の hunk 1。`grep -n "sigma-9" candidate.css` が何も返さないこと。import URL が `pages/theme:sigma-10-jp.txt` 内のものと一致すること。

**Delivery-stage forms.** なし。この行はデプロイ後の最終形であり、URL はドラフト用や確認 Wiki 用のホストではなく本番配信先である。

### 2. Header background: storage image re-layered, gradient written out (diff hunk 2, first rule)

**What changed.** `div#container-wrap` の背景は、ストレージバナー画像（`header-bg.png`、ルート相対 URL はバイト単位で同一）と `background-size: 100px 141px` を保ち、第2層が `var(--c-header)` ではなくリテラルの `linear-gradient(180deg, black 25%, #002bbd 100%)` になる。`--c-header` と `--c-topbar` を定義していた `#container-wrap` ルールは削除される。

**Why.** 要件「ヘッダー背景、グラデーション、オーバーレイは、Sigma-10のヘッダーとトップバーと競合するため再表現します」による。`--c-*` 変数は ukwhatn の「Sigma9 Customizable Header」層のインターフェースであり、Sigma-9 では他のルールがこれを消費する。しかし Sigma-10 JP ベースには `--c-header` / `--c-topbar` を消費する箇所がなく（REPORT24 F1）、本ファイル内でも消費箇所は各1件だけである。定義を残しても、新しいベースには存在しないカスタマイズインターフェースを無効なまま保持することになる。各値を唯一の利用箇所に書き下せば、描かれるグラデーションは同一に保たれる（25% 地点の黒から `#002bbd` へ。/start 行が記録する「黒→#002bbd」である）。

**Verify.** グラデーションの色停止位置を、`diff.md` hunk 2 で削除される `--c-header` 定義と比較すること。画像 URL と `background-size` の行が同ハンク内の context（不変）行であること。Sigma-10 キャプチャ（`evidence/p24/sigma10-jp.css`）に `--c-` 変数が含まれないこと。

**Delivery-stage forms.** なし。ルート相対の画像 URL は、candidate が GitHub Pages 上の元のパスで original を置き換えた時点で、original のものとまったく同じ解決をする。

### 3. Top-bar overlay band: gradient written out, band kept (diff hunk 2, second rule)

**What changed.** `div#container-wrap::after` は背景以外のすべての値（position、`top: 140px`、`height: 23px`、ドロップシャドウ）が不変で、背景だけが `var(--c-topbar)` からリテラルの `linear-gradient(180deg, #535353 0%, #3c3c3c 53%)` になる。change class 2 と同じ書き下しである。

**Why.** 要件の同じ一文と、REPORT24 F3 の条件付き判断による。Sigma-10 は `#top-bar` をすでに `top: 140px`、高さ21px に配置するため、このバンドを再表現するのはストレージのグラデーションと影が今も必要だからに限る。そして /start 行はオーバーレイ（「top140/23pxオーバーレイ」）を、削除ではなく再表現すべき構成要素として挙げている。このバンドはトップバーメニューの背後の帯を着色し、ヘッダーの影を落とすものである。Sigma-10 JP ベースは `#top-bar` 自体に背景を与えないため、バンドを落とせばメニューがヘッダーグラデーションの上に直接乗り、影も失われる。ヘッダージオメトリは両ベースで同一（`#header` 高さ140px、padding-bottom 22px）であり、元の140px / 23px の配置は今も正しい配置である。

**Verify.** グラデーションの色停止位置を `diff.md` hunk 2 で削除される `--c-topbar` 定義と比較すること。同ルールの他の宣言がすべて context 行であること。Sigma-10 キャプチャにおける `#top-bar` のジオメトリ（`top:140px; height:21px`）。

**Delivery-stage forms.** なし。

### 4. Site title: both pseudo-elements replaced (diff hunk 3)

**What changed.** Sigma-9 層のモバイル専用ブロック（`@media(max-width:768px)`：`h1 a span` を隠し、`::before { content: "SCP-JP ストレージ"; font-size: 25px }` を表示）は、無条件の2ルールに置き換わる。`#header h1 a::before { content: "SCP-JP ストレージ" }` と `#header h1 a::after { content: none }` である。span を隠すルールは引き継がない。

**Why.** 要件「固定「SCP財団」の疑似要素は「SCP-JP ストレージ」に置き換え、モバイルのspan非表示も新しい構造に合わせます」と、/start の節の前文「Sigma-10ではどちらのWikiでも、ヘッダーが「SCP財団」を疑似要素で固定し、サイト名のh1 spanを隠します」による。具体的に、Sigma-10 JP ベースは `#header h1 a span { font-size: 0 }` を**全幅で**設定し、`#header h1 a::before { content: 'SCP' }` と `#header h1 a::after { content: '財団' }` を持つ。この変更の形は、そこから導かれる3つの帰結で決まる。

- span はベースがすでに隠すため、candidate の span 非表示ルールは死んだコードになる。Sigma-9 層の「モバイルの span 非表示」は、要件が予告するとおり新しい構造に吸収される。
- `::before` だけを上書きする（Sigma-9 ルールの素朴な移植）と「SCP-JP ストレージ財団」と描画される。REPORT24 F5 がまさにこの失敗を名指ししている。最終タイトルがちょうど「SCP-JP ストレージ」になるよう、疑似要素は両方とも設定しなければならない。
- ベースは疑似タイトルを全幅で表示するため、置き換えも無条件になる。目に見える帰結として、デスクトップのヘッダータイトルの文字列が変わる。Sigma-9 ではデスクトップのヘッダーはサイト名 span の「SCP-JPファイルストレージ」を表示していた。Sigma-10 では span は決して描画されず、ヘッダーは要件が選んだ文字列「SCP-JP ストレージ」を全幅で表示する。

**Verify.** `diff.md` の hunk 3。上で引用したベースの3ルールは Sigma-10 キャプチャ（`evidence/p24/sigma10-jp.css` の末尾付近にある `#header h1 a::before` / `::after` / `span` のルール）に存在すること。candidate の2つの content 値が、要件の文字列と `none` であること。

**Delivery-stage forms.** 追加行のうち6行は、`::before` ルールの上にある `REVIEW:` コメントである（「Judgment calls」参照）。これはパッケージ段階の注記であって移植の一部ではなく、タイトルサイズの問題が決着した時点で解消し、デプロイ前までに取り除く。このハンクの他の行に delivery-stage のものはない。

## Deliberately unchanged

- **privileged.css rule.** privileged.css は外部で管理され、現状のまま保持され、candidate を受けることは決してない。`manage.scp-jp.com` がモデレータ権限スコープの URL で配信するもので、テーマシステムの外で運用されており、要件も保持を命じている（「privileged.cssは維持します」、REPORT24 F6）。`candidate.css` 内の import 行は original とバイト単位で同一であり、ベース import の直後という位置も同じで、カスケード上の位置は保たれる。`original-privileged.css` が本パッケージにあるのは記録のためのミラーとしてのみである。
- **Title size rule (REPORT24 F4).** `#header h1 a { font-size: 150% }` はそのまま引き継ぐ。Sigma-10 ベースは同じ要素に `1.5em` を設定するため、このルールは新しいベースでは no-op である。それでも残すのは、ストレージのタイトルサイズを、タイトルを所有する層自身が表明するためであり、REPORT24 の判断も「carries as-is」である。
- **Attribution block.** ukwhatn の「Sigma9 Customizable Header」コメント（著者、出典、CC BY-SA 3.0）はそのまま引き継ぐ。上書き層の設計と値は今もこのファイルに由来しており、ライセンス表記は我々が剥がしてよいものではない（`--c-*` インターフェース自体は change class 2 のとおり無くなる。コメントは層の来歴として残る）。
- **Banner image URL and size.** `/files/util/storage/media/component/theme/header-bg.png` と `background-size: 100px 141px` はバイト単位で同一である（change class 2）。
- **Overlay geometry and shadow.** `top: 140px`、`height: 23px`、`box-shadow` の値はバイト単位で同一である（change class 3）。
- **Layers outside this file.** サイト全体の top-bar 非表示ブロック（REPORT24 F7：`#top-bar a.newpage`、`.top-startlink`、top-bar の div 1件の非表示）と、共有の `#side-bar .menu-item` ブロック（F8）は、別々のサイト全体スタイル層で配信されており、`evidence/p24/scp-jp-storage-sitewide-topbar.css` と共有サイドバーのキャプチャとして取得されている。要件はこれらを保持し（「top-bar非表示の調整…は維持します」、REPORT24 §4 の FS 項目4）、移植はこれらを引き継ぎも削除もしない。編集ではなく、描画確認の場で検証されるものである。

## Judgment calls and open questions

- **REVIEW — title size on mobile.** `candidate.css` 内の唯一の `REVIEW:` コメントで、`::before` ルールの上に置いた。Sigma-9 層はモバイルのタイトルを25px に固定していた。candidate は疑似要素にサイズを設定しないため、Sigma-10 自身の `#header h1 a` のサイズ指定が効く（デスクトップは 1.5em、`max-width: 767px` ブロック内では `calc(.75em + 2vw)`）。要件が命じるのはタイトルの**文字列**の置き換えと span 非表示の適応であり、サイズではないため、この形にした。ストレージのタイトルがモバイルで固定25px を保つべきなら、追加は media ルール1件であり、実機幅での現行タイトルと見比べて描画確認の場で決めるべき事項である。
- **Band height 23px vs Sigma-10's 21px bar.** candidate はバンドを Sigma-10 のバーの21px に縮めず、元の23px を保つ。バンドはバーそのものではなく背景の帯であり、両ベースともヘッダー領域は140px + 下パディング22px で、バンドのはみ出す2px とその影は、Sigma-9 のときとまったく同じくパディング領域に落ちる。高さを変えれば影の位置が動き、それを求める要件はない。
- **Desktop title text.** change class 4 に記録したとおり、移行後のヘッダーは全幅で「SCP-JP ストレージ」と読めるようになり、Sigma-9 のデスクトップが表示していた「SCP-JPファイルストレージ」（サイト名）とは異なる。これは要件が選んだ置き換え文字列と、Sigma-10 の常時 span 非表示との組み合わせによる帰結であり、デプロイ時の驚きではなく、レビュー済みの帰結としてここに明示する。
- **Questions only site-admin access can settle**（REPORT24 §5 から引き継ぎ、未解決）。FS の Site Manager 設定において import されるテーマファイルが唯一のサイトテーマソースか、配信される style ブロックのうちどれが管理用 Custom CSS フィールドか。privileged.css（sid 4548695）が今も FS に適用されているか、その user-target 非表示が今も必要か。移行後の上書き層を import されるテーマファイルに置くのか Custom CSS フィールドに置くのか。
- **Verification status, restated.** 本パッケージの内容はすべてソースレベルのものである。ファイルハッシュ、生成された diff、取得済みの両ベースとのルール単位の比較。要件が名指しする描画確認（「添付ファイルページで確認します」。FS が存在する目的である添付ファイルページでの確認）は、candidate がブラウザから読み込める場所にまだデプロイされていないため、実施していない。本パッケージのいかなる記述も、描画された振る舞いを主張するものではない。
