import networkx
import math
import matplotlib.pyplot as plt

def parse_graph(input_text):
    graph = networkx.DiGraph()

    for line in input_text:
        split = line.split(" ")
        v_to = split[1]
        v_from_start = split.index("to") + 2
        v_from_list = " ".join(split[v_from_start:]).split(", ")
        v_to_list = [v_to for _ in v_from_list]
        weight = 30 - int(split[4].split("=")[1].replace(";", ""))
        weight_list = [weight] * len(v_from_list)

        # Add edges going both ways
        data_1 = list(zip(v_from_list, v_to_list, weight_list))
        data_2 = list(zip(v_to_list, v_from_list, weight_list))

        graph.add_weighted_edges_from(data_1, capacity=30)
        graph.add_weighted_edges_from(data_2, capacity=30)

    return graph

def part_1(input_text):
    graph = parse_graph(input_text)

    flow = networkx.flow.shortest_augmenting_path(graph, "AA", SUPERSINK_NODE)
    total = 0
    for node in flow:
        for v in flow[node].values():
            total += v
    print(total)

def part_2(input_text):
    print(input_text)
