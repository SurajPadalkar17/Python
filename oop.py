# oop is a programming paradiym where the sofware design revolves around object/data rather than function.
# why? == it helps to mimic real world entities and thier interactions.
# also help in code reusablity and maintablity of code.
# class := it is user defined data types it is blue print or template for an object.
# object is instance of types class mimic real world entity,
'''
class student :
    def set_name(s,name):
        s.name = name
    def get_name (s):
        return s.name
    
student1 = student()
student1.set_name("shehnaaz")
print(student1.get_name())    


class rectangle : 
    
   def set_dimention(self,height,width):
    self.height = height
    self.width = width
   def area(self):
    return self.height * self.width
   def perimeter(self):
    return 2*(self.height + self.width)


#create object
rectangle1 = rectangle()
height = int(input("Enter height :"))
width = int(input("Enter the width :"))
rectangle1.set_dimention(height,width)
print("The height and width are :",rectangle1.height,rectangle1.width)
print("The area is",rectangle1.area())
print("the perimeter is :",rectangle1.perimeter())



# CONSTRUCTOR class name same as the object name.
# def__init__(self,parameter1,parameter2,...):
   # initialize instance variables(attributes)here
   


class rectangle : 
   def __init__(self,height,width):
     self.height=height
     self.width = width
   #def set_dimention(self,height,width):
    #self.height = height
    #self.width = width
   def area(self):
    return self.height * self.width
   def perimeter(self):
    return 2*(self.height + self.width)


#create object
height = int(input("Enter height :"))
width = int(input("Enter the width :"))
rectangle1 = rectangle(height,width)

#rectangle1.set_dimention(height,width)
print("The height and width are :",rectangle1.height,rectangle1.width)
print("The area is",rectangle1.area())
print("the perimeter is :",rectangle1.perimeter())


# Attributes :
  #1)class : defined inside class andall object instances will have their attributes
  #2)instance : specific to a particular instance object 

class student :
    def set_name(s,name):
        s.name = name   # class attributes
    def get_name (s):
        return s.name
    
student1 = student()
student1.set_name("shehnaaz")
print(student1.get_name())    
student1.eng_marks = 45   # instance attributes 
print(student1.eng_marks)



# Access modifiers 
 #1)public :
 #2)private:
 #3)protected :
 
# public modifiers
class ABC:
    def __init__(self) :
        self.public_attributes = None  # this is public ttribute
        
    def public_function (): # this is public function
        pass
    
obj1 = ABC()
obj1.public_attributes
obj1.public_function()


#private modifiers

class ABC:
    def __init__(self) :
        self.__private_attributes = None  # this is public ttribute
        
    def __private_function (): # this is public function
        pass 
obj1 = ABC()
print(obj1.__private_attributes)  # will throw error



#protected modifier
class ABC:
    def __init__(self) :
        self._protected_attributes =10 # this is public ttribute
        
    def _protected_function (): # this is public function
        pass
'''






# INHERITANCE ::==
class Parent:
    def __init__(self) :
        self.super_attribute = True
        print("This is parent class")

class Child(Parent):
    def __init__(self):
        #super().__init__()
        print("this is child class")
        print(self.super_attribute)
child1 = Child()

   