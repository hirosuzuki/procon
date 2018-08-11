N = int(input())

def solve(N):
    result = ""
    k = 1
    while 1:
        c = N % 2
        result = "01"[c] + result
        N = (N - k * c) // 2
        k = -k
        if N == 0:
            break
    return result

print(solve(N))
