import sys

N, M = map(int, sys.stdin.readline().split())
square = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
roadI = [0 for _ in range(N)]
roadJ = [0 for _ in range(M)]

for i in range(N):
    for j in range(M):
        roadI[i] += square[i][j]

for j in range(M):
    for i in range(N):
        roadJ[j] += square[i][j]

result = -10**9
for i1 in range(N-1):
    for i2 in range(i1+1, N):
        for j1 in range(M-1):
            for j2 in range(j1+1, M):
                temp = roadI[i1] + roadI[i2] + roadJ[j1] + roadJ[j2] - \
                    square[i1][j1] - square[i2][j1] - \
                    square[i1][j2] - square[i2][j2] + \
                    ((i2 - i1 - 1) * (j2 - j1 - 1))
                result = max(result, temp)
print(result)
