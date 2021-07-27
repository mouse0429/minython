import sys

def MakeNum(A):
    result=int(A[2])*100+int(A[1])*10+int(A[0])
    return result

A, B=map(str, sys.stdin.readline().split())
A=list(A)
B=list(B)

if MakeNum(A)>MakeNum(B):
    print(MakeNum(A))
else:
    print(MakeNum(B))
