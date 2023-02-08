# การสร้าง class แบบแยกไฟล์
# from (ชื่อไฟล์) import (ชื่อคลาส)
from accounting import Accounting
from programmer import Programmer
from sale import Sale

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
    
acc1 = Accounting("a",10000,30)

dev1 = Programmer("c",30000,2,"python java")

sel1 = Sale("e",50000,"BKK")
