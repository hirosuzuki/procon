def solve(N, A):
    result = 0
    while True:
        if any(x % 2 == 1 for x in A):
            return result
        A = [x / 2 for x in A]
        result += 1

N = int(input())
A = [int(x) for x in input().split()]

print(solve(N, A))