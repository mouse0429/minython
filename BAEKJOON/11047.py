import sys
N, K = map(int, sys.stdin.readline().split())
arr = [0]*N
newLen = 0
result = 0

for i in range(N):
    temp = int(sys.stdin.readline())
    if temp > K:
        continue
    else:
        arr[i] = temp
        newLen += 1

for i in range(newLen-1, -1, -1):
    if K == 0:
        break
    result += K // arr[i]
    K %= arr[i]

print(result)