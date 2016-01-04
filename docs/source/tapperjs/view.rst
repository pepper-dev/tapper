=====
Tapper.view
=====

| Tapperのviewに関する処理を記述しています。
| また、シーンの切り替えやボタンのタッチイベントのバインドを行っています。

初期化
========

| Tapper.coreの初期化時にTapper.viewが初期化されます。
| Tapper.view初期化時にはhtmlに存在する全ての
| *data-btn-id* を持つノードのタッチイベントを設定します。
| *data-btn-id* を持つノードのtouchstartではtouchedクラスを付与し、
| touchend時に *Tapper/View/ButtonTouched* にraiseEventを実行します。

Tapper.view.changeScene(id)
========

| シーン切り替え後にTapper.contents.onScene *n* をコールします。
| また、*Tapper/View/ChangeScene* イベントを検知した際にコールされます。

.. code-block:: javascript

    // javascriptでコールする場合
    Tapper.view.changeScene(1);

    // ALMemoryのイベントでシーンの切り替えを行う場合
    Tapper.utl.raiseEvent("Tapper/View/ChangeScene", 1);

Tapper.view.buttonSelect(btn_id)
========

| *Tapper/View/ButtonSelect* イベントを検知した際にコールされます。
| また、btn_idで指定されたidを持つノードにselectedクラスを付与します。

Tapper.view.buttonReset
=========

| selectedクラスを付与された全てのノードからselectedクラスを削除します。

