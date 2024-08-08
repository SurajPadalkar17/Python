# Pass by value : 
                # it is for immutable objectls like string int float tuple. 
     # when it is assigned to function a copy of the object is created and assigned to local variable in fun()
     # any change made to them in side fun do  not affect the original variable outside fun.
     
# pass by value 
def addone(x):
    x = x+1
    print("inside function value of x is",x)

x = 5
addone(x)
print("outside function value of x is",x)          




# pass by reference .
 # (mutable object)like dict list.
 #a reference to actual object is pass to function.
 # changes inside fun will affect the original objet.


def modifylist(lst):
    lst.append(7)
   # lst = [4,5,6]
    print("Inside function:",lst)
lst = [1,2,3]
modifylist(lst)
print("outside function:",lst)
    
