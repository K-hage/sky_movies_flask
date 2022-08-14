from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship

from project.setup.db import models


class User(models.Base):
    """ Модель пользователя """

    __tablename__ = 'users'

    email = Column(String(255), nullable=False, unique=True)
    password = Column(String(255), nullable=False)
    name = Column(String(255))
    surname = Column(String(255))
    favorite_genre = Column(Integer, ForeignKey("genres.id"))
    genre = relationship("Genre")
