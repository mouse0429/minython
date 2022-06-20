import math

arr = list(map(int, input().strip()))
arr.reverse()
result = []

for i in range(math.ceil(len(arr)/3)):
    if (3*i+2) <= (len(arr)-1):
        result.append(arr[3*i]+2*arr[3*i+1]+4*arr[3*i+2])
    elif (3*i+1) <= (len(arr)-1):
        result.append(arr[3*i]+2*arr[3*i+1])
    else:
        result.append(arr[3*i])

result.reverse()
print(''.join(str(_) for _ in result))
