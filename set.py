# Set is container for storing multiple values in variable.{}
#the element of det can be print in unordered
#  cannot access element from indexe
# cannot update exiting valued but can remove or add
#duplicates are not allowed
#mix of all data types



# creating a set
names = { "sia","mia","tia"}

print(names)

print(len(names))
print(type(names))

#acccess elements
for i in names:
    print(i)

#check if item exit in set

if "sia" in names:
    print("sia is in the set")
    
#add elements in set
names.add("gia")
print(names)

#add another sequence in set
names_list = ["Ria","kia"]
names.update(names_list)
print(names)

#removing elements from sets

names.remove("tia")
names.discard("ria")# this function will not throw an erroe if value is not present in set
print(names)

#joining two sets

s1= {"a","b","c"}
s2 = {"d","e","a"}
print(s1,s2)

s3 = s1.union(s2)
print(s3)

s1.update(s2)
print(s1)


#keep only duplicate while joining
s1= {"a","b","c"}
s2 = {"d","e","a"}
s1.intersection_update(s2)
print(s1)


#kweep all value except duplications
s1= {"a","b","c"}
s2 = {"d","e","a"}
s1.symmetric_difference_update(s2)
print(s1)


# for ffinding common elements in list using sets
# DUPLICATES 

l1 =[1,5,5]
l2 = [3,4,5,5,10]
l3 = [5,5,10,20]
# we cannot direct convert or add list or find common elemenethence first typecast into sets
#typecastin into sets
s1 =set(l1)
s2 =set(l2)
s3 =set(l3)

#join using intersection_update

s1s2 = s1.intersection(s2)
final_set = s1s2.intersection(s3)
 
final_list = list(final_set)
 
print(final_set)
print(type(final_list))
print(final_list)
 