N = int(input())
A = [int(_) for _ in input().split()]
B = [int(_) for _ in input().split()]

def calc():
    result = 0
    for i in range(N):
        x = min(A[i], B[i])
        A[i] -= x
        B[i] -= x
        result += x
        x = min(A[i + 1], B[i])
        A[i + 1] -= x
        B[i] -= x
        result += x
    return result

print(calc())
