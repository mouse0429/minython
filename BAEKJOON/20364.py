import sys

N, Q = map(int, sys.stdin.readline().split())
lands = [0 for _ in range(N+1)]
for _ in range(Q):
    x = int(sys.stdin.readline())
    route = []
    while x > 0:
        route.append(x)
        x //= 2
    route = route[::-1]
    for i in range(len(route)):
        if lands[route[i]] == 1:
            print(route[i])
            break
    else:
        lands[route[-1]] = 1
        print(0)