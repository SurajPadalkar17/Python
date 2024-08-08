'''fruits =["apple","banana","cherry","mango"]
print(fruits)
print(len(fruits))
print(type(fruits))
fruits[1]="strawberry"
print(fruits)
#check item in list
if "cherry" in fruits:
    print("cherry is part of list")
if "Kiwi" not in fruits:
    print("kiwi is not part of the list")

#indexing in list
print(fruits[1])
print(fruits[-3])
print(fruits[1:3])
print(fruits[-3:-1])

#Adding elements to list

fruits =["apple","banana","cherry","mango"]
fruits.append("kiwi")
print(fruits)
fruits.insert(2,"kiwi")
print(fruits)

more_fruits =["kiwi","papaya"]
fruits.extend(more_fruits)
print(fruits)


#Remove elements from a list
fruits =["apple","banana","cherry","mango"]
fruits.pop()
print(fruits)
fruits.pop(2)
print(fruits)
fruits.remove("banana")
print(fruits) 



#Changing item in list

fruits =["apple","banana","cherry","mango"]
fruits[1] = "kiwi "
print(fruits)
fruits[1:3]=["papaya"]
print(fruits)


# Sorting a list
fruits =["apple","banana","cherry","mango"]
fruits.sort() # by default in ascending
print(fruits)
fruits.sort(reverse=True) #descending

print(fruits)

fruits.reverse()
print(fruits)

#List comprehension (when we want to make a new list from itom of existing list)
fruits =["apple","banana","cherry","mango"]
new_fruits=[fruit for fruit in fruits if "a" in fruit]
print(new_fruits)

# copy a list
new_fruits=fruits.copy()
print(new_fruits)

new_fruits = fruits + new_fruits
print(new_fruits)'''

#nested list(add list in listq)

fruits =["apple","banana","cherry","mango"]
fruits.insert(2,["kiwi","papaya"])
print(fruits)
print(fruits[2][0])