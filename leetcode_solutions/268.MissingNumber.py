'''
Given an array nums containing n distinct numbers in the range [0, n], return the only number in the range that is missing from the array.

 
'''
class Solution:
    def missingNumber(self, nums) -> int:

        listCon=[i for i in range(0,len(nums)+1)]

        return list(set(listCon).difference(set(nums)))[0]
        