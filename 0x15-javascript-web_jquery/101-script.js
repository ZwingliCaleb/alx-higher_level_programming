//this script adds, removes and clears <li> elementsfrom a list when a user performs a series of clicks.

$(document).ready(function() {
  $('#add_item').click(function() {
    $('.my_list').append('<li>Item</li>');
  });

  $('#remove_item').click(function() {
    $('.my_list li:last-child').remove();
  });

  $('#clear_list').click(function() {
    $('.my_list').empty();
  });
});

