# coding=utf-8

from sqlalchemy import Column, String, Integer, Boolean, CHAR, ForeignKey, Table
from sqlalchemy.orm import relationship
from main_domain import MainDomain
from offers_location import OffersLocation

from base import Base

companies_main_domains_association = Table(
    'companies_mainDomains', Base.metadata,
    Column('company_id', Integer, ForeignKey('companies.id')),
    Column('main_domain_id', Integer, ForeignKey('main_domains.id'))
)

companies_offers_locations_association = Table(
    'companies _offers_locations', Base.metadata,
    Column('company_id', Integer, ForeignKey('companies.id')),
    Column('offers_locations_id', Integer, ForeignKey('offers_locations.id'))
)


class Company(Base):
    __tablename__ = 'companies'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    size = Column(String)
    presence_day = Column(CHAR)
    wanted_degrees = Column(Integer)
    co_op_student = Column(Boolean)
    cdi = Column(Boolean)
    nationality_disc = Column(Boolean)
    offer_length = Column(Integer)
    main_domains = relationship("MainDomain", secondary=companies_main_domains_association)
    offers_locations = relationship("OffersLocation", secondary=companies_offers_locations_association)

    def __init__(self, name, size, presence_day, wanted_degrees, co_op_student,
                 cdi, nationality_disc, offer_length):
        self.name = name
        self.size = size
        self.presence_day = presence_day
        self.wanted_degrees = wanted_degrees
        self.co_op_student = co_op_student
        self.cdi = cdi
        self.nationality_disc = nationality_disc
        self.offer_length = offer_length
