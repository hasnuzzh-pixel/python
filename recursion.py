#syntax of a recursion function
#def recursive_function(parameters):
 #if base_case_condition:
   #return base_case_value
#else:
     #return recursive_function(modified_parameters)

# factorial of a number:
def factorial(n):
    #Base case
    if n==0 or n==1:
        return 1

    #Recursive case
    else:
        return n * factorial(n-1)
#Test the function
print(factorial(5))

#fibnonacci sequence

def fibonacci(n):
    #Base cases
    if n == 0:
        return 0
    elif n==1:
        return 1
    #Recursive case
    else:
        return fibonacci(n-1)+ fibonacci(n-2)

#Test the function
print(fibonacci(6))

#sum of list
def sum_list(lst):
    #Base case
    if not lst:
      return 0
    #Recursive case
    else:
        return lst[0]+sum_list(lst[1:])
#Test the function
print(sum_list([1,2,3,4,5]))

#example of iterative factorial:
def iterative_factorial(n):
    for i in range(1,n*1):
        result *=i
        return result

print(iterative_factorial(5))