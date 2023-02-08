# Class var , Instance var
# Class variable : ตัวแปรที่ทำงานภายในคลาสซึ่งเราสามารถกำหนดค่าและเข้าถึงค่าได้เลยโดยไม่ต้องสร้าง obj
# Insatance variable : ตัวแปรของ obj สามารถเข้าถึงข้อมูลได้ก็ต่อเมื่อสร้าง obj ก่อนเท่านั้น
class Test2:
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
        print("-------------------")
    
aom = Test2("Nattawut",20000,"Programmer")
mu = Test2("Music",30000,"Programmer")
aom._display()
mu._display()

# การเข้าถึง class variable ต้องระบุชื่อคลาสหรือ obj ด้วยยย
print(Test2._minSalary)
print(aom._minSalary)
print(Test2._maxSalary)

# การเข้าถึง instance variable ต้องระบุชื่อ obj ด้วยยย
print(aom._name)
print(mu._name)
