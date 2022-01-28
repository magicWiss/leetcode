'''
Given the root of a binary tree, return the postorder traversal of its nodes' values.
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def ricPost(self,root,out):
        #caso base 0
        if root==None:
            return out
        #caso base siamo in una foglia
        if root.left==None and root.right==None:
            #inserisco il nodo
            out.append(root.val)
            return out
        
        self.ricPost(root.left,out)
        self.ricPost(root.right,out)
        out.append(root.val)
        return out

    def postorderTraversal(self, root):

        out=[]

        self.ricPost(root,out)

        return out
        