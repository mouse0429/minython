import sys
import math


def getNewN(r, c):
    return math.floor(math.log2(max(r, c)+1))


def getNumOfZ(newN, newR, newC):
    if newR < newN and newC < newN:
        return 0, newR, newC
    elif newR < newN and newC >= newN:
        return 1, newR, newC-newN
    elif newR >= newN and newC < newN:
        return 2, newR-newN, newC
    else:
        return 3, newR-newN, newC-newN


N, r, c = map(int, sys.stdin.readline().split())
newN = getNewN(r, c)

answer = 0
newR = r
newC = c
for i in range(newN, -1, -1):
    numZ, newR, newC = getNumOfZ(2**i, newR, newC)
    answer += 2**(2*i)*numZ
print(answer)
