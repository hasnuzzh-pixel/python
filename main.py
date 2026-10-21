#main.py
import mymodule

message =mymodule.greet("alice")
print(message)
#from mymodule import greet,greet1
message = mymodule.greet1("alice")
print(message)

#import mymodule as m
message = mymodule.greet3("alice")
print(message)
#import math
import math
print(math.sqrt(25))
#import factorial
import math
print(math.factorial(5))
from math import pi
print(pi)