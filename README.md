
# Tapper

pepperタブレット開発の雛形生成ツールです。

----

## ・環境

* Python2.7

----

## ・インストール方法

インストール時にはpipを使うと便利です。

```shell
# pipのインストール
$ easy_install pip
```

環境に合わせて読み替えてください。
```shell
# tapperのインストール
$ pip install tapper
```

----

## ・仕様

インストール後はtapperコマンドがインストールされます。

```shell
$ tapper --help
usage: tapper [-h] {create,update} ...

positional arguments:
  {create,update}  sub-command help
    create         create scaffolds.
    update         update scaffplds.

optional arguments:
  -h, --help       show this help message and exit
```

### ・ファイル構成

```shell
$ tapper create # create サブコマンドで雛形を生成
Tapper create.
  Scene 1
    mkdir: ./html
    mkdir: ./html/css
    mkdir: ./html/js
    mkdir: ./html/img
    mkdir: ./html/img/preloads
    create: ./html/index.html
    create: ./html/css/contents.css
    create: ./html/css/normalize.css
    create: ./html/js/tapper.js
    create: ./html/js/contents.js
  Succeeded.
$ ls # 実行後はhtmlディレクトリが生成される
html
$ tree html
html                  # タブレットが参照するhtmlディレクトリ
├── css               # スタイルシート用のディレクトリ
│   ├── contents.css  # ユーザスタイルシート
│   └── normalize.css # デフォルトのスタイルリセット用のスタイルシート
├── img               # 画像用のディレクトリ
│   └── preloads      # タブレット表示時にプリロードされる画像用のディレクトリ
├── index.html        # 表示されるindex.html
└── js                # javascript用のディレクトリ
    ├── contents.js   # アプリケーション用のjsファイル
    └── tapper.js     # 自動生成のjsファイル

4 directories, 5 files
```

### index.html

* デフォルトではviewportで1.335倍に拡大しています。(1280 * 800)
* 各cssとjavascriptを読み込んでいます。
* デフォルトではsceneが1つ定義されています。

### tapper.js

* tapper.jsは直接編集してしまうとupdate時に上書きされてしまうので
  直接書き換えないようにしてください。

### contents.js

* create時に下のようなjavascriptファイルが生成されます。

```javascript
// pepper contents

Tapper.contents = {

    onLoad: function() {
        console.log("onLoad.");
    },

    onStart: function() {
        console.log("onStart.");
    },

    onScene1: function() {
        console.log("onScene1");
    }
}
```

#### ・onLoad

* QiMessagingの接続前かつ画像のプリロードの前に呼び出されます。
* タブレットのWebviewが表示されたタイミングで呼び出されるので、
  javascript内で使用するグローバル変数の宣言などで使用します。

#### ・onStart

* 上記onLoadの処理終了後に呼び出されます。

#### ・onScene_[n]_

* Sceneの切り替え時に呼び出されます。


----

## サブコマンド

#### ・create

カレントディレクトリにpepperアプリで使用できるhtml雛形を生成します。

```shell
# 雛形を生成
$ tapper create
```

--sceneオプションを付与することで生成される雛形のsection数を指定できます。

```shell
# sceneを3つもつ雛形を生成
$ tapper create --scene 3
```

#### ・update

* カレントディレクトリにあるtapperプロジェクトのtapper.jsを更新します。
* img/preloadsに画像を追加した場合は必ず実行してください。

```shell
$ tapper update
```
