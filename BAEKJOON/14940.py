import sys
from collections import deque

n, m = map(int, sys.stdin.readline().split())
lands = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
results = [[-1 for _ in range(m)] for _ in range(n)]


dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

q = deque()
for i in range(n):
    for j in range(m):
        if lands[i][j] == 2:
            q.append([i, j])
            results[i][j] = 0
            break
        
while q:
    curr = q.popleft()
    for i in range(4):
        nextX = curr[0] + dx[i]
        nextY = curr[1] + dy[i]
        if nextX < 0 or nextX >= n or nextY < 0 or nextY >= m or lands[nextX][nextY] == 0 or results[nextX][nextY] != -1:
            continue
        else:
            results[nextX][nextY] = results[curr[0]][curr[1]] + 1
            q.append([nextX, nextY])

for i in range(n):
    for j in range(m):
        if lands[i][j] != 0:
            print(results[i][j], end=" ")
        else:
            print(0, end=" ")
    print()
