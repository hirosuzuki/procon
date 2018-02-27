def solve(H, W, s):
    from collections import deque, defaultdict
    dotcount = sum([sum([c == "." for c in row]) for row in s])
    s = [row + "#" for row in s]
    s.append("#" * (W + 1))
    print(s)
    distance = defaultdict(lambda:9999999999999)
    q = deque()
    q.append((0, 0, 0))
    distance[0, 0] = 0
    while q:
        x, y, d = q.popleft()
        print(x, y, d)
        for dx, dy in ((-1, 0), (+1, 0), (0, -1), (0, +1)):
            nx, ny, nd = x + dx, y + dy, d + 1
            if s[ny][nx] == "." and nd < distance[nx, ny]:
                distance[nx, ny] = nd
                q.append((nx, ny, nd))
    return dotcount - distance[W - 1, H - 1] - 1

#H, W = [int(_) for _ in input().split()]
#s = [input() for y in range(H)]


H, W = 5, 5
s = """
.#...
.#...
.....
.#.#.
...#.
""".strip().split()

H, W = 10, 37
s = """
.....................................
...#...####...####..###...###...###..
..#.#..#...#.##....#...#.#...#.#...#.
..#.#..#...#.#.....#...#.#...#.#...#.
.#...#.#..##.#.....#...#.#.###.#.###.
.#####.####..#.....#...#..##....##...
.#...#.#...#.#.....#...#.#...#.#...#.
.#...#.#...#.##....#...#.#...#.#...#.
.#...#.####...####..###...###...###..
.....................................
""".strip().split()

H, W = 3, 3
s = ["..#", "#..", "..."]

print(solve(H, W, s))

