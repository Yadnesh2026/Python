#Dictionary in Python - Are used to store data value in key:value pairs
dict={
    "name":"Vedant",
    "cgpa":9.37,
    "Branch":"BTech ITDS",
    "is_adult":True,
    "subjects":["python","C","Java","C++"],
    "topics":("dict","Set")
}
print(dict)
print(dict["name"]) #Can access the key:value from this 

dict["name"] = "Anisha" #Asign new value in the key
dict["cgpa"]= 9.47
dict["surname"]="vidulkar"#Assign the new value in DIct
print(dict)


#null Dict -Can add the value after making Dictinonary
null_Dict ={} 
null_Dict["name"]="Vedant"
print(null_Dict)

#Nested Dictinory
student={
    "name":"Vedant",
    "Subjects":{
        "phy":97,
        "chem":92,
        "Bio":89
    }
}

print(student);
print(student["Subjects"]["phy"]) #Print in the Nested form 

#---------------Dictonory Methods----------------

#.keys() Method - Print the Key from the dictonory 
print("In the Key Format :",student.keys());

print(list(student.keys())) # TO Type cast them in list format
print(len(student.keys()))

#Values Method - Print all the values from the dictinory 
print(("In the Values Format :",student.values()))

#.items Methods - return all key valye pairs as tuples
print("In the Tuple Format :",student.items())
print("list Items format :",list(student.items()))

pairs = list(student.items()) #Print in specfic keyvalue in tuple format
print(pairs[0])

#.get Method - returns the key according to value 
print("get value by key :",student.get("name"))

#Update Method - Insert the new key:value pair
student.update({"city":"Pune"})
print(student)

newDict = {"area":"Viman Nagar","Pin":412105} #Adding the new Dictinory 
student.update(newDict)
print(student)

#List and Dictinory are mutubles

#Sets in Python - set is collection of the unordered items (Unique Order) and ignores duplicate values 

#Note - Sets does does only consist of unqique value 
collection = {1,2,3,4,"order","type","type"}
print(collection)
print(type(collection))
print(len(collection))

collection2 = set() #To create empty SET
print(type(collection2))

#-------------SET Methods
#In sets we cannot add list and Dictinory that are mutable becuse sets elemtn is mutable
#set.add(el) - add the element
collection2.add(1)
collection2.add("Added new")
collection2.add(("name","anisha"))
print(collection2)

#Set Remove
collection2.remove(("name","anisha"))
print(collection2)

#Clear Method
print(collection2.clear())

collection2.clear()
print(len(collection2))





