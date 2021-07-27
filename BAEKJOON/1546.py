N=int(input())
score=list(map(int,input().split()))
M=max(score)
aver=0
for i in range(N):
    aver+=round(score[i]/M*100,2)
print(aver/N)
