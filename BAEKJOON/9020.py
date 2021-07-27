import sys
import math
def Prime(X):
    p=2
    while p*p<=X:
        if X%p==0:
            return False
        p+=1
    return True

T=int(sys.stdin.readline())
for _ in range(T):
    X=int(sys.stdin.readline())
    if X%2==0:
        A=int(X/2)
    else:
        A=int(X/2)+1
    B=X-A
    while True:
        if (Prime(A)&Prime(B))==True:
            break
        A+=1
        B-=1
    print(B,A)
    
