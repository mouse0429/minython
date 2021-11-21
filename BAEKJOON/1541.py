import sys
str = sys.stdin.readline().strip()
equation = []
element = ''

for i in range(len(str)):
	if str[i] == '+':
		equation.append(int(element))
		equation.append('+')
		element = ''
	elif str[i] == '-':
		equation.append(int(element))
		equation.append('-')
		element = ''
	else:
		element += str[i]
equation.append(int(element))

i = 0
result = 0
while True:
	if i == len(equation):
		break
	elif equation[i] == '-':
		i+=1
		while i < len(equation) and equation[i] != '-':
			if equation[i] != '+':
				result -= equation[i]
			i+=1
	elif equation[i] == '+':
		i+=1
	else:
		result += equation[i]
		i+=1
print(result)