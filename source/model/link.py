class Link:
    def __init__(self, student, company, strength):
        self.student = student
        self.company = company
        self.strength = strength

    def __str__(self):
        return str(self.student) + " - " + str(self.company)
