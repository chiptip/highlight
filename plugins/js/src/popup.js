ouibaApp.service('pageInfoService', function() {
    this.getInfo = function(callback) {
        var model = {};

        chrome.tabs.query({'active': true}, function (tabs) {
            if (tabs.length > 0)
            {
                model.title = tabs[0].title;
                model.url = tabs[0].url;

                callback(model);
                chrome.tabs.sendMessage(tabs[0].id, { 'action': 'PageInfo' }, function (response) {
                    // callback(model);
                });
            }

        });
    };
});

ouibaApp.controller("PageController", function ($scope, pageInfoService) {
    $scope.message = "Hello from Ouiba";

    pageInfoService.getInfo(function(info){
        console.log("callback from PageInfoService");
        $scope.title = info.title;
        $scope.url = info.url;
        $scope.$apply();
    });
});
