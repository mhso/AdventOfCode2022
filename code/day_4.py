def part_1(input_text):
    sum_overlapping = 0
    for line in input_text:
        range_1, range_2 = line.split(",")
        min_1, max_1 = tuple(map(int, range_1.split("-")))
        min_2, max_2 = tuple(map(int, range_2.split("-")))

        section_1 = set(range(min_1, max_1 + 1))
        section_2 = set(range(min_2, max_2 + 1))        

        if section_1.issubset(section_2) or section_2.issubset(section_1):
            sum_overlapping += 1

    print(sum_overlapping)

def part_2(input_text):
    sum_overlapping = 0
    for line in input_text:
        range_1, range_2 = line.split(",")
        min_1, max_1 = tuple(map(int, range_1.split("-")))
        min_2, max_2 = tuple(map(int, range_2.split("-")))

        section_1 = set(range(min_1, max_1 + 1))
        section_2 = set(range(min_2, max_2 + 1))        

        if not section_1.isdisjoint(section_2) or not section_2.isdisjoint(section_1):
            sum_overlapping += 1

    print(sum_overlapping)
