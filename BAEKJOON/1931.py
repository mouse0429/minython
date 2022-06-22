import sys
N = int(sys.stdin.readline())
arr = [tuple(map(int, sys.stdin.readline().split())) for _ in range(N)]

arr.sort(key=lambda x: (x[1], x[0]))

result = 1
curr = arr[0][1]

for i in range(1, N):
    if arr[i][0] >= curr:
        result += 1
        curr = arr[i][1]

print(result)