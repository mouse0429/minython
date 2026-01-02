T = int(input())


def turn(table, n):
    new_table = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            new_table[i][j] = table[n - 1 - j][i]
    return new_table


for t in range(1, T + 1):
    N = int(input())
    table = [list(map(str, input().split())) for _ in range(N)]
    answer = [["" for _ in range(3)] for _ in range(N)]
    for k in range(3):
        table = turn(table, N)
        for i in range(N):
            answer[i][k] = "".join(table[i])
    print(f"#{t}")
    for i in range(N):
        print(*answer[i])
