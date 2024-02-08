let path = "";
addEventListener('message', evt => {
  evt.source.postMessage(path.includes(evt.data) ? true : false);
  path = "";
});

addEventListener('fetch', evt => {
  path = (new URL(evt.request.url)).pathname;
});
