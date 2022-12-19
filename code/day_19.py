import networkx

def create_graph(input_text):
    graph = networkx.DiGraph()

    for line in input_text:
        split = line.replace("Blueprint: ", "").split(".")
        ore_ore = int(split[0].split(" ")[-2])
        clay_ore = int(split[1].split(" ")[-2])
        obsidian_ore, obsidian_clay = tuple(map(int, split[2].split(" ")[-5::3]))
        geode_ore, geode_obsidian = tuple(map(int, split[3].split(" ")[-5::3]))

        print(ore_ore, clay_ore, obsidian_ore, obsidian_clay, geode_ore, geode_obsidian)

def part_1(input_text):
    graph = create_graph(input_text)

def part_2(input_text):
    print(input_text)
