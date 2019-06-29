S = input()

from collections import Counter

cs = Counter(S)

result = list(cs.values()) == [2, 2]

if result:
    print("Yes")
else:
    print("No")