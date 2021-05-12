$('#add_item').on('click', () => {
  const newLi = '<li>Item</li>';
  $('UL.my_list').append(newLi);
});
