Q, H, S, D = [int(_) for _ in input().split()]
N = int(input())

l = min(Q*4, H*2, S)
l2 = min(D, l*2)

# print(l2, l)

r = (N // 2) * l2 + (N % 2) * l

print(r)

