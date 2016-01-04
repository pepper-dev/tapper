=====
Tapper.proxy
=====

| Tapperでは接続を確立したALProxyサービスをTapper.proxy[*ALProxyName* ]に保持しています。
| Tapper.utlでラップされていないAPIをコールしたい場合は
| Tapper.proxy.ALMemoryを呼び出してください。

.. code-block:: javascript

    Tapper.proxy.ALMemory.getTimestamp("Memory/Name").then(function(val_timestamp) {
        console.log(val_timestamp);
    });
