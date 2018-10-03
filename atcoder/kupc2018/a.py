N = int(input())
S = [int(_) for _ in input().split()]
A = [int(_) for _ in input().split()]

result = max(s * a for s, a in zip(S, A))

print(result)