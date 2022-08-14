from marshmallow import Schema, fields


class UserSchema(Schema):
    """ Модель пользователя """

    __tablename__ = 'user'

    id = fields.Int(dump_only=True)
    email = fields.Str()
    name = fields.Str()
    surname = fields.Str()
    favorite_genre = fields.Int()  # берем данные из жанров
