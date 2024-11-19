# #VARIABLES IN PYTHON
# x=2 
# print(x+3)
# y=3
# print(x+y)
# x=9
# print(x+y)
# print(x+10)
# #print(_+y) DOUBT

# #STRING VARIABLE (inmutable)
# n="youtube"
# print(n)
# print(n+'rocks')
# print(n[0])
# print(n[-1])
# print(n[0:3])
# print(n[-1:-4])
# print(n[1:])
# print(n[:6])
# print('mar'+n[5:])


#LIST IN PYTHON (mutable)

# l=[25,12,36,95,14]
# if "6" in marks:
#   print("Yes")
# else:
#   print("No")

# print(l)
# print(l[0])
# print(l[1:3])
# v=[9.5,'prasad',25]
# print(v)
# print([l,v])
#print(len(l))
# l.append(45)
# print(l)
# l.clear()
# print(l)
# l.insert(2,77)
# print(l)
# l.remove(77)
# print(l)

# l=[25,12,36,95,14]
# l.pop(3)
# print(l)
# print(l[0:5:2])

# print(marks[-3]) # Negative index
# print(marks[len(marks)-3]) # Positive index
# print(marks[5-3]) # Positive index
# print(marks[2]) # Positive index

# l=["ganga",6,7]
# if "ganga" in l:
#     print("yes")
# else:
#     print("no")

#LIST COMPREHENSION
# lst=[i*i for i in range(4)]
# print((lst)) 

# lst=[i*i for i in range(10)]
# print((lst))
# lst=[i*i for i in range(10) if i%2==0]
# print(lst)


#IF YOU WANT TO DELEST MULTIPLE VALUES
# l=[25,12,36,95,14]
# #del l[1:3]
# print(min(l))
# print(max(l))
# print(sum(l))
# l.sort()
# print(l)



# #TUPLE IN PYTHON  it is like a lidt but (inmutsble)
# #tuple is faster thsn list
# tup=(21,36,14,25)
# print(tup[2])

#HOW TO REVERSE A NO.
# a=345
# print(str(a)[::-1])

# #Taking Input of a Python List # #

# # input the list as string
# string = input("Enter elements (Space-Separated): ")
# # split the strings and store it to a list
# lst = string.split()  
# print('The list is:', lst)   # printing the list





#method 2

# # input size of the list
# n = int(input("Enter the size of list : "))
# # store integers in a list using map,
# # split and strip functions
# lst = list(map(int, input("Enter the integer\
# elements:").strip().split()))[:n]
# # printing the list

# print('The list is:', lst) 


#MATRIX OR 2D LIST

#function advanced part
#1) *args
# def summation(a,b):
#     return a+b
# print(summation(3,5))

# for multiple parameters like 2,3,4,5,6, for finding there summation  we ues args

# def summation(num1,*args):
#     addi = 0
#     print(args)
#     print(num1)
#     for i in args:
#         addi+=1
#     return addi
# print(summation(2,3,4,5))

#Q use *args to multiply a given sert of values
# def mul(*args):
#     add=1
#     for i in args:
#         add*=i
#         total=i
#         return total
#     print(mul(2,3,4)) 


#KWARGS
#learn it yourself



#LAMBDA FUNCTION
def add(a,b):
 return a+b 
print(add(2,4))

add1=lambda a,b,c: a+b+c
print(add1(1,2,3))

add2=lambda a,b,c:a**2+b**2+c**2
print(add2(1,2,3))


length = lambda a :len(a)
s="computer"
print(length(s))
print(len(s))

l=[1,3,4,5,6,88,90]
l.sort
print(l)
print(l[::-1])


l=[1,3,4,5,6,88,90]
n=len(l)
l.sort()
for i in range(n):
 print(l[-i-1])






