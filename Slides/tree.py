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

    def find_imbalance(self, node = -1, curr_layer = 0):
        if curr_layer <= self.highest_layer:
            if node == -1:
                node = self.root
            
            if node is not None:
                print(node)
                self.traversal(node.left, curr_layer + 1)
                self.traversal(node.right, curr_layer + 1)
                return
            
            return node
        


    def print_tree(self, node = -1, curr_layer = 0):
        if node == -1:
            node = self.root
        
        if node is not None:
            print(node)
            self.traversal(node.left, curr_layer + 1)
            self.traversal(node.right, curr_layer + 1)
            return
        
        
    def insert(self, new_node):
        self.find_imbalance = new_node
        