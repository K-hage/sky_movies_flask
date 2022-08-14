from project.config import config
from project.dao.models import Genre, Director, Movie, User
from project.server import create_app, db

app = create_app(config)


@app.shell_context_processor
def shell():
    return {
        "db": db,
        "Genre": Genre,
        "Director": Director,
        "Movie": Movie,
        'User': User
    }


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000)
