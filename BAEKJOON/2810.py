N = int(input())
seatInfo = list(input())
cupList = ['*']

index = 0
while(index != N):
	if seatInfo[index] == 'S':
		cupList.append('S')
		cupList.append('*')
		index+=1
	else:
		cupList.append('L')
		cupList.append('L')
		cupList.append('*')
		index += 2

result = cupList.count('*')
if result>N:
	print(N)
else:
	print(result)
