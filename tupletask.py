#1
my_tuple =(1,2,3,4)
print(my_tuple[2])
#2
my_tuple =(10,20,30)
my_list=list(my_tuple)
print(my_list)
#3
my_list =[1,2,3]
my_tuple =tuple(my_list)
print(my_tuple)
#4
my_tuple =("a","b","c","d")
print(my_tuple[1:3])
#5
my_tuple =("x","y","z")
print("x" in my_tuple)
#6
my_tuple =(5,3,9,1)
print(max(my_tuple))
#7
my_tuple =(1,2,3)
my_tuple =my_tuple * 2
print(my_tuple)
#8
my_tuple =(1,2,2,3,2)
print(my_tuple.count(2))
#9
my_tuple =("dog","cat","mouse")
print(my_tuple.index("cat"))
#10
my_tuple =(1,2,3,4,5)
print(my_tuple[::-1])
#11
my_tuple1 =(1,2)
my_tuple2 =(3,4)
my_tuple = my_tuple1 + my_tuple2
print(my_tuple)
#12
my_tuple =tuple("hello")
print(my_tuple)
#13
my_tuple =(1,2,3,4)
my_list =[my_tuple[0],my_tuple[-1]]
print(my_list)
#14
my_tuple =(10,20,30,40)
my_list =list(my_tuple)
my_list[2] =99
my_tuple =tuple(my_list)
print(my_tuple)
#15
my_tuple =(1,2,3)
a,b,c = my_tuple
print(a, b, c)
#16
my_tuple =(1,2,3)
my_tuple =(my_tuple,)
print(my_tuple)
#17
my_tuple1 =("a","b")
my_tuple2 =("c","d")
my_tuple = my_tuple1 + my_tuple2
print(my_tuple)
#18
my_tuple =(1,2,3)
print(my_tuple == my_tuple[::-1])
#19
my_tuple =([1,2], [3,4])
my_list = my_tuple[0] + my_tuple[1]
print(my_list)
#20
my_tuple =(1,[2,3,4],4)
my_tuple[1].append(5)
print(my_tuple)