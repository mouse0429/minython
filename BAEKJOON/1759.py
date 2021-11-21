import sys
import itertools

L, C = map(int, sys.stdin.readline().split())
text = sys.stdin.readline().split()

vowel = []
con = []
last = []
code = []
tempResult = []
result = []

for i in range(C):
	if text[i] == 'a' or text[i] == 'e' or text[i] == 'i' or text[i] == 'o' or text[i] == 'u':
		vowel.append(text[i])
	else:
		con.append(text[i])


for i in range(len(vowel)):
	for j in range(len(con)-1):
		for k in range(j+1,len(con)):
			code.append(vowel[i])
			code.append(con[j])
			code.append(con[k])
			text.remove(vowel[i])
			text.remove(con[j])
			text.remove(con[k])
			last = list(itertools.combinations(text,L-3))
			for m in range(len(last)):
				tempResult = code+list(last[m])
				tempResult.sort()
				if tempResult in result:
					continue
				result.append(tempResult)
			code.clear()
			text.clear()
			text = vowel + con

result.sort()
for i in range(len(result)):
	print(''.join(result[i]))