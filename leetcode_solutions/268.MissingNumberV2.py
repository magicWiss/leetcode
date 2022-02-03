'''
Given an array nums containing n distinct numbers in the range [0, n], return the only number in the range that is missing from the array.

 
'''
class Solution:
    def missingNumber(self, nums) -> int:

        #trasform array
        for i in range(0,len(nums)):

            val=nums[i]     #access the value
            if val<0:       #if the value is already fixed
                val*=-1     #we return to the original
                if val==len(nums)+1:    #if the val is == -len(nums)+1 then the original was 0
                    val=0

            if val <len(nums):      

                if nums[val]>0:                         #we fix the value of the element in pos val
                    nums[val]*=-1
                elif nums[val]==0:
                    nums[val]=-1*(len(nums)+1)
                
            
        
        #get the output
        for i in range (0,len(nums)):

            if nums[i]>=0:
                return i
        
        return len(nums)
        
