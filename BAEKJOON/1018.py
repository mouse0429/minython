import sys

M,N=map(int, input().split())
W=[['W']*N for _ in range(M)]
B=[['B']*N for _ in range(M)]
L=[['B']*N for _ in range(M)]
MinL=[]

for i in range(8):
    for j in range(8):
        if (i%2==0) & (j%2!=0):
            W[i][j]='B'
            B[i][j]='W'
        elif (i%2!=0) & (j%2==0):
            W[i][j]='B'
            B[i][j]='W'

for i in range(M):
    L[i]=list(map(str, sys.stdin.readline().strip()))


for i in range(M-7):
    for j in range(N-7):
        WNum,BNum=0,0
        for m in range(8):
            for n in range(8):
                if W[m][n]!=L[i+m][j+n]:
                    WNum+=1
                if B[m][n]!=L[i+m][j+n]:
                    BNum+=1
        MinL.append(min(WNum,BNum))
print(min(MinL))
