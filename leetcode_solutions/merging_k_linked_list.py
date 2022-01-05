'''
Created on 5 gen 2022
You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.

Merge all the linked-lists into one sorted linked-list and return it.
@author: Wissel
'''
#Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeKLists(self, lists):
        
        output=ListNode()               #dummy head
        
        map={}                          #memorizza elementi e loro occorrenze
        
        #Creazione della mappa di appoggio
        for i in lists:                 #per ogni linked list
            
            j=i                         #puntatore al primo elemento della linke list
            
            while j:                    #per tutta la linke list
                
                if(j.val in map):
                    map[j.val]+=1
                else:
                    map[j.val]=1
                j=j.next
        #iteratore della nuova linke list
        dummy=output
        lista=list(map.items())
        lista.sort()
                   
        #creazioe della super liked list
        for k in range(len(lista)):
            
            v,o=lista[k]
            
            while o>0:
                
                current=ListNode(v)
                dummy.next=current
                dummy=dummy.next
                o-=1
                
                
        return output.next
                    
        
                
                
        
