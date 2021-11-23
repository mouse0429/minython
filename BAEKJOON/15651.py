import itertools as it
N, M = map(int, input().split())

L = list(it.product([i+1 for i in range(N)], repeat=M))

for i in range(len(L)):
	for j in range(M):
		print(L[i][j], end=' ')
	print()