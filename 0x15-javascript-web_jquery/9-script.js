// This is a script that fetches from  a url and displays the value of hello from that fetch in the html tag DIV#hello

$(() => {
	$.get('https://fourtonfish.com/hellosalut/?lang=fr', (data, textStatus) => {
		if (textStatus === 'success'){
			$('div#hello').text(data.hello);
		}
	});
});
