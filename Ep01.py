# การสร้าง class and object
# class คือแม่แบบ 
# obj คือ สิ่งที่ถูกสร้างขึ้นจาก class

class Employee: # การสร้าง class

    # การสร้าง method
    def detail(self,empname,empage):

        # การสร้าง attribute
        self.name = empname
        self.age = empage
    
    def display(self):

        # การสร้าง attribute
        print("test :{}".format(self.name))
        print("test :{}".format(self.age))
        print("------------")

# การสร้างวัตถุ
obj1 = Employee()
obj1.detail("Nattawut",19)
obj1.display()

obj2 = Employee()
obj2.detail("Prayut",99)
obj2.display()

obj3 = Employee()
obj3.detail("Pravit",98)
obj3.display()