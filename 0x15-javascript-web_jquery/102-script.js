document.addEventListener('DOMContentLoaded', function () {
  const url = 'https://fourtonfish.com/hellosalut/';

  $('INPUT#btn_translate').click(function () {
    const lanValue = $('#language_code').val();
    const finalUrl = `${url}?lang=${lanValue}`;
    $.get(finalUrl, function (data, txtStatus) {
      $('DIV#hello').text('');
      if (txtStatus === 'success' && lanValue) {
        $('DIV#hello').text(data.hello);
      }
    });
  });
});
