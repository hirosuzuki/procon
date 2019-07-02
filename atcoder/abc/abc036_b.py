N = int(input())
S = [input() for i in range(N)]

cs = ["".join([S[N - j - 1][i] for j in range(N)]) for i in range(N)]

print(*cs, sep="\n")