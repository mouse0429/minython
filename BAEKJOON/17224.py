import sys
N, L, K = map(int, sys.stdin.readline().split())

problem =[]
result = 0
solvedNum = 0

for i in range(N):
	easy, diff = map(int, sys.stdin.readline().split())
	problem.append([easy, diff])

problem.sort(key=lambda problem: problem[1])

for i in range(N):
	if solvedNum == K:
		break
	if problem[i][1] <= L:
		result += 140
		solvedNum += 1
	elif problem[i][0] <= L:
		result += 100
		solvedNum += 1
	else:
		continue

print(result)
