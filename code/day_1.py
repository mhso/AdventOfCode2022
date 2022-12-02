def part_1(input_text):
    calories = []
    curr_sum = 0

    if input_text[-1] != "":
        input_text.append("")

    for line in input_text:
        if line == "":
            calories.append(curr_sum)
            curr_sum = 0
        else:
            curr_sum += int(line)

    print(max(calories))

def part_2(input_text):
    calories = []
    curr_sum = 0

    if input_text[-1] != "":
        input_text.append("")

    for line in input_text:
        if line == "":
            calories.append(curr_sum)
            curr_sum = 0
        else:
            curr_sum += int(line)

    print(sum(sorted(calories, reverse=True)[:3]))
