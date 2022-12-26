
from diff.sk_diff import math_1

from summ.sk_sum import math_2

def cal():
    a = 10 
    b = 5

    sum_1= math_2.sk_sum_1(a,b)
    dif_1 = math_1.sk_diff_1(a,b)

    print("The sum is :",sum_1)
    print("The diff is :",dif_1)


class test:
    count = 5 
    def __init__(self,a):
        self.a = a

    def add_plus_one(self):
        return self.a+1

    @staticmethod
    def add(a,b):
        return a+b
    
    @classmethod
    def add_plus_2(cls,val):
        val = val+5
        k = cls(val)
        g = k.add_plus_one()
        return g



class emp:
    def __init__(self,age:int ,sal:float):
        self.age = age
        self.sal = sal


    def sal_display(self):
        print(f"the salary is {self.sal}")

    @staticmethod
    def senior_Sal(age):
        if age > 50:
            print("Senoir person salary")
        else:
            print("Junior")

    @classmethod
    def sal_diff(cls,age,sal):
        return cls(age,sal*10)
    def display(self):
        print("am in")
        return print(f"salary in classmethod :{self.sal}")
        
            

        


if __name__ == "__main__":
    print('Program Starts:')
    # d = test(5)
    # k = d.add_plus_one()
    # j = d.add_plus_2(20)
    # x = d.add(5,3)
    # print(d)
    # print(k)
    # print(x) 
    # print(j)
    emp_obj = emp(24,3000)
    emp_obj.senior_Sal(24)
    emp.senior_Sal(24)
    emp_classmethod_obj = emp.sal_diff(24,200)
    emp_classmethod_obj.display()
    #emp.sal_saturation(emp_obj.age)