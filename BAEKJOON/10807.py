N = int(input())
L = input().split()
ch = input()
count = 0
for i in range(N):
    if ch == L[i]:
        count += 1
print(count)