//This script toggles classes when a toggle tag is clicked
//

$(document).ready(function() {
  $('#toggle_header').click(function() {
    $('header').toggleClass('red green');
  });
});

