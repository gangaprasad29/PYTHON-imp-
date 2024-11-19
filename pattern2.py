# a=int(input("enter no. of rows"))
# for i in range(1,a+1):
#     for j in range(i):
#         print("#",end="")
#     print()

# a=int(input("enter no. of rows"))
# for i in range(a):
#     for j in range(a):
#         print("#",end="")
#     print()    

# a=int(input("enter no. of rows"))
# for i in range(1,a+3):
#     for j in range(a):
#         print("#",end="")
#     print()

# a=int(input("enter no. of rows"))
# for i in range(a):
#     for j in range(a-i):
#         print("#",end="")
#     print()
##OR
# a=int(input("enter no. of rows"))
# for i in range(a):
#     for j in range(i,a):
#         print("#",end="")
#     print()


# a=int(input("enter no. of rows"))
# for i in range(a):
#     for j in range(i,a):
#         print('',end=" ")
#     for j in range(i+1):
#         print("#",end="")
#     print() 

a=int(input("enter no. of rows"))
for i in range(a):
    for j in range(i,a):
        print('',end=" ")
    for j in range(i+1):
        print("#",end=" ")
    print() 
