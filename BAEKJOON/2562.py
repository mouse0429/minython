import sys
n=9
A=[]
for i in range(n):
    A.append(int(sys.stdin.readline().strip()))
max=A[0]
num=1
for i in range(n):
    if max<A[i]:
        max=A[i]
        num=i+1
print(max)
print(num)
