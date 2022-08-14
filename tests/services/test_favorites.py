from unittest.mock import patch

import pytest

from project.dao.models import Favorite, Movie
from project.exceptions import ItemNotFound
from project.services import FavoritesService


class TestFavoritesService:

    @pytest.fixture()
    @patch('project.dao.FavoritesDAO')
    def favorites_dao_mock(self, dao_mock):
        dao = dao_mock()
        dao.get_by_id.return_value = Favorite(
            id=1,
            user_id=1,
            movie_id=1
        )
        dao.get_all.return_value = [
            Favorite(
                id=1,
                user_id=1,
                movie_id=1
            ),
            Favorite(
                id=2,
                user_id=1,
                movie_id=2
            ),
        ]
        dao.create.return_value = Favorite(
            id=1,
            user_id=1,
            movie_id=1
        )
        dao.get_user_favorites.return_value = [
            Favorite(
                id=1,
                user_id=1,
                movie_id=1
            ),
            Favorite(
                id=2,
                user_id=1,
                movie_id=2
            ),
        ]
        return dao

    @pytest.fixture()
    def favorites_service(self, favorites_dao_mock):
        return FavoritesService(dao=favorites_dao_mock)

    @pytest.fixture
    def favorite(self, db):
        obj = Favorite(id=1,
                       user_id=1,
                       movie_id=1)
        db.session.add(obj)
        db.session.commit()
        return obj

    @pytest.fixture
    def movie(self, db):
        obj = Movie(
            id=1,
            title="TestMovie1",
            description="test",
            trailer="test",
            year=1999,
            rating=8.0,
            genre_id=1,
            director_id=2
        )
        db.session.add(obj)
        db.session.commit()
        return obj

    @pytest.fixture
    def favorite_dict(self):
        favorite = {
            'user_id': 3,
            'movie_id': 3
        }
        return favorite

    def test_get_favorite(self, favorites_service, favorite):
        assert favorites_service.get_item(favorite.id)

    @pytest.mark.skip
    def test_favorite_not_found(self, favorites_dao_mock, favorites_service):
        favorites_dao_mock.get_by_id.return_value = None

        with pytest.raises(ItemNotFound):
            favorites_service.get_item(10)

    @pytest.mark.parametrize('page', [1, None], ids=['with page', 'without page'])
    def test_get_favorites(self, favorites_dao_mock, favorites_service, page):
        favorites = favorites_service.get_all(page=page)
        assert len(favorites) == 2
        assert favorites == favorites_dao_mock.get_all.return_value
        favorites_dao_mock.get_all.assert_called_with(page=page)

    def test_create(self, favorites_dao_mock, favorites_service, movie):
        favorite = favorites_service.create(1, 1)
        assert favorite.id is not None
        assert favorite.user_id == 1
        assert favorite.movie_id == movie.id

    def test_get_user_favorites(self, favorites_dao_mock, favorites_service):
        favorites = favorites_service.get_user_favorites(1)
        assert len(favorites) == 2
        assert favorites == favorites_dao_mock.get_user_favorites.return_value
