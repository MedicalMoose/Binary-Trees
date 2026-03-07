class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
    
    def addLeft(self, data):
        self.left = BinaryTreeNode(data)
    
    def addRight(self, data):
        self.right = BinaryTreeNode(data)

data = []

tree = BinaryTreeNode(10)
tree.addLeft(5)
tree.addRight(15)
tree.right.addLeft(12)

def inOrder(node):
    if node is None:
        return
    inOrder(node.left)
    data.append(node.data)
    inOrder(node.right)

inOrder(tree)
print(data)

def insert(root, value):
    if root is None:
        return BinaryTreeNode(value)
    elif value < root.data:
        root.left = insert(root.left, value)
    else:
        root.right = insert(root.right, value)
    return root

EmptyTree = None
nodes = [50, 30, 70, 20, 40, 60, 80]
for node in nodes:
    EmptyTree = insert(EmptyTree, node)

data.clear()
inOrder(EmptyTree)
print(data)

def search(root, value):
    flag = False
    if root is None:
        return flag
    elif root.data == value:
        flag = True
    elif value < root.data:
        flag = search(root.left, value)
    else:
        flag = search(root.right, value)
    return flag

print(search(EmptyTree, 60))
print(search(EmptyTree, 25))

def height(root):
    if root is None:
        return 0
    left_height = height(root.left)
    right_height = height(root.right)
    return max(left_height, right_height) + 1

print(height(EmptyTree))