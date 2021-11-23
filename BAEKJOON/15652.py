import itertools as it
N, M = map(int, input().split())

L = list(it.combinations_with_replacement([i+1 for i in range(N)],M))

for i in range(len(L)):
	for j in range(M):
		print(L[i][j], end = ' ')
	print()