#การสร้าง class
class Employee:
    #การสร้าง method (ว่าให้ทำอะไรบ้าง)
    def detail(self,name,salary):
        #การสร้าง attribute (ค่าของตัวแปรต่างๆ)
        self.name = name
        self.salary = salary
    def display(self):
        print("name   : {}".format(self.name))
        print("salary : {}".format(self.salary))

#การสร้าง obj
obj1 = Employee()
obj2 = Employee()
#การเรียกใช้ class แต่ละ method
obj1.detail("aom",25000)
obj1.display()

obj2.detail("mu",99999)
obj2.display()