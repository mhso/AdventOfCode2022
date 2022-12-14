from functools import cmp_to_key

def compare_values(val_1, val_2):
    if isinstance(val_1, int) and isinstance(val_2, int):
        if val_1 == val_2:
            return 0

        return 1 if val_1 < val_2 else -1

    # Create singular list if any input is an integer
    if not isinstance(val_1, list):
        val_1 = [val_1]
    if not isinstance(val_2, list):
        val_2 = [val_2]

    for x, y in zip(val_1, val_2):
        comparison = compare_values(x, y)
        if comparison != 0:
            return comparison

    if len(val_1) == len(val_2):
        return 0

    return 1 if len(val_1) < len(val_2) else -1

def parse_input(input_text):
    return list(map(lambda x: eval(x), filter(lambda x: x != "", input_text)))

def part_1(input_text):
    parsed = parse_input(input_text)
    correct_order = []
    for index, (value_1, value_2) in enumerate(zip(parsed[0::3], parsed[1::3]), start=1):
        if compare_values(value_1, value_2) == 1:
            correct_order.append(index)

    print(correct_order)
    print(sum(correct_order))

def part_2(input_text):
    parsed = parse_input(input_text)
    parsed.extend([[2], [6]]) # Add divider packets
    parsed.sort(key=lambda x: cmp_to_key(compare_values)(x), reverse=True)

    print((parsed.index([2]) + 1) * (parsed.index([6]) + 1))
