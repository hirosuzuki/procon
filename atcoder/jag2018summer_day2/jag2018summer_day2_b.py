N = int(input())

cs = [5, 2, 5, 2, 5, 10*18]

def calc(n, cs):
    if len(cs) == 1:
        return 1
    result = 0
    for i in range(cs[0]):
        if i <= n:
            result += calc(n - i, cs[1:])
    return result

print(calc(N, cs))
