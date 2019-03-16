w = input()

from collections import Counter

cs = Counter(w)

result = all(cs[c] % 2 == 0 for c in cs)

if result:
    print("Yes")
else:
    print("No")