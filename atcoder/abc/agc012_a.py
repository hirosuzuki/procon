N = int(input())
A = [int(_) for _ in input().split()]

r = sum(sorted(A, reverse=True)[1:N*2:2])

print(r)
