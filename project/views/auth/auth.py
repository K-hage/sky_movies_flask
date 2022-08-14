from flask import request
from flask_restx import Namespace, Resource

from project.container import user_service, auth_service, user_schema

api = Namespace('auth')


@api.route('/register/')
class RegisterView(Resource):
    """
    CBV регистрации
    """

    @api.doc(description='Регистрация пользователя')
    def post(self):
        """
        Создает нового пользователя по email и паролю
        """

        json_req = request.json
        try:
            user = user_service.create(json_req)
        except TypeError as e:
            return str(e), 400
        return user_schema.dump(user), 200


@api.route('/login/')
@api.doc(description='Аутентификация')
class LoginView(Resource):
    """
    CBV аутентификации
    """

    @api.doc(description='Получение токенов')
    @api.response(400, 'Bad Request')
    def post(self):
        """
        Получение токенов пользователя по email
        """

        new_user_json = request.json

        email = new_user_json.get('email', None)
        password = new_user_json.get('password', None)

        if None in [email, password]:
            return 'Bad Request', 400

        tokens = auth_service.generate_tokens(email, password)

        return tokens, 200

    @api.doc(description='Обновление токенов')
    def put(self):
        """
        Обновление токенов пользователя
        """

        data = request.json
        token = data.get('refresh_token')

        tokens = auth_service.approve_refresh_token(token)
        return tokens, 200
