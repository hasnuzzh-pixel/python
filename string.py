#string slicing
#basic slicing 
s ="Hello, World!"
print(s[0:5])
#negative indices
print(s[-6:-1])
#skipping characters
print(s[0:12:2])
#reversing a string
print(s[::-1])
#modifying strings
#replace method
s ="Hello,World!"
new_s =s.replace("World","Python")
print(new_s)
#uppercase and lowercase
print(s.upper())
print(s.lower())
#string concatenation
#using + operator
s1 ="Hello"
s2 ="World"
result =s1 +","+s2 +"!"
print(result)
#using join()
words =["python","is","awesome"]
sentence =" ".join(words)
print(sentence)
#formatted strings
#using % operator
name ="hasna"
age =21
formatted_string ="My name is %s,and I am %dyears old."%(name,age)
print(formatted_string)
#using format()method
name ="hasna"
age =21
formatted_string ="My name is {},and I am 21 yers old.".format(name,age)
print(formatted_string)
#escape charactrs
#inserting a newline
print("Hello\nWorld")
#inserting a tab
print("Hello\tWorld")
#using quotes within a string
print('He said, "Python is amazing!''')
#string methods
#len()
s ="Hello,World!"
print(len(s))
#strip()
s =" Hello, World! "
print(s.strip())
#split()
s ="Hello, World!"
print(s.split(","))
#find()
s ="Hello, World!"
print(s.find("World"))
#count()
s ="Hello, Hello, World!"
print(s.count("Hello"))
#startswith() and endwith()
s ="Hello World!"
print(s.startswith("Hello"))
print(s.endswith("World!"))
#upper() and lower()
s ="Hello, World!"
print(s.upper())
print(s.lower())
#replace
s ="Hello, World!"
print(s.replace("World","Python"))