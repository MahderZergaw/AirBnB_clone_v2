#!/usr/bin/python3
""" City Module for HBNB project """
import models
from models.base_model import BaseModel, Base
import sqlalchemy
from sqlalchemy import Column, String
import os
from sqlalchemy.orm import relationship
from sqlalchemy import ForeignKey


class City(BaseModel):
    """ The city class, contains state ID and name """
    if os.getenv("HBNB_TYPE_STORAGE") == "db":
        _tablename_ = "cities"
        state_id = Column(String(128), nullable=False)
        name = Column(String(60), ForeignKey("states.id"),
                      nullable=False)
        places = relationship("Place", backref="cities",
                              cascade="all, delete-orphan")
    else:
        name = ""
        state_id = ""

    def _init_(self, *args, **kwargs):
        "initializing city class"
        super()._init_(*args, **kwargs)
