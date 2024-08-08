# strings are sequence  of characters
# strings are immutable ()


name1 = 'Colllege wallah'
name2 = "physics wallah"
name3 = '''MBA
wallaah'''
print(name1,name2,name3)
print(type(name1))
print(type(name2))
print(type(name3))


# indexing in string..

name1 = 'Colllege wallah'
print(name1[0])
print(name1[-1])

# traverse a string

name1 = 'Colllege wallah'
for i in name1:
    print(i)
    
    
    
#list comprehenshion:

name1 = 'Colllege wallah'
list = [char for char in name1]
for i in list:
    print(i)



#find length

name1 = 'Colllege wallah' 
print(len(name1))

# find character or sub string in string using find()

print(name1.find('w'))
print(name1.find('ege'))


# slicing a string
# use to get part of string

name1 = 'Colllege wallah' 
print(name1[2:7])
print(name1[:7])
print(name1[2:])
print(name1[-6:])


#modyfying string 
#1) converting character to upper case.  upper()
str1 = "new york"
str2 = str1.upper()
print(str2)
str3 = str2.lower()
print(str3)

 
# for capitalising the first character of string
str4 = str3.capitalize()
print(str4) 

# for stripping?removing any trailing whitespaces.

str5 = "     hello world !    " # it remove spaces
print(str5.strip())
print(str5)


# replace () will replace old substring with new substring 'count ' no of times
# if count not given all the names will replced in string

str6="Hello world , what a beautiful world this is !"
print(str6.replace("world ","earth",1)) # only first world replace
print(str6.replace("world","earth")) # all world replace with earth


# split ().use to split string into a list of substring.
# syntax =:    string.split(sep,maxsplit)

str7 ="ria, pia, sia, pia, mia"
list = str7.split()#in this, wherever the space is occured the string will separate
print(list)
list1 = str7.split(",",2)# when comma occur the string will separated
print(list1)


# concatenation of two string
str8 = "hello world !"
str9 = "what a grate place this is"
print(str8+str9)


# string formating.
#format().use to insert variable value in string.
fruit1 = "mango"
fruit2 = "apple"
str0 = "the king of fruit is {s},the red fruit is {r}".format(s=fruit1,r=fruit2)
print(str0)