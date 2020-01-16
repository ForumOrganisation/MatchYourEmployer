# coding=utf-8

from sqlalchemy import Column, String, Integer

from base import Base


class mainDomain(Base):
    __tablename__ = 'mainDomains'

    id = Column(Integer, primary_key=True)
    name = Column(String)

    def __init__(self, name):
        self.name = name
