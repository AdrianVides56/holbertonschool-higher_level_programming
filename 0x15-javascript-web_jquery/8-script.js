const url = 'https://swapi-api.hbtn.io/api/films/?format=json';

$.get(url, (data) => {
  for (let movie = 0; movie < data.results.length; movie++) {
    $('UL#list_movies').append('<li>' + data.results[movie].title + '</li>');
  }
});
