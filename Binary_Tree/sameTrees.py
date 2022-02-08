# 100. Same Tree
# Easy level

# Given the roots of two binary trees p and q, write a function to check if they are the same or not.
# Two binary trees are considered the same if they are structurally identical, and the nodes have the same value.

from logging.config import valid_ident
from turtle import left, right


Input: p = [1,2,3], q = [1,2,3]
#   p:  
#        1    
    #   / \
    #  2    3

    # q:
    #   1
    #  / \
    # 2   3

# Output: true

Input: p = [1,2], q = [1,null,2]
# Output: false

Input: p = [1,2,1], q = [1,1,2]
# Output: false

class TreeNodes(self, val, left, right):
    self.val = val
    self.left = left
    self.right = right

   
def isSameTree(p, q):

        # base case 
    if p is None and q is None:
        return True
    if p is None or q is None:
        return False 
    if p.val != q.val:
        return False 


    # Do the recursive call where there are nodes in p and q
    # preOrder DFS = <root> <left> <right>
    if p and q:
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)


# Time: O(N) because we are traversing through all nodes in both trees
# Space: O(Log(N)) in balance Trees but worst case is O(N)




    


        