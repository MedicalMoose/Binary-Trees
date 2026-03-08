class TreeNode:
    def __init__(self, data):
        self.data = data
        self.children = []
        self.string = ""

    def addChild(self, node):
        self.children.append(TreeNode(node))
    
    def __str__(self, level = 0):
        self.string += "    " * level + self.data + "\n"
        for node in self.children:
            self.string += node.__str__(level + 1)
        return self.string
    
Tree = TreeNode("Drinks")
Tree.addChild("Cold")
Tree.addChild("Hot")
Tree.children[0].addChild("Cola")
Tree.children[0].addChild("Fanta")
Tree.children[1].addChild("Tea")
Tree.children[1].addChild("Coffee")
print(Tree)