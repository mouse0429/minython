arr = list(map(int, input().strip()))
arr.sort(reverse=True) 
if arr[-1] != 0:
    print(-1)
elif int(''.join(map(str, arr))) % 30 == 0: 
    print(int(''.join(map(str, arr))))
else:
    print(-1)