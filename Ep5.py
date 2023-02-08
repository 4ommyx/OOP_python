# getter setter method
class Test2:
    def __init__(self,name,salary,department):
        # Private attribute
        self.__name = name # Private
        self.__salary = salary # Private
        self.__department = department # Private
    # Protected method
    def _display(self):
        print("name   : {}".format(self.__name))
        print("salary : {}".format(self.__salary))
        print("department : {}".format(self.__department))
        print("-------------------")
    # setter method (สามารถแก้ไขข้อมูลแบบ private ได้)
    def setName(self,newName):
        self.__name = newName

    def setSalary(self,newSalary):
        self.__salary = newSalary

    def setDepartment(self,newDepartment):
        self.__department = newDepartment

    # getter method (ส่งค่าในคลาสเพื่อนำมาใช้งานได้)
    def getName(self):
        return self.__name
    
    def getSalary(self):
        return self.__salary
    
    def getDepartment(self):
        return self.__department
    
obj1 = Test2("Nattawut",20000,"Programmer")

# เมื่อตั้งเป็น Private แล้วไม่สามารถแก้ไขได้
obj1.__name = "Music"
obj1.__salary = 99999
obj1.__department = "Sleeper"
obj1._display()

# แต่เราสามารถใช้ setter แก้ไขข้อมูลชนิด Private ได้
obj1.setName("Music")
obj1.setSalary(99999)
obj1.setDepartment("sleeper")
obj1._display()

# การใช้ getter เพื่อ return ค่าออกมาและนำมาใช้นอก class
print("Name : {}".format(obj1.__name))
print("Name : {}".format(obj1.getName()))

print("Salary : {}".format(obj1.__salary))
print("Salary : {}".format(obj1.getSalary()))

print("Department : {}".format(obj1.__department))
print("Department : {}".format(obj1.getDepartment()))
