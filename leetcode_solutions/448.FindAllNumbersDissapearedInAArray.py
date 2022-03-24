class Solution:
    def findDisappearedNumbers(self, nums):
        
        for i in range(0,len(nums)):
            if nums[i]==len(nums) or nums[i]==-1*len(nums):      #upper bound
                nums[0]=0               #we know that there can't be 0 in the List
            elif nums[i]>0:
                    if nums[nums[i]]>0:
                        nums[nums[i]]*=-1
            elif nums[i]<0:
                if nums[-1*nums[i]]>0:
                    nums[-1*nums[i]]*=-1
            
            
        out=[]
        for i in range(1,len(nums)):
                if nums[i]>0:
                    out.append(i)

        if nums[0]>0:
            out.append(len(nums))
        return out
if __name__=="__main__":
    print(Solution().findDisappearedNumbers([4,3,2,7,8,2,3,1]))