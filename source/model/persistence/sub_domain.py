# coding=utf-8

from sqlalchemy import Column, String, Integer

from base import Base


class sub_domain(Base):
    __tablename__ = 'main_domains'

    id = Column(Integer, primary_key=True)
    name = Column(String)

    def __init__(self, name):
        self.name = name
