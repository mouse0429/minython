L = list(input())

result = 1
for i in range(len(L)-1):
	if ord(L[i]) >= ord(L[i+1]):
		result+=1

print(result)
