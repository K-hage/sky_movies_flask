from project.dao.base import BaseDAO
from .models import User


class UsersDAO(BaseDAO[User]):
    """
    DAO пользователя, наследует базовый DAO
    """
    __model__ = User

    def get_email(self, email):
        """
        Получение данных пользователя по email
        """
        return self._db_session.query(self.__model__). \
            filter(self.__model__.email == email). \
            first_or_404(description=f'Пользователь с email: {email} не найден.')

    def update_info(self, data, email):
        """
        Обновления данных пользователя по email
        """

        self._db_session.query(self.__model__).filter(self.__model__.email == email).update(data)
        self._db_session.commit()
