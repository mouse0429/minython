import sys

N, M, K = map(int, sys.stdin.readline().split())

hands = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
tempSum = [0 for _ in range(N)]

for j in range(M):
    for i in range(N):
        tempSum[i] += hands[i][j]
        if tempSum[i] >= K:
            print(i+1, j+1)
            exit(0)
