 
# Using nested if else
a = int(input("Enter the first no"))
b = int(input("Enter the second no "))
c = int(input("Enter the Third  no "))

if a > b :
    if a > c :
        print(a," a is greter no")
    else :
        print(c,"c is greter")
else :
    if b > c :
        print(b,"b is greter no")
    else :
        print(c,"c is greter no")
        
        
# Take Positive integer and tell if it is divisible by 5 or 3 but not divisible by 15.

number =int(input("Enter the no:"))

if number % 15 ==0 :
    print("it is divisible by 15")
else :
    if  number % 3 == 0 or number % 5 ==0 :
        print(" No is divisible by 3 or 5")
    else :
        print("It is nether divisible by 5 or 3")