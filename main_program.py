from pydantic import BaseModel
from typing import Optional


def clean_str_int(str_val):
    if bool(str_val):return '1'
    else:pass

def clean_str_bool(str_val):
    if bool(str_val):return 'y'
    else:pass

class User(BaseModel):
    id:int
    user_name:str
    pass_word:Optional[str]
    test:Optional[bool]



data = {'id':'1234','user_name':"Subrat",'pass_word':'kumar','test':'y'}


data_1 = {'id':clean_str_int('Subrat Kumar Das'),'user_name':"Subrat",'pass_word':'kumar','test':'n'}

data_2 = {'id':clean_str_int('Subrat Kumar Das'),'user_name':"Subrat",'pass_word':'kumar','test':clean_str_bool('LOW')}

data_3 = {'id':clean_str_int('Subrat Kumar Das'),'user_name':"Subrat",'pass_word':'kumar','test':clean_str_bool('')}
data_4 = {'id':clean_str_int('Subrat Kumar Das'),'user_name':"Subrat",'pass_word':'kumar','test':'N'}

def timer_decorator(func):
    def timer_wrapper(*args, **kwargs):
        import datetime                 
        before = datetime.datetime.now()
        #print(before)                     
        result = func(*args,**kwargs)                
        after = datetime.datetime.now()
        #print(after)                        
        print("Elapsed Time = {0}".format(after-before) )     
    return timer_wrapper
    
@timer_decorator
def sum(x, y):
    print(x + y)
    return x + y

if __name__ == "__main__":
    print('Program Starts:')
    user = User(**data_4)
    k = user
    print(k)

