'''
Created on 5 gen 2022
Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.

The overall run time complexity should be O(log (m+n)).
@author: Wissel
'''

class Solution:
    def findMedianSortedArrays(self, nums1, nums2) :
        
        total=nums1+nums2
        output=0
        total.sort()
        
        if(len(total)%2==0):            #pari
            
            output=total[len(total)//2]+total[len(total)//2+1]
            output=output/2
            return output
        
        return total[len(total)//2]
    

        
        