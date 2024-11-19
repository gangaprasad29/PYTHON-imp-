#FOR FACTORIAL OF A NO.#
n=int(input("enter a no."))
fact=1
for i in range(1,n+1):
    fact*=i
    print(fact)

#M2
    i=1
    fact=1
    while(i<=n):
        fact*=1
        i+=1
        print(fact)


#NESTED LOOP#
        for i in range(5):
            for j in range(1,11):
                print(j)

                #TO PRINT TABLE FROM 1 TO 5
                for i in range(1,6):
                    for j in range(1,11):
                        print(f"{i}*{j}={i*j}")
                print()


for i in range(4):
    for j in range(4):
        print("*",end=" ")
        print()
        #output will
        # ****
        # ****
        # ****
        # ****


for i in range(1,5):
    for j in range(1,i+1):
        print("*",end=" ")
        print()
#the output
        # *
        # **
        # ***
        # ****

        #TO FIND 1ST, 2ND, THIRD,LAST PLAYER IN THE RACE
        n=6
        l=[10,25,34,14,65,32]
        last=l.index(max(l))
        first=l.index(min(l))
        print("first",first+1)
        print("last",last+1) 
        #now to find runner up
        l[first]=10**6#take vary large value
        second_or_runnerup = l.index(min(l))
        print("second",second_or_runnerup+1)



        