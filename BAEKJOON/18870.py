import sys
N=int(sys.stdin.readline())
L=list(map(int, sys.stdin.readline().split()))
newL=set(L); newL=sorted(list(newL))
dic={}
for i in range(len(newL)):
    dic[newL[i]]=i
for i in range(N):
    print(dic[L[i]],end=" ")
