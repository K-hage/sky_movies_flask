import jwt

from flask import request, abort, current_app


def auth_required(func):
    """ Аутентификация пользователя """

    def wrapper(*args, **kwargs):

        # проверка на присутствие авторизации в заголовке
        if 'Authorization' not in request.headers:
            abort(401)

        data = request.headers['Authorization']
        token = data.split("Bearer ")[-1]

        try:
            jwt.decode(token, current_app.config['JWT_SECRET'], algorithms=[current_app.config['JWT_ALGORITHM']])
        except Exception as e:
            print("JWT Decode Exception", e)
            abort(401)
        return func(*args, **kwargs)

    return wrapper
