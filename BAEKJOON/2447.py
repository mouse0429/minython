import sys
sys.setrecursionlimit(10**6)

def star(len):
    if len==1:
        return ['*']

    str = star(len//3)
    L=[]

    for s in str:
        L.append(s*3)
    for s in str:
        L.append(s+' '*(len//3)+s)
    for s in str:
        L.append(s*3)
    return L

n=int(sys.stdin.readline().strip())
print('\n'.join(star(n)))
