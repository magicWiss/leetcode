'''
Given an integer array nums and an integer k, return true if there are two distinct indices i and j in the array such that 
nums[i] == nums[j] and abs(i - j) <= k.

'''
class Solution:
    def containsNearbyDuplicate(self, nums, k: int) -> bool:

        mappa={}

        for i in range(0,len(nums)):

            if nums[i] not in mappa:
                mappa[nums[i]]=[]
                mappa[nums[i]].append(i)
            else:
                for j in mappa[nums[i]]:
                    if abs(j-i)<=k:
                        return True
                
                mappa[nums[i]].append(i)
        return False
        