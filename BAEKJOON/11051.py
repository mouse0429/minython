import sys
import math

N, K = map(int, sys.stdin.readline().split())

if K > N-K:
    K = N-K
if K == 0:
    print(1)
    exit()

factorialN = math.factorial(N)
factorialK = math.factorial(K)

factorialN 

# result = 1
# temp = 1
# tempK = math.factorial(K)

# for i in range(N, N-K, -1):
#     temp *= i
#     if temp % tempK == 0 and tempK != 1:
#         temp //= tempK
#         tempK = 1

#     if temp > 10007:
#         temp %= 10007
#         result *= temp
#         temp = 1
#     elif i == N-K+1 and result == 1:
#         result = temp

print(result % 10007)