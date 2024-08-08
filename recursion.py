# recursion  is calling same function again and again

'''def factorial(n):
    if n== 0 :
        return 1
    ans = n * factorial(n-1)
    return ans
n = int (input("enter the n:"))
output=factorial(n)
print("factorial of no is",output)




# print no from 1 to n

def number(n):
    #base case
    if n==0:
        return 
    
    number(n-1)
    print(n)
n= int(input("enter the n:"))
number(n)


# Sum From 1 to nm no.

def sum(n):
    # base case
    if n==1:
        return 1
    ans = n + sum(n-1)
    return ans
n= int(input("Entert n:"))
print(sum(n)) 

# power of a to b
def power_a_b(a,b):
    # base case
    if b == 0:
        return 1
    ans = a * power_a_b(a,b-1)
    return ans
a= int(input("Enter the a:"))
b=(int(input("enter th b:")))
print(power_a_b(a,b))'''



# fibonacci series 

def fibonacci(n):
    # base case 1
    if n == 1:
        return 0
    # base case 2
    elif n==2 :
        return 1
    # recursive case
    else :
        return (fibonacci(n-1)+fibonacci(n-2))
    
n = int (input("enter the n:"))
for i in range (1,n+1):
    print(fibonacci(i))