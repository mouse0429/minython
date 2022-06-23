arr = list(input().strip())
zeroNum = 0
oneNum = 0

currElement = 0
for i in range(len(arr)):
    if currElement != arr[i]:
        if arr[i] == '0':
            zeroNum += 1
        else:
            oneNum += 1
    currElement = arr[i]

if len(set(arr)) == 1:
  print(0)
else:
  print(min(zeroNum, oneNum))