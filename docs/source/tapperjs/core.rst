=====
Tapper.core
=====

| jsのロード時にTapperフレームワークの初期化を行います。
| 実行される処理は下記の通りです。

* Tapperオブジェクトの初期化
* QiSessionの接続
* 画像のプリロード
* Tapper/InitDataのjson文字列をパースしてTapper.init_dataに設定

| 実行前にTapper.contents.onLoadの実行
| 初期化処理終了時にTapper.contents.onStartの呼び出しを行います。

