import sys
N = int(sys.stdin.readline())
short = {}


for _ in range(N):
    full = sys.stdin.readline().rstrip()
    words = full.split()
    for i in range(len(words)):
        if words[i][0].upper() not in short:
            key = words[i][0].upper()
            words[i] = "[" + words[i][0] + "]" + words[i][1:]
            short[key] = " ".join(words)
            print(short[key])
            break
    else:
        flag = 0
        for i in range(len(words)):
            if flag == 1:
                break
            for j in range(len(words[i])):
                if words[i][j].upper() not in short:
                    key = words[i][j].upper()
                    words[i] = words[i][:j] + \
                        "[" + words[i][j] + "]" + words[i][j+1:]
                    short[key] = " ".join(words)
                    print(short[key])
                    flag = 1
                    break
        if flag == 0:
            print(full)
