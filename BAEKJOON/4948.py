import sys
import math

def Prime(X):
    num=0
    prime=[True for i in range(X+1)]
    p=2
    while p*p<=X:
        if(prime[p]==True):
            for i in range(p*2,X+1,p):
                prime[i]=False
        p+=1
    prime[0]=False
    prime[1]=False
    for i in range(X+1):
        if prime[i]:
            num+=1
    return num
while True:
    n=int(sys.stdin.readline())
    if n==0:
        break
    print(Prime(2*n)-Prime(n))
