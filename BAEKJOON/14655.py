import sys
N = int(sys.stdin.readline())
firstRound = list(map(int, sys.stdin.readline().split()))
secondRound = list(map(int, sys.stdin.readline().split()))

for i in range(N):
	if firstRound[i] < 0:
		firstRound[i] = firstRound[i] * (-1)

print(sum(firstRound)*2)