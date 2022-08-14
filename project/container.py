from project.dao import GenresDAO, DirectorsDAO, MoviesDAO, UsersDAO, FavoritesDAO
from project.dao.schema import GenreSchema, DirectorSchema, MovieSchema, UserSchema

from project.services import GenresService, DirectorsService, MoviesService, UsersService, AuthService, FavoritesService
from project.setup.db import db

# DAO
genre_dao = GenresDAO(db.session)  # жанров
director_dao = DirectorsDAO(db.session)  # режиссеров
movie_dao = MoviesDAO(db.session)  # фильмов
user_dao = UsersDAO(db.session)  # пользователей
favorite_dao = FavoritesDAO(db.session)  # избранного

# Services
genre_service = GenresService(dao=genre_dao)  # жанров
director_service = DirectorsService(dao=director_dao)  # режиссеров
movie_service = MoviesService(dao=movie_dao)  # фильмов
user_service = UsersService(dao=user_dao)  # пользователей
auth_service = AuthService(user_service=user_service)  # аутентификации
favorite_service = FavoritesService(dao=favorite_dao)  # избранного

# Schema
genre_schema = GenreSchema()  # жанров
director_schema = DirectorSchema()  # режиссеров
movie_schema = MovieSchema()  # фильмов
user_schema = UserSchema()  # пользователей
