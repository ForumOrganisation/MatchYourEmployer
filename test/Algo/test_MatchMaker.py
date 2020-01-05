import unittest
from source.Algo import MatchMaker, DistanceEvaluator
from source.Model import Student, Company, MatchingParameters


class SimpleTest(unittest.TestCase):
    def test_run(self):
        number_student = 5
        number_company = 5
        students = [Student() for _ in range(number_student)]
        company = [Company() for _ in range(number_company)]
        main_computer = MatchMaker(students, company)

        parameters = MatchingParameters(1.0, DistanceEvaluator, 2, 2)

        matching = main_computer.compute_matching(parameters)
        print(matching)


if __name__ == '__main__':
    unittest.main()
