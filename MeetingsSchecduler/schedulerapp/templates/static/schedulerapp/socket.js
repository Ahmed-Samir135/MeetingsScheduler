(function () {
  const chatSocket = new WebSocket("ws://" + window.location.host + "/ws/");
  chatSocket.onmessage = (e) => {
    htmx.trigger("#tbody", "refresh");
  };
})();
