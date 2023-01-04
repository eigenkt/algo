    #     17
    #    /  \
    #  10    30
    #  / \   / \ 
    # 7  11 20  33

class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

root = Node(17)
root.left = Node(10)
root.right = Node(30)
root.left.left = Node(7)
root.left.right = Node(11)
root.right.left = Node(20)
root.right.right = Node(33)


    #     17
    #    /  \
    #  10    30
    #  / \   / \ 
    # 7  11 20  33

def breadth_first_search(root):
    if root is None:
        return

    queue = [root]
    while queue:
        node = queue.pop(0)
        print(node.val)  # process the node

        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
