=====
Tapper.utl
=====

| 頻繁に使用するALProxyのメソッドを定義しています。
| 定義されているAPIは以下の通りです。

Tapper.utl.raiseEvent(name, val)
========

ALMemory.raiseEventを実行します。

.. code-block:: javascript

    Tapper.utl.raiseEvent("Memory/Name", "foo");


Tapper.utl.subscribeEvent(name, func)
=========

ALMemoryのイベントを監視します。

.. code-block:: javascript

    Tapper.utl.subscribeEvent("Memory/Name", function(val) {
        console.log("Raised event [ Memory/Name ] value = " + val);
    });

Tapper.utl.getData(name, succeeded, failed)
=========

ALMemory.getDataを実行します。

.. code-block:: javascript

    Tapper.utl.getData("Memory/Name", function(data) {
        console.log("Get data [ Memory/Name ] value = " + data);
    }, function() {
        console.warn("Memory name is not defined.[ Memory/Name ]");
    });


