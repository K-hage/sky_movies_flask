from project.dao.base import BaseDAO
from .models import Genre


class GenresDAO(BaseDAO[Genre]):
    """
    DAO жанров, наследует базовый DAO
    """
    __model__ = Genre
