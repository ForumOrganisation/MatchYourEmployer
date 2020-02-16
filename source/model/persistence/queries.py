# coding=utf-8

# 1 - imports
from company import Company
from student import Student
from base import Session

# 2 - extract a session
session = Session()

# 3 - extract all movies
companies = session.query(Company).all()
students = session.query(Student).all()

# 4 - print movies' details
print(companies)
print('\n')
print(students)