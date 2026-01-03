from collections import deque

T = int(input())
dx = [-1, -1, -1, 0, 0, 1, 1, 1]
dy = [-1, 0, 1, -1, 1, -1, 0, 1]

for tc in range(T):
    N = int(input())
    table = [list(input().rstrip()) for _ in range(N)]

    for i in range(N):
        for j in range(N):
            if table[i][j] == ".":
                cnt = 0
                for k in range(8):
                    new_x, new_y = i + dx[k], j + dy[k]
                    if new_x < 0 or new_x >= N or new_y < 0 or new_y >= N:
                        continue
                    if table[new_x][new_y] == "*":
                        cnt += 1
                table[i][j] = cnt

    visited = [[False for _ in range(N)] for _ in range(N)]
    answer = 0
    for i in range(N):
        for j in range(N):
            if visited[i][j] or table[i][j] == "*":
                continue
            if table[i][j] == 0:
                answer += 1
                q = deque([])
                q.append([i, j])
                visited[i][j] = True

                while q:
                    x, y = q.popleft()
                    for k in range(8):
                        new_x, new_y = x + dx[k], y + dy[k]
                        if (
                            new_x < 0
                            or new_x >= N
                            or new_y < 0
                            or new_y >= N
                            or visited[new_x][new_y]
                            or table[new_x][new_y] == "*"
                        ):
                            continue
                        if table[new_x][new_y] == 0:
                            q.append([new_x, new_y])
                        visited[new_x][new_y] = True

    for i in range(N):
        for j in range(N):
            if not visited[i][j] and table[i][j] != "*":
                answer += 1
    print(f"#{tc+1} {answer}")
