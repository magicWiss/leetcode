'''
Given a 1-indexed array of integers numbers that is already sorted in non-decreasing order, find two numbers such that they add up to a 
specific target number. Let these two numbers be numbers[index1] and numbers[index2] where 1 <= index1 < index2 <= numbers.length.

Return the indices of the two numbers, index1 and index2, added by one as an integer array [index1, index2] of length 2.

The tests are generated such that there is exactly one solution. You may not use the same element twice.
'''

class Solution:
    def twoSum(self, numbers, target: int):

        values=dict()
        for i, num in enumerate(numbers):
            if target - num in values:
                return [values[target-num]+1,i+1]

            values[num]=i