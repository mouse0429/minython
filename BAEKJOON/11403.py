import sys

N = int(sys.stdin.readline())


def canGoIndices(point, matrix, N):
    indices = []
    for i in range(N):
        if matrix[point][i] == 1:
            indices.append(i)
    return indices


def canGo(start, end, matrix, N, visited):
    indices = canGoIndices(start, matrix, N)
    if end in indices:
        return True
    else:
        for idx in indices:
            if idx in visited:
                continue
            visited.append(idx)
            if (canGo(idx, end, matrix, N, visited)):
                return True
        return False


matrix = [list(map(int, sys.stdin.readline().split())) for N in range(N)]

for i in range(N):
    for j in range(N):
        if (canGo(i, j, matrix, N, [])):
            print(1, end=" ")
        else:
            print(0, end=" ")
    print()
