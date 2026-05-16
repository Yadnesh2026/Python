

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