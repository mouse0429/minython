import sys
N=int(input())
all=[]
for i in range(N):
    all.append(list(sys.stdin.readline().strip()))
    add=0
    result = 0
    for j in range(len(all[i])):
        if all[i][j] == 'X':
            add=0
            continue
        else:
            add+=1
            result+=add
    print(result)
