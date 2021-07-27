import math
import sys

T=int(input())
for i in range(T):
    x1,y1,r1,x2,y2,r2=map(int,sys.stdin.readline().split())
    d=math.sqrt((x1-x2)**2+(y1-y2)**2)
    if (abs(r1-r2)<d)&(r1+r2>d):
        print(2)
    elif (x1==x2)&(y1==y2)&(r1==r2):
        print(-1)
    elif (r1+r2==d)|(abs(r1-r2)==d):
        print(1)
    else:
        print(0)
