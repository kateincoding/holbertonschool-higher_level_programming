$(function () {
  $.get('https://fourtonfish.com/hellosalut/?lang=fr', function (data, txtStatus) {
    if (txtStatus === 'success') {
      $('DIV#hello').text(data.hello);
    }
  });
});
