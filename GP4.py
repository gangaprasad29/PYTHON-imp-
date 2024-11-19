#29
#DOCSTRING & PEP-8
#helps to undarstand function

# def square(n):
#   '''Takes in a number n, returns the square of n'''
#   # docstrings are just after a function like in this example it is after line 4 in linne 5
#   print(n**2)
# square(5)
# print(square.__doc__)

#pep-8 (python enhancement proposal )

#30
#RECURSION IN PYTHON 
#recursion is basically a function 
#calling function in the same function is called recursion

#favtorial[7]=7*6*5*4*3*2*1
#factorial[n]=n*factorial(n-1)

# def factorial(n):
#     if(n==0 or n==1):
#         return 1
#     else:
#         return factorial(n-1)*n #we call a function in same function but with different argument which is (n-1)
    
# print(factorial(3))
# print(factorial(4))
# print(factorial(5))


## Q calculation of fibonacci series
# f(0)=0
# f(1)=1
# f(2)=f1+f0
# f(n)=f(n-1) + f(n-2)

# def fibonacci(n):
#     if(n==0):
#         return 0
#     elif(n==1):
#         return 1
#     else:
#         return(fibonacci(n-1)+fibonacci(n-2))
    
# print(fibonacci(3))
# print(fibonacci(4))
# print(fibonacci(5))    
# print(fibonacci(6))    


#### SET IN PYTHON ###
# we creat set for storing data in a list  which is not same
# it does print a repeated values only once
# sets are unordered collecrion of dataitmes
#you can do all operations whicw you do with list but only the condition is values are not repeated
#sets are unchangable
# sets do not contain duplicate items

# s={2,3,4,2}
# print(s) 
# i={"ganga",2,1,4.6,76}
# print(i)
# # for accessing set items
# for value in i:
#     print(i)

# a={}
# print(type(a)) # dictionery
# # for empty set
# b=set()
# print(type(b))

#32#

## METHODS OF SET ##
#summetric difference( vo value jo common nahi hain)=(A U B)-(A n B)
#set understands 1 as True &0 as False

## .union()    |
## .update()    |=
## .intersection()  &
## .intersecdtion_update()  &=
## .difference()  
## .difference_update()
## .symmetric_difference()
## .symmetric_difference_update()
## .issubset()
## .issuperset









# s1={1,2,5,6}
# s2={3,6,7}
# print(s1.union(s2))
# print(s1.intersection(s2))
# print(s1,s2)
# s1.update(s2)
# print(s1,s2)
# s1.intersection_update(s2)
# print(s1,s2)

# cities={"tokyo","madrid","berlin","delhi"}
# cities2={"seoul","kabul","delhi"}
# cities3= cities.difference(cities2) # jo values cities main hain but cities2 main nahi hain
# print(cities3)

# cities={"tokyo","madrid","berlin","delhi"}
# cities2={"tokyo","seoul","kabul","madrid"}
# cities3= cities.difference(cities2) # print those values which are not common
# print(cities3)

##isdisjoint(): it check if atoms of given set is present in another set
  
# cities={"tokyo","madrid","berlin","delhi"}
# cities2={"tokyo","seoul","kabul","madrid"}
# print(cities.isdisjoint(cities2)) # aagar common hain to false nahito true 
# cities3={"seoul","madrid","kabul"}
# print(cities.issuperset(cities3))


# cities={"tokyo","madrid","berlin","delhi"}
# cities.add("mumbai")
# print(cities)
# ## if you want to add more than 1 item use update
# #remove/diskart
# cities.remove("tokyo")
# print(cities)
# cities.discard("madrid")
# print(cities)
# # main diff b/n remove & discard is if you try to deleat which is not in set remove creat error but discard not
# #pop()

# cities={"tokyo","madrid","berlin","delhi"}
# item=cities.pop()
# print(cities)
# print(item)

# #del using this we can delet entire set
# cities={"tokyo","madrid","berlin","delhi"}
# del cities
# print(cities) # name error is o/p

# cities={"tokyo","madrid","berlin","delhi"}
# cities.clear()
# print(cities)

# info = {"Carla", 19, False, 5.9}
# if "Carla" in info:
#     print("Carla is present.")
# else:
#     print("Carla is absent.")
       

