import sys

N = int(sys.stdin.readline())
L = [int(sys.stdin.readline()) for _ in range(N)]
L.sort()
result = 0

for i in range(1,N+1):
	m = L.pop()
	if int(m*i) > result:
		result = int(m*i)

print(result)