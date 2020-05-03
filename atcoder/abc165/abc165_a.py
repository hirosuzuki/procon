K = int(input())
A, B = [int(_) for _ in input().split()]

x = B // K * K

if A <= x <= B:
    print("OK")
else:
    print("NG")
