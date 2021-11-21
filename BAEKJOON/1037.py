import sys
num = int(sys.stdin.readline())
L = list(map(int,sys.stdin.readline().split()))
print(max(L)*min(L))