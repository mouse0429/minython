import sys
N, k = map(int, sys.stdin.readline().split())
grade = list(map(int, sys.stdin.readline().split()))
grade.sort(reverse=True)
print(grade[k-1])