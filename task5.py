import networkx as nx
import matplotlib.pyplot as plt

class Node:
    def __init__(self, key, color="#000000"):
        self.left = None
        self.right = None
        self.val = key
        self.color = color 

def add_edges(graph, node, pos, x=0, y=0, layer=1):
    if node is not None:
        graph.add_node(node.val, pos=(x, y), layer=layer, color=node.color)
        if node.left is not None:
            graph.add_edge(node.val, node.left.val)
            l = 1 / layer
            add_edges(graph, node.left, pos, x-l, y-1, layer+1)
        if node.right is not None:
            graph.add_edge(node.val, node.right.val)
            r = 1 / layer
            add_edges(graph, node.right, pos, x+r, y-1, layer+1)
    return graph

def draw_tree(tree_root, title=""):
    graph = nx.DiGraph()
    pos = {}
    tree = add_edges(graph, tree_root, pos)

    colors = [node[1]['color'] for node in tree.nodes(data=True)]

    plt.figure(figsize=(12, 8))
    nx.draw(tree, pos=nx.get_node_attributes(tree, 'pos'),
            with_labels=True, arrows=False, node_size=2500,
            node_color=colors, font_weight='bold')
    plt.title(title, fontsize=16)
    plt.show()

def generate_gradient_colors(n, base_color=(18, 150, 240)):
    """
    Generate n hex colors with increasing brightness.
    base_color: RGB tuple for base (dark) color.
    """
    gradient = []
    for i in range(n):
        factor = 0.4 + 0.6 * (i / max(1, n-1))  # Brightness factor from 0.4 to 1.0
        r = min(255, int(base_color[0] * factor))
        g = min(255, int(base_color[1] * factor))
        b = min(255, int(base_color[2] * factor))
        gradient.append(f'#{r:02x}{g:02x}{b:02x}')
    return gradient

def count_nodes(node):
    if not node:
        return 0
    return 1 + count_nodes(node.left) + count_nodes(node.right)

def in_order_traversal(node, colors, counter):
    if node:
        in_order_traversal(node.left, colors, counter)
        node.color = colors[counter[0]]
        counter[0] += 1
        in_order_traversal(node.right, colors, counter)

def pre_order_traversal(node, colors, counter):
    if node:
        node.color = colors[counter[0]]
        counter[0] += 1
        pre_order_traversal(node.left, colors, counter)
        pre_order_traversal(node.right, colors, counter)


root = Node(10)
root.left = Node(7)
root.right = Node(5)
root.left.left = Node(3)
root.left.right = Node(0)
root.right.left = Node(1)
root.right.right = Node(6)


total_nodes = count_nodes(root)

colors_inorder = generate_gradient_colors(total_nodes)
counter = [0]
in_order_traversal(root, colors_inorder, counter)
draw_tree(root, title="In-Order Traversal (From Dark to Light Colors)")

colors_preorder = generate_gradient_colors(total_nodes)
counter = [0]
pre_order_traversal(root, colors_preorder, counter)
draw_tree(root, title="Pre-Order Traversal (From Dark to Light Colors)")
