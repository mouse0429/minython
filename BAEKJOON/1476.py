import sys
E, S, M = map(int,sys.stdin.readline().split())
b=0
p=0
while True:
	if p == 1:
		break
	if E == S and S == M:
		print(E)
		break
	for i in range((b*28+S)//19+1):
		c=i
		for j in range((c*19+M)//15+1):
			a=j
			if a*15+E == b*28+S and b*28+S == c*19+M:
				print(a*15+E)
				p=1
	b+=1
