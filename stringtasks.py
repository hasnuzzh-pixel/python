s ="hello"
s =s.upper()
print(s)
s ="PYTHON"
s =s.lower()
print(s)
s ="hello world"
new_s =s.replace("world","python")
print(new_s)
s ="hello"
print(s[1:4])
s ="python"
print(s[::-1])
s1 ="hello"
s2 ="world"
result =s1 +" "+ s2
print(result)
s ="hi,hi,hi"
print(s.count("hi"))
s ="concatenate"
print(s.find("cat"))
s ="banana"
print(s.count("a"))
s =" hello "
print(s.strip())
s ="hello"
print(s.index("o"))
s ="a,b,c,d"
print(s.split(","))
my_list =["a","b","c"]
s = ''.join(my_list)
print(s)
s ="abcdef"
print(s[::2])
s ="banana"
print(s.replace("a","@"))
s ="hello123"
print(s.isalnum())
s ="python"
print(s.capitalize())
s ="hello world"
print(s.title())
s ="python"
print(s.replace("a","").replace("e","").replace("i","").replace("o","").replace("u",""))
s ="madam"
print(s == s[::-1])