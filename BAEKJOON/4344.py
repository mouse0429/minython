import sys
C=int(input())
for i in range(C):
    score = list(map(int, sys.stdin.readline().split()))
    N=score[0]
    del score[0]
    p = 0
    for j in range(N):
        if score[j] > sum(score)/N:
            p+=1
    print("{:.3f}%".format(round(p/N*100,3)))
