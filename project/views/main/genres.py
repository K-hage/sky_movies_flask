from flask_restx import Namespace, Resource

from project.container import genre_service, genre_schema
from project.setup.api.parsers import page_parser

api = Namespace('genres')


@api.route('/')
class GenresView(Resource):
    """
    CBV жанров
    """

    @api.doc(decriptions="Все жанры")
    @api.expect(page_parser)
    def get(self):
        """
        Все жанры
        """

        genres = genre_service.get_all(**page_parser.parse_args())
        return genre_schema.dump(genres, many=True), 200


@api.route('/<genre_id>/')
class GenreView(Resource):
    """
    CBV жанра
    """

    @api.doc(decriptions="Жанр по id")
    @api.response(404, 'Not Found')
    def get(self, genre_id: int):
        """
        Жанр по id
        """

        genre = genre_service.get_item(genre_id)
        return genre_schema.dump(genre), 200
