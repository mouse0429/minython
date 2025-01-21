import sys

sys.setrecursionlimit(10**5)

V, E = map(int, sys.stdin.readline().split())

parents = [i for i in range(V+1)]
edges = [list(map(int, sys.stdin.readline().split())) for _ in range(E)]


def find(node):
    global parents
    if parents[node] == node:
        return node
    else:
        parents[node] = find(parents[node])
        return parents[node]


def union(a, b):
    global parents
    x = find(a)
    y = find(b)
    if x < y:
        parents[y] = x
    else:
        parents[x] = y


edges.sort(key=lambda x: x[2])

result = 0
cnt = 0
for i in range(E):
    a, b, c = edges[i][0], edges[i][1], edges[i][2]
    if cnt == V-1:
        break
    if find(a) != find(b):
        result += c
        cnt += 1
        union(a, b)

print(result)
