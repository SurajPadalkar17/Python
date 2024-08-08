#arithmatic operator

print("sum :",10+5)
print("substraction :",10-5)
print("multiplication :",10*5)
print("division :",10/5)
print("modulus :",10%5)
print("floor division :",10//5)
print("exponential :",10**5)

# Assignment operator

n1 = 5
n2 = n1
print(n2, n1)
n2 += n1
print(n1,n2)
n2 -= n1
print(n1,n2)
n2 *= n1
print(n1,n2)



# comparisn operator
n1 = 4
n2 = 90
print(n1==n2)
print(n1!=n2)
print(n1<=n2)
print(n1>=n2)


# Logical operator
exp1 = 2 > 1   #T
exp2 = 5 < 4   # f
print("ex1 and exp2 :",exp1 and exp2)
print("ex1 or exp2 :",exp1 or exp2)
print("not ex1 :",not(exp1))

# Identity opearator
x = 5
y = 5
print("if x is y :" , x is y)
print("if x is not y:",x is not y)

#membership operator
fruits = ["apple","banana","cherry"]
print("if banana is present in fruits :","banana" in fruits)
print("if mango is not present in fruits :","mango"not in fruits)

# Bitwiswe operator

a = 5
b = 3
print(" a and b :", a & b)
print(" a or b :", a | b)
print(" a xor b :", a ^ b)
