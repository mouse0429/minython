while True:
    a, b = map(int, input().split())
    if a == 0 and b == 0:
        exit(0)
    print(f"{a // b} {a%b} / {b}")