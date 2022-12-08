def part_1(input_text):
    grid = [list(map(int, line)) for line in input_text]
    trees_seen = set()

    # Check horizontally
    for y in range(len(grid)):
        # Always add outermost trees
        trees_seen.add((0, y))
        trees_seen.add((len(grid[y]) - 1, y))

        # Check left to right
        for x in range(1, len(grid[y])):
            if grid[y][x - 1] < grid[y][x]:
                trees_seen.add((x, y))

        # Check right to left
        for x in range(len(grid[y]) - 2, -1, -1):
            if grid[y][x + 1] < grid[y][x]:
                trees_seen.add((x, y))

    # Check vertically
    for x in range(len(grid[0])):
        # Always add outermost trees
        trees_seen.add((x, 0))
        trees_seen.add((x, len(grid) - 1))

        # Check top to bottom
        for y in range(1, len(grid)):
            if grid[y - 1][x] < grid[y][x]:
                trees_seen.add((x, y))

        # Check bottom to top
        for y in range(len(grid) - 2, -1, -1):
            if grid[y + 1][x] < grid[y][x]:
                trees_seen.add((x, y))

    print(trees_seen)

    print(len(trees_seen))

def part_2(input_text):
    print(input_text)
