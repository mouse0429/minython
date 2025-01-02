import sys

T = int(sys.stdin.readline())
for j in range(T):
    N = int(sys.stdin.readline())
    nums = list(map(int, sys.stdin.readline().split()))
    while True:
        if len(nums) == 2:
            break
        newNums = []
        for i in range(len(nums)//2):
            newNums.append(nums[i]+nums[-i-1])
        if len(nums) % 2 != 0:
            newNums.append(nums[len(nums)//2]*2)
        nums = newNums
    print(f"Case #{j+1}: ", end="")
    if nums[0] > nums[1]:
        print("Alice")
    else:
        print("Bob")
