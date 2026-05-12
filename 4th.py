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


