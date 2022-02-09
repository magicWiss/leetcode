'''
Given an integer array nums, 
return the third distinct maximum number in this array. If the third maximum does not exist, return the maximum number.
'''
class Solution:
    def thirdMax(self, nums) -> int:
        nums=list(set(nums))

        nums.sort(reverse=True)
        if len(nums)<3:
            return nums[0]
        else:
            return nums[2]