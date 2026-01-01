# 23분

T = int(input())
for test_case in range(1, T + 1):
  MAX = 10**7
  costs = list(map(int, input().split()))
  tables = list(map(int, input().split()))
  dp = [MAX for _ in range(13)]
  dp[0] = 0
  
  for i in range(1,13):
    if i >= 12:
      dp[i] = min(dp[i-12] + costs[3], dp[i])
    if i >= 3:
      dp[i] = min(dp[i-3] + costs[2], dp[i])
    dp[i] = min(dp[i-1] + costs[1], dp[i])
    dp[i] = min(dp[i-1] + costs[0]*tables[i-1], dp[i])
  print(f"#{test_case} {dp[12]}")