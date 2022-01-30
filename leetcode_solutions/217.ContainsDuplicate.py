'''
Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.
'''
class Solution:
    def containsDuplicate(self, nums) -> bool:

        allEl=set()
        for i in nums:
            if i not in allEl:
                allEl.add(i)

            elif i in allEl:
                return True
        return False        