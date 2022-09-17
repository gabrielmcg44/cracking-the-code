
DIFFICULTY_LEVELS = {
    "easy": 0,
    "medium": 1,
    "hard": 2
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
    def __init__(self, difficulty):
        if difficulty not in DIFFICULTY_LEVELS.keys():
            raise ValueError("Invalid difficulty")
        
        self.difficulty = difficulty


class CallCenter:
    def __init__(self, respondents, managers, directors):
        self.respondents = [ Respondent() for i in range(respondents) ]
        self.managers = [ Manager() for i in range(managers) ]
        self.directors = [ Director() for i in range(directors) ]
    
    def dispatch_call(self, call):
        for employee_group in [ self.respondents, self.managers, self.directors ]:
            for employee in employee_group:
                if employee.current_call is None:
                    if employee.level >= DIFFICULTY_LEVELS[call.difficulty]:
                        employee.current_call = call
                        return
                    
                    break
        
        raise ValueError("All apt employees are busy")
        
    def picture(self):
        print("Respondents:", [0 if employee.current_call is None else 1 for employee in self.respondents])
        print("Managers:", [0 if employee.current_call is None else 1 for employee in self.managers])
        print("Directors:", [0 if employee.current_call is None else 1 for employee in self.directors])
        
call_center = CallCenter(10, 5, 2)
call_center.dispatch_call(Call("easy"))
call_center.dispatch_call(Call("hard"))
call_center.dispatch_call(Call("medium"))
call_center.dispatch_call(Call("easy"))
call_center.dispatch_call(Call("easy"))
call_center.dispatch_call(Call("easy"))
call_center.dispatch_call(Call("medium"))
call_center.dispatch_call(Call("easy"))

print("Respondents:", [0 if employee.current_call is None else 1 for employee in call_center.respondents])
print("Managers:", [0 if employee.current_call is None else 1 for employee in call_center.managers])
print("Directors:", [0 if employee.current_call is None else 1 for employee in call_center.directors])


                    