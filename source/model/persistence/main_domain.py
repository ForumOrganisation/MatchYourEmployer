# coding=utf-8

from sqlalchemy import Column, String, Integer, ForeignKey, Table
from sqlalchemy.orm import relationship

from base import Base

main_domains_sub_domains_association = Table(
    'main_domains_sub_domains', Base.metadata,
    Column('main_domain_id', Integer, ForeignKey('main_domains.id')),
    Column('sub_domain_id', Integer, ForeignKey('sub_domains.id'))
)


class MainDomain(Base):
    __tablename__ = 'main_domains'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    sub_domains = relationship("SubDomain", secondary=main_domains_sub_domains_association)

    def __init__(self, name):
        self.name = name
