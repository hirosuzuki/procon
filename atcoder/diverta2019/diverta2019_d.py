N = int(input())

def solve0(N):
    result = 0
    for i in range(2, N):
        if N % i == N // i:
            print("!", N // i, i, N % i)
            result += i
    return result

def solve(N):
    import math
    r = math.ceil(math.sqrt(N))
    result = 0
    for i in range(1, r + 1):
        d, m = divmod(N - i, i)
        if m == 0 and d > i:
            # print("*", i)
            result += d
    return result

#result0 = solve0(N)
result = solve(N)

#print(result0)
print(result)
