from flask_restx import Api


# Создаем api по адресу root/docs
api = Api(
    title="Flask Course Project 4",
    doc="/docs",
)
