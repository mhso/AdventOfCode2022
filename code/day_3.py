def get_char_score(char):
    num_val = ord(char)
    return num_val - 96 if num_val > 96 else num_val - 38

def part_1(input_text):
    sum_scores = 0
    for line in input_text:
        half_1 = set(line[:len(line) // 2])
        half_2 = set(line[len(line) // 2:])

        common = half_1.intersection(half_2).pop()
        sum_scores += get_char_score(common)

    print(sum_scores)

def part_2(input_text):
    sum_scores = 0
    for index in range(0, len(input_text), 3):
        lines = input_text[index : index + 3]

        common = set(lines[0]).intersection(set(lines[1])).intersection(set(lines[2])).pop()
        sum_scores += get_char_score(common)

    print(sum_scores)
