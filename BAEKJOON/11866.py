N, K = map(int, input().split())
arr = [i+1 for i in range(N)]
result = []
K -= 1

start = 0
while True:
    lenArr = len(arr)
    currIdx = (start+K) % lenArr
    result.append(str(arr[currIdx]))
    del arr[currIdx]
    if len(arr) == 0:
        break
    else:
        start = currIdx % (lenArr-1)

answer = ", ".join(result)

print("<", end="")
print(answer, end="")
print(">")
