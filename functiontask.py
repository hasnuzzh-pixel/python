#1
def check_number(x):
    if x %2 ==0:
        return "even"
    else:
        return "odd"

num = int(input("enter a number: "))
print(check_number(num))
#2
def largest(a,b,c):
    if a>b and a>c:
        return "a is largest"
    elif b>c and b>a:
        return "b is largest"
    else:
        return "c is largest"
x = int(input("enter  first number: "))
y = int(input("enter second number: "))
z = int(input("enter third number: "))
print(largest (x,y,z))

#3
def sum_numbers(numbers):
    total = 0
    for num in numbers:
        total =  total + num
    return total
    
numbers =[10,20,30,40]
print(sum_numbers(numbers))
#4
def even_numbers(numbers):
    new_list = []
    for num in numbers:
        if num %2 ==0:
            new_list.append(num)
    return new_list

numbers = [1,2,3,4,5,6,7,8,]
print(even_numbers(numbers))

#5
def string_length(text):
    return len(text)

word = input("Enter a string: ")
print(string_length(word))

#6
def convert_upper(text):
    return text.upper()

word = input("enter a string: ")
print(convert_upper(word))

#7
def check_number(num):
    if num>0:
       return "positive"
    elif num<0:
        return "negative"
    else:
        return "Zero"

num =int(input("enter a number: "))
print(check_number(num))

#8
def check_number(num):
    if num % 3 == 0 and num %5 == 0:
       return "true"
    else:
       return "False"

num = int(input("enter a number: "))
print(check_number(num))

#9
def find_max(numbers):
    return max(numbers)

numbers = [10,20,5,30,15]
print(find_max(numbers))
#10
def check_marks(marks):
    if marks >= 90:
        return "A grade"
    elif marks >= 75:
        return "B grade"
    elif marks >= 60:
        return "c grade"
    else:
        return "fail"

marks=int(input("enter marks: "))
print(check_marks(marks))

#11
def discount_price(price):
     discount = price * 10 / 100
     return price - discount
price = float(input("enter price: "))
print(discount_price(price))

#12
def count_even_odd (numbers):
    even = 0
    odd = 0

    for num in numbers:
        if num %2 == 0:
            even += 1
        else:
            odd += 1

    return even, odd

numbers =[10,15,20,25,30]
print(count_even_odd(numbers))

#13
def celsius_to_faherenheit(celsus):
    return (celsius *9/5) + 32

celsius = float(input("enter celsius: "))
print(celsius_to_faherenheit(celsius))