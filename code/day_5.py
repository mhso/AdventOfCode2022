def parse_initial_stacks(input_text):
    initial_height = input_text.index("") - 1
    indexes = input_text[initial_height].split(None)
    num_stacks = int(indexes[-1])

    stacks = [[] for _ in range(num_stacks)]

    for line in input_text[:initial_height]:
        letters = line[1::4]
        
        for index, letter in enumerate(letters):
            if letter != " ":
                stacks[index].append(letter)

    # Reverse the stacks so upper element is last in list
    for stack in stacks:
        stack.reverse()

    return stacks, initial_height

def part_1(input_text):
    stacks, initial_height = parse_initial_stacks(input_text)

    # Simulate the different moves from/to stacks
    for line in input_text[initial_height + 2:]:
        split = line.split(" ")
        amount = int(split[1])
        stack_from = int(split[3])
        stack_to = int(split[5])

        for _ in range(amount):
            letter = stacks[stack_from - 1].pop()
            stacks[stack_to - 1].append(letter)

    for stack in stacks:
        print(stack[-1], end="")

    print()

def part_2(input_text):
    stacks, initial_height = parse_initial_stacks(input_text)

    # Simulate the different moves from/to stacks
    for line in input_text[initial_height + 2:]:
        split = line.split(" ")
        amount = int(split[1])
        stack_from = int(split[3])
        stack_to = int(split[5])

        temp_list = []

        for _ in range(amount):
            temp_list.append(stacks[stack_from - 1].pop())

        temp_list.reverse()
        stacks[stack_to - 1].extend(temp_list)

    for stack in stacks:
        print(stack[-1], end="")

    print()
