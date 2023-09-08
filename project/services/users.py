import base64
import hashlib
import hmac

from flask import current_app, abort

from project.services.base import BaseService


class UsersService(BaseService):
    """ Сервис пользователя наследует базовый сервис"""

    @property
    def hash_salt(self):
        return current_app.config['PWD_HASH_SALT']

    @property
    def hash_iterations(self):
        return current_app.config['PWD_HASH_ITERATIONS']

    def get_email(self, email):
        """
        Возвращает данные пользователя по email
        """

        return self.dao.get_email(email)

    def create(self, data):
        """
        Метод создания пользователя
        """

        data['password'] = self.get_hash(data['password'])
        self.dao.create(data)

    def update_user_info(self, data, email):
        """
        Метод изменения информации пользователя
        """

        self.get_email(email)
        if 'password' not in data.keys() and 'email' not in data.keys():
            self.dao.update_info(data, email)
        else:
            abort(405)

    def update_password(self, passwords, email):
        """
        Метод обновления пароля пользователя по email
        """
        user = self.get_email(email)
        old_pass = passwords.get('old_password', None)
        new_pass = passwords.get('new_password', None)
        if None not in [old_pass, new_pass] and self.compare_passwords(user.password, old_pass):
            self.dao.update_info({'password': self.get_hash(new_pass)}, email)

    def get_hash(self, password):
        """
        Метод хэширования пароля
        """

        return base64.b64encode(hashlib.pbkdf2_hmac(
            'sha256',
            password.encode('utf-8'),  # Convert the password to bytes
            self.hash_salt,
            self.hash_iterations
        ))

    def compare_passwords(self, pass_hash, other_pass):
        """
        Метод проверки хэшированных паролей на совпадение
        """

        decoded_digest = base64.b64decode(pass_hash)

        hash_digest = hashlib.pbkdf2_hmac(
            'sha256',
            other_pass.encode('utf-8'),  # Convert the password to bytes
            self.hash_salt,
            self.hash_iterations
        )
        return hmac.compare_digest(decoded_digest, hash_digest)
