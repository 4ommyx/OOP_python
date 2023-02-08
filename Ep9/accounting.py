from employee import Employee

class Accounting(Employee):
    _departmentName = "Account"
    def __init__ (self,name,salary,age):
        super().__init__(name,salary,self._departmentName) # ใช้ self เพราะดึงมาจากตัวมันเอง
        super()._display() 
        self.age = age # (ตัวแปรที่สร้างมาใหม่)
        self._display()

    def _display(self):
        print("age   : {}".format(self.age))
        print("---------------------")
        print(self.__str__())
        print("---------------------")

    def __str__(self):
        return(super().__str__()+" | Age : {}".format(self.age))
        