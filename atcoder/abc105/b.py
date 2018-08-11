N = int(input())

def solve(N):
    for i in range(0, N + 1, 4):
        j = N - i
        if j % 7 == 0:
            return True
    return False

if solve(N):
    print("Yes")
else:
    print("No")