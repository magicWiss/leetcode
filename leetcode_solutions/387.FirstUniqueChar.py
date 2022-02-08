'''
Given a string s, find the first non-repeating character in it and return its index. If it does not exist, return -1.
'''
import collections


class Solution:
    def firstUniqChar(self, s: str) -> int:
        
        mappa=collections.Counter(s)

        for i,j in enumerate(s):
            if mappa[j]==1:
                return i
        return -1