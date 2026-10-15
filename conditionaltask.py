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

#16
num=int(input("enter a number: "))

if num %3 == 0 and num %5 ==0:
    print("multiple of both 3 and 5")
else:
    print("not a multiple of both 3 and 5")

#17
for i in range(5):
    print("Hello")

#18
numbers =[1,2,3,4,5]

for num in numbers:
    if num > 3:
        print(num)

#19
Username ="admin"
password ="1234"

for i in range(3):
    u=input("enter username: ")
    p=input("enter password: ")

    if u.lower() == Username and p ==password:
        print("login successful")
        break
    else:
        print("Invalid username or password")
        print("Attempts remaining:", 2-i)

else:
    print("Account lockled")

#20
signal = input("enter color or number: ").lower()

if signal == "1" or signal =="red":
    print("stop and wait for 60 seconds")
elif signal =="2" or signal =="yellow":
    print("Ready and wait for 5 seconds")
elif signal =="3" or signal == "green":
    print("Go and drive safely")
else:
    print("Invalid signal")