from sqlalchemy import Column, Integer, ForeignKey, Table
from sqlalchemy.orm import relationship

from project.setup.db import models


class Favorite(models.Base):
    """ Модель избранное """

    __tablename__ = 'favorites'

    user_id = Column(Integer, ForeignKey("users.id"))
    user = relationship("User")
    movie_id = Column(Integer, ForeignKey("movies.id"))
    movie = relationship("Movie")
