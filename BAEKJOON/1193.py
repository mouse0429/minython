import sys
X=int(sys.stdin.readline())
sum=0
i=1
while sum < X:
    sum+=i
    i+=1
if i%2 == 0:
    a=0
    for j in range(X-sum+i-1):
        a+=1
else:
    a=i
    for j in range(X-sum+i-1):
        a-=1
print(i-a, "/", a, sep="")
