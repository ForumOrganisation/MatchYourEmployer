# coding=utf-8

from sqlalchemy import Column, String, Integer, Boolean, CHAR, ForeignKey, Table
from sqlalchemy.orm import relationship

from base import Base

companies_mainDomains_association = Table(
    'companies_mainDomains', Base.metadata,
    Column('companie_id', Integer, ForeignKey('companies.id')),
    Column('mainDomain_id', Integer, ForeignKey('mainDomains.id'))
)

class Company(Base):
    __tablename__ = 'companies'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    size = Column(String)
    presenceDay = Column(CHAR)
    wantedDegrees = Column(Integer)
    co_opStudent = Column(Boolean)
    cdi = Column(Boolean)
    nationalityDisc = Column(Boolean)
    offerLength = Column(Integer)
    pfePeriod = Column(Integer)
    criteriaOrdering = Column(Integer)
    mainDomains = relationship("MainDomain", secondary=companies_mainDomains_association)

    def __init__(self, name, size, presenceDay, wantedDegrees, co_opStudent,
                 cdi, nationalityDisc, offerLength, pfePeriod, criteriaOrdering):
        self.name = name
        self.size = size
        self.presenceDay = presenceDay
        self.wantedDegrees = wantedDegrees
        self.co_opStudent = co_opStudent
        self.cdi = cdi
        self.nationalityDisc = nationalityDisc
        self.offerLength = offerLength
        self.pfePeriod = pfePeriod
        self.criteriaOrdering = criteriaOrdering
