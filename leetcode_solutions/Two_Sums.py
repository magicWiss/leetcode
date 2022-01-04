'''
Created on 4 gen 2022

@author: Wissel

Problem 1 of leet code: Two Sums
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.
'''

class Solution:
    def twoSum(self, nums, target):
        
        prev_val={}                 #emptyHashmap
        
        for i,n in enumerate(nums):         #i is the index, n is the element
            
            current=target-n
            
            if current in prev_val:
                return [i,prev_val[current]]
            
            prev_val[n]=i

def __main__():
    
    sol=Solution()
    lista=[2,24,6,-1,4]
    target=28
    print(sol.twoSum(lista, target))

if __main__():
    __main__()
    
                
