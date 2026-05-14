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

#Static Methods - Method that dont use self parameters 





        