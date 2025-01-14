import sys

dp = [[0 for _ in range(10)] for _ in range(65)]
dp[1] = [1 for _ in range(10)]

for i in range(2, 65):
    dp[i][0] = dp[i-1][0]
    for j in range(1, 10):
        dp[i][j] = dp[i][j-1] + dp[i-1][j]

T = int(sys.stdin.readline())
for _ in range(T):
    n = int(sys.stdin.readline())
    print(sum(dp[n]))
