N = int(input())
arr = list(map(int, input().split(' ')))

result = 0
temp = 0
i = 0
j = 1
while i < N-1 and j < N:
    if arr[i] < arr[j]:
        temp = 0
        i = j
        j = i+1
    else:
        temp += 1
        j += 1
    if result < temp:
        result = temp

print(result)
