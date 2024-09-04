class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


# Function to build a binary tree from leaves to root
def build_tree_from_leaves(leaf_values):
    nodes = [TreeNode(value) for value in leaf_values]

    while len(nodes) > 1:
        new_level = []
        for i in range(0, len(nodes), 2):
            left = nodes[i]
            right = nodes[i + 1] if i + 1 < len(nodes) else None
            parent = TreeNode(left.value + (right.value if right else 0), left, right)
            new_level.append(parent)
        nodes = new_level

    return nodes[0] if nodes else None


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
    # Example usage
    leaf_values = [1, 2, 3, 4, 5, 6, 7, 8]
    root = build_tree_from_leaves(leaf_values)

    # Function to print the tree (in-order traversal)
    def print_tree(node):
        if node:
            print_tree(node.left)
            print(node.value, end=' ')
            print_tree(node.right)

    print_tree(root)
