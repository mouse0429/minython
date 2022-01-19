import math
from itertools import combinations_with_replacement

N = int(input())
List = [i*i for i in range(1,int(math.sqrt(N))+1)]

if N in List:
	print(1)
else:
	for i in range(1,N+1):
		for j in combinations_with_replacement(List, i):
			if sum(j) == N:
				print(i)
				exit()
