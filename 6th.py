#Functions in Python - Block of statment that perform specfic task
# def sum(a,b):
#     sum2 =a+b
#     return sum2

# print(sum(5,5))

# def avg(a,b,c):
#     avg =a+b+c/3
#     return avg

# print(avg(6,5,1))

#Qs1 print the len of a list 
cities =["delhi","gugaon","mumbai","chennai"]

def list(cities2):
    sum =len(cities)
    return sum

print(list(cities))

#Qs2  Print them all in One line
heros = ["Spiderman","captain America","Iron Man","Wizard"]

def print2(h):
    for i in h:
        print(i,end=" ")  #IMP Note - end=" " hleps to print the list in one line 


print(print2(heros))


