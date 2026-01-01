INITIAL = "start"

T = int(input())
for t in range(1, T + 1):
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    if N > M:
        A, B = B, A
        N, M = M, N
    answer = INITIAL
    for i in range(M - N + 1):
        tmp = 0
        for j in range(N):
            tmp += A[j] * B[j + i]
        if answer == INITIAL:
            answer = tmp
        else:
            answer = max(answer, tmp)
    print(f"#{t} {answer}")
