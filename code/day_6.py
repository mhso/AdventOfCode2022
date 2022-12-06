def part_1(input_text):
    line = input_text[0]
    for index, character in enumerate(line[3:], start=3):
        four_chars = set(line[index - 3:index] + character)
        if len(four_chars) == 4:
            print(index + 1)
            break

def part_2(input_text):
    line = input_text[0]
    for index, character in enumerate(line[13:], start=13):
        four_chars = set(line[index - 13:index] + character)
        if len(four_chars) == 14:
            print(index + 1)
            break
