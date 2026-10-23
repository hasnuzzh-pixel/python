#errors in python
try:
    a = 10
    b = 2
    print(a/ b)
except:
    print("something went wrong")

try:
    a = 10
    b= 0
    print(a / b )
except: 
    print("cannot divide by zero")

#common expection errors
#1 zero division error
#a = 10
#b = 0
#print(a / b)

#type error
#a = 10
#B = "Hello"

#print (a + b)
#key error
#student = {
  #  "name": "hasna",
  #  "age":  21
#}
#print(student["mark"])
#value error
#a = int("hello")
#print(a)

#index error
#numbers = [10, 20, 30]
#print(numbers[5])

#expection handling
try:
    
    print(10 / 0)
except ZeroDivisionError:
    print("cannot divide by zero")

#using else and finally in expection handling
try:
    num=int(input("enter a number: "))
    result= 10/num
except ZeroDivisionError:
    print("division by zero is not allowed!")
else:
    print(f"the result is {result}")

finally:
    print("this will always be printed")
