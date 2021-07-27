def FindNum(n):
    L=[i+100 for i in range(n-99)]
    for i in range(len(L)):
        D=list(str(L[i]))
        if int(D[0])-int(D[1])!=int(D[1])-int(D[2]):
            L[i]=0
        i+=1
    return(len(set(L))-1)

n=int(input())
if(n<100):
    print(n)
elif(n<1000):
    print(99+FindNum(n))
else:
    print(99+FindNum(999))
