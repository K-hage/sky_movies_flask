import pytest

from project.dao.models import Movie, Genre, Director


class TestMoviesView:

    @pytest.fixture
    def director(self, db):
        obj = Director(id=1, name="director")
        db.session.add(obj)
        db.session.commit()
        return obj

    @pytest.fixture
    def genre(self, db):
        obj = Genre(id=1, name="genre")
        db.session.add(obj)
        db.session.commit()
        return obj

    @pytest.fixture
    def movie(self, db):
        obj = Movie(
            title="TestMovie1",
            description="test",
            trailer="test",
            year=1999,
            rating=8.0,
            genre_id=1,
            director_id=1
        )
        db.session.add(obj)
        db.session.commit()
        return obj

    def test_many(self, client, director, genre, movie):
        response = client.get("/movies/")
        assert response.status_code == 200
        assert response.json == [
            {"id": movie.id,
             'title': movie.title,
             'description': movie.description,
             'trailer': movie.trailer,
             'year': movie.year,
             'rating': movie.rating,
             'genre': {'id': 1, 'name': 'genre'},
             'director': {'id': 1, 'name': 'director'}
             }
        ]

    def test_movie_pages(self, client, movie):
        response = client.get("/movies/?page=1")
        assert response.status_code == 200
        assert len(response.json) == 1

        response = client.get("/movies/?page=2")
        assert response.status_code == 200
        assert len(response.json) == 0

    def test_movie(self, client, director, genre, movie):
        response = client.get("/movies/1/")
        assert response.status_code == 200
        assert response.json == {"id": movie.id,
                                 'title': movie.title,
                                 'description': movie.description,
                                 'trailer': movie.trailer,
                                 'year': movie.year,
                                 'rating': movie.rating,
                                 'genre': {'id': 1, 'name': 'genre'},
                                 'director': {'id': 1, 'name': 'director'}
                                 }

    def test_movie_not_found(self, client, movie):
        response = client.get("/movies/2/")
        assert response.status_code == 404
