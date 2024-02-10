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

def draw_tree(tree_root):
    tree = nx.DiGraph()
    pos = {tree_root.id: (0, 0)}
    tree = add_edges(tree, tree_root, pos)

    colors = [node[1]['color'] for node in tree.nodes(data=True)]
    labels = {node[0]: node[1]['label'] for node in tree.nodes(data=True)}  # Використовуйте значення вузла для міток

    plt.figure(figsize=(8, 5))
    nx.draw(tree, pos=pos, labels=labels, arrows=False, node_size=2500, node_color=colors)
    plt.show()

def draw_heap(heap):
    """Бінарна купа може бути представлена як масив, де елементи впорядковані за певними правилами. Для батьківського вузла на позиції i в масиві ці правила наступні:
    Лівий дочірній вузол знаходиться на позиції 2i + 1
    Правий дочірній вузол знаходиться на позиції 2i + 2
    """
    root = Node(heap[0])
    heap_nodes = [None for _ in range(len(heap))]
    heap_nodes[0] = root
    
    for i in range(len(heap)):
        if 2 * i + 1 < len(heap):
            heap_nodes[i].left = Node(heap[2 * i + 1])
            heap_nodes[2 * i + 1] = heap_nodes[i].left
        if 2 * i + 2 < len(heap):
            heap_nodes[i].right = Node(heap[2 * i + 2])        
            heap_nodes[2 * i + 2] = heap_nodes[i].right
            
    draw_tree(root)

# Створення дерева
root = Node(0)
root.left = Node(4)
root.left.left = Node(5)
root.left.right = Node(10)
root.right = Node(1)
root.right.left = Node(3)

# Відображення дерева
#draw_tree(root)

heap = [0, 4, 1, 5, 10, 3]
draw_heap(heap)