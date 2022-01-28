'''
Given the heads of two singly linked-lists headA and headB, return the node at which the two lists intersect. If the two linked lists have no intersection at all, return null.

For example, the following two linked lists begin to intersect at node c1
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA, headB) :

        if headA ==None or headB==None:
            return None
        
        #secondo caso
        mappa=dict()
        output=None

        #iterators
        p1=headA
        p2=headB

        while p1!=None or p2!=None:
            
            if p1!=None:

                #getting the hasvalue
                hashVal=hash(p1)
                if hashVal in mappa:
                    return p1
                mappa[hashVal]=p1
                p1=p1.next
            if p2!=None:

                #getting the hasvalue
                hashVal=hash(p2)
                if hashVal in mappa:
                    return p2
                mappa[hashVal]=p1
                p2=p2.next
        return None

'''
class Solution:
    # @param two ListNodes
    # @return the intersected ListNode
    def getIntersectionNode(self, headA, headB):
        curA,curB = headA,headB
        lenA,lenB = 0,0
        while curA is not None:
            lenA += 1
            curA = curA.next
        while curB is not None:
            lenB += 1
            curB = curB.next
        curA,curB = headA,headB
        if lenA > lenB:
            for i in range(lenA-lenB):
                curA = curA.next
        elif lenB > lenA:
            for i in range(lenB-lenA):
                curB = curB.next
        while curB != curA:
            curB = curB.next
            curA = curA.next
        return curA

'''
        

        