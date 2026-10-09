a=int(input("enter a number: "))
op=input("enter operation: ")
b=int(input("enter a number: "))
if op =="+":
  print("result:", a+b)
elif op =="-":
  print("result:", a-b)
elif op =="*":
  print("result:",a*b)
elif op =="/":
   print("result:",a/b)
else:
   print("invalid operator")
