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
f = open("demo.txt","w+")
f.write("neww added")
f.close()
