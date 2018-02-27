
def solve(N, M, A, B):
    if N * M < A * 2 + B * 2:
        print("NO")
        return
    s = [["."] * M for i in range(N)]
    if N % 2 == 1:
        for i in range(M // 2):
            A -= 1
            s[N - 1][i * 2] = "<"
            s[N - 1][i * 2 + 1] = ">"
        N -= 1
    if M % 2 == 1:
        for i in range(N // 2):
            B -= 1
            s[i * 2][M - 1] = "^"
            s[i * 2 + 1][M - 1] = "V"
        M -= 1
    print(N, M, A, B)

    def check(x, y):
        if x >= M or y >= N:
            return False
        return s[y][x] == "."

    for x in range(M // 2):
        for y in range(N // 2):
            if A >= 2:
                s[y * 2][x * 2] = "<"
                s[y * 2][x * 2 + 1] = ">"
                s[y * 2 + 1][x * 2] = "<"
                s[y * 2 + 1][x * 2 + 1] = ">"
                A -= 2
                continue
            if B >= 2:
                s[y * 2][x * 2] = "^"
                s[y * 2 + 1][x * 2] = "V"
                s[y * 2][x * 2 + 1] = "^"
                s[y * 2 + 1][x * 2 + 1] = "V"
                B -= 2
                continue
            if A == 1 and B == 1:
                if check(x * 2 + 2, y * 2 + 1):
                    s[y * 2][x * 2] = "^"
                    s[y * 2 + 1][x * 2 + 1] = "V"
                    s[y * 2 + 1][x * 2 + 1] = "<"
                    s[y * 2 + 1][x * 2 + 2] = ">"
                    A -= 1
                    B -= 1
                    break
                if check(x * 2 + 1, y * 2 + 2):
                    s[y * 2][x * 2] = "<"
                    s[y * 2][x * 2 + 1] = ">"
                    s[y * 2 + 1][x * 2 + 1] = "^"
                    s[y * 2 + 2][x * 2 + 1] = "V"
                    A -= 1
                    B -= 1
                    break
                print("NO")
                return
            if A == 1 and B == 0:
                s[y * 2][x * 2] = "<"
                s[y * 2][x * 2 + 1] = ">"
                A -= 1
                break
            if A == 0 and B == 1:
                s[y * 2][x * 2] = "^"
                s[y * 2 + 1][x * 2] = "V"
                B -= 1
                break
    if A >= 1 or B >= 1:
        print("NO")
        return
    print("YES")
    for r in s:
        print("".join(r))

N, M, A, B = 5, 5, 7, 4
# N, M, A, B = [int(_) for _ in input().split()]

solve(N, M, A, B)

