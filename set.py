#creating a set
#using curly braces
my_set ={1,2,3,4}
print(my_set)
#using set()function
another_set =set([5,6,7])
print(another_set)
#empty set
empty_set =set()
print(type(empty_set))
#adding items to a set
#adding a single item
my_set ={1,2,3}
my_set.add(4)
print(my_set)
#adding  multiple item
my_set ={1,2,3}
my_set.update([4,5,6])
print(my_set)
#removing items from a set
#remove()
my_set ={1,2,3,4}
my_set.remove(2)
print(my_set)
#discard
my_set ={1,2,3,4}
my_set.discard(5)
print(my_set)
#pop()
my_set ={1,2,3,4}
removed_item =my_set.pop()
print(removed_item)
#clear()
my_set ={1,2,3}
my_set.clear()
print(my_set)
#joining sets
#union()
set1 ={1,2,3}
set2 ={3,4,5}
result =set1.union(set2)
print(result)
#update()
set1 ={1,2,3}
set2 ={4,5,6}
set1.update(set2)
print(set1)
#set intersection(&)
set1 ={1,2,3,}
set2 ={2,3,4}
result =set1 - set2
print(result)
#set symmetric difference
set1 ={1,2,3}
set2 ={2,3,4}
result =set1 ^ set2
print(result)
#copy()
set1 ={1,2,3}
set2 =set1.copy()
print(set2)
#issubset(set)
set1 ={1,2}
set2 ={1,2,3,4}
print(set1.issubset(set2))
#issuperset(set)
set1 ={1,2,3,4}
set2 ={1,2}
print(set1.issuperset(set2))
#frozen sets
my_frozenset =frozenset([1,2,3,4])
print(my_frozenset)