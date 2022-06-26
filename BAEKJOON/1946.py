import sys
T=int(sys.stdin.readline())
for i in range(T):
	N=int(sys.stdin.readline())
	arr = [tuple(map(int, sys.stdin.readline().split())) for _ in range(N)]
	arr.sort(key=(lambda x:x[0]==1 or x[1]==1))
	print(arr)
	result =1
	for j in range(1,N):
		if arr[j][0] < arr[0][0] or arr[j][1] < arr[0][1]:
			result += 1
	print(result)