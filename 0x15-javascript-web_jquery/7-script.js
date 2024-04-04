//using jQuery API

var url = 'https://swapi.co/api/people/5/?format=json';
$.get(url, function(data, stat) {
  $div#character').text(data.name);
});
