from flask_restx.reqparse import RequestParser

# Парсер аргумента страницы page
page_parser: RequestParser = RequestParser()
page_parser.add_argument(
    name='page',
    type=int,
    location='args',
    required=False,
    help='Выберите страницу'
)

# Парсер аргумента status для сортировки фильмов
status_parser: RequestParser = RequestParser()
status_parser.add_argument(
    name='status',
    type=str,
    location='args',
    required=False,
    help='При указание в поле "new" выведет свежие фильмы по году'
)
