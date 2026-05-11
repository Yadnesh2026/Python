#---------- Arithmetic Operators
a=5
b=2

print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a%b) #Modules of the number - Reminder
print(a**b) #power of number 5

#----------Relational Operstors (==,!=,>,<,<=,>=)
a=50
b=20

print(a==b)
print(a!=b)
print(a>=b)
print(a<=b)

#------------Assigment Operators(=, +=, *=, /=, %=, **=)
num=10
num-=10

print(num)

#-------------Logical Operators(not, and, or)

print(not False) #not 

num2=True
num3=False

# print( not (num2>num3))

print("and oprator :",num2 and num3)
# print(50 and 40)

print("OR Oprator :",num2 or num3)



#Type Conversion
a= 2
b=4.25

#Automaically Change from Integer to Float 
sum = a + b
print(sum) #6.25



#Type Casting
c=int("2")#Change from Sting to Int by Manual Casting 
d=6

print(c+d)

#Input in Python - Used input() Value
# name= input("Enter Your Name :")
# print("Welcome",name)

# #Convert it to Integer using type casting
# val= int(input("Enter the Value:"))
# print(val)

# inp1 = int(input("Enter the first Number: "));
# inp2= int(input("Enter the secound number :"))

# sum = inp1 + inp2
# print(sum);

# inp3 = int(input("Enter the Area"))
# sum = inp3 * inp3

# print(sum);

inp4 = int(input("Enter the 1st No. :"))
inp5 = int(input("enter the 2nd No."))

print(inp4 >= inp5)
