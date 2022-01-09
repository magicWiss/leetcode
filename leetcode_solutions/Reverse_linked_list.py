'''Given the head of a singly linked list, reverse the list, and return the reversed list.'''

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseList(self, head):
        out=None
        temp=list()
        p=head
        while p!=None:
            temp.append(p.val)
            p=p.next
        if(len(temp)==0):
            return None
        
        i=len(temp)-1
        value=temp[i]
        newHead=ListNode(value)
        p=newHead
        i-=1
        while i>=0:
            newNode=ListNode(temp[i])
            p.next=newNode
            p=p.next
            i-=1
        return newHead
            