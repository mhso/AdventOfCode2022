def get_neighbors(grid, x, y):
    neighbors = []
    if x > 0:
        neighbors.append((x-1, y))
    if x < len(grid[y]) - 1:
        neighbors.append((x+1, y))
    if y > 0:
        neighbors.append((x, y-1))
    if y < len(grid) - 1:
        neighbors.append((x, y+1))

    return list(filter(
        lambda cell: grid[cell[1]][cell[0]] - grid[y][x] <= 1,
        neighbors
    ))

def find_start_and_end(input_text):
    goal_x, goal_y = 0, 0
    start_x, start_y = 0, 0
    for y, line in enumerate(input_text):
        try:
            goal_x = line.index("E")
            goal_y = y
        except ValueError:
            pass
        finally:
            try:
                start_x = line.index("S")
                start_y = y
            except ValueError:
                pass

    return start_x, start_y, goal_x, goal_y

def part_1(input_text):
    start_x, start_y, goal_x, goal_y = find_start_and_end(input_text)
    grid = [list(map(lambda x: ord(x) - 97, line)) for line in input_text]
    grid[start_y][start_x] = 0
    grid[goal_y][goal_x] = 25

    queue = [(start_x, start_y)]
    visited_cells = {(start_x, start_y)}
    path_to = {}

    while queue != []:
        x, y = queue.pop(0)

        if x == goal_x and y == goal_y:
            break

        for cell in get_neighbors(grid, x, y):
            if cell not in visited_cells:
                visited_cells.add(cell)
                queue.append(cell)
                path_to[cell] = (x, y)

    count = 0
    x, y = goal_x, goal_y
    while (next_cell := path_to.get((x, y))) is not None:
        x, y = next_cell
        count += 1

    print(count)

def part_2(input_text):
    start_x, start_y, goal_x, goal_y = find_start_and_end(input_text)

    start_coords = []
    for y in range(len(input_text)):
        for x in range(len(input_text[y])):
            if input_text[y][x] == "a" or input_text[y][x] == "S":
                start_coords.append((x, y))

    grid = [list(map(lambda x: ord(x) - 97, line)) for line in input_text]
    grid[goal_y][goal_x] = 25

    shortest_path = len(grid) * len(grid[0])

    for start_x, start_y in start_coords:
        grid[start_y][start_x] = 0

        queue = [(start_x, start_y)]
        visited_cells = {(start_x, start_y)}
        path_to = {}

        while queue != []:
            x, y = queue.pop(0)

            if x == goal_x and y == goal_y:
                break

            for cell in get_neighbors(grid, x, y):
                if cell not in visited_cells:
                    visited_cells.add(cell)
                    queue.append(cell)
                    path_to[cell] = (x, y)

        count = 0
        x, y = goal_x, goal_y
        while (next_cell := path_to.get((x, y))) is not None:
            x, y = next_cell
            count += 1

        if count > 0 and count < shortest_path:
            shortest_path = count

    print(shortest_path)
