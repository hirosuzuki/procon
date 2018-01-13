# https://practice.contest.atcoder.jp/tasks/practice_2

n, q = [int(x) for x in input().split()]
cs = [chr(ord("A") + i) for i in range(n)]

# import random
# n = 26
# vs = [i for i in range(n)]
# random.shuffle(vs)
# answer = cs[:]
# random.shuffle(answer)
# print(answer)

cmp_counter = 0

def cmp(x, y):
    global cmp_counter
    cmp_counter += 1
    # return ord(x) - ord(y)
    # r = answer.index(x) - answer.index(y)
    # print(x, y, r)
    # return r
    print("?", x, y, flush=True)
    resp = input()
    return 1 if resp == ">" else -1

def sort(xs):
    result = []
    for c in xs:
        l = 0
        r = len(result)
        while l < r:
            m = (l + r) // 2
            if cmp(c, result[m]) > 0:
                l = m + 1
            else:
                r = m
        result.insert(l, c)
    return result

cs = sort(cs)

print("!", "".join(cs))
# print(cmp_counter)