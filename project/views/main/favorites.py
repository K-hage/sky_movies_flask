from flask import request
from flask_restx import Namespace, Resource

from project.container import favorite_service, auth_service, user_service, movie_schema
from project.tools.decorators import auth_required

api = Namespace('favorites')


@api.route('/movies/')
class FavoritesView(Resource):
    """ CBV избранных фильмов """

    @auth_required
    def get(self):
        """
        Возвращает все избранные фильмы зарегистрированного пользователя
        """

        token = request.headers['Authorization'].split("Bearer ")[-1]
        data = auth_service.decode_token(token)

        user = user_service.get_email(data.get('email'))
        user_id = user.id

        favorites = favorite_service.get_user_favorites(user_id)
        return movie_schema.dump(favorites, many=True), 200


@api.route('/movies/<int:movie_id>/')
class FavoritesMoviesView(Resource):
    """
    CBV избранное
    """

    @auth_required
    def post(self, movie_id):
        """
        Добавить фильм в избранное
        """

        token = request.headers['Authorization'].split("Bearer ")[-1]
        data = auth_service.decode_token(token)
        user = user_service.get_email(data.get('email'))
        favorite_service.create(user.id, movie_id)

        return '', 204

    @auth_required
    def delete(self, movie_id):
        """
        Удалить фильм из избранного
        """

        token = request.headers['Authorization'].split("Bearer ")[-1]
        data = auth_service.decode_token(token)
        user = user_service.get_email(data.get('email'))
        favorite_service.delete(user.id, movie_id)

        return '', 204
