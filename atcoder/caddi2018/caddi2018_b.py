N = int(input())
A = [int(input()) for i in range(N)]

result = False
for a in A:
    if a % 2 == 1:
        result = True

if result:
    print("first")
else:
    print("second")
