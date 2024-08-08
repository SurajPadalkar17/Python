#Program for finding positive or negative no

no = int(input("Enter the any no"))
if no >=0 :
    print("no is positive")
else :
    print("no is negative")
 
 
    
# Program for even or odd

n = int(input("Enter the no"))
if n % 2 == 0:
    print("no is even")
else :
    print("no is odd")
    


#Program for how much profit or loss made.

cost_price = int(input("Enter the cost price of object : "))
selling_price = int(input("Enter the selling price of object : "))

if cost_price < selling_price :
    print("In This transaction profit happen and The total profit gain = ",selling_price - cost_price)
elif cost_price > selling_price :
    print("In this transaction loss is made and Loss happen and loss is",cost_price - selling_price)
else:
    print("No Profit or Loss happen in this")
    
    

# Marks if else
marks=int(input("Enter the marks of student ot of 100:"))
if marks > 80:
    print("You got Excelent marks ")
elif marks > 60:
    print("You got Very Good marks :")
elif marks >50 :
    print("you got good marks:")
else :
    print("you got poor marks")
    