#Q plendrom no. or string
# a=input()
# if(a==a[::-1]):
#  print("plendrom")
# else:
#  print("not plendrom")

# a=int(input())
# reversed=int(str(a)[::-1])
# if(a == reversed):
#  print("plendrom")
# else:
#  print("not plendrom")

##############LIST PRACTICE################
#1: Find the length of the list and simply swap the first element with (n-1)th element
# def swapl(l):
#  size=len(l)
#  t=l[0]
#  l[0]=l[size-1]
#  l[size-1]=t
#  return l
# l=[12,23,4,5,6,8,9]
# print(swapl(l))

#m2 for swaping 
# def swapl(l):
#  size=len(l)
#  l[0],l[size-1]=l[size-1],l[0]
#  return l
# l=[2,33,55,44,66,87]
# print(swapl(l))

#m3
# def swapl(l):
#  size=len(l)
#  t=l[0],l[size-1]
#  l[size-1],l[0]=t
#  return l
# l=[2,33,55,44,66,87]
# print(swapl(l))

# l=[2,33,55,44,66,87]
# print(l)
# print(*l)
# a, *b, c = l
 
# print(a)
# print(b)
# print(c)

# def swapList(list):
     
#     start, *middle, end = list
#     list = [end, *middle, start]
     
#     return list
     
# # Driver code
# newList = [12, 35, 9, 56, 24]
 
# print(swapList(newList))
