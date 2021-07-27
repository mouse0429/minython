import sys
N=int(input())
L=list(sys.stdin.readline().split())
prime=[i+2 for i in range(998) if i+2%2!=0]
prime.append(2);prime.sort()
for i in range(len(prime)):
    for j in range(i-1):
        if (prime[j]!=-1) & (prime[i]%prime[j]==0):
            prime[i]=-1
            break
num=0
for i in range(N):
    if int(L[i]) in prime:
        num+=1
print(num)
