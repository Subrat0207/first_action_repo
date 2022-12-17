
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



if __name__ == "__main__":
    print('Program Starts:')
    d = test(5)
    k = d.add_plus_one()
    j = d.add_plus_2(20)
    x = d.add(5,3)
    print(d)
    print(k)
    print(x) 
    print(j)