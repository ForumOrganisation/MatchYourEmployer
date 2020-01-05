import unittest
from source.algo import MatchMaker, DistanceEvaluator
from source.model import Student, Company, MatchingParameters


class SimpleTest(unittest.TestCase):
    def test_run(self):
        number_student = 5
        number_company = 5
        students = [Student() for _ in range(number_student)]
        company = [Company() for _ in range(number_company)]
        main_computer = MatchMaker(students, company)

        parameters = MatchingParameters(0.0, DistanceEvaluator, 2, 2)

        matching = main_computer.compute_matching(parameters)
        print("\n".join(map(str, matching.links)))


if __name__ == '__main__':
    unittest.main()
