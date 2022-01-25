'''
Given the root of a binary tree, return the preorder traversal of its nodes' values.
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def ric (self,root,out):

            if root==None:
                return out
            
            if root.left!=None:
                out.append(root.left.val)
                self.ric(root.left, out)

            if root.right!=None:
                out.append(root.right.val)

            
                self.ric(root.right, out)

            return out
    def preorderTraversal(self, root ):

        out=[]          #empty list

        if root==None:
            return out
        out.append(root.val)
        return self.ric(root,out)
        