import sys

L=[[0]*15 for row in range(14)]
for i in range(14):
    L[i][0]=i+1

for i in range(14):
    for j in range(14):
        for k in range(i+1):
            L[i][j+1]+=L[k][j]
        
T=int(sys.stdin.readline())
for i in range(T):
    k=int(sys.stdin.readline())
    n=int(sys.stdin.readline())
    print(L[n-1][k])
