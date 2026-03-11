from node import Node
from tree import Tree

NodeNine = Node(9)
NodeEight = Node(8)
NodeSeven = Node()
NodeSix = Node()
NodeFive = Node()
NodeFour = Node(4, NodeEight, NodeNine)
NodeThree = Node(3, NodeSix, NodeSeven)
NodeTwo = Node(2, NodeFour, NodeFive)
NodeOne = Node(1, NodeTwo, NodeThree)

NewTree = Tree(NodeOne)
NewTree.print_tree()
