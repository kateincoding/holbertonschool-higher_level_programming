$.get('https://swapi-api.hbtn.io/api/films/?format=json', function (data, textStatus) {
  if (textStatus === 'success') {
    for (const result of data.results) {
      $('UL#list_movies').append(`<li>${result.title}</li>`);
    }
  }
});
