import sys
import heapq

T = int(sys.stdin.readline())
val = 1000000007

for _ in range(T):
    N = int(sys.stdin.readline())
    slime = list(map(int, sys.stdin.readline().split()))
    heapq.heapify(slime)

    num = N
    result = 1
    while num >= 2:
        A = heapq.heappop(slime)
        B = heapq.heappop(slime)

        newSlime = A * B
        result *= newSlime % val
        num -= 1

        heapq.heappush(slime, newSlime)

    print(result % val)
