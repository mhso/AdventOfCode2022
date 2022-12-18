import numpy as np
from scipy.ndimage import label
import math

def get_bounds(coords):
    max_x = np.max(coords[:, 0])
    max_y = np.max(coords[:, 1])
    max_z = np.max(coords[:, 2])
    return max_z + 5, max_y + 5, max_x + 5

def dist(x_1, y_1, z_1, x_2, y_2, z_2):
    return math.sqrt((x_2 - x_1) ** 2 + (y_2 - y_1) ** 2 + (z_2 - z_1) ** 2)

def get_area(coords):
    total_area = 0

    for index, (x_1, y_1, z_1) in enumerate(coords):
        covered_sides = 0
        for other_index, (x_2, y_2, z_2) in enumerate(coords):
            if index != other_index:
                if dist(x_1, y_1, z_1, x_2, y_2, z_2) == 1:
                    covered_sides += 1

        total_area += (6 - covered_sides)

    return total_area

def part_1(input_text):
    coords = [tuple(map(int, line.split(","))) for line in input_text]
    total_area = get_area(coords)

    print(total_area)

def part_2(input_text):
    coords = [list(map(int, line.split(","))) for line in input_text]

    grid = np.ones(get_bounds(np.array(coords)))
    for x, y, z in coords:
        grid[z, y, x] = 0

    structure_3d = np.array([
        [[0, 0, 0], [0, 1, 0], [0, 0, 0]],
        [[0, 1, 0], [1, 0, 1], [0, 1, 0]],
        [[0, 0, 0], [0, 1, 0], [0, 0, 0]],
    ])

    labeled, _ = label(grid, structure_3d)

    for new_coords in np.argwhere(labeled > 1):
        coords.append(list(reversed(new_coords.tolist())))

    total_area = get_area(coords)
    print(total_area)
