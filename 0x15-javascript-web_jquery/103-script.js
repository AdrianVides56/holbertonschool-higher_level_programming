document.addEventListener('DOMContentLoaded', () => {
  const url = 'https://www.fourtonfish.com/hellosalut/';

  $('INPUT#btn_translate').on('click', (e) => {
    const salutation = url + '?lang=' + $('INPUT#language_code').val();
    $.get(salutation, (data) => {
      $('DIV#hello').text(data.hello);
    });
  });
  $('INPUT#language_code').on('keypress', (e) => {
    if (e.keyCode === 13) {
      const salutation = url + '?lang=' + $('INPUT#language_code').val();
      $.get(salutation, (data) => {
        $('DIV#hello').text(data.hello);
      });
    }
  });
});
