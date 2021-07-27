import sys
T=int(input())
for i in range(T):
    R,S=map(str,sys.stdin.readline().split())
    S=list(S)
    for j in range(len(S)):
        for k in range(int(R)):
            print(S[j], end="")
    print()
