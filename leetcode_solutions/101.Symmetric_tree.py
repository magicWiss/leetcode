'''
Given the root of a binary tree, check whether it is a mirror of itself (i.e., symmetric around its center).

 
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def simmetric(self,l,r):
        out=True
        if l and r:
            out=out and l.val==r.val
            out= out and self.simmetric(l.left,r.right)
            out= out and self.simmetric(l.right, r.left)

        if l==None and r or r==None and l:
            return False
        return out
    def isSymmetric(self, root) -> bool:

        out=True
        if root==None:
            return False

        else:
            left=root.right
            right=root.right

            return self.simmetric(root,root)

        