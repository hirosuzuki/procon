P, Q, R = [int(_) for _ in input().split()]

result = sum([P, Q, R]) - max(P, Q, R)

print(result)
