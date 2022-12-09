def sign(x):
    return 1 if x >= 0 else -1

def part_1(input_text):
    head_x, head_y = 0, 0
    tail_x, tail_y = 0, 0
    visited_spots = set()

    for line in input_text:
        direction, amount = line.split(" ")
        amount = int(amount)

        for _ in range(amount):
            # Move the head
            if direction == "D":
                head_y += 1
            elif direction == "U":
                head_y -= 1
            elif direction == "R":
                head_x += 1
            elif direction == "L":
                head_x -= 1

            # Move the tail
            if head_x == tail_x: # Horizontal case
                if abs(head_y - tail_y) > 1:
                    tail_y += sign(head_y - tail_y)
            elif head_y == tail_y: # Vertical case
                if abs(head_x - tail_x) > 1:
                    tail_x += sign(head_x - tail_x)
            elif (head_x - tail_x) ** 2 + (head_y - tail_y) ** 2 > 2:  # Diagonal case
                tail_y += sign(head_y - tail_y)
                tail_x += sign(head_x - tail_x)

            visited_spots.add((tail_x, tail_y))

    print(len(visited_spots))

def part_2(input_text):
    knots = [[0, 0] for _ in range(10)]
    visited_spots = set()

    for line in input_text:
        direction, amount = line.split(" ")
        amount = int(amount)

        for _ in range(amount):
            # Move the head
            if direction == "D":
                knots[0][1] += 1
            elif direction == "U":
                knots[0][1] -= 1
            elif direction == "R":
                knots[0][0] += 1
            elif direction == "L":
                knots[0][0] -= 1

            # Move the knots
            head_x, head_y = knots[0]
            for index in range(1, 10):
                tail_x, tail_y = knots[index]
                if head_x == tail_x: # Horizontal case
                    if abs(head_y - tail_y) > 1:
                        tail_y += sign(head_y - tail_y)
                elif head_y == tail_y: # Vertical case
                    if abs(head_x - tail_x) > 1:
                        tail_x += sign(head_x - tail_x)
                elif (head_x - tail_x) ** 2 + (head_y - tail_y) ** 2 > 2:  # Diagonal case
                    tail_y += sign(head_y - tail_y)
                    tail_x += sign(head_x - tail_x)

                knots[index] = [tail_x, tail_y]
                head_x, head_y = tail_x, tail_y

            visited_spots.add((tail_x, tail_y))

    print(len(visited_spots))
