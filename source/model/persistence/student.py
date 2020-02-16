# coding=utf-8

from sqlalchemy import Column, String, Integer, ForeignKey, Table
from sqlalchemy.orm import relationship
from main_domain import MainDomain
from offers_location import OffersLocation

from base import Base

students_offers_locations_association = Table(
    'students _offers_locations', Base.metadata,
    Column('student_id', Integer, ForeignKey('students.id')),
    Column('offers_locations_id', Integer, ForeignKey('offers_locations.id'))
)

students_main_domains_association = Table(
    'students_main_domains', Base.metadata,
    Column('student_id', Integer, ForeignKey('students.id')),
    Column('main_domain_id', Integer, ForeignKey('main_domains.id'))
)


class Student(Base):
    __tablename__ = 'students'

    id = Column(Integer, primary_key=True)
    first_name = Column(String)
    last_name = Column(String)
    email = Column(String)
    school = Column(String)
    email = Column(String)
    offer_length = Column(Integer)
    contract_type = Column(String)
    company_size = Column(String)
    nationality = Column(String)
    geo_mobility = relationship("OffersLocation", secondary=students_offers_locations_association)
    main_domains = relationship("MainDomain", secondary=students_main_domains_association)

    def __init__(self, first_name, last_name, email, school, offer_length, contract_type,
                 company_size, nationality):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.school = school
        self.offer_length = offer_length
        self.contract_type = contract_type
        self.company_size = company_size
        self.nationality = nationality

