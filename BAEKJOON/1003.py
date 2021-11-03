import sys

T = int(input())

fibo = [0]*41
fibo[1] = 1

for i in range(2,41):
	fibo[i]=fibo[i-1]+fibo[i-2]

for i in range(T):
	N = int(sys.stdin.readline())
	if N == 0:
		print(1,0)
	elif N == 1:
		print(0,1)
	else:
		print(fibo[N-1], fibo[N])

