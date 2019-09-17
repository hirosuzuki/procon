N = int(input())

result = "%02d:%02d:%02d" % (N // 3600, N // 60 % 60, N % 60)

print(result)
