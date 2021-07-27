import sys
N=int(input())
data = list(map(int, sys.stdin.readline().split()))
max = data[0]
min = data[0]
for i in range(N):
    if max<data[i]:
        max = data[i]
    if min>data[i]:
        min = data[i]
print(min,max)
