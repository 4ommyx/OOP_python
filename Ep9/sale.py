from employee import Employee

class Sale(Employee) :
    _departmentName = "Saler"
    def __init__ (self,name,salary,area):
        super().__init__(name,salary,self._departmentName)
        super()._display()
        self.area = area
        self._display()

    def _display(self):
        print("Area   : {}".format(self.area))
        print("---------------------")
        print(self.__str__())
        print("---------------------")

    def __str__(self):
        return(super().__str__()+" | Area : {}".format(self.area))
