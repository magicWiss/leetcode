'''
Given an array nums of size n, return the majority element.

The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.
'''
class Solution:
    def majorityElement(self, nums) -> int:

        nums.sort()

        majority=len(nums)//2

        found=False

        i=0
        while i <len(nums):

            if i+majority < len(nums):

                if nums[i]==nums[i+majority-1]:
                    return nums[i]
            
            i=i+1
        return 0 


         
        
