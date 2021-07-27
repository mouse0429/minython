import sys
import math

def Prime(X):
    for i in range(2,int(math.sqrt(X))+1):
        if X%i==0:
            return False
    return True

M,N=map(int, sys.stdin.readline().split())
if M<2:
    M=2
for i in range(M,N+1):
    if Prime(i)==True:
        print(i)

