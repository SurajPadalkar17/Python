'''#print star pattern in square 
n = int(input("Enter the n :"))

for _ in range(n):
    print("*"*5)

#Print the no 
n = int(input("Enter the n :"))
for i in range (n):
    for j in range (1,n+1):#loop for column
     print(j,end= "  ")
    print()
    
#LEFT RIANGLE Number PATTERN
n = int(input("enter the value of n:"))
for i in range (1,n+1):
    for j in range(1,i+1):
        print(j,end="")
    print()

#LEFT RIANGLE ALPHABET PATTERN
n = int(input("Enter the n"))
for i in range(n):
    for j in range (i+1):
        print(chr(j+65),end="")
    print()'''


#  Pyramid no pattern

n = int(input("Enter the n"))

for i in range (1 , n+1) :
    print(" " * (n - i),end ="")
    for j in range ( 1 , 2*i):
        print(j,end="")
    print()   
    
