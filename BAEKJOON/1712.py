import sys
A,B,C=map(int, sys.stdin.readline().split())
if C-B > 0:
    print(int(A/(C-B))+1)
else:
    print(-1)
