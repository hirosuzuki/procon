N = int(input())
H = [int(_) for _ in input().split()]

result = True
for i in range(1, N):
    if H[i] < H[i - 1]:
        if H[i] == H[i - 1] - 1:
            H[i] += 1
        else:
            result = False
            break

print(["No", "Yes"][result])
