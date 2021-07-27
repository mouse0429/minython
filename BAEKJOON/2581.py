M=int(input())
N=int(input())
L=[i for i in range(M,N+1) if i>=2]
for i in range(len(L)):
    for j in range(2,L[i]):
        if L[i]==2:
            continue
        elif L[i]%j==0:
            L[i]=-1
            break
sum=0
num=0
for i in range(len(L)):
    if L[i]!=-1:
        if num==0:
            num=L[i]
        sum+=L[i]
if sum==0:
    print(-1)
else:
    print(sum)
    print(num)
