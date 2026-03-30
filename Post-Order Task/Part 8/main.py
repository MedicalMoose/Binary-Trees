from node import Node
from tree import Tree

NodeSix = Node(30)
NodeFive = Node(8)
NodeFour = Node(2)
NodeThree = Node(20, None, NodeSix)
NodeTwo = Node(5, NodeFour, NodeFive)
NodeOne = Node(10, NodeTwo, NodeThree)

BinaryTree = Tree(NodeOne)

print(f"Nodes: {BinaryTree.post_order_list()}")
print(f"# of Nodes: {BinaryTree.node_count}")
print(f"# of Leaves: {BinaryTree.leaf_count}")
print(f"Height: {BinaryTree.height}")