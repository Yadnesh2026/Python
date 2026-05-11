#List n Python - Store set of Values
#list are mutable - means can be change
marks = [94.2,86.2,98.1,96.2,77.1]
print(marks)
print(type(marks))
print(marks[1])

student =["vedant",98.5,"Pune"]
print(student)

#------List Slicing - Never Print the last index in slice
marks2 = [82,96,76,89,91]
print(marks2[1:4])

#Negative Index - Never Print the last index in slice
print(marks2[-3:-1])

#---------List Methods----Means its also called mutate method (Change when needed)
list = [1,2,5,3]

#Append Method - Add value in last
list.append(4)
print(list)

#Sort Method - Sorts in aascending Order
list.sort()
print(list)

#Sort in Descending Order
list.sort(reverse=True)
print(list)

#Reverse Method
list.reverse()
print(list)

#Insert Method list.index(idx,el)
list.insert(1,4) #1- index, 5- value
print(list)

#Remove Method
list.remove(1) # Remove 1 from the list 
print(list)

#Pop Method - Delete the value from Index
list.pop(2) #Remove the value of index 2
print(list)

