#Q1
# i=1
# while i in range(0,11):
#     print(i,end="") 
#     i+=1

    #Q2
    # Printing the pattern
# for i in range(1, 6):
#     for j in range(1, i + 1):
#         print(j, end=' ')
#     print()


#Q3
# Printing multiplication table
# for i in range(1, 12):
#     print(f"\nMultiplication table for {i}:\n")
#     for j in range(1, 11):
#         result = i * j
#         print(f"{i} x {j} = {result}")


#Q4
# num=[1,4,9,12,16,425,434,464,512,524,724]
# for i in num[::1]:
#     if i%4==0:
#         print(i)

#Q5
# Printing the pattern
# for i in range(5, 0, -1):
#     for j in range(5, i - 1, -1):
#         print(j, end=' ')
#     print()


#Q6
# num=[1,4,9,12,16,425,434,464,512,524,724]
# for i in num[::-1]:
#     if i%4==0:
#         print(i)

#Q3 m2
# for i in range(1,13):
#     for j in range(1,11):
#         print(f"{i}*{j}={i*j}")

#Q7
# Finding the factorial of 14 without using a defined function
# n= 14
# f = 1

# for i in range(1, n + 1):
#     f*= i

# print(f"The factorial of {n} is: {f}")


# f=0
# for i in range(5):
#     f*=i
#     print(f)
# fact=1
# for i in range(6):
#     fact*=i
#     print(fact)
# for i in range(6):
#                   for j in range(i+1):
#                        print("*", end  = " ")
#                   print()

# for k in range(20):
#                   for l in range(20):
#                        print("*", end  = " ")
#                   print()

# L = [1,1,1,1,1,1]
# print(L.insert(1))