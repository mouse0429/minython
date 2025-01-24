import sys


def gcd(a, b):
    while b:
        a, b = b, a % b
    return a


T = int(sys.stdin.readline())
for _ in range(T):
    nums = list(map(int, sys.stdin.readline().split()))
    result = 0
    for i in range(len(nums)-1):
        for j in range(i+1, len(nums)):
            result = max(result, gcd(nums[i], nums[j]))
    print(result)
