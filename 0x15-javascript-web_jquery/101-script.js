document.addEventListener('DOMContentLoaded', function () {
  const item = '<li>Item</li>';
  $('DIV#add_item').click(function () {
    $('UL.my_list').append(item);
  });
  $('DIV#remove_item').click(function () {
    $('UL.my_list>li:last-child').remove();
  });
  $('DIV#clear_list').click(function () {
    $('UL.my_list>li').remove();
  });
});
