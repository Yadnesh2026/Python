#Loops in Python

#While Loop
number = 1

while number<=100:
    # print(number)
    number+=1


# #Print the table
# n=1
# i= int(input("Enter the number :"))

# while (n<=10):
#     print(n*i)
#     n+=1

#Qs4
# nums=[1,4,9,16,25,36,49,64,81,100]
# idx =0

# while idx < len(nums):
#     print(nums[idx])
#     idx +=1

# #Qs5
# num2 = (1,4,9,16,25,36,49,64,81,100);
# i=0
# x=64

# while i < len(num2):
#     if(num2[i]== x):
#         print("Found",i)
#     i +=1

# #Break nd Continue
# j=0

# while(j<=5):
#     if(j ==3):
#         j +=1
#         continue #ski[]
#     print(j)
#     j +=1

# #Qs6
# num3 = (1,4,9,16,25,36,49,64,81,100);
# a=0
# x=25

# while a< len(num3):
#     if(num3[a] == 25):
#         print("Found",a)
#         break
#     else:
#         print("finding...")
#     a +=1

#For Loop in python - for triversers
# list = [1,2,3]

# for el in list:
#     print(el)

#Used with else
# vegitable = "ApnaCollege"

# for vegi in vegitable:
#     if(vegi == "o"):
#         print("Found O")
#         break
#     print(vegi)
# else:
#     print("END")

# list2 = (1,4,9,16,25,36,49,64,81,100)

# for num in list2:
#     if(num == 16):
#         print("Found 16")
#         break
#     print(num)


#Range funcation - Returns a sequence of numbers, Starting from 0 by default and increment by 1(By deafult)
#range(start?, stop, step?) ? - optional
#stop is not printed 

# for i in range(1,100,2):
#     print(i)

# n=5
# for i in range(1,11):
#     print(n*i)

#Pass statment - To pass the null statment that does nothing
# for i in range(5):
#     pass

# print("After the pass")
#Pass is known for adding code after words like acts as a placeholder

#Qs1
n=5

sum=0
for i in range(n+1):
    sum += i

print("total sum",sum)

#Qs2
n=7
sum=0
i=1

while i<=n:
    print(sum)
    sum +=1 






