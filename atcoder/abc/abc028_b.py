S = input()

cs = [0] * 6

for c in S:
    cs[ord(c) - ord("A")] += 1

print(*cs)
