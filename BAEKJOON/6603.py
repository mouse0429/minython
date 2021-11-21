from itertools import combinations
import sys

T = []
S = []

S = sys.stdin.readline().split()
k = S[0]
S.remove(k)

while k!= '0':
	T.append(S)
	S = []
	S = sys.stdin.readline().split()
	k = S[0]
	S.remove(k)

for i in range(len(T)):
	L = list(combinations(T[i],6))
	for j in range(len(L)):
		for k in range(len(L[j])):
			print(L[j][k], end=' ')
		print("")
	print("")