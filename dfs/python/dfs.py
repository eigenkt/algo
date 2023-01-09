class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

def dfs(node):
    if node:
        print(node.value)
        dfs(node.left)
        dfs(node.right)

# Example usage
root = Node(1, Node(2, Node(4), Node(5)), Node(3, Node(6), Node(7)))
dfs(root)
