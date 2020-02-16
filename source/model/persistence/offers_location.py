# coding=utf-8

from sqlalchemy import Column, String, Integer, Boolean

from base import Base


class OffersLocation(Base):
    __tablename__ = 'offers_locations'

    id = Column(Integer, primary_key=True)
    code = Column(String)

    def __init__(self, code):
       self.code = code