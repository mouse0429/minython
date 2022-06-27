def check(N, L, posX, posY):
	for i in range(N):
		for j in range(N):
			if i == posX:
				L[i][j] = 'X'
			elif j == posY:
				L[i][j] = 'X'
			elif i+j == posX+posY:
				L[i][j] = 'X'
			elif j+abs(posX-i) == posY:
				L[i][j] = 'X'
	return L
	
import math
N = int(input())
chess = [['O']*N]*N

chess = check(N, chess, 3, 2)

for i in range(N):
	for j in range(N):
		print(chess[i][j], end='')
	print()

'''
for i in range(math.factorial(N)):
	for j in range(N):
		L[i][j] = 'X':
'''
