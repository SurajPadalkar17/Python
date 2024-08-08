# it is sequence data types
# in dictionary it store key value pair. (like phone no diary)
# it denoted in {}
# value is in fixed order(vice versa of set)
# value can be shareable changeable .
#keys are unique.
#it can be any data types.

phones = {
    "john": 908980890,
    "Ria" :78986886,
    "joy" :78989987,
}
print(phones)

print(type(phones))

print(len(phones))

# Access items from dictionary

print(phones["john"])
print(phones.get("john"))

print(phones.keys())

#update value in dictionary

phones  ["john"] = 656565
print(phones)

# add elements in dictionary

phones ["kia"] =2121212
print(phones)

# add another ditionary

more_phones = {
    "suraj":8432135,
    "raj" :36238823
}
phones.update(more_phones)
print(phones)


# remove element 

phones.pop("john")
print(phones)
    
phones.popitem() # this will remove the last added item in dictionary.
print(phones)

#phones.clear() # this will   empty the dictionary

#printing elements of dictionary
for x in phones:
    print(x) #this give only keys
    
for x in phones:
    print(phones[x]) # this give no only

for x in phones.items(): # if want to print both
    print(x)
    

# nested dictionary

phones = {
    "area1" : {
        "x":21212,
        "y" :32133,
        "z":221
    },
    "area2" : {
        "a":21212,
        "b" :32133,
        "c":221
    }
} 
  
print(phones["area1"]["y"])
print(phones["area2"],"c")


# sum dictiony elements

dict = {
    "a" :100,
    "b" :300,
    "c" :20
}
print(sum(dict.values()))
