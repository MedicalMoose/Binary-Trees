class Tree:
    def __init__(self, root = None):
        self.root = root
        self.highest_layer = None

    def traversal(self, node = -1, curr_layer = 0):
        if node == -1:
            node = self.root
        
        if node is not None:
            print(node)
            self.traversal(node.left, curr_layer + 1)
            self.traversal(node.right, curr_layer + 1)
            return

        if self.highest_layer is None or self.highest_layer > curr_layer:
            self.highest_layer = curr_layer

    def print_tree(self, node = -1, curr_layer = 0):
        if node == -1:
            node = self.root
        
        if node is not None:
            print(node)
            self.traversal(node.left, curr_layer + 1)
            self.traversal(node.right, curr_layer + 1)
            return
        
        
    def insert(self, new_node):
        if self.root is None:
            self.root = new_node
            return
        node_list = [self.root]
        while node_list:
            node = node_list.pop(0)
            if node.left is None or node.left.data is None:
                node.left = new_node
                return
            else:
                node_list.append(node.left)
            if node.right is None or node.right.data is None:
                node.right = new_node
                return
            else:
                node_list.append(node.right)
