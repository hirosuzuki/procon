SE = [[int(_) for _ in input().split()] for i in range(3)]

result = sum([s * e // 10 for s, e in SE])
print(result)