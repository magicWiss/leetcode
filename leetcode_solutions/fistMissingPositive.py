#Given an unsorted integer array nums, return the smallest missing positive integer.

#You must implement an algorithm that runs in O(n) time and uses constant extra space

#COMPLEXITY O(n Log(n))-->non accettabile ma corretto

class Solution:
    def firstMissingPositive(self, nums):
        nums.sort()
        current_min=1
        for i in range(len(nums)):
            if current_min==nums[i]:
                current_min+=1
        return current_min