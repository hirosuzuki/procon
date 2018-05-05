ABC = [int(_) for _ in input().split()]
K = int(input())

a, b, c = sorted(ABC)
print(a + b + c * 2 ** K)
