m = int(input())

def calc(m):
    if m < 100:
        return "00"
    if 100 <= m <= 5000:
        return "%02d" % (m // 100)
    if 6000 <= m <= 30000:
        return "%02d" % (m // 1000 + 50)
    if 35000 <= m <= 70000:
        return "%02d" % ((m // 1000 - 30) // 5 + 80)
    if 70000 < m:
        return "89"
    return

print(calc(m))