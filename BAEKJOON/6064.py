import sys
import math

T = int(sys.stdin.readline())

for _ in range(T):
    M, N, X, Y = map(int, sys.stdin.readline().split())
    lastDay = math.lcm(N, M)

    day = X
    while day <= lastDay:
        if day % N == Y % N:
            print(day)
            break
        day += M
    else:
        print(-1)
