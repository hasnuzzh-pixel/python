#1
numbers =[12,5,12,9,7]
largest =max(numbers)
second = None
for n in numbers:
    if n < largest:
        if second is None or n > second:
            second = n
if second is None:
   print("No second_largest distict value")
else:
   print(second)

#2
text ="programming"

for ch in text:
    if text.count(ch) == 1:
     print(ch)
    break
#example 2
text ="aabbcc"

for ch in text:
   if text.count(ch) ==1:
      print(ch)
      break

else:
   print("No non-repeating character")
