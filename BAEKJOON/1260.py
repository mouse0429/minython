import sys
from collections import deque

N, M, V = map(int, sys.stdin.readline().split())
graph = [[0 for _ in range(N)] for _ in range(N)]
visitedDFS = []
visitedBFS = []

for i in range(M):
    a, b = map(int, sys.stdin.readline().split())
    graph[a-1][b-1] = 1
    graph[b-1][a-1] = 1


def dfs(curr):
    global visitedDFS, graph
    visitedDFS.append(curr+1)
    for i in range(N):
        if graph[curr][i] == 1 and i+1 not in visitedDFS:
            dfs(i)


def bfs(start):
    queue = deque()
    visited = [0 for _ in range(N)]
    queue.append(start)
    visited[start] = 1

    while len(queue) != 0:
        curr = queue.popleft()
        visitedBFS.append(curr+1)
        for i in range(N):
            if graph[curr][i] == 1 and visited[i] != 1:
                queue.append(i)
                visited[i] = 1


dfs(V-1)
bfs(V-1)

print(*visitedDFS)
print(*visitedBFS)
