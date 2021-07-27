import collections
import sys

T=int(sys.stdin.readline())
L=[0 for _ in range(T)];
freqList=[]

for i in range(T):
    N=int(sys.stdin.readline())
    L[i]=N
L.sort()

freqList=collections.Counter(L).most_common(2)

if len(freqList)<2:
    freq=freqList[0][0]
elif freqList[0][1]==freqList[1][1]:
    freq=freqList[1][0]
else:
    freq=freqList[0][0]

print(round(sum(L)/T))
print(L[int(T/2)])
print(freq)
print(max(L)-min(L))
