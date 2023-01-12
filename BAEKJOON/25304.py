import sys
X = int(sys.stdin.readline())
N = int(sys.stdin.readline())
realTotal=0
for i in range(N):
    a, b = map(int, sys.stdin.readline().split())
    realTotal += a*b
if X == realTotal:
    print("Yes")
else:
    print("No")