chrome.extension.onMessage.addListener(
  function (request, sender, sendResponse) {
    if (request.action == 'PageInfo') {
        var pageInfos = [];
        sendResponse(pageInfos);
    }
  }
);
