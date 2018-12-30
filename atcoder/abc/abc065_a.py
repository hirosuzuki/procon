X, A, B = [int(_) for _ in input().split()]

d = -A + B

if d <= 0:
    print("delicious")
elif d <= X:
    print("safe")
else:
    print("dangerous")
    