n=int(input("Enter number of elements: "))
j=0
L=[0 for i in range(n)]
for i in range(n):
    a=int(input("Enter element: "))
    if a!=0:
        L[j]=a
        print("j=",j)
        j+=1
for i in L:
    print(i,end=" ")