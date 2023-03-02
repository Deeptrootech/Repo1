# OOPS Concepts

# class
from abc import abstractmethod


class Animal:
    pass


# class and object
print()
class vehicle:
    city = "bvn"
    def __init__(self,name,price):
        self.name = name
        self.price = price
    
    def insurance(self,stroke):
        if stroke == 4:
            print("this vehicle needs insurance")
        else:
            print("No need of insurance")

v1= vehicle("car",700000)   
print(v1.name)
v1.insurance(4)

# Inheritance
print()

class phone:
    def __init__(self,name,ram,sound):
        self.name = name
        self.ram = ram
        self.sound= sound
    
    def price(self):
        print("price of phone is 10100")


class smartphone(phone):
    def __init__(self,name,ram,sound,camera):
        self.camera = camera

        phone.__init__(self,name,ram,sound)


p1 = smartphone("samsung",4,"dolby atmos","108mp")

print(p1.name)
print(p1.camera)

# multilevel Inheritance 
print()

class A:
    def __init__(self,fname,lname):
        self.fname = fname
        self.lname = lname
    def my(self):
        print("c1")
class B(A):
    def __init__(self,fname,lname,fname1,lname1,sname):
        self.fname1 = fname1
        self.lname1 = lname1
        self.sname = sname
        A.__init__(self,fname,lname)
    def my1(self):
        print("c2")
    def my(self):
        print("c21")
class C(B):
    def __init__(self,fname,lname,fname1,lname1,sname,cname):
        self.cname = cname
        B.__init__(self,fname,lname,fname1,lname1,sname)
    def my2(self):
        print("c3")
    def my(self):
        print("c32")

c1 = C("deep","pathak","deep1","pathak1","hello","bvn")
print(c1.fname)
print(c1.fname1)
print(c1.cname)
c1.my1()

# Multiple Inheritance

print()

class A:
    def __init__(self,fname,lname):
        self.fname = fname
        self.lname = lname
    def my(self):
        print("a1")
    def my1(self):
        print("a2")
class B:
    def __init__(self,fname1,lname1,sname):
        self.fname1 = fname1
        self.lname1 = lname1
        self.sname = sname
    def my(self):
        print("b1")
    def my2(self):
        print("b2")

class c(A,B):
    def __init__(self,fname1,fname,lname,lname1,sname,age):
        A.__init__(self,fname,lname)
        B.__init__(self,fname1,lname1,sname)
        self.age = age

p1= c("WE","4d","fw","3r","gg",45)

print(p1.age)
p1.my()
p1.my1()
p1.my2()


# Method overloading
print()
print("Python does not support method overloading...")
# overloading ma function nu name ne e badhu same hoi but parameters diffrent hoi to python na function ma if else condition lagavi overloading achieve kari shakai

# Method overriding
print()

class Class1:                          
    def display(self):
        print("Hello from Class1")

class Class2:
    def display(self):
        print("Hello from Class2")

c1 = Class1()
c2 = Class2()

c1.display()
c2.display()

# overriding in multiple inheritance
print()
class Parent1():
    def show(self):
        print("Inside Parent1")
    def display(self):
        print("Inside Parent1")
		
class Parent2():
	def display(self):
		print("Inside Parent2")
		
class Child(Parent1, Parent2):
	def show(self):
		print("Inside Child")
        
obj = Child()

obj.show()
obj.display()


# Polymorphism.
# polymorphism is a concept of overriding.......(We can also say example of len() as polymorphism)
print()
class Bird:
   
    def intro(self):
        print("There are many types of birds.")
 
    def flight(self):
        print("Most of the birds can fly but some cannot.")
 
class sparrow():
   
    def flight(self):
        print("Sparrows can fly.")
 

s1 = sparrow()
s1.flight()


# Instance method
print()
class Person1:
    def data(self):
        print("this is instance method")

i1= Person1()  # In instance method we need to create an instance of a class then only      
i1.data()      # we can call that method that's why no need to pass "self"

# static method
class Person1:
    @staticmethod
    def data():
        print("this is static method")

Person1.data()   # We can call static methods without creatying instance of a class

# abstract method

from abc import ABC, abstractmethod # If we inharite abstract clas then we must implement    
class POLYGON(ABC):                 # it's all methods...
    @abstractmethod
    def number_of_sides(self):
        pass
class RECTANGLE(POLYGON):
    def number_of_sides(self):
        print("Abstract method called from polygon named abstract class")

r1=RECTANGLE()
r1.number_of_sides()