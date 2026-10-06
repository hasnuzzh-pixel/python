#1
my_set ={1,2,3,4}
print(my_set)
#2
my_set ={1,2,3,4}
my_set.add(5)
print(my_set)
#3
my_set ={1,2,3,4}
my_set.remove(3)
print(my_set)
#4
my_set ={1,2,3,4}
print(2 in my_set)
#5
my_list =[1,2,2,3,4,4]
my_set =set(my_list)
print(my_set)
#6
my_tuple =(10,20,30)
my_set =set(my_tuple)
print(my_set)
#7
my_set1 ={1,2,3}
my_set2 ={3,4,5}
result =my_set1.union(my_set2)
print(result)
#8
my_set1 ={1,2,3}
my_set2 ={3,4,5}
result =my_set1 & my_set2
print(result)
#9
my_set1 ={1,2,3,4,}
my_set2 ={3,4}
result =my_set1 - my_set2
print(result)
#10
my_set ={5,6,7}
my_set =my_set.copy()
print(my_set)
#11
my_set ={1,2,3}
my_set.clear()
print(my_set)
#12
my_set1 ={1,2}
my_set2 ={1,2,3}
print(my_set1.issubset(my_set2))
#13
my_set1 ={1,2,3}
my_set2 ={1,2}
print(my_set1.issuperset(my_set2))
#14
my_set1 ={1,2,3}
my_set2 ={3,4,5}
result =my_set1 ^ my_set2
print(result)
#15
my_set ={8,9,10}
my_set.update([1,2,3])
print(my_set)
#16
my_set ={1,2,3}
removed_item =my_set.pop()
print(removed_item)
#17
my_set1 ={1,2,3}
my_set2 ={3,2,1}
print(my_set1 == my_set2)
#18
my_list =[1,2,2,3,4,4,5]
my_set =set(my_list)
print(my_set)
#19
my_set ={1,2,3}
my_list =list(my_set)
print(my_list)
#20
my_set ={1,2,3,4,5}
my_set.difference_update ({2,4})
print(my_set)