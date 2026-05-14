#OOPs - Object Oritended Programming - To map with real world scenarios we started using objects i code

#1. Classand Object - Class is a blueprint for creating a objects
class Student: #creating class
    name="karan"

s1 =Student() #Object (insatnce)
print(s1.name)

#Car Example
class Cars():
    color = "Blue"
    brand = "BMW"

car1 = Cars()
print(car1.brand)

# Init Function - All the functio have function called _init_()_ function
class Student2:
    def __init__(self,fullname):
        self.name = fullname
        print("This is the full name",self.name)

s1 =Student2("karan")

        