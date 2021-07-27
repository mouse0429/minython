N=int(input())
L=[]; i=0
while len(L)<N:
    L=list(filter(lambda s:'666' in str(s), range(10**i)))
    i+=1
print(L[N-1])
