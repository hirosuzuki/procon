def total_digits(n):
    r = 0
    while n:
        r += n % 10
        n = n // 10
    return r

def solve(N, A, B):
    result = 0
    for i in range(N + 1):
        s = total_digits(i)
        if A <= s <= B:
            result += i
    return result

N, A, B = [int(x) for x in input().split()]

print(solve(N, A, B))