A, B, C = [int(_) for _ in input().split()]
 
def solve(A, B, C):
    result = 0
    if A == B == C and A % 2 == 0 and B % 2 == 0 and C % 2 == 0:
        return -1
    while 1:
        if A % 2 == 1 or B % 2 == 1 or C % 2 == 1:
            return result
        A, B, C = A/2+B/2, B/2+C/2, C/2+A/2
        result += 1

print(solve(A, B, C))
