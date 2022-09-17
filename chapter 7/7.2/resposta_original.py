
DIFFICULTY_LEVELS = {
    easy: 0,
    medium: 1,
    hard: 2
}

class Respondent:
    def __init__(self, level=0):
        self.current_call = None
        self.level = level
    
class Manager:
    def __init__(self, level=1):
        self.current_call = None
        self.level = level

class Director:
    def __init__(self, level=2):
        self.current_call = None
        self.level = level
        
class Call:
    def __init__(self, difficulty):,
        if difficulty not in DIFFICULTY_LEVELS.keys():
            throw("Invalid difficulty");
        
        self.difficulty = difficulty


class CallCenter:
    def __init__(self, respondents, managers, directors):
        self.respondents = [ Respondent() ] * respondents
        self.managers = [ Managers() ] * managers
        self.directors = [ Directors() ] * directors
    
    def dispatch_call(self, call):
        for employee_group in [ self.respondents, self.managers, self.directors ]:
            for employee in [ employee_group ]:
                if employee.current_call is None:
                    if employee.level >= call.difficulty:
                        employee.current_call = call
                        return
                    
                    break
        
        throw("All apt employees are busy")
                    