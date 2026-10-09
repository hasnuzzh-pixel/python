#if condition
#a=float(input("enter a number"))
print(a,type(a))

if a > 0:
    print("a is postive")
elif a==0:
    print("a is zero")
elif a==-1.1:
    print("a is float")
else:
    print("a is negative")
#nested if
a=1
if a>0:
    if a==1.1:
        print("a is positive float")
    else:
        print("a is positive")

else:
    print("a is negative")

#logical operator(and,or,not)
x=10
y=5
if x>5 and y<10:
    print("Both conditions are true")

if x>5 or y>10:
    print("one condition is true")

if not x<5:
    print("x is not less than 5")  

#ternary operator
x=5
result ="Greater than 10" if x>10 else"10 or less"
print(result)
#1.for loop
fruits =["apple","banana","cherry"]
for fruit in fruits:
    print(fruit)








#2.while loop
x=0
while x<5:
    print(x)
    x+=1