#OOPs - Object Oritended Programming - To map with real world scenarios we started using objects i code

#1. Class and Object - Class is a blueprint for creating a objects
class Student: #creating class
    name="karan"

s1 =Student() #Object (insatnce)
print(s1.name)

#Car Example
# class Cars():
#     color = "Blue"
#     brand = "BMW"

# car1 = Cars()
# print(car1.brand)

# Init Function - All the functio have function called _init_()_ function  (Constructor)
class Student2:
    #default constructors
    def __init__(self): #Creatign the class of init
        print("This is the full name")


    #parameterzied constructors
    def __init__(self,fullname): #Creatign the class of init
        self.name = fullname
        print("This is the full name",self.name)


s1 =Student2("karan")
s2 = Student2("vedant") #Data Stored in object is known as attribute



#Methods -  Methods are functions that belong to objects 
class Student3:
    def __init__(self,name,marks): #Constructor of the program
        self.name = name
        self.marks = marks
        print("this are the name of student",self.name)
        print("This is the marks of student",self.marks)

    def college(self):
        print("The college name is of",self.name)
    
    def college2(self):
        print("The are marks are total",self.marks)


s3 = Student3("Vedant",98)
s3.college()
s3.college2()

#Example 3 -  Marks of student and avg of them
class Student4:
    def __init__(self,name,phy,chem,bio):
        self.name = name
        self.phy = phy
        self.chem = chem
        self.bio = bio

    def Avg(self):
        avg = (self.phy + self.chem + self.bio) /3
        print("The avg  is",avg)

s4 = Student4("Karan",98,86,80)
s4.Avg();

#Static Methods - Method that dont use self parameters (work at the class level)
class Student5:

    @staticmethod #Also Known as Decorater
    def college5():
        print("This is Static Method")

s5 =Student5()
s5.college5()

#IMP Parts of OOPs
#1. Abstraction - hiding the implenebtion details of a class and only shoing the essential features to the use.
#Example - TO show only main component of class

#2.Encapsulation - Wrapping data and functions into a single unit(objects).
#Example - To store all the values and function in one capsule (Class)

#Qs2
class Account:
    def __init__(self,bal,acc):
        self.balance = bal
        self.acc = acc

    def debit(self,amount):
        self.balance -= amount
        print("The amount is debited",amount,"Balance is",self.balance)

    def credit(self,amount2):
        self.balance += amount2
        print("The Total Amount are ",amount2,"balance is",self.balance)


atm = Account(500, 5612134)
atm.debit(200)
atm.credit(300)

#del keywords - Used to delete object propertie sor object itself
class Student6:
    def __init__(self,name):
        self.name = name


s6 = Student6("Vedant")
del s6.name #To delete the function
# print(s6.name)

#Private(like) attributes and methods - which can be used within the class
class perosn:
    __name = "Vedant" #Make Priavte with double underscore to attribute

    def __hello(self): #make private with methods 
        print("This is the hello")

    def welcome(self):
        self.__hello()

# p = perosn()
# print(p.welcome())



#Inheritance - When one class(child/derived) dervies the properties and methods of another class(parent, base)
class Car:   #Parent Class
    color = "Blue"
    @staticmethod
    def start():
        print("Car Started")

    @staticmethod
    def stop():
        print("Car stopped")

class Toyota(Car): #Child Class
    def __init__(self,name):
        self.name = name

car1 = Toyota("Glanza")
print(car1.color)

#Types of Inheritance

# 1. Single Inheritance
#  Base Class (Parent) -> Derived (Child)

#2. Multi-level Inheritance
# Base Class(Parent) -> Dervied (Child) -> Derived (Child) Also conisst of base class property

class Cars2: #parent 
    @staticmethod
    def on():
        print("the engine is on")

    @staticmethod
    def off():
        print("the engine is off")

class Suzuki(Cars2): #Child 1
    def __init__(self,name):
        self.name = name


class factory(Suzuki): #Child 2 Can also take info frm parent
    def __init__(self,model2):
        self.model2 = model2
        print("Model of this car is",model2)
        


c2 = factory("X%$")
c2.on() #Directlt call the upper most call (Parent)

#3. Multiple Inheritance 
# (Base Class)Parent + (Base Class) Parent -> Derived (Child)

class A:
    varA = "welcome to class A"

class B:
    varB = "welcome to Class B"
    
class C(A,B):
    varC = "welcome to Class C"

c1 = C()

print(c1.varC)
print(c1.varB)


#Super Method - super() is used to access methods of the parent class
class Car3:
    def __init__(self,type):
        self.type = type

    @staticmethod
    def on2():
        print("Car started")

    @staticmethod
    def off2():
        print("Car Stopped")

class BMW(Car3):
    def __init__(self,name,type):
        self.name = name
        super().__init__(type) #inheritat the attribute of main class there is why super is used
        super().off2() 


c4 = BMW("X5","320d")
print(c4.name)


#Different types of methods in python OOPs - IMPORTANT ------------------------------
#1. Static Method
#2. Class Method - (cls)
#3. insatnce method (self,name)

#Class Method - A Class method is bound to the class & recives the class as an implicit first argument
class Person2:
    name = "vedant"

    @classmethod
    def changeName(cls,name):
        cls.name = name

p2 = Person2()
p2.changeName("dsfa")
print(p2.name)

#Property Decoration - we use @property on any method in the class to sued the method as property
class result:
    def __init__(self,phy,chem,math):
        self.phy = phy
        self.chem = chem
        self.math = math
    
    @property #property method - convert this to an attribute 
    def percenatge(self):
        return ((self.phy + self.chem + self.math)/3)
    
result = result(95,78,70)
print(result.percenatge)

#getter and setter decorater learn it 


#4.Polymorphism - Operator Overloading (Ekch ghosti che khup form hh)
#When the same operator is allowed to have different meaning according to the context
class Complex:

    def __init__(self, real, img):
        self.real = real
        self.img = img

    def show(self):
        print("The number is", self.real, "+", self.img, "i")

    def __add__(self, num):
        num1 = self.real + num.real
        num2 = self.img + num.img

        return Complex(num1, num2)


num1 = Complex(1, 5)
num2 = Complex(2, 3)

num3  = num1 + num2
num3.show()

#Qs1
class Cricle:
    def __init__(self,radius):
        self.radius = radius
    
    #1 Area of Cricle
    def Area(self):
        calsi = 3.14 *(self.radius * self.radius)
        print("The Area of Cricle is",calsi)

    #Parimeter of cricle
    def Parimeter(self):
        calsi2 = (2*3.14*self.radius)
        print("The parimeter of the Cricle is",calsi2)

cric = Cricle(6)
cric.Area()
cric.Parimeter()

#Qs2
class Employee:

    def __init__(self,role,dept,salary):
        self.role = role
        self.dept = dept
        self.salary = salary

    def Details(self):
        print("This is Role",self.role)
        print("This is dept",self.dept)
        print("This is salary",self.salary)
        
class Engineer(Employee):

    def __init__(self,name,age,place):
        self.name = name
        self.age = age
        self.place = place

        super().__init__("Engineer","Computer",45000)



cd = Engineer("Vedant","22","Pune")

print(cd.name)
cd.Details()

#Qs3
class Order:
    def __init__(self,item,price):
        self.item = item
        self.price = price

    def __gt__(self,ord2): #Dundur functions
        return self.price > ord2.price
    

ord1 = Order("Chips",20)
ord2 = Order("Onion",15)

print(ord1>ord2)

    







        
    