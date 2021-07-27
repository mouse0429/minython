def f(N,start,via,end):
    if N-1==0:
        return print(start,end)
    f(N-1,start,end,via)
    print(start,end)
    f(N-1,via,start,end)
    
N=int(input())
print(2**N-1)
f(N,1,2,3)
