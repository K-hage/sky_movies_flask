from typing import Optional


from project.dao.models import Movie
from project.services.base import BaseService


class MoviesService(BaseService):

    def get_all(self, page: Optional[int] = None, status: Optional[int] = None) -> list[Movie]:
        """
        Возвращает список фильмов из базы данных
        Параметры:
        status - сортировка фильмов по году выпуска
        page - выдает указанную страницу с определенным в config количеством элементов
        """

        return self.dao.get_all(page=page, status=status)
