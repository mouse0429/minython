import sys
R, C = map(int, sys.stdin.readline().split())
Rg, Cg, Rp, Cp = map(int, sys.stdin.readline().split())
room = [list(str(sys.stdin.readline().rstrip())) for _ in range(R)]

for i in range(R):
    for j in range(C):
        if room[i][j] == "P":
            for m in range(Rp):
                for n in range(Cp):
                    if i+m >= R or j+n >= C or room[i+m][j+n] == "G":
                        print(1)
                        exit(0)
            print(0)
            exit(0)
