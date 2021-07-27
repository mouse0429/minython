N=int(input())
P=[i for i in range(2,N+1)]
while N!=1:
    for i in range(len(P)):
        if N%P[i]==0:
            N=N//P[i]
            print(P[i])
            break
