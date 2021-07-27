import sys
a,b,c=-1,-1,-1
while True:
    a,b,c=map(int,sys.stdin.readline().split())
    if a==0:
        break
    if c==max(a,b,c):
        if c**2==a**2+b**2:
            print("right")
        else:
            print("wrong")
    elif b==max(a,b,c):
        if b**2==a**2+c**2:
            print("right")
        else:
            print("wrong")
    else:
        if a**2==c**2+b**2:
            print("right")
        else:
            print("wrong")
        
