import unittest
from source.algo import Scorer
from source.model.persistence import Student, Company, MainDomain, SubDomain

class SimpleTest(unittest.TestCase):
    def test_run(self):

        wavestone = Company('Wavestone', 'ETI', 'W', 45, True, True, False, '56')

        # 5 - creates students
        kenza = Student('Kenza', 'BOUZID', 4, 'kenza.bouzid@insa-lyon.fr', 'INSA Lyon', '4', 'Stage', 'ETI', 'Marocaine')

        # 6 - creates main and sub domains
        conseil = MainDomain('Etude et Conseil')
        info = MainDomain('Informatique')
        tc = MainDomain('Telecommunication')
        sousDomain = SubDomain('Conseil en nouvelles technologies')

        # 7 - add main domains to companies and students
        conseil.sub_domains = [sousDomain]
        wavestone.main_domains = [conseil, info, tc]
        kenza.main_domain = [info]

        scorer = Scorer(kenza, wavestone)

        scorer.computeScore()

        print(scorer.Score)

if __name__ == '__main__':
    unittest.main()
