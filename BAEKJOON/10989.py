import sys

T=int(sys.stdin.readline())
save=[0 for i in range(0,10001)]
for _ in range(T):
    N=int(sys.stdin.readline())
    save[N]+=1

sum=0; i=1
while sum!=T:
    if save[i]!=0:
        for j in range(save[i]):
            sys.stdout.write(str(i)+'\n')
            sum+=1
    i+=1
