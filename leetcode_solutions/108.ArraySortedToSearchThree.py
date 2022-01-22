'''
Given an integer array nums where the elements are sorted in ascending order, convert it to a height-balanced binary search tree.

A height-balanced binary tree is a binary tree in which the depth of the two subtrees of every node never differs by more than one.
'''

# Definition for a binary tree node.
import numbers


class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right
class Solution:
    def sortedArrayToBST(self, nums):
        if len(nums)==0:
            return None
        if len(nums)==1:
            return TreeNode(nums[0])
        
        
        
        root=TreeNode(nums[len(nums)//2])
        sx_array=nums[0:len(nums)//2]
        dx_array=nums[len(nums)//2+1:len(nums)]

        root.left=self.sortedArrayToBST(sx_array)
        root.right=self.sortedArrayToBST(dx_array)
        
        return root