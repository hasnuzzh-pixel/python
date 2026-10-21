#A STANDARD PYTHON LIBRARIES
# 1 math functions
import math

print(math.sqrt(16))
print(math.factorial(5))

#2 date time
from datetime import datetime


now=datetime.now()
print(now)

#3 os operating system
import os

current_dir = os.getcwd()
print(current_dir)

#4 sys system specific parameters functions
import sys


print(sys.version)

#5 json working with JSON data
import json

data = '{"name": "john", "age":30}'
parsed_data =json.loads(data)
print(parsed_data)
