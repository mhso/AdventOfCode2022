import numpy as np
np.set_printoptions(linewidth=100)

def parse_coords(input_text):
    coords = []
    for line in input_text:
        split = list(map(lambda x: x.split(" "), line.split(":")))
        coords.append(
            tuple(
                map(
                    lambda x: int(x.replace(",", "")[2:]),
                    filter(
                        lambda x: "x=" in x or "y=" in x,
                        split[0] + split[1]
                    )
                )
            )
        )
    return coords

def manhattan_dist(x_1, y_1, x_2, y_2):
    return abs(x_2 - x_1) + abs(y_2 - y_1)

def is_contained(s_x, s_y, b_x, b_y, x, y):
    d_x = abs(b_x - s_x)
    d_y = abs(b_y - s_y)
    return x <= s_x + d_x and y <= s_y + d_x and x >= s_x - d_y and y >= s_y - d_y

def get_sensor_reach(s_x, s_y, b_x, b_y):
    dist_x = s_x - b_x
    dist_y = s_y - b_y
    center_square = (
        (b_x, b_y), (b_x, s_y + dist_y), (s_x + dist_x, s_y + dist_y), (s_x + dist_x, b_y)
    )
    width = abs(center_square[0][0] - center_square[2][0]) // 2
    height = abs(center_square[0][1] - center_square[2][1]) // 2

    if b_x < s_x:
        width = -width
    if b_y < s_y:
        height = -height

    triangles = [
        ((b_x + width, b_y + height), center_square[1], center_square[0]),
        ((center_square[2][0] - width, b_y + height), center_square[2], center_square[3]),
        ((b_x - width, b_y + height), center_square[1], center_square[2]),
        ((b_x - width, center_square[2][1] + height), center_square[0], center_square[3]),
    ]
    print(triangles)

def is_within_reach(s_x, s_y, x, y, dist):
    return manhattan_dist(s_x, s_y, x, y) <= dist

def part_1(input_text):
    coords = parse_coords(input_text)

    y = 2000000
    rows = set()
    excluded_coords = set((b_x, b_y) for _, _, b_x, b_y in coords)
    excluded_coords.update(set((s_x, s_y) for s_x, s_y, _, _ in coords))
    min_x = min(min(x[0], x[2]) for x in coords)
    max_x = max(max(x[0], x[2]) for x in coords)
    longest_dist = max(abs(x[0] - x[2]) for x in coords)

    for s_x, s_y, b_x, b_y in coords:
        distance = manhattan_dist(s_x, s_y, b_x, b_y)
        for x in range(min_x - longest_dist, max_x + longest_dist + 1):
            if is_within_reach(s_x, s_y, x, y, distance) and not (x, y) in excluded_coords:
                rows.add(x)

    print(len(rows))

def get_reach(s_x, s_y, b_x, b_y, max_val):
    dist = manhattan_dist(s_x, s_y, b_x, b_y) + 1
    x_1 = s_x
    x_2 = s_x
    reach = set()
    for y in range(s_y - dist, s_y + dist+1):
        if y == s_y:
            x_1, x_2 = x_2, x_1

        if 0 <= y <= max_val:
            if 0 <= x_1 <= max_val:
                reach.add((x_1, y))
            if 0 <= x_2 <= max_val:
                reach.add((x_2, y))

        x_1 -= 1
        x_2 += 1

    return reach

def part_2(input_text):
    coords = parse_coords(input_text)

    max_value = 4_000_000

    for index, (sx_1, sy_1, bx_1, by_1) in enumerate(coords):
        reach = get_reach(sx_1, sy_1, bx_1, by_1, max_value)
        for x, y in reach:
            in_any = False

            for other_index, (sx_2, sy_2, bx_2, by_2) in enumerate(coords):
                if other_index != index:
                    dist = manhattan_dist(sx_2, sy_2, bx_2, by_2)
                    if is_within_reach(sx_2, sy_2, x, y, dist):
                        in_any = True
                        break

            if not in_any:
                print(x, y)
                print(x * max_value + y)
                exit(0)
