import numpy.random as rd


class Student:

    student_id_count = 1  # static variable counting the number of students

    def __init__(self, diploma, school, centre_of_inter,
                 offer_length, department, geo_mobility,
                 nationality, presence_day, study_after_graduate):
        self.id_student = Student.student_id_count  # a student's ID takes the value of the instance count variable
        Student.student_id_count += 1
        self.diploma = diploma
        self.school = school
        self.centre_of_inter = centre_of_inter
        self.offer_length = offer_length
        self.department = department
        self.geo_mobility = geo_mobility # takes values fr, e, w for france, europe and world
        self.nationality = nationality
        self.presence_day = presence_day  # takes 3 values: w, t or b, for wednesday, thursday and both
        self.study_after_graduate = study_after_graduate  # boolean

    def __str__(self):
        return "Student " + str(self.id_student)
