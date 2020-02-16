from model.persistence import Company, Student

class Scorer:
    def __init__(self, student: Student, company: Company):
        self.student = student
        self.company = company
        self.score = 0

    def computeScore(self):
        for domain in self.student.main_domains:
            if domain in self.company:
                self.score+=1
                break
        
        if self.student.study_year in self.company.wanted_degrees:
            self.score += 1

        for contract in self.student.contract_type:
            if contract.lower() == 'alternance' and self.company.co_op_student:
                self.score += 1
                break
            
            elif contract.lower() == 'stage':
                self.score += 1
                break
            
            elif contract.lower() == 'cdi' and self.company.cdi:
                self.score += 1
                break

        if self.student.offer_length in self.company.offer_length:
            self.score += 1

        for location in self.company.offers_locations:
            if location in self.student.geo_mobility:
                self.score += 1
                break
        
        self.score /= 5
