#File I/O - Python can be used to perform operations on a file(read and write data)

#Open File Operations
# f = open("filename","mode") #mode - read mode, write mode , deafult parametr is read

# r - readfile ,
# w - Create a file and writing again,
# x - new file, 
# a - append the data,
# b - binary mode, 
# t - for open text file, 
# + - open a disk file for updating(reading and writing)

#r+ - read + overwrite the data, pointer start (No truncate)
#w+ - read + overwrite (truncate) (New data old data is delete )
#a+ - read + append, pointer end (No truncate)

# f= open("demo.txt","r") #read mode

# data = f.read() # To see the file data
# print(data)
# print(type(data))
# # f.close() #Close the file

# data2 = f.readline() #read Line by line
# print(data2)

#Write in the file - write the data again new
# f= open("demo.txt","w")
# f.write("I want to learn Javscript tomm")
# f.close()

# # Append the data in same file
# f= open("demo1.txt","a")
# f.write("\n Added the new data here") #\n add in next line
# f.close()

#r+ mode - over write in the start of file
# f = open("demo.txt","r+")
# f.write("abc;kl;")
# print(f.read())
# f.close()

#w+ mode - wrte new text and delete last text in w mode
# f = open("demo.txt","w+")
# f.write("neww added")
# f.close()

#with syntax - Change the name to another 
# with open("demo.txt","r") as f:
#     data =f.read()
#     print(data) #do not use close syntax here

# with open("demo.txt","w") as f:
#     f.write("New data ")

#Deleteing a file using os modules
import os

# os.remove("demo.txt") #Delete the file

#Example 1
# with open("practice.txt","w") as f:
#     f.write("Hi everyone\n ")
#     f.write("We are leanring File I/O\n")
#     f.write("using Java \n")
#     f.write("I like programming in Java")

#Example2 - Change the above data word from java to python
with open("practice.txt","r") as f:
    data = f.read()

    replace = data.replace("Java","python") #Replace is an method of string
    print(replace)

with open("practice.txt","w") as f:
    f.write(replace)




    