N = int(input())
As = list(map(int, input().split()))

print(max(sum(As), -min(As)))
