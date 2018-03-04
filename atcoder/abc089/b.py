N = int(input())
S = [_ for _ in input().split()]

r = 3
for x in S:
    if x == "Y":
        r = 4

if r == 3:
    print("Three")
else:
    print("Four")
