# การห่อหุ้ม (Encapsulation)
# - เป็นการซ่อนรายละเอียดการทำงานไว้ภายในไม่ให้ภายนอกนั้นเข้าถึงข้อมูลได้
# - ทำให้ภายนอกไม่สามารถเข้าแก้ไขเปลี่ยนแปลงข้อมูลภายในได้
# - ข้อดีของการห่อหุ้มคือสามารถสร้างความปลอดภัยให้กับข้อมูลได้

# Access Modifier 
# คือระดับในการเข้าถึง Class,Attribute,Method ต่างๆ ในระดับการเข้าถึงที่เราระบุดังนี้
# Public    ()
# ใครๆ ก็สามารถเข้าถึงและเรียกใช้งานได้ 
# Protected (_) 
# เป็นการประกาศระดับการเข้าถึงเฉพาะคลาสของตัวมันเองและคลาสลูกที่สืบทอดคุณสมบัติไปใช้เท่านั้น
# Private   (__) 
# เป็นการประกาศระดับการเข้าถึงที่เข้มงวดที่สุด จะมีแต่คลาสตัวมันเองเท่านั้นที่มีสิทธิ์เข้าถึงและใช้งานได้

# การใช้งาน Access Modifier
# -----------------------

# Public Modifier
class Test:
    def __init__(self,name,salary,department):
        # public attribute
        self.name = name
        self.salary = salary
        self.department = department
        # เราสามารถเรียกใช้ method display 
        # ได้เลยระบุ self.ข้างหน้าด้วยนะ
        self.display()
    # public method
    def display(self):
        print("name   : {}".format(self.name))
        print("salary : {}".format(self.salary))
        print("department : {}".format(self.department))
        print("-------------------")

    def __del__(self):
        print("Destructor")

obj1 = Test("Nattawut",20000,"Programmer")
obj1.salary = 50000
obj2 = Test("Music",99999999,"Sleeper")
# เรียกใช้ method display()
# obj1.display()

# Protected Modifier (_)
class Test1:
    def __init__(self,name,salary,department):
        # Protected attribute
        self._name = name
        self._salary = salary
        self._department = department
        # เราสามารถเรียกใช้ method display 
        # ได้เลยระบุ self.ข้างหน้าด้วยนะ
        self._display()
    # Protected method
    def _display(self):
        print("name   : {}".format(self._name))
        print("salary : {}".format(self._salary))
        print("department : {}".format(self._department))
        print("-------------------")

    def __del__(self):
        print("Destructor")

obj1 = Test1("Nattawut",20000,"Programmer")
obj1._salary = 50000
obj1._display()

# Private Modifier (_)
class Test2:
    def __init__(self,name,salary,department):
        # Private attribute
        self._name = name # Protected
        self.__salary = salary # Private
        self.__department = department # Private
    # Protected method
    def _display(self):
        print("name   : {}".format(self._name))
        print("salary : {}".format(self.__salary))
        print("department : {}".format(self.__department))
        print("-------------------")

    def __del__(self):
        print("Destructor")

obj1 = Test2("Nattawut",20000,"Programmer")
obj1._name = "Music"
obj1.__salary = 99999
obj1.__department = "Sleeper"
obj1._display()
# name เปลี่ยนได้ salary department เปลี่ยนไม่ได้