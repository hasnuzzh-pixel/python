#return statement
def mutiply(a,b):
    return a*b

result=mutiply(4,5)
print(result)
#doestrings in functions
def add(a,b):
    """this function add two numbers."""
    return a+b

print(add.__doc__)
#lambda function
add=lambda a,b:a+b
print(add(3,5))
#using lambda with map()
numbers=[1,2,3,4]
sqaured=map(lambda x:x **2,numbers)
print(list(sqaured))
#using lambda with filter()
numbers=[1,2,3,4,5,6]
even_numbers=filter(lambda x:x %2==0,numbers)
print(list(even_numbers))
#using lambda with reduce()
from functools import reduce
numbers=[1,2,3,4]
sum_result=reduce(lambda x,y:x+y,numbers)
print(sum_result)
#high order function
def increment(n):
    return lambda x:x+n

add_5=increment(5)
print(add_5(10))
#function scope
#LEGB(local,enclosing,global,built_in)

x=10 #global scope

def outer_function():
    x=5 #enclosing scope
def inner_function():
    x=2 #local scope
    print(x)


    inner_function()

outer_function()
print(x)