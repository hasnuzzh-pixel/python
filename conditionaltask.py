#1
num=int(input("enter a number: "))

if num > 0:
    print("positive")
elif num < 0:
    print("negative")
else:
     print("zero")

#2
num=int(input("enter a number: "))

if num %2==0:
    print("even")
else:
    print("odd")

#3
num=int(input("enter a number: "))
if num > 100:
    print("greater than 100")
else:
    print("not greater than 100")

#4
age=int(input("enter your age: "))
if age>=18:
    print("eligible to vote")
else:
    print("not eligible to vote")
#5
a=int(input(" enter first  number: "))
b=int(input("enter second number: "))
if a>b:
    print("a is greater")
elif b<a:
    print("b is greater")
else:
    print("both are equal")
#6
a=int(input("enter first number: "))
b=int(input("enter second number: "))
c=int(input("enter third number: "))
if a>b and b>c:
    print("a is largest")
elif b>a and b>c:
    print("b is largest")
else:
    print("c is largest")
#7
year=int(input("enter a year: "))
if year % 400 == 0:
    print("leap year")
elif year % 100 == 0:
    print("not a leap year")
elif year % 4 == 0:
    print("leap year")
else:
    print("not a leap year")
#8
mark=int(input("enter a mark: "))
if mark>=40:
    print("pass")
else:
    print("fail")
#9
mark=int(input("enter a mark: "))
if mark>=90:
    print("A grade")
elif mark>=75:
    print("B grade")
elif mark>=60:
    print("C grade")
else:
    print("fail")
#10
ch=(input("enter a character: "))
if ch in "aieou":
    print("vowel")
else:
    print("consonant")
#11 
for i in range(1,11):
    if i == 6:
        break
    print(i)
#12
for i in range(1,11):
    if i == 5:
        continue
    print(i)

#13
num = 10
if num > 5:
    pass
print("Hello")

#14
for i in range(1,21):
    if i %2==0:
        print(i)

#15
total =0
for i in range(1,11):
    total=total+i
    print(total)

