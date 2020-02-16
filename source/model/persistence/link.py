from sqlalchemy import Column, String, Integer

from base import Base


class Link(Base):
    __tablename__ = 'links'

    id = Column(Integer, primary_key=True)
    student = Column(String)
    company = Column(String)
    strength = Column(String)

    def __init__(self, student, company, strength):
        self.student = student
        self.company = company
        self.strength = strength
