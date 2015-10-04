ouibaApp.service('pageInfoService', function() {
    this.getInfo = function(callback) {
        var model = {};

        chrome.tabs.query({'active': true}, function (tabs) {
            if (tabs.length > 0)
            {
                model.title = tabs[0].title;
                model.url = tabs[0].url;
                callback(model);
            }
        });
    };
});

ouibaApp.service('lookupService', function($http){
    this.lookup = function(url, success_cb, failure_cb) {
        $http({
            method: 'POST',
            url: 'http://www.ouiba.com/api/events/',
            data: { url: url }
        }).then(function successCallback(response) {
            success_cb();
        }, function errorCallback(response) {
            failure_cb();
        });
    };
});

ouibaApp.controller("PageController", function($scope, pageInfoService, lookupService) {
    success_callback = function(){
        console.log("successful");
    };

    failure_callback = function(){
        console.log("failed");
    };

    $scope.message = "Hello from Ouiba";
    pageInfoService.getInfo(function(info){
        console.log("callback from PageInfoService");
        $scope.title = info.title;
        $scope.url = info.url;
        $scope.$apply();

        // sending this to the server
        lookupService.lookup($scope.url, success_callback, failure_callback);
    });
});
