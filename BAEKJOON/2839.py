N=int(input())
if N%5==0:
    print(N//5)
elif N%5==3:
    print(N//5+1)
elif N%5==1:
    print(N//5-1+2)
elif N%5==2:
    if N//5>1:
        print(N//5-2+4)
    else:
        print(-1)
elif N%5==4:
        if N//5>0:
            print(N//5-1+3)
        else:
            print(-1)
elif N%3==0:
    print(N//3)

else:
    print(-1)
