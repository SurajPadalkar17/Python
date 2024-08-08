a = int(input("Enter the 1 st no:"))
b = int(input("enter the 2 nd no"))

operator = input("Enter the operator")

match operator :
    case "+":
        print('addition is :',a + b)
    case "-" :
        print("substraction is ",a-b)
    case "*":
        print('Multiplication  is :',a * b)
    case "/" :
        print("division is ",a / b)
    case _:
        print("Enter valid operator")