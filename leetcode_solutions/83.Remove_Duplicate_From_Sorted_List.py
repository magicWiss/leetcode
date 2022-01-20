'''
Given the head of a sorted linked list, delete all duplicates such that each element appears only once. 
Return the linked list sorted as well.

'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head):

        if head==None or head.next==None:
            return head

        first=head
        second=head.next

        while second!=None:

            if second.val==first.val:
                
                first.next=second.next
               
                second=second.next
            else:
            
                first=first.next
                second=second.next
            

        return head
        