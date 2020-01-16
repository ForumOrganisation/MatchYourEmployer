# coding=utf-8

from sqlalchemy import Column, String, Integer, Boolean

from base import Base


class offers_location(Base):
    __tablename__ = 'offers_locations'

    id = Column(Integer, primary_key=True)
    city = Column(String)
    country = Column(String)
    in_out = Column(Boolean)

    def __init__(self, city, country, in_out):
        self.city = city
        self.country = country
        self.in_out = in_out
