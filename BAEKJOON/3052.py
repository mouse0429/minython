import sys
s=[]
result =0
for i in range(10):
    A=int(sys.stdin.readline())%42
    s.append(A)
for i in range(42):
    if s.count(i)>0:
        result+=1
print(result)
