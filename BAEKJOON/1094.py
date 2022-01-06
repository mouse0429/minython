X = int(input())

S = [64]
while(True):
	if(sum(S) > X):
		shortestStick = S.pop()/2
		S.append(shortestStick)
		if(sum(S) < X):
			S.append(shortestStick)
	elif sum(S) == X:
		print(len(S))
		break