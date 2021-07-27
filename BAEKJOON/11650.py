import sys
T=int(sys.stdin.readline())
X=[(0,0) for _ in range(T)];
for i in range(T):
    x,y=map(int, sys.stdin.readline().split())
    X[i]=(x,y)
X.sort()
for i in range(T):
    print(X[i][0],X[i][1])
