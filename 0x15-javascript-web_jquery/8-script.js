//using jQuery API

var url = 'https://swapi.co/api/films/?format=json';
$.get(url, function (data) {
	var films = data.results;
	for (var film of films) {
		$('ul#list_movies').append(`<li>${film.title}</li>`);
	}
});
