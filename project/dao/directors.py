from project.dao.base import BaseDAO
from .models import Director


class DirectorsDAO(BaseDAO[Director]):
    """
    DAO режиссера, наследует базовый DAO
    """
    __model__ = Director
