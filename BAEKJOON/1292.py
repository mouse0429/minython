A, B = map(int, input().split())
N = 1
result = 0
L = []
while(len(L) <= B):
    for i in range(N):
        L.append(N)
    N += 1

for i in range(A, B+1):
    result += L[i-1]
print(result)
