N, K = map(int, input().split())
As = list(map(int, input().split()))
As.sort(reverse=True)

start, end = 0, As[0]
while start <= end:
    mid = (start + end) // 2
    candy = 0
    for i in range(N):
        temp = As[i] - mid
        if temp <= 0:
            break
        else:
            candy += temp
    if candy <= K:
        end = mid - 1
    else:
        start = mid + 1

print(start)
