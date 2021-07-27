import sys
N=int(sys.stdin.readline())
s=set()
for _ in range(N):
    s.add(sys.stdin.readline().rstrip())
s=list(s)
s=sorted(s)
s.sort(key=(lambda x:len(x)))
print("\n".join(s))
