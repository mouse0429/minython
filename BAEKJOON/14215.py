a, b, c = map(int, input().split())
l = max([a, b, c])
s = a+b+c-l
print(min(2*s-1, a+b+c))
