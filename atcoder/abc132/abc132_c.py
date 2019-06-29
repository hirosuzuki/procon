N = int(input())
D = [int(_) for _ in input().split()]

D.sort()

result = D[N//2] - D[N//2-1]

print(result)
