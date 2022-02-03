'''
Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Note that you must do this in-place without making a copy of the array.

'''
class Solution:
    def findZero(self,i,nums):
        for j in range(i,len(nums)):
            if nums[j]==0:
                return j
        return len(nums)
    def moveZeroes(self, nums) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if len(nums)==1 or len(nums)==0:
            return
        #initialize i
        i=self.findZero(0,nums)         #find first zero

        j=i+1
        while j<len(nums):

            if nums[j]!=0:
                nums[i],nums[j]=nums[j],nums[i]
                i=self.findZero(i,nums)
            j+=1


        