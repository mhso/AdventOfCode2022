import numpy as np

def parse_lines(input_text):
    lines = []
    for line in input_text:
        split_lines = line.split("->")

        for index, coords_2 in enumerate(split_lines[1:], start=1):
            coords_1 = split_lines[index-1]
            x_1, y_1 = map(int, coords_1.strip().split(","))
            x_2, y_2 = map(int, coords_2.strip().split(","))

            lines.append((x_1, y_1, x_2, y_2))

    return lines

def construct_grid(input_text):
    lines = parse_lines(input_text)

    # Determine dimensions of grid
    min_x = min(map(lambda x: min(x[0], x[2]), lines))
    max_x = max(map(lambda x: max(x[0], x[2]), lines))
    max_y = max(map(lambda x: max(x[1], x[3]), lines)) + 2

    width = max_x - min_x + 1
    height = max_y + 1
    min_x -= width + (height * 2)
    max_x += width + (height * 2)

    grid = np.zeros((height, max_x - min_x + 1))

    # Create lines in grid
    for x_1, y_1, x_2, y_2 in lines:
        x_1 -= min_x
        x_2 -= min_x
        if x_1 == x_2:
            start_y = min(y_1, y_2)
            end_y = max(y_1, y_2)
            grid[start_y:end_y + 1, x_1] = 1
        else:
            start_x = min(x_2, x_1)
            end_x = max(x_1, x_2)
            grid[y_1, start_x:end_x + 1] = 1

    # Create floor
    grid[max_y, :] = 1

    return grid, 500 - min_x

def visualize_grid(grid):
    char_grid = np.full(grid.shape, ".", dtype=np.str0)
    char_grid[grid == 1] = "#"
    char_grid[grid == 2] = "o"

    for index in range(char_grid.shape[0]):
        print(char_grid[index].tolist())

def simulate(grid, start_x):
    simulation_over = False

    while not simulation_over:
        sand_x, sand_y = start_x, 0

        while True:
            if sand_y == grid.shape[0] - 1:
                simulation_over = True
                break

            if grid[sand_y+1, sand_x] == 0:
                sand_y += 1
            elif grid[sand_y+1, sand_x-1] == 0:
                sand_x -= 1
                sand_y += 1
            elif grid[sand_y+1, sand_x+1] == 0:
                sand_x += 1
                sand_y += 1
            else: # Sand has come to rest
                grid[sand_y, sand_x] = 2
                sand_x, sand_y = start_x, 0

def part_1(input_text):
    grid, start_x = construct_grid(input_text)
    start_y = 0
    
    simulation_over = False

    while not simulation_over:
        sand_x, sand_y = start_x, start_y

        while True:
            if sand_y == grid.shape[0] - 3:
                # Sand flows out the bottom
                simulation_over = True
                break

            if grid[sand_y+1, sand_x] == 0:
                sand_y += 1
            elif grid[sand_y+1, sand_x-1] == 0:
                sand_x -= 1
                sand_y += 1
            elif grid[sand_y+1, sand_x+1] == 0:
                sand_x += 1
                sand_y += 1
            else: # Sand has come to rest
                grid[sand_y, sand_x] = 2
                sand_x, sand_y = start_x, start_y

    print(np.count_nonzero(grid == 2))

def part_2(input_text):
    grid, start_x = construct_grid(input_text)
    start_y = 0

    simulation_over = False

    while not simulation_over:
        sand_x, sand_y = start_x, start_y

        while True:
            if sand_y < grid.shape[0] - 1 and grid[sand_y+1, sand_x] == 0:
                sand_y += 1
            elif sand_y < grid.shape[0] - 1 and sand_x > 0 and grid[sand_y+1, sand_x-1] == 0:
                sand_x -= 1
                sand_y += 1
            elif sand_y < grid.shape[0] - 1 and sand_x < grid.shape[1] - 1 and grid[sand_y+1, sand_x+1] == 0:
                sand_x += 1
                sand_y += 1
            else: # Sand has come to rest
                grid[sand_y, sand_x] = 2

                if sand_x == start_x and sand_y == start_y:
                    simulation_over = True
                    break

                sand_x, sand_y = start_x, start_y

    print(np.count_nonzero(grid == 2))
