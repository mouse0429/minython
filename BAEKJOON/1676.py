N = int(input())
fact = 1
result = 0

for i in range(N):
	fact *= (i+1)

while fact % 10 == 0:
	fact //= 10
	result += 1

print(result)