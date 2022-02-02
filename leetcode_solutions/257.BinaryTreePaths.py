'''
Given the root of a binary tree, return all root-to-leaf paths in any order.

A leaf is a node with no children.

 
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root):

        out=[]
        if not root:
            return out
        current_string=str(root.val)
        #case1->root has no child
        if root.left==None and root.right==None:
            out.append(current_string)
        
        #going left
        if root.left!=None:
            self.dfs_path(root.left,current_string,out)
        if root.right!=None:
            self.dfs_path(root.right,current_string,out)

        return out

    def dfs_path(self,root,stri,out):

        stri+="->"+str(root.val)
        if root.left!=None:
            self.dfs_path(root.left,stri,out)
        if root.right!=None:
            self.dfs_path(root.right,stri,out)
        if root.left==None and root.right==None:
            
            out.append(stri)
            return


        