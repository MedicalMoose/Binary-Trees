class Node:
    def __init__(self, data = None, left = None, right = None):
        self.data = data
        self.left = left
        self.right = right

    def __str__(self):
        return f"Node storing {self.data}"

NodeSix = Node(30)
NodeFive = Node(8)
NodeFour = Node(2)
NodeThree = Node(20, None, NodeSix)
NodeTwo = Node(5, NodeFour, NodeFive)
NodeOne = Node(10, NodeTwo, NodeThree)

class Tree:
    def __init__(self, root = None):
        self._root = root

    @property
    def root(self):
        return self._root
    
    @root.setter
    def root(self, new_root):
        self.root = new_root

    # I did have to rely on stack overflow for this, but I think I get it now
    def post_order_traversal(self, root = None):
        if root is None: 
            root = self.root
        stack_one = [root]
        stack_two = []
        output = []
        while stack_one != []:
            node = stack_one.pop()
            stack_two.append(node)
            stack_one.append(node.left) if node.left is not None else ""
            stack_one.append(node.right) if node.right is not None else ""
        while stack_two != []:
            output.append(stack_two.pop().data)
        return output


BinaryTree = Tree(NodeOne)
print(BinaryTree.post_order_traversal())