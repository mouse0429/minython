import sys
T=int(input())
for i in range(T):
    H, W, N = map(int,sys.stdin.readline().split())
    if N%H==0:
        if N//H>9:
            print(H,N//H,sep="")
        else:
            print(H,0,N//H,sep="")
    else:
        if N//H>8:
            print(N%H,N//H+1,sep="")
        else:
            print(N%H,0,N//H+1,sep="")
