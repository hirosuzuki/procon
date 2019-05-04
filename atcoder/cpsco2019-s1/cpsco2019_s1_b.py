S = input()

from collections import Counter

cs = set(Counter(S).values())

if len(cs) == 1:
    print("Yes")
else:
    print("No")
