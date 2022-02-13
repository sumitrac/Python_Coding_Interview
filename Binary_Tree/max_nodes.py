# Given the tree, each nodes an integers, 
# output the mapping of max values 

input = [1,2,3,2,4]
'''
    1
   / \
  2    3
      /  \
     2    4

'''

output = [[2,2], [2,3], [4,4]]

# base cases - check if root is mot empty
# what to return if tree is empty?
# traverse and compare, left noded path 
# traverse and compare, right nodes path
# use dfs 

def TreeNode(self, val, left, right):
    self.val =val
    self.left = left
    self.right = right

def mapping_tree(self, node):
    # base case 
    if node is None:
        return 

    result = []
    maxNode = 0

    def is_mapping_tree(node, maxNode):

        # base case
        if node.left is None and node.right is None:
            result.append([node, maxNode])
            maxNode = 0

        if node.left:
            if node.left <= maxNode:
                maxNode = node.left 
            is_mapping_tree(node.left)

        if node.right:
            if node.right <= maxNode:
                maxNode = node.right
            is_mapping_tree(node.right)

        is_mapping_tree(node, maxNode)
        return result 

    
