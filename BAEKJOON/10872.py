def f(N):
    if (N==0)|(N==1):
        return 1
    return N*f(N-1)

N=int(input())
print(f(N))
