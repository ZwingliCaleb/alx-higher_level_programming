//Javascript script to fetch and print how to say hello depending on the language

$(document).ready(function() {
  $('#btn_translate').click(fetchTranslation);
  $('#language_code').keypress(function(event) {
    if (event.which === 13) {
      fetchTranslation();
    }
  });

  function fetchTranslation() {
    const languageCode = $('#language_code').val();
    const url = `https://www.fourtonfish.com/hellosalut/hello/${languageCode}`;

    $.getJSON(url, function(data) {
      $('#hello').text(data.hello);
    });
  }
});

