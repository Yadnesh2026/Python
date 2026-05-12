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
nums=[1,4,9,16,25,36,49,64,81,100]
idx =0

while idx < len(nums):
    print(nums[idx])
    idx +=1

#Qs5
num2 = (1,4,9,16,25,36,49,64,81,100);
i=0
x=64

while i < len(num2):
    if(num2[i]== x):
        print("Found",i)
    else:
        print("finding")
    i +=1