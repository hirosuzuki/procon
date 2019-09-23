A, B = [int(_) for _ in input().split()]

if A > B:
    A, B = B, A

if (B - A) % 2 == 0:
    print((B + A) // 2)
else:
    print("IMPOSSIBLE ")
