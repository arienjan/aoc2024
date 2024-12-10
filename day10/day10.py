def check_path(map, head, value, x, y, peaks, trails, visited):
    if value == 9 and len(visited) == 10:
        peaks.add((head, y, x))
        trails.append((y, x))
        return
    for v in [(1,0),(-1,0),(0,1),(0,-1)]:
        y2 = y + v[0]
        x2 = x + v[1]
        testval = value + 1
        if y2 >= 0 and y2 < len(map) and x2 >=0 and x2 < len(map[0]) and map[y2][x2] == testval and (y2, x2) not in visited:
            v2 = visited.copy()
            v2.append((y2, x2))
            check_path(map, head, testval, x2, y2, peaks, trails, v2)

input = [list(map(int, [-1 if g == '.' else g for g in list(f.strip())])) for f in open('input.txt').readlines()]
peaks = set()
trails = []
i = 0
for y in range(len(input)):
    for x in range(len(input[0])):
        if input[y][x] == 0:
            visited = [(y, x)]
            check_path(input, i, 0, x, y, peaks, trails, visited)
        i+= 1

print(len(peaks))
print(len(trails))