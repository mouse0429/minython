import sys
N=int(input())
num=0
for i in range(N):
    s=sys.stdin.readline()
    check=list(set(s))
    for j in range(len(s)-1):
        if s[j] != s[j+1]:
            if s[j] in check:
                check.remove(s[j])
            else:
                num-=1
                break
    num+=1
print(num)

