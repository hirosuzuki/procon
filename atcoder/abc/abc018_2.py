S = input()
N = int(input())
LR = [[int(_) for _ in input().split()] for i in range(N)]

result = S

for l, r in LR:
    result = result[:l-1] + result[l-1:r][::-1] + result[r:]

print(result)
