# escape sequances chacters
# print("gangaprasad\nurekar")
# print("hey i am a \"good boy\"\nand you also")
# print("hey",3,5, sep=' , ',end="009" )
# print('prasad')

# DATA TYPES(list,tuple,bulian(true or false),...) & variabale
# a=116
# print(a)
# b='prasad'
# print(b)
# c='ganga'
# d=32
# print(c+b)
# print(c+""+b)
# print(a+d)

# dict={"name":"prasad","age":19}
# print(dict)

# 7
# operators
# print(8+4)
# print(8-4)
# print(8*4)
# print(8/4)
# print(8%4)
# print(9//4)
# print(5**2)
# #Q create a calculator
# a=int(input("first no."))
# b=int(input("second no."))
# print(a+b)
# print(a-b)
# print(a*b)
# print(a/b)
# print(a%b)
# print(a//b)
# print(a**b)

# 9
# TYPECASTING (conveersion of one data type into another data type)
# functions like int(),float(),tuple(),dict().... are used used for type casting
# a="1" #string
# b="3" #string
# print(a+b)
# print(int(a)+int(b))

# implicite type casting (one DT is convert into another DT automatically)
# c=2.4
# d=4
# print(c+d)

# 10
# taking user input in python
# a=input("enter your name")
# print("my name is ",a)

# c=int(input())
# d=int(input())
# print(c+d)

# 11
# string in python
# name="gangaprasad"
# print(name[0])
# multi line string
# apple='''he said,
# hi prasad
# i am good'''
# print(apple)

# USE OF FOR LOOP
# name="gangaprasad"
# for character in name:
#     print(character,end='')

# 12
# STRING SLICING
# a="gangaprasad"
# print(len(a))
# print(a[0:7])
# print(a[0:10])
# print(a[0:-3])
# print(a[:10])
# print(a[0:])
# A="harry"
# print(A[-4:-2])
# print(A[-2:-4]) #no output
# print(a[0:10:2]) #start:end:increment
# print(a[::-1]) #REVERSE STRING

# STRING METHODS IN PYTHON
# a="gangaprasad!!!!"
# print(len(a))
# print(a.upper())
# print(a.lower())
# print(a.rstrip("!"))
# print(a.replace("gangaprasad","yogesh"))
# print(a.split(" ")) # convert string into list
# print(a.capitalize()) # it converts only 1st character capital and make all character small
# print(a.count("a"))
# print(a.endswith("!!")) # end with !! or not
# print(a.startswith("!!")) # start with !! or not
# print(a.find("r")) #shows first occarance index
# print(a.isalnum()) # a-z & A-Z & 0-9 hain to true
# print(a.isalpha()) # a-z & A-Z  hain to true
# print(a.islower()) # sare sharacter lower hain to true
# print(a.isprintable()) #aagar sare character printable hain to true nahito false like (\)
# print(a.isspace())
# print(a.istitle()) # aagar 1st character capital hain to T

# 14
# IF ELSE condition
# a=int (input())
# if(a%4==0):
#    print("leap")
# else:
#    print("not leap")

# type 2
# a=int(input('a1'))
# b=int(input('a2'))
# c=int(input('a3'))
# if(a==b and b==c ):
#     print("equiT")
# elif(a==b or b==c or a==c):
#     print("sioT")
# else:
#     print("scalenT")
# print("i am happy now")

# nested if 
# num =int(input("enter a no."))
# if (num < 0):
#     print("Number is negative.")
# elif (num > 0):
#     if (num <= 10):
#         print("Number is between 1-10")
#     elif (num > 10 and num <= 20):
#         print("Number is between 11-20")
#     else:
#         print("Number is greater than 20")
# else:
#     print("Number is zero")

# import time
# timestamp = time.strftime('%H:%M:%S')
# print(timestamp)
# timestamp = time.strftime('%H')
# print(timestamp)
# timestamp = time.strftime('%M')
# print(timestamp)
# timestamp = time.strftime('%S')
# print(timestamp)


# MATCH CASE STAMENTS (like a switch case)
# x = int(input("Enter the value of x: "))
# # x is the variable to match
# match x:
#     # if x is 0
#     case 0:
#         print("x is zero")
#     # case with if-condition
#     case 4:
#         print("case is 4")
   
#     case _: #case _: means default statement
#      print(x)

# FOR LOOP 
# for i in range(1,21):
#    print(i)

# name='Gangaprasad'
# for i in name:
#     print(i,end=",")


# colors = ["Red", "Green", "Blue", "Yellow"]
# for color in colors:
#   print(color)
#   for i in color:
#     print(i)

# 18
# WHILE LOOP
# i=0
# while(i<6):
#     print(i)
#     i+=1

# i = int(input("Enter the number: "))
# print(i)
# while(i<=38):
#   i = int(input("Enter the number: "))
#   print(i)

# print("Done with the loop")

# a=5
# while(a>0):
#     print(a)
#     a-=1
# else:
#     print(" i am inside else")

