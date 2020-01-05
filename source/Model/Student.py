import numpy.random as rd


class Student:
    def __init__(self):
        self.id_student = rd.randint(pow(10, 9))  # TODO pick a better id
