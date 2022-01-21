'''
Given the roots of two binary trees p and q, write a function to check if they are the same or not.

Two binary trees are considered the same if they are structurally identical, and the nodes have the same value.

'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, r1, r2) -> bool:

        out=True

        if r1 and r2:

            out=out and r1.val==r2.val

            out=out and self.isSameTree(r1.left,r2.left)
            
            out=out and self.isSameTree(r1.right,r2.right)

        if r1 and r2==None or r1==None and r2:
            out=False
        
        return out

        