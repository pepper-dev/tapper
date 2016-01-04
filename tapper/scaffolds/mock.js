
var MockData = {
    "Tapper/InitData": '{ "DummyKey": "DummyData" }'
};

var MockEvents = [];

var MockProxy = {
    subscriber: function(name) {
        return {
            then: function(callback) {
                var sub = new EventSubscription(name);
                sub.signal = {
                    connect: function(func) {
                        MockEvents.push({
                            "name": name,
                            "func": func,
                            "id": MockEvents.length + 1
                        });
                        return {
                            then: function(l) {
                                l(MockEvents.length);
                            }
                        }
                    },
                    disconnect: function(id) {
                        var i = MockEvents.indexOf(Events[id]);
                        MockEvents.splice(i - 1, 1);
                    }
                };
                callback(sub);
            }
        }
    },
    getData: function(name) {
        console.log("getData : " + name);
        return {
            then: function(func) {
                try {
                    func(MockData[name]);
                } catch (e) {
                    console.warn("ダミーデータがセットされていません。\nmock.jsのMockDataにKeyとValueを追加することでダミーデータを設定できます。");
                }
            }
        }
    },
    raiseEvent: function(name, value) {
        $.each(MockEvents, function(i, v) {
            if (v.name == name) {
                v.func(value);
            }
        });
    }
}

var MockService = {
    then: function(succeeded, failed) {
        succeeded(MockProxy);
    }
}

var MockSession = {
    service: function(name) {
        console.log("Mock create : " + name);
        return MockService;
    }
}

function QiSession( callback ) {
    callback(MockSession);
}

