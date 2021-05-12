document.addEventListener('DOMContentLoaded', () => {
  const url = 'https://www.fourtonfish.com/hellosalut/';

  $('INPUT#btn_translate').on('click', () => {
    const salutation = url + '?lang=' + $('INPUT#language_code').val();
    $.get(salutation, (data) => {
      $('DIV#hello').text(data.hello);
    });
  });
});
