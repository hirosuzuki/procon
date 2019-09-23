N = int(input())
A = [int(_) for _ in input().split()]

def check():
    cs = []
    for i in range(N):
        if A[i] != i + 1:
            cs.append(i)
    if len(cs) == 0:
        return True
    if len(cs) != 2:
        return False
    return True

if check():
    print("YES")
else:
    print("NO")
