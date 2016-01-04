=======
tapper.update
=======

| tapperプロジェクトでは
| *html/img/preloads* 内に含まれている画像ファイルをWebview表示時にプリロードさせることができます。

使用例
==========

下記のようなディレクトリ構成のケースで

.. code-block:: shell

  $ tree
  .
  ├── css
  │   ├── contents.css
  │   └── normalize.css
  ├── img
  │   └── preloads
  │       └── sample.png
  ├── index.html
  └── js
      ├── contents.js
      └── tapper.js

*img/preloads/sample.png* を表示時にプリロードさせたい場合

.. code-block:: shell

  $ tapper update

tapper updateコマンドを実行すると

.. code-block:: shell

  $ tapper update
  Tapper update.
      load: sample.png
      create: ./js/tapper.js
    Succeeded.

.. code-block:: javascript

  16      // image preload
  17      var _preload_img = function() {
  18          var image = [
  19          'img/preloads/sample.png'
  20          ];
  21          $.each(image, function(i, src) {
  22              $('<img>').attr('src', src);
  23          });
  24      }

| 上記のようにpreload処理にsample.pngが含まれていることが確認できます。
| tapper updateによりtapper.jsを更新した場合
| tapper.jsに対して行った修正は上書きされてしまうので注意してください。
