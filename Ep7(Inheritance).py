# Inheritance 
# -----------
# คือการสืบทอดคุณสมบัติบางอย่างที่มีมีอยู่แล้วโดยการสร้างเพิ่มเติมจากสิ่งที่มีอยู่แล้วได้เลย 
# โดยแบ่งเป็น คลาสแม่(Superclass) ----> คลาสลูก(Subclass) Ex (Player) ----> (GK,DEF,MID,ST)
# คุณสมบัติที่ถ่ายทอดนั้นจะถ่ายทอดได้ทั้งหมด ยกเว้น Private

# Super() 
# ------
# Inheritance เป็นกระบวนการทำงานจาก sub ---> supper 
# ซึ่งเราต้องกำหนดค่าให้ sub ก่อนโดยผ่าน consactor 
# และทำการใช้คำสั่ง super() ในการดึง method จาก superclass 
# ให้สามารถใช้ได้ใน subclass นั่นเอง

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
        print("---------------------")

# Employee สืบทอด Accounting
class Accounting(Employee):
    _departmentName = "Account"
    def __init__ (self,name,salary):
        super().__init__(name,salary,self._departmentName) # ใช้ self เพราะดึงมาจากตัวมันเอง
        super()._display()

class Programmer(Employee):
    _departmentName = "Dev"
    def __init__ (self,name,salary):
        super().__init__(name,salary,self._departmentName)
        super()._display()



class Sale(Employee) :
    _departmentName = "Saler"
    def __init__ (self,name,salary):
        super().__init__(name,salary,self._departmentName)
        super()._display()

acc1 = Accounting("a",10000)
acc2 = Accounting("b",20000)

dev1 = Programmer("c",30000)
dev2 = Programmer("d",40000)

sel1 = Sale("e",50000)
sel2 = Sale("f",60000)
