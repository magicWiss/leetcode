'''
Given the head of a linked list and an integer val, remove all the nodes of the linked list that has Node.val == val, and return the new head.
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head, val: int):
            if not head:
                return head

            node = head
            while node and node.next:
                if node.next.val == val:
                    node.next = node.next.next

                else:
                    node = node.next

            if head.val == val:
                head = head.next

            return head            
        