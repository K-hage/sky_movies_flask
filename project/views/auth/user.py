from flask import request
from flask_restx import Namespace, Resource

from project.container import user_service, auth_service, user_schema
from project.tools.decorators import auth_required

api = Namespace('user')


@api.route('/')
class RegisterView(Resource):
    """
    CBV регистрации
    """

    @auth_required
    def get(self):
        """
        Возвращает информацию пользователя(профиль)
        """

        token = request.headers['Authorization'].split("Bearer ")[-1]
        data = auth_service.decode_token(token)
        email = data.get('email')
        user = user_service.get_email(email)
        return user_schema.dump(user), 200

    @api.response(204, 'Created')
    @auth_required
    def patch(self):
        """
        Изменить информацию пользователя (имя, фамилия, любимый жанр)
        """

        json_req = request.json
        token = request.headers['Authorization'].split("Bearer ")[-1]
        data = auth_service.decode_token(token)
        email = data.get('email')
        try:
            user_service.check_is_dict(json_req)
            user_service.update_user_info(json_req, email)
        except TypeError as e:
            return str(e), 400

        return '', 204


@api.route('/password/')
class PasswordViews(Resource):
    """
    CBV обновления пароля пользователя
    """

    @api.response(204, 'Created')
    @auth_required
    def put(self):
        """
        Обновляет пароль пользователя
        """

        json_req = request.json
        token = request.headers['Authorization'].split("Bearer ")[-1]
        data = auth_service.decode_token(token)
        email = data.get('email')
        try:
            user_service.check_is_dict(json_req)
            user_service.update_password(json_req, email)
        except TypeError as e:
            return str(e), 400

        return '', 204
