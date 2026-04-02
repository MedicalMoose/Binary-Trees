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
        self.node_count = None
        self.leaf_count = None
        self.height = None
        self.setup_tree()

    @property
    def root(self):
        return self._root
    
    @root.setter
    def root(self, new_root):
        self.root = new_root

    def setup_tree(self, node = 0, counts = [0, 0, 0], height = 0):
        if node == 0:
            node = self.root
    
        if node.left is not None:
            self.setup_tree(node.left, counts, height + 1)
        if node.right is not None:
            self.setup_tree(node.right, counts, height + 1)
        
        # Counts = [no_nodes, no_leaves, height]
        counts[0] += 1
        if node.left is None and node.right is None:
            counts[1] += 1
        if height > counts[2]:
            counts[2] = height
        
        self.node_count = counts[0]
        self.leaf_count = counts[1]
        self.height = counts[2]


    def post_order_traversal(self, node = 0):
        if node == 0:
            node = self.root
    
        if node.left is not None:
            self.post_order_traversal(node.left)
        if node.right is not None:
            self.post_order_traversal(node.right)
        
        print(node.data)

    def post_order_list(self, node = 0, result = []):
        if node == 0:
            node = self.root
    
        if node.left is not None:
            self.post_order_list(node.left)
        if node.right is not None:
            self.post_order_list(node.right)
        
        result.append(node.data)
        return result


BinaryTree = Tree(NodeOne)

print(BinaryTree.root)
print(BinaryTree.root.left)
print(BinaryTree.root.right)
print(BinaryTree.root.left.left)

print(*BinaryTree.post_order_list())
print(BinaryTree.node_count)
print(BinaryTree.leaf_count)
print(BinaryTree.height)