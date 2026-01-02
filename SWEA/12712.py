from collections import deque

T = int(input())
dx1 = [0, 1, 0, -1]
dy1 = [1, 0, -1, 0]
dx2 = [-1, -1, 1, 1]
dy2 = [-1, 1, 1, -1]

for t in range(1, T + 1):
    N, M = map(int, input().split())
    fly = [list(map(int, input().split())) for _ in range(N)]
    answer = 0
    q = deque([])
    for i in range(N):
        for j in range(N):
            q = deque([])
            for k in range(4):
                q.append([i, j, k, 0])
            cnt = fly[i][j]
            while q:
                x, y, d, r = q.popleft()
                new_x, new_y = x + dx1[d], y + dy1[d]
                if new_x < 0 or new_x >= N or new_y < 0 or new_y >= N or r + 1 >= M:
                    continue
                else:
                    q.append([new_x, new_y, d, r + 1])
                    cnt += fly[new_x][new_y]
            answer = max(answer, cnt)

            q = deque([])
            for k in range(4):
                q.append([i, j, k, 0])
            cnt = fly[i][j]
            while q:
                x, y, d, r = q.popleft()
                new_x, new_y = x + dx2[d], y + dy2[d]
                if new_x < 0 or new_x >= N or new_y < 0 or new_y >= N or r + 1 >= M:
                    continue
                else:
                    q.append([new_x, new_y, d, r + 1])
                    cnt += fly[new_x][new_y]
            answer = max(answer, cnt)
    print(f"#{t} {answer}")
