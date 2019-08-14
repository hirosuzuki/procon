N = int(input())
S = input()

def solve(N, S):
    i = 0
    x = 'b'
    while len(x) < len(S):
        i += 1
        if i % 3 == 1:
            x = "a" + x + "c"
        elif i % 3 == 2:
            x = "c" + x + "a"
        else:
            x = "b" + x + "b"
    if x == S:
        return i
    else:
        return -1

print(solve(N, S))
