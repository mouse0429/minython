ip = list(map(str, input().split(":")))

if ip[0] == "" and ip[1] == "":
    ip = ["0000" for _ in range(10-len(ip))] + ip[2:]
elif ip[-1] == "" and ip[-2] == "":
    ip = ip[:len(ip)-2]+["0000" for _ in range(10-len(ip))]
else:
    idx = -1
    for i in range(len(ip)):
        if ip[i] == "":
            idx = i
    if idx != -1:
        ip = ip[:idx+1] + ["0000" for _ in range(8-len(ip))] + ip[idx+1:]

for i in range(8):
    if len(ip[i]) != 4:
        ip[i] = "0"*(4-len(ip[i])) + ip[i]

print(":".join(ip))
