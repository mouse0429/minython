import sys
P = [1,1,1,2,2,3]
T = int(input())
for i in range(T):
	n = int(sys.stdin.readline())
	if (len(P) >= n):
		print(P[n-1])
	else:
		for i in range(len(P),n):
			P.append(int(P[i-5]+P[i-1]))
		print(P[n-1])