T = [int(input()) for i in range(5)]

t = sorted(T, key=lambda x:(x - 1) % 10)

result = sum((x + 9) // 10 * 10 for x in t[1:]) + t[0]

print(result)
