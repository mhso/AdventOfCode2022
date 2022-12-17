import numpy as np
from collections import Counter

ROCKS = [
    np.array([[1, 1, 1, 1]], dtype=np.uint8), # Horizontal line
    np.array([
        [0, 1, 0],
        [1, 1, 1],
        [0, 1, 0]
    ], dtype=np.uint8), # Plus block
    np.array([
        [0, 0, 1],
        [0, 0, 1],
        [1, 1, 1]
    ], dtype=np.uint8), # L block
    np.array([
        [1],
        [1],
        [1],
        [1]
    ], dtype=np.uint8), # Vertical line
    np.array([
        [1, 1],
        [1, 1]
    ], dtype=np.uint8) # Square block
]

def visualize(cavern, n_lines=10):
    copy = np.empty_like(cavern, dtype=np.str0)
    copy[cavern == 0] = "."
    copy[cavern == 1] = "#"

    print(copy[-n_lines:, :])

def simulate(jetstreams, rocks):
    width = 7
    height = rocks * 4
    floor = height - 1
    cavern = np.zeros((height, width + 2), dtype=np.uint8)
    cavern[-1:] = 1
    cavern[:, 0] = 1
    cavern[:, -1] = 1

    rock_index = 0
    jet_index = 0

    heights = []

    rock = ROCKS[1]

    for _ in range(rocks):
        rock = ROCKS[rock_index % 5].copy()
        x = 3
        y = floor - rock.shape[0] - 3
        rock_mask = rock != 0
        old_cavern = np.zeros_like(cavern)

        heights.append(height - floor - 1)

        while True:
            diff_x = 1 if jetstreams[jet_index] == ">" else -1

            # Simulate moving horizontally
            copy_cavern = np.zeros_like(cavern)
            copy_cavern[y:y + rock.shape[0], x+diff_x:x+diff_x + rock.shape[1]] = rock_mask

            if np.any(cavern & copy_cavern): # Collision
                diff_x = 0
            else:
                old_cavern = copy_cavern

            y += 1
            x += diff_x

            # Simulate moving vertically
            copy_cavern = np.zeros_like(cavern)
            copy_cavern[y:y + rock.shape[0], x:x + rock.shape[1]] = rock_mask

            jet_index += 1

            if jet_index == len(jetstreams):
                jet_index = 0

            if np.any(cavern & copy_cavern): # Collision
                floor = min(floor, y - 1)
                rock_index += 1
                cavern = old_cavern | cavern
                break

            old_cavern = copy_cavern

    return heights

def part_1(input_text):
    heights = simulate(input_text[0], 2022)
    print(heights[-1])

def find_pattern(seq, repetitions=2):
    for n in range(len(seq), 1, -1):
        substrings = [seq[i:i + n] for i in range(len(seq) - n + 1)]
        freqs = Counter(substrings)
        if freqs.most_common(1)[0][1] >= repetitions:
            seq = freqs.most_common(1)[0][0]
            break

    return seq

def part_2(input_text):
    heights = simulate(input_text[0], 5000)
    diffs_int = [h - heights[i-1] for i, h in enumerate(heights[1:], start=1)]
    diffs_str = "".join(str(diff) for diff in diffs_int)
    pattern = find_pattern(diffs_str, repetitions=2)

    starts_at = diffs_str.find(pattern)
    next_start = diffs_str.find(pattern, starts_at + 1)

    pattern_len = next_start - starts_at

    sum_pattern = sum(diffs_int[starts_at:starts_at + pattern_len])

    rounds = (1000000000000 - starts_at)
    leftover = rounds % pattern_len

    rounds -= leftover

    sum_leftover = sum(diffs_int[starts_at:starts_at + leftover])

    cycles = rounds / pattern_len

    print(int(sum_pattern * cycles + heights[starts_at] + sum_leftover))
