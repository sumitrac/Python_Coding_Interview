# Binary Tree Preorder Traversal
# Given the root of a binary tree, return the preorder traversal of its nodes' values.

root = [1,null,2,3]
    # 1
    #  \
    #    2
    #   /
    # 3
# output = [1,2,3]

class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right 

    def preOrderTraversal(self, root):
        '''
        preorder traversal -> <root> <left> <right>
        1
        \
            2
        /
        3
        '''

        result = []

        if root is None:
            return []
        else: 
            result.append(root.value) #append the root node

        if root.left:
            result += self.preOrderTraversal(root.left) # if left, appends left nodes
        
        if root.right:
            result += self.preOrderTraversal(root.right) # if right, appends right nodes
            
        return result 

# print(preOrderTraversal(root))

