'''
Given the root of a binary tree, return the sum of all left leaves.
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumDFS(self,root,isLeft):
        if root==None:
            return 0
        if not root.left and not root.right:
            return root.val*isLeft
        
        return self.sumDFS(root.left,1)+self.sumDFS(root.right,0)
    def sumOfLeftLeaves(self, root) -> int:
        
        return self.sumDFS(root,False)