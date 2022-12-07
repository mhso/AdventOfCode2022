class Node:
    def __init__(self, name, is_dir, parent, size=0):
        self.name = name
        self.is_dir = is_dir
        self.size = size
        self.parent = parent
        if self.parent is not None:
            self.parent.add_child(self)
        self.children = {}

    def add_child(self, node):
        self.children[node.name] = node

    def get_child(self, name):
        return self.children.get(name)

    def __hash__(self):
        return self.name.__hash__()

    def __eq__(self, __o: object):
        parent_none = self.parent is None and __o.parent is None
        return (parent_none or self.parent.name == __o.parent.name) and self.name == __o.name

    def __str__(self):
        return f"<Node:name={self.name}|size={self.size}>"

def get_size(node):
    if node.is_dir:
        node.size = sum(get_size(child_node) for child_node in node.children.values())
        return node.size
    else:
        return node.size

def create_directory_tree(input_text):
    root_node = Node("/", "dir", None)
    curr_node = root_node

    # First pass: Create the directory tree structure
    for line in input_text[1:]:
        split = line.split(" ")
        if split[0] == "$": # Command
            if split[1] == "cd":
                directory = split[2]

                if directory == "..": # Go up one level
                    curr_node = curr_node.parent
                    continue

                # If we already visited this directory, get corresponding node
                if (child_node := curr_node.get_child(directory)) is not None:
                    curr_node = child_node
                else: # Create new node for this directory
                    curr_node = Node(directory, "dir", curr_node)

        else: # Listing of files and directories
            name = split[1]
            # Try get child node from current active directory
            child_node = curr_node.get_child(name)

            # Create new child node
            if child_node is None:
                is_dir = split[0] == "dir"
                node_size = int(split[0]) if not is_dir else 0
                child_node = Node(name, is_dir, curr_node, node_size)

    # Second pass: Calculate size of the different directories
    get_size(root_node)

    return root_node

def part_1(input_text):
    # Initialize directory tree
    root_node = create_directory_tree(input_text)

    queue = [root_node]
    small_nodes = []
    visited_nodes = {root_node}

    # BFS to traverse tree and find nodes smaller than 100.000 in size
    while queue != []:
        node = queue.pop()

        if node.is_dir:
            # Iterate through child nodes of directory
            for child_node in node.children.values():
                if child_node not in visited_nodes:
                    visited_nodes.add(child_node)
                    queue.append(child_node)

                    if child_node.is_dir and child_node.size <= 100_000:
                        small_nodes.append(child_node)

    print(sum(node.size for node in small_nodes))

def part_2(input_text):
    # Initialize directory tree
    root_node = create_directory_tree(input_text)
    space_total = 70_000_000
    space_required = 40_000_000
    used_space = root_node.size

    queue = [root_node]
    best_node = None
    smallest_size = space_total
    visited_nodes = {root_node}

    # BFS to traverse tree and find smallest directory to delete
    while queue != []:
        node = queue.pop()

        if node.is_dir:
            # Iterate through child nodes of directory
            for child_node in node.children.values():
                if child_node not in visited_nodes:
                    visited_nodes.add(child_node)
                    queue.append(child_node)

                    if child_node.is_dir:
                        if used_space - child_node.size <= space_required and child_node.size < smallest_size:
                            best_node = child_node
                            smallest_size = child_node.size

    print(best_node.size)
