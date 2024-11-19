#Q print following pattern
"""
*
**
***
****
*****
"""

# a=int(input("enter the no. of rows"))
# for i in range(1,a+1):
#     for j in range(1,i+1):
#         print("*",end=" ")
#     print()   

 #Q print following pattern
"""
*
***
*****
"""   

# a=int(input("enter no. of rows"))
# k=1
# for i in range(1,a+1):
#     for j in range(1,k+1):
#         print("*",end=" ")
#     k+=2
#     print() 

#Q
# a=int(input("enter no. of rows"))
# for i in range(1,a+1):
#     for j in range(a):
#         print("#",end =" ")
#     print()    

#Q
a=int(input("enter no. of rows"))
for i in range(0,a):
    for j in range(0,a-i-1):
        print(end=" ")
    for j in range(0,i+1):
         print("*",end=" ")

    print()    





