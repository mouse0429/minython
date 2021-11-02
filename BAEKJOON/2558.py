import sys
A, B = input().split()
divisorA = int(A)
divisorB = int(B)
min = 1
max = 1
check = 0
while(True):
	if check != 0:
		max = min*divisorA*divisorB
		break
	else:
		if divisorA >= divisorB and divisorB != 1:
			for i in range(2,divisorB+1):
				if divisorA % i == 0 and divisorB % i == 0:
					min *= i
					divisorA = divisorA // i
					divisorB = divisorB // i	
					break	
				elif i == divisorB:
					check = 1
					break		
		elif divisorA < divisorB and divisorA != 1:
			for i in range(2,divisorA+1):
				if divisorA % i == 0 and divisorB % i == 0:
					min *= i
					divisorA = divisorA // i
					divisorB = divisorB // i
					break
				elif i == divisorA:
					check = 1
					break
		else:
			check = 1
print(min)
print(max)