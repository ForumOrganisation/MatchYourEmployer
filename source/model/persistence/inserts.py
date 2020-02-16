# 1 - imports

from base import Session, engine, Base
from company import Company
from link import Link
from main_domain import MainDomain
from offers_location import OffersLocation
from student import Student
from sub_domain import SubDomain


# 2 - generate database schema
Base.metadata.create_all(engine)

# 3 - create a new session
session = Session()

# 4 - create companies
wavestone = Company('Wavestone', 'ETI', 'W', 45, True, True, False, int('110000', 2))

# 5 - creates students
kenza = Student('Kenza', 'BOUZID', 'kenza.bouzid@insa-lyon.fr', 'INSA Lyon', int('001000', 2), 'Stage', 'ETI', 'Marocaine')

# 6 - creates main and sub domains
conseil = MainDomain('Etude et Conseil')
sousDomain = SubDomain('Conseil en nouvelles technologies')

# 7 - add main domains to companies and students
conseil.sub_domains = [sousDomain]
wavestone.main_domains = [conseil]
kenza.main_domain = [conseil]

# 9 - persists data
session.add(wavestone)
session.add(kenza)

# 10 - commit and close session
session.commit()
session.close()