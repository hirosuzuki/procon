Y = int(input())

def solve(Y):
    if Y % 400 == 0:
        return True
    if Y % 100 == 0:
        return False
    if Y % 4 == 0:
        return True
    return False

if solve(Y):
    print("YES")
else:
    print("NO")