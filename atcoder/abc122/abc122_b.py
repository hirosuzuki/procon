S = input()

ACGT = "ACGT"

i = 0

result = 0

while i < len(S):
    while i < len(S) and S[i] not in ACGT:
        i += 1
    st = i
    while i < len(S) and S[i] in ACGT:
        i += 1
    result = max(result, i - st)

print(result)

