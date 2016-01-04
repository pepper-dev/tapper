.. tapper documentation master file, created by
   sphinx-quickstart on Thu Dec 10 19:22:47 2015.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

==================================
Tapper
==================================


| Tapperはpepperアプリケーションのディスプレイ側の開発用フレームワークです。
| BSD-Licenceの下でライセンスされています。

Github https://github.com/pepper-dev/tapper

Tapperとは
=================

| Tapperで作成したひな形はpepperアプリケーションにおけるjqueryやqimessaging
| ALProxyとの連携部分を定義したtapper.jsを読み込んでいます。

| 例えば、tapper.jsで定義されている
| Tapper.utl.raiseEventやTapper.utl.subscriveEventを使用することで
| ALMemoryとの連携を簡単に行うことができます。
|
| あまり使用しないALProxyのサービスは読み込んでいないので
| 軽量なアプリケーションでも問題なく使用することができます。


単純な使用例
=================

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

.. toctree::
   :maxdepth: 2


導入手順
==================

pipを使用してインストールします。

.. code-block:: shell

  $ easy_install pip
  $ pip install tapper

マニュアル
==================

CUI tools
------------------
* :doc:`tapper/create`
* :doc:`tapper/update`

tapper.js
------------------
* :doc:`tapperjs/core`
* :doc:`tapperjs/utl`
* :doc:`tapperjs/session`
* :doc:`tapperjs/proxy`
* :doc:`tapperjs/view`

contents.js
------------------
* :doc:`tapperjs/contents`
