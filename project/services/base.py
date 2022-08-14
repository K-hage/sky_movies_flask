from typing import Optional


class BaseService:
    """
    Сервис базовый
    """

    def __init__(self, dao) -> None:
        self.dao = dao

    def get_item(self, pk: int):
        """
        Возвращает данные по id
        """

        return self.dao.get_by_id(pk)

    def get_all(self, page: Optional[int] = None) -> list:
        """
        Возвращает список из базы данных
        Параметры:
        page - выдает указанную страницу с определенным в config количеством элементов
        """

        return self.dao.get_all(page=page)
