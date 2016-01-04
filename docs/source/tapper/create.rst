========
tapper.create
========

| tapperの最も基本的なコマンドです。


ひな形を作成する
================

下記のようにコマンドラインからtapperコマンドを使用することで、簡単にpepper用のhtmlのひな形を生成することができます。

.. code-block:: shell

 $ tapper create
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


sceneオプション
===============

sceneオプションをつけることで最初に作成するsceneの数を指定することができます。
sceneの数は後からでも変更できるので、
途中でsceneが増えた場合でもcreateを実行し直す必要はありません。

.. code-block:: shell

 $ tapper create --scene 5
 Tapper create.
  Scene 5
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


sceneオプションを指定して生成されたindex.html

.. code-block:: html

    <!DOCTYPE html>
    <html>
        <head>
            <meta charset="UTF-8">
            <meta http-equiv="Content-Type" content="text/html; charset=utf-8">
            <meta name="viewport" content="initial-scale = 1.335, minimum-scale = 1.335, maximum-scale = 1.335"/>

            <link rel="stylesheet" href="css/normalize.css" />
            <link rel="stylesheet" href="css/contents.css" />

            <script>
            var Tapper_Debug = false;
            var Tapper_Debug_Host = "pepper.local";
            </script>

            <script src="/libs/qimessaging/2/qimessaging.js"></script>
            <script src="/lib/jquery/jquery.min.js"></script>
            <script src="js/tapper.js"></script>
            <script src="js/contents.js"></script>

        </head>
        <body>
            <section id="scene1" style="display: block;">
            </section>
            <section id="scene2" style="display: none;">
            </section>
            <section id="scene3" style="display: none;">
            </section>
            <section id="scene4" style="display: none;">
            </section>
            <section id="scene5" style="display: none;">
            </section>
        </body>
    </html>
