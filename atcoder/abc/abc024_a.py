A, B, C, K = [int(_) for _ in input().split()]
S, T = [int(_) for _ in input().split()]

result = A * S + B * T - (C * (S + T)) * (S + T >= K)

print(result)