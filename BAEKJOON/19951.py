import sys

N, M = map(int, sys.stdin.readline().split())
ground = list(map(int, sys.stdin.readline().split()))
diff = [0 for _ in range(N)]

for i in range(M):
    a, b, k = map(int, sys.stdin.readline().split())
    diff[a-1] += k
    if b < N:
        diff[b] -= k

for i in range(N):
    if i != 0:
        diff[i] += diff[i-1]
    print(ground[i]+diff[i], end=" ")
