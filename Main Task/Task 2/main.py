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

print(tree.data)
print(tree.left.data)
print(tree.right.data)
print(tree.right.left.data)