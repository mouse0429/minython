import itertools as it
N, M = map(int, input().split())
L = set(it.combinations([i+1 for i in range(N)],M))
L = list(L)
L.sort()

for i in range(len(L)):
	for j in range(M):
		print(L[i][j], end=' ')
	print()