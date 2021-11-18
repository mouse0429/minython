import sys
N = int(input())
S = 0
A = list(map(int, sys.stdin.readline().split()))
B = list(map(int, sys.stdin.readline().split()))
indexB = [-1]*N
sortedA = sorted(A)

for i in range(N):
	k = 0
	for j in range(N):
		if B[i] <= B[j]:
			k += 1
	k-= 1
	while(k in indexB):
		k -= 1
	indexB[i] = k
	A[i] = sortedA[indexB[i]]

for i in range(N):
	S += A[i]*B[i]
print(S)