# coding=utf-8

# 1 - imports
from company import Company
from student import Student
from base import Session

# 2 - extract a session
session = Session()

# 3 - extract all companies and students
companies = session.query(Company).all()
students = session.query(Student).all()

# 4 - print movies' details

print('### Recent companies:')
for company in companies:
    print(f'{company.name} of size {company.size}')
print('')


print('### Recent students:')
for student in students:
    print(f'{student.first_name}  {student.last_name}')
print('')