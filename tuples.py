#tuples is used to store multiple items or values in variable. 
# use () bracket
# we cannot change value in tuple ones its fix but in list we can (immutable)
# duplicate allowed
# mix of different data types.


# creating a tuples
'''
colours = ("red","yellow","green")

#creating a tuple with 1 items.
fruit = ("apple") # it shows the type of string hence we need to add comma
         
#check type of tuple)
print(type(colours))
print(type(fruit)) 

fruit = ("apple",)#here the type will be tuple
print(type(fruit)) 

#check length of tuple.

print(len(colours))
print(len(fruit))

# Accesing items in tuple.

print(colours[0]) # positive index
print(colours[-1])# negative index
print(colours[0:2]) # range index
print(colours[-2:]) # range index..if we give only statring point then it will access alll the element upto last.



#Check item present in tuple.

if "green" in colours:
    print("Green colour is in tuple")


#traverse in tuple.
for i in colours:
    print(i)
    
#concanate 2 tuples
more_colours = ("blue","brown")
colours = colours + more_colours
print(colours)


#unpacking of data.

colours = ("red","yellow","green")
colour1,colour2,colour3 = colours
print(colour1,colour2,colour3)'''



# Reverse tuple
input_tuple=(1,2,3,4,5,6)
list=[]

# adding reversed value in list
for x in reversed(input_tuple):
    list.append(x)

output_tuple = tuple(list)# typecast the list
print(output_tuple)