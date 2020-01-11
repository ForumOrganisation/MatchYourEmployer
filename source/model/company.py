import numpy.random as rd


class Company:

    company_id_count = 1

    def __init__(self, domains, accepted_nationalities, domains_localisation,
                 school, presence_day, wanted_diploma, wanted_department,
                 mobility, offer_length):
        self.id_company = Company.company_id_count  # Same as Student class
        Company.company_id_count += 1
        self.domains_localisation = dict(domains_localisation)
        self.domains = list(domains)
        self.accepted_nationalities = list(accepted_nationalities)
        self.school = school  # boolean
        self.presence_day = presence_day  # Same as Student class
        self.wanted_diploma = list(wanted_diploma)
        self.wanted_department = list(wanted_department)
        self.mobility = mobility  # Same as Student class
        self.offer_length = offer_length  # 1 if they accept less than 6 months, 0 otherwise



    def __str__(self):
        return "Company " + str(self.id_company)
