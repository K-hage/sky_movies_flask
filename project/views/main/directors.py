from flask_restx import Namespace, Resource

from project.container import director_service, director_schema
from project.setup.api.parsers import page_parser

api = Namespace('directors')


@api.route('/')
class DirectorsView(Resource):
    """
    CBV режиссеров
    """

    @api.doc(decriptions="Все режиссеры")
    @api.expect(page_parser)
    def get(self):
        """
        Все режиссеры
        """

        directors = director_service.get_all(**page_parser.parse_args())
        return director_schema.dump(directors, many=True), 200


@api.route('/<int:director_id>/')
class DirectorView(Resource):
    """
    CBV режиссера
    """

    @api.doc(decriptions="Режиссер по id")
    @api.response(404, 'Not Found')
    def get(self, director_id: int):
        """
        Режиссер по id.
        """

        director = director_service.get_item(director_id)
        return director_schema.dump(director), 200
