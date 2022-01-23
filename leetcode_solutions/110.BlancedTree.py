'''

Given a binary tree, determine if it is height-balanced.

For this problem, a height-balanced binary tree is defined as:

a binary tree in which the left and right subtrees of every node differ in height by no more than 1.

 
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    

    def isBalanced(self, root) -> bool:
        
        def dfs(root):
            if root==None:
                return [True,0]
            
            left,right=dfs(root.left),dfs(root.right)
            
            balanced=abs(left[1]-right[1])<=1
            balanced=balanced and left[0] and right[0]

            return [balanced, 1+max(left[1],right[1])]
        return dfs(root)[0]
        
       
