S = input()

from collections import Counter

cs = Counter(S)

if all(v <= 1 for v in cs.values()):
    print("yes")
else:
    print("no")
