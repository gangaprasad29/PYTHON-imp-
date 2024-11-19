# ##38
# ###coustom reeor 

# a= int(input("enter any value between 5 & 9:"))
# if (a<5 or a>9):
#     raise ValueError("value could be between 5&9")


##41
### SHORT HAND IF ELSE

# a=330
# b=3303
# print("A") if a>b else print("=") if a==b else print("B")
# c=9 if a>b else 0
# print(c)

# a=3305
# b=3303
# print("A") if a>b else print("=") if a==b else print("B")
# c=9 if a>b else 0
# print(c)

##42
### ENUMERATE FUNCTION

# marks=[12,33,56,78,98,1,6]
# index=0
# for mark in marks:
#     print(mark)
#     if(index == 4):
#         print("prasad, awesome!")
#     index+=1

#### or

# marks=[12,33,56,78,98,1,6]
# for index,mark in enumerate(marks):
#     print(mark)
#     if(index == 4):
#         print("prasad, awesome!")

#46
##OS MODULES
## it is an uilt in module in python

# import os

# if(not os.path.exists("data")):
#     os.mkdir("data") 

# for i in range(0,100):
#     os.mkdir(f"data/Day{i+1}")

#### IF WE HAVE TO RENAME THEN

# import os

# for i in range(0,100):
#     os.rename(f"data/Day{i+1}",f"data/tutorial{i+1}")

# import os
# folders = os.listdir("data")

# for folder in folders:
#     print(folders)
#     print(os.listdir(f"data/{folder}"))
    

###48
#local & global variables

# x=4
# print(x)
 
# def hello():
#     x=5
#     print(f"the local x is {x}")
#     print("Hello ganga")

# print(f"the global x is {x}")
# hello()
# print(f"the global x is {x}")
    
## HOW TO USE GLOBAl VARIABLRE IN  A FUNCTION

# x=10 # global variable
# def my_function():
#     global x
#     x=4
#     y=5
#     print(y) # local variable

# my_function()
# print(x)
# # print(y) # will give error because it is local variable & is not accessible outside of the function










