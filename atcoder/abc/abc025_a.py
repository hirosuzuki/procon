S = input()
N = int(input())


result = S[(N - 1) // 5] + S[(N - 1) % 5]

print(result)
