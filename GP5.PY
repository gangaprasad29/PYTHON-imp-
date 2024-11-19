# ##33
# ##DICTIONARIES## it is orderd

# dic={"harry":"human",
#      "spoon":"object"}
# print(dic["harry"])

# info={"name":"ganga","age":19}
# print(info)
# print(info["name"]) #will rise error when wrong i/p
# print(info.get("name2")) #will give none while wrong i/p
# print(info.keys())
# print(info.values())

# info = {'name':'Karan', 'age':19, 'eligible':True}
# # print(info) 
# # print(info.keys())
# # print(info.values())

# # for key in info.keys():
# #   print(f"The value corresponding to the key {key} is {info[key]}")

# print(info.items())
# for key, value in info.items():
#   print(f"The value corresponding to the key {key} is {value}") 


#####DICTIONARY METHODS ############

# ep1 = {122:45,123:89,567:69,670:69}
# ep2={222:67,566:90}
# # # #ep1.update(ep2)
# # # ep1.clear()
# # ep1.pop(122)
# ep1.popitem() #it removes last item
# del ep1[567]
# print(ep1)

# empt={} 
# print(empt)


##35
## FOR LOOOP WITH ELSE IN PYTHON

# for i in range (5):
#     print(i)

# else:
#     print(" sorry no i ")


# for i in []:
#     print(i)
# else:
#     print(" sorry no i ")


# for i in range (6):
#     print(i)
#     if i==4:
#      break

# else:
#     print(" sorry no i ")


# i=0
# while i<7:
#     print(i)
#     i=i+1
# #     if i==4:
# #      break
# else:
#      print(" sorry no i ")
    

# for x in range(5):
#     print("iteration on {} in for loop".format(x+1))
# else:
#     print("else block in loop")
#     print("out of loop")


##36
## EXCEPTION HANDELING IN PYTHON or error handeling 

# a=input("enter rhe no.")
# print("multiplicarion table of {a} is :")
# try:
#  for i in range (1,11):
#     print(f"{int(a)}x{i}={int(a)*i}")
# except:
#   print("sorry some error occers")
# print("some imp lines of code ")
# print("end of program")

# try:
#     num=int(input("enter an integer:"))
# except ValueError:
#     print("no. enterd is not an integer")
# except IndexError:
#     print("index error")


##37
###finally keyword in python

try:
    l=[1,5,6,7]
    i=int (input("enter the index:"))
    print(l[i])
except:
  print("some error occurred")

# finally:
#  print("i am always excuted")
print("i am always excuted")
#### frk kya hain dono main(try and finally) is following


def func1():
 try:
    l=[1,5,6,7]
    i=int (input("enter the index:"))
    print(l[i])
    return 1 #sucessfully chal gaiya
 except:
  print("some error occurred")
  return 0 #matlab erroe aagaiya

 finally:
  print("i am always excuted")
  #print("i am always excuted")
x = func1()
print(x)



