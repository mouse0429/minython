import sys
L=[]
T=int(sys.stdin.readline())
for _ in range(T):
    N=int(sys.stdin.readline())
    L.append(N)
L.sort()
for i in range(T):
    print(L[i])
