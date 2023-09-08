from project.exceptions import ItemNotFound
from project.services.base import BaseService


class FavoritesService(BaseService):

    def create(self, user_id, movie_id):
        """
        Создаем данные избранного пользователем фильма
        """

        data = {
            'user_id': user_id,
            'movie_id': movie_id
        }
        return self.dao.create(data)

    def get_user_favorites(self, user_id):
        """
        Получаем все избранные фильмы пользователя по id
        """

        favourites = self.dao.get_user_favorites(user_id)

        if not favourites:
            raise ItemNotFound('Not Found')

        return favourites

    def delete(self, user_id, movie_id):
        """
        Удаляем из избранного пользователя фильм
        """

        data = self.dao.get_favorite(user_id, movie_id)
        self.dao.delete(data.id)
