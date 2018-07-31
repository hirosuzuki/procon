S = input()

from collections import Counter

cs = Counter(S)

result = not (((cs["N"] > 0) ^ (cs["S"] > 0)) | ((cs["W"] > 0) ^ (cs["E"] > 0)))

if result:
    print("Yes")
else:
    print("No")