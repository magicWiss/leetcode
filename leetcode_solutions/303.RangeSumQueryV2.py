'''
Given an integer array nums, handle multiple queries of the following type:

Calculate the sum of the elements of nums between indices left and right inclusive where left <= right.
Implement the NumArray class:

NumArray(int[] nums) Initializes the object with the integer array nums.
int sumRange(int left, int right) Returns the sum of the elements of nums between indices left and right inclusive 
(i.e. nums[left] + nums[left + 1] + ... + nums[right]).


Duo the fact that the numArray class will be use only for getting the sum, if we use a simple sum operation we will have a
operation of cost o(n) each call.
We could overcome this inefficiency by memorizing the cumsum for each position
es:
numArray ->[val1, val1+val2, val2+val3]
when we get the sum we will simply get numArray[right]-numArray[eft]
'''
class NumArray:

    def __init__(self, nums):
        self.array=[]
        curr=0
        for i in range (0,len(nums)):
            curr+=nums[i]
            self.array.append(curr)
        

    def sumRange(self, left: int, right: int) -> int:
        if left==0:
            return self.array[right]
        return self.array[right]-self.array[left-1]
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)