def solve(a):
    result = 0
    for i in range(len(a)):
        result+=a[i]
    return result

n=int(input())
a=[]
for i in range(n):
    a.append(i+1)
print(solve(a))
    
