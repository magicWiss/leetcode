'''
Given a binary search tree (BST), find the lowest common ancestor (LCA) of two given nodes in the BST.

According to the definition of LCA on Wikipedia: 
“The lowest common ancestor is defined between two nodes p and q as the lowest node in T that has both p and q as descendants
 (where we allow a node to be a descendant of itself).”
'''

#we find the result when we operate a split in the search (p> curr.val and q< curr.val (viceversa) or one of p and q are equal to curr.val)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root, p, q):

        curr=root           #starting from root

        while curr:         #there is a solution, so we eventually will exit the loop

            #case 1->right search on the BTS
            if curr.val<p.val and curr.val<q.val:
                curr=curr.right
            #case 2->left search on BTS
            elif curr.val>p.val and curr.val>q.val:
                curr=curr.left
            
            #in any other cases we found the solution
            else:
                return curr
        