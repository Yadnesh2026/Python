#Ex1
class Laptop:
    def __init__(self,brand,ram,price):
        self.brand = brand
        self.ram = ram
        self.price = price

    def showDetails(self):
        print("Brand",self.brand)
        print("RAM",self.ram)
        print("Price",self.price)

lappy = Laptop("Hp","16GB",65000)
lappy.showDetails()

#Ex2
class Student:
    def __init__(self,name,marks1,marks2,marks3):
        self.name = name
        self.marks1 = marks1
        self.marks2 = marks2
        self.marks3 = marks3

    def Avg(self):
        avg = (self.marks1 + self.marks2 + self.marks3)/3
        print("The Avg of the Marks are",avg)

s = Student("vedant",97,89,78)
s.Avg()

#Ex3
class Rectangle:
    def __init__(self,len,width):
        self.len = len
        self.width = width

    def Area(self):
        area = self.len * self.width
        print("Area",area)

    def Perimeter(self):
        peri = 2 * (self.len +self.width)
        print("Perimeter",peri)

r = Rectangle(5,10)
r.Area()
r.Perimeter()

# #Ex4
# class BankAcc:
#     def __init__(self,name,balance):
#         self.name = name
#         self.bal = balance

#     def Deposit(self,debited):
#         self.debited -= self.bal
#         print("Deposit Amount",debited)

#     def Credit(self,Credited):
#         self.credited += self.debited
#         print("Credited Amout",Credited)


# b = BankAcc("Vedant",5000)
# b.Deposit(2000)

#Ex5
class Mobile:
    def __init__(self,battery =100,power ="off"):
        self.battery =battery
        self.power = power

    def switchOn(self):
        if(self.power == "off"):
            self.power = "Onn"
            print("Mobile switched ON")
    
    def switchOff(self):
        if(self.power == "Onn"):
            self.power ="Off"
            print("Mobile switched OFF")

    def charging(self):
        print("The phone is charging")


m = Mobile(100,"off")
m.switchOn()
m.switchOff()

#Ex6
class Animal:
    def eat(self):
        print("He is eating")

    def sleep(self):
        print("He is sleeping")

class Dog(Animal):
    def bark(self):
        print("DOg is Braking")

a = Dog()
a.eat()
a.sleep()
a.bark()

#Ex7
class Vehicle():
    def start(self):
        print("the Engine is started")

    def stop(self):
        print("the engine is stopped")
    
class Bike(Vehicle):
    def bikeName(self):
        print("this is bikename ")

b = Bike()
b.start()
b.stop()

#Ex7
class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age

class Teacher(Person):
    def __init__(self,subject,name,age):
        self.subject = subject
        super().__init__(name,age)

t = Teacher("math","vedant",22)
print(t.name)
print(t.age)
print(t.subject)

#Ex8
class ATM:
    def __init__(self,pin):
        self.__pin = pin

    def changePin(self,newPin):
        self.__pin = newPin

    def showPin(self):
        print("This is the PIN",self.__pin)

a = ATM(5462)
a.changePin(8457)
a.showPin()


#Ex10
class Book:
    def __init__(self,title,author,price):
        self.title = title
        self.author = author
        self.price = price

    
