#Given the head of a singly linked list, return true if it is a palindrome.

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def isPalindrome(self, head):
        
        p=head
        #dimensione lista
        dim=0
        while(p):
            dim+=1
            p=p.next
        
        #Verifica di palindromicità
        p=head
        conta=0
        temp_list=[None for i in range(dim)]
        while(p):
            temp_list[dim - (conta +1)]=p.val
            if(temp_list[(dim-1)-(dim-1 -conta )])!=None:
                if(temp_list[(dim-1)-(dim-1 -conta )])!=p.val:
                    return False
            conta+=1
            p=p.next
        return True
        