# zip () function is in pythone which can combine two iterative value.(a=z,b=y...)
# reverse operation is performed by using reverse = alphabates[ : : -1]

input_string = input("Enter the string :")

n = int(input("Enter the n :"))

# creating dictionary for mirror operation.
alphabates = "abcdefghijklmnopqrstuvwxyz"
reverse_alphabates = alphabates[::-1] # reverse of alphabates
dict1 = dict(zip(alphabates,reverse_alphabates))

# finding the part of string on which we will do mirror opearation 

prefix = input_string[0 : n-1]
suffix = input_string[n-1 :]


# finding thr mirror string

mirror = ""
for i in range (0,len(suffix)):
    mirror = mirror + dict1[suffix[i]]

#creating the final string 
result = prefix + mirror
print("the result is ",result)