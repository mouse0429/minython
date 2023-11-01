import sys
N, M = map(int, sys.stdin.readline().split())

matrixA = [list(map(int, sys.stdin.readline().strip())) for _ in range(N)]
matrixB = [list(map(int, sys.stdin.readline().strip())) for _ in range(N)]

cnt = 0
for i in range(N):
    for j in range(M):
        if matrixA[i][j] != matrixB[i][j] and j <= M-3 and i <= N-3:
            cnt += 1
            for m in range(i, i+3):
                for n in range(j, j+3):
                    matrixA[m][n] = (matrixA[m][n] + 1) % 2

if matrixA != matrixB:
    print(-1)
else:
    print(cnt)
