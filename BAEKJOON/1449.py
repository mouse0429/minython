N, L = map(int, input().split())
water = list(map(int, input().split()))

water.sort()
pipes = [0 for i in range((water[-1]+L)*2+1)]


result = 0
for i in range(len(water)):
    targetIdx = water[i] * 2

    if pipes[targetIdx-1] and pipes[targetIdx] and pipes[targetIdx+1]:
        continue
    elif pipes[targetIdx-1] == 0:
        for i in range(L*2+1):
            pipes[targetIdx+i-1] = 1
    else:
        for i in range(L*2+1):
            pipes[targetIdx+i] = 1
    result += 1

print(result)
