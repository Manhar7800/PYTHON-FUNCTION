"""
*args: argument: tuple as a parameter.

**kwargs: key with argument :dictionary as a parameter
"""



def myfun(*args):
    for i in args:
        print(i)


myfun(10,20,30,11,23,234)


#kwargs:

def myfun(**kwargs):
    for k,v in kwargs.items():
        print(f"{k} = {v}")


myfun(name="aaa",subject="python")