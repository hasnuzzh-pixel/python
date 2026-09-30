#creating a tuple
my_tuple =(1,2,3,'python',4.5)
print(my_tuple)
#single item tuple
single_tuple =(5,)
print(type(single_tuple))
#accessing tuple items
my_tuple =('apple','banana','cherry')
print(my_tuple[1])
print(my_tuple[-1])
#slicing tuples
my_tuple =(10,20,30,40,50)
print(my_tuple[1:4])
#updating a tuple
#reassinging a tuple
my_tuple =(1,2,3)
my_tuple =(4,5,6)
print(my_tuple)
#converted tuple to list
my_tuple =('apple','banana','cherry')
temp_list =list(my_tuple)
temp_list[1] ='orange'
my_tuple =tuple(temp_list)
print(my_tuple)
#unpacking tuples
my_tuple =('apple','banana','cherry')
(fruit1,fruit2,fruit3) =my_tuple
print(fruit1)
print(fruit2)
print(fruit3)
#using*(asterisk)
my_tuple =(1,2,3,4,5)
(first,*middle,last)=my_tuple
print(first)
print(middle)
print(last)
#joining tuples
tuple1 =(1,2,3)
tuple2 =(4,5,6)
joined_tuples =tuple1 + tuple2
print(joined_tuples)
#tuple methods
#count
my_tuple =(1,2,3,2,2,4)
print(my_tuple.count(2))
#index
my_tuple =('apple','banana','cherry')
print(my_tuple.index('banana'))
#deleting a tuple
my_tuple =('apple','banana','cheryy')
del my_tuple
