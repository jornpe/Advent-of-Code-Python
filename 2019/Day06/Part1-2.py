from treelib import Tree

with open("input.txt") as f:
    objects = [line.split(')') for line in f.read().split('\n')]


def build_tree(root: str, objects: list) -> Tree:
    tree = Tree()
    tree.create_node(identifier=root)
    queue = [root]
    while queue:
        orb = queue.pop(0)
        neighbours = [o for o in objects if o[0] == orb]
        if not neighbours:
            continue
        for obj in neighbours:
            queue.append(obj[1])
            tree.create_node(identifier=obj[1], parent=obj[0])
    return tree


def count_orbits(graph: Tree) -> int:
    orbits = 0
    paths = graph.paths_to_leaves()
    unique_paths = set(p for sub in paths for p in sub if p != graph.root)
    for p in graph.children(graph.root):
        orbits += count_orbits(graph.subtree(p.identifier))
    return orbits + len(unique_paths)


def get_path_to_santa(tree: Tree) -> int:
    you = [p for p in tree.paths_to_leaves() if 'YOU' in p]
    san = [p for p in tree.paths_to_leaves() if 'SAN' in p]
    path = list(set(*you) - set(*san)) + list(set(*san) - set(*you))
    return len(path) - 2  # -2 to remove the 'YOU' and 'SAN', also the common node is removed


graph = build_tree('COM', objects)
print(f'⭐ Part 1: {count_orbits(graph)}')
print(f'⭐ Part 2: {get_path_to_santa(graph)}')
