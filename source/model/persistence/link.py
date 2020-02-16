from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship, backref

from base import Base


class Link(Base):
    __tablename__ = 'links'

    id = Column(Integer, primary_key=True)
    student_id = Column(Integer, ForeignKey('students.id'))
    Student = relationship("Student", backref=backref("links", uselist=False))
    company_id = Column(Integer, ForeignKey('companies.id'))
    company = relationship("Company", backref=backref("links", uselist=False))
    strength = Column(String)


    def __init__(self, student_id, company_id, strength):
        self.student_id = student_id
        self.company_id = company_id
        self.strength = strength
