eng_marks = int(input("Enter the english marks"))
math_marks = int(input("Enter the maths marks"))

if eng_marks > 80 and math_marks > 80 :
    print('You got A grade')
elif eng_marks > 80  or math_marks > 80 :
    print("B grade")
else :
    print("c grade")



# four digit no
number = int(input("Enter thr number"))

if number >=1000 and number <= 9999 :
    print("the entered no is 4 digit")
else :
    print("Entered digit is not 4 no.") 
    
    
# Finding gretest no among 3


a = int(input("Enter the first no"))
b = int(input("Enter the second no "))
c = int(input("Enter the Third  no "))

if a > b and a > c :
    print("numer a is greter")
elif b > a and b > c:
    print("The no b is greter")
else :
    print("No c is greter")
    
    
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