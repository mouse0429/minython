N = int(input())
nums = list(map(int, input().split()))

result = []
for i in range(len(nums)-1, -1, -1):
    result = result[:nums[i]] + [i+1] + result[nums[i]:]

print(*result)
