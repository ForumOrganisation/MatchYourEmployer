import numpy.random as rd


class Company:
    def __init__(self):
        self.id_company = rd.randint(pow(10, 9))  # TODO pick a better id
