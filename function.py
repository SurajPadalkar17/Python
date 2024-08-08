''' function are blocks of reusable code that perform specific task
 There are two types of function
    1)built in :
                 print,sum,etc
    2) user defined function:
    def function name (parameter):
         # statement
         return 
         

# function which takes 2 no as iput and returns thier sum

def add(n1,n2):
    print("n1:",n1)
    print("n2",n2)
    sum = n1+ n2
    return sum
#positional arguments
print("sum is :",add(2,3))




# keyword argument (named argument)
print("The sum is ",add(n2=2, n1=3))

#default arguments
 # in this the value in given in function itself (aside of def)
  

# arbitrary arguments
# def add _all_No(* args)  // here we can add many arguments
# arg is tuple hence the value stored in arg is in tuple()

def addallnumbers ( *args):
    sum = 0
    for i in  args:
        sum += i
    return sum 
output = addallnumbers(1,45,1,4,5,6,7,4)
print("addition is",output)

# ** kwargs
def studentinfo(**kwargs):
    for x , y in kwargs.items():
        print(x ,"is", y)


studentinfo(names ="urvi",age = 22,city="delhi")
studentinfo(names ="ria",age = 21,city="bombay")


# sum of 1 to n numbers

def sumoneton(n):
    sum = 0
    for i in range (1,n+1):
        sum += i
    return sum
n = int(input("Enter the n:"))
# call function
output = sumoneton(n)
print("sum of first n term is:",output)'''

# function in between function

def outer_function ():
    x = 1 
    
    def inner_function():
        y = 2
        result = x + y
        print(result)
    return inner_function()
output = outer_function()
print(output)