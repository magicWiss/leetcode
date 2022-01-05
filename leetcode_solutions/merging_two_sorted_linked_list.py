'''
Created on 5 gen 2022
ou are given the heads of two sorted linked lists list1 and list2.

Merge the two lists in a one sorted list. The list should be made by splicing together the nodes of the first two lists.

Return the head of the merged linked list.
@author: Wissel
'''
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeTwoLists(self, list1, list2) :
        
        first=list1                             #testa della prima lista
        second=list2                            #testa della seconda lista
        
        risultato=ListNode(0,None)              #dummy head della lista out
            
        iteratore_res=risultato                 #iteratore seconda lista
        
        while first and second:                 #finchè uno dei due non è null
            
            if(first.val<=second.val):
                
                iteratore_res.next=first
                first=first.next
            else:
                iteratore_res.next=second
                second=second.next
            
            iteratore_res=iteratore_res.next
            
        if(first==None):
            iteratore_res.next=second
            return risultato.next

        if(second==None):
            iteratore_res.next=first
            return risultato.next

            
                
        
        
