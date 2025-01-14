import sys

maxX = 1000000
N, K = map(int, sys.stdin.readline().split())
ice = [0 for _ in range(maxX+1)]

for _ in range(N):
    g, x = map(int, sys.stdin.readline().split())
    ice[x] = g

start, end = 0, min(2*K, maxX)
val = sum(ice[start:end+1])
result = val

while end < maxX:
    start, end = start + 1, end + 1
    val = val - ice[start-1] + ice[end]
    result = max(result, val)

print(result)
