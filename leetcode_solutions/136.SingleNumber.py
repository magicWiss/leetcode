'''
Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.

You must implement a solution with a linear runtime complexity and use only constant extra space.

 

'''

#idea->si fa l'xor tra tutti i valori a coppie

class Solution:
    def singleNumber(self, nums) -> int:

        res=0

        for i in nums:

            res=res ^ i
        return res
        