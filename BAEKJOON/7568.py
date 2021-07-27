import sys
N=int(sys.stdin.readline())
x=[0 for _ in range(N)]
y=[0 for _ in range(N)]
z=[1 for _ in range(N)]
for i in range(N):
    x[i],y[i]=map(int,sys.stdin.readline().split())
for i in range(N):
    for j in range(N):
        if x==j:
            continue
        if (x[j]>x[i]) & (y[j]>y[i]):
            z[i]+=1
    print(z[i],end=" ")
