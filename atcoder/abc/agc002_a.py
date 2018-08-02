A, B = [int(_) for _ in input().split()]

if A <= 0 <= B:
    print("Zero")
elif 0 < A:
    print("Positive")
elif B < 0:
    d = B - A
    if d % 2 == 0:
        print("Negative")
    else:
        print("Positive")
