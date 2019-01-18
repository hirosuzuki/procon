S = [input() for i in range(3)]

from itertools import permutations

result = "x"

for r in permutations([0, 1, 2]):
    s = S[r[0]] + S[r[1]] + S[r[2]]
    result = min(result, s)

print(result)
