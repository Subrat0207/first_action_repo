
from diff.sk_diff import math_1

from summ.sk_sum import math_2

def cal():
    a = 10 
    b = 5

    sum_1= math_2.sk_sum_1(a,b)
    dif_1 = math_1.sk_diff_1(a,b)

    print("The sum is :",sum_1)
    print("The diff is :",dif_1)


if __name__ == "__main__":
    print('Program Starts:')
    cal()
