# Polymorphism 
# คือคุณสมบัติที่ตอบสนองต่อ method เดียวกันด้วยวิธีที่ต่างกันและสามารถกำหนด obj ได้หลายรูปแบบ  

# Overloading method : method ที่ชื่อเหมือนกันและอยู่ในคลาสเดียวกัน โดยแยกความแตกต่างด้วย Parameter
# Overriding method : method ของคลาสลูกที่มีชือเหมือนกับคลาสแม่

# Superclass (ข้อมูล,รูปแบบการทำงานที่คล้ายหรือเหมือนกัน)
# |
# |
# V
# Subclass (ข้อมูล,รูปแบบการทำงานที่มีความแตกต่างกัน)
class Employee:
    # class variable
    _maxSalary = 99990
    _minSalary = 11110

    def __init__(self,name,salary,department):
        # instance variable
        self._name = name 
        self.__salary = salary 
        self._department = department 
    
    def _display(self):
        print("name   : {}".format(self._name))
        print("salary : {}".format(self.__salary))
        print("department : {}".format(self._department))

    def _getIncome(self,bonus = 9):
        return (self.__salary*12)+bonus

    def __str__(self): 
        return ("Name : {} | Department : {} | salary : {} | Income : {} ".format(self._name,self._department,self.__salary,self._getIncome()))
    
# Subclass (คลาสลูก)
# Employee สืบทอด Accounting
class Accounting(Employee):
    _departmentName = "Account"
    def __init__ (self,name,salary,age):
        super().__init__(name,salary,self._departmentName) # ใช้ self เพราะดึงมาจากตัวมันเอง
        self.age = age # (ตัวแปรที่สร้างมาใหม่)
        self._display()

    def _display(self):
        super()._display()
        print("age   : {}".format(self.age))
        print("---------------------")
        print(self.__str__())
        print("---------------------")

    def __str__(self):
        return(super().__str__()+" | Age : {}".format(self.age))
        
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

class Sale(Employee) :
    _departmentName = "Saler"
    def __init__ (self,name,salary,area):
        super().__init__(name,salary,self._departmentName)
        self.area = area
        self._display()

    def _display(self):
        super()._display()
        print("Area   : {}".format(self.area))
        print("---------------------")
        print(self.__str__())
        print("---------------------")

    def __str__(self):
        return(super().__str__()+" | Area : {}".format(self.area))

acc1 = Accounting("a",10000,30)

dev1 = Programmer("c",30000,2,"python java")

sel1 = Sale("e",50000,"BKK")
