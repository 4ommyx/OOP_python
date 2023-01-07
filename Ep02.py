# การสร้าง Constructor เป็นการทำงานของ method 
# โดยไม่ต้องเรียกใช้งาน จะทำงานตลอดเวลา 
# Destructor จะทำงานเมื่อจบโปรแกรม


class Employee: # การสร้าง class

    # การสร้าง method
    def __init__ (self,empname,empage):

        # การสร้าง attribute
        self.name = empname
        self.age = empage

    def display(self):

        # การสร้าง attribute
        print("test :{}".format(self.name))
        print("test :{}".format(self.age))
        print("------------")

obj = Employee("Nattawut",19)
obj.display()

