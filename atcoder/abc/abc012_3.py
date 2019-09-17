N = int(input())

r = 2025 - N

for i in range(1, 10):
    if r % i == 0 and r // i <= 9:
        print(i, "x", r // i)
        