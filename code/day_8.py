def part_1(input_text):
    grid = [list(map(int, line)) for line in input_text]

    trees_seen = set()

    # Check horizontally
    for y in range(len(grid)):
        # Always add outermost trees
        trees_seen.add((0, y))
        trees_seen.add((len(grid[y]) - 1, y))

        max_value = 0

        # Check left to right
        for x in range(len(grid[y])):
            if grid[y][x] > max_value:
                trees_seen.add((x, y))
                max_value = grid[y][x]

        max_value = 0

        # Check right to left
        for x in range(len(grid[y]) - 1, -1, -1):
            if grid[y][x] > max_value:
                trees_seen.add((x, y))
                max_value = grid[y][x]

    # Check vertically
    for x in range(len(grid[0])):
        # Always add outermost trees
        trees_seen.add((x, 0))
        trees_seen.add((x, len(grid) - 1))

        max_value = 0

        # Check top to bottom
        for y in range(len(grid)):
            if grid[y][x] > max_value:
                trees_seen.add((x, y))
                max_value = grid[y][x]

        max_value = 0

        # Check bottom to top
        for y in range(len(grid) - 1, -1, -1):
            if grid[y][x] > max_value:
                trees_seen.add((x, y))
                max_value = grid[y][x]

    print(len(trees_seen))

def part_2(input_text):
    grid = [list(map(int, line)) for line in input_text]

    max_score = 0
    for tree_y in range(len(grid)):
        for tree_x in range(len(grid[tree_y])):
            value = grid[tree_y][tree_x]

            # Check left to right
            count_right = 0
            for x in range(tree_x + 1, len(grid[tree_y])):
                count_right += 1
                if grid[tree_y][x] >= value:
                    break

            # Check right to left
            count_left = 0
            for x in range(tree_x - 1, -1, -1):
                count_left += 1
                if grid[tree_y][x] >= value:
                    break

            # Check top to bottom
            count_bottom = 0
            for y in range(tree_y + 1, len(grid)):
                count_bottom += 1
                if grid[y][tree_x] >= value:
                    break

            # Check bottom to top
            count_top = 0
            for y in range(tree_y - 1, -1, -1):
                count_top += 1
                if grid[y][tree_x] >= value:
                    break

            scenic_score = count_left * count_right * count_bottom * count_top

            if scenic_score > max_score:
                max_score = scenic_score

    print(max_score)
