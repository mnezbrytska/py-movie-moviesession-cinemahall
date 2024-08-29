from typing import Optional

from django.db.models import QuerySet

from db.models import Movie


def get_movies(
        genres_ids: Optional[list[int]] = None,
        actors_ids: Optional[list[int]] = None
) -> QuerySet:
    movie = Movie.objects.all()
    if genres_ids:
        movie = movie.filter(genres__id__in=genres_ids)
    if actors_ids:
        movie = movie.filter(actors__id__in=actors_ids)
    return movie.distinct()


def get_movie_by_id(movie_id: int) -> Movie:
    return Movie.objects.get(pk=movie_id)


def create_movie(
        movie_title: str,
        movie_description: str,
        genres_ids: Optional[list[int]] = None,
        actors_ids: Optional[list[int]] = None
) -> Movie:
    new_film = Movie.objects.create(
        title=movie_title,
        description=movie_description
    )
    if genres_ids:
        new_film.genres.set(genres_ids)
    if actors_ids:
        new_film.actors.set(actors_ids)
    return new_film
