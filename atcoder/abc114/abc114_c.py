N = int(input())

nums = [3, 5, 7]

def iter_nums():
    xs = nums
    base = 10
    while 1:
        for x in xs:
            yield x
        xs = [n * base + x for n in nums for x in xs]
        base *= 10

def calc(N):
    result = 0
    for n in iter_nums():
        if n > N:
            break
        s = str(n)
        if "3" in s and "5" in s and "7" in s:
            result += 1
    return result

result = calc(N)

print(result)