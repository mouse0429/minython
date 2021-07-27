N=int(input())
for i in range(N):
    L=list(str(i))
    s=i
    for j in range(1,len(L)+1):
        s+=int(L[j-1])
    if s == N:
        print(i)
        break
    elif i==N-1:
        print(0)
