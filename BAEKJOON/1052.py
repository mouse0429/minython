import sys
import math

N, K = map(int, sys.stdin.readline().split())

leftWater = N
for bottle in range(K):
    literPerBottle = 2 ** math.floor(math.log2(leftWater))
    if bottle == K - 1 and leftWater - literPerBottle > 0:
        print(literPerBottle * 2 - leftWater)
    elif leftWater - literPerBottle == 0:
        print(0)
        break
    leftWater -= literPerBottle
