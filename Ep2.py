# Constructor (เอาไว้ใช้กำหนดค่า Atribute)
# ----------
# เป็น method พิเศษที่จะถูกใช้งานเมื่อตอนเริ่มต้นสร้างวัตถุ 
# โดยเราไม่จำเป็นต้องเรียกใช้งานมันเลย 
# def __init__(self):
#     pass

# Destructor  (เอาไว้เคลียร์แรม)
# -----------
# เป็น method ที่ตรงข้ามกับ Constructor จะถูกใช้งานเมื่อสิ้นสุดการทำงานของ Class 
# จะเป็นกลุ่มคำสั่งที่ทำหน้าที่คืนหน่วยความจำให้ระบบ
# def __del__(self):
#     pass

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
obj1.salary = 99999
obj1.display()
obj2.display()
