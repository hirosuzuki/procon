A = int(input())
S = input()

def solve(A, S):
    n = A
    if n == 0:
        return True
    r = False
    for c in S:
        if c == "+":
            n += 1
        else:
            n -= 1
        if n == 0:
            r = True
    return r

if solve(A, S):
    print("Yes")
else:
    print("No")
