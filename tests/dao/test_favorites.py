import pytest

from project.dao import FavoritesDAO
from project.dao.models import Favorite, Movie, Director


class TestFavoritesDAO:

    @pytest.fixture
    def favorites_dao(self, db):
        return FavoritesDAO(db.session)

    @pytest.fixture
    def movie_1(self, db):
        movie = Movie(
            id=1,
            title="TestMovie1",
            description="test",
            trailer="test",
            year=1999,
            rating=8.0,
            genre_id=1,
            director_id=2
        )
        db.session.add(movie)
        db.session.commit()
        return movie

    @pytest.fixture
    def movie_2(self, db):
        movie = Movie(
            id=2,
            title="TestMovie2",
            description="test",
            trailer="test",
            year=1999,
            rating=8.0,
            genre_id=1,
            director_id=2
        )
        db.session.add(movie)
        db.session.commit()
        return movie

    @pytest.fixture
    def favorite_1(self, db):
        director = Favorite(id=1, user_id=1, movie_id=1)
        db.session.add(director)
        db.session.commit()
        return director

    @pytest.fixture
    def favorite_2(self, db):
        director = Favorite(id=2, user_id=1, movie_id=2)
        db.session.add(director)
        db.session.commit()
        return director

    def test_get_director_by_id(self, favorite_1, favorites_dao):
        assert favorites_dao.get_by_id(favorite_1.id) == favorite_1

    @pytest.mark.skip
    def test_get_director_by_id_not_found(self, favorites_dao):
        assert not favorites_dao.get_by_id(1)

    def test_get_all_directors(self, favorites_dao, favorite_1, favorite_2):
        assert favorites_dao.get_all() == [favorite_1, favorite_2]

    def test_get_directors_by_page(self, app, favorites_dao, favorite_1, favorite_2):
        app.config['ITEMS_PER_PAGE'] = 1
        assert favorites_dao.get_all(page=1) == [favorite_1]
        assert favorites_dao.get_all(page=2) == [favorite_2]
        assert favorites_dao.get_all(page=3) == []

    def test_get_user_favorites(self, favorites_dao, favorite_1, favorite_2, movie_1, movie_2):
        favorites = favorites_dao.get_user_favorites(1)
        assert len(favorites) == 2
        assert favorites == [movie_1, movie_2]

    def test_get_favorites(self, favorites_dao, favorite_1, movie_1):
        favorite = favorites_dao.get_favorite(1, 1)
        assert favorite == favorite_1
