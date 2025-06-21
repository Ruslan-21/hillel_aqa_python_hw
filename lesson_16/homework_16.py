class Employee:

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary



class Manager(Employee):

    def __init__(self, name, salary, department):
        Employee.__init__(self, name, salary)
        self.department = department


class Developer(Employee):

    def __init__(self, name, salary, programming_language):
        Employee.__init__(self, name, salary)
        self.programming_language = programming_language

class TeamLead(Manager, Developer):

    def __init__(self, name, salary, department, programming_language, team_size):
        Manager.__init__(self, name, salary, department)
        Developer.__init__(self, name, salary, programming_language)
        self.team_size = team_size

def test_team_lead():
    lead = TeamLead('Alex', 30000, 'IT', 'Python', 3)

    assert lead.name == 'Alex'
    assert lead.salary == 30000
    assert lead.department == 'IT'
    assert lead.programming_language == 'Python'
    assert lead.team_size == 3