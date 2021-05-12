document.addEventListener('DOMContentLoaded', () => {
  const newElement = '<li>Item</li>';
  $('DIV#add_item').on('click', () => {
    $('UL.my_list').append(newElement);
  });
  $('DIV#remove_item').on('click', () => {
    $('UL.my_list li').last().remove();
  });
  $('DIV#clear_list').on('click', () => {
    $('UL.my_list').empty();
  });
});
