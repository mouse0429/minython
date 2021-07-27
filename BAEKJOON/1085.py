import math
x,y,w,h=map(int, input().split())
print(min(abs(x),abs(x-w),abs(y), abs(y-h)))

