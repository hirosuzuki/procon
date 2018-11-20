A, B, K = [int(_) for _ in input().split()]

n = A
while n <= B:
    print(n)
    n += 1
    if n >= A + K:
        n = max(n, B - K + 1)
