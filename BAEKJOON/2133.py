N = int(input())
dp = [0 for _ in range(N+1)]

if N % 2 != 0:
    print(0)
else:
    dp[2] = 3
    for i in range(4, N+1, 2):
        dp[i] = 2 + dp[i-2] * 3 + sum(dp[:i-2]) * 2
    print(dp[N])
