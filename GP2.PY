#19
#BREAK AND CONTINUE
# for i in range(12):
#      if (i == 10):
#       break
#      print("5x",i+1,"=",5*(i+1))
     
#      print("loop ko chood gaiya")
     
# for i in range(12):
#   if(i == 10):
#     print("Skip the iteration")
#     continue
#   print("5 X", i, "=", 5 * i)

# i = 0
# while True:
#   print(i)
#   i = i + 1
#   if(i%100 == 0):
#     break

# FUNCTIONS IN PYTHON #

# def calculateGmean(a, b):
#   mean = (a*b)/(a+b)
#   print(mean)

# def isGreater(a, b):
#   if(a>b):
#     print("First number is greater")
#   else:
#     print("Second number is greater or equal")

# def isLesser(a, b):
#   pass
  

# a = 9
# b = 8
# isGreater(a, b)
# calculateGmean(a, b)
# # gmean1 = (a*b)/(a+b)
# # print(gmean1)
# c = 8
# d = 74
# isGreater(c, d)
# calculateGmean(c, d)
# # gmean2 = (c*d)/(c+d)
# # print(gmean2)

####function by 2nd teacher
# def prasad(): # function defination 
#     print("hello")
#     print("good morning") #function call 
# prasad()

# prasad()

# def add(a,b):
#     x=a+b
#     print(x)
# add(5,4)
# add(543,54)
# add(5465,344)


# def add_sub(a,b):
#     x=a+b
#     y=a-b
#     return x,y
# result1,result2=add_sub(5,4)
# print(result1,result2)

#21
#FUNCTION ARGUMEMENT (4 types of argument)
# def avarage(a,b):
#     print("the avarage is",(a+b)/2)
# avarage(54,55)

# def avarage(a=9,b=8):                #default argument
#     print("the avarage is",(a+b)/2)  #default argument
# avarage(6,3)                            #default argument
# avarage(9)                            #default argument
# avarage(b=5)                            #default argument

# def average(*numbers):
#    #print(type(numbers))
#    sum=0
#    for i in numbers:
#        sum+=i
#        print("Average is:",sum/len(numbers))
# average(5,6,8,90)

# **=dictionary

# def name(**name):
#  print("Helllo",name["fname"],name["mname"],name["lname"])
# name(mname="Nagnath",lname="Urekar",fname="Gangaprasad")

#use of return

# def average(*numbers):
#     sum=0
#     for i in numbers:
#         sum=sum+i
#     #return 7
#     return sum/len(numbers)
# c=average(5,6,4,7)
# print(c)

#22 &23
#LIST IN P YTHON
#list methods in python
# l=[1,2,3,4,5,77]
# l.append(66)
# print(l)
# l.pop(2) #remove index no. 2 element
# print(l)
# m=l.copy()
# m[0]=0
# print(l)
# l.insert(1,99)
# print(l)

# l=[1,2,3,4,5,77]
# m=[200,300,600]
# l.extend(m)
# print(l)
# k=l+m       #concatination
# print(k)   #concatination

#TUPLE & OPERATIONS IN  TUPLE (IMMUTABKE)

# tup=(1,2,34)
# print(type(tup),tup)
# tup[0]=9 will give error because tuple is inmutable
# print(tup[0])
# print(tup[3])
# print(tup[1])
# print(tup[1:2])

### tup=(1) aagar kroge to class int hoga to 1 ke side , lganese class tuple print hoga
#tup=(1,)
#print(type(tup),tup)

# tup=(1,2,34)
# if 34 in tup:
#     print("yes present")

# tup=("apple","banana","mango","orange")
# t=list(tup)
# t.append(44)                 #add item
# t.insert(3,"papaya")         #add  item at given index
# t.pop(3)                     #remove given index item
# t[2]="tomato"
# tup=tuple(t)
# print(tup)

# t1=("India","china")
# t2=('pakistan',"nepal")
# southestasia=t1+t2
# print(southestasia)

# tuple1 = (0, 1, 2, 3, 2, 31, 1, 3, 2, 3)
# res = tuple1.count(3)
# print('Count of 3 in tuple1 is:', res)
# res = tuple1.index(3)
# print(res)
# res = tuple1.index(31)
# print('Count of 3 in tuple1 is:', res)
# res = tuple1.index(3, 4, 8) # 3 ki occerance index no. in b/n 4 to 8
# print('Count of 3 in tuple1 is:', res)
# res = len(tuple1)
# print('Count of 3 in tuple1 is:', res)


#exercies 2

# import time
# t = time.strftime('%H:%M:%S') 
# hour = int(time.strftime('%H'))
# # hour = int(input("Enter hour: "))
# # print(hour)

# if(hour>=0 and hour<12):
#   print("Good Morning Sir!")
# elif(hour>=12 and hour<17):
#   print("Good Afternoon Sir!")
# elif(hour>=17 and hour<0):
#   print("Good Night Sir!")


#exercies 3 (kon banega karodpati)
# Q .1. create a program capable of displaying questions to the user like KBC  .                                                                                                                                       
# Q .2. USE  list data type to store the question and their correct answers.
# Q .3. display the final amount the person is taking home after playing the game


