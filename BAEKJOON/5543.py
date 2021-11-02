price = [0] * 5
set = [0] * 6

for i in range(5):
	price[i] = int(input())

for i in range(3):
	set[i] = price[i]+price[3]-50
	set[i+3] = price[i]+price[4]-50

print(min(set))