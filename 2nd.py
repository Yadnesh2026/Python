#-----------Indexing --------------------------------------------------
str1 = "This is a string.\n Whats up"
print(str1)
print("Lenght of the String:",len(str1));#To print len of String
print(str1[5])# To print the Index

#-----------Slicing - Accessing Parts of a String -------------------------
str2 = "vedant is Nice Person"
print(str2[1:11])
print(str2[5:len(str2)]) #Till Last Index of the sentence 
print(str2[5:])#Till the last index of the string 

#Negative Index
print(str2[-7:-2])

#.endswith function - Checks if the String Ends with that Sentence
print(str2.endswith("son"))

#capitalize FUnction - Capital the String
print(str2.capitalize());

#Replace Function - Replace the String from old to new
print(str2.replace("e","a"))

#Find Function - Find the Word in the String
print(str2.find("v"))

#Count Function - Count the Words that Ocurrs
print(str2.count("e"))

#---------Conditional Statements
#1. if-elif-else
# light =input("Enter the Color: ")

# if(light=="red"):
#     print("Stop")
# elif(light=="yellow"):
#     print("Ready")
# else:
#     print("gooo")

# print("End of Code")

#Nesting loop

#ODD EVEN Number find
# User = int(input("Enter the number: "))

# rem = User%2

# if(rem ==0):
#     print("EVEN")
# else:
#     print("ODD")

#Greater Number Finder
a =5
b=10
c=1

if(a>=b and a>=c):
    print("A is the Greater Number")
elif(b>=a and b>=c):
    print("B is the Greater Number")
else:
    print("C is the Greater Number")


