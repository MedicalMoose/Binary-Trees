class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
    
    def addLeft(self, data):
        self.left = BinaryTreeNode(data)
    
    def addRight(self, data):
        self.right = BinaryTreeNode(data)

tree = BinaryTreeNode(10)
tree.addLeft(5)
tree.addRight(15)
tree.right.addLeft(12)

data = []

def inOrder(node):
    if node is None:
        return
    inOrder(node.left)
    data.append(node.data)
    inOrder(node.right)

def insert(root, value):
    if root is None:
        return BinaryTreeNode(value)
    elif value < root.data:
        root.left = insert(root.left, value)
    else:
        root.right = insert(root.right, value)
    return root
    
insert(tree, 13)
inOrder(tree)
print(data)