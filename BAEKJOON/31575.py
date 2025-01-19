import sys

N, M = map(int, sys.stdin.readline().split())
miro = [list(map(int, sys.stdin.readline().split())) for _ in range(M)]
visited = [[False for _ in range(N)] for _ in range(M)]


def dfs(x, y):
    global miro, visited

    dx = [1, 0]
    dy = [0, 1]

    if x == M-1 and y == N-1:
        print("Yes")
        exit(0)

    for i in range(2):
        newX, newY = x + dx[i], y + dy[i]
        if newX >= M or newY >= N or miro[newX][newY] != 1 or visited[newX][newY]:
            continue
        dfs(newX, newY)
    visited[x][y] = True


dfs(0, 0)
print("No")
