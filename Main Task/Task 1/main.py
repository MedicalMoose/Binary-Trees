class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
    
    def addLeft(self, data):
        self.left = BinaryTreeNode(data)
    
    def addRight(self, data):
        self.right = BinaryTreeNode(data)