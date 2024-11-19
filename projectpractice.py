#Q write a program to find out common letters b/n two strings
# a="NAINA"
# b="REENE"

def common_letters():
    a=input("enter 1st string:")
    b=input("enter 2nd string:")
    s1=set(a)
    s2=set(b)
    lst=s1&s2
    print(lst)
common_letters()
 
 




