#Functions in Python - Block of statment that perform specfic task
# def sum(a,b):
#     sum2 =a+b
#     return sum2

# print(sum(5,5))

# def avg(a,b,c):
#     avg =a+b+c/3
#     return avg

# print(avg(6,5,1))

# #Qs1 print the len of a list 
# cities =["delhi","gugaon","mumbai","chennai"]

# def list(cities2):
#     sum =len(cities)
#     return sum

# print(list(cities))

# #Qs2  Print them all in One line
# heros = ["Spiderman","captain America","Iron Man","Wizard"]

# def print2(h):
#     for i in h:
#         print(i,end=" ")  #IMP Note - end=" " hleps to print the list in one line 


# print(print2(heros))

#Qs3 - Factorial of n
# def factorial(n):
#     fact = 1
#     for i in range(1,n+1):
#         fact *=i
#     print(fact)

# print(factorial(8))

#Qs4 - Convert USD TO INR
# def converter(usd_value):
#     inr_value = usd_value * 83
#     print(usd_value,"USD =", inr_value)

# converter(9)

# user = int(input("Enter the Number :"))
# def check(user2):
#     if(user2 % 2==0):
#         print("ODD")
#     else:
#         print("EVEN")

# check(user);

#Recursion - When a function calls itself repeatedly 
# def num(n):
#     if(n == 0): #In recusrion this is called as base case
#         return
#     print(n)
#     num(n-1)
#     print("END") #Call stack Example

# num(5)

#Recursion and Factorial
# def rec(n):
#     if(n==1 or n==0):
#         return 1
#     return rec(n-1)*n

# print(rec(5))

#Qs1
# def calsi(n):
#     if(n ==0): #base Case
#         return 0
#     return calsi(n-1) +n

# print(calsi(5))

#Qs2
list2 = ["anisha","vedant","Shourya"]
def all(list,idx):
    # if(list ==3):
    #     return
    for i in list:
        print(i)
        idx +=1
 
all(list2,0)