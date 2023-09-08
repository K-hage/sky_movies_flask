from marshmallow import Schema, fields


class FavoriteSchema(Schema):
    """ Схема для сериализации режиссеров """

    id = fields.Int(dump_only=True)
    user_id = fields.Nested('UserSchema')
    movie_id = fields.Nested('MovieSchema')
