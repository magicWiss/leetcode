'''
You are given a sorted unique integer array nums.

Return the smallest sorted list of ranges that cover all the numbers in the array exactly. 
That is, each element of nums is covered by exactly one of the ranges, 
and there is no integer x such that x is in one of the ranges but not in nums.

'''

class Solution:
    def summaryRanges(self, nums):
        if len(nums)==0:
            return []
        out=[]
        i=0
        if len(nums)==1:
            interval=str(nums[i])
            out.append(interval)
            return out

        for j in range(1,len(nums)):

            if nums[j]-1!=nums[j-1]:
                if i!=j-1:
                    interval=str(nums[i])+"->"+str(nums[j-1])
                else:
                    interval=str(nums[i])

                out.append(interval)
                i=j
            if j==len(nums)-1:
                if nums[j]-1==nums[j-1]:
                    interval=str(nums[i])+"->"+str(nums[j])
                    out.append(interval)
                    i=j
                else:
                    interval=str(nums[j])
                    out.append(interval)

                
            
        return out



            



        