from employee import Employee

class Programmer(Employee):
    _departmentName = "Dev"
    def __init__ (self,name,salary,exp,skill):
        super().__init__(name,salary,self._departmentName)
        self.exp = exp
        self.skill = skill
        self._display()

    def _display(self):
        super()._display()
        print("Exp   : {}".format(self.exp))
        print("Skill   : {}".format(self.skill))
        print("---------------------")
        print(self.__str__())
        print("---------------------")

    def __str__(self):
        return(super().__str__()+" | Exp : {} | Skill : {}".format(self.exp,self.skill))
