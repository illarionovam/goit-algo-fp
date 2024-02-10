import uuid

import networkx as nx
import matplotlib.pyplot as plt

class Node:
    def __init__(self, key, color="skyblue"):
        self.left = None
        self.right = None
        self.val = key
        self.color = color  # Додатковий аргумент для зберігання кольору вузла
        self.id = str(uuid.uuid4())  # Унікальний ідентифікатор для кожного вузла

def add_edges(graph, node, pos, x=0, y=0, layer=1):
    if node is not None:
        graph.add_node(node.id, color=node.color, label=node.val)  # Використання id та збереження значення вузла
        if node.left:
            graph.add_edge(node.id, node.left.id)
            l = x - 1 / 2 ** layer
            pos[node.left.id] = (l, y - 1)
            l = add_edges(graph, node.left, pos, x=l, y=y - 1, layer=layer + 1)
        if node.right:
            graph.add_edge(node.id, node.right.id)
            r = x + 1 / 2 ** layer
            pos[node.right.id] = (r, y - 1)
            r = add_edges(graph, node.right, pos, x=r, y=y - 1, layer=layer + 1)
    return graph

def draw_tree(tree_root, search = None):
    tree = nx.DiGraph()
    pos = {tree_root.id: (0, 0)}
    tree = add_edges(tree, tree_root, pos)

    if search == "dfs":
        dfs_colors = {}
        dfs(tree_root, set(), dfs_colors)
        colors = [dfs_colors[node_id] for node_id in tree.nodes()]  # використовуємо колір для обходу у глибину
    elif search == "bfs":
        bfs_colors = bfs(tree_root)
        colors = [bfs_colors[node_id] for node_id in tree.nodes()]
    else:
        colors = [node[1]['color'] for node in tree.nodes(data=True)]

    labels = {node[0]: node[1]['label'] for node in tree.nodes(data=True)}  # Використовуйте значення вузла для міток

    plt.figure(figsize=(8, 5))
    nx.draw(tree, pos=pos, labels=labels, arrows=False, node_size=2500, node_color=colors)
    plt.show()

def generate_color(index):
    # Генерація кольору на основі індексу
    # Кольори змінюються від темного до світлого відтінку
    r = hex(int(25 + index * 10) % 256)[2:].zfill(2)
    g = hex(int(200 - index * 10) % 256)[2:].zfill(2)
    b = hex(int(100 + index * 20) % 256)[2:].zfill(2)
    return '#' + r + g + b

def dfs(node, visited, depth_colors):
    # найзвичайніший dfs, просто по ходу обходу фарбуємо вершини
    if node is not None:
        visited.add(node)
        depth_colors[node.id] = generate_color(len(visited))
        if node.left not in visited:
            dfs(node.left, visited, depth_colors)
        if node.right not in visited:
            dfs(node.right, visited, depth_colors)

def bfs(root):
    # найзвичайніший bfs, просто по ходу обходу фарбуємо вершини
    visited = set()
    queue = [root]
    visited.add(root)
    breadth_colors = {root.id: generate_color(1)}

    while queue:
        node = queue.pop(0)
        if node.left and node.left not in visited:
            visited.add(node.left)
            queue.append(node.left)
            breadth_colors[node.left.id] = generate_color(len(visited))
        if node.right and node.right not in visited:
            visited.add(node.right)
            queue.append(node.right)
            breadth_colors[node.right.id] = generate_color(len(visited))

    return breadth_colors

# Створення дерева
root = Node(0)
root.left = Node(4)
root.left.left = Node(5)
root.left.right = Node(10)
root.right = Node(1)
root.right.left = Node(3)

# Відображення дерева
draw_tree(root)
draw_tree(root, "dfs")
draw_tree(root, "bfs")