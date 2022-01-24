# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root) -> int:

        depth=1
        if root==None:
            return 0
        if root.left==None and root.right==None:
            return 1
        left=self.minDepth(root.left)
        right=self.minDepth(root.right)
        if right*left==0: 
            if left==0:
                depth=depth+right
            
            elif right==0:
                depth=depth+left
            return depth
        depth=depth+min(left,right)
        return depth
        