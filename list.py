#creating a list
my_list =[1,2,3]
print(my_list)
#Accessing list items
my_list =["apple","banana","cherry"]
print(my_list[1])
print(my_list[-1])
#changing list items
my_list =["apple","banana","cherry"]
my_list[1] ="orange"
print(my_list)
#changing multiple items
my_list =[1,2,3,4,5]
my_list[1:3] =["a","b"]
print(my_list)
#adding items to a list
#append()
my_list =["apple","banana"]
my_list.append("cherry")
print(my_list)
#insert()
my_list =["apple","banana"]
my_list.insert(1,"cheryy")
print(my_list)
#extend()
my_list =["apple","banana"]
new_list =["cheryy","orange"]
my_list.extend(new_list)
print(my_list)
#removing items from a list
#remove()
my_list =["apple","banana","cherry"]
my_list.remove("banana")
print(my_list)
#pop()
my_list =["apple","banana","cherry"]
popped_item =my_list.pop(1)
print(popped_item)
print(my_list)
#del()
my_list =["apple","banana","cherry"]
del my_list[0]
print(my_list)
#clear()
my_list =["apple","banana","cherry"]
my_list.clear()
print(my_list)
#list methods
#count()
my_list =[1,2,2,3,2,4]
print(my_list.count(2))
#index()
my_list =[10,20,30,40]
print(my_list.index(30))
#sorting a list
#sorted()
numbers =[3,5,1,4,2]
numbers.sort()
print(numbers)
#desending order
numbers =[3,5,1,4,2]
numbers.sort(reverse=True)
print(numbers)
#copying a list
original_list =["apple","banana","cherry"]
copied_list =original_list.copy()
print(copied_list)
#joining lists
list1 =["apple","banana"]
list2 =["cherry","orange"]
combined_list =list1 + list2
print(combined_list)