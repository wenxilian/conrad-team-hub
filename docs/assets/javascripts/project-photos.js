// 官方配图载入失败时显示来源入口，避免把损坏图标留在阅读正文中。
document.querySelectorAll('.case-photo').forEach(function (figure) {
  var img = figure.querySelector('img');
  var note = figure.querySelector('.photo-unavailable');
  function failed() { img.hidden = true; note.hidden = false; }
  img.addEventListener('error', failed);
  img.addEventListener('load', function () { if (img.naturalWidth > 0) { img.hidden = false; note.hidden = true; } });
  if (img.complete && !img.naturalWidth) failed();
});
