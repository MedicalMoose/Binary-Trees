class Node:
    def __init__(self, data = None, left = None, right = None):
        self.data = data
        self.left = left
        self.right = right

    def __str__(self):
        return f"Node storing {self.data}"
    
NodeFive = Node("E")
NodeFour = Node("D")
NodeThree = Node("C")
NodeTwo = Node("B", NodeFour, NodeFive)
NodeOne = Node("A", NodeTwo, NodeThree)

class Tree:
    def __init__(self, root = None):
        self._root = root

    @property
    def root(self):
        return self._root
    
    @root.setter
    def root(self, new_root):
        self.root = new_root

    def post_order_traversal(self, node = 0):
        if node == 0:
            node = self.root
    
        if node.left is not None:
            self.post_order_traversal(node.left)
        if node.right is not None:
            self.post_order_traversal(node.right)
        
        print(node.data)


BinaryTree = Tree(NodeOne)

print(BinaryTree.root)
print(BinaryTree.root.left)
print(BinaryTree.root.right)
print(BinaryTree.root.left.left)

BinaryTree.post_order_traversal()