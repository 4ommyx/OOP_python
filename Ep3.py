# instance ,dir ,__class__
class Test:
    def __init__(self,name,salary,department):
        self.name = name
        self.salary = salary
        self.department = department

    def display(self):
        print("name   : {}".format(self.name))
        print("salary : {}".format(self.salary))
        print("department : {}".format(self.department))

    def __del__(self):
        print("Destructor")

obj1 = Test("Nattawut",20000,"Programmer")
obj2 = Test("Music",99999999,"Sleeper")

# instance 
# (เป็นการตรวจสอบว่า obj นั้นๆทำงานใน class ที่ระบุหรือไม่ โดยจะ Return ค่าเป็น boolen)
a = isinstance(obj1,Test)
print(a)

# dir (เป็นการส่งค่า atribute,method ใน class ว่ามีตัวใดบ้างเก็บไว้ใน list)
print(dir(obj2))
print(dir(obj1.name))

# class (เป็นการระบุว่า obj นั้นอยู่ใน class ใด)
print(obj1.__class__)