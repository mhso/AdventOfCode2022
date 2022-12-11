import math

def parse_input(input_text):
    monkey_items = []
    operations = []
    divisible_by = []
    tests_true = []
    tests_false = []

    for line in input_text:
        line_stripped = line.strip()
        if line_stripped.startswith("Starting"):
            items = list(map(int, line.split(":")[1].strip().split(",")))
            monkey_items.append(items)
        elif line_stripped.startswith("Operation"):
            operation_split = line.split(":")[1].strip().split(" ")
            operation = operation_split[-2]
            amount = operation_split[-1]
            if amount != "old":
                amount = int(operation_split[-1])

            operations.append((operation, amount))

        elif line_stripped.startswith("Test"):
            div = int(line.split(":")[1].strip().split(" ")[-1])
            divisible_by.append(div)

        elif line_stripped.startswith("If"):
            split = line_stripped.split(":")
            bool_value = split[0].split(" ")[1]
            throw_to = int(split[1].split(" ")[-1])
            if bool_value == "true":
                tests_true.append(throw_to)
            else:
                tests_false.append(throw_to)

    return monkey_items, operations, divisible_by, tests_true, tests_false

def part_1(input_text):
    monkey_items, operations, divisible_by, tests_true, tests_false = parse_input(input_text)
    inspections = [0] * len(monkey_items)
    rounds = 20

    for _ in range(rounds):
        for monkey in range(len(monkey_items)):
            while (items := monkey_items[monkey]) != []:
                item = items.pop(0)
                operation, amount = operations[monkey]
                if amount == "old":
                    amount = item

                item = item * amount if operation == "*" else item + amount
                item = item // 3

                if item % divisible_by[monkey] == 0:
                    throw_to = tests_true[monkey]
                else:
                    throw_to = tests_false[monkey]

                monkey_items[throw_to].append(item)

                inspections[monkey] += 1

    inspections.sort(reverse=True)

    print(inspections[0] * inspections[1])

def part_2(input_text):
    monkey_items, operations, divisible_by, tests_true, tests_false = parse_input(input_text)
    inspections = [0] * len(monkey_items)
    rounds = 10000

    lcm = math.lcm(*divisible_by)

    for _ in range(rounds):
        for monkey in range(len(monkey_items)):
            while (items := monkey_items[monkey]) != []:
                item = items.pop(0)
                operation, amount = operations[monkey]

                if amount == "old":
                    amount = item

                item = item * amount if operation == "*" else item + amount
                item = (item % lcm)

                if item % divisible_by[monkey] == 0:
                    throw_to = tests_true[monkey]
                else:
                    throw_to = tests_false[monkey]

                monkey_items[throw_to].append(item)

                inspections[monkey] += 1

    inspections.sort(reverse=True)

    print(inspections[0] * inspections[1])
