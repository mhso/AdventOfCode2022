def part_1(input_text):
    x_value = 1
    signal_strength = 0
    cycle = 1
    for instruction in input_text:
        cycles_needed = 0
        # Determine how many cycles instruction takes
        if instruction.startswith("addx"):
            cycles_needed = 2

        else:
            cycles_needed = 1

        # Run the cycles
        for _ in range(cycles_needed):
            if (cycle + 20) % 40 == 0:
                signal_strength += cycle * x_value

            cycle += 1

        # Add value to x register
        if instruction.startswith("addx"):
            amount = int(instruction.split(" ")[1])
            x_value += amount

    print(signal_strength)

def part_2(input_text):
    image = [[0 for _ in range(40)] for _ in range(6)]

    x_value = 1
    signal_strength = 0
    cycle = 1
    for instruction in input_text:
        # Determine how many cycles instruction takes
        cycles_needed = 0
        if instruction.startswith("addx"):
            cycles_needed = 2

        else:
            cycles_needed = 1

        # Run the cycles
        for _ in range(cycles_needed):
            if (cycle + 20) % 40 == 0:
                signal_strength += cycle * x_value

            # Draw pixel
            x = (cycle - 1) % 40
            y = (cycle - 1) // 40

            lit = x_value >= x - 1 and x_value <= x + 1
            image[y][x] = "#" if lit else "."

            cycle += 1

        # Add value to x register
        if instruction.startswith("addx"):
            amount = int(instruction.split(" ")[1])
            x_value += amount

    for row in image:
        print("".join(row))
