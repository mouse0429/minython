T = int(input())
for i in range(T):
	N, M = input().split()
	M = int(M)
	N = int(N)
	result = 1
	for j in range(N):
		result *= M
		M -=1
	for j in range(N):
		result //= N-j
	print(int(result))