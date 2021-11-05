fiboArr = [0] * 47
fiboArr[1] = 1

n = int(input())
for i in range(2,n+1):
	fiboArr[i] = fiboArr[i-1]+fiboArr[i-2]

print(fiboArr[n])