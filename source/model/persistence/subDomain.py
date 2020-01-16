# coding=utf-8

from sqlalchemy import Column, String, Integer, Boolean, CHAR, ForeignKey, Table
from sqlalchemy.orm import relationship

from base import Base

mainDomains_subnDomains_association = Table(
    'mainDomains_subDomains', Base.metadata,
    Column('companie_id', Integer, ForeignKey('companies.id')),
    Column('mainDomain_id', Integer, ForeignKey('mainDomains.id'))
)

class subDomain(Base):
    __tablename__ = 'mainDomains'

    id = Column(Integer, primary_key=True)
    name = Column(String)

    def __init__(self, name):
        self.name = name
