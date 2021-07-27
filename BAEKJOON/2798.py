import sys
import itertools
N,M=map(int, sys.stdin.readline().split())
Card=list(sys.stdin.readline().split())
Combi=[]; PCard=[]
temp=itertools.combinations(Card,3)
Combi+=temp
T=len(Combi)
for i in range(T):
    s=int(Combi[i][0])+int(Combi[i][1])+int(Combi[i][2])-M
    if s<=0:
        PCard.append(s)
print(max(PCard)+M)


