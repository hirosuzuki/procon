N = int(input())
a = [int(_) for _ in input().split()]

a.sort(reverse=True)
print(sum(a[::2]) - sum(a[1::2]))
