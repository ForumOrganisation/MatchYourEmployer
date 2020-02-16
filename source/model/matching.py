from collections import defaultdict
class Matching:
    def __init__(self, students, companies, parameters, links):
        self.students = students
        self.companies = companies
        self.parameters = parameters
        self.links = links
    def get_map_links(self):
        res_map = defaultdict(set)
        for link in self.links:
            id_student = link.student.id_student
            id_company = link.company.id_company
            res_map[id_student].add(id_company)
            res_map[id_company].add(id_student)
        return res_map