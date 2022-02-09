##################################  
        # Binary Trees
##################################
# Given a Binary tree, Traverse it using DFS using recursion.
# Unlike linear data structures:(Array, Linked List, Queues, Stacks, etc) 
# which have only one logical way to traverse them, trees can be traversed in different ways. 
# Generally, there are 2 widely used ways for traversing trees:

    # DFS or Depth First Search
    # BFS or Breadth First Search


# What is a binary treee?
    # - At most have 2 children
    # - exactly 1 root
    # - exactly 1 path between root and any nodes 
    # - root only is also a binary Tree
    # - empty node is also a binary tree 


## Binary Tree Traversal: Tree Traversal means a process of visiting each node in the tree exactly once in some order.
# visit --> reading/ processing data in a node

############################################
# Breadth First Search: visit all nodes at same level first. It is a level order 
# #example:     R  ----> level one
#             /   \
#            D     J -----> Level two 
#           / \   / \
#          M   N P   Q  ----- level three 

###########################################
# Depth First Search: Should go depther first before going into right nodes or left nodes.
    # DFS (Depth-first search) is technique used for traversing tree or graph. 
    # Here backtracking is used for traversal. 
    # In this traversal first the deepest node is visited and then backtracks to it’s parent node if no sibling of that node exist. 

    # Example   1 
#             /   \
#            2     3 
#           / \    
#          4   5     ------> This leafs are visited first and backtrack 

# Common traversal in Depth First Search 
    # InOrder: (left, root, right) ---> [4, 2, 5, 1, 3]
    # PreOrder: (root, left, right) ---> [1, 2, 4, 5, 3]
    # PostOrder: (left, right, root) ---> [4, 5, 2, 3, 1]


# InOrder Traversal Practice:

# A class that represents an individual node in a Binary Tree


from turtle import left, right


class Node:
    def __init__(self, val) -> None:
        self.val = val
        self.right = right
        self.left = left 

def print_InOrder(root): #inorder --> (left, root, right)
    if root:
        # first recurse on the left child
        print_InOrder(root.left)

        #the print root node
        print(root.val)

        # now recurse on right child 
        print_InOrder(root.right)

# Driver code
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

print #\n Inorder traversal of binary tree is" 
print_InOrder(root)






