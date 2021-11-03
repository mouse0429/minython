import sys
T=int(sys.stdin.readline())
X=[(0,0) for _ in range(T)]
for i in range(T):
    x,y=map(int, sys.stdin.readline().split())
    X[i]=(x,y)
newX=sorted(X,key=lambda X: (X[1],X[0]))
for i in range(T):
    print(newX[i][0],newX[i][1])
