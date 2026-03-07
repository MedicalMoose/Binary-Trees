class TreeNode:
    def __init__(self, data):
        self.data = data
        self.children = []
        
    def addChild(self, node):
        self.children.append(TreeNode(node))