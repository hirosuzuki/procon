S = input()

result = 10**9
for i in range(len(S) - 2):
    r = int(S[i:i+3])
    result = min(result, abs(753 - r))
print(result)
