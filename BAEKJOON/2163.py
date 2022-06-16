N, M = map(int, input().split(' '))
print(M-1 + (N-1)*M) if M > N else print(N-1 + (M-1)*N)