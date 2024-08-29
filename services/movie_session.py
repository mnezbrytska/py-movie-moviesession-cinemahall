from typing import Optional

from django.db.models import QuerySet

from db.models import MovieSession


def create_movie_session(
        movie_show_time: str,
        cinema_hall_id: int,
        movie_id: int,
) -> MovieSession:
    return MovieSession.objects.create(
        show_time=movie_show_time,
        cinema_hall_id=cinema_hall_id,
        movie_id=movie_id
    )


def get_movies_sessions(session_date: Optional[str] = None) -> QuerySet:
    movie_session = MovieSession.objects.all()
    if session_date:
        movie_session = movie_session.filter(show_time__date=session_date)
    return movie_session


def get_movie_session_by_id(movie_id: int) -> MovieSession:
    return MovieSession.objects.get(pk=movie_id)


def update_movie_session(
        session_id: int,
        show_time: Optional[str] = None,
        movie_id: Optional[int] = None,
        cinema_hall_id: Optional[int] = None
) -> Optional[MovieSession]:
    update_session = {}
    if show_time:
        update_session["show_time"] = show_time
    if movie_id:
        update_session["movie_id"] = movie_id
    if cinema_hall_id:
        update_session["cinema_hall_id"] = cinema_hall_id
    if not update_session:
        return None
    movie_session = MovieSession.objects.get(id=session_id)
    for key, value in update_session.items():
        setattr(movie_session, key, value)
    movie_session.save()
    return movie_session


def delete_movie_session_by_id(session_id: int) -> None:
    get_movie_session_by_id(session_id).delete()
